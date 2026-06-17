"""Tests for the Track 3c multi-asset momentum harness."""
from __future__ import annotations

import numpy as np
import pandas as pd

from helix_v3.backtest import multiasset_research as ma


def _df(closes) -> pd.DataFrame:
    idx = pd.date_range("2021-01-01", periods=len(closes), freq="1D", tz="UTC")
    c = np.array(closes, dtype=float)
    return pd.DataFrame(
        {"Open": c, "High": c * 1.005, "Low": c * 0.995, "Close": c}, index=idx
    )


def test_tsmom_goes_long_an_uptrend() -> None:
    df = _df(np.linspace(100, 200, 400))     # persistent uptrend
    entries = ma.tsmom_entries(df, lookback=120, holding=20)
    assert entries
    assert all(d == "BUY" for _, d in entries)   # rising past return -> long


def test_tsmom_goes_short_a_downtrend() -> None:
    df = _df(np.linspace(200, 100, 400))     # persistent downtrend
    entries = ma.tsmom_entries(df, lookback=120, holding=20)
    assert entries
    assert all(d == "SELL" for _, d in entries)


def test_tsmom_entries_are_spaced_by_holding() -> None:
    df = _df(np.linspace(100, 140, 400))
    entries = ma.tsmom_entries(df, lookback=120, holding=20)
    idxs = [i for i, _ in entries]
    assert all(b - a == 20 for a, b in zip(idxs, idxs[1:]))
    assert idxs[0] == 120                     # first entry once lookback is available


def test_cost_r_floored() -> None:
    # with no MT5 session symbol_info returns None -> cost falls back to the floor
    assert ma.instrument_cost_r("DEFINITELY_NOT_A_SYMBOL", atr_price=10.0) == ma.COST_R_FLOOR
    assert ma.instrument_cost_r("ANY", atr_price=0.0) == ma.COST_R_FLOOR
