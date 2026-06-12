"""TradeJournal - Persistent trade logging and performance analytics.

Records every trade with full context: setup type, pre-entry bias, quant signals,
vision verdicts, entry/exit prices, pips, pip value, lot sizing, P&L, duration,
and outcome classification.

Uses SQLite for zero-config local persistence.
"""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from config.settings import settings
from helix_v3.core.types import (
    ConsensusResult,
    ExecutionOrder,
    QuantSignal,
)
from helix_v3.utils.logger import get_logger

logger = get_logger("trade_journal")

DB_PATH = Path(settings.log_dir) / "trade_journal.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS trades (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,

    -- Identification
    ticket          INTEGER UNIQUE,
    symbol          TEXT NOT NULL,
    timeframe       TEXT NOT NULL,
    direction       TEXT NOT NULL,
    setup_type      TEXT NOT NULL DEFAULT 'MMM',

    -- Pre-Entry Context
    bias_direction      TEXT,
    bias_confidence     REAL,
    cycle_level         INTEGER,
    accumulation_active INTEGER,
    stop_hunt_detected  INTEGER,
    stop_hunt_dir       TEXT,
    stop_hunt_breach    REAL,
    stop_hunt_zscore    REAL,
    ema_trend           TEXT,
    ema_5_angle         REAL,
    ema_13_angle        REAL,
    ema_50_angle        REAL,
    ema_200_angle       REAL,
    ema_800_angle       REAL,
    fast_slow_divergence REAL,
    session_high        REAL,
    session_low         REAL,
    session_range_pips  REAL,
    vol_compression     REAL,

    -- Vision Consensus
    consensus_mode      TEXT,
    consensus_agreed    INTEGER,
    vision_model_1      TEXT,
    vision_dir_1        TEXT,
    vision_conf_1       REAL,
    vision_m_w_1        INTEGER,
    vision_rrt_1        INTEGER,
    vision_pin_1        INTEGER,
    vision_model_2      TEXT,
    vision_dir_2        TEXT,
    vision_conf_2       REAL,
    vision_m_w_2        INTEGER,
    vision_rrt_2        INTEGER,
    vision_pin_2        INTEGER,
    avg_confidence      REAL,

    -- Order Details
    lot_size        REAL NOT NULL,
    entry_price     REAL NOT NULL,
    stop_loss       REAL NOT NULL,
    take_profit_1   REAL NOT NULL,
    take_profit_2   REAL NOT NULL,
    sl_pips         REAL NOT NULL,
    risk_reward     REAL NOT NULL,
    pip_value       REAL,
    risk_amount     REAL,
    spread_at_entry REAL,

    -- Execution Timestamps
    opened_at       TEXT NOT NULL,
    closed_at       TEXT,
    duration_minutes REAL,

    -- Exit Details
    exit_price      REAL,
    exit_reason     TEXT,
    pips_gained     REAL,
    gross_profit    REAL,
    commission      REAL DEFAULT 0,
    swap            REAL DEFAULT 0,
    net_profit      REAL,

    -- Partial Closes
    t1_hit          INTEGER DEFAULT 0,
    t1_close_price  REAL,
    t1_close_lots   REAL,
    t1_pips         REAL,
    t1_profit       REAL,
    t1_hit_at       TEXT,

    -- Outcome
    outcome         TEXT,
    equity_before   REAL,
    equity_after    REAL,
    drawdown_at_entry REAL,

    -- Chart Reference
    chart_path      TEXT,

    -- Tags / Notes
    tags            TEXT,
    notes           TEXT,

    -- Metadata
    created_at      TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_trades_symbol ON trades(symbol);
CREATE INDEX IF NOT EXISTS idx_trades_opened ON trades(opened_at);
CREATE INDEX IF NOT EXISTS idx_trades_outcome ON trades(outcome);
CREATE INDEX IF NOT EXISTS idx_trades_ticket ON trades(ticket);

