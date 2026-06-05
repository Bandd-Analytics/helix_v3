"""MMM Session Classification and Asian Range Calculator.

Ported from V2 sm_worktime with Helix V3 adaptations.

Session boundaries (GMT per MMM Book p. 8):
    Dead Gap:    17:00-20:30 ET (22:00-01:30 GMT)
    Asia:        00:30-07:30 GMT
    London Gap:  07:00-08:00 GMT (changeover zone — stop hunts likely)
    London:      07:30-13:30 GMT
    NY Gap:      13:00-14:00 GMT (changeover zone — NYC reversal)
    US/NYC:      13:30-22:00 GMT

Trading day resets at 17:00 ET (22:00 GMT / 01:00 EAT).

Key outputs:
  - Per-bar session labels (ASIA, LONDON, US, LONDON_GAP, NY_GAP, OFFHOURS)
  - Per-day Asian range (high, low, mid, pips) — date-precise
  - Session boundary indices for chart vertical separators
  - Day-of-week labels at session transitions
  - Weekly open range (first 4 hours of new trading week)
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd


# Session boundaries in minutes-from-midnight GMT
ASIA_START = 0 * 60 + 30       # 00:30
ASIA_END = 7 * 60 + 30         # 07:30
LONDON_START = 7 * 60 + 30     # 07:30
LONDON_END = 13 * 60 + 30      # 13:30
US_START = 13 * 60 + 30        # 13:30
US_END = 22 * 60 + 0           # 22:00
LONDON_GAP_START = 7 * 60 + 0  # 07:00
LONDON_GAP_END = 8 * 60 + 0    # 08:00
NY_GAP_START = 13 * 60 + 0     # 13:00
NY_GAP_END = 14 * 60 + 0       # 14:00

# Trading day reset at 22:00 GMT (17:00 ET)
DAY_RESET_MINUTES = 22 * 60


@dataclass
class SessionInfo:
    """Session classification result for a DataFrame."""
    labels: pd.Series                    # Per-bar: ASIA/LONDON/US/LONDON_GAP/NY_GAP/OFFHOURS
    asian_ranges: Dict[str, dict]        # Per-date: {date_str: {high, low, mid, pips}}
    session_boundaries: List[Tuple[int, str]]  # (bar_index, label) for vertical separators
    day_labels: List[Tuple[int, str]]    # (bar_index, "Monday") for day markers
    weekly_open_range: Optional[dict]    # {high, low, mid, pips} for first 4h of week


def classify_sessions(df: pd.DataFrame, pip_size: float = 0.0001) -> SessionInfo:
    """Classify each bar into MMM sessions and compute per-day Asian ranges.

    Args:
        df: OHLCV DataFrame with UTC DatetimeIndex.
        pip_size: For pip calculation (0.0001 for most, 0.01 for JPY, 0.1 for XAUUSD).

    Returns:
        SessionInfo with labels, Asian ranges, boundaries, and day labels.
    """
    ts = df.index
    hour_min = ts.hour * 60 + ts.minute

    # Classify sessions
    labels = np.full(len(df), "OFFHOURS", dtype=object)
    labels[(hour_min >= ASIA_START) & (hour_min < ASIA_END)] = "ASIA"
    labels[(hour_min >= LONDON_START) & (hour_min < LONDON_END)] = "LONDON"
    labels[(hour_min >= US_START) & (hour_min < US_END)] = "US"
    # Gaps overwrite (changeover zones are analytically important)
    labels[(hour_min >= LONDON_GAP_START) & (hour_min < LONDON_GAP_END)] = "LONDON_GAP"
    labels[(hour_min >= NY_GAP_START) & (hour_min < NY_GAP_END)] = "NY_GAP"

    label_series = pd.Series(labels, index=ts)

    # --- Per-day Asian range (date-precise) ---
    # Trading day: group by date, but Asian session spans midnight
    # Use the date of the Asian END (07:30 bar's date) as the trading day
    asian_mask = (hour_min >= ASIA_START) & (hour_min < ASIA_END)
    asian_bars = df[asian_mask]

    asian_ranges = {}
    if not asian_bars.empty:
        # Group by calendar date
        for date, group in asian_bars.groupby(asian_bars.index.date):
            date_str = str(date)
            h = float(group["High"].max())
            l = float(group["Low"].min())
            mid = (h + l) / 2.0
            pips = (h - l) / pip_size
            asian_ranges[date_str] = {
                "high": h, "low": l, "mid": mid, "pips": pips,
                "start_idx": df.index.get_loc(group.index[0]),
                "end_idx": df.index.get_loc(group.index[-1]),
            }

    # --- Session boundary indices for chart separators ---
    boundaries = []
    prev_label = labels[0]
    for i in range(1, len(labels)):
        if labels[i] != prev_label:
            # Only mark major transitions
            if (prev_label, labels[i]) in [
                ("ASIA", "LONDON_GAP"), ("ASIA", "LONDON"),
                ("LONDON", "NY_GAP"), ("LONDON", "US"),
                ("LONDON_GAP", "LONDON"),
                ("NY_GAP", "US"),
                ("US", "OFFHOURS"), ("OFFHOURS", "ASIA"),
            ]:
                boundaries.append((i, labels[i]))
            prev_label = labels[i]

    # --- Day-of-week labels at day transitions ---
    day_labels_list = []
    prev_date = None
    for i, t in enumerate(ts):
        curr_date = t.date()
        if curr_date != prev_date:
            day_name = t.strftime("%A")
            day_labels_list.append((i, day_name))
            prev_date = curr_date

    # --- Weekly open range (first 4 hours of new trading week) ---
    weekly_open = None
    for i, t in enumerate(ts):
        # New week starts Sunday evening / Monday early
        if t.weekday() == 0 and t.hour < 4:
            # Collect first 4 hours (16 M15 bars)
            end_i = min(i + 16, len(df))
            week_start = df.iloc[i:end_i]
            if len(week_start) > 0:
                wh = float(week_start["High"].max())
                wl = float(week_start["Low"].min())
                weekly_open = {
                    "high": wh, "low": wl, "mid": (wh + wl) / 2.0,
                    "pips": (wh - wl) / pip_size,
                    "start_idx": i, "end_idx": end_i - 1,
                }
            break  # Only need the most recent Monday

    # If no Monday in the data, try to find any week start
    if weekly_open is None:
        mondays = [i for i, t in enumerate(ts) if t.weekday() == 0]
        if mondays:
            m_idx = mondays[-1]  # Most recent Monday
            end_i = min(m_idx + 16, len(df))
            week_start = df.iloc[m_idx:end_i]
            if len(week_start) > 0:
                wh = float(week_start["High"].max())
                wl = float(week_start["Low"].min())
                weekly_open = {
                    "high": wh, "low": wl, "mid": (wh + wl) / 2.0,
                    "pips": (wh - wl) / pip_size,
                    "start_idx": m_idx, "end_idx": end_i - 1,
                }

    return SessionInfo(
        labels=label_series,
        asian_ranges=asian_ranges,
        session_boundaries=boundaries,
        day_labels=day_labels_list,
        weekly_open_range=weekly_open,
    )


def get_today_asian_range(session_info: SessionInfo, df: pd.DataFrame) -> Optional[dict]:
    """Get the Asian range for the most recent trading day."""
    if not session_info.asian_ranges:
        return None
    # Get the latest date
    latest_date = max(session_info.asian_ranges.keys())
    return session_info.asian_ranges[latest_date]


def get_prev_day_hod_lod(df_d1: pd.DataFrame) -> Tuple[float, float, float, float]:
    """Get previous and current day HOD/LOD from daily bars.

    Returns: (prev_hod, prev_lod, current_hod, current_lod)
    """
    if len(df_d1) < 2:
        return 0, 0, 0, 0
    prev = df_d1.iloc[-2]
    curr = df_d1.iloc[-1]
    return (
        float(prev["High"]), float(prev["Low"]),
        float(curr["High"]), float(curr["Low"]),
    )
