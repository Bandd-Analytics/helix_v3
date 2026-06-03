"""Market Structure Flashcard System.

Saves snapshots of market structure at entry and exit points to learn
which patterns produce wins vs losses. Over time, builds a database of
pattern-outcome pairs that can be queried for:
- Which M/W formations at which cycle levels win most?
- Which session + stop hunt combos produce the best entries?
- Which pairs are strongest at which cycle positions?
- What does a winning L3 reversal look like vs a losing one?

Each flashcard captures:
- Chart image path (the 1024x1024 vision chart at moment of signal)
- Full MTF context (weekly/4H/1H/15M analysis snapshot)
- Entry signal details
- Outcome (win/loss/BE, pips, P&L)
- Tags for pattern classification
"""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from config.settings import settings
from helix_v3.utils.logger import get_logger

logger = get_logger("flashcards")

DB_PATH = Path(settings.log_dir) / "flashcards.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS flashcards (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at          TEXT NOT NULL DEFAULT (datetime('now')),

    -- Identity
    symbol              TEXT NOT NULL,
    timeframe           TEXT NOT NULL,
    ticket              INTEGER,

    -- Snapshot timing
    snapshot_type       TEXT NOT NULL,
    snapshot_at         TEXT NOT NULL,

    -- Chart reference
    chart_path          TEXT,

    -- Weekly context
    weekly_cycle        TEXT,
    weekly_phase        TEXT,
    weekly_trend        TEXT,
    days_from_peak      INTEGER,

    -- 4H context
    h4_cycle            TEXT,
    h4_level            INTEGER,
    h4_trend            TEXT,
    h4_choppy           INTEGER,

    -- 1H context
    h1_session          TEXT,
    h1_trend            TEXT,
    h1_intraday_level   INTEGER,
    h1_hod_locked       INTEGER,
    h1_lod_locked       INTEGER,
    h1_50_200_cross     TEXT,

    -- 15M entry context
    asian_range_pips    REAL,
    accumulation_valid  INTEGER,
    stop_hunt_detected  INTEGER,
    stop_hunt_direction TEXT,
    stop_hunt_pips      REAL,
    push_count          INTEGER,
    m_w_forming         INTEGER,
    rrt_detected        INTEGER,
    entry_direction     TEXT,
    entry_confidence    REAL,
    confluence_score    INTEGER,

    -- Signal details
    ema_5_angle         REAL,
    ema_13_angle        REAL,
    ema_50_angle        REAL,
    ema_200_angle       REAL,
    ema_800_angle       REAL,
    fast_slow_div       REAL,

    -- Outcome (filled after trade closes)
    outcome             TEXT,
    pips_gained         REAL,
    net_profit          REAL,
    duration_minutes    REAL,
    exit_reason         TEXT,
    t1_hit              INTEGER DEFAULT 0,

    -- Pattern tags (JSON array)
    tags                TEXT,
    notes               TEXT,

    -- Risk profile used
    risk_tier           TEXT,
    risk_pct            REAL,
    lot_size            REAL
);

