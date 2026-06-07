"""Validate taught MMM rule candidates against historical market behavior.

This module evaluates paraphrased training-derived rule cards as hypotheses.
It does not promote a rule into live strategy logic. Promotion still happens
through the validation library after sufficient replay evidence.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import zlib
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

import pandas as pd

from config.pair_profiles import PairProfile, get_pair_profile
from config.settings import settings
from helix_v3.backtest.data_store import HistoricalDataStore
from helix_v3.backtest.mmm_event_replay import (
    MMMEventOutcome,
    ReplaySetup,
    label_mmm_event_path,
)
from helix_v3.core.sessions import SessionInfo, classify_sessions
from helix_v3.core.tdi import TDISignal, compute_tdi
from helix_v3.core.types import Direction

DEFAULT_DB_PATH = Path(settings.log_dir) / "taught_rule_validation.db"

FAVORABLE_OUTCOMES = {"TARGET_2", "TRAIL_STOP", "TIME_EXIT_PROFIT", "OPEN_PROFIT"}
DIRECT_ENTRY_RULES = {
    "MMM-TRAIN-002",
    "MMM-TRAIN-003",
    "MMM-TRAIN-004",
    "MMM-TRAIN-006",
}

SCHEMA = """
CREATE TABLE IF NOT EXISTS taught_rule_events (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at          TEXT NOT NULL DEFAULT (datetime('now')),

    rule_id             TEXT NOT NULL,
    symbol              TEXT NOT NULL,
    timeframe           TEXT NOT NULL,
    snapshot_at         TEXT NOT NULL,
    direction           TEXT NOT NULL,
    entry_price         REAL NOT NULL,
    score               REAL NOT NULL,

    outcome             TEXT NOT NULL,
    exit_pips           REAL,
    max_favorable_pips  REAL,
    max_adverse_pips    REAL,
    t1_hit              INTEGER NOT NULL,
    minutes_to_t1       REAL,

    details_json        TEXT NOT NULL,
    outcome_json        TEXT NOT NULL,

    UNIQUE(rule_id, symbol, timeframe, snapshot_at, direction)
);

CREATE INDEX IF NOT EXISTS idx_taught_rule_events_rule
    ON taught_rule_events(rule_id, symbol);
CREATE INDEX IF NOT EXISTS idx_taught_rule_events_outcome
    ON taught_rule_events(outcome);
