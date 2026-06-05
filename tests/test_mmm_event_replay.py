from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd

from helix_v3.backtest.mmm_event_replay import (
    ReplaySetup,
    build_setup_signature,
    build_calibration_recommendations,
    build_advisory_grade_rows,
    enrich_flashcard_fields,
    build_calibration_profile_proposals,
    build_gate_ablation,
    label_mmm_event_path,
    summarize_convergence,
)
from helix_v3.core.types import Direction


def _setup(**overrides) -> ReplaySetup:
    data = {
        "symbol": "GBPUSD",
        "timeframe": "M15",
        "snapshot_at": datetime(2026, 6, 4, 10, 0, tzinfo=timezone.utc),
        "direction": Direction.BUY,
        "confluence_score": 70,
        "weekly_phase": "LATE_WEEK",
        "weekly_trend": Direction.BUY,
        "h4_level": 3,
        "h4_trend": Direction.SELL,
        "h1_session": "TRUE_TREND",
        "h1_trend": Direction.NEUTRAL,
        "asian_range_pips": 16.0,
        "accumulation_valid": True,
        "stop_hunt_detected": True,
        "stop_hunt_direction": Direction.BUY,
        "stop_hunt_pips": 30.0,
        "push_count": 5,
        "m_w_forming": True,
        "rrt_detected": True,
        "source": "test",
        "source_id": 1,
    }
    data.update(overrides)
    return ReplaySetup(**data)


def test_mmm_event_path_buy_hits_target_2() -> None:
    idx = pd.date_range("2026-06-04 10:00:00+00:00", periods=7, freq="15min")
    df = pd.DataFrame(
        {
            "Open": [1.1000, 1.1005, 1.1015, 1.1030, 1.1050, 1.1060, 1.1070],
            "High": [1.1005, 1.1015, 1.1032, 1.1055, 1.1078, 1.1080, 1.1085],
            "Low": [1.0995, 1.1002, 1.1010, 1.1028, 1.1048, 1.1058, 1.1068],
            "Close": [1.1002, 1.1012, 1.1030, 1.1050, 1.1075, 1.1078, 1.1080],
        },
        index=idx,
    )

    outcome = label_mmm_event_path(
        df,
        setup=_setup(),
        entry_price=1.1000,
        pip_size=0.0001,
        asian_high=1.1010,
        asian_low=1.0980,
    )

    assert outcome.outcome == "TARGET_2"
    assert outcome.t1_hit is True
    assert round(outcome.sl_pips or 0, 1) == 23.0
    assert round(outcome.t2_pips or 0, 1) == 57.5
    assert "T1_HIT" in outcome.event_path


def test_mmm_event_path_stale_exit_only_when_not_in_profit() -> None:
    idx = pd.date_range("2026-06-04 10:00:00+00:00", periods=8, freq="15min")
    df = pd.DataFrame(
        {
            "Open": [1.1000, 1.0998, 1.0997, 1.0996, 1.0998, 1.0999, 1.0997, 1.0996],
            "High": [1.1002, 1.1000, 1.0999, 1.0998, 1.1000, 1.1000, 1.0999, 1.0998],
            "Low": [1.0998, 1.0995, 1.0994, 1.0993, 1.0995, 1.0996, 1.0995, 1.0994],
            "Close": [1.1000, 1.0998, 1.0997, 1.0996, 1.0998, 1.0999, 1.0997, 1.0996],
        },
        index=idx,
    )

    outcome = label_mmm_event_path(
        df,
        setup=_setup(),
        entry_price=1.1000,
        pip_size=0.0001,
        asian_high=1.1010,
        asian_low=1.0980,
    )

    assert outcome.outcome == "STALE_EXIT"
    assert outcome.t1_hit is False
    assert outcome.exit_pips is not None
    assert outcome.exit_pips <= 0


def test_setup_signature_normalizes_pair_specific_ranges() -> None:
    gbp = build_setup_signature(_setup(symbol="GBPJPY", stop_hunt_pips=42.0, asian_range_pips=22.0))
    eur = build_setup_signature(
        _setup(
            symbol="EURJPY",
            stop_hunt_pips=34.0,
            asian_range_pips=24.0,
            source_id=2,
        )
    )

    assert gbp.setup_family == "THE_33_MW"
    assert "JPY_WEAKNESS" in gbp.theme_tags
    assert "AR_TIGHT" in gbp.normalized_key
    assert "HUNT_PAIR_RANGE" in gbp.normalized_key
    assert gbp.raw_key != eur.raw_key
    assert gbp.normalized_key == eur.normalized_key


def test_summarize_convergence_groups_similar_jpy_cross_setups() -> None:
    signatures = [
        build_setup_signature(_setup(symbol="GBPJPY", source_id=1, stop_hunt_pips=42.0)),
        build_setup_signature(_setup(symbol="EURJPY", source_id=2, stop_hunt_pips=34.0)),
        build_setup_signature(_setup(symbol="USDJPY", source_id=3, stop_hunt_pips=50.0)),
    ]

    groups = summarize_convergence(signatures, min_symbols=2)

    assert groups
    assert groups[0].theme == "JPY_WEAKNESS"
    assert groups[0].symbols == ["EURJPY", "GBPJPY", "USDJPY"]
    assert groups[0].score > 0


