"""Historical data store for offline backtesting.

Pre-fetches all required timeframes from MT5 for a date range, then serves
sliced DataFrames to BacktestEngine.fetch_rates() without further MT5 calls.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Dict, List, Tuple

import MetaTrader5 as mt5
import pandas as pd

from config.settings import settings
from helix_v3.core.instruments import fallback_pip_size, pip_size_from_digits
from helix_v3.utils.logger import get_logger

logger = get_logger("backtest_data_store")

TIMEFRAMES = {
    "M15": (mt5.TIMEFRAME_M15, 15),
    "H1": (mt5.TIMEFRAME_H1, 60),
    "H4": (mt5.TIMEFRAME_H4, 240),
    "D1": (mt5.TIMEFRAME_D1, 1440),
}

# Extra bars to pre-fetch before start_date so indicators have warm-up data
WARMUP_BARS = {
    "M15": 400,   # ~4 days of M15 bars for EMAs/TDI
    "H1": 200,    # ~8 days
    "H4": 200,    # ~33 days for 800 EMA
    "D1": 200,    # ~200 days for long EMAs
}


class HistoricalDataStore:
    """Pre-fetches and caches historical OHLCV for offline replay."""

    def __init__(
        self,
        symbols: List[str],
        start_date: datetime,
        end_date: datetime,
    ) -> None:
        self._symbols = symbols
        self._start = start_date.replace(tzinfo=timezone.utc) if start_date.tzinfo is None else start_date
        self._end = end_date.replace(tzinfo=timezone.utc) if end_date.tzinfo is None else end_date
        self._cache: Dict[Tuple[str, str], pd.DataFrame] = {}
        self._pip_sizes: Dict[str, float] = {}
        self._tick_values: Dict[str, float] = {}
        self._symbol_digits: Dict[str, int] = {}

    def load(self) -> None:
        """Fetch all data from MT5 into memory. Call once before backtesting."""
        mt5_cfg = settings.mt5
        init_kwargs: dict = {}
        if mt5_cfg.path:
            init_kwargs["path"] = mt5_cfg.path
        if mt5_cfg.login:
            init_kwargs["login"] = mt5_cfg.login
            init_kwargs["password"] = mt5_cfg.password
            init_kwargs["server"] = mt5_cfg.server

        if not mt5.initialize(**init_kwargs):
            raise ConnectionError(f"MT5 initialization failed: {mt5.last_error()}")

        try:
            for symbol in self._symbols:
                self._cache_symbol_info(symbol)
                for tf_name, (tf_mt5, tf_minutes) in TIMEFRAMES.items():
                    self._fetch_timeframe(symbol, tf_name, tf_mt5, tf_minutes)

            total_bars = sum(len(df) for df in self._cache.values())
            logger.info(
                "Data store loaded: %d symbols, %d timeframes, %d total bars",
                len(self._symbols), len(TIMEFRAMES), total_bars,
            )
        finally:
            mt5.shutdown()

    def _cache_symbol_info(self, symbol: str) -> None:
        info = mt5.symbol_info(symbol)
        if info is None:
            logger.warning("Symbol info not available for %s, using defaults", symbol)
            self._pip_sizes[symbol] = fallback_pip_size(symbol)
            self._tick_values[symbol] = 1.0
            self._symbol_digits[symbol] = 3 if "JPY" in symbol else 5
            return

        if not info.visible:
            mt5.symbol_select(symbol, True)
            info = mt5.symbol_info(symbol)

        digits = info.digits
        point = info.point
        pip_size = pip_size_from_digits(point=float(point), digits=int(digits))
        self._pip_sizes[symbol] = pip_size
        self._tick_values[symbol] = info.trade_tick_value
        self._symbol_digits[symbol] = digits

    def _fetch_timeframe(
        self, symbol: str, tf_name: str, tf_mt5: int, tf_minutes: int
    ) -> None:
        warmup = WARMUP_BARS.get(tf_name, 200)
        fetch_start = self._start - timedelta(minutes=tf_minutes * warmup)

        rates = mt5.copy_rates_range(symbol, tf_mt5, fetch_start, self._end)
        if rates is None or len(rates) == 0:
            logger.warning(
                "No data for %s %s (%s to %s)",
                symbol, tf_name, fetch_start.isoformat(), self._end.isoformat(),
            )
            self._cache[(symbol, tf_name)] = pd.DataFrame()
            return

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
        self._cache[(symbol, tf_name)] = df
        logger.info("Loaded %s %s: %d bars (%s to %s)",
                     symbol, tf_name, len(df),
                     df.index[0].isoformat(), df.index[-1].isoformat())

    def get_rates(
        self, symbol: str, timeframe: str, as_of: datetime, count: int
    ) -> pd.DataFrame:
        """Return `count` bars ending at or before `as_of`."""
        key = (symbol, timeframe)
        df = self._cache.get(key)
        if df is None or df.empty:
            return pd.DataFrame()

        as_of_ts = pd.Timestamp(as_of).tz_localize("UTC") if as_of.tzinfo is None else pd.Timestamp(as_of)
        mask = df.index <= as_of_ts
        sliced = df.loc[mask]
        if len(sliced) > count:
            sliced = sliced.iloc[-count:]
        return sliced.copy()

    def get_pip_size(self, symbol: str) -> float:
        return self._pip_sizes.get(symbol, 0.0001)

    def get_tick_value(self, symbol: str) -> float:
        return self._tick_values.get(symbol, 1.0)

    def get_digits(self, symbol: str) -> int:
        return self._symbol_digits.get(symbol, 5)

    def get_m15_timestamps(self, symbol: str) -> pd.DatetimeIndex:
        """Return all M15 bar timestamps within the backtest window."""
        key = (symbol, "M15")
        df = self._cache.get(key)
        if df is None or df.empty:
            return pd.DatetimeIndex([])
        start_ts = pd.Timestamp(self._start).tz_localize("UTC") if self._start.tzinfo is None else pd.Timestamp(self._start)
        end_ts = pd.Timestamp(self._end).tz_localize("UTC") if self._end.tzinfo is None else pd.Timestamp(self._end)
        mask = (df.index >= start_ts) & (df.index <= end_ts)
        return df.index[mask]

    @property
    def symbols(self) -> List[str]:
        return list(self._symbols)

    @property
    def start_date(self) -> datetime:
        return self._start

    @property
    def end_date(self) -> datetime:
        return self._end
