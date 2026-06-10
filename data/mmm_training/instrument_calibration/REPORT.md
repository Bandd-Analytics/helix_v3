# Instrument Calibration Report

Generated: 2026-06-09 14:29 EAT

This is an offline research audit. It does not place, modify, or close trades.

## Summary

| Symbol | Status | Tradeable | Digits | Point | PipSize | TickSize | TickValue | PipValue/Lot | Spread | Occ | Demo | Asym | AvgExit | P90Abs | AvgValue/Lot |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| XAUUSD | RESEARCH_CALIBRATED_EXECUTION_BLOCKED | 0 | 2 | 0.010000 | 0.010000 | 0.010000 | 1.00 | 1.00 | 7.0 | 7789 | 8 | 18 | -192.1 | +1497.0 | -192.12 |
| US30 | RESEARCH_CALIBRATED_EXECUTION_BLOCKED | 0 | 2 | 0.010000 | 0.010000 | 0.010000 | 0.01 | 0.01 | 120.0 | 97 | 0 | 0 | +674.3 | +8915.0 | 6.74 |
| USTEC | RESEARCH_CALIBRATED_EXECUTION_BLOCKED | 0 | 2 | 0.010000 | 0.010000 | 0.010000 | 0.01 | 0.01 | 100.0 | 160 | 0 | 1 | +65.7 | +7373.0 | 0.66 |

## Notes

### XAUUSD
- MT5 units: point=0.01, pip_size=0.01, pip_value_per_lot=1.00.
- Replay translation: avg_exit_price_move=-1.921, p90_abs_exit_price_move=14.970, p90_mfe_price_move=11.950, p90_mae_price_move=9.160.
- PairProfile is analysis-only; keep out of live validation and auto-entry.
- Promising research candidates exist, but visual flashcard and demo validation are still required.

### US30
- MT5 units: point=0.01, pip_size=0.01, pip_value_per_lot=0.01.
- Replay translation: avg_exit_price_move=6.743, p90_abs_exit_price_move=89.150, p90_mfe_price_move=92.000, p90_mae_price_move=79.500.
- PairProfile is analysis-only; keep out of live validation and auto-entry.
- Index point values are broker-specific; require manual contract-value approval.
- No expectancy candidates found in setup intelligence.

### USTEC
- MT5 units: point=0.01, pip_size=0.01, pip_value_per_lot=0.01.
- Replay translation: avg_exit_price_move=0.657, p90_abs_exit_price_move=73.730, p90_mfe_price_move=71.000, p90_mae_price_move=53.600.
- PairProfile is analysis-only; keep out of live validation and auto-entry.
- Index point values are broker-specific; require manual contract-value approval.
- Promising research candidates exist, but visual flashcard and demo validation are still required.
