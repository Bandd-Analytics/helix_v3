"""Unit tests for the Track 3d cointegration diagnostic math (no MT5 needed).

Verifies the hand-rolled OLS / ADF / half-life against constructed series with
known properties, so the live verdict rests on validated machinery.
"""
import math

import numpy as np

from helix_v3.backtest.cointegration_research import (
    EG_CRIT_5,
    adf_stat,
    half_life,
    hedge_ratio,
)


def _ou_series(n=1500, lam=-0.05, sigma=0.01, seed=0):
    """Ornstein-Uhlenbeck (stationary, mean-reverting) path."""
    rng = np.random.default_rng(seed)
    s = np.zeros(n)
    for t in range(1, n):
        s[t] = s[t - 1] + lam * s[t - 1] + sigma * rng.standard_normal()
    return s


def _random_walk(n=1500, sigma=0.01, seed=0):
    rng = np.random.default_rng(seed)
    return np.cumsum(sigma * rng.standard_normal(n))


def test_adf_rejects_for_stationary_series():
    # A strongly mean-reverting series should produce a very negative ADF stat,
    # well past the 5% Engle-Granger critical value.
    stat = adf_stat(_ou_series(lam=-0.10))
    assert stat is not None
    assert stat < EG_CRIT_5, f"stationary series should pass the gate, got {stat:.2f}"


def test_adf_does_not_reject_for_random_walk():
    # A random walk is NOT stationary -> ADF stat should be near 0 / not pass.
    stat = adf_stat(_random_walk())
    assert stat is not None
    assert stat > EG_CRIT_5, f"random walk should fail the gate, got {stat:.2f}"


def test_hedge_ratio_recovers_known_beta():
    rng = np.random.default_rng(1)
    log_b = np.cumsum(0.01 * rng.standard_normal(2000))
    true_beta, true_alpha = 1.7, 0.3
    log_a = true_alpha + true_beta * log_b + 0.001 * rng.standard_normal(2000)
    alpha, beta = hedge_ratio(log_a, log_b)
    assert abs(beta - true_beta) < 0.05
    assert abs(alpha - true_alpha) < 0.05


def test_half_life_positive_and_sane_for_ou():
    # lam=-0.05 -> HL = -ln2/lam ~= 13.86 bars
    hl = half_life(_ou_series(lam=-0.05))
    assert hl is not None and math.isfinite(hl)
    assert 8 < hl < 22, f"HL out of expected OU range: {hl}"


def test_half_life_infinite_for_random_walk():
    hl = half_life(_random_walk())
    # a random walk has lam ~ 0; estimator may land slightly +/- but should be
    # either inf (lam>=0) or a very large positive number.
    assert hl is not None
    assert hl == math.inf or hl > 100
