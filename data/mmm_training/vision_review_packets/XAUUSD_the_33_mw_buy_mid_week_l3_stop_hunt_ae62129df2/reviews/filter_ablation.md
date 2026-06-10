# XAUUSD Vision Filter Ablation

Generated: 2026-06-09T15:36:08.599186+00:00
Sample total: 11

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `hunt_to_ar_ratio_le_2_0` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `hunt_to_ar_ratio_le_2_5` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `confluence_gte_60` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `confluence_gte_70` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 72.7% | 62.5% | 62.5% | 62.5% | +526.1 | 5.26 | 2.10 | +1566.1 | +357.7 |
| `tdi_rsi_gte_50` | 9 | R_REPEATER | 81.8% | 55.6% | 55.6% | 66.7% | +330.7 | 2.62 | 1.57 | +1343.1 | +420.0 |
| `ratio_le_2_and_asian_gte_30` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 72.7% | 62.5% | 62.5% | 62.5% | +526.1 | 5.26 | 2.10 | +1566.1 | +357.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `feature_momentum_breakout_exception` | 9 | R_REPEATER | 81.8% | 66.7% | 66.7% | 66.7% | +394.6 | 2.49 | 0.83 | +1407.4 | +185.7 |
| `feature_eurjpy_tdi50_reclaim` | 9 | R_REPEATER | 81.8% | 55.6% | 55.6% | 66.7% | +330.7 | 2.62 | 1.57 | +1343.1 | +420.0 |

These are hypothesis ablations only; no row promotes a live rule by itself.
