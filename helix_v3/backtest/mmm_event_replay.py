"""MMM event-based replay and setup-signature analysis.

This module is intentionally offline-only. It labels flashcards/model snapshots
against the trade-management rules documented in CLAUDE.md:

- pair-specific Asian range and structural SL
- T1 at 1R, then SL to breakeven
- 90 minute stale exit only if the trade is not in profit
- pair-specific trailing and max-duration exits

The fixed-horizon replay remains useful as a diagnostic, but this module is the
MMM-aligned evaluator for setup mining and model calibration.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import asdict, dataclass, field, replace
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Iterable, Optional

import pandas as pd

from config.pair_profiles import PairProfile, get_pair_profile
from config.settings import settings
from helix_v3.core.advisory_confidence import AdvisorySetup, score_advisory_setup
from helix_v3.core.patterns import scan_patterns
from helix_v3.core.sessions import classify_sessions, get_today_asian_range
from helix_v3.core.tdi import compute_daily_hilo, compute_tdi
from helix_v3.core.types import Direction
from helix_v3.journal.flashcards import FlashcardSystem
from helix_v3.utils.logger import get_logger

logger = get_logger("mmm_event_replay")

DEFAULT_DB_PATH = Path(settings.log_dir) / "vision_backtests.db"
FLASHCARDS_DB_PATH = Path(settings.log_dir) / "flashcards.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS mmm_setup_signatures (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at          TEXT NOT NULL DEFAULT (datetime('now')),

    source              TEXT NOT NULL,
    source_id           INTEGER NOT NULL,
    symbol              TEXT NOT NULL,
    timeframe           TEXT NOT NULL,
    snapshot_at         TEXT NOT NULL,
    direction           TEXT NOT NULL,

    normalized_key      TEXT NOT NULL,
    raw_key             TEXT NOT NULL,
    setup_family        TEXT NOT NULL,
    primary_theme       TEXT,
    convergence_theme_score REAL NOT NULL DEFAULT 0,
    theme_tags          TEXT NOT NULL,
    ratios              TEXT NOT NULL,
    raw_json            TEXT NOT NULL,

    UNIQUE(source, source_id)
);

CREATE TABLE IF NOT EXISTS mmm_event_outcomes (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at          TEXT NOT NULL DEFAULT (datetime('now')),

    source              TEXT NOT NULL,
    source_id           INTEGER NOT NULL,
    signature_id        INTEGER REFERENCES mmm_setup_signatures(id),
    evaluated_at        TEXT NOT NULL,

    symbol              TEXT NOT NULL,
    timeframe           TEXT NOT NULL,
    snapshot_at         TEXT NOT NULL,
    direction           TEXT NOT NULL,

    entry_price         REAL,
    stop_loss_price     REAL,
    t1_price            REAL,
    t2_price            REAL,
    sl_pips             REAL,
    t1_pips             REAL,
    t2_pips             REAL,

    exit_at             TEXT,
    exit_price          REAL,
    exit_pips           REAL,
    max_favorable_pips  REAL,
    max_adverse_pips    REAL,
    t1_hit              INTEGER NOT NULL,
    minutes_to_t1       REAL,

    outcome             TEXT NOT NULL,
    label               TEXT NOT NULL,
    event_path          TEXT NOT NULL,
    notes               TEXT,

    UNIQUE(source, source_id)
);

CREATE INDEX IF NOT EXISTS idx_mmm_sig_key ON mmm_setup_signatures(normalized_key);
CREATE INDEX IF NOT EXISTS idx_mmm_sig_symbol ON mmm_setup_signatures(symbol, snapshot_at);
CREATE INDEX IF NOT EXISTS idx_mmm_outcome ON mmm_event_outcomes(outcome);
CREATE INDEX IF NOT EXISTS idx_mmm_outcome_symbol ON mmm_event_outcomes(symbol, snapshot_at);
"""

SIGNATURE_COLUMN_MIGRATIONS = {
    "primary_theme": "TEXT",
    "convergence_theme_score": "REAL NOT NULL DEFAULT 0",
}


@dataclass(frozen=True)
class ReplaySetup:
    """Normalized setup fields needed by the event replay."""

    symbol: str
    timeframe: str
    snapshot_at: datetime
    direction: Direction
    confluence_score: int = 0
    weekly_phase: str = ""
    weekly_trend: Direction = Direction.NEUTRAL
    h4_level: int = 0
    h4_trend: Direction = Direction.NEUTRAL
    h1_session: str = ""
    h1_trend: Direction = Direction.NEUTRAL
    asian_range_pips: Optional[float] = None
    accumulation_valid: bool = False
    stop_hunt_detected: bool = False
    stop_hunt_direction: Direction = Direction.NEUTRAL
    stop_hunt_pips: Optional[float] = None
    push_count: int = 0
    m_w_forming: bool = False
    m_w_pattern: str = ""
    rrt_detected: bool = False
    tdi_signals: list[str] = field(default_factory=list)
    tdi_shark_fin: bool = False
    tdi_shark_direction: str = ""
    tdi_vb_squeeze: bool = False
    tdi_divergence: str = ""
    tdi_crossed_signal: str = ""
    tdi_rsi: Optional[float] = None
    tdi_signal: Optional[float] = None
    tdi_base: Optional[float] = None
    pattern_trade_type: str = ""
    pattern_count: int = 0
    pattern_rrt_count: int = 0
    pattern_spike_count: int = 0
    pattern_pin_bar_count: int = 0
    pattern_half_batman: bool = False
    setup_class: str = ""
    source: str = "flashcard"
    source_id: int = 0


@dataclass(frozen=True)
class SetupSignature:
    """Pair-normalized setup identity for mining and convergence."""

    source: str
    source_id: int
    symbol: str
    timeframe: str
    snapshot_at: datetime
    direction: Direction
    normalized_key: str
    raw_key: str
    setup_family: str
    primary_theme: str
    convergence_theme_score: float
    theme_tags: list[str]
    ratios: dict[str, float]
    raw_json: dict[str, Any]


@dataclass(frozen=True)
class MMMEventOutcome:
    """Event-based replay result."""

    source: str
    source_id: int
    symbol: str
    timeframe: str
    snapshot_at: datetime
    direction: Direction
    entry_price: Optional[float]
    stop_loss_price: Optional[float]
    t1_price: Optional[float]
    t2_price: Optional[float]
    sl_pips: Optional[float]
    t1_pips: Optional[float]
    t2_pips: Optional[float]
    exit_at: Optional[datetime]
    exit_price: Optional[float]
    exit_pips: Optional[float]
    max_favorable_pips: Optional[float]
    max_adverse_pips: Optional[float]
    t1_hit: bool
    minutes_to_t1: Optional[float]
    outcome: str
    label: str
    event_path: list[str] = field(default_factory=list)
    notes: str = ""


@dataclass(frozen=True)
class ConvergenceGroup:
    theme: str
    setup_key: str
    symbols: list[str]
    directions: list[str]
    count: int
    avg_confluence: float
    score: float


class MMMReplayStore:
    """SQLite persistence for MMM signatures and event outcomes."""

    def __init__(self, db_path: Optional[Path] = None) -> None:
        self._db_path = db_path or DEFAULT_DB_PATH
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self._db_path))
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.executescript(SCHEMA)
        self._ensure_columns()
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    def _ensure_columns(self) -> None:
        existing = {
            row["name"]
            for row in self._conn.execute("PRAGMA table_info(mmm_setup_signatures)").fetchall()
        }
        for column, column_type in SIGNATURE_COLUMN_MIGRATIONS.items():
            if column not in existing:
                self._conn.execute(
                    f"ALTER TABLE mmm_setup_signatures ADD COLUMN {column} {column_type}"
                )

    def record_signature(self, signature: SetupSignature) -> int:
        self._conn.execute(
            """INSERT OR REPLACE INTO mmm_setup_signatures (
                source, source_id, symbol, timeframe, snapshot_at, direction,
                normalized_key, raw_key, setup_family, primary_theme,
                convergence_theme_score, theme_tags, ratios, raw_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                signature.source,
                signature.source_id,
                signature.symbol,
                signature.timeframe,
                _to_utc(signature.snapshot_at).isoformat(),
                signature.direction.value,
                signature.normalized_key,
                signature.raw_key,
                signature.setup_family,
                signature.primary_theme,
                signature.convergence_theme_score,
                json.dumps(signature.theme_tags),
                json.dumps(signature.ratios, sort_keys=True),
                json.dumps(signature.raw_json, default=str, sort_keys=True),
            ),
        )
        self._conn.commit()
        row = self._conn.execute(
            """SELECT id FROM mmm_setup_signatures
            WHERE source = ? AND source_id = ?""",
            (signature.source, signature.source_id),
        ).fetchone()
        return int(row["id"])

    def record_outcome(self, outcome: MMMEventOutcome, signature_id: Optional[int]) -> int:
        self._conn.execute(
            """INSERT OR REPLACE INTO mmm_event_outcomes (
                source, source_id, signature_id, evaluated_at,
                symbol, timeframe, snapshot_at, direction,
                entry_price, stop_loss_price, t1_price, t2_price,
                sl_pips, t1_pips, t2_pips,
                exit_at, exit_price, exit_pips,
                max_favorable_pips, max_adverse_pips,
                t1_hit, minutes_to_t1,
                outcome, label, event_path, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                outcome.source,
                outcome.source_id,
                signature_id,
                datetime.now(timezone.utc).isoformat(),
                outcome.symbol,
                outcome.timeframe,
                _to_utc(outcome.snapshot_at).isoformat(),
                outcome.direction.value,
                outcome.entry_price,
                outcome.stop_loss_price,
                outcome.t1_price,
                outcome.t2_price,
                outcome.sl_pips,
                outcome.t1_pips,
                outcome.t2_pips,
                _to_utc(outcome.exit_at).isoformat() if outcome.exit_at else None,
                outcome.exit_price,
                outcome.exit_pips,
                outcome.max_favorable_pips,
                outcome.max_adverse_pips,
                int(outcome.t1_hit),
                outcome.minutes_to_t1,
                outcome.outcome,
                outcome.label,
                json.dumps(outcome.event_path),
                outcome.notes,
            ),
        )
        self._conn.commit()
        row = self._conn.execute(
            """SELECT id FROM mmm_event_outcomes
            WHERE source = ? AND source_id = ?""",
            (outcome.source, outcome.source_id),
        ).fetchone()
        return int(row["id"])

    def pair_report(self, *, min_total: int = 1) -> list[dict[str, Any]]:
        rows = self._conn.execute(
            """SELECT
                o.symbol,
                COUNT(*) AS total,
                SUM(CASE WHEN o.outcome IN ('TARGET_2', 'TRAIL_STOP', 'TIME_EXIT_PROFIT',
                    'OPEN_PROFIT') THEN 1 ELSE 0 END) AS favorable,
                SUM(CASE WHEN o.t1_hit = 1 THEN 1 ELSE 0 END) AS t1_hits,
                AVG(o.exit_pips) AS avg_exit_pips,
                AVG(o.max_favorable_pips) AS avg_mfe,
                AVG(o.max_adverse_pips) AS avg_mae
            FROM mmm_event_outcomes o
            GROUP BY o.symbol
            HAVING total >= ?
            ORDER BY favorable * 1.0 / total DESC, avg_exit_pips DESC""",
            (min_total,),
        ).fetchall()
        return [dict(row) for row in rows]

    def setup_report(self, *, min_total: int = 2) -> list[dict[str, Any]]:
        rows = self._conn.execute(
            """SELECT
                s.normalized_key,
                s.setup_family,
                COUNT(*) AS total,
                GROUP_CONCAT(DISTINCT s.symbol) AS symbols,
                SUM(CASE WHEN o.outcome IN ('TARGET_2', 'TRAIL_STOP', 'TIME_EXIT_PROFIT',
                    'OPEN_PROFIT') THEN 1 ELSE 0 END) AS favorable,
                SUM(CASE WHEN o.t1_hit = 1 THEN 1 ELSE 0 END) AS t1_hits,
                AVG(o.exit_pips) AS avg_exit_pips,
                AVG(o.max_favorable_pips) AS avg_mfe
            FROM mmm_setup_signatures s
            JOIN mmm_event_outcomes o
              ON o.source = s.source AND o.source_id = s.source_id
            GROUP BY s.normalized_key, s.setup_family
            HAVING total >= ?
            ORDER BY favorable * 1.0 / total DESC, avg_exit_pips DESC""",
            (min_total,),
        ).fetchall()
        return [dict(row) for row in rows]

    def get_signatures(self, *, limit: int = 500) -> list[SetupSignature]:
        rows = self._conn.execute(
            """SELECT * FROM mmm_setup_signatures
            ORDER BY snapshot_at DESC
            LIMIT ?""",
            (limit,),
        ).fetchall()
        signatures: list[SetupSignature] = []
        for row in rows:
            signatures.append(
                SetupSignature(
                    source=str(row["source"]),
                    source_id=int(row["source_id"]),
                    symbol=str(row["symbol"]),
                    timeframe=str(row["timeframe"]),
                    snapshot_at=_parse_time(str(row["snapshot_at"])),
                    direction=_parse_direction(row["direction"]),
                    normalized_key=str(row["normalized_key"]),
                    raw_key=str(row["raw_key"]),
                    setup_family=str(row["setup_family"]),
                    primary_theme=str(row["primary_theme"] or ""),
                    convergence_theme_score=float(row["convergence_theme_score"] or 0.0),
                    theme_tags=_load_json_list(row["theme_tags"]),
                    ratios=_load_json_dict(row["ratios"]),
                    raw_json=_load_json_dict(row["raw_json"]),
                )
            )
        return signatures

    def calibration_records(self, *, min_total: int = 1) -> list[dict[str, Any]]:
        rows = self._conn.execute(
            """SELECT
                o.symbol,
                o.direction,
                o.snapshot_at,
                o.outcome,
                o.exit_pips,
                o.max_favorable_pips,
                o.max_adverse_pips,
                o.t1_hit,
                o.sl_pips,
                o.minutes_to_t1,
                s.normalized_key,
                s.primary_theme,
                s.convergence_theme_score,
                s.theme_tags,
                s.ratios,
                s.raw_json
            FROM mmm_event_outcomes o
            LEFT JOIN mmm_setup_signatures s
              ON s.source = o.source AND s.source_id = o.source_id
            WHERE o.symbol IN (
                SELECT symbol
                FROM mmm_event_outcomes
                GROUP BY symbol
                HAVING COUNT(*) >= ?
            )
            ORDER BY o.symbol, o.snapshot_at""",
            (min_total,),
        ).fetchall()

        records = []
        for row in rows:
            record = dict(row)
            record["ratios"] = _load_json_dict(record.get("ratios"))
            record["raw_json"] = _load_json_dict(record.get("raw_json"))
            record["theme_tags"] = _load_json_list(record.get("theme_tags"))
            records.append(record)
        return records


