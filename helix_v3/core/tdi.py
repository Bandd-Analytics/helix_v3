"""Traders Dynamic Index (TDI) — V2-Verified MMM Implementation.

Ported from core-helix V2/v3_intelligence/sm_indicators/tdi.py with
V3-specific signal detection layered on top.

VERIFIED PARAMETERS (2026-04-27 — from MT4 Inputs dialog screenshot):
  - RSI period = 21 (NOT 13 as originally claimed in MMM book body)
  - RSI Price Line (Green) = 2-period SMA of RSI
  - Trade Signal Line (Red) = 7-period SMA of RSI
  - Market Base Line (Yellow) = 34-period SMA of RSI
  - Volatility Bands = Bollinger(34, 1.6185) on RSI
  - Shark Fin levels = 63/37 (NOT 68/32)
  - VB threshold lines = 45 (high) / 55 (low)

All smoothing uses SMA (rolling mean), NOT EMA — matching MT4/MT5 iRSI() output.
RSI uses Wilder's smoothing: ewm(alpha=1/period, adjust=False).

Signal types:
  - SIGNAL_CROSS: RSI Price Line crosses Trade Signal Line
  - MBL_CROSS (Blood in the Water): RSI Price Line crosses Market Base Line
  - HOOK: RSI re-enters VB from extreme (counter-trend)
  - SHARK_FIN: RSI breaks VB then re-enters (stop hunt confirmation)
  - VB_SQUEEZE: Tight bands = Asian consolidation
  - DIVERGENCE: Price vs RSI divergence

Also includes: pivot calculator, ADR (Wilder ATR), NewHUD dashboard,
crossover arrows, daily HiLo.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

from helix_v3.utils.logger import get_logger

logger = get_logger("tdi")


# =====================================================================
# TDI Signal Types
# =====================================================================

class TDISignal(Enum):
    SIGNAL_CROSS_BULLISH = "SIGNAL_CROSS_BULLISH"
    SIGNAL_CROSS_BEARISH = "SIGNAL_CROSS_BEARISH"
    MBL_CROSS_BULLISH = "MBL_CROSS_BULLISH"      # Blood in the Water — BUY
    MBL_CROSS_BEARISH = "MBL_CROSS_BEARISH"      # Blood in the Water — SELL
    HOOK_BULLISH = "HOOK_BULLISH"
    HOOK_BEARISH = "HOOK_BEARISH"
    SHARK_FIN_SHORT = "SHARK_FIN_SHORT"
    SHARK_FIN_LONG = "SHARK_FIN_LONG"
    RSI_OVERBOUGHT = "RSI_OVERBOUGHT"
    RSI_OVERSOLD = "RSI_OVERSOLD"
    VB_SQUEEZE = "VB_SQUEEZE"
    BULLISH_DIVERGENCE = "BULLISH_DIVERGENCE"
    BEARISH_DIVERGENCE = "BEARISH_DIVERGENCE"
    NONE = "NONE"


# =====================================================================
# TDI Parameters — V2-Verified 2026-04-27
# =====================================================================

RSI_PERIOD = 21              # VERIFIED (was 13 — CORRECTED)
RSI_PRICE_LINE = 2           # Green: 2-period SMA of RSI
TRADE_SIGNAL_LINE = 7        # Red: 7-period SMA of RSI (was 2 — CORRECTED)
MARKET_BASE_LINE = 34        # Yellow: 34-period SMA of RSI
VB_PERIOD = 34               # Bollinger period on RSI
VB_STD = 1.6185              # Bollinger std dev multiplier
SHARK_FIN_UPPER = 63.0       # VERIFIED (was 68 — CORRECTED)
SHARK_FIN_LOWER = 37.0       # VERIFIED (was 32 — CORRECTED)
VB_HIGH_THRESHOLD = 45.0     # NEW — VB high display line
VB_LOW_THRESHOLD = 55.0      # NEW — VB low display line
VB_SQUEEZE_THRESHOLD = 12.0  # VB width below this = squeeze/consolidation


# =====================================================================
# TDI Result
# =====================================================================

@dataclass
class TDIResult:
    """Full TDI computation result."""
    # Raw lines (full series for chart plotting)
    rsi_line: pd.Series          # Green — RSI Price Line (SMA of raw RSI)
    signal_line: pd.Series       # Red — Trade Signal Line
    market_base: pd.Series       # Yellow — Market Base Line
    upper_vb: pd.Series          # Upper volatility band
    lower_vb: pd.Series          # Lower volatility band

    # Current values (latest bar)
    rsi: float
    signal: float
    base: float
    upper: float
    lower: float

    # Computed signals
    signals: List[TDISignal]
    shark_fin_active: bool
    shark_fin_direction: str     # "SHORT" / "LONG" / ""
    vb_width: float
    vb_squeeze: bool
    rsi_above_base: bool
    rsi_crossed_signal: str      # "bullish" / "bearish" / "none"
    divergence: str              # "bullish" / "bearish" / "none"


# =====================================================================
# Wilder RSI — matches MT4/MT5 iRSI() output
# =====================================================================

def _wilder_rsi(close: pd.Series, period: int) -> pd.Series:
    """Wilder RSI matching MT4/MT5 iRSI() Wilder smoothing.

    Uses ewm(alpha=1/period, adjust=False) — the Wilder RMA convention.
    Edge cases: avg_loss==0 → RSI=100, avg_gain==0 → RSI=0.
    """
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    avg_gain = gain.ewm(alpha=1.0 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, adjust=False).mean()

    zero_loss = avg_loss == 0.0
    rs = avg_gain / avg_loss.where(avg_loss != 0, other=1.0)
    rsi = 100.0 - (100.0 / (1.0 + rs))
    rsi = rsi.where(~zero_loss, other=100.0)
    rsi.iloc[:period - 1] = float("nan")
    return rsi


# =====================================================================
# TDI Compute — V2-verified implementation
# =====================================================================

def compute_tdi(df: pd.DataFrame) -> TDIResult:
    """Compute TDI with V2-verified parameters.

    Lines computed using SMA (rolling mean), NOT EMA — matching V2/MT4/MT5.
    """
    closes = df["Close"]
    rsi_raw = _wilder_rsi(closes, RSI_PERIOD)

    # Green: RSI Price Line — SMA(rsi_raw, 2)
    rsi_pl = rsi_raw.rolling(RSI_PRICE_LINE).mean()

    # Red: Trade Signal Line — SMA(rsi_raw, 7)
    tsl = rsi_raw.rolling(TRADE_SIGNAL_LINE).mean()

    # Yellow: Market Base Line — SMA(rsi_raw, 34)
    mbl = rsi_raw.rolling(MARKET_BASE_LINE).mean()

    # Volatility Bands — Bollinger on rsi_raw (population stddev per V2)
    sigma = rsi_raw.rolling(VB_PERIOD).std(ddof=0)
    upper_vb = mbl + VB_STD * sigma
    lower_vb = mbl - VB_STD * sigma

    # Current values
    curr_rsi = float(rsi_pl.iloc[-1]) if not pd.isna(rsi_pl.iloc[-1]) else 50.0
    curr_signal = float(tsl.iloc[-1]) if not pd.isna(tsl.iloc[-1]) else 50.0
    curr_base = float(mbl.iloc[-1]) if not pd.isna(mbl.iloc[-1]) else 50.0
    curr_upper = float(upper_vb.iloc[-1]) if not pd.isna(upper_vb.iloc[-1]) else 68.0
    curr_lower = float(lower_vb.iloc[-1]) if not pd.isna(lower_vb.iloc[-1]) else 32.0
    vb_width = curr_upper - curr_lower

    signals: List[TDISignal] = []

    # VB Squeeze
    vb_squeeze = vb_width < VB_SQUEEZE_THRESHOLD
    if vb_squeeze:
        signals.append(TDISignal.VB_SQUEEZE)

    # Overbought / Oversold (using verified 63/37 thresholds)
    if curr_rsi >= SHARK_FIN_UPPER:
        signals.append(TDISignal.RSI_OVERBOUGHT)
    elif curr_rsi <= SHARK_FIN_LOWER:
        signals.append(TDISignal.RSI_OVERSOLD)

    # --- Signal Cross: rsi_pl crosses tsl (shift(1) guard per V2) ---
    rsi_crossed = "none"
    if len(rsi_pl) >= 2:
        prev_pl = float(rsi_pl.iloc[-2]) if not pd.isna(rsi_pl.iloc[-2]) else curr_rsi
        prev_tsl = float(tsl.iloc[-2]) if not pd.isna(tsl.iloc[-2]) else curr_signal
        if prev_pl <= prev_tsl and curr_rsi > curr_signal:
            rsi_crossed = "bullish"
            signals.append(TDISignal.SIGNAL_CROSS_BULLISH)
        elif prev_pl >= prev_tsl and curr_rsi < curr_signal:
            rsi_crossed = "bearish"
            signals.append(TDISignal.SIGNAL_CROSS_BEARISH)

    # --- MBL Cross (Blood in the Water) per V2 ---
    # Requires: rsi_pl crosses mbl AND rsi_pl is on correct side of tsl
    if len(rsi_pl) >= 2:
        prev_pl = float(rsi_pl.iloc[-2]) if not pd.isna(rsi_pl.iloc[-2]) else curr_rsi
        prev_mbl = float(mbl.iloc[-2]) if not pd.isna(mbl.iloc[-2]) else curr_base
        if prev_pl <= prev_mbl and curr_rsi > curr_base and curr_rsi > curr_signal:
            signals.append(TDISignal.MBL_CROSS_BULLISH)
        elif prev_pl >= prev_mbl and curr_rsi < curr_base and curr_rsi < curr_signal:
            signals.append(TDISignal.MBL_CROSS_BEARISH)

    # --- Hook: rsi_pl re-enters VB from extreme (counter-trend per V2) ---
    if len(rsi_pl) >= 2:
        prev_pl = float(rsi_pl.iloc[-2]) if not pd.isna(rsi_pl.iloc[-2]) else curr_rsi
        prev_vb_lower = float(lower_vb.iloc[-2]) if not pd.isna(lower_vb.iloc[-2]) else curr_lower
        prev_vb_upper = float(upper_vb.iloc[-2]) if not pd.isna(upper_vb.iloc[-2]) else curr_upper
        if curr_rsi > curr_lower and prev_pl <= prev_vb_lower and curr_rsi < 40:
            signals.append(TDISignal.HOOK_BULLISH)
        if curr_rsi < curr_upper and prev_pl >= prev_vb_upper and curr_rsi > 60:
            signals.append(TDISignal.HOOK_BEARISH)

    # --- Shark Fin detection (RSI broke out of VB then re-entered) ---
    shark_fin_active = False
    shark_fin_dir = ""
    if len(rsi_pl) >= 6:
        recent_pl = rsi_pl.iloc[-6:].values
        recent_upper = upper_vb.iloc[-6:].values
        recent_lower = lower_vb.iloc[-6:].values

        above_upper = recent_pl[:-1] > recent_upper[:-1]
        now_inside = recent_pl[-1] <= recent_upper[-1]
        if np.any(above_upper[~np.isnan(above_upper)]) and now_inside:
            signals.append(TDISignal.SHARK_FIN_SHORT)
            shark_fin_active = True
            shark_fin_dir = "SHORT"

        below_lower = recent_pl[:-1] < recent_lower[:-1]
        now_inside_low = recent_pl[-1] >= recent_lower[-1]
        if np.any(below_lower[~np.isnan(below_lower)]) and now_inside_low:
            signals.append(TDISignal.SHARK_FIN_LONG)
            shark_fin_active = True
            shark_fin_dir = "LONG"

    rsi_above_base = curr_rsi > curr_base

    # Divergence
    divergence = _detect_divergence(df, rsi_raw)
    if divergence == "bullish":
        signals.append(TDISignal.BULLISH_DIVERGENCE)
    elif divergence == "bearish":
        signals.append(TDISignal.BEARISH_DIVERGENCE)

    if not signals:
        signals.append(TDISignal.NONE)

    return TDIResult(
        rsi_line=rsi_pl,
        signal_line=tsl,
        market_base=mbl,
        upper_vb=upper_vb,
        lower_vb=lower_vb,
        rsi=curr_rsi,
        signal=curr_signal,
        base=curr_base,
        upper=curr_upper,
        lower=curr_lower,
        signals=signals,
        shark_fin_active=shark_fin_active,
        shark_fin_direction=shark_fin_dir,
        vb_width=vb_width,
        vb_squeeze=vb_squeeze,
        rsi_above_base=rsi_above_base,
        rsi_crossed_signal=rsi_crossed,
        divergence=divergence,
    )


def _detect_divergence(df: pd.DataFrame, rsi: pd.Series, lookback: int = 20) -> str:
    if len(df) < lookback:
        return "none"
    prices = df["Close"].iloc[-lookback:].values
    rsi_vals = rsi.iloc[-lookback:].values
    mid = lookback // 2

    price_high_1 = np.nanmax(prices[:mid])
    price_high_2 = np.nanmax(prices[mid:])
    rsi_high_1 = np.nanmax(rsi_vals[:mid])
    rsi_high_2 = np.nanmax(rsi_vals[mid:])
    if price_high_2 > price_high_1 and rsi_high_2 < rsi_high_1:
        return "bearish"

    price_low_1 = np.nanmin(prices[:mid])
    price_low_2 = np.nanmin(prices[mid:])
    rsi_low_1 = np.nanmin(rsi_vals[:mid])
    rsi_low_2 = np.nanmin(rsi_vals[mid:])
    if price_low_2 < price_low_1 and rsi_low_2 > rsi_low_1:
        return "bullish"

    return "none"


# =====================================================================
# Wilder ATR — matches MT4/MT5 iATR() output (ported from V2)
# =====================================================================

def _wilder_atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int) -> pd.Series:
    """ATR with Wilder's smoothing — matches MT4/MT5 iATR()."""
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.ewm(alpha=1.0 / period, adjust=False).mean()


