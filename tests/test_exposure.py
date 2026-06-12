"""Tests for the portfolio currency-exposure cap (audit Tier 2.6)."""
from __future__ import annotations

import pytest

from helix_v3.core.exposure import OpenRisk, currency_risk, exposure_violation
from helix_v3.core.types import Direction

CAP = 0.02  # 2x 1% single-trade risk


def test_currency_risk_signs() -> None:
    assert currency_risk("EURUSD", Direction.BUY, 0.01) == {"EUR": 0.01, "USD": -0.01}
    assert currency_risk("GBPJPY", Direction.SELL, 0.008) == {"GBP": -0.008, "JPY": 0.008}
    # Gold long = USD short for news purposes
    assert currency_risk("XAUUSD", Direction.BUY, 0.005) == {"XAU": 0.005, "USD": -0.005}
    # Indices stay in their own bucket
    assert currency_risk("US30", Direction.BUY, 0.003) == {"US30": 0.003}


def test_audit_example_three_gbp_longs() -> None:
    """3 GBP longs at 0.8% = 2.4% correlated GBP — the third is blocked."""
    opens = [
        OpenRisk("GBPUSD", Direction.BUY, 0.008),
        OpenRisk("GBPJPY", Direction.BUY, 0.008),
    ]
    # Second GBP long was fine (1.6% <= 2.0%)
    assert exposure_violation("GBPJPY", Direction.BUY, 0.008, opens[:1], CAP) is None
    # Third blows through the cap (2.4% > 2.0%)
    reason = exposure_violation("GBPAUD", Direction.BUY, 0.008, opens, CAP)
    assert reason is not None
    assert "GBP" in reason


def test_netting_offsets() -> None:
    """A GBP short against two GBP longs REDUCES net GBP — always allowed."""
    opens = [
        OpenRisk("GBPUSD", Direction.BUY, 0.01),
        OpenRisk("GBPJPY", Direction.BUY, 0.01),
    ]
    assert exposure_violation("GBPCHF", Direction.SELL, 0.01, opens, CAP) is None


def test_quote_currency_counts() -> None:
    """Three USD shorts via different bases still stack USD exposure."""
    opens = [
        OpenRisk("EURUSD", Direction.BUY, 0.01),   # short USD 1%
        OpenRisk("GBPUSD", Direction.BUY, 0.01),   # short USD 1%
    ]
    reason = exposure_violation("AUDUSD", Direction.BUY, 0.01, opens, CAP)
    assert reason is not None
    assert "USD" in reason


def test_breakeven_positions_free_the_cap() -> None:
    """Positions with stops at breakeven contribute zero risk."""
    opens = [
        OpenRisk("GBPUSD", Direction.BUY, 0.0),    # SL at BE
        OpenRisk("GBPJPY", Direction.BUY, 0.008),
    ]
    assert exposure_violation("GBPAUD", Direction.BUY, 0.008, opens, CAP) is None


def test_unrelated_currency_not_blocked() -> None:
    opens = [
        OpenRisk("GBPUSD", Direction.BUY, 0.01),
        OpenRisk("GBPJPY", Direction.BUY, 0.01),
    ]
    # EURCHF touches neither GBP nor the violating side of USD/JPY
    assert exposure_violation("EURCHF", Direction.BUY, 0.01, opens, CAP) is None


def test_block_requires_new_trade_to_worsen() -> None:
    """An already-over-cap book must not block trades that reduce it."""
    opens = [
        OpenRisk("GBPUSD", Direction.BUY, 0.015),
        OpenRisk("GBPJPY", Direction.BUY, 0.015),  # net GBP +3% (over cap)
    ]
    # Another GBP long: blocked
    assert exposure_violation("GBPCHF", Direction.BUY, 0.008, opens, CAP) is not None
    # A GBP short reduces the bucket: allowed
    assert exposure_violation("GBPCHF", Direction.SELL, 0.008, opens, CAP) is None
