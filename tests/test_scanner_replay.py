from __future__ import annotations

from datetime import datetime, timezone

from helix_v3.backtest.scanner_replay import ScannerCandidate, baseline_direction
from helix_v3.core.types import Direction


def _candidate(**overrides) -> ScannerCandidate:
    data = {
        "id": 1,
        "scan_time": datetime(2026, 6, 4, 11, 0, tzinfo=timezone.utc),
        "symbol": "GBPJPY",
        "timeframe": "M15",
        "bid": 215.094,
        "ask": 215.100,
        "spread_pips": 0.6,
        "session": "LONDON",
        "bias": Direction.BUY,
        "trend": Direction.BUY,
        "trade_readiness": 70,
        "readiness_notes": "Stop hunt + absorption",
        "stop_hunt_active": True,
        "stop_hunt_direction": Direction.SELL,
        "stop_hunt_breach_pips": 29.9,
        "atr_14": 8.3,
    }
    data.update(overrides)
    return ScannerCandidate(**data)


def test_stop_hunt_then_bias_prefers_reversal_direction() -> None:
    candidate = _candidate()

    assert baseline_direction(candidate, policy="stop_hunt_then_bias") == Direction.SELL


def test_stop_hunt_then_bias_falls_back_to_bias() -> None:
    candidate = _candidate(
        stop_hunt_active=False,
        stop_hunt_direction=Direction.NEUTRAL,
        bias=Direction.BUY,
    )

    assert baseline_direction(candidate, policy="stop_hunt_then_bias") == Direction.BUY
