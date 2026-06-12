# GBPJPY Vision Filter Ablation

Generated: 2026-06-12T01:33:26.335099+00:00
Sample total: 10

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_RUNNER | 100.0% | 90.0% | 90.0% | 50.0% | +18.4 | 69.22 | 7.69 | +25.7 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 4 | R_RUNNER | 40.0% | 100.0% | 100.0% | 75.0% | +24.8 | 999.00 | 999.00 | +33.0 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 6 | R_RUNNER | 60.0% | 100.0% | 100.0% | 66.7% | +25.5 | 999.00 | 999.00 | +34.3 | +5.1 |
| `stop_hunt_le_90` | 10 | R_RUNNER | 100.0% | 90.0% | 90.0% | 50.0% | +18.4 | 69.22 | 7.69 | +25.7 | +7.2 |
| `asian_range_gte_30` | 4 | R_RUNNER | 40.0% | 100.0% | 100.0% | 75.0% | +24.8 | 999.00 | 999.00 | +33.0 | +3.4 |
| `confluence_gte_60` | 10 | R_RUNNER | 100.0% | 90.0% | 90.0% | 50.0% | +18.4 | 69.22 | 7.69 | +25.7 | +7.2 |
| `confluence_gte_70` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +21.9 | 999.00 | 999.00 | +33.1 | +1.3 |
| `tdi_rsi_gt_signal` | 9 | R_RUNNER | 90.0% | 88.9% | 88.9% | 44.4% | +16.8 | 57.09 | 7.14 | +24.2 | +7.3 |
| `tdi_rsi_gte_50` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +21.9 | 999.00 | 999.00 | +33.1 | +1.3 |
| `ratio_le_2_and_asian_gte_30` | 4 | R_RUNNER | 40.0% | 100.0% | 100.0% | 75.0% | +24.8 | 999.00 | 999.00 | +33.0 | +3.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_RUNNER | 40.0% | 100.0% | 100.0% | 75.0% | +24.8 | 999.00 | 999.00 | +33.0 | +3.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 4 | R_RUNNER | 40.0% | 100.0% | 100.0% | 75.0% | +24.8 | 999.00 | 999.00 | +33.0 | +3.4 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_RUNNER | 100.0% | 90.0% | 90.0% | 50.0% | +18.4 | 69.22 | 7.69 | +25.7 | +7.2 |
| `feature_momentum_breakout_exception` | 10 | R_RUNNER | 100.0% | 90.0% | 90.0% | 50.0% | +18.4 | 69.22 | 7.69 | +25.7 | +7.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +21.9 | 999.00 | 999.00 | +33.1 | +1.3 |
| `feature_tdi_quality_gte_1` | 5 | R_RUNNER | 50.0% | 100.0% | 100.0% | 60.0% | +25.6 | 999.00 | 999.00 | +33.2 | +5.0 |
| `feature_post_hunt_reclaim` | 4 | R_RUNNER | 40.0% | 100.0% | 100.0% | 75.0% | +24.8 | 999.00 | 999.00 | +33.0 | +3.4 |
| `feature_higher_low_w_confirmation` | 3 | R_RUNNER | 30.0% | 100.0% | 100.0% | 66.7% | +21.4 | 999.00 | 999.00 | +31.7 | +3.5 |
| `feature_shark_fin_cluster_wait` | 9 | R_RUNNER | 90.0% | 100.0% | 100.0% | 55.6% | +20.8 | 999.00 | 999.00 | +28.1 | +6.5 |
| `feature_confirmation_timing_or_quality` | 9 | R_RUNNER | 90.0% | 100.0% | 100.0% | 55.6% | +20.8 | 999.00 | 999.00 | +28.1 | +6.5 |
| `mgmt_first_2_bar_mae_le_10` | 7 | R_RUNNER | 70.0% | 85.7% | 85.7% | 71.4% | +21.3 | 56.26 | 9.38 | +29.4 | +5.1 |
| `mgmt_reclaim_ar_mid_within_3` | 4 | R_RUNNER | 40.0% | 100.0% | 100.0% | 75.0% | +24.8 | 999.00 | 999.00 | +33.0 | +3.4 |
| `mgmt_first_3_mfe_ge_first_2_mae` | 5 | R_RUNNER | 50.0% | 100.0% | 100.0% | 80.0% | +23.8 | 999.00 | 999.00 | +32.5 | +3.2 |

These are hypothesis ablations only; no row promotes a live rule by itself.
