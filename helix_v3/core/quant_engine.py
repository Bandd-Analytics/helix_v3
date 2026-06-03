"""MMMQuantitativeEngine - Mathematical pre-filtering for Market Maker Method signals.

Implements volatility compression scoring, stop-hunt detection, and EMA vector
divergence analysis against live MT5 data.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Tuple

import MetaTrader5 as mt5
import numpy as np
import pandas as pd

from config.settings import settings
from helix_v3.core.types import (
    Direction,
    EMAVector,
    QuantSignal,
    SessionBounds,
    StopHuntSignal,
)
from helix_v3.utils.logger import get_logger

logger = get_logger("quant_engine")

# MT5 timeframe mapping
TF_MAP: Dict[str, int] = {
    "M1": mt5.TIMEFRAME_M1,
    "M5": mt5.TIMEFRAME_M5,
    "M15": mt5.TIMEFRAME_M15,
    "M30": mt5.TIMEFRAME_M30,
    "H1": mt5.TIMEFRAME_H1,
    "H4": mt5.TIMEFRAME_H4,
    "D1": mt5.TIMEFRAME_D1,
}


class MMMQuantitativeEngine:
    """Core quantitative engine for Market Maker Method signal generation.

    Interfaces with MT5 to fetch OHLCV data and applies mathematical constraints:
    - Asian session volatility compression scoring
    - Post-session stop-hunt detection with mean-reversion Z-scores
    - Multi-period EMA vector divergence analysis
    """

    def __init__(self) -> None:
        self._connected: bool = False
        self._cfg = settings.trading
        self._ema_periods: List[int] = self._cfg.ema_periods

    # ------------------------------------------------------------------
    # MT5 Connection
    # ------------------------------------------------------------------

    def connect(self) -> bool:
        if self._connected:
            return True

        mt5_cfg = settings.mt5
        init_kwargs: dict = {}
        if mt5_cfg.path:
            init_kwargs["path"] = mt5_cfg.path
        if mt5_cfg.login:
            init_kwargs["login"] = mt5_cfg.login
            init_kwargs["password"] = mt5_cfg.password
            init_kwargs["server"] = mt5_cfg.server

        if not mt5.initialize(**init_kwargs):
            logger.error("MT5 initialization failed: %s", mt5.last_error())
            return False

        self._connected = True
        logger.info("MT5 connected | Account: %s", mt5.account_info().login)
        return True

    def disconnect(self) -> None:
        if self._connected:
            mt5.shutdown()
            self._connected = False
            logger.info("MT5 disconnected")

    # ------------------------------------------------------------------
    # Data Fetching
    # ------------------------------------------------------------------

    def fetch_rates(
        self, symbol: str, timeframe: str, count: int = 1000
    ) -> pd.DataFrame:
        tf = TF_MAP.get(timeframe)
        if tf is None:
            raise ValueError(f"Unsupported timeframe: {timeframe}")

        rates = mt5.copy_rates_from_pos(symbol, tf, 0, count)
        if rates is None or len(rates) == 0:
            error = mt5.last_error()
            logger.error("Failed to fetch rates for %s %s: %s", symbol, timeframe, error)
            raise ConnectionError(f"MT5 data fetch failed: {error}")

        df = pd.DataFrame(rates)
        df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
        df.set_index("time", inplace=True)
        df.rename(
            columns={
                "open": "Open",
                "high": "High",
                "low": "Low",
                "close": "Close",
                "tick_volume": "Volume",
            },
            inplace=True,
        )
        return df

    def _get_pip_value(self, symbol: str) -> float:
        info = mt5.symbol_info(symbol)
        if info is None:
            return 0.0001
        digits = info.digits
        return 10 ** (-digits) * (10 if digits in (3, 5) else 1)

    # ------------------------------------------------------------------
    # 1. Volatility Compression Score (Asian Accumulation)
    # ------------------------------------------------------------------

    def compute_session_bounds(
        self, symbol: str, lookback_days: int = 20
    ) -> Optional[SessionBounds]:
        df_m15 = self.fetch_rates(symbol, "M15", count=lookback_days * 96 + 200)

        est_offset = timedelta(hours=-5)
        df_m15 = df_m15.copy()
        df_m15["hour_est"] = (df_m15.index + est_offset).hour

        asian_start = self._cfg.asian_session_start
        asian_end = self._cfg.asian_session_end

        # Current session mask: 21:00-02:00 EST (wraps midnight)
        if asian_start > asian_end:
            current_mask = (df_m15["hour_est"] >= asian_start) | (
                df_m15["hour_est"] < asian_end
            )
        else:
            current_mask = (df_m15["hour_est"] >= asian_start) & (
                df_m15["hour_est"] < asian_end
            )

        asian_bars = df_m15[current_mask]
        if asian_bars.empty:
            logger.warning("No Asian session bars found for %s", symbol)
            return None

        # Get today's session
        today = asian_bars.index.max().date()
        today_mask = asian_bars.index.date == today
        today_session = asian_bars[today_mask]

        if today_session.empty:
            yesterday = today - timedelta(days=1)
            today_mask = asian_bars.index.date >= yesterday
            today_session = asian_bars[today_mask].tail(20)

        session_high: float = today_session["High"].max()
        session_low: float = today_session["Low"].min()
        pip_val = self._get_pip_value(symbol)
        range_pips = (session_high - session_low) / pip_val

        # Rolling volatility: std of range per session over lookback
        df_m15["bar_range"] = df_m15["High"] - df_m15["Low"]
        asian_ranges = df_m15.loc[current_mask, "bar_range"]

        # Group by date for daily session ranges
        asian_ranges_grouped = asian_ranges.groupby(asian_ranges.index.date)
        daily_session_ranges = asian_ranges_grouped.sum()

        if len(daily_session_ranges) < 5:
            vol_compression = 1.0
        else:
            current_range = daily_session_ranges.iloc[-1]
            percentile_threshold = np.percentile(
                daily_session_ranges.values, self._cfg.accumulation_percentile * 100
            )
            vol_compression = float(current_range / daily_session_ranges.mean()) if daily_session_ranges.mean() > 0 else 1.0

        is_accumulation = vol_compression <= self._cfg.accumulation_percentile

        return SessionBounds(
            high=session_high,
            low=session_low,
            range_pips=range_pips,
            volatility_compression=vol_compression,
            is_accumulation=is_accumulation,
            timestamp=datetime.now(timezone.utc),
        )

    # ------------------------------------------------------------------
    # 2. Stop-Hunt Detection
    # ------------------------------------------------------------------

    def detect_stop_hunt(
        self,
        symbol: str,
        session: SessionBounds,
    ) -> Optional[StopHuntSignal]:
        df_m1 = self.fetch_rates(symbol, "M1", count=120)
        pip_val = self._get_pip_value(symbol)

        latest = df_m1.iloc[-1]
        current_high = latest["High"]
        current_low = latest["Low"]

        breach_above = (current_high - session.high) / pip_val
        breach_below = (session.low - current_low) / pip_val

        min_pips = self._cfg.stop_hunt_min_pips
        max_pips = self._cfg.stop_hunt_max_pips

        direction: Optional[Direction] = None
        breach_pips: float = 0.0

        if min_pips <= breach_above <= max_pips:
            direction = Direction.SELL  # stop hunt above -> expect reversal down
            breach_pips = breach_above
        elif min_pips <= breach_below <= max_pips:
            direction = Direction.BUY  # stop hunt below -> expect reversal up
            breach_pips = breach_below

        if direction is None:
            return None

        # Mean-reversion Z-score on M1 closes
        closes = df_m1["Close"].values
        rolling_mean = np.mean(closes[-60:])
        rolling_std = np.std(closes[-60:])

        if rolling_std < 1e-10:
            return None

        z_score = (closes[-1] - rolling_mean) / rolling_std

        # Absorption: price spiked out but Z-score shows mean reversion starting
        is_absorption = abs(z_score) > 1.5

        logger.info(
            "Stop hunt detected %s | dir=%s breach=%.1f pips z=%.2f absorption=%s",
            symbol, direction.value, breach_pips, z_score, is_absorption,
        )

        return StopHuntSignal(
            direction=direction,
            breach_pips=breach_pips,
            z_score=float(z_score),
            is_absorption=is_absorption,
            timestamp=datetime.now(timezone.utc),
        )

    # ------------------------------------------------------------------
    # 3. EMA Vector Divergence
    # ------------------------------------------------------------------

    def compute_ema_vectors(
        self, symbol: str, timeframe: str = "M15"
    ) -> EMAVector:
        df = self.fetch_rates(symbol, timeframe, count=1000)
        closes = df["Close"]

        emas: Dict[int, pd.Series] = {}
        for period in self._ema_periods:
            emas[period] = closes.ewm(span=period, adjust=False).mean()

        def _angle(series: pd.Series, lookback: int = 5) -> float:
            if len(series) < lookback + 1:
                return 0.0
            delta = series.iloc[-1] - series.iloc[-lookback - 1]
            return float(np.degrees(np.arctan2(delta, lookback)))

        angles = {p: _angle(emas[p]) for p in self._ema_periods}

        # Fast/slow divergence: angle between 5 EMA and 200 EMA
        fast_slow_div = angles[5] - angles[200]

        # Trend alignment: all EMAs stacked in same direction
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
            fast_slow_divergence=fast_slow_div,
            trend_alignment=trend,
        )

    # ------------------------------------------------------------------
    # Combined Signal
    # ------------------------------------------------------------------

    def generate_signal(
        self, symbol: str, timeframe: str = "M15"
    ) -> QuantSignal:
        session = self.compute_session_bounds(symbol)
        stop_hunt: Optional[StopHuntSignal] = None

        if session is not None:
            stop_hunt = self.detect_stop_hunt(symbol, session)

        ema_vec = self.compute_ema_vectors(symbol, timeframe)

        accumulation_active = session.is_accumulation if session else False
        stop_hunt_detected = stop_hunt is not None and stop_hunt.is_absorption

        pre_filter_passed = accumulation_active and stop_hunt_detected

        signal = QuantSignal(
            symbol=symbol,
            timeframe=timeframe,
            timestamp=datetime.now(timezone.utc),
            session_bounds=session,
            stop_hunt=stop_hunt,
            ema_vector=ema_vec,
            accumulation_active=accumulation_active,
            stop_hunt_detected=stop_hunt_detected,
            pre_filter_passed=pre_filter_passed,
        )

        logger.info(
            "Signal %s %s | accum=%s hunt=%s filter=%s trend=%s",
            symbol, timeframe,
            accumulation_active, stop_hunt_detected,
            pre_filter_passed, ema_vec.trend_alignment.value,
        )

        return signal
