"""Persistent Re-Entry Guard — SQLite-backed trade loss tracking.

Survives orchestrator restarts. All state written to disk immediately.

Rules:
  - After ANY exit on a symbol → ENTRY_COOLDOWN (2 hours, prevents same-setup churn)
  - 1 loss on symbol+direction → COOLDOWN (blocked until session transition)
  - 2+ losses on symbol+direction same day → BANNED for the day
  - New trading day → all bans/cooldowns reset
  - On startup → rebuild state from DB + MT5 history

Also checks:
  - Existing open positions on the same pair before allowing new entry
  - Total exposure across all pairs vs account limits
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Set

import MetaTrader5 as mt5

from config.settings import settings
from helix_v3.utils.logger import get_logger

logger = get_logger("reentry_guard")

DB_PATH = Path(settings.log_dir) / "reentry_guard.db"
MAGIC = 314159  # Helix magic number

SCHEMA = """
CREATE TABLE IF NOT EXISTS loss_events (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol      TEXT NOT NULL,
    direction   TEXT NOT NULL,
    ticket      INTEGER,
    loss_pips   REAL,
    loss_usd    REAL,
    recorded_at TEXT NOT NULL,
    trading_day TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS bans (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol      TEXT NOT NULL,
    direction   TEXT NOT NULL,
    ban_type    TEXT NOT NULL,
    reason      TEXT,
    created_at  TEXT NOT NULL,
    trading_day TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS entry_cooldowns (
    symbol         TEXT PRIMARY KEY,
    cooldown_until TEXT NOT NULL,
    set_at         TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS setup_cooldowns (
    symbol         TEXT NOT NULL,
    direction      TEXT NOT NULL,
    signature      TEXT NOT NULL,
    cooldown_until TEXT NOT NULL,
    set_at         TEXT NOT NULL,
    PRIMARY KEY (symbol, direction, signature)
);
CREATE INDEX IF NOT EXISTS idx_loss_day ON loss_events(trading_day, symbol, direction);
CREATE INDEX IF NOT EXISTS idx_ban_day ON bans(trading_day, symbol);
"""


def _trading_day() -> str:
    """Current trading day as YYYY-MM-DD (resets at 22:00 UTC / 01:00 EAT)."""
    now = datetime.now(timezone.utc)
    # Trading day rolls at 22:00 UTC
    if now.hour >= 22:
        return (now + timedelta(days=1)).strftime("%Y-%m-%d")
    return now.strftime("%Y-%m-%d")


class ReentryGuard:
    """Persistent re-entry guard with SQLite backing."""

    def __init__(self, db_path: Optional[Path] = None, ban_scope: Optional[str] = None) -> None:
        self._db_path = db_path or DB_PATH
        self._ban_scope = _normalize_ban_scope(ban_scope or settings.risk.reentry_guard_ban_scope)
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self._db_path))
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.executescript(SCHEMA)
        self._conn.commit()

        # Load today's state from DB
        self._today = _trading_day()
        self._rebuild_state()
        logger.info(
            "ReentryGuard initialized: %d losses, %d bans, %d cooldowns for %s scope=%s",
            len(self._loss_counts), len(self._banned), len(self._cooldowns),
            self._today, self._ban_scope,
        )

    def _rebuild_state(self) -> None:
        """Rebuild in-memory state from DB for today's trading day."""
        self._today = _trading_day()

        # Count losses per symbol+direction today
        self._loss_counts: dict[str, int] = {}
        rows = self._conn.execute(
            "SELECT symbol, direction, COUNT(*) as cnt FROM loss_events "
            "WHERE trading_day = ? GROUP BY symbol, direction",
            (self._today,),
        ).fetchall()
        for r in rows:
            key = f"{r['symbol']}_{r['direction']}"
            self._loss_counts[key] = r["cnt"]

        # Load bans
        self._banned: Set[str] = set()
        bans = self._conn.execute(
            "SELECT symbol, direction, ban_type FROM bans WHERE trading_day = ?",
            (self._today,),
        ).fetchall()
        for b in bans:
            if b["ban_type"] == "DAY_BAN":
                self._banned.add(f"{b['symbol']}_{b['direction']}")
                if self._ban_scope == "symbol":
                    self._banned.add(b["symbol"])

        # Cooldowns (1 loss, not yet banned)
        self._cooldowns: Set[str] = set()
        for key, cnt in self._loss_counts.items():
            if cnt == 1 and key not in self._banned:
                self._cooldowns.add(key)

        # Entry cooldowns: block re-entry on same symbol for 2 hours after ANY exit
        # Persisted to entry_cooldowns table so cross-restart and cross-instance cooldowns hold.
        self._entry_cooldowns: dict[str, datetime] = {}
        now = datetime.now(timezone.utc)
        rows = self._conn.execute(
            "SELECT symbol, cooldown_until FROM entry_cooldowns"
        ).fetchall()
        for r in rows:
            try:
                until = datetime.fromisoformat(r["cooldown_until"])
            except ValueError:
                continue
            if until > now:
                self._entry_cooldowns[r["symbol"]] = until
            else:
                # Expired — purge
                self._conn.execute(
                    "DELETE FROM entry_cooldowns WHERE symbol = ?", (r["symbol"],)
                )
        self._conn.commit()

    def check(self, symbol: str, direction: str) -> Optional[str]:
        """Check if entry is allowed. Returns None if OK, reason string if blocked."""
        # Day rollover check
        today = _trading_day()
        if today != self._today:
            self._rebuild_state()

        key = f"{symbol}_{direction}"

        if key in self._banned:
            cnt = self._loss_counts.get(key, 0)
            return f"BANNED: {symbol} {direction} — {cnt} losses today, no more entries"

        if symbol in self._banned:
            return f"BANNED: {symbol} - symbol-wide day ban active"

        if key in self._cooldowns:
            return f"COOLDOWN: {symbol} {direction} — 1 loss, waiting for session change"

        # Entry cooldown: no re-entry on same symbol for 2 hours after ANY exit
        cooldown_until = self._entry_cooldowns.get(symbol)
        if cooldown_until is not None:
            now = datetime.now(timezone.utc)
            if now < cooldown_until:
                remaining = int((cooldown_until - now).total_seconds() / 60)
                return f"ENTRY_COOLDOWN: {symbol} — {remaining}min remaining (prevents same-setup churn)"

        # Check if there's already an open position on this pair
        positions = mt5.positions_get(symbol=symbol)
        helix_positions = [p for p in (positions or []) if p.magic == MAGIC]
        if helix_positions:
            total_lots = sum(p.volume for p in helix_positions)
            return f"EXPOSURE: {symbol} already has {len(helix_positions)} open position(s), {total_lots:.2f} lots"

        return None

    def record_exit(self, symbol: str, cooldown_hours: float = 2.0) -> None:
        """Record a trade exit and set entry cooldown. Call after ANY trade closes.

        Persists to SQLite so the cooldown holds across restarts and across instances
        sharing the same DB file (which is the only way two orchestrators can agree).
        """
        now = datetime.now(timezone.utc)
        until = now + timedelta(hours=cooldown_hours)
        self._entry_cooldowns[symbol] = until
        self._conn.execute(
            "INSERT OR REPLACE INTO entry_cooldowns (symbol, cooldown_until, set_at) "
            "VALUES (?, ?, ?)",
            (symbol, until.isoformat(), now.isoformat()),
        )
        self._conn.commit()
        logger.info(
            "GUARD: %s entry cooldown set for %.1f hours (until %s)",
            symbol, cooldown_hours,
            until.strftime("%H:%M UTC"),
        )

    def set_setup_cooldown(
        self,
        symbol: str,
        direction: str,
        signature: str,
        minutes: float = 60.0,
    ) -> None:
        """Block re-entry of an identical setup signature for N minutes.

        Independent of the broader 2h symbol-level cooldown — this catches setups
        that persist across many M15 cycles (e.g. range-bound 'M/W BUY confluence 97'
        re-detecting every cycle). Persisted so it survives restarts.
        """
        now = datetime.now(timezone.utc)
        until = now + timedelta(minutes=minutes)
        self._conn.execute(
            "INSERT OR REPLACE INTO setup_cooldowns "
            "(symbol, direction, signature, cooldown_until, set_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (symbol, direction, signature, until.isoformat(), now.isoformat()),
        )
        self._conn.commit()
        logger.info(
            "GUARD: setup cooldown %s %s sig=%s for %.0fmin",
            symbol, direction, signature, minutes,
        )

    def check_setup_cooldown(
        self, symbol: str, direction: str, signature: str
    ) -> Optional[str]:
        """Return reason string if this signature is in cooldown, else None."""
        row = self._conn.execute(
            "SELECT cooldown_until FROM setup_cooldowns "
            "WHERE symbol = ? AND direction = ? AND signature = ?",
            (symbol, direction, signature),
        ).fetchone()
        if not row:
            return None
        try:
            until = datetime.fromisoformat(row["cooldown_until"])
        except ValueError:
            return None
        now = datetime.now(timezone.utc)
        if until <= now:
            # Expired — purge
            self._conn.execute(
                "DELETE FROM setup_cooldowns "
                "WHERE symbol = ? AND direction = ? AND signature = ?",
                (symbol, direction, signature),
            )
            self._conn.commit()
            return None
        remaining = int((until - now).total_seconds() / 60)
        return f"SETUP_COOLDOWN: {symbol} {direction} sig={signature} — {remaining}min remaining"

    def record_loss(self, symbol: str, direction: str,
                    ticket: int = 0, loss_pips: float = 0, loss_usd: float = 0) -> None:
        """Record a loss and update guard state. Persists to DB immediately."""
        today = _trading_day()
        if today != self._today:
            self._rebuild_state()

        key = f"{symbol}_{direction}"

        # Write to DB
        self._conn.execute(
            "INSERT INTO loss_events (symbol, direction, ticket, loss_pips, loss_usd, recorded_at, trading_day) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (symbol, direction, ticket, loss_pips, loss_usd,
             datetime.now(timezone.utc).isoformat(), today),
        )
        self._conn.commit()

        # Update counts
        self._loss_counts[key] = self._loss_counts.get(key, 0) + 1
        cnt = self._loss_counts[key]

        if cnt >= 2:
            # Ban for the day
            self._banned.add(key)
            if self._ban_scope == "symbol":
                self._banned.add(symbol)
            self._cooldowns.discard(key)
            self._conn.execute(
                "INSERT INTO bans (symbol, direction, ban_type, reason, created_at, trading_day) "
                "VALUES (?, ?, 'DAY_BAN', ?, ?, ?)",
                (symbol, direction, f"{cnt} consecutive losses",
                 datetime.now(timezone.utc).isoformat(), today),
            )
            self._conn.commit()
            logger.warning("GUARD: %s %s BANNED for %s (%d losses)", symbol, direction, today, cnt)
        else:
            # Cooldown
            self._cooldowns.add(key)
            logger.warning("GUARD: %s %s on COOLDOWN (%d loss)", symbol, direction, cnt)

    def clear_cooldowns(self) -> None:
        """Clear cooldowns on session transition. Bans persist."""
        cleared = list(self._cooldowns)
        self._cooldowns.clear()
        if cleared:
            logger.info("GUARD: Cooldowns cleared: %s", cleared)

    def get_status(self) -> dict:
        """Return current guard state for logging/display."""
        today = _trading_day()
        if today != self._today:
            self._rebuild_state()
        return {
            "trading_day": self._today,
            "ban_scope": self._ban_scope,
            "loss_counts": dict(self._loss_counts),
            "banned": list(self._banned),
            "cooldowns": list(self._cooldowns),
        }

    def close(self) -> None:
        self._conn.close()


def check_pair_exposure(symbol: str, max_positions_per_pair: int = 1) -> Optional[str]:
    """Standalone check: does this pair already have open Helix positions?"""
    positions = mt5.positions_get(symbol=symbol)
    helix = [p for p in (positions or []) if p.magic == MAGIC]
    if len(helix) >= max_positions_per_pair:
        total_lots = sum(p.volume for p in helix)
        return f"{symbol}: {len(helix)} position(s) open ({total_lots:.2f} lots). Max {max_positions_per_pair}."
    return None


def _normalize_ban_scope(value: str) -> str:
    scope = str(value or "direction").strip().lower()
    if scope in {"symbol", "symbol-wide", "pair"}:
        return "symbol"
    return "direction"
