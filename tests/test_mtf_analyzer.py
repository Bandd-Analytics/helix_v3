"""Tests for the M15 stop-hunt gate and M/W detector (audit Tier 2.1 / 2.2).

Synthetic GBPJPY data (pip 0.01, hunt range 30-130p, Asian range max 50p).
Baseline bars give an Asian range of 200.20 / 199.98 (22p, accumulation
valid). The last 20 bars are post-Asian, where the detector scans.
"""
from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd

from config.pair_profiles import get_pair_profile
from helix_v3.core.mtf_analyzer import MTFAnalyzer
from helix_v3.core.types import Direction


class _FakeEngine:
    def __init__(self, m15: pd.DataFrame, d1: pd.DataFrame) -> None:
        self._m15 = m15
        self._d1 = d1

    def fetch_rates(self, symbol: str, timeframe: str, count: int = 200) -> pd.DataFrame:
        if timeframe == "D1":
            return self._d1.tail(count)
        return self._m15.tail(count)

    def _get_pip_value(self, symbol: str) -> float:
        return 0.01


# Last bar 2026-06-12 20:00 UTC -> the latest Asian session (00:30-07:30 UTC
# on Jun 12) is complete and the last 20 bars are all post-Asian.
_INDEX = pd.date_range(
    datetime(2026, 6, 10, 18, 15, tzinfo=timezone.utc),
    periods=200,
    freq="15min",
)
_LAST20 = len(_INDEX) - 20  # detector window starts here


def _baseline_rows() -> list[dict]:
    return [
        {
            "Open": 200.05,
            "High": 200.20,
            "Low": 199.98,
            "Close": 200.06,
            "Volume": 100,
        }
        for _ in _INDEX
    ]


def _run(rows: list[dict]):
    m15 = pd.DataFrame(rows, index=_INDEX)
    d1_index = pd.date_range(
        datetime(2026, 5, 20, tzinfo=timezone.utc),
        periods=20,
        freq="1D",
    )
    d1 = pd.DataFrame(
        {
            "Open": [200.0] * 20,
            "High": [201.0] * 20,
            "Low": [199.0] * 20,
            "Close": [200.2] * 20,
        },
        index=d1_index,
    )
    analyzer = MTFAnalyzer(_FakeEngine(m15, d1))
    return analyzer._analyze_15m("GBPJPY", get_pair_profile("GBPJPY"))


def _confirm_up(rows: list[dict], close: float) -> None:
    """Make the forming bar close above a W neckline."""
    rows[-1]["Close"] = close
    rows[-1]["High"] = max(rows[-1]["High"], close + 0.02)


def test_w_bottom_with_soft_hunt_is_buy() -> None:
    rows = _baseline_rows()
    # Two troughs 6p below the Asian low (soft breach), bump/neckline between.
    rows[_LAST20 + 13]["Low"] = 199.92
    rows[_LAST20 + 15]["High"] = 200.12  # neckline
    rows[_LAST20 + 17]["Low"] = 199.93
    _confirm_up(rows, 200.16)  # neckline break

    entry = _run(rows)

    assert entry.m_w_forming is True
    assert entry.m_w_pattern == "W_BOTTOM"
    assert entry.stop_hunt_detected is True
    assert entry.stop_hunt_direction == Direction.BUY
    assert 5.0 <= entry.stop_hunt_pips <= 7.0
    assert entry.entry_direction == Direction.BUY


def test_m_top_with_soft_hunt_is_sell() -> None:
    rows = _baseline_rows()
    # Two peaks 6-7p above the Asian high (soft breach), valley between.
    rows[_LAST20 + 13]["High"] = 200.26
    rows[_LAST20 + 15]["Low"] = 200.10  # neckline
    rows[_LAST20 + 17]["High"] = 200.27
    # Baseline close 200.06 already sits below the neckline (confirmed).

    entry = _run(rows)

    assert entry.m_w_forming is True
    assert entry.m_w_pattern == "M_TOP"
    assert entry.stop_hunt_detected is True
    assert entry.stop_hunt_direction == Direction.SELL
    assert 6.0 <= entry.stop_hunt_pips <= 8.0
    assert entry.entry_direction == Direction.SELL


def test_mw_without_breach_is_not_a_hunt() -> None:
    """Tier 2.1 regression: an M/W with zero breach must not fabricate a hunt."""
    rows = _baseline_rows()
    # W anchored within tolerance of the Asian low but never breaching it.
    rows[_LAST20 + 13]["Low"] = 199.99
    rows[_LAST20 + 15]["Low"] = 200.04
    rows[_LAST20 + 15]["High"] = 200.12  # neckline
    rows[_LAST20 + 17]["Low"] = 199.99
    _confirm_up(rows, 200.16)

    entry = _run(rows)

    assert entry.m_w_forming is True
    assert entry.m_w_pattern == "W_BOTTOM"
    assert entry.stop_hunt_detected is False
    assert entry.stop_hunt_pips == 0.0
    assert entry.entry_signal is False
    assert entry.entry_direction == Direction.NEUTRAL


def test_mw_with_breach_beyond_max_is_not_readmitted() -> None:
    """A breach the hard gate rejected as too deep can't re-enter via M/W."""
    rows = _baseline_rows()
    # Troughs 138p below the Asian low — beyond GBPJPY's 130p hunt max.
    rows[_LAST20 + 13]["Low"] = 198.60
    rows[_LAST20 + 15]["High"] = 200.12  # neckline
    rows[_LAST20 + 17]["Low"] = 198.61
    _confirm_up(rows, 200.16)

    entry = _run(rows)

    assert entry.m_w_forming is True
    assert entry.stop_hunt_detected is False
    assert entry.entry_signal is False


def test_hard_hunt_without_pattern_uses_breach_side() -> None:
    """Classic hunt: 35p breach below the Asian low -> BUY, no pattern needed."""
    rows = _baseline_rows()
    rows[_LAST20 + 15]["Low"] = 199.63  # lone spike, no M/W geometry

    entry = _run(rows)

    assert entry.m_w_forming is False
    assert entry.stop_hunt_detected is True
    assert entry.stop_hunt_direction == Direction.BUY
    assert 34.0 <= entry.stop_hunt_pips <= 36.0
    # No M/W, no RRT, <3 pushes -> hunt alone is not an entry.
    assert entry.entry_signal is False
