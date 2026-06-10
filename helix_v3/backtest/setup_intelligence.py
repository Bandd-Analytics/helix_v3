"""Derived MMM setup intelligence database and reports.

This module turns raw historical flashcards and event replay outcomes into
queryable recurrence, profitability, price-level, session/day, and cross-pair
statistics. It is offline-only and does not touch live MT5 execution.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from config.pair_profiles import get_pair_profile
from config.settings import settings

FLASHCARDS_DB_PATH = Path(settings.log_dir) / "flashcards.db"
REPLAY_DB_PATH = Path(settings.log_dir) / "vision_backtests.db"
DEFAULT_INTELLIGENCE_DB_PATH = Path(settings.log_dir) / "setup_intelligence.db"
DEFAULT_REPORT_PATH = Path("data/mmm_training/setup_intelligence/REPORT.md")
DEFAULT_BASKET_REPORT_PATH = Path("data/mmm_training/setup_intelligence/ALERT_ONLY_BASKET.md")

FAVORABLE_OUTCOMES = {"TARGET_2", "TRAIL_STOP", "TIME_EXIT_PROFIT", "OPEN_PROFIT"}
DAY_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

SCHEMA = """
CREATE TABLE IF NOT EXISTS setup_occurrences (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    source              TEXT NOT NULL,
    source_id           INTEGER NOT NULL,
    signature_id        INTEGER,
    outcome_id          INTEGER,
    symbol              TEXT NOT NULL,
    timeframe           TEXT NOT NULL,
    snapshot_at         TEXT NOT NULL,
    snapshot_date       TEXT NOT NULL,
    day_of_week         TEXT NOT NULL,
    hour_utc            INTEGER NOT NULL,
    session             TEXT NOT NULL,
    direction           TEXT NOT NULL,
    normalized_key      TEXT NOT NULL,
    setup_family        TEXT NOT NULL,
    primary_theme       TEXT,
    weekly_phase        TEXT,
    weekly_trend        TEXT,
    h4_level            INTEGER,
    h4_trend            TEXT,
    h1_trend            TEXT,
    confluence_score    INTEGER,
    entry_price         REAL,
    stop_loss_price     REAL,
    t1_price            REAL,
    t2_price            REAL,
    sl_pips             REAL,
    t1_pips             REAL,
    t2_pips             REAL,
    exit_at             TEXT,
    exit_pips           REAL,
    max_favorable_pips  REAL,
    max_adverse_pips    REAL,
    t1_hit              INTEGER NOT NULL,
    minutes_to_t1       REAL,
    outcome             TEXT NOT NULL,
    event_path          TEXT NOT NULL,
    favorable           INTEGER NOT NULL,
    fast_profit         INTEGER NOT NULL,
    clean_departure     INTEGER NOT NULL,
    price_level_tag     TEXT NOT NULL,
    chart_path          TEXT,
    UNIQUE(source, source_id)
);

CREATE TABLE IF NOT EXISTS setup_stats (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol              TEXT NOT NULL,
    direction           TEXT NOT NULL,
    normalized_key      TEXT NOT NULL,
    setup_family        TEXT NOT NULL,
    primary_theme       TEXT,
    total               INTEGER NOT NULL,
    favorable           INTEGER NOT NULL,
    favorable_rate      REAL NOT NULL,
    t1_rate             REAL NOT NULL,
    fast_profit_rate    REAL NOT NULL,
    clean_departure_rate REAL NOT NULL,
    avg_exit_pips       REAL,
    avg_mfe             REAL,
    avg_mae             REAL,
    first_seen          TEXT,
    last_seen           TEXT,
    active_days         REAL NOT NULL,
    recurrence_per_30d  REAL NOT NULL,
    reappearance_score  REAL NOT NULL,
    opportunity_score   REAL NOT NULL,
    top_session         TEXT,
    top_day             TEXT,
    top_price_level     TEXT,
    example_flashcards  TEXT NOT NULL,
    rrs_grade           TEXT NOT NULL DEFAULT '',
    positive_expectancy INTEGER NOT NULL DEFAULT 0,
    decision            TEXT NOT NULL,
    UNIQUE(symbol, direction, normalized_key)
);

CREATE TABLE IF NOT EXISTS price_level_stats (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol              TEXT NOT NULL,
    direction           TEXT NOT NULL,
    price_level_tag     TEXT NOT NULL,
    total               INTEGER NOT NULL,
    favorable           INTEGER NOT NULL,
    favorable_rate      REAL NOT NULL,
    fast_profit_rate    REAL NOT NULL,
    clean_departure_rate REAL NOT NULL,
    avg_exit_pips       REAL,
    avg_mfe             REAL,
    avg_mae             REAL,
    avg_entry_price     REAL,
    UNIQUE(symbol, direction, price_level_tag)
);

CREATE TABLE IF NOT EXISTS day_session_stats (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol              TEXT NOT NULL,
    direction           TEXT NOT NULL,
    day_of_week         TEXT NOT NULL,
    session             TEXT NOT NULL,
    total               INTEGER NOT NULL,
    favorable           INTEGER NOT NULL,
    favorable_rate      REAL NOT NULL,
    fast_profit_rate    REAL NOT NULL,
    avg_exit_pips       REAL,
    avg_mfe             REAL,
    avg_mae             REAL,
    UNIQUE(symbol, direction, day_of_week, session)
);

CREATE TABLE IF NOT EXISTS cross_pair_stats (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    direction           TEXT NOT NULL,
    normalized_key      TEXT NOT NULL,
    setup_family        TEXT NOT NULL,
    symbols             TEXT NOT NULL,
    symbol_count        INTEGER NOT NULL,
    total               INTEGER NOT NULL,
    favorable           INTEGER NOT NULL,
    favorable_rate      REAL NOT NULL,
    avg_exit_pips       REAL,
    fast_profit_rate    REAL NOT NULL,
    rrs_grade           TEXT NOT NULL DEFAULT '',
    positive_expectancy INTEGER NOT NULL DEFAULT 0,
    top_session         TEXT,
    top_day             TEXT,
    opportunity_score   REAL NOT NULL,
    UNIQUE(direction, normalized_key)
);

CREATE TABLE IF NOT EXISTS expectancy_candidates (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol              TEXT NOT NULL,
    direction           TEXT NOT NULL,
    normalized_key      TEXT NOT NULL,
    setup_family        TEXT NOT NULL,
    primary_theme       TEXT,
    rrs_grade           TEXT NOT NULL,
    candidate_tier      TEXT NOT NULL,
    total               INTEGER NOT NULL,
    favorable           INTEGER NOT NULL,
    favorable_rate      REAL NOT NULL,
    t1_rate             REAL NOT NULL,
    fast_profit_rate    REAL NOT NULL,
    clean_departure_rate REAL NOT NULL,
    avg_exit_pips       REAL,
    avg_win_pips        REAL,
    avg_loss_pips       REAL,
    gross_profit_pips   REAL NOT NULL,
    gross_loss_pips     REAL NOT NULL,
    profit_factor       REAL NOT NULL,
    payoff_ratio        REAL NOT NULL,
    avg_mfe             REAL,
    avg_mae             REAL,
    split_passes        INTEGER NOT NULL,
    split_summary       TEXT NOT NULL,
    recurrence_per_30d  REAL NOT NULL,
    reappearance_score  REAL NOT NULL,
    opportunity_score   REAL NOT NULL,
    top_session         TEXT,
    top_day             TEXT,
    top_price_level     TEXT,
    example_flashcards  TEXT NOT NULL,
    notes               TEXT NOT NULL,
    UNIQUE(symbol, direction, normalized_key)
);

