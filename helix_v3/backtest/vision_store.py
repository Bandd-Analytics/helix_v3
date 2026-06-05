"""Persistence and path labeling for vision-model backtests.

This module stores model predictions separately from the live trade journal so
offline experiments cannot contaminate execution records. It is intentionally
SQLite-first: once the labeled corpus is large enough, embeddings/retrieval can
be layered on top without changing the source-of-truth tables.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

import pandas as pd

from config.settings import settings
from helix_v3.core.types import Direction, VisionVerdict
from helix_v3.utils.logger import get_logger

logger = get_logger("vision_backtest_store")

DB_PATH = Path(settings.log_dir) / "vision_backtests.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS vision_predictions (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at          TEXT NOT NULL DEFAULT (datetime('now')),

    -- Source references
    source              TEXT NOT NULL DEFAULT 'vision_consensus',
    source_scan_id      INTEGER,
    flashcard_id        INTEGER,

    -- Snapshot identity
    symbol              TEXT NOT NULL,
    timeframe           TEXT NOT NULL,
    snapshot_at         TEXT NOT NULL,
    chart_path          TEXT,

    -- Model identity and role
    provider            TEXT NOT NULL,
    model_name          TEXT NOT NULL,
    model_role          TEXT NOT NULL,
    prompt_version      TEXT NOT NULL,

    -- Normalized verdict
    direction           TEXT NOT NULL,
    confidence          REAL NOT NULL,
    setup_class         TEXT,
    cycle_level         INTEGER,
    entry_quality       INTEGER,
    m_w_detected        INTEGER,
    rrt_detected        INTEGER,
    pin_bar_detected    INTEGER,
    expected_path       TEXT,
    invalidation        TEXT,
    risk_flags          TEXT,
    reasoning           TEXT,

    -- Raw payload for audits
    raw_json            TEXT NOT NULL,
    backtest_status     TEXT NOT NULL DEFAULT 'PENDING'
);

CREATE TABLE IF NOT EXISTS backtest_outcomes (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    prediction_id       INTEGER NOT NULL REFERENCES vision_predictions(id),
    evaluated_at        TEXT NOT NULL,
    horizon_minutes     INTEGER NOT NULL,

    -- Replay assumptions
    entry_price         REAL NOT NULL,
    direction           TEXT NOT NULL,
    stop_loss_pips      REAL,
    take_profit_pips    REAL,

    -- Path stats
    pips_at_horizon     REAL,
    max_favorable_pips  REAL,
    max_adverse_pips    REAL,
    hit_take_profit     INTEGER,
    hit_stop_loss       INTEGER,

    -- Label
    outcome             TEXT NOT NULL,
    label               TEXT NOT NULL,
    notes               TEXT,

    UNIQUE(prediction_id, horizon_minutes)
);

CREATE INDEX IF NOT EXISTS idx_vp_symbol_time ON vision_predictions(symbol, snapshot_at);
CREATE INDEX IF NOT EXISTS idx_vp_model_role ON vision_predictions(model_role, model_name);
CREATE INDEX IF NOT EXISTS idx_vp_status ON vision_predictions(backtest_status);
CREATE INDEX IF NOT EXISTS idx_bo_prediction ON backtest_outcomes(prediction_id);
CREATE INDEX IF NOT EXISTS idx_bo_outcome ON backtest_outcomes(outcome);
"""


@dataclass(frozen=True)
class PathOutcome:
    horizon_minutes: int
    entry_price: float
    direction: Direction
    stop_loss_pips: Optional[float]
    take_profit_pips: Optional[float]
    pips_at_horizon: Optional[float]
    max_favorable_pips: Optional[float]
    max_adverse_pips: Optional[float]
    hit_take_profit: bool
    hit_stop_loss: bool
    outcome: str
    label: str
    notes: str = ""