CREATE TABLE IF NOT EXISTS trade_updates (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    trade_id    INTEGER NOT NULL REFERENCES trades(id),
    field       TEXT NOT NULL,
    old_value   TEXT,
    new_value   TEXT,
    updated_at  TEXT NOT NULL DEFAULT (datetime('now'))
);
"""


class TradeJournal:
    """Persistent trade journal backed by SQLite.

    Records full lifecycle of each trade:
    - Entry: quant signals, vision verdicts, order parameters
    - Management: T1 partial close, SL modifications
    - Exit: close price, pips, P&L, outcome classification
    - Analytics: win rate, avg RR, Sharpe, drawdown, per-setup stats
    """

    def __init__(self, db_path: Optional[Path] = None) -> None:
        self._db_path = db_path or DB_PATH
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self._db_path))
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.executescript(SCHEMA)
        self._conn.commit()
        logger.info("Trade journal initialized: %s", self._db_path)

    def close(self) -> None:
        self._conn.close()

    # ------------------------------------------------------------------
    # Record Entry
    # ------------------------------------------------------------------

    def record_entry(
        self,
        order: ExecutionOrder,
        signal: QuantSignal,
        consensus: ConsensusResult,
        consensus_mode: str = "local",
        equity_before: Optional[float] = None,
        spread_at_entry: Optional[float] = None,
        pip_value: Optional[float] = None,
        chart_path: Optional[str] = None,
        tags: Optional[List[str]] = None,
        notes: Optional[str] = None,
    ) -> int:
        """Record a new trade entry with full context. Returns trade ID."""

        # Unpack vision verdicts
        v1 = consensus.verdicts[0] if len(consensus.verdicts) > 0 else None
        v2 = consensus.verdicts[1] if len(consensus.verdicts) > 1 else None

        risk_amount = None
        if equity_before and settings.risk.max_risk_per_trade:
            risk_amount = equity_before * settings.risk.max_risk_per_trade

        drawdown = None
        if equity_before:
            try:
                import MetaTrader5 as mt5
                bal = mt5.account_info()
                if bal:
                    drawdown = (bal.balance - equity_before) / bal.balance if bal.balance > 0 else 0
            except Exception:
                pass

        cursor = self._conn.execute(
            """INSERT INTO trades (
                ticket, symbol, timeframe, direction, setup_type,
                bias_direction, bias_confidence, cycle_level,
                accumulation_active, stop_hunt_detected,
                stop_hunt_dir, stop_hunt_breach, stop_hunt_zscore,
                ema_trend, ema_5_angle, ema_13_angle, ema_50_angle,
                ema_200_angle, ema_800_angle, fast_slow_divergence,
                session_high, session_low, session_range_pips, vol_compression,
                consensus_mode, consensus_agreed,
                vision_model_1, vision_dir_1, vision_conf_1,
                vision_m_w_1, vision_rrt_1, vision_pin_1,
                vision_model_2, vision_dir_2, vision_conf_2,
                vision_m_w_2, vision_rrt_2, vision_pin_2,
                avg_confidence,
                lot_size, entry_price, stop_loss, take_profit_1, take_profit_2,
                sl_pips, risk_reward, pip_value, risk_amount,
                spread_at_entry, opened_at, equity_before, drawdown_at_entry,
                chart_path, tags, notes
            ) VALUES (
                ?, ?, ?, ?, ?,
                ?, ?, ?,
                ?, ?,
                ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?,
                ?, ?, ?,
                ?, ?, ?,
                ?, ?, ?,
                ?, ?, ?,
                ?,
                ?, ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?
            )""",
            (
                order.ticket,
                order.symbol,
                signal.timeframe,
                order.direction.value,
                "MMM",
                # Pre-entry bias
                consensus.direction.value,
                consensus.avg_confidence,
                v1.cycle_level.value if v1 and v1.cycle_level else None,
                int(signal.accumulation_active),
                int(signal.stop_hunt_detected),
                signal.stop_hunt.direction.value if signal.stop_hunt else None,
                signal.stop_hunt.breach_pips if signal.stop_hunt else None,
                signal.stop_hunt.z_score if signal.stop_hunt else None,
                # EMA context
                signal.ema_vector.trend_alignment.value,
                signal.ema_vector.ema_5_angle,
                signal.ema_vector.ema_13_angle,
                signal.ema_vector.ema_50_angle,
                signal.ema_vector.ema_200_angle,
                signal.ema_vector.ema_800_angle,
                signal.ema_vector.fast_slow_divergence,
                # Session
                signal.session_bounds.high if signal.session_bounds else None,
                signal.session_bounds.low if signal.session_bounds else None,
                signal.session_bounds.range_pips if signal.session_bounds else None,
                signal.session_bounds.volatility_compression if signal.session_bounds else None,
                # Consensus
                consensus_mode,
                int(consensus.agreed),
                v1.model_name if v1 else None,
                v1.direction.value if v1 else None,
                v1.confidence if v1 else None,
                int(v1.m_w_detected) if v1 else None,
                int(v1.rrt_detected) if v1 else None,
                int(v1.pin_bar_detected) if v1 else None,
                v2.model_name if v2 else None,
                v2.direction.value if v2 else None,
                v2.confidence if v2 else None,
                int(v2.m_w_detected) if v2 else None,
                int(v2.rrt_detected) if v2 else None,
                int(v2.pin_bar_detected) if v2 else None,
                consensus.avg_confidence,
                # Order
                order.lot_size,
                order.entry_price,
                order.stop_loss,
                order.take_profit_1,
                order.take_profit_2,
                order.sl_pips,
                order.risk_reward,
                pip_value,
                risk_amount,
                spread_at_entry,
                datetime.now(timezone.utc).isoformat(),
                equity_before,
                drawdown,
                chart_path,
                json.dumps(tags) if tags else None,
                notes,
            ),
        )
        self._conn.commit()
        trade_id = cursor.lastrowid

        logger.info(
            "JOURNAL ENTRY #%d: %s %s %s %.2f lots @ %.5f SL=%.1f pips",
            trade_id, order.direction.value, order.symbol,
            signal.timeframe, order.lot_size, order.entry_price, order.sl_pips,
        )
        return trade_id

    # ------------------------------------------------------------------
    # Record T1 Partial Close
    # ------------------------------------------------------------------

    def record_t1_hit(
        self,
        ticket: int,
        close_price: float,
        close_lots: float,
        pips: float,
        profit: float,
    ) -> None:
        self._conn.execute(
            """UPDATE trades SET
                t1_hit = 1, t1_close_price = ?, t1_close_lots = ?,
                t1_pips = ?, t1_profit = ?, t1_hit_at = ?,
                updated_at = ?
            WHERE ticket = ?""",
            (
                close_price, close_lots, pips, profit,
                datetime.now(timezone.utc).isoformat(),
                datetime.now(timezone.utc).isoformat(),
                ticket,
            ),
        )
        self._conn.commit()
        logger.info("JOURNAL T1 HIT: ticket=%d pips=%.1f profit=%.2f", ticket, pips, profit)

    # ------------------------------------------------------------------
    # Record Exit
    # ------------------------------------------------------------------

    def record_exit(
        self,
        ticket: int,
        exit_price: float,
        exit_reason: str,
        pips_gained: float,
        gross_profit: float,
        commission: float = 0.0,
        swap: float = 0.0,
        equity_after: Optional[float] = None,
    ) -> None:
        net_profit = gross_profit - commission + swap

        # Calculate duration
        row = self._conn.execute(
            "SELECT opened_at FROM trades WHERE ticket = ?", (ticket,)
        ).fetchone()

        duration = None
        if row and row["opened_at"]:
            opened = datetime.fromisoformat(row["opened_at"])
            duration = (datetime.now(timezone.utc) - opened).total_seconds() / 60

        # Classify outcome
        if pips_gained > 0:
            outcome = "WIN"
        elif pips_gained == 0:
            outcome = "BREAKEVEN"
        else:
            outcome = "LOSS"

        self._conn.execute(
            """UPDATE trades SET
                exit_price = ?, exit_reason = ?, pips_gained = ?,
                gross_profit = ?, commission = ?, swap = ?, net_profit = ?,
                closed_at = ?, duration_minutes = ?,
                outcome = ?, equity_after = ?, updated_at = ?
            WHERE ticket = ?""",
            (
                exit_price, exit_reason, pips_gained,
                gross_profit, commission, swap, net_profit,
                datetime.now(timezone.utc).isoformat(), duration,
                outcome, equity_after,
                datetime.now(timezone.utc).isoformat(),
                ticket,
            ),
        )
        self._conn.commit()
        logger.info(
            "JOURNAL EXIT: ticket=%d %s pips=%.1f net=%.2f %s (%.0f min)",
            ticket, exit_reason, pips_gained, net_profit, outcome, duration or 0,
        )

    # ------------------------------------------------------------------
    # Sync from MT5 (update open trades, detect closes)
    # ------------------------------------------------------------------

    def sync_from_mt5(self) -> Dict[str, int]:
        """Sync journal with MT5 positions and deal history.

        - Updates P&L on open trades
        - Detects and records closed trades from MT5 deal history
        Returns dict with counts of actions taken.
        """
        import MetaTrader5 as mt5

        stats = {"updated": 0, "closed": 0}

        # Get all open journal trades without exit
        open_trades = self._conn.execute(
            "SELECT id, ticket, symbol, direction, entry_price, lot_size "
            "FROM trades WHERE closed_at IS NULL AND ticket IS NOT NULL"
        ).fetchall()

        open_tickets = {row["ticket"] for row in open_trades}

        # Check which are still open in MT5
        positions = mt5.positions_get()
        mt5_open_tickets = set()
        if positions:
            for pos in positions:
                if pos.magic == 314159 and pos.ticket in open_tickets:
                    mt5_open_tickets.add(pos.ticket)

        # Trades that were open in journal but no longer in MT5 = closed
        closed_tickets = open_tickets - mt5_open_tickets

        for ticket in closed_tickets:
            # Fetch deal history for this position
            deals = mt5.history_deals_get(position=ticket)
            if not deals or len(deals) < 2:
                continue

            # The closing deal is the last one
            close_deal = deals[-1]

            row = self._conn.execute(
                "SELECT direction, entry_price, lot_size, symbol FROM trades WHERE ticket = ?",
                (ticket,),
            ).fetchone()

            if not row:
                continue

            direction = row["direction"]
            entry = row["entry_price"]
            symbol = row["symbol"]

            exit_price = close_deal.price
            pip_size_info = mt5.symbol_info(symbol)
            if pip_size_info:
                point = pip_size_info.point
                pip_size = point * 10 if pip_size_info.digits in (3, 5) else point
            else:
                pip_size = 0.0001

            if direction == "BUY":
                pips = (exit_price - entry) / pip_size
            else:
                pips = (entry - exit_price) / pip_size

            gross = close_deal.profit
            commission = close_deal.commission
            swap_val = close_deal.swap

            reason = "SL" if close_deal.comment and "sl" in close_deal.comment.lower() else \
                     "TP" if close_deal.comment and "tp" in close_deal.comment.lower() else \
                     "MANUAL"

            info = mt5.account_info()
            eq_after = info.equity if info else None

            self.record_exit(
                ticket=ticket,
                exit_price=exit_price,
                exit_reason=reason,
                pips_gained=pips,
                gross_profit=gross,
                commission=commission,
                swap=swap_val,
                equity_after=eq_after,
            )
            stats["closed"] += 1

        return stats

    # ------------------------------------------------------------------
    # Queries & Analytics
    # ------------------------------------------------------------------

    def get_trade(self, ticket: int) -> Optional[Dict[str, Any]]:
        row = self._conn.execute(
            "SELECT * FROM trades WHERE ticket = ?", (ticket,)
        ).fetchone()
        return dict(row) if row else None

    def get_open_trades(self) -> List[Dict[str, Any]]:
        rows = self._conn.execute(
            "SELECT * FROM trades WHERE closed_at IS NULL ORDER BY opened_at DESC"
        ).fetchall()
        return [dict(r) for r in rows]

    def get_closed_trades(self, limit: int = 50) -> List[Dict[str, Any]]:
        rows = self._conn.execute(
            "SELECT * FROM trades WHERE closed_at IS NOT NULL ORDER BY closed_at DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [dict(r) for r in rows]

    def get_all_trades(self, limit: int = 100) -> List[Dict[str, Any]]:
        rows = self._conn.execute(
            "SELECT * FROM trades ORDER BY opened_at DESC LIMIT ?", (limit,)
        ).fetchall()
        return [dict(r) for r in rows]

    def get_trades_by_symbol(self, symbol: str) -> List[Dict[str, Any]]:
        rows = self._conn.execute(
            "SELECT * FROM trades WHERE symbol = ? ORDER BY opened_at DESC", (symbol,)
        ).fetchall()
        return [dict(r) for r in rows]

    def get_trades_by_setup(self, setup_type: str) -> List[Dict[str, Any]]:
        rows = self._conn.execute(
            "SELECT * FROM trades WHERE setup_type = ? ORDER BY opened_at DESC",
            (setup_type,),
        ).fetchall()
        return [dict(r) for r in rows]

    # ------------------------------------------------------------------
    # Performance Analytics
    # ------------------------------------------------------------------

    def get_performance_summary(self) -> Dict[str, Any]:
        """Comprehensive performance report across all closed trades."""
        rows = self._conn.execute(
            "SELECT * FROM trades WHERE closed_at IS NOT NULL"
        ).fetchall()

        if not rows:
            return {"total_trades": 0, "message": "No closed trades yet"}

        trades = [dict(r) for r in rows]
        total = len(trades)
        wins = [t for t in trades if t["outcome"] == "WIN"]
        losses = [t for t in trades if t["outcome"] == "LOSS"]
        breakevens = [t for t in trades if t["outcome"] == "BREAKEVEN"]

        all_pips = [t["pips_gained"] or 0 for t in trades]
        all_profits = [t["net_profit"] or 0 for t in trades]
        win_pips = [t["pips_gained"] or 0 for t in wins]
        loss_pips = [abs(t["pips_gained"] or 0) for t in losses]

        avg_win_pips = sum(win_pips) / len(win_pips) if win_pips else 0
        avg_loss_pips = sum(loss_pips) / len(loss_pips) if loss_pips else 0

        # Profit factor
        gross_wins = sum(t["net_profit"] or 0 for t in wins)
        gross_losses = abs(sum(t["net_profit"] or 0 for t in losses))
        profit_factor = gross_wins / gross_losses if gross_losses > 0 else float("inf")

        # Sharpe-like ratio (simplified)
        import statistics
        avg_return = statistics.mean(all_profits) if all_profits else 0
        std_return = statistics.stdev(all_profits) if len(all_profits) > 1 else 1
        sharpe = (avg_return / std_return) if std_return > 0 else 0

        # Max drawdown in pips
        cumulative = []
        running = 0
        peak = 0
        max_dd = 0
        for p in all_pips:
            running += p
            cumulative.append(running)
            peak = max(peak, running)
            dd = peak - running
            max_dd = max(max_dd, dd)

        # Per-symbol breakdown
        symbols = set(t["symbol"] for t in trades)
        by_symbol = {}
        for sym in symbols:
            sym_trades = [t for t in trades if t["symbol"] == sym]
            sym_wins = [t for t in sym_trades if t["outcome"] == "WIN"]
            by_symbol[sym] = {
                "trades": len(sym_trades),
                "win_rate": len(sym_wins) / len(sym_trades) * 100 if sym_trades else 0,
                "total_pips": sum(t["pips_gained"] or 0 for t in sym_trades),
                "net_profit": sum(t["net_profit"] or 0 for t in sym_trades),
            }

        # Per-cycle-level breakdown
        cycle_stats = {}
        for lvl in [1, 2, 3]:
            lvl_trades = [t for t in trades if t["cycle_level"] == lvl]
            if lvl_trades:
                lvl_wins = [t for t in lvl_trades if t["outcome"] == "WIN"]
                cycle_stats[f"level_{lvl}"] = {
                    "trades": len(lvl_trades),
                    "win_rate": len(lvl_wins) / len(lvl_trades) * 100,
                    "total_pips": sum(t["pips_gained"] or 0 for t in lvl_trades),
                }

        # Average duration
        durations = [t["duration_minutes"] for t in trades if t["duration_minutes"]]
        avg_duration = sum(durations) / len(durations) if durations else 0

        return {
            "total_trades": total,
            "wins": len(wins),
            "losses": len(losses),
            "breakevens": len(breakevens),
            "win_rate_pct": len(wins) / total * 100 if total else 0,
            "total_pips": sum(all_pips),
            "avg_pips_per_trade": sum(all_pips) / total if total else 0,
            "avg_win_pips": avg_win_pips,
            "avg_loss_pips": avg_loss_pips,
            "avg_rr_achieved": avg_win_pips / avg_loss_pips if avg_loss_pips > 0 else 0,
            "total_net_profit": sum(all_profits),
            "profit_factor": profit_factor,
            "sharpe_ratio": sharpe,
            "max_drawdown_pips": max_dd,
            "avg_duration_minutes": avg_duration,
            "best_trade_pips": max(all_pips) if all_pips else 0,
            "worst_trade_pips": min(all_pips) if all_pips else 0,
            "t1_hit_rate_pct": sum(1 for t in trades if t["t1_hit"]) / total * 100 if total else 0,
            "by_symbol": by_symbol,
            "by_cycle_level": cycle_stats,
        }

    def print_summary(self) -> str:
        """Return a formatted performance summary string."""
        s = self.get_performance_summary()
        if s["total_trades"] == 0:
            return "No closed trades recorded yet."

        lines = [
            "",
            "=" * 65,
            "  HELIX V3 TRADE JOURNAL - PERFORMANCE SUMMARY",
            "=" * 65,
            "",
            f"  Total Trades:      {s['total_trades']}",
            f"  Wins / Losses / BE:{s['wins']} / {s['losses']} / {s['breakevens']}",
            f"  Win Rate:          {s['win_rate_pct']:.1f}%",
            f"  T1 Hit Rate:       {s['t1_hit_rate_pct']:.1f}%",
            "",
            f"  Total Pips:        {s['total_pips']:+.1f}",
            f"  Avg Pips/Trade:    {s['avg_pips_per_trade']:+.1f}",
            f"  Avg Win:           {s['avg_win_pips']:.1f} pips",
            f"  Avg Loss:          {s['avg_loss_pips']:.1f} pips",
            f"  Avg RR Achieved:   {s['avg_rr_achieved']:.2f}",
            "",
            f"  Net Profit:        ${s['total_net_profit']:+.2f}",
            f"  Profit Factor:     {s['profit_factor']:.2f}",
            f"  Sharpe Ratio:      {s['sharpe_ratio']:.2f}",
            f"  Max DD (pips):     {s['max_drawdown_pips']:.1f}",
            "",
            f"  Best Trade:        {s['best_trade_pips']:+.1f} pips",
            f"  Worst Trade:       {s['worst_trade_pips']:+.1f} pips",
            f"  Avg Duration:      {s['avg_duration_minutes']:.0f} min",
            "",
            "  --- By Symbol ---",
        ]

        for sym, data in s["by_symbol"].items():
            lines.append(
                f"  {sym:8s}: {data['trades']:3d} trades | "
                f"WR={data['win_rate']:.0f}% | "
                f"{data['total_pips']:+.1f} pips | "
                f"${data['net_profit']:+.2f}"
            )

        if s["by_cycle_level"]:
            lines.append("")
            lines.append("  --- By Cycle Level ---")
            for lvl, data in s["by_cycle_level"].items():
                lines.append(
                    f"  {lvl:10s}: {data['trades']:3d} trades | "
                    f"WR={data['win_rate']:.0f}% | "
                    f"{data['total_pips']:+.1f} pips"
                )

        lines.append("")
        lines.append("=" * 65)

        output = "\n".join(lines)
        return output

    # ------------------------------------------------------------------
    # Period-Based Reports
    # ------------------------------------------------------------------

    def get_period_stats(
        self, since: str, until: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get performance stats for trades closed within a time range.

        Args:
            since: ISO datetime string (UTC) for period start.
            until: ISO datetime string (UTC) for period end. Defaults to now.
        """
        if until is None:
            until = datetime.now(timezone.utc).isoformat()

        rows = self._conn.execute(
            "SELECT * FROM trades WHERE closed_at IS NOT NULL AND closed_at >= ? AND closed_at <= ?",
            (since, until),
        ).fetchall()

        trades = [dict(r) for r in rows]
        total = len(trades)

        if total == 0:
            return {
                "total_trades": 0,
                "wins": 0, "losses": 0, "breakevens": 0,
                "win_rate": 0, "total_pips": 0, "net_profit": 0,
                "profit_factor": 0, "max_drawdown_pips": 0,
                "avg_duration_minutes": 0, "t1_hit_count": 0,
                "best_trade": None, "worst_trade": None,
                "by_symbol": {}, "winning_setups": [],
                "equity_start": 0, "equity_end": 0,
            }

        wins = [t for t in trades if t["outcome"] == "WIN"]
        losses = [t for t in trades if t["outcome"] == "LOSS"]
        breakevens = [t for t in trades if t["outcome"] == "BREAKEVEN"]

        all_pips = [t["pips_gained"] or 0 for t in trades]
        all_profits = [t["net_profit"] or 0 for t in trades]

        gross_wins = sum(t["net_profit"] or 0 for t in wins)
        gross_losses = abs(sum(t["net_profit"] or 0 for t in losses))
        pf = gross_wins / gross_losses if gross_losses > 0 else float("inf")

        # Max drawdown
        running = 0.0
        peak = 0.0
        max_dd = 0.0
        for p in all_pips:
            running += p
            peak = max(peak, running)
            max_dd = max(max_dd, peak - running)

        # Durations
        durations = [t["duration_minutes"] for t in trades if t["duration_minutes"]]
        avg_dur = sum(durations) / len(durations) if durations else 0

        # Best / worst
        best = max(trades, key=lambda t: t["pips_gained"] or -9999)
        worst = min(trades, key=lambda t: t["pips_gained"] or 9999)

        # By symbol
        symbols = set(t["symbol"] for t in trades)
        by_symbol = {}
        for sym in symbols:
            st = [t for t in trades if t["symbol"] == sym]
            sw = [t for t in st if t["outcome"] == "WIN"]
            by_symbol[sym] = {
                "trades": len(st),
                "win_rate": len(sw) / len(st) * 100 if st else 0,
                "total_pips": sum(t["pips_gained"] or 0 for t in st),
                "net_profit": sum(t["net_profit"] or 0 for t in st),
            }

        # Winning setups: group by (cycle_level, bias_direction)
        setup_groups: Dict[str, Dict] = {}
        for t in trades:
            key = f"L{t.get('cycle_level', '?')}_{t.get('bias_direction', '?')}"
            if key not in setup_groups:
                setup_groups[key] = {"total": 0, "wins": 0, "cycle_level": t.get("cycle_level"), "bias": t.get("bias_direction")}
            setup_groups[key]["total"] += 1
            if t["outcome"] == "WIN":
                setup_groups[key]["wins"] += 1

        winning_setups = []
        for _key, data in setup_groups.items():
            data["win_rate"] = data["wins"] / data["total"] * 100 if data["total"] else 0
            winning_setups.append(data)
        winning_setups.sort(key=lambda x: x["win_rate"], reverse=True)

        # Equity
        eq_start = trades[0].get("equity_before") if trades else 0
        eq_end = trades[-1].get("equity_after") if trades else 0

        return {
            "total_trades": total,
            "wins": len(wins),
            "losses": len(losses),
            "breakevens": len(breakevens),
            "win_rate": len(wins) / total * 100 if total else 0,
            "total_pips": sum(all_pips),
            "net_profit": sum(all_profits),
            "profit_factor": pf,
            "max_drawdown_pips": max_dd,
            "avg_duration_minutes": avg_dur,
            "t1_hit_count": sum(1 for t in trades if t["t1_hit"]),
            "best_trade": best,
            "worst_trade": worst,
            "by_symbol": by_symbol,
            "winning_setups": winning_setups,
            "equity_start": eq_start or 0,
            "equity_end": eq_end or 0,
        }

    def get_session_stats(self) -> Dict[str, Any]:
        """Stats for the current trading session (since last Asian open, 00:00 EAT)."""
        from datetime import timedelta
        eat = timezone(timedelta(hours=3))
        now_eat = datetime.now(eat)
        # Session start: today at 00:00 EAT
        session_start = now_eat.replace(hour=0, minute=0, second=0, microsecond=0)
        since_utc = session_start.astimezone(timezone.utc).isoformat()
        return self.get_period_stats(since_utc)

    def get_daily_stats(self, date: Optional[str] = None) -> Dict[str, Any]:
        """Stats for a specific day (default: today). Date format: YYYY-MM-DD."""
        from datetime import timedelta
        eat = timezone(timedelta(hours=3))
        if date:
            day = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=eat)
        else:
            day = datetime.now(eat).replace(hour=0, minute=0, second=0, microsecond=0)
        end = day + timedelta(days=1)
        return self.get_period_stats(
            day.astimezone(timezone.utc).isoformat(),
            end.astimezone(timezone.utc).isoformat(),
        )

    def get_weekly_stats(self) -> Dict[str, Any]:
        """Stats for the current week (Monday to now)."""
        from datetime import timedelta
        eat = timezone(timedelta(hours=3))
        now = datetime.now(eat)
        monday = (now - timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
        return self.get_period_stats(monday.astimezone(timezone.utc).isoformat())

    def get_monthly_stats(self) -> Dict[str, Any]:
        """Stats for the current month."""
        from datetime import timedelta
        eat = timezone(timedelta(hours=3))
        now = datetime.now(eat)
        month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        return self.get_period_stats(month_start.astimezone(timezone.utc).isoformat())

    def print_trade_log(self, limit: int = 20) -> str:
        """Return a formatted table of recent trades."""
        trades = self.get_all_trades(limit)
        if not trades:
            return "No trades recorded yet."

        lines = [
            "",
            f"{'#':>4} {'Ticket':>8} {'Symbol':8} {'Dir':4} {'Lots':>5} "
            f"{'Entry':>10} {'Exit':>10} {'SL Pips':>7} {'Pips':>7} "
            f"{'P&L':>8} {'RR':>4} {'Outcome':8} {'Setup':6} {'Cycle':5}",
            "-" * 110,
        ]

        for t in trades:
            pips = t["pips_gained"]
            pips_str = f"{pips:+.1f}" if pips is not None else "open"
            pnl = t["net_profit"]
            pnl_str = f"${pnl:+.2f}" if pnl is not None else "-"
            exit_str = f"{t['exit_price']:.5f}"[:10] if t["exit_price"] else "open"
            outcome = t["outcome"] or "OPEN"
            cycle = f"L{t['cycle_level']}" if t["cycle_level"] else "-"

            lines.append(
                f"{t['id']:>4} {t['ticket'] or 0:>8} {t['symbol']:8} "
                f"{t['direction']:4} {t['lot_size']:>5.2f} "
                f"{t['entry_price']:>10.5f} {exit_str:>10} "
                f"{t['sl_pips']:>7.1f} {pips_str:>7} "
                f"{pnl_str:>8} {t['risk_reward']:>4.1f} "
                f"{outcome:8} {t['setup_type']:6} {cycle:>5}"
            )

        return "\n".join(lines)