CREATE TABLE IF NOT EXISTS intelligence_metadata (
    key                 TEXT PRIMARY KEY,
    value               TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_intel_occ_symbol_time ON setup_occurrences(symbol, snapshot_at);
CREATE INDEX IF NOT EXISTS idx_intel_occ_key ON setup_occurrences(normalized_key);
CREATE INDEX IF NOT EXISTS idx_intel_stats_score ON setup_stats(opportunity_score);
CREATE INDEX IF NOT EXISTS idx_intel_stats_symbol ON setup_stats(symbol, direction);
CREATE INDEX IF NOT EXISTS idx_intel_expectancy_tier ON expectancy_candidates(candidate_tier);
"""


@dataclass(frozen=True)
class IntelligenceBuildResult:
    occurrences: int
    setup_stats: int
    price_level_stats: int
    day_session_stats: int
    cross_pair_stats: int
    expectancy_candidates: int
    report_path: Optional[Path] = None


class SetupIntelligenceBuilder:
    def __init__(
        self,
        *,
        flashcards_db: Path = FLASHCARDS_DB_PATH,
        replay_db: Path = REPLAY_DB_PATH,
        output_db: Path = DEFAULT_INTELLIGENCE_DB_PATH,
    ) -> None:
        self.flashcards_db = flashcards_db
        self.replay_db = replay_db
        self.output_db = output_db

    def rebuild(self, *, report_path: Optional[Path] = DEFAULT_REPORT_PATH) -> IntelligenceBuildResult:
        self.output_db.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(self.output_db))
        conn.row_factory = sqlite3.Row
        try:
            conn.executescript(SCHEMA)
            _ensure_schema_columns(conn)
            _clear_tables(conn)
            rows = self._load_source_rows(conn)
            occurrences = [_occurrence_from_row(row) for row in rows]
            _insert_occurrences(conn, occurrences)
            setup_stats = _build_setup_stats(conn)
            price_stats = _build_price_level_stats(conn)
            session_stats = _build_day_session_stats(conn)
            cross_stats = _build_cross_pair_stats(conn)
            expectancy_candidates = _build_expectancy_candidates(conn)
            _set_metadata(conn, "rebuilt_at", datetime.now(timezone.utc).isoformat())
            _set_metadata(conn, "source_flashcards_db", str(self.flashcards_db))
            _set_metadata(conn, "source_replay_db", str(self.replay_db))
            conn.commit()

            if report_path:
                report_path.parent.mkdir(parents=True, exist_ok=True)
                report_path.write_text(format_report(conn), encoding="utf-8")

            return IntelligenceBuildResult(
                occurrences=len(occurrences),
                setup_stats=setup_stats,
                price_level_stats=price_stats,
                day_session_stats=session_stats,
                cross_pair_stats=cross_stats,
                expectancy_candidates=expectancy_candidates,
                report_path=report_path,
            )
        finally:
            conn.close()

    def _load_source_rows(self, conn: sqlite3.Connection) -> list[sqlite3.Row]:
        if not self.flashcards_db.exists():
            raise FileNotFoundError(f"Flashcards DB not found: {self.flashcards_db}")
        if not self.replay_db.exists():
            raise FileNotFoundError(f"Replay DB not found: {self.replay_db}")
        conn.execute("ATTACH DATABASE ? AS replay_db", (str(self.replay_db),))
        conn.execute("ATTACH DATABASE ? AS flashcards_db", (str(self.flashcards_db),))
        return conn.execute(
            """SELECT
                s.id AS signature_id,
                s.source,
                s.source_id,
                s.symbol,
                s.timeframe,
                s.snapshot_at,
                s.direction,
                s.normalized_key,
                s.setup_family,
                s.primary_theme,
                o.id AS outcome_id,
                o.entry_price,
                o.stop_loss_price,
                o.t1_price,
                o.t2_price,
                o.sl_pips,
                o.t1_pips,
                o.t2_pips,
                o.exit_at,
                o.exit_pips,
                o.max_favorable_pips,
                o.max_adverse_pips,
                o.t1_hit,
                o.minutes_to_t1,
                o.outcome,
                o.event_path,
                f.chart_path,
                f.weekly_phase,
                f.weekly_trend,
                f.h4_level,
                f.h4_trend,
                f.h1_session,
                f.h1_trend,
                f.confluence_score,
                f.feature_close_to_ar_low_pips,
                f.feature_close_to_ar_mid_pips,
                f.feature_close_to_ar_high_pips,
                f.feature_close_to_hod_pips,
                f.feature_close_to_lod_pips,
                f.feature_range_pos
            FROM replay_db.mmm_setup_signatures s
            JOIN replay_db.mmm_event_outcomes o
              ON o.source = s.source AND o.source_id = s.source_id
            LEFT JOIN flashcards_db.flashcards f
              ON f.id = s.source_id
             AND s.source = 'historical_flashcard'
            WHERE s.source = 'historical_flashcard'
            ORDER BY s.symbol, s.snapshot_at""",
        ).fetchall()


def format_report(conn: sqlite3.Connection) -> str:
    _ensure_database_schema(conn)
    rebuilt_at = _metadata(conn, "rebuilt_at") or datetime.now(timezone.utc).isoformat()
    lines = [
        "# MMM Setup Intelligence Report",
        "",
        f"Generated: {rebuilt_at}",
        "",
        "This report is derived from historical flashcards and MMM event replay outcomes.",
        "It is a research/watchdog decision surface, not live execution approval.",
        "",
        "## Coverage",
        "",
    ]
    coverage = conn.execute(
        """SELECT symbol, COUNT(*) total, SUM(favorable) favorable,
                  AVG(exit_pips) avg_exit, MIN(snapshot_at) first_seen, MAX(snapshot_at) last_seen
        FROM setup_occurrences
        GROUP BY symbol
        ORDER BY symbol"""
    ).fetchall()
    lines.append("| Pair | Occurrences | Fav% | AvgExit | First Seen | Last Seen |")
    lines.append("|---|---:|---:|---:|---|---|")
    for row in coverage:
        fav_rate = _rate(row["favorable"], row["total"])
        lines.append(
            f"| {row['symbol']} | {row['total']} | {fav_rate:.1f}% | "
            f"{_fmt(row['avg_exit'])} | {_date(row['first_seen'])} | {_date(row['last_seen'])} |"
        )

    _append_setup_section(
        lines,
        conn,
        "Top Pair-Specific Setups",
        """SELECT * FROM setup_stats
        WHERE total >= 20
        ORDER BY opportunity_score DESC, favorable_rate DESC, avg_exit_pips DESC
        LIMIT 25""",
    )
    _append_rrs_section(lines, conn)
    _append_expectancy_candidates_section(lines, conn)
    _append_setup_section(
        lines,
        conn,
        "Positive-Expectancy Rate Exceptions",
        """SELECT * FROM setup_stats
        WHERE total >= 10
          AND positive_expectancy = 1
          AND favorable_rate < 85.0
        ORDER BY opportunity_score DESC, favorable_rate DESC, avg_exit_pips DESC
        LIMIT 25""",
    )
    _append_setup_section(
        lines,
        conn,
        "Fast-Profit Setups",
        """SELECT * FROM setup_stats
        WHERE total >= 10 AND fast_profit_rate > 0
        ORDER BY fast_profit_rate DESC, opportunity_score DESC
        LIMIT 20""",
    )
    _append_cross_pair_section(lines, conn)
    _append_price_level_section(lines, conn)
    _append_session_section(lines, conn)
    _append_decision_policy(lines)
    return "\n".join(lines) + "\n"


def format_expectancy_candidate_report(
    conn: sqlite3.Connection,
    *,
    tier: Optional[str] = None,
    symbol: Optional[str] = None,
    limit: int = 50,
) -> str:
    _ensure_database_schema(conn)
    clauses: list[str] = []
    params: list[Any] = []
    if tier:
        clauses.append("candidate_tier = ?")
        params.append(tier)
    if symbol:
        clauses.append("symbol = ?")
        params.append(symbol.upper())
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    params.append(limit)
    rows = conn.execute(
        f"""SELECT * FROM expectancy_candidates
        {where}
        ORDER BY CASE candidate_tier
            WHEN 'DEMO_CANDIDATE' THEN 0
            WHEN 'ASYMMETRIC_EXCEPTION' THEN 1
            ELSE 2
        END,
        opportunity_score DESC,
        profit_factor DESC,
        avg_exit_pips DESC
        LIMIT ?""",
        params,
    ).fetchall()
    if not rows:
        return "No expectancy-led research candidates matched the filters."
    lines = [
        "HELIX V3 EXPECTANCY-LED RESEARCH CANDIDATES",
        "Research-only; live validation library unchanged",
        "",
        (
            f"{'Pair':<8} {'Dir':<5} {'Tier':<22} {'RRS':<12} {'N':>5} "
            f"{'Fav%':>7} {'AvgExit':>9} {'PF':>6} {'Payoff':>7} {'Split':>5} Setup"
        ),
        "-" * 140,
    ]
    for row in rows:
        lines.append(
            f"{row['symbol']:<8} {row['direction']:<5} {row['candidate_tier']:<22} "
            f"{row['rrs_grade']:<12} {row['total']:>5} {row['favorable_rate']:>6.1f}% "
            f"{_fmt(row['avg_exit_pips']):>9} {row['profit_factor']:>6.2f} "
            f"{row['payoff_ratio']:>7.2f} {row['split_passes']:>2}/3   "
            f"{_short_key(row['normalized_key'], 72)}"
        )
    return "\n".join(lines)


def format_alert_only_basket_report(
    conn: sqlite3.Connection,
    *,
    limit: int = 25,
    symbol: Optional[str] = None,
) -> str:
    _ensure_database_schema(conn)
    clauses: list[str] = []
    params: list[Any] = []
    if symbol:
        clauses.append("symbol = ?")
        params.append(symbol.upper())
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    params.append(limit)
    rows = conn.execute(
        f"""SELECT * FROM expectancy_candidates
        {where}
        ORDER BY CASE candidate_tier
            WHEN 'DEMO_CANDIDATE' THEN 0
            WHEN 'ASYMMETRIC_EXCEPTION' THEN 1
            ELSE 2
        END,
        CASE rrs_grade
            WHEN 'R_RUNNER' THEN 0
            WHEN 'R_REPEATER' THEN 1
            ELSE 2
        END,
        split_passes DESC,
        profit_factor DESC,
        payoff_ratio DESC,
        avg_exit_pips DESC,
        total DESC
        LIMIT ?""",
        params,
    ).fetchall()

    generated_at = datetime.now(timezone.utc).isoformat()
    lines = [
        "# Alert-Only Demo Basket",
        "",
        f"Generated: {generated_at}",
        "",
        "This is an observation basket only. It does not promote validation-library records, "
        "place trades, or approve live execution.",
        "",
        "| Rank | Mode | Pair | Dir | Tier | RRS | N | Fav% | AvgExit | PF | Payoff | Splits | Session | Day | Setup |",
        "|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|",
    ]
    if not rows:
        lines.append("| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |")
    for rank, row in enumerate(rows, start=1):
        lines.append(
            f"| {rank} | {_basket_mode(row)} | {row['symbol']} | {row['direction']} | "
            f"{row['candidate_tier']} | {row['rrs_grade']} | {row['total']} | "
            f"{row['favorable_rate']:.1f}% | {_fmt(row['avg_exit_pips'])} | "
            f"{row['profit_factor']:.2f} | {row['payoff_ratio']:.2f} | "
            f"{row['split_passes']}/3 | {row['top_session'] or '-'} | "
            f"{row['top_day'] or '-'} | `{_short_key(row['normalized_key'], 72)}` |"
        )
    lines.extend(
        [
            "",
            "## Mode Rules",
            "",
            "- `DEMO_ALERT`: tradeable pair, `DEMO_CANDIDATE`; alert and forward-score only.",
            "- `WATCH_ALERT`: tradeable pair, still collecting evidence.",
            "- `ASYM_WATCH`: asymmetric/fat-tail candidate; inspect adverse excursion carefully.",
            "- `RESEARCH_ONLY`: analysis-only instrument or profile; no demo entry.",
            "",
            "Promotion still requires deterministic replay, visual audit, split stability, and explicit user approval.",
            "",
        ]
    )
    return "\n".join(lines)


def _occurrence_from_row(row: sqlite3.Row) -> dict[str, Any]:
    snapshot_at = _parse_time(row["snapshot_at"])
    favorable = str(row["outcome"]) in FAVORABLE_OUTCOMES
    fast_profit = bool(row["t1_hit"]) and (
        row["minutes_to_t1"] is not None and float(row["minutes_to_t1"]) <= 45.0
    )
    clean_departure = _clean_departure(
        favorable=favorable,
        max_adverse_pips=_optional_float(row["max_adverse_pips"]),
        sl_pips=_optional_float(row["sl_pips"]),
    )
    return {
        "source": row["source"],
        "source_id": row["source_id"],
        "signature_id": row["signature_id"],
        "outcome_id": row["outcome_id"],
        "symbol": row["symbol"],
        "timeframe": row["timeframe"],
        "snapshot_at": snapshot_at.isoformat(),
        "snapshot_date": snapshot_at.date().isoformat(),
        "day_of_week": DAY_NAMES[snapshot_at.weekday()],
        "hour_utc": snapshot_at.hour,
        "session": str(row["h1_session"] or _session_from_hour(snapshot_at.hour)),
        "direction": row["direction"],
        "normalized_key": row["normalized_key"],
        "setup_family": row["setup_family"],
        "primary_theme": row["primary_theme"],
        "weekly_phase": row["weekly_phase"],
        "weekly_trend": row["weekly_trend"],
        "h4_level": row["h4_level"],
        "h4_trend": row["h4_trend"],
        "h1_trend": row["h1_trend"],
        "confluence_score": row["confluence_score"],
        "entry_price": row["entry_price"],
        "stop_loss_price": row["stop_loss_price"],
        "t1_price": row["t1_price"],
        "t2_price": row["t2_price"],
        "sl_pips": row["sl_pips"],
        "t1_pips": row["t1_pips"],
        "t2_pips": row["t2_pips"],
        "exit_at": row["exit_at"],
        "exit_pips": row["exit_pips"],
        "max_favorable_pips": row["max_favorable_pips"],
        "max_adverse_pips": row["max_adverse_pips"],
        "t1_hit": int(bool(row["t1_hit"])),
        "minutes_to_t1": row["minutes_to_t1"],
        "outcome": row["outcome"],
        "event_path": row["event_path"],
        "favorable": int(favorable),
        "fast_profit": int(fast_profit),
        "clean_departure": int(clean_departure),
        "price_level_tag": _price_level_tag(row),
        "chart_path": row["chart_path"],
    }


def _insert_occurrences(conn: sqlite3.Connection, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    columns = list(rows[0].keys())
    placeholders = ",".join("?" for _ in columns)
    conn.executemany(
        f"""INSERT OR REPLACE INTO setup_occurrences
        ({','.join(columns)}) VALUES ({placeholders})""",
        [tuple(row[column] for column in columns) for row in rows],
    )


def _build_setup_stats(conn: sqlite3.Connection) -> int:
    groups = conn.execute(
        """SELECT symbol, direction, normalized_key, setup_family, primary_theme,
                  COUNT(*) total,
                  SUM(favorable) favorable,
                  SUM(t1_hit) t1_hits,
                  SUM(fast_profit) fast_profit,
                  SUM(clean_departure) clean_departure,
                  AVG(exit_pips) avg_exit_pips,
                  AVG(max_favorable_pips) avg_mfe,
                  AVG(max_adverse_pips) avg_mae,
                  MIN(snapshot_at) first_seen,
                  MAX(snapshot_at) last_seen
        FROM setup_occurrences
        GROUP BY symbol, direction, normalized_key, setup_family, primary_theme"""
    ).fetchall()
    inserted = 0
    for row in groups:
        first_seen = _parse_time(row["first_seen"])
        last_seen = _parse_time(row["last_seen"])
        active_days = max(1.0, (last_seen - first_seen).total_seconds() / 86400.0)
        recurrence = float(row["total"] or 0) / active_days * 30.0
        favorable_rate = _rate(row["favorable"], row["total"])
        t1_rate = _rate(row["t1_hits"], row["total"])
        fast_rate = _rate(row["fast_profit"], row["total"])
        clean_rate = _rate(row["clean_departure"], row["total"])
        reappearance_score = _reappearance_score(
            total=int(row["total"]),
            active_days=active_days,
            recurrence_per_30d=recurrence,
            last_seen=last_seen,
        )
        opportunity_score = _opportunity_score(
            total=int(row["total"]),
            favorable_rate=favorable_rate,
            avg_exit_pips=_optional_float(row["avg_exit_pips"]) or 0.0,
            fast_profit_rate=fast_rate,
            recurrence_per_30d=recurrence,
        )
        avg_exit = _optional_float(row["avg_exit_pips"]) or 0.0
        conn.execute(
            """INSERT INTO setup_stats (
                symbol, direction, normalized_key, setup_family, primary_theme,
                total, favorable, favorable_rate, t1_rate, fast_profit_rate,
                clean_departure_rate, avg_exit_pips, avg_mfe, avg_mae,
                first_seen, last_seen, active_days, recurrence_per_30d,
                reappearance_score, opportunity_score, top_session, top_day,
                top_price_level, example_flashcards, rrs_grade, positive_expectancy,
                decision
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                row["symbol"],
                row["direction"],
                row["normalized_key"],
                row["setup_family"],
                row["primary_theme"],
                row["total"],
                row["favorable"],
                favorable_rate,
                t1_rate,
                fast_rate,
                clean_rate,
                row["avg_exit_pips"],
                row["avg_mfe"],
                row["avg_mae"],
                row["first_seen"],
                row["last_seen"],
                active_days,
                recurrence,
                reappearance_score,
                opportunity_score,
                _top_value(conn, row, "session"),
                _top_value(conn, row, "day_of_week"),
                _top_value(conn, row, "price_level_tag"),
                json.dumps(_example_flashcards(conn, row)),
                rrs_grade(favorable_rate),
                int(avg_exit > 0.0),
                _decision(
                    total=int(row["total"]),
                    favorable_rate=favorable_rate,
                    avg_exit_pips=avg_exit,
                    fast_profit_rate=fast_rate,
                ),
            ),
        )
        inserted += 1
    return inserted


