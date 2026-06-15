"""FX non-MMM signal research — Edge Discovery / Forward Plan Track 3a.

MMM has no validated directional edge (Edge Discovery Phase 1). This harness
tests whether ANY classic, non-MMM signal family does — on the same liquid FX
majors, under the same gauntlet that killed the MMM rules and signatures:

  - first-touch / path-ordered labeling (rule_stats.first_touch_outcome — stop
    wins same-bar ambiguity)
  - per-entry ATR brackets (target = stop = k×ATR, symmetric 1:1)
  - non-overlapping samples (one trade per horizon window)
  - exact binomial test of the signal's favorable rate vs the UNCONDITIONAL
    first-touch rate with the identical bracket/horizon (the control)
  - one-sided expectancy test in net R-multiples (after a round-trip cost)
  - Benjamini-Hochberg across the whole signal×pair grid
  - embargoed walk-forward: in-sample BH-significant + positive net-R AND
    replicates on the held-out window

Starter signal families (deliberately simple, well-studied, cheap to trade):
  - Donchian breakout (momentum)
  - MA cross (trend)
  - Z-score reversion (mean reversion)

Reads bars from MT5. Offline research only — records nothing, gates nothing.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable, Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

from helix_v3.training.rule_stats import (
    benjamini_hochberg,
    binomial_p_at_least,
    first_touch_outcome,
)

MAJORS = ["EURUSD", "GBPUSD", "AUDUSD", "USDJPY", "USDCHF", "NZDUSD", "USDCAD"]
DEFAULT_TIMEFRAME = "H4"
ATR_PERIOD = 14
K_ATR = 1.0                 # bracket = 1x ATR, symmetric (1:1 RR)
HORIZON_BARS = 12           # max bars to first touch
MIN_CELL_N = 30
MIN_HOLDOUT_N = 15
BH_Q = 0.10
COST_R_DEFAULT = 0.10       # round-trip cost as a fraction of the 1xATR stop
IN_SAMPLE_END = datetime(2025, 1, 1, tzinfo=timezone.utc)


# ---------------------------------------------------------------------------
# Bars
# ---------------------------------------------------------------------------

def fetch_bars(symbol: str, timeframe: str, n_bars: int) -> pd.DataFrame:
    """OHLC from MT5 with a UTC index. Empty frame if MT5 has no data."""
    import MetaTrader5 as mt5
    tf_map = {
        "M15": mt5.TIMEFRAME_M15, "H1": mt5.TIMEFRAME_H1,
        "H4": mt5.TIMEFRAME_H4, "D1": mt5.TIMEFRAME_D1,
    }
    rates = mt5.copy_rates_from_pos(symbol, tf_map[timeframe], 0, n_bars)
    if rates is None or len(rates) == 0:
        return pd.DataFrame()
    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
    df = df.rename(columns={"open": "Open", "high": "High", "low": "Low", "close": "Close"})
    return df.set_index("time")[["Open", "High", "Low", "Close"]]


def atr(df: pd.DataFrame, period: int = ATR_PERIOD) -> pd.Series:
    h, l, c = df["High"], df["Low"], df["Close"]
    prev = c.shift(1)
    tr = pd.concat([h - l, (h - prev).abs(), (l - prev).abs()], axis=1).max(axis=1)
    return tr.rolling(period).mean()


def pip_size_for(symbol: str) -> float:
    return 0.01 if symbol.endswith("JPY") else 0.0001


# ---------------------------------------------------------------------------
# Signals — each returns [(bar_index, "BUY"/"SELL"), ...] (entry at that close)
# ---------------------------------------------------------------------------

def donchian_breakout(df: pd.DataFrame, n: int = 20) -> List[Tuple[int, str]]:
    hi = df["High"].rolling(n).max().shift(1)
    lo = df["Low"].rolling(n).min().shift(1)
    out = []
    c = df["Close"].values
    hiv, lov = hi.values, lo.values
    for i in range(n, len(df)):
        if np.isnan(hiv[i]) or np.isnan(lov[i]):
            continue
        if c[i] > hiv[i]:
            out.append((i, "BUY"))
        elif c[i] < lov[i]:
            out.append((i, "SELL"))
    return out


def ma_cross(df: pd.DataFrame, fast: int = 20, slow: int = 50) -> List[Tuple[int, str]]:
    f = df["Close"].rolling(fast).mean().values
    s = df["Close"].rolling(slow).mean().values
    out = []
    for i in range(slow + 1, len(df)):
        if np.isnan(f[i - 1]) or np.isnan(s[i - 1]):
            continue
        if f[i - 1] <= s[i - 1] and f[i] > s[i]:
            out.append((i, "BUY"))
        elif f[i - 1] >= s[i - 1] and f[i] < s[i]:
            out.append((i, "SELL"))
    return out


def zscore_reversion(df: pd.DataFrame, lookback: int = 20, z: float = 2.0) -> List[Tuple[int, str]]:
    c = df["Close"]
    mean = c.rolling(lookback).mean()
    std = c.rolling(lookback).std()
    zs = ((c - mean) / std).values
    out = []
    for i in range(lookback, len(df)):
        if np.isnan(zs[i]):
            continue
        if zs[i] <= -z:
            out.append((i, "BUY"))     # stretched down -> fade up
        elif zs[i] >= z:
            out.append((i, "SELL"))
    return out


SIGNALS: Dict[str, Callable[[pd.DataFrame], List[Tuple[int, str]]]] = {
    "donchian20": lambda df: donchian_breakout(df, 20),
    "ma_cross_20_50": lambda df: ma_cross(df, 20, 50),
    "zscore_revert_2": lambda df: zscore_reversion(df, 20, 2.0),
}


# ---------------------------------------------------------------------------
# Labeling + audit
# ---------------------------------------------------------------------------

@dataclass
class CellResult:
    signal: str
    symbol: str
    n: int
    favorable: int
    fav_rate: float
    base_rate: float
    p_value: Optional[float]
    mean_net_r: float
    p_expectancy: Optional[float]
    bh_significant: bool = False
    bh_exp_significant: bool = False
    holdout_n: int = 0
    holdout_mean_net_r: float = 0.0
    verdict: str = ""


def _label_entries(
    df: pd.DataFrame, atr_series: pd.Series, entries: Sequence[Tuple[int, str]],
    *, pip_size: float, cost_r: float,
) -> List[Tuple[datetime, bool, float]]:
    """Return [(entry_time, favorable, net_r)] for non-overlapping entries.

    Bracket per entry = K_ATR x ATR(entry). 1:1, so net_r = +1−cost (target),
    −1−cost (stop), or the path-clipped close-to-close at expiry, minus cost.
    """
    out: List[Tuple[datetime, bool, float]] = []
    last_exit_idx = -1
    a = atr_series.values
    for i, direction in entries:
        if i <= last_exit_idx or i >= len(df) - 1 or np.isnan(a[i]) or a[i] <= 0:
            continue
        bracket_pips = (K_ATR * a[i]) / pip_size
        entry_price = float(df["Close"].iloc[i])
        ft = first_touch_outcome(
            df, i, direction, entry_price, bracket_pips, bracket_pips,
            HORIZON_BARS, pip_size,
        )
        if ft is None:
            continue
        last_exit_idx = i + ft.bars_held
        r = ft.pips_result / bracket_pips - cost_r       # net R-multiple
        favorable = ft.outcome == "TARGET"
        out.append((df.index[i].to_pydatetime(), favorable, r))
    return out


def _base_rate_labels(
    df: pd.DataFrame, atr_series: pd.Series, *, pip_size: float, cost_r: float,
) -> List[Tuple[datetime, bool, float]]:
    """Unconditional control: enter EVERY horizon-th bar, both directions."""
    entries: List[Tuple[int, str]] = []
    for i in range(ATR_PERIOD, len(df) - 1, HORIZON_BARS):
        entries.append((i, "BUY"))
    return _label_entries(df, atr_series, entries, pip_size=pip_size, cost_r=cost_r)


def _expectancy_p(rs: Sequence[float]) -> Optional[float]:
    import math
    n = len(rs)
    if n < MIN_CELL_N:
        return None
    mean = sum(rs) / n
    var = sum((r - mean) ** 2 for r in rs) / (n - 1)
    if var <= 0:
        return 0.0 if mean > 0 else 1.0
    t = mean / math.sqrt(var / n)
    return 0.5 * math.erfc(t / math.sqrt(2.0))


def _make_cell(
    signal: str, symbol: str,
    labels: Sequence[Tuple[datetime, bool, float]], base_rate: float,
) -> CellResult:
    in_s = [x for x in labels if x[0] < IN_SAMPLE_END]
    hold = [x for x in labels if x[0] >= IN_SAMPLE_END]
    n = len(in_s)
    k = sum(f for _, f, _ in in_s)
    rs = [r for _, _, r in in_s]
    hold_r = [r for _, _, r in hold]
    p = binomial_p_at_least(k, n, base_rate) if n >= MIN_CELL_N and base_rate > 0 else None
    return CellResult(
        signal=signal, symbol=symbol, n=n, favorable=k,
        fav_rate=(k / n if n else 0.0), base_rate=base_rate, p_value=p,
        mean_net_r=(sum(rs) / n if n else 0.0), p_expectancy=_expectancy_p(rs),
        holdout_n=len(hold),
        holdout_mean_net_r=(sum(hold_r) / len(hold_r)) if hold_r else 0.0,
    )


def _grade(results: List[CellResult]) -> List[CellResult]:
    """BH on both tracks + walk-forward verdict (shared by all audit paths)."""
    for r, f in zip(results, benjamini_hochberg([r.p_value for r in results], q=BH_Q)):
        r.bh_significant = f
    for r, f in zip(results, benjamini_hochberg([r.p_expectancy for r in results], q=BH_Q)):
        r.bh_exp_significant = f
    for r in results:
        if r.p_value is None:
            r.verdict = "INSUFFICIENT_N"
            continue
        edge = (r.bh_significant and r.mean_net_r > 0) or r.bh_exp_significant
        replicates = r.holdout_n >= MIN_HOLDOUT_N and r.holdout_mean_net_r > 0
        r.verdict = "VALIDATED" if (edge and replicates) else "DEAD"
    return results


def _base_rate(df: pd.DataFrame, a: pd.Series, pip: float, cost_r: float) -> float:
    base = _base_rate_labels(df, a, pip_size=pip, cost_r=cost_r)
    base_in = [b for b in base if b[0] < IN_SAMPLE_END]
    return (sum(f for _, f, _ in base_in) / len(base_in)) if base_in else 0.0


def audit(
    symbols: Sequence[str] = MAJORS, timeframe: str = DEFAULT_TIMEFRAME,
    n_bars: int = 6000, cost_r: float = COST_R_DEFAULT,
) -> List[CellResult]:
    import MetaTrader5 as mt5
    mt5.initialize()  # idempotent; harness may run as a standalone process

    results: List[CellResult] = []
    for symbol in symbols:
        df = fetch_bars(symbol, timeframe, n_bars)
        if df.empty or len(df) < 200:
            continue
        a = atr(df)
        pip = pip_size_for(symbol)
        base_rate = _base_rate(df, a, pip, cost_r)
        for sig_name, sig_fn in SIGNALS.items():
            labels = _label_entries(df, a, sig_fn(df), pip_size=pip, cost_r=cost_r)
            results.append(_make_cell(sig_name, symbol, labels, base_rate))
    return _grade(results)


def _align_closes(pair_dfs: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    # Union index — do NOT dropna across pairs (that collapses the window to
    # the shortest-history pair). Per-bar gaps are handled by the >=4 guard.
    return pd.DataFrame({s: df["Close"] for s, df in pair_dfs.items()})


def cross_sectional_momentum_entries(
    pair_dfs: Dict[str, pd.DataFrame], lookback: int = 60, top_k: int = 1,
) -> Dict[str, List[Tuple[int, str]]]:
    """Each bar: long the top_k highest-momentum pairs, short the lowest.

    Relative (cross-sectional) momentum — structurally different from the
    per-pair absolute signals. Direction is by RANK, not by an absolute level.
    """
    closes = _align_closes(pair_dfs)
    rets = closes.pct_change(lookback)
    entries: Dict[str, List[Tuple[int, str]]] = {s: [] for s in pair_dfs}
    pos = {s: {t: i for i, t in enumerate(pair_dfs[s].index)} for s in pair_dfs}
    for t, row in rets.iterrows():
        r = row.dropna()
        if len(r) < 4:
            continue
        ranked = r.sort_values()
        for s in ranked.index[-top_k:]:          # strongest -> long (continuation)
            i = pos[s].get(t)
            if i is not None:
                entries[s].append((i, "BUY"))
        for s in ranked.index[:top_k]:            # weakest -> short
            i = pos[s].get(t)
            if i is not None:
                entries[s].append((i, "SELL"))
    return entries


def audit_cross_sectional(
    symbols: Sequence[str] = MAJORS, timeframe: str = DEFAULT_TIMEFRAME,
    n_bars: int = 6000, cost_r: float = COST_R_DEFAULT, lookback: int = 60,
) -> List[CellResult]:
    import MetaTrader5 as mt5
    mt5.initialize()
    pair_dfs = {s: fetch_bars(s, timeframe, n_bars) for s in symbols}
    pair_dfs = {s: df for s, df in pair_dfs.items() if not df.empty and len(df) >= 200}
    if len(pair_dfs) < 4:
        return []
    entries_by_sym = cross_sectional_momentum_entries(pair_dfs, lookback=lookback)
    # Cross-sectional momentum is ONE strategy across the universe — pool every
    # pair's entries into a single cell (per-pair N is too sparse at top_k=1).
    # The control is the pooled unconditional base rate over the same pairs.
    pooled_labels: List[Tuple[datetime, bool, float]] = []
    base_fav, base_n = 0, 0
    for symbol, df in pair_dfs.items():
        a = atr(df)
        pip = pip_size_for(symbol)
        pooled_labels.extend(
            _label_entries(df, a, entries_by_sym[symbol], pip_size=pip, cost_r=cost_r)
        )
        base = [b for b in _base_rate_labels(df, a, pip_size=pip, cost_r=cost_r)
                if b[0] < IN_SAMPLE_END]
        base_fav += sum(f for _, f, _ in base)
        base_n += len(base)
    base_rate = base_fav / base_n if base_n else 0.0
    return _grade([_make_cell(f"xs_mom_{lookback}", "POOLED", pooled_labels, base_rate)])


def format_report(results: Sequence[CellResult], timeframe: str) -> str:
    validated = [r for r in results if r.verdict == "VALIDATED"]
    testable = [r for r in results if r.p_value is not None]
    lines = [
        "# Track 3a — FX non-MMM signal audit",
        "",
        f"Timeframe {timeframe} | {len(results)} cells, {len(testable)} testable "
        f"(N>={MIN_CELL_N}) | BH q={BH_Q} | bracket {K_ATR}xATR 1:1 | "
        f"horizon {HORIZON_BARS} bars | in-sample < {IN_SAMPLE_END.date()}",
        "",
        f"**VALIDATED: {len(validated)}**",
        "",
        "| signal | sym | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |",
        "|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|",
    ]
    for r in sorted(testable, key=lambda r: (r.verdict != "VALIDATED", r.p_value)):
        pe = f"{r.p_expectancy:.3f}" if r.p_expectancy is not None else "—"
        lines.append(
            f"| {r.signal} | {r.symbol} | {r.n} | {100*r.fav_rate:.0f} | "
            f"{100*r.base_rate:.0f} | {r.p_value:.3f} | {pe} | {r.mean_net_r:+.2f} | "
            f"{r.holdout_n} | {r.holdout_mean_net_r:+.2f} | {r.verdict} |"
        )
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="Track 3a FX non-MMM signal audit")
    ap.add_argument("--timeframe", default=DEFAULT_TIMEFRAME)
    ap.add_argument("--bars", type=int, default=6000)
    ap.add_argument("--cost-r", type=float, default=COST_R_DEFAULT)
    ap.add_argument("--out", default="logs/signal_research.md")
    args = ap.parse_args()
    results = audit(timeframe=args.timeframe, n_bars=args.bars, cost_r=args.cost_r)
    results += audit_cross_sectional(
        timeframe=args.timeframe, n_bars=args.bars, cost_r=args.cost_r
    )
    md = format_report(results, args.timeframe)
    from pathlib import Path
    Path(args.out).write_text(md, encoding="utf-8")
    print(md)
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
