"""Tests for the two-state market regime filter (audit Tier 2.8)."""
from __future__ import annotations

import math
from datetime import datetime, timezone

import pandas as pd

from helix_v3.core import regime
from helix_v3.core.regime import assess_regime


class _FakeEngine:
    def __init__(self, d1: pd.DataFrame) -> None:
        self._d1 = d1

    def fetch_rates(self, symbol: str, timeframe: str, count: int = 300) -> pd.DataFrame:
        assert timeframe == "D1"
        return self._d1.tail(count)


def _d1(rows: list[dict]) -> pd.DataFrame:
    index = pd.date_range(
        datetime(2025, 6, 1, tzinfo=timezone.utc), periods=len(rows), freq="1D"
    )
    return pd.DataFrame(rows, index=index)


def _bar(center: float, half_range: float, close_offset: float = 0.0) -> dict:
    return {
        "Open": center,
        "High": center + half_range,
        "Low": center - half_range,
        "Close": center + close_offset,
    }


def _clear_cache() -> None:
    regime._cache.clear()


def test_choppy_normal_vol_is_present() -> None:
    _clear_cache()
    # Price oscillates around 1.10 with ranges breathing between 50 and
    # 110 pips (sinusoidal): mid-percentile vol, near-zero efficiency ratio.
    rows = [
        _bar(
            1.10,
            0.0040 + 0.0015 * math.sin(i / 5.0),
            0.0010 * (1 if i % 2 == 0 else -1),
        )
        for i in range(300)
    ]
    state = assess_regime(_FakeEngine(_d1(rows)), "EURUSD")
    assert state.mmm_present is True
    assert 0.10 <= state.vol_percentile <= 0.95
    assert state.efficiency_ratio < 0.2


def test_one_way_trend_is_absent() -> None:
    _clear_cache()
    # Constant ranges (vol percentile unremarkable) but closes march up
    # every single day — efficiency ratio near 1.
    rows = []
    price = 1.10
    for _ in range(300):
        rows.append({
            "Open": price,
            "High": price + 0.0050,
            "Low": price - 0.0010,
            "Close": price + 0.0040,
        })
        price += 0.0040
    state = assess_regime(_FakeEngine(_d1(rows)), "EURUSD")
    assert state.efficiency_ratio > 0.9
    assert state.mmm_present is False
    assert "one-way" in state.reason


def test_vol_spike_is_absent() -> None:
    _clear_cache()
    # A year of quiet 30-pip days, then two weeks of 300-pip days (choppy,
    # so ER stays low) — crisis-vol percentile.
    rows = [
        _bar(1.10, 0.0015, 0.0005 * (1 if i % 2 == 0 else -1))
        for i in range(280)
    ]
    rows += [
        _bar(1.10, 0.0150, 0.0030 * (1 if i % 2 == 0 else -1))
        for i in range(14)
    ]
    state = assess_regime(_FakeEngine(_d1(rows)), "EURUSD")
    assert state.vol_percentile > 0.95
    assert state.mmm_present is False
    assert "crisis vol" in state.reason


def test_dead_vol_is_absent() -> None:
    _clear_cache()
    # A year of 80-pip days collapsing into two months of 5-pip days.
    rows = [
        _bar(1.10, 0.0040, 0.0010 * (1 if i % 2 == 0 else -1))
        for i in range(240)
    ]
    rows += [
        _bar(1.10, 0.00025, 0.0001 * (1 if i % 2 == 0 else -1))
        for i in range(60)
    ]
    state = assess_regime(_FakeEngine(_d1(rows)), "EURUSD")
    assert state.vol_percentile < 0.10
    assert state.mmm_present is False
    assert "dead vol" in state.reason


def test_insufficient_data_fails_open() -> None:
    _clear_cache()
    rows = [_bar(1.10, 0.0040) for _ in range(20)]
    state = assess_regime(_FakeEngine(_d1(rows)), "EURUSD")
    assert state.mmm_present is True
    assert "fail open" in state.reason


def test_fetch_failure_fails_open() -> None:
    _clear_cache()

    class _Broken:
        def fetch_rates(self, *a, **k):
            raise ConnectionError("MT5 down")

    state = assess_regime(_Broken(), "EURUSD")
    assert state.mmm_present is True


def test_cached_per_d1_bar() -> None:
    _clear_cache()
    rows = [
        _bar(1.10, 0.0040, 0.0010 * (1 if i % 2 == 0 else -1))
        for i in range(300)
    ]
    eng = _FakeEngine(_d1(rows))
    first = assess_regime(eng, "EURUSD")
    assert assess_regime(eng, "EURUSD") is first  # same D1 bar -> cached object