def _build_price_level_stats(conn: sqlite3.Connection) -> int:
    rows = conn.execute(
        """SELECT symbol, direction, price_level_tag,
                  COUNT(*) total, SUM(favorable) favorable,
                  SUM(fast_profit) fast_profit,
                  SUM(clean_departure) clean_departure,
                  AVG(exit_pips) avg_exit_pips,
                  AVG(max_favorable_pips) avg_mfe,
                  AVG(max_adverse_pips) avg_mae,
                  AVG(entry_price) avg_entry_price
        FROM setup_occurrences
        GROUP BY symbol, direction, price_level_tag"""
    ).fetchall()
    for row in rows:
        conn.execute(
            """INSERT INTO price_level_stats (
                symbol, direction, price_level_tag, total, favorable, favorable_rate,
                fast_profit_rate, clean_departure_rate, avg_exit_pips, avg_mfe,
                avg_mae, avg_entry_price
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                row["symbol"],
                row["direction"],
                row["price_level_tag"],
                row["total"],
                row["favorable"],
                _rate(row["favorable"], row["total"]),
                _rate(row["fast_profit"], row["total"]),
                _rate(row["clean_departure"], row["total"]),
                row["avg_exit_pips"],
                row["avg_mfe"],
                row["avg_mae"],
                row["avg_entry_price"],
            ),
        )
    return len(rows)


def _build_day_session_stats(conn: sqlite3.Connection) -> int:
    rows = conn.execute(
        """SELECT symbol, direction, day_of_week, session,
                  COUNT(*) total, SUM(favorable) favorable,
                  SUM(fast_profit) fast_profit,
                  AVG(exit_pips) avg_exit_pips,
                  AVG(max_favorable_pips) avg_mfe,
                  AVG(max_adverse_pips) avg_mae
        FROM setup_occurrences
        GROUP BY symbol, direction, day_of_week, session"""
    ).fetchall()
    for row in rows:
        conn.execute(
            """INSERT INTO day_session_stats (
                symbol, direction, day_of_week, session, total, favorable,
                favorable_rate, fast_profit_rate, avg_exit_pips, avg_mfe, avg_mae
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                row["symbol"],
                row["direction"],
                row["day_of_week"],
                row["session"],
                row["total"],
                row["favorable"],
                _rate(row["favorable"], row["total"]),
                _rate(row["fast_profit"], row["total"]),
                row["avg_exit_pips"],
                row["avg_mfe"],
                row["avg_mae"],
            ),
        )
    return len(rows)


