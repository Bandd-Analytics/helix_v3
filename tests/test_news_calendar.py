"""Tests for the high-impact news blackout (audit Tier 2.5)."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from helix_v3.core.news_calendar import (
    HIGH_IMPACT,
    NewsCalendar,
    NewsEvent,
    _parse_ff_events,
    symbol_currencies,
)

NFP = NewsEvent(
    time_utc=datetime(2026, 6, 5, 12, 30, tzinfo=timezone.utc),
    currency="USD",
    title="Non-Farm Employment Change",
    impact=HIGH_IMPACT,
)
BOE = NewsEvent(
    time_utc=datetime(2026, 6, 5, 11, 0, tzinfo=timezone.utc),
    currency="GBP",
    title="Official Bank Rate",
    impact=HIGH_IMPACT,
)
LOW_USD = NewsEvent(
    time_utc=datetime(2026, 6, 5, 12, 30, tzinfo=timezone.utc),
    currency="USD",
    title="Some Minor Print",
    impact="Low",
)


def _cal(events) -> NewsCalendar:
    return NewsCalendar(events=events, blackout_minutes=30)


def test_symbol_currencies() -> None:
    assert symbol_currencies("EURUSD") == {"EUR", "USD"}
    assert symbol_currencies("GBPJPY") == {"GBP", "JPY"}
    assert symbol_currencies("XAUUSD") == {"USD"}
    assert symbol_currencies("US30") == {"USD"}


def test_blackout_window_edges() -> None:
    cal = _cal([NFP])
    t = NFP.time_utc
    assert cal.blackout("EURUSD", t) is NFP
    assert cal.blackout("EURUSD", t - timedelta(minutes=30)) is NFP   # window opens
    assert cal.blackout("EURUSD", t + timedelta(minutes=30)) is NFP   # window closes
    assert cal.blackout("EURUSD", t - timedelta(minutes=31)) is None
    assert cal.blackout("EURUSD", t + timedelta(minutes=31)) is None


def test_currency_relevance() -> None:
    cal = _cal([NFP, BOE])
    at = datetime(2026, 6, 5, 12, 30, tzinfo=timezone.utc)
    # USD event blocks USD pairs and gold, not EURGBP
    assert cal.blackout("EURUSD", at) is NFP
    assert cal.blackout("XAUUSD", at) is NFP
    assert cal.blackout("EURGBP", at) is None
    # BOE blocks GBP pairs at 11:00
    at_boe = datetime(2026, 6, 5, 11, 10, tzinfo=timezone.utc)
    assert cal.blackout("GBPJPY", at_boe) is BOE
    assert cal.blackout("EURUSD", at_boe) is None


def test_low_impact_ignored() -> None:
    cal = _cal([LOW_USD])
    assert cal.blackout("EURUSD", LOW_USD.time_utc) is None


def test_injected_calendar_ignores_enabled_flag() -> None:
    # Injected events (tests/backtest) always evaluate — the env toggle
    # only governs the live feed path.
    cal = _cal([NFP])
    assert cal.blackout("USDJPY", NFP.time_utc) is NFP


def test_parse_ff_events_format() -> None:
    raw = [
        {
            "title": "CPI y/y",
            "country": "USD",
            "date": "2026-06-10T08:30:00-04:00",
            "impact": "High",
        },
        {"title": "broken", "country": "EUR"},  # missing date -> skipped
    ]
    events = _parse_ff_events(raw)
    assert len(events) == 1
    assert events[0].time_utc == datetime(2026, 6, 10, 12, 30, tzinfo=timezone.utc)
    assert events[0].currency == "USD"
    assert events[0].impact == HIGH_IMPACT