CREATE INDEX IF NOT EXISTS idx_fc_symbol ON flashcards(symbol);
CREATE INDEX IF NOT EXISTS idx_fc_outcome ON flashcards(outcome);
CREATE INDEX IF NOT EXISTS idx_fc_type ON flashcards(snapshot_type);
CREATE INDEX IF NOT EXISTS idx_fc_tags ON flashcards(tags);
CREATE INDEX IF NOT EXISTS idx_fc_weekly_cycle ON flashcards(weekly_cycle);
CREATE INDEX IF NOT EXISTS idx_fc_h4_level ON flashcards(h4_level);
CREATE INDEX IF NOT EXISTS idx_fc_confluence ON flashcards(confluence_score);
"""


class FlashcardSystem:
    """Persistent market structure learning database.

    Records chart snapshots with full MTF context at:
    - ENTRY: when a trade is opened
    - EXIT: when a trade closes (adds outcome data)
    - SCAN: interesting structures detected during 15-min scans (no trade taken)
    - MISSED: valid setups that weren't traded (for review)

    Query methods allow pattern mining:
    - What structures win? What loses?
    - Best cycle level for each pair?
    - Which sessions produce the best entries?
    """

    def __init__(self, db_path: Optional[Path] = None) -> None:
        self._db_path = db_path or DB_PATH
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self._db_path))
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.executescript(SCHEMA)
        self._conn.commit()
        logger.info("Flashcard system initialized: %s", self._db_path)

    def close(self) -> None:
        self._conn.close()

    # ------------------------------------------------------------------
    # Save Flashcard
    # ------------------------------------------------------------------

    def save_entry_flashcard(
        self,
        symbol: str,
        timeframe: str,
        ticket: int,
        chart_path: str,
        mtf_context: Dict[str, Any],
        tags: Optional[List[str]] = None,
        notes: str = "",
    ) -> int:
        return self._save(
            snapshot_type="ENTRY",
            symbol=symbol,
            timeframe=timeframe,
            ticket=ticket,
            chart_path=chart_path,
            mtf_context=mtf_context,
            tags=tags,
            notes=notes,
        )

    def save_scan_flashcard(
        self,
        symbol: str,
        timeframe: str,
        chart_path: str,
        mtf_context: Dict[str, Any],
        tags: Optional[List[str]] = None,
        notes: str = "",
    ) -> int:
        return self._save(
            snapshot_type="SCAN",
            symbol=symbol,
            timeframe=timeframe,
            chart_path=chart_path,
            mtf_context=mtf_context,
            tags=tags,
            notes=notes,
        )

    def save_missed_flashcard(
        self,
        symbol: str,
        timeframe: str,
        chart_path: str,
        mtf_context: Dict[str, Any],
        reason: str = "",
        tags: Optional[List[str]] = None,
    ) -> int:
        return self._save(
            snapshot_type="MISSED",
            symbol=symbol,
            timeframe=timeframe,
            chart_path=chart_path,
            mtf_context=mtf_context,
            tags=tags,
            notes=f"MISSED: {reason}",
        )

    def _save(
        self,
        snapshot_type: str,
        symbol: str,
        timeframe: str,
        chart_path: str,
        mtf_context: Dict[str, Any],
        ticket: Optional[int] = None,
        tags: Optional[List[str]] = None,
        notes: str = "",
    ) -> int:
        w = mtf_context.get("weekly", {})
        h4 = mtf_context.get("four_hour", {})
        h1 = mtf_context.get("one_hour", {})
        m15 = mtf_context.get("fifteen_min", {})
        ema = mtf_context.get("ema", {})
        profile = mtf_context.get("profile", {})

        cursor = self._conn.execute(
            """INSERT INTO flashcards (
                symbol, timeframe, ticket, snapshot_type, snapshot_at, chart_path,
                weekly_cycle, weekly_phase, weekly_trend, days_from_peak,
                h4_cycle, h4_level, h4_trend, h4_choppy,
                h1_session, h1_trend, h1_intraday_level, h1_hod_locked, h1_lod_locked, h1_50_200_cross,
                asian_range_pips, accumulation_valid, stop_hunt_detected, stop_hunt_direction,
                stop_hunt_pips, push_count, m_w_forming, rrt_detected,
                entry_direction, entry_confidence, confluence_score,
                ema_5_angle, ema_13_angle, ema_50_angle, ema_200_angle, ema_800_angle, fast_slow_div,
                tags, notes, risk_tier, risk_pct, lot_size
            ) VALUES (
                ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?, ?,
                ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?
            )""",
            (
                symbol, timeframe, ticket, snapshot_type,
                datetime.now(timezone.utc).isoformat(), chart_path,
                w.get("cycle_position"), w.get("week_phase"), w.get("trend_direction"), w.get("days_since_peak"),
                h4.get("cycle_position"), h4.get("level_count"), h4.get("trend_direction"), h4.get("is_choppy"),
                h1.get("session_phase"), h1.get("trend_direction"), h1.get("intraday_level"),
                h1.get("hod_locked"), h1.get("lod_locked"), h1.get("ema_50_200_cross"),
                m15.get("asian_range_pips"), m15.get("accumulation_valid"), m15.get("stop_hunt_detected"),
                m15.get("stop_hunt_direction"), m15.get("stop_hunt_pips"), m15.get("push_count"),
                m15.get("m_w_forming"), m15.get("rrt_detected"),
                m15.get("entry_direction"), m15.get("entry_confidence"), mtf_context.get("confluence_score"),
                ema.get("ema_5_angle"), ema.get("ema_13_angle"), ema.get("ema_50_angle"),
                ema.get("ema_200_angle"), ema.get("ema_800_angle"), ema.get("fast_slow_div"),
                json.dumps(tags) if tags else None, notes,
                profile.get("risk_tier"), profile.get("max_risk_pct"), profile.get("lot_size"),
            ),
        )
        self._conn.commit()
        fc_id = cursor.lastrowid
        logger.info("Flashcard #%d saved: %s %s %s", fc_id, snapshot_type, symbol, timeframe)
        return fc_id

    # ------------------------------------------------------------------
    # Update Outcome (after trade closes)
    # ------------------------------------------------------------------

    def record_outcome(
        self,
        ticket: int,
        outcome: str,
        pips_gained: float,
        net_profit: float,
        duration_minutes: float,
        exit_reason: str,
        t1_hit: bool = False,
    ) -> None:
        self._conn.execute(
            """UPDATE flashcards SET
                outcome = ?, pips_gained = ?, net_profit = ?,
                duration_minutes = ?, exit_reason = ?, t1_hit = ?
            WHERE ticket = ? AND snapshot_type = 'ENTRY'""",
            (outcome, pips_gained, net_profit, duration_minutes, exit_reason, int(t1_hit), ticket),
        )
        self._conn.commit()
        logger.info("Flashcard outcome: ticket=%d %s %+.1f pips", ticket, outcome, pips_gained)

    # ------------------------------------------------------------------
    # Pattern Queries
    # ------------------------------------------------------------------

    def get_winning_patterns(self, min_trades: int = 3) -> List[Dict[str, Any]]:
        """Group flashcards by pattern signature and rank by win rate."""
        rows = self._conn.execute(
            """SELECT
                h4_level, weekly_cycle, h1_session, entry_direction,
                stop_hunt_detected, m_w_forming, rrt_detected,
                COUNT(*) as total,
                SUM(CASE WHEN outcome = 'WIN' THEN 1 ELSE 0 END) as wins,
                AVG(pips_gained) as avg_pips,
                AVG(net_profit) as avg_profit
            FROM flashcards
            WHERE snapshot_type = 'ENTRY' AND outcome IS NOT NULL
            GROUP BY h4_level, weekly_cycle, h1_session, entry_direction,
                     stop_hunt_detected, m_w_forming, rrt_detected
            HAVING total >= ?
            ORDER BY (wins * 1.0 / total) DESC""",
            (min_trades,),
        ).fetchall()
        return [dict(r) for r in rows]

    def get_pattern_by_symbol(self, symbol: str) -> Dict[str, Any]:
        """Win rate and performance breakdown for a specific pair."""
        rows = self._conn.execute(
            """SELECT outcome, COUNT(*) as cnt, AVG(pips_gained) as avg_pips,
                      AVG(duration_minutes) as avg_dur
            FROM flashcards
            WHERE symbol = ? AND snapshot_type = 'ENTRY' AND outcome IS NOT NULL
            GROUP BY outcome""",
            (symbol,),
        ).fetchall()
        return {r["outcome"]: dict(r) for r in rows}

    def get_best_cycle_level(self) -> List[Dict[str, Any]]:
        """Which cycle level (L1/L2/L3) produces the best results?"""
        rows = self._conn.execute(
            """SELECT h4_level, COUNT(*) as total,
                SUM(CASE WHEN outcome = 'WIN' THEN 1 ELSE 0 END) as wins,
                AVG(pips_gained) as avg_pips,
                ROUND(SUM(CASE WHEN outcome = 'WIN' THEN 1.0 ELSE 0 END) / COUNT(*) * 100, 1) as win_rate
            FROM flashcards
            WHERE snapshot_type = 'ENTRY' AND outcome IS NOT NULL AND h4_level IS NOT NULL
            GROUP BY h4_level
            ORDER BY win_rate DESC"""
        ).fetchall()
        return [dict(r) for r in rows]

    def get_best_session(self) -> List[Dict[str, Any]]:
        """Which session produces the best entries?"""
        rows = self._conn.execute(
            """SELECT h1_session, COUNT(*) as total,
                SUM(CASE WHEN outcome = 'WIN' THEN 1 ELSE 0 END) as wins,
                AVG(pips_gained) as avg_pips,
                ROUND(SUM(CASE WHEN outcome = 'WIN' THEN 1.0 ELSE 0 END) / COUNT(*) * 100, 1) as win_rate
            FROM flashcards
            WHERE snapshot_type = 'ENTRY' AND outcome IS NOT NULL AND h1_session IS NOT NULL
            GROUP BY h1_session
            ORDER BY win_rate DESC"""
        ).fetchall()
        return [dict(r) for r in rows]

    def get_confluence_vs_outcome(self) -> List[Dict[str, Any]]:
        """Does higher confluence score = better outcomes?"""
        rows = self._conn.execute(
            """SELECT
                CASE
                    WHEN confluence_score >= 75 THEN '75-100'
                    WHEN confluence_score >= 50 THEN '50-74'
                    WHEN confluence_score >= 25 THEN '25-49'
                    ELSE '0-24'
                END as score_bucket,
                COUNT(*) as total,
                SUM(CASE WHEN outcome = 'WIN' THEN 1 ELSE 0 END) as wins,
                AVG(pips_gained) as avg_pips,
                ROUND(SUM(CASE WHEN outcome = 'WIN' THEN 1.0 ELSE 0 END) / COUNT(*) * 100, 1) as win_rate
            FROM flashcards
            WHERE snapshot_type = 'ENTRY' AND outcome IS NOT NULL
            GROUP BY score_bucket
            ORDER BY score_bucket DESC"""
        ).fetchall()
        return [dict(r) for r in rows]

    def get_total_flashcards(self) -> Dict[str, int]:
        row = self._conn.execute(
            """SELECT
                COUNT(*) as total,
                SUM(CASE WHEN snapshot_type = 'ENTRY' THEN 1 ELSE 0 END) as entries,
                SUM(CASE WHEN snapshot_type = 'SCAN' THEN 1 ELSE 0 END) as scans,
                SUM(CASE WHEN snapshot_type = 'MISSED' THEN 1 ELSE 0 END) as missed,
                SUM(CASE WHEN outcome = 'WIN' THEN 1 ELSE 0 END) as wins,
                SUM(CASE WHEN outcome = 'LOSS' THEN 1 ELSE 0 END) as losses
            FROM flashcards"""
        ).fetchone()
        return dict(row)

    def print_learning_report(self) -> str:
        """Formatted learning insights report."""
        stats = self.get_total_flashcards()
        if stats["total"] == 0:
            return "No flashcards recorded yet. System will learn as trades are taken."

        lines = [
            "",
            "=" * 65,
            "  HELIX V3 MARKET STRUCTURE LEARNING REPORT",
            "=" * 65,
            "",
            f"  Total Flashcards: {stats['total']}",
            f"  Entries: {stats['entries']} | Scans: {stats['scans']} | Missed: {stats['missed']}",
            f"  Wins: {stats['wins']} | Losses: {stats['losses']}",
        ]

        # Best cycle level
        levels = self.get_best_cycle_level()
        if levels:
            lines.append("\n  --- Best Cycle Level ---")
            for l in levels:
                lines.append(f"  L{l['h4_level']}: {l['total']}T WR={l['win_rate']}% avg={l['avg_pips']:+.1f}p")

        # Best session
        sessions = self.get_best_session()
        if sessions:
            lines.append("\n  --- Best Entry Session ---")
            for s in sessions:
                lines.append(f"  {s['h1_session']}: {s['total']}T WR={s['win_rate']}% avg={s['avg_pips']:+.1f}p")

        # Confluence vs outcome
        conf = self.get_confluence_vs_outcome()
        if conf:
            lines.append("\n  --- Confluence Score vs Win Rate ---")
            for c in conf:
                lines.append(f"  Score {c['score_bucket']}: {c['total']}T WR={c['win_rate']}% avg={c['avg_pips']:+.1f}p")

        lines.append("")
        lines.append("=" * 65)
        return "\n".join(lines)
