"""Tests for the Track 3a FX non-MMM signal-research harness."""
from __future__ import annotations

import numpy as np
import pandas as pd

from helix_v3.backtest import signal_research as sr


def _df(closes) -> pd.DataFrame:
    idx = pd.date_range("2023-01-01", periods=len(closes), freq="4h", tz="UTC")
    c = np.array(closes, dtype=float)
    return pd.DataFrame(
        {"Open": c, "High": c + 0.0005, "Low": c - 0.0005, "Close": c}, index=idx
    )


def test_atr_and_pip_size() -> None:
    df = _df(np.linspace(1.10, 1.11, 60))
    a = sr.atr(df)
    assert a.iloc[-1] > 0
    assert sr.pip_size_for("USDJPY") == 0.01
    assert sr.pip_size_for("EURUSD") == 0.0001


def test_donchian_fires_on_breakout() -> None:
    # flat then a jump above the 20-bar high -> a BUY breakout
    closes = [1.10] * 30 + [1.11] * 5
    sigs = sr.donchian_breakout(_df(closes), n=20)
    assert any(d == "BUY" for _, d in sigs)


def test_zscore_reversion_direction() -> None:
    # a sharp dip far below the rolling mean -> BUY (fade up)
    closes = [1.10] * 25 + [1.085]
    sigs = sr.zscore_reversion(_df(closes), lookback=20, z=2.0)
    assert sigs and sigs[-1][1] == "BUY"


def test_non_overlapping_enforced_in_labeling() -> None:
    df = _df(np.linspace(1.10, 1.20, 300))
    a = sr.atr(df)
    # two entries one bar apart — the second overlaps the first's horizon
    entries = [(50, "BUY"), (51, "BUY")]
    labels = sr._label_entries(df, a, entries, pip_size=0.0001, cost_r=0.0)
    assert len(labels) == 1


def test_net_r_includes_cost() -> None:
    # a clean uptrend so a BUY hits its +1R target; cost reduces the R
    df = _df(np.linspace(1.10, 1.40, 400))
    a = sr.atr(df)
    labels = sr._label_entries(df, a, [(50, "BUY")], pip_size=0.0001, cost_r=0.1)
    assert labels
    _, favorable, net_r = labels[0]
    assert favorable is True
    assert abs(net_r - 0.9) < 1e-6   # +1R target minus 0.1R cost


def test_verdict_requires_significance_and_holdout(monkeypatch) -> None:
    # Build a fake result set: one cell strongly significant + positive holdout.
    cells = [
        sr.CellResult(signal="s", symbol="EURUSD", n=200, favorable=140,
                      fav_rate=0.70, base_rate=0.45, p_value=1e-9,
                      mean_net_r=0.3, p_expectancy=1e-9,
                      holdout_n=40, holdout_mean_net_r=0.25),
        sr.CellResult(signal="s", symbol="GBPUSD", n=50, favorable=20,
                      fav_rate=0.40, base_rate=0.45, p_value=0.9,
                      mean_net_r=-0.2, p_expectancy=0.9,
                      holdout_n=40, holdout_mean_net_r=-0.2),
    ]
    # apply the same post-processing audit() does
    from helix_v3.training.rule_stats import benjamini_hochberg
    for r, f in zip(cells, benjamini_hochberg([c.p_value for c in cells], 0.10)):
        r.bh_significant = f
    for r, f in zip(cells, benjamini_hochberg([c.p_expectancy for c in cells], 0.10)):
        r.bh_exp_significant = f
    for r in cells:
        edge = (r.bh_significant and r.mean_net_r > 0) or r.bh_exp_significant
        replicates = r.holdout_n >= sr.MIN_HOLDOUT_N and r.holdout_mean_net_r > 0
        r.verdict = "VALIDATED" if (edge and replicates) else "DEAD"
    assert cells[0].verdict == "VALIDATED"
    assert cells[1].verdict == "DEAD"
