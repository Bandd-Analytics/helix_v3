"""Management-as-alpha research — Forward Plan Track 3b.

3a proved entry *direction* has no validated FX edge (6 families, all DEAD).
3b asks the genuinely different question: can EXIT MANAGEMENT convert a
direction-neutral entry stream into positive net-R after realistic costs? If
yes, the system would not need the entry edge we've shown it doesn't have.

The one design idea that makes the test clean: **hold the entry stream fixed,
vary ONLY the exit policy, and measure each policy against the symmetric-1:1
control on the IDENTICAL entries.** That isolates management from entry
selection — the same trap 3a was built to dodge, applied to exits.

Neutral entry streams (held fixed):
  - random-sign: direction from a stable hash of the bar timestamp — the null,
    truly uncorrelated with price (reproducible, no RNG state).
  - z-fade: z-score>=2 mean-reversion (3a's least-bad family) — a faint,
    unvalidated tendency; "cheap and roughly neutral".

Exit policies (the "management families", each a grid cell):
  sym_1_1 (CONTROL) · tp_2R (let winners run) · tp_0p5R (cut quick) ·
  trail_1R (Van Tharp claim) · be_1R (breakeven at +1R) ·
  scaleout (50% at 1R + trail rest — the production T1/trail analog) ·
  time_stop (hold to horizon, exit market).

Cost realism is decisive here: cost scales with FILL COUNT — `cost_r * fills/2`,
so a plain round trip = cost_r (3a-comparable) and a scale-out pays 1.5x. That
is where the random-entry-plus-trailing-stop folklore usually dies.

Same gauntlet as every 3a family (reused verbatim from signal_research):
first-touch path ordering, non-overlap, binomial + expectancy, BH across the
WHOLE entry x policy grid, embargoed 2025-26 holdout. Offline; gates nothing.

A survivor (BH-significant + cost-positive in-sample AND positive holdout) is
re-run through the PRODUCTION TradeSimulator (engine.py) before it may advance
to Track 2 forward demo — the research sim must not be the only witness.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

from helix_v3.backtest.signal_research import (
    ATR_PERIOD,
    COST_R_DEFAULT,
    DEFAULT_TIMEFRAME,
    HORIZON_BARS,
    IN_SAMPLE_END,
    K_ATR,
    MAJORS,
    CellResult,
    _grade,
    _make_cell,
    atr,
    fetch_bars,
    format_report,
    pip_size_for,
    zscore_reversion,
)


# ---------------------------------------------------------------------------
# Exit policies — everything is expressed in R-multiples of the 1xATR stop
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ExitPolicy:
    name: str
    stop_R: Optional[float] = 1.0      # initial stop distance (None = no hard stop)
    target_R: Optional[float] = None   # full take-profit (None = none)
    trail_R: Optional[float] = None    # trail this far behind peak once peak>=trail_R
    be_R: Optional[float] = None        # move stop to breakeven when fav reaches be_R
    partial_R: Optional[float] = None  # close `partial_frac` of position at this R
    partial_frac: float = 0.0


POLICIES: List[ExitPolicy] = [
    ExitPolicy("sym_1_1", stop_R=1.0, target_R=1.0),                       # CONTROL
    ExitPolicy("tp_2R", stop_R=1.0, target_R=2.0),                         # let run
    ExitPolicy("tp_0p5R", stop_R=1.0, target_R=0.5),                       # cut quick
    ExitPolicy("trail_1R", stop_R=1.0, trail_R=1.0),                       # Van Tharp
    ExitPolicy("be_1R", stop_R=1.0, target_R=2.0, be_R=1.0),              # risk-off at 1R
    ExitPolicy("scaleout", stop_R=1.0, trail_R=1.0,                        # production T1
               partial_R=1.0, partial_frac=0.5),
    ExitPolicy("time_stop", stop_R=None),                                  # pure holding
]

CONTROL_POLICY = POLICIES[0]


# ---------------------------------------------------------------------------
# Bar-by-bar exit simulator
# ---------------------------------------------------------------------------

def simulate_exit(
    df: pd.DataFrame, i: int, direction: str, atr_i: float, p: ExitPolicy,
    *, cost_r: float, horizon: int,
) -> Optional[Tuple[float, int, int]]:
    """Walk bars i+1..i+horizon under policy `p`; return (net_r, fills, bars).

    Works in R-space: 1R = K_ATR x ATR(entry) in price. Per bar, the adverse
    extreme is checked BEFORE the favorable one (same conservative same-bar
    ordering as rule_stats.first_touch_outcome — the intrabar path is unknown,
    assume the worst). Trail/breakeven update at bar close and bind next bar.
    Cost = cost_r * fills / 2, so a plain round trip (2 fills) = cost_r.
    """
    unit = K_ATR * atr_i
    if unit <= 0:
        return None
    end = min(i + horizon, len(df) - 1)
    if end <= i:
        return None
    entry = float(df["Close"].iloc[i])
    H, L, C = df["High"].values, df["Low"].values, df["Close"].values

    def fav(price: float) -> float:
        return (price - entry) / unit if direction == "BUY" else (entry - price) / unit

    pos = 1.0
    realized = 0.0
    fills = 1                      # the entry fill
    stop = None if p.stop_R is None else -p.stop_R
    peak = 0.0
    be_done = False
    partial_done = p.partial_R is None
    j = end
    for j in range(i + 1, end + 1):
        # most/least favorable point reached inside this bar
        fav_hi = fav(H[j]) if direction == "BUY" else fav(L[j])
        fav_lo = fav(L[j]) if direction == "BUY" else fav(H[j])

        if stop is not None and fav_lo <= stop:        # adverse first (conservative)
            realized += pos * stop
            fills += 1
            pos = 0.0
            break
        if p.target_R is not None and fav_hi >= p.target_R:
            realized += pos * p.target_R
            fills += 1
            pos = 0.0
            break
        if not partial_done and fav_hi >= p.partial_R:
            realized += p.partial_frac * p.partial_R
            pos -= p.partial_frac
            fills += 1
            partial_done = True
        if (not be_done) and p.be_R is not None and fav_hi >= p.be_R:
            stop = 0.0 if stop is None else max(stop, 0.0)
            be_done = True
        peak = max(peak, fav_hi)
        if p.trail_R is not None and peak >= p.trail_R:
            trailed = peak - p.trail_R
            stop = trailed if stop is None else max(stop, trailed)

    if pos > 0:                                         # unresolved -> exit at horizon
        realized += pos * fav(C[end])
        fills += 1

    net_r = realized - cost_r * fills / 2.0
    return net_r, fills, j - i


# ---------------------------------------------------------------------------
# Neutral entry streams (held fixed across policies)
# ---------------------------------------------------------------------------

def _stable_bit(x: int) -> int:
    """splitmix64 finalizer -> low bit. A raw parity test fails on regularly
    spaced bars (every H4 step is an even number of seconds -> all one side);
    this avalanches the timestamp so the sign is ~50/50 yet deterministic.
    """
    x &= 0xFFFFFFFFFFFFFFFF
    x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
    x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & 0xFFFFFFFFFFFFFFFF
    x ^= x >> 31
    return x & 1


def random_sign_entries(df: pd.DataFrame) -> List[Tuple[int, str]]:
    """Direction from a STABLE hash of the bar's epoch-second — ~50/50 and
    uncorrelated with price. Deterministic (no RNG state, survives resume).
    Non-overlap in labeling culls these to a spaced, tradeable subset.
    """
    out: List[Tuple[int, str]] = []
    idx = df.index
    for i in range(ATR_PERIOD, len(df) - 1):
        secs = int(idx[i].value // 1_000_000_000)
        out.append((i, "BUY" if _stable_bit(secs) == 0 else "SELL"))
    return out


def zfade_entries(df: pd.DataFrame) -> List[Tuple[int, str]]:
    return zscore_reversion(df, lookback=20, z=2.0)


ENTRY_STREAMS: Dict[str, "callable"] = {
    "random": random_sign_entries,
    "zfade": zfade_entries,
}


# ---------------------------------------------------------------------------
# Labeling + audit
# ---------------------------------------------------------------------------

def _label_managed(
    df: pd.DataFrame, atr_series: pd.Series, entries: Sequence[Tuple[int, str]],
    policy: ExitPolicy, *, cost_r: float, horizon: int,
) -> List[Tuple[datetime, bool, float]]:
    """[(entry_time, favorable, net_r)] for non-overlapping managed entries."""
    out: List[Tuple[datetime, bool, float]] = []
    last_exit_idx = -1
    a = atr_series.values
    for i, direction in entries:
        if i <= last_exit_idx or i >= len(df) - 1 or np.isnan(a[i]) or a[i] <= 0:
            continue
        res = simulate_exit(df, i, direction, a[i], policy, cost_r=cost_r, horizon=horizon)
        if res is None:
            continue
        net_r, _fills, bars = res
        last_exit_idx = i + bars
        out.append((df.index[i].to_pydatetime(), bool(net_r > 0), net_r))
    return out


def audit_management(
    symbols: Sequence[str] = MAJORS, timeframe: str = DEFAULT_TIMEFRAME,
    n_bars: int = 6000, cost_r: float = COST_R_DEFAULT, horizon: int = HORIZON_BARS,
) -> List[CellResult]:
    """Grid = entry-stream x exit-policy, pooled across pairs, graded together.

    base_rate for every policy on a stream is that stream's CONTROL (sym_1_1)
    favorable rate — so the binomial leg asks 'does this policy beat the
    baseline exit on the same entries', while the expectancy leg catches
    R-magnitude edges (e.g. let-winners-run trades a lower hit rate for size).
    """
    import MetaTrader5 as mt5
    mt5.initialize()

    pair_dfs: Dict[str, pd.DataFrame] = {}
    for symbol in symbols:
        df = fetch_bars(symbol, timeframe, n_bars)
        if not df.empty and len(df) >= 200:
            pair_dfs[symbol] = df
    if not pair_dfs:
        return []
    atrs = {s: atr(df) for s, df in pair_dfs.items()}

    results: List[CellResult] = []
    for stream_name, stream_fn in ENTRY_STREAMS.items():
        entries_by_sym = {s: stream_fn(df) for s, df in pair_dfs.items()}

        # control base rate for this stream (pooled, in-sample)
        ctrl_pooled: List[Tuple[datetime, bool, float]] = []
        for s, df in pair_dfs.items():
            ctrl_pooled.extend(_label_managed(
                df, atrs[s], entries_by_sym[s], CONTROL_POLICY,
                cost_r=cost_r, horizon=horizon))
        ctrl_in = [c for c in ctrl_pooled if c[0] < IN_SAMPLE_END]
        base_rate = (sum(f for _, f, _ in ctrl_in) / len(ctrl_in)) if ctrl_in else 0.0

        for policy in POLICIES:
            pooled: List[Tuple[datetime, bool, float]] = []
            for s, df in pair_dfs.items():
                pooled.extend(_label_managed(
                    df, atrs[s], entries_by_sym[s], policy,
                    cost_r=cost_r, horizon=horizon))
            results.append(
                _make_cell(f"{stream_name}/{policy.name}", "POOLED", pooled, base_rate))

    return _grade(results)


def main() -> None:
    ap = argparse.ArgumentParser(description="Track 3b management-as-alpha audit")
    ap.add_argument("--timeframe", default=DEFAULT_TIMEFRAME)
    ap.add_argument("--bars", type=int, default=6000)
    ap.add_argument("--cost-r", type=float, default=COST_R_DEFAULT)
    ap.add_argument("--out", default="logs/management_research.md")
    args = ap.parse_args()
    results = audit_management(
        timeframe=args.timeframe, n_bars=args.bars, cost_r=args.cost_r)
    md = format_report(results, args.timeframe).replace(
        "Track 3a — FX non-MMM signal audit",
        "Track 3b — management-as-alpha audit (entry held fixed, exit varied)")
    from pathlib import Path
    Path(args.out).write_text(md, encoding="utf-8")
    print(md)
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
