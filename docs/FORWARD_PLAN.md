# Helix V3 — Path Forward

Date: 2026-06-15. Written after the audit closed and Edge Discovery Phase 1 concluded.

## Where we honestly stand

- **The audit is closed.** The system is *capital-safe*: kill switch, regime filter,
  news blackout, exposure caps, idempotent order-send, journal correctness, watchdog.
  It will not blow up.
- **There is no validated directional edge.** Two independent honest analyses agree:
  Tier 2.4 killed every directional MMM *rule*; Edge Discovery Phase 1 (`signature_audit.py`)
  found **0 validated signatures across 10 grids**, and a per-pair test showed *every* pair's
  best in-sample cell collapses out of sample. MMM does not predict direction on any of the
  15 instruments tested, and zero-cost doesn't change it.
- **What IS validated is entirely defensive** — regime gating (2.8), defensive timing exits
  (2.4 stale/Friday), sizing/safety. None of it picks entry direction. **The system has no
  validated ENTRY edge at all.**
- **The broker universe is broad** (FX majors/minors/exotics, commodities, indices, crypto,
  bonds, hundreds of stock CFDs) but **MMM is an FX-session method** — it does not transfer to
  single-name equities or 24/7 crypto. Broad-universe alpha is a *different, larger program*,
  not MMM pair selection.

**The one rule that governs everything below: no real capital is risked until a specific
entry edge has been forward-validated on demo. Every edge candidate clears the same gauntlet —
first-touch labels, non-overlapping samples, binomial + expectancy tests, Benjamini-Hochberg,
embargoed walk-forward, realistic costs.** This is the discipline that killed the Sharpe-4.37
illusion; it is non-negotiable.

Status legend: `[ ]` todo · `[~]` in progress · `[x]` done

---

## Track 1 — Make the live system honest (days)

Stop the system from *claiming* a directional edge it doesn't have. Small, concrete code.

- [x] **1.1 Demote the directional confidence gate to a logger.** (Done 2026-06-15, commit
  17453f4.) `advisory_confidence`'s grade is computed + journaled for research but no longer
  blocks entries, in BOTH the live orchestrator and the backtest engine, behind a new
  `ADVISORY_GATE` toggle (default false = demoted). Mirrors the Tier 2.7 vision demotion.
  Tests in `tests/test_advisory_gate_demotion.py`.
- [x] **1.2 A/B the gate empirically, don't assume.** (Done 2026-06-15. Logs:
  `logs/ab_gate_off.log` / `logs/ab_gate_on.log`.) Honest 365-day backtest both ways.
  **Gate OFF (demoted): −$58.10 (−5.8%), 76 trades, 27.6% win, PF 0.67, Sharpe −1.49, DD
  8.4%. Gate ON (legacy): −$70.99 (−7.1%), 88 trades, 29.5% win, PF 0.71, Sharpe −0.99, DD
  8.3%.** Both lose and both trip the 8% breaker — no configuration of the directional
  system is investable. The gate adds no value; demoted keeps marginally more capital with
  less churn. **Decision: keep the gate OFF (demoted default).** The PF/Sharpe vs net-$
  split is noise around a clearly-losing system — the gate is not a lever that matters.
- [x] **1.3 Re-baseline and accept.** (Done 2026-06-15.) **The honest pivoted baseline is
  −$58.10 / −5.8% over 365 days, PF 0.67, daily-$ Sharpe −1.49, DSR prob 0.00, max MTM DD
  8.4%, breaker tripped.** Accepted, exactly as Tier 1.9 accepted −7.3%. There is no entry
  edge; the number is negative by construction and that is the truth of the system today.
- [x] **1.4 Document system status.** (Done 2026-06-15: `docs/SYSTEM_STATUS.md`.)
  *Capital-safe, entry-edge unproven, DEMO ONLY.* The validated defensive gates are the
  system's real value; directional entries are unproven and must not be funded.

## Track 2 — Close the demo→outcome loop for forward truth (≈1 week)

Repurpose the Edge-Discovery Phase 2 infrastructure. Not to promote MMM survivors (there are
none) — to collect **genuine forward out-of-sample outcomes** so the negative is confirmed
(or, if we're wrong, refuted) on live demo data, and any latent signal would surface.

- [ ] **2.1 Live/demo outcome recording.** Wire executed demo trades → flashcard/outcome →
  `mmm_event_replay` store (the missing live write point). Idempotent, server-time stamped.
- [ ] **2.2 Embargoed promotion wired.** Call `promote_from_replay(before=…)` at EOD so IF
  anything ever clears the bar, it's promoted honestly (never from its own window).
- [ ] **2.3 Standing monthly re-audit.** Re-run `signature_audit.py` over the growing dataset
  (historical + forward demo). A cron/scheduled check, not a one-off.
- [ ] **HARD GATE.** No real capital until Track 3 produces a survivor that ALSO replicates
  on this forward demo data.

## Track 3 — Find a real entry edge (the substantive work, months)

The only honest road to profit. Reuse `signature_audit.py` + `rule_stats.py`; same gauntlet.
**Pick ONE domain to start** (decision below) — do not search all at once (multiple-testing).

- [ ] **3a — FX, non-MMM signals.** Trend/momentum (timeframe breakout, MA stacks), carry
  (swap-ranked longs/shorts), mean-reversion (band fade), cross-sectional currency strength.
  FX is the cheapest, most liquid universe — best cost profile, lowest overfit surface.
  *Recommended first* — same instruments we know, fresh signal families, cheap to test.
- [ ] **3b — Management-as-alpha.** The ONLY thing that validated is defensive (exits/sizing).
  Test whether good exits + a cheap neutral entry (e.g. mean-reversion fade) beats costs —
  i.e. the edge lives in *management*, not entry selection. A genuinely different hypothesis.
- [ ] **3c — Multi-asset breadth.** The broad CFD universe (equities, indices, commodities,
  crypto) with *instrument-appropriate* signals (momentum, cross-sectional, vol). Highest
  overfit risk and worst costs → do LAST, with the most discipline, only if 3a/3b stall.
- [ ] **3.x — Per candidate**: define signal → first-touch label → audit (BH + embargo +
  cost) → survivors only advance to Track 2 forward demo. Most candidates will die; that's
  the process working.

## Track 4 — Gate to real capital (only after Track 3 + Track 2 deliver)

- [ ] A survivor must clear, in order: (1) in-sample BH-significant + cost-positive,
  (2) embargoed holdout replication, (3) forward demo replication for ≥N trades (Track 2).
  Only then size real capital, starting at the broker minimum, scaling with realized track
  record. Never skip a stage.

---

## The decision in front of you

1. **Run Tracks 1+2 now** (make the system honest + collect forward truth) — low effort,
   high integrity, no downside. I recommend doing this regardless.
2. **Choose the Track 3 domain to pursue for a real edge**: **3a FX-non-MMM** (recommended
   first), **3b management-as-alpha**, or **3c multi-asset** — or explicitly pause Track 3
   and run only 1+2 for now while you decide.

My recommendation: **do Tracks 1+2 immediately, and start Track 3 with 3a (FX, non-MMM
signals).** It reuses everything we've built, has the best cost/overfit profile, and is the
fastest way to learn whether *any* systematic edge exists on the instruments we already trade —
before committing to the much larger, riskier multi-asset search.