def _build_cross_pair_stats(conn: sqlite3.Connection) -> int:
    rows = conn.execute(
        """SELECT direction, normalized_key, setup_family,
                  GROUP_CONCAT(DISTINCT symbol) symbols,
                  COUNT(DISTINCT symbol) symbol_count,
                  COUNT(*) total,
                  SUM(favorable) favorable,
                  SUM(fast_profit) fast_profit,
                  AVG(exit_pips) avg_exit_pips
        FROM setup_occurrences
        GROUP BY direction, normalized_key, setup_family
        HAVING symbol_count >= 2"""
    ).fetchall()
    for row in rows:
        favorable_rate = _rate(row["favorable"], row["total"])
        fast_rate = _rate(row["fast_profit"], row["total"])
        avg_exit = _optional_float(row["avg_exit_pips"]) or 0.0
        opportunity_score = _opportunity_score(
            total=int(row["total"]),
            favorable_rate=favorable_rate,
            avg_exit_pips=avg_exit,
            fast_profit_rate=fast_rate,
            recurrence_per_30d=0.0,
        )
        conn.execute(
            """INSERT INTO cross_pair_stats (
                direction, normalized_key, setup_family, symbols, symbol_count,
                total, favorable, favorable_rate, avg_exit_pips, fast_profit_rate,
                rrs_grade, positive_expectancy, top_session, top_day, opportunity_score
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                row["direction"],
                row["normalized_key"],
                row["setup_family"],
                row["symbols"],
                row["symbol_count"],
                row["total"],
                row["favorable"],
                favorable_rate,
                row["avg_exit_pips"],
                fast_rate,
                rrs_grade(favorable_rate),
                int(avg_exit > 0.0),
                _top_cross_value(conn, row, "session"),
                _top_cross_value(conn, row, "day_of_week"),
                opportunity_score,
            ),
        )
    return len(rows)


def _build_expectancy_candidates(conn: sqlite3.Connection) -> int:
    rows = conn.execute(
        """SELECT
                  ss.*,
                  COALESCE(SUM(CASE WHEN o.exit_pips > 0 THEN o.exit_pips ELSE 0 END), 0)
                      AS gross_profit_pips,
                  ABS(COALESCE(SUM(CASE WHEN o.exit_pips < 0 THEN o.exit_pips ELSE 0 END), 0))
                      AS gross_loss_pips,
                  AVG(CASE WHEN o.exit_pips > 0 THEN o.exit_pips END) AS avg_win_pips,
                  AVG(CASE WHEN o.exit_pips < 0 THEN o.exit_pips END) AS avg_loss_pips
        FROM setup_stats ss
        JOIN setup_occurrences o
          ON o.symbol = ss.symbol
         AND o.direction = ss.direction
         AND o.normalized_key = ss.normalized_key
        WHERE ss.total >= 10
          AND ss.positive_expectancy = 1
        GROUP BY ss.id
        ORDER BY ss.opportunity_score DESC"""
    ).fetchall()

    inserted = 0
    for row in rows:
        gross_profit = float(row["gross_profit_pips"] or 0.0)
        gross_loss = float(row["gross_loss_pips"] or 0.0)
        avg_win = _optional_float(row["avg_win_pips"])
        avg_loss = _optional_float(row["avg_loss_pips"])
        profit_factor = _profit_factor(gross_profit, gross_loss)
        payoff_ratio = _payoff_ratio(avg_win, avg_loss)
        split_passes, split_summary = _split_stability(
            conn,
            symbol=str(row["symbol"]),
            direction=str(row["direction"]),
            normalized_key=str(row["normalized_key"]),
        )
        candidate_tier = expectancy_candidate_tier(
            total=int(row["total"] or 0),
            rrs=str(row["rrs_grade"] or ""),
            favorable_rate=float(row["favorable_rate"] or 0.0),
            avg_exit_pips=_optional_float(row["avg_exit_pips"]) or 0.0,
            profit_factor=profit_factor,
            payoff_ratio=payoff_ratio,
            split_passes=split_passes,
        )
        if candidate_tier == "REJECT_EXPECTANCY":
            continue
        conn.execute(
            """INSERT INTO expectancy_candidates (
                symbol, direction, normalized_key, setup_family, primary_theme,
                rrs_grade, candidate_tier, total, favorable, favorable_rate,
                t1_rate, fast_profit_rate, clean_departure_rate, avg_exit_pips,
                avg_win_pips, avg_loss_pips, gross_profit_pips, gross_loss_pips,
                profit_factor, payoff_ratio, avg_mfe, avg_mae, split_passes,
                split_summary, recurrence_per_30d, reappearance_score,
                opportunity_score, top_session, top_day, top_price_level,
                example_flashcards, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                row["symbol"],
                row["direction"],
                row["normalized_key"],
                row["setup_family"],
                row["primary_theme"],
                row["rrs_grade"],
                candidate_tier,
                row["total"],
                row["favorable"],
                row["favorable_rate"],
                row["t1_rate"],
                row["fast_profit_rate"],
                row["clean_departure_rate"],
                row["avg_exit_pips"],
                avg_win,
                avg_loss,
                gross_profit,
                gross_loss,
                profit_factor,
                payoff_ratio,
                row["avg_mfe"],
                row["avg_mae"],
                split_passes,
                split_summary,
                row["recurrence_per_30d"],
                row["reappearance_score"],
                row["opportunity_score"],
                row["top_session"],
                row["top_day"],
                row["top_price_level"],
                row["example_flashcards"],
                _expectancy_notes(candidate_tier, str(row["rrs_grade"] or "")),
            ),
        )
        inserted += 1
    return inserted


