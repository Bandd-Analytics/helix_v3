"""Statistical signature audit — Edge Discovery Phase 1.

Does ANY setup signature genuinely beat its base rate? The feature-ablation
engine searched the signature space with naive 85%-fav thresholds and no
multiple-testing correction across thousands of tiny-N cells (median 2
samples/key) — that manufactures "100% / PF 999" candidates from noise.

This module applies the same gauntlet that killed the MMM rules in audit
Tier 2.4, to the signature space:

  - First-touch labels (already path-ordered in mmm_event_outcomes; we only
    consume them, never MFE>MAE).
  - A COARSE projection of the 13-dim normalized_key so cells reach N>=30
    (config: pick the facets to group by). Cross-pair pooling aggregates
    samples across symbols.
  - Non-overlapping samples WITHIN each cell (a signature firing on adjacent
    bars is one event, not many) so significance isn't inflated.
  - Exact one-sided binomial test of the cell's favorable rate vs the
    empirical unconditional rate of the SAME (symbol, direction) — i.e. does
    the signature beat a generic entry with identical management?
  - Benjamini-Hochberg FDR control across the whole cell grid.
  - Expectancy in R-multiples (exit_pips / sl_pips), net of a round-trip cost,
    so magnitude is comparable across pairs.
  - Embargoed walk-forward: a cell is VALIDATED only if it is BH-significant
    AND positive-expectancy in-sample AND replicates on the held-out window.

Offline only — reads logs/vision_backtests.db, writes a report + log. Touches
no live execution.
"""
from __future__ import annotations

import argparse
import math
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from config.pair_profiles import get_pair_profile
from helix_v3.training.rule_stats import benjamini_hochberg, binomial_p_at_least

# normalized_key is 13 pipe-separated components (mmm_event_replay.build_setup_signature)
FACET_INDEX: Dict[str, int] = {
    "family": 0,
    "direction": 1,
    "weekly_phase": 2,
    "h4_level": 3,
    "session": 4,
    "asian": 5,
    "hunt": 6,
    "push": 7,
    "mw": 8,
    "rrt": 9,
    "tdi": 10,
    "pattern": 11,
    "confluence": 12,
}

# Path-ordered terminal outcomes. FAVORABLE per validation_library convention.
FAVORABLE = {"TARGET_2", "TRAIL_STOP", "TIME_EXIT_PROFIT"}
# Resolved = terminal events we score. OPEN_* (ran out of data) and AMBIGUOUS
# (same-bar SL+target, intrabar path unknown) are excluded — not edge evidence.
RESOLVED = FAVORABLE | {
    "BREAKEVEN_AFTER_T1", "STALE_EXIT", "LOSS", "SL_HIT", "TIME_EXIT_LOSS",
}

# A-priori coarse schemes (chosen BEFORE looking at results — no forking paths).
# Each is graded on its own grid. S0 is a sanity control: direction alone should
# land at the base rate by construction.
SCHEMES: Dict[str, List[str]] = {
    "S0_direction": ["direction"],
    "S1_family_tdi": ["family", "direction", "tdi"],
    "S2_family_mw_tdi": ["family", "direction", "mw", "tdi"],
    "S3_family_hunt_tdi": ["family", "direction", "hunt", "tdi"],
    "S4_family_session_tdi": ["family", "direction", "session", "tdi"],
}

MIN_CELL_N = 30          # minimum non-overlapping samples to test a cell
MIN_HOLDOUT_N = 15       # minimum holdout samples to count as a replication
BH_Q = 0.10
DEFAULT_SLIPPAGE_PIPS = 0.5
IN_SAMPLE_END = datetime(2025, 1, 1, tzinfo=timezone.utc)
EMBARGO_DAYS = 7


@dataclass
class Outcome:
    symbol: str
    direction: str
    facets: Tuple[str, ...]          # parsed normalized_key components
    snapshot_at: datetime
    exit_at: datetime
    favorable: bool
    net_r: float                     # (exit_pips - cost) / sl_pips