"""


@dataclass(frozen=True)
class TaughtRuleHit:
    rule_id: str
    symbol: str
    timeframe: str
    snapshot_at: datetime
    direction: Direction
    entry_price: float
    score: float
    details: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class TaughtRuleEvaluation:
    hit: TaughtRuleHit
    outcome: MMMEventOutcome


class TaughtRuleValidationStore:
    def __init__(self, db_path: Optional[Path] = None) -> None:
        self._db_path = db_path or DEFAULT_DB_PATH
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self._db_path))
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.executescript(SCHEMA)
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    def record(self, evaluation: TaughtRuleEvaluation) -> None:
        hit = evaluation.hit
        outcome = evaluation.outcome
        self._conn.execute(
            """INSERT OR REPLACE INTO taught_rule_events (
                rule_id, symbol, timeframe, snapshot_at, direction, entry_price, score,
                outcome, exit_pips, max_favorable_pips, max_adverse_pips,
                t1_hit, minutes_to_t1, details_json, outcome_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                hit.rule_id,
                hit.symbol,
                hit.timeframe,
                _to_utc(hit.snapshot_at).isoformat(),
                hit.direction.value,
                hit.entry_price,
                hit.score,
                outcome.outcome,
                outcome.exit_pips,
                outcome.max_favorable_pips,
                outcome.max_adverse_pips,
                int(outcome.t1_hit),
                outcome.minutes_to_t1,
                json.dumps(hit.details, sort_keys=True, default=str),
                json.dumps(asdict(outcome), sort_keys=True, default=str),
            ),
        )
        self._conn.commit()

    def record_many(self, evaluations: list[TaughtRuleEvaluation]) -> None:
        for evaluation in evaluations:
            self.record(evaluation)

    def delete_scope(
        self,
        *,
        symbols: list[str],
        rule_ids: set[str],
        timeframe: str = "M15",
    ) -> int:
        if not symbols or not rule_ids:
            return 0
        symbol_marks = ", ".join("?" for _ in symbols)
        rule_marks = ", ".join("?" for _ in rule_ids)
        cursor = self._conn.execute(
            f"""DELETE FROM taught_rule_events
            WHERE symbol IN ({symbol_marks})
              AND rule_id IN ({rule_marks})
              AND timeframe = ?""",
            (*symbols, *sorted(rule_ids), timeframe),
        )
        self._conn.commit()
        return int(cursor.rowcount or 0)

    def summary_rows(self, *, min_total: int = 1) -> list[dict[str, Any]]:
        rows = self._conn.execute(
            """SELECT
                rule_id,
                symbol,
                COUNT(*) AS total,
                SUM(CASE WHEN outcome IN ('TARGET_2', 'TRAIL_STOP', 'TIME_EXIT_PROFIT',
                    'OPEN_PROFIT') THEN 1 ELSE 0 END) AS favorable,
                SUM(CASE WHEN t1_hit = 1 THEN 1 ELSE 0 END) AS t1_hits,
                AVG(exit_pips) AS avg_exit_pips,
                AVG(max_favorable_pips) AS avg_mfe,
                AVG(max_adverse_pips) AS avg_mae
            FROM taught_rule_events
            GROUP BY rule_id, symbol
            HAVING total >= ?
            ORDER BY rule_id, favorable * 1.0 / total DESC, total DESC""",
            (min_total,),
        ).fetchall()
        return [_summary_row_dict(row) for row in rows]

    def report(self, *, min_total: int = 1) -> str:
        rows = self.summary_rows(min_total=min_total)
        if not rows:
            return "No taught-rule validation events recorded yet."

        lines = [
            "",
            "=" * 118,
            "  MMM TRAINING RULE VALIDATION",
            "=" * 118,
            f"  {'Rule':<14} {'Symbol':<8} {'N':>5} {'Fav%':>7} {'T1%':>7} "
            f"{'AvgExit':>9} {'MFE':>9} {'MAE':>9}",
            "-" * 118,
        ]
        for row in rows:
            total = int(row["total"])
            lines.append(
                f"  {str(row['rule_id']):<14} {str(row['symbol']):<8} {total:>5} "
                f"{float(row['favorable_rate']):>6.1f}% "
                f"{float(row['t1_rate']):>6.1f}% "
                f"{_fmt(row['avg_exit_pips']):>9} "
                f"{_fmt(row['avg_mfe']):>9} "
                f"{_fmt(row['avg_mae']):>9}"
            )
        lines.append("=" * 118)
        return "\n".join(lines)

    def markdown_report(
        self,
        *,
        min_total: int = 1,
        generated_at: Optional[datetime] = None,
        scanner_baseline: Optional[str] = None,
    ) -> str:
        rows = self.summary_rows(min_total=min_total)
        generated = _to_utc(generated_at or datetime.now(timezone.utc))
        if not rows:
            return "\n".join(
                [
                    "# MMM Taught Rule Validation Report",
                    "",
                    f"Generated: {generated.isoformat()}",
                    "",
                    "No taught-rule validation events are recorded yet.",
                    "",
                ]
            )

        watch = [
            f"{row['rule_id']} {row['symbol']}"
            for row in rows
            if _validation_decision(row).startswith("watch")
        ]
        weak_or_rejected = [
            f"{row['rule_id']} {row['symbol']}"
            for row in rows
            if _validation_decision(row) == "needs_stricter_filter"
        ]

        lines = [
            "# MMM Taught Rule Validation Report",
            "",
            f"Generated: {generated.isoformat()}",
            "",
            "Scope: first-pass historical M15 replay of paraphrased MMM training rule cards.",
            "These are detector hypotheses, not promoted trading rules.",
            "",
            "## Promotion State",
            "",
            "- Promoted rules: none.",
            "- Watchlist: " + (", ".join(watch) if watch else "none."),
            "- Needs stricter filters: "
            + (", ".join(weak_or_rejected) if weak_or_rejected else "none."),
            "",
            "## Scanner Baseline Gate",
            "",
        ]
        if scanner_baseline:
            lines.append(f"- Current scanner baseline: {scanner_baseline}")
        else:
            lines.append("- Current scanner baseline: not embedded in this report.")
        lines.extend(
            [
                "- No taught candidate is promoted unless it beats the scanner baseline "
                "after pair-specific replay.",
                "",
                "## Results",
                "",
                "| Decision | Rule | Symbol | N | Fav% | T1% | AvgExit | MFE | MAE |",
                "|---|---|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in rows:
            lines.append(
                f"| {_validation_decision(row)} | {row['rule_id']} | {row['symbol']} | "
                f"{int(row['total'])} | {float(row['favorable_rate']):.1f}% | "
                f"{float(row['t1_rate']):.1f}% | {_fmt(row['avg_exit_pips'])} | "
                f"{_fmt(row['avg_mfe'])} | {_fmt(row['avg_mae'])} |"
            )
        lines.extend(
            [
                "",
                "## Interpretation",
                "",
                "- `MMM-TRAIN-004` is the only practical watchlist family in this pass, "
                "especially GBPJPY, AUDUSD, and USDJPY; sample size remains low.",
                "- `MMM-TRAIN-002` is weakly positive only on GBPJPY and should be "
                "pair-specific if refined.",
                "- `MMM-TRAIN-003` and `MMM-TRAIN-006` underperform in this naive detector "
                "form and should not be used as entry gates.",
                "- `MMM-TRAIN-001`, `MMM-TRAIN-005`, `MMM-TRAIN-007`, and `MMM-TRAIN-008` "
                "still need dedicated validators because they are context, day-map, exit, "
                "or preparation rules rather than direct entries.",
                "",
                "## Next Calibration Work",
                "",
                "- Tighten `MMM-TRAIN-004` with pair-specific Asian range, session, "
                "return-inside, and M/W confirmation filters.",
                "- Build a pivot/day-map validator for `MMM-TRAIN-005` before evaluating "
                "M3-to-M1 target logic.",
                "- Compare each refined taught-rule detector against the scanner baseline "
                "and only then promote to the validation library.",
                "",
            ]
        )
        return "\n".join(lines)

    def write_markdown_report(
        self,
        path: Path,
        *,
        min_total: int = 1,
        scanner_baseline: Optional[str] = None,
    ) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            self.markdown_report(
                min_total=min_total,
                scanner_baseline=scanner_baseline,
            ),
            encoding="utf-8",
        )
        return path


class TaughtRuleValidator:
    def __init__(self, *, store: Optional[TaughtRuleValidationStore] = None) -> None:
        self._store = store or TaughtRuleValidationStore()

    def close(self) -> None:
        self._store.close()

    def validate_frames(
        self,
        *,
        symbol: str,
        df_m15: pd.DataFrame,
        pip_size: float,
        rule_ids: Optional[set[str]] = None,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        step_bars: int = 4,
        min_spacing_minutes: int = 90,
        limit_per_rule: int = 100,
    ) -> list[TaughtRuleEvaluation]:
        df = _normalize_df(df_m15)
        if df.empty:
            return []

        profile = get_pair_profile(symbol)
        sessions = classify_sessions(df, pip_size)
        allowed_rules = rule_ids or DIRECT_ENTRY_RULES
        counts: dict[str, int] = {}
        last_hit: dict[tuple[str, Direction], datetime] = {}
        evaluations: list[TaughtRuleEvaluation] = []

        start_ts = _timestamp_for_index(start, df.index) if start else df.index[0]
        end_ts = _timestamp_for_index(end, df.index) if end else df.index[-1]
        candidate_positions = [
            idx
            for idx, ts in enumerate(df.index)
            if idx >= 60 and start_ts <= ts <= end_ts and idx % max(1, step_bars) == 0
        ]

        for position in candidate_positions:
            hits: list[TaughtRuleHit] = []
            if "MMM-TRAIN-002" in allowed_rules:
                hit = detect_three_hit_w_reversal(symbol, df, position, pip_size, profile, sessions)
                if hit:
                    hits.append(hit)
            if "MMM-TRAIN-003" in allowed_rules:
                hit = detect_stop_hunt_high_m_reversal(symbol, df, position, pip_size, profile, sessions)
                if hit:
                    hits.append(hit)
            if "MMM-TRAIN-004" in allowed_rules:
                hit = detect_asian_stop_hunt_tdi_shark(symbol, df, position, pip_size, profile, sessions)
                if hit:
                    hits.append(hit)
            if "MMM-TRAIN-006" in allowed_rules:
                hits.extend(detect_hod_lod_ma_confirmation(symbol, df, position, pip_size, profile, sessions))

            for hit in hits:
                if counts.get(hit.rule_id, 0) >= limit_per_rule:
                    continue
                key = (hit.rule_id, hit.direction)
                previous = last_hit.get(key)
                if previous and (
                    hit.snapshot_at - previous
                ).total_seconds() < min_spacing_minutes * 60:
                    continue
                outcome = evaluate_hit(hit, df=df, pip_size=pip_size, profile=profile)
                evaluation = TaughtRuleEvaluation(hit=hit, outcome=outcome)
                self._store.record(evaluation)
                evaluations.append(evaluation)
                counts[hit.rule_id] = counts.get(hit.rule_id, 0) + 1
                last_hit[key] = hit.snapshot_at
        return evaluations

    def report(self, *, min_total: int = 1) -> str:
        return self._store.report(min_total=min_total)


def detect_three_hit_w_reversal(
    symbol: str,
    df: pd.DataFrame,
    position: int,
    pip_size: float,
    profile: PairProfile,
    sessions: SessionInfo,
) -> Optional[TaughtRuleHit]:
    if _session_at(sessions, df.index[position]) == "ASIA":
        return None
    window = df.iloc[position - 11 : position + 1]
    if len(window) < 12:
        return None

    window_low = float(window["Low"].min())
    window_high = float(window["High"].max())
    test_zone_pips = max(3.0, profile.stop_hunt_min_pips * 0.25)
    tests = window[(window["Low"] - window_low) / pip_size <= test_zone_pips]
    if len(tests) < 3:
        return None

    current = window.iloc[-1]
    current_close = float(current["Close"])
    current_open = float(current["Open"])
    range_pips = (window_high - window_low) / pip_size
    close_reclaim_pips = (current_close - window_low) / pip_size
    if current_close <= current_open or close_reclaim_pips < max(8.0, range_pips * 0.25):
        return None

    asian = _asian_for_timestamp(sessions, df.index[position])
    asian_low = _optional_float((asian or {}).get("low"))
    stop_hunt_pips = max(0.0, (asian_low - window_low) / pip_size) if asian_low else 0.0
    snapshot_at = _dt_from_index(df.index[position])
    return TaughtRuleHit(
        rule_id="MMM-TRAIN-002",
        symbol=symbol,
        timeframe="M15",
        snapshot_at=snapshot_at,
        direction=Direction.BUY,
        entry_price=current_close,
        score=min(100.0, 40.0 + len(tests) * 10.0 + close_reclaim_pips),
        details={
            "detector": "three_hit_w_reversal",
            "push_count": int(len(tests)),
            "window_low": window_low,
            "window_high": window_high,
            "range_pips": range_pips,
            "close_reclaim_pips": close_reclaim_pips,
            "asian_range_pips": _optional_float((asian or {}).get("pips")),
            "stop_hunt_pips": stop_hunt_pips,
            "m_w_pattern": "W_BOTTOM",
        },
    )


def detect_stop_hunt_high_m_reversal(
    symbol: str,
    df: pd.DataFrame,
    position: int,
    pip_size: float,
    profile: PairProfile,
    sessions: SessionInfo,
) -> Optional[TaughtRuleHit]:
    del profile
    level = _upper_liquidity_level(df, position, sessions)
    if level is None:
        return None

    window = df.iloc[position - 5 : position + 1]
    if len(window) < 6:
        return None
    breach_pips = (float(window["High"].max()) - level) / pip_size
    current = window.iloc[-1]
    close = float(current["Close"])
    if breach_pips < 2.0 or close >= level or close >= float(current["Open"]):
        return None

    snapshot_at = _dt_from_index(df.index[position])
    asian = _asian_for_timestamp(sessions, df.index[position])
    return TaughtRuleHit(
        rule_id="MMM-TRAIN-003",
        symbol=symbol,
        timeframe="M15",
        snapshot_at=snapshot_at,
        direction=Direction.SELL,
        entry_price=close,
        score=min(100.0, 45.0 + breach_pips * 2.0),
        details={
            "detector": "stop_hunt_high_m_reversal",
            "liquidity_level": level,
            "breach_pips": breach_pips,
            "asian_range_pips": _optional_float((asian or {}).get("pips")),
            "stop_hunt_pips": breach_pips,
            "m_w_pattern": "M_TOP",
        },
    )


def detect_asian_stop_hunt_tdi_shark(
    symbol: str,
    df: pd.DataFrame,
    position: int,
    pip_size: float,
    profile: PairProfile,
    sessions: SessionInfo,
) -> Optional[TaughtRuleHit]:
    asian = _asian_for_timestamp(sessions, df.index[position])
    if not asian:
        return None
    if _session_at(sessions, df.index[position]) == "ASIA":
        return None

    asian_high = _optional_float(asian.get("high"))
    asian_low = _optional_float(asian.get("low"))
    if asian_high is None or asian_low is None:
        return None

    window = df.iloc[position - 5 : position + 1]
    current = window.iloc[-1]
    close = float(current["Close"])
    high_hunt = (float(window["High"].max()) - asian_high) / pip_size
    low_hunt = (asian_low - float(window["Low"].min())) / pip_size
    snapshot_at = _dt_from_index(df.index[position])
    possible_short = high_hunt >= profile.stop_hunt_min_pips and close < asian_high
    possible_long = low_hunt >= profile.stop_hunt_min_pips and close > asian_low
    if not possible_short and not possible_long:
        return None

    past = df.iloc[max(0, position - 120) : position + 1]
    if len(past) < 60:
        return None
    tdi = compute_tdi(past)
    signals = [signal.value for signal in tdi.signals]

    if possible_short and TDISignal.SHARK_FIN_SHORT.value in signals:
        return TaughtRuleHit(
            rule_id="MMM-TRAIN-004",
            symbol=symbol,
            timeframe="M15",
            snapshot_at=snapshot_at,
            direction=Direction.SELL,
            entry_price=close,
            score=min(100.0, 55.0 + high_hunt),
            details={
                "detector": "asian_stop_hunt_tdi_shark",
                "asian_high": asian_high,
                "asian_low": asian_low,
                "asian_range_pips": _optional_float(asian.get("pips")),
                "stop_hunt_pips": high_hunt,
                "tdi_signals": signals,
                "tdi_shark_direction": tdi.shark_fin_direction,
                "m_w_pattern": "M_TOP",
            },
        )

    if possible_long and TDISignal.SHARK_FIN_LONG.value in signals:
        return TaughtRuleHit(
            rule_id="MMM-TRAIN-004",
            symbol=symbol,
            timeframe="M15",
            snapshot_at=snapshot_at,
            direction=Direction.BUY,
            entry_price=close,
            score=min(100.0, 55.0 + low_hunt),
            details={
                "detector": "asian_stop_hunt_tdi_shark",
                "asian_high": asian_high,
                "asian_low": asian_low,
                "asian_range_pips": _optional_float(asian.get("pips")),
                "stop_hunt_pips": low_hunt,
                "tdi_signals": signals,
                "tdi_shark_direction": tdi.shark_fin_direction,
                "m_w_pattern": "W_BOTTOM",
            },
        )
    return None


def detect_hod_lod_ma_confirmation(
    symbol: str,
    df: pd.DataFrame,
    position: int,
    pip_size: float,
    profile: PairProfile,
    sessions: SessionInfo,
) -> list[TaughtRuleHit]:
    del profile
    if position < 20:
        return []
    past = df.iloc[: position + 1]
    ema5 = past["Close"].ewm(span=5, adjust=False).mean()
    ema13 = past["Close"].ewm(span=13, adjust=False).mean()
    prev5, curr5 = float(ema5.iloc[-2]), float(ema5.iloc[-1])
    prev13, curr13 = float(ema13.iloc[-2]), float(ema13.iloc[-1])
    current = past.iloc[-1]
    close = float(current["Close"])
    snapshot_at = _dt_from_index(df.index[position])
    hits: list[TaughtRuleHit] = []

    upper = _upper_liquidity_level(df, position, sessions)
    if upper is not None:
        window = df.iloc[position - 7 : position + 1]
        breach_pips = (float(window["High"].max()) - upper) / pip_size
        if breach_pips >= 2.0 and close < upper and prev5 >= prev13 and curr5 < curr13:
            hits.append(
                TaughtRuleHit(
                    rule_id="MMM-TRAIN-006",
                    symbol=symbol,
                    timeframe="M15",
                    snapshot_at=snapshot_at,
                    direction=Direction.SELL,
                    entry_price=close,
                    score=min(100.0, 50.0 + breach_pips * 2.0),
                    details={
                        "detector": "hod_lod_ma_confirmation",
                        "confirmation": "EMA5_CROSS_BELOW_EMA13",
                        "liquidity_level": upper,
                        "stop_hunt_pips": breach_pips,
                        "m_w_pattern": "M_TOP",
                    },
                )
            )

    lower = _lower_liquidity_level(df, position, sessions)
    if lower is not None:
        window = df.iloc[position - 7 : position + 1]
        breach_pips = (lower - float(window["Low"].min())) / pip_size
        if breach_pips >= 2.0 and close > lower and prev5 <= prev13 and curr5 > curr13:
            hits.append(
                TaughtRuleHit(
                    rule_id="MMM-TRAIN-006",
                    symbol=symbol,
                    timeframe="M15",
                    snapshot_at=snapshot_at,
                    direction=Direction.BUY,
                    entry_price=close,
                    score=min(100.0, 50.0 + breach_pips * 2.0),
                    details={
                        "detector": "hod_lod_ma_confirmation",
                        "confirmation": "EMA5_CROSS_ABOVE_EMA13",
                        "liquidity_level": lower,
                        "stop_hunt_pips": breach_pips,
                        "m_w_pattern": "W_BOTTOM",
                    },
                )
            )
    return hits


def evaluate_hit(
    hit: TaughtRuleHit,
    *,
    df: pd.DataFrame,
    pip_size: float,
    profile: Optional[PairProfile] = None,
) -> MMMEventOutcome:
    details = hit.details
    setup = ReplaySetup(
        symbol=hit.symbol,
        timeframe=hit.timeframe,
        snapshot_at=hit.snapshot_at,
        direction=hit.direction,
        confluence_score=int(min(100, max(0, round(hit.score)))),
        asian_range_pips=_optional_float(details.get("asian_range_pips")),
        accumulation_valid=bool(_optional_float(details.get("asian_range_pips"))),
        stop_hunt_detected=True,
        stop_hunt_direction=hit.direction,
        stop_hunt_pips=_optional_float(details.get("stop_hunt_pips")),
        push_count=int(details.get("push_count", 3 if details.get("m_w_pattern") else 0) or 0),
        m_w_forming=bool(details.get("m_w_pattern")),
        m_w_pattern=str(details.get("m_w_pattern") or ""),
        tdi_signals=list(details.get("tdi_signals", [])),
        tdi_shark_fin=bool(details.get("tdi_shark_direction")),
        tdi_shark_direction=str(details.get("tdi_shark_direction") or ""),
        source="taught_rule",
        source_id=_stable_source_id(hit),
    )
    return label_mmm_event_path(
        df,
        setup=setup,
        entry_price=hit.entry_price,
        pip_size=pip_size,
        profile=profile,
        asian_high=_optional_float(details.get("asian_high")),
        asian_low=_optional_float(details.get("asian_low")),
    )


def run_mt5_validation(
    *,
    symbols: list[str],
    days: int,
    rule_ids: Optional[set[str]],
    step_bars: int,
    limit_per_rule: int,
    min_spacing_minutes: int,
    db_path: Optional[Path] = None,
    replace_scope: bool = False,
) -> str:
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days)
    data_store = HistoricalDataStore(symbols, start, end)
    data_store.load()
    store = TaughtRuleValidationStore(db_path)
    if replace_scope:
        store.delete_scope(
            symbols=symbols,
            rule_ids=rule_ids or DIRECT_ENTRY_RULES,
        )
    validator = TaughtRuleValidator(store=store)
    try:
        for symbol in symbols:
            df_m15 = data_store.get_rates(symbol, "M15", end, days * 96 + 800)
            validator.validate_frames(
                symbol=symbol,
                df_m15=df_m15,
                pip_size=data_store.get_pip_size(symbol),
                rule_ids=rule_ids,
                start=start,
                end=end,
                step_bars=step_bars,
                min_spacing_minutes=min_spacing_minutes,
                limit_per_rule=limit_per_rule,
            )
        return validator.report(min_total=1)
    finally:
        validator.close()