# =====================================================================
# Pivot Points — V2-verified with R3/S3 + day-type logic
# =====================================================================

def compute_pivots(
    prev_high: float,
    prev_low: float,
    prev_close: float,
    prev_candle_bullish: bool = True,
) -> dict:
    """Compute pivot points from previous day's H/L/C.

    Includes R3/S3 and MMM day-type prediction:
      Red prior candle → M1/M3 day (HOD between S2/S1 or PP/R1)
      Green prior candle → M2/M4 day (HOD between S1/PP or R1/R2)
    """
    pp = (prev_high + prev_low + prev_close) / 3.0
    r1 = 2 * pp - prev_low
    s1 = 2 * pp - prev_high
    r2 = pp + (prev_high - prev_low)
    s2 = pp - (prev_high - prev_low)
    r3 = prev_high + 2 * (pp - prev_low)
    s3 = prev_low - 2 * (prev_high - pp)

    # MMM mid-pivots (Book pp. 42-43)
    m1 = (s2 + s1) / 2.0
    m2 = (s1 + pp) / 2.0
    m3 = (pp + r1) / 2.0
    m4 = (r1 + r2) / 2.0

    # Day type prediction
    day_type = "M2_M4" if prev_candle_bullish else "M1_M3"

    return {
        "PP": pp, "R1": r1, "R2": r2, "R3": r3,
        "S1": s1, "S2": s2, "S3": s3,
        "M1": m1, "M2": m2, "M3": m3, "M4": m4,
        "day_type": day_type,
    }


