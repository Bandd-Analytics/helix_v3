# XAUUSD Vision Filter Ablation

Generated: 2026-06-09T15:36:08.578154+00:00
Sample total: 11

Setup: `RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +549.0 | 9.66 | 4.14 | +858.3 | +251.8 |
| `hunt_to_ar_ratio_le_2_0` | 6 | R_RUNNER | 54.5% | 83.3% | 83.3% | 33.3% | +623.3 | 34.39 | 6.88 | +856.0 | +280.3 |
| `hunt_to_ar_ratio_le_2_5` | 6 | R_RUNNER | 54.5% | 83.3% | 83.3% | 33.3% | +623.3 | 34.39 | 6.88 | +856.0 | +280.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +549.0 | 9.66 | 4.14 | +858.3 | +251.8 |
| `confluence_gte_60` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +549.0 | 9.66 | 4.14 | +858.3 | +251.8 |
| `confluence_gte_70` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +549.0 | 9.66 | 4.14 | +858.3 | +251.8 |
| `tdi_rsi_gt_signal` | 10 | R_REPEATER | 90.9% | 70.0% | 70.0% | 40.0% | +615.1 | 11.51 | 3.29 | +928.9 | +261.4 |
| `tdi_rsi_gte_50` | 8 | R_RUNNER | 72.7% | 75.0% | 75.0% | 25.0% | +672.6 | 10.09 | 3.36 | +1009.8 | +292.9 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_RUNNER | 54.5% | 83.3% | 83.3% | 33.3% | +623.3 | 34.39 | 6.88 | +856.0 | +280.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_RUNNER | 45.5% | 100.0% | 100.0% | 40.0% | +770.4 | 999.00 | 999.00 | +996.8 | +305.2 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 0.0% | +372.0 | 999.00 | 999.00 | +654.0 | +467.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 90.9% | 60.0% | 60.0% | 30.0% | +338.0 | 5.85 | 2.92 | +640.2 | +259.2 |
| `feature_momentum_breakout_exception` | 10 | R_REPEATER | 90.9% | 60.0% | 60.0% | 40.0% | +566.7 | 9.13 | 4.57 | +878.7 | +230.3 |
| `feature_eurjpy_tdi50_reclaim` | 8 | R_RUNNER | 72.7% | 75.0% | 75.0% | 25.0% | +672.6 | 10.09 | 3.36 | +1009.8 | +292.9 |

These are hypothesis ablations only; no row promotes a live rule by itself.
