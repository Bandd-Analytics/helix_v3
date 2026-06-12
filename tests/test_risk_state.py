"""Kill-switch tests (Tier 0.4).

The old breaker computed (balance - equity) / balance, which resets to ~0 the
moment a loss is REALIZED — these tests pin the replacement: persisted balance
high-water mark, daily anchor, latched daily trips.
"""

from __future__ import annotations

from datetime import datetime, timezone
from types import SimpleNamespace

from helix_v3.execution.risk_state import RiskState

DAY1 = datetime(2026, 6, 12, 10, 0, tzinfo=timezone.utc)
DAY2 = datetime(2026, 6, 13, 10, 0, tzinfo=timezone.utc)


def _risk_state(tmp_path) -> RiskState:
    return RiskState(
        db_path=tmp_path / "risk_state.db",
        max_daily_loss_pct=0.04,
        max_total_drawdown_pct=0.08,
    )


def test_realized_losses_trip_the_daily_limit(tmp_path) -> None:
    """Regression: (balance-equity)/balance is 0 after a realized loss."""
    rs = _risk_state(tmp_path)
    ok, _ = rs.check(balance=1000.0, equity=1000.0, now=DAY1)
    assert ok

    # Loss realized: balance and equity BOTH drop — old formula saw 0% DD.
    ok, reason = rs.check(balance=950.0, equity=950.0, now=DAY1)
    assert not ok
    assert "daily loss" in reason


def test_daily_trip_latches_for_the_rest_of_the_day(tmp_path) -> None:
    rs = _risk_state(tmp_path)
    rs.check(balance=1000.0, equity=1000.0, now=DAY1)
    rs.check(balance=950.0, equity=950.0, now=DAY1)

    # Equity recovers — still blocked until the trading day rolls.
    ok, reason = rs.check(balance=950.0, equity=999.0, now=DAY1)
    assert not ok
    assert "latched" in reason


def test_new_trading_day_resets_the_daily_latch(tmp_path) -> None:
    rs = _risk_state(tmp_path)
    rs.check(balance=1000.0, equity=1000.0, now=DAY1)
    rs.check(balance=950.0, equity=950.0, now=DAY1)

    ok, _ = rs.check(balance=960.0, equity=960.0, now=DAY2)
    assert ok


def test_total_drawdown_measured_from_persisted_high_water_mark(tmp_path) -> None:
    rs = _risk_state(tmp_path)
    rs.check(balance=1000.0, equity=1000.0, now=DAY1)
    rs.close()

    # Restart: HWM must survive. Day 2 anchor is 945, so the daily loss is
    # only 3.2% — but total drawdown from the $1000 HWM is 8.5%.
    rs2 = _risk_state(tmp_path)
    ok, reason = rs2.check(balance=945.0, equity=915.0, now=DAY2)
    assert not ok
    assert "total drawdown" in reason


def test_floating_losses_count_via_equity(tmp_path) -> None:
    rs = _risk_state(tmp_path)
    rs.check(balance=1000.0, equity=1000.0, now=DAY1)

    # Balance untouched (position still open) but equity down 5% floating.
    ok, reason = rs.check(balance=1000.0, equity=950.0, now=DAY1)
    assert not ok
    assert "daily loss" in reason


def test_gatekeeper_kill_switch_blocks_and_notifies_once(tmp_path, monkeypatch) -> None:
    from helix_v3.execution.gatekeeper import MT5ExecutionGatekeeper

    gatekeeper = MT5ExecutionGatekeeper.__new__(MT5ExecutionGatekeeper)
    gatekeeper._active_orders = {}
    gatekeeper.journal = SimpleNamespace()
    gatekeeper.risk_state = _risk_state(tmp_path)
    gatekeeper._kill_notified_day = ""
    alerts: list = []
    gatekeeper.kill_switch_callback = alerts.append

    account = {"balance": 1000.0, "equity": 1000.0}
    monkeypatch.setattr(gatekeeper, "_get_account_balance", lambda: account["balance"])
    monkeypatch.setattr(gatekeeper, "_get_account_equity", lambda: account["equity"])

    assert gatekeeper.check_drawdown_limit() is True

    # Realized 5% loss — the old formula would have returned True here.
    account["balance"] = account["equity"] = 950.0
    assert gatekeeper.check_drawdown_limit() is False
    assert gatekeeper.check_drawdown_limit() is False

    # Alert fired exactly once per trading day
    assert len(alerts) == 1
    assert "KILL SWITCH" in alerts[0]
