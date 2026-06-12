"""Look-ahead regression tests (Tier 1.1).

MT5 indexes bars by OPEN time. The old `index <= as_of` filter served the
currently-forming higher-TF bar with its final OHLC — up to 3h45m of future
data inside every MTF gate. These tests pin the completed-bars-only contract.
"""

from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd

from helix_v3.backtest.data_store import HistoricalDataStore


def _frame(times: list, base: float = 1.0) -> pd.DataFrame:
    idx = pd.DatetimeIndex([pd.Timestamp(t, tz="UTC") for t in times], name="time")
    return pd.DataFrame(
        {
            "Open": [base + i * 0.001 for i in range(len(times))],
            "High": [base + 0.002 + i * 0.001 for i in range(len(times))],
            "Low": [base - 0.002 + i * 0.001 for i in range(len(times))],
            "Close": [base + 0.001 + i * 0.001 for i in range(len(times))],
            "Volume": [100] * len(times),
        },
        index=idx,
    )


def _store() -> HistoricalDataStore:
    store = HistoricalDataStore.__new__(HistoricalDataStore)
    store._symbols = ["EURUSD"]
    store._start = datetime(2026, 6, 1, tzinfo=timezone.utc)
    store._end = datetime(2026, 6, 2, tzinfo=timezone.utc)
    store._cache = {
        ("EURUSD", "H4"): _frame(
            ["2026-06-01 00:00", "2026-06-01 04:00", "2026-06-01 08:00"]
        ),
        ("EURUSD", "M15"): _frame(
            ["2026-06-01 05:00", "2026-06-01 05:15", "2026-06-01 05:30"]
        ),
        ("EURUSD", "D1"): _frame(["2026-05-31 00:00", "2026-06-01 00:00"]),
    }
    store._pip_sizes = {"EURUSD": 0.0001}
    store._tick_values = {"EURUSD": 1.0}
    store._symbol_digits = {"EURUSD": 5}
    return store


def test_forming_h4_bar_is_not_served() -> None:
    """At 05:30, the 04:00 H4 bar is still forming (closes 08:00). The old
    filter served it with final OHLC — 2.5 hours of future data."""
    store = _store()
    df = store.get_rates("EURUSD", "H4", datetime(2026, 6, 1, 5, 30, tzinfo=timezone.utc), 10)
    assert list(df.index) == [pd.Timestamp("2026-06-01 00:00", tz="UTC")]


def test_h4_bar_becomes_visible_exactly_at_its_close() -> None:
    store = _store()
    df = store.get_rates("EURUSD", "H4", datetime(2026, 6, 1, 8, 0, tzinfo=timezone.utc), 10)
    assert list(df.index) == [
        pd.Timestamp("2026-06-01 00:00", tz="UTC"),
        pd.Timestamp("2026-06-01 04:00", tz="UTC"),
    ]


def test_forming_d1_bar_is_not_served_intraday() -> None:
    """Intraday, today's D1 bar must be invisible — the old filter handed the
    backtest today's end-of-day close at 05:30 in the morning."""
    store = _store()
    df = store.get_rates("EURUSD", "D1", datetime(2026, 6, 1, 5, 30, tzinfo=timezone.utc), 10)
    assert list(df.index) == [pd.Timestamp("2026-05-31 00:00", tz="UTC")]


def test_m15_bar_visible_at_its_close_not_at_its_open() -> None:
    store = _store()
    at_open = store.get_rates(
        "EURUSD", "M15", datetime(2026, 6, 1, 5, 30, tzinfo=timezone.utc), 10
    )
    assert pd.Timestamp("2026-06-01 05:30", tz="UTC") not in at_open.index

    at_close = store.get_rates(
        "EURUSD", "M15", datetime(2026, 6, 1, 5, 45, tzinfo=timezone.utc), 10
    )
    assert at_close.index[-1] == pd.Timestamp("2026-06-01 05:30", tz="UTC")


def test_live_fetch_skips_the_forming_bar(monkeypatch) -> None:
    """quant_engine must fetch from position 1 (last completed bar), not 0."""
    import helix_v3.core.quant_engine as qe

    captured = {}

    def fake_copy_rates_from_pos(symbol, tf, start_pos, count):
        captured["start_pos"] = start_pos
        return [
            {
                "time": 1750000000 + i * 900,
                "open": 1.1,
                "high": 1.101,
                "low": 1.099,
                "close": 1.1005,
                "tick_volume": 100,
                "spread": 1,
                "real_volume": 0,
            }
            for i in range(count)
        ]

    monkeypatch.setattr(qe.mt5, "copy_rates_from_pos", fake_copy_rates_from_pos)
    engine = qe.MMMQuantitativeEngine()
    df = engine.fetch_rates("EURUSD", "M15", count=5)

    assert captured["start_pos"] == 1
    assert len(df) == 5
