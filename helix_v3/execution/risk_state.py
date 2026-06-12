"""Persistent account risk state — the kill switch's memory.

SQLite-backed (logs/risk_state.db), survives restarts. Replaces the broken
(balance - equity) / balance breaker, which reset to ~0 the moment a loss was
REALIZED (balance dropped with equity), so the system could lose 3% per trade
indefinitely without ever tripping.

Tracked here:
  - Balance high-water mark (HWM): total drawdown is measured from the best
    balance the account has ever reached, not from the current balance.
  - Daily anchor balance: the balance at the first check of each trading day.
    Realized + floating losses against it trip the daily-loss limit.
  - Daily trips are LATCHED: once the daily-loss limit fires, no new entries
    for the rest of that trading day even if equity recovers.

Trading day rolls at 22:00 UTC (01:00 EAT), matching the re-entry guard.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Tuple

from config.settings import settings
from helix_v3.utils.logger import get_logger

logger = get_logger("risk_state")

DB_PATH = Path(settings.log_dir) / "risk_state.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS state (
    key        TEXT PRIMARY KEY,
    value      REAL NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS daily_anchor (
    trading_day TEXT PRIMARY KEY,
    balance     REAL NOT NULL,
    set_at      TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS trips (
    trading_day TEXT NOT NULL,
    reason      TEXT NOT NULL,
    tripped_at  TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_trips_day ON trips(trading_day);
"""


def _trading_day(now: Optional[datetime] = None) -> str:
    """Current trading day as YYYY-MM-DD (rolls at 22:00 UTC / 01:00 EAT)."""
    now = now or datetime.now(timezone.utc)
    if now.hour >= 22:
        return (now + timedelta(days=1)).strftime("%Y-%m-%d")
    return now.strftime("%Y-%m-%d")


class RiskState:
    """Persistent kill-switch state. All writes hit disk immediately (WAL)."""

    def __init__(
        self,
        db_path: Optional[Path] = None,
        max_daily_loss_pct: Optional[float] = None,
        max_total_drawdown_pct: Optional[float] = None,
    ) -> None:
        self._db_path = Path(db_path) if db_path else DB_PATH
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self._db_path))
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.executescript(SCHEMA)
        self._conn.commit()
        self.max_daily_loss_pct = (
            max_daily_loss_pct
            if max_daily_loss_pct is not None
            else settings.risk.max_daily_loss_pct
        )
        self.max_total_drawdown_pct = (
            max_total_drawdown_pct
            if max_total_drawdown_pct is not None
            else settings.risk.max_drawdown_pct
        )

    # ------------------------------------------------------------------

    def _now_iso(self, now: Optional[datetime] = None) -> str:
        return (now or datetime.now(timezone.utc)).strftime("%Y-%m-%dT%H:%M:%SZ")

    def _get_hwm(self) -> Optional[float]:
        row = self._conn.execute(
            "SELECT value FROM state WHERE key='balance_hwm'"
        ).fetchone()
        return row[0] if row else None

    def _set_hwm(self, value: float, now: Optional[datetime] = None) -> None:
        self._conn.execute(
            "INSERT INTO state(key, value, updated_at) VALUES('balance_hwm', ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
            (value, self._now_iso(now)),
        )
        self._conn.commit()

    def _get_daily_anchor(self, day: str, balance: float, now: Optional[datetime] = None) -> float:
        row = self._conn.execute(
            "SELECT balance FROM daily_anchor WHERE trading_day=?", (day,)
        ).fetchone()
        if row:
            return row[0]
        self._conn.execute(
            "INSERT INTO daily_anchor(trading_day, balance, set_at) VALUES(?, ?, ?)",
            (day, balance, self._now_iso(now)),
        )
        self._conn.commit()
        logger.info("Daily anchor set for %s: $%.2f", day, balance)
        return balance

    def _is_tripped(self, day: str) -> Optional[str]:
        row = self._conn.execute(
            "SELECT reason FROM trips WHERE trading_day=? ORDER BY tripped_at DESC LIMIT 1",
            (day,),
        ).fetchone()
        return row[0] if row else None

    def _trip(self, day: str, reason: str, now: Optional[datetime] = None) -> None:
        self._conn.execute(
            "INSERT INTO trips(trading_day, reason, tripped_at) VALUES(?, ?, ?)",
            (day, reason, self._now_iso(now)),
        )
        self._conn.commit()
        logger.critical("KILL SWITCH TRIPPED for %s: %s", day, reason)

    # ------------------------------------------------------------------

    def check(
        self,
        balance: float,
        equity: float,
        now: Optional[datetime] = None,
    ) -> Tuple[bool, str]:
        """Return (ok, reason). ok=False blocks all new entries.

        Realized losses count: both the daily anchor and the HWM are balance
        based, while the comparison uses EQUITY so floating losses also count.
        """
        if balance <= 0 or equity <= 0:
            return False, f"invalid account state (balance={balance}, equity={equity})"

        day = _trading_day(now)

        # Latched daily trip — no resume within the trading day.
        latched = self._is_tripped(day)
        if latched:
            return False, f"latched for {day}: {latched}"

        # High-water mark (rises with balance, never falls)
        hwm = self._get_hwm()
        if hwm is None or balance > hwm:
            hwm = balance
            self._set_hwm(hwm, now)

        # Total drawdown from HWM (floating included via equity)
        total_dd = (hwm - equity) / hwm
        if total_dd >= self.max_total_drawdown_pct:
            reason = (
                f"total drawdown {total_dd:.1%} >= {self.max_total_drawdown_pct:.1%} "
                f"limit (HWM ${hwm:.2f}, equity ${equity:.2f})"
            )
            self._trip(day, reason, now)
            return False, reason

        # Daily realized + floating loss vs the day's anchor balance
        anchor = self._get_daily_anchor(day, balance, now)
        if anchor > 0:
            daily_loss = (anchor - equity) / anchor
            if daily_loss >= self.max_daily_loss_pct:
                reason = (
                    f"daily loss {daily_loss:.1%} >= {self.max_daily_loss_pct:.1%} "
                    f"limit (anchor ${anchor:.2f}, equity ${equity:.2f})"
                )
                self._trip(day, reason, now)
                return False, reason

        return True, "ok"

    def close(self) -> None:
        self._conn.close()
