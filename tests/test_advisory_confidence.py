from __future__ import annotations

from helix_v3.core.advisory_confidence import (
    AdvisorySetup,
    classify_tdi_state,
    score_advisory_setup,
    summarize_peer_convergence,
)


def _setup(**overrides) -> AdvisorySetup:
    data = {
        "symbol": "GBPJPY",
        "direction": "BUY",
        "confluence_score": 70,
        "trade_valid": True,
        "h4_level": 3,
        "h1_session": "TRUE_TREND",
        "asian_range_ratio": 0.5,
        "stop_hunt_detected": True,
        "hunt_range_ratio": 0.8,
        "push_count": 3,
        "m_w_forming": True,
        "m_w_pattern": "W_BOTTOM",
        "rrt_detected": True,
        "tdi_state": "TDI_CONFIRM",
        "pattern_trade_type": "THE_33",
        "themes": ["GBP_STRENGTH", "JPY_WEAKNESS"],
    }
    data.update(overrides)
    return AdvisorySetup(**data)


def test_tdi_state_classifies_confirm_and_conflict() -> None:
    assert (
        classify_tdi_state(
            signals=["SHARK_FIN_LONG"],
            direction="BUY",
            shark_fin_active=True,
            shark_fin_direction="LONG",
            rsi=42.0,
        )
        == "TDI_CONFIRM"
    )
    assert (
        classify_tdi_state(
            signals=["SIGNAL_CROSS_BEARISH"],
            direction="BUY",
            rsi=42.0,
        )
        == "TDI_CONFLICT"
    )


def test_advisory_score_rewards_cross_pair_convergence() -> None:
    setup = _setup()
    peers = [
        _setup(symbol="EURJPY", themes=["EUR_STRENGTH", "JPY_WEAKNESS"], confluence_score=68),
        _setup(symbol="USDJPY", themes=["USD_STRENGTH", "JPY_WEAKNESS"], confluence_score=64),
    ]

    convergence = summarize_peer_convergence(setup, peers)
    score = score_advisory_setup(setup, peers)

    assert convergence.score >= 50
    assert score.grade == "A"
    assert score.convergence_score == convergence.score
    assert score.peer_symbols == ["EURJPY", "USDJPY"]


def test_advisory_blocks_weak_mmm_structure() -> None:
    score = score_advisory_setup(
        _setup(
            confluence_score=58,
            m_w_forming=False,
            push_count=1,
            stop_hunt_detected=False,
            tdi_state="TDI_CONFLICT",
        )
    )

    assert score.grade == "AVOID"
    assert "M/W formation missing" in score.blockers
    assert "TDI conflicts with direction" in score.blockers