def _upper_liquidity_level(
    df: pd.DataFrame,
    position: int,
    sessions: SessionInfo,
) -> Optional[float]:
    ts = df.index[position]
    prev_hod, _prev_lod = _previous_day_hilo(df, ts)
    asian = _asian_for_timestamp(sessions, ts)
    levels = [value for value in [prev_hod, _optional_float((asian or {}).get("high"))] if value]
    return max(levels) if levels else None


def _lower_liquidity_level(
    df: pd.DataFrame,
    position: int,
    sessions: SessionInfo,
) -> Optional[float]:
    ts = df.index[position]
    _prev_hod, prev_lod = _previous_day_hilo(df, ts)
    asian = _asian_for_timestamp(sessions, ts)
    levels = [value for value in [prev_lod, _optional_float((asian or {}).get("low"))] if value]
    return min(levels) if levels else None


def _previous_day_hilo(df: pd.DataFrame, ts: pd.Timestamp) -> tuple[Optional[float], Optional[float]]:
    current_date = ts.date()
    previous_dates = sorted({idx.date() for idx in df.index if idx.date() < current_date})
    if not previous_dates:
        return None, None
    previous = df[[idx.date() == previous_dates[-1] for idx in df.index]]
    if previous.empty:
        return None, None
    return float(previous["High"].max()), float(previous["Low"].min())


