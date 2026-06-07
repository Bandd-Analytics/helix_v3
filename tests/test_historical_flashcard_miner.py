from __future__ import annotations

import sqlite3
from datetime import datetime, timezone

import pandas as pd

from helix_v3.backtest.historical_flashcard_miner import (
    HistoricalFlashcardMiner,
    HistoricalSliceEngine,
    _fetch_rates_chunked,
)
from helix_v3.backtest.mmm_event_replay import (
    MMMEventOutcome,
    ReplaySetup,
    build_setup_signature,
)
from helix_v3.core.types import Direction
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


def test_fetch_rates_chunked_splits_large_ranges() -> None:
    calls = []

    def fake_fetch(symbol, timeframe, start, end):  # noqa: ANN001
        calls.append((symbol, timeframe, start, end))
        if end - start > pd.Timedelta(days=7):
            raise ConnectionError("too large")
        idx = pd.date_range(start, end, periods=2)
        return pd.DataFrame(
            {
                "Open": [1.0, 1.0],
                "High": [1.1, 1.1],
                "Low": [0.9, 0.9],
                "Close": [1.0, 1.0],
            },
            index=idx,
        )

    result = _fetch_rates_chunked(
        fake_fetch,
        "GBPJPY",
        "M15",
        datetime(2026, 1, 1, tzinfo=timezone.utc),
        datetime(2026, 1, 20, tzinfo=timezone.utc),
    )

    assert len(calls) > 1
    assert not result.empty
    assert result.index.is_monotonic_increasing


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


def test_pair_research_archive_exports_profitable_flashcards(tmp_path) -> None:
    flashcards_db = tmp_path / "flashcards.db"
    replay_db = tmp_path / "replay.db"
    library_db = tmp_path / "library.db"
    snapshot_at = datetime(2026, 5, 20, 9, 30, tzinfo=timezone.utc)

    flashcards = FlashcardSystem(db_path=flashcards_db)
    try:
        flashcard_id = flashcards.save_historical_flashcard(
            symbol="GBPJPY",
            timeframe="M15",
            chart_path="charts/historical/gbpjpy.png",
            snapshot_at=snapshot_at,
            mtf_context={
                "weekly": {"week_phase": "LATE_WEEK", "trend_direction": "BUY"},
                "four_hour": {"level_count": 3, "trend_direction": "BUY"},
                "one_hour": {"session_phase": "TRUE_TREND", "trend_direction": "BUY"},
                "fifteen_min": {
                    "entry_direction": "BUY",
                    "m_w_forming": True,
                    "m_w_pattern": "W_BOTTOM",
                    "push_count": 3,
                    "stop_hunt_detected": True,
                    "stop_hunt_direction": "BUY",
                    "stop_hunt_pips": 42.0,
                },
                "tdi": {"signals": ["SHARK_FIN_LONG"]},
                "patterns": {"trade_type": "THE_33"},
                "convergence": {"themes": ["GBP_STRENGTH", "JPY_WEAKNESS"]},
                "advisory": {"confidence_score": 82.0, "grade": "B"},
                "confluence_score": 76,
            },
        )
        flashcards.record_outcome_by_id(
            flashcard_id,
            outcome="TRAIL_STOP",
            pips_gained=34.0,
            duration_minutes=90.0,
            exit_reason="unit test",
            t1_hit=True,
        )
    finally:
        flashcards.close()

    miner = HistoricalFlashcardMiner(
        flashcards_db_path=flashcards_db,
        replay_db_path=replay_db,
        library_db_path=library_db,
    )
    try:
        setup = ReplaySetup(
            symbol="GBPJPY",
            timeframe="M15",
            snapshot_at=snapshot_at,
            direction=Direction.BUY,
            confluence_score=76,
            weekly_phase="LATE_WEEK",
            h4_level=3,
            h1_session="TRUE_TREND",
            asian_range_pips=22.0,
            accumulation_valid=True,
            stop_hunt_detected=True,
            stop_hunt_direction=Direction.BUY,
            stop_hunt_pips=42.0,
            push_count=3,
            m_w_forming=True,
            m_w_pattern="W_BOTTOM",
            tdi_shark_fin=True,
            tdi_shark_direction="LONG",
            pattern_trade_type="THE_33",
            source="historical_flashcard",
            source_id=flashcard_id,
        )
        signature_id = miner._replay_store.record_signature(build_setup_signature(setup))
        miner._replay_store.record_outcome(
            MMMEventOutcome(
                source="historical_flashcard",
                source_id=flashcard_id,
                symbol="GBPJPY",
                timeframe="M15",
                snapshot_at=snapshot_at,
                direction=Direction.BUY,
                entry_price=200.0,
                stop_loss_price=199.5,
                t1_price=200.5,
                t2_price=201.25,
                sl_pips=50.0,
                t1_pips=50.0,
                t2_pips=125.0,
                exit_at=snapshot_at,
                exit_price=200.34,
                exit_pips=34.0,
                max_favorable_pips=52.0,
                max_adverse_pips=12.0,
                t1_hit=True,
                minutes_to_t1=45.0,
                outcome="TRAIL_STOP",
                label="GBPJPY_BUY_TRAIL_STOP",
                event_path=["ENTRY", "T1_HIT", "TRAIL_STOP"],
                notes="unit test",
            ),
            signature_id,
        )
        written = miner.export_pair_research_archive(
            symbols=["GBPJPY"],
            output_root=tmp_path / "pair_research",
            min_total=1,
            min_favorable_rate=55.0,
            min_avg_exit_pips=0.0,
            max_examples=10,
            scanner_baseline="baseline",
        )
    finally:
        miner.close()

    summary = (tmp_path / "pair_research" / "GBPJPY" / "SUMMARY.md").read_text(encoding="utf-8")
    examples = (
        tmp_path / "pair_research" / "GBPJPY" / "profitable_flashcards.jsonl"
    ).read_text(encoding="utf-8")

    assert written
    assert "Baseline-Qualified Setups" in summary
    assert "TRAIL_STOP" in examples
    assert str(flashcard_id) in examples
