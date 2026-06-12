"""MT5 connection watchdog (audit Tier 3.1).

A dead terminal must never look like a quiet market. `positions_get()
-> None` used to silently become "no positions" — position management
went blind with open trades on the book and nobody was told.

The watchdog:
- tracks the last SUCCESSFUL broker poll (monotonic clock),
- reconnects with exponential backoff (5s doubling to 5min),
- fires a dead-man alert through the notifier ONCE per outage when no
  poll has succeeded for MT5_DEADMAN_MIN minutes (default 5),
- announces recovery once the connection returns.

Time is injectable for tests; the actual MT5 reconnect lives in
`_do_reconnect` so the policy logic is testable without a terminal.
"""
from __future__ import annotations

import time
from typing import Callable, Optional

from config.settings import settings
from helix_v3.utils.logger import get_logger

logger = get_logger("mt5_watchdog")

INITIAL_BACKOFF_SEC = 5.0
MAX_BACKOFF_SEC = 300.0


class MT5Watchdog:
    def __init__(
        self,
        alert_callback: Optional[Callable[[str], None]] = None,
        deadman_minutes: Optional[float] = None,
        now_fn: Callable[[], float] = time.monotonic,
    ) -> None:
        self.alert_callback = alert_callback
        self._now = now_fn
        self._deadman_sec = 60.0 * (
            deadman_minutes
            if deadman_minutes is not None
            else settings.mt5.deadman_minutes
        )
        self._last_success = self._now()
        self._last_attempt = -MAX_BACKOFF_SEC
        self._backoff = INITIAL_BACKOFF_SEC
        self._alerted = False

    # -- state ----------------------------------------------------------

    def seconds_down(self) -> float:
        return self._now() - self._last_success

    @property
    def alerted(self) -> bool:
        return self._alerted

    def record_success(self) -> None:
        """A broker call returned real data — connection is alive."""
        if self._alerted:
            msg = (
                f"HELIX V3 MT5 RECOVERED\n{'=' * 25}\n"
                f"Broker connection restored after "
                f"{self.seconds_down() / 60:.0f} min down."
            )
            logger.warning("MT5 RECOVERED after %.0f min down", self.seconds_down() / 60)
            self._send_alert(msg)
        self._last_success = self._now()
        self._backoff = INITIAL_BACKOFF_SEC
        self._alerted = False

    def record_failure(self, context: str = "") -> None:
        """A broker call returned None/raised — check the dead-man timer."""
        down_min = self.seconds_down() / 60
        logger.error(
            "MT5 poll failure (%s) — %.1f min since last success", context, down_min
        )
        if self.seconds_down() >= self._deadman_sec and not self._alerted:
            self._alerted = True
            msg = (
                f"HELIX V3 MT5 DEAD-MAN ALERT\n{'=' * 25}\n"
                f"No successful broker poll in {down_min:.0f} min "
                f"(last failure: {context or 'unknown'}).\n"
                f"Position management is BLIND — open positions are "
                f"unmanaged until the terminal returns."
            )
            logger.critical(
                "MT5 DEAD-MAN: no successful poll in %.0f min (%s)", down_min, context
            )
            self._send_alert(msg)

    def _send_alert(self, msg: str) -> None:
        if self.alert_callback is None:
            return
        try:
            self.alert_callback(msg)
        except Exception as e:
            logger.error("Watchdog alert delivery failed: %s", e)

    # -- polling / reconnect ---------------------------------------------

    def poll(self) -> bool:
        """One health check (account_info). Reconnects on failure."""
        try:
            import MetaTrader5 as mt5

            healthy = mt5.account_info() is not None
        except Exception as e:
            logger.error("MT5 health poll raised: %s", e)
            healthy = False

        if healthy:
            self.record_success()
            return True

        self.record_failure("account_info poll")
        self.try_reconnect()
        return False

    def try_reconnect(self) -> bool:
        """Reconnect attempt, rate-limited by exponential backoff."""
        now = self._now()
        if now - self._last_attempt < self._backoff:
            return False
        self._last_attempt = now
        backoff_used = self._backoff
        self._backoff = min(self._backoff * 2.0, MAX_BACKOFF_SEC)

        logger.warning(
            "MT5 reconnect attempt (next retry in %.0fs if this fails)", self._backoff
        )
        if self._do_reconnect():
            logger.info("MT5 reconnect succeeded (after %.0fs backoff)", backoff_used)
            self.record_success()
            return True
        return False

    def _do_reconnect(self) -> bool:
        """The actual MT5 teardown + initialize (overridable in tests)."""
        try:
            import MetaTrader5 as mt5

            mt5.shutdown()
            mt5_cfg = settings.mt5
            init_kwargs: dict = {}
            if mt5_cfg.path:
                init_kwargs["path"] = mt5_cfg.path
            if mt5_cfg.login:
                init_kwargs["login"] = mt5_cfg.login
                init_kwargs["password"] = mt5_cfg.password
                init_kwargs["server"] = mt5_cfg.server
            if not mt5.initialize(**init_kwargs):
                logger.error("MT5 re-initialize failed: %s", mt5.last_error())
                return False
            return mt5.account_info() is not None
        except Exception as e:
            logger.error("MT5 reconnect raised: %s", e)
            return False
