"""Two-state market regime filter (audit Tier 2.8).

MMM's accumulate -> hunt -> reverse cycle assumes a range-cycling market
with normal volatility. Two cheap D1 measures decide whether those
conditions are PRESENT or ABSENT before any pair-level logic runs:

1. Realized-vol percentile — ATR(20, D1) ranked against its own trailing
   year. Dead vol (< P10): no accumulation worth hunting. Crisis vol
   (> P95): stops get run far beyond any "hunt" geometry.
2. Trendiness — Kaufman efficiency ratio of the last 20 daily closes
   (|net move| / sum of |daily moves|). A one-way market (ER > 0.50)
   does not cycle back through the Asian range; M/W reversal logic is
   the wrong tool there.

Reads D1 through the quant engine, so backtests see it as-of decision
time (Tier 1.1). Results are cached per (symbol, last D1 bar) — the
state can only change once per day. Fails OPEN on missing data (a data
hiccup must not silently halt live trading; it logs instead).

Toggle: REGIME_FILTER env (default true).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Tuple

from helix_v3.core.tdi import _wilder_atr
from helix_v3.utils.logger import get_logger

logger = get_logger("regime")

REGIME_LOOKBACK_DAYS = 252   # trailing distribution for the vol percentile
ER_WINDOW = 20               # efficiency-ratio window (trading days)
VOL_PCT_MIN = 0.10           # below: dead market, nothing to hunt
VOL_PCT_MAX = 0.95           # above: crisis vol, hunt geometry meaningless
ER_MAX = 0.50                # above: one-way market, cycle logic broken


@dataclass(frozen=True)
class RegimeState:
    mmm_present: bool
    vol_percentile: float
    efficiency_ratio: float
    reason: str


_cache: Dict[str, Tuple[object, RegimeState]] = {}  # symbol -> (last D1 bar ts, state)


def _fail_open(reason: str) -> RegimeState:
    return RegimeState(True, 0.5, 0.0, reason)


def assess_regime(engine, symbol: str) -> RegimeState:
    """PRESENT/ABSENT verdict for MMM conditions on this symbol today."""
    try:
        df = engine.fetch_rates(symbol, "D1", REGIME_LOOKBACK_DAYS + ER_WINDOW + 10)
    except Exception as e:
        logger.warning("Regime data fetch failed for %s: %s — failing open", symbol, e)
        return _fail_open("regime data unavailable — fail open")

    if df is None or len(df) < ER_WINDOW + 30:
        logger.warning(
            "Regime: insufficient D1 history for %s (%d bars) — failing open",
            symbol, 0 if df is None else len(df),
        )
        return _fail_open("insufficient D1 history — fail open")

    last_ts = df.index[-1]
    hit = _cache.get(symbol)
    if hit is not None and hit[0] == last_ts:
        return hit[1]

    # 1. Realized-vol percentile: today's ATR(20) vs its trailing year
    atr = _wilder_atr(df["High"], df["Low"], df["Close"], 20).dropna()
    hist = atr.iloc[-min(len(atr), REGIME_LOOKBACK_DAYS):]
    current_atr = float(hist.iloc[-1])
    # Mid-rank percentile (ties split) — strict <= would pin a flat
    # distribution's latest value to P100.
    vol_pct = float((hist < current_atr).mean() + 0.5 * (hist == current_atr).mean())

    # 2. Trendiness: Kaufman efficiency ratio over the last ER_WINDOW days
    closes = df["Close"].iloc[-(ER_WINDOW + 1):]
    net = abs(float(closes.iloc[-1]) - float(closes.iloc[0]))
    path = float(closes.diff().abs().sum())
    er = net / path if path > 0 else 0.0

    reasons = []
    if vol_pct < VOL_PCT_MIN:
        reasons.append(f"dead vol (P{vol_pct * 100:.0f} < P{VOL_PCT_MIN * 100:.0f})")
    if vol_pct > VOL_PCT_MAX:
        reasons.append(f"crisis vol (P{vol_pct * 100:.0f} > P{VOL_PCT_MAX * 100:.0f})")
    if er > ER_MAX:
        reasons.append(f"one-way market (ER {er:.2f} > {ER_MAX:.2f})")

    state = RegimeState(
        mmm_present=not reasons,
        vol_percentile=round(vol_pct, 3),
        efficiency_ratio=round(er, 3),
        reason="; ".join(reasons) if reasons else
        f"MMM conditions present (vol P{vol_pct * 100:.0f}, ER {er:.2f})",
    )
    _cache[symbol] = (last_ts, state)
    return state
