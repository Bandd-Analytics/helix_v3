"""Relative-value / cointegration research — Edge Hunt Track 3d.

Pre-registration: docs/EDGE_3D_COINTEGRATION.md (approved 2026-06-17).

Every dead avenue so far (3a entries, 3b management, 3c momentum) bet on
DIRECTION. This is the one structural category the hunt never touched:
market-neutral mean reversion of a hedged spread between two co-moving series
(Chan, glossary section 2 mean-reversion family). It predicts no direction.

Track 3a's z-score test was SINGLE-pair reversion (a price vs its own MA); this
is CROSS-pair cointegration (a hedged spread vs its own equilibrium) — different
object, different null.

DISCIPLINE (same gauntlet as every family, plus the pre-registered guardrails):
  - FIXED candidate set chosen on economic grounds, NOT an all-vs-all stationarity
    sweep (that would data-snoop over ~C(22,2) combinations).
  - Hedge ratio (beta) estimated IN-SAMPLE ONLY, frozen, applied to the holdout.
  - Engle-Granger cointegration gate: ADF on the spread residual must pass at 5%
    IN-SAMPLE *and* stay passing on the embargoed holdout (beta frozen).
  - THE COST TEST FIRST: a pairs trade is two legs — open both, close both ~=
    2x per-leg full spread. Before simulating anything, check the expected gross
    reversion (2 sigma_spread) exceeds the two-leg round-trip cost. If gross <
    cost even in-sample, the candidate is DEAD on arithmetic — no simulation.

No scipy/statsmodels in this codebase (rule_stats hand-rolls its stats); the ADF
test and OLS here are hand-rolled on numpy, with MacKinnon Engle-Granger critical
values. Offline research only — records nothing, gates nothing.

This module is the FIRST-PASS DIAGNOSTIC (cointegration gate + cost test). The
first-touch spread simulator is built only if a candidate survives this pass —
per the pre-registration, most or all are expected to die here.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

from helix_v3.backtest.signal_research import IN_SAMPLE_END, fetch_bars
from helix_v3.backtest.multiasset_research import _median_spread_points

# Pre-registered candidate set (FIXED — docs/EDGE_3D_COINTEGRATION.md). Each row
# is two legs with a shared real-economy driver. Order is (leg_A, leg_B).
CANDIDATE_PAIRS: List[Tuple[str, str]] = [
    ("AUDUSD", "NZDUSD"),   # 1. commodity / Australasian bloc — classic FX coint pair
    ("EURUSD", "GBPUSD"),   # 2. European bloc, shared USD leg
    ("USDCHF", "EURUSD"),   # 3. EUR/CHF near-peg -> USDCHF & EURUSD co-move (inverse)
    ("USDCAD", "USDNOK"),   # 4. oil-linked dollar pairs (dropped if USDNOK absent)
    ("XAUUSD", "XAGUSD"),   # 5. gold/silver — canonical cointegrated commodity spread
]

DEFAULT_TIMEFRAME = "D1"
N_BARS = 1600                 # ~6 years D1: in-sample to 2025-01-01, ~1.5y holdout
ADF_LAGS = 1                  # fixed (no sweep); ADF with constant + 1 lagged diff
Z_ENTRY = 2.0                 # pre-registered, no sweep
MIN_IN_SAMPLE = 200
MIN_HOLDOUT = 60

# MacKinnon (2010) asymptotic Engle-Granger critical values, residual-based ADF,
# 1 cointegrating regressor (N=2), constant, no trend. Gate at 5%.
EG_CRIT = {"1%": -3.9001, "5%": -3.3377, "10%": -3.0462}
EG_CRIT_5 = EG_CRIT["5%"]


# ---------------------------------------------------------------------------
# Hand-rolled OLS + ADF (no scipy/statsmodels)
# ---------------------------------------------------------------------------

def _ols(X: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Return (beta, se) for y = X beta + eps via least squares.

    se uses the classical residual variance estimate sigma^2 (X'X)^-1.
    """
    beta, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    n, k = X.shape
    dof = max(n - k, 1)
    sigma2 = float(resid @ resid) / dof
    xtx_inv = np.linalg.pinv(X.T @ X)
    se = np.sqrt(np.maximum(np.diag(xtx_inv) * sigma2, 0.0))
    return beta, se