# =====================================================================
# ADR Marker — V2-verified ATR(14) Wilder smoothing
# =====================================================================

def compute_adr_marker(df_daily: pd.DataFrame, pip_size: float = 0.0001) -> dict:
    """Compute ADR marker using Wilder ATR(14) — matches V2 SM_ADR_Marker.

    Returns dict with adr (price), marker_high, marker_low, adr_pips.
    """
    atr = _wilder_atr(df_daily["High"], df_daily["Low"], df_daily["Close"], 14)
    adr = float(atr.iloc[-1])
    today_open = float(df_daily["Open"].iloc[-1])

    return {
        "adr": adr,
        "adr_pips": adr / pip_size,
        "marker_mid": today_open,
        "marker_high": today_open + adr / 2.0,
        "marker_low": today_open - adr / 2.0,
    }


# =====================================================================
# NewHUD Dashboard — ported from V2 SM_NewHUD
# =====================================================================

def compute_hud(df_daily: pd.DataFrame, pip_size: float = 0.0001) -> dict:
    """Compute the full NewHUD dashboard metrics.

    Requires daily OHLC bars (at least 132 for HYADR).
    Returns dict with all HUD fields matching your flashcard screenshots.
    """
    h = df_daily["High"]
    l = df_daily["Low"]
    c = df_daily["Close"]
    o = df_daily["Open"]

    tdr = float(h.iloc[-1] - l.iloc[-1])
    ydr = float(h.iloc[-2] - l.iloc[-2]) if len(df_daily) >= 2 else 0

    daily_ranges = h - l

    def _rolling_mean(series, n):
        if len(series) >= n:
            return float(series.iloc[-n:].mean())
        return float(series.mean())

    wadr = _rolling_mean(daily_ranges, 5)
    madr = _rolling_mean(daily_ranges, 22)
    hyadr = _rolling_mean(daily_ranges, 132) if len(df_daily) >= 132 else _rolling_mean(daily_ranges, len(df_daily))

    # Week high/low
    wh = float(h.iloc[-5:].max()) if len(df_daily) >= 5 else float(h.max())
    wl = float(l.iloc[-5:].min()) if len(df_daily) >= 5 else float(l.min())
    wr = wh - wl

    # Current price (latest close)
    bid = float(c.iloc[-1])
    hod = float(h.iloc[-1])
    lod = float(l.iloc[-1])

    # Monthly/multi-week ranges
    mwr = _rolling_mean(daily_ranges, 5) * 5    # approximate weekly range
    mwr_3 = _rolling_mean(daily_ranges, 15) * 5
    mwr_6 = _rolling_mean(daily_ranges, 30) * 5

    return {
        "HOD": hod,
        "LOD": lod,
        "HOD_dist": (hod - bid) / pip_size,
        "LOD_dist": (bid - lod) / pip_size,
        "TDR": tdr / pip_size,
        "YDR": ydr / pip_size,
        "WADR": wadr / pip_size,
        "MADR": madr / pip_size,
        "HYADR": hyadr / pip_size,
        "PTO": (bid - float(o.iloc[-1])) / pip_size,
        "WH": wh,
        "WL": wl,
        "WH_dist": (wh - bid) / pip_size,
        "WL_dist": (bid - wl) / pip_size,
        "WR": wr / pip_size,
        "MWR": mwr / pip_size,
        "3MWR": mwr_3 / pip_size,
        "6MWR": mwr_6 / pip_size,
        "3xADR": wadr * 3 / pip_size,
    }