class VisionBacktestStore:
    """SQLite persistence for vision predictions and replay labels."""

    def __init__(self, db_path: Optional[Path] = None) -> None:
        self._db_path = db_path or DB_PATH
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self._db_path))
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.executescript(SCHEMA)
        self._conn.commit()
        logger.info("Vision backtest store initialized: %s", self._db_path)

    def close(self) -> None:
        self._conn.close()

    def record_prediction(
        self,
        *,
        symbol: str,
        timeframe: str,
        snapshot_at: datetime,
        provider: str,
        model_role: str,
        verdict: VisionVerdict,
        prompt_version: str,
        chart_path: Optional[str] = None,
        source: str = "vision_consensus",
        source_scan_id: Optional[int] = None,
        flashcard_id: Optional[int] = None,
    ) -> int:
        raw_json = verdict.raw_json or {}
        risk_flags = raw_json.get("risk_flags") or verdict.risk_flags or []

        cursor = self._conn.execute(
            """INSERT INTO vision_predictions (
                source, source_scan_id, flashcard_id,
                symbol, timeframe, snapshot_at, chart_path,
                provider, model_name, model_role, prompt_version,
                direction, confidence, setup_class, cycle_level, entry_quality,
                m_w_detected, rrt_detected, pin_bar_detected,
                expected_path, invalidation, risk_flags, reasoning,
                raw_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                source,
                source_scan_id,
                flashcard_id,
                symbol,
                timeframe,
                snapshot_at.astimezone(timezone.utc).isoformat(),
                chart_path,
                provider,
                verdict.model_name,
                model_role,
                prompt_version,
                verdict.direction.value,
                verdict.confidence,
                verdict.setup_class,
                verdict.cycle_level.value if verdict.cycle_level else None,
                verdict.entry_quality,
                int(verdict.m_w_detected),
                int(verdict.rrt_detected),
                int(verdict.pin_bar_detected),
                verdict.expected_path,
                verdict.invalidation,
                json.dumps(risk_flags, default=str),
                verdict.reasoning,
                json.dumps(raw_json, default=str),
            ),
        )
        self._conn.commit()
        prediction_id = int(cursor.lastrowid)
        logger.info(
            "Vision prediction #%d stored: %s %s %s %s %.2f",
            prediction_id,
            symbol,
            timeframe,
            verdict.model_name,
            verdict.direction.value,
            verdict.confidence,
        )
        return prediction_id

    def record_outcome(self, prediction_id: int, outcome: PathOutcome) -> int:
        cursor = self._conn.execute(
            """INSERT OR REPLACE INTO backtest_outcomes (
                prediction_id, evaluated_at, horizon_minutes,
                entry_price, direction, stop_loss_pips, take_profit_pips,
                pips_at_horizon, max_favorable_pips, max_adverse_pips,
                hit_take_profit, hit_stop_loss, outcome, label, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                prediction_id,
                datetime.now(timezone.utc).isoformat(),
                outcome.horizon_minutes,
                outcome.entry_price,
                outcome.direction.value,
                outcome.stop_loss_pips,
                outcome.take_profit_pips,
                outcome.pips_at_horizon,
                outcome.max_favorable_pips,
                outcome.max_adverse_pips,
                int(outcome.hit_take_profit),
                int(outcome.hit_stop_loss),
                outcome.outcome,
                outcome.label,
                outcome.notes,
            ),
        )
        self._conn.execute(
            "UPDATE vision_predictions SET backtest_status = 'EVALUATED' WHERE id = ?",
            (prediction_id,),
        )
        self._conn.commit()
        return int(cursor.lastrowid)

    def get_pending_predictions(self, limit: int = 100) -> list[dict[str, Any]]:
        return self.get_predictions(status="PENDING", limit=limit)

    def get_predictions(
        self,
        *,
        status: Optional[str] = None,
        limit: int = 100,
    ) -> list[dict[str, Any]]:
        if status is None:
            rows = self._conn.execute(
                """SELECT * FROM vision_predictions
                ORDER BY snapshot_at
                LIMIT ?""",
                (limit,),
            ).fetchall()
            return [dict(row) for row in rows]

        rows = self._conn.execute(
            """SELECT * FROM vision_predictions
            WHERE backtest_status = ?
            ORDER BY snapshot_at
            LIMIT ?""",
            (status, limit),
        ).fetchall()
        return [dict(row) for row in rows]

    def find_prediction_id(
        self,
        *,
        source: str,
        source_scan_id: Optional[int],
        model_role: str,
        model_name: str,
    ) -> Optional[int]:
        row = self._conn.execute(
            """SELECT id FROM vision_predictions
            WHERE source = ?
              AND source_scan_id IS ?
              AND model_role = ?
              AND model_name = ?
            ORDER BY id
            LIMIT 1""",
            (source, source_scan_id, model_role, model_name),
        ).fetchone()
        return int(row["id"]) if row else None

    def summarize(self) -> dict[str, Any]:
        predictions = self._conn.execute(
            "SELECT COUNT(*) AS total FROM vision_predictions"
        ).fetchone()["total"]
        outcomes = self._conn.execute(
            """SELECT outcome, COUNT(*) AS total,
                      AVG(pips_at_horizon) AS avg_pips,
                      AVG(max_favorable_pips) AS avg_mfe,
                      AVG(max_adverse_pips) AS avg_mae
            FROM backtest_outcomes
            GROUP BY outcome"""
        ).fetchall()
        return {
            "predictions": predictions,
            "outcomes": [dict(row) for row in outcomes],
        }

    def summarize_performance(
        self, horizon_minutes: int = 90
    ) -> list[dict[str, Any]]:
        rows = self._conn.execute(
            """SELECT
                p.provider,
                p.model_role,
                p.model_name,
                p.prompt_version,
                o.horizon_minutes,
                COUNT(*) AS total,
                SUM(CASE WHEN o.outcome IN ('WIN', 'OPEN_PROFIT') THEN 1 ELSE 0 END) AS favorable,
                SUM(CASE WHEN o.outcome IN ('LOSS', 'OPEN_LOSS') THEN 1 ELSE 0 END) AS adverse,
                AVG(o.pips_at_horizon) AS avg_pips,
                AVG(o.max_favorable_pips) AS avg_mfe,
                AVG(o.max_adverse_pips) AS avg_mae,
                ROUND(
                    SUM(CASE WHEN o.outcome IN ('WIN', 'OPEN_PROFIT') THEN 1.0 ELSE 0 END)
                    / COUNT(*) * 100,
                    1
                ) AS favorable_rate
            FROM vision_predictions p
            JOIN backtest_outcomes o ON o.prediction_id = p.id
            WHERE o.horizon_minutes = ?
            GROUP BY p.provider, p.model_role, p.model_name, p.prompt_version, o.horizon_minutes
            ORDER BY favorable_rate DESC, avg_pips DESC""",
            (horizon_minutes,),
        ).fetchall()
        return [dict(row) for row in rows]


