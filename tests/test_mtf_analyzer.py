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


def test_mtf_analyzer_uses_most_recent_mw_pattern_direction() -> None:
    index = pd.date_range(
        datetime(2026, 6, 12, 2, 15, tzinfo=timezone.utc),
        periods=200,
        freq="15min",
    )
    rows = [
        {
            "Open": 200.05,
            "High": 200.20,
            "Low": 199.98,
            "Close": 200.06,
            "Volume": 100,
        }
        for _ in index
    ]

    last_20_start = len(rows) - 20

    # Older W-bottom candidate.
    rows[last_20_start + 3]["Low"] = 199.90
    rows[last_20_start + 5]["Low"] = 200.04
    rows[last_20_start + 7]["Low"] = 199.92

    # More recent M-top candidate.
    rows[last_20_start + 13]["High"] = 200.35
    rows[last_20_start + 15]["High"] = 200.20
    rows[last_20_start + 17]["High"] = 200.38

    m15 = pd.DataFrame(rows, index=index)
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
    entry = analyzer._analyze_15m("GBPJPY", get_pair_profile("GBPJPY"))

    assert entry.m_w_forming is True
    assert entry.m_w_pattern == "M_TOP"
    assert entry.stop_hunt_direction == Direction.SELL
    assert entry.entry_direction == Direction.SELL