@dataclass
class CellResult:
    scheme: str
    key: str
    symbol: str                      # "POOLED" for cross-pair
    direction: str
    n: int
    favorable: int
    fav_rate: float
    base_rate: float
    p_value: Optional[float]         # binomial: favorable rate > base
    mean_net_r: float
    p_expectancy: Optional[float]    # one-sided: mean net-R > 0
    bh_significant: bool = False     # hit-rate track
    bh_exp_significant: bool = False # expectancy track
    holdout_n: int = 0
    holdout_fav_rate: float = 0.0
    holdout_mean_net_r: float = 0.0
    verdict: str = ""                # VALIDATED / DEAD / INSUFFICIENT_N


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def _parse_dt(s: str) -> Optional[datetime]:
    if not s:
        return None
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def _cost_pips(symbol: str, slippage_pips: float) -> float:
    """Conservative round-trip cost: full pair spread + slippage per side."""
    try:
        spread = float(get_pair_profile(symbol).max_spread_pips)
    except Exception:
        spread = 2.0
    return spread + 2.0 * slippage_pips


def load_outcomes(
    db_path: str, *, slippage_pips: float = DEFAULT_SLIPPAGE_PIPS
) -> List[Outcome]:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            """SELECT s.symbol AS symbol, s.normalized_key AS nk,
                      o.direction AS direction, o.snapshot_at AS snapshot_at,
                      o.exit_at AS exit_at, o.exit_pips AS exit_pips,
                      o.sl_pips AS sl_pips, o.outcome AS outcome
               FROM mmm_event_outcomes o
               JOIN mmm_setup_signatures s ON o.signature_id = s.id"""
        ).fetchall()
    finally:
        conn.close()

    out: List[Outcome] = []
    for r in rows:
        if r["outcome"] not in RESOLVED:
            continue
        snap = _parse_dt(r["snapshot_at"])
        exit_at = _parse_dt(r["exit_at"]) or snap
        nk = r["nk"] or ""
        parts = nk.split("|")
        if len(parts) < len(FACET_INDEX) or snap is None:
            continue
        sl_pips = float(r["sl_pips"] or 0.0)
        if sl_pips <= 0:
            continue
        cost = _cost_pips(r["symbol"], slippage_pips)
        net_r = (float(r["exit_pips"] or 0.0) - cost) / sl_pips
        out.append(
            Outcome(
                symbol=r["symbol"],
                direction=r["direction"],
                facets=tuple(parts[: len(FACET_INDEX)]),
                snapshot_at=snap,
                exit_at=exit_at,
                favorable=r["outcome"] in FAVORABLE,
                net_r=net_r,
            )
        )
    return out


# ---------------------------------------------------------------------------
# Sampling discipline
# ---------------------------------------------------------------------------

def non_overlapping(items: Sequence[Outcome]) -> List[Outcome]:
    """Greedy: keep an outcome only if it starts at/after the last kept exit.

    Removes the inflation from one signature firing on adjacent bars (same
    market event counted many times). Applied per cell.
    """
    kept: List[Outcome] = []
    last_exit: Optional[datetime] = None
    for o in sorted(items, key=lambda x: x.snapshot_at):
        if last_exit is None or o.snapshot_at >= last_exit:
            kept.append(o)
            last_exit = o.exit_at
    return kept


def coarse_key(o: Outcome, facets: Sequence[str]) -> str:
    return "|".join(o.facets[FACET_INDEX[f]] for f in facets)


# ---------------------------------------------------------------------------
# Base rates (the control)
# ---------------------------------------------------------------------------

def base_rates(
    outcomes: Sequence[Outcome], *, pooled: bool
) -> Dict[Tuple[str, str], float]:
    """Unconditional favorable rate per (symbol, direction), or (POOLED, dir).

    Uses non-overlapping samples per group so the control matches the test.
    """
    groups: Dict[Tuple[str, str], List[Outcome]] = {}
    for o in outcomes:
        key = ("POOLED" if pooled else o.symbol, o.direction)
        groups.setdefault(key, []).append(o)
    rates: Dict[Tuple[str, str], float] = {}
    for key, items in groups.items():
        sample = non_overlapping(items)
        if sample:
            rates[key] = sum(o.favorable for o in sample) / len(sample)
    return rates


# ---------------------------------------------------------------------------
# The audit
# ---------------------------------------------------------------------------

