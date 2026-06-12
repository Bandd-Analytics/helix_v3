"""Tests for ATR-normalized gates (audit Tier 2.3).

resolve_profile: the eight pip gates become GATE_RATIOS x ATR(20, D1),
with spread-based floors as the per-instrument facts. d1_atr_pips: Wilder
ATR through a quant engine, None on failure (static fallback).
"""
from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd
import pytest

from config.pair_profiles import GATE_RATIOS, get_pair_profile, resolve_profile
from helix_v3.core.volatility import d1_atr_pips


def test_no_atr_falls_back_to_static_profile() -> None:
    static = get_pair_profile("GBPJPY")
    for atr in (None, 0.0, -5.0):
        pp = resolve_profile("GBPJPY", atr)
        assert pp == static
        assert pp.atr_pips == 0.0


def test_gates_scale_with_atr() -> None:
    atr = 120.0
    pp = resolve_profile("GBPJPY", atr)

    assert pp.atr_pips == 120.0
    assert pp.asian_range_max_pips == pytest.approx(GATE_RATIOS.asian_range_max * atr)
    assert pp.stop_hunt_min_pips == pytest.approx(GATE_RATIOS.stop_hunt_min * atr)
    assert pp.stop_hunt_max_pips == pytest.approx(GATE_RATIOS.stop_hunt_max * atr)
    assert pp.expected_level_move_pips == pytest.approx(GATE_RATIOS.expected_level_move * atr)
    assert pp.trail_activation_pips == pytest.approx(GATE_RATIOS.trail_activation * atr)
    assert pp.trail_distance_pips == pytest.approx(GATE_RATIOS.trail_distance * atr)
    assert pp.sl_buffer_pips == pytest.approx(GATE_RATIOS.sl_buffer * atr)
    assert pp.min_sl_pips == pytest.approx(GATE_RATIOS.min_sl * atr)

    # Instrument facts unchanged
    static = get_pair_profile("GBPJPY")
    assert pp.max_risk_pct == static.max_risk_pct
    assert pp.max_spread_pips == static.max_spread_pips
    assert pp.stale_exit_minutes == static.stale_exit_minutes


def test_spread_floors_apply_in_quiet_regimes() -> None:
    # GBPJPY spread fact is 4.0p. At ATR=20p the raw ratios would give
    # trail_distance 3p, sl_buffer 1p, min_sl 5p — all inside the spread.
    pp = resolve_profile("GBPJPY", 20.0)

    assert pp.sl_buffer_pips == 4.0          # >= 1 spread
    assert pp.trail_distance_pips == 8.0     # >= 2 spreads
    assert pp.min_sl_pips == 16.0            # >= 4 spreads
    # Activation can never sit below the trail distance
    assert pp.trail_activation_pips >= pp.trail_distance_pips


def test_xauusd_gets_real_gates_by_construction() -> None:
    """The audit's vacuous 8000/15000-pip gold gates disappear with ATR."""
    atr = 11572.0  # measured 2026-06-12
    pp = resolve_profile("XAUUSD", atr)

    assert pp.stop_hunt_max_pips == pytest.approx(atr)          # was 15000 (P90 artifact)
    assert pp.asian_range_max_pips == pytest.approx(0.55 * atr)  # was 8000 (always passed)
    assert pp.stop_hunt_min_pips == pytest.approx(0.30 * atr)    # was 200 (0.017 ATR — noise)


class _FakeEngine:
    def __init__(self, d1: pd.DataFrame, pip: float = 0.0001) -> None:
        self._d1 = d1
        self._pip = pip

    def fetch_rates(self, symbol: str, timeframe: str, count: int = 200) -> pd.DataFrame:
        assert timeframe == "D1"
        return self._d1.tail(count)

    def _get_pip_value(self, symbol: str) -> float:
        return self._pip


def test_d1_atr_pips_constant_range() -> None:
    # Constant 10-pip daily bars -> Wilder ATR converges to exactly 10 pips.
    index = pd.date_range(datetime(2026, 4, 1, tzinfo=timezone.utc), periods=40, freq="1D")
    d1 = pd.DataFrame(
        {
            "Open": [1.1005] * 40,
            "High": [1.1010] * 40,
            "Low": [1.1000] * 40,
            "Close": [1.1005] * 40,
        },
        index=index,
    )
    atr = d1_atr_pips(_FakeEngine(d1), "EURUSD")
    assert atr == pytest.approx(10.0, rel=1e-3)


def test_d1_atr_pips_returns_none_on_failure() -> None:
    class _BrokenEngine:
        def fetch_rates(self, *a, **k):
            raise ConnectionError("MT5 down")

        def _get_pip_value(self, symbol: str) -> float:
            return 0.0001

    assert d1_atr_pips(_BrokenEngine(), "EURUSD") is None

    # Too little data -> None as well
    index = pd.date_range(datetime(2026, 6, 1, tzinfo=timezone.utc), periods=5, freq="1D")
    short = pd.DataFrame(
        {"Open": [1.0] * 5, "High": [1.001] * 5, "Low": [0.999] * 5, "Close": [1.0] * 5},
        index=index,
    )
    assert d1_atr_pips(_FakeEngine(short), "EURUSD") is None
