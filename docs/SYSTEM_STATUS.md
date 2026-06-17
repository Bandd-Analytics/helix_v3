# Helix V3 — Honest System Status

Last updated: 2026-06-17.

## One-line status

**Capital-safe. Entry-edge UNPROVEN. DEMO ONLY — do not fund.**

## What this means

The system will not blow up — the audit (`docs/AUDIT_FIX_PLAN.md`, closed) hardened every
capital-loss path. But a **completed, thorough edge hunt** proved it has **no validated
directional edge** — not in the original MMM rules, and not in any alternative searched:

- **Tier 2.4** killed every directional MMM *rule* (mw_direction, midweek_reversal,
  pivot_day_map, asian_accumulation) on every pair.
- **Edge Discovery Phase 1** (`docs/EDGE_DISCOVERY_PLAN.md`, `helix_v3/backtest/signature_audit.py`)
  found **0 validated signatures across 10 grids**; every pair's best in-sample cell collapses
  out of sample. No tradeable directional edge exists at the signature level either.
- **The honest backtest** (365-day, look-ahead-free, real costs) loses money in every
  configuration: **−5.8% with the advisory gate demoted, −7.1% with it on**, both tripping
  the 8% drawdown breaker.

**The Forward-Plan Track 3 edge hunt is now COMPLETE (2026-06-17) — FOUR structurally
distinct avenues, the same gauntlet (first-touch labels, non-overlap, binomial + expectancy,
Benjamini-Hochberg, embargoed walk-forward, realistic costs), all DEAD:**

- **3a — FX non-MMM signals** (`signal_research.py`): 6 families — Donchian, MA-cross, z-fade,
  cross-sectional momentum, carry, regime-gated carry. Carry was the closest (real but
  crash-prone premium); none survived the embargoed holdout.
- **3b — Management-as-alpha** (`management_research.py`): 14 cells — can exit management turn a
  *direction-neutral* entry profitable? No. "Cut quick" hits 65% but still loses (hit-rate ≠
  expectancy); trailing stops were among the worst.
- **3c — Multi-asset momentum** (`multiasset_research.py`): D1 time-series momentum on index /
  gold / crypto CFDs. The harness flagged a nominal survivor — but the benchmark-relative test
  showed **no alpha over buy-and-hold** (pooled mean diff −0.29 in-sample, −0.30 holdout,
  negative on all 6 instruments). The apparent edge was *beta to a 2025 bull market*, not alpha.
- **3d — Relative value / cointegration** (`cointegration_research.py`, pre-registered in
  `docs/EDGE_3D_COINTEGRATION.md`): the one *market-neutral* category — spread reversion, not
  direction. 5 economically-chosen pairs, hedge ratio frozen in-sample, Engle-Granger ADF gate
  required in-sample AND across the embargoed holdout. **All five failed the cointegration gate.**
  AUDUSD/NZDUSD was stationary in-sample (ADF −4.23) but broke out of sample (ADF +0.21); the
  rest weren't cointegrated even in-sample. Cost was expected to be the killer but never bit —
  instability did. No survivor, so no simulator was built.

The four avenues span every category in Chan's taxonomy of systematic edge — direction (3a),
management of a neutral entry (3b), trend (3c), and market-neutral spread reversion (3d). The
system's entries are **no better than chance after costs**, no tested alternative beats a
passive benchmark, and the one market-neutral hope was not stable enough to trade. Running it
on real money would be funding a coin flip with a spread. The negative is now thorough across
the whole map, not provisional.

## What IS validated (and is genuinely valuable)

Purely *defensive* machinery — it protects capital, it does not generate alpha:

- Kill switch + persisted drawdown breaker (Tier 0.4)
- Regime filter — trade only when D1 vol/trendiness say conditions exist (Tier 2.8)
- News blackout + defensive management around high-impact events (Tier 2.5)
- Per-currency net exposure cap (Tier 2.6)
- Defensive timing exits — stale-exit, Friday-exit (the only Tier 2.4 survivors)
- Idempotent order-send, filling-mode/stops portability, journal correctness, MT5 watchdog

## Operating rules until an edge exists

1. **DEMO ONLY.** No real capital. The forward-plan gate (Track 4) requires an edge that
   passes in-sample BH + cost + embargoed holdout AND replicates on forward demo before any
   funding.
2. **Advisory grade is a logger, not a gate** (`ADVISORY_GATE=false`, default). It is
   journaled for research; it does not block entries.
3. **Do not expand pairs/instruments to chase edge.** That is the forking-paths trap that
   produced the original Sharpe-4.37 illusion. 3c already tested the disciplined multi-asset
   case and found no alpha — do not reopen it as an unconstrained instrument sweep.
4. **Track 3 is complete and exhausted** (`docs/FORWARD_PLAN.md`). Do NOT re-test 3a/3b/3c —
   they are settled negatives. A new edge candidate must be a *genuinely new hypothesis*, run
   through the same gauntlet AND benchmarked against the right null (e.g. buy-and-hold for
   drifting assets, not zero), then forward-validated on demo (Track 2) before any funding.
5. **Track 2 keeps running** — live/demo outcomes accrue to the replay store and the monthly
   signature re-audit stays armed, so any latent forward signal would still surface on its own.

## The honest framing

The audit, Phase 1, and the completed Track 3 hunt did not fail — they prevented trading a
no-edge system as if it had one, and they did so *thoroughly*: every plausible directional
hypothesis we could pose was tested and honestly rejected, including one that briefly looked
like a winner until the correct benchmark exposed it. The system today is a well-built,
capital-safe *execution and risk* platform for which **no directional alpha has been found to
exist** on the instruments and methods available to it. That is not a gap waiting to be filled
by more searching of the same ground — it is a measured result. Any future work must bring a
genuinely new edge hypothesis to the table; absent that, the honest use of this system is as a
disciplined, defensive, demo-only research platform.