def label_mmm_event_path(
    df: pd.DataFrame,
    *,
    setup: ReplaySetup,
    entry_price: float,
    pip_size: float,
    profile: Optional[PairProfile] = None,
    asian_high: Optional[float] = None,
    asian_low: Optional[float] = None,
) -> MMMEventOutcome:
    """Replay a setup through MMM trade-management events.

    OHLC cannot recover intrabar order. If SL and T1/T2 are both reachable in
    the same candle before state is known, the label is AMBIGUOUS.
    """

    profile = profile or get_pair_profile(setup.symbol)
    direction = setup.direction
    snapshot_at = _to_utc(setup.snapshot_at)

    if direction == Direction.NEUTRAL:
        return _empty_outcome(setup, "NO_TRADE", "Neutral setup is not entered.")
    if df.empty:
        return _empty_outcome(setup, "NO_DATA", "No OHLC data supplied.")

    df = _normalize_df_index(df)
    snap = _timestamp_for_index(snapshot_at, df.index)
    future = df[(df.index > snap) & (df.index <= snap + timedelta(minutes=profile.max_duration_minutes))]
    if future.empty:
        return _empty_outcome(setup, "NO_DATA", "No future OHLC bars after snapshot.")

    if asian_high is None or asian_low is None:
        asian_high, asian_low = infer_asian_range(df[df.index <= snap], pip_size)

    sl_price, sl_pips = _structural_stop(
        setup=setup,
        entry_price=entry_price,
        pip_size=pip_size,
        profile=profile,
        asian_high=asian_high,
        asian_low=asian_low,
    )
    t1_pips = sl_pips * profile.t1_rr
    t2_pips = sl_pips * 2.5
    t1_price = _price_at_pips(direction, entry_price, t1_pips, pip_size)
    t2_price = _price_at_pips(direction, entry_price, t2_pips, pip_size)

    state = "FILLED"
    active_sl = sl_price
    t1_hit = False
    minutes_to_t1: Optional[float] = None
    max_fav = 0.0
    max_adv = 0.0
    event_path = ["ENTRY"]

    for idx, row in future.iterrows():
        bar_time = _dt_from_index(idx)
        high = float(row["High"])
        low = float(row["Low"])
        close = float(row["Close"])
        minutes = (bar_time - snapshot_at).total_seconds() / 60.0

        fav = _favorable_pips(direction, entry_price, high, low, pip_size)
        adv = _adverse_pips(direction, entry_price, high, low, pip_size)
        max_fav = max(max_fav, fav)
        max_adv = max(max_adv, adv)

        sl_hit = _sl_reached(direction, active_sl, high, low)
        t1_reached = _target_reached(direction, t1_price, high, low)
        t2_reached = _target_reached(direction, t2_price, high, low)

        if state == "FILLED":
            if sl_hit and (t1_reached or t2_reached):
                return _final_outcome(
                    setup,
                    "AMBIGUOUS",
                    entry_price,
                    sl_price,
                    t1_price,
                    t2_price,
                    sl_pips,
                    t1_pips,
                    t2_pips,
                    bar_time,
                    close,
                    _directional_pips(direction, entry_price, close, pip_size),
                    max_fav,
                    max_adv,
                    False,
                    None,
                    event_path + ["AMBIGUOUS_SL_AND_TARGET"],
                    "SL and target were both reachable inside the same OHLC candle.",
                )
            if sl_hit:
                return _final_outcome(
                    setup,
                    "LOSS",
                    entry_price,
                    sl_price,
                    t1_price,
                    t2_price,
                    sl_pips,
                    t1_pips,
                    t2_pips,
                    bar_time,
                    active_sl,
                    -sl_pips,
                    max_fav,
                    max_adv,
                    False,
                    None,
                    event_path + ["SL_HIT"],
                    "Structural stop was hit before T1.",
                )
            if t2_reached:
                event_path.extend(["T1_HIT", "TARGET_2"])
                return _final_outcome(
                    setup,
                    "TARGET_2",
                    entry_price,
                    sl_price,
                    t1_price,
                    t2_price,
                    sl_pips,
                    t1_pips,
                    t2_pips,
                    bar_time,
                    t2_price,
                    t2_pips,
                    max_fav,
                    max_adv,
                    True,
                    minutes,
                    event_path,
                    "T2 was reachable before any stop event.",
                )
            if t1_reached:
                state = "T1_HIT"
                t1_hit = True
                minutes_to_t1 = minutes
                active_sl = entry_price
                event_path.append("T1_HIT")
                # Do not test the new managed stop inside the same OHLC candle.
                # The bar may have touched breakeven before T1; that order is
                # unrecoverable without tick data.
                continue

            close_pips = _directional_pips(direction, entry_price, close, pip_size)
            stale_exit_min = getattr(profile, "stale_exit_minutes", profile.stale_minutes)

            # Phase 1: tighten SL at stale_minutes for extended-window pairs
            if (state == "FILLED" and minutes >= profile.stale_minutes
                    and close_pips <= 0 and stale_exit_min > profile.stale_minutes):
                # Tighten SL to half — reduce risk during extended window
                if sl_pips > 0:
                    half_sl = sl_pips / 2.0
                    if direction == Direction.BUY:
                        active_sl = entry_price - half_sl * pip_size
                    else:
                        active_sl = entry_price + half_sl * pip_size
                state = "STALE_TIGHTENED"
                event_path.append("STALE_TIGHTEN")

            # Phase 2: full exit at stale_exit_minutes
            if state in ("FILLED", "STALE_TIGHTENED") and minutes >= stale_exit_min and close_pips <= 0:
                return _final_outcome(
                    setup,
                    "STALE_EXIT",
                    entry_price,
                    sl_price,
                    t1_price,
                    t2_price,
                    sl_pips,
                    t1_pips,
                    t2_pips,
                    bar_time,
                    close,
                    close_pips,
                    max_fav,
                    max_adv,
                    False,
                    None,
                    event_path + ["STALE_EXIT"],
                    f"Stale exit at {stale_exit_min}min: trade was not in profit.",
                )

        if state == "T1_HIT":
            sl_hit = _sl_reached(direction, active_sl, high, low)
            t2_reached = _target_reached(direction, t2_price, high, low)
            if sl_hit and t2_reached:
                return _final_outcome(
                    setup,
                    "AMBIGUOUS",
                    entry_price,
                    sl_price,
                    t1_price,
                    t2_price,
                    sl_pips,
                    t1_pips,
                    t2_pips,
                    bar_time,
                    close,
                    _directional_pips(direction, entry_price, close, pip_size),
                    max_fav,
                    max_adv,
                    True,
                    minutes_to_t1,
                    event_path + ["AMBIGUOUS_BE_OR_T2"],
                    "Breakeven/trailing stop and T2 were both reachable inside one candle.",
                )
            if t2_reached:
                return _final_outcome(
                    setup,
                    "TARGET_2",
                    entry_price,
                    sl_price,
                    t1_price,
                    t2_price,
                    sl_pips,
                    t1_pips,
                    t2_pips,
                    bar_time,
                    t2_price,
                    t2_pips,
                    max_fav,
                    max_adv,
                    True,
                    minutes_to_t1,
                    event_path + ["TARGET_2"],
                    "T2 was reached after T1.",
                )
            if sl_hit:
                exit_pips = _directional_pips(direction, entry_price, active_sl, pip_size)
                outcome = "TRAIL_STOP" if exit_pips > 0 else "BREAKEVEN_AFTER_T1"
                return _final_outcome(
                    setup,
                    outcome,
                    entry_price,
                    sl_price,
                    t1_price,
                    t2_price,
                    sl_pips,
                    t1_pips,
                    t2_pips,
                    bar_time,
                    active_sl,
                    exit_pips,
                    max_fav,
                    max_adv,
                    True,
                    minutes_to_t1,
                    event_path + [outcome],
                    "Managed stop was reached after T1.",
                )

            close_pips = _directional_pips(direction, entry_price, close, pip_size)
            if close_pips >= profile.trail_activation_pips:
                proposed_sl = _price_at_pips(
                    direction,
                    entry_price,
                    max(0.0, close_pips - profile.trail_distance_pips),
                    pip_size,
                )
                active_sl = _better_stop(direction, active_sl, proposed_sl)

        if minutes >= profile.max_duration_minutes:
            close_pips = _directional_pips(direction, entry_price, close, pip_size)
            outcome = "TIME_EXIT_PROFIT" if close_pips > 0 else "TIME_EXIT_LOSS"
            return _final_outcome(
                setup,
                outcome,
                entry_price,
                sl_price,
                t1_price,
                t2_price,
                sl_pips,
                t1_pips,
                t2_pips,
                bar_time,
                close,
                close_pips,
                max_fav,
                max_adv,
                t1_hit,
                minutes_to_t1,
                event_path + [outcome],
                "Pair-specific max duration reached.",
            )

    last = future.iloc[-1]
    last_time = _dt_from_index(future.index[-1])
    close_pips = _directional_pips(direction, entry_price, float(last["Close"]), pip_size)
    outcome = "OPEN_PROFIT" if close_pips > 0 else "OPEN_LOSS" if close_pips < 0 else "OPEN_FLAT"
    return _final_outcome(
        setup,
        outcome,
        entry_price,
        sl_price,
        t1_price,
        t2_price,
        sl_pips,
        t1_pips,
        t2_pips,
        last_time,
        float(last["Close"]),
        close_pips,
        max_fav,
        max_adv,
        t1_hit,
        minutes_to_t1,
        event_path + [outcome],
        "Replay data ended before a terminal MMM event.",
    )


def build_setup_signature(setup: ReplaySetup, profile: Optional[PairProfile] = None) -> SetupSignature:
    """Build a pair-normalized setup signature."""

    profile = profile or get_pair_profile(setup.symbol)
    asian_pips = _none_to_zero(setup.asian_range_pips)
    hunt_pips = _none_to_zero(setup.stop_hunt_pips)

    asian_ratio = _safe_ratio(asian_pips, profile.asian_range_max_pips)
    hunt_ratio = _safe_ratio(hunt_pips, profile.stop_hunt_max_pips)
    level_ratio = _safe_ratio(hunt_pips, profile.expected_level_move_pips)

    setup_family = classify_setup_family(setup)
    mw_pattern = setup.m_w_pattern or infer_m_w_pattern(setup)
    mw_state = mw_pattern or ("MW" if setup.m_w_forming else "NO_MW")
    tdi_state = classify_tdi_state(setup)
    pattern_state = setup.pattern_trade_type or setup_family
    rrt_state = "RRT" if setup.rrt_detected else "NO_RRT"
    push_bucket = bucket_push_count(setup.push_count)
    asian_bucket = bucket_ratio(asian_ratio)
    hunt_bucket = bucket_hunt(setup, profile)
    confluence_bucket = bucket_confluence(setup.confluence_score)
    h4_bucket = f"L{setup.h4_level}" if setup.h4_level else "L0"
    theme_tags = currency_theme_tags(setup.symbol, setup.direction)
    primary_theme = primary_theme_tag(theme_tags)
    theme_score = single_setup_theme_score(theme_tags, setup.confluence_score)

    raw_key = "|".join(
        [
            setup.symbol,
            setup.direction.value,
            setup.weekly_phase or "NO_WEEK",
            setup.weekly_trend.value,
            h4_bucket,
            setup.h4_trend.value,
            setup.h1_session or "NO_SESSION",
            setup.h1_trend.value,
            f"AR_{round(asian_pips, 1)}",
            f"HUNT_{round(hunt_pips, 1)}",
            push_bucket,
            mw_state,
            rrt_state,
            tdi_state,
            pattern_state,
        ]
    )

    normalized_key = "|".join(
        [
            setup_family,
            setup.direction.value,
            setup.weekly_phase or "NO_WEEK",
            h4_bucket,
            setup.h1_session or "NO_SESSION",
            f"AR_{asian_bucket}",
            f"HUNT_{hunt_bucket}",
            push_bucket,
            mw_state,
            rrt_state,
            tdi_state,
            pattern_state,
            confluence_bucket,
        ]
    )

    raw_json = {
        "setup": asdict(setup),
        "profile": asdict(profile),
        "buckets": {
            "asian": asian_bucket,
            "hunt": hunt_bucket,
            "push": push_bucket,
            "tdi": tdi_state,
            "pattern": pattern_state,
            "confluence": confluence_bucket,
        },
    }

    return SetupSignature(
        source=setup.source,
        source_id=setup.source_id,
        symbol=setup.symbol,
        timeframe=setup.timeframe,
        snapshot_at=setup.snapshot_at,
        direction=setup.direction,
        normalized_key=normalized_key,
        raw_key=raw_key,
        setup_family=setup_family,
        primary_theme=primary_theme,
        convergence_theme_score=theme_score,
        theme_tags=theme_tags,
        ratios={
            "asian_range_to_pair_max": asian_ratio,
            "hunt_to_pair_max": hunt_ratio,
            "hunt_to_expected_level_move": level_ratio,
            "confluence": float(setup.confluence_score) / 100.0,
            "single_setup_theme_score": theme_score / 100.0,
        },
        raw_json=raw_json,
    )


