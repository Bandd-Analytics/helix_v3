"""Multi-asset breadth research — Forward Plan Track 3c (the closing test).

3a (FX entry signals) and 3b (management-as-alpha) both found NO edge — but
both lived in FX majors, the most efficient, least-trending liquid market on
earth. The one systematic edge with a strong out-of-sample prior — time-series
(absolute) momentum (Moskowitz-Ooi-Pedersen; AQR) — is documented WEAKEST in FX
and STRONGEST in commodities, equity indices, and crypto. 3c tests exactly that
hypothesis, and ONLY that, on a deliberately NARROW instrument set so the
multiple-testing surface stays tiny (the plan flags broad CFD breadth as the
overfit trap — we avoid it).

Discipline (Forward Plan guardrail):
  - ONE signal, theory-specified, no sweep: D1 time-series momentum — direction
    = sign of the trailing `lookback`-bar return; hold `holding` bars. Bars, not
    calendar (CFD weeks differ: crypto 7d, indices 5d) — a single pre-registered
    construct.
  - Momentum is a holding-period premium (like carry), so it is scored with the
    holding-return labeler, not a tight bracket.
  - Costs are INSTRUMENT-APPROPRIATE and data-driven: cost_r derived per symbol
    from live MT5 spread / ATR (round-trip), NOT a guessed constant — so crypto's
    wide spreads are charged honestly. A survivor that only works on optimistic
    costs is not a survivor.
  - Same gauntlet as every family: non-overlap, binomial + expectancy, BH across
    the whole grid (per-instrument cells + one pooled equal-weight TSMOM cell),
    embargoed 2025-26 holdout.

A survivor is re-run through the production TradeSimulator before it may advance
to Track 2 forward demo. The honest prior is that this dies too — but if it
does, the edge hunt closes on a COMPLETE negative (FX entry + FX management +
cross-asset momentum) rather than a narrow one.

Offline research only — records nothing, gates nothing.
"""
from __future__ import annotations

import argparse
from datetime import datetime
from typing import List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

from helix_v3.backtest.signal_research import (
    ATR_PERIOD,
    IN_SAMPLE_END,
    K_ATR,
    MIN_CELL_N,
    CellResult,
    _expectancy_p,
    _grade,
    _label_holding_return,
    _make_cell,
    atr,
    fetch_bars,
    format_report,
)

# Narrow, pre-committed universe — broker-confirmed names (this ICMarkets feed
# uses USTEC for Nasdaq and DE40 for the DAX). Trending asset classes only; NO
# single stocks (that is the breadth overfit trap the plan warns against).
CANDIDATE_SYMBOLS = [
    "US500", "USTEC", "DE40",     # equity index CFDs
    "XAUUSD",                       # gold (commodity)
    "BTCUSD", "ETHUSD",            # crypto
]

DEFAULT_TIMEFRAME = "D1"
LOOKBACK = 120        # momentum formation window (bars) — single committed value
HOLDING = 20          # holding horizon (bars)
N_BARS = 2000
COST_R_FLOOR = 0.02   # never assume a cost below this even if spread is tight


def tsmom_entries(df: pd.DataFrame, lookback: int = LOOKBACK, holding: int = HOLDING
                  ) -> List[Tuple[int, str]]:
    """Time-series momentum: every `holding` bars, go with the sign of the
    trailing `lookback`-bar return. Non-overlap is enforced in the labeler.
    """
    close = df["Close"].values
    out: List[Tuple[int, str]] = []
    for i in range(lookback, len(df) - holding, holding):
        past = close[i - lookback]
        if past <= 0 or np.isnan(past):
            continue
        out.append((i, "BUY" if close[i] > past else "SELL"))
    return out


def _median_spread_points(symbol: str, timeframe: str, n_bars: int) -> Optional[float]:
    """Median per-bar spread (in points) over recent history.

    MT5 rate bars carry a `spread` field — its median is a far more robust cost
    input than the live quote, which reads 0 when the market is closed (several
    of these CFDs were closed at probe time). Returns None if unavailable.
    """
    import MetaTrader5 as mt5
    tf_map = {"M15": mt5.TIMEFRAME_M15, "H1": mt5.TIMEFRAME_H1,
              "H4": mt5.TIMEFRAME_H4, "D1": mt5.TIMEFRAME_D1}
    rates = mt5.copy_rates_from_pos(symbol, tf_map[timeframe], 0, n_bars)
    if rates is None or len(rates) == 0 or "spread" not in rates.dtype.names:
        return None
    spreads = np.asarray(rates["spread"], dtype=float)
    spreads = spreads[spreads > 0]
    return float(np.median(spreads)) if len(spreads) else None


