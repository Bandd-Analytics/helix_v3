# XAUUSD Vision Filter Ablation

Generated: 2026-06-09T15:36:08.608859+00:00
Sample total: 11

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `confluence_gte_60` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `confluence_gte_70` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 0.0% | -25.4 | 0.92 | 1.38 | +908.2 | +617.2 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 16.7% | +352.3 | 2.06 | 2.06 | +1372.3 | +552.0 |
| `ratio_le_2_and_asian_gte_30` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 0.0% | -25.4 | 0.92 | 1.38 | +908.2 | +617.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 90.9% | 50.0% | 50.0% | 10.0% | -192.4 | 0.72 | 0.72 | +1017.5 | +1059.3 |
| `feature_momentum_breakout_exception` | 8 | R_REPEATER | 72.7% | 50.0% | 50.0% | 12.5% | -304.8 | 0.62 | 0.62 | +844.9 | +1213.4 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 16.7% | +352.3 | 2.06 | 2.06 | +1372.3 | +552.0 |

These are hypothesis ablations only; no row promotes a live rule by itself.