def summarize_convergence(
    signatures: Iterable[SetupSignature],
    *,
    min_symbols: int = 2,
) -> list[ConvergenceGroup]:
    """Group similar normalized setups by currency-theme convergence."""

    grouped: dict[tuple[str, str], list[SetupSignature]] = {}
    for sig in signatures:
        setup_key = _convergence_key(sig.normalized_key)
        for theme in sig.theme_tags:
            grouped.setdefault((theme, setup_key), []).append(sig)

    groups: list[ConvergenceGroup] = []
    for (theme, setup_key), items in grouped.items():
        symbols = sorted({item.symbol for item in items})
        if len(symbols) < min_symbols:
            continue
        conf_values = [
            float(item.ratios.get("confluence", 0.0)) * 100.0
            for item in items
        ]
        avg_conf = sum(conf_values) / len(conf_values) if conf_values else 0.0
        direction_consistency = 1.0 if len({item.direction.value for item in items}) == 1 else 0.5
        score = min(
            100.0,
            (len(symbols) - 1) * 30.0
            + min(len(items), 5) * 6.0
            + avg_conf * 0.25
            + direction_consistency * 15.0,
        )
        groups.append(
            ConvergenceGroup(
                theme=theme,
                setup_key=setup_key,
                symbols=symbols,
                directions=sorted({item.direction.value for item in items}),
                count=len(items),
                avg_confluence=avg_conf,
                score=score,
            )
        )

    return sorted(groups, key=lambda group: (group.score, group.count), reverse=True)


def build_calibration_recommendations(
    records: Iterable[dict[str, Any]],
    *,
    min_total: int = 5,
) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        grouped.setdefault(str(record["symbol"]), []).append(record)

    recommendations: list[dict[str, Any]] = []
    for symbol, items in grouped.items():
        total = len(items)
        if total < min_total:
            continue
        favorable = [item for item in items if is_favorable_outcome(str(item.get("outcome")))]
        stale = [item for item in items if item.get("outcome") == "STALE_EXIT"]
        t1_hits = [item for item in items if bool(item.get("t1_hit"))]
        tdi_known = [item for item in items if "TDI_UNKNOWN" not in str(item.get("normalized_key") or "")]
        tdi_confirm = [item for item in items if "TDI_CONFIRM" in str(item.get("normalized_key") or "")]
        tdi_conflict = [item for item in items if "TDI_CONFLICT" in str(item.get("normalized_key") or "")]

        fav_rate = len(favorable) / total * 100.0
        stale_rate = len(stale) / total * 100.0
        t1_rate = len(t1_hits) / total * 100.0
        avg_exit = _avg(_optional_float(item.get("exit_pips")) for item in items)
        avg_mfe = _avg(_optional_float(item.get("max_favorable_pips")) for item in items)
        avg_mae = _avg(_optional_float(item.get("max_adverse_pips")) for item in items)
        avg_asian_ratio = _avg(
            _optional_float(item.get("ratios", {}).get("asian_range_to_pair_max"))
            for item in items
        )
        avg_hunt_ratio = _avg(
            _optional_float(item.get("ratios", {}).get("hunt_to_pair_max"))
            for item in items
        )

        notes: list[str] = []
        profile = _profile_from_record(items[0])

        if len(tdi_known) < total * 0.5:
            notes.append("Backfill more TDI context before making TDI mandatory.")
        elif tdi_confirm and _rate(tdi_confirm, is_favorable_record) > fav_rate + 10:
            notes.append("TDI confirmation is outperforming; raise weight or require it for this pair.")
        elif tdi_conflict and _rate(tdi_conflict, is_favorable_record) < fav_rate - 10:
            notes.append("TDI conflict is underperforming; block or heavily penalize conflict setups.")

        if stale_rate >= 60.0 and t1_rate < 20.0:
            notes.append("High stale rate with low T1 hits; raise confluence threshold and require stronger TDI/pattern confirmation.")
        elif stale_rate >= 40.0:
            notes.append("Stale exits are elevated; review entry timing and avoid late-session continuation entries.")

        if avg_mfe is not None and profile:
            trail_activation = _optional_float(profile.get("trail_activation_pips"))
            if trail_activation and avg_mfe < trail_activation * 0.5:
                notes.append("Average MFE is far below trail activation; current entries are too early/weak for this pair.")

        if avg_mae is not None and avg_mfe is not None and avg_mae > avg_mfe * 1.5:
            notes.append("MAE dominates MFE; tighten setup filter or wait for cleaner post-hunt reversal.")

        if avg_asian_ratio is not None:
            if avg_asian_ratio > 1.0 and fav_rate < 45.0:
                notes.append("Wide Asian ranges are not paying; lower or strictly enforce pair Asian max.")
            elif avg_asian_ratio < 0.45 and fav_rate > 55.0:
                notes.append("Tight accumulation is working; prioritize tighter Asian range buckets.")

        if avg_hunt_ratio is not None and avg_hunt_ratio > 1.0 and fav_rate < 45.0:
            notes.append("Extended hunts are underperforming; cap stop-hunt max or require extra confirmation.")

        if fav_rate >= 60.0 and t1_rate >= 40.0:
            summary = "keep settings; expand sample"
        elif fav_rate >= 50.0:
            summary = "minor tuning only"
        elif stale_rate >= 60.0:
            summary = "tighten entry gate"
        else:
            summary = "pair-specific recalibration needed"

        if not notes:
            notes.append("No strong recommendation yet; collect more event-labeled samples.")

        recommendations.append(
            {
                "symbol": symbol,
                "total": total,
                "favorable_rate": fav_rate,
                "stale_rate": stale_rate,
                "t1_rate": t1_rate,
                "avg_exit_pips": avg_exit,
                "avg_mfe": avg_mfe,
                "avg_mae": avg_mae,
                "summary": summary,
                "notes": notes,
            }
        )

    return sorted(
        recommendations,
        key=lambda rec: (rec["favorable_rate"], rec["avg_exit_pips"] or -999.0),
        reverse=True,
    )


def is_favorable_outcome(outcome: str) -> bool:
    return outcome in {"TARGET_2", "TRAIL_STOP", "TIME_EXIT_PROFIT", "OPEN_PROFIT"}


def is_favorable_record(record: dict[str, Any]) -> bool:
    return is_favorable_outcome(str(record.get("outcome")))


def build_gate_ablation(
    records: Iterable[dict[str, Any]],
    *,
    min_total: int = 5,
    symbol: Optional[str] = None,
) -> list[dict[str, Any]]:
    """Compare MMM gate variants against recorded event outcomes."""

    sample = [
        record for record in records
        if symbol is None or str(record.get("symbol")) == symbol
    ]
    if not sample:
        return []

    baseline = _summarize_gate("baseline", "Current replay sample", sample, sample)
    gates: list[tuple[str, str, Callable[[dict[str, Any]], bool]]] = [
        ("baseline", "Current replay sample", lambda record: True),
        ("mw_required", "Require explicit M_TOP/W_BOTTOM", _has_mw),
        ("push3_required", "Require MMM three-push structure", _has_push3),
        ("rrt_required", "Require RRT confirmation", _has_rrt),
        ("tdi_confirm", "Require TDI confirmation", _has_tdi_confirm),
        ("no_tdi_conflict", "Block TDI conflict", _no_tdi_conflict),
        ("asian_tight", "Asian range <= 50% of pair max", _asian_tight),
        ("asian_pair_valid", "Asian range <= pair max", _asian_pair_valid),
        ("hunt_pair_valid", "Stop hunt inside pair max", _hunt_pair_valid),
        ("convergence_50", "Convergence theme score >= 50", _convergence_50),
        (
            "mmm_strict",
            "M/W + push3 + no TDI conflict + pair-valid range/hunt",
            lambda record: (
                _has_mw(record)
                and _has_push3(record)
                and _no_tdi_conflict(record)
                and _asian_pair_valid(record)
                and _hunt_pair_valid(record)
            ),
        ),
        (
            "vision_ready",
            "Strict gate + RRT + TDI confirm",
            lambda record: (
                _has_mw(record)
                and _has_push3(record)
                and _has_rrt(record)
                and _has_tdi_confirm(record)
                and _asian_pair_valid(record)
                and _hunt_pair_valid(record)
            ),
        ),
    ]

    rows: list[dict[str, Any]] = []
    for name, description, predicate in gates:
        kept = [record for record in sample if predicate(record)]
        row = _summarize_gate(name, description, kept, sample)
        row["enough_sample"] = row["total"] >= min_total
        row["delta_favorable_rate"] = row["favorable_rate"] - baseline["favorable_rate"]
        row["delta_avg_exit_pips"] = _delta_optional(
            row["avg_exit_pips"], baseline["avg_exit_pips"]
        )
        rows.append(row)
    return rows


def build_advisory_grade_rows(
    records: Iterable[dict[str, Any]],
    *,
    min_total: int = 3,
    symbol: Optional[str] = None,
    peer_window_minutes: int = 240,
) -> list[dict[str, Any]]:
    scored = build_advisory_outcome_records(
        records,
        symbol=symbol,
        peer_window_minutes=peer_window_minutes,
    )
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in scored:
        grouped.setdefault(str(row["grade"]), []).append(row)

    rows: list[dict[str, Any]] = []
    for grade, items in grouped.items():
        if len(items) < min_total:
            continue
        metrics = _summarize_records(items)
        metrics["grade"] = grade
        metrics["avg_advisory_score"] = _avg(
            _optional_float(item.get("advisory_score")) for item in items
        )
        metrics["avg_convergence_score"] = _avg(
            _optional_float(item.get("convergence_score")) for item in items
        )
        rows.append(metrics)

    grade_order = {"A": 5, "B": 4, "C": 3, "D": 2, "AVOID": 1}
    return sorted(rows, key=lambda row: grade_order.get(str(row["grade"]), 0), reverse=True)


def build_advisory_outcome_records(
    records: Iterable[dict[str, Any]],
    *,
    symbol: Optional[str] = None,
    peer_window_minutes: int = 240,
) -> list[dict[str, Any]]:
    sample = [
        record for record in records
        if symbol is None or str(record.get("symbol")) == symbol
    ]
    setup_rows = [
        (record, _advisory_setup_from_record(record))
        for record in sample
    ]
    scored: list[dict[str, Any]] = []
    for record, setup in setup_rows:
        peers = [
            peer for peer_record, peer in setup_rows
            if peer.symbol != setup.symbol
            and _within_peer_window(record, peer_record, peer_window_minutes)
        ]
        advisory = score_advisory_setup(setup, peers)
        scored.append(
            {
                **record,
                "grade": advisory.grade,
                "action": advisory.action,
                "advisory_score": advisory.final_score,
                "convergence_score": advisory.convergence_score,
                "peer_symbols": advisory.peer_symbols,
            }
        )
    return scored


