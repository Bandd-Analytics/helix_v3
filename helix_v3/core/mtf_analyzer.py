"""Multi-Timeframe MMM Analyzer.

Implements the correct MMM top-down analysis sequence from the Steve Mauro methodology:

1. WEEKLY STRUCTURE (W1/D1): Where are we in the 3-day/weekly cycle?
   - Identify peak formation high/low
   - Count levels (L1, L2, L3)
   - Determine if mid-week reversal is due

2. 4-HOUR CONTEXT (H4): Multi-day cycle position
   - 3-day cycle level count
   - Peak formations and consolidation zones
   - EMA stack alignment (5/13/50/200/800)

3. 1-HOUR CONFIRMATION (H1): Intraday trend direction
   - Intraday level count (mirrors 3-day pattern)
   - EMA crossovers and momentum
   - Session identification (Asian/London/NY)
   - HOD/LOD identification

4. 15-MINUTE ENTRY (M15): Precise timing
   - Asian range box (accumulation < 50 pips)
   - Stop hunt detection (25-50 pips beyond range)
   - M/W formation identification
   - RRT, pin bars, entry signals
   - 3 pushes count

Each timeframe feeds context DOWN to the next. You never enter on M15
without knowing where you are on H1, H4, and weekly.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Dict, List

import numpy as np
import pandas as pd

from config.pair_profiles import PairProfile, get_pair_profile
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.types import Direction, EMAVector
from helix_v3.utils.logger import get_logger

logger = get_logger("mtf_analyzer")


class CyclePosition(Enum):
    PEAK_HIGH = "PEAK_HIGH"
    LEVEL_1 = "LEVEL_1"
    LEVEL_2 = "LEVEL_2"
    LEVEL_3 = "LEVEL_3"
    PEAK_LOW = "PEAK_LOW"
    UNKNOWN = "UNKNOWN"


class WeekPhase(Enum):
    EARLY_WEEK = "EARLY_WEEK"          # Sun-Mon: initial direction
    MID_WEEK_REVERSAL = "MID_WEEK"     # Tue-Wed: reversal zone
    LATE_WEEK = "LATE_WEEK"            # Thu-Fri: continuation/profit taking
    WEEKEND = "WEEKEND"


class SessionPhase(Enum):
    ACCUMULATION = "ACCUMULATION"       # Asian session, circular trading
    STOP_HUNT = "STOP_HUNT"            # 1-4am ET, defining HOD/LOD
    TRUE_TREND = "TRUE_TREND"          # London open, trend run
    NYC_REVERSAL = "NYC_REVERSAL"      # NY open, opposite LOD/HOD
    RETURN_TO_ACCUM = "RETURN_ACCUM"   # Post-NY, back to center


@dataclass
class WeeklyContext:
    """Weekly/multi-day cycle analysis."""
    cycle_position: CyclePosition
    week_phase: WeekPhase
    trend_direction: Direction              # Overall weekly bias
    days_since_peak: int                    # Days since last peak high/low
    peak_high: float
    peak_low: float
    midweek_reversal_expected: bool
    ema_stack: Dict[int, float]             # Current EMA values on D1/H4
    notes: str = ""


@dataclass
class FourHourContext:
    """4-hour / 3-day cycle analysis."""
    cycle_position: CyclePosition
    level_count: int                        # 1, 2, or 3
    trend_direction: Direction
    consolidation_high: float
    consolidation_low: float
    ema_vector: EMAVector
    peak_formation_detected: bool
    is_choppy: bool                         # L3 = choppy
    notes: str = ""


@dataclass
class OneHourContext:
    """1-hour intraday analysis."""
    intraday_level: int                     # Intraday 1/2/3
    session_phase: SessionPhase
    trend_direction: Direction
    hod: float                              # High of day
    lod: float                              # Low of day
    hod_locked: bool                        # Has HOD been defined?
    lod_locked: bool
    ema_vector: EMAVector
    ema_50_200_cross: str                   # "bullish" / "bearish" / "none"
    notes: str = ""


@dataclass
class FifteenMinEntry:
    """15-minute entry-level analysis."""
    asian_range_high: float
    asian_range_low: float
    asian_range_pips: float
    accumulation_valid: bool                # Range < pair max
    stop_hunt_detected: bool
    stop_hunt_direction: Direction
    stop_hunt_pips: float
    push_count: int                         # Count of pushes (target: 3)
    m_w_forming: bool
    rrt_detected: bool
    entry_signal: bool
    entry_direction: Direction
    entry_confidence: float
    m_w_pattern: str = ""                   # "W_BOTTOM" / "M_TOP" / ""
    adr_pct_used: float = 0.0              # How much of ADR consumed today (0-200%+)
    volume_z_asian: float = 0.0            # Volume Z during Asian (< -1 = genuine accumulation)
    notes: str = ""


@dataclass
class MTFAnalysis:
    """Complete multi-timeframe analysis result."""
    symbol: str
    timestamp: datetime
    weekly: WeeklyContext
    four_hour: FourHourContext
    one_hour: OneHourContext
    fifteen_min: FifteenMinEntry
    pair_profile: PairProfile

    # Composite assessment
    trade_valid: bool = False
    trade_direction: Direction = Direction.NEUTRAL
    trade_confidence: float = 0.0
    confluence_score: int = 0               # 0-100
    rejection_reasons: List[str] = field(default_factory=list)


class MTFAnalyzer:
    """Multi-timeframe MMM analysis engine.

    Performs the correct top-down sequence:
    Weekly -> 4H -> 1H -> 15M

    Only produces entry signals when ALL timeframes align.
    """

    def __init__(self, engine: MMMQuantitativeEngine) -> None:
        self._engine = engine

    def analyze(self, symbol: str) -> MTFAnalysis:
        """Run full top-down MTF analysis for a symbol."""
        pp = get_pair_profile(symbol)
        now = datetime.now(timezone.utc)

        weekly = self._analyze_weekly(symbol)
        four_hour = self._analyze_4h(symbol)
        one_hour = self._analyze_1h(symbol)
        fifteen_min = self._analyze_15m(symbol, pp)

        # Build composite assessment
        analysis = MTFAnalysis(
            symbol=symbol,
            timestamp=now,
            weekly=weekly,
            four_hour=four_hour,
            one_hour=one_hour,
            fifteen_min=fifteen_min,
            pair_profile=pp,
        )

        self._compute_confluence(analysis)
        return analysis

    # ------------------------------------------------------------------
    # Weekly / Multi-Day Analysis
    # ------------------------------------------------------------------

    def _analyze_weekly(self, symbol: str) -> WeeklyContext:
        df_d1 = self._engine.fetch_rates(symbol, "D1", count=30)
        df_h4 = self._engine.fetch_rates(symbol, "H4", count=120)

        closes = df_d1["Close"]
        # EMA stack on D1
        ema_stack = {}
        for p in [5, 13, 50, 200]:
            ema_stack[p] = float(closes.ewm(span=p, adjust=False).mean().iloc[-1])

        # Find recent peak high and peak low (last 10 days)
        recent = df_d1.iloc[-10:]
        peak_high = float(recent["High"].max())
        peak_low = float(recent["Low"].min())

        peak_high_idx = recent["High"].idxmax()
        peak_low_idx = recent["Low"].idxmin()

        days_since_high = (df_d1.index[-1] - peak_high_idx).days
        days_since_low = (df_d1.index[-1] - peak_low_idx).days

        # Determine if we're coming from a peak high or peak low
        if days_since_high < days_since_low:
            trend = Direction.SELL  # Coming down from peak high
            days_since_peak = days_since_high
        else:
            trend = Direction.BUY  # Coming up from peak low
            days_since_peak = days_since_low

        # Week phase
        weekday = now_utc().weekday()
        if weekday in (6, 0):  # Sun-Mon
            week_phase = WeekPhase.EARLY_WEEK
        elif weekday in (1, 2):  # Tue-Wed
            week_phase = WeekPhase.MID_WEEK_REVERSAL
        elif weekday in (3, 4):  # Thu-Fri
            week_phase = WeekPhase.LATE_WEEK
        else:
            week_phase = WeekPhase.WEEKEND

        midweek_reversal = week_phase == WeekPhase.MID_WEEK_REVERSAL

        # Cycle position from level count on H4
        cycle_pos = self._count_levels_from_peak(df_h4, trend)

        return WeeklyContext(
            cycle_position=cycle_pos,
            week_phase=week_phase,
            trend_direction=trend,
            days_since_peak=days_since_peak,
            peak_high=peak_high,
            peak_low=peak_low,
            midweek_reversal_expected=midweek_reversal,
            ema_stack=ema_stack,
            notes=f"Weekly {trend.value} bias, {week_phase.value}, {days_since_peak}d from peak",
        )

    # ------------------------------------------------------------------
    # 4-Hour Analysis (3-Day Cycle)
    # ------------------------------------------------------------------

    def _analyze_4h(self, symbol: str) -> FourHourContext:
        df = self._engine.fetch_rates(symbol, "H4", count=120)

        ema_vec = self._compute_ema_vector(df)

        # Level count: look at last 3 days (18 x H4 bars)
        recent = df.iloc[-18:]
        high = float(recent["High"].max())
        low = float(recent["Low"].min())

        cycle_pos = self._count_levels_from_peak(df, ema_vec.trend_alignment)

        # Detect choppiness (L3 indicator): range compression in last 6 bars
        last_6 = df.iloc[-6:]
        range_6 = last_6["High"].max() - last_6["Low"].min()
        avg_range = (df["High"] - df["Low"]).rolling(18).mean().iloc[-1]
        is_choppy = range_6 < avg_range * 0.6

        peak_detected = False
        if len(df) >= 3:
            h1 = df["High"].iloc[-3]
            h2 = df["High"].iloc[-2]
            h3 = df["High"].iloc[-1]
            if h2 > h1 and h2 > h3:
                peak_detected = True
            l1 = df["Low"].iloc[-3]
            l2 = df["Low"].iloc[-2]
            l3 = df["Low"].iloc[-1]
            if l2 < l1 and l2 < l3:
                peak_detected = True

        level = cycle_pos.value.split("_")[-1] if "LEVEL" in cycle_pos.value else "0"

        return FourHourContext(
            cycle_position=cycle_pos,
            level_count=int(level) if level.isdigit() else 0,
            trend_direction=ema_vec.trend_alignment,
            consolidation_high=high,
            consolidation_low=low,
            ema_vector=ema_vec,
            peak_formation_detected=peak_detected,
            is_choppy=is_choppy,
            notes=f"H4 {cycle_pos.value}, choppy={is_choppy}",
        )

    # ------------------------------------------------------------------
    # 1-Hour Analysis (Intraday)
    # ------------------------------------------------------------------

    def _analyze_1h(self, symbol: str) -> OneHourContext:
        df = self._engine.fetch_rates(symbol, "H1", count=100)
        ema_vec = self._compute_ema_vector(df)

        # Today's data for HOD/LOD
        today = df.index[-1].date()
        today_bars = df[df.index.date == today]
        if today_bars.empty:
            today_bars = df.iloc[-24:]

        hod = float(today_bars["High"].max())
        lod = float(today_bars["Low"].min())

        # HOD/LOD locked: if stop hunt has occurred (sharp move + reversal)
        recent_3 = df.iloc[-3:]
        hod_locked = float(recent_3["High"].max()) < hod * 0.999
        lod_locked = float(recent_3["Low"].min()) > lod * 1.001

        # Session phase
        hour_utc = now_utc().hour
        if 1 <= hour_utc < 5:
            session = SessionPhase.ACCUMULATION
        elif 5 <= hour_utc < 8:
            session = SessionPhase.STOP_HUNT
        elif 8 <= hour_utc < 13:
            session = SessionPhase.TRUE_TREND
        elif 13 <= hour_utc < 17:
            session = SessionPhase.NYC_REVERSAL
        else:
            session = SessionPhase.RETURN_TO_ACCUM

        # EMA 50/200 cross
        closes = df["Close"]
        ema50 = closes.ewm(span=50, adjust=False).mean()
        ema200 = closes.ewm(span=200, adjust=False).mean()
        if ema50.iloc[-1] > ema200.iloc[-1] and ema50.iloc[-3] <= ema200.iloc[-3]:
            cross = "bullish"
        elif ema50.iloc[-1] < ema200.iloc[-1] and ema50.iloc[-3] >= ema200.iloc[-3]:
            cross = "bearish"
        else:
            cross = "none"

        # Intraday level count (simplified)
        intraday_level = self._count_intraday_levels(today_bars)

        return OneHourContext(
            intraday_level=intraday_level,
            session_phase=session,
            trend_direction=ema_vec.trend_alignment,
            hod=hod,
            lod=lod,
            hod_locked=hod_locked,
            lod_locked=lod_locked,
            ema_vector=ema_vec,
            ema_50_200_cross=cross,
            notes=f"H1 {session.value}, HOD={hod:.5f} LOD={lod:.5f}",
        )

    # ------------------------------------------------------------------
    # 15-Minute Entry Analysis
    # ------------------------------------------------------------------

    def _analyze_15m(self, symbol: str, pp: PairProfile) -> FifteenMinEntry:
        df = self._engine.fetch_rates(symbol, "M15", count=200)
        pip_size = self._engine._get_pip_value(symbol)

        # Asian range (21:00-02:00 EST = 02:00-07:00 UTC)
        est_offset = timedelta(hours=-5)
        hours_est = (df.index + est_offset).hour

        asian_mask = (hours_est >= 21) | (hours_est < 2)
        today = df.index[-1].date()
        today_mask = df.index.date >= (today - timedelta(days=1))
        asian = df[asian_mask & today_mask]

        if not asian.empty:
            ar_high = float(asian["High"].max())
            ar_low = float(asian["Low"].min())
        else:
            ar_high = float(df.iloc[-20:]["High"].max())
            ar_low = float(df.iloc[-20:]["Low"].min())

        ar_pips = (ar_high - ar_low) / pip_size
        accum_valid = ar_pips <= pp.asian_range_max_pips

        # Stop hunt detection — scan ALL post-Asian bars for ANY breach,
        # not just current price. The stop hunt happens then price reverses,
        # so by scan time the current price may already be back inside range.
        #
        # Per MMM: a W-bottom retest of Asian low IS the stop hunt even if
        # the breach is only a few pips. The M/W formation confirms it.
        # We use two thresholds:
        #   - "hard" hunt: breach >= stop_hunt_min_pips (classic 25-50p)
        #   - "soft" hunt: any breach of Asian boundary + M/W or RRT confirmation

        post_asian = df[~asian_mask | (~today_mask)]

        hunt_detected = False
        hunt_dir = Direction.NEUTRAL
        hunt_pips = 0.0

        # Scan all post-Asian bars for maximum breach
        max_breach_above = 0.0
        max_breach_below = 0.0
        if not post_asian.empty:
            max_high = float(post_asian["High"].max())
            min_low = float(post_asian["Low"].min())
            max_breach_above = (max_high - ar_high) / pip_size
            max_breach_below = (ar_low - min_low) / pip_size

        # Hard stop hunt: classic 25-50 pip breach
        if pp.stop_hunt_min_pips <= max_breach_above <= pp.stop_hunt_max_pips:
            hunt_detected = True
            hunt_dir = Direction.SELL
            hunt_pips = max_breach_above
        elif pp.stop_hunt_min_pips <= max_breach_below <= pp.stop_hunt_max_pips:
            hunt_detected = True
            hunt_dir = Direction.BUY
            hunt_pips = max_breach_below

        # M/W detection — this determines the DIRECTION per MMM
        # W-bottom = BUY (double bottom, MM hunted lows, true trend is up)
        # M-top = SELL (double top, MM hunted highs, true trend is down)
        last_20 = df.iloc[-20:]
        m_w = False
        m_w_direction = Direction.NEUTRAL
        m_w_highs = last_20["High"].values
        m_w_lows = last_20["Low"].values

        # Check W-bottom first (two troughs with peak between)
        for i in range(2, len(m_w_lows) - 2):
            if m_w_lows[i] > m_w_lows[i - 2] and m_w_lows[i] > m_w_lows[i + 2]:
                trough_diff = abs(m_w_lows[i - 2] - m_w_lows[i + 2]) / pip_size
                if trough_diff < 20:
                    m_w = True
                    m_w_direction = Direction.BUY
                    break

        # Check M-top (two peaks with valley between)
        if not m_w:
            for i in range(2, len(m_w_highs) - 2):
                if m_w_highs[i] < m_w_highs[i - 2] and m_w_highs[i] < m_w_highs[i + 2]:
                    peak_diff = abs(m_w_highs[i - 2] - m_w_highs[i + 2]) / pip_size
                    if peak_diff < 20:
                        m_w = True
                        m_w_direction = Direction.SELL
                        break

        # RRT detection
        rrt = self._detect_rrt(df.iloc[-4:])
        m_w_pattern = ""
        if m_w_direction == Direction.BUY:
            m_w_pattern = "W_BOTTOM"
        elif m_w_direction == Direction.SELL:
            m_w_pattern = "M_TOP"

        # DIRECTION LOGIC — M/W pattern overrides stop hunt side
        # Per MMM: the M/W formation tells you the TRUE direction.
        # The stop hunt just confirms liquidity was grabbed.
        current = float(df.iloc[-1]["Close"])

        if m_w and m_w_direction != Direction.NEUTRAL:
            # M/W pattern determines direction — this is the primary signal
            if not hunt_detected:
                hunt_detected = True
                hunt_pips = max(max_breach_above, max_breach_below)
            hunt_dir = m_w_direction
        elif hunt_detected and m_w:
            # Hunt was detected by breach, but M/W should override direction
            hunt_dir = m_w_direction
        elif not hunt_detected and (m_w or rrt):
            # Soft hunt: any breach + pattern confirmation
            if max_breach_above >= 1.0 or max_breach_below >= 1.0:
                hunt_detected = True
                hunt_pips = max(max_breach_above, max_breach_below)
                # Use M/W direction if available, otherwise infer from price position
                if m_w_direction != Direction.NEUTRAL:
                    hunt_dir = m_w_direction
                elif current > ar_high:
                    hunt_dir = Direction.BUY
                elif current < ar_low:
                    hunt_dir = Direction.SELL

        # Count pushes in stop hunt zone (3 pushes expected)
        push_count = 0
        if hunt_detected:
            if hunt_dir == Direction.SELL:
                above = post_asian[post_asian["High"] > ar_high]
                if not above.empty:
                    push_count = self._count_pushes(above["High"].values, direction="up")
            else:
                below = post_asian[post_asian["Low"] < ar_low]
                if not below.empty:
                    push_count = self._count_pushes(below["Low"].values, direction="down")
                # Also count pushes TO the Asian low (W retests)
                if push_count == 0:
                    near_low = post_asian[post_asian["Low"] < ar_low + 5 * pip_size]
                    if not near_low.empty:
                        push_count = self._count_pushes(near_low["Low"].values, direction="down")

        # Entry signal: accumulation + (hunt OR soft hunt with M/W) + pattern confirmation
        entry_signal = accum_valid and hunt_detected and (m_w or rrt or push_count >= 3)
        entry_dir = hunt_dir if entry_signal else Direction.NEUTRAL

        # Confidence based on how many confirmations
        conf = 0.0
        if accum_valid:
            conf += 0.20
        if hunt_detected:
            conf += 0.20
            if hunt_pips >= pp.stop_hunt_min_pips:
                conf += 0.10  # bonus for deep hunt
        if push_count >= 3:
            conf += 0.15
        elif push_count >= 2:
            conf += 0.10
        if m_w:
            conf += 0.25
        if rrt:
            conf += 0.15
        # Bonus: price already reversed past Asian range (strong confirmation)
        if hunt_detected and ((hunt_dir == Direction.BUY and current > ar_high) or
                               (hunt_dir == Direction.SELL and current < ar_low)):
            conf += 0.10

        # --- ADR% used: how much of today's expected range is consumed ---
        # If > 80%, the day's move may be done — entering is risky (stale exit likely)
        adr_pct = 0.0
        try:
            df_d1 = self._engine.fetch_rates(symbol, "D1", 20)
            from helix_v3.core.tdi import _wilder_atr
            atr = _wilder_atr(df_d1["High"], df_d1["Low"], df_d1["Close"], 14)
            adr_val = float(atr.iloc[-1])
            # Today's range from M15 data
            today = df.index[-1].date()
            today_bars = df[df.index.date == today]
            if not today_bars.empty and adr_val > 0:
                today_range = float(today_bars["High"].max()) - float(today_bars["Low"].min())
                adr_pct = (today_range / adr_val) * 100.0
        except Exception:
            adr_pct = 0.0

        # --- Volume Z during Asian session: confirms genuine accumulation ---
        # Z < -1.0 = abnormally quiet (genuine accumulation)
        # Z > 0 = normal/active volume during Asian (not true accumulation)
        vol_z_asian = 0.0
        try:
            vol_col = "Volume" if "Volume" in df.columns else "tick_volume"
            if vol_col in df.columns and not asian.empty:
                asian_vols = asian[vol_col].values.astype(float)
                all_vols = df[vol_col].values.astype(float)
                if len(all_vols) > 20:
                    vol_mean = np.mean(all_vols[-100:])
                    vol_std = np.std(all_vols[-100:])
                    if vol_std > 0 and len(asian_vols) > 0:
                        asian_avg_vol = np.mean(asian_vols)
                        vol_z_asian = (asian_avg_vol - vol_mean) / vol_std
        except Exception:
            vol_z_asian = 0.0

        return FifteenMinEntry(
            asian_range_high=ar_high,
            asian_range_low=ar_low,
            asian_range_pips=ar_pips,
            accumulation_valid=accum_valid,
            stop_hunt_detected=hunt_detected,
            stop_hunt_direction=hunt_dir,
            stop_hunt_pips=hunt_pips,
            push_count=push_count,
            m_w_forming=m_w,
            rrt_detected=rrt,
            entry_signal=entry_signal,
            entry_direction=entry_dir,
            entry_confidence=min(1.0, conf),
            m_w_pattern=m_w_pattern,
            adr_pct_used=adr_pct,
            volume_z_asian=vol_z_asian,
            notes=f"AR={ar_pips:.0f}p valid={accum_valid} hunt={hunt_detected} pushes={push_count} M/W={m_w} ADR%={adr_pct:.0f}",
        )

    # ------------------------------------------------------------------
    # Confluence Scoring
    # ------------------------------------------------------------------

    def _compute_confluence(self, a: MTFAnalysis) -> None:
        """Score the alignment across all 4 timeframes."""
        score = 0
        reasons: List[str] = []

        # Weekly direction should agree with entry
        entry_dir = a.fifteen_min.entry_direction
        if entry_dir == Direction.NEUTRAL:
            reasons.append("No 15M entry signal")
        elif a.weekly.trend_direction == entry_dir:
            score += 20
        elif a.weekly.trend_direction != Direction.NEUTRAL:
            reasons.append(f"Weekly trend {a.weekly.trend_direction.value} conflicts with entry {entry_dir.value}")

        # Mid-week reversal alignment
        if a.weekly.midweek_reversal_expected:
            score += 10  # More opportunity for reversals

        # 4H level count: L3 entries are highest probability per MMM
        if a.four_hour.level_count == 3:
            score += 15
        elif a.four_hour.level_count == 2:
            score += 10
        if a.four_hour.is_choppy and a.four_hour.level_count < 3:
            reasons.append("H4 choppy but not at L3 — avoid")

        # 4H trend agrees
        if a.four_hour.trend_direction == entry_dir:
            score += 10
        elif a.four_hour.trend_direction != Direction.NEUTRAL:
            reasons.append(f"H4 trend {a.four_hour.trend_direction.value} conflicts")

        # 1H confirmation
        if a.one_hour.trend_direction == entry_dir:
            score += 10
        if a.one_hour.hod_locked or a.one_hour.lod_locked:
            score += 5
        if a.one_hour.session_phase in (SessionPhase.TRUE_TREND, SessionPhase.STOP_HUNT):
            score += 5  # Best entry sessions
        elif a.one_hour.session_phase == SessionPhase.RETURN_TO_ACCUM:
            reasons.append("Session winding down — poor entry timing")

        # 15M entry quality
        if a.fifteen_min.accumulation_valid:
            score += 5
        else:
            reasons.append(f"Asian range too wide: {a.fifteen_min.asian_range_pips:.0f} pips")

        if a.fifteen_min.stop_hunt_detected:
            score += 10
        if a.fifteen_min.push_count >= 3:
            score += 5
        if a.fifteen_min.m_w_forming:
            # CALIBRATED: M/W London gets full weight, outside gets reduced.
            # 90-day validation: 52-60% hit rate in London vs 37-44% outside.
            if a.one_hour.session_phase in (SessionPhase.TRUE_TREND, SessionPhase.STOP_HUNT):
                score += 10  # Full M/W weight during London
            elif a.one_hour.session_phase == SessionPhase.NYC_REVERSAL:
                score += 5   # NYC reversal is secondary window
            else:
                score += 2   # Minimal weight — needs strong confluence elsewhere
                reasons.append("M/W outside London — reduced confidence")
        if a.fifteen_min.rrt_detected:
            score += 5

        # --- ADR% used filter (from Helix AR indicator) ---
        # If > 80% of ADR consumed, the day's move is likely done.
        # Entering now risks a stale exit. Hard rejection.
        adr_pct = a.fifteen_min.adr_pct_used
        if adr_pct > 120:
            reasons.append(f"ADR exhausted: {adr_pct:.0f}% used (>120%) — move is done")
        elif adr_pct > 80:
            reasons.append(f"ADR mostly used: {adr_pct:.0f}% (>80%) — late entry risk")

        # --- Volume Z accumulation quality (from Volume Z-Score indicator) ---
        # Genuine accumulation has low volume (Z < -1). Normal/high volume
        # during Asian range means the range is contested, not accumulated.
        vol_z = a.fifteen_min.volume_z_asian
        if vol_z < -1.0:
            score += 5  # Genuine quiet accumulation — bonus
        elif vol_z > 0.5 and a.fifteen_min.accumulation_valid:
            # Range is tight but volume is active — not true accumulation
            reasons.append(f"Asian range tight but volume active (Z={vol_z:.1f}) — contested, not accumulated")

        # Final assessment
        # CALIBRATED: threshold 50 -> 55. Filters worst setups without killing volume.
        a.confluence_score = min(100, score)
        a.rejection_reasons = reasons
        a.trade_direction = entry_dir
        a.trade_confidence = a.fifteen_min.entry_confidence
        a.trade_valid = (
            a.confluence_score >= 55
            and entry_dir != Direction.NEUTRAL
            and len(reasons) <= 1  # Allow 1 minor conflict
        )

    # ------------------------------------------------------------------
    # Helper Methods
    # ------------------------------------------------------------------

    def _compute_ema_vector(self, df: pd.DataFrame) -> EMAVector:
        closes = df["Close"]
        emas = {}
        for p in [5, 13, 50, 200, 800]:
            emas[p] = closes.ewm(span=p, adjust=False).mean()

        def angle(s, lookback=5):
            if len(s) < lookback + 1:
                return 0.0
            delta = s.iloc[-1] - s.iloc[-lookback - 1]
            return float(np.degrees(np.arctan2(delta, lookback)))

        angles = {p: angle(emas[p]) for p in emas}
        all_angles = list(angles.values())

        if all(a > 0 for a in all_angles):
            trend = Direction.BUY
        elif all(a < 0 for a in all_angles):
            trend = Direction.SELL
        else:
            trend = Direction.NEUTRAL

        return EMAVector(
            ema_5_angle=angles[5],
            ema_13_angle=angles[13],
            ema_50_angle=angles[50],
            ema_200_angle=angles[200],
            ema_800_angle=angles[800],
            fast_slow_divergence=angles[5] - angles[200],
            trend_alignment=trend,
        )

    def _count_levels_from_peak(self, df: pd.DataFrame, trend: Direction) -> CyclePosition:
        """Count L1/L2/L3 from the most recent peak."""
        if len(df) < 20:
            return CyclePosition.UNKNOWN

        recent = df.iloc[-30:] if len(df) >= 30 else df
        closes = recent["Close"].values
        highs = recent["High"].values
        lows = recent["Low"].values

        if trend == Direction.SELL:
            peak_idx = np.argmax(highs)
            remaining = closes[peak_idx:]
        elif trend == Direction.BUY:
            peak_idx = np.argmin(lows)
            remaining = closes[peak_idx:]
        else:
            return CyclePosition.UNKNOWN

        if len(remaining) < 5:
            return CyclePosition.PEAK_HIGH if trend == Direction.SELL else CyclePosition.PEAK_LOW

        # Count significant reversals (consolidation zones)
        swings = 0
        last_dir = None
        for i in range(1, len(remaining)):
            diff = remaining[i] - remaining[i - 1]
            if abs(diff) < 1e-10:
                continue
            curr_dir = 1 if diff > 0 else -1
            if last_dir is not None and curr_dir != last_dir:
                swings += 1
            last_dir = curr_dir

        # Map swing count to levels (rough heuristic)
        if swings <= 2:
            return CyclePosition.LEVEL_1
        elif swings <= 5:
            return CyclePosition.LEVEL_2
        else:
            return CyclePosition.LEVEL_3

    def _count_intraday_levels(self, today_bars: pd.DataFrame) -> int:
        if len(today_bars) < 3:
            return 0
        closes = today_bars["Close"].values
        swings = 0
        last_dir = None
        for i in range(1, len(closes)):
            diff = closes[i] - closes[i - 1]
            if abs(diff) < 1e-10:
                continue
            curr_dir = 1 if diff > 0 else -1
            if last_dir is not None and curr_dir != last_dir:
                swings += 1
            last_dir = curr_dir
        return min(3, swings // 2)

    def _count_pushes(self, values: np.ndarray, direction: str) -> int:
        if len(values) < 2:
            return 1
        pushes = 1
        for i in range(1, len(values)):
            if direction == "up" and values[i] > values[i - 1]:
                pushes += 1
            elif direction == "down" and values[i] < values[i - 1]:
                pushes += 1
        return min(pushes, 5)

    def _detect_m_w(self, bars: pd.DataFrame, pip_size: float) -> bool:
        if len(bars) < 6:
            return False
        highs = bars["High"].values
        lows = bars["Low"].values

        # M pattern: two peaks with valley between
        for i in range(2, len(highs) - 2):
            if highs[i] < highs[i - 2] and highs[i] < highs[i + 2]:
                peak_diff = abs(highs[i - 2] - highs[i + 2]) / pip_size
                if peak_diff < 15:  # Peaks within 15 pips
                    return True

        # W pattern: two troughs with peak between
        for i in range(2, len(lows) - 2):
            if lows[i] > lows[i - 2] and lows[i] > lows[i + 2]:
                trough_diff = abs(lows[i - 2] - lows[i + 2]) / pip_size
                if trough_diff < 15:
                    return True

        return False

    def _detect_rrt(self, bars: pd.DataFrame) -> bool:
        if len(bars) < 2:
            return False
        for i in range(len(bars) - 1):
            b1_body = abs(bars.iloc[i]["Close"] - bars.iloc[i]["Open"])
            b2_body = abs(bars.iloc[i + 1]["Close"] - bars.iloc[i + 1]["Open"])
            b1_bull = bars.iloc[i]["Close"] > bars.iloc[i]["Open"]
            b2_bull = bars.iloc[i + 1]["Close"] > bars.iloc[i + 1]["Open"]
            if b1_bull != b2_bull and b1_body > 0 and b2_body > 0:
                ratio = min(b1_body, b2_body) / max(b1_body, b2_body)
                if ratio > 0.6:  # Bodies within 60% of each other
                    return True
        return False

    # ------------------------------------------------------------------
    # Formatted Report
    # ------------------------------------------------------------------

    def format_analysis(self, a: MTFAnalysis) -> str:
        lines = [
            f"\n{'='*60}",
            f"  MTF ANALYSIS: {a.symbol} | {a.timestamp.strftime('%Y-%m-%d %H:%M UTC')}",
            f"{'='*60}",
            "",
            f"  WEEKLY:  {a.weekly.cycle_position.value} | {a.weekly.week_phase.value} | Trend: {a.weekly.trend_direction.value}",
            f"           Peak H={a.weekly.peak_high:.5f} L={a.weekly.peak_low:.5f} | {a.weekly.days_since_peak}d from peak",
            f"           Mid-week reversal: {'YES' if a.weekly.midweek_reversal_expected else 'no'}",
            "",
            f"  4-HOUR:  {a.four_hour.cycle_position.value} (L{a.four_hour.level_count}) | Trend: {a.four_hour.trend_direction.value}",
            f"           Choppy: {a.four_hour.is_choppy} | Peak detected: {a.four_hour.peak_formation_detected}",
            "",
            f"  1-HOUR:  Session: {a.one_hour.session_phase.value} | Trend: {a.one_hour.trend_direction.value}",
            f"           HOD={a.one_hour.hod:.5f} locked={a.one_hour.hod_locked} | LOD={a.one_hour.lod:.5f} locked={a.one_hour.lod_locked}",
            f"           50/200 cross: {a.one_hour.ema_50_200_cross} | Intraday L{a.one_hour.intraday_level}",
            "",
            f"  15-MIN:  Asian range: {a.fifteen_min.asian_range_pips:.0f} pips (valid={a.fifteen_min.accumulation_valid})",
            f"           Stop hunt: {a.fifteen_min.stop_hunt_detected} dir={a.fifteen_min.stop_hunt_direction.value} {a.fifteen_min.stop_hunt_pips:.1f}p",
            f"           Pushes: {a.fifteen_min.push_count} | M/W: {a.fifteen_min.m_w_pattern or a.fifteen_min.m_w_forming} | RRT: {a.fifteen_min.rrt_detected}",
            "",
            f"  VERDICT: {'TRADE VALID' if a.trade_valid else 'NO TRADE'}",
            f"           Direction: {a.trade_direction.value} | Confidence: {a.trade_confidence:.0%}",
            f"           Confluence: {a.confluence_score}/100",
        ]

        if a.rejection_reasons:
            lines.append(f"           Rejections: {'; '.join(a.rejection_reasons)}")

        lines.append(f"           Profile: {a.pair_profile.risk_tier} tier, {a.pair_profile.max_risk_pct*100:.1f}% risk")
        lines.append(f"{'='*60}")

        return "\n".join(lines)


def now_utc() -> datetime:
    return datetime.now(timezone.utc)
