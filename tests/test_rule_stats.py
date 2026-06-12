"""Tests for the Tier 2.4 statistical machinery (rule_stats)."""
from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd
import pytest

from helix_v3.training.rule_stats import (
    EXPIRY,
    STOP,
    TARGET,
    benjamini_hochberg,
    binomial_p_at_least,
    empirical_base_rate,
    first_touch_outcome,
)


def _df(rows: list[dict]) -> pd.DataFrame:
    index = pd.date_range(
        datetime(2026, 6, 1, tzinfo=timezone.utc), periods=len(rows), freq="15min"
    )
    return pd.DataFrame(rows, index=index)


def _bar(o: float, h: float, low: float, c: float) -> dict:
    return {"Open": o, "High": h, "Low": low, "Close": c}


PIP = 0.0001


def test_target_touched_first_is_target() -> None:
    df = _df([
        _bar(1.1000, 1.1002, 1.0998, 1.1000),   # entry bar
        _bar(1.1000, 1.1011, 1.0999, 1.1008),   # +11p high, never -10p
        _bar(1.1008, 1.1009, 1.0985, 1.0990),   # would stop AFTER target
    ])
    ft = first_touch_outcome(df, 0, "BUY", 1.1000, 10.0, 10.0, 10, PIP)
    assert ft.outcome == TARGET
    assert ft.bars_held == 1
    assert ft.pips_result == 10.0


def test_stop_then_rally_is_stop_not_hit() -> None:
    """The exact failure the audit flagged: MFE>MAE scored this a HIT."""
    df = _df([
        _bar(1.1000, 1.1002, 1.0998, 1.1000),   # entry bar
        _bar(1.1000, 1.1003, 1.0989, 1.0992),   # -11p low first (stopped)
        _bar(1.0992, 1.1030, 1.0991, 1.1028),   # then a 30p rally (MFE >> MAE)
    ])
    ft = first_touch_outcome(df, 0, "BUY", 1.1000, 10.0, 10.0, 10, PIP)
    assert ft.outcome == STOP
    assert ft.bars_held == 1
    assert ft.pips_result == -10.0


def test_same_bar_ambiguity_resolves_to_stop() -> None:
    df = _df([
        _bar(1.1000, 1.1002, 1.0998, 1.1000),
        _bar(1.1000, 1.1015, 1.0985, 1.1000),   # bar contains BOTH levels
    ])
    ft = first_touch_outcome(df, 0, "BUY", 1.1000, 10.0, 10.0, 10, PIP)
    assert ft.outcome == STOP


def test_expiry_when_neither_touched() -> None:
    df = _df([_bar(1.1000, 1.1004, 1.0996, 1.1000)] * 6)
    ft = first_touch_outcome(df, 0, "BUY", 1.1000, 10.0, 10.0, 4, PIP)
    assert ft.outcome == EXPIRY
    assert ft.bars_held == 4


def test_sell_direction_mirrors() -> None:
    df = _df([
        _bar(1.1000, 1.1002, 1.0998, 1.1000),
        _bar(1.1000, 1.1001, 1.0988, 1.0990),   # -12p low = SELL target
    ])
    ft = first_touch_outcome(df, 0, "SELL", 1.1000, 10.0, 10.0, 10, PIP)
    assert ft.outcome == TARGET


def test_binomial_known_values() -> None:
    # P(X >= 6 | n=10, p=0.5) = 386/1024
    assert binomial_p_at_least(6, 10, 0.5) == pytest.approx(386 / 1024, rel=1e-9)
    # Edge cases
    assert binomial_p_at_least(0, 10, 0.5) == 1.0
    assert binomial_p_at_least(11, 10, 0.5) == 0.0
    assert binomial_p_at_least(10, 10, 0.5) == pytest.approx(0.5 ** 10, rel=1e-9)


def test_benjamini_hochberg_classic_example() -> None:
    # Benjamini & Hochberg (1995) worked example, m=15, q=0.05:
    # the 4 smallest p-values are rejected (note p=0.0095 rejected because
    # rank-4 0.0095 <= 4/15*0.05 = 0.0133 covers ranks 1-4 by step-up).
    pvals = [
        0.0001, 0.0004, 0.0019, 0.0095, 0.0201, 0.0278, 0.0298, 0.0344,
        0.0459, 0.3240, 0.4262, 0.5719, 0.6528, 0.7590, 1.0000,
    ]
    flags = benjamini_hochberg(pvals, q=0.05)
    assert flags == [True] * 4 + [False] * 11


def test_benjamini_hochberg_handles_none() -> None:
    flags = benjamini_hochberg([None, 0.001, None, 0.9], q=0.10)
    assert flags == [False, True, False, False]
    assert benjamini_hochberg([None, None]) == [False, False]


def test_empirical_base_rate_non_overlapping() -> None:
    # Strong uptrend: every bar +5p with 12p range — BUY base rate should
    # be high, SELL base rate low, and sampling must be non-overlapping
    # (200 bars / horizon 4 -> ~50 samples, not 200).
    rows = []
    price = 1.1000
    for _ in range(200):
        rows.append(_bar(price, price + 0.0010, price - 0.0002, price + 0.0005))
        price += 0.0005
    df = _df(rows)

    buy_rate, n_buy = empirical_base_rate(df, "BUY", 10.0, 10.0, 4, PIP)
    sell_rate, n_sell = empirical_base_rate(df, "SELL", 10.0, 10.0, 4, PIP)
    assert n_buy <= 50 and n_sell <= 50
    assert buy_rate > 0.9
    assert sell_rate < 0.1


def test_empirical_base_rate_insufficient_returns_none() -> None:
    df = _df([_bar(1.1, 1.101, 1.099, 1.1)] * 20)
    rate, n = empirical_base_rate(df, "BUY", 10.0, 10.0, 4, PIP)
    assert rate is None