def build_calibration_profile_proposals(
    records: Iterable[dict[str, Any]],
    *,
    min_total: int = 5,
    symbol: Optional[str] = None,
) -> list[dict[str, Any]]:
    sample = [
        record for record in records
        if symbol is None or str(record.get("symbol")) == symbol
    ]
    grouped: dict[str, list[dict[str, Any]]] = {}
    for record in sample:
        grouped.setdefault(str(record["symbol"]), []).append(record)

    proposals: list[dict[str, Any]] = []
    for pair, items in grouped.items():
        if len(items) < min_total:
            continue
        metrics = _summarize_records(items)
        gates = {
            row["name"]: row
            for row in build_gate_ablation(items, min_total=min_total)
        }
        settings = _proposed_pair_settings(metrics, gates, min_total=min_total)
        evidence = _proposal_evidence(gates, min_total=min_total)
        proposals.append(
            {
                "symbol": pair,
                "total": metrics["total"],
                "baseline": metrics,
                "settings": settings,
                "evidence": evidence,
                "patch_preview": _profile_patch_preview(settings),
                "notes": _proposal_notes(metrics, gates, settings),
            }
        )

    return sorted(
        proposals,
        key=lambda row: (
            row["baseline"]["favorable_rate"],
            row["baseline"]["avg_exit_pips"] or -999.0,
        ),
        reverse=True,
    )


def _summarize_gate(
    name: str,
    description: str,
    kept: list[dict[str, Any]],
    full_sample: list[dict[str, Any]],
) -> dict[str, Any]:
    metrics = _summarize_records(kept)
    metrics["name"] = name
    metrics["description"] = description
    metrics["kept_pct"] = len(kept) / len(full_sample) * 100.0 if full_sample else 0.0
    return metrics


def _summarize_records(records: Iterable[dict[str, Any]]) -> dict[str, Any]:
    items = list(records)
    total = len(items)
    if not items:
        return {
            "total": 0,
            "favorable_rate": 0.0,
            "stale_rate": 0.0,
            "t1_rate": 0.0,
            "avg_exit_pips": None,
            "avg_mfe": None,
            "avg_mae": None,
        }
    return {
        "total": total,
        "favorable_rate": _rate(items, is_favorable_record),
        "stale_rate": _rate(items, lambda item: item.get("outcome") == "STALE_EXIT"),
        "t1_rate": _rate(items, lambda item: bool(item.get("t1_hit"))),
        "avg_exit_pips": _avg(_optional_float(item.get("exit_pips")) for item in items),
        "avg_mfe": _avg(_optional_float(item.get("max_favorable_pips")) for item in items),
        "avg_mae": _avg(_optional_float(item.get("max_adverse_pips")) for item in items),
    }


def _proposed_pair_settings(
    metrics: dict[str, Any],
    gates: dict[str, dict[str, Any]],
    *,
    min_total: int,
) -> dict[str, Any]:
    fav_rate = float(metrics["favorable_rate"])
    stale_rate = float(metrics["stale_rate"])
    t1_rate = float(metrics["t1_rate"])

    if fav_rate >= 60.0 and t1_rate >= 40.0:
        min_confluence = 50
        advisory_min = 60.0
    elif fav_rate >= 45.0:
        min_confluence = 55
        advisory_min = 65.0
    elif stale_rate >= 60.0 or fav_rate < 20.0:
        min_confluence = 65
        advisory_min = 75.0
    else:
        min_confluence = 60
        advisory_min = 70.0

    return {
        "min_confluence_score": min_confluence,
        "require_m_w": True,
        "require_push3": True,
        "require_rrt": _gate_improves(gates, "rrt_required", min_total=min_total, min_lift=5.0),
        "require_tdi_confirmation": _gate_improves(
            gates, "tdi_confirm", min_total=min_total, min_lift=10.0
        ),
        "block_tdi_conflict": True,
        "max_asian_range_ratio": 0.8
        if _gate_improves(gates, "asian_tight", min_total=min_total, min_lift=5.0)
        else 1.0,
        "max_hunt_range_ratio": 1.0,
        "min_convergence_score": 50.0
        if _gate_improves(gates, "convergence_50", min_total=min_total, min_lift=8.0)
        else 0.0,
        "advisory_min_score": advisory_min,
    }


def _proposal_evidence(
    gates: dict[str, dict[str, Any]],
    *,
    min_total: int,
) -> list[dict[str, Any]]:
    candidates = [
        row for name, row in gates.items()
        if name != "baseline" and row["total"] >= min_total
    ]
    return sorted(
        candidates,
        key=lambda row: (row["favorable_rate"], row["avg_exit_pips"] or -999.0),
        reverse=True,
    )[:5]


def _proposal_notes(
    metrics: dict[str, Any],
    gates: dict[str, dict[str, Any]],
    settings: dict[str, Any],
) -> list[str]:
    notes: list[str] = []
    if metrics["stale_rate"] >= 60.0:
        notes.append("High stale rate: raise threshold and prefer cleaner post-hunt reversal.")
    if metrics["favorable_rate"] < 30.0:
        notes.append("Low favorable rate: use advisory score as review filter before vision spend.")
    if settings["require_tdi_confirmation"]:
        notes.append("TDI confirmation improved the sample enough to propose requiring it.")
    elif gates.get("tdi_confirm", {}).get("total", 0):
        notes.append("TDI confirmation did not independently improve enough; keep it weighted, not mandatory.")
    if settings["min_convergence_score"]:
        notes.append("Cross-pair convergence improved results; require theme score >= 50.")
    if not notes:
        notes.append("Settings are conservative; collect a larger pair-specific sample before enforcement.")
    return notes


def _profile_patch_preview(settings: dict[str, Any]) -> list[str]:
    return [
        f"min_confluence_score={settings['min_confluence_score']},",
        f"require_m_w={settings['require_m_w']},",
        f"require_push3={settings['require_push3']},",
        f"require_rrt={settings['require_rrt']},",
        f"require_tdi_confirmation={settings['require_tdi_confirmation']},",
        f"block_tdi_conflict={settings['block_tdi_conflict']},",
        f"max_asian_range_ratio={settings['max_asian_range_ratio']},",
        f"max_hunt_range_ratio={settings['max_hunt_range_ratio']},",
        f"min_convergence_score={settings['min_convergence_score']},",
        f"advisory_min_score={settings['advisory_min_score']},",
    ]


def _gate_improves(
    gates: dict[str, dict[str, Any]],
    gate_name: str,
    *,
    min_total: int,
    min_lift: float,
) -> bool:
    baseline = gates.get("baseline", {})
    gate = gates.get(gate_name, {})
    return (
        int(gate.get("total") or 0) >= min_total
        and float(gate.get("favorable_rate") or 0.0)
        >= float(baseline.get("favorable_rate") or 0.0) + min_lift
    )


def _advisory_setup_from_record(record: dict[str, Any]) -> AdvisorySetup:
    raw_json = record.get("raw_json") if isinstance(record.get("raw_json"), dict) else {}
    setup = raw_json.get("setup") if isinstance(raw_json, dict) else {}
    setup = setup if isinstance(setup, dict) else {}
    ratios = record.get("ratios") if isinstance(record.get("ratios"), dict) else {}
    direction = _direction_text(record.get("direction") or setup.get("direction"))
    symbol = str(record.get("symbol") or setup.get("symbol") or "")
    return AdvisorySetup(
        symbol=symbol,
        direction=direction,
        confluence_score=int(
            setup.get("confluence_score")
            or (_optional_float(ratios.get("confluence")) or 0.0) * 100
        ),
        trade_valid=direction in {"BUY", "SELL"},
        h4_level=int(setup.get("h4_level") or 0),
        h1_session=str(setup.get("h1_session") or ""),
        asian_range_pips=_optional_float(setup.get("asian_range_pips")),
        asian_range_ratio=_optional_float(ratios.get("asian_range_to_pair_max")),
        stop_hunt_detected=_truthy(setup.get("stop_hunt_detected")),
        stop_hunt_pips=_optional_float(setup.get("stop_hunt_pips")),
        hunt_range_ratio=_optional_float(ratios.get("hunt_to_pair_max")),
        push_count=int(setup.get("push_count") or 0),
        m_w_forming=_truthy(setup.get("m_w_forming")) or _has_mw(record),
        m_w_pattern=str(setup.get("m_w_pattern") or _mw_from_key(record)),
        rrt_detected=_truthy(setup.get("rrt_detected")) or _has_rrt(record),
        tdi_state=_tdi_state_from_key(record),
        pattern_trade_type=str(setup.get("pattern_trade_type") or _pattern_from_key(record)),
        themes=list(record.get("theme_tags") or currency_theme_tags(symbol, _parse_direction(direction))),
    )


def _has_mw(record: dict[str, Any]) -> bool:
    key = str(record.get("normalized_key") or "")
    setup = _record_setup(record)
    return (
        "M_TOP" in key
        or "W_BOTTOM" in key
        or _truthy(setup.get("m_w_forming"))
        or bool(setup.get("m_w_pattern"))
    )


def _has_push3(record: dict[str, Any]) -> bool:
    return "PUSH3_PLUS" in str(record.get("normalized_key") or "") or int(
        _record_setup(record).get("push_count") or 0
    ) >= 3


def _has_rrt(record: dict[str, Any]) -> bool:
    key = f"|{record.get('normalized_key') or ''}|"
    return "|RRT|" in key or _truthy(_record_setup(record).get("rrt_detected"))


def _has_tdi_confirm(record: dict[str, Any]) -> bool:
    return "TDI_CONFIRM" in str(record.get("normalized_key") or "")


def _no_tdi_conflict(record: dict[str, Any]) -> bool:
    return "TDI_CONFLICT" not in str(record.get("normalized_key") or "")


def _asian_tight(record: dict[str, Any]) -> bool:
    ratio = _optional_float((record.get("ratios") or {}).get("asian_range_to_pair_max"))
    return ratio is not None and ratio <= 0.5


def _asian_pair_valid(record: dict[str, Any]) -> bool:
    ratio = _optional_float((record.get("ratios") or {}).get("asian_range_to_pair_max"))
    return ratio is not None and ratio <= 1.0


def _hunt_pair_valid(record: dict[str, Any]) -> bool:
    ratio = _optional_float((record.get("ratios") or {}).get("hunt_to_pair_max"))
    return ratio is not None and 0 < ratio <= 1.0


def _convergence_50(record: dict[str, Any]) -> bool:
    score = _optional_float(record.get("convergence_theme_score"))
    return score is not None and score >= 50.0


def _record_setup(record: dict[str, Any]) -> dict[str, Any]:
    raw_json = record.get("raw_json") if isinstance(record.get("raw_json"), dict) else {}
    setup = raw_json.get("setup") if isinstance(raw_json, dict) else {}
    return setup if isinstance(setup, dict) else {}


def _tdi_state_from_key(record: dict[str, Any]) -> str:
    key = str(record.get("normalized_key") or "")
    for state in ("TDI_CONFIRM", "TDI_CONFLICT", "TDI_SQUEEZE", "TDI_NEUTRAL", "TDI_NONE"):
        if state in key:
            return state
    return "TDI_UNKNOWN"


def _mw_from_key(record: dict[str, Any]) -> str:
    key = str(record.get("normalized_key") or "")
    if "W_BOTTOM" in key:
        return "W_BOTTOM"
    if "M_TOP" in key:
        return "M_TOP"
    return ""


def _pattern_from_key(record: dict[str, Any]) -> str:
    parts = str(record.get("normalized_key") or "").split("|")
    return parts[-2] if len(parts) >= 2 else ""


def _direction_text(value: Any) -> str:
    text = getattr(value, "value", value)
    text = str(text or "NEUTRAL").upper()
    if "." in text:
        text = text.split(".")[-1]
    return text if text in {"BUY", "SELL"} else "NEUTRAL"


def _truthy(value: Any) -> bool:
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y"}
    return bool(value)


def _delta_optional(value: Optional[float], baseline: Optional[float]) -> Optional[float]:
    if value is None or baseline is None:
        return None
    return value - baseline


def _within_peer_window(
    left: dict[str, Any],
    right: dict[str, Any],
    peer_window_minutes: int,
) -> bool:
    left_time = _optional_time(left.get("snapshot_at"))
    right_time = _optional_time(right.get("snapshot_at"))
    if left_time is None or right_time is None:
        return True
    delta_minutes = abs((left_time - right_time).total_seconds()) / 60.0
    return delta_minutes <= peer_window_minutes


def _optional_time(value: Any) -> Optional[datetime]:
    if not value:
        return None
    try:
        return _parse_time(str(value))
    except (TypeError, ValueError):
        return None


