"""MMM Candlestick Pattern Detection — Context-Aware.

Per Steve Mauro: candlestick patterns are ONLY significant at the right location.
A hammer mid-trend is meaningless. A hammer at HOD/LOD is critical.

Patterns detected:
  1. Spike candles / Empire State (trap candles at L1/stop hunt)
  2. Spinning tops, hammers, inverted hammers
  3. Doji candles
  4. Evening star / Morning star (extended RRT, 45-min RRT on M15)
  5. Railroad Tracks (RRT) — compressed M/W
  6. High Test Pattern (reversal at previous day's high)
  7. Low Test Pattern (reversal at previous day's low)
  8. Pin bars (long wick rejections at key levels)
  9. Half Batman (one-sided M or W with continuation)

Trade types (per MMM book):
  - Straightaway Trade: breakout from Asian, no stop hunt
  - 2nd Leg M/W Setup: classic stop hunt reversal
  - The 33 Trade: 3 pushes in stop hunt zone
  - NYC Reversal: reversal at NY open
  - EMA 200 Bounce: reversal off 200 EMA
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

from helix_v3.utils.logger import get_logger

logger = get_logger("patterns")


class PatternType(Enum):
    SPIKE_CANDLE = "SPIKE_CANDLE"
    HAMMER = "HAMMER"
    INVERTED_HAMMER = "INVERTED_HAMMER"
    SPINNING_TOP = "SPINNING_TOP"
    DOJI = "DOJI"
    EVENING_STAR = "EVENING_STAR"
    MORNING_STAR = "MORNING_STAR"
    RRT = "RRT"
    HIGH_TEST = "HIGH_TEST"
    LOW_TEST = "LOW_TEST"
    PIN_BAR_BULL = "PIN_BAR_BULL"
    PIN_BAR_BEAR = "PIN_BAR_BEAR"
    HALF_BATMAN = "HALF_BATMAN"
    M_TOP = "M_TOP"
    W_BOTTOM = "W_BOTTOM"


class TradeType(Enum):
    STRAIGHTAWAY = "STRAIGHTAWAY"
    SECOND_LEG_MW = "SECOND_LEG_MW"
    THE_33 = "THE_33"
    NYC_REVERSAL = "NYC_REVERSAL"
    EMA_200_BOUNCE = "EMA_200_BOUNCE"
    SWING = "SWING"
    NONE = "NONE"


@dataclass
class DetectedPattern:
    pattern: PatternType
    bar_index: int          # Index in the DataFrame
    price: float            # Price level of pattern
    significance: float     # 0-1, how significant (context-dependent)
    notes: str = ""


@dataclass
class PatternScan:
    """Result of full pattern scan on a DataFrame."""
    patterns: List[DetectedPattern] = field(default_factory=list)
    trade_type: TradeType = TradeType.NONE
    rrt_count: int = 0
    spike_count: int = 0
    pin_bar_count: int = 0
    m_w_detected: bool = False
    half_batman: bool = False


def scan_patterns(
    df: pd.DataFrame,
    pip_size: float,
    prev_hod: Optional[float] = None,
    prev_lod: Optional[float] = None,
    asian_high: Optional[float] = None,
    asian_low: Optional[float] = None,
    ema_200: Optional[float] = None,
    session_hour_utc: int = 12,
) -> PatternScan:
    """Scan DataFrame for all MMM candlestick patterns.

    Context parameters (prev_hod, asian levels, etc.) enable
    location-aware pattern significance scoring.
    """
    result = PatternScan()
    if len(df) < 5:
        return result

    opens = df["Open"].values
    highs = df["High"].values
    lows = df["Low"].values
    closes = df["Close"].values

    for i in range(2, len(df)):
        o, h, l, c = opens[i], highs[i], lows[i], closes[i]
        body = abs(c - o)
        full_range = h - l
        if full_range < 1e-10:
            continue

        upper_wick = h - max(o, c)
        lower_wick = min(o, c) - l
        body_ratio = body / full_range
        upper_ratio = upper_wick / full_range
        lower_ratio = lower_wick / full_range

        price = c
        is_bullish = c > o

        # --- Spike / Empire State candle (Z-score based) ---
        # Uses statistical Z-score instead of hardcoded 2.5x multiplier.
        # Adapts to pair-specific volatility automatically.
        # Z >= 2.5 = extreme (spike), Z >= 1.5 = large (significant)
        lookback = min(20, i)
        if lookback >= 5:
            recent_bodies = np.array([abs(closes[j] - opens[j]) for j in range(i - lookback, i)])
            body_mean = np.mean(recent_bodies)
            body_std = np.std(recent_bodies)
            body_z = (body - body_mean) / body_std if body_std > 0 else 0

            # Also compute volume Z if volume data available
            vol_z = 0.0
            if "Volume" in df.columns or "tick_volume" in df.columns:
                vol_col = "Volume" if "Volume" in df.columns else "tick_volume"
                recent_vols = df[vol_col].values[i - lookback:i].astype(float)
                cur_vol = float(df[vol_col].values[i])
                vol_mean = np.mean(recent_vols)
                vol_std = np.std(recent_vols)
                vol_z = (cur_vol - vol_mean) / vol_std if vol_std > 0 else 0

            # Extreme: body Z >= 2.5 OR (body Z >= 1.5 AND volume Z >= 1.5)
            is_extreme = body_z >= 2.5 or (body_z >= 1.5 and vol_z >= 1.5)
            if is_extreme:
                sig = _context_significance(price, prev_hod, prev_lod, asian_high, asian_low)
                note = f"Spike candle — body Z={body_z:.1f} vol Z={vol_z:.1f}, MM trap"
                result.patterns.append(DetectedPattern(
                    PatternType.SPIKE_CANDLE, i, price, sig, note,
                ))
                result.spike_count += 1

        # --- Doji ---
        if body_ratio < 0.1 and full_range / pip_size > 3:
            sig = _context_significance(price, prev_hod, prev_lod, asian_high, asian_low)
            result.patterns.append(DetectedPattern(
                PatternType.DOJI, i, price, sig * 0.7,
                "Indecision — look for direction on next candle",
            ))

        # --- Spinning Top ---
        if 0.1 <= body_ratio <= 0.35 and upper_ratio > 0.2 and lower_ratio > 0.2:
            sig = _context_significance(price, prev_hod, prev_lod, asian_high, asian_low)
            result.patterns.append(DetectedPattern(
                PatternType.SPINNING_TOP, i, price, sig * 0.6,
            ))

        # --- Hammer (bullish reversal) ---
        if lower_ratio > 0.6 and upper_ratio < 0.1 and body_ratio < 0.35:
            sig = _context_significance(price, prev_hod, prev_lod, asian_high, asian_low)
            result.patterns.append(DetectedPattern(
                PatternType.HAMMER, i, price, sig,
                "Hammer — bullish reversal signal at lows",
            ))

        # --- Inverted Hammer (bearish reversal) ---
        if upper_ratio > 0.6 and lower_ratio < 0.1 and body_ratio < 0.35:
            sig = _context_significance(price, prev_hod, prev_lod, asian_high, asian_low)
            result.patterns.append(DetectedPattern(
                PatternType.INVERTED_HAMMER, i, price, sig,
                "Inverted hammer — bearish reversal signal at highs",
            ))

        # --- Pin Bar ---
        if lower_ratio > 0.65 and body_ratio < 0.25:
            sig = _context_significance(price, prev_hod, prev_lod, asian_high, asian_low)
            result.patterns.append(DetectedPattern(
                PatternType.PIN_BAR_BULL, i, price, sig,
                "Bullish pin bar — long lower wick rejection",
            ))
            result.pin_bar_count += 1
        elif upper_ratio > 0.65 and body_ratio < 0.25:
            sig = _context_significance(price, prev_hod, prev_lod, asian_high, asian_low)
            result.patterns.append(DetectedPattern(
                PatternType.PIN_BAR_BEAR, i, price, sig,
                "Bearish pin bar — long upper wick rejection",
            ))
            result.pin_bar_count += 1

    # --- RRT detection (consecutive opposing candles of similar size) ---
    for i in range(1, len(df)):
        b1_body = abs(closes[i - 1] - opens[i - 1])
        b2_body = abs(closes[i] - opens[i])
        b1_bull = closes[i - 1] > opens[i - 1]
        b2_bull = closes[i] > opens[i]

        if b1_bull != b2_bull and b1_body > 0 and b2_body > 0:
            ratio = min(b1_body, b2_body) / max(b1_body, b2_body)
            if ratio > 0.6:
                price = closes[i]
                sig = _context_significance(price, prev_hod, prev_lod, asian_high, asian_low)
                result.patterns.append(DetectedPattern(
                    PatternType.RRT, i, price, sig,
                    "Railroad Tracks — compressed M/W, expect reversal",
                ))
                result.rrt_count += 1

    # --- Evening Star / Morning Star (3-candle pattern) ---
    for i in range(2, len(df)):
        b1 = abs(closes[i - 2] - opens[i - 2])
        b2 = abs(closes[i - 1] - opens[i - 1])
        b3 = abs(closes[i] - opens[i])

        if b1 < 1e-10 or b3 < 1e-10:
            continue

        # Evening Star: big green, small body, big red
        if (closes[i - 2] > opens[i - 2] and  # green
                b2 < b1 * 0.4 and              # small middle
                closes[i] < opens[i] and        # red
                b3 > b1 * 0.5):                 # significant red
            sig = _context_significance(highs[i - 1], prev_hod, prev_lod, asian_high, asian_low)
            result.patterns.append(DetectedPattern(
                PatternType.EVENING_STAR, i, highs[i - 1], sig,
                "Evening Star — bearish reversal (extended 45-min RRT)",
            ))

        # Morning Star: big red, small body, big green
        if (closes[i - 2] < opens[i - 2] and  # red
                b2 < b1 * 0.4 and              # small middle
                closes[i] > opens[i] and        # green
                b3 > b1 * 0.5):                 # significant green
            sig = _context_significance(lows[i - 1], prev_hod, prev_lod, asian_high, asian_low)
            result.patterns.append(DetectedPattern(
                PatternType.MORNING_STAR, i, lows[i - 1], sig,
                "Morning Star — bullish reversal (extended 45-min RRT)",
            ))

    # --- High Test / Low Test (test of previous day's HOD/LOD) ---
    if prev_hod is not None:
        for i in range(len(df)):
            if abs(highs[i] - prev_hod) / pip_size < 10:
                # Price approached previous HOD
                if closes[i] < prev_hod:  # Closed below = rejection
                    result.patterns.append(DetectedPattern(
                        PatternType.HIGH_TEST, i, prev_hod, 0.9,
                        f"High Test — rejected at prev HOD {prev_hod:.5f}",
                    ))

    if prev_lod is not None:
        for i in range(len(df)):
            if abs(lows[i] - prev_lod) / pip_size < 10:
                if closes[i] > prev_lod:
                    result.patterns.append(DetectedPattern(
                        PatternType.LOW_TEST, i, prev_lod, 0.9,
                        f"Low Test — rejected at prev LOD {prev_lod:.5f}",
                    ))

    # --- M Top / W Bottom (over last 20 bars) ---
    if len(df) >= 12:
        last_20 = min(20, len(df))
        h_slice = highs[-last_20:]
        l_slice = lows[-last_20:]

        # M top: two peaks with valley between
        for i in range(2, len(h_slice) - 2):
            if h_slice[i] < h_slice[i - 2] and h_slice[i] < h_slice[i + 2]:
                peak_diff = abs(h_slice[i - 2] - h_slice[i + 2]) / pip_size
                if peak_diff < 20:
                    result.m_w_detected = True
                    result.patterns.append(DetectedPattern(
                        PatternType.M_TOP, len(df) - last_20 + i + 2,
                        float(max(h_slice[i - 2], h_slice[i + 2])), 0.85,
                        "M-Top — double peak reversal",
                    ))
                    break

        # W bottom
        for i in range(2, len(l_slice) - 2):
            if l_slice[i] > l_slice[i - 2] and l_slice[i] > l_slice[i + 2]:
                trough_diff = abs(l_slice[i - 2] - l_slice[i + 2]) / pip_size
                if trough_diff < 20:
                    result.m_w_detected = True
                    result.patterns.append(DetectedPattern(
                        PatternType.W_BOTTOM, len(df) - last_20 + i + 2,
                        float(min(l_slice[i - 2], l_slice[i + 2])), 0.85,
                        "W-Bottom — double trough reversal",
                    ))
                    break

    # --- Half Batman ---
    # One-sided M or W where only one side reverses (continuation pattern)
    if len(df) >= 10:
        recent_h = highs[-10:]
        recent_l = lows[-10:]
        # Half batman bullish: sharp drop, flat bottom, ramp up (like W but one side only)
        min_idx = np.argmin(recent_l)
        if 2 <= min_idx <= 7:
            left_drop = recent_h[0] - recent_l[min_idx]
            right_rise = recent_h[-1] - recent_l[min_idx]
            if right_rise > left_drop * 0.8 and left_drop / pip_size > 15:
                result.half_batman = True
                result.patterns.append(DetectedPattern(
                    PatternType.HALF_BATMAN, len(df) - 10 + min_idx,
                    float(recent_l[min_idx]), 0.75,
                    "Half Batman — one-sided reversal with continuation",
                ))

    # --- Determine Trade Type ---
    result.trade_type = _classify_trade_type(
        result, session_hour_utc, asian_high, asian_low, ema_200,
        closes[-1] if len(closes) > 0 else 0,
        pip_size,
    )

    return result


def _context_significance(
    price: float,
    prev_hod: Optional[float],
    prev_lod: Optional[float],
    asian_high: Optional[float],
    asian_low: Optional[float],
    tolerance_pct: float = 0.002,
) -> float:
    """Score pattern significance based on location context.

    Patterns at HOD/LOD/Asian boundaries are most significant (0.9-1.0).
    Patterns mid-range are low significance (0.2-0.4).
    """
    sig = 0.3  # base significance

    if prev_hod and abs(price - prev_hod) / prev_hod < tolerance_pct:
        sig = max(sig, 0.9)
    if prev_lod and abs(price - prev_lod) / prev_lod < tolerance_pct:
        sig = max(sig, 0.9)
    if asian_high and abs(price - asian_high) / asian_high < tolerance_pct:
        sig = max(sig, 0.8)
    if asian_low and abs(price - asian_low) / asian_low < tolerance_pct:
        sig = max(sig, 0.8)

    return sig


def _classify_trade_type(
    scan: PatternScan,
    session_hour_utc: int,
    asian_high: Optional[float],
    asian_low: Optional[float],
    ema_200: Optional[float],
    current_price: float,
    pip_size: float,
) -> TradeType:
    """Classify the current setup into an MMM trade type."""

    # 33 Trade: 3+ pushes in stop hunt zone
    if scan.rrt_count >= 2 or scan.pin_bar_count >= 3:
        return TradeType.THE_33

    # NYC Reversal: reversal patterns during NY session (13-17 UTC)
    if 13 <= session_hour_utc <= 17 and scan.m_w_detected:
        return TradeType.NYC_REVERSAL

    # EMA 200 Bounce
    if ema_200 and pip_size > 0:
        dist = abs(current_price - ema_200) / pip_size
        if dist < 15 and scan.pin_bar_count > 0:
            return TradeType.EMA_200_BOUNCE

    # 2nd Leg M/W
    if scan.m_w_detected:
        return TradeType.SECOND_LEG_MW

    # Straightaway: no stop hunt, direct breakout from Asian
    if asian_high and asian_low:
        ar = (asian_high - asian_low) / pip_size
        if ar < 30 and not scan.m_w_detected and scan.spike_count == 0:
            above = (current_price - asian_high) / pip_size
            below = (asian_low - current_price) / pip_size
            if above > 20 or below > 20:
                return TradeType.STRAIGHTAWAY

    return TradeType.NONE
