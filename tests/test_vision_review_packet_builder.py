from __future__ import annotations

import json
from datetime import datetime, timezone

from helix_v3.backtest.mmm_event_replay import (
    MMMEventOutcome,
    MMMReplayStore,
    ReplaySetup,
    build_setup_signature,
)
from helix_v3.core.types import Direction
from helix_v3.journal.flashcards import FlashcardSystem
from helix_v3.training.vision_review_packet_builder import (
    PacketConfig,
    _load_setup_candidates,
    build_review_packets,
)


def _setup(source_id: int, snapshot_at: datetime) -> ReplaySetup:
    return ReplaySetup(
        symbol="GBPJPY",
        timeframe="M15",
        snapshot_at=snapshot_at,
        direction=Direction.BUY,
        confluence_score=76,
        weekly_phase="EARLY_WEEK",
        h4_level=3,
        h1_session="STOP_HUNT",
        asian_range_pips=25.0,
        accumulation_valid=True,
        stop_hunt_detected=True,
        stop_hunt_direction=Direction.BUY,
        stop_hunt_pips=45.0,
        push_count=3,
        m_w_forming=True,
        m_w_pattern="W_BOTTOM",
        pattern_trade_type="THE_33",
        source="historical_flashcard",
        source_id=source_id,
    )


def _outcome(setup: ReplaySetup, *, outcome: str, exit_pips: float) -> MMMEventOutcome:
    return MMMEventOutcome(
        source=setup.source,
        source_id=setup.source_id,
        symbol=setup.symbol,
        timeframe=setup.timeframe,
        snapshot_at=setup.snapshot_at,
        direction=setup.direction,
        entry_price=200.0,
        stop_loss_price=199.5,
        t1_price=200.5,
        t2_price=201.25,
        sl_pips=50.0,
        t1_pips=50.0,
        t2_pips=125.0,
        exit_at=setup.snapshot_at,
        exit_price=200.0 + exit_pips / 100.0,
        exit_pips=exit_pips,
        max_favorable_pips=max(0.0, exit_pips + 5.0),
        max_adverse_pips=5.0 if exit_pips > 0 else 12.0,
        t1_hit=exit_pips > 15.0,
        minutes_to_t1=45.0 if exit_pips > 15.0 else None,
        outcome=outcome,
        label=f"GBPJPY_BUY_{outcome}",
        event_path=["ENTRY", outcome],
        notes="unit test",
    )


def test_vision_review_packet_builder_exports_balanced_packet(tmp_path) -> None:
    flashcards_db = tmp_path / "flashcards.db"
    replay_db = tmp_path / "vision_backtests.db"
    pair_root = tmp_path / "pair_research"
    output_root = tmp_path / "packets"
    chart_dir = tmp_path / "charts"
    chart_dir.mkdir()

    flashcards = FlashcardSystem(db_path=flashcards_db)
    store = MMMReplayStore(replay_db)
    normalized_key = ""
    try:
        specs = [
            ("TARGET_2", 24.0),
            ("TRAIL_STOP", 14.0),
            ("TIME_EXIT_LOSS", -8.0),
        ]
        for index, (outcome_name, exit_pips) in enumerate(specs, start=1):
            snapshot_at = datetime(2026, 6, index, 7, 0, tzinfo=timezone.utc)
            chart_path = chart_dir / f"chart_{index}.png"
            chart_path.write_bytes(b"fake png")
            flashcard_id = flashcards.save_historical_flashcard(
                symbol="GBPJPY",
                timeframe="M15",
                chart_path=str(chart_path),
                snapshot_at=snapshot_at,
                mtf_context={
                    "weekly": {"week_phase": "EARLY_WEEK", "trend_direction": "BUY"},
                    "four_hour": {"level_count": 3, "trend_direction": "BUY"},
                    "one_hour": {"session_phase": "STOP_HUNT", "trend_direction": "BUY"},
                    "fifteen_min": {
                        "entry_direction": "BUY",
                        "m_w_forming": True,
                        "m_w_pattern": "W_BOTTOM",
                        "push_count": 3,
                        "stop_hunt_detected": True,
                        "stop_hunt_direction": "BUY",
                        "stop_hunt_pips": 45.0,
                    },
                    "tdi": {"signals": []},
                    "patterns": {"trade_type": "THE_33"},
                    "confluence_score": 76,
                },
            )
            flashcards.record_outcome_by_id(
                flashcard_id,
                outcome=outcome_name,
                pips_gained=exit_pips,
                duration_minutes=90.0,
                exit_reason="unit test",
                t1_hit=exit_pips > 15.0,
            )
            setup = _setup(flashcard_id, snapshot_at)
            signature = build_setup_signature(setup)
            normalized_key = signature.normalized_key
            sig_id = store.record_signature(signature)
            store.record_outcome(_outcome(setup, outcome=outcome_name, exit_pips=exit_pips), sig_id)
    finally:
        flashcards.close()
        store.close()

    pair_dir = pair_root / "GBPJPY"
    pair_dir.mkdir(parents=True)
    (pair_dir / "setup_performance.json").write_text(
        json.dumps(
            [
                {
                    "symbol": "GBPJPY",
                    "direction": "BUY",
                    "normalized_key": normalized_key,
                    "total": 3,
                    "favorable_rate": 66.7,
                    "avg_exit_pips": 10.0,
                }
            ]
        ),
        encoding="utf-8",
    )

    packets = build_review_packets(
        PacketConfig(
            flashcards_db=flashcards_db,
            replay_db=replay_db,
            pair_research_root=pair_root,
            output_root=output_root,
            symbols=("GBPJPY",),
            min_total=3,
            winners_per_setup=2,
            losers_per_setup=1,
        )
    )

    assert len(packets) == 1
    packet = packets[0]
    manifest = json.loads((packet / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["counts"]["winners"] == 2
    assert manifest["counts"]["losers"] == 1
    assert (packet / "blind_prompt.md").exists()
    assert (packet / "labeled_comparison_prompt.md").exists()
    assert "answer_key.csv" in (packet / "README.md").read_text(encoding="utf-8")
    image_names = [path.name for path in (packet / "images").glob("*.png")]
    assert len(image_names) == 3
    assert all("winner" not in name and "loser" not in name for name in image_names)


def test_vision_review_packet_builder_can_include_non_w_bottom_candidates(tmp_path) -> None:
    pair_root = tmp_path / "pair_research"
    output_root = tmp_path / "packets"
    pair_dir = pair_root / "XAUUSD"
    pair_dir.mkdir(parents=True)
    rrt_key = "RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|AR_TIGHT|NO_MW|RRT"
    (pair_dir / "setup_performance.json").write_text(
        json.dumps(
            [
                {
                    "symbol": "XAUUSD",
                    "direction": "SELL",
                    "normalized_key": rrt_key,
                    "total": 17,
                    "favorable_rate": 70.6,
                    "avg_exit_pips": 358.7,
                }
            ]
        ),
        encoding="utf-8",
    )

    default_candidates = _load_setup_candidates(
        PacketConfig(
            pair_research_root=pair_root,
            output_root=output_root,
            symbols=("XAUUSD",),
            min_total=10,
            copy_images=False,
        ),
        "XAUUSD",
    )
    all_shape_candidates = _load_setup_candidates(
        PacketConfig(
            pair_research_root=pair_root,
            output_root=output_root,
            symbols=("XAUUSD",),
            min_total=10,
            copy_images=False,
            require_w_bottom=False,
        ),
        "XAUUSD",
    )

    assert default_candidates == []
    assert len(all_shape_candidates) == 1
    assert all_shape_candidates[0]["normalized_key"] == rrt_key