class MMMEventReplay:
    """Replay flashcards into MMM event labels."""

    def __init__(
        self,
        *,
        replay_db_path: Optional[Path] = None,
        flashcards_db_path: Optional[Path] = None,
    ) -> None:
        self._store = MMMReplayStore(replay_db_path)
        self._flashcards_db_path = flashcards_db_path or FLASHCARDS_DB_PATH

    def close(self) -> None:
        self._store.close()

    def get_flashcard_setups(
        self,
        *,
        min_confluence: int = 50,
        limit: int = 100,
        include_neutral: bool = False,
    ) -> list[ReplaySetup]:
        conn = sqlite3.connect(str(self._flashcards_db_path))
        conn.row_factory = sqlite3.Row
        try:
            direction_clause = "" if include_neutral else "AND entry_direction != 'NEUTRAL'"
            rows = conn.execute(
                f"""SELECT * FROM flashcards
                WHERE confluence_score >= ?
                  AND entry_direction IS NOT NULL
                  {direction_clause}
                ORDER BY snapshot_at
                LIMIT ?""",
                (min_confluence, limit),
            ).fetchall()
            return [setup_from_flashcard_row(row) for row in rows]
        finally:
            conn.close()

    def enrich_flashcards(
        self,
        *,
        fetch_rates: Callable[[str, str, datetime, datetime], pd.DataFrame],
        get_pip_size: Callable[[str], float],
        min_confluence: int = 30,
        limit: int = 500,
        missing_only: bool = True,
    ) -> int:
        """Backfill TDI, pattern, M/W type, convergence, and setup signatures."""

        # Ensures additive flashcard migrations are applied before update SQL.
        flashcards = FlashcardSystem(db_path=self._flashcards_db_path)
        flashcards.close()

        conn = sqlite3.connect(str(self._flashcards_db_path))
        conn.row_factory = sqlite3.Row
        try:
            clauses = ["confluence_score >= ?", "entry_direction IS NOT NULL"]
            params: list[Any] = [min_confluence]
            if missing_only:
                clauses.append(
                    """(
                        tdi_signals IS NULL OR tdi_signals = '[]'
                        OR pattern_trade_type IS NULL OR pattern_trade_type = ''
                        OR m_w_pattern IS NULL OR m_w_pattern = ''
                        OR advisory_confidence_score IS NULL
                    )"""
                )
            params.append(limit)
            rows = conn.execute(
                f"""SELECT * FROM flashcards
                WHERE {' AND '.join(clauses)}
                ORDER BY snapshot_at
                LIMIT ?""",
                params,
            ).fetchall()

            enriched = 0
            for row in rows:
                data = dict(row)
                direction = _parse_direction(data.get("entry_direction"))
                if direction == Direction.NEUTRAL:
                    continue
                snapshot_at = _parse_time(str(data["snapshot_at"]))
                symbol = str(data["symbol"])
                timeframe = str(data.get("timeframe") or "M15")
                pip_size = get_pip_size(symbol)

                try:
                    df_m15 = fetch_rates(
                        symbol,
                        timeframe,
                        snapshot_at - timedelta(days=7),
                        snapshot_at + timedelta(minutes=15),
                    )
                    df_d1 = fetch_rates(
                        symbol,
                        "D1",
                        snapshot_at - timedelta(days=220),
                        snapshot_at + timedelta(days=1),
                    )
                except Exception as exc:
                    logger.warning("Flashcard enrichment fetch failed #%s %s: %s", data["id"], symbol, exc)
                    continue

                df_m15 = _normalize_df_index(df_m15)
                df_d1 = _normalize_df_index(df_d1)
                snap = _timestamp_for_index(snapshot_at, df_m15.index)
                past_m15 = df_m15[df_m15.index <= snap]
                past_d1 = df_d1[df_d1.index <= _timestamp_for_index(snapshot_at, df_d1.index)]
                if len(past_m15) < 60:
                    logger.warning("Flashcard enrichment skipped #%s: insufficient M15 bars", data["id"])
                    continue

                enriched_fields = enrich_flashcard_fields(
                    data,
                    past_m15=past_m15,
                    past_d1=past_d1,
                    pip_size=pip_size,
                )
                _update_flashcard_enrichment(conn, int(data["id"]), enriched_fields)

                updated = data | enriched_fields
                setup = setup_from_flashcard_row(updated)
                signature = build_setup_signature(setup, get_pair_profile(symbol))
                self._store.record_signature(signature)
                enriched += 1

            conn.commit()
            return enriched
        finally:
            conn.close()

    def label_flashcards(
        self,
        *,
        fetch_rates: Callable[[str, str, datetime, datetime], pd.DataFrame],
        get_pip_size: Callable[[str], float],
        min_confluence: int = 50,
        limit: int = 100,
    ) -> int:
        count = 0
        for setup in self.get_flashcard_setups(min_confluence=min_confluence, limit=limit):
            profile = get_pair_profile(setup.symbol)
            start = setup.snapshot_at - timedelta(days=3)
            end = setup.snapshot_at + timedelta(minutes=profile.max_duration_minutes + 30)
            df = fetch_rates(setup.symbol, setup.timeframe, start, end)
            if df.empty:
                continue
            pip_size = get_pip_size(setup.symbol)
            df = _normalize_df_index(df)
            entry = nearest_close(df, setup.snapshot_at)
            if entry is None:
                continue
            signature = build_setup_signature(setup, profile)
            signature_id = self._store.record_signature(signature)
            outcome = label_mmm_event_path(
                df,
                setup=setup,
                entry_price=entry,
                pip_size=pip_size,
                profile=profile,
            )
            self._store.record_outcome(outcome, signature_id)
            count += 1
        return count

    def pair_report(self, *, min_total: int = 1) -> str:
        rows = self._store.pair_report(min_total=min_total)
        if not rows:
            return "No MMM event outcomes recorded."
        lines = [
            "",
            "=" * 92,
            "  HELIX V3 MMM EVENT PERFORMANCE BY PAIR",
            "=" * 92,
            f"  {'Pair':8} {'N':>5} {'Fav%':>7} {'T1%':>7} {'AvgExit':>9} {'MFE':>9} {'MAE':>9}",
            "-" * 92,
        ]
        for row in rows:
            total = int(row["total"])
            fav = float(row["favorable"] or 0) / total * 100.0 if total else 0.0
            t1 = float(row["t1_hits"] or 0) / total * 100.0 if total else 0.0
            lines.append(
                f"  {row['symbol']:8} {total:>5} {fav:>6.1f}% {t1:>6.1f}% "
                f"{_fmt(row['avg_exit_pips']):>9} {_fmt(row['avg_mfe']):>9} "
                f"{_fmt(row['avg_mae']):>9}"
            )
        lines.append("=" * 92)
        return "\n".join(lines)

    def setup_report(self, *, min_total: int = 2) -> str:
        rows = self._store.setup_report(min_total=min_total)
        if not rows:
            return "No repeated MMM setup signatures recorded."
        lines = [
            "",
            "=" * 112,
            "  HELIX V3 REPEATED MMM SETUP SIGNATURES",
            "=" * 112,
            f"  {'N':>4} {'Fav%':>7} {'T1%':>7} {'AvgExit':>9} {'MFE':>9} {'Symbols':<24} Setup",
            "-" * 112,
        ]
        for row in rows:
            total = int(row["total"])
            fav = float(row["favorable"] or 0) / total * 100.0 if total else 0.0
            t1 = float(row["t1_hits"] or 0) / total * 100.0 if total else 0.0
            lines.append(
                f"  {total:>4} {fav:>6.1f}% {t1:>6.1f}% "
                f"{_fmt(row['avg_exit_pips']):>9} {_fmt(row['avg_mfe']):>9} "
                f"{str(row['symbols'] or '')[:24]:<24} {row['normalized_key']}"
            )
        lines.append("=" * 112)
        return "\n".join(lines)

    def convergence_report(self, *, min_symbols: int = 2, limit: int = 500) -> str:
        groups = summarize_convergence(
            self._store.get_signatures(limit=limit),
            min_symbols=min_symbols,
        )
        if not groups:
            return "No cross-pair convergence groups recorded."
        lines = [
            "",
            "=" * 112,
            "  HELIX V3 CROSS-PAIR SETUP CONVERGENCE",
            "=" * 112,
            f"  {'Theme':<16} {'Score':>7} {'Pairs':>5} {'AvgConf':>8} {'Symbols':<32} Setup",
            "-" * 112,
        ]
        for group in groups:
            lines.append(
                f"  {group.theme:<16} {group.score:>6.1f} {len(group.symbols):>5} "
                f"{group.avg_confluence:>7.1f}% "
                f"{', '.join(group.symbols)[:32]:<32} {group.setup_key}"
            )
        lines.append("=" * 112)
        return "\n".join(lines)

    def calibration_report(self, *, min_total: int = 5) -> str:
        records = self._store.calibration_records(min_total=min_total)
        recommendations = build_calibration_recommendations(records, min_total=min_total)
        if not recommendations:
            return "No pairs have enough MMM event outcomes for calibration."

        lines = [
            "",
            "=" * 120,
            "  HELIX V3 PAIR CALIBRATION RECOMMENDATIONS",
            "=" * 120,
            f"  {'Pair':8} {'N':>5} {'Fav%':>7} {'Stale%':>8} {'T1%':>7} "
            f"{'AvgExit':>9} {'MFE':>9} Recommendation",
            "-" * 120,
        ]
        for rec in recommendations:
            lines.append(
                f"  {rec['symbol']:8} {rec['total']:>5} "
                f"{rec['favorable_rate']:>6.1f}% {rec['stale_rate']:>7.1f}% "
                f"{rec['t1_rate']:>6.1f}% {_fmt(rec['avg_exit_pips']):>9} "
                f"{_fmt(rec['avg_mfe']):>9} {rec['summary']}"
            )
            for note in rec["notes"]:
                lines.append(f"  {'':8} {'':>5} {'':>7} {'':>8} {'':>7} {'':>9} {'':>9} - {note}")
        lines.append("=" * 120)
        return "\n".join(lines)

    def gate_ablation_report(
        self,
        *,
        min_total: int = 5,
        symbol: Optional[str] = None,
    ) -> str:
        records = self._store.calibration_records(min_total=1)
        rows = build_gate_ablation(records, min_total=min_total, symbol=symbol)
        if not rows:
            return "No MMM event outcomes recorded for gate ablation."

        title = "HELIX V3 MMM GATE ABLATION"
        if symbol:
            title = f"{title} - {symbol}"
        lines = [
            "",
            "=" * 132,
            f"  {title}",
            "=" * 132,
            f"  {'Gate':<18} {'N':>5} {'Keep%':>7} {'Fav%':>7} {'Lift':>7} "
            f"{'T1%':>7} {'Stale%':>8} {'AvgExit':>9} {'MFE':>9} Description",
            "-" * 132,
        ]
        for row in rows:
            sample_mark = "" if row["enough_sample"] else "*"
            lines.append(
                f"  {row['name']:<18} {row['total']:>4}{sample_mark} "
                f"{row['kept_pct']:>6.1f}% {row['favorable_rate']:>6.1f}% "
                f"{row['delta_favorable_rate']:>+6.1f}% {row['t1_rate']:>6.1f}% "
                f"{row['stale_rate']:>7.1f}% {_fmt(row['avg_exit_pips']):>9} "
                f"{_fmt(row['avg_mfe']):>9} {row['description']}"
            )
        lines.append("  * below --min-total; use as directional evidence only.")
        lines.append("=" * 132)
        return "\n".join(lines)

    def advisory_report(
        self,
        *,
        min_total: int = 3,
        symbol: Optional[str] = None,
        peer_window_minutes: int = 240,
    ) -> str:
        records = self._store.calibration_records(min_total=1)
        rows = build_advisory_grade_rows(
            records,
            min_total=min_total,
            symbol=symbol,
            peer_window_minutes=peer_window_minutes,
        )
        if not rows:
            return "No advisory grade buckets have enough MMM event outcomes."

        title = "HELIX V3 CONVERGENCE-WEIGHTED ADVISORY OUTCOMES"
        if symbol:
            title = f"{title} - {symbol}"
        lines = [
            "",
            "=" * 116,
            f"  {title}",
            "=" * 116,
            f"  {'Grade':<8} {'N':>5} {'Fav%':>7} {'T1%':>7} {'Stale%':>8} "
            f"{'AvgExit':>9} {'AdvScore':>9} {'Conv':>7}",
            "-" * 116,
        ]
        for row in rows:
            lines.append(
                f"  {row['grade']:<8} {row['total']:>5} {row['favorable_rate']:>6.1f}% "
                f"{row['t1_rate']:>6.1f}% {row['stale_rate']:>7.1f}% "
                f"{_fmt(row['avg_exit_pips']):>9} {_fmt(row['avg_advisory_score']):>9} "
                f"{_fmt(row['avg_convergence_score']):>7}"
            )
        lines.append("=" * 116)
        return "\n".join(lines)

    def calibration_proposal_report(
        self,
        *,
        min_total: int = 5,
        symbol: Optional[str] = None,
    ) -> str:
        records = self._store.calibration_records(min_total=1)
        proposals = build_calibration_profile_proposals(
            records,
            min_total=min_total,
            symbol=symbol,
        )
        if not proposals:
            return "No pairs have enough MMM event outcomes for calibration proposals."

        title = "HELIX V3 PAIR PROFILE CALIBRATION PROPOSALS"
        if symbol:
            title = f"{title} - {symbol}"
        lines = [
            "",
            "=" * 120,
            f"  {title}",
            "=" * 120,
        ]
        for proposal in proposals:
            baseline = proposal["baseline"]
            settings = proposal["settings"]
            lines.append(
                f"  {proposal['symbol']} N={proposal['total']} "
                f"Fav={baseline['favorable_rate']:.1f}% "
                f"T1={baseline['t1_rate']:.1f}% "
                f"Stale={baseline['stale_rate']:.1f}% "
                f"AvgExit={_fmt(baseline['avg_exit_pips'])}"
            )
            lines.append(
                "    Proposed advisory gates: "
                f"min_conf={settings['min_confluence_score']}, "
                f"advisory_min={settings['advisory_min_score']:.0f}, "
                f"MW={settings['require_m_w']}, Push3={settings['require_push3']}, "
                f"RRT={settings['require_rrt']}, TDI={settings['require_tdi_confirmation']}, "
                f"Conv>={settings['min_convergence_score']:.0f}"
            )
            lines.append("    Patch preview for this PairProfile:")
            for patch_line in proposal["patch_preview"]:
                lines.append(f"      {patch_line}")
            lines.append("    Evidence:")
            if proposal["evidence"]:
                for evidence in proposal["evidence"]:
                    lines.append(
                        f"      {evidence['name']}: N={evidence['total']} "
                        f"Fav={evidence['favorable_rate']:.1f}% "
                        f"Lift={evidence['delta_favorable_rate']:+.1f}% "
                        f"AvgExit={_fmt(evidence['avg_exit_pips'])}"
                    )
            else:
                lines.append("      No single gate has enough sample yet.")
            for note in proposal["notes"]:
                lines.append(f"    - {note}")
            lines.append("-" * 120)
        lines.append("=" * 120)
        return "\n".join(lines)


