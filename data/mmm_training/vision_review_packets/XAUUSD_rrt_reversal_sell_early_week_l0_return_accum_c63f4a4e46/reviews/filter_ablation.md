# XAUUSD Vision Filter Ablation

Generated: 2026-06-09T15:36:08.585110+00:00
Sample total: 15

Setup: `RRT_REVERSAL|SELL|EARLY_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | R_REPEATER | 100.0% | 53.3% | 53.3% | 26.7% | +224.9 | 6.36 | 5.57 | +461.7 | +127.9 |
| `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 80.0% | 58.3% | 58.3% | 33.3% | +260.3 | 6.73 | 4.81 | +502.1 | +142.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 80.0% | 58.3% | 58.3% | 33.3% | +260.3 | 6.73 | 4.81 | +502.1 | +142.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | R_REPEATER | 100.0% | 53.3% | 53.3% | 26.7% | +224.9 | 6.36 | 5.57 | +461.7 | +127.9 |
| `confluence_gte_60` | 9 | S_STRANGER | 60.0% | 44.4% | 44.4% | 11.1% | +208.4 | 8.33 | 10.41 | +400.7 | +120.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 80.0% | 41.7% | 41.7% | 25.0% | +104.4 | 2.99 | 4.19 | +317.2 | +135.0 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -72.0 | 0.41 | 0.82 | +137.3 | +132.7 |
| `ratio_le_2_and_asian_gte_30` | 12 | R_REPEATER | 80.0% | 58.3% | 58.3% | 33.3% | +260.3 | 6.73 | 4.81 | +502.1 | +142.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | R_REPEATER | 66.7% | 50.0% | 50.0% | 30.0% | +133.7 | 3.45 | 3.45 | +357.7 | +145.3 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -358.0 | 0.00 | 0.00 | +0.0 | +191.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | R_REPEATER | 100.0% | 53.3% | 53.3% | 26.7% | +224.9 | 6.36 | 5.57 | +461.7 | +127.9 |
| `feature_momentum_breakout_exception` | 14 | R_REPEATER | 93.3% | 57.1% | 57.1% | 28.6% | +266.5 | 14.77 | 11.08 | +494.6 | +123.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -72.0 | 0.41 | 0.82 | +137.3 | +132.7 |

These are hypothesis ablations only; no row promotes a live rule by itself.
