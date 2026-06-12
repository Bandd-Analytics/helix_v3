"""MT5ExecutionGatekeeper - Risk management and low-latency MT5 order execution.

Transforms validated consensus signals into live MT5 trades with dynamic lot
sizing, structural stop-loss placement, partial profit taking, and slippage
protection.
"""

from __future__ import annotations

import math
from typing import Dict, List, Optional

import MetaTrader5 as mt5

from config.pair_profiles import PairProfile, get_pair_profile, resolve_profile
from config.settings import settings
from helix_v3.core.types import (
    ConsensusResult,
    Direction,
    ExecutionOrder,
    QuantSignal,
)
from helix_v3.core.exposure import OpenRisk, exposure_violation
from helix_v3.core.news_calendar import get_news_calendar
from helix_v3.core.volatility import d1_atr_pips_mt5
from helix_v3.execution.risk_state import RiskState, _trading_day
from helix_v3.journal.trade_journal import TradeJournal
from helix_v3.utils.logger import get_logger

logger = get_logger("execution_gatekeeper")


class MT5ExecutionGatekeeper:
    """Bulletproof trade execution with strict risk guardrails.

    Guardrails:
    - Dynamic lot sizing via fractional Kelly: Equity * Risk% / (SL_pips * pip_value)
    - Stop-loss pinned 3 pips behind peak formation high/low
    - Slippage protection and spread widening blocks
    - Partial close at 1:1 RR, remainder to breakeven
    - Max drawdown circuit breaker (8%)
    """

    # MT5 connection watchdog (Tier 3.1) — injected by the orchestrator.
    # Class-level default so test doubles built without __init__ have it.
    watchdog = None

    def __init__(self) -> None:
        self._risk_cfg = settings.risk
        self._active_orders: Dict[int, ExecutionOrder] = {}
        self.journal = TradeJournal()
        self.risk_state = RiskState()
        # Optional: called once per trading day with the trip reason
        # (the orchestrator wires this to the notifier).
        self.kill_switch_callback = None
        self._kill_notified_day: str = ""

    # ------------------------------------------------------------------
    # Account & Symbol Info
    # ------------------------------------------------------------------

    def _get_account_equity(self) -> float:
        info = mt5.account_info()
        if info is None:
            raise ConnectionError("Cannot retrieve MT5 account info")
        return float(info.equity)

    def _resolved_profile(self, symbol: str) -> PairProfile:
        """Pair profile with gates scaled to ATR(20, D1) — Tier 2.3.

        Falls back to the static profile if MT5 can't serve D1 bars.
        """
        return resolve_profile(symbol, d1_atr_pips_mt5(symbol))

    def _get_account_balance(self) -> float:
        info = mt5.account_info()
        if info is None:
            raise ConnectionError("Cannot retrieve MT5 account info")
        return float(info.balance)

    def _get_symbol_info(self, symbol: str) -> mt5.SymbolInfo:
        info = mt5.symbol_info(symbol)
        if info is None:
            raise ValueError(f"Symbol {symbol} not found or not enabled in MT5")
        if not info.visible:
            mt5.symbol_select(symbol, True)
            info = mt5.symbol_info(symbol)
        return info

    def _get_pip_value(self, symbol: str) -> float:
        info = self._get_symbol_info(symbol)
        digits = info.digits
        point = info.point
        # For 5-digit brokers (e.g., EURUSD 1.12345), 1 pip = 10 points
        pip_size = point * 10 if digits in (3, 5) else point
        return pip_size

    def _get_pip_cost(self, symbol: str, lot_size: float) -> float:
        info = self._get_symbol_info(symbol)
        pip_size = self._get_pip_value(symbol)
        # trade_tick_value is the value of 1 point move for 1 lot
        tick_value = info.trade_tick_value
        tick_size = info.trade_tick_size
        if tick_size == 0:
            return 0.0
        return (pip_size / tick_size) * tick_value * lot_size

    # ------------------------------------------------------------------
    # Order-Send Portability (Tier 3.3)
    # ------------------------------------------------------------------

    DEVIATION_PIPS = 1.0  # slippage budget floor; actual budget >= pair spread

    def _filling_mode(self, symbol: str) -> int:
        """Filling mode the symbol actually supports (IOC was hardcoded).

        symbol_info.filling_mode is a bitmask (1 = FOK, 2 = IOC). Prefer
        IOC — partial fills reconcile fine in execute_order — then FOK,
        else RETURN.
        """
        try:
            flags = int(getattr(self._get_symbol_info(symbol), "filling_mode", 0))
        except Exception:
            return mt5.ORDER_FILLING_IOC
        if flags & 2:
            return mt5.ORDER_FILLING_IOC
        if flags & 1:
            return mt5.ORDER_FILLING_FOK
        return mt5.ORDER_FILLING_RETURN

    def _deviation_points(self, symbol: str) -> int:
        """Slippage allowance in POINTS from a pip-denominated budget.

        The hardcoded 10 points meant 1 pip on EURUSD but 10 pips on
        XAUUSD. The budget is now pips — max(DEVIATION_PIPS, the pair's
        spread limit) — converted per symbol.
        """
        try:
            info = self._get_symbol_info(symbol)
            pip = self._get_pip_value(symbol)
            budget_pips = max(
                self.DEVIATION_PIPS, get_pair_profile(symbol).max_spread_pips
            )
            return max(1, int(round(budget_pips * pip / info.point)))
        except Exception:
            return 10

    def _min_stop_distance(self, symbol: str) -> float:
        """Broker minimum stop distance as a PRICE delta (trade_stops_level)."""
        try:
            info = self._get_symbol_info(symbol)
            return max(0, int(getattr(info, "trade_stops_level", 0))) * float(info.point)
        except Exception:
            return 0.0

    # ------------------------------------------------------------------
    # Drawdown Circuit Breaker
    # ------------------------------------------------------------------

    def check_drawdown_limit(self) -> bool:
        """Kill switch: realized + floating losses vs persisted HWM and daily anchor.

        The old (balance - equity) / balance formula reset to ~0 the moment a
        loss was realized, so the account could bleed indefinitely. RiskState
        measures total drawdown from the balance high-water mark and daily
        loss from the day's anchor balance, both persisted to SQLite.
        """
        equity = self._get_account_equity()
        balance = self._get_account_balance()

        ok, reason = self.risk_state.check(balance=balance, equity=equity)
        if not ok:
            logger.critical("KILL SWITCH: %s — blocking all new trades.", reason)
            self._notify_kill(reason)
            return False
        return True

    def _notify_kill(self, reason: str) -> None:
        """Send the kill-switch alert at most once per trading day."""
        day = _trading_day()
        if self._kill_notified_day == day:
            return
        self._kill_notified_day = day
        if self.kill_switch_callback:
            try:
                self.kill_switch_callback(
                    f"HELIX V3 KILL SWITCH\n{'='*25}\n{reason}\nAll new entries blocked."
                )
            except Exception as e:
                logger.error("Kill-switch notification failed: %s", e)

    # ------------------------------------------------------------------
    # Position Count Check
    # ------------------------------------------------------------------

    def check_position_limit(self) -> bool:
        positions = mt5.positions_total()
        if positions is None:
            return False
        if positions >= self._risk_cfg.max_concurrent_positions:
            logger.warning(
                "Position limit reached: %d/%d",
                positions, self._risk_cfg.max_concurrent_positions,
            )
            return False
        return True

    # ------------------------------------------------------------------
    # Dynamic Lot Sizing
    # ------------------------------------------------------------------

    def calculate_lot_size(
        self, symbol: str, sl_pips: float
    ) -> Optional[float]:
        """Lot = (Equity * PairRisk%) / (SL_pips * PipValue_per_lot)

        Safety layers:
        1. SL floor — never size off fewer pips than pair minimum
        2. Account-proportional max lot — caps based on equity, not static
        3. Post-calc risk verification — returns None (order ABORTED) if even
           the broker minimum lot exceeds the hard risk cap

        Returns the lot size, or None if no lot satisfies the risk cap.
        """
        profile = self._resolved_profile(symbol)
        equity = self._get_account_equity()
        risk_pct = profile.max_risk_pct
        risk_amount = equity * risk_pct

        # --- Safety 1: SL floor prevents lot inflation from tight stops ---
        effective_sl = sl_pips
        if sl_pips < profile.min_sl_pips:
            logger.warning(
                "SL floor applied %s: %.1f pips < min %.1f — using floor for lot calc",
                symbol, sl_pips, profile.min_sl_pips,
            )
            effective_sl = profile.min_sl_pips

        info = self._get_symbol_info(symbol)
        pip_size = self._get_pip_value(symbol)
        tick_value = info.trade_tick_value
        tick_size = info.trade_tick_size

        if tick_size == 0 or effective_sl == 0:
            logger.error("Invalid tick_size or sl_pips for lot calculation — rejecting")
            return None

        pip_value_per_lot = (pip_size / tick_size) * tick_value
        raw_lot = risk_amount / (effective_sl * pip_value_per_lot)

        # --- Safety 2: Account-proportional max lot ---
        # Never allow a lot size where a 2x SL move would exceed 3% of equity
        max_loss_pct = 0.03  # Hard cap: 3% of equity absolute max
        if pip_value_per_lot > 0:
            account_max_lot = (equity * max_loss_pct) / (effective_sl * pip_value_per_lot)
        else:
            account_max_lot = info.volume_min

        # Clamp to broker limits, pair max lot, account max lot
        vol_min = info.volume_min
        vol_max = min(info.volume_max, profile.max_lot_size, account_max_lot)
        vol_step = info.volume_step

        lot = max(vol_min, min(raw_lot, vol_max))
        # FLOOR to the volume step — rounding could round UP past the cap.
        if vol_step > 0:
            lot = math.floor((lot / vol_step) + 1e-9) * vol_step
        lot = round(lot, 2)
        if lot < vol_min:
            lot = vol_min

        # --- Safety 3: Post-calc risk verification (rejects, never clamps-and-sends) ---
        actual_risk = lot * effective_sl * pip_value_per_lot
        actual_risk_pct = actual_risk / equity if equity > 0 else 1.0
        if actual_risk_pct > max_loss_pct:
            min_risk = vol_min * effective_sl * pip_value_per_lot
            min_risk_pct = min_risk / equity if equity > 0 else 1.0
            if min_risk_pct > max_loss_pct:
                logger.error(
                    "RISK REJECT %s: even broker min lot %.2f risks %.1f%% > %.1f%% cap — "
                    "order aborted (equity=$%.2f, sl=%.1f pips)",
                    symbol, vol_min, min_risk_pct * 100, max_loss_pct * 100,
                    equity, effective_sl,
                )
                return None
            lot = vol_min
            actual_risk = min_risk
            actual_risk_pct = min_risk_pct
            logger.warning(
                "Risk verification clamped %s to min lot %.2f (risk %.1f%%)",
                symbol, lot, actual_risk_pct * 100,
            )

        logger.info(
            "Lot sizing %s [%s]: equity=$%.2f risk=%.1f%% ($%.2f) "
            "sl=%.1f pips (effective=%.1f) -> %.2f lots ($%.2f at risk, %.1f%%)",
            symbol, profile.risk_tier, equity, risk_pct * 100, risk_amount,
            sl_pips, effective_sl, lot, actual_risk, actual_risk_pct * 100,
        )
        return lot

    # ------------------------------------------------------------------
    # Spread / Slippage Checks
    # ------------------------------------------------------------------

    def _check_spread(self, symbol: str) -> bool:
        profile = get_pair_profile(symbol)
        tick = mt5.symbol_info_tick(symbol)
        if tick is None:
            return False

        pip_size = self._get_pip_value(symbol)
        spread = (tick.ask - tick.bid) / pip_size

        if spread > profile.max_spread_pips:
            logger.warning(
                "Spread too wide for %s: %.1f pips > %.1f limit (%s tier)",
                symbol, spread, profile.max_spread_pips, profile.risk_tier,
            )
            return False
        return True

    def _position_risk_pct(self, pos, equity: float) -> float:
        """Loss fraction if this open position's CURRENT stop is hit.

        A stop at/past breakeven risks nothing; no stop at all is scored
        at the pair's full intended risk (conservative).
        """
        try:
            if pos.sl == 0:
                return get_pair_profile(pos.symbol).max_risk_pct
            if pos.type == mt5.POSITION_TYPE_BUY and pos.sl >= pos.price_open:
                return 0.0
            if pos.type == mt5.POSITION_TYPE_SELL and pos.sl <= pos.price_open:
                return 0.0
            pip_size = self._get_pip_value(pos.symbol)
            dist_pips = abs(pos.price_open - pos.sl) / pip_size
            loss = dist_pips * self._get_pip_cost(pos.symbol, pos.volume)
            return loss / equity if equity > 0 else 0.0
        except Exception as e:
            logger.error("Position risk calc failed for %s: %s", pos.symbol, e)
            return get_pair_profile(pos.symbol).max_risk_pct

    def _check_currency_exposure(self, symbol: str, direction: Direction) -> bool:
        """Per-currency NET exposure cap across open positions (Tier 2.6).

        3 GBP longs at 0.8% = one GBP news candle = 2.4% correlated loss.
        Cap = MAX_CCY_EXPOSURE_MULT x max_risk_per_trade (default 2x1% = 2%).
        """
        if direction not in (Direction.BUY, Direction.SELL):
            return True
        try:
            equity = self._get_account_equity()
            opens = []
            for pos in (mt5.positions_get() or []):
                pos_dir = (
                    Direction.BUY if pos.type == mt5.POSITION_TYPE_BUY else Direction.SELL
                )
                opens.append(OpenRisk(pos.symbol, pos_dir, self._position_risk_pct(pos, equity)))
        except Exception as e:
            logger.error("Exposure check failed for %s: %s — allowing entry", symbol, e)
            return True

        cap_pct = (
            settings.risk.max_currency_exposure_mult * settings.risk.max_risk_per_trade
        )
        new_risk = get_pair_profile(symbol).max_risk_pct
        reason = exposure_violation(symbol, direction, new_risk, opens, cap_pct)
        if reason is not None:
            logger.warning("CURRENCY EXPOSURE BLOCK: %s — %s", symbol, reason)
            return False
        return True

    def _check_news_blackout(self, symbol: str) -> bool:
        """No entries within the high-impact news window (Tier 2.5).

        Fail-open on calendar errors — the calendar logs loudly when the
        feed is down; a broken feed must not silently halt all trading.
        """
        try:
            event = get_news_calendar().blackout(symbol)
        except Exception as e:
            logger.error("News blackout check failed for %s: %s", symbol, e)
            return True
        if event is not None:
            logger.warning(
                "NEWS BLACKOUT: %s entry blocked — %s %s at %s (±%d min window)",
                symbol, event.currency, event.title,
                event.time_utc.strftime("%H:%M UTC"),
                get_news_calendar().blackout_minutes,
            )
            return False
        return True

    # ------------------------------------------------------------------
    # Order Construction & Execution
    # ------------------------------------------------------------------

    def build_order(
        self,
        symbol: str,
        signal: QuantSignal,
        consensus: ConsensusResult,
    ) -> Optional[ExecutionOrder]:
        if not self.check_drawdown_limit():
            return None
        if not self.check_position_limit():
            return None
        if not self._check_spread(symbol):
            return None
        if not self._check_news_blackout(symbol):
            return None
        if not self._check_currency_exposure(symbol, consensus.direction):
            return None

        direction = consensus.direction
        pip_size = self._get_pip_value(symbol)

        tick = mt5.symbol_info_tick(symbol)
        if tick is None:
            logger.error("Cannot get tick for %s", symbol)
            return None

        # Determine entry price
        if direction == Direction.BUY:
            entry = tick.ask
        elif direction == Direction.SELL:
            entry = tick.bid
        else:
            return None

        # SL placement: behind structural level with sensible cap
        # Cap at expected_level_move_pips — if SL needs to be wider than one
        # full level move, the entry is too far from the formation.
        profile = self._resolved_profile(symbol)
        buffer = profile.sl_buffer_pips * pip_size
        max_sl_dist = profile.expected_level_move_pips * pip_size

        if signal.session_bounds is not None:
            if direction == Direction.BUY:
                structural_sl = signal.session_bounds.low - buffer
                sl_dist = entry - structural_sl
                sl = entry - min(sl_dist, max_sl_dist) if sl_dist > 0 else structural_sl
            else:
                structural_sl = signal.session_bounds.high + buffer
                sl_dist = structural_sl - entry
                sl = entry + min(sl_dist, max_sl_dist) if sl_dist > 0 else structural_sl
        else:
            # Fallback: use stop hunt breach or fixed 30 pips
            fallback_pips = 30.0
            if direction == Direction.BUY:
                sl = entry - (fallback_pips * pip_size)
            else:
                sl = entry + (fallback_pips * pip_size)

        sl_pips = abs(entry - sl) / pip_size

        # --- SL FLOOR: widen actual SL if too tight (prevents suicide stops) ---
        if sl_pips < profile.min_sl_pips:
            logger.warning(
                "SL FLOOR ENFORCED %s: structural SL %.1f pips < min %.1f — widening SL",
                symbol, sl_pips, profile.min_sl_pips,
            )
            sl_pips = profile.min_sl_pips
            if direction == Direction.BUY:
                sl = entry - (sl_pips * pip_size)
            else:
                sl = entry + (sl_pips * pip_size)

        lot_size = self.calculate_lot_size(symbol, sl_pips)
        if lot_size is None:
            logger.error("Order aborted for %s: lot sizing rejected by risk cap", symbol)
            return None

        # TP levels — calibrated from 90-day validation data
        # T1: 1:1 RR (locks in profit, SL to breakeven)
        # T2: min(expected_level_move, 2.5x SL) — targets realistic move, not blind multiple
        risk_distance = abs(entry - sl)
        level_move_dist = profile.expected_level_move_pips * pip_size
        tp2_dist = min(level_move_dist, risk_distance * 2.5)
        tp2_dist = max(tp2_dist, risk_distance * 1.5)  # Never less than 1.5:1 RR

        if direction == Direction.BUY:
            tp1 = entry + risk_distance  # 1:1 RR
            tp2 = entry + tp2_dist
        else:
            tp1 = entry - risk_distance
            tp2 = entry - tp2_dist

        rr = abs(entry - tp2) / abs(entry - sl) if abs(entry - sl) > 0 else 0

        order = ExecutionOrder(
            symbol=symbol,
            direction=direction,
            lot_size=lot_size,
            entry_price=entry,
            stop_loss=round(sl, 5),
            take_profit_1=round(tp1, 5),
            take_profit_2=round(tp2, 5),
            sl_pips=sl_pips,
            risk_reward=rr,
        )

        logger.info(
            "Order built: %s %s %.2f lots @ %.5f SL=%.5f TP1=%.5f TP2=%.5f RR=%.1f",
            direction.value, symbol, lot_size, entry, sl, tp1, tp2, rr,
        )
        return order

    def execute_order(
        self,
        order: ExecutionOrder,
        signal: Optional[QuantSignal] = None,
        consensus: Optional[ConsensusResult] = None,
        consensus_mode: str = "local",
        chart_path: Optional[str] = None,
        max_retries: int = 3,
    ) -> Optional[int]:
        """Send order to MT5 with retry logic for off-quotes.

        If signal and consensus are provided, the trade is auto-recorded
        in the journal on fill.

        Returns ticket number on success, None on failure.
        """
        order_type = (
            mt5.ORDER_TYPE_BUY
            if order.direction == Direction.BUY
            else mt5.ORDER_TYPE_SELL
        )
        pos_type = 0 if order.direction == Direction.BUY else 1

        info = self._get_symbol_info(order.symbol)
        vol_min = info.volume_min

        # Snapshot Helix tickets on this symbol BEFORE the first send. Any new
        # magic-314159 position in our direction afterwards is a fill from THIS
        # order — an order_send that returns None or DONE_PARTIAL may still
        # have reached the server, and blindly resending full volume was the
        # double-fill bug.
        pre_existing = {
            p.ticket
            for p in (mt5.positions_get(symbol=order.symbol) or [])
            if p.magic == 314159
        }

        def _new_fills() -> list:
            positions = mt5.positions_get(symbol=order.symbol) or []
            return [
                p for p in positions
                if p.magic == 314159 and p.type == pos_type and p.ticket not in pre_existing
            ]

        def _finalize(ticket: int) -> int:
            order.ticket = ticket
            order.status = "FILLED"
            self._active_orders[ticket] = order
            logger.info(
                "ORDER FILLED: ticket=%d %s %s %.2f",
                ticket, order.direction.value, order.symbol, order.lot_size,
            )

            # Auto-journal the trade
            if signal and consensus:
                try:
                    equity = self._get_account_equity()
                    pip_val = self._get_pip_cost(order.symbol, order.lot_size)
                    spread = None
                    tick_now = mt5.symbol_info_tick(order.symbol)
                    if tick_now:
                        spread = (tick_now.ask - tick_now.bid) / self._get_pip_value(order.symbol)
                    self.journal.record_entry(
                        order=order,
                        signal=signal,
                        consensus=consensus,
                        consensus_mode=consensus_mode,
                        equity_before=equity,
                        spread_at_entry=spread,
                        pip_value=pip_val,
                        chart_path=chart_path,
                    )
                except Exception as e:
                    logger.error("Journal entry failed: %s", e)

            return ticket

        # Tier 3.3: respect the broker's minimum stop distance — widen an
        # SL/TP that sits inside trade_stops_level instead of burning an
        # order_check reject (order_check remains the final authority).
        min_dist = self._min_stop_distance(order.symbol)
        if min_dist > 0:
            digits = int(info.digits)
            if order.direction == Direction.BUY:
                sl_limit = order.entry_price - min_dist
                tp_limit = order.entry_price + min_dist
                if order.stop_loss > sl_limit:
                    logger.warning(
                        "STOPS LEVEL: widening %s SL %.5f -> %.5f (min distance)",
                        order.symbol, order.stop_loss, sl_limit,
                    )
                    order.stop_loss = round(sl_limit, digits)
                if order.take_profit_2 < tp_limit:
                    order.take_profit_2 = round(tp_limit, digits)
            else:
                sl_limit = order.entry_price + min_dist
                tp_limit = order.entry_price - min_dist
                if order.stop_loss < sl_limit:
                    logger.warning(
                        "STOPS LEVEL: widening %s SL %.5f -> %.5f (min distance)",
                        order.symbol, order.stop_loss, sl_limit,
                    )
                    order.stop_loss = round(sl_limit, digits)
                if order.take_profit_2 > tp_limit:
                    order.take_profit_2 = round(tp_limit, digits)

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": order.symbol,
            "volume": order.lot_size,
            "type": order_type,
            "price": order.entry_price,
            "sl": order.stop_loss,
            "tp": order.take_profit_2,  # Initial TP at T2 level
            "deviation": self._deviation_points(order.symbol),  # pips -> points (Tier 3.3)
            "magic": 314159,
            "comment": "HelixV3_MMM",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": self._filling_mode(order.symbol),  # broker-supported (Tier 3.3)
        }

        # Margin / validity pre-check — catches NO_MONEY and invalid stops
        # before burning retries against the server.
        check = mt5.order_check(request)
        if check is None:
            logger.error("order_check returned None for %s — aborting order", order.symbol)
            order.status = "REJECTED"
            return None
        if check.retcode != 0:
            logger.error(
                "order_check rejected %s: retcode=%d comment=%s — aborting order",
                order.symbol, check.retcode, getattr(check, "comment", ""),
            )
            order.status = "REJECTED"
            return None

        remaining = order.lot_size

        for attempt in range(1, max_retries + 1):
            request["volume"] = round(remaining, 2)

            # Refresh price before each attempt
            tick = mt5.symbol_info_tick(order.symbol)
            if tick is not None:
                request["price"] = (
                    tick.ask if order.direction == Direction.BUY else tick.bid
                )

            result = mt5.order_send(request)

            if result is None:
                # The order may have reached the server despite the None —
                # reconcile against live positions before any resend.
                logger.error(
                    "order_send returned None on attempt %d — checking server for fills",
                    attempt,
                )
                fills = _new_fills()
                filled = round(sum(p.volume for p in fills), 2)
                outstanding = round(order.lot_size - filled, 2)
                if filled > 0 and outstanding < vol_min:
                    logger.warning(
                        "Order filled despite None result (%.2f lots) — adopting ticket %d",
                        filled, fills[0].ticket,
                    )
                    return _finalize(fills[0].ticket)
                if filled > 0:
                    remaining = outstanding
                    logger.warning(
                        "Partial fill after None result: %.2f filled, %.2f outstanding",
                        filled, remaining,
                    )
                continue

            if result.retcode == mt5.TRADE_RETCODE_DONE:
                return _finalize(result.order)

            if result.retcode == mt5.TRADE_RETCODE_DONE_PARTIAL:
                # A live position EXISTS — resending full volume would stack
                # exposure. Resend only the unfilled remainder, if any.
                fills = _new_fills()
                filled = round(sum(p.volume for p in fills), 2)
                if filled <= 0:
                    filled = round(getattr(result, "volume", 0.0), 2)
                outstanding = round(order.lot_size - filled, 2)
                if outstanding < vol_min:
                    return _finalize(result.order or (fills[0].ticket if fills else 0))
                remaining = outstanding
                logger.warning(
                    "DONE_PARTIAL on attempt %d: %.2f filled, resending only %.2f remainder",
                    attempt, filled, remaining,
                )
                continue

            if result.retcode == mt5.TRADE_RETCODE_PLACED:
                # Accepted by the server, pending execution — NOT a failure.
                # Never resend; if it fills after we return, orphan adoption
                # picks it up on the next manage cycle.
                fills = _new_fills()
                filled = round(sum(p.volume for p in fills), 2)
                if filled > 0 and round(order.lot_size - filled, 2) < vol_min:
                    return _finalize(fills[0].ticket)
                order.status = "PENDING"
                logger.warning(
                    "Order PLACED (pending execution) for %s — not resending; "
                    "orphan adoption will register the fill if it executes",
                    order.symbol,
                )
                return None

            logger.warning(
                "Order attempt %d/%d failed: retcode=%d comment=%s",
                attempt, max_retries, result.retcode, result.comment,
            )

            # Don't retry on terminal errors
            if result.retcode in (
                mt5.TRADE_RETCODE_INVALID,
                mt5.TRADE_RETCODE_INVALID_VOLUME,
                mt5.TRADE_RETCODE_INVALID_PRICE,
                mt5.TRADE_RETCODE_INVALID_STOPS,
                mt5.TRADE_RETCODE_NO_MONEY,
                mt5.TRADE_RETCODE_MARKET_CLOSED,
            ):
                logger.error("Terminal error, not retrying: %d", result.retcode)
                break

        order.status = "REJECTED"
        return None

    # ------------------------------------------------------------------
    # Trade Management (T1, Trailing SL, Time Exit, Session Exit)
    # ------------------------------------------------------------------

    def manage_open_positions(self) -> List[str]:
        """Comprehensive trade management for all open Helix positions.

        Checks (in order):
        1. Max duration exit — close if trade exceeds time limit
        2. Stale trade exit — close if trade hasn't moved after threshold
        3. Session-based exit — close before specified session
        4. T1 partial close — 50% at 1:1 RR, SL to breakeven
        5. Trailing stop — lock in profit after activation threshold

        Returns list of action descriptions for notification.
        """
        positions = mt5.positions_get()
        if positions is None:
            # Tier 3.1: a dead terminal must never look like a quiet market.
            # With open trades on the book, this cycle had NO trailing, NO
            # stale exits, NO T1 — say so loudly and feed the watchdog.
            logger.error(
                "positions_get() returned None — MT5 connection suspect; "
                "position management BLIND this cycle (last_error=%s)",
                mt5.last_error(),
            )
            if self.watchdog is not None:
                self.watchdog.record_failure("positions_get None in manage_open_positions")
            return []
        if self.watchdog is not None:
            self.watchdog.record_success()

        actions: List[str] = []
        # Robust server time: try MT5 tick time, fall back to wall clock
        now_ts = mt5.symbol_info_tick(settings.trading.symbols[0])
        server_time = now_ts.time if now_ts else 0
        if server_time == 0:
            # Fallback to wall clock expressed as a SERVER-stamped epoch —
            # position.time is server-stamped, so raw utcnow() would be 2-3h off
            from helix_v3.core.market_time import utc_now_server_epoch
            server_time = utc_now_server_epoch()
            logger.warning("Using wall clock for position management (MT5 tick time unavailable)")

        for pos in positions:
            if pos.magic != 314159:
                continue

            ticket = pos.ticket
            order = self._active_orders.get(ticket)
            if order is None:
                # Adopt orphaned Helix positions (from restart)
                direction = Direction.BUY if pos.type == 0 else Direction.SELL
                order = ExecutionOrder(
                    symbol=pos.symbol, direction=direction,
                    lot_size=pos.volume, entry_price=pos.price_open,
                    stop_loss=pos.sl, take_profit_1=0, take_profit_2=pos.tp,
                    sl_pips=0, risk_reward=0, ticket=ticket, status="FILLED",
                )
                pip_size = self._get_pip_value(pos.symbol)
                sl_dist = abs(pos.price_open - pos.sl)
                # SL at/past breakeven (in the profit direction) means T1
                # already fired or the trade is trailing. Reconstructing
                # take_profit_1 = entry here re-fired a 50% partial close on
                # EVERY restart.
                breakeven_tol = pip_size  # within 1 pip of entry = breakeven
                sl_at_or_past_entry = pos.sl != 0 and (
                    (direction == Direction.BUY and pos.sl >= pos.price_open - breakeven_tol)
                    or (direction == Direction.SELL and pos.sl <= pos.price_open + breakeven_tol)
                )
                if sl_at_or_past_entry:
                    order.status = "T1_HIT"
                    order.take_profit_1 = pos.price_open
                    order.sl_pips = 0.0
                    logger.info(
                        "Adopted post-T1 position: %s ticket=%d (SL at/past breakeven, resuming trail)",
                        pos.symbol, ticket,
                    )
                else:
                    # Pre-T1: reconstruct T1 at 1:1 RR from the SL distance
                    if direction == Direction.BUY:
                        order.take_profit_1 = pos.price_open + sl_dist
                    else:
                        order.take_profit_1 = pos.price_open - sl_dist
                    order.sl_pips = sl_dist / pip_size
                    logger.info("Adopted orphaned position: %s ticket=%d", pos.symbol, ticket)
                self._active_orders[ticket] = order

            pip_size = self._get_pip_value(pos.symbol)
            pp = self._resolved_profile(pos.symbol)
            entry = pos.price_open
            current = pos.price_current
            duration_min = (server_time - pos.time) / 60 if server_time > pos.time else 0

            if order.direction == Direction.BUY:
                profit_pips = (current - entry) / pip_size
                hit_t1 = current >= order.take_profit_1
            else:
                profit_pips = (entry - current) / pip_size
                hit_t1 = current <= order.take_profit_1

            # --- 0. News blackout management (Tier 2.5) ---
            # Inside the high-impact window: a red position is the hunted —
            # flatten it. A green position locks gains at breakeven.
            news_ev = None
            try:
                news_ev = get_news_calendar().blackout(pos.symbol)
            except Exception as e:
                logger.error("News blackout check failed for %s: %s", pos.symbol, e)
            if news_ev is not None:
                if profit_pips <= 0:
                    logger.warning(
                        "NEWS EXIT: %s ticket=%d %+.1f pips — %s %s at %s, closing red position",
                        pos.symbol, ticket, profit_pips, news_ev.currency,
                        news_ev.title, news_ev.time_utc.strftime("%H:%M UTC"),
                    )
                    self._partial_close(pos, pos.volume)
                    actions.append(
                        f"NEWS EXIT: {pos.symbol} {order.direction.value} ticket={ticket} "
                        f"{profit_pips:+.1f} pips before {news_ev.currency} {news_ev.title}"
                    )
                    continue
                # In profit: lock at breakeven through the event (only tighten)
                if order.direction == Direction.BUY and pos.sl < entry:
                    self._modify_sl(ticket, pos.symbol, entry)
                    actions.append(
                        f"NEWS BE: {pos.symbol} ticket={ticket} SL->breakeven before "
                        f"{news_ev.currency} {news_ev.title}"
                    )
                elif order.direction == Direction.SELL and (pos.sl > entry or pos.sl == 0):
                    self._modify_sl(ticket, pos.symbol, entry)
                    actions.append(
                        f"NEWS BE: {pos.symbol} ticket={ticket} SL->breakeven before "
                        f"{news_ev.currency} {news_ev.title}"
                    )

            # --- 1. Max Duration Exit (pair-gated) ---
            max_dur = pp.max_duration_minutes
            if duration_min >= max_dur:
                logger.warning(
                    "MAX DURATION EXIT: %s ticket=%d after %.0f min (limit=%d) pips=%+.1f",
                    pos.symbol, ticket, duration_min, max_dur, profit_pips,
                )
                self._partial_close(pos, pos.volume)
                actions.append(
                    f"TIME EXIT: {pos.symbol} {order.direction.value} ticket={ticket} after {duration_min:.0f}min pips={profit_pips:+.1f}"
                )
                continue

            # --- 2. Tiered Stale Trade Management (calibrated from 90-day validation) ---
            # Phase 1 (stale_minutes, 90 min): Tighten SL to half original distance.
            #   Risk is halved — if the setup was right, reduced SL gives it room.
            #   If the setup was wrong, the tighter SL cuts loss sooner.
            # Phase 2 (stale_exit_minutes): Full exit — no more waiting.
            # For low-vol pairs (stale_exit == stale_minutes), phases collapse to immediate exit.
            stale_phase1 = pp.stale_minutes       # 90 min — universal tighten point
            stale_phase2 = pp.stale_exit_minutes   # 90-150 min — pair-specific exit

            if duration_min >= stale_phase2 and profit_pips <= 0 and order.status in ("FILLED", "STALE_TIGHTENED"):
                # Phase 2: Full exit — extended window exhausted
                logger.warning(
                    "STALE EXIT (Phase 2): %s ticket=%d | %+.1f pips after %.0f min (limit=%d) — closing",
                    pos.symbol, ticket, profit_pips, duration_min, stale_phase2,
                )
                self._partial_close(pos, pos.volume)
                actions.append(
                    f"STALE EXIT: {pos.symbol} {order.direction.value} ticket={ticket} {profit_pips:+.1f} pips after {duration_min:.0f}min"
                )
                continue

            if (duration_min >= stale_phase1 and profit_pips <= 0
                    and order.status == "FILLED" and stale_phase2 > stale_phase1):
                # Phase 1: Tighten SL to half original distance (reduce risk exposure)
                # Only applies to pairs with extended window (GBPAUD, GBPJPY, GBPNZD)
                if order.sl_pips > 0:
                    half_sl_dist = (order.sl_pips / 2.0) * pip_size
                    if order.direction == Direction.BUY:
                        new_sl = entry - half_sl_dist
                        if new_sl > pos.sl:  # Only tighten, never widen
                            self._modify_sl(ticket, pos.symbol, new_sl)
                    else:
                        new_sl = entry + half_sl_dist
                        if new_sl < pos.sl:
                            self._modify_sl(ticket, pos.symbol, new_sl)

                    order.status = "STALE_TIGHTENED"
                    logger.warning(
                        "STALE TIGHTEN (Phase 1): %s ticket=%d | %+.1f pips after %.0f min — "
                        "SL tightened to 50%% (%.1f pips), exit at %d min",
                        pos.symbol, ticket, profit_pips, duration_min,
                        order.sl_pips / 2.0, stale_phase2,
                    )
                    actions.append(
                        f"STALE TIGHTEN: {pos.symbol} ticket={ticket} SL halved at {duration_min:.0f}min, "
                        f"exit at {stale_phase2}min if still flat"
                    )

            elif duration_min >= stale_phase1 and profit_pips <= 0 and order.status == "FILLED":
                # No extension — immediate exit (low-vol pairs where stale_exit == stale_minutes)
                logger.warning(
                    "STALE EXIT: %s ticket=%d | %+.1f pips after %.0f min (not in profit) — closing",
                    pos.symbol, ticket, profit_pips, duration_min,
                )
                self._partial_close(pos, pos.volume)
                actions.append(
                    f"STALE EXIT: {pos.symbol} {order.direction.value} ticket={ticket} {profit_pips:+.1f} pips after {duration_min:.0f}min"
                )
                continue
            # NOTE: If profit_pips > 0 after stale threshold, trade STAYS OPEN and trails via rule 5

            # --- 3. Session-Based Exit (pair-gated) ---
            from helix_v3.scanner.market_scanner import _get_session_name
            current_session = _get_session_name()
            close_session = pp.close_before_session
            if current_session == close_session and order.status in ("FILLED", "T1_HIT", "STALE_TIGHTENED"):
                if profit_pips < self._risk_cfg.stale_trade_max_pips:
                    logger.warning(
                        "SESSION EXIT: %s ticket=%d closing before %s | pips=%+.1f",
                        pos.symbol, ticket, close_session, profit_pips,
                    )
                    self._partial_close(pos, pos.volume)
                    actions.append(
                        f"SESSION EXIT: {pos.symbol} {order.direction.value} ticket={ticket} before {close_session} pips={profit_pips:+.1f}"
                    )
                    continue

            # --- 4. T1 Partial Close at 1:1 RR ---
            just_hit_t1 = False
            if hit_t1 and order.status in ("FILLED", "STALE_TIGHTENED"):
                close_volume = round(
                    pos.volume * self._risk_cfg.partial_close_ratio, 2
                )
                if close_volume >= 0.01:
                    self._partial_close(pos, close_volume)
                    order.status = "T1_HIT"
                    just_hit_t1 = True

                    # Move SL to breakeven — retry once immediately; the
                    # persistent enforcement below (4.5) catches the rest.
                    if not self._modify_sl(pos.ticket, pos.symbol, entry):
                        self._modify_sl(pos.ticket, pos.symbol, entry)
                    logger.info(
                        "T1 HIT: %s ticket=%d closed %.2f lots, SL -> breakeven",
                        pos.symbol, ticket, close_volume,
                    )
                    actions.append(
                        f"T1 HIT: {pos.symbol} ticket={ticket} +{profit_pips:.1f} pips, closed {close_volume} lots"
                    )

                    # Journal the T1 hit
                    try:
                        t1_profit = profit_pips * self._get_pip_cost(pos.symbol, close_volume)
                        self.journal.record_t1_hit(
                            ticket=ticket,
                            close_price=current,
                            close_lots=close_volume,
                            pips=profit_pips,
                            profit=t1_profit,
                        )
                    except Exception as e:
                        logger.error("Journal T1 record failed: %s", e)

            # --- 4.5 Breakeven enforcement (Tier 3.3) ---
            # A post-T1 position without a breakeven stop is naked risk on a
            # remainder that already paid out once. Retry every cycle; if it
            # keeps failing, alert ONCE (and announce when it's restored).
            if order.status == "T1_HIT" and not just_hit_t1:
                be_missing = (
                    (order.direction == Direction.BUY and pos.sl < entry)
                    or (order.direction == Direction.SELL
                        and (pos.sl > entry or pos.sl == 0))
                )
                if be_missing:
                    alerted = getattr(self, "_be_alert_tickets", None)
                    if alerted is None:
                        alerted = self._be_alert_tickets = set()
                    if self._modify_sl(ticket, pos.symbol, entry):
                        if ticket in alerted:
                            alerted.discard(ticket)
                            actions.append(
                                f"BE RESTORED: {pos.symbol} ticket={ticket} "
                                f"post-T1 stop back at breakeven"
                            )
                    elif ticket not in alerted:
                        alerted.add(ticket)
                        logger.critical(
                            "POST-T1 POSITION WITHOUT BREAKEVEN: %s ticket=%d "
                            "sl=%.5f entry=%.5f — modify failing, retrying every cycle",
                            pos.symbol, ticket, pos.sl, entry,
                        )
                        actions.append(
                            f"BE FAILED: {pos.symbol} ticket={ticket} post-T1 stop "
                            f"NOT at breakeven (sl={pos.sl:.5f}) — retrying, check manually"
                        )

            # --- 5. Trailing Stop Loss (pair-gated) ---
            if settings.risk.trailing_stop_enabled and order.status == "T1_HIT":
                activation = pp.trail_activation_pips
                trail_dist = pp.trail_distance_pips

                if profit_pips >= activation:
                    if order.direction == Direction.BUY:
                        new_sl = current - (trail_dist * pip_size)
                        if new_sl > pos.sl:
                            self._modify_sl(ticket, pos.symbol, new_sl)
                            logger.info(
                                "TRAIL SL: %s ticket=%d SL %.5f -> %.5f (+%.1f pips profit locked)",
                                pos.symbol, ticket, pos.sl, new_sl, profit_pips - trail_dist,
                            )
                            actions.append(
                                f"TRAIL: {pos.symbol} ticket={ticket} SL->{new_sl:.5f} locking {profit_pips - trail_dist:.1f} pips"
                            )
                    else:
                        new_sl = current + (trail_dist * pip_size)
                        if new_sl < pos.sl:
                            self._modify_sl(ticket, pos.symbol, new_sl)
                            logger.info(
                                "TRAIL SL: %s ticket=%d SL %.5f -> %.5f (+%.1f pips profit locked)",
                                pos.symbol, ticket, pos.sl, new_sl, profit_pips - trail_dist,
                            )
                            actions.append(
                                f"TRAIL: {pos.symbol} ticket={ticket} SL->{new_sl:.3f} locking {profit_pips - trail_dist:.1f} pips"
                            )

        return actions

    def _partial_close(self, position, volume: float) -> bool:
        close_type = (
            mt5.ORDER_TYPE_SELL
            if position.type == mt5.ORDER_TYPE_BUY
            else mt5.ORDER_TYPE_BUY
        )

        tick = mt5.symbol_info_tick(position.symbol)
        price = (
            tick.bid if close_type == mt5.ORDER_TYPE_SELL else tick.ask
        ) if tick else 0

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": position.symbol,
            "volume": volume,
            "type": close_type,
            "position": position.ticket,
            "price": price,
            "deviation": self._deviation_points(position.symbol),
            "magic": 314159,
            "comment": "HelixV3_T1_partial",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": self._filling_mode(position.symbol),
        }

        result = mt5.order_send(request)
        if result and result.retcode == mt5.TRADE_RETCODE_DONE:
            return True

        logger.error(
            "Partial close failed for %s: %s",
            position.symbol,
            result.comment if result else "None",
        )
        return False

    def _modify_sl(self, ticket: int, symbol: str, new_sl: float) -> bool:
        """Modify a position's stop, portably and safely (Tier 3.3).

        - Preserves the existing TP in the request — TRADE_ACTION_SLTP
          with tp omitted CLEARS the take profit, so every trail/BE move
          was silently wiping TP2.
        - Respects trade_stops_level: a stop inside the broker minimum is
          clamped to the closest allowed price, and skipped entirely if
          clamping would LOOSEN the existing stop.
        - Respects freeze_level: a stop about to trigger is left alone.
        - Rounds to the symbol's digits (the fixed 5 was wrong for
          JPY/gold/indices).
        On any pre-check lookup failure, falls back to the raw modify.
        """
        digits = 5
        current_tp = 0.0
        try:
            info = self._get_symbol_info(symbol)
            digits = int(info.digits)
            point = float(info.point)
            stops_dist = max(0, int(getattr(info, "trade_stops_level", 0))) * point
            freeze_dist = max(0, int(getattr(info, "trade_freeze_level", 0))) * point
            plist = mt5.positions_get(ticket=ticket)
            pos = plist[0] if plist else None
            tick = mt5.symbol_info_tick(symbol)
            if pos is not None:
                current_tp = float(pos.tp or 0.0)
                if tick is not None:
                    if pos.type == mt5.POSITION_TYPE_BUY:
                        market = float(tick.bid)
                        if (
                            freeze_dist > 0 and pos.sl > 0
                            and 0 <= market - pos.sl <= freeze_dist
                        ):
                            logger.debug(
                                "SL modify skipped %s ticket=%d: stop inside freeze level",
                                symbol, ticket,
                            )
                            return False
                        limit = market - stops_dist
                        if stops_dist > 0 and new_sl > limit:
                            if pos.sl > 0 and limit <= pos.sl:
                                logger.debug(
                                    "SL modify skipped %s ticket=%d: clamped stop "
                                    "would not improve (stops level)", symbol, ticket,
                                )
                                return False
                            new_sl = limit
                    else:
                        market = float(tick.ask)
                        if (
                            freeze_dist > 0 and pos.sl > 0
                            and 0 <= pos.sl - market <= freeze_dist
                        ):
                            logger.debug(
                                "SL modify skipped %s ticket=%d: stop inside freeze level",
                                symbol, ticket,
                            )
                            return False
                        limit = market + stops_dist
                        if stops_dist > 0 and new_sl < limit:
                            if pos.sl > 0 and limit >= pos.sl:
                                logger.debug(
                                    "SL modify skipped %s ticket=%d: clamped stop "
                                    "would not improve (stops level)", symbol, ticket,
                                )
                                return False
                            new_sl = limit
        except Exception as e:
            logger.debug("SL modify pre-check unavailable for %s: %s", symbol, e)

        request = {
            "action": mt5.TRADE_ACTION_SLTP,
            "position": ticket,
            "symbol": symbol,
            "sl": round(new_sl, digits),
        }
        if current_tp > 0:
            request["tp"] = round(current_tp, digits)

        result = mt5.order_send(request)
        if result and result.retcode == mt5.TRADE_RETCODE_DONE:
            return True

        logger.error(
            "SL modify failed for ticket %d: %s",
            ticket, result.comment if result else "None",
        )
        return False

    # ------------------------------------------------------------------
    # Emergency Close All
    # ------------------------------------------------------------------

    def close_all_positions(self) -> int:
        """Emergency close all Helix positions. Returns count of closed."""
        positions = mt5.positions_get()
        if not positions:
            return 0

        closed = 0
        for pos in positions:
            if pos.magic != 314159:
                continue
            if self._partial_close(pos, pos.volume):
                closed += 1
                logger.info("Emergency closed: %s ticket=%d", pos.symbol, pos.ticket)

        self._active_orders.clear()
        return closed
