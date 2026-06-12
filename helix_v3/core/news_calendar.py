"""High-impact news blackout (audit Tier 2.5).

A stop-hunt strategy trading through NFP/CPI/central-bank releases is the
hunted. This module answers one question: is `symbol` inside the +/-N
minute window of a high-impact event on one of its currencies?

Source: ForexFactory's free weekly calendar JSON (no API key). Fetched
lazily, cached to disk; scheduled events don't move, so a stale cache of
the current week is still valid — only a missing/expired-week cache
degrades to fail-open (with a loud warning). The decision logic is pure
and injectable for tests and for backtest replay from a CSV.
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import List, Optional

from config.settings import settings
from helix_v3.utils.logger import get_logger

logger = get_logger("news_calendar")

FF_CALENDAR_URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"
CACHE_PATH = Path(settings.log_dir) / "news_calendar_cache.json"
FETCH_TTL_SEC = 6 * 3600          # re-fetch at most every 6h
HIGH_IMPACT = "High"

# Currencies whose events matter per instrument. FX pairs derive from the
# symbol; metals and US indices are USD instruments.
_SPECIAL_SYMBOLS = {
    "XAUUSD": {"USD"},
    "XAGUSD": {"USD"},
    "US30": {"USD"},
    "USTEC": {"USD"},
    "US500": {"USD"},
}
_KNOWN_CCY = {"USD", "EUR", "GBP", "JPY", "AUD", "NZD", "CAD", "CHF", "CNY"}


def symbol_currencies(symbol: str) -> set:
    """Currencies whose high-impact events block this instrument."""
    if symbol in _SPECIAL_SYMBOLS:
        return set(_SPECIAL_SYMBOLS[symbol])
    base, quote = symbol[:3].upper(), symbol[3:6].upper()
    return {c for c in (base, quote) if c in _KNOWN_CCY}


@dataclass(frozen=True)
class NewsEvent:
    time_utc: datetime
    currency: str
    title: str
    impact: str


def _parse_ff_events(raw: list) -> List[NewsEvent]:
    events = []
    for item in raw:
        try:
            dt = datetime.fromisoformat(str(item["date"]))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            events.append(NewsEvent(
                time_utc=dt.astimezone(timezone.utc),
                currency=str(item.get("country", "")).upper(),
                title=str(item.get("title", "")),
                impact=str(item.get("impact", "")),
            ))
        except (KeyError, ValueError, TypeError):
            continue
    return events


class NewsCalendar:
    """Blackout decisions over a high-impact event list.

    Pass `events` explicitly for tests/backtest replay; otherwise events
    come from the ForexFactory weekly feed via a disk cache.
    """

    def __init__(
        self,
        events: Optional[List[NewsEvent]] = None,
        blackout_minutes: Optional[int] = None,
    ) -> None:
        self._injected = events is not None
        self._events: List[NewsEvent] = events or []
        self._last_fetch: float = 0.0
        self.blackout_minutes = (
            blackout_minutes
            if blackout_minutes is not None
            else settings.risk.news_blackout_minutes
        )

    # -- feed ---------------------------------------------------------

    def _refresh(self) -> None:
        if self._injected or time.monotonic() - self._last_fetch < FETCH_TTL_SEC and self._events:
            return
        fetched = self._fetch_feed()
        if fetched is not None:
            self._events = fetched
            self._last_fetch = time.monotonic()
            self._save_cache(fetched)
            return
        cached = self._load_cache()
        if cached is not None:
            # Scheduled events don't move — a stale current-week cache beats nothing.
            self._events = cached
            self._last_fetch = time.monotonic()
            logger.warning("News feed unavailable — using cached calendar (%d events)", len(cached))
        else:
            self._last_fetch = time.monotonic()  # don't hammer a dead feed
            logger.warning(
                "News feed unavailable and no cache — blackout DISABLED until feed returns"
            )

    def _fetch_feed(self) -> Optional[List[NewsEvent]]:
        try:
            import httpx

            resp = httpx.get(FF_CALENDAR_URL, timeout=10.0, follow_redirects=True)
            resp.raise_for_status()
            return _parse_ff_events(resp.json())
        except Exception as e:
            logger.warning("News calendar fetch failed: %s", e)
            return None

    def _save_cache(self, events: List[NewsEvent]) -> None:
        try:
            CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
            CACHE_PATH.write_text(json.dumps([
                {
                    "date": e.time_utc.isoformat(),
                    "country": e.currency,
                    "title": e.title,
                    "impact": e.impact,
                }
                for e in events
            ]), encoding="utf-8")
        except OSError as e:
            logger.warning("News cache write failed: %s", e)

    def _load_cache(self) -> Optional[List[NewsEvent]]:
        try:
            if not CACHE_PATH.exists():
                return None
            return _parse_ff_events(json.loads(CACHE_PATH.read_text(encoding="utf-8")))
        except (OSError, ValueError) as e:
            logger.warning("News cache read failed: %s", e)
            return None

    # -- decisions ----------------------------------------------------

    def blackout(self, symbol: str, at_utc: Optional[datetime] = None) -> Optional[NewsEvent]:
        """The high-impact event putting `symbol` in blackout at `at_utc`, if any."""
        if not settings.risk.news_blackout_enabled and not self._injected:
            return None
        self._refresh()
        if not self._events:
            return None

        at = at_utc or datetime.now(timezone.utc)
        if at.tzinfo is None:
            at = at.replace(tzinfo=timezone.utc)
        window = timedelta(minutes=self.blackout_minutes)
        currencies = symbol_currencies(symbol)

        for ev in self._events:
            if ev.impact != HIGH_IMPACT or ev.currency not in currencies:
                continue
            if abs(ev.time_utc - at) <= window:
                return ev
        return None


_singleton: Optional[NewsCalendar] = None


def get_news_calendar() -> NewsCalendar:
    """Shared live calendar (one feed cache per process)."""
    global _singleton
    if _singleton is None:
        _singleton = NewsCalendar()
    return _singleton
