"""Event-driven backtesting engine for Helix V3 MMM strategy.

Replays the V2 orchestrator pipeline on historical data:
  MTFAnalyzer -> confluence check -> entry decision -> trade management -> P&L

Usage:
    python -m helix_v3.backtest.engine --days 14
    python -m helix_v3.backtest.engine --pairs GBPJPY,EURUSD --start 2026-05-01 --end 2026-06-01
    python -m helix_v3.backtest.engine --days 14 --verbose
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional

import pandas as pd

from config.pair_profiles import PairProfile, get_pair_profile, get_tradeable_symbols
from helix_v3.core.exposure import OpenRisk, exposure_violation
from helix_v3.core.regime import assess_regime
from helix_v3.backtest.data_store import HistoricalDataStore
from helix_v3.core.mtf_analyzer import MTFAnalyzer
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.tdi import compute_tdi
from helix_v3.core.patterns import scan_patterns
from helix_v3.core.advisory_confidence import (
    AdvisorySetup,
    advisory_setup_from_mtf,
    score_advisory_setup,
)
from helix_v3.core.types import Direction
from helix_v3.utils.logger import get_logger

try:
    from helix_v3.backtest.mmm_event_replay import (
        MMMReplayStore,
        build_setup_signature,
        outcome_from_closed_trade,
        replay_setup_from_mtf,
    )
    _HAS_REPLAY = True
except ImportError:
    _HAS_REPLAY = False

logger = get_logger("backtest_engine")


# ---------------------------------------------------------------------------
# BacktestEngine — subclass of quant engine that reads from data store
# ---------------------------------------------------------------------------

class BacktestEngine(MMMQuantitativeEngine):
    """Quant engine that reads from pre-fetched historical data instead of MT5."""

    def __init__(self, data_store: HistoricalDataStore) -> None:
        super().__init__()
        self._data_store = data_store
        self._current_time: datetime = data_store.start_date
        self._connected = True  # Pretend we're connected

    def set_current_time(self, dt: datetime) -> None:
        self._current_time = dt

    def connect(self) -> bool:
        return True

    def disconnect(self) -> None:
        pass

    def fetch_rates(
        self, symbol: str, timeframe: str, count: int = 1000
    ) -> pd.DataFrame:
        df = self._data_store.get_rates(symbol, timeframe, self._current_time, count)
        if df.empty:
            raise ConnectionError(
                f"No historical data for {symbol} {timeframe} at {self._current_time}"
            )
        return df

    def _get_pip_value(self, symbol: str) -> float:
        return self._data_store.get_pip_size(symbol)


# ---------------------------------------------------------------------------
# Trade simulation
# ---------------------------------------------------------------------------

@dataclass
class SimulatedTrade:
    symbol: str
    direction: Direction
    entry_price: float
    entry_time: datetime
    lot_size: float
    stop_loss: float
    take_profit_1: float
    take_profit_2: float
    sl_pips: float
    pip_size: float
    pip_value_per_lot: float = 10.0
    # State
    status: str = "OPEN"  # OPEN, T1_HIT, CLOSED
    exit_price: float = 0.0
    exit_time: Optional[datetime] = None
    exit_reason: str = ""
    pnl_pips: float = 0.0
    pnl_dollars: float = 0.0
    max_favorable_pips: float = 0.0
    max_adverse_pips: float = 0.0
    t1_closed: bool = False
    t1_pips: float = 0.0
    remaining_lots: float = 0.0
    current_sl: float = 0.0
    stale_tightened: bool = False
    last_close: float = 0.0
    realized_dollars: float = 0.0
    advisory_grade: str = ""
    advisory_score: float = 0.0
    # ATR-resolved profile frozen at entry (Tier 2.3) — management params
    # (trail/stale/duration) come from entry-time volatility, not a static
    # table and not a peek at later bars.
    profile: Optional[PairProfile] = None

    def __post_init__(self):
        self.remaining_lots = self.lot_size
        self.current_sl = self.stop_loss
        self.last_close = self.entry_price


class TradeSimulator:
    """Simulates trade lifecycle bar-by-bar matching live V2 rules.

    Honest accounting (audit Tier 1.4-1.6):
      - P&L comes from the actual computed lot x pip value, not from
        equity-fraction shortcuts; risk is taken from equity at ENTRY.
      - T1 partials book realized cash at the closed size immediately;
        the remainder is all that TP2/SL can pay later.
      - Costs: full spread (half per side) + slippage per side on every
        fill, commission per lot per round trip at final close.
      - SL fills at the bar OPEN when the bar gapped through the stop.
      - Same-bar ordering is conservative: SL first, then T1, then TP2.
      - Equity curve and the drawdown breaker are MARK-TO-MARKET.
    """

    def __init__(
        self,
        initial_equity: float = 1000.0,
        slippage_pips: float = 0.5,
        commission_per_lot: float = 0.0,
    ) -> None:
        self.equity = initial_equity          # realized cash
        self.mtm_equity = initial_equity      # realized + floating
        self.peak_equity = initial_equity     # peak of MTM equity
        self.slippage_pips = slippage_pips
        self.commission_per_lot = commission_per_lot
        self.open_trades: List[SimulatedTrade] = []
        self.closed_trades: List[SimulatedTrade] = []
        self.equity_curve: List[tuple] = []  # (datetime, mtm_equity)

    # -- cost model --------------------------------------------------------

    def _side_cost_pips(self, symbol: str) -> float:
        """Half the full spread plus slippage — paid on EVERY fill side."""
        profile = get_pair_profile(symbol)
        return profile.max_spread_pips / 2.0 + self.slippage_pips

    def _net_exit_price(self, trade: SimulatedTrade, fill_price: float) -> float:
        cost = self._side_cost_pips(trade.symbol) * trade.pip_size
        if trade.direction == Direction.BUY:
            return fill_price - cost
        return fill_price + cost

    def open_trade(
        self,
        symbol: str,
        direction: Direction,
        entry_price: float,
        entry_time: datetime,
        sl_price: float,
        pip_size: float,
        pip_value_per_lot: float,
        profile: Optional[PairProfile] = None,
    ) -> Optional[SimulatedTrade]:
        """Open a simulated trade with proper lot sizing.

        `entry_price` is the raw bar close — entry costs (half spread +
        slippage, adverse direction) are applied here. `profile` should be
        the ATR-resolved profile from decision time (Tier 2.3); it is
        frozen on the trade for all management decisions.
        """
        profile = profile or get_pair_profile(symbol)

        entry_cost = self._side_cost_pips(symbol) * pip_size
        if direction == Direction.BUY:
            entry_price = entry_price + entry_cost
        else:
            entry_price = entry_price - entry_cost

        sl_pips = abs(entry_price - sl_price) / pip_size

        # Apply SL floor — widen actual SL if too tight (prevents suicide stops)
        if sl_pips < profile.min_sl_pips:
            sl_pips = profile.min_sl_pips
            if direction == Direction.BUY:
                sl_price = entry_price - (sl_pips * pip_size)
            else:
                sl_price = entry_price + (sl_pips * pip_size)
        effective_sl = sl_pips

        # Lot sizing: Equity * Risk% / (SL_pips * pip_value_per_lot)
        risk_amount = self.equity * profile.max_risk_pct
        if pip_value_per_lot <= 0 or effective_sl <= 0:
            return None

        raw_lot = risk_amount / (effective_sl * pip_value_per_lot)

        # Account-proportional cap (3% hard limit)
        account_max_lot = (self.equity * 0.03) / (effective_sl * pip_value_per_lot)
        lot = min(raw_lot, profile.max_lot_size, account_max_lot)
        # FLOOR to lot step (matching the live gatekeeper — never round up)
        lot = max(0.01, round(math.floor(lot / 0.01 + 1e-9) * 0.01, 2))

        # TP levels — calibrated from validation data
        # T1: 1:1 RR (unchanged — locks in profit)
        # T2: min(expected_level_move, 2.5x SL) — targets realistic move, not blind multiple
        risk_dist = abs(entry_price - sl_price)
        level_move_dist = profile.expected_level_move_pips * pip_size
        # T2 distance = the smaller of level move or 2.5x SL (whichever is reachable)
        tp2_dist = min(level_move_dist, risk_dist * 2.5)
        # But never less than 1.5x SL (minimum RR worth holding for)
        tp2_dist = max(tp2_dist, risk_dist * 1.5)

        if direction == Direction.BUY:
            tp1 = entry_price + risk_dist
            tp2 = entry_price + tp2_dist
        else:
            tp1 = entry_price - risk_dist
            tp2 = entry_price - tp2_dist

        trade = SimulatedTrade(
            symbol=symbol,
            direction=direction,
            entry_price=entry_price,
            entry_time=entry_time,
            lot_size=lot,
            stop_loss=sl_price,
            take_profit_1=tp1,
            take_profit_2=tp2,
            sl_pips=sl_pips,
            pip_size=pip_size,
            pip_value_per_lot=pip_value_per_lot,
            profile=profile,
        )
        self.open_trades.append(trade)
        return trade

    def process_bar(self, bar_time: datetime, bars: Dict[str, pd.Series]) -> List[str]:
        """Process one M15 bar for all open trades. Returns action descriptions.

        Same-bar ordering is conservative: SL first (assume the worst path),
        then T1 partial, then TP2 on the remainder.
        """
        actions = []
        still_open = []

        for trade in self.open_trades:
            bar = bars.get(trade.symbol)
            if bar is None:
                still_open.append(trade)
                continue

            bar_open = float(bar["Open"])
            high = float(bar["High"])
            low = float(bar["Low"])
            close = float(bar["Close"])
            trade.last_close = close
            profile = trade.profile or get_pair_profile(trade.symbol)

            # Track MFE/MAE
            if trade.direction == Direction.BUY:
                fav = (high - trade.entry_price) / trade.pip_size
                adv = (trade.entry_price - low) / trade.pip_size
                profit_pips = (close - trade.entry_price) / trade.pip_size
            else:
                fav = (trade.entry_price - low) / trade.pip_size
                adv = (high - trade.entry_price) / trade.pip_size
                profit_pips = (trade.entry_price - close) / trade.pip_size

            trade.max_favorable_pips = max(trade.max_favorable_pips, fav)
            trade.max_adverse_pips = max(trade.max_adverse_pips, adv)

            duration_min = (bar_time - trade.entry_time).total_seconds() / 60

            # --- 1. SL hit (gap-aware: a stop is a market order — when the
            # bar OPENS beyond the stop it fills at the open, not the level) ---
            sl_hit = False
            if trade.direction == Direction.BUY and low <= trade.current_sl:
                sl_hit = True
                fill = min(bar_open, trade.current_sl)
            elif trade.direction == Direction.SELL and high >= trade.current_sl:
                sl_hit = True
                fill = max(bar_open, trade.current_sl)

            if sl_hit:
                self.close_trade(trade, fill, bar_time, "SL_HIT")
                actions.append(f"SL HIT: {trade.symbol} {trade.pnl_pips:+.1f}p")
                continue

            # --- 2. T1 partial close at 1:1 RR (checked BEFORE TP2: if both
            # are inside one bar, T1 banked first is the conservative path) ---
            if not trade.t1_closed:
                t1_hit = False
                if trade.direction == Direction.BUY and high >= trade.take_profit_1:
                    t1_hit = True
                elif trade.direction == Direction.SELL and low <= trade.take_profit_1:
                    t1_hit = True

                if t1_hit:
                    self._book_t1(trade)
                    actions.append(f"T1 HIT: {trade.symbol} +{trade.t1_pips:.1f}p, SL->BE")

            # --- 3. TP2 hit (remainder only if T1 already banked) ---
            tp2_hit = False
            if trade.direction == Direction.BUY and high >= trade.take_profit_2:
                tp2_hit = True
            elif trade.direction == Direction.SELL and low <= trade.take_profit_2:
                tp2_hit = True

            if tp2_hit:
                self.close_trade(trade, trade.take_profit_2, bar_time, "TP2_HIT")
                actions.append(f"TP2 HIT: {trade.symbol} {trade.pnl_pips:+.1f}p")
                continue

            # --- 4. Max duration exit ---
            if duration_min >= profile.max_duration_minutes:
                self.close_trade(trade, close, bar_time, "MAX_DURATION")
                actions.append(f"TIME EXIT: {trade.symbol} {trade.pnl_pips:+.1f}p")
                continue

            # --- 5. Tiered stale trade management ---
            # Phase 1 (stale_minutes): Tighten SL to 50% for extended pairs
            # Phase 2 (stale_exit_minutes): Full exit
            stale_phase1 = profile.stale_minutes
            stale_phase2 = getattr(profile, "stale_exit_minutes", stale_phase1)

            if duration_min >= stale_phase2 and profit_pips <= 0:
                self.close_trade(trade, close, bar_time, "STALE")
                actions.append(f"STALE EXIT: {trade.symbol} {trade.pnl_pips:+.1f}p at {duration_min:.0f}min")
                continue

            if (duration_min >= stale_phase1 and profit_pips <= 0
                    and stale_phase2 > stale_phase1
                    and not trade.stale_tightened):
                # Phase 1: tighten the LIVE stop (current_sl — exits read it)
                # to half the original distance, in the trade's own pip size.
                # The old code computed pip_size = min_sl/min_sl = 1.0 and
                # wrote trade.stop_loss, which nothing reads: a double no-op.
                if trade.sl_pips > 0:
                    half_dist = (trade.sl_pips / 2.0) * trade.pip_size
                    if trade.direction == Direction.BUY:
                        new_sl = trade.entry_price - half_dist
                        if new_sl > trade.current_sl:
                            trade.current_sl = new_sl
                    else:
                        new_sl = trade.entry_price + half_dist
                        if new_sl < trade.current_sl:
                            trade.current_sl = new_sl
                    trade.stale_tightened = True
                    actions.append(f"STALE TIGHTEN: {trade.symbol} SL halved at {duration_min:.0f}min")

            # --- 6. Trailing stop (after T1) ---
            if trade.t1_closed and profit_pips >= profile.trail_activation_pips:
                if trade.direction == Direction.BUY:
                    new_sl = close - profile.trail_distance_pips * trade.pip_size
                    if new_sl > trade.current_sl:
                        trade.current_sl = new_sl
                else:
                    new_sl = close + profile.trail_distance_pips * trade.pip_size
                    if new_sl < trade.current_sl:
                        trade.current_sl = new_sl

            still_open.append(trade)

        self.open_trades = still_open

        # Mark-to-market equity snapshot — drawdown must see floating losses
        unrealized = sum(self._unrealized_pnl(t) for t in self.open_trades)
        self.mtm_equity = self.equity + unrealized
        self.peak_equity = max(self.peak_equity, self.mtm_equity)
        self.equity_curve.append((bar_time, self.mtm_equity))

        return actions

    def _book_t1(self, trade: SimulatedTrade) -> None:
        """Bank the T1 partial: realized cash for the closed half, SL to BE."""
        net = self._net_exit_price(trade, trade.take_profit_1)
        if trade.direction == Direction.BUY:
            pips = (net - trade.entry_price) / trade.pip_size
        else:
            pips = (trade.entry_price - net) / trade.pip_size

        t1_lots = round(trade.lot_size * 0.5, 2)
        dollars = pips * trade.pip_value_per_lot * t1_lots
        trade.realized_dollars += dollars
        self.equity += dollars

        trade.t1_closed = True
        trade.t1_pips = pips
        trade.remaining_lots = round(trade.lot_size - t1_lots, 2)
        trade.current_sl = trade.entry_price  # SL to breakeven
        trade.status = "T1_HIT"

    def close_trade(
        self,
        trade: SimulatedTrade,
        fill_price: float,
        exit_time: datetime,
        reason: str,
    ) -> None:
        """Close the remaining position at fill_price (exit costs applied here)."""
        net = self._net_exit_price(trade, fill_price)
        if trade.direction == Direction.BUY:
            rem_pips = (net - trade.entry_price) / trade.pip_size
        else:
            rem_pips = (trade.entry_price - net) / trade.pip_size

        rem_dollars = rem_pips * trade.pip_value_per_lot * trade.remaining_lots
        commission = self.commission_per_lot * trade.lot_size

        trade.exit_price = net
        trade.exit_time = exit_time
        trade.exit_reason = reason
        trade.status = "CLOSED"
        trade.realized_dollars += rem_dollars - commission
        trade.pnl_dollars = trade.realized_dollars

        # Lot-weighted average pips across the T1 leg and the remainder
        t1_lots = round(trade.lot_size - trade.remaining_lots, 2)
        if trade.lot_size > 0:
            trade.pnl_pips = (
                trade.t1_pips * t1_lots + rem_pips * trade.remaining_lots
            ) / trade.lot_size
        else:
            trade.pnl_pips = rem_pips

        self.equity += rem_dollars - commission
        trade.remaining_lots = 0.0
        self.closed_trades.append(trade)

    def _unrealized_pnl(self, trade: SimulatedTrade) -> float:
        """Mark the open remainder to the latest close."""
        if trade.direction == Direction.BUY:
            pips = (trade.last_close - trade.entry_price) / trade.pip_size
        else:
            pips = (trade.entry_price - trade.last_close) / trade.pip_size
        return pips * trade.pip_value_per_lot * trade.remaining_lots

    def has_open_position(self, symbol: str) -> bool:
        return any(t.symbol == symbol for t in self.open_trades)

    def has_open_direction(self, symbol: str, direction: Direction) -> bool:
        return any(
            t.symbol == symbol and t.direction == direction
            for t in self.open_trades
        )

    @property
    def max_drawdown_pct(self) -> float:
        """Current drawdown from peak, MARK-TO-MARKET (floating losses count)."""
        if self.peak_equity <= 0:
            return 0.0
        return (self.peak_equity - self.mtm_equity) / self.peak_equity


# ---------------------------------------------------------------------------
# BacktestRunner — orchestrates the full pipeline
# ---------------------------------------------------------------------------

class BacktestRunner:
    """Replays V2 pipeline on historical data."""

    def __init__(
        self,
        data_store: HistoricalDataStore,
        initial_equity: float = 1000.0,
        min_confluence: int = 50,
        max_concurrent: int = 3,
        verbose: bool = False,
        use_validation: bool = False,
        slippage_pips: float = 0.5,
        commission_per_lot: float = 0.0,
        news_events: Optional[list] = None,
    ) -> None:
        self.data_store = data_store
        self.engine = BacktestEngine(data_store)
        self.mtf = MTFAnalyzer(self.engine)
        # News blackout (Tier 2.5): historical high-impact events, injected
        # (e.g. --news-csv). None = no blackout in this backtest run.
        self._news_calendar = None
        self._news_blocks = 0
        # Currency exposure cap (Tier 2.6)
        self._exposure_blocks = 0
        # Regime filter (Tier 2.8)
        from config.settings import settings as _settings
        self._regime_enabled = _settings.risk.regime_filter_enabled
        self._regime_blocks = 0
        if news_events:
            from helix_v3.core.news_calendar import NewsCalendar

            self._news_calendar = NewsCalendar(events=news_events)
        self.simulator = TradeSimulator(
            initial_equity,
            slippage_pips=slippage_pips,
            commission_per_lot=commission_per_lot,
        )
        self.min_confluence = min_confluence
        self.max_concurrent = max_concurrent
        self.verbose = verbose
        self.use_validation = use_validation
        # In-memory re-entry guard for speed
        self._loss_cooldowns: Dict[str, datetime] = {}  # "SYMBOL_DIR" -> cooldown_until
        self._loss_counts: Dict[str, int] = {}  # "SYMBOL_DIR" -> consecutive losses
        self._day_bans: Dict[str, str] = {}  # "SYMBOL_DIR" -> ban_date
        # Entry cooldown: block re-entry on same symbol for 2 hours after ANY exit
        self._entry_cooldowns: Dict[str, datetime] = {}  # "SYMBOL" -> cooldown_until
        # Advisory peer tracking for convergence scoring
        self._current_advisory_setups: Dict[str, AdvisorySetup] = {}  # symbol -> latest setup
        # Replay store for recording trade outcomes
        self._replay_store = MMMReplayStore() if _HAS_REPLAY else None
        # Track ReplaySetup per trade for outcome recording (keyed by "SYMBOL_entry_time")
        self._trade_setups: Dict[str, object] = {}  # "SYMBOL_timestamp" -> ReplaySetup
        # Monotonic source-id for replay records. len(closed_trades) at entry
        # time collided for concurrent trades AND across runs (the tables are
        # UNIQUE(source, source_id) with INSERT OR REPLACE — collisions
        # silently overwrote earlier outcomes). Seed with ms epoch so every
        # run owns a distinct id range.
        self._next_source_id = int(datetime.now(timezone.utc).timestamp() * 1000)
        # Validation library for filtering entries
        self._validation_lib = None
        self._validation_blocks = 0
        self._validation_matches = 0
        self._graveyard_warnings = 0
        if use_validation and _HAS_REPLAY:
            try:
                from pathlib import Path

                from config.settings import settings
                from helix_v3.backtest.validation_library import ValidationLibrary

                # WALK-FORWARD: build a partitioned library that only knows
                # outcomes from strictly BEFORE the evaluation window, with a
                # 1-week embargo. Querying the live library here let the
                # backtest trade patterns promoted from these exact bars.
                wf_path = Path(settings.log_dir) / "validation_library_walkforward.db"
                for suffix in ("", "-wal", "-shm"):
                    Path(str(wf_path) + suffix).unlink(missing_ok=True)
                cutoff = data_store.start_date - timedelta(days=7)
                self._validation_lib = ValidationLibrary(db_path=wf_path)
                count = self._validation_lib.rebuild_from_replay(before=cutoff)
                logger.info(
                    "Walk-forward validation library: %d setups from outcomes "
                    "before %s (1-week embargo before window start)",
                    count, cutoff.strftime("%Y-%m-%d"),
                )
            except Exception as e:
                logger.warning("Failed to build walk-forward validation library: %s", e)

    def run(self) -> None:
        """Execute the backtest."""
        symbols = self.data_store.symbols
        all_timestamps = set()
        for sym in symbols:
            ts = self.data_store.get_m15_timestamps(sym)
            all_timestamps.update(ts)

        sorted_times = sorted(all_timestamps)
        total_bars = len(sorted_times)

        logger.info(
            "Backtest starting: %d symbols, %d M15 bars, %s to %s",
            len(symbols), total_bars,
            self.data_store.start_date.strftime("%Y-%m-%d"),
            self.data_store.end_date.strftime("%Y-%m-%d"),
        )

        for i, bar_time in enumerate(sorted_times):
            dt = bar_time.to_pydatetime().replace(tzinfo=timezone.utc)
            # Decisions happen at the CLOSE of the just-finished M15 bar.
            # The data store only serves bars fully closed by as_of, so with
            # as_of = bar close the M15 bar itself is visible (its close is
            # known) while forming H1/H4/D1 bars are not (Tier 1.1).
            decision_time = dt + timedelta(minutes=15)
            self.engine.set_current_time(decision_time)

            # Get M15 bars for all symbols at this timestamp
            current_bars: Dict[str, pd.Series] = {}
            for sym in symbols:
                df = self.data_store.get_rates(sym, "M15", decision_time, 1)
                if not df.empty and df.index[-1] == bar_time:
                    current_bars[sym] = df.iloc[-1]

            # Manage open trades first
            actions = self.simulator.process_bar(decision_time, current_bars)
            for action in actions:
                if self.verbose:
                    logger.info("[%s] %s", dt.strftime("%m-%d %H:%M"), action)
                # Entry cooldown after ANY exit (prevents same-setup churn)
                self._record_exit(action, decision_time)
                # Additional loss-specific guard
                if "SL HIT" in action or "STALE EXIT" in action:
                    self._record_loss(action, decision_time)

            # Skip if too many open positions
            if len(self.simulator.open_trades) >= self.max_concurrent:
                continue

            # Check drawdown circuit breaker
            if self.simulator.max_drawdown_pct >= 0.08:
                continue

            # Scan each symbol for entries
            for sym in symbols:
                if sym not in current_bars:
                    continue
                if self.simulator.has_open_position(sym):
                    continue
                if len(self.simulator.open_trades) >= self.max_concurrent:
                    break

                try:
                    self._check_entry(sym, decision_time)
                except Exception as e:
                    if self.verbose:
                        logger.debug("Skip %s at %s: %s", sym, dt, e)

            # Progress logging every 500 bars
            if (i + 1) % 500 == 0:
                logger.info(
                    "Progress: %d/%d bars (%.0f%%) | Equity: $%.2f | Trades: %d",
                    i + 1, total_bars, (i + 1) / total_bars * 100,
                    self.simulator.equity, len(self.simulator.closed_trades),
                )

        # Close any remaining open trades at last bar
        end_time = sorted_times[-1].to_pydatetime().replace(tzinfo=timezone.utc) + timedelta(minutes=15)
        for trade in list(self.simulator.open_trades):
            last_bar = current_bars.get(trade.symbol)
            fill = float(last_bar["Close"]) if last_bar is not None else trade.entry_price
            self.simulator.close_trade(trade, fill, end_time, "BACKTEST_END")
        self.simulator.open_trades.clear()

        logger.info(
            "Backtest complete: %d trades, equity $%.2f -> $%.2f",
            len(self.simulator.closed_trades),
            self.simulator.equity_curve[0][1] if self.simulator.equity_curve else 0,
            self.simulator.equity,
        )

    def _check_entry(self, symbol: str, bar_time: datetime) -> None:
        """Run MTF analysis and check entry conditions for one symbol."""
        # News blackout (Tier 2.5) — cheapest gate, check before analysis
        if self._news_calendar is not None:
            if self._news_calendar.blackout(symbol, bar_time) is not None:
                self._news_blocks += 1
                return

        # Regime filter (Tier 2.8) — MMM conditions present on this symbol?
        # Reads D1 as-of decision time through the BacktestEngine; the
        # verdict is cached per D1 bar so this is one check per day.
        if self._regime_enabled:
            regime = assess_regime(self.engine, symbol)
            if not regime.mmm_present:
                self._regime_blocks += 1
                if self.verbose:
                    logger.debug(
                        "[%s] %s REGIME SKIP: %s",
                        bar_time.strftime("%m-%d %H:%M"), symbol, regime.reason,
                    )
                return

        # Re-entry guard
        direction_key_buy = f"{symbol}_BUY"
        direction_key_sell = f"{symbol}_SELL"

        buy_banned = self._is_banned(direction_key_buy, bar_time)
        sell_banned = self._is_banned(direction_key_sell, bar_time)
        if buy_banned and sell_banned:
            return

        # MTF analysis (uses BacktestEngine.fetch_rates -> historical data)
        try:
            analysis = self.mtf.analyze(symbol)
        except Exception:
            return

        if not analysis.trade_valid:
            return
        if analysis.confluence_score < self.min_confluence:
            return

        direction = analysis.trade_direction
        if direction == Direction.NEUTRAL:
            return

        # Check direction-specific ban
        dir_key = f"{symbol}_{direction.value}"
        if self._is_banned(dir_key, bar_time):
            return

        # Advisory confidence scoring — grade the setup
        df_m15_tdi = self.data_store.get_rates(symbol, "M15", bar_time, 200)
        tdi_result = compute_tdi(df_m15_tdi) if not df_m15_tdi.empty else None
        pip_size = self.data_store.get_pip_size(symbol)
        pat_scan = scan_patterns(
            df_m15_tdi.iloc[-50:], pip_size,
            asian_high=analysis.fifteen_min.asian_range_high,
            asian_low=analysis.fifteen_min.asian_range_low,
        ) if not df_m15_tdi.empty else None

        advisory_setup = advisory_setup_from_mtf(
            analysis, tdi_result=tdi_result, patterns=pat_scan,
        )
        self._current_advisory_setups[symbol] = advisory_setup
        advisory = score_advisory_setup(
            advisory_setup, self._current_advisory_setups.values(),
        )

        # Block D and AVOID grades
        if advisory.grade in ("D", "AVOID"):
            if self.verbose:
                logger.debug(
                    "[%s] %s %s blocked: grade=%s score=%.0f blockers=%s",
                    bar_time.strftime("%m-%d %H:%M"), direction.value, symbol,
                    advisory.grade, advisory.final_score, advisory.blockers[:3],
                )
            return

        # Validation library filter — only enter proven setups
        if self._validation_lib and _HAS_REPLAY:
            rs = replay_setup_from_mtf(
                analysis, snapshot_at=bar_time,
                tdi_result=tdi_result, patterns=pat_scan,
                source="backtest",
            )
            matches = self._validation_lib.validate_setup(rs)
            if matches:
                best = matches[0]
                self._validation_matches += 1
                # Block if historically poor (<30% win rate)
                if best.total >= 5 and best.favorable_rate < 30.0:
                    self._validation_blocks += 1
                    if self.verbose:
                        logger.debug(
                            "[%s] %s %s VALIDATION BLOCK: %.0f%% win (%d samples)",
                            bar_time.strftime("%m-%d %H:%M"), direction.value, symbol,
                            best.favorable_rate, best.total,
                        )
                    return
                # Check graveyard for repeat offenders
                grave = self._validation_lib._conn.execute(
                    """SELECT times_demoted FROM setup_graveyard
                       WHERE normalized_key = ? AND (symbol = ? OR symbol = '')
                       AND times_demoted >= 3
                       LIMIT 1""",
                    (best.normalized_key, symbol),
                ).fetchone()
                if grave:
                    self._graveyard_warnings += 1
                    self._validation_blocks += 1
                    if self.verbose:
                        logger.debug(
                            "[%s] %s %s GRAVEYARD BLOCK: demoted %dx",
                            bar_time.strftime("%m-%d %H:%M"), direction.value, symbol,
                            grave[0],
                        )
                    return
            elif self.use_validation:
                # No match in validation library — skip unproven setups
                self._validation_blocks += 1
                return

        # Get entry price from M15 bar
        df_m15 = self.data_store.get_rates(symbol, "M15", bar_time, 1)
        if df_m15.empty:
            return

        bar = df_m15.iloc[-1]
        pip_size = self.data_store.get_pip_size(symbol)
        # ATR-resolved at decision time by the MTF analyzer (Tier 2.3)
        profile = getattr(analysis, "pair_profile", None) or get_pair_profile(symbol)

        # Raw bar close — entry costs (half spread + slippage, adverse side)
        # are applied inside TradeSimulator.open_trade (Tier 1.5).
        entry_price = float(bar["Close"])

        # SL from session bounds (Asian range) with sensible cap
        # Per MMM: SL goes behind the formation that invalidates the trade.
        # But if the stop hunt was deep, SL can end up absurdly far from entry.
        # Cap SL distance at expected_level_move_pips — if SL needs to be wider
        # than one full level move, the entry is too far from the structure.
        max_sl_dist = profile.expected_level_move_pips * pip_size
        if analysis.fifteen_min.asian_range_low and analysis.fifteen_min.asian_range_high:
            buffer = profile.sl_buffer_pips * pip_size
            if direction == Direction.BUY:
                structural_sl = analysis.fifteen_min.asian_range_low - buffer
                sl_dist = entry_price - structural_sl
                if sl_dist > max_sl_dist:
                    sl_price = entry_price - max_sl_dist
                else:
                    sl_price = structural_sl
            else:
                structural_sl = analysis.fifteen_min.asian_range_high + buffer
                sl_dist = structural_sl - entry_price
                if sl_dist > max_sl_dist:
                    sl_price = entry_price + max_sl_dist
                else:
                    sl_price = structural_sl
        else:
            # Fallback: 30 pips
            fallback = 30.0 * pip_size
            if direction == Direction.BUY:
                sl_price = entry_price - fallback
            else:
                sl_price = entry_price + fallback

        # Approximate pip value per lot
        tick_value = self.data_store.get_tick_value(symbol)
        digits = self.data_store.get_digits(symbol)
        point = 10 ** (-digits)
        pip_size_calc = point * 10 if digits in (3, 5) else point
        pip_value_per_lot = (pip_size_calc / point) * tick_value if point > 0 else 10.0

        # Currency exposure cap (Tier 2.6) — same NET-per-currency rule the
        # live gatekeeper enforces. Risk per open trade = loss at its
        # current stop (breakeven stop = 0).
        from config.settings import settings as _settings
        eq = self.simulator.mtm_equity
        opens = []
        for t in self.simulator.open_trades:
            if t.direction == Direction.BUY:
                dist = max(0.0, t.entry_price - t.current_sl)
            else:
                dist = max(0.0, t.current_sl - t.entry_price)
            loss = (dist / t.pip_size) * t.pip_value_per_lot * t.remaining_lots
            opens.append(OpenRisk(t.symbol, t.direction, loss / eq if eq > 0 else 0.0))
        cap_pct = (
            _settings.risk.max_currency_exposure_mult * _settings.risk.max_risk_per_trade
        )
        violation = exposure_violation(symbol, direction, profile.max_risk_pct, opens, cap_pct)
        if violation is not None:
            self._exposure_blocks += 1
            if self.verbose:
                logger.debug(
                    "[%s] %s EXPOSURE BLOCK: %s",
                    bar_time.strftime("%m-%d %H:%M"), symbol, violation,
                )
            return

        trade = self.simulator.open_trade(
            symbol=symbol,
            direction=direction,
            entry_price=entry_price,
            entry_time=bar_time,
            sl_price=sl_price,
            pip_size=pip_size,
            pip_value_per_lot=pip_value_per_lot,
            profile=profile,
        )

        if trade:
            trade.advisory_grade = advisory.grade
            trade.advisory_score = advisory.final_score
            # Store replay setup for outcome recording when trade closes
            if _HAS_REPLAY:
                self._next_source_id += 1
                rs = replay_setup_from_mtf(
                    analysis, snapshot_at=bar_time,
                    tdi_result=tdi_result, patterns=pat_scan,
                    source="backtest", source_id=self._next_source_id,
                )
                trade_key = f"{symbol}_{bar_time.isoformat()}"
                self._trade_setups[trade_key] = rs
            if self.verbose:
                logger.info(
                    "[%s] ENTRY: %s %s %.2fL @ %.5f SL=%.5f conf=%d grade=%s(%.0f)",
                    bar_time.strftime("%m-%d %H:%M"),
                    direction.value, symbol, trade.lot_size,
                    entry_price, sl_price, analysis.confluence_score,
                    advisory.grade, advisory.final_score,
                )

    def _record_exit(self, action: str, bar_time: datetime) -> None:
        """Set entry cooldown and record outcome to replay store."""
        # T1 HIT means the trade is still open (partial close), skip
        if "T1 HIT" in action:
            return
        parts = action.split(":")
        if len(parts) < 2:
            return
        symbol = parts[1].strip().split()[0]
        # 2 hour entry cooldown on the symbol after any exit
        self._entry_cooldowns[symbol] = bar_time + timedelta(hours=2)

        # Record outcome to replay store — find the most recently closed trade for this symbol
        if self._replay_store and _HAS_REPLAY:
            for trade in reversed(self.simulator.closed_trades):
                if trade.symbol == symbol:
                    entry_ts = trade.entry_time
                    if hasattr(entry_ts, 'isoformat'):
                        trade_key = f"{symbol}_{entry_ts.isoformat()}"
                    else:
                        trade_key = f"{symbol}_{str(entry_ts)}"
                    rs = self._trade_setups.pop(trade_key, None)
                    if rs is not None:
                        try:
                            sig = build_setup_signature(rs)
                            sig_id = self._replay_store.record_signature(sig)
                            outcome = outcome_from_closed_trade(trade, rs)
                            self._replay_store.record_outcome(outcome, sig_id)
                        except Exception as e:
                            logger.warning("Replay record failed for %s: %s", symbol, e)
                    break

    def _record_loss(self, action: str, bar_time: datetime) -> None:
        """Update re-entry guard after a losing trade."""
        parts = action.split(":")
        if len(parts) < 2:
            return
        symbol = parts[1].strip().split()[0]
        # Find the closed trade
        for trade in reversed(self.simulator.closed_trades):
            if trade.symbol == symbol and trade.pnl_pips < 0:
                dir_key = f"{symbol}_{trade.direction.value}"
                count = self._loss_counts.get(dir_key, 0) + 1
                self._loss_counts[dir_key] = count

                if count >= 2:
                    # Day ban
                    self._day_bans[dir_key] = bar_time.strftime("%Y-%m-%d")
                else:
                    # Cooldown: 4 hours
                    self._loss_cooldowns[dir_key] = bar_time + timedelta(hours=4)
                break

    def _is_banned(self, dir_key: str, bar_time: datetime) -> bool:
        """Check if a symbol/direction is banned or in cooldown."""
        # Day ban
        ban_date = self._day_bans.get(dir_key)
        if ban_date and bar_time.strftime("%Y-%m-%d") == ban_date:
            return True

        # Loss cooldown
        cooldown_until = self._loss_cooldowns.get(dir_key)
        if cooldown_until and bar_time < cooldown_until:
            return True

        # Entry cooldown (same symbol, any direction — prevents same-setup churn)
        symbol = dir_key.rsplit("_", 1)[0]
        entry_cooldown = self._entry_cooldowns.get(symbol)
        if entry_cooldown and bar_time < entry_cooldown:
            return True

        # Reset consecutive count on new day
        if ban_date and bar_time.strftime("%Y-%m-%d") != ban_date:
            self._day_bans.pop(dir_key, None)
            self._loss_counts.pop(dir_key, None)

        return False


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _load_news_csv(path: str) -> list:
    """Parse a historical events CSV: time_utc,currency[,title] per line."""
    from helix_v3.core.news_calendar import HIGH_IMPACT, NewsEvent

    events = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.lower().startswith("time"):
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) < 2:
                continue
            dt = datetime.fromisoformat(parts[0])
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            events.append(NewsEvent(
                time_utc=dt.astimezone(timezone.utc),
                currency=parts[1].upper(),
                title=parts[2] if len(parts) > 2 else "",
                impact=HIGH_IMPACT,
            ))
    return events


def main(argv: Optional[list] = None) -> None:
    parser = argparse.ArgumentParser(description="Helix V3 MMM Strategy Backtester")
    parser.add_argument("--days", type=int, default=14, help="Days to backtest (from today)")
    parser.add_argument("--start", type=str, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, help="End date (YYYY-MM-DD)")
    parser.add_argument("--pairs", type=str, help="Comma-separated pairs (default: all 13)")
    parser.add_argument("--equity", type=float, default=1000.0, help="Starting equity")
    parser.add_argument("--min-confluence", type=int, default=55, help="Min confluence score")
    parser.add_argument("--max-positions", type=int, default=3, help="Max concurrent positions")
    parser.add_argument("--verbose", "-v", action="store_true", help="Detailed trade logging")
    parser.add_argument("--slippage", type=float, default=0.5,
                        help="Slippage in pips per fill side (default 0.5)")
    parser.add_argument("--slippage-mult", type=float, default=1.0,
                        help="Slippage stress multiplier: run at 0/1/2 to bracket the edge")
    parser.add_argument("--commission", type=float, default=0.0,
                        help="Commission per lot per round trip in account currency")
    parser.add_argument("--validation", action="store_true",
                        help="Only enter setups matched by validation library (proven patterns)")
    parser.add_argument("--promote", action="store_true",
                        help="After the run, promote this run's outcomes into the LIVE "
                             "validation library (off by default: a backtest must not "
                             "silently feed the gate it will be tested against)")
    parser.add_argument("--news-csv", type=str, default=None,
                        help="CSV of historical high-impact events (time_utc,currency[,title]) "
                             "— entries blocked within the blackout window (Tier 2.5)")
    parser.add_argument("--compare", action="store_true",
                        help="Run twice (with and without validation) and compare results")
    args = parser.parse_args(argv)

    # Date range
    if args.start and args.end:
        start = datetime.strptime(args.start, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        end = datetime.strptime(args.end, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    else:
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=args.days)

    # Pairs
    if args.pairs:
        symbols = [p.strip() for p in args.pairs.split(",")]
    else:
        symbols = get_tradeable_symbols()

    print(f"\nHelix V3 Backtest: {start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}")
    print(f"Pairs: {', '.join(symbols)}")
    print(f"Starting equity: ${args.equity:.2f}")
    print(f"Min confluence: {args.min_confluence}")
    if args.validation or args.compare:
        print("Validation library: ACTIVE (only proven setups)")
    print()

    news_events = None
    if args.news_csv:
        news_events = _load_news_csv(args.news_csv)
        print(f"News blackout: {len(news_events)} high-impact events loaded")

    # Load data from MT5
    print("Loading historical data from MT5...")
    store = HistoricalDataStore(symbols, start, end)
    store.load()
    print()

    if args.compare:
        # Run BOTH modes and compare
        from helix_v3.backtest.report import print_backtest_report

        print("=" * 80)
        print("  RUN 1: BASELINE (no validation filter)")
        print("=" * 80)
        runner_base = BacktestRunner(
            data_store=store,
            initial_equity=args.equity,
            min_confluence=args.min_confluence,
            max_concurrent=args.max_positions,
            verbose=args.verbose,
            slippage_pips=args.slippage * args.slippage_mult,
            commission_per_lot=args.commission,
            use_validation=False,
            news_events=news_events,
        )
        runner_base.run()
        print_backtest_report(runner_base.simulator, start, end)

        print("\n" + "=" * 80)
        print("  RUN 2: VALIDATION LIBRARY ACTIVE (only proven setups)")
        print("=" * 80)
        runner_val = BacktestRunner(
            data_store=store,
            initial_equity=args.equity,
            min_confluence=args.min_confluence,
            max_concurrent=args.max_positions,
            verbose=args.verbose,
            slippage_pips=args.slippage * args.slippage_mult,
            commission_per_lot=args.commission,
            use_validation=True,
            news_events=news_events,
        )
        runner_val.run()
        print_backtest_report(runner_val.simulator, start, end)

        # Comparison summary
        b = runner_base.simulator
        v = runner_val.simulator
        b_trades = len(b.closed_trades)
        v_trades = len(v.closed_trades)
        b_wins = sum(1 for t in b.closed_trades if t.pnl_pips > 0)
        v_wins = sum(1 for t in v.closed_trades if t.pnl_pips > 0)
        b_pips = sum(t.pnl_pips for t in b.closed_trades)
        v_pips = sum(t.pnl_pips for t in v.closed_trades)
        b_wr = b_wins / b_trades * 100 if b_trades else 0
        v_wr = v_wins / v_trades * 100 if v_trades else 0

        print("\n" + "=" * 80)
        print("  COMPARISON: BASELINE vs VALIDATION LIBRARY")
        print("=" * 80)
        print(f"  {'Metric':<25}{'Baseline':>15}{'Validated':>15}{'Delta':>15}")
        print(f"  {'-'*70}")
        print(f"  {'Trades':<25}{b_trades:>15}{v_trades:>15}{v_trades - b_trades:>+15}")
        print(f"  {'Wins':<25}{b_wins:>15}{v_wins:>15}{v_wins - b_wins:>+15}")
        print(f"  {'Win Rate':<25}{b_wr:>14.1f}%{v_wr:>14.1f}%{v_wr - b_wr:>+14.1f}%")
        print(f"  {'Total Pips':<25}{b_pips:>15.1f}{v_pips:>15.1f}{v_pips - b_pips:>+15.1f}")
        print(f"  {'Final Equity':<25}${b.equity:>14.2f}${v.equity:>14.2f}${v.equity - b.equity:>+14.2f}")
        print(f"  {'Validation Matches':<25}{'-':>15}{runner_val._validation_matches:>15}")
        print(f"  {'Validation Blocks':<25}{'-':>15}{runner_val._validation_blocks:>15}")
        print(f"  {'Graveyard Warnings':<25}{'-':>15}{runner_val._graveyard_warnings:>15}")
        print("=" * 80)
        return

    # Single run
    runner = BacktestRunner(
        data_store=store,
        initial_equity=args.equity,
        min_confluence=args.min_confluence,
        max_concurrent=args.max_positions,
        verbose=args.verbose,
        slippage_pips=args.slippage * args.slippage_mult,
        commission_per_lot=args.commission,
        use_validation=args.validation,
        news_events=news_events,
    )
    runner.run()

    # Print report
    from helix_v3.backtest.report import print_backtest_report
    print_backtest_report(runner.simulator, start, end)

    if runner.use_validation:
        print(f"\n  VALIDATION STATS: {runner._validation_matches} matches, "
              f"{runner._validation_blocks} blocks, "
              f"{runner._graveyard_warnings} graveyard warnings")

    if runner._news_calendar is not None:
        print(f"\n  NEWS BLACKOUT: {runner._news_blocks} entry checks blocked")
    if runner._exposure_blocks:
        print(f"\n  CURRENCY EXPOSURE: {runner._exposure_blocks} entries blocked")
    if runner._regime_blocks:
        print(f"\n  REGIME FILTER: {runner._regime_blocks} symbol-bars skipped (MMM conditions absent)")

    # Promotion into the LIVE library is opt-in (Tier 1.3): silently promoting
    # a run's own outcomes built the self-reinforcing loop the audit flagged.
    if _HAS_REPLAY and args.promote:
        try:
            from helix_v3.backtest.validation_library import ValidationLibrary
            lib = ValidationLibrary()
            promoted = lib.promote_from_replay(
                min_total=5, min_favorable_rate=55.0, min_symbols=1,
            )
            records = lib.top_records(limit=5)
            print(f"\n  VALIDATION LIBRARY: promoted {promoted} patterns")
            if records:
                print("  Top proven patterns:")
                for r in records:
                    print(f"    {r.setup_family:<20} {r.symbol or 'CROSS':<8} "
                          f"win={r.favorable_rate:.1f}% n={r.total} "
                          f"target={r.realistic_target_pips or 0:.1f}p")
            lib.close()
        except Exception as e:
            logger.warning("Validation library promotion failed: %s", e)
    elif _HAS_REPLAY:
        print("\n  (Outcomes recorded to replay store; live-library promotion "
              "skipped — pass --promote to opt in.)")


if __name__ == "__main__":
    main()
