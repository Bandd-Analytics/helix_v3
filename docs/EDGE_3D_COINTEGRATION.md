# Edge Hunt Track 3d — Relative Value / Cointegration (PRE-REGISTRATION)

Date: 2026-06-17. Status: **pre-registered, NOT yet run.** No code beyond this page
exists. This document is written *before* any data is touched — that is the whole point.
Approve or reject it as written; do not let the harness be designed after seeing a result.

> **Why this is allowed.** `SYSTEM_STATUS.md` rule 4 closes Track 3a/3b/3c as settled
> negatives and forbids *re-testing* them — but explicitly permits "a genuinely new
> hypothesis, run through the same gauntlet AND benchmarked against the right null." Every
> dead avenue so far bet on **direction** (3a entries, 3b management of a neutral entry, 3c
> momentum vs buy-and-hold). Cointegration bets on **the spread between two co-moving series
> reverting to a stationary mean** — it is market-neutral and predicts no direction at all.
> It is the one structural category in the glossary (Chan, §1.2 / §2 mean-reversion family)
> that the hunt never touched. Track 3a's z-score test was *single-pair* reversion (a price
> vs its own moving average); this is *cross-pair* cointegration (a hedged spread vs its own
> equilibrium). Different object, different null, genuinely new.

## My honest prior (stated up front, so the result can't move it after the fact)

**I expect this to die too, and I expect it to die at COST, not at statistics.** A pairs
trade has two legs; you cross the spread to open both and again to close both — roughly **2×
the round-trip cost** that already bled Track 3a's carry edge to death under Carver's speed
limit. Major-FX cointegration is also thin and unstable: the obvious relationships are the
most-arbitraged on earth, and cointegration tends to break *precisely during regime shifts* —
i.e. while you are in the trade. The likely fingerprint is the same one that killed everything
else: a faint in-sample lead that collapses in the embargoed holdout. **The value of running
it is not "probably a winner" — it is closing the last open structural door with the same
discipline, so the conclusion becomes complete instead of "we stopped after three."**

Two outcomes, both useful:
- **Dies** (my bet): direction-timing, management, momentum, AND relative-value are now all
  falsified — every category Chan describes. Clean, defensible license to close the hunt.
- **Survives**: the first measured edge in the project's history — *and* a new market-neutral
  system, not a rescue of MMM. Helix-the-execution-engine stays the platform; the alpha is a
  different machine bolted onto it. Set expectations accordingly before celebrating.

---

## The hypothesis (single, pre-registered)

> For a **small, economically-motivated** set of FX pairs, the log-price spread of a hedged
> pair is **stationary (cointegrated)** in-sample, **remains stationary** out-of-sample, and
> trading its mean-reversion produces **positive net expectancy after a realistic two-leg
> cost**, surviving Benjamini-Hochberg and an embargoed holdout.

One hypothesis, one pre-registered candidate set, no threshold sweep. If it fails, it fails;
we do not widen the universe or tune thresholds and re-run (that is the forking-paths trap
that produced Sharpe-4.37).

## Candidate set (FIXED — chosen on economic grounds, before any test)

Pre-registered pairs-of-pairs, motivated by shared real-economy drivers, NOT by an
all-vs-all stationarity sweep (which would data-snoop over ~C(22,2)≈231 combinations):

| # | Leg A | Leg B | Economic rationale |
|---|-------|-------|--------------------|
| 1 | AUDUSD | NZDUSD | Commodity/Australasian bloc — the classic FX cointegration pair |
| 2 | EURUSD | GBPUSD | European bloc, shared USD leg |
| 3 | USDCHF | EURUSD | EUR/CHF historically near-pegged → USDCHF and EURUSD co-move tightly |
| 4 | USDCAD | USDNOK*| Oil-linked dollar pairs (*drop if USDNOK absent from broker; do not substitute) |
| 5 | XAUUSD | XAGUSD | Gold/silver — the canonical cointegrated commodity spread (sanity benchmark) |

5 candidates → BH correction over 5 cells. No additions after seeing results. If a leg is
unavailable on the broker, that row is dropped and reported as dropped — never swapped for a
different pair post hoc.

## Method (reuses the existing gauntlet verbatim where possible)

