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

from dataclasses import dataclass, field
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

# Session-open "box" windows (first volatile push after open)
# Matches Pine: London 07:30-08:45, NY 13:30-14:45 (75 minutes / 5 M15 bars)
LONDON_BOX_START = LONDON_START
LONDON_BOX_END = LONDON_START + 75       # 08:45
NY_BOX_START = US_START
NY_BOX_END = US_START + 75               # 14:45

# Rolling window for average Asian range
ASIAN_AVG_WINDOW = 20

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
    # London open box: first 75 min of London session, per date
    london_open_boxes: Dict[str, dict] = field(default_factory=dict)
    # NY open box: first 75 min of US session, per date
    ny_open_boxes: Dict[str, dict] = field(default_factory=dict)
    # Gann 0/0.5/1 segments: frozen Asian H/Mid/L extending from Asian end to next Asian start
    gann_segments: List[dict] = field(default_factory=list)
    # Rolling 20-session average Asian range in pips
    asian_avg_pips: float = 0.0


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
            low = float(group["Low"].min())
            mid = (h + low) / 2.0
            pips = (h - low) / pip_size
            asian_ranges[date_str] = {
                "high": h, "low": low, "mid": mid, "pips": pips,
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

    # --- London open box (first 75 min of London) and NY open box (first 75 min of NYC) ---
    london_open_boxes = _build_open_boxes(
        df, hour_min, LONDON_BOX_START, LONDON_BOX_END, pip_size
    )
    ny_open_boxes = _build_open_boxes(
        df, hour_min, NY_BOX_START, NY_BOX_END, pip_size
    )

    # --- Gann segments: each Asian range carries forward until the next Asian session ---
    gann_segments: List[dict] = []
    dates_sorted = sorted(asian_ranges.keys())
    for i, dstr in enumerate(dates_sorted):
        ar = asian_ranges[dstr]
        seg_start = ar["end_idx"]
        if i + 1 < len(dates_sorted):
            seg_end = asian_ranges[dates_sorted[i + 1]]["start_idx"]
        else:
            seg_end = len(df) - 1
        if seg_end <= seg_start:
            continue
        gann_segments.append({
            "date": dstr,
            "start_idx": seg_start,
            "end_idx": seg_end,
            "low": ar["low"],
            "mid": ar["mid"],
            "high": ar["high"],
        })

    # --- Rolling 20-session average Asian range (pips) ---
    if dates_sorted:
        recent_pips = [asian_ranges[d]["pips"] for d in dates_sorted[-ASIAN_AVG_WINDOW:]]
        asian_avg_pips = float(sum(recent_pips) / len(recent_pips))
    else:
        asian_avg_pips = 0.0

    return SessionInfo(
        labels=label_series,
        asian_ranges=asian_ranges,
        session_boundaries=boundaries,
        day_labels=day_labels_list,
        weekly_open_range=weekly_open,
        london_open_boxes=london_open_boxes,
        ny_open_boxes=ny_open_boxes,
        gann_segments=gann_segments,
        asian_avg_pips=asian_avg_pips,
    )


def _build_open_boxes(
    df: pd.DataFrame,
    hour_min: np.ndarray,
    box_start: int,
    box_end: int,
    pip_size: float,
) -> Dict[str, dict]:
    """Return per-date opening-range box: H/L of bars within [box_start, box_end) GMT minutes."""
    mask = (hour_min >= box_start) & (hour_min < box_end)
    sub = df[mask]
    out: Dict[str, dict] = {}
    if sub.empty:
        return out
    for date, group in sub.groupby(sub.index.date):
        h = float(group["High"].max())
        low = float(group["Low"].min())
        out[str(date)] = {
            "high": h,
            "low": low,
            "mid": (h + low) / 2.0,
            "pips": (h - low) / pip_size,
            "start_idx": df.index.get_loc(group.index[0]),
            "end_idx": df.index.get_loc(group.index[-1]),
        }
    return out


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
