"""Statistical machinery for honest rule validation (audit Tier 2.4).

The old validator scored "hits" as MFE > MAE over a window — a trade that
gets stopped out and then rallies counted as a HIT. This module provides:

- first_touch_outcome: path-ordered labeling. Walk bars in order; the
  level touched FIRST decides the outcome. Same-bar ambiguity (both target
  and stop inside one bar) resolves conservatively to the stop.
- non_overlapping sampling discipline is the caller's job, but
  empirical_base_rate implements it for the unconditional control sample.
- binomial_p_at_least: exact one-sided binomial tail P(X >= k | n, p0),
  no scipy dependency (log-space, stable to n in the thousands).
- benjamini_hochberg: FDR control across the rule x pair grid.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple

import pandas as pd

# ---------------------------------------------------------------------------
# First-touch labeling
# ---------------------------------------------------------------------------

TARGET = "TARGET"
STOP = "STOP"
EXPIRY = "EXPIRY"


@dataclass
class FirstTouch:
    outcome: str          # TARGET / STOP / EXPIRY
    bars_held: int
    pips_result: float    # +target_pips, -stop_pips, or close-to-close at expiry


def first_touch_outcome(
    df: pd.DataFrame,
    start_idx: int,
    direction: str,          # "BUY" / "SELL"
    entry_price: float,
    target_pips: float,
    stop_pips: float,
    horizon_bars: int,
    pip_size: float,
) -> Optional[FirstTouch]:
    """Label an entry by whichever level price touches FIRST.

    Walks bars start_idx+1 .. start_idx+horizon_bars in path order.
    A bar that contains BOTH levels is labeled STOP (conservative — the
    intrabar path is unknown, assume the worst). Returns None if there
    are no bars after the entry.
    """
    if direction == "BUY":
        target = entry_price + target_pips * pip_size
        stop = entry_price - stop_pips * pip_size
    else:
        target = entry_price - target_pips * pip_size
        stop = entry_price + stop_pips * pip_size

    end = min(start_idx + horizon_bars, len(df) - 1)
    if end <= start_idx:
        return None

    for i in range(start_idx + 1, end + 1):
        high = float(df.iloc[i]["High"])
        low = float(df.iloc[i]["Low"])
        if direction == "BUY":
            hit_stop = low <= stop
            hit_target = high >= target
        else:
            hit_stop = high >= stop
            hit_target = low <= target

        if hit_stop:  # conservative: stop wins any same-bar ambiguity
            return FirstTouch(STOP, i - start_idx, -stop_pips)
        if hit_target:
            return FirstTouch(TARGET, i - start_idx, target_pips)

    exit_close = float(df.iloc[end]["Close"])
    if direction == "BUY":
        pips = (exit_close - entry_price) / pip_size
    else:
        pips = (entry_price - exit_close) / pip_size
    return FirstTouch(EXPIRY, end - start_idx, pips)


def empirical_base_rate(
    df: pd.DataFrame,
    direction: str,
    target_pips: float,
    stop_pips: float,
    horizon_bars: int,
    pip_size: float,
) -> Tuple[Optional[float], int]:
    """Unconditional first-touch target rate for one direction.

    Samples entries every horizon_bars (non-overlapping outcome windows)
    at bar closes across the whole series — the base rate an entry with
    NO signal achieves with the same target/stop/horizon. EXPIRY samples
    are excluded (same convention as rule scoring). Returns (rate, n);
    rate is None when fewer than 30 resolved samples exist.
    """
    hits = 0
    resolved = 0
    idx = 0
    while idx < len(df) - 2:
        entry = float(df.iloc[idx]["Close"])
        ft = first_touch_outcome(
            df, idx, direction, entry, target_pips, stop_pips, horizon_bars, pip_size
        )
        if ft is not None and ft.outcome in (TARGET, STOP):
            resolved += 1
            if ft.outcome == TARGET:
                hits += 1
        idx += horizon_bars

    if resolved < 30:
        return None, resolved
    return hits / resolved, resolved


# ---------------------------------------------------------------------------
# Exact one-sided binomial test (no scipy)
# ---------------------------------------------------------------------------

def _log_binom_pmf(k: int, n: int, p: float) -> float:
    return (
        math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
        + k * math.log(p) + (n - k) * math.log(1.0 - p)
    )


def binomial_p_at_least(k: int, n: int, p0: float) -> float:
    """Exact P(X >= k) for X ~ Binomial(n, p0), one-sided 'greater'."""
    if n <= 0:
        return 1.0
    if k <= 0:
        return 1.0
    if p0 <= 0.0:
        return 0.0 if k > 0 else 1.0
    if p0 >= 1.0:
        return 1.0
    if k > n:
        return 0.0
    total = 0.0
    for i in range(k, n + 1):
        total += math.exp(_log_binom_pmf(i, n, p0))
    return min(1.0, total)


# ---------------------------------------------------------------------------
# Benjamini-Hochberg FDR control
# ---------------------------------------------------------------------------

def benjamini_hochberg(
    pvals: Sequence[Optional[float]], q: float = 0.10
) -> List[bool]:
    """Reject/accept flags under BH at FDR q.

    None entries (untestable results) are never rejected and don't count
    toward the number of tests.
    """
    indexed = [(i, p) for i, p in enumerate(pvals) if p is not None]
    m = len(indexed)
    flags = [False] * len(pvals)
    if m == 0:
        return flags

    indexed.sort(key=lambda t: t[1])
    cutoff_rank = 0
    for rank, (_, p) in enumerate(indexed, start=1):
        if p <= q * rank / m:
            cutoff_rank = rank
    for rank, (orig_idx, _) in enumerate(indexed, start=1):
        if rank <= cutoff_rank:
            flags[orig_idx] = True
    return flags