def label_future_path(
    df: pd.DataFrame,
    *,
    snapshot_at: datetime,
    direction: Direction,
    entry_price: float,
    pip_size: float,
    horizon_minutes: int,
    stop_loss_pips: Optional[float] = None,
    take_profit_pips: Optional[float] = None,
) -> PathOutcome:
    """Label the future path after a prediction using OHLC bars.

    If TP and SL are touched within the same candle, the label is AMBIGUOUS
    because intrabar order cannot be recovered from OHLC alone.
    """

    if direction == Direction.NEUTRAL:
        return PathOutcome(
            horizon_minutes=horizon_minutes,
            entry_price=entry_price,
            direction=direction,
            stop_loss_pips=stop_loss_pips,
            take_profit_pips=take_profit_pips,
            pips_at_horizon=None,
            max_favorable_pips=None,
            max_adverse_pips=None,
            hit_take_profit=False,
            hit_stop_loss=False,
            outcome="NO_TRADE",
            label=f"NO_TRADE_{horizon_minutes}M",
            notes="Neutral prediction is not path-labeled as a trade.",
        )

    if df.empty:
        return _no_data_outcome(
            horizon_minutes, entry_price, direction, stop_loss_pips, take_profit_pips
        )

    snap = pd.Timestamp(snapshot_at)
    if snap.tzinfo is not None and df.index.tz is None:
        snap = snap.tz_convert(timezone.utc).tz_localize(None)
    elif snap.tzinfo is None and df.index.tz is not None:
        snap = snap.tz_localize(timezone.utc)

    end = snap + timedelta(minutes=horizon_minutes)
    future = df[(df.index > snap) & (df.index <= end)]
    if future.empty:
        return _no_data_outcome(
            horizon_minutes, entry_price, direction, stop_loss_pips, take_profit_pips
        )

    favorable: list[float] = []
    adverse: list[float] = []
    pips_at_horizon = _directional_pips(
        direction, entry_price, float(future["Close"].iloc[-1]), pip_size
    )

    first_tp_at: Optional[pd.Timestamp] = None
    first_sl_at: Optional[pd.Timestamp] = None
    ambiguous_at: Optional[pd.Timestamp] = None

    for idx, row in future.iterrows():
        high = float(row["High"])
        low = float(row["Low"])
        if direction == Direction.BUY:
            fav = max(0.0, (high - entry_price) / pip_size)
            adv = max(0.0, (entry_price - low) / pip_size)
        else:
            fav = max(0.0, (entry_price - low) / pip_size)
            adv = max(0.0, (high - entry_price) / pip_size)

        favorable.append(fav)
        adverse.append(adv)

        tp_hit = take_profit_pips is not None and fav >= take_profit_pips
        sl_hit = stop_loss_pips is not None and adv >= stop_loss_pips
        if tp_hit and sl_hit and ambiguous_at is None:
            ambiguous_at = pd.Timestamp(idx)
        elif tp_hit and first_tp_at is None:
            first_tp_at = pd.Timestamp(idx)
        elif sl_hit and first_sl_at is None:
            first_sl_at = pd.Timestamp(idx)

    max_favorable = max(favorable) if favorable else None
    max_adverse = max(adverse) if adverse else None

    hit_tp = first_tp_at is not None or ambiguous_at is not None
    hit_sl = first_sl_at is not None or ambiguous_at is not None

    if ambiguous_at is not None and (
        first_tp_at is None or first_sl_at is None or ambiguous_at <= min(first_tp_at, first_sl_at)
    ):
        outcome = "AMBIGUOUS"
        notes = "TP and SL were both reachable inside the same OHLC candle."
    elif first_tp_at is not None and (first_sl_at is None or first_tp_at < first_sl_at):
        outcome = "WIN"
        notes = "Take-profit threshold hit before stop-loss threshold."
    elif first_sl_at is not None and (first_tp_at is None or first_sl_at < first_tp_at):
        outcome = "LOSS"
        notes = "Stop-loss threshold hit before take-profit threshold."
    elif pips_at_horizon > 0:
        outcome = "OPEN_PROFIT"
        notes = "Neither TP nor SL hit; horizon close was favorable."
    elif pips_at_horizon < 0:
        outcome = "OPEN_LOSS"
        notes = "Neither TP nor SL hit; horizon close was adverse."
    else:
        outcome = "BREAKEVEN"
        notes = "Neither TP nor SL hit; horizon close was flat."

    return PathOutcome(
        horizon_minutes=horizon_minutes,
        entry_price=entry_price,
        direction=direction,
        stop_loss_pips=stop_loss_pips,
        take_profit_pips=take_profit_pips,
        pips_at_horizon=pips_at_horizon,
        max_favorable_pips=max_favorable,
        max_adverse_pips=max_adverse,
        hit_take_profit=hit_tp,
        hit_stop_loss=hit_sl,
        outcome=outcome,
        label=f"{outcome}_{horizon_minutes}M",
        notes=notes,
    )


