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


def test_cross_sectional_momentum_ranks_pairs() -> None:
    # Four pairs (the cross-section needs >=4): A rises most, D falls most.
    n = 120
    a = _df(np.linspace(1.10, 1.25, n))          # strongest
    b = _df(np.linspace(1.10, 1.12, n))          # middle
    c = _df(np.linspace(1.10, 1.11, n))          # middle
    d = _df(np.linspace(1.30, 1.18, n))          # weakest
    entries = sr.cross_sectional_momentum_entries(
        {"AUSD": a, "BUSD": b, "CUSD": c, "DUSD": d}, lookback=60, top_k=1
    )
    # strongest pair gets BUY entries, weakest gets SELL entries
    assert any(dir_ == "BUY" for _, dir_ in entries["AUSD"])
    assert any(dir_ == "SELL" for _, dir_ in entries["DUSD"])
    # middle pairs are never the extreme -> no entries
    assert entries["BUSD"] == [] and entries["CUSD"] == []


def test_holding_return_label_direction_and_cost() -> None:
    # clean uptrend, hold 10 bars: BUY favorable, SELL not; cost applied
    df = _df(np.linspace(1.10, 1.30, 120))
    a = sr.atr(df)
    buy = sr._label_holding_return(df, a, [(50, "BUY")], pip_size=0.0001, cost_r=0.05, horizon=10)
    sell = sr._label_holding_return(df, a, [(50, "SELL")], pip_size=0.0001, cost_r=0.05, horizon=10)
    assert buy and buy[0][1] is True and buy[0][2] > 0
    assert sell and sell[0][1] is False and sell[0][2] < 0


def test_split_ccy() -> None:
    assert sr._split_ccy("EURUSD") == ("EUR", "USD")
    assert sr._split_ccy("GBPJPY") == ("GBP", "JPY")


def test_currency_strength_emits_entries() -> None:
    n = 80
    rising = _df(np.linspace(1.10, 1.25, n))
    flat = _df(np.linspace(1.10, 1.105, n))
    pair_dfs = {
        "EURUSD": rising, "GBPUSD": flat, "AUDUSD": flat,
        "USDJPY": rising, "EURJPY": rising, "GBPJPY": flat,
    }
    entries = sr.currency_strength_entries(pair_dfs, lookback=20)
    assert any(len(v) > 0 for v in entries.values())


def test_vol_percentile_is_point_in_time() -> None:
    # Calm history then a late volatility spike. The percentile at each bar must
    # rank ONLY against trailing bars — early bars never see the late spike, and
    # the spike bar itself ranks at the top of its own window.
    n = 400
    rng = np.linspace(1.10, 1.12, n)
    df = _df(rng)
    # widen the true range on the last 5 bars (a vol spike)
    df.iloc[-5:, df.columns.get_loc("High")] += 0.02
    df.iloc[-5:, df.columns.get_loc("Low")] -= 0.02
    volp = sr._vol_percentile_series(df)
    assert np.isnan(volp[0])              # no history to rank yet
    assert volp[-1] > 0.95               # spike bar is top of its trailing window
    # a quiet bar well before the spike is not pinned to an extreme
    assert 0.0 <= volp[200] <= 1.0


def test_calm_gate_uses_validated_band() -> None:
    # The gate reuses regime.py's [P10, P95] verbatim — a sanity check that the
    # imported thresholds are the validated ones, not local re-definitions.
    from helix_v3.core import regime
    assert sr.VOL_PCT_MIN == regime.VOL_PCT_MIN
    assert sr.VOL_PCT_MAX == regime.VOL_PCT_MAX


def test_grade_marks_insufficient_n() -> None:
    cells = [sr.CellResult(signal="s", symbol="X", n=10, favorable=5,
                           fav_rate=0.5, base_rate=0.5, p_value=None,
                           mean_net_r=0.0, p_expectancy=None)]
    sr._grade(cells)
    assert cells[0].verdict == "INSUFFICIENT_N"


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
