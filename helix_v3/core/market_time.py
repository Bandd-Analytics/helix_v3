"""Canonical market time: broker-server-time conversion + ONE session definition.

THE PROBLEM THIS SOLVES (audit Tier 1.2): MT5 returns bar times stamped in the
BROKER's server clock. IC Markets runs GMT+2 in (northern) winter and GMT+3
while US daylight saving is active — chosen so the daily bar closes at New
York 17:00. The codebase labeled those stamps as UTC, so every session window
(the Asian range above all — the foundation of the MMM premise) was computed
2-3 hours off and silently shifted twice a year. Three contradictory session
definitions existed across quant_engine, sessions.py and mtf_analyzer.

Rules:
  - Convert server stamps to TRUE UTC at ingest (quant_engine.fetch_rates and
    backtest data_store both do this) — everything downstream is real UTC.
  - All session windows are defined HERE, in UTC, per MMM Book p.8. Import
    them; never redefine.

MT5 epoch fields (bar time, tick.time, position.time) are "Unix" seconds that
render as server wall time when interpreted as UTC. server↔UTC conversion is
therefore a plain offset shift, with the offset decided by New York DST.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

NY_TZ = ZoneInfo("America/New_York")

# ---------------------------------------------------------------------------
# Broker server clock (IC Markets: GMT+2, GMT+3 during US DST)
# ---------------------------------------------------------------------------


def server_offset_hours(dt_utc: datetime) -> int:
    """Broker server offset from UTC at the given moment.

    Decided by US DST (the broker tracks New York 17:00 close). The 2-3h
    ambiguity of evaluating DST on a server-stamped time is irrelevant except
    within hours of the switch itself.
    """
    if dt_utc.tzinfo is None:
        dt_utc = dt_utc.replace(tzinfo=timezone.utc)
    ny = dt_utc.astimezone(NY_TZ)
    return 3 if ny.dst() else 2


def server_stamp_to_utc(dt: datetime) -> datetime:
    """Convert a server-time-labeled datetime (tz-naive or mislabeled UTC) to true UTC."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt - timedelta(hours=server_offset_hours(dt))


def utc_to_server_stamp(dt_utc: datetime) -> datetime:
    """Inverse of server_stamp_to_utc (still labeled UTC, as MT5 does)."""
    if dt_utc.tzinfo is None:
        dt_utc = dt_utc.replace(tzinfo=timezone.utc)
    return dt_utc + timedelta(hours=server_offset_hours(dt_utc))


def server_epoch_to_utc(epoch: float) -> datetime:
    """MT5 epoch field (bar/tick/position time) -> true UTC datetime."""
    return server_stamp_to_utc(datetime.fromtimestamp(epoch, tz=timezone.utc))


def utc_now_server_epoch() -> int:
    """Current wall-clock time expressed as an MT5 server-stamped epoch.

    Use when comparing wall clock against MT5 epoch fields (position.time,
    tick.time) — those are server-stamped, so naive utcnow() is 2-3h off.
    """
    now = datetime.now(timezone.utc)
    return int(now.timestamp()) + server_offset_hours(now) * 3600


def server_index_to_utc(idx: pd.DatetimeIndex) -> pd.DatetimeIndex:
    """Convert an MT5 server-stamped (UTC-labeled) DatetimeIndex to true UTC.

    Vectorized; handles US-DST switches inside the range (each timestamp gets
    the offset in force at that moment).
    """
    if len(idx) == 0:
        return idx
    if idx.tz is None:
        idx = idx.tz_localize("UTC")
    ny = idx.tz_convert(NY_TZ)
    is_dst = pd.Index(ny.strftime("%z")) == "-0400"
    offsets = np.where(is_dst, 3, 2)
    return idx - pd.to_timedelta(offsets, unit="h")


# ---------------------------------------------------------------------------
# Session windows — MMM Book p.8, fixed GMT. Minutes from midnight UTC.
# ---------------------------------------------------------------------------

ASIA_START = 0 * 60 + 30       # 00:30
ASIA_END = 7 * 60 + 30         # 07:30
LONDON_START = 7 * 60 + 30     # 07:30
LONDON_END = 13 * 60 + 30      # 13:30
US_START = 13 * 60 + 30        # 13:30
US_END = 22 * 60               # 22:00
LONDON_GAP_START = 7 * 60      # 07:00 (changeover — stop hunts likely)
LONDON_GAP_END = 8 * 60        # 08:00
NY_GAP_START = 13 * 60         # 13:00 (changeover — NYC reversal)
NY_GAP_END = 14 * 60           # 14:00

# Trading day resets at 22:00 UTC (17:00 New York / 01:00 EAT)
DAY_RESET_MINUTES = 22 * 60


def asian_session_mask(idx: pd.DatetimeIndex) -> np.ndarray:
    """Boolean mask: bars inside the Asian accumulation window (true UTC index)."""
    hour_min = idx.hour * 60 + idx.minute
    return np.asarray((hour_min >= ASIA_START) & (hour_min < ASIA_END))


def session_name_at(dt_utc: datetime) -> str:
    """Scanner-facing session label for a true-UTC moment.

    Names preserved from the legacy market_scanner so close_before_session
    profiles, report scheduling and notification grouping keep working:
    ASIAN_EARLY, ASIAN_LATE, LONDON_PREMARKET, LONDON, NY_OVERLAP, NY_LATE.
    """
    if dt_utc.tzinfo is None:
        dt_utc = dt_utc.replace(tzinfo=timezone.utc)
    hour = dt_utc.astimezone(timezone.utc).hour
    if 21 <= hour or hour < 2:
        return "ASIAN_EARLY"
    if 2 <= hour < 7:
        return "ASIAN_LATE"
    if 7 <= hour < 8:
        return "LONDON_PREMARKET"
    if 8 <= hour < 12:
        return "LONDON"
    if 12 <= hour < 16:
        return "NY_OVERLAP"
    if 16 <= hour < 21:
        return "NY_LATE"
    return "UNKNOWN"


# MMM intraday phase hour boundaries (true UTC) — used by the MTF analyzer.
PHASE_ACCUMULATION = (1, 5)    # deep Asia
PHASE_STOP_HUNT = (5, 8)       # late Asia / London pre-open
PHASE_TRUE_TREND = (8, 13)     # London
PHASE_NYC_REVERSAL = (13, 17)  # NY overlap
# everything else: return to accumulation
