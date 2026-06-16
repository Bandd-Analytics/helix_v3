# Track 3a — FX non-MMM signal audit

Timeframe H4 | 24 cells, 21 testable (N>=30) | BH q=0.1 | bracket 1.0xATR 1:1 | horizon 12 bars | in-sample < 2025-01-01

**VALIDATED: 0**

| signal | sym | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| xs_mom_60 | POOLED | 2016 | 51 | 47 | 0.001 | 0.999 | -0.07 | 1282 | -0.14 | DEAD |
| zscore_revert_2 | GBPUSD | 218 | 56 | 47 | 0.005 | 0.397 | +0.02 | 141 | -0.04 | DEAD |
| zscore_revert_2 | NZDUSD | 216 | 56 | 49 | 0.032 | 0.342 | +0.03 | 128 | -0.18 | DEAD |
| ma_cross_20_50 | NZDUSD | 68 | 56 | 49 | 0.156 | 0.442 | +0.02 | 56 | -0.08 | DEAD |
| zscore_revert_2 | AUDUSD | 218 | 50 | 46 | 0.158 | 0.884 | -0.08 | 134 | +0.02 | DEAD |
| donchian20 | USDJPY | 273 | 49 | 46 | 0.181 | 0.972 | -0.12 | 152 | -0.04 | DEAD |
| carry_h20 | POOLED | 336 | 53 | 50 | 0.207 | 0.213 | +0.13 | 126 | -0.17 | DEAD |
| zscore_revert_2 | EURUSD | 211 | 50 | 48 | 0.240 | 0.847 | -0.07 | 141 | -0.07 | DEAD |
| zscore_revert_2 | USDCHF | 216 | 49 | 46 | 0.268 | 0.964 | -0.12 | 133 | -0.17 | DEAD |
| donchian20 | EURUSD | 244 | 48 | 48 | 0.529 | 0.976 | -0.13 | 148 | -0.13 | DEAD |
| ma_cross_20_50 | USDJPY | 73 | 45 | 46 | 0.609 | 0.936 | -0.18 | 55 | -0.19 | DEAD |
| donchian20 | AUDUSD | 261 | 46 | 46 | 0.624 | 0.998 | -0.18 | 149 | -0.11 | DEAD |
| ma_cross_20_50 | GBPUSD | 71 | 45 | 47 | 0.650 | 0.953 | -0.20 | 63 | -0.18 | DEAD |
| zscore_revert_2 | USDJPY | 233 | 45 | 46 | 0.655 | 0.998 | -0.19 | 129 | -0.17 | DEAD |
| donchian20 | USDCHF | 253 | 45 | 46 | 0.674 | 0.999 | -0.19 | 148 | -0.08 | DEAD |
| donchian20 | NZDUSD | 263 | 48 | 49 | 0.708 | 0.988 | -0.14 | 156 | -0.13 | DEAD |
| ma_cross_20_50 | AUDUSD | 77 | 43 | 46 | 0.768 | 0.976 | -0.22 | 56 | +0.11 | DEAD |
| ccy_strength_20 | POOLED | 1253 | 45 | 47 | 0.953 | 1.000 | -0.18 | 880 | -0.12 | DEAD |
| ma_cross_20_50 | EURUSD | 80 | 39 | 48 | 0.955 | 0.998 | -0.32 | 52 | +0.12 | DEAD |
| ma_cross_20_50 | USDCHF | 81 | 37 | 46 | 0.963 | 0.999 | -0.34 | 58 | -0.27 | DEAD |
| donchian20 | GBPUSD | 262 | 41 | 47 | 0.967 | 1.000 | -0.26 | 149 | -0.04 | DEAD |