def hedge_ratio(log_a: np.ndarray, log_b: np.ndarray) -> Tuple[float, float]:
    """OLS of log(A) on [1, log(B)] -> (intercept, beta). In-sample only."""
    X = np.column_stack([np.ones_like(log_b), log_b])
    beta, _ = _ols(X, log_a)
    return float(beta[0]), float(beta[1])


def adf_stat(series: np.ndarray, lags: int = ADF_LAGS) -> Optional[float]:
    """Augmented Dickey-Fuller t-stat on gamma in
        d_r_t = alpha + gamma r_{t-1} + sum_i delta_i d_r_{t-i} + eps.
    More negative = stronger evidence of stationarity (reversion). None if
    too short.
    """
    r = np.asarray(series, dtype=float)
    r = r[~np.isnan(r)]
    n = len(r)
    if n < lags + 20:
        return None
    dr = np.diff(r)                      # length n-1
    # rows usable: from index `lags` of dr (need lags prior diffs + level)
    rows = len(dr) - lags
    if rows < 10:
        return None
    y = dr[lags:]                        # d_r_t
    cols = [np.ones(rows), r[lags:-1]]   # const, r_{t-1}  (aligned to y)
    for i in range(1, lags + 1):
        cols.append(dr[lags - i: len(dr) - i])   # d_r_{t-i}
    X = np.column_stack(cols)
    beta, se = _ols(X, y)
    gamma, gamma_se = beta[1], se[1]
    if gamma_se <= 0:
        return None
    return float(gamma / gamma_se)


def half_life(spread: np.ndarray) -> Optional[float]:
    """OU half-life of reversion: d_s = alpha + lam s_{t-1}; HL = -ln2/lam."""
    s = np.asarray(spread, dtype=float)
    s = s[~np.isnan(s)]
    if len(s) < 30:
        return None
    ds = np.diff(s)
    X = np.column_stack([np.ones(len(ds)), s[:-1]])
    beta, _ = _ols(X, ds)
    lam = float(beta[1])
    if lam >= 0:
        return math.inf
    return -math.log(2.0) / lam


# ---------------------------------------------------------------------------
# Cost test (the priority diagnostic)
# ---------------------------------------------------------------------------

def relative_spread(symbol: str, df: pd.DataFrame,
                    timeframe: str, n_bars: int) -> Optional[float]:
    """Round-trip spread per leg as a fraction of price (a return-unit cost).

    median historical spread (points) * point / median Close. Median spread is
    robust to the closed-market snapshot (some CFDs read 0 live). Round trip per
    leg = pay half-spread to open + half-spread to close = one full spread.
    """
    import MetaTrader5 as mt5
    info = mt5.symbol_info(symbol)
    if info is None:
        return None
    med_pts = _median_spread_points(symbol, timeframe, n_bars)
    if med_pts is None:
        med_pts = float(info.spread)
    med_price = float(np.median(df["Close"].values))
    if med_price <= 0:
        return None
    return (med_pts * info.point) / med_price


@dataclass
class CointResult:
    pair: str
    n_in: int
    n_hold: int
    beta: float
    half_life: float
    sigma_spread: float          # std of in-sample spread (log units / return units)
    adf_in: Optional[float]
    adf_hold: Optional[float]
    coint_in: bool
    coint_hold: bool
    rel_spread_a: float
    rel_spread_b: float
    gross: float                 # expected gross reversion = 2 * sigma_spread
    cost: float                  # two-leg round trip = rel_a + |beta| * rel_b
    gross_over_cost: float
    cost_pass: bool
    verdict: str
    note: str = ""