def test_enrich_flashcard_fields_adds_tdi_pattern_and_theme() -> None:
    idx = pd.date_range("2026-06-04 00:00:00+00:00", periods=120, freq="15min")
    closes = [1.1000 + i * 0.0001 for i in range(120)]
    df_m15 = pd.DataFrame(
        {
            "Open": closes,
            "High": [close + 0.0004 for close in closes],
            "Low": [close - 0.0004 for close in closes],
            "Close": closes,
        },
        index=idx,
    )
    d1_idx = pd.date_range("2026-05-25 00:00:00+00:00", periods=12, freq="1D")
    df_d1 = pd.DataFrame(
        {
            "Open": [1.09] * 12,
            "High": [1.11] * 12,
            "Low": [1.08] * 12,
            "Close": [1.10] * 12,
        },
        index=d1_idx,
    )

    fields = enrich_flashcard_fields(
        {
            "id": 1,
            "symbol": "GBPUSD",
            "timeframe": "M15",
            "snapshot_at": "2026-06-04T10:00:00+00:00",
            "entry_direction": "BUY",
            "confluence_score": 70,
            "m_w_forming": 1,
            "push_count": 3,
        },
        past_m15=df_m15,
        past_d1=df_d1,
        pip_size=0.0001,
    )

    assert fields["m_w_pattern"] == "W_BOTTOM"
    assert fields["tdi_signals"].startswith("[")
    assert fields["pattern_trade_type"]
    assert fields["convergence_theme_score"] > 0


def test_build_calibration_recommendations_flags_stale_pair() -> None:
    records = [
        {
            "symbol": "GBPUSD",
            "outcome": "STALE_EXIT",
            "exit_pips": -2.0,
            "max_favorable_pips": 3.0,
            "max_adverse_pips": 7.0,
            "t1_hit": 0,
            "normalized_key": "THE_33_MW|SELL|TDI_CONFIRM",
            "ratios": {"asian_range_to_pair_max": 0.7, "hunt_to_pair_max": 0.8},
            "raw_json": {"profile": {"trail_activation_pips": 20}},
        }
        for _ in range(5)
    ]

    recommendations = build_calibration_recommendations(records, min_total=5)

    assert recommendations[0]["symbol"] == "GBPUSD"
    assert recommendations[0]["summary"] == "tighten entry gate"
    assert any("High stale rate" in note for note in recommendations[0]["notes"])


def _event_record(**overrides):
    data = {
        "symbol": "GBPUSD",
        "direction": "BUY",
        "outcome": "STALE_EXIT",
        "exit_pips": -2.0,
        "max_favorable_pips": 3.0,
        "max_adverse_pips": 7.0,
        "t1_hit": 0,
        "normalized_key": (
            "THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|"
            "PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74"
        ),
        "primary_theme": "GBP_STRENGTH",
        "convergence_theme_score": 60.0,
        "theme_tags": ["GBP_STRENGTH", "USD_WEAKNESS"],
        "ratios": {
            "asian_range_to_pair_max": 0.7,
            "hunt_to_pair_max": 0.8,
            "confluence": 0.7,
        },
        "raw_json": {
            "setup": {
                "symbol": "GBPUSD",
                "direction": "BUY",
                "confluence_score": 70,
                "h4_level": 3,
                "h1_session": "TRUE_TREND",
                "asian_range_pips": 28.0,
                "stop_hunt_detected": True,
                "stop_hunt_pips": 32.0,
                "push_count": 3,
                "m_w_forming": True,
                "m_w_pattern": "W_BOTTOM",
                "rrt_detected": True,
                "pattern_trade_type": "THE_33",
            }
        },
    }
    data.update(overrides)
    return data


def test_gate_ablation_compares_mmm_filters() -> None:
    records = [_event_record(outcome="TARGET_2", exit_pips=20.0, t1_hit=1) for _ in range(4)]
    records += [
        _event_record(
            outcome="LOSS",
            exit_pips=-12.0,
            t1_hit=0,
            normalized_key="STOP_HUNT|BUY|LATE_WEEK|L1|TRUE_TREND|AR_WIDE|HUNT_EXTENDED|PUSH1|NO_MW|NO_RRT|TDI_CONFLICT|STOP_HUNT|CONF_50_74",
            convergence_theme_score=0.0,
            ratios={
                "asian_range_to_pair_max": 1.2,
                "hunt_to_pair_max": 1.3,
                "confluence": 0.58,
            },
            raw_json={"setup": {"symbol": "GBPUSD", "direction": "BUY", "confluence_score": 58}},
        )
        for _ in range(4)
    ]

    rows = build_gate_ablation(records, min_total=2)
    by_name = {row["name"]: row for row in rows}

    assert by_name["baseline"]["total"] == 8
    assert by_name["vision_ready"]["total"] == 4
    assert by_name["vision_ready"]["favorable_rate"] == 100.0
    assert by_name["vision_ready"]["delta_favorable_rate"] > 0


def test_calibration_profile_proposals_emit_pair_profile_fields() -> None:
    records = [_event_record(outcome="TARGET_2", exit_pips=20.0, t1_hit=1) for _ in range(3)]
    records += [_event_record(outcome="LOSS", exit_pips=-10.0, t1_hit=0) for _ in range(3)]

    proposals = build_calibration_profile_proposals(records, min_total=3)

    assert proposals[0]["symbol"] == "GBPUSD"
    assert proposals[0]["settings"]["require_m_w"] is True
    assert any("min_confluence_score" in line for line in proposals[0]["patch_preview"])


def test_advisory_grade_rows_bucket_outcomes() -> None:
    records = [
        _event_record(symbol="GBPJPY", theme_tags=["GBP_STRENGTH", "JPY_WEAKNESS"]),
        _event_record(symbol="EURJPY", theme_tags=["EUR_STRENGTH", "JPY_WEAKNESS"]),
        _event_record(symbol="USDJPY", theme_tags=["USD_STRENGTH", "JPY_WEAKNESS"]),
    ]

    rows = build_advisory_grade_rows(records, min_total=1)

    assert rows
    assert rows[0]["grade"] in {"A", "B", "C", "D", "AVOID"}
