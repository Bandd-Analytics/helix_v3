# Track 3a — FX non-MMM signal audit

Timeframe H4 | 25 cells, 22 testable (N>=30) | BH q=0.1 | bracket 1.0xATR 1:1 | horizon 12 bars | in-sample < 2025-01-01

**VALIDATED: 0**

| signal | sym | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| xs_mom_60 | POOLED | 2014 | 51 | 46 | 0.000 | 0.999 | -0.07 | 1284 | -0.14 | DEAD |
| zscore_revert_2 | NZDUSD | 215 | 56 | 46 | 0.002 | 0.314 | +0.03 | 128 | -0.18 | DEAD |
| zscore_revert_2 | GBPUSD | 217 | 55 | 45 | 0.002 | 0.420 | +0.01 | 141 | -0.04 | DEAD |
| zscore_revert_2 | EURUSD | 210 | 50 | 42 | 0.011 | 0.828 | -0.06 | 141 | -0.07 | DEAD |
| zscore_revert_2 | AUDUSD | 217 | 50 | 42 | 0.014 | 0.896 | -0.09 | 134 | +0.02 | DEAD |
| carry_regime_h20 | POOLED | 200 | 54 | 46 | 0.020 | 0.365 | +0.07 | 79 | -0.45 | DEAD |
| ma_cross_20_50 | NZDUSD | 68 | 56 | 46 | 0.057 | 0.442 | +0.02 | 56 | -0.08 | DEAD |
| donchian20 | EURUSD | 243 | 47 | 42 | 0.066 | 0.979 | -0.13 | 148 | -0.13 | DEAD |
| donchian20 | AUDUSD | 260 | 46 | 42 | 0.129 | 0.998 | -0.18 | 149 | -0.11 | DEAD |
| carry_h20 | POOLED | 336 | 53 | 50 | 0.207 | 0.213 | +0.13 | 126 | -0.17 | DEAD |
| donchian20 | NZDUSD | 262 | 47 | 46 | 0.305 | 0.990 | -0.14 | 156 | -0.13 | DEAD |
| zscore_revert_2 | USDCHF | 215 | 49 | 48 | 0.472 | 0.958 | -0.12 | 133 | -0.16 | DEAD |
| donchian20 | USDJPY | 272 | 49 | 49 | 0.490 | 0.967 | -0.11 | 152 | -0.04 | DEAD |
| ma_cross_20_50 | AUDUSD | 76 | 42 | 42 | 0.544 | 0.982 | -0.24 | 56 | +0.11 | DEAD |
| ma_cross_20_50 | GBPUSD | 71 | 45 | 45 | 0.552 | 0.953 | -0.20 | 63 | -0.16 | DEAD |
| ma_cross_20_50 | EURUSD | 80 | 39 | 42 | 0.777 | 0.998 | -0.32 | 53 | +0.13 | DEAD |
| ma_cross_20_50 | USDJPY | 73 | 45 | 49 | 0.778 | 0.936 | -0.18 | 55 | -0.19 | DEAD |
| donchian20 | USDCHF | 252 | 45 | 48 | 0.882 | 0.999 | -0.19 | 148 | -0.09 | DEAD |
| zscore_revert_2 | USDJPY | 232 | 45 | 49 | 0.886 | 0.997 | -0.18 | 129 | -0.17 | DEAD |
| donchian20 | GBPUSD | 262 | 41 | 45 | 0.911 | 1.000 | -0.26 | 149 | -0.04 | DEAD |
| ccy_strength_20 | POOLED | 1252 | 45 | 48 | 0.948 | 1.000 | -0.18 | 881 | -0.12 | DEAD |
| ma_cross_20_50 | USDCHF | 81 | 37 | 48 | 0.985 | 0.999 | -0.34 | 58 | -0.27 | DEAD |