def _append_setup_section(
    lines: list[str],
    conn: sqlite3.Connection,
    title: str,
    sql: str,
) -> None:
    lines.extend(["", f"## {title}", ""])
    rows = conn.execute(sql).fetchall()
    if not rows:
        lines.append("No setup rows met this section's threshold.")
        return
    lines.append(
        "| Pair | Dir | RRS | N | Fav% | AvgExit | Fast% | Recur/30d | Reappear | Opp | Decision | Setup |"
    )
    lines.append("|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|")
    for row in rows:
        lines.append(
            f"| {row['symbol']} | {row['direction']} | {row['rrs_grade']} | "
            f"{row['total']} | "
            f"{row['favorable_rate']:.1f}% | {_fmt(row['avg_exit_pips'])} | "
            f"{row['fast_profit_rate']:.1f}% | {row['recurrence_per_30d']:.2f} | "
            f"{row['reappearance_score']:.1f} | {row['opportunity_score']:.1f} | "
            f"{row['decision']} | `{_short_key(row['normalized_key'])}` |"
        )


def _append_rrs_section(lines: list[str], conn: sqlite3.Connection) -> None:
    lines.extend(["", "## RRS Performance Bands", ""])
    lines.extend(
        [
            "`R_RUNNER` means Fav >= 75%. `R_REPEATER` means Fav >= 50% and < 75%.",
            "`S_STRANGER` means Fav < 50%. Positive-expectancy rows have AvgExit > 0.",
            "",
        ]
    )
    rows = conn.execute(
        """SELECT rrs_grade,
                  COUNT(*) setup_rows,
                  SUM(total) occurrences,
                  SUM(positive_expectancy) positive_rows,
                  AVG(favorable_rate) avg_fav_rate,
                  AVG(avg_exit_pips) avg_exit_pips,
                  AVG(opportunity_score) avg_opportunity
        FROM setup_stats
        WHERE total >= 10
        GROUP BY rrs_grade
        ORDER BY CASE rrs_grade
            WHEN 'R_RUNNER' THEN 0
            WHEN 'R_REPEATER' THEN 1
            ELSE 2
        END"""
    ).fetchall()
    if not rows:
        lines.append("No setup rows met the RRS threshold.")
        return
    lines.append("| RRS | Setup Rows | Occurrences | Positive Rows | AvgFav% | AvgExit | AvgOpp |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for row in rows:
        lines.append(
            f"| {row['rrs_grade']} | {row['setup_rows']} | {row['occurrences']} | "
            f"{row['positive_rows']} | {row['avg_fav_rate']:.1f}% | "
            f"{_fmt(row['avg_exit_pips'])} | {row['avg_opportunity']:.1f} |"
        )


def _append_expectancy_candidates_section(lines: list[str], conn: sqlite3.Connection) -> None:
    lines.extend(["", "## Expectancy-Led Research Candidates", ""])
    lines.extend(
        [
            "These rows are research-only. They are not inserted into the live validation library.",
            "",
        ]
    )
    summary = conn.execute(
        """SELECT candidate_tier, rrs_grade, COUNT(*) rows, SUM(total) occurrences,
                  AVG(favorable_rate) avg_fav_rate,
                  AVG(avg_exit_pips) avg_exit_pips,
                  AVG(profit_factor) avg_profit_factor
        FROM expectancy_candidates
        GROUP BY candidate_tier, rrs_grade
        ORDER BY CASE candidate_tier
            WHEN 'DEMO_CANDIDATE' THEN 0
            WHEN 'ASYMMETRIC_EXCEPTION' THEN 1
            ELSE 2
        END,
        CASE rrs_grade
            WHEN 'R_RUNNER' THEN 0
            WHEN 'R_REPEATER' THEN 1
            ELSE 2
        END"""
    ).fetchall()
    if not summary:
        lines.append("No expectancy candidates met the research threshold.")
        return

    lines.append("| Tier | RRS | Rows | Occurrences | AvgFav% | AvgExit | AvgPF |")
    lines.append("|---|---|---:|---:|---:|---:|---:|")
    for row in summary:
        lines.append(
            f"| {row['candidate_tier']} | {row['rrs_grade']} | {row['rows']} | "
            f"{row['occurrences']} | {row['avg_fav_rate']:.1f}% | "
            f"{_fmt(row['avg_exit_pips'])} | {row['avg_profit_factor']:.2f} |"
        )

    rows = conn.execute(
        """SELECT * FROM expectancy_candidates
        ORDER BY CASE candidate_tier
            WHEN 'DEMO_CANDIDATE' THEN 0
            WHEN 'ASYMMETRIC_EXCEPTION' THEN 1
            ELSE 2
        END,
        opportunity_score DESC,
        profit_factor DESC,
        avg_exit_pips DESC
        LIMIT 25"""
    ).fetchall()
    lines.extend(["", "| Pair | Dir | Tier | RRS | N | Fav% | AvgExit | PF | Payoff | Splits | Opp | Setup |"])
    lines.append("|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|")
    for row in rows:
        lines.append(
            f"| {row['symbol']} | {row['direction']} | {row['candidate_tier']} | "
            f"{row['rrs_grade']} | {row['total']} | {row['favorable_rate']:.1f}% | "
            f"{_fmt(row['avg_exit_pips'])} | {row['profit_factor']:.2f} | "
            f"{row['payoff_ratio']:.2f} | {row['split_passes']}/3 | "
            f"{row['opportunity_score']:.1f} | `{_short_key(row['normalized_key'])}` |"
        )


def _append_cross_pair_section(lines: list[str], conn: sqlite3.Connection) -> None:
    lines.extend(["", "## Cross-Pair Recurrence", ""])
    rows = conn.execute(
        """SELECT * FROM cross_pair_stats
        WHERE total >= 20
        ORDER BY opportunity_score DESC, symbol_count DESC, favorable_rate DESC
        LIMIT 20"""
    ).fetchall()
    if not rows:
        lines.append("No cross-pair setup rows met the report threshold.")
        return
    lines.append("| Dir | RRS | Symbols | N | Fav% | AvgExit | Fast% | Top Session | Setup |")
    lines.append("|---|---|---|---:|---:|---:|---:|---|---|")
    for row in rows:
        lines.append(
            f"| {row['direction']} | {row['rrs_grade']} | {row['symbols']} | {row['total']} | "
            f"{row['favorable_rate']:.1f}% | {_fmt(row['avg_exit_pips'])} | "
            f"{row['fast_profit_rate']:.1f}% | {row['top_session'] or '-'} | "
            f"`{_short_key(row['normalized_key'])}` |"
        )


def _append_price_level_section(lines: list[str], conn: sqlite3.Connection) -> None:
    lines.extend(["", "## Price-Level Departures", ""])
    rows = conn.execute(
        """SELECT * FROM price_level_stats
        WHERE total >= 20
        ORDER BY fast_profit_rate DESC, favorable_rate DESC, avg_exit_pips DESC
        LIMIT 25"""
    ).fetchall()
    if not rows:
        lines.append("No price-level rows met the report threshold.")
        return
    lines.append("| Pair | Dir | Level | N | Fav% | Fast% | Clean% | AvgExit | AvgEntry |")
    lines.append("|---|---|---|---:|---:|---:|---:|---:|---:|")
    for row in rows:
        lines.append(
            f"| {row['symbol']} | {row['direction']} | {row['price_level_tag']} | "
            f"{row['total']} | {row['favorable_rate']:.1f}% | "
            f"{row['fast_profit_rate']:.1f}% | {row['clean_departure_rate']:.1f}% | "
            f"{_fmt(row['avg_exit_pips'])} | {_fmt_price(row['avg_entry_price'])} |"
        )


def _append_session_section(lines: list[str], conn: sqlite3.Connection) -> None:
    lines.extend(["", "## Day And Session Edge", ""])
    rows = conn.execute(
        """SELECT * FROM day_session_stats
        WHERE total >= 20
        ORDER BY favorable_rate DESC, avg_exit_pips DESC
        LIMIT 25"""
    ).fetchall()
    if not rows:
        lines.append("No day/session rows met the report threshold.")
        return
    lines.append("| Pair | Dir | Day | Session | N | Fav% | Fast% | AvgExit |")
    lines.append("|---|---|---|---|---:|---:|---:|---:|")
    for row in rows:
        lines.append(
            f"| {row['symbol']} | {row['direction']} | {row['day_of_week']} | "
            f"{row['session']} | {row['total']} | {row['favorable_rate']:.1f}% | "
            f"{row['fast_profit_rate']:.1f}% | {_fmt(row['avg_exit_pips'])} |"
        )


def _append_decision_policy(lines: list[str]) -> None:
    lines.extend(
        [
            "",
            "## Decision Policy",
            "",
            "- `PROMOTE_CANDIDATE`: enough sample and positive edge for supervised demo/watchdog testing.",
            "- `WATCH_RESEARCH`: usable for alerting and further sampling, not live execution.",
            "- `REJECT_OR_REFINE`: weak edge or sparse sample; do not trade as-is.",
            "- RRS is a favorable-rate band for analysis, not a live execution gate.",
            "- Positive-expectancy rate exceptions are setup rows below the old 85% scanner rate",
            "  bar that still have AvgExit > 0 and enough sample for review.",
            "- `DEMO_CANDIDATE`, `WATCH_CANDIDATE`, and `ASYMMETRIC_EXCEPTION` are",
            "  expectancy-led research tiers. They are not inserted into `validation_setups`.",
            "",
            "Fast-profit means T1 was reached within 45 minutes. Clean departure means the setup was",
            "favorable and adverse excursion stayed within a conservative SL-relative bound.",
        ]
    )


def _price_level_tag(row: sqlite3.Row) -> str:
    candidates = {
        "AR_LOW": _optional_float(row["feature_close_to_ar_low_pips"]),
        "AR_MID": _optional_float(row["feature_close_to_ar_mid_pips"]),
        "AR_HIGH": _optional_float(row["feature_close_to_ar_high_pips"]),
        "HOD": _optional_float(row["feature_close_to_hod_pips"]),
        "LOD": _optional_float(row["feature_close_to_lod_pips"]),
    }
    near = [
        (name, abs(value))
        for name, value in candidates.items()
        if value is not None and abs(value) <= (8.0 if name in {"HOD", "LOD"} else 5.0)
    ]
    if near:
        return min(near, key=lambda item: item[1])[0]
    range_pos = _optional_float(row["feature_range_pos"])
    if range_pos is None:
        return "UNCLASSIFIED"
    if range_pos <= 0.2:
        return "AR_LOWER_QUINTILE"
    if range_pos <= 0.4:
        return "AR_LOWER_MID"
    if range_pos <= 0.6:
        return "AR_MID_ZONE"
    if range_pos <= 0.8:
        return "AR_UPPER_MID"
    return "AR_UPPER_QUINTILE"


def _clean_departure(
    *,
    favorable: bool,
    max_adverse_pips: Optional[float],
    sl_pips: Optional[float],
) -> bool:
    if not favorable or max_adverse_pips is None:
        return False
    threshold = 10.0
    if sl_pips and sl_pips > 0:
        threshold = min(threshold, sl_pips * 0.35)
    return abs(max_adverse_pips) <= threshold


def _top_value(conn: sqlite3.Connection, row: sqlite3.Row, column: str) -> str:
    result = conn.execute(
        f"""SELECT {column} value, COUNT(*) total
        FROM setup_occurrences
        WHERE symbol = ? AND direction = ? AND normalized_key = ?
        GROUP BY {column}
        ORDER BY total DESC, value
        LIMIT 1""",
        (row["symbol"], row["direction"], row["normalized_key"]),
    ).fetchone()
    return str(result["value"]) if result else ""


def _top_cross_value(conn: sqlite3.Connection, row: sqlite3.Row, column: str) -> str:
    result = conn.execute(
        f"""SELECT {column} value, COUNT(*) total
        FROM setup_occurrences
        WHERE direction = ? AND normalized_key = ?
        GROUP BY {column}
        ORDER BY total DESC, value
        LIMIT 1""",
        (row["direction"], row["normalized_key"]),
    ).fetchone()
    return str(result["value"]) if result else ""


def _example_flashcards(conn: sqlite3.Connection, row: sqlite3.Row, limit: int = 5) -> list[int]:
    rows = conn.execute(
        """SELECT source_id
        FROM setup_occurrences
        WHERE symbol = ? AND direction = ? AND normalized_key = ?
        ORDER BY favorable DESC, exit_pips DESC
        LIMIT ?""",
        (row["symbol"], row["direction"], row["normalized_key"], limit),
    ).fetchall()
    return [int(item["source_id"]) for item in rows]


def _reappearance_score(
    *,
    total: int,
    active_days: float,
    recurrence_per_30d: float,
    last_seen: datetime,
) -> float:
    sample_score = min(1.0, total / 50.0)
    recurrence_score = min(1.0, recurrence_per_30d / 5.0)
    age_days = max(0.0, (datetime.now(timezone.utc) - last_seen).total_seconds() / 86400.0)
    recency_score = max(0.0, 1.0 - min(1.0, age_days / 365.0))
    coverage_score = min(1.0, active_days / 365.0)
    return round(100.0 * (
        0.35 * sample_score
        + 0.35 * recurrence_score
        + 0.20 * recency_score
        + 0.10 * coverage_score
    ), 1)


def _opportunity_score(
    *,
    total: int,
    favorable_rate: float,
    avg_exit_pips: float,
    fast_profit_rate: float,
    recurrence_per_30d: float,
) -> float:
    sample_score = min(1.0, total / 50.0)
    edge_score = max(0.0, min(1.0, favorable_rate / 100.0))
    profit_score = max(0.0, min(1.0, (avg_exit_pips + 10.0) / 40.0))
    fast_score = max(0.0, min(1.0, fast_profit_rate / 100.0))
    recurrence_score = max(0.0, min(1.0, recurrence_per_30d / 5.0))
    return round(100.0 * (
        0.30 * edge_score
        + 0.25 * profit_score
        + 0.20 * sample_score
        + 0.15 * fast_score
        + 0.10 * recurrence_score
    ), 1)


def _decision(
    *,
    total: int,
    favorable_rate: float,
    avg_exit_pips: float,
    fast_profit_rate: float,
) -> str:
    if total >= 30 and favorable_rate >= 60.0 and avg_exit_pips >= 5.0 and fast_profit_rate >= 10.0:
        return "PROMOTE_CANDIDATE"
    if total >= 10 and favorable_rate >= 50.0 and avg_exit_pips > 0.0:
        return "WATCH_RESEARCH"
    return "REJECT_OR_REFINE"


def expectancy_candidate_tier(
    *,
    total: int,
    rrs: str,
    favorable_rate: float,
    avg_exit_pips: float,
    profit_factor: float,
    payoff_ratio: float,
    split_passes: int,
) -> str:
    if total < 10 or avg_exit_pips <= 0.0 or profit_factor < 1.05:
        return "REJECT_EXPECTANCY"
    if rrs == "R_RUNNER" or favorable_rate >= 75.0:
        if split_passes >= 2 and profit_factor >= 1.10:
            return "DEMO_CANDIDATE"
        return "WATCH_CANDIDATE"
    if rrs == "R_REPEATER" or favorable_rate >= 50.0:
        if split_passes >= 2 and profit_factor >= 1.15 and avg_exit_pips >= 3.0:
            return "DEMO_CANDIDATE"
        return "WATCH_CANDIDATE"
    if (
        split_passes >= 2
        and profit_factor >= 1.50
        and payoff_ratio >= 2.0
        and avg_exit_pips >= 5.0
    ):
        return "ASYMMETRIC_EXCEPTION"
    if split_passes >= 1 and profit_factor >= 1.25 and payoff_ratio >= 1.5:
        return "WATCH_CANDIDATE"
    return "REJECT_EXPECTANCY"


def _profit_factor(gross_profit_pips: float, gross_loss_pips: float) -> float:
    if gross_loss_pips <= 0.0:
        return 999.0 if gross_profit_pips > 0.0 else 0.0
    return round(max(0.0, gross_profit_pips) / gross_loss_pips, 2)


def _payoff_ratio(avg_win_pips: Optional[float], avg_loss_pips: Optional[float]) -> float:
    win = avg_win_pips or 0.0
    loss = abs(avg_loss_pips or 0.0)
    if loss <= 0.0:
        return 999.0 if win > 0.0 else 0.0
    return round(max(0.0, win) / loss, 2)


def _split_stability(
    conn: sqlite3.Connection,
    *,
    symbol: str,
    direction: str,
    normalized_key: str,
    split_min_total: int = 3,
) -> tuple[int, str]:
    rows = conn.execute(
        """SELECT exit_pips
        FROM setup_occurrences
        WHERE symbol = ? AND direction = ? AND normalized_key = ?
        ORDER BY snapshot_at""",
        (symbol, direction, normalized_key),
    ).fetchall()
    values: list[float] = []
    for row in rows:
        value = _optional_float(row["exit_pips"])
        if value is not None:
            values.append(value)
    if not values:
        return 0, "train:N=0,Avg=+0.0; validation:N=0,Avg=+0.0; oos:N=0,Avg=+0.0"

    labels = ("train", "validation", "oos")
    slices = _chronological_slices(values, parts=3)
    passes = 0
    summaries: list[str] = []
    for label, split_values in zip(labels, slices):
        avg = sum(split_values) / len(split_values) if split_values else 0.0
        if len(split_values) >= split_min_total and avg > 0.0:
            passes += 1
        summaries.append(f"{label}:N={len(split_values)},Avg={avg:+.1f}")
    return passes, "; ".join(summaries)


def _chronological_slices(values: list[float], *, parts: int) -> list[list[float]]:
    if parts <= 0:
        return []
    base = len(values) // parts
    remainder = len(values) % parts
    slices: list[list[float]] = []
    start = 0
    for index in range(parts):
        size = base + (1 if index < remainder else 0)
        end = start + size
        slices.append(values[start:end])
        start = end
    return slices


def _expectancy_notes(candidate_tier: str, rrs: str) -> str:
    if candidate_tier == "DEMO_CANDIDATE":
        return "Research-only: qualifies for supervised demo/watchdog review, not live approval."
    if candidate_tier == "ASYMMETRIC_EXCEPTION":
        return (
            "Research-only fat-tail candidate: audit payoff, point value, and adverse excursion "
            "before demo use."
        )
    return f"Research-only {rrs} candidate: keep collecting evidence before promotion."


def _basket_mode(row: sqlite3.Row) -> str:
    symbol = str(row["symbol"] or "").upper()
    try:
        profile = get_pair_profile(symbol)
    except Exception:
        return "RESEARCH_ONLY"
    if not profile.tradeable:
        return "RESEARCH_ONLY"
    tier = str(row["candidate_tier"] or "")
    if tier == "DEMO_CANDIDATE":
        return "DEMO_ALERT"
    if tier == "ASYMMETRIC_EXCEPTION":
        return "ASYM_WATCH"
    return "WATCH_ALERT"


def rrs_grade(favorable_rate: float) -> str:
    if favorable_rate >= 75.0:
        return "R_RUNNER"
    if favorable_rate >= 50.0:
        return "R_REPEATER"
    return "S_STRANGER"


def _ensure_schema_columns(conn: sqlite3.Connection) -> None:
    _ensure_columns(
        conn,
        "setup_stats",
        {
            "rrs_grade": "TEXT NOT NULL DEFAULT ''",
            "positive_expectancy": "INTEGER NOT NULL DEFAULT 0",
        },
    )
    _ensure_columns(
        conn,
        "cross_pair_stats",
        {
            "rrs_grade": "TEXT NOT NULL DEFAULT ''",
            "positive_expectancy": "INTEGER NOT NULL DEFAULT 0",
        },
    )


def _ensure_database_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    _ensure_schema_columns(conn)


def _ensure_columns(
    conn: sqlite3.Connection,
    table: str,
    columns: dict[str, str],
) -> None:
    existing = {
        str(row["name"])
        for row in conn.execute(f"PRAGMA table_info({table})").fetchall()
    }
    for column, column_type in columns.items():
        if column not in existing:
            conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {column_type}")


def _clear_tables(conn: sqlite3.Connection) -> None:
    for table in (
        "setup_occurrences",
        "setup_stats",
        "price_level_stats",
        "day_session_stats",
        "cross_pair_stats",
        "expectancy_candidates",
        "intelligence_metadata",
    ):
        conn.execute(f"DELETE FROM {table}")


def _set_metadata(conn: sqlite3.Connection, key: str, value: str) -> None:
    conn.execute(
        """INSERT OR REPLACE INTO intelligence_metadata (key, value) VALUES (?, ?)""",
        (key, value),
    )


def _metadata(conn: sqlite3.Connection, key: str) -> str:
    row = conn.execute(
        "SELECT value FROM intelligence_metadata WHERE key = ?",
        (key,),
    ).fetchone()
    return str(row["value"]) if row else ""


def _rate(numerator: Any, denominator: Any) -> float:
    total = int(denominator or 0)
    if total <= 0:
        return 0.0
    return float(numerator or 0) / total * 100.0


def _parse_time(value: Any) -> datetime:
    if isinstance(value, datetime):
        dt = value
    else:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _session_from_hour(hour: int) -> str:
    if 0 <= hour < 7:
        return "ASIA"
    if 7 <= hour < 13:
        return "LONDON"
    if 13 <= hour < 16:
        return "NY_OVERLAP"
    if 16 <= hour < 22:
        return "NY_LATE"
    return "DEAD_GAP"


def _optional_float(value: Any) -> Optional[float]:
    try:
        if value is None:
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def _fmt(value: Any) -> str:
    number = _optional_float(value)
    if number is None:
        return "-"
    return f"{number:+.1f}"


def _fmt_price(value: Any) -> str:
    number = _optional_float(value)
    if number is None:
        return "-"
    return f"{number:.5f}"


def _date(value: Any) -> str:
    if not value:
        return "-"
    return _parse_time(value).date().isoformat()


def _short_key(key: str, max_len: int = 76) -> str:
    if len(key) <= max_len:
        return key
    return key[: max_len - 3] + "..."


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Build MMM setup intelligence database")
    sub = parser.add_subparsers(dest="command", required=True)

    p_rebuild = sub.add_parser("rebuild", help="Rebuild derived setup intelligence")
    p_rebuild.add_argument("--flashcards-db", type=Path, default=FLASHCARDS_DB_PATH)
    p_rebuild.add_argument("--replay-db", type=Path, default=REPLAY_DB_PATH)
    p_rebuild.add_argument("--output-db", type=Path, default=DEFAULT_INTELLIGENCE_DB_PATH)
    p_rebuild.add_argument("--report-path", type=Path, default=DEFAULT_REPORT_PATH)

    p_report = sub.add_parser("report", help="Print the generated report")
    p_report.add_argument("--output-db", type=Path, default=DEFAULT_INTELLIGENCE_DB_PATH)

    p_expectancy = sub.add_parser(
        "expectancy-report",
        help="Print expectancy-led research candidates only",
    )
    p_expectancy.add_argument("--output-db", type=Path, default=DEFAULT_INTELLIGENCE_DB_PATH)
    p_expectancy.add_argument(
        "--tier",
        choices=("DEMO_CANDIDATE", "WATCH_CANDIDATE", "ASYMMETRIC_EXCEPTION"),
    )
    p_expectancy.add_argument("--symbol")
    p_expectancy.add_argument("--limit", type=int, default=50)

    p_basket = sub.add_parser(
        "basket-report",
        help="Write an RRS/expectancy-ranked alert-only demo basket",
    )
    p_basket.add_argument("--output-db", type=Path, default=DEFAULT_INTELLIGENCE_DB_PATH)
    p_basket.add_argument("--report-path", type=Path, default=DEFAULT_BASKET_REPORT_PATH)
    p_basket.add_argument("--symbol")
    p_basket.add_argument("--limit", type=int, default=25)

    args = parser.parse_args(argv)
    if args.command == "rebuild":
        result = SetupIntelligenceBuilder(
            flashcards_db=args.flashcards_db,
            replay_db=args.replay_db,
            output_db=args.output_db,
        ).rebuild(report_path=args.report_path)
        print(
            "Setup intelligence rebuilt: "
            f"{result.occurrences} occurrences, "
            f"{result.setup_stats} setup stats, "
            f"{result.price_level_stats} price-level stats, "
            f"{result.day_session_stats} day/session stats, "
            f"{result.cross_pair_stats} cross-pair stats, "
            f"{result.expectancy_candidates} expectancy candidates."
        )
        if result.report_path:
            print(f"Report: {result.report_path}")
    elif args.command == "report":
        conn = sqlite3.connect(str(args.output_db))
        conn.row_factory = sqlite3.Row
        try:
            print(format_report(conn))
        finally:
            conn.close()
    elif args.command == "expectancy-report":
        conn = sqlite3.connect(str(args.output_db))
        conn.row_factory = sqlite3.Row
        try:
            print(
                format_expectancy_candidate_report(
                    conn,
                    tier=args.tier,
                    symbol=args.symbol,
                    limit=args.limit,
                )
            )
        finally:
            conn.close()
    elif args.command == "basket-report":
        conn = sqlite3.connect(str(args.output_db))
        conn.row_factory = sqlite3.Row
        try:
            report = format_alert_only_basket_report(
                conn,
                symbol=args.symbol,
                limit=args.limit,
            )
            args.report_path.parent.mkdir(parents=True, exist_ok=True)
            args.report_path.write_text(report + "\n", encoding="utf-8")
            print(report)
            print(f"\nReport: {args.report_path}")
        finally:
            conn.close()


if __name__ == "__main__":
    main()