New module `helix_v3/backtest/cointegration_research.py`, parallel to `signal_research.py`,
reusing `training.rule_stats` (`benjamini_hochberg`, `binomial_p_at_least`), the shared
`IN_SAMPLE_END = 2025-01-01` embargo split, and the `CellResult` / `_grade` /
`format_report` machinery. Tests in `tests/test_cointegration_research.py`.

Per candidate pair (A, B):

1. **Hedge ratio — in-sample only.** OLS of log(A) on log(B) over the in-sample window →
   hedge ratio β and spread `s_t = log(A_t) − β·log(B_t)`. β is **frozen** at the in-sample
   value and applied unchanged to the holdout (no look-ahead, no refitting on holdout data).
   *Static OLS first.* Kalman dynamic-β (Chan's upgrade) is a documented OPTIONAL second pass,
   run only if static shows a live signal — it adds parameters, so it must justify itself.
2. **Cointegration gate.** Engle-Granger: ADF test on the in-sample spread residual. Require
   **ADF p < 0.05 in-sample**. Then re-test ADF on the holdout spread (β frozen) — require it
   **stays p < 0.05**. A pair that is cointegrated in-sample but not out-of-sample is DEAD at
   this gate, before any trade is simulated. This gate alone will kill most candidates.
3. **Parameter derivation — no guessing.** Half-life of reversion from the OU regression
   (`half_life = −log(2)/λ`, λ from regressing Δs on lagged s, in-sample). The half-life sets
   the **holding-horizon cap**; entry z-threshold pre-fixed at **|z| ≥ 2.0** (no sweep), exit
   on reversion to z = 0 or horizon cap, hard stop at **|z| ≥ 3.5**.
4. **Labeling — first-touch on the spread.** Enter when |z| ≥ 2 (fade toward mean),
   non-overlapping. First-touch outcome on the spread: reversion to z=0 = favorable, z=±3.5
   stop = unfavorable, horizon-cap close = path-clipped. Result in R-multiples of the
   z=2→3.5 stop distance, **minus the two-leg cost** (next item).
5. **THE COST TEST — done first and cheaply.** Round-trip cost = **open both legs + close
   both legs = 4 spread crossings ≈ 2× the per-leg full spread**, using **median historical
   spread per symbol** (the robust estimate `multiasset_research.py` already established).
   Before simulating anything, compute: does the expected gross reversion move (typical z=2
   deviation × spread-σ, in account currency on a $1k micro-lot) exceed 2× round-trip cost?
   **If gross < cost even in-sample, the candidate is DEAD on arithmetic — no simulation
   needed.** This is where I expect most or all candidates to fall.
6. **Significance + verdict — identical to 3a.** One-sided expectancy t-test on net R; exact
   binomial of favorable rate vs the unconditional spread-reversion base rate; Benjamini-
   Hochberg (q=0.10) across the 5 cells; verdict VALIDATED only if (BH-significant positive
   net-R in-sample) AND (holdout mean net-R > 0 on ≥15 trades) AND (cointegration held in
   holdout, gate 2).

## Kill thresholds (WRITTEN BEFORE RUNNING — the kill is automatic, not negotiable)

The track is **DEAD and the hunt closes** unless, at the end:

- **≥1 candidate** passes ALL of: in-sample ADF p<0.05 **and** holdout ADF p<0.05 **and**
  positive expected gross > 2× cost **and** BH-significant positive in-sample net-R **and**
  holdout net-R > 0 on ≥15 trades.

If **zero** candidates clear that bar → write the result into `SYSTEM_STATUS.md` and
`FORWARD_PLAN.md` as **Track 3d DEAD**, mark the relative-value category falsified, and the
edge hunt is **complete across all four structural categories** → Door B (repurpose the
platform). No "one more universe." No threshold tuning. That is the pre-commitment.

If **≥1 candidate survives** → it advances to Track 2 forward-demo replication (Track 4 gate),
exactly like any other survivor would have. It is NOT funded on the strength of a backtest.

## Time-box

≤ **3 weeks** from approval. Pre-registration today. If the cost test (step 5) kills every
candidate in the first pass — likely — the verdict lands in **days**, not weeks.

## What I need from you now

Approve, amend, or reject **this page** — the candidate set, the |z|≥2 / stop-3.5 thresholds,
the 2× cost model, and the kill bar — *before* I write `cointegration_research.py`. Designing
the harness is mechanical once these are fixed; fixing them after seeing a number is how the
last illusion got built. Your call on the design is the actual decision.