def _enum_val(obj: Any) -> str:
    """Extract string value from an enum or return the string itself."""
    val = getattr(obj, "value", obj)
    return str(val) if val else ""


def _to_direction(obj: Any) -> Direction:
    """Convert an enum, string, or None to Direction."""
    if obj is None:
        return Direction.NEUTRAL
    if isinstance(obj, Direction):
        return obj
    val = getattr(obj, "value", obj)
    try:
        return Direction(str(val).upper())
    except (ValueError, AttributeError):
        return Direction.NEUTRAL


def replay_setup_from_mtf(
    analysis: Any,
    *,
    snapshot_at: datetime,
    tdi_result: Any = None,
    patterns: Any = None,
    source: str = "live",
    source_id: int = 0,
) -> ReplaySetup:
    """Build a ReplaySetup from a live MTF analysis + optional TDI/patterns."""
    m15 = getattr(analysis, "fifteen_min", None)
    h4 = getattr(analysis, "four_hour", None)
    h1 = getattr(analysis, "one_hour", None)
    weekly = getattr(analysis, "weekly", None)

    tdi_sigs = []
    tdi_rsi = tdi_signal = tdi_base = None
    tdi_shark = False
    tdi_shark_dir = ""
    tdi_vb = False
    tdi_div = ""
    tdi_cross = ""
    if tdi_result is not None:
        tdi_sigs = [s.value for s in getattr(tdi_result, "signals", []) if getattr(s, "value", "NONE") != "NONE"]
        tdi_rsi = getattr(tdi_result, "rsi", None)
        tdi_signal = getattr(tdi_result, "signal", None)
        tdi_base = getattr(tdi_result, "base", None)
        tdi_shark = bool(getattr(tdi_result, "shark_fin_active", False))
        tdi_shark_dir = str(getattr(tdi_result, "shark_fin_direction", "") or "")
        tdi_vb = bool(getattr(tdi_result, "vb_squeeze", False))
        for s in tdi_sigs:
            if "DIVERGENCE" in s:
                tdi_div = s
            if "CROSS" in s:
                tdi_cross = s

    pat_type = ""
    pat_count = pat_rrt = pat_spike = pat_pin = 0
    pat_batman = False
    if patterns is not None:
        pat_type = str(getattr(getattr(patterns, "trade_type", ""), "value", getattr(patterns, "trade_type", "")))
        pat_list = getattr(patterns, "patterns", [])
        pat_count = len(pat_list)
        for p in pat_list:
            pv = str(getattr(getattr(p, "pattern", ""), "value", getattr(p, "pattern", "")))
            if "RRT" in pv or "RAILROAD" in pv:
                pat_rrt += 1
            if "SPIKE" in pv:
                pat_spike += 1
            if "PIN" in pv:
                pat_pin += 1
            if "BATMAN" in pv:
                pat_batman = True

    return ReplaySetup(
        symbol=str(getattr(analysis, "symbol", "")),
        timeframe="M15",
        snapshot_at=snapshot_at,
        direction=getattr(analysis, "trade_direction", Direction.NEUTRAL),
        confluence_score=int(getattr(analysis, "confluence_score", 0) or 0),
        weekly_phase=_enum_val(getattr(weekly, "week_phase", "")),
        weekly_trend=_to_direction(getattr(weekly, "trend_direction", None)),
        h4_level=int(getattr(h4, "level_count", 0) or 0),
        h4_trend=_to_direction(getattr(h4, "trend_direction", None)),
        h1_session=_enum_val(getattr(h1, "session_phase", "")),
        h1_trend=_to_direction(getattr(h1, "trend_direction", None)),
        asian_range_pips=getattr(m15, "asian_range_pips", None),
        accumulation_valid=bool(getattr(m15, "accumulation_valid", False)),
        stop_hunt_detected=bool(getattr(m15, "stop_hunt_detected", False)),
        stop_hunt_direction=_to_direction(getattr(m15, "stop_hunt_direction", None)),
        stop_hunt_pips=getattr(m15, "stop_hunt_pips", None),
        push_count=int(getattr(m15, "push_count", 0) or 0),
        m_w_forming=bool(getattr(m15, "m_w_forming", False)),
        m_w_pattern=str(getattr(m15, "m_w_pattern", "") or ""),
        rrt_detected=bool(getattr(m15, "rrt_detected", False)),
        tdi_signals=tdi_sigs,
        tdi_shark_fin=tdi_shark,
        tdi_shark_direction=tdi_shark_dir,
        tdi_vb_squeeze=tdi_vb,
        tdi_divergence=tdi_div,
        tdi_crossed_signal=tdi_cross,
        tdi_rsi=tdi_rsi,
        tdi_signal=tdi_signal,
        tdi_base=tdi_base,
        pattern_trade_type=pat_type,
        pattern_count=pat_count,
        pattern_rrt_count=pat_rrt,
        pattern_spike_count=pat_spike,
        pattern_pin_bar_count=pat_pin,
        pattern_half_batman=pat_batman,
        source=source,
        source_id=source_id,
    )


def outcome_from_closed_trade(
    trade: Any,
    replay_setup: ReplaySetup,
) -> MMMEventOutcome:
    """Build an MMMEventOutcome from a closed SimulatedTrade or live trade data."""
    sl_pips = getattr(trade, "sl_pips", None)
    pip_size = getattr(trade, "pip_size", 0.0001)
    entry = getattr(trade, "entry_price", 0.0)
    sl = getattr(trade, "stop_loss", 0.0)
    tp1 = getattr(trade, "take_profit_1", 0.0)
    tp2 = getattr(trade, "take_profit_2", 0.0)

    t1_pips = abs(tp1 - entry) / pip_size if pip_size > 0 and tp1 else None
    t2_pips = abs(tp2 - entry) / pip_size if pip_size > 0 and tp2 else None

    exit_price = getattr(trade, "exit_price", entry)
    direction = getattr(trade, "direction", Direction.NEUTRAL)
    if direction == Direction.BUY:
        exit_pips = (exit_price - entry) / pip_size if pip_size > 0 else 0
    elif direction == Direction.SELL:
        exit_pips = (entry - exit_price) / pip_size if pip_size > 0 else 0
    else:
        exit_pips = 0

    exit_reason = str(getattr(trade, "exit_reason", ""))
    t1_closed = bool(getattr(trade, "t1_closed", False))

    # Map exit reason to replay outcome labels
    outcome_map = {
        "SL_HIT": "SL_HIT",
        "TP2_HIT": "TARGET_2",
        "STALE": "STALE_EXIT",
        "MAX_DURATION": "TIME_EXIT" if exit_pips > 0 else "TIME_EXIT_LOSS",
        "BACKTEST_END": "OPEN_PROFIT" if exit_pips > 0 else "OPEN_LOSS",
    }
    outcome = outcome_map.get(exit_reason, exit_reason)
    if exit_reason == "MAX_DURATION" and exit_pips > 0:
        outcome = "TIME_EXIT_PROFIT"

    duration_min = 0.0
    entry_time = getattr(trade, "entry_time", None)
    exit_time = getattr(trade, "exit_time", None)
    if entry_time and exit_time:
        duration_min = (exit_time - entry_time).total_seconds() / 60

    return MMMEventOutcome(
        source=replay_setup.source,
        source_id=replay_setup.source_id,
        symbol=replay_setup.symbol,
        timeframe="M15",
        snapshot_at=replay_setup.snapshot_at,
        direction=direction,
        entry_price=entry,
        stop_loss_price=sl,
        t1_price=tp1,
        t2_price=tp2,
        sl_pips=sl_pips,
        t1_pips=t1_pips,
        t2_pips=t2_pips,
        exit_at=exit_time,
        exit_price=exit_price,
        exit_pips=exit_pips,
        max_favorable_pips=getattr(trade, "max_favorable_pips", None),
        max_adverse_pips=getattr(trade, "max_adverse_pips", None),
        t1_hit=t1_closed,
        minutes_to_t1=None,
        outcome=outcome,
        label=f"{outcome}_{int(duration_min)}M",
        event_path=[exit_reason],
        notes=f"grade={getattr(trade, 'advisory_grade', '')} score={getattr(trade, 'advisory_score', 0):.0f}",
    )


def _live_outcome_label(
    reason: str, exit_pips: float, t1_hit: bool, tol: float
) -> str:
    """Map a live journal exit_reason + economics to the replay taxonomy.

    Keeps live outcomes in the SAME label set the signature audit consumes so
    forward demo data is directly comparable to the historical backtest data.
    `favorable` = {TARGET_2, TRAIL_STOP, TIME_EXIT_PROFIT}; everything else is
    unfavorable. Classification is by economics first (the money is the truth),
    refined by the exit reason and whether T1 was taken.
    """
    reason = (reason or "").upper()
    if exit_pips > tol:                                   # made money
        if reason == "TP":
            return "TARGET_2"
        return "TRAIL_STOP" if t1_hit else "TIME_EXIT_PROFIT"
    if exit_pips < -tol:                                  # lost money
        if reason in ("SL", "STOP_OUT") and not t1_hit:
            return "LOSS"
        if reason == "TIME_EXIT":
            return "TIME_EXIT_LOSS"
        return "STALE_EXIT"
    return "BREAKEVEN_AFTER_T1" if t1_hit else "STALE_EXIT"  # ~flat


def live_outcome_from_journal_row(
    row: dict[str, Any],
    replay_setup: ReplaySetup,
    *,
    breakeven_tol_pips: float = 1.0,
) -> Optional[MMMEventOutcome]:
    """Build an MMMEventOutcome from a CLOSED trade-journal row (live path).

    Forward-validation loop (Forward Plan Track 2.1): the journal already has
    full entry + exit accounting after `sync_from_mt5`, so a closed row plus the
    setup captured at entry is enough to record a live outcome — no MT5 or
    bar-replay needed. `row` is a plain dict (caller converts the sqlite Row).
    Returns None for non-terminal rows (still open, or a T1 partial) so the
    caller never records a half-finished trade.
    """
    def _f(key: str, default: float = 0.0) -> float:
        try:
            return float(row.get(key))
        except (TypeError, ValueError):
            return default

    reason = str(row.get("exit_reason") or "").upper()
    closed_at = row.get("closed_at")
    if reason == "T1_PARTIAL" or not closed_at:
        return None

    entry = _f("entry_price")
    sl = _f("stop_loss")
    tp1 = _f("take_profit_1")
    tp2 = _f("take_profit_2")
    sl_pips = _f("sl_pips")
    exit_price = _f("exit_price", entry)
    exit_pips = _f("pips_gained")
    t1_hit = bool(_f("t1_hit"))
    duration_min = _f("duration_minutes")

    pip_size = abs(entry - sl) / sl_pips if sl_pips > 0 and entry and sl else None
    t1_pips = abs(tp1 - entry) / pip_size if pip_size and tp1 else None
    t2_pips = abs(tp2 - entry) / pip_size if pip_size and tp2 else None

    outcome = _live_outcome_label(reason, exit_pips, t1_hit, breakeven_tol_pips)
    event_path = ["ENTRY"] + (["T1_HIT"] if t1_hit else []) + [outcome]

    exit_at = None
    try:
        exit_at = _to_utc(closed_at) if isinstance(closed_at, str) else closed_at
    except Exception:
        exit_at = None

    return MMMEventOutcome(
        source=replay_setup.source,
        source_id=replay_setup.source_id,
        symbol=replay_setup.symbol,
        timeframe="M15",
        snapshot_at=replay_setup.snapshot_at,
        direction=replay_setup.direction,
        entry_price=entry,
        stop_loss_price=sl,
        t1_price=tp1,
        t2_price=tp2,
        sl_pips=sl_pips,
        t1_pips=t1_pips,
        t2_pips=t2_pips,
        exit_at=exit_at,
        exit_price=exit_price,
        exit_pips=exit_pips,
        max_favorable_pips=None,
        max_adverse_pips=None,
        t1_hit=t1_hit,
        minutes_to_t1=None,
        outcome=outcome,
        label=f"{outcome}_{int(duration_min)}M",
        event_path=event_path,
        notes=f"live exit_reason={reason}",
    )