# =====================================================================
# Crossover Arrows — ported from V2 SM_Crossover_Arrows
# =====================================================================

def compute_crossover_arrows(df: pd.DataFrame) -> dict:
    """Dual EMA crossover detection — EMA 7/13 + EMA 50/200.

    Uses shift(1) guard against repainting per V2.
    Returns dict with latest crossover signals and EMA values.
    """
    closes = df["Close"]

    ema_7 = closes.ewm(span=7, adjust=False).mean()
    ema_13 = closes.ewm(span=13, adjust=False).mean()
    ema_50 = closes.ewm(span=50, adjust=False).mean()
    ema_200 = closes.ewm(span=200, adjust=False).mean()

    # Short-term cross: 7/13 (shift(1) guard)
    short_bull = (ema_7 > ema_13) & (ema_7.shift(1) <= ema_13.shift(1))
    short_bear = (ema_7 < ema_13) & (ema_7.shift(1) >= ema_13.shift(1))

    # Long-term cross: 50/200
    golden = (ema_50 > ema_200) & (ema_50.shift(1) <= ema_200.shift(1))
    death = (ema_50 < ema_200) & (ema_50.shift(1) >= ema_200.shift(1))

    # Latest signal
    latest_short = "NONE"
    if short_bull.iloc[-1]:
        latest_short = "BUY"
    elif short_bear.iloc[-1]:
        latest_short = "SELL"

    latest_long = "NONE"
    if golden.iloc[-1]:
        latest_long = "GOLDEN_CROSS"
    elif death.iloc[-1]:
        latest_long = "DEATH_CROSS"

    # All crossover bar indices for chart marking
    buy_bars = list(short_bull[short_bull].index)
    sell_bars = list(short_bear[short_bear].index)

    return {
        "ema_7": ema_7,
        "ema_13": ema_13,
        "ema_50": ema_50,
        "ema_200": ema_200,
        "short_cross": latest_short,
        "long_cross": latest_long,
        "buy_bars": buy_bars[-5:],     # last 5 for chart
        "sell_bars": sell_bars[-5:],
    }


