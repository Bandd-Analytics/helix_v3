"""Canonical market-time tests (Tier 1.2).

IC Markets stamps bars in server time: GMT+2 in NY-winter, GMT+3 while US
daylight saving is active. The old code labeled those stamps as UTC, shifting
the Asian range 2-3 hours and silently moving it twice a year.
"""

from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd

from helix_v3.core.market_time import (
    asian_session_mask,
    server_index_to_utc,
    server_offset_hours,
    server_stamp_to_utc,
    session_name_at,
    utc_now_server_epoch,
    utc_to_server_stamp,
)


def test_server_offset_follows_us_dst() -> None:
    assert server_offset_hours(datetime(2026, 1, 15, 12, 0, tzinfo=timezone.utc)) == 2
    assert server_offset_hours(datetime(2026, 6, 15, 12, 0, tzinfo=timezone.utc)) == 3


def test_server_index_to_utc_winter_and_summer() -> None:
    idx = pd.DatetimeIndex(
        [
            pd.Timestamp("2026-01-15 10:00", tz="UTC"),  # server stamp, NY winter
            pd.Timestamp("2026-06-15 10:00", tz="UTC"),  # server stamp, US DST
        ]
    )
    converted = server_index_to_utc(idx)
    assert converted[0] == pd.Timestamp("2026-01-15 08:00", tz="UTC")
    assert converted[1] == pd.Timestamp("2026-06-15 07:00", tz="UTC")


def test_scalar_round_trip() -> None:
    stamp = datetime(2026, 6, 15, 10, 0, tzinfo=timezone.utc)  # server-labeled
    assert utc_to_server_stamp(server_stamp_to_utc(stamp)) == stamp


def test_utc_now_server_epoch_is_offset_ahead() -> None:
    now = datetime.now(timezone.utc)
    expected = int(now.timestamp()) + server_offset_hours(now) * 3600
    assert abs(utc_now_server_epoch() - expected) <= 2  # seconds of slack


def test_asian_session_mask_boundaries() -> None:
    idx = pd.DatetimeIndex(
        [
            pd.Timestamp("2026-06-15 00:15", tz="UTC"),  # before window
            pd.Timestamp("2026-06-15 00:30", tz="UTC"),  # window opens
            pd.Timestamp("2026-06-15 07:15", tz="UTC"),  # last in-window bar
            pd.Timestamp("2026-06-15 07:30", tz="UTC"),  # window closed
        ]
    )
    assert list(asian_session_mask(idx)) == [False, True, True, False]


def test_session_names_match_scanner_legacy() -> None:
    cases = {
        23: "ASIAN_EARLY",
        3: "ASIAN_LATE",
        7: "LONDON_PREMARKET",
        10: "LONDON",
        14: "NY_OVERLAP",
        18: "NY_LATE",
    }
    for hour, expected in cases.items():
        dt = datetime(2026, 6, 15, hour, 0, tzinfo=timezone.utc)
        assert session_name_at(dt) == expected, hour