def diagnose_pair(
    leg_a: str, leg_b: str, timeframe: str = DEFAULT_TIMEFRAME, n_bars: int = N_BARS,
) -> Optional[CointResult]:
    df_a = fetch_bars(leg_a, timeframe, n_bars)
    df_b = fetch_bars(leg_b, timeframe, n_bars)
    pair = f"{leg_a}/{leg_b}"
    if df_a.empty or df_b.empty:
        return CointResult(pair, 0, 0, 0, 0, 0, None, None, False, False,
                           0, 0, 0, 0, 0, False, "DROPPED",
                           note=f"missing bars ({leg_a if df_a.empty else leg_b})")

    # align on common timestamps
    joined = pd.concat([df_a["Close"].rename("A"), df_b["Close"].rename("B")],
                       axis=1, join="inner").dropna()
    if len(joined) < MIN_IN_SAMPLE + MIN_HOLDOUT:
        return CointResult(pair, len(joined), 0, 0, 0, 0, None, None, False, False,
                           0, 0, 0, 0, 0, False, "DROPPED", note="too few aligned bars")

    log_a = np.log(joined["A"].values)
    log_b = np.log(joined["B"].values)
    ts = joined.index
    is_mask = ts < pd.Timestamp(IN_SAMPLE_END)
    n_in, n_hold = int(is_mask.sum()), int((~is_mask).sum())
    if n_in < MIN_IN_SAMPLE or n_hold < MIN_HOLDOUT:
        return CointResult(pair, n_in, n_hold, 0, 0, 0, None, None, False, False,
                           0, 0, 0, 0, 0, False, "DROPPED",
                           note=f"split too small (in={n_in}, hold={n_hold})")

    # hedge ratio frozen on in-sample, applied to the whole series
    alpha, beta = hedge_ratio(log_a[is_mask], log_b[is_mask])
    spread = log_a - (alpha + beta * log_b)
    spread_in, spread_hold = spread[is_mask], spread[~is_mask]

    sigma = float(np.std(spread_in, ddof=1))
    adf_in = adf_stat(spread_in)
    adf_hold = adf_stat(spread_hold)
    coint_in = adf_in is not None and adf_in < EG_CRIT_5
    coint_hold = adf_hold is not None and adf_hold < EG_CRIT_5
    hl = half_life(spread_in) or math.inf

    rel_a = relative_spread(leg_a, df_a, timeframe, n_bars) or 0.0
    rel_b = relative_spread(leg_b, df_b, timeframe, n_bars) or 0.0

    # gross reversion captured entering at z=Z_ENTRY, exiting at z=0: Z_ENTRY*sigma.
    # The hedged-position P&L for a log-spread move ds ~= notional * ds, so per
    # unit notional the gross is Z_ENTRY * sigma (a return). Two-leg round-trip
    # cost = full spread on leg A + |beta| (notional held) * full spread on leg B.
    gross = Z_ENTRY * sigma
    cost = rel_a + abs(beta) * rel_b
    ratio = gross / cost if cost > 0 else math.inf
    cost_pass = ratio > 1.0

    # Verdict at this diagnostic stage: a candidate may ADVANCE to simulation only
    # if it is cointegrated in BOTH windows AND clears the cost arithmetic.
    if coint_in and coint_hold and cost_pass:
        verdict = "ADVANCE"
    elif not (coint_in and coint_hold):
        verdict = "DEAD_COINT"
    else:
        verdict = "DEAD_COST"

    return CointResult(
        pair, n_in, n_hold, beta, hl, sigma, adf_in, adf_hold, coint_in, coint_hold,
        rel_a, rel_b, gross, cost, ratio, cost_pass, verdict,
    )


def run_diagnostic(
    pairs: List[Tuple[str, str]] = CANDIDATE_PAIRS,
    timeframe: str = DEFAULT_TIMEFRAME, n_bars: int = N_BARS,
) -> List[CointResult]:
    import MetaTrader5 as mt5
    mt5.initialize()
    for legs in pairs:
        for s in legs:
            if mt5.symbol_info(s) is not None:
                mt5.symbol_select(s, True)
    out: List[CointResult] = []
    for leg_a, leg_b in pairs:
        res = diagnose_pair(leg_a, leg_b, timeframe, n_bars)
        if res is not None:
            out.append(res)
    return out


def _fmt(x: Optional[float], nd: int = 2, dash_inf: bool = False) -> str:
    if x is None:
        return "—"
    if dash_inf and (x == math.inf or x != x):
        return "inf"
    return f"{x:.{nd}f}"


