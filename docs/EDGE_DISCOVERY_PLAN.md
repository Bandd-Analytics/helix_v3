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

- [ ] **1.1 Verify + lock the labeling.** Confirm `mmm_event_replay.label_mmm_event_path`
  is **first-touch / path-ordered** (stop wins same-bar ambiguity), NOT MFE>MAE — the exact
  defect Tier 2.4 found in the old `rule_validator`. If it isn't, relabel the 56k outcomes
  through the `rule_stats` first-touch labeler. Define `favorable` once and reuse it. This
  is the correctness foundation; everything downstream is void if labels are path-blind.
- [ ] **1.2 Coarse signature scheme.** Add a configurable, lower-cardinality projection of
  the 13-dim `normalized_key` (e.g. `setup_family × direction × tdi_state × hunt_bucket`,
  with the noisiest dims collapsed) targeting cells of N≥30. Keep the full key for drill-down.
  Goal: turn 5,766 sparse keys into ~hundreds of well-powered cells.
- [ ] **1.3 Cross-pair pooling.** Currency-agnostic test of each coarse signature pooled
  across the 15 symbols (425 keys reach N≥30 pooled). Report pair-level breakdown alongside
  the pooled verdict so a pooled edge driven by one pair is visible.
- [ ] **1.4 The audit itself.** For each coarse signature: binomial test of its first-touch
  favorable rate vs the **empirical unconditional first-touch base rate** (per pair and
  pooled), on **non-overlapping** samples, with **Benjamini-Hochberg at q=0.10 across the
  entire signature grid**. Also report expectancy in pips at realistic costs (reuse the
  Tier 1.5 cost model). Output: a ranked table of signatures with p-value, base rate,
  lift, expectancy, BH-significance, verdict (VALIDATED / DEAD / INSUFFICIENT_N).
- [ ] **1.5 Embargoed walk-forward holdout.** Split 2022–2024 (in-sample) vs 2025–2026
  (holdout) with a ≥1-week embargo. A signature is **VALIDATED only if it survives BH
  in-sample AND replicates on the holdout** (same direction, still beats base rate). This is
  the true OOS gate the feature ablation never had.
- [ ] **1.6 Accept the verdict.** Record the surviving signature set (or the honest "none
  survive") to a log, exactly as Tier 1.9 / 2.4 accepted their numbers. If a non-empty,
  cost-positive, holdout-replicated set exists → proceed to Phase 2. If not → the directional
  edge is disproven at the signature level too, and the project pivots (regime/timing-only
  execution, or Phase 3 feature search as a last look).

## Phase 2 — Close the demo → outcome → promotion loop (forward validation)

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

## Phase 3 — Feature model (conditional)

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
