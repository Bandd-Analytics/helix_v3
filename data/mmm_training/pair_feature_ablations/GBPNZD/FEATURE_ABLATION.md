# GBPNZD Pair Feature Ablation

Generated: 2026-06-09T15:36:25.886499+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | R_RUNNER | 81.8% | +30.0 | `all` | 11 | R_RUNNER | 81.8% | +30.0 | 13.28 | 2.95 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 18 | R_REPEATER | 66.7% | +15.2 | `confluence_gte_60` | 13 | R_RUNNER | 76.9% | +20.6 | 55.72 | 4.64 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 18 | R_REPEATER | 66.7% | +10.3 | `tdi_rsi_gte_50` | 9 | R_REPEATER | 66.7% | +15.0 | 5.67 | 2.84 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 17 | R_REPEATER | 64.7% | +17.3 | `tdi_rsi_gte_50` | 10 | R_REPEATER | 70.0% | +27.6 | 4.57 | 1.96 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | R_REPEATER | 63.6% | +18.0 | `all` | 11 | R_REPEATER | 63.6% | +18.0 | 7.09 | 3.04 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 29 | R_REPEATER | 58.6% | +18.8 | `tdi_rsi_gte_50` | 14 | R_REPEATER | 71.4% | +27.7 | 5.12 | 2.05 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 43 | R_REPEATER | 53.5% | +4.4 | `confluence_gte_60` | 30 | R_REPEATER | 63.3% | +9.2 | 2.68 | 1.41 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 23 | R_REPEATER | 52.2% | +7.1 | `hunt_to_ar_ratio_le_2_0` | 17 | R_REPEATER | 58.8% | +11.5 | 2.34 | 1.64 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 20 | R_REPEATER | 50.0% | +13.3 | `tdi_rsi_gt_signal` | 5 | R_REPEATER | 60.0% | +36.0 | 53.88 | 17.96 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | R_REPEATER | 50.0% | +4.8 | `stop_hunt_le_90` | 8 | R_REPEATER | 62.5% | +9.9 | 1.83 | 1.10 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 12 | R_REPEATER | 50.0% | +4.6 | `tdi_rsi_gte_50` | 11 | R_REPEATER | 54.5% | +5.3 | 1.63 | 1.09 | 1 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 14 | R_REPEATER | 50.0% | +4.1 | `stop_hunt_le_90` | 12 | R_REPEATER | 58.3% | +10.1 | 2.80 | 2.00 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 20 | R_REPEATER | 50.0% | +4.0 | `confluence_gte_60` | 10 | R_REPEATER | 50.0% | +6.7 | 1.86 | 1.49 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 25 | S_STRANGER | 48.0% | +9.7 | `tdi_rsi_gt_signal` | 8 | R_REPEATER | 62.5% | +18.6 | 4.80 | 1.92 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 25 | S_STRANGER | 48.0% | +8.1 | `tdi_rsi_gte_50` | 20 | R_REPEATER | 50.0% | +8.7 | 2.13 | 1.92 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 21 | S_STRANGER | 47.6% | +12.1 | `tdi_rsi_gt_signal` | 12 | R_REPEATER | 66.7% | +23.1 | 5.76 | 2.16 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 45.0% | +8.1 | `confluence_gte_70` | 6 | R_REPEATER | 50.0% | +22.0 | 10.87 | 7.24 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 42.9% | +12.7 | `tdi_rsi_gte_50` | 9 | R_REPEATER | 66.7% | +26.3 | 4.40 | 2.20 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 42.9% | -2.0 | `stop_hunt_le_90` | 13 | S_STRANGER | 46.2% | +0.3 | 1.02 | 1.02 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 22 | S_STRANGER | 40.9% | +8.4 | `confluence_gte_70` | 7 | R_REPEATER | 57.1% | +32.2 | 4.83 | 1.93 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 40.0% | +14.2 | `tdi_rsi_gte_50` | 7 | R_REPEATER | 57.1% | +27.7 | 14.11 | 10.59 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 40.0% | +0.7 | `confluence_gte_60` | 6 | R_REPEATER | 66.7% | +19.7 | 1.92 | 0.96 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 33.3% | -5.1 | `tdi_rsi_gte_50` | 14 | S_STRANGER | 42.9% | -4.4 | 0.76 | 0.88 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | -8.1 | `hunt_to_ar_ratio_le_2_0` | 6 | R_REPEATER | 50.0% | +2.8 | 1.20 | 1.20 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 49 | S_STRANGER | 32.7% | -7.4 | `tdi_rsi_gte_50` | 23 | S_STRANGER | 47.8% | -4.5 | 0.74 | 0.74 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 31.6% | -14.4 | `tdi_rsi_gt_signal` | 8 | R_REPEATER | 50.0% | -17.4 | 0.45 | 0.45 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 31.2% | -6.6 | `confluence_gte_60` | 7 | R_REPEATER | 57.1% | +0.2 | 1.02 | 0.41 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | +0.3 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 40.0% | +0.5 | 1.07 | 1.07 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | -6.7 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 33.3% | -6.4 | 0.60 | 0.60 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 30.0% | -18.9 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 44.4% | -19.0 | 0.35 | 0.35 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 14 | S_STRANGER | 28.6% | -17.1 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 42.9% | -10.1 | 0.18 | 0.24 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 28.6% | -26.5 | `stop_hunt_le_90` | 12 | S_STRANGER | 33.3% | -20.5 | 0.39 | 0.78 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 27.8% | -5.6 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 66.7% | +18.8 | 4.18 | 2.09 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | -4.1 | `all` | 11 | S_STRANGER | 27.3% | -4.1 | 0.66 | 1.16 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 37 | S_STRANGER | 27.0% | -13.0 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 40.0% | -18.6 | 0.30 | 0.45 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 20.0% | -10.1 | `stop_hunt_le_90` | 8 | S_STRANGER | 25.0% | -8.1 | 0.44 | 1.11 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 15 | S_STRANGER | 20.0% | -17.1 | `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 27.3% | -12.0 | 0.33 | 0.78 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 27 | S_STRANGER | 18.5% | -13.8 | `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 20.0% | -14.7 | 0.20 | 0.63 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 22 | S_STRANGER | 18.2% | -5.8 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 33.3% | +5.5 | 1.86 | 3.72 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 18 | S_STRANGER | 16.7% | -4.6 | `all` | 18 | S_STRANGER | 16.7% | -4.6 | 0.55 | 1.38 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 15.8% | -7.0 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 18.2% | -3.7 | 0.68 | 2.71 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 15.4% | +0.9 | `tdi_rsi_gt_signal` | 10 | S_STRANGER | 20.0% | +4.8 | 1.47 | 4.40 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -11.0 | `all` | 13 | S_STRANGER | 15.4% | -11.0 | 0.28 | 0.62 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -18.1 | `stop_hunt_le_90` | 8 | S_STRANGER | 25.0% | -1.7 | 0.81 | 2.03 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 18 | S_STRANGER | 11.1% | -13.1 | `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 14.3% | -13.7 | 0.21 | 0.42 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -16.0 | `stop_hunt_le_90` | 8 | S_STRANGER | 12.5% | -7.5 | 0.30 | 1.49 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 19 | S_STRANGER | 5.3% | -20.5 | `confluence_gte_70` | 11 | S_STRANGER | 9.1% | -16.6 | 0.17 | 1.75 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 0.0% | -12.7 | `confluence_gte_60` | 8 | S_STRANGER | 0.0% | -12.0 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 11 | S_STRANGER | 0.0% | -34.8 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 0.0% | -31.2 | 0.00 | 0.00 | 0 | 0 | fail |

## Candidate Details

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=60.0% Avg=+18.8; validation N=6 Fav=100.0% Avg=+39.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | R_RUNNER | 100.0% | 81.8% | 81.8% | 27.3% | +30.0 | 13.28 | 2.95 | +44.5 | +13.6 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 0.0% | +4.0 | 1.59 | 1.59 | +28.9 | +18.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | R_RUNNER | 100.0% | 81.8% | 81.8% | 27.3% | +30.0 | 13.28 | 2.95 | +44.5 | +13.6 |
| `confluence_gte_60` | 11 | R_RUNNER | 100.0% | 81.8% | 81.8% | 27.3% | +30.0 | 13.28 | 2.95 | +44.5 | +13.6 |
| `confluence_gte_70` | 11 | R_RUNNER | 100.0% | 81.8% | 81.8% | 27.3% | +30.0 | 13.28 | 2.95 | +44.5 | +13.6 |
| `tdi_rsi_gt_signal` | 5 | R_REPEATER | 45.5% | 60.0% | 60.0% | 0.0% | +15.5 | 3.87 | 2.58 | +30.4 | +19.6 |
| `tdi_rsi_gte_50` | 5 | R_RUNNER | 45.5% | 80.0% | 80.0% | 0.0% | +26.7 | 6.72 | 1.68 | +39.1 | +18.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | R_RUNNER | 100.0% | 81.8% | 81.8% | 27.3% | +30.0 | 13.28 | 2.95 | +44.5 | +13.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=100.0% Avg=+32.1; validation N=7 Fav=57.1% Avg=+10.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | R_REPEATER | 100.0% | 66.7% | 77.8% | 33.3% | +15.2 | 9.60 | 2.06 | +25.2 | +16.3 |
| `hunt_to_ar_ratio_le_2_0` | 18 | R_REPEATER | 100.0% | 66.7% | 77.8% | 33.3% | +15.2 | 9.60 | 2.06 | +25.2 | +16.3 |
| `hunt_to_ar_ratio_le_2_5` | 18 | R_REPEATER | 100.0% | 66.7% | 77.8% | 33.3% | +15.2 | 9.60 | 2.06 | +25.2 | +16.3 |
| `stop_hunt_le_90` | 18 | R_REPEATER | 100.0% | 66.7% | 77.8% | 33.3% | +15.2 | 9.60 | 2.06 | +25.2 | +16.3 |
| `asian_range_gte_30` | 18 | R_REPEATER | 100.0% | 66.7% | 77.8% | 33.3% | +15.2 | 9.60 | 2.06 | +25.2 | +16.3 |
| `confluence_gte_60` | 13 | R_RUNNER | 72.2% | 76.9% | 92.3% | 38.5% | +20.6 | 55.72 | 4.64 | +29.0 | +14.0 |
| `confluence_gte_70` | 2 | R_REPEATER | 11.1% | 50.0% | 50.0% | 0.0% | +5.0 | 3.04 | 3.04 | +15.6 | +21.3 |
| `tdi_rsi_gt_signal` | 13 | R_REPEATER | 72.2% | 69.2% | 76.9% | 46.2% | +13.9 | 14.36 | 2.87 | +24.3 | +14.7 |
| `tdi_rsi_gte_50` | 8 | R_RUNNER | 44.4% | 75.0% | 75.0% | 25.0% | +13.9 | 5.76 | 1.92 | +24.5 | +20.4 |
| `ratio_le_2_and_asian_gte_30` | 18 | R_REPEATER | 100.0% | 66.7% | 77.8% | 33.3% | +15.2 | 9.60 | 2.06 | +25.2 | +16.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | R_REPEATER | 72.2% | 69.2% | 76.9% | 46.2% | +13.9 | 14.36 | 2.87 | +24.3 | +14.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | R_REPEATER | 100.0% | 66.7% | 77.8% | 33.3% | +15.2 | 9.60 | 2.06 | +25.2 | +16.3 |
| `feature_stale_hod_exhaustion_reject` | 18 | R_REPEATER | 100.0% | 66.7% | 77.8% | 33.3% | +15.2 | 9.60 | 2.06 | +25.2 | +16.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+5.9; validation N=3 Fav=100.0% Avg=+33.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | R_REPEATER | 100.0% | 66.7% | 66.7% | 33.3% | +10.3 | 2.90 | 1.45 | +30.5 | +17.0 |
| `hunt_to_ar_ratio_le_2_0` | 17 | R_REPEATER | 94.4% | 64.7% | 64.7% | 35.3% | +9.1 | 2.59 | 1.41 | +30.1 | +17.8 |
| `hunt_to_ar_ratio_le_2_5` | 18 | R_REPEATER | 100.0% | 66.7% | 66.7% | 33.3% | +10.3 | 2.90 | 1.45 | +30.5 | +17.0 |
| `stop_hunt_le_90` | 16 | R_REPEATER | 88.9% | 62.5% | 62.5% | 37.5% | +9.4 | 2.53 | 1.52 | +30.9 | +18.0 |
| `asian_range_gte_30` | 18 | R_REPEATER | 100.0% | 66.7% | 66.7% | 33.3% | +10.3 | 2.90 | 1.45 | +30.5 | +17.0 |
| `confluence_gte_60` | 18 | R_REPEATER | 100.0% | 66.7% | 66.7% | 33.3% | +10.3 | 2.90 | 1.45 | +30.5 | +17.0 |
| `confluence_gte_70` | 18 | R_REPEATER | 100.0% | 66.7% | 66.7% | 33.3% | +10.3 | 2.90 | 1.45 | +30.5 | +17.0 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 44.4% | 62.5% | 62.5% | 25.0% | +4.5 | 1.58 | 0.95 | +31.2 | +20.5 |
| `tdi_rsi_gte_50` | 9 | R_REPEATER | 50.0% | 66.7% | 66.7% | 11.1% | +15.0 | 5.67 | 2.84 | +33.4 | +22.9 |
| `ratio_le_2_and_asian_gte_30` | 17 | R_REPEATER | 94.4% | 64.7% | 64.7% | 35.3% | +9.1 | 2.59 | 1.41 | +30.1 | +17.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 44.4% | 62.5% | 62.5% | 25.0% | +4.5 | 1.58 | 0.95 | +31.2 | +20.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | R_REPEATER | 88.9% | 62.5% | 62.5% | 37.5% | +9.4 | 2.53 | 1.52 | +30.9 | +18.0 |
| `feature_stale_hod_exhaustion_reject` | 18 | R_REPEATER | 100.0% | 66.7% | 66.7% | 33.3% | +10.3 | 2.90 | 1.45 | +30.5 | +17.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+18.3; validation N=3 Fav=66.7% Avg=+58.9; out_of_sample N=6 Fav=66.7% Avg=+13.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | R_REPEATER | 100.0% | 64.7% | 64.7% | 11.8% | +17.3 | 3.61 | 1.97 | +37.1 | +24.1 |
| `hunt_to_ar_ratio_le_2_0` | 14 | R_REPEATER | 82.4% | 64.3% | 64.3% | 14.3% | +19.2 | 3.58 | 1.99 | +40.7 | +23.9 |
| `hunt_to_ar_ratio_le_2_5` | 14 | R_REPEATER | 82.4% | 64.3% | 64.3% | 14.3% | +19.2 | 3.58 | 1.99 | +40.7 | +23.9 |
| `stop_hunt_le_90` | 15 | R_REPEATER | 88.2% | 66.7% | 66.7% | 13.3% | +18.1 | 3.61 | 1.81 | +39.4 | +23.6 |
| `asian_range_gte_30` | 17 | R_REPEATER | 100.0% | 64.7% | 64.7% | 11.8% | +17.3 | 3.61 | 1.97 | +37.1 | +24.1 |
| `confluence_gte_60` | 17 | R_REPEATER | 100.0% | 64.7% | 64.7% | 11.8% | +17.3 | 3.61 | 1.97 | +37.1 | +24.1 |
| `confluence_gte_70` | 17 | R_REPEATER | 100.0% | 64.7% | 64.7% | 11.8% | +17.3 | 3.61 | 1.97 | +37.1 | +24.1 |
| `tdi_rsi_gt_signal` | 9 | R_REPEATER | 52.9% | 66.7% | 66.7% | 11.1% | +28.3 | 4.79 | 2.40 | +48.1 | +26.9 |
| `tdi_rsi_gte_50` | 10 | R_REPEATER | 58.8% | 70.0% | 70.0% | 10.0% | +27.6 | 4.57 | 1.96 | +45.5 | +26.9 |
| `ratio_le_2_and_asian_gte_30` | 14 | R_REPEATER | 82.4% | 64.3% | 64.3% | 14.3% | +19.2 | 3.58 | 1.99 | +40.7 | +23.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 47.1% | 62.5% | 62.5% | 12.5% | +31.4 | 4.74 | 2.84 | +51.4 | +28.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | R_REPEATER | 88.2% | 66.7% | 66.7% | 13.3% | +18.1 | 3.61 | 1.81 | +39.4 | +23.6 |
| `feature_stale_hod_exhaustion_reject` | 17 | R_REPEATER | 100.0% | 64.7% | 64.7% | 11.8% | +17.3 | 3.61 | 1.97 | +37.1 | +24.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=71.4% Avg=+20.7; validation N=4 Fav=50.0% Avg=+13.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `hunt_to_ar_ratio_le_2_0` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `hunt_to_ar_ratio_le_2_5` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `stop_hunt_le_90` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `asian_range_gte_30` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `confluence_gte_60` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `confluence_gte_70` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `tdi_rsi_gt_signal` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 63.6% | 57.1% | 57.1% | 14.3% | +9.5 | 3.05 | 2.28 | +28.6 | +20.7 |
| `ratio_le_2_and_asian_gte_30` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `feature_stale_hod_exhaustion_reject` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +18.0 | 7.09 | 3.04 | +37.1 | +15.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=57.1% Avg=+9.2; validation N=7 Fav=85.7% Avg=+46.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | R_REPEATER | 100.0% | 58.6% | 58.6% | 41.4% | +18.8 | 4.22 | 2.23 | +40.9 | +15.3 |
| `hunt_to_ar_ratio_le_2_0` | 28 | R_REPEATER | 96.6% | 60.7% | 60.7% | 42.9% | +19.5 | 4.24 | 2.00 | +40.2 | +15.7 |
| `hunt_to_ar_ratio_le_2_5` | 29 | R_REPEATER | 100.0% | 58.6% | 58.6% | 41.4% | +18.8 | 4.22 | 2.23 | +40.9 | +15.3 |
| `stop_hunt_le_90` | 23 | R_REPEATER | 79.3% | 60.9% | 60.9% | 47.8% | +18.1 | 3.88 | 1.66 | +37.6 | +16.8 |
| `asian_range_gte_30` | 29 | R_REPEATER | 100.0% | 58.6% | 58.6% | 41.4% | +18.8 | 4.22 | 2.23 | +40.9 | +15.3 |
| `confluence_gte_60` | 29 | R_REPEATER | 100.0% | 58.6% | 58.6% | 41.4% | +18.8 | 4.22 | 2.23 | +40.9 | +15.3 |
| `confluence_gte_70` | 29 | R_REPEATER | 100.0% | 58.6% | 58.6% | 41.4% | +18.8 | 4.22 | 2.23 | +40.9 | +15.3 |
| `tdi_rsi_gt_signal` | 14 | R_REPEATER | 48.3% | 71.4% | 71.4% | 50.0% | +24.3 | 4.75 | 1.42 | +45.2 | +15.8 |
| `tdi_rsi_gte_50` | 14 | R_REPEATER | 48.3% | 71.4% | 71.4% | 35.7% | +27.7 | 5.12 | 2.05 | +50.3 | +15.3 |
| `ratio_le_2_and_asian_gte_30` | 28 | R_REPEATER | 96.6% | 60.7% | 60.7% | 42.9% | +19.5 | 4.24 | 2.00 | +40.2 | +15.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | R_REPEATER | 48.3% | 71.4% | 71.4% | 50.0% | +24.3 | 4.75 | 1.42 | +45.2 | +15.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | R_REPEATER | 79.3% | 60.9% | 60.9% | 47.8% | +18.1 | 3.88 | 1.66 | +37.6 | +16.8 |
| `feature_stale_hod_exhaustion_reject` | 29 | R_REPEATER | 100.0% | 58.6% | 58.6% | 41.4% | +18.8 | 4.22 | 2.23 | +40.9 | +15.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=14 Fav=57.1% Avg=+14.3; validation N=16 Fav=68.8% Avg=+4.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 43 | R_REPEATER | 100.0% | 53.5% | 53.5% | 23.3% | +4.4 | 1.52 | 1.12 | +29.7 | +15.2 |
| `hunt_to_ar_ratio_le_2_0` | 37 | S_STRANGER | 86.0% | 48.6% | 48.6% | 21.6% | +0.7 | 1.07 | 0.95 | +27.6 | +15.5 |
| `hunt_to_ar_ratio_le_2_5` | 41 | R_REPEATER | 95.3% | 51.2% | 51.2% | 22.0% | +3.8 | 1.43 | 1.16 | +29.2 | +15.7 |
| `stop_hunt_le_90` | 35 | R_REPEATER | 81.4% | 51.4% | 51.4% | 22.9% | +3.3 | 1.41 | 1.10 | +28.3 | +16.6 |
| `asian_range_gte_30` | 43 | R_REPEATER | 100.0% | 53.5% | 53.5% | 23.3% | +4.4 | 1.52 | 1.12 | +29.7 | +15.2 |
| `confluence_gte_60` | 30 | R_REPEATER | 69.8% | 63.3% | 63.3% | 23.3% | +9.2 | 2.68 | 1.41 | +33.3 | +13.6 |
| `confluence_gte_70` | 4 | R_RUNNER | 9.3% | 75.0% | 75.0% | 0.0% | +0.2 | 1.10 | 0.37 | +25.0 | +13.4 |
| `tdi_rsi_gt_signal` | 23 | R_REPEATER | 53.5% | 56.5% | 56.5% | 21.7% | +2.9 | 1.28 | 0.89 | +28.2 | +16.1 |
| `tdi_rsi_gte_50` | 29 | R_REPEATER | 67.4% | 62.1% | 62.1% | 13.8% | +7.9 | 2.53 | 1.41 | +32.9 | +16.1 |
| `ratio_le_2_and_asian_gte_30` | 37 | S_STRANGER | 86.0% | 48.6% | 48.6% | 21.6% | +0.7 | 1.07 | 0.95 | +27.6 | +15.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 20 | R_REPEATER | 46.5% | 50.0% | 50.0% | 20.0% | -0.2 | 0.98 | 0.88 | +27.8 | +16.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 35 | R_REPEATER | 81.4% | 51.4% | 51.4% | 22.9% | +3.3 | 1.41 | 1.10 | +28.3 | +16.6 |
| `feature_stale_hod_exhaustion_reject` | 43 | R_REPEATER | 100.0% | 53.5% | 53.5% | 23.3% | +4.4 | 1.52 | 1.12 | +29.7 | +15.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=13 Fav=46.2% Avg=+1.7; out_of_sample N=4 Fav=100.0% Avg=+43.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | R_REPEATER | 100.0% | 52.2% | 52.2% | 17.4% | +7.1 | 1.62 | 1.49 | +32.9 | +25.2 |
| `hunt_to_ar_ratio_le_2_0` | 17 | R_REPEATER | 73.9% | 58.8% | 58.8% | 17.6% | +11.5 | 2.34 | 1.64 | +34.2 | +22.7 |
| `hunt_to_ar_ratio_le_2_5` | 22 | R_REPEATER | 95.7% | 54.5% | 54.5% | 18.2% | +7.8 | 1.68 | 1.40 | +33.0 | +25.9 |
| `stop_hunt_le_90` | 19 | R_REPEATER | 82.6% | 57.9% | 57.9% | 21.1% | +13.6 | 2.75 | 2.00 | +35.1 | +21.6 |
| `asian_range_gte_30` | 23 | R_REPEATER | 100.0% | 52.2% | 52.2% | 17.4% | +7.1 | 1.62 | 1.49 | +32.9 | +25.2 |
| `confluence_gte_60` | 23 | R_REPEATER | 100.0% | 52.2% | 52.2% | 17.4% | +7.1 | 1.62 | 1.49 | +32.9 | +25.2 |
| `confluence_gte_70` | 23 | R_REPEATER | 100.0% | 52.2% | 52.2% | 17.4% | +7.1 | 1.62 | 1.49 | +32.9 | +25.2 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 26.1% | 33.3% | 33.3% | 16.7% | +5.6 | 1.51 | 3.02 | +25.4 | +30.3 |
| `tdi_rsi_gte_50` | 19 | R_REPEATER | 82.6% | 52.6% | 52.6% | 10.5% | +5.8 | 1.46 | 1.31 | +33.3 | +28.4 |
| `ratio_le_2_and_asian_gte_30` | 17 | R_REPEATER | 73.9% | 58.8% | 58.8% | 17.6% | +11.5 | 2.34 | 1.64 | +34.2 | +22.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 13.0% | 33.3% | 33.3% | 0.0% | +4.6 | 1.69 | 3.38 | +22.4 | +30.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | R_REPEATER | 82.6% | 57.9% | 57.9% | 21.1% | +13.6 | 2.75 | 2.00 | +35.1 | +21.6 |
| `feature_stale_hod_exhaustion_reject` | 23 | R_REPEATER | 100.0% | 52.2% | 52.2% | 17.4% | +7.1 | 1.62 | 1.49 | +32.9 | +25.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=50.0% Avg=+31.3; validation N=1 Fav=100.0% Avg=+54.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 45.0% | +13.3 | 2.62 | 1.84 | +35.8 | +18.7 |
| `hunt_to_ar_ratio_le_2_0` | 18 | R_REPEATER | 90.0% | 50.0% | 50.0% | 44.4% | +14.5 | 3.12 | 2.08 | +34.9 | +16.7 |
| `hunt_to_ar_ratio_le_2_5` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 45.0% | +13.3 | 2.62 | 1.84 | +35.8 | +18.7 |
| `stop_hunt_le_90` | 16 | R_REPEATER | 80.0% | 56.2% | 56.2% | 43.8% | +17.1 | 3.47 | 1.93 | +37.4 | +17.3 |
| `asian_range_gte_30` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 45.0% | +13.3 | 2.62 | 1.84 | +35.8 | +18.7 |
| `confluence_gte_60` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 45.0% | +13.3 | 2.62 | 1.84 | +35.8 | +18.7 |
| `confluence_gte_70` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 45.0% | +13.3 | 2.62 | 1.84 | +35.8 | +18.7 |
| `tdi_rsi_gt_signal` | 5 | R_REPEATER | 25.0% | 60.0% | 60.0% | 60.0% | +36.0 | 53.88 | 17.96 | +56.5 | +5.2 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 75.0% | 46.7% | 46.7% | 40.0% | +11.3 | 2.23 | 1.91 | +35.6 | +20.9 |
| `ratio_le_2_and_asian_gte_30` | 18 | R_REPEATER | 90.0% | 50.0% | 50.0% | 44.4% | +14.5 | 3.12 | 2.08 | +34.9 | +16.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 25.0% | 60.0% | 60.0% | 60.0% | +36.0 | 53.88 | 17.96 | +56.5 | +5.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | R_REPEATER | 80.0% | 56.2% | 56.2% | 43.8% | +17.1 | 3.47 | 1.93 | +37.4 | +17.3 |
| `feature_stale_hod_exhaustion_reject` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 45.0% | +13.3 | 2.62 | 1.84 | +35.8 | +18.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-62.5; validation N=5 Fav=60.0% Avg=+6.7; out_of_sample N=2 Fav=100.0% Avg=+54.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +4.8 | 1.37 | 1.37 | +36.7 | +27.2 |
| `hunt_to_ar_ratio_le_2_0` | 8 | R_REPEATER | 80.0% | 50.0% | 50.0% | 0.0% | +4.4 | 1.32 | 1.32 | +40.2 | +28.2 |
| `hunt_to_ar_ratio_le_2_5` | 8 | R_REPEATER | 80.0% | 50.0% | 50.0% | 0.0% | +4.4 | 1.32 | 1.32 | +40.2 | +28.2 |
| `stop_hunt_le_90` | 8 | R_REPEATER | 80.0% | 62.5% | 62.5% | 12.5% | +9.9 | 1.83 | 1.10 | +37.0 | +24.9 |
| `asian_range_gte_30` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +4.8 | 1.37 | 1.37 | +36.7 | +27.2 |
| `confluence_gte_60` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +4.8 | 1.37 | 1.37 | +36.7 | +27.2 |
| `confluence_gte_70` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +4.8 | 1.37 | 1.37 | +36.7 | +27.2 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 11.1% | +0.6 | 1.04 | 1.30 | +34.9 | +28.2 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 40.0% | 40.0% | 0.0% | +10.4 | 2.20 | 3.30 | +41.0 | +27.2 |
| `ratio_le_2_and_asian_gte_30` | 8 | R_REPEATER | 80.0% | 50.0% | 50.0% | 0.0% | +4.4 | 1.32 | 1.32 | +40.2 | +28.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 0.0% | -1.0 | 0.93 | 1.25 | +38.4 | +29.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | R_REPEATER | 80.0% | 62.5% | 62.5% | 12.5% | +9.9 | 1.83 | 1.10 | +37.0 | +24.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +4.8 | 1.37 | 1.37 | +36.7 | +27.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=85.7% Avg=+20.6; validation N=4 Fav=0.0% Avg=-21.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 33.3% | +4.6 | 1.58 | 1.32 | +28.6 | +22.4 |
| `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 33.3% | +4.6 | 1.58 | 1.32 | +28.6 | +22.4 |
| `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 33.3% | +4.6 | 1.58 | 1.32 | +28.6 | +22.4 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 33.3% | +4.6 | 1.58 | 1.32 | +28.6 | +22.4 |
| `asian_range_gte_30` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 33.3% | +4.6 | 1.58 | 1.32 | +28.6 | +22.4 |
| `confluence_gte_60` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 28.6% | -1.1 | 0.89 | 0.89 | +25.1 | +23.6 |
| `confluence_gte_70` | 3 | R_RUNNER | 25.0% | 100.0% | 100.0% | 33.3% | +21.4 | 999.00 | 999.00 | +28.8 | +20.3 |
| `tdi_rsi_gt_signal` | 10 | R_REPEATER | 83.3% | 50.0% | 50.0% | 30.0% | +3.3 | 1.36 | 1.09 | +29.3 | +23.6 |
| `tdi_rsi_gte_50` | 11 | R_REPEATER | 91.7% | 54.5% | 54.5% | 36.4% | +5.3 | 1.63 | 1.09 | +30.0 | +23.6 |
| `ratio_le_2_and_asian_gte_30` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 33.3% | +4.6 | 1.58 | 1.32 | +28.6 | +22.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | R_REPEATER | 83.3% | 50.0% | 50.0% | 30.0% | +3.3 | 1.36 | 1.09 | +29.3 | +23.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 33.3% | +4.6 | 1.58 | 1.32 | +28.6 | +22.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 33.3% | +4.6 | 1.58 | 1.32 | +28.6 | +22.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=10 Fav=60.0% Avg=+4.5; out_of_sample N=2 Fav=50.0% Avg=+38.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +4.1 | 1.44 | 1.44 | +31.6 | +27.7 |
| `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 85.7% | 58.3% | 58.3% | 25.0% | +5.6 | 1.54 | 1.10 | +34.7 | +26.8 |
| `hunt_to_ar_ratio_le_2_5` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +4.1 | 1.44 | 1.44 | +31.6 | +27.7 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 85.7% | 58.3% | 58.3% | 25.0% | +10.1 | 2.80 | 2.00 | +32.8 | +21.0 |
| `asian_range_gte_30` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +4.1 | 1.44 | 1.44 | +31.6 | +27.7 |
| `confluence_gte_60` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +4.1 | 1.44 | 1.44 | +31.6 | +27.7 |
| `confluence_gte_70` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +4.1 | 1.44 | 1.44 | +31.6 | +27.7 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -32.0 | 0.00 | 0.00 | +26.1 | +49.6 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 92.9% | 46.2% | 46.2% | 15.4% | +3.1 | 1.31 | 1.53 | +30.1 | +28.9 |
| `ratio_le_2_and_asian_gte_30` | 12 | R_REPEATER | 85.7% | 58.3% | 58.3% | 25.0% | +5.6 | 1.54 | 1.10 | +34.7 | +26.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -32.0 | 0.00 | 0.00 | +26.1 | +49.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 85.7% | 58.3% | 58.3% | 25.0% | +10.1 | 2.80 | 2.00 | +32.8 | +21.0 |
| `feature_stale_hod_exhaustion_reject` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +4.1 | 1.44 | 1.44 | +31.6 | +27.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+14.5; validation N=5 Fav=40.0% Avg=-1.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +4.0 | 1.48 | 1.18 | +34.6 | +17.9 |
| `hunt_to_ar_ratio_le_2_0` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +4.0 | 1.48 | 1.18 | +34.6 | +17.9 |
| `hunt_to_ar_ratio_le_2_5` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +4.0 | 1.48 | 1.18 | +34.6 | +17.9 |
| `stop_hunt_le_90` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +4.0 | 1.48 | 1.18 | +34.6 | +17.9 |
| `asian_range_gte_30` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +4.0 | 1.48 | 1.18 | +34.6 | +17.9 |
| `confluence_gte_60` | 10 | R_REPEATER | 50.0% | 50.0% | 50.0% | 20.0% | +6.7 | 1.86 | 1.49 | +27.0 | +17.8 |
| `confluence_gte_70` | 2 | R_REPEATER | 10.0% | 50.0% | 50.0% | 0.0% | -6.8 | 0.57 | 0.57 | +21.2 | +24.4 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 20.0% | 25.0% | 25.0% | 25.0% | -2.0 | 0.86 | 1.72 | +69.0 | +27.3 |
| `tdi_rsi_gte_50` | 14 | R_REPEATER | 70.0% | 50.0% | 50.0% | 35.7% | +6.2 | 1.70 | 1.22 | +41.0 | +19.1 |
| `ratio_le_2_and_asian_gte_30` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +4.0 | 1.48 | 1.18 | +34.6 | +17.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 20.0% | 25.0% | 25.0% | 25.0% | -2.0 | 0.86 | 1.72 | +69.0 | +27.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +4.0 | 1.48 | 1.18 | +34.6 | +17.9 |
| `feature_stale_hod_exhaustion_reject` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +4.0 | 1.48 | 1.18 | +34.6 | +17.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+19.1; validation N=2 Fav=100.0% Avg=+17.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 48.0% | 48.0% | 32.0% | +9.7 | 2.29 | 2.09 | +27.5 | +14.3 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 96.0% | 45.8% | 45.8% | 33.3% | +7.4 | 1.94 | 1.94 | +25.6 | +14.0 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 100.0% | 48.0% | 48.0% | 32.0% | +9.7 | 2.29 | 2.09 | +27.5 | +14.3 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 88.0% | 45.5% | 45.5% | 36.4% | +7.6 | 1.97 | 1.97 | +25.9 | +14.9 |
| `asian_range_gte_30` | 25 | S_STRANGER | 100.0% | 48.0% | 48.0% | 32.0% | +9.7 | 2.29 | 2.09 | +27.5 | +14.3 |
| `confluence_gte_60` | 13 | R_REPEATER | 52.0% | 61.5% | 61.5% | 30.8% | +18.0 | 3.74 | 2.34 | +33.5 | +11.9 |
| `confluence_gte_70` | 1 | R_RUNNER | 4.0% | 100.0% | 100.0% | 100.0% | +48.7 | 999.00 | 999.00 | +49.3 | +12.3 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 32.0% | 62.5% | 62.5% | 50.0% | +18.6 | 4.80 | 1.92 | +36.1 | +12.7 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 48.0% | 58.3% | 58.3% | 33.3% | +22.0 | 4.38 | 2.50 | +40.8 | +14.3 |
| `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 96.0% | 45.8% | 45.8% | 33.3% | +7.4 | 1.94 | 1.94 | +25.6 | +14.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 32.0% | 62.5% | 62.5% | 50.0% | +18.6 | 4.80 | 1.92 | +36.1 | +12.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 88.0% | 45.5% | 45.5% | 36.4% | +7.6 | 1.97 | 1.97 | +25.9 | +14.9 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 48.0% | 48.0% | 32.0% | +9.7 | 2.29 | 2.09 | +27.5 | +14.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=14 Fav=42.9% Avg=+4.6; validation N=6 Fav=66.7% Avg=+18.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 48.0% | 48.0% | 24.0% | +8.1 | 1.92 | 1.92 | +32.3 | +18.5 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 88.0% | 45.5% | 45.5% | 27.3% | +6.1 | 1.70 | 1.87 | +30.3 | +18.9 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 96.0% | 45.8% | 45.8% | 25.0% | +7.5 | 1.82 | 1.99 | +31.9 | +19.1 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 84.0% | 42.9% | 42.9% | 28.6% | +4.7 | 1.52 | 1.86 | +30.0 | +19.3 |
| `asian_range_gte_30` | 25 | S_STRANGER | 100.0% | 48.0% | 48.0% | 24.0% | +8.1 | 1.92 | 1.92 | +32.3 | +18.5 |
| `confluence_gte_60` | 19 | S_STRANGER | 76.0% | 47.4% | 47.4% | 15.8% | +9.3 | 2.09 | 2.33 | +32.9 | +20.8 |
| `confluence_gte_70` | 2 | R_REPEATER | 8.0% | 50.0% | 50.0% | 50.0% | +2.4 | 1.27 | 1.27 | +38.7 | +13.6 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 16.0% | 50.0% | 50.0% | 25.0% | +0.6 | 1.06 | 1.06 | +32.4 | +25.6 |
| `tdi_rsi_gte_50` | 20 | R_REPEATER | 80.0% | 50.0% | 50.0% | 20.0% | +8.7 | 2.13 | 1.92 | +33.5 | +20.1 |
| `ratio_le_2_and_asian_gte_30` | 22 | S_STRANGER | 88.0% | 45.5% | 45.5% | 27.3% | +6.1 | 1.70 | 1.87 | +30.3 | +18.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 16.0% | 50.0% | 50.0% | 25.0% | +0.6 | 1.06 | 1.06 | +32.4 | +25.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 84.0% | 42.9% | 42.9% | 28.6% | +4.7 | 1.52 | 1.86 | +30.0 | +19.3 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 48.0% | 48.0% | 24.0% | +8.1 | 1.92 | 1.92 | +32.3 | +18.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=55.6% Avg=+23.1; validation N=3 Fav=100.0% Avg=+22.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 47.6% | 52.4% | 28.6% | +12.1 | 2.84 | 2.07 | +34.6 | +15.0 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 95.2% | 45.0% | 50.0% | 30.0% | +5.9 | 1.86 | 1.49 | +27.8 | +14.9 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 100.0% | 47.6% | 52.4% | 28.6% | +12.1 | 2.84 | 2.07 | +34.6 | +15.0 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 95.2% | 45.0% | 50.0% | 30.0% | +11.9 | 2.72 | 2.18 | +35.2 | +14.5 |
| `asian_range_gte_30` | 21 | S_STRANGER | 100.0% | 47.6% | 52.4% | 28.6% | +12.1 | 2.84 | 2.07 | +34.6 | +15.0 |
| `confluence_gte_60` | 9 | R_REPEATER | 42.9% | 55.6% | 66.7% | 22.2% | +19.6 | 4.95 | 1.65 | +43.1 | +14.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | R_REPEATER | 57.1% | 66.7% | 66.7% | 33.3% | +23.1 | 5.76 | 2.16 | +48.8 | +13.5 |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 38.1% | 50.0% | 50.0% | 37.5% | +4.0 | 1.81 | 0.91 | +26.2 | +17.2 |
| `ratio_le_2_and_asian_gte_30` | 20 | S_STRANGER | 95.2% | 45.0% | 50.0% | 30.0% | +5.9 | 1.86 | 1.49 | +27.8 | +14.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | R_REPEATER | 52.4% | 63.6% | 63.6% | 36.4% | +12.9 | 3.44 | 1.47 | +37.8 | +13.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 95.2% | 45.0% | 50.0% | 30.0% | +11.9 | 2.72 | 2.18 | +35.2 | +14.5 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 47.6% | 52.4% | 28.6% | +12.1 | 2.84 | 2.07 | +34.6 | +15.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=50.0% Avg=+22.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 45.0% | 45.0% | 35.0% | +8.1 | 2.47 | 2.74 | +25.4 | +18.0 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +7.6 | 2.27 | 2.55 | +25.1 | +18.6 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 95.0% | 42.1% | 42.1% | 31.6% | +7.0 | 2.20 | 2.76 | +24.3 | +18.7 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +7.6 | 2.27 | 2.55 | +25.1 | +18.6 |
| `asian_range_gte_30` | 20 | S_STRANGER | 100.0% | 45.0% | 45.0% | 35.0% | +8.1 | 2.47 | 2.74 | +25.4 | +18.0 |
| `confluence_gte_60` | 19 | S_STRANGER | 95.0% | 47.4% | 47.4% | 36.8% | +8.6 | 2.48 | 2.48 | +25.7 | +18.7 |
| `confluence_gte_70` | 6 | R_REPEATER | 30.0% | 50.0% | 50.0% | 66.7% | +22.0 | 10.87 | 7.24 | +38.1 | +13.5 |
| `tdi_rsi_gt_signal` | 10 | R_REPEATER | 50.0% | 50.0% | 50.0% | 30.0% | +8.8 | 2.53 | 2.53 | +26.7 | +22.5 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 50.0% | 40.0% | 40.0% | 20.0% | +4.3 | 1.58 | 2.37 | +22.9 | +23.9 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +7.6 | 2.27 | 2.55 | +25.1 | +18.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 40.0% | 50.0% | 50.0% | 25.0% | +7.7 | 2.13 | 2.13 | +26.3 | +25.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +7.6 | 2.27 | 2.55 | +25.1 | +18.6 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 45.0% | 45.0% | 35.0% | +8.1 | 2.47 | 2.74 | +25.4 | +18.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=57.1% Avg=+17.0; validation N=2 Fav=100.0% Avg=+58.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +12.7 | 2.38 | 2.78 | +34.6 | +18.4 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 78.6% | 36.4% | 36.4% | 27.3% | +9.6 | 1.92 | 2.88 | +34.9 | +19.3 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +12.7 | 2.38 | 2.78 | +34.6 | +18.4 |
| `stop_hunt_le_90` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 22.2% | -1.3 | 0.91 | 2.72 | +28.9 | +20.3 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +12.7 | 2.38 | 2.78 | +34.6 | +18.4 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +12.7 | 2.38 | 2.78 | +34.6 | +18.4 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +12.7 | 2.38 | 2.78 | +34.6 | +18.4 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +12.7 | 2.38 | 2.78 | +34.6 | +18.4 |
| `tdi_rsi_gte_50` | 9 | R_REPEATER | 64.3% | 66.7% | 66.7% | 22.2% | +26.3 | 4.40 | 2.20 | +42.8 | +16.9 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 78.6% | 36.4% | 36.4% | 27.3% | +9.6 | 1.92 | 2.88 | +34.9 | +19.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 78.6% | 36.4% | 36.4% | 27.3% | +9.6 | 1.92 | 2.88 | +34.9 | +19.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 22.2% | -1.3 | 0.91 | 2.72 | +28.9 | +20.3 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +12.7 | 2.38 | 2.78 | +34.6 | +18.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=40.0% Avg=-5.0; validation N=3 Fav=66.7% Avg=+17.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 14.3% | -2.0 | 0.86 | 1.00 | +31.1 | +32.2 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 14.3% | -2.0 | 0.86 | 1.00 | +31.1 | +32.2 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 14.3% | -2.0 | 0.86 | 1.00 | +31.1 | +32.2 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 92.9% | 46.2% | 46.2% | 15.4% | +0.3 | 1.02 | 1.02 | +33.4 | +31.8 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 14.3% | -2.0 | 0.86 | 1.00 | +31.1 | +32.2 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 14.3% | -2.0 | 0.86 | 1.00 | +31.1 | +32.2 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 14.3% | -2.0 | 0.86 | 1.00 | +31.1 | +32.2 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -34.8 | 0.00 | 0.00 | +20.2 | +55.4 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 92.9% | 38.5% | 38.5% | 15.4% | -5.3 | 0.64 | 0.89 | +29.4 | +33.5 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 14.3% | -2.0 | 0.86 | 1.00 | +31.1 | +32.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -34.8 | 0.00 | 0.00 | +20.2 | +55.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 92.9% | 46.2% | 46.2% | 15.4% | +0.3 | 1.02 | 1.02 | +33.4 | +31.8 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 14.3% | -2.0 | 0.86 | 1.00 | +31.1 | +32.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=60.0% Avg=+35.1; out_of_sample N=2 Fav=50.0% Avg=+25.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 40.9% | 50.0% | 31.8% | +8.4 | 1.63 | 1.48 | +34.0 | +20.5 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 77.3% | 35.3% | 47.1% | 35.3% | +8.0 | 1.63 | 1.63 | +35.4 | +19.0 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 100.0% | 40.9% | 50.0% | 31.8% | +8.4 | 1.63 | 1.48 | +34.0 | +20.5 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 81.8% | 38.9% | 50.0% | 33.3% | +7.1 | 1.57 | 1.40 | +33.3 | +22.4 |
| `asian_range_gte_30` | 22 | S_STRANGER | 100.0% | 40.9% | 50.0% | 31.8% | +8.4 | 1.63 | 1.48 | +34.0 | +20.5 |
| `confluence_gte_60` | 18 | S_STRANGER | 81.8% | 44.4% | 50.0% | 27.8% | +8.7 | 1.54 | 1.54 | +35.8 | +23.4 |
| `confluence_gte_70` | 7 | R_REPEATER | 31.8% | 57.1% | 71.4% | 57.1% | +32.2 | 4.83 | 1.93 | +53.5 | +15.7 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -17.0 | 0.00 | 0.00 | +15.8 | +5.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 45.5% | 10.0% | 10.0% | 20.0% | -16.5 | 0.34 | 2.68 | +22.2 | +31.1 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 77.3% | 35.3% | 47.1% | 35.3% | +8.0 | 1.63 | 1.63 | +35.4 | +19.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.5% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +24.6 | +10.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 81.8% | 38.9% | 50.0% | 33.3% | +7.1 | 1.57 | 1.40 | +33.3 | +22.4 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 40.9% | 50.0% | 31.8% | +8.4 | 1.63 | 1.48 | +34.0 | +20.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=57.1% Avg=+27.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 0.0% | +14.2 | 3.12 | 4.68 | +35.3 | +14.8 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 0.0% | +16.6 | 3.52 | 4.40 | +36.2 | +15.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 0.0% | +14.2 | 3.12 | 4.68 | +35.3 | +14.8 |
| `stop_hunt_le_90` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 0.0% | +16.6 | 3.52 | 4.40 | +36.2 | +15.1 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 0.0% | +14.2 | 3.12 | 4.68 | +35.3 | +14.8 |
| `confluence_gte_60` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | -1.5 | 0.74 | 2.22 | +19.3 | +9.5 |
| `confluence_gte_70` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -6.4 | 0.00 | 0.00 | +3.1 | +7.9 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | +90.4 | 201.78 | 201.78 | +112.1 | +22.3 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 70.0% | 57.1% | 57.1% | 0.0% | +27.7 | 14.11 | 10.59 | +45.9 | +16.9 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 0.0% | +16.6 | 3.52 | 4.40 | +36.2 | +15.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | +90.4 | 201.78 | 201.78 | +112.1 | +22.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 0.0% | +16.6 | 3.52 | 4.40 | +36.2 | +15.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 0.0% | +14.2 | 3.12 | 4.68 | +35.3 | +14.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=66.7% Avg=+19.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +0.7 | 1.03 | 1.54 | +37.9 | +20.8 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +45.2 | 999.00 | 999.00 | +47.2 | +1.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +0.7 | 1.03 | 1.54 | +37.9 | +20.8 |
| `confluence_gte_60` | 6 | R_REPEATER | 60.0% | 66.7% | 66.7% | 33.3% | +19.7 | 1.92 | 0.96 | +60.9 | +11.8 |
| `confluence_gte_70` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -13.5 | 0.00 | 0.00 | +61.8 | +18.5 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 28.6% | -6.8 | 0.78 | 1.04 | +33.2 | +25.3 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 33.3% | +11.0 | 1.61 | 1.61 | +48.4 | +31.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +0.7 | 1.03 | 1.54 | +37.9 | +20.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=37.5% Avg=-5.0; out_of_sample N=6 Fav=50.0% Avg=-3.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 33.3% | 33.3% | 29.2% | -5.1 | 0.71 | 1.24 | +22.2 | +23.1 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 87.5% | 28.6% | 28.6% | 28.6% | -10.0 | 0.50 | 1.08 | +18.6 | +23.2 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 100.0% | 33.3% | 33.3% | 29.2% | -5.1 | 0.71 | 1.24 | +22.2 | +23.1 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 87.5% | 28.6% | 28.6% | 28.6% | -10.0 | 0.50 | 1.08 | +18.6 | +23.2 |
| `asian_range_gte_30` | 24 | S_STRANGER | 100.0% | 33.3% | 33.3% | 29.2% | -5.1 | 0.71 | 1.24 | +22.2 | +23.1 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 33.3% | 33.3% | 29.2% | -5.1 | 0.71 | 1.24 | +22.2 | +23.1 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 33.3% | 33.3% | 29.2% | -5.1 | 0.71 | 1.24 | +22.2 | +23.1 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 45.8% | 36.4% | 36.4% | 27.3% | -11.3 | 0.52 | 0.90 | +23.9 | +23.1 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 58.3% | 42.9% | 42.9% | 28.6% | -4.4 | 0.76 | 0.88 | +24.8 | +30.8 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 87.5% | 28.6% | 28.6% | 28.6% | -10.0 | 0.50 | 1.08 | +18.6 | +23.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 41.7% | 40.0% | 40.0% | 30.0% | -12.0 | 0.52 | 0.79 | +21.9 | +25.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 87.5% | 28.6% | 28.6% | 28.6% | -10.0 | 0.50 | 1.08 | +18.6 | +23.2 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 33.3% | 33.3% | 29.2% | -5.1 | 0.71 | 1.24 | +22.2 | +23.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=50.0% Avg=+2.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 8.3% | -8.1 | 0.54 | 1.08 | +18.4 | +28.2 |
| `hunt_to_ar_ratio_le_2_0` | 6 | R_REPEATER | 50.0% | 50.0% | 50.0% | 16.7% | +2.8 | 1.20 | 1.20 | +23.9 | +25.5 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 11.1% | -0.7 | 0.95 | 1.19 | +21.7 | +23.5 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 8.3% | -8.1 | 0.54 | 1.08 | +18.4 | +28.2 |
| `asian_range_gte_30` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 0.0% | -7.7 | 0.35 | 0.69 | +17.2 | +19.6 |
| `confluence_gte_60` | 11 | S_STRANGER | 91.7% | 36.4% | 36.4% | 9.1% | -3.0 | 0.78 | 1.36 | +19.6 | +24.2 |
| `confluence_gte_70` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -32.1 | 0.00 | 0.00 | +22.4 | +45.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 0.0% | -11.1 | 0.40 | 0.67 | +15.7 | +30.4 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 0.0% | -9.1 | 0.43 | 1.07 | +15.6 | +28.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 8.3% | -8.1 | 0.54 | 1.08 | +18.4 | +28.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 8.3% | -8.1 | 0.54 | 1.08 | +18.4 | +28.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=19 Fav=52.6% Avg=-2.1; out_of_sample N=4 Fav=25.0% Avg=-16.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 49 | S_STRANGER | 100.0% | 32.7% | 36.7% | 24.5% | -7.4 | 0.54 | 0.84 | +24.9 | +25.6 |
| `hunt_to_ar_ratio_le_2_0` | 33 | S_STRANGER | 67.3% | 30.3% | 36.4% | 21.2% | -10.7 | 0.39 | 0.62 | +24.2 | +27.5 |
| `hunt_to_ar_ratio_le_2_5` | 47 | S_STRANGER | 95.9% | 29.8% | 34.0% | 21.3% | -8.6 | 0.49 | 0.85 | +24.4 | +26.3 |
| `stop_hunt_le_90` | 36 | S_STRANGER | 73.5% | 25.0% | 30.6% | 19.4% | -13.0 | 0.32 | 0.67 | +22.0 | +29.1 |
| `asian_range_gte_30` | 49 | S_STRANGER | 100.0% | 32.7% | 36.7% | 24.5% | -7.4 | 0.54 | 0.84 | +24.9 | +25.6 |
| `confluence_gte_60` | 40 | S_STRANGER | 81.6% | 27.5% | 32.5% | 22.5% | -10.8 | 0.43 | 0.80 | +25.8 | +28.2 |
| `confluence_gte_70` | 15 | S_STRANGER | 30.6% | 20.0% | 33.3% | 20.0% | -12.8 | 0.33 | 0.59 | +21.3 | +30.3 |
| `tdi_rsi_gt_signal` | 27 | S_STRANGER | 55.1% | 44.4% | 44.4% | 29.6% | -0.8 | 0.93 | 1.01 | +32.5 | +20.7 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 46.9% | 47.8% | 47.8% | 30.4% | -4.5 | 0.74 | 0.74 | +36.9 | +27.7 |
| `ratio_le_2_and_asian_gte_30` | 33 | S_STRANGER | 67.3% | 30.3% | 36.4% | 21.2% | -10.7 | 0.39 | 0.62 | +24.2 | +27.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 20 | S_STRANGER | 40.8% | 45.0% | 45.0% | 25.0% | -4.2 | 0.68 | 0.76 | +30.3 | +23.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 36 | S_STRANGER | 73.5% | 25.0% | 30.6% | 19.4% | -13.0 | 0.32 | 0.67 | +22.0 | +29.1 |
| `feature_stale_hod_exhaustion_reject` | 49 | S_STRANGER | 100.0% | 32.7% | 36.7% | 24.5% | -7.4 | 0.54 | 0.84 | +24.9 | +25.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=50.0% Avg=-17.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 31.6% | 31.6% | 21.1% | -14.4 | 0.36 | 0.72 | +24.1 | +42.6 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 94.7% | 27.8% | 27.8% | 22.2% | -16.7 | 0.30 | 0.72 | +23.1 | +44.7 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 31.6% | 31.6% | 21.1% | -14.4 | 0.36 | 0.72 | +24.1 | +42.6 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 94.7% | 27.8% | 27.8% | 16.7% | -17.1 | 0.28 | 0.68 | +23.2 | +44.8 |
| `asian_range_gte_30` | 19 | S_STRANGER | 100.0% | 31.6% | 31.6% | 21.1% | -14.4 | 0.36 | 0.72 | +24.1 | +42.6 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 31.6% | 31.6% | 21.1% | -14.4 | 0.36 | 0.72 | +24.1 | +42.6 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 31.6% | 31.6% | 21.1% | -14.4 | 0.36 | 0.72 | +24.1 | +42.6 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 42.1% | 50.0% | 50.0% | 25.0% | -17.4 | 0.45 | 0.45 | +22.9 | +47.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 47.4% | 33.3% | 33.3% | 11.1% | -11.9 | 0.41 | 0.82 | +23.0 | +42.6 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 94.7% | 27.8% | 27.8% | 22.2% | -16.7 | 0.30 | 0.72 | +23.1 | +44.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 36.8% | 42.9% | 42.9% | 28.6% | -23.8 | 0.34 | 0.45 | +20.0 | +53.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 94.7% | 27.8% | 27.8% | 16.7% | -17.1 | 0.28 | 0.68 | +23.2 | +44.8 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 31.6% | 31.6% | 21.1% | -14.4 | 0.36 | 0.72 | +24.1 | +42.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=80.0% Avg=+5.9; validation N=2 Fav=0.0% Avg=-14.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 18.8% | -6.6 | 0.48 | 0.55 | +17.5 | +20.6 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 87.5% | 21.4% | 35.7% | 14.3% | -10.3 | 0.29 | 0.46 | +15.7 | +22.9 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 93.8% | 26.7% | 40.0% | 13.3% | -8.7 | 0.36 | 0.48 | +16.5 | +21.7 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 87.5% | 21.4% | 35.7% | 14.3% | -10.3 | 0.29 | 0.46 | +15.7 | +22.9 |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 18.8% | -6.6 | 0.48 | 0.55 | +17.5 | +20.6 |
| `confluence_gte_60` | 7 | R_REPEATER | 43.8% | 57.1% | 71.4% | 14.3% | +0.2 | 1.02 | 0.41 | +23.8 | +17.9 |
| `confluence_gte_70` | 1 | R_RUNNER | 6.2% | 100.0% | 100.0% | 100.0% | +12.9 | 999.00 | 999.00 | +52.0 | +5.4 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 62.5% | 20.0% | 30.0% | 20.0% | -10.5 | 0.34 | 0.68 | +16.6 | +25.5 |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 50.0% | 50.0% | 50.0% | 12.5% | -3.5 | 0.71 | 0.71 | +22.7 | +28.7 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 87.5% | 21.4% | 35.7% | 14.3% | -10.3 | 0.29 | 0.46 | +15.7 | +22.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 56.2% | 11.1% | 22.2% | 11.1% | -14.5 | 0.18 | 0.54 | +14.8 | +28.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 87.5% | 21.4% | 35.7% | 14.3% | -10.3 | 0.29 | 0.46 | +15.7 | +22.9 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 18.8% | -6.6 | 0.48 | 0.55 | +17.5 | +20.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+0.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.3 | 1.03 | 1.72 | +19.0 | +13.5 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 42.9% | -2.8 | 0.78 | 3.11 | +20.1 | +11.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.3 | 1.03 | 1.72 | +19.0 | +13.5 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 37.5% | -4.6 | 0.65 | 3.24 | +17.6 | +13.1 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.3 | 1.03 | 1.72 | +19.0 | +13.5 |
| `confluence_gte_60` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 66.7% | -6.7 | 0.00 | 0.00 | +13.2 | +18.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 40.0% | 40.0% | 0.0% | -7.3 | 0.52 | 0.79 | +14.7 | +14.5 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 40.0% | 40.0% | 20.0% | +0.5 | 1.07 | 1.07 | +15.0 | +19.8 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 42.9% | -2.8 | 0.78 | 3.11 | +20.1 | +11.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -25.4 | 0.00 | 0.00 | +8.3 | +14.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 37.5% | -4.6 | 0.65 | 3.24 | +17.6 | +13.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.3 | 1.03 | 1.72 | +19.0 | +13.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=-26.0; validation N=5 Fav=40.0% Avg=+9.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 40.0% | -6.7 | 0.57 | 0.71 | +18.4 | +8.9 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 33.3% | 44.4% | 44.4% | -6.4 | 0.60 | 0.60 | +20.2 | +8.4 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 33.3% | 44.4% | 44.4% | -6.4 | 0.60 | 0.60 | +20.2 | +8.4 |
| `stop_hunt_le_90` | 7 | S_STRANGER | 70.0% | 28.6% | 42.9% | 42.9% | -13.0 | 0.32 | 0.32 | +18.7 | +6.1 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 40.0% | -6.7 | 0.57 | 0.71 | +18.4 | +8.9 |
| `confluence_gte_60` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 100.0% | +5.1 | 999.00 | 999.00 | +30.5 | +3.3 |
| `confluence_gte_70` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +10.2 | 999.00 | 999.00 | +40.5 | +3.3 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 25.0% | 37.5% | 25.0% | -11.6 | 0.40 | 0.66 | +13.9 | +9.4 |
| `tdi_rsi_gte_50` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 33.3% | 44.4% | 44.4% | -6.4 | 0.60 | 0.60 | +20.2 | +8.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 70.0% | 28.6% | 42.9% | 28.6% | -11.9 | 0.42 | 0.56 | +15.6 | +8.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 70.0% | 28.6% | 42.9% | 42.9% | -13.0 | 0.32 | 0.32 | +18.7 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 40.0% | -6.7 | 0.57 | 0.71 | +18.4 | +8.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=50.0% Avg=-25.0; out_of_sample N=3 Fav=33.3% Avg=-7.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | -18.9 | 0.32 | 0.58 | +19.7 | +28.4 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 27.8% | 27.8% | 33.3% | -19.6 | 0.33 | 0.65 | +20.4 | +28.3 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | -18.9 | 0.32 | 0.58 | +19.7 | +28.4 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 85.0% | 29.4% | 29.4% | 35.3% | -14.4 | 0.41 | 0.74 | +22.0 | +31.9 |
| `asian_range_gte_30` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | -18.9 | 0.32 | 0.58 | +19.7 | +28.4 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | -18.9 | 0.32 | 0.58 | +19.7 | +28.4 |
| `confluence_gte_70` | 2 | R_REPEATER | 10.0% | 50.0% | 50.0% | 0.0% | -1.9 | 0.52 | 0.52 | +11.6 | +22.3 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 65.0% | 15.4% | 15.4% | 30.8% | -21.7 | 0.17 | 0.67 | +15.1 | +18.9 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 45.0% | 44.4% | 44.4% | 22.2% | -19.0 | 0.35 | 0.35 | +25.8 | +42.9 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 90.0% | 27.8% | 27.8% | 33.3% | -19.6 | 0.33 | 0.65 | +20.4 | +28.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 60.0% | 16.7% | 16.7% | 33.3% | -21.0 | 0.18 | 0.65 | +15.6 | +16.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 85.0% | 29.4% | 29.4% | 35.3% | -14.4 | 0.41 | 0.74 | +22.0 | +31.9 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | -18.9 | 0.32 | 0.58 | +19.7 | +28.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=42.9% Avg=-10.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 0.0% | -17.1 | 0.21 | 0.37 | +15.8 | +33.1 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 78.6% | 27.3% | 36.4% | 0.0% | -8.5 | 0.39 | 0.68 | +17.5 | +24.4 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 30.8% | 38.5% | 0.0% | -8.4 | 0.36 | 0.58 | +16.0 | +24.5 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 85.7% | 25.0% | 33.3% | 0.0% | -9.3 | 0.35 | 0.70 | +16.5 | +24.7 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 0.0% | -17.1 | 0.21 | 0.37 | +15.8 | +33.1 |
| `confluence_gte_60` | 11 | S_STRANGER | 78.6% | 27.3% | 36.4% | 0.0% | -8.0 | 0.40 | 0.70 | +16.5 | +25.5 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -37.0 | 0.00 | 0.00 | +0.0 | +16.7 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 71.4% | 30.0% | 30.0% | 0.0% | -23.7 | 0.06 | 0.15 | +15.9 | +37.7 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 50.0% | 42.9% | 42.9% | 0.0% | -10.1 | 0.18 | 0.24 | +18.7 | +26.9 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 78.6% | 27.3% | 36.4% | 0.0% | -8.5 | 0.39 | 0.68 | +17.5 | +24.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 50.0% | 28.6% | 28.6% | 0.0% | -12.9 | 0.13 | 0.32 | +18.5 | +25.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 85.7% | 25.0% | 33.3% | 0.0% | -9.3 | 0.35 | 0.70 | +16.5 | +24.7 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 0.0% | -17.1 | 0.21 | 0.37 | +15.8 | +33.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=12 Fav=33.3% Avg=-20.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -26.5 | 0.30 | 0.74 | +23.8 | +46.4 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 78.6% | 27.3% | 27.3% | 0.0% | -32.1 | 0.17 | 0.46 | +21.0 | +46.4 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 85.7% | 25.0% | 25.0% | 0.0% | -35.9 | 0.14 | 0.43 | +20.2 | +49.8 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 85.7% | 33.3% | 33.3% | 8.3% | -20.5 | 0.39 | 0.78 | +26.7 | +46.7 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -26.5 | 0.30 | 0.74 | +23.8 | +46.4 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -26.5 | 0.30 | 0.74 | +23.8 | +46.4 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -26.5 | 0.30 | 0.74 | +23.8 | +46.4 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 0.0% | -60.7 | 0.09 | 0.37 | +14.0 | +69.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 0.0% | -48.0 | 0.00 | 0.03 | +17.4 | +61.7 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 78.6% | 27.3% | 27.3% | 0.0% | -32.1 | 0.17 | 0.46 | +21.0 | +46.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 0.0% | -67.8 | 0.13 | 0.27 | +18.6 | +74.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 85.7% | 33.3% | 33.3% | 8.3% | -20.5 | 0.39 | 0.78 | +26.7 | +46.7 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -26.5 | 0.30 | 0.74 | +23.8 | +46.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=66.7% Avg=+24.6; out_of_sample N=3 Fav=66.7% Avg=+12.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -5.6 | 0.61 | 1.47 | +20.7 | +22.9 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 94.4% | 23.5% | 23.5% | 11.8% | -7.5 | 0.51 | 1.53 | +19.3 | +23.5 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 94.4% | 23.5% | 23.5% | 11.8% | -7.5 | 0.51 | 1.53 | +19.3 | +23.5 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 88.9% | 25.0% | 25.0% | 12.5% | -7.0 | 0.54 | 1.49 | +19.4 | +23.2 |
| `asian_range_gte_30` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -5.6 | 0.61 | 1.47 | +20.7 | +22.9 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -5.6 | 0.61 | 1.47 | +20.7 | +22.9 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -5.6 | 0.61 | 1.47 | +20.7 | +22.9 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 88.9% | 31.2% | 31.2% | 6.2% | -5.7 | 0.63 | 1.39 | +21.0 | +24.2 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 33.3% | 66.7% | 66.7% | 16.7% | +18.8 | 4.18 | 2.09 | +44.1 | +20.3 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 94.4% | 23.5% | 23.5% | 11.8% | -7.5 | 0.51 | 1.53 | +19.3 | +23.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 83.3% | 26.7% | 26.7% | 6.7% | -7.9 | 0.53 | 1.45 | +19.4 | +25.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 88.9% | 25.0% | 25.0% | 12.5% | -7.0 | 0.54 | 1.49 | +19.4 | +23.2 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -5.6 | 0.61 | 1.47 | +20.7 | +22.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=25.0% Avg=-8.3; out_of_sample N=3 Fav=33.3% Avg=+7.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 0.0% | -4.1 | 0.66 | 1.16 | +23.8 | +24.2 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 0.0% | -4.1 | 0.66 | 1.16 | +23.8 | +24.2 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 0.0% | -4.1 | 0.66 | 1.16 | +23.8 | +24.2 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 0.0% | -4.1 | 0.66 | 1.16 | +23.8 | +24.2 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 11.1% | 22.2% | 0.0% | -11.9 | 0.20 | 0.69 | +20.1 | +28.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 0.0% | -19.0 | 0.00 | 0.00 | +21.1 | +33.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 0.0% | -4.1 | 0.66 | 1.16 | +23.8 | +24.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=33.3% Avg=-24.5; out_of_sample N=4 Fav=50.0% Avg=-9.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 27.0% | 29.7% | 16.2% | -13.0 | 0.39 | 0.81 | +17.1 | +26.5 |
| `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 67.6% | 28.0% | 28.0% | 16.0% | -9.6 | 0.47 | 1.06 | +17.7 | +27.3 |
| `hunt_to_ar_ratio_le_2_5` | 37 | S_STRANGER | 100.0% | 27.0% | 29.7% | 16.2% | -13.0 | 0.39 | 0.81 | +17.1 | +26.5 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 73.0% | 29.6% | 33.3% | 22.2% | -7.1 | 0.58 | 0.96 | +19.5 | +28.9 |
| `asian_range_gte_30` | 37 | S_STRANGER | 100.0% | 27.0% | 29.7% | 16.2% | -13.0 | 0.39 | 0.81 | +17.1 | +26.5 |
| `confluence_gte_60` | 31 | S_STRANGER | 83.8% | 25.8% | 29.0% | 16.1% | -15.9 | 0.29 | 0.61 | +15.8 | +25.7 |
| `confluence_gte_70` | 6 | S_STRANGER | 16.2% | 16.7% | 16.7% | 16.7% | -17.0 | 0.06 | 0.25 | +16.0 | +34.9 |
| `tdi_rsi_gt_signal` | 29 | S_STRANGER | 78.4% | 27.6% | 27.6% | 13.8% | -14.8 | 0.36 | 0.86 | +17.4 | +28.3 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 27.0% | 40.0% | 40.0% | 0.0% | -18.6 | 0.30 | 0.45 | +18.7 | +42.8 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 67.6% | 28.0% | 28.0% | 16.0% | -9.6 | 0.47 | 1.06 | +17.7 | +27.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 20 | S_STRANGER | 54.1% | 25.0% | 25.0% | 15.0% | -11.0 | 0.41 | 1.06 | +17.3 | +27.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 73.0% | 29.6% | 33.3% | 22.2% | -7.1 | 0.58 | 0.96 | +19.5 | +28.9 |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 27.0% | 29.7% | 16.2% | -13.0 | 0.39 | 0.81 | +17.1 | +26.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=0.0% Avg=-13.5; out_of_sample N=5 Fav=40.0% Avg=-4.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -10.1 | 0.34 | 1.01 | +18.2 | +20.5 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 33.3% | -7.2 | 0.44 | 1.11 | +19.0 | +16.2 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -10.1 | 0.34 | 1.01 | +18.2 | +20.5 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 25.0% | -8.1 | 0.44 | 1.11 | +16.8 | +17.1 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -10.1 | 0.34 | 1.01 | +18.2 | +20.5 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -10.1 | 0.34 | 1.01 | +18.2 | +20.5 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -10.1 | 0.34 | 1.01 | +18.2 | +20.5 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | -3.8 | 0.80 | 1.60 | +21.6 | +23.8 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 25.0% | -10.1 | 0.39 | 0.97 | +18.7 | +24.4 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 33.3% | -7.2 | 0.44 | 1.11 | +19.0 | +16.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +12.5 | 2.24 | 2.24 | +26.7 | +6.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 25.0% | -8.1 | 0.44 | 1.11 | +16.8 | +17.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -10.1 | 0.34 | 1.01 | +18.2 | +20.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-44.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=30.0% Avg=-8.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -17.1 | 0.21 | 0.75 | +17.8 | +23.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 86.7% | 23.1% | 23.1% | 23.1% | -13.2 | 0.28 | 0.84 | +16.2 | +19.2 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -17.1 | 0.21 | 0.75 | +17.8 | +23.1 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 86.7% | 23.1% | 23.1% | 23.1% | -13.2 | 0.28 | 0.84 | +16.2 | +19.2 |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -17.1 | 0.21 | 0.75 | +17.8 | +23.1 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -17.1 | 0.21 | 0.75 | +17.8 | +23.1 |
| `confluence_gte_70` | 5 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -39.6 | 0.00 | 0.00 | +10.8 | +48.4 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 86.7% | 23.1% | 23.1% | 23.1% | -16.6 | 0.23 | 0.70 | +20.0 | +24.9 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -44.5 | 0.14 | 0.27 | +26.6 | +66.3 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 86.7% | 23.1% | 23.1% | 23.1% | -13.2 | 0.28 | 0.84 | +16.2 | +19.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 73.3% | 27.3% | 27.3% | 27.3% | -12.0 | 0.33 | 0.78 | +18.5 | +20.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 86.7% | 23.1% | 23.1% | 23.1% | -13.2 | 0.28 | 0.84 | +16.2 | +19.2 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -17.1 | 0.21 | 0.75 | +17.8 | +23.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=17 Fav=29.4% Avg=-10.8; out_of_sample N=8 Fav=0.0% Avg=-22.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 18.5% | 22.2% | 3.7% | -13.8 | 0.20 | 0.69 | +12.6 | +28.4 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 81.5% | 18.2% | 22.7% | 4.5% | -14.3 | 0.16 | 0.54 | +11.5 | +27.5 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 92.6% | 20.0% | 24.0% | 4.0% | -14.7 | 0.20 | 0.63 | +11.8 | +28.0 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 81.5% | 18.2% | 22.7% | 4.5% | -15.8 | 0.15 | 0.49 | +11.5 | +28.9 |
| `asian_range_gte_30` | 27 | S_STRANGER | 100.0% | 18.5% | 22.2% | 3.7% | -13.8 | 0.20 | 0.69 | +12.6 | +28.4 |
| `confluence_gte_60` | 27 | S_STRANGER | 100.0% | 18.5% | 22.2% | 3.7% | -13.8 | 0.20 | 0.69 | +12.6 | +28.4 |
| `confluence_gte_70` | 27 | S_STRANGER | 100.0% | 18.5% | 22.2% | 3.7% | -13.8 | 0.20 | 0.69 | +12.6 | +28.4 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 44.4% | 8.3% | 8.3% | 0.0% | -18.6 | 0.04 | 0.41 | +8.8 | +33.9 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 48.1% | 7.7% | 7.7% | 0.0% | -23.2 | 0.03 | 0.34 | +10.1 | +40.1 |
| `ratio_le_2_and_asian_gte_30` | 22 | S_STRANGER | 81.5% | 18.2% | 22.7% | 4.5% | -14.3 | 0.16 | 0.54 | +11.5 | +27.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 37.0% | 10.0% | 10.0% | 0.0% | -17.6 | 0.05 | 0.42 | +8.1 | +32.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 81.5% | 18.2% | 22.7% | 4.5% | -15.8 | 0.15 | 0.49 | +11.5 | +28.9 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 18.5% | 22.2% | 3.7% | -13.8 | 0.20 | 0.69 | +12.6 | +28.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+5.2; validation N=2 Fav=50.0% Avg=+6.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -5.8 | 0.51 | 1.92 | +15.2 | +15.7 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 95.5% | 19.0% | 19.0% | 28.6% | -5.2 | 0.55 | 1.92 | +15.8 | +16.1 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -5.8 | 0.51 | 1.92 | +15.2 | +15.7 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 86.4% | 15.8% | 15.8% | 21.1% | -8.6 | 0.37 | 1.72 | +13.4 | +17.3 |
| `asian_range_gte_30` | 22 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -5.8 | 0.51 | 1.92 | +15.2 | +15.7 |
| `confluence_gte_60` | 15 | S_STRANGER | 68.2% | 20.0% | 20.0% | 26.7% | -4.4 | 0.55 | 1.82 | +14.0 | +14.0 |
| `confluence_gte_70` | 1 | S_STRANGER | 4.5% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +8.1 | +10.7 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 77.3% | 17.6% | 17.6% | 23.5% | -7.9 | 0.41 | 1.66 | +15.5 | +18.4 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 40.9% | 33.3% | 33.3% | 22.2% | +5.5 | 1.86 | 3.72 | +21.0 | +20.5 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 95.5% | 19.0% | 19.0% | 28.6% | -5.2 | 0.55 | 1.92 | +15.8 | +16.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 77.3% | 17.6% | 17.6% | 23.5% | -7.9 | 0.41 | 1.66 | +15.5 | +18.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 86.4% | 15.8% | 15.8% | 21.1% | -8.6 | 0.37 | 1.72 | +13.4 | +17.3 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -5.8 | 0.51 | 1.92 | +15.2 | +15.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=16.7% Avg=-3.9; validation N=6 Fav=16.7% Avg=-5.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 16.7% | 22.2% | 27.8% | -4.6 | 0.55 | 1.38 | +15.9 | +16.7 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 100.0% | 16.7% | 22.2% | 27.8% | -4.6 | 0.55 | 1.38 | +15.9 | +16.7 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 16.7% | 22.2% | 27.8% | -4.6 | 0.55 | 1.38 | +15.9 | +16.7 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 16.7% | 22.2% | 27.8% | -4.6 | 0.55 | 1.38 | +15.9 | +16.7 |
| `asian_range_gte_30` | 18 | S_STRANGER | 100.0% | 16.7% | 22.2% | 27.8% | -4.6 | 0.55 | 1.38 | +15.9 | +16.7 |
| `confluence_gte_60` | 6 | S_STRANGER | 33.3% | 0.0% | 16.7% | 16.7% | -15.1 | 0.17 | 0.66 | +14.7 | +7.7 |
| `confluence_gte_70` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -13.3 | 0.00 | 0.00 | +7.6 | +16.9 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 72.2% | 7.7% | 15.4% | 23.1% | -6.2 | 0.42 | 1.67 | +16.4 | +18.5 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -9.2 | 0.00 | 0.00 | +12.0 | +18.5 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 100.0% | 16.7% | 22.2% | 27.8% | -4.6 | 0.55 | 1.38 | +15.9 | +16.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 72.2% | 7.7% | 15.4% | 23.1% | -6.2 | 0.42 | 1.67 | +16.4 | +18.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 16.7% | 22.2% | 27.8% | -4.6 | 0.55 | 1.38 | +15.9 | +16.7 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 16.7% | 22.2% | 27.8% | -4.6 | 0.55 | 1.38 | +15.9 | +16.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=16.7% Avg=-14.3; out_of_sample N=5 Fav=20.0% Avg=+9.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -7.0 | 0.54 | 1.89 | +18.2 | +28.1 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 94.7% | 16.7% | 22.2% | 11.1% | -6.5 | 0.57 | 1.86 | +19.2 | +25.6 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -7.0 | 0.54 | 1.89 | +18.2 | +28.1 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 89.5% | 17.6% | 23.5% | 11.8% | -4.0 | 0.69 | 2.08 | +19.6 | +23.7 |
| `asian_range_gte_30` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -7.0 | 0.54 | 1.89 | +18.2 | +28.1 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -7.0 | 0.54 | 1.89 | +18.2 | +28.1 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -7.0 | 0.54 | 1.89 | +18.2 | +28.1 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 68.4% | 15.4% | 15.4% | 7.7% | -12.3 | 0.35 | 1.73 | +15.2 | +33.4 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 57.9% | 18.2% | 18.2% | 9.1% | -3.7 | 0.68 | 2.71 | +19.4 | +32.7 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 94.7% | 16.7% | 22.2% | 11.1% | -6.5 | 0.57 | 1.86 | +19.2 | +25.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 63.2% | 16.7% | 16.7% | 8.3% | -12.0 | 0.37 | 1.67 | +16.4 | +30.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 89.5% | 17.6% | 23.5% | 11.8% | -4.0 | 0.69 | 2.08 | +19.6 | +23.7 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -7.0 | 0.54 | 1.89 | +18.2 | +28.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+49.5; validation N=7 Fav=14.3% Avg=+5.3; out_of_sample N=2 Fav=0.0% Avg=-19.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 23.1% | +0.9 | 1.08 | 2.88 | +20.2 | +17.5 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 23.1% | +0.9 | 1.08 | 2.88 | +20.2 | +17.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 23.1% | +0.9 | 1.08 | 2.88 | +20.2 | +17.5 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 23.1% | +0.9 | 1.08 | 2.88 | +20.2 | +17.5 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 23.1% | +0.9 | 1.08 | 2.88 | +20.2 | +17.5 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 23.1% | +0.9 | 1.08 | 2.88 | +20.2 | +17.5 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 23.1% | +0.9 | 1.08 | 2.88 | +20.2 | +17.5 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 76.9% | 20.0% | 20.0% | 30.0% | +4.8 | 1.47 | 4.40 | +25.4 | +18.8 |
| `tdi_rsi_gte_50` | 3 | R_REPEATER | 23.1% | 66.7% | 66.7% | 33.3% | +41.1 | 5.37 | 2.69 | +55.4 | +32.4 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 23.1% | +0.9 | 1.08 | 2.88 | +20.2 | +17.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 76.9% | 20.0% | 20.0% | 30.0% | +4.8 | 1.47 | 4.40 | +25.4 | +18.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 23.1% | +0.9 | 1.08 | 2.88 | +20.2 | +17.5 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 23.1% | +0.9 | 1.08 | 2.88 | +20.2 | +17.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=13 Fav=15.4% Avg=-11.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 7.7% | -11.0 | 0.28 | 0.62 | +18.3 | +22.6 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 84.6% | 9.1% | 27.3% | 9.1% | -13.0 | 0.22 | 0.58 | +13.9 | +21.2 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 7.7% | -11.0 | 0.28 | 0.62 | +18.3 | +22.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 84.6% | 9.1% | 27.3% | 9.1% | -13.0 | 0.22 | 0.58 | +13.9 | +21.2 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 7.7% | -11.0 | 0.28 | 0.62 | +18.3 | +22.6 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 7.7% | -11.0 | 0.28 | 0.62 | +18.3 | +22.6 |
| `confluence_gte_70` | 4 | S_STRANGER | 30.8% | 0.0% | 50.0% | 0.0% | -3.0 | 0.44 | 0.44 | +21.8 | +15.6 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 53.8% | 0.0% | 28.6% | 0.0% | -19.6 | 0.06 | 0.16 | +9.5 | +24.7 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -25.2 | 0.00 | 0.00 | +19.9 | +32.9 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 84.6% | 9.1% | 27.3% | 9.1% | -13.0 | 0.22 | 0.58 | +13.9 | +21.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 53.8% | 0.0% | 28.6% | 0.0% | -19.6 | 0.06 | 0.16 | +9.5 | +24.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 84.6% | 9.1% | 27.3% | 9.1% | -13.0 | 0.22 | 0.58 | +13.9 | +21.2 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 7.7% | -11.0 | 0.28 | 0.62 | +18.3 | +22.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=0.0% Avg=-5.0; out_of_sample N=5 Fav=40.0% Avg=+0.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 28.6% | -18.1 | 0.19 | 0.95 | +12.2 | +12.6 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 28.6% | -18.1 | 0.19 | 0.95 | +12.2 | +12.6 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 28.6% | -18.1 | 0.19 | 0.95 | +12.2 | +12.6 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 57.1% | 25.0% | 25.0% | 37.5% | -1.7 | 0.81 | 2.03 | +14.7 | +17.5 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 28.6% | -18.1 | 0.19 | 0.95 | +12.2 | +12.6 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 28.6% | -18.1 | 0.19 | 0.95 | +12.2 | +12.6 |
| `confluence_gte_70` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -37.0 | 0.00 | 0.00 | +2.8 | +10.0 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 25.0% | -14.5 | 0.26 | 1.15 | +11.0 | +13.9 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -39.0 | 0.00 | 0.00 | +15.5 | +45.6 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 28.6% | -18.1 | 0.19 | 0.95 | +12.2 | +12.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 25.0% | -14.5 | 0.26 | 1.15 | +11.0 | +13.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 57.1% | 25.0% | 25.0% | 37.5% | -1.7 | 0.81 | 2.03 | +14.7 | +17.5 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 28.6% | -18.1 | 0.19 | 0.95 | +12.2 | +12.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=22.2% Avg=-9.4; validation N=5 Fav=0.0% Avg=-21.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 11.1% | -13.1 | 0.18 | 0.53 | +13.2 | +14.4 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 77.8% | 14.3% | 28.6% | 14.3% | -13.7 | 0.21 | 0.42 | +15.3 | +14.8 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 11.1% | -13.1 | 0.18 | 0.53 | +13.2 | +14.4 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 94.4% | 11.8% | 23.5% | 11.8% | -13.8 | 0.18 | 0.49 | +13.4 | +13.5 |
| `asian_range_gte_30` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 11.1% | -13.1 | 0.18 | 0.53 | +13.2 | +14.4 |
| `confluence_gte_60` | 9 | S_STRANGER | 50.0% | 11.1% | 33.3% | 0.0% | -16.7 | 0.20 | 0.39 | +12.8 | +15.3 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 0.0% | -6.9 | 0.44 | 0.89 | +22.3 | +18.9 |
| `tdi_rsi_gte_50` | 4 | R_REPEATER | 22.2% | 50.0% | 50.0% | 0.0% | -3.7 | 0.67 | 0.67 | +23.5 | +21.3 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 77.8% | 14.3% | 28.6% | 14.3% | -13.7 | 0.21 | 0.42 | +15.3 | +14.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 11.1% | 50.0% | 50.0% | 0.0% | -3.3 | 0.71 | 0.71 | +31.8 | +20.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 94.4% | 11.8% | 23.5% | 11.8% | -13.8 | 0.18 | 0.49 | +13.4 | +13.5 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 11.1% | -13.1 | 0.18 | 0.53 | +13.2 | +14.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=16.7% Avg=-7.4; out_of_sample N=2 Fav=0.0% Avg=-7.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -16.0 | 0.14 | 0.95 | +15.2 | +14.5 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 11.1% | -17.8 | 0.14 | 0.95 | +14.5 | +14.7 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -16.0 | 0.14 | 0.95 | +15.2 | +14.5 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 25.0% | -7.5 | 0.30 | 1.49 | +16.9 | +10.5 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -16.0 | 0.14 | 0.95 | +15.2 | +14.5 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -16.0 | 0.14 | 0.95 | +15.2 | +14.5 |
| `confluence_gte_70` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +8.9 | +4.3 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -54.1 | 0.00 | 0.00 | +4.7 | +2.3 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -21.4 | 0.00 | 0.00 | +18.8 | +33.4 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 11.1% | -17.8 | 0.14 | 0.95 | +14.5 | +14.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -54.1 | 0.00 | 0.00 | +4.7 | +2.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 25.0% | -7.5 | 0.30 | 1.49 | +16.9 | +10.5 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -16.0 | 0.14 | 0.95 | +15.2 | +14.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-34.8; validation N=8 Fav=12.5% Avg=-13.5; out_of_sample N=2 Fav=0.0% Avg=-20.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 5.3% | 5.3% | 5.3% | -20.5 | 0.09 | 1.53 | +12.1 | +31.3 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 94.7% | 5.6% | 5.6% | 5.6% | -20.7 | 0.09 | 1.50 | +12.2 | +31.2 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 5.3% | 5.3% | 5.3% | -20.5 | 0.09 | 1.53 | +12.1 | +31.3 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 94.7% | 5.6% | 5.6% | 5.6% | -20.6 | 0.09 | 1.51 | +12.5 | +32.8 |
| `asian_range_gte_30` | 19 | S_STRANGER | 100.0% | 5.3% | 5.3% | 5.3% | -20.5 | 0.09 | 1.53 | +12.1 | +31.3 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 5.3% | 5.3% | 5.3% | -20.5 | 0.09 | 1.53 | +12.1 | +31.3 |
| `confluence_gte_70` | 11 | S_STRANGER | 57.9% | 9.1% | 9.1% | 0.0% | -16.6 | 0.17 | 1.75 | +10.3 | +32.6 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 47.4% | 0.0% | 0.0% | 11.1% | -29.4 | 0.00 | 0.00 | +15.4 | +42.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 47.4% | 0.0% | 0.0% | 11.1% | -26.3 | 0.00 | 0.00 | +14.0 | +38.9 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 94.7% | 5.6% | 5.6% | 5.6% | -20.7 | 0.09 | 1.50 | +12.2 | +31.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 42.1% | 0.0% | 0.0% | 12.5% | -30.9 | 0.00 | 0.00 | +15.9 | +43.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 94.7% | 5.6% | 5.6% | 5.6% | -20.6 | 0.09 | 1.51 | +12.5 | +32.8 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 5.3% | 5.3% | 5.3% | -20.5 | 0.09 | 1.53 | +12.1 | +31.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=0.0% Avg=-9.8; out_of_sample N=1 Fav=0.0% Avg=-27.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +17.6 | +32.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 0.0% | 0.0% | 0.0% | -13.7 | 0.00 | 0.00 | +17.8 | +31.8 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +17.6 | +32.5 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +17.6 | +32.5 |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +17.6 | +32.5 |
| `confluence_gte_60` | 8 | S_STRANGER | 72.7% | 0.0% | 0.0% | 0.0% | -12.0 | 0.00 | 0.00 | +13.3 | +31.4 |
| `confluence_gte_70` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -14.6 | 0.00 | 0.00 | +11.4 | +36.9 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -16.9 | 0.00 | 0.00 | +19.2 | +34.6 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -14.3 | 0.00 | 0.00 | +24.8 | +37.1 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 90.9% | 0.0% | 0.0% | 0.0% | -13.7 | 0.00 | 0.00 | +17.8 | +31.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -16.9 | 0.00 | 0.00 | +19.2 | +34.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +17.6 | +32.5 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +17.6 | +32.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=0.0% Avg=-38.2; out_of_sample N=2 Fav=0.0% Avg=-10.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -34.8 | 0.00 | 0.00 | +8.1 | +19.8 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 72.7% | 0.0% | 0.0% | 0.0% | -31.2 | 0.00 | 0.00 | +9.3 | +24.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -34.8 | 0.00 | 0.00 | +8.1 | +19.8 |
| `stop_hunt_le_90` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 0.0% | -38.4 | 0.00 | 0.00 | +10.0 | +14.8 |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -34.8 | 0.00 | 0.00 | +8.1 | +19.8 |
| `confluence_gte_60` | 10 | S_STRANGER | 90.9% | 0.0% | 0.0% | 0.0% | -31.5 | 0.00 | 0.00 | +8.1 | +14.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -47.4 | 0.00 | 0.00 | +16.8 | +20.1 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -36.6 | 0.00 | 0.00 | +26.7 | +38.0 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 72.7% | 0.0% | 0.0% | 0.0% | -31.2 | 0.00 | 0.00 | +9.3 | +24.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -36.6 | 0.00 | 0.00 | +26.7 | +38.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 0.0% | -38.4 | 0.00 | 0.00 | +10.0 | +14.8 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -34.8 | 0.00 | 0.00 | +8.1 | +19.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
