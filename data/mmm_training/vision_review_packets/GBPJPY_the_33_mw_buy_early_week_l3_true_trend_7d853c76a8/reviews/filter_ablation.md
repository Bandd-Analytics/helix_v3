# GBPJPY Vision Filter Ablation

Generated: 2026-06-09T15:36:08.571152+00:00
Sample total: 16

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | R_REPEATER | 100.0% | 62.5% | 62.5% | 25.0% | +15.0 | 4.06 | 2.43 | +27.1 | +12.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_RUNNER | 62.5% | 80.0% | 80.0% | 30.0% | +27.5 | 17.98 | 4.49 | +37.1 | +9.4 |
| `hunt_to_ar_ratio_le_2_5` | 11 | R_RUNNER | 68.8% | 81.8% | 81.8% | 36.4% | +26.7 | 19.13 | 4.25 | +37.2 | +8.6 |
| `stop_hunt_le_90` | 12 | R_RUNNER | 75.0% | 83.3% | 83.3% | 33.3% | +25.1 | 19.60 | 3.92 | +35.4 | +9.4 |
| `asian_range_gte_30` | 11 | R_REPEATER | 68.8% | 72.7% | 72.7% | 27.3% | +23.7 | 9.43 | 3.53 | +33.8 | +10.3 |
| `confluence_gte_60` | 16 | R_REPEATER | 100.0% | 62.5% | 62.5% | 25.0% | +15.0 | 4.06 | 2.43 | +27.1 | +12.0 |
| `confluence_gte_70` | 10 | R_REPEATER | 62.5% | 60.0% | 60.0% | 10.0% | +8.5 | 2.37 | 1.58 | +21.7 | +12.6 |
| `tdi_rsi_gt_signal` | 6 | R_RUNNER | 37.5% | 100.0% | 100.0% | 33.3% | +26.8 | 999.00 | 999.00 | +37.9 | +7.6 |
| `tdi_rsi_gte_50` | 9 | R_RUNNER | 56.2% | 77.8% | 77.8% | 33.3% | +19.6 | 5.52 | 1.58 | +31.6 | +11.7 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_RUNNER | 62.5% | 80.0% | 80.0% | 30.0% | +27.5 | 17.98 | 4.49 | +37.1 | +9.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_RUNNER | 25.0% | 100.0% | 100.0% | 25.0% | +33.6 | 999.00 | 999.00 | +43.5 | +6.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | R_RUNNER | 68.8% | 81.8% | 81.8% | 27.3% | +25.7 | 18.45 | 4.10 | +35.1 | +10.2 |
| `feature_stale_hod_exhaustion_reject` | 16 | R_REPEATER | 100.0% | 62.5% | 62.5% | 25.0% | +15.0 | 4.06 | 2.43 | +27.1 | +12.0 |
| `feature_momentum_breakout_exception` | 8 | R_REPEATER | 50.0% | 50.0% | 50.0% | 25.0% | +11.8 | 3.57 | 3.57 | +23.7 | +11.6 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_RUNNER | 37.5% | 83.3% | 83.3% | 33.3% | +22.1 | 12.05 | 2.41 | +34.0 | +8.3 |

These are hypothesis ablations only; no row promotes a live rule by itself.
