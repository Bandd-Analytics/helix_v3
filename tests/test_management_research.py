"""Tests for the Track 3b management-as-alpha harness."""
from __future__ import annotations

import numpy as np
import pandas as pd

from helix_v3.backtest import management_research as mr


def _df(closes, *, hi=0.0005, lo=0.0005) -> pd.DataFrame:
    idx = pd.date_range("2023-01-01", periods=len(closes), freq="4h", tz="UTC")
    c = np.array(closes, dtype=float)
    return pd.DataFrame(
        {"Open": c, "High": c + hi, "Low": c - lo, "Close": c}, index=idx
    )


def _atr_const(df, val=0.0010) -> pd.Series:
    return pd.Series(val, index=df.index)


def test_target_hit_pays_one_R_minus_cost() -> None:
    # clean uptrend: a BUY under sym_1_1 should hit +1R; cost = cost_r (2 fills)
    df = _df(np.linspace(1.10, 1.20, 60))
    net, fills, bars = mr.simulate_exit(
        df, 5, "BUY", 0.0010, mr.CONTROL_POLICY, cost_r=0.1, horizon=20)
    assert fills == 2
    assert abs(net - 0.9) < 1e-6           # +1R target minus 0.1R round-trip cost


def test_stop_wins_same_bar_ambiguity() -> None:
    # a bar that straddles BOTH levels must be labeled a stop (conservative)
    df = _df([1.1000, 1.1000, 1.1000], hi=0.02, lo=0.02)
    net, fills, bars = mr.simulate_exit(
        df, 0, "BUY", 0.0010, mr.CONTROL_POLICY, cost_r=0.0, horizon=2)
    assert net < 0                          # resolved as a -1R stop, not a +1R win


def test_scaleout_costs_more_fills_than_plain_exit() -> None:
    # uptrend through +1R then onward: scaleout books a partial -> >=3 fills
    df = _df(np.linspace(1.10, 1.30, 80))
    _, fills, _ = mr.simulate_exit(
        df, 5, "BUY", 0.0010, mr.POLICIES[5], cost_r=0.1, horizon=30)  # scaleout
    assert mr.POLICIES[5].name == "scaleout"
    assert fills >= 3                       # entry + partial + final


def test_time_stop_is_pure_holding_return() -> None:
    # no hard stop/target: exit at horizon close. Down move => BUY loses.
    df = _df(np.linspace(1.20, 1.10, 60))
    net, _, _ = mr.simulate_exit(
        df, 5, "BUY", 0.0010, mr.POLICIES[6], cost_r=0.0, horizon=20)  # time_stop
    assert mr.POLICIES[6].name == "time_stop"
    assert net < 0


def test_random_sign_entries_are_deterministic_and_balanced() -> None:
    df = _df(np.linspace(1.10, 1.11, 500))
    a = mr.random_sign_entries(df)
    b = mr.random_sign_entries(df)
    assert a == b                           # reproducible — no RNG state
    frac_buy = sum(1 for _, d in a if d == "BUY") / len(a)
    assert 0.3 < frac_buy < 0.7             # roughly balanced, not all one side


def test_label_managed_enforces_non_overlap() -> None:
    df = _df(np.linspace(1.10, 1.30, 200))
    a = _atr_const(df)
    # two entries one bar apart — the second overlaps the first's hold window
    labels = mr._label_managed(
        df, a, [(50, "BUY"), (51, "BUY")], mr.CONTROL_POLICY, cost_r=0.0, horizon=12)
    assert len(labels) == 1


def test_let_winners_run_beats_cut_quick_on_a_trend() -> None:
    # on a persistent uptrend, tp_2R should out-earn tp_0p5R per BUY entry
    df = _df(np.linspace(1.10, 1.50, 120))
    a = 0.0010
    run, _, _ = mr.simulate_exit(df, 5, "BUY", a, mr.POLICIES[1], cost_r=0.05, horizon=40)
    cut, _, _ = mr.simulate_exit(df, 5, "BUY", a, mr.POLICIES[2], cost_r=0.05, horizon=40)
    assert mr.POLICIES[1].name == "tp_2R" and mr.POLICIES[2].name == "tp_0p5R"
    assert run > cut
