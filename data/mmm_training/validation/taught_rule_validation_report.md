# MMM Taught Rule Validation Report

Generated: 2026-06-07T11:21:45.896371+00:00

Scope: first-pass historical M15 replay of paraphrased MMM training rule cards.
These are detector hypotheses, not promoted trading rules.

## Promotion State

- Promoted rules: none.
- Watchlist: MMM-TRAIN-002 GBPJPY, MMM-TRAIN-004 GBPJPY, MMM-TRAIN-004 AUDUSD, MMM-TRAIN-004 USDJPY, MMM-TRAIN-004 EURJPY
- Needs stricter filters: MMM-TRAIN-002 EURUSD, MMM-TRAIN-002 GBPUSD, MMM-TRAIN-002 USDJPY, MMM-TRAIN-002 AUDUSD, MMM-TRAIN-002 EURJPY, MMM-TRAIN-002 GBPCHF, MMM-TRAIN-003 AUDUSD, MMM-TRAIN-003 EURUSD, MMM-TRAIN-003 GBPJPY, MMM-TRAIN-003 EURJPY, MMM-TRAIN-003 USDJPY, MMM-TRAIN-003 GBPCHF, MMM-TRAIN-003 GBPUSD, MMM-TRAIN-004 EURUSD, MMM-TRAIN-004 GBPUSD, MMM-TRAIN-004 GBPCHF, MMM-TRAIN-006 GBPJPY, MMM-TRAIN-006 AUDUSD, MMM-TRAIN-006 USDJPY, MMM-TRAIN-006 EURJPY, MMM-TRAIN-006 GBPUSD, MMM-TRAIN-006 EURUSD, MMM-TRAIN-006 GBPCHF

## Scanner Baseline Gate

- Current scanner baseline: 90m scanner baseline: N=100, Fav=85.0%, AvgExit=+10.9p, MFE=+24.0p, MAE=+4.5p
- No taught candidate is promoted unless it beats the scanner baseline after pair-specific replay.

## Results

| Decision | Rule | Symbol | N | Fav% | T1% | AvgExit | MFE | MAE |
|---|---|---|---:|---:|---:|---:|---:|---:|
| watch_weak_pair_specific | MMM-TRAIN-002 | GBPJPY | 50 | 44.0% | 18.0% | 5.7 | 26.4 | 18.5 |
| needs_stricter_filter | MMM-TRAIN-002 | EURUSD | 50 | 28.0% | 22.0% | 1.6 | 10.0 | 8.5 |
| needs_stricter_filter | MMM-TRAIN-002 | GBPUSD | 50 | 28.0% | 20.0% | -1.8 | 12.9 | 9.1 |
| needs_stricter_filter | MMM-TRAIN-002 | USDJPY | 50 | 28.0% | 10.0% | 3.0 | 15.2 | 9.7 |
| needs_stricter_filter | MMM-TRAIN-002 | AUDUSD | 50 | 26.0% | 8.0% | -0.6 | 6.7 | 6.3 |
| needs_stricter_filter | MMM-TRAIN-002 | EURJPY | 50 | 18.0% | 8.0% | -2.0 | 13.5 | 13.9 |
| needs_stricter_filter | MMM-TRAIN-002 | GBPCHF | 50 | 12.0% | 4.0% | -4.3 | 6.9 | 6.7 |
| needs_stricter_filter | MMM-TRAIN-003 | AUDUSD | 41 | 26.8% | 31.7% | -2.7 | 7.3 | 6.4 |
| needs_stricter_filter | MMM-TRAIN-003 | EURUSD | 39 | 23.1% | 28.2% | -4.8 | 7.3 | 5.5 |
| needs_stricter_filter | MMM-TRAIN-003 | GBPJPY | 50 | 20.0% | 30.0% | -7.9 | 16.8 | 15.6 |
| needs_stricter_filter | MMM-TRAIN-003 | EURJPY | 50 | 18.0% | 28.0% | -3.9 | 11.8 | 12.1 |
| needs_stricter_filter | MMM-TRAIN-003 | USDJPY | 40 | 17.5% | 27.5% | -3.0 | 12.0 | 9.9 |
| needs_stricter_filter | MMM-TRAIN-003 | GBPCHF | 50 | 14.0% | 28.0% | -7.4 | 6.9 | 7.1 |
| needs_stricter_filter | MMM-TRAIN-003 | GBPUSD | 44 | 13.6% | 25.0% | -5.9 | 9.8 | 7.8 |
| watch | MMM-TRAIN-004 | GBPJPY | 12 | 50.0% | 50.0% | 16.1 | 36.2 | 16.2 |
| watch | MMM-TRAIN-004 | AUDUSD | 8 | 50.0% | 75.0% | 2.9 | 14.1 | 7.4 |
| watch | MMM-TRAIN-004 | USDJPY | 6 | 50.0% | 66.7% | 14.5 | 28.3 | 11.7 |
| watch_low_sample | MMM-TRAIN-004 | EURJPY | 8 | 37.5% | 50.0% | 11.8 | 25.5 | 10.7 |
| needs_stricter_filter | MMM-TRAIN-004 | EURUSD | 5 | 20.0% | 20.0% | -2.9 | 15.9 | 16.6 |
| needs_stricter_filter | MMM-TRAIN-004 | GBPUSD | 5 | 20.0% | 60.0% | 2.3 | 15.8 | 6.0 |
| needs_stricter_filter | MMM-TRAIN-004 | GBPCHF | 1 | 0.0% | 0.0% | -29.6 | 0.4 | 41.7 |
| needs_stricter_filter | MMM-TRAIN-006 | GBPJPY | 17 | 35.3% | 29.4% | 8.1 | 26.9 | 13.0 |
| needs_stricter_filter | MMM-TRAIN-006 | AUDUSD | 20 | 25.0% | 35.0% | -2.9 | 9.1 | 6.3 |
| needs_stricter_filter | MMM-TRAIN-006 | USDJPY | 14 | 21.4% | 28.6% | -5.5 | 13.4 | 16.6 |
| needs_stricter_filter | MMM-TRAIN-006 | EURJPY | 25 | 20.0% | 28.0% | -4.8 | 9.5 | 10.8 |
| needs_stricter_filter | MMM-TRAIN-006 | GBPUSD | 15 | 20.0% | 40.0% | -0.6 | 19.2 | 11.1 |
| needs_stricter_filter | MMM-TRAIN-006 | EURUSD | 17 | 17.6% | 23.5% | -4.0 | 7.6 | 8.7 |
| needs_stricter_filter | MMM-TRAIN-006 | GBPCHF | 15 | 13.3% | 20.0% | -1.5 | 6.2 | 7.2 |

## Interpretation

- `MMM-TRAIN-004` is the only practical watchlist family in this pass, especially GBPJPY, AUDUSD, and USDJPY; sample size remains low.
- `MMM-TRAIN-002` is weakly positive only on GBPJPY and should be pair-specific if refined.
- `MMM-TRAIN-003` and `MMM-TRAIN-006` underperform in this naive detector form and should not be used as entry gates.
- `MMM-TRAIN-001`, `MMM-TRAIN-005`, `MMM-TRAIN-007`, and `MMM-TRAIN-008` still need dedicated validators because they are context, day-map, exit, or preparation rules rather than direct entries.

## Next Calibration Work

- Tighten `MMM-TRAIN-004` with pair-specific Asian range, session, return-inside, and M/W confirmation filters.
- Build a pivot/day-map validator for `MMM-TRAIN-005` before evaluating M3-to-M1 target logic.
- Compare each refined taught-rule detector against the scanner baseline and only then promote to the validation library.
