# GBPJPY Vision Filter Ablation

Generated: 2026-06-09T15:36:08.557601+00:00
Sample total: 20

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | R_RUNNER | 100.0% | 85.0% | 85.0% | 35.0% | +8.8 | 11.74 | 1.38 | +20.2 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 16 | R_RUNNER | 80.0% | 93.8% | 93.8% | 31.2% | +9.0 | 999.00 | 999.00 | +19.8 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 16 | R_RUNNER | 80.0% | 93.8% | 93.8% | 31.2% | +9.0 | 999.00 | 999.00 | +19.8 | +4.8 |
| `stop_hunt_le_90` | 18 | R_RUNNER | 90.0% | 94.4% | 94.4% | 38.9% | +10.7 | 999.00 | 999.00 | +21.2 | +4.7 |
| `asian_range_gte_30` | 16 | R_RUNNER | 80.0% | 93.8% | 93.8% | 31.2% | +9.0 | 999.00 | 999.00 | +19.8 | +4.8 |
| `confluence_gte_60` | 19 | R_RUNNER | 95.0% | 84.2% | 84.2% | 36.8% | +8.8 | 11.19 | 1.40 | +20.1 | +5.3 |
| `confluence_gte_70` | 5 | R_RUNNER | 25.0% | 100.0% | 100.0% | 0.0% | +6.4 | 999.00 | 999.00 | +16.5 | +6.6 |
| `tdi_rsi_gt_signal` | 13 | R_RUNNER | 65.0% | 84.6% | 84.6% | 30.8% | +7.1 | 6.60 | 1.20 | +19.7 | +6.3 |
| `tdi_rsi_gte_50` | 9 | R_RUNNER | 45.0% | 77.8% | 77.8% | 0.0% | +4.7 | 3.57 | 1.02 | +16.0 | +8.1 |
| `ratio_le_2_and_asian_gte_30` | 16 | R_RUNNER | 80.0% | 93.8% | 93.8% | 31.2% | +9.0 | 999.00 | 999.00 | +19.8 | +4.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | R_RUNNER | 55.0% | 100.0% | 100.0% | 36.4% | +9.8 | 999.00 | 999.00 | +21.3 | +5.7 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 5.0% | 100.0% | 100.0% | 0.0% | +9.0 | 999.00 | 999.00 | +20.4 | +4.5 |
| `feature_extreme_hunt_with_exception` | 16 | R_RUNNER | 80.0% | 93.8% | 93.8% | 31.2% | +9.0 | 999.00 | 999.00 | +19.8 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 20 | R_RUNNER | 100.0% | 85.0% | 85.0% | 35.0% | +8.8 | 11.74 | 1.38 | +20.2 | +5.2 |
| `feature_momentum_breakout_exception` | 14 | R_RUNNER | 70.0% | 78.6% | 78.6% | 28.6% | +7.3 | 7.21 | 1.31 | +19.6 | +5.5 |
| `feature_eurjpy_tdi50_reclaim` | 7 | R_REPEATER | 35.0% | 71.4% | 71.4% | 0.0% | +3.5 | 2.51 | 1.00 | +14.9 | +8.7 |

These are hypothesis ablations only; no row promotes a live rule by itself.
