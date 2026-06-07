from __future__ import annotations

import sqlite3
from datetime import datetime, timezone

from helix_v3.backtest.mmm_event_replay import (
    MMMEventOutcome,
    MMMReplayStore,
    ReplaySetup,
    build_setup_signature,
)
from helix_v3.backtest.validation_library import ValidationLibrary
from helix_v3.core.types import Direction


def _setup(source_id: int = 1) -> ReplaySetup:
    return ReplaySetup(
        symbol="GBPCHF",
        timeframe="M15",
        snapshot_at=datetime(2026, 6, 1, 9, 0, tzinfo=timezone.utc),
        direction=Direction.SELL,
        confluence_score=72,
        weekly_phase="LATE_WEEK",
        h4_level=3,
        h1_session="TRUE_TREND",
        asian_range_pips=20.0,
        accumulation_valid=True,
        stop_hunt_detected=True,
        stop_hunt_direction=Direction.SELL,
        stop_hunt_pips=30.0,
        push_count=3,
        m_w_forming=True,
        m_w_pattern="M_TOP",
        rrt_detected=False,
        tdi_rsi=48.0,
        pattern_trade_type="THE_33",
        source="historical_flashcard",
        source_id=source_id,
    )


def _outcome(setup: ReplaySetup) -> MMMEventOutcome:
    return MMMEventOutcome(
        source=setup.source,
        source_id=setup.source_id,
        symbol=setup.symbol,
        timeframe=setup.timeframe,
        snapshot_at=setup.snapshot_at,
        direction=setup.direction,
        entry_price=1.1000,
        stop_loss_price=1.1050,
        t1_price=1.0950,
        t2_price=1.0875,
        sl_pips=50.0,
        t1_pips=50.0,
        t2_pips=125.0,
        exit_at=datetime(2026, 6, 1, 10, 0, tzinfo=timezone.utc),
        exit_price=1.0940,
        exit_pips=60.0,
        max_favorable_pips=80.0,
        max_adverse_pips=10.0,
        t1_hit=True,
        minutes_to_t1=45.0,
        outcome="TRAIL_STOP",
        label="GBPCHF_SELL_TRAIL_STOP",
        event_path=["ENTRY", "T1_HIT", "TRAIL_STOP"],
        notes="unit test",
    )


def test_validation_library_promotes_and_validates_setup(tmp_path) -> None:
    replay_db = tmp_path / "vision_backtests.db"
    store = MMMReplayStore(replay_db)
    try:
        for source_id in range(1, 4):
            setup = _setup(source_id)
            sig_id = store.record_signature(build_setup_signature(setup))
            store.record_outcome(_outcome(setup), sig_id)
    finally:
        store.close()

    library = ValidationLibrary(db_path=tmp_path / "library.db", replay_db_path=replay_db)
    try:
        promoted = library.promote_from_replay(
            min_total=3,
            min_favorable_rate=55,
            min_avg_exit_pips=0,
        )
        matches = library.validate_setup(_setup(99))
    finally:
        library.close()

    assert promoted == 1
    assert matches
    assert matches[0].symbol == "GBPCHF"
    assert matches[0].favorable_rate == 100.0
    assert matches[0].realistic_target_pips and matches[0].realistic_target_pips > 0


def test_validation_library_report_handles_empty_db(tmp_path) -> None:
    library = ValidationLibrary(db_path=tmp_path / "library.db", replay_db_path=tmp_path / "missing.db")
    try:
        report = library.report()
    finally:
        library.close()

    assert "No validation-library records" in report


def test_validation_library_schema_has_unique_key(tmp_path) -> None:
    library = ValidationLibrary(db_path=tmp_path / "library.db", replay_db_path=tmp_path / "missing.db")
    library.close()

    conn = sqlite3.connect(str(tmp_path / "library.db"))
    try:
        indexes = conn.execute("PRAGMA index_list(validation_setups)").fetchall()
    finally:
        conn.close()

    assert any(index[2] for index in indexes)


def test_validation_library_rebuild_clears_records_that_fail_new_gate(tmp_path) -> None:
    replay_db = tmp_path / "vision_backtests.db"
    store = MMMReplayStore(replay_db)
    try:
        for source_id in range(1, 4):
            setup = _setup(source_id)
            sig_id = store.record_signature(build_setup_signature(setup))
            store.record_outcome(_outcome(setup), sig_id)
    finally:
        store.close()

    library = ValidationLibrary(db_path=tmp_path / "library.db", replay_db_path=replay_db)
    try:
        assert library.promote_from_replay(min_total=3, min_favorable_rate=55) == 1
        rebuilt = library.rebuild_from_replay(min_total=3, min_favorable_rate=101)
        report = library.report()
    finally:
        library.close()

    assert rebuilt == 0
    assert "No validation-library records" in report
