# Edge Discovery — Phase 1 Signature Audit

Resolved outcomes: 53569  |  BH q=0.1  |  min cell N=30  |  in-sample < 2025-01-01  |  holdout embargo 7d

**TOTAL VALIDATED across all grids: 0**

A cell is VALIDATED only if it is BH-significant AND positive net-R in-sample AND replicates (beats base + positive net-R) on the embargoed holdout with N>=15.

## S0_direction|per_pair — 30 cells, 18 testable (N>=30), 0 hit-rate-sig, 0 expectancy-sig, 0 VALIDATED

## S0_direction|pooled — 2 cells, 2 testable (N>=30), 0 hit-rate-sig, 0 expectancy-sig, 0 VALIDATED

## S1_family_tdi|per_pair — 253 cells, 88 testable (N>=30), 2 hit-rate-sig, 0 expectancy-sig, 0 VALIDATED

| key | sym | dir | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| THE_33_MW|BUY|TDI_CONFLICT | GBPCHF | BUY | 652 | 27 | 21 | 0.0001 | 1.0000 | -0.32 | 637 | -0.31 | DEAD |
| THE_33_MW|BUY|TDI_CONFLICT | GBPUSD | BUY | 559 | 25 | 19 | 0.0003 | 1.0000 | -0.36 | 429 | -0.35 | DEAD |

## S1_family_tdi|pooled — 40 cells, 34 testable (N>=30), 3 hit-rate-sig, 0 expectancy-sig, 0 VALIDATED

| key | sym | dir | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| THE_33_MW|BUY|TDI_CONFLICT | POOLED | BUY | 2014 | 27 | 22 | 0.0000 | 1.0000 | -0.31 | 1863 | -0.36 | DEAD |
| THE_33_MW|BUY|TDI_NONE | POOLED | BUY | 2391 | 25 | 22 | 0.0016 | 1.0000 | -0.49 | 2318 | -0.51 | DEAD |
| RRT_REVERSAL|BUY|TDI_CONFIRM | POOLED | BUY | 83 | 35 | 22 | 0.0064 | 0.9163 | -0.14 | 54 | -0.15 | DEAD |

## S2_family_mw_tdi|per_pair — 253 cells, 88 testable (N>=30), 2 hit-rate-sig, 0 expectancy-sig, 0 VALIDATED

| key | sym | dir | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| THE_33_MW|BUY|W_BOTTOM|TDI_CONFLICT | GBPCHF | BUY | 652 | 27 | 21 | 0.0001 | 1.0000 | -0.32 | 637 | -0.31 | DEAD |
| THE_33_MW|BUY|W_BOTTOM|TDI_CONFLICT | GBPUSD | BUY | 559 | 25 | 19 | 0.0003 | 1.0000 | -0.36 | 429 | -0.35 | DEAD |

## S2_family_mw_tdi|pooled — 40 cells, 34 testable (N>=30), 3 hit-rate-sig, 0 expectancy-sig, 0 VALIDATED

| key | sym | dir | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| THE_33_MW|BUY|W_BOTTOM|TDI_CONFLICT | POOLED | BUY | 2014 | 27 | 22 | 0.0000 | 1.0000 | -0.31 | 1863 | -0.36 | DEAD |
| THE_33_MW|BUY|W_BOTTOM|TDI_NONE | POOLED | BUY | 2391 | 25 | 22 | 0.0016 | 1.0000 | -0.49 | 2318 | -0.51 | DEAD |
| RRT_REVERSAL|BUY|NO_MW|TDI_CONFIRM | POOLED | BUY | 83 | 35 | 22 | 0.0064 | 0.9163 | -0.14 | 54 | -0.15 | DEAD |

## S3_family_hunt_tdi|per_pair — 460 cells, 114 testable (N>=30), 2 hit-rate-sig, 0 expectancy-sig, 0 VALIDATED

| key | sym | dir | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| THE_33_MW|BUY|HUNT_PAIR_RANGE|TDI_CONFLICT | GBPCHF | BUY | 469 | 28 | 21 | 0.0002 | 1.0000 | -0.27 | 391 | -0.34 | DEAD |
| THE_33_MW|BUY|HUNT_EXTENDED|TDI_CONFLICT | GBPUSD | BUY | 60 | 38 | 19 | 0.0003 | 0.6757 | -0.07 | 22 | -0.37 | DEAD |

