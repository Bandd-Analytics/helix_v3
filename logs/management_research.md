# Track 3b — management-as-alpha audit (entry held fixed, exit varied)

Timeframe H4 | 14 cells, 14 testable (N>=30) | BH q=0.1 | bracket 1.0xATR 1:1 | horizon 12 bars | in-sample < 2025-01-01

**VALIDATED: 0**

| signal | sym | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| random/tp_0p5R | POOLED | 7101 | 65 | 49 | 0.000 | 1.000 | -0.13 | 5201 | -0.11 | DEAD |
| zfade/tp_0p5R | POOLED | 1381 | 65 | 52 | 0.000 | 1.000 | -0.12 | 1014 | -0.12 | DEAD |
| zfade/scaleout | POOLED | 1245 | 52 | 52 | 0.476 | 0.975 | -0.06 | 907 | -0.10 | DEAD |
| random/sym_1_1 | POOLED | 4993 | 49 | 49 | 0.506 | 1.000 | -0.12 | 3628 | -0.09 | DEAD |
| zfade/sym_1_1 | POOLED | 1304 | 52 | 52 | 0.511 | 0.992 | -0.07 | 953 | -0.10 | DEAD |
| zfade/time_stop | POOLED | 827 | 51 | 52 | 0.642 | 0.035 | +0.16 | 587 | +0.03 | DEAD |
| random/time_stop | POOLED | 1722 | 48 | 49 | 0.734 | 0.959 | -0.10 | 1217 | -0.15 | DEAD |
| random/scaleout | POOLED | 3874 | 48 | 49 | 0.897 | 1.000 | -0.14 | 2812 | -0.12 | DEAD |
| zfade/trail_1R | POOLED | 1245 | 47 | 52 | 1.000 | 0.562 | -0.01 | 907 | -0.06 | DEAD |
| zfade/tp_2R | POOLED | 1227 | 38 | 52 | 1.000 | 0.893 | -0.05 | 891 | -0.13 | DEAD |
| random/tp_2R | POOLED | 3524 | 35 | 49 | 1.000 | 1.000 | -0.09 | 2477 | -0.12 | DEAD |
| random/trail_1R | POOLED | 3874 | 43 | 49 | 1.000 | 1.000 | -0.10 | 2812 | -0.09 | DEAD |
| random/be_1R | POOLED | 3949 | 27 | 49 | 1.000 | 1.000 | -0.11 | 2835 | -0.13 | DEAD |
| zfade/be_1R | POOLED | 1265 | 29 | 52 | 1.000 | 0.919 | -0.05 | 925 | -0.13 | DEAD |