def label_many_horizons(
    df: pd.DataFrame,
    *,
    snapshot_at: datetime,
    direction: Direction,
    entry_price: float,
    pip_size: float,
    horizons: Iterable[int] = (30, 90, 240),
    stop_loss_pips: Optional[float] = None,
    take_profit_pips: Optional[float] = None,
) -> list[PathOutcome]:
    return [
        label_future_path(
            df,
            snapshot_at=snapshot_at,
            direction=direction,
            entry_price=entry_price,
            pip_size=pip_size,
            horizon_minutes=h,
            stop_loss_pips=stop_loss_pips,
            take_profit_pips=take_profit_pips,
        )
        for h in horizons
    ]


def _directional_pips(
    direction: Direction, entry_price: float, close_price: float, pip_size: float
) -> float:
    if direction == Direction.BUY:
        return (close_price - entry_price) / pip_size
    if direction == Direction.SELL:
        return (entry_price - close_price) / pip_size
    return 0.0


def _no_data_outcome(
    horizon_minutes: int,
    entry_price: float,
    direction: Direction,
    stop_loss_pips: Optional[float],
    take_profit_pips: Optional[float],
) -> PathOutcome:
    return PathOutcome(
        horizon_minutes=horizon_minutes,
        entry_price=entry_price,
        direction=direction,
        stop_loss_pips=stop_loss_pips,
        take_profit_pips=take_profit_pips,
        pips_at_horizon=None,
        max_favorable_pips=None,
        max_adverse_pips=None,
        hit_take_profit=False,
        hit_stop_loss=False,
        outcome="NO_DATA",
        label=f"NO_DATA_{horizon_minutes}M",
        notes="No future OHLC bars were available for this horizon.",
    )
