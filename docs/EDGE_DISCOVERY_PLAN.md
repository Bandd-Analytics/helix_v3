# Helix V3 — Edge Discovery Plan

Source: post-audit strategic direction, 2026-06-15. The audit (`docs/AUDIT_FIX_PLAN.md`,
now fully closed) proved the system protects capital correctly but that **no directional
MMM rule beats its base rate** — Tier 2.4 killed `mw_direction`, `midweek_reversal`,
`pivot_day_map`, and `asian_accumulation` on every pair; only defensive timing rules
(stale/Friday exits) survived. This plan is about earning a *real, measured* directional
edge from data, or honestly concluding there isn't one.

**Rule of engagement: the Sharpe-4.37 mistake must not recur.** Every claimed edge passes
the same gauntlet that killed the rules: first-touch labeling, non-overlapping samples,
binomial test vs the empirical base rate, Benjamini-Hochberg across the whole grid, and a
true embargoed walk-forward holdout. A signature that doesn't survive all five **dies**.

Status legend: `[ ]` todo · `[~]` in progress · `[x]` done

---

## Grounding facts (measured 2026-06-15)

- `logs/vision_backtests.db`: **56,225 labeled outcomes**, **2022-03-16 → 2026-06-11**
  (~4.25 yr), **15 symbols**, **5,766 distinct `normalized_key` signatures**.
- Signature space is **over-granular**: median **2 samples/signature**. Per-(pair,key)
  cells with N≥30 = 249; N≥50 = 47. The tiny-N "100% fav / PF 999" candidates in the
  feature ablation are noise, not edge.
- **Cross-pair pooling ~5×'s the testable universe**: pooled keys with N≥30 = 425,
  N≥50 = 249, N≥100 = 104. The lever for statistical power is **coarsening the signature
  scheme + cross-pair pooling**, not more history.

## Current-state diagnosis (why edge isn't proven)

1. **The live edge-layer is a disproven model.** `advisory_confidence.py` gates on
   hand-tuned MMM weights (M/W +8, TDI conflict −20, …) — exactly the components Tier 2.4
   refuted. Zero empirical calibration.
2. **The rigorous statistics never reached the signature space.** Tier 2.4's
   `training/rule_stats.py` (first-touch, binomial vs base rate, BH) was applied to a few
   *rules*; the feature-ablation engine (`training/vision_filter_ablation.py`) searches the
   *signature* space with naive 85%-fav / +10.9-pip thresholds and **no multiple-testing
   correction** across 26 variants × ~13 pairs × many setups.
3. **Nothing is validated out-of-sample.** Every "demo_watch_candidate" (GBPNZD, AUDUSD)
   has **out-of-sample N = 0** — they passed train+validation on N=9–11 and the holdout
   fold is empty.
4. **The learning loop is open.** No live/demo outcome → replay → promotion path is wired
   (`validation_library` is read-only at runtime); the system can't earn forward evidence.
5. **Unified signatures, fragmented gating.** `setup_intelligence`, the feature ablations,
   and `validation_library` share the `normalized_key` scheme but are otherwise
   disconnected; setup intelligence only *logs* an RRS tag — it gates nothing.

---

## Phase 1 — Statistical signature audit (does ANY edge exist?)

Cheapest honest verdict, reuses `rule_stats.py`. Pure offline analysis over the 56k
outcomes; no live wiring. Likely most signatures die (as the rules did) — that is a valid
and important result, not a failure.

- [x] **1.1 Verify + lock the labeling.** (Done 2026-06-15.) Confirmed
  `mmm_event_replay.label_mmm_event_path` is **first-touch / path-ordered**: it walks future
  bars in time order, simulates full MMM management (SL → T1/breakeven → trail → stale →
  max-duration), checks SL before targets, and returns `AMBIGUOUS` when SL and a target are
  both reachable in one OHLC candle. This is NOT the MFE>MAE defect — no relabeling needed.
  Outcome taxonomy over the 56,225 stored labels: STALE_EXIT 40.6%, LOSS 21.2%,
  TIME_EXIT_PROFIT 16.3%, BREAKEVEN_AFTER_T1 5.3%, TARGET_2 4.5%, AMBIGUOUS 3.8% (excluded),
  TRAIL_STOP 3.5%, TIME_EXIT_LOSS 3.1%, … `favorable` = {TARGET_2, TRAIL_STOP,
  TIME_EXIT_PROFIT}. **Base favorable rate over 53,569 resolved outcomes = 25.5%** — a
  low-hit-rate / run-the-winners profile (consistent with the −7.3% Tier 1.9 backtest).
- [x] **1.2 Coarse signature scheme.** (Done 2026-06-15: `helix_v3/backtest/signature_audit.py`.)
  Positional projection of the 13-dim `normalized_key` onto configurable facets. Five
  a-priori schemes graded each on its own grid (chosen before looking at results — no
  forking paths): S0 direction-only (sanity), S1 family×dir×tdi, S2 +mw, S3 +hunt,
  S4 +session. Turns 5,766 sparse keys into tens–hundreds of N≥30 cells.
- [x] **1.3 Cross-pair pooling.** (Done.) Every scheme run per-pair AND pooled (POOLED,
  direction-controlled). Pooled grids reach the largest N (e.g. THE_33_MW BUY cells of
  n>2000); per-pair grids preserve drill-down.
- [x] **1.4 The audit itself.** (Done.) Per cell: non-overlapping sampling (greedy by
  snapshot→exit window), **binomial test** of favorable rate vs the empirical
  unconditional rate of the same (symbol, direction), AND a one-sided **expectancy test**
  (mean net-R > 0, normal-approx) to catch asymmetric/fat-tail edges a hit-rate test misses.
  **Benjamini-Hochberg q=0.10 on BOTH tracks** across each grid. Expectancy in net R-multiples
  (`(exit_pips − round-trip cost) / sl_pips`, cross-pair comparable). Verdict per cell. Tests
  in `tests/test_signature_audit.py` (incl. a planted-edge positive control + S0 sanity).
