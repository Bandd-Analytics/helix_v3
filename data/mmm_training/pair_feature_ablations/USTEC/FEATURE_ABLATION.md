# USTEC Pair Feature Ablation

Generated: 2026-06-09T15:36:29.773947+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `RRT_REVERSAL|BUY|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 30.8% | +1168.1 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 33.3% | +1265.4 | 2.15 | 4.29 | 0 | 1 | watch_research |

## Candidate Details

### RRT_REVERSAL|BUY|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|BUY|EARLY_WEEK|L3|RETURN_ACCUM|AR_VALID|HUNT_EXTENDED|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=12 Fav=33.3% Avg=+1265.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +1168.1 | 2.15 | 4.29 | +3274.6 | +2475.4 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +1168.1 | 2.15 | 4.29 | +3274.6 | +2475.4 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +1168.1 | 2.15 | 4.29 | +3274.6 | +2475.4 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +1168.1 | 2.15 | 4.29 | +3274.6 | +2475.4 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 46.2% | 16.7% | 16.7% | 16.7% | -33.3 | 0.98 | 4.91 | +2585.0 | +2493.3 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 33.3% | +1265.4 | 2.15 | 4.29 | +3156.7 | +2534.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +1168.1 | 2.15 | 4.29 | +3274.6 | +2475.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