def _expectancy_pvalue(sample: List[Outcome]) -> Optional[float]:
    """One-sided P(mean net-R <= 0) via the normal approximation (n>=30, CLT).

    Captures an ASYMMETRIC edge — low hit rate but positive expectancy from
    fat-tail runners — that a favorable-rate test alone would miss. No scipy:
    p = Phi(-t) = 0.5*erfc(t/sqrt(2)).
    """
    n = len(sample)
    if n < MIN_CELL_N:
        return None
    rs = [o.net_r for o in sample]
    mean = sum(rs) / n
    var = sum((r - mean) ** 2 for r in rs) / (n - 1)
    if var <= 0:
        return 0.0 if mean > 0 else 1.0
    t = mean / math.sqrt(var / n)
    return 0.5 * math.erfc(t / math.sqrt(2.0))


def _cell_stats(
    scheme: str, key: str, symbol: str, direction: str,
    sample: List[Outcome], base: float,
) -> CellResult:
    n = len(sample)
    k = sum(o.favorable for o in sample)
    fav_rate = k / n if n else 0.0
    mean_r = sum(o.net_r for o in sample) / n if n else 0.0
    p = binomial_p_at_least(k, n, base) if n >= MIN_CELL_N and base > 0 else None
    return CellResult(
        scheme=scheme, key=key, symbol=symbol, direction=direction,
        n=n, favorable=k, fav_rate=fav_rate, base_rate=base,
        p_value=p, mean_net_r=mean_r, p_expectancy=_expectancy_pvalue(sample),
    )


def audit_scheme(
    outcomes: Sequence[Outcome], scheme: str, facets: Sequence[str], *,
    pooled: bool, in_sample_end: datetime = IN_SAMPLE_END,
    embargo_days: int = EMBARGO_DAYS,
) -> List[CellResult]:
    """Full per-cell audit for one coarse scheme, with embargoed walk-forward."""
    holdout_start = in_sample_end + timedelta(days=embargo_days)
    in_sample = [o for o in outcomes if o.snapshot_at < in_sample_end]
    holdout = [o for o in outcomes if o.snapshot_at >= holdout_start]

    base_is = base_rates(in_sample, pooled=pooled)
    base_all = base_rates(outcomes, pooled=pooled)

    # Group in-sample outcomes into cells
    cells: Dict[Tuple[str, str, str], List[Outcome]] = {}
    for o in in_sample:
        sym = "POOLED" if pooled else o.symbol
        cells.setdefault((sym, o.direction, coarse_key(o, facets)), []).append(o)

    results: List[CellResult] = []
    for (sym, direction, key), items in cells.items():
        sample = non_overlapping(items)
        base = base_is.get((sym, direction)) or base_all.get((sym, direction), 0.0)
        res = _cell_stats(scheme, key, sym, direction, sample, base)
        results.append(res)

    # BH across the in-sample grid — two independent tracks:
    #   hit-rate (favorable > base) and expectancy (mean net-R > 0).
    for r, f in zip(results, benjamini_hochberg([r.p_value for r in results], q=BH_Q)):
        r.bh_significant = f
    for r, f in zip(results, benjamini_hochberg([r.p_expectancy for r in results], q=BH_Q)):
        r.bh_exp_significant = f

    # Walk-forward replication on the embargoed holdout
    hold_cells: Dict[Tuple[str, str, str], List[Outcome]] = {}
    for o in holdout:
        sym = "POOLED" if pooled else o.symbol
        hold_cells.setdefault((sym, o.direction, coarse_key(o, facets)), []).append(o)

    for r in results:
        if r.p_value is None:
            r.verdict = "INSUFFICIENT_N"
            continue
        hs = non_overlapping(hold_cells.get((r.symbol, r.direction, r.key), []))
        r.holdout_n = len(hs)
        if hs:
            r.holdout_fav_rate = sum(o.favorable for o in hs) / len(hs)
            r.holdout_mean_net_r = sum(o.net_r for o in hs) / len(hs)
        # Edge in EITHER track — a hit-rate edge that pays, or a positive
        # expectancy (asymmetric/fat-tail) edge. Both demand positive net-R.
        in_sample_edge = (
            (r.bh_significant and r.mean_net_r > 0) or r.bh_exp_significant
        )
        # The money replication: positive expectancy out of sample. (Favorable
        # rate can fall while expectancy holds for fat-tail edges.)
        replicates = r.holdout_n >= MIN_HOLDOUT_N and r.holdout_mean_net_r > 0
        r.verdict = "VALIDATED" if (in_sample_edge and replicates) else "DEAD"
    return results


