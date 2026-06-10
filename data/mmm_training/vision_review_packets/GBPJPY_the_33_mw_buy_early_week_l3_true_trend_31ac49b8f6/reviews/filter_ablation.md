# GBPJPY Vision Filter Ablation

Generated: 2026-06-09T15:36:08.564120+00:00
Sample total: 22

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | R_REPEATER | 100.0% | 63.6% | 63.6% | 9.1% | +7.6 | 2.25 | 1.29 | +26.1 | +18.9 |
| `hunt_to_ar_ratio_le_2_0` | 15 | R_REPEATER | 68.2% | 73.3% | 73.3% | 6.7% | +14.2 | 4.94 | 1.80 | +29.3 | +15.8 |
| `hunt_to_ar_ratio_le_2_5` | 18 | R_REPEATER | 81.8% | 66.7% | 66.7% | 5.6% | +9.6 | 2.76 | 1.38 | +27.4 | +17.7 |
| `stop_hunt_le_90` | 16 | R_RUNNER | 72.7% | 75.0% | 75.0% | 6.2% | +13.5 | 5.00 | 1.67 | +30.2 | +15.0 |
| `asian_range_gte_30` | 18 | R_REPEATER | 81.8% | 61.1% | 61.1% | 5.6% | +8.1 | 2.20 | 1.40 | +25.0 | +19.1 |
| `confluence_gte_60` | 22 | R_REPEATER | 100.0% | 63.6% | 63.6% | 9.1% | +7.6 | 2.25 | 1.29 | +26.1 | +18.9 |
| `confluence_gte_70` | 22 | R_REPEATER | 100.0% | 63.6% | 63.6% | 9.1% | +7.6 | 2.25 | 1.29 | +26.1 | +18.9 |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 4.5% | 100.0% | 100.0% | 100.0% | +42.5 | 999.00 | 999.00 | +60.2 | +1.2 |
| `tdi_rsi_gte_50` | 19 | R_REPEATER | 86.4% | 68.4% | 68.4% | 5.3% | +10.2 | 3.21 | 1.48 | +28.1 | +18.0 |
| `ratio_le_2_and_asian_gte_30` | 15 | R_REPEATER | 68.2% | 73.3% | 73.3% | 6.7% | +14.2 | 4.94 | 1.80 | +29.3 | +15.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 4.5% | 100.0% | 100.0% | 100.0% | +42.5 | 999.00 | 999.00 | +60.2 | +1.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | R_RUNNER | 81.8% | 77.8% | 77.8% | 11.1% | +13.7 | 5.56 | 1.59 | +30.8 | +15.5 |
| `feature_stale_hod_exhaustion_reject` | 18 | R_REPEATER | 81.8% | 61.1% | 61.1% | 11.1% | +8.2 | 2.22 | 1.42 | +26.5 | +18.8 |
| `feature_momentum_breakout_exception` | 9 | R_REPEATER | 40.9% | 55.6% | 55.6% | 11.1% | +2.5 | 1.30 | 1.04 | +19.8 | +21.8 |
| `feature_eurjpy_tdi50_reclaim` | 12 | R_REPEATER | 54.5% | 66.7% | 66.7% | 0.0% | +7.8 | 2.44 | 1.22 | +24.6 | +19.5 |

These are hypothesis ablations only; no row promotes a live rule by itself.
