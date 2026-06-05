from __future__ import annotations

import sqlite3
from datetime import datetime, timezone

import pandas as pd

from helix_v3.backtest.historical_flashcard_miner import HistoricalSliceEngine
from helix_v3.journal.flashcards import FlashcardSystem


def test_historical_slice_engine_returns_only_bars_before_snapshot() -> None:
    idx = pd.date_range("2026-06-01 00:00:00+00:00", periods=8, freq="15min")
    df = pd.DataFrame(
        {
            "Open": range(8),
            "High": range(1, 9),
            "Low": range(8),
            "Close": range(8),
        },
        index=idx,
    )
    engine = HistoricalSliceEngine(
        symbol="EURUSD",
        frames={"M15": df},
        snapshot_at=datetime(2026, 6, 1, 1, 0, tzinfo=timezone.utc),
        pip_size=0.0001,
    )

    result = engine.fetch_rates("EURUSD", "M15", count=3)

    assert len(result) == 3
    assert result.index[-1] == pd.Timestamp("2026-06-01 01:00:00+00:00")
    assert result["Close"].iloc[-1] == 4


def test_historical_flashcard_preserves_snapshot_timestamp(tmp_path) -> None:
    db_path = tmp_path / "flashcards.db"
    snapshot_at = datetime(2026, 5, 20, 9, 30, tzinfo=timezone.utc)
    flashcards = FlashcardSystem(db_path=db_path)
    try:
        flashcard_id = flashcards.save_historical_flashcard(
            symbol="GBPCHF",
            timeframe="M15",
            chart_path="charts/historical/test.png",
            snapshot_at=snapshot_at,
            mtf_context={
                "weekly": {"week_phase": "LATE_WEEK", "trend_direction": "SELL"},
                "four_hour": {"level_count": 3, "trend_direction": "SELL"},
                "one_hour": {"session_phase": "TRUE_TREND", "trend_direction": "SELL"},
                "fifteen_min": {
                    "entry_direction": "SELL",
                    "m_w_forming": True,
                    "m_w_pattern": "M_TOP",
                    "push_count": 3,
                    "stop_hunt_detected": True,
                    "stop_hunt_direction": "SELL",
                },
                "tdi": {"signals": ["SHARK_FIN_SHORT"]},
                "patterns": {"trade_type": "THE_33"},
                "convergence": {"themes": ["GBP_WEAKNESS", "CHF_STRENGTH"]},
                "advisory": {"confidence_score": 78.0, "grade": "B"},
                "confluence_score": 72,
            },
        )
        flashcards.record_outcome_by_id(
            flashcard_id,
            outcome="TRAIL_STOP",
            pips_gained=24.0,
            duration_minutes=75.0,
            exit_reason="unit test",
            t1_hit=True,
        )
    finally:
        flashcards.close()

    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT * FROM flashcards WHERE id = ?", (flashcard_id,)).fetchone()
    finally:
        conn.close()

    assert row["snapshot_type"] == "HISTORICAL"
    assert row["snapshot_at"] == snapshot_at.isoformat()
    assert row["outcome"] == "TRAIL_STOP"
    assert row["pips_gained"] == 24.0