# =====================================================================
# Daily HiLo — ported from V2 SM_Daily_HiLo v2.01
# =====================================================================

def compute_daily_hilo(df_daily: pd.DataFrame, days_back: int = 14) -> dict:
    """PHOD/PLOD with N-day snake history.

    Returns dict with phod, plod (yesterday) and snake lists for N days back.
    """
    if len(df_daily) < 2:
        return {"phod": 0, "plod": 0, "snake_highs": [], "snake_lows": []}

    phod = float(df_daily["High"].iloc[-2])
    plod = float(df_daily["Low"].iloc[-2])

    n = min(days_back, len(df_daily) - 1)
    snake_highs = [float(df_daily["High"].iloc[-(i + 2)]) for i in range(n)]
    snake_lows = [float(df_daily["Low"].iloc[-(i + 2)]) for i in range(n)]

    return {
        "phod": phod,
        "plod": plod,
        "snake_highs": snake_highs,
        "snake_lows": snake_lows,
    }


# Legacy compat
def compute_adr(df_daily: pd.DataFrame, period: int = 14) -> float:
    """Legacy ADR — now uses Wilder ATR(14) per V2."""
    atr = _wilder_atr(df_daily["High"], df_daily["Low"], df_daily["Close"], period)
    return float(atr.iloc[-1])
