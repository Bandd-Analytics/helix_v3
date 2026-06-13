"""The single notifier interface (audit Tier 3.5).

Telegram is the PRIMARY backend — it has native photo upload, no
message limits, and has been the chart channel since WhatsApp went
text-only (Tier 0.8). WhatsApp remains as the fallback adapter when
Telegram isn't configured, or when forced via NOTIFICATION_BACKEND.

Both backends implement NotifierProtocol below. Orchestration code
must depend only on these methods — never on backend-specific extras.
All transport is fire-and-forget through notifications.dispatch
(Tier 3.2); a method returning True means "queued", not "delivered".

Note: the two backends keep their own message FORMATTING deliberately
— Telegram uses HTML + photo captions, WhatsApp is plain-text-only.
The shared surface is the interface, not the templates.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Protocol, runtime_checkable


@runtime_checkable
class NotifierProtocol(Protocol):
    """What the orchestrator, gatekeeper callbacks, and auto_scan rely on."""

    @property
    def enabled(self) -> bool: ...

    def _send(self, message: str, image_path: Optional[str] = None) -> bool: ...

    def send_with_chart(self, message: str, chart_path: str) -> bool: ...

    def notify_trade_setup(self, *args: Any, **kwargs: Any) -> bool: ...

    def notify_trade_entry(self, *args: Any, **kwargs: Any) -> bool: ...

    def notify_t1_hit(self, *args: Any, **kwargs: Any) -> bool: ...

    def notify_trade_exit(self, *args: Any, **kwargs: Any) -> bool: ...

    def notify_market_conditions(self, *args: Any, **kwargs: Any) -> bool: ...

    def notify_scanner_watchlist(self, report: str) -> bool: ...

    def notify_period_report(self, *args: Any, **kwargs: Any) -> bool: ...

    def notify_setup_with_chart(self, *args: Any, **kwargs: Any) -> bool: ...

    def notify_drawdown_warning(self, *args: Any, **kwargs: Any) -> bool: ...


def create_notifier() -> NotifierProtocol:
    """Backend selection: Telegram primary, WhatsApp adapter/fallback.

    NOTIFICATION_BACKEND=whatsapp forces the adapter; anything else
    (including unset) prefers Telegram when it is configured.
    """
    import os

    from helix_v3.notifications.telegram import TelegramNotifier
    from helix_v3.notifications.whatsapp import WhatsAppNotifier
    from helix_v3.utils.logger import get_logger

    logger = get_logger("notifications")
    backend = os.getenv("NOTIFICATION_BACKEND", "").lower()
    if backend == "whatsapp":
        return WhatsAppNotifier()

    notifier = TelegramNotifier()
    if notifier.enabled:
        return notifier
    logger.warning("Telegram not configured — falling back to WhatsApp adapter")
    return WhatsAppNotifier()
