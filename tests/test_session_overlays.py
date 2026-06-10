"""Smoke test for the Pine-port session overlays: London/NY open boxes,
Gann segments, rolling Asian average. Builds a synthetic 3-day M15 frame
and asserts each structure is populated and internally consistent.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from helix_v3.core.sessions import (  # noqa: E402
    ASIA_END,
    ASIA_START,
    LONDON_BOX_END,
    LONDON_BOX_START,
    NY_BOX_END,
    NY_BOX_START,
    classify_sessions,
)


def _synthetic_m15(days: int = 3) -> pd.DataFrame:
    """3 full days of M15 bars starting Monday 00:00 UTC. Synthetic walk."""
    n = 96 * days  # 96 fifteen-minute bars per day
    start = pd.Timestamp("2026-06-01 00:00", tz="UTC")  # Monday
    idx = pd.date_range(start=start, periods=n, freq="15min")
    rng = np.random.default_rng(7)
    walk = np.cumsum(rng.normal(0, 0.0003, n))
    close = 1.1000 + walk
    high = close + rng.uniform(0.00005, 0.00040, n)
    low = close - rng.uniform(0.00005, 0.00040, n)
    open_ = np.roll(close, 1)
    open_[0] = close[0]
    df = pd.DataFrame(
        {"Open": open_, "High": high, "Low": low, "Close": close},
        index=idx,
    )
    return df


def test_session_overlays_populated() -> None:
    df = _synthetic_m15(days=3)
    info = classify_sessions(df, pip_size=0.0001)

    # 3 Asian sessions visible -> 3 ranges and 3 boxes per overlay
    assert len(info.asian_ranges) == 3, info.asian_ranges
    assert len(info.london_open_boxes) == 3, info.london_open_boxes
    assert len(info.ny_open_boxes) == 3, info.ny_open_boxes
    # Gann segments: each Asian carries forward, so 3 segments
    assert len(info.gann_segments) == 3, info.gann_segments

    # Rolling Asian average sane
    assert info.asian_avg_pips > 0
    pips_list = [ar["pips"] for ar in info.asian_ranges.values()]
    assert abs(info.asian_avg_pips - sum(pips_list) / len(pips_list)) < 1e-6

    # Each Gann segment's level must equal that day's Asian H/Mid/L
    for seg in info.gann_segments:
        ar = info.asian_ranges[seg["date"]]
        assert seg["high"] == ar["high"]
        assert seg["low"] == ar["low"]
        assert abs(seg["mid"] - (ar["high"] + ar["low"]) / 2.0) < 1e-12
        assert seg["end_idx"] > seg["start_idx"]

    # Open-box bars must fall inside their declared minute windows
    for date_str, box in info.london_open_boxes.items():
        start_ts = df.index[box["start_idx"]]
        end_ts = df.index[box["end_idx"]]
        for ts in (start_ts, end_ts):
            m = ts.hour * 60 + ts.minute
            assert LONDON_BOX_START <= m < LONDON_BOX_END, (date_str, ts, m)

    for date_str, box in info.ny_open_boxes.items():
        start_ts = df.index[box["start_idx"]]
        end_ts = df.index[box["end_idx"]]
        for ts in (start_ts, end_ts):
            m = ts.hour * 60 + ts.minute
            assert NY_BOX_START <= m < NY_BOX_END, (date_str, ts, m)

    # Asian range bars actually sit inside the Asian session window
    for date_str, ar in info.asian_ranges.items():
        s_ts = df.index[ar["start_idx"]]
        e_ts = df.index[ar["end_idx"]]
        for ts in (s_ts, e_ts):
            m = ts.hour * 60 + ts.minute
            assert ASIA_START <= m < ASIA_END, (date_str, ts, m)


if __name__ == "__main__":
    test_session_overlays_populated()
    print("OK")