def setup_from_flashcard_row(row: sqlite3.Row | dict[str, Any]) -> ReplaySetup:
    data = dict(row)
    return ReplaySetup(
        symbol=str(data["symbol"]),
        timeframe=str(data.get("timeframe") or "M15"),
        snapshot_at=_parse_time(str(data["snapshot_at"])),
        direction=_parse_direction(data.get("entry_direction")),
        confluence_score=int(data.get("confluence_score") or 0),
        weekly_phase=str(data.get("weekly_phase") or ""),
        weekly_trend=_parse_direction(data.get("weekly_trend")),
        h4_level=int(data.get("h4_level") or 0),
        h4_trend=_parse_direction(data.get("h4_trend")),
        h1_session=str(data.get("h1_session") or ""),
        h1_trend=_parse_direction(data.get("h1_trend")),
        asian_range_pips=_optional_float(data.get("asian_range_pips")),
        accumulation_valid=bool(data.get("accumulation_valid")),
        stop_hunt_detected=bool(data.get("stop_hunt_detected")),
        stop_hunt_direction=_parse_direction(data.get("stop_hunt_direction")),
        stop_hunt_pips=_optional_float(data.get("stop_hunt_pips")),
        push_count=int(data.get("push_count") or 0),
        m_w_forming=bool(data.get("m_w_forming")),
        m_w_pattern=str(data.get("m_w_pattern") or ""),
        rrt_detected=bool(data.get("rrt_detected")),
        tdi_signals=_load_json_list(data.get("tdi_signals")),
        tdi_shark_fin=bool(data.get("tdi_shark_fin")),
        tdi_shark_direction=str(data.get("tdi_shark_direction") or ""),
        tdi_vb_squeeze=bool(data.get("tdi_vb_squeeze")),
        tdi_divergence=str(data.get("tdi_divergence") or ""),
        tdi_crossed_signal=str(data.get("tdi_crossed_signal") or ""),
        tdi_rsi=_optional_float(data.get("tdi_rsi")),
        tdi_signal=_optional_float(data.get("tdi_signal")),
        tdi_base=_optional_float(data.get("tdi_base")),
        pattern_trade_type=str(data.get("pattern_trade_type") or ""),
        pattern_count=int(data.get("pattern_count") or 0),
        pattern_rrt_count=int(data.get("pattern_rrt_count") or 0),
        pattern_spike_count=int(data.get("pattern_spike_count") or 0),
        pattern_pin_bar_count=int(data.get("pattern_pin_bar_count") or 0),
        pattern_half_batman=bool(data.get("pattern_half_batman")),
        setup_class=str(data.get("snapshot_type") or ""),
        source="flashcard",
        source_id=int(data.get("id") or 0),
    )


def enrich_flashcard_fields(
    row: sqlite3.Row | dict[str, Any],
    *,
    past_m15: pd.DataFrame,
    past_d1: pd.DataFrame,
    pip_size: float,
) -> dict[str, Any]:
    data = dict(row)
    direction = _parse_direction(data.get("entry_direction"))
    setup = setup_from_flashcard_row(data)
    m_w_pattern = str(data.get("m_w_pattern") or "") or infer_m_w_pattern(setup)

    tdi = compute_tdi(past_m15)
    tdi_signals = [signal.value for signal in tdi.signals if signal.value != "NONE"]

    prev_hod: Optional[float] = None
    prev_lod: Optional[float] = None
    if len(past_d1) >= 2:
        hilo = compute_daily_hilo(past_d1)
        prev_hod = float(hilo["phod"]) if hilo["phod"] else None
        prev_lod = float(hilo["plod"]) if hilo["plod"] else None

    asian_high, asian_low = infer_asian_range(past_m15, pip_size)
    patterns = scan_patterns(
        past_m15.iloc[-50:],
        pip_size,
        prev_hod=prev_hod,
        prev_lod=prev_lod,
        asian_high=asian_high,
        asian_low=asian_low,
        session_hour_utc=past_m15.index[-1].hour,
    )

    if not m_w_pattern:
        detected = {pattern.pattern.value for pattern in patterns.patterns}
        if "W_BOTTOM" in detected:
            m_w_pattern = "W_BOTTOM"
        elif "M_TOP" in detected:
            m_w_pattern = "M_TOP"

    theme_tags = currency_theme_tags(str(data["symbol"]), direction)
    theme_score = single_setup_theme_score(theme_tags, int(data.get("confluence_score") or 0))
    profile = get_pair_profile(str(data["symbol"]))
    enriched_setup = replace(
        setup,
        m_w_pattern=m_w_pattern,
        tdi_signals=tdi_signals,
        tdi_shark_fin=tdi.shark_fin_active,
        tdi_shark_direction=tdi.shark_fin_direction,
        tdi_vb_squeeze=tdi.vb_squeeze,
        tdi_divergence=tdi.divergence,
        tdi_crossed_signal=tdi.rsi_crossed_signal,
        tdi_rsi=tdi.rsi,
        tdi_signal=tdi.signal,
        tdi_base=tdi.base,
        pattern_trade_type=patterns.trade_type.value,
        pattern_count=len(patterns.patterns),
        pattern_rrt_count=patterns.rrt_count,
        pattern_spike_count=patterns.spike_count,
        pattern_pin_bar_count=patterns.pin_bar_count,
        pattern_half_batman=patterns.half_batman,
    )
    advisory_setup = AdvisorySetup(
        symbol=enriched_setup.symbol,
        direction=enriched_setup.direction.value,
        confluence_score=enriched_setup.confluence_score,
        trade_valid=enriched_setup.direction != Direction.NEUTRAL,
        h4_level=enriched_setup.h4_level,
        h1_session=enriched_setup.h1_session,
        asian_range_pips=enriched_setup.asian_range_pips,
        asian_range_ratio=_safe_ratio(
            _none_to_zero(enriched_setup.asian_range_pips),
            profile.asian_range_max_pips,
        ),
        stop_hunt_detected=enriched_setup.stop_hunt_detected,
        stop_hunt_pips=enriched_setup.stop_hunt_pips,
        hunt_range_ratio=_safe_ratio(
            _none_to_zero(enriched_setup.stop_hunt_pips),
            profile.stop_hunt_max_pips,
        ),
        push_count=enriched_setup.push_count,
        m_w_forming=enriched_setup.m_w_forming,
        m_w_pattern=enriched_setup.m_w_pattern,
        rrt_detected=enriched_setup.rrt_detected,
        tdi_state=classify_tdi_state(enriched_setup),
        pattern_trade_type=enriched_setup.pattern_trade_type,
        themes=theme_tags,
    )
    advisory = score_advisory_setup(advisory_setup)

    return {
        "m_w_pattern": m_w_pattern,
        "tdi_signals": json.dumps(tdi_signals),
        "tdi_shark_fin": int(tdi.shark_fin_active),
        "tdi_shark_direction": tdi.shark_fin_direction,
        "tdi_vb_squeeze": int(tdi.vb_squeeze),
        "tdi_divergence": tdi.divergence,
        "tdi_crossed_signal": tdi.rsi_crossed_signal,
        "tdi_rsi": tdi.rsi,
        "tdi_signal": tdi.signal,
        "tdi_base": tdi.base,
        "pattern_trade_type": patterns.trade_type.value,
        "pattern_count": len(patterns.patterns),
        "pattern_rrt_count": patterns.rrt_count,
        "pattern_spike_count": patterns.spike_count,
        "pattern_pin_bar_count": patterns.pin_bar_count,
        "pattern_half_batman": int(patterns.half_batman),
        "convergence_themes": json.dumps(theme_tags),
        "convergence_theme_score": theme_score,
        "advisory_confidence_score": advisory.final_score,
        "advisory_grade": advisory.grade,
        "advisory_action": advisory.action,
        "advisory_reasons": json.dumps(advisory.reasons),
        "advisory_blockers": json.dumps(advisory.blockers),
    }


def _update_flashcard_enrichment(
    conn: sqlite3.Connection,
    flashcard_id: int,
    fields: dict[str, Any],
) -> None:
    assignments = ", ".join(f"{column} = ?" for column in fields)
    conn.execute(
        f"UPDATE flashcards SET {assignments} WHERE id = ?",
        (*fields.values(), flashcard_id),
    )


def infer_asian_range(df: pd.DataFrame, pip_size: float) -> tuple[Optional[float], Optional[float]]:
    if df.empty:
        return None, None
    try:
        sessions = classify_sessions(df, pip_size=pip_size)
        today_asian = get_today_asian_range(sessions, df)
    except Exception:
        today_asian = None
    if today_asian:
        return float(today_asian["high"]), float(today_asian["low"])
    recent = df.iloc[-32:] if len(df) >= 32 else df
    if recent.empty:
        return None, None
    return float(recent["High"].max()), float(recent["Low"].min())


def nearest_close(df: pd.DataFrame, snapshot_at: datetime) -> Optional[float]:
    if df.empty:
        return None
    df = _normalize_df_index(df)
    snap = _timestamp_for_index(_to_utc(snapshot_at), df.index)
    past = df[df.index <= snap]
    if past.empty:
        return float(df["Open"].iloc[0])
    return float(past["Close"].iloc[-1])


def classify_setup_family(setup: ReplaySetup) -> str:
    if setup.m_w_forming and setup.push_count >= 3:
        return "THE_33_MW"
    if setup.m_w_forming:
        return "SECOND_LEG_MW"
    if setup.rrt_detected:
        return "RRT_REVERSAL"
    if setup.stop_hunt_detected:
        return "STOP_HUNT"
    if setup.accumulation_valid:
        return "ACCUMULATION"
    return setup.setup_class or "UNCLASSIFIED"


def infer_m_w_pattern(setup: ReplaySetup) -> str:
    if not setup.m_w_forming:
        return ""
    if setup.direction == Direction.BUY:
        return "W_BOTTOM"
    if setup.direction == Direction.SELL:
        return "M_TOP"
    return ""


def classify_tdi_state(setup: ReplaySetup) -> str:
    signals = {signal.upper() for signal in setup.tdi_signals}
    if not signals and not setup.tdi_vb_squeeze and not setup.tdi_shark_fin:
        if setup.tdi_rsi is None:
            return "TDI_UNKNOWN"
        return "TDI_NONE"

    if tdi_confirms_direction(setup):
        return "TDI_CONFIRM"
    if tdi_conflicts_direction(setup):
        return "TDI_CONFLICT"
    if setup.tdi_vb_squeeze:
        return "TDI_SQUEEZE"
    return "TDI_NEUTRAL"


def tdi_confirms_direction(setup: ReplaySetup) -> bool:
    signals = {signal.upper() for signal in setup.tdi_signals}
    if setup.direction == Direction.BUY:
        return bool(
            signals
            & {
                "SHARK_FIN_LONG",
                "MBL_CROSS_BULLISH",
                "SIGNAL_CROSS_BULLISH",
                "HOOK_BULLISH",
                "BULLISH_DIVERGENCE",
            }
        ) or setup.tdi_shark_direction.upper() == "LONG"
    if setup.direction == Direction.SELL:
        return bool(
            signals
            & {
                "SHARK_FIN_SHORT",
                "MBL_CROSS_BEARISH",
                "SIGNAL_CROSS_BEARISH",
                "HOOK_BEARISH",
                "BEARISH_DIVERGENCE",
            }
        ) or setup.tdi_shark_direction.upper() == "SHORT"
    return False


def tdi_conflicts_direction(setup: ReplaySetup) -> bool:
    signals = {signal.upper() for signal in setup.tdi_signals}
    if setup.direction == Direction.BUY:
        return bool(
            signals
            & {
                "SHARK_FIN_SHORT",
                "MBL_CROSS_BEARISH",
                "SIGNAL_CROSS_BEARISH",
                "HOOK_BEARISH",
                "BEARISH_DIVERGENCE",
            }
        ) or setup.tdi_shark_direction.upper() == "SHORT"
    if setup.direction == Direction.SELL:
        return bool(
            signals
            & {
                "SHARK_FIN_LONG",
                "MBL_CROSS_BULLISH",
                "SIGNAL_CROSS_BULLISH",
                "HOOK_BULLISH",
                "BULLISH_DIVERGENCE",
            }
        ) or setup.tdi_shark_direction.upper() == "LONG"
    return False


def primary_theme_tag(theme_tags: list[str]) -> str:
    return theme_tags[0] if theme_tags else ""


def single_setup_theme_score(theme_tags: list[str], confluence_score: int) -> float:
    if not theme_tags:
        return 0.0
    return min(100.0, 20.0 + confluence_score * 0.4)


def bucket_ratio(value: float) -> str:
    if value <= 0:
        return "NONE"
    if value <= 0.5:
        return "TIGHT"
    if value <= 1.0:
        return "VALID"
    if value <= 1.3:
        return "WIDE"
    return "EXTREME"


def bucket_hunt(setup: ReplaySetup, profile: PairProfile) -> str:
    pips = _none_to_zero(setup.stop_hunt_pips)
    if not setup.stop_hunt_detected or pips <= 0:
        return "NONE"
    if pips < profile.stop_hunt_min_pips:
        return "SOFT"
    if pips <= profile.stop_hunt_max_pips:
        return "PAIR_RANGE"
    return "EXTENDED"