## S3_family_hunt_tdi|pooled — 94 cells, 49 testable (N>=30), 4 hit-rate-sig, 0 expectancy-sig, 0 VALIDATED

| key | sym | dir | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| THE_33_MW|BUY|HUNT_PAIR_RANGE|TDI_CONFLICT | POOLED | BUY | 1758 | 27 | 22 | 0.0000 | 1.0000 | -0.30 | 1633 | -0.35 | DEAD |
| THE_33_MW|BUY|HUNT_EXTENDED|TDI_CONFLICT | POOLED | BUY | 307 | 32 | 22 | 0.0001 | 1.0000 | -0.24 | 257 | -0.29 | DEAD |
| RRT_REVERSAL|BUY|HUNT_EXTENDED|TDI_NONE | POOLED | BUY | 34 | 47 | 22 | 0.0013 | 0.1140 | +0.28 | 0 | +0.00 | DEAD |
| THE_33_MW|BUY|HUNT_EXTENDED|TDI_NONE | POOLED | BUY | 353 | 29 | 22 | 0.0041 | 1.0000 | -0.39 | 333 | -0.77 | DEAD |

## S4_family_session_tdi|per_pair — 692 cells, 162 testable (N>=30), 2 hit-rate-sig, 0 expectancy-sig, 0 VALIDATED

| key | sym | dir | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| THE_33_MW|BUY|ACCUMULATION|TDI_CONFLICT | GBPCHF | BUY | 217 | 33 | 21 | 0.0000 | 1.0000 | -0.29 | 153 | -0.21 | DEAD |
| RRT_REVERSAL|SELL|RETURN_ACCUM|TDI_CONFLICT | XAUUSD | SELL | 68 | 46 | 26 | 0.0005 | 0.0285 | +0.20 | 0 | +0.00 | DEAD |

## S4_family_session_tdi|pooled — 167 cells, 66 testable (N>=30), 8 hit-rate-sig, 0 expectancy-sig, 0 VALIDATED

| key | sym | dir | n | fav% | base% | p_hit | p_exp | netR | hold_n | hold_netR | verdict |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| THE_33_MW|BUY|ACCUMULATION|TDI_CONFLICT | POOLED | BUY | 865 | 30 | 22 | 0.0000 | 1.0000 | -0.31 | 538 | -0.32 | DEAD |
| THE_33_MW|BUY|ACCUMULATION|TDI_NONE | POOLED | BUY | 1056 | 27 | 22 | 0.0006 | 1.0000 | -0.50 | 690 | -0.41 | DEAD |
| RRT_REVERSAL|SELL|RETURN_ACCUM|TDI_CONFLICT | POOLED | SELL | 72 | 44 | 26 | 0.0007 | 0.0398 | +0.18 | 0 | +0.00 | DEAD |
| SECOND_LEG_MW|BUY|ACCUMULATION|TDI_CONFIRM | POOLED | BUY | 65 | 40 | 22 | 0.0011 | 0.9318 | -0.19 | 50 | -0.28 | DEAD |
| THE_33_MW|BUY|ACCUMULATION|TDI_SQUEEZE | POOLED | BUY | 647 | 28 | 22 | 0.0015 | 1.0000 | -0.34 | 320 | -0.55 | DEAD |
| RRT_REVERSAL|BUY|RETURN_ACCUM|TDI_CONFIRM | POOLED | BUY | 35 | 46 | 22 | 0.0020 | 0.2341 | +0.10 | 1 | -0.25 | DEAD |
| THE_33_MW|BUY|NYC_REVERSAL|TDI_CONFLICT | POOLED | BUY | 359 | 29 | 22 | 0.0024 | 1.0000 | -0.22 | 77 | -0.18 | DEAD |
| THE_33_MW|BUY|NYC_REVERSAL|TDI_NONE | POOLED | BUY | 491 | 27 | 22 | 0.0090 | 1.0000 | -0.38 | 444 | -0.69 | DEAD |