def format_report(results: List[CointResult], timeframe: str) -> str:
    advance = [r for r in results if r.verdict == "ADVANCE"]
    lines = [
        "# Edge Hunt Track 3d — Cointegration / relative-value (first-pass diagnostic)",
        "",
        f"Pre-registration: `docs/EDGE_3D_COINTEGRATION.md`. {timeframe} bars, "
        f"in-sample < {IN_SAMPLE_END.date()}, embargoed holdout after. Engle-Granger "
        f"ADF gate at 5% crit {EG_CRIT_5:+.2f} (MacKinnon, N=2, const). Cost = two-leg "
        f"round-trip spread (rel_A + |beta|*rel_B); gross = {Z_ENTRY}*sigma_spread.",
        "",
        "Spread/σ/gross/cost are in **return units (bps = 1e-4)**.",
        "",
        f"**ADVANCE to simulation: {len(advance)}** "
        f"(cointegrated in BOTH windows AND gross > cost).",
        "",
        "| pair | n_in | n_hold | beta | half_life(bars) | sigma(bps) | ADF_in | "
        "coint_in | ADF_hold | coint_hold | gross(bps) | cost(bps) | gross/cost | verdict |",
        "|---|--:|--:|--:|--:|--:|--:|:-:|--:|:-:|--:|--:|--:|---|",
    ]
    order = {"ADVANCE": 0, "DEAD_COST": 1, "DEAD_COINT": 2, "DROPPED": 3}
    for r in sorted(results, key=lambda r: order.get(r.verdict, 9)):
        if r.verdict == "DROPPED":
            lines.append(
                f"| {r.pair} | {r.n_in} | {r.n_hold} | — | — | — | — | — | — | — | — | — | — | "
                f"DROPPED ({r.note}) |")
            continue
        lines.append(
            f"| {r.pair} | {r.n_in} | {r.n_hold} | {r.beta:+.3f} | "
            f"{_fmt(r.half_life, 1, dash_inf=True)} | {1e4*r.sigma_spread:.0f} | "
            f"{_fmt(r.adf_in)} | {'Y' if r.coint_in else 'n'} | {_fmt(r.adf_hold)} | "
            f"{'Y' if r.coint_hold else 'n'} | {1e4*r.gross:.0f} | {1e4*r.cost:.0f} | "
            f"{_fmt(r.gross_over_cost)} | {r.verdict} |")
    lines += [
        "",
        "## Verdict legend",
        "- **ADVANCE** — cointegrated in both windows AND gross reversion > two-leg "
        "cost. Only these proceed to the first-touch spread simulator.",
        "- **DEAD_COINT** — fails the Engle-Granger gate (not stationary in-sample, "
        "or stationarity does not survive the embargoed holdout with beta frozen).",
        "- **DEAD_COST** — cointegrated, but the expected reversion does not clear the "
        "two-leg round-trip spread. Dead on arithmetic; no simulation can rescue it.",
        "- **DROPPED** — leg unavailable on the broker feed or too little aligned data "
        "(reported, never silently swapped).",
        "",
    ]
    if advance:
        lines.append(
            f"**{len(advance)} candidate(s) cleared the gate — proceed to build the "
            "first-touch spread simulator (pre-registration step 4/6).**")
    else:
        lines.append(
            "**Zero candidates cleared the gate. Per the pre-registration kill bar, "
            "Track 3d is DEAD and the relative-value category is falsified — the edge "
            "hunt is complete across all four structural categories. No simulation is "
            "written; no threshold is tuned. Door B.**")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="Track 3d cointegration first-pass diagnostic")
    ap.add_argument("--timeframe", default=DEFAULT_TIMEFRAME)
    ap.add_argument("--bars", type=int, default=N_BARS)
    ap.add_argument("--out", default="logs/cointegration_research.md")
    args = ap.parse_args()
    results = run_diagnostic(timeframe=args.timeframe, n_bars=args.bars)
    md = format_report(results, args.timeframe)
    from pathlib import Path
    Path(args.out).write_text(md, encoding="utf-8")
    print(md.encode("ascii", "replace").decode("ascii"))   # console may be cp1252
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
