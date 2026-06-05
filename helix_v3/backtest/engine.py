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
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from config.pair_profiles import get_pair_profile, PAIR_PROFILES
from config.settings import settings
from helix_v3.backtest.data_store import HistoricalDataStore
from helix_v3.core.mtf_analyzer import MTFAnalyzer, MTFAnalysis
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.tdi import compute_tdi, compute_pivots, compute_adr, compute_daily_hilo
from helix_v3.core.patterns import scan_patterns
from helix_v3.core.types import Direction, QuantSignal, SessionBounds
from helix_v3.utils.logger import get_logger

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
    remaining_lots: float = 0.0
    current_sl: float = 0.0

    def __post_init__(self):
        self.remaining_lots = self.lot_size
        self.current_sl = self.stop_loss


class TradeSimulator:
    """Simulates trade lifecycle bar-by-bar matching live V2 rules."""

    def __init__(self, initial_equity: float = 1000.0) -> None:
        self.equity = initial_equity
        self.peak_equity = initial_equity
        self.open_trades: List[SimulatedTrade] = []
        self.closed_trades: List[SimulatedTrade] = []
        self.equity_curve: List[tuple] = []  # (datetime, equity)

    def open_trade(
        self,
        symbol: str,
        direction: Direction,
        entry_price: float,
        entry_time: datetime,
        sl_price: float,
        pip_size: float,
        pip_value_per_lot: float,
    ) -> Optional[SimulatedTrade]:
        """Open a simulated trade with proper lot sizing."""
        profile = get_pair_profile(symbol)
        sl_pips = abs(entry_price - sl_price) / pip_size

        # Apply SL floor (matching live gatekeeper fix)
        effective_sl = max(sl_pips, profile.min_sl_pips)

        # Lot sizing: Equity * Risk% / (SL_pips * pip_value_per_lot)
        risk_amount = self.equity * profile.max_risk_pct
        if pip_value_per_lot <= 0 or effective_sl <= 0:
            return None

        raw_lot = risk_amount / (effective_sl * pip_value_per_lot)

        # Account-proportional cap (3% hard limit)
        account_max_lot = (self.equity * 0.03) / (effective_sl * pip_value_per_lot)
        lot = min(raw_lot, profile.max_lot_size, account_max_lot)
        lot = max(0.01, round(round(lot / 0.01) * 0.01, 2))

        # TP levels
        risk_dist = abs(entry_price - sl_price)
        if direction == Direction.BUY:
            tp1 = entry_price + risk_dist
            tp2 = entry_price + risk_dist * 2.5
        else:
            tp1 = entry_price - risk_dist
            tp2 = entry_price - risk_dist * 2.5

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
        )
        self.open_trades.append(trade)
        return trade

    def process_bar(self, bar_time: datetime, bars: Dict[str, pd.Series]) -> List[str]:
        """Process one M15 bar for all open trades. Returns action descriptions."""
        actions = []
        still_open = []

        for trade in self.open_trades:
            bar = bars.get(trade.symbol)
            if bar is None:
                still_open.append(trade)
                continue

            high = float(bar["High"])
            low = float(bar["Low"])
            close = float(bar["Close"])
            profile = get_pair_profile(trade.symbol)

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

            # --- Check SL hit ---
            sl_hit = False
            if trade.direction == Direction.BUY and low <= trade.current_sl:
                sl_hit = True
            elif trade.direction == Direction.SELL and high >= trade.current_sl:
                sl_hit = True

            if sl_hit:
                trade.exit_price = trade.current_sl
                trade.exit_time = bar_time
                trade.exit_reason = "SL_HIT"
                trade.status = "CLOSED"
                self._finalize_trade(trade)
                actions.append(f"SL HIT: {trade.symbol} {trade.pnl_pips:+.1f}p")
                self.closed_trades.append(trade)
                continue

            # --- Check TP2 hit ---
            tp2_hit = False
            if trade.direction == Direction.BUY and high >= trade.take_profit_2:
                tp2_hit = True
            elif trade.direction == Direction.SELL and low <= trade.take_profit_2:
                tp2_hit = True

            if tp2_hit:
                trade.exit_price = trade.take_profit_2
                trade.exit_time = bar_time
                trade.exit_reason = "TP2_HIT"
                trade.status = "CLOSED"
                self._finalize_trade(trade)
                actions.append(f"TP2 HIT: {trade.symbol} {trade.pnl_pips:+.1f}p")
                self.closed_trades.append(trade)
                continue

            # --- Max duration exit ---
            if duration_min >= profile.max_duration_minutes:
                trade.exit_price = close
                trade.exit_time = bar_time
                trade.exit_reason = "MAX_DURATION"
                trade.status = "CLOSED"
                self._finalize_trade(trade)
                actions.append(f"TIME EXIT: {trade.symbol} {trade.pnl_pips:+.1f}p")
                self.closed_trades.append(trade)
                continue

            # --- Stale trade (90 min not in profit) ---
            if duration_min >= profile.stale_minutes and profit_pips <= 0:
                trade.exit_price = close
                trade.exit_time = bar_time
                trade.exit_reason = "STALE"
                trade.status = "CLOSED"
                self._finalize_trade(trade)
                actions.append(f"STALE EXIT: {trade.symbol} {trade.pnl_pips:+.1f}p")
                self.closed_trades.append(trade)
                continue

            # --- T1 partial close at 1:1 RR ---
            if not trade.t1_closed:
                t1_hit = False
                if trade.direction == Direction.BUY and high >= trade.take_profit_1:
                    t1_hit = True
                elif trade.direction == Direction.SELL and low <= trade.take_profit_1:
                    t1_hit = True

                if t1_hit:
                    trade.t1_closed = True
                    trade.remaining_lots = round(trade.lot_size * 0.5, 2)
                    trade.current_sl = trade.entry_price  # SL to breakeven
                    trade.status = "T1_HIT"
                    actions.append(f"T1 HIT: {trade.symbol} +{fav:.1f}p, SL->BE")

            # --- Trailing stop (after T1) ---
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

        # Record equity snapshot
        unrealized = sum(self._unrealized_pnl(t) for t in self.open_trades)
        self.equity_curve.append((bar_time, self.equity + unrealized))

        return actions

    def _finalize_trade(self, trade: SimulatedTrade) -> None:
        """Calculate final P&L and update equity."""
        if trade.direction == Direction.BUY:
            trade.pnl_pips = (trade.exit_price - trade.entry_price) / trade.pip_size
        else:
            trade.pnl_pips = (trade.entry_price - trade.exit_price) / trade.pip_size

        # Simplified P&L: pips * lot * pip_value_per_lot (approximate)
        # For accuracy we'd need tick_value, but this is a reasonable approximation
        profile = get_pair_profile(trade.symbol)
        risk_per_pip = (self.equity * profile.max_risk_pct) / trade.sl_pips if trade.sl_pips > 0 else 0
        trade.pnl_dollars = trade.pnl_pips * (risk_per_pip / trade.sl_pips) * trade.sl_pips if trade.sl_pips > 0 else 0

        # Simpler: use risk amount as the unit
        # If SL hit: lose risk_amount. If TP2 hit: win risk_amount * RR
        risk_amount = self.equity * profile.max_risk_pct
        if trade.sl_pips > 0:
            trade.pnl_dollars = (trade.pnl_pips / trade.sl_pips) * risk_amount

        self.equity += trade.pnl_dollars
        self.peak_equity = max(self.peak_equity, self.equity)

    def _unrealized_pnl(self, trade: SimulatedTrade) -> float:
        """Rough unrealized P&L estimate for equity curve."""
        return 0.0  # Conservative: don't count unrealized

    def has_open_position(self, symbol: str) -> bool:
        return any(t.symbol == symbol for t in self.open_trades)

    def has_open_direction(self, symbol: str, direction: Direction) -> bool:
        return any(
            t.symbol == symbol and t.direction == direction
            for t in self.open_trades
        )

    @property
    def max_drawdown_pct(self) -> float:
        if self.peak_equity <= 0:
            return 0.0
        return (self.peak_equity - self.equity) / self.peak_equity


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
    ) -> None:
        self.data_store = data_store
        self.engine = BacktestEngine(data_store)
        self.mtf = MTFAnalyzer(self.engine)
        self.simulator = TradeSimulator(initial_equity)
        self.min_confluence = min_confluence
        self.max_concurrent = max_concurrent
        self.verbose = verbose
        # In-memory re-entry guard for speed
        self._loss_cooldowns: Dict[str, datetime] = {}  # "SYMBOL_DIR" -> cooldown_until
        self._loss_counts: Dict[str, int] = {}  # "SYMBOL_DIR" -> consecutive losses
        self._day_bans: Dict[str, str] = {}  # "SYMBOL_DIR" -> ban_date
        # Entry cooldown: block re-entry on same symbol for 2 hours after ANY exit
        self._entry_cooldowns: Dict[str, datetime] = {}  # "SYMBOL" -> cooldown_until

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
            self.engine.set_current_time(dt)

            # Get M15 bars for all symbols at this timestamp
            current_bars: Dict[str, pd.Series] = {}
            for sym in symbols:
                df = self.data_store.get_rates(sym, "M15", dt, 1)
                if not df.empty and df.index[-1] == bar_time:
                    current_bars[sym] = df.iloc[-1]

            # Manage open trades first
            actions = self.simulator.process_bar(dt, current_bars)
            for action in actions:
                if self.verbose:
                    logger.info("[%s] %s", dt.strftime("%m-%d %H:%M"), action)
                # Entry cooldown after ANY exit (prevents same-setup churn)
                self._record_exit(action, dt)
                # Additional loss-specific guard
                if "SL HIT" in action or "STALE EXIT" in action:
                    self._record_loss(action, dt)

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
                    self._check_entry(sym, dt)
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
        for trade in list(self.simulator.open_trades):
            last_bar = current_bars.get(trade.symbol)
            if last_bar is not None:
                trade.exit_price = float(last_bar["Close"])
            else:
                trade.exit_price = trade.entry_price
            trade.exit_time = sorted_times[-1].to_pydatetime().replace(tzinfo=timezone.utc)
            trade.exit_reason = "BACKTEST_END"
            trade.status = "CLOSED"
            self.simulator._finalize_trade(trade)
            self.simulator.closed_trades.append(trade)
        self.simulator.open_trades.clear()

        logger.info(
            "Backtest complete: %d trades, equity $%.2f -> $%.2f",
            len(self.simulator.closed_trades),
            self.simulator.equity_curve[0][1] if self.simulator.equity_curve else 0,
            self.simulator.equity,
        )

    def _check_entry(self, symbol: str, bar_time: datetime) -> None:
        """Run MTF analysis and check entry conditions for one symbol."""
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

        # Get entry price from M15 bar
        df_m15 = self.data_store.get_rates(symbol, "M15", bar_time, 1)
        if df_m15.empty:
            return

        bar = df_m15.iloc[-1]
        pip_size = self.data_store.get_pip_size(symbol)
        profile = get_pair_profile(symbol)

        # Simulate spread (half spread on each side)
        spread_pips = profile.max_spread_pips * 0.5  # Use half of max as typical
        spread = spread_pips * pip_size

        if direction == Direction.BUY:
            entry_price = float(bar["Close"]) + spread / 2
        else:
            entry_price = float(bar["Close"]) - spread / 2

        # SL from session bounds (Asian range)
        if analysis.fifteen_min.asian_range_low and analysis.fifteen_min.asian_range_high:
            buffer = profile.sl_buffer_pips * pip_size
            if direction == Direction.BUY:
                sl_price = analysis.fifteen_min.asian_range_low - buffer
            else:
                sl_price = analysis.fifteen_min.asian_range_high + buffer
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

        trade = self.simulator.open_trade(
            symbol=symbol,
            direction=direction,
            entry_price=entry_price,
            entry_time=bar_time,
            sl_price=sl_price,
            pip_size=pip_size,
            pip_value_per_lot=pip_value_per_lot,
        )

        if trade and self.verbose:
            logger.info(
                "[%s] ENTRY: %s %s %.2fL @ %.5f SL=%.5f conf=%d",
                bar_time.strftime("%m-%d %H:%M"),
                direction.value, symbol, trade.lot_size,
                entry_price, sl_price, analysis.confluence_score,
            )

    def _record_exit(self, action: str, bar_time: datetime) -> None:
        """Set entry cooldown after ANY trade exit (prevents same-setup churn)."""
        parts = action.split(":")
        if len(parts) < 2:
            return
        symbol = parts[1].strip().split()[0]
        # 2 hour entry cooldown on the symbol after any exit
        self._entry_cooldowns[symbol] = bar_time + timedelta(hours=2)

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

