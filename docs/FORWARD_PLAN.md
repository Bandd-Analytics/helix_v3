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

- [x] **2.1 Live/demo outcome recording.** (Done 2026-06-15.) `orchestrator_v2._record_live_replay_outcome`
  joins the setup captured at entry with the closed trade-journal row (synced before the
  handler runs) by ticket and records a live `MMMEventOutcome` to the replay store — the
  previously-dead write point. New pure `mmm_event_replay.live_outcome_from_journal_row` maps
  the journal exit_reason + economics into the SAME replay taxonomy the audit consumes (so
  live and backtest data are comparable). The replay store writes `vision_backtests.db` — the
  audit's own source — so forward outcomes feed the audit automatically. Tests in
  `tests/test_live_replay_outcome.py`.
- [x] **2.2 Embargoed promotion wired.** (Done 2026-06-15.) The EOD `promote_from_replay` call
  now passes `before = now − PROMOTION_EMBARGO_DAYS` (default 7), so a pattern can never be
  promoted from the very trades about to be taken — the Tier 1.3 walk-forward separation now
  holds live too.
- [x] **2.3 Standing monthly re-audit.** (Done 2026-06-15.) `_kick_monthly_signature_audit`
  runs `signature_audit.run_audit` in a daemon thread on the 1st-of-month report tick and
  notifies the validated-cell count (0 = "remains DEMO ONLY"). Live outcomes accrue into the
  audit's store, so the monthly check sees forward demo data with no extra plumbing.
- [ ] **HARD GATE.** No real capital until Track 3 produces a survivor that ALSO replicates
  on this forward demo data. *(Standing — not a code task.)*

## Track 3 — Find a real entry edge (the substantive work, months)

The only honest road to profit. Reuse `signature_audit.py` + `rule_stats.py`; same gauntlet.
**Pick ONE domain to start** (decision below) — do not search all at once (multiple-testing).

- [x] **3a — FX, non-MMM signals.** *(Concluded 2026-06-16 — 6 families, all DEAD. Harness:
  `helix_v3/backtest/signal_research.py`, tests `tests/test_signal_research.py`.)* Reusable
  gauntlet for fresh signals: per-entry ATR brackets, first-touch labels, non-overlap,
  binomial + expectancy tests, BH, embargoed walk-forward — identical discipline to Phase 1.
  **First batch (3 families × 7 majors, H4, report `logs/signal_research_h4.md`): VALIDATED
  = 0.** Donchian breakout + MA cross trade BELOW base rate (no intraday trend on H4 majors);
  z-score mean-reversion is the least-bad (55–56% fav vs 51–52% base on NZD/GBP) but is
  sub-BH-significant and collapses out of sample. Same fingerprint as MMM — faint leads, no
  survivors. **Cross-sectional momentum added (`audit_cross_sectional`, pooled across majors):
  n=2018, hit-rate 51% vs 48% base, p=0.002 (significantly above base!) — but netR −0.07 and
  holdout −0.15 → DEAD.** A real hit-rate edge that doesn't pay after costs. **Carry added**
  (swap-ranked direction, D1, 20-day HOLDING return — `audit_carry` + `_label_holding_return`,
  since carry is a slow premium not a bracket-timing edge): n=336, 54% positive vs 49% base,
  p=0.045, **netR +0.126 in-sample (POSITIVE — the carry premium is real)** but **holdout
  −0.164 → DEAD.** Textbook carry: a crash-prone risk premium that pays for years then unwinds;
  the embargoed 2025–26 holdout caught a USD-carry drawdown. The closest any family came to an
  edge — but not robust under the discipline. **Cross-sectional currency-strength added**
  (currency-decomposed over a 22-pair basket, nets USD out — `audit_currency_strength`):
  n=1254, 45% vs 48% base (BELOW base), netR −0.18, holdout −0.12 → DEAD. **Regime-conditioned
  carry added** (the most promising lead chased to ground — `audit_carry_regime` +
  `_vol_percentile_series`, carry gated to the VALIDATED Tier 2.8 vol band [P10,P95] from
  `regime.py`, point-in-time per entry, control = same calm-regime bars): n=200, 54% vs 46% base,
  **p_hit 0.020 (now significant above base in-sample, up from 0.207 ungated), netR +0.07
  in-sample** — but **holdout −0.45 (WORSE than ungated carry's −0.17) → DEAD.** Textbook
  overfitting fingerprint: the calm-vol gate improved *every* in-sample number while the embargoed
  holdout collapsed harder — the gate concentrated entries into the worst of the 2025–26 carry
  unwind. Pre-registered, single hypothesis, no threshold sweep — exactly the discipline that
  killed Sharpe-4.37. **Six families tested, all DEAD.** **Verdict reached: no robust directional
  FX edge in classic signals. Carry is a real-but-unreliable premium that does not survive the
  embargo even when regime-gated. 3a is concluded — the price-signal/carry well is dry.** Next:
  **Track 3b (management-as-alpha)** — the only validated component is defensive, so test whether
  good exits + a cheap neutral entry beats costs. (D1/weekly price signals remain a theoretically
  possible avenue but carry the same fingerprint and lower prior; deprioritized below 3b.)
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
