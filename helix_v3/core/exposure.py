"""Portfolio currency-exposure cap (audit Tier 2.6).

Three GBP longs at 0.8% each are not three independent trades — one GBP
news candle is a ~2.4% correlated loss. This module measures NET signed
risk per currency across open positions and blocks a new entry when it
would push any currency it touches beyond the cap.

Semantics:
- BUY EURUSD = long EUR / short USD; SELL GBPJPY = short GBP / long JPY.
- XAUUSD = XAU vs USD (a gold long is a USD short for news purposes).
- Index symbols (US30/USTEC/US500) occupy only their own bucket — their
  USD sensitivity is not a clean FX short.
- Exposure is NET: a GBPUSD long and a GBPJPY short offset in GBP.
- Risk per position = loss at its CURRENT stop (a breakeven stop = 0) —
  protected positions don't consume the cap.
- A new entry is blocked only if it WORSENS the violating bucket; an
  offsetting trade is always allowed.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Iterable, Optional

from helix_v3.core.types import Direction

_INDEX_SYMBOLS = {"US30", "USTEC", "US500", "DE40", "UK100"}


@dataclass(frozen=True)
class OpenRisk:
    """One open position's contribution: symbol, direction, risk fraction."""
    symbol: str
    direction: Direction
    risk_pct: float  # potential loss at current stop / equity, >= 0


def currency_risk(symbol: str, direction: Direction, risk_pct: float) -> Dict[str, float]:
    """Signed per-currency risk of one position. Long base = +, short = -."""
    sign = 1.0 if direction == Direction.BUY else -1.0
    risk = max(0.0, risk_pct)
    if symbol in _INDEX_SYMBOLS:
        return {symbol: sign * risk}
    base, quote = symbol[:3].upper(), symbol[3:6].upper()
    if not quote:
        return {base or symbol: sign * risk}
    return {base: sign * risk, quote: -sign * risk}


def exposure_violation(
    symbol: str,
    direction: Direction,
    risk_pct: float,
    open_risks: Iterable[OpenRisk],
    cap_pct: float,
) -> Optional[str]:
    """Reason the new entry breaches the per-currency cap, or None if it fits.

    Sums signed exposure per currency over open positions plus the
    candidate. A bucket over `cap_pct` only blocks when the candidate's
    own contribution pushes in the violating direction.
    """
    totals: Dict[str, float] = defaultdict(float)
    for pos in open_risks:
        for ccy, signed in currency_risk(pos.symbol, pos.direction, pos.risk_pct).items():
            totals[ccy] += signed

    new_contrib = currency_risk(symbol, direction, risk_pct)
    for ccy, signed in new_contrib.items():
        totals[ccy] += signed

    for ccy, signed in new_contrib.items():
        net = totals[ccy]
        if abs(net) > cap_pct + 1e-9 and net * signed > 0:
            return (
                f"{ccy} net exposure {net * 100:+.1f}% would exceed cap "
                f"{cap_pct * 100:.1f}% (new {symbol} {direction.value} adds "
                f"{signed * 100:+.1f}%)"
            )
    return None
