"""Fire-and-forget notification dispatch (audit Tier 3.2).

Notification HTTP (Twilio/Telegram, 30s timeouts) used to run
synchronously inside the trade path — a slow notifier delayed SL
management. All transport sends now go through a single-worker thread
pool: one worker keeps messages in order, the caller returns
immediately, and failures are logged in the worker instead of raised
into the trade path.
"""
from __future__ import annotations

from concurrent.futures import Future, ThreadPoolExecutor
from typing import Callable, Optional

from helix_v3.utils.logger import get_logger

logger = get_logger("notify_dispatch")

# One worker = strict FIFO across all notifiers; sends never interleave.
_executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="notify")


def fire_and_forget(
    fn: Callable, *args, description: str = "notification", **kwargs
) -> Optional[Future]:
    """Queue `fn(*args, **kwargs)` on the notify worker; never raises.

    Returns the Future (mainly for tests), or None if the executor is
    already shut down (interpreter exit).
    """

    def _run():
        try:
            fn(*args, **kwargs)
        except Exception as e:
            logger.error("Background %s failed: %s", description, e)

    try:
        return _executor.submit(_run)
    except RuntimeError:
        # Interpreter shutting down — drop the message rather than crash.
        logger.warning("Notify executor closed — dropped %s", description)
        return None
