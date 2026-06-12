"""Tests for the MT5 connection watchdog (audit Tier 3.1)."""
from __future__ import annotations

from helix_v3.execution.mt5_watchdog import (
    INITIAL_BACKOFF_SEC,
    MAX_BACKOFF_SEC,
    MT5Watchdog,
)


class _Clock:
    def __init__(self) -> None:
        self.t = 1000.0

    def __call__(self) -> float:
        return self.t

    def advance(self, sec: float) -> None:
        self.t += sec


def _watchdog(clock: _Clock, alerts: list, deadman_minutes: float = 5.0) -> MT5Watchdog:
    return MT5Watchdog(
        alert_callback=alerts.append,
        deadman_minutes=deadman_minutes,
        now_fn=clock,
    )


def test_deadman_alert_fires_once_per_outage() -> None:
    clock, alerts = _Clock(), []
    wd = _watchdog(clock, alerts)

    # Failures inside the dead-man window: no alert yet
    clock.advance(120)
    wd.record_failure("poll")
    assert alerts == []

    # Past 5 minutes: exactly one alert, repeated failures don't re-fire
    clock.advance(200)
    wd.record_failure("poll")
    wd.record_failure("poll")
    clock.advance(600)
    wd.record_failure("poll")
    assert len(alerts) == 1
    assert "DEAD-MAN" in alerts[0]
    assert wd.alerted is True


def test_recovery_resets_and_announces() -> None:
    clock, alerts = _Clock(), []
    wd = _watchdog(clock, alerts)

    clock.advance(400)
    wd.record_failure("poll")
    assert len(alerts) == 1

    wd.record_success()
    assert len(alerts) == 2
    assert "RECOVERED" in alerts[1]
    assert wd.alerted is False
    assert wd.seconds_down() == 0.0

    # A NEW outage alerts again
    clock.advance(400)
    wd.record_failure("poll")
    assert len(alerts) == 3
    assert "DEAD-MAN" in alerts[2]


def test_success_without_prior_alert_is_silent() -> None:
    clock, alerts = _Clock(), []
    wd = _watchdog(clock, alerts)
    wd.record_success()
    wd.record_success()
    assert alerts == []


def test_reconnect_backoff_gating() -> None:
    clock, alerts = _Clock(), []
    wd = _watchdog(clock, alerts)
    attempts = []
    wd._do_reconnect = lambda: attempts.append(clock.t) or False  # always fails

    assert wd.try_reconnect() is False
    assert len(attempts) == 1

    # Inside the (doubled) backoff window: no new attempt
    clock.advance(INITIAL_BACKOFF_SEC)
    wd.try_reconnect()
    assert len(attempts) == 1

    # Past it: attempt #2, backoff doubles again
    clock.advance(INITIAL_BACKOFF_SEC * 2)
    wd.try_reconnect()
    assert len(attempts) == 2

    # Backoff never exceeds the cap
    for _ in range(20):
        clock.advance(MAX_BACKOFF_SEC)
        wd.try_reconnect()
    assert wd._backoff == MAX_BACKOFF_SEC


def test_reconnect_success_resets_backoff_and_recovers() -> None:
    clock, alerts = _Clock(), []
    wd = _watchdog(clock, alerts)

    clock.advance(400)
    wd.record_failure("poll")  # dead-man fired
    assert len(alerts) == 1

    wd._do_reconnect = lambda: True
    clock.advance(MAX_BACKOFF_SEC)
    assert wd.try_reconnect() is True
    assert wd._backoff == INITIAL_BACKOFF_SEC
    assert wd.seconds_down() == 0.0
    assert len(alerts) == 2 and "RECOVERED" in alerts[1]


def test_alert_callback_failure_does_not_raise() -> None:
    clock = _Clock()

    def _boom(msg: str) -> None:
        raise RuntimeError("notifier down")

    wd = MT5Watchdog(alert_callback=_boom, deadman_minutes=5.0, now_fn=clock)
    clock.advance(400)
    wd.record_failure("poll")  # must not raise
    assert wd.alerted is True