def _asian_for_timestamp(sessions: SessionInfo, ts: pd.Timestamp) -> Optional[dict[str, Any]]:
    return sessions.asian_ranges.get(str(ts.date()))


def _session_at(sessions: SessionInfo, ts: pd.Timestamp) -> str:
    if ts in sessions.labels.index:
        return str(sessions.labels.loc[ts])
    return ""


def _stable_source_id(hit: TaughtRuleHit) -> int:
    key = f"{hit.rule_id}|{hit.symbol}|{hit.snapshot_at.isoformat()}|{hit.direction.value}"
    return zlib.crc32(key.encode("utf-8"))


def _normalize_df(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()
    out = df.copy()
    if not isinstance(out.index, pd.DatetimeIndex):
        raise ValueError("Expected DataFrame with DatetimeIndex")
    if out.index.tz is None:
        out.index = out.index.tz_localize(timezone.utc)
    else:
        out.index = out.index.tz_convert(timezone.utc)
    return out.sort_index()


def _timestamp_for_index(value: datetime, index: pd.DatetimeIndex) -> pd.Timestamp:
    ts = pd.Timestamp(value)
    if index.tz is not None and ts.tzinfo is None:
        ts = ts.tz_localize(timezone.utc)
    elif index.tz is None and ts.tzinfo is not None:
        ts = ts.tz_convert(timezone.utc).tz_localize(None)
    elif index.tz is not None and ts.tzinfo is not None:
        ts = ts.tz_convert(index.tz)
    return ts


def _dt_from_index(value: Any) -> datetime:
    ts = pd.Timestamp(value)
    if ts.tzinfo is None:
        ts = ts.tz_localize(timezone.utc)
    else:
        ts = ts.tz_convert(timezone.utc)
    return ts.to_pydatetime()


def _to_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def _optional_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _summary_row_dict(row: sqlite3.Row) -> dict[str, Any]:
    total = int(row["total"] or 0)
    favorable = int(row["favorable"] or 0)
    t1_hits = int(row["t1_hits"] or 0)
    favorable_rate = favorable / total * 100.0 if total else 0.0
    t1_rate = t1_hits / total * 100.0 if total else 0.0
    return {
        "rule_id": str(row["rule_id"]),
        "symbol": str(row["symbol"]),
        "total": total,
        "favorable": favorable,
        "t1_hits": t1_hits,
        "favorable_rate": favorable_rate,
        "t1_rate": t1_rate,
        "avg_exit_pips": _optional_float(row["avg_exit_pips"]),
        "avg_mfe": _optional_float(row["avg_mfe"]),
        "avg_mae": _optional_float(row["avg_mae"]),
    }


def _validation_decision(row: dict[str, Any]) -> str:
    total = int(row["total"])
    favorable_rate = float(row["favorable_rate"])
    t1_rate = float(row["t1_rate"])
    avg_exit = _optional_float(row["avg_exit_pips"]) or 0.0

    if total >= 5 and avg_exit > 0 and favorable_rate >= 45.0:
        return "watch"
    if total < 15 and avg_exit >= 5.0 and t1_rate >= 50.0:
        return "watch_low_sample"
    if total >= 30 and avg_exit > 0 and favorable_rate >= 40.0:
        return "watch_weak_pair_specific"
    return "needs_stricter_filter"


def _fmt(value: Any) -> str:
    number = _optional_float(value)
    if number is None:
        return "-"
    return f"{number:.1f}"


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Validate taught MMM rule candidates")
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate", help="Run historical MT5 validation")
    p_validate.add_argument("--symbols", required=True, help="Comma-separated symbols")
    p_validate.add_argument("--days", type=int, default=180)
    p_validate.add_argument("--rule-id", action="append", dest="rule_ids")
    p_validate.add_argument("--step-bars", type=int, default=4)
    p_validate.add_argument("--limit-per-rule", type=int, default=100)
    p_validate.add_argument("--min-spacing-minutes", type=int, default=90)
    p_validate.add_argument("--db-path", type=Path)
    p_validate.add_argument(
        "--replace-scope",
        action="store_true",
        help="Delete existing rows for the selected symbols/rules before validating",
    )

    p_report = sub.add_parser("report", help="Report stored validation results")
    p_report.add_argument("--min-total", type=int, default=1)
    p_report.add_argument("--db-path", type=Path)

    p_export = sub.add_parser("export-report", help="Write stored validation results to markdown")
    p_export.add_argument("--min-total", type=int, default=1)
    p_export.add_argument("--db-path", type=Path)
    p_export.add_argument(
        "--output",
        type=Path,
        default=Path("data/mmm_training/validation/taught_rule_validation_report.md"),
    )
    p_export.add_argument("--scanner-baseline")

    args = parser.parse_args(argv)
    if args.command == "validate":
        symbols = [item.strip().upper() for item in args.symbols.split(",") if item.strip()]
        report = run_mt5_validation(
            symbols=symbols,
            days=args.days,
            rule_ids=set(args.rule_ids) if args.rule_ids else None,
            step_bars=args.step_bars,
            limit_per_rule=args.limit_per_rule,
            min_spacing_minutes=args.min_spacing_minutes,
            db_path=args.db_path,
            replace_scope=args.replace_scope,
        )
        print(report)
    elif args.command == "report":
        store = TaughtRuleValidationStore(args.db_path)
        try:
            print(store.report(min_total=args.min_total))
        finally:
            store.close()
    elif args.command == "export-report":
        store = TaughtRuleValidationStore(args.db_path)
        try:
            path = store.write_markdown_report(
                args.output,
                min_total=args.min_total,
                scanner_baseline=args.scanner_baseline,
            )
            print(f"Wrote {path}")
        finally:
            store.close()


if __name__ == "__main__":
    main()
