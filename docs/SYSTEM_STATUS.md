# Helix V3 — Honest System Status

Last updated: 2026-06-15.

## One-line status

**Capital-safe. Entry-edge UNPROVEN. DEMO ONLY — do not fund.**

## What this means

The system will not blow up — the audit (`docs/AUDIT_FIX_PLAN.md`, closed) hardened every
capital-loss path. But two independent honest analyses proved it has **no validated
directional edge**:

- **Tier 2.4** killed every directional MMM *rule* (mw_direction, midweek_reversal,
  pivot_day_map, asian_accumulation) on every pair.
- **Edge Discovery Phase 1** (`docs/EDGE_DISCOVERY_PLAN.md`, `helix_v3/backtest/signature_audit.py`)
  found **0 validated signatures across 10 grids**; every pair's best in-sample cell collapses
  out of sample. No tradeable directional edge exists at the signature level either.
- **The honest backtest** (365-day, look-ahead-free, real costs) loses money in every
  configuration: **−5.8% with the advisory gate demoted, −7.1% with it on**, both tripping
  the 8% drawdown breaker.

So the system's directional entries are **no better than chance after costs.** Running it on
real money would be funding a coin flip with a spread.

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
   produced the original Sharpe-4.37 illusion. Edge candidates come only from the disciplined
   Track 3 search.
4. **The path to a real edge is `docs/FORWARD_PLAN.md` Track 3** (currently 3a: FX non-MMM
   signals), validated through the same gauntlet, then forward-validated on demo (Track 2).

## The honest framing

The audit and Phase 1 did not fail — they prevented trading a no-edge system as if it had one.
The system today is a well-built, capital-safe *execution and risk* platform that is still
*searching for* its alpha. That search is the real work ahead.
