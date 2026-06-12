"""ATR(20, D1) — the universal gate scale (audit Tier 2.3).

Every pip-denominated gate in the system is a ratio of this number
(see config.pair_profiles.GATE_RATIOS / resolve_profile). The live and
backtest pipelines share d1_atr_pips() — it reads through the quant
engine, so in backtest mode the data store serves only closed bars
as-of decision time (Tier 1.1, no look-ahead). The gatekeeper talks to
MT5 directly and uses d1_atr_pips_mt5() with a short TTL cache.
"""
from __future__ import annotations

import time
from typing import Optional

import pandas as pd

from helix_v3.core.instruments import fallback_pip_size, pip_size_from_digits
from helix_v3.core.tdi import _wilder_atr

ATR_PERIOD = 20


def _atr_pips(df: pd.DataFrame, pip_size: float, period: int) -> Optional[float]:
    if df is None or len(df) < period + 1 or pip_size <= 0:
        return None
    atr = float(_wilder_atr(df["High"], df["Low"], df["Close"], period).iloc[-1])
    return atr / pip_size if atr > 0 else None


def d1_atr_pips(engine, symbol: str, period: int = ATR_PERIOD) -> Optional[float]:
    """ATR(period, D1) in pips via a quant engine (live MT5 or backtest store).

    Returns None when data is unavailable — callers fall back to the
    static profile values.
    """
    try:
        df = engine.fetch_rates(symbol, "D1", period + 10)
        return _atr_pips(df, engine._get_pip_value(symbol), period)
    except Exception:
        return None


# Gatekeeper path: raw MT5, cached. D1 ATR moves once per day; the manage
# loop runs every few seconds and must not hammer the terminal.
_mt5_cache: dict[str, tuple[float, float]] = {}
_MT5_CACHE_TTL_SEC = 600.0


def d1_atr_pips_mt5(symbol: str, period: int = ATR_PERIOD) -> Optional[float]:
    """ATR(period, D1) in pips straight from MT5, ~10-minute cache."""
    now = time.monotonic()
    hit = _mt5_cache.get(symbol)
    if hit is not None and now - hit[0] < _MT5_CACHE_TTL_SEC:
        return hit[1]

    try:
        import MetaTrader5 as mt5

        # Position 1: skip the forming daily bar (same rule as Tier 1.1).
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_D1, 1, period + 10)
        if rates is None or len(rates) < period + 1:
            return None
        df = pd.DataFrame(rates).rename(
            columns={"high": "High", "low": "Low", "close": "Close"}
        )
        info = mt5.symbol_info(symbol)
        if info is not None:
            pip = pip_size_from_digits(point=float(info.point), digits=int(info.digits))
        else:
            pip = fallback_pip_size(symbol)
        val = _atr_pips(df, pip, period)
    except Exception:
        return None

    if val is not None:
        _mt5_cache[symbol] = (now, val)
    return val
