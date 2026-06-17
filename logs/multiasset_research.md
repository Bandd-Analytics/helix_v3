# Track 3c — multi-asset time-series momentum audit

Timeframe D1 | 7 cells, 7 testable (N>=30) | BH q=0.1 | TSMOM lookback 120 | holding 20 bars (holding-return) | in-sample < 2025-01-01

**VALIDATED: 1**

| signal | sym | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| tsmom_120 | POOLED | 440 | 57 | 62 | 0.986 | 0.010 | +0.42 | 118 | +0.23 | VALIDATED |
| tsmom_120 | USTEC | 76 | 71 | 71 | 0.557 | 0.011 | +0.88 | 17 | -0.03 | DEAD |
| tsmom_120 | ETHUSD | 68 | 49 | 51 | 0.728 | 0.354 | +0.18 | 25 | -0.28 | DEAD |
| tsmom_120 | BTCUSD | 68 | 53 | 57 | 0.805 | 0.234 | +0.48 | 25 | +0.05 | DEAD |
| tsmom_120 | XAUUSD | 76 | 51 | 58 | 0.899 | 0.098 | +0.51 | 17 | +2.34 | DEAD |
| tsmom_120 | DE40 | 76 | 55 | 62 | 0.902 | 0.553 | -0.04 | 17 | -0.18 | DEAD |
| tsmom_120 | US500 | 76 | 63 | 72 | 0.970 | 0.110 | +0.49 | 17 | -0.20 | DEAD |

## Benchmark-relative test — TSMOM vs BUY-AND-HOLD (the correct null)

diff = tsmom_r − buyhold_r per entry (lookback 120, holding 20, same ATR/cost). Edge requires mean diff > 0 in-sample (BH-significant) AND a positive holdout mean diff.

| sym | n_in | mean_diff_in | p_in | n_hold | mean_diff_hold |
|---|--:|--:|--:|--:|--:|
| US500 | 76 | -0.191 | 0.712 | 17 | -0.928 |
| USTEC | 76 | -0.017 | 0.521 | 17 | -1.045 |
| DE40 | 76 | -0.497 | 0.884 | 17 | -0.693 |
| XAUUSD | 76 | -0.395 | 0.868 | 17 | +0.000 |
| BTCUSD | 68 | -0.353 | 0.629 | 25 | +0.417 |
| ETHUSD | 68 | -0.293 | 0.655 | 25 | -0.024 |
| **POOLED** | 440 | -0.290 | 0.891 | 118 | -0.301 |

**Alpha over buy-and-hold: NO** (pooled mean diff in=-0.290, holdout=-0.301).