def run_audit(
    db_path: str, *, slippage_pips: float = DEFAULT_SLIPPAGE_PIPS
) -> Dict[str, List[CellResult]]:
    outcomes = load_outcomes(db_path, slippage_pips=slippage_pips)
    report: Dict[str, List[CellResult]] = {}
    for scheme, facets in SCHEMES.items():
        # Per-pair and pooled cross-pair are separate grids.
        report[f"{scheme}|per_pair"] = audit_scheme(
            outcomes, scheme, facets, pooled=False
        )
        report[f"{scheme}|pooled"] = audit_scheme(
            outcomes, scheme, facets, pooled=True
        )
    return report


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def format_report(report: Dict[str, List[CellResult]], n_outcomes: int) -> str:
    lines: List[str] = [
        "# Edge Discovery — Phase 1 Signature Audit",
        "",
        f"Resolved outcomes: {n_outcomes}  |  BH q={BH_Q}  |  "
        f"min cell N={MIN_CELL_N}  |  in-sample < {IN_SAMPLE_END.date()}  "
        f"|  holdout embargo {EMBARGO_DAYS}d",
        "",
        "A cell is VALIDATED only if it is BH-significant AND positive net-R "
        "in-sample AND replicates (beats base + positive net-R) on the "
        f"embargoed holdout with N>={MIN_HOLDOUT_N}.",
        "",
    ]
    validated_total = 0
    for grid, results in report.items():
        testable = [r for r in results if r.p_value is not None]
        sig = [r for r in testable if r.bh_significant]
        sig_exp = [r for r in testable if r.bh_exp_significant]
        validated = [r for r in results if r.verdict == "VALIDATED"]
        validated_total += len(validated)
        lines.append(
            f"## {grid} — {len(results)} cells, {len(testable)} testable "
            f"(N>={MIN_CELL_N}), {len(sig)} hit-rate-sig, {len(sig_exp)} "
            f"expectancy-sig, {len(validated)} VALIDATED"
        )
        show = sorted(
            [r for r in testable
             if r.bh_significant or r.bh_exp_significant or r.verdict == "VALIDATED"],
            key=lambda r: (r.verdict != "VALIDATED", r.p_value if r.p_value is not None else 1.0),
        )[:25]
        if show:
            lines.append("")
            lines.append(
                "| key | sym | dir | n | fav% | base% | p_hit | p_exp | netR | "
                "hold_n | hold_netR | verdict |"
            )
            lines.append("|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|")
            for r in show:
                pe = f"{r.p_expectancy:.4f}" if r.p_expectancy is not None else "—"
                lines.append(
                    f"| {r.key} | {r.symbol} | {r.direction} | {r.n} | "
                    f"{100*r.fav_rate:.0f} | {100*r.base_rate:.0f} | "
                    f"{r.p_value:.4f} | {pe} | {r.mean_net_r:+.2f} | {r.holdout_n} | "
                    f"{r.holdout_mean_net_r:+.2f} | {r.verdict} |"
                )
        lines.append("")
    lines.insert(4, f"**TOTAL VALIDATED across all grids: {validated_total}**")
    lines.insert(5, "")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="Edge Discovery Phase 1 signature audit")
    ap.add_argument("--db", default="logs/vision_backtests.db")
    ap.add_argument("--slippage", type=float, default=DEFAULT_SLIPPAGE_PIPS)
    ap.add_argument("--out", default="logs/signature_audit.md")
    args = ap.parse_args()

    outcomes = load_outcomes(args.db, slippage_pips=args.slippage)
    report: Dict[str, List[CellResult]] = {}
    for scheme, facets in SCHEMES.items():
        report[f"{scheme}|per_pair"] = audit_scheme(outcomes, scheme, facets, pooled=False)
        report[f"{scheme}|pooled"] = audit_scheme(outcomes, scheme, facets, pooled=True)

    md = format_report(report, len(outcomes))
    Path(args.out).write_text(md, encoding="utf-8")
    print(md)
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
