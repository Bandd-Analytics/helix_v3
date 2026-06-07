# MMM Methodology — Canonical Documentation

Extracted from Steve Mauro's Market Maker Method seminar notes, training videos,
and validated against the Helix V3 codebase implementation.

## Document Index

| # | File | Topic |
|---|------|-------|
| 01 | [market_maker_theory.md](01_market_maker_theory.md) | Core theory: who market makers are, how they move price |
| 02 | [3_day_cycle.md](02_3_day_cycle.md) | The 3-day cycle: L1, L2, L3 levels and peak formation |
| 03 | [weekly_cycle.md](03_weekly_cycle.md) | Weekly structure: early week, mid-week reversal, late week |
| 04 | [session_structure.md](04_session_structure.md) | Daily session phases: Asia, London Gap, London, NY Gap, NYC |
| 05 | [asian_accumulation.md](05_asian_accumulation.md) | Asian session accumulation: range detection and validity |
| 06 | [stop_hunt.md](06_stop_hunt.md) | Stop hunt mechanics: hard hunts, soft hunts, 3 pushes |
| 07 | [mw_formations.md](07_mw_formations.md) | M-top and W-bottom formations: the primary direction signal |
| 08 | [entry_setups.md](08_entry_setups.md) | Trade types: Straightaway, 2nd Leg M/W, The 33, NYC Reversal, EMA 200 Bounce |
| 09 | [candlestick_patterns.md](09_candlestick_patterns.md) | Context-aware patterns: RRT, spike, hammer, pin bar, half batman |
| 10 | [tdi_indicator.md](10_tdi_indicator.md) | TDI: Shark Fin, Blood in the Water, VB Squeeze, hooks, divergence |
| 11 | [pivot_points.md](11_pivot_points.md) | Pivot points: R3/S3, M1-M4 mid-pivots, day-type prediction |
| 12 | [ema_structure.md](12_ema_structure.md) | EMA stack: 5/13/50/200/800, crossovers, trend alignment |
| 13 | [mtf_analysis.md](13_mtf_analysis.md) | Multi-timeframe analysis sequence: Weekly -> H4 -> H1 -> M15 |
| 14 | [trade_management.md](14_trade_management.md) | Trade management: SL, T1, trailing, stale exit, session exit |
| 15 | [risk_management.md](15_risk_management.md) | Risk: per-pair tiers, lot sizing, drawdown limits, re-entry guard |
| 16 | [pair_characteristics.md](16_pair_characteristics.md) | Per-pair behavior: pip values, volatility, optimal sessions |

## Source Attribution

- **Primary**: Steve Mauro MMM Seminar Notes (84-page book)
- **Secondary**: Steve Mauro training video content (pending extraction by Codex)
- **Tertiary**: Helix V3 codebase implementation (validated through live/demo trading)

## Validation Status

Each rule document includes a `Validation Status` section that will be populated
by the rule_validator.py framework once backtesting is complete. Status levels:

- **UNTESTED**: Rule documented but not yet validated against market data
- **VALIDATED**: Rule tested against historical data with statistical significance
- **PARTIALLY_VALIDATED**: Some conditions confirmed, others inconclusive
- **CONTRADICTED**: Market data contradicts the taught rule — needs investigation
- **CALIBRATED**: Rule validated AND parameters tuned from historical data