def instrument_cost_r(symbol: str, atr_price: float,
                      timeframe: str = DEFAULT_TIMEFRAME, n_bars: int = N_BARS) -> float:
    """Round-trip spread as a fraction of the 1xATR stop — instrument-appropriate.

    cost_r = 2 x (median_spread_points x point) / (K_ATR x ATR_price), using the
    MEDIAN HISTORICAL spread (robust to the closed-market snapshot), floored at
    COST_R_FLOOR. Data-driven, not a guessed constant; deliberately the spread a
    survivor must overcome, so optimism can't manufacture an edge.
    """
    import MetaTrader5 as mt5
    info = mt5.symbol_info(symbol)
    if info is None or atr_price <= 0:
        return COST_R_FLOOR
    med_pts = _median_spread_points(symbol, timeframe, n_bars)
    if med_pts is None:
        med_pts = float(info.spread)         # fall back to the live snapshot
    spread_price = med_pts * info.point
    cost = 2.0 * spread_price / (K_ATR * atr_price)
    return max(COST_R_FLOOR, float(cost))


def _resolve_universe(symbols: Sequence[str], timeframe: str, n_bars: int
                      ) -> List[Tuple[str, pd.DataFrame]]:
    import MetaTrader5 as mt5
    out: List[Tuple[str, pd.DataFrame]] = []
    for s in symbols:
        if mt5.symbol_info(s) is None:
            continue
        mt5.symbol_select(s, True)
        df = fetch_bars(s, timeframe, n_bars)
        if not df.empty and len(df) >= LOOKBACK + HOLDING + 60:
            out.append((s, df))
    return out


def audit_multiasset(
    symbols: Sequence[str] = CANDIDATE_SYMBOLS, timeframe: str = DEFAULT_TIMEFRAME,
    n_bars: int = N_BARS, lookback: int = LOOKBACK, holding: int = HOLDING,
) -> List[CellResult]:
    import MetaTrader5 as mt5
    mt5.initialize()
    universe = _resolve_universe(symbols, timeframe, n_bars)
    if not universe:
        return []

    results: List[CellResult] = []
    pooled: List[Tuple[datetime, bool, float]] = []
    pooled_base_pos = pooled_base_n = 0

    for symbol, df in universe:
        a = atr(df)
        cost_r = instrument_cost_r(symbol, float(a.dropna().iloc[-1]), timeframe, n_bars)
        entries = tsmom_entries(df, lookback, holding)
        labels = _label_holding_return(
            df, a, entries, pip_size=1.0, cost_r=cost_r, horizon=holding)
        # control: unconditional BUY H-bar holding return positive rate
        ctrl = _label_holding_return(
            df, a, [(i, "BUY") for i in range(lookback, len(df) - holding, holding)],
            pip_size=1.0, cost_r=cost_r, horizon=holding)
        ctrl_in = [c for c in ctrl if c[0] < IN_SAMPLE_END]
        base_rate = (sum(f for _, f, _ in ctrl_in) / len(ctrl_in)) if ctrl_in else 0.0
        results.append(_make_cell(f"tsmom_{lookback}", symbol, labels, base_rate))

        pooled.extend(labels)
        pooled_base_pos += sum(f for _, f, _ in ctrl_in)
        pooled_base_n += len(ctrl_in)

    pooled_base = pooled_base_pos / pooled_base_n if pooled_base_n else 0.0
    results.append(_make_cell(f"tsmom_{lookback}", "POOLED", pooled, pooled_base))
    return _grade(results)


