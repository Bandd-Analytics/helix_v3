# XAUUSD Vision Filter Ablation

Generated: 2026-06-09T15:36:08.591188+00:00
Sample total: 17

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | R_REPEATER | 100.0% | 70.6% | 70.6% | 52.9% | +358.7 | 6.06 | 2.02 | +640.5 | +182.0 |
| `hunt_to_ar_ratio_le_2_0` | 14 | R_REPEATER | 82.4% | 71.4% | 71.4% | 50.0% | +327.9 | 4.81 | 1.93 | +647.1 | +192.4 |
| `hunt_to_ar_ratio_le_2_5` | 17 | R_REPEATER | 100.0% | 70.6% | 70.6% | 52.9% | +358.7 | 6.06 | 2.02 | +640.5 | +182.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | R_REPEATER | 100.0% | 70.6% | 70.6% | 52.9% | +358.7 | 6.06 | 2.02 | +640.5 | +182.0 |
| `confluence_gte_60` | 13 | R_RUNNER | 76.5% | 76.9% | 76.9% | 53.8% | +270.9 | 5.32 | 1.60 | +548.2 | +179.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 14 | R_RUNNER | 82.4% | 78.6% | 78.6% | 64.3% | +369.8 | 7.45 | 1.35 | +659.5 | +157.7 |
| `tdi_rsi_gte_50` | 3 | R_REPEATER | 17.6% | 66.7% | 66.7% | 100.0% | +101.2 | 999.00 | 999.00 | +265.3 | +106.3 |
| `ratio_le_2_and_asian_gte_30` | 14 | R_REPEATER | 82.4% | 71.4% | 71.4% | 50.0% | +327.9 | 4.81 | 1.93 | +647.1 | +192.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | R_RUNNER | 70.6% | 83.3% | 83.3% | 58.3% | +416.0 | 7.22 | 1.44 | +732.1 | +162.9 |
| `feature_fresh_reclaim_within_8` | 3 | S_STRANGER | 17.6% | 33.3% | 33.3% | 66.7% | -27.8 | 0.76 | 0.76 | +186.7 | +216.7 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | R_REPEATER | 100.0% | 70.6% | 70.6% | 52.9% | +358.7 | 6.06 | 2.02 | +640.5 | +182.0 |
| `feature_momentum_breakout_exception` | 17 | R_REPEATER | 100.0% | 70.6% | 70.6% | 52.9% | +358.7 | 6.06 | 2.02 | +640.5 | +182.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_REPEATER | 17.6% | 66.7% | 66.7% | 100.0% | +101.2 | 999.00 | 999.00 | +265.3 | +106.3 |

These are hypothesis ablations only; no row promotes a live rule by itself.