def bucket_push_count(push_count: int) -> str:
    if push_count >= 3:
        return "PUSH3_PLUS"
    if push_count == 2:
        return "PUSH2"
    if push_count == 1:
        return "PUSH1"
    return "PUSH0"


def bucket_confluence(score: int) -> str:
    if score >= 75:
        return "CONF_75_PLUS"
    if score >= 50:
        return "CONF_50_74"
    if score >= 30:
        return "CONF_30_49"
    return "CONF_LOW"


def currency_theme_tags(symbol: str, direction: Direction) -> list[str]:
    if direction == Direction.NEUTRAL:
        return []
    base, quote = split_symbol(symbol)
    if direction == Direction.BUY:
        return [f"{base}_STRENGTH", f"{quote}_WEAKNESS"]
    return [f"{base}_WEAKNESS", f"{quote}_STRENGTH"]


def split_symbol(symbol: str) -> tuple[str, str]:
    if symbol == "XAUUSD":
        return "XAU", "USD"
    if len(symbol) >= 6:
        return symbol[:3], symbol[3:6]
    return symbol, "UNKNOWN"


def _structural_stop(
    *,
    setup: ReplaySetup,
    entry_price: float,
    pip_size: float,
    profile: PairProfile,
    asian_high: Optional[float],
    asian_low: Optional[float],
) -> tuple[float, float]:
    buffer = profile.sl_buffer_pips * pip_size
    fallback_pips = max(
        profile.stop_hunt_min_pips,
        _none_to_zero(setup.stop_hunt_pips),
        profile.trail_activation_pips,
    ) + profile.sl_buffer_pips
    if setup.direction == Direction.BUY:
        sl = (asian_low - buffer) if asian_low is not None else entry_price - fallback_pips * pip_size
    else:
        sl = (asian_high + buffer) if asian_high is not None else entry_price + fallback_pips * pip_size
    sl_pips = abs(entry_price - sl) / pip_size
    if sl_pips <= 0:
        sl_pips = fallback_pips
        sl = _price_at_pips(setup.direction, entry_price, -sl_pips, pip_size)
    return float(sl), float(sl_pips)


def _price_at_pips(direction: Direction, entry: float, pips: float, pip_size: float) -> float:
    if direction == Direction.BUY:
        return entry + pips * pip_size
    return entry - pips * pip_size


def _favorable_pips(
    direction: Direction,
    entry_price: float,
    high: float,
    low: float,
    pip_size: float,
) -> float:
    if direction == Direction.BUY:
        return max(0.0, (high - entry_price) / pip_size)
    return max(0.0, (entry_price - low) / pip_size)


def _adverse_pips(
    direction: Direction,
    entry_price: float,
    high: float,
    low: float,
    pip_size: float,
) -> float:
    if direction == Direction.BUY:
        return max(0.0, (entry_price - low) / pip_size)
    return max(0.0, (high - entry_price) / pip_size)


def _directional_pips(
    direction: Direction,
    entry_price: float,
    price: float,
    pip_size: float,
) -> float:
    if direction == Direction.BUY:
        return (price - entry_price) / pip_size
    if direction == Direction.SELL:
        return (entry_price - price) / pip_size
    return 0.0


def _target_reached(direction: Direction, target: float, high: float, low: float) -> bool:
    return high >= target if direction == Direction.BUY else low <= target


def _sl_reached(direction: Direction, stop: float, high: float, low: float) -> bool:
    return low <= stop if direction == Direction.BUY else high >= stop


def _better_stop(direction: Direction, current: float, proposed: float) -> float:
    return max(current, proposed) if direction == Direction.BUY else min(current, proposed)


def _final_outcome(
    setup: ReplaySetup,
    outcome: str,
    entry_price: float,
    stop_loss_price: float,
    t1_price: float,
    t2_price: float,
    sl_pips: float,
    t1_pips: float,
    t2_pips: float,
    exit_at: datetime,
    exit_price: float,
    exit_pips: float,
    max_favorable_pips: float,
    max_adverse_pips: float,
    t1_hit: bool,
    minutes_to_t1: Optional[float],
    event_path: list[str],
    notes: str,
) -> MMMEventOutcome:
    return MMMEventOutcome(
        source=setup.source,
        source_id=setup.source_id,
        symbol=setup.symbol,
        timeframe=setup.timeframe,
        snapshot_at=setup.snapshot_at,
        direction=setup.direction,
        entry_price=entry_price,
        stop_loss_price=stop_loss_price,
        t1_price=t1_price,
        t2_price=t2_price,
        sl_pips=sl_pips,
        t1_pips=t1_pips,
        t2_pips=t2_pips,
        exit_at=exit_at,
        exit_price=exit_price,
        exit_pips=exit_pips,
        max_favorable_pips=max_favorable_pips,
        max_adverse_pips=max_adverse_pips,
        t1_hit=t1_hit,
        minutes_to_t1=minutes_to_t1,
        outcome=outcome,
        label=f"{setup.symbol}_{setup.direction.value}_{outcome}",
        event_path=event_path,
        notes=notes,
    )


def _empty_outcome(setup: ReplaySetup, outcome: str, notes: str) -> MMMEventOutcome:
    return MMMEventOutcome(
        source=setup.source,
        source_id=setup.source_id,
        symbol=setup.symbol,
        timeframe=setup.timeframe,
        snapshot_at=setup.snapshot_at,
        direction=setup.direction,
        entry_price=None,
        stop_loss_price=None,
        t1_price=None,
        t2_price=None,
        sl_pips=None,
        t1_pips=None,
        t2_pips=None,
        exit_at=None,
        exit_price=None,
        exit_pips=None,
        max_favorable_pips=None,
        max_adverse_pips=None,
        t1_hit=False,
        minutes_to_t1=None,
        outcome=outcome,
        label=f"{setup.symbol}_{setup.direction.value}_{outcome}",
        event_path=[outcome],
        notes=notes,
    )


def _normalize_df_index(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    out = df.copy()
    if not isinstance(out.index, pd.DatetimeIndex):
        raise TypeError("Replay dataframe must use a DatetimeIndex")
    if out.index.tz is None:
        out.index = out.index.tz_localize(timezone.utc)
    else:
        out.index = out.index.tz_convert(timezone.utc)
    return out


def _timestamp_for_index(dt: datetime, index: pd.DatetimeIndex) -> pd.Timestamp:
    ts = pd.Timestamp(_to_utc(dt))
    if index.tz is None:
        return ts.tz_localize(None)
    return ts.tz_convert(index.tz)


def _dt_from_index(idx: Any) -> datetime:
    ts = pd.Timestamp(idx)
    if ts.tzinfo is None:
        ts = ts.tz_localize(timezone.utc)
    return ts.to_pydatetime().astimezone(timezone.utc)


def _parse_direction(value: Any) -> Direction:
    try:
        return Direction(str(value or "NEUTRAL").upper())
    except ValueError:
        return Direction.NEUTRAL


def _parse_time(value: str) -> datetime:
    return _to_utc(datetime.fromisoformat(value.replace("Z", "+00:00")))


def _to_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _optional_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _avg(values: Iterable[Optional[float]]) -> Optional[float]:
    nums = [float(value) for value in values if value is not None]
    if not nums:
        return None
    return sum(nums) / len(nums)


def _rate(records: Iterable[dict[str, Any]], predicate: Callable[[dict[str, Any]], bool]) -> float:
    items = list(records)
    if not items:
        return 0.0
    return sum(1 for item in items if predicate(item)) / len(items) * 100.0


def _profile_from_record(record: dict[str, Any]) -> dict[str, Any]:
    raw_json = record.get("raw_json") or {}
    profile = raw_json.get("profile") if isinstance(raw_json, dict) else {}
    return profile if isinstance(profile, dict) else {}


def _none_to_zero(value: Optional[float]) -> float:
    return 0.0 if value is None else float(value)


def _safe_ratio(value: float, denominator: float) -> float:
    if denominator <= 0:
        return 0.0
    return float(value) / float(denominator)


def _convergence_key(normalized_key: str) -> str:
    parts = normalized_key.split("|")
    # Drop direction and exact confluence bucket for broader cross convergence.
    return "|".join(part for i, part in enumerate(parts) if i not in (1, len(parts) - 1))


def _load_json_list(value: Any) -> list[str]:
    try:
        parsed = json.loads(str(value or "[]"))
    except json.JSONDecodeError:
        return []
    if not isinstance(parsed, list):
        return []
    return [str(item) for item in parsed]


def _load_json_dict(value: Any) -> dict[str, Any]:
    try:
        parsed = json.loads(str(value or "{}"))
    except json.JSONDecodeError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _fmt(value: Any) -> str:
    return "-" if value is None else f"{float(value):+.1f}"


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="MMM event-based replay and setup mining")
    sub = parser.add_subparsers(dest="command", required=True)

    p_flashcards = sub.add_parser("flashcards", help="Replay flashcards through MMM events")
    p_flashcards.add_argument("--min-confluence", type=int, default=50)
    p_flashcards.add_argument("--limit", type=int, default=100)

    p_enrich = sub.add_parser("enrich-flashcards", help="Backfill flashcard TDI/pattern context")
    p_enrich.add_argument("--min-confluence", type=int, default=30)
    p_enrich.add_argument("--limit", type=int, default=500)
    p_enrich.add_argument(
        "--all",
        action="store_true",
        help="Recompute rows even when enrichment fields are already populated",
    )

    p_pair = sub.add_parser("pair-report", help="Show event performance by pair")
    p_pair.add_argument("--min-total", type=int, default=1)

    p_setup = sub.add_parser("setup-report", help="Show repeated normalized setup signatures")
    p_setup.add_argument("--min-total", type=int, default=2)

    p_convergence = sub.add_parser("convergence-report", help="Show cross-pair setup convergence")
    p_convergence.add_argument("--min-symbols", type=int, default=2)
    p_convergence.add_argument("--limit", type=int, default=500)

    p_calibration = sub.add_parser("calibration-report", help="Show pair setting recommendations")
    p_calibration.add_argument("--min-total", type=int, default=5)

    p_ablation = sub.add_parser("gate-ablation-report", help="Compare MMM entry gate variants")
    p_ablation.add_argument("--min-total", type=int, default=5)
    p_ablation.add_argument("--symbol", default=None)

    p_advisory = sub.add_parser(
        "advisory-report",
        help="Bucket outcomes by convergence-weighted advisory grade",
    )
    p_advisory.add_argument("--min-total", type=int, default=3)
    p_advisory.add_argument("--symbol", default=None)
    p_advisory.add_argument("--peer-window-minutes", type=int, default=240)

    p_propose = sub.add_parser(
        "calibration-propose",
        help="Preview PairProfile advisory gate changes from replay evidence",
    )
    p_propose.add_argument("--min-total", type=int, default=5)
    p_propose.add_argument("--symbol", default=None)

    args = parser.parse_args(argv)
    replay = MMMEventReplay()
    try:
        if args.command == "flashcards":
            from helix_v3.backtest.scanner_replay import (
                connect_mt5,
                disconnect_mt5,
                fetch_rates_range,
                get_pip_size,
            )

            if not connect_mt5():
                raise SystemExit(1)
            try:
                count = replay.label_flashcards(
                    fetch_rates=fetch_rates_range,
                    get_pip_size=get_pip_size,
                    min_confluence=args.min_confluence,
                    limit=args.limit,
                )
            finally:
                disconnect_mt5()
            print(f"Recorded/reused {count} MMM event outcomes.")
        elif args.command == "enrich-flashcards":
            from helix_v3.backtest.scanner_replay import (
                connect_mt5,
                disconnect_mt5,
                fetch_rates_range,
                get_pip_size,
            )

            if not connect_mt5():
                raise SystemExit(1)
            try:
                count = replay.enrich_flashcards(
                    fetch_rates=fetch_rates_range,
                    get_pip_size=get_pip_size,
                    min_confluence=args.min_confluence,
                    limit=args.limit,
                    missing_only=not args.all,
                )
            finally:
                disconnect_mt5()
            print(f"Enriched {count} flashcards.")
        elif args.command == "pair-report":
            print(replay.pair_report(min_total=args.min_total))
        elif args.command == "setup-report":
            print(replay.setup_report(min_total=args.min_total))
        elif args.command == "convergence-report":
            print(replay.convergence_report(min_symbols=args.min_symbols, limit=args.limit))
        elif args.command == "calibration-report":
            print(replay.calibration_report(min_total=args.min_total))
        elif args.command == "gate-ablation-report":
            print(replay.gate_ablation_report(min_total=args.min_total, symbol=args.symbol))
        elif args.command == "advisory-report":
            print(
                replay.advisory_report(
                    min_total=args.min_total,
                    symbol=args.symbol,
                    peer_window_minutes=args.peer_window_minutes,
                )
            )
        elif args.command == "calibration-propose":
            print(replay.calibration_proposal_report(min_total=args.min_total, symbol=args.symbol))
    finally:
        replay.close()


if __name__ == "__main__":
    main()