def audit_alpha_vs_buyhold(
    symbols: Sequence[str] = CANDIDATE_SYMBOLS, timeframe: str = DEFAULT_TIMEFRAME,
    n_bars: int = N_BARS, lookback: int = LOOKBACK, holding: int = HOLDING,
) -> str:
    """The CORRECT test: does TSMOM beat BUY-AND-HOLD, not zero?

    The raw audit's expectancy test uses a zero null — trivially passed by assets
    with upward drift. The only thing that counts as an edge is outperformance vs
    passively holding the same instruments. Per entry bar, diff = tsmom_r −
    buy_hold_r (identical bars, ATR, cost); diff is nonzero only when momentum
    flips SHORT, so this measures whether momentum's short calls actually pay.
    Reports per-instrument and pooled mean diff, one-sided t-test p, and the
    embargoed-holdout mean diff.
    """
    import MetaTrader5 as mt5
    mt5.initialize()
    universe = _resolve_universe(symbols, timeframe, n_bars)

    def _stats(diffs):
        rs = [d for _, d in diffs]
        n = len(rs)
        mean = sum(rs) / n if n else 0.0
        p = _expectancy_p(rs) if n >= MIN_CELL_N else None
        return n, mean, p

    lines = [
        "",
        "## Benchmark-relative test — TSMOM vs BUY-AND-HOLD (the correct null)",
        "",
        f"diff = tsmom_r - buyhold_r per entry (lookback {lookback}, holding {holding}, "
        "same ATR/cost). Edge requires mean diff > 0 in-sample (BH-significant) AND a "
        "positive holdout mean diff.",
        "",
        "| sym | n_in | mean_diff_in | p_in | n_hold | mean_diff_hold |",
        "|---|--:|--:|--:|--:|--:|",
    ]
    pooled_in, pooled_hold = [], []
    for symbol, df in universe:
        a = atr(df)
        cost_r = instrument_cost_r(symbol, float(a.dropna().iloc[-1]), timeframe, n_bars)
        bars = list(range(lookback, len(df) - holding, holding))
        ts = {t: r for t, _, r in _label_holding_return(
            df, a, tsmom_entries(df, lookback, holding),
            pip_size=1.0, cost_r=cost_r, horizon=holding)}
        bh = {t: r for t, _, r in _label_holding_return(
            df, a, [(i, "BUY") for i in bars],
            pip_size=1.0, cost_r=cost_r, horizon=holding)}
        diffs = [(t, ts[t] - bh[t]) for t in ts if t in bh]
        din = [(t, d) for t, d in diffs if t < IN_SAMPLE_END]
        dho = [(t, d) for t, d in diffs if t >= IN_SAMPLE_END]
        pooled_in += din
        pooled_hold += dho
        n_i, m_i, p_i = _stats(din)
        n_h, m_h, _ = _stats(dho)
        ps = f"{p_i:.3f}" if p_i is not None else "—"
        lines.append(
            f"| {symbol} | {n_i} | {m_i:+.3f} | {ps} | {n_h} | {m_h:+.3f} |")

    n_i, m_i, p_i = _stats(pooled_in)
    n_h, m_h, _ = _stats(pooled_hold)
    ps = f"{p_i:.3f}" if p_i is not None else "—"
    lines.append(f"| **POOLED** | {n_i} | {m_i:+.3f} | {ps} | {n_h} | {m_h:+.3f} |")
    edge = (p_i is not None and p_i < 0.05 and m_i > 0 and m_h > 0)
    lines += ["", f"**Alpha over buy-and-hold: {'YES' if edge else 'NO'}** "
              f"(pooled mean diff in={m_i:+.3f}, holdout={m_h:+.3f})."]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="Track 3c multi-asset momentum audit")
    ap.add_argument("--timeframe", default=DEFAULT_TIMEFRAME)
    ap.add_argument("--bars", type=int, default=N_BARS)
    ap.add_argument("--lookback", type=int, default=LOOKBACK)
    ap.add_argument("--holding", type=int, default=HOLDING)
    ap.add_argument("--out", default="logs/multiasset_research.md")
    args = ap.parse_args()
    results = audit_multiasset(
        timeframe=args.timeframe, n_bars=args.bars,
        lookback=args.lookback, holding=args.holding)
    md = format_report(results, args.timeframe).replace(
        "Track 3a — FX non-MMM signal audit",
        "Track 3c — multi-asset time-series momentum audit").replace(
        f"bracket {K_ATR}xATR 1:1 | horizon 12 bars",
        f"TSMOM lookback {args.lookback} | holding {args.holding} bars (holding-return)")
    md += "\n" + audit_alpha_vs_buyhold(
        timeframe=args.timeframe, n_bars=args.bars,
        lookback=args.lookback, holding=args.holding)
    from pathlib import Path
    Path(args.out).write_text(md, encoding="utf-8")
    print(md.encode("ascii", "replace").decode("ascii"))   # console may be cp1252
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
