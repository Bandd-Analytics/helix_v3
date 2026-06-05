"""MT5ExecutionGatekeeper - Risk management and low-latency MT5 order execution.

Transforms validated consensus signals into live MT5 trades with dynamic lot
sizing, structural stop-loss placement, partial profit taking, and slippage
protection.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, List, Optional

import MetaTrader5 as mt5
import numpy as np

from config.pair_profiles import PairProfile, get_pair_profile
from config.settings import settings
from helix_v3.core.types import (
    ConsensusResult,
    Direction,
    ExecutionOrder,
    QuantSignal,
)
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

    def __init__(self) -> None:
        self._risk_cfg = settings.risk
        self._active_orders: Dict[int, ExecutionOrder] = {}
        self.journal = TradeJournal()

    # ------------------------------------------------------------------
    # Account & Symbol Info
    # ------------------------------------------------------------------

    def _get_account_equity(self) -> float:
        info = mt5.account_info()
        if info is None:
            raise ConnectionError("Cannot retrieve MT5 account info")
        return float(info.equity)

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
    # Drawdown Circuit Breaker
    # ------------------------------------------------------------------

    def check_drawdown_limit(self) -> bool:
        equity = self._get_account_equity()
        balance = self._get_account_balance()

        if balance == 0:
            return False

        drawdown = (balance - equity) / balance
        if drawdown >= self._risk_cfg.max_drawdown_pct:
            logger.critical(
                "DRAWDOWN CIRCUIT BREAKER: %.2f%% >= %.2f%% limit. Blocking all new trades.",
                drawdown * 100, self._risk_cfg.max_drawdown_pct * 100,
            )
            return False
        return True

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
    ) -> float:
        """Lot = (Equity * PairRisk%) / (SL_pips * PipValue_per_lot)

        Safety layers:
        1. SL floor — never size off fewer pips than pair minimum
        2. Account-proportional max lot — caps based on equity, not static
        3. Post-calc risk verification — rejects if actual $ risk exceeds limit
        """
        profile = get_pair_profile(symbol)
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
            logger.error("Invalid tick_size or sl_pips for lot calculation")
            return info.volume_min

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
        lot = round(lot / vol_step) * vol_step
        lot = round(lot, 2)

        # --- Safety 3: Post-calc risk verification ---
        actual_risk = lot * effective_sl * pip_value_per_lot
        actual_risk_pct = actual_risk / equity if equity > 0 else 1.0
        if actual_risk_pct > max_loss_pct:
            lot = vol_min
            actual_risk = lot * effective_sl * pip_value_per_lot
            actual_risk_pct = actual_risk / equity if equity > 0 else 1.0
            logger.warning(
                "Risk verification clamped %s to min lot %.2f (risk was %.1f%%)",
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

        # SL placement: pair-specific buffer behind peak formation
        profile = get_pair_profile(symbol)
        buffer = profile.sl_buffer_pips * pip_size

        if signal.session_bounds is not None:
            if direction == Direction.BUY:
                sl = signal.session_bounds.low - buffer
            else:
                sl = signal.session_bounds.high + buffer
        else:
            # Fallback: use stop hunt breach or fixed 30 pips
            fallback_pips = 30.0
            if direction == Direction.BUY:
                sl = entry - (fallback_pips * pip_size)
            else:
                sl = entry + (fallback_pips * pip_size)

        sl_pips = abs(entry - sl) / pip_size
        lot_size = self.calculate_lot_size(symbol, sl_pips)

        # TP levels
        risk_distance = abs(entry - sl)
        if direction == Direction.BUY:
            tp1 = entry + risk_distance  # 1:1 RR
            tp2 = entry + (risk_distance * 2.5)  # 2.5:1 RR
        else:
            tp1 = entry - risk_distance
            tp2 = entry - (risk_distance * 2.5)

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

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": order.symbol,
            "volume": order.lot_size,
            "type": order_type,
            "price": order.entry_price,
            "sl": order.stop_loss,
            "tp": order.take_profit_2,  # Initial TP at T2 level
            "deviation": 10,  # Max slippage in points
            "magic": 314159,
            "comment": "HelixV3_MMM",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        for attempt in range(1, max_retries + 1):
            # Refresh price before each attempt
            tick = mt5.symbol_info_tick(order.symbol)
            if tick is not None:
                request["price"] = (
                    tick.ask if order.direction == Direction.BUY else tick.bid
                )

            result = mt5.order_send(request)
            if result is None:
                logger.error("order_send returned None on attempt %d", attempt)
                continue

            if result.retcode == mt5.TRADE_RETCODE_DONE:
                ticket = result.order
                order.ticket = ticket
                order.status = "FILLED"
                self._active_orders[ticket] = order
                logger.info(
                    "ORDER FILLED: ticket=%d %s %s %.2f @ %.5f",
                    ticket, order.direction.value, order.symbol,
                    order.lot_size, result.price,
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
            return []

        actions: List[str] = []
        now_ts = mt5.symbol_info_tick(settings.trading.symbols[0])
        server_time = now_ts.time if now_ts else 0

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
                # Reconstruct T1 from SL/TP
                pip_size = self._get_pip_value(pos.symbol)
                sl_dist = abs(pos.price_open - pos.sl)
                if direction == Direction.BUY:
                    order.take_profit_1 = pos.price_open + sl_dist
                else:
                    order.take_profit_1 = pos.price_open - sl_dist
                order.sl_pips = sl_dist / pip_size
                self._active_orders[ticket] = order
                logger.info("Adopted orphaned position: %s ticket=%d", pos.symbol, ticket)

            pip_size = self._get_pip_value(pos.symbol)
            pp = get_pair_profile(pos.symbol)
            entry = pos.price_open
            current = pos.price_current
            duration_min = (server_time - pos.time) / 60 if server_time > pos.time else 0

            if order.direction == Direction.BUY:
                profit_pips = (current - entry) / pip_size
                hit_t1 = current >= order.take_profit_1
            else:
                profit_pips = (entry - current) / pip_size
                hit_t1 = current <= order.take_profit_1

            # --- 1. Max Duration Exit (pair-gated) ---
            max_dur = pp.max_duration_minutes
            if duration_min >= max_dur:
                logger.warning(
                    "MAX DURATION EXIT: %s ticket=%d after %.0f min (limit=%d) pips=%+.1f",
                    pos.symbol, ticket, duration_min, max_dur, profit_pips,
                )
                self._partial_close(pos, pos.volume)
                actions.append(
                    f"TIME EXIT: {pos.symbol} ticket={ticket} after {duration_min:.0f}min pips={profit_pips:+.1f}"
                )
                continue

            # --- 2. Stale Trade Detection (90 min universal, exit if NOT in profit) ---
            stale_min = pp.stale_minutes  # 90 min for all pairs
            if duration_min >= stale_min and profit_pips <= 0 and order.status == "FILLED":
                logger.warning(
                    "STALE TRADE: %s ticket=%d | %+.1f pips after %.0f min (not in profit) — closing",
                    pos.symbol, ticket, profit_pips, duration_min,
                )
                self._partial_close(pos, pos.volume)
                actions.append(
                    f"STALE EXIT: {pos.symbol} ticket={ticket} {profit_pips:+.1f} pips after {duration_min:.0f}min (not in profit)"
                )
                continue
            # NOTE: If profit_pips > 0 after 90 min, trade STAYS OPEN and trails via rule 5

            # --- 3. Session-Based Exit (pair-gated) ---
            from helix_v3.scanner.market_scanner import _get_session_name
            current_session = _get_session_name()
            close_session = pp.close_before_session
            if current_session == close_session and order.status in ("FILLED", "T1_HIT"):
                if profit_pips < self._risk_cfg.stale_trade_max_pips:
                    logger.warning(
                        "SESSION EXIT: %s ticket=%d closing before %s | pips=%+.1f",
                        pos.symbol, ticket, close_session, profit_pips,
                    )
                    self._partial_close(pos, pos.volume)
                    actions.append(
                        f"SESSION EXIT: {pos.symbol} ticket={ticket} before {close_session} pips={profit_pips:+.1f}"
                    )
                    continue

            # --- 4. T1 Partial Close at 1:1 RR ---
            if hit_t1 and order.status == "FILLED":
                close_volume = round(
                    pos.volume * self._risk_cfg.partial_close_ratio, 2
                )
                if close_volume >= 0.01:
                    self._partial_close(pos, close_volume)
                    order.status = "T1_HIT"

                    # Move SL to breakeven
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

            # --- 5. Trailing Stop Loss ---
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
            "deviation": 10,
            "magic": 314159,
            "comment": "HelixV3_T1_partial",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
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
        request = {
            "action": mt5.TRADE_ACTION_SLTP,
            "position": ticket,
            "symbol": symbol,
            "sl": round(new_sl, 5),
        }

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
