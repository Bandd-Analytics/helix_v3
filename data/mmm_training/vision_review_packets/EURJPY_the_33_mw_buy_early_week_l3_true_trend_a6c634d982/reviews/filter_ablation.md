# EURJPY Vision Filter Ablation

Generated: 2026-06-09T15:36:08.551331+00:00
Sample total: 21

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 14.3% | +10.1 | 5.96 | 5.96 | +19.5 | +8.0 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 66.7% | 42.9% | 42.9% | 14.3% | +8.3 | 5.09 | 5.94 | +16.8 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 18 | R_REPEATER | 85.7% | 50.0% | 50.0% | 11.1% | +10.8 | 7.53 | 6.69 | +19.3 | +8.0 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 81.0% | 47.1% | 47.1% | 11.8% | +9.9 | 6.62 | 6.62 | +18.6 | +8.3 |
| `asian_range_gte_30` | 20 | S_STRANGER | 95.2% | 45.0% | 45.0% | 15.0% | +9.6 | 5.50 | 6.11 | +19.3 | +8.1 |
| `confluence_gte_60` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 14.3% | +10.1 | 5.96 | 5.96 | +19.5 | +8.0 |
| `confluence_gte_70` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 14.3% | +10.1 | 5.96 | 5.96 | +19.5 | +8.0 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 71.4% | 46.7% | 46.7% | 13.3% | +9.9 | 4.92 | 4.92 | +19.1 | +9.8 |
| `tdi_rsi_gte_50` | 15 | R_REPEATER | 71.4% | 53.3% | 53.3% | 0.0% | +11.1 | 5.94 | 5.20 | +20.5 | +8.6 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 61.9% | 38.5% | 38.5% | 15.4% | +7.4 | 4.40 | 6.16 | +16.3 | +8.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 47.6% | 40.0% | 40.0% | 20.0% | +8.2 | 4.25 | 5.31 | +16.2 | +10.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 66.7% | 42.9% | 42.9% | 14.3% | +8.3 | 5.09 | 5.94 | +16.8 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 14.3% | +10.1 | 5.96 | 5.96 | +19.5 | +8.0 |
| `feature_momentum_breakout_exception` | 10 | R_REPEATER | 47.6% | 60.0% | 60.0% | 20.0% | +14.5 | 8.99 | 4.50 | +22.8 | +7.6 |
| `feature_eurjpy_tdi50_reclaim` | 9 | R_REPEATER | 42.9% | 66.7% | 66.7% | 0.0% | +17.2 | 12.90 | 6.45 | +25.2 | +7.4 |

These are hypothesis ablations only; no row promotes a live rule by itself.