- [x] **1.5 Embargoed walk-forward holdout.** (Done.) In-sample < 2025-01-01, holdout ≥
  2025-01-08 (7-day embargo). VALIDATED only if BH-significant (either track) AND positive
  net-R in-sample AND positive net-R on the holdout with N≥15.
- [x] **1.6 Accept the verdict.** (Done 2026-06-15. Report: `logs/signature_audit.md`.)
  **TOTAL VALIDATED = 0 across all 10 grids.** A faint, real hit-rate signal exists (a
  handful of cells beat base by ~3–8pp at p<0.01, large N) but **every BH-significant cell
  has NEGATIVE net-R** — the edge is too small for the run-the-winners payoff at any cost.
  **0 cells are expectancy-BH-significant** (gross or net). The only directionally-consistent
  positive is **SECOND_LEG_MW BUY** (second-leg M/W *continuation* longs — NOT the primary
  M/W reversal): gross +0.04…+0.14R that replicates across the embargo (e.g.
  `SECOND_LEG_MW|BUY|HUNT_PAIR_RANGE|TDI_CONFIRM` +0.08R n133 → +0.07R n155), but it is
  **sub-BH-significant even gross and goes net-negative after costs.** The S0 direction-only
  control sits exactly at base rate (0 significant) and the planted-edge test validates —
  so this is a true negative, not a power failure. **Verdict: no tradeable directional edge
  exists at the signature level**, extending Tier 2.4's rule verdict to the full signature
  space. The SECOND_LEG_MW continuation lead is the single most promising direction for any
  future research, but it does not clear significance or costs today. → Phase 2 has nothing
  to forward-validate; the project pivots to what IS validated (regime + defensive timing).

## Phase 2 — Close the demo → outcome → promotion loop (forward validation)

**GATED OUT (2026-06-15): Phase 1 yielded zero survivors — there is nothing to
forward-validate.** Closing the loop is still worthwhile infrastructure for the day a
survivor exists, but it is no longer the next step. Left here as the standing design for
when/if a future signal clears the Phase 1 bar.

Only if Phase 1 yields survivors. Turns the open learning loop into a closed one so
survivors accrue genuine forward OOS evidence before any real-money consideration.

- [ ] **2.1 Live/demo outcome recording.** Wire executed demo trades → flashcard/outcome →
  `mmm_event_replay` store (no live write point exists today). Idempotent, server-time
  stamped (reuse `market_time`).
- [ ] **2.2 Walk-forward promotion, embargoed.** Call `promote_from_replay(before=…)`
  (the Tier 1.3 param exists but the orchestrator never passes it) at EOD so promotion can
  never use outcomes inside its own evaluation window.
- [ ] **2.3 Wire survivors into the live gate.** Replace/augment the disproven advisory
  weights with the Phase-1-validated signature edge. Decide and document gate semantics
  (membership-required vs confidence-boost) and keep the <30% graveyard block. Vision stays
  a logger (Tier 2.7) until it shows lift.
- [ ] **2.4 Forward-validate.** Accumulate real OOS demo outcomes on the survivors; promote
  to "tradeable" only after the forward fold independently clears the Phase-1 bar. No
  real-money sizing until a survivor has forward evidence, not just historical.

## Phase 3 — Feature model (conditional — DECISION PENDING)

Phase 1 did not show strong latent signal — the one positive lead (SECOND_LEG_MW BUY
continuation) is sub-BH-significant and cost-negative, exactly the regime where an ML model
most easily manufactures an overfit illusion (the Sharpe-4.37 trap). The disciplined default
is **skip**. The only argument *for* a focused model is to test whether a sub-population of
SECOND_LEG_MW BUY is larger than the ~0.1R pooled gross average. **This is a strategic
go/no-go for the user**, not an automatic step.

Only if Phase 1 shows latent signal that bucketed signatures can't capture (e.g. strong
univariate lifts that don't isolate into a clean cell). Otherwise skip.

- [ ] **3.1 Engineered-feature model.** Gradient-boosted trees / logistic over continuous
  setup features (hunt/AR ratios, push counts, TDI values, confluence, regime, session)
  predicting first-touch favorable. Nested CV for tuning + a single embargoed holdout year
  for the verdict. Calibrated probabilities (reliability curve), not raw scores.
- [ ] **3.2 Honest comparison.** The model earns its place only if its holdout expectancy
  beats both the quant baseline and the Phase-1 signature set at realistic costs.

---

## Non-negotiable correctness gates (apply to every phase)

- First-touch / path-ordered labeling — never MFE>MAE.
- Non-overlapping samples (no window double-counting).
- Multiple-testing correction (Benjamini-Hochberg) across the full grid tested.
- True embargoed holdout; never promote from the evaluation window.
- Realistic costs (reuse Tier 1.5 spread/commission/slippage).
- Report dropped/under-powered cells loudly — silent truncation reads as coverage.

## Definition of done

A written, accepted verdict on whether a measured directional edge exists:
- **If yes** — a holdout-replicated, cost-positive signature set wired into live gates with
  a closed forward-validation loop (Phases 1+2 done), and a recorded forward track record
  before any real-money step.
- **If no** — the honest conclusion that directional edge is unproven at the signature level,
  with the project explicitly pivoted to what *is* validated (regime + defensive timing),
  recorded the same way Tier 1.9 accepted −7.3%.
