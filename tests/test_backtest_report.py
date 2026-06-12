"""Statistics tests (Tier 1.7).

The old Sharpe was mean(pnl_pips)/std(pnl_pips) x sqrt(252) — per-trade pip
statistics annualized as if each trade were a daily return, mixing pips
across pairs. These tests pin the replacement: daily MTM dollar-return
Sharpe, MTM drawdown, and the Deflated Sharpe probability.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from helix_v3.backtest.report import (
    deflated_sharpe_probability,
    equity_curve_metrics,
)

T0 = datetime(2026, 1, 5, 0, 0, tzinfo=timezone.utc)


def _daily_curve(values: list) -> list:
    return [(T0 + timedelta(days=i), v) for i, v in enumerate(values)]


def test_mtm_drawdown_from_curve() -> None:
    m = equity_curve_metrics(_daily_curve([100.0, 110.0, 99.0, 105.0]))
    assert m["max_dd_dollars"] == 11.0
    assert m["max_dd_pct"] == 10.0


def test_flat_curve_has_zero_sharpe() -> None:
    m = equity_curve_metrics(_daily_curve([100.0] * 10))
    assert m["daily_sharpe"] == 0.0


def test_steady_gains_have_high_sharpe_and_zero_dd() -> None:
    m = equity_curve_metrics(_daily_curve([100.0 * 1.01**i for i in range(30)]))
    assert m["daily_sharpe"] > 10.0  # near-constant positive returns
    assert m["max_dd_dollars"] == 0.0


def test_daily_returns_use_last_snapshot_of_each_day() -> None:
    # Two intraday points per day; only the close-of-day values matter.
    curve = []
    for i, (mid, close) in enumerate([(95.0, 100.0), (130.0, 101.0), (90.0, 102.0), (140.0, 103.0)]):
        curve.append((T0 + timedelta(days=i, hours=6), mid))
        curve.append((T0 + timedelta(days=i, hours=20), close))
    m = equity_curve_metrics(curve)
    # Daily closes 100->101->102->103: ~1% steady gains, near-zero variance
    assert m["n_days"] == 3
    assert m["daily_sharpe"] > 10.0
    # ...but the intraday excursion to 90 after a 130 peak IS the drawdown
    assert m["max_dd_dollars"] == 40.0


def test_deflated_sharpe_zero_skill_is_unconvincing() -> None:
    assert deflated_sharpe_probability(0.0, n_obs=252) < 0.5


def test_deflated_sharpe_strong_long_track_record_is_convincing() -> None:
    # Daily SR 0.2 (annual ~3.2) over 2 years
    assert deflated_sharpe_probability(0.2, n_obs=504) > 0.95


def test_more_trials_demand_more_evidence() -> None:
    few = deflated_sharpe_probability(0.1, n_obs=252, n_trials=10)
    many = deflated_sharpe_probability(0.1, n_obs=252, n_trials=1000)
    assert many < few