def main(argv: Optional[list] = None) -> None:
    parser = argparse.ArgumentParser(description="Helix V3 MMM Strategy Backtester")
    parser.add_argument("--days", type=int, default=14, help="Days to backtest (from today)")
    parser.add_argument("--start", type=str, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, help="End date (YYYY-MM-DD)")
    parser.add_argument("--pairs", type=str, help="Comma-separated pairs (default: all 13)")
    parser.add_argument("--equity", type=float, default=1000.0, help="Starting equity")
    parser.add_argument("--min-confluence", type=int, default=50, help="Min confluence score")
    parser.add_argument("--max-positions", type=int, default=3, help="Max concurrent positions")
    parser.add_argument("--verbose", "-v", action="store_true", help="Detailed trade logging")
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
        symbols = list(PAIR_PROFILES.keys())

    print(f"\nHelix V3 Backtest: {start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}")
    print(f"Pairs: {', '.join(symbols)}")
    print(f"Starting equity: ${args.equity:.2f}")
    print(f"Min confluence: {args.min_confluence}")
    print()

    # Load data from MT5
    print("Loading historical data from MT5...")
    store = HistoricalDataStore(symbols, start, end)
    store.load()
    print()

    # Run backtest
    runner = BacktestRunner(
        data_store=store,
        initial_equity=args.equity,
        min_confluence=args.min_confluence,
        max_concurrent=args.max_positions,
        verbose=args.verbose,
    )
    runner.run()

    # Print report
    from helix_v3.backtest.report import print_backtest_report
    print_backtest_report(runner.simulator, start, end)


if __name__ == "__main__":
    main()
