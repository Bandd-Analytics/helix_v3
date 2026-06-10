# GBPAUD Pair Feature Ablation

Generated: 2026-06-09T15:36:24.918158+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 26 | R_REPEATER | 61.5% | +19.8 | `tdi_rsi_gte_50` | 7 | R_REPEATER | 71.4% | +28.6 | 999.00 | 999.00 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 15 | R_REPEATER | 60.0% | +13.4 | `confluence_gte_60` | 10 | R_RUNNER | 80.0% | +21.5 | 13.64 | 3.41 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 30 | R_REPEATER | 56.7% | +12.8 | `confluence_gte_70` | 6 | R_REPEATER | 66.7% | +7.5 | 3.72 | 0.93 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 30 | R_REPEATER | 56.7% | +12.7 | `stop_hunt_le_90` | 28 | R_REPEATER | 57.1% | +14.3 | 3.77 | 2.59 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 46 | R_REPEATER | 56.5% | +9.0 | `tdi_rsi_gt_signal` | 20 | R_REPEATER | 65.0% | +15.7 | 5.26 | 2.43 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 33 | R_REPEATER | 54.5% | +5.4 | `confluence_gte_70` | 9 | R_REPEATER | 55.6% | +13.0 | 7.08 | 5.67 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 13 | R_REPEATER | 53.8% | +8.9 | `tdi_rsi_gt_signal` | 7 | R_REPEATER | 57.1% | +3.1 | 1.21 | 0.90 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 13 | R_REPEATER | 53.8% | -2.3 | `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 58.3% | +0.7 | 1.07 | 0.76 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | R_REPEATER | 50.0% | +9.8 | `tdi_rsi_gte_50` | 7 | R_REPEATER | 71.4% | +19.1 | 12.74 | 5.09 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 14 | R_REPEATER | 50.0% | +9.4 | `tdi_rsi_gte_50` | 8 | R_REPEATER | 50.0% | +15.1 | 4.64 | 4.64 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 16 | R_REPEATER | 50.0% | +5.2 | `all` | 16 | R_REPEATER | 50.0% | +5.2 | 1.58 | 0.98 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 35 | S_STRANGER | 45.7% | +8.4 | `tdi_rsi_gte_50` | 15 | R_REPEATER | 53.3% | +4.4 | 1.41 | 0.78 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 20 | S_STRANGER | 45.0% | +3.7 | `confluence_gte_70` | 5 | R_REPEATER | 60.0% | +9.6 | 3.61 | 2.41 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 43.8% | +3.1 | `tdi_rsi_gte_50` | 7 | R_RUNNER | 85.7% | +15.1 | 2.04 | 0.34 | 1 | 1 | research_only_split_fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 35 | S_STRANGER | 42.9% | -1.2 | `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 43.3% | +1.5 | 1.21 | 1.40 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 41.2% | -1.4 | `tdi_rsi_gte_50` | 7 | R_REPEATER | 71.4% | +11.7 | 3.13 | 1.25 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 40.0% | -3.9 | `tdi_rsi_gt_signal` | 5 | R_REPEATER | 60.0% | +1.2 | 1.17 | 0.78 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 38.9% | +5.8 | `stop_hunt_le_90` | 15 | S_STRANGER | 46.7% | +8.7 | 2.64 | 3.02 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 42 | S_STRANGER | 38.1% | +3.7 | `hunt_to_ar_ratio_le_2_5` | 38 | S_STRANGER | 39.5% | +5.3 | 2.13 | 2.99 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 22 | S_STRANGER | 36.4% | -1.0 | `confluence_gte_70` | 5 | R_REPEATER | 60.0% | +4.0 | 1.31 | 0.87 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 36.4% | -1.9 | `tdi_rsi_gte_50` | 8 | R_REPEATER | 50.0% | +6.0 | 1.86 | 1.86 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 26 | S_STRANGER | 34.6% | -2.8 | `tdi_rsi_gt_signal` | 21 | S_STRANGER | 42.9% | +2.2 | 1.31 | 1.75 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 35 | S_STRANGER | 34.3% | -0.4 | `confluence_gte_70` | 7 | S_STRANGER | 42.9% | +4.8 | 3.16 | 3.16 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 21 | S_STRANGER | 33.3% | -0.9 | `tdi_rsi_gt_signal` | 10 | R_REPEATER | 50.0% | +4.9 | 2.28 | 1.37 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 33.3% | -12.2 | `stop_hunt_le_90` | 8 | S_STRANGER | 37.5% | -15.5 | 0.33 | 0.55 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 16 | S_STRANGER | 31.2% | -8.0 | `confluence_gte_70` | 6 | R_REPEATER | 50.0% | +5.9 | 1.79 | 1.79 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 30.8% | -8.1 | `stop_hunt_le_90` | 11 | S_STRANGER | 36.4% | -7.7 | 0.52 | 0.92 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | -0.5 | `stop_hunt_le_90` | 8 | S_STRANGER | 37.5% | +2.3 | 1.30 | 1.30 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | -3.9 | `confluence_gte_70` | 9 | S_STRANGER | 33.3% | -3.6 | 0.70 | 1.41 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 20 | S_STRANGER | 30.0% | -9.4 | `confluence_gte_60` | 14 | S_STRANGER | 35.7% | -3.1 | 0.80 | 1.12 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 24 | S_STRANGER | 29.2% | -3.5 | `confluence_gte_70` | 7 | S_STRANGER | 42.9% | -4.1 | 0.26 | 0.26 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 28.6% | -2.4 | `confluence_gte_60` | 11 | S_STRANGER | 36.4% | +0.9 | 1.24 | 2.17 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 14 | S_STRANGER | 28.6% | -3.5 | `confluence_gte_60` | 11 | S_STRANGER | 36.4% | -3.2 | 0.73 | 1.27 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 14 | S_STRANGER | 28.6% | -15.3 | `tdi_rsi_gt_signal` | 10 | S_STRANGER | 30.0% | -22.0 | 0.12 | 0.29 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | -6.6 | `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 30.0% | -5.5 | 0.65 | 0.98 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 25.0% | -5.2 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | -0.2 | 0.99 | 0.99 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 23.1% | -3.6 | `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 25.0% | -3.2 | 0.72 | 2.15 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 22 | S_STRANGER | 22.7% | -17.7 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 40.0% | -13.4 | 0.48 | 0.72 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | -5.2 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 37.5% | -3.8 | 0.39 | 0.51 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | -24.4 | `all` | 14 | S_STRANGER | 21.4% | -24.4 | 0.13 | 0.48 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -8.4 | `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 28.6% | -4.3 | 0.49 | 0.65 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -8.3 | `confluence_gte_60` | 7 | S_STRANGER | 28.6% | -0.9 | 0.83 | 1.66 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 24 | S_STRANGER | 16.7% | +0.4 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 25.0% | +7.1 | 2.57 | 4.29 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 16.7% | -9.4 | `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 17.6% | -7.2 | 0.53 | 1.16 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 13.3% | -20.2 | `stop_hunt_le_90` | 13 | S_STRANGER | 15.4% | -13.4 | 0.10 | 0.57 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 16 | S_STRANGER | 6.2% | -7.9 | `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 10.0% | -8.6 | 0.43 | 1.73 | 0 | 0 | fail |

## Candidate Details

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+25.2; validation N=2 Fav=100.0% Avg=+37.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | R_REPEATER | 100.0% | 61.5% | 65.4% | 42.3% | +19.8 | 6.33 | 2.23 | +39.8 | +9.4 |
| `hunt_to_ar_ratio_le_2_0` | 23 | R_REPEATER | 88.5% | 56.5% | 60.9% | 39.1% | +16.5 | 4.93 | 2.11 | +33.5 | +9.6 |
| `hunt_to_ar_ratio_le_2_5` | 25 | R_REPEATER | 96.2% | 60.0% | 64.0% | 40.0% | +19.4 | 6.01 | 2.25 | +38.9 | +9.8 |
| `stop_hunt_le_90` | 24 | R_REPEATER | 92.3% | 58.3% | 62.5% | 37.5% | +18.8 | 5.68 | 2.27 | +36.9 | +10.2 |
| `asian_range_gte_30` | 26 | R_REPEATER | 100.0% | 61.5% | 65.4% | 42.3% | +19.8 | 6.33 | 2.23 | +39.8 | +9.4 |
| `confluence_gte_60` | 18 | R_REPEATER | 69.2% | 66.7% | 72.2% | 55.6% | +25.0 | 30.25 | 4.65 | +44.8 | +8.4 |
| `confluence_gte_70` | 3 | R_REPEATER | 11.5% | 66.7% | 66.7% | 100.0% | +24.8 | 999.00 | 999.00 | +52.9 | +5.6 |
| `tdi_rsi_gt_signal` | 23 | R_REPEATER | 88.5% | 60.9% | 65.2% | 39.1% | +18.0 | 5.37 | 1.79 | +39.8 | +10.2 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 26.9% | 71.4% | 71.4% | 57.1% | +28.6 | 999.00 | 999.00 | +53.0 | +10.2 |
| `ratio_le_2_and_asian_gte_30` | 23 | R_REPEATER | 88.5% | 56.5% | 60.9% | 39.1% | +16.5 | 4.93 | 2.11 | +33.5 | +9.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 20 | R_REPEATER | 76.9% | 55.0% | 60.0% | 35.0% | +13.9 | 3.95 | 1.64 | +32.6 | +10.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | R_REPEATER | 92.3% | 58.3% | 62.5% | 37.5% | +18.8 | 5.68 | 2.27 | +36.9 | +10.2 |
| `feature_stale_hod_exhaustion_reject` | 26 | R_REPEATER | 100.0% | 61.5% | 65.4% | 42.3% | +19.8 | 6.33 | 2.23 | +39.8 | +9.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=71.4% Avg=+9.2; validation N=3 Fav=100.0% Avg=+50.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | R_REPEATER | 100.0% | 60.0% | 66.7% | 46.7% | +13.4 | 3.59 | 1.79 | +34.0 | +16.5 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | R_REPEATER | 100.0% | 60.0% | 66.7% | 46.7% | +13.4 | 3.59 | 1.79 | +34.0 | +16.5 |
| `confluence_gte_60` | 10 | R_RUNNER | 66.7% | 80.0% | 80.0% | 60.0% | +21.5 | 13.64 | 3.41 | +38.0 | +14.5 |
| `confluence_gte_70` | 1 | R_RUNNER | 6.7% | 100.0% | 100.0% | 0.0% | +12.2 | 999.00 | 999.00 | +31.9 | +14.6 |
| `tdi_rsi_gt_signal` | 9 | R_REPEATER | 60.0% | 55.6% | 66.7% | 33.3% | +12.2 | 2.83 | 1.42 | +33.7 | +19.5 |
| `tdi_rsi_gte_50` | 8 | R_RUNNER | 53.3% | 75.0% | 75.0% | 50.0% | +14.6 | 2.99 | 1.00 | +37.6 | +20.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | R_REPEATER | 100.0% | 60.0% | 66.7% | 46.7% | +13.4 | 3.59 | 1.79 | +34.0 | +16.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+7.5; validation N=1 Fav=100.0% Avg=+7.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | R_REPEATER | 100.0% | 56.7% | 60.0% | 30.0% | +12.8 | 3.29 | 2.01 | +32.3 | +18.0 |
| `hunt_to_ar_ratio_le_2_0` | 27 | R_REPEATER | 90.0% | 55.6% | 59.3% | 25.9% | +12.1 | 3.34 | 2.09 | +30.6 | +18.3 |
| `hunt_to_ar_ratio_le_2_5` | 29 | R_REPEATER | 96.7% | 55.2% | 58.6% | 27.6% | +12.5 | 3.15 | 2.04 | +32.1 | +18.3 |
| `stop_hunt_le_90` | 27 | R_REPEATER | 90.0% | 55.6% | 59.3% | 25.9% | +12.1 | 3.34 | 2.09 | +30.6 | +18.3 |
| `asian_range_gte_30` | 30 | R_REPEATER | 100.0% | 56.7% | 60.0% | 30.0% | +12.8 | 3.29 | 2.01 | +32.3 | +18.0 |
| `confluence_gte_60` | 20 | R_REPEATER | 66.7% | 55.0% | 55.0% | 30.0% | +7.7 | 2.43 | 1.77 | +27.2 | +19.0 |
| `confluence_gte_70` | 6 | R_REPEATER | 20.0% | 66.7% | 66.7% | 33.3% | +7.5 | 3.72 | 0.93 | +22.2 | +18.8 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 16.7% | 20.0% | 20.0% | 20.0% | -4.1 | 0.59 | 1.78 | +21.8 | +20.3 |
| `tdi_rsi_gte_50` | 20 | R_REPEATER | 66.7% | 50.0% | 50.0% | 20.0% | +8.5 | 2.25 | 2.02 | +29.1 | +23.1 |
| `ratio_le_2_and_asian_gte_30` | 27 | R_REPEATER | 90.0% | 55.6% | 59.3% | 25.9% | +12.1 | 3.34 | 2.09 | +30.6 | +18.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 16.7% | 20.0% | 20.0% | 20.0% | -4.1 | 0.59 | 1.78 | +21.8 | +20.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | R_REPEATER | 90.0% | 55.6% | 59.3% | 25.9% | +12.1 | 3.34 | 2.09 | +30.6 | +18.3 |
| `feature_stale_hod_exhaustion_reject` | 30 | R_REPEATER | 100.0% | 56.7% | 60.0% | 30.0% | +12.8 | 3.29 | 2.01 | +32.3 | +18.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=14 Fav=50.0% Avg=+15.7; validation N=14 Fav=64.3% Avg=+12.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | R_REPEATER | 100.0% | 56.7% | 56.7% | 26.7% | +12.7 | 3.23 | 2.28 | +33.3 | +15.7 |
| `hunt_to_ar_ratio_le_2_0` | 27 | R_REPEATER | 90.0% | 55.6% | 55.6% | 29.6% | +14.4 | 3.67 | 2.69 | +35.3 | +14.4 |
| `hunt_to_ar_ratio_le_2_5` | 29 | R_REPEATER | 96.7% | 55.2% | 55.2% | 27.6% | +12.7 | 3.15 | 2.36 | +33.7 | +16.1 |
| `stop_hunt_le_90` | 28 | R_REPEATER | 93.3% | 57.1% | 57.1% | 28.6% | +14.3 | 3.77 | 2.59 | +34.9 | +13.9 |
| `asian_range_gte_30` | 30 | R_REPEATER | 100.0% | 56.7% | 56.7% | 26.7% | +12.7 | 3.23 | 2.28 | +33.3 | +15.7 |
| `confluence_gte_60` | 30 | R_REPEATER | 100.0% | 56.7% | 56.7% | 26.7% | +12.7 | 3.23 | 2.28 | +33.3 | +15.7 |
| `confluence_gte_70` | 30 | R_REPEATER | 100.0% | 56.7% | 56.7% | 26.7% | +12.7 | 3.23 | 2.28 | +33.3 | +15.7 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 53.3% | 43.8% | 43.8% | 25.0% | -0.5 | 0.95 | 1.08 | +26.7 | +20.9 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 56.7% | 41.2% | 41.2% | 29.4% | +5.8 | 1.86 | 2.39 | +29.0 | +16.6 |
| `ratio_le_2_and_asian_gte_30` | 27 | R_REPEATER | 90.0% | 55.6% | 55.6% | 29.6% | +14.4 | 3.67 | 2.69 | +35.3 | +14.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 46.7% | 42.9% | 42.9% | 28.6% | +0.3 | 1.04 | 1.21 | +28.5 | +20.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | R_REPEATER | 93.3% | 57.1% | 57.1% | 28.6% | +14.3 | 3.77 | 2.59 | +34.9 | +13.9 |
| `feature_stale_hod_exhaustion_reject` | 30 | R_REPEATER | 100.0% | 56.7% | 56.7% | 26.7% | +12.7 | 3.23 | 2.28 | +33.3 | +15.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=60.0% Avg=+12.7; validation N=10 Fav=70.0% Avg=+18.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 46 | R_REPEATER | 100.0% | 56.5% | 56.5% | 34.8% | +9.0 | 2.52 | 1.55 | +28.1 | +14.8 |
| `hunt_to_ar_ratio_le_2_0` | 40 | R_REPEATER | 87.0% | 55.0% | 55.0% | 37.5% | +8.6 | 2.35 | 1.49 | +29.2 | +15.7 |
| `hunt_to_ar_ratio_le_2_5` | 45 | R_REPEATER | 97.8% | 55.6% | 55.6% | 35.6% | +8.9 | 2.47 | 1.58 | +27.9 | +15.0 |
| `stop_hunt_le_90` | 42 | R_REPEATER | 91.3% | 57.1% | 57.1% | 35.7% | +9.0 | 2.48 | 1.44 | +28.7 | +15.7 |
| `asian_range_gte_30` | 46 | R_REPEATER | 100.0% | 56.5% | 56.5% | 34.8% | +9.0 | 2.52 | 1.55 | +28.1 | +14.8 |
| `confluence_gte_60` | 25 | R_REPEATER | 54.3% | 56.0% | 56.0% | 32.0% | +11.6 | 5.37 | 3.45 | +28.6 | +12.4 |
| `confluence_gte_70` | 7 | R_REPEATER | 15.2% | 57.1% | 57.1% | 14.3% | +10.8 | 7.66 | 5.75 | +23.5 | +13.9 |
| `tdi_rsi_gt_signal` | 20 | R_REPEATER | 43.5% | 65.0% | 65.0% | 35.0% | +15.7 | 5.26 | 2.43 | +33.7 | +13.4 |
| `tdi_rsi_gte_50` | 23 | R_REPEATER | 50.0% | 56.5% | 56.5% | 17.4% | +9.4 | 2.32 | 1.61 | +29.7 | +18.3 |
| `ratio_le_2_and_asian_gte_30` | 40 | R_REPEATER | 87.0% | 55.0% | 55.0% | 37.5% | +8.6 | 2.35 | 1.49 | +29.2 | +15.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 16 | R_REPEATER | 34.8% | 62.5% | 62.5% | 37.5% | +16.1 | 5.01 | 2.50 | +35.6 | +15.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 42 | R_REPEATER | 91.3% | 57.1% | 57.1% | 35.7% | +9.0 | 2.48 | 1.44 | +28.7 | +15.7 |
| `feature_stale_hod_exhaustion_reject` | 46 | R_REPEATER | 100.0% | 56.5% | 56.5% | 34.8% | +9.0 | 2.52 | 1.55 | +28.1 | +14.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=75.0% Avg=+19.7; out_of_sample N=5 Fav=40.0% Avg=+7.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | R_REPEATER | 100.0% | 54.5% | 54.5% | 15.2% | +5.4 | 1.89 | 1.37 | +23.3 | +13.9 |
| `hunt_to_ar_ratio_le_2_0` | 29 | R_REPEATER | 87.9% | 55.2% | 55.2% | 13.8% | +6.5 | 2.16 | 1.49 | +23.5 | +13.3 |
| `hunt_to_ar_ratio_le_2_5` | 32 | R_REPEATER | 97.0% | 53.1% | 53.1% | 15.6% | +5.2 | 1.83 | 1.40 | +23.3 | +14.2 |
| `stop_hunt_le_90` | 29 | R_REPEATER | 87.9% | 55.2% | 55.2% | 17.2% | +4.3 | 1.76 | 1.21 | +21.3 | +12.3 |
| `asian_range_gte_30` | 33 | R_REPEATER | 100.0% | 54.5% | 54.5% | 15.2% | +5.4 | 1.89 | 1.37 | +23.3 | +13.9 |
| `confluence_gte_60` | 33 | R_REPEATER | 100.0% | 54.5% | 54.5% | 15.2% | +5.4 | 1.89 | 1.37 | +23.3 | +13.9 |
| `confluence_gte_70` | 9 | R_REPEATER | 27.3% | 55.6% | 55.6% | 0.0% | +13.0 | 7.08 | 5.67 | +25.6 | +13.0 |
| `tdi_rsi_gt_signal` | 17 | R_REPEATER | 51.5% | 52.9% | 52.9% | 17.6% | +9.6 | 2.86 | 1.91 | +28.2 | +14.6 |
| `tdi_rsi_gte_50` | 19 | R_REPEATER | 57.6% | 52.6% | 52.6% | 0.0% | +6.0 | 1.88 | 1.69 | +24.5 | +19.0 |
| `ratio_le_2_and_asian_gte_30` | 29 | R_REPEATER | 87.9% | 55.2% | 55.2% | 13.8% | +6.5 | 2.16 | 1.49 | +23.5 | +13.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | R_REPEATER | 45.5% | 53.3% | 53.3% | 13.3% | +10.6 | 2.92 | 1.83 | +28.4 | +14.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | R_REPEATER | 87.9% | 55.2% | 55.2% | 17.2% | +4.3 | 1.76 | 1.21 | +21.3 | +12.3 |
| `feature_stale_hod_exhaustion_reject` | 33 | R_REPEATER | 100.0% | 54.5% | 54.5% | 15.2% | +5.4 | 1.89 | 1.37 | +23.3 | +13.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=66.7% Avg=+8.7; validation N=1 Fav=0.0% Avg=-30.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | R_REPEATER | 100.0% | 53.8% | 61.5% | 38.5% | +8.9 | 1.84 | 1.15 | +37.9 | +17.5 |
| `hunt_to_ar_ratio_le_2_0` | 13 | R_REPEATER | 100.0% | 53.8% | 61.5% | 38.5% | +8.9 | 1.84 | 1.15 | +37.9 | +17.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | R_REPEATER | 100.0% | 53.8% | 61.5% | 38.5% | +8.9 | 1.84 | 1.15 | +37.9 | +17.5 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 92.3% | 50.0% | 58.3% | 41.7% | +4.4 | 1.39 | 0.99 | +35.5 | +18.9 |
| `asian_range_gte_30` | 13 | R_REPEATER | 100.0% | 53.8% | 61.5% | 38.5% | +8.9 | 1.84 | 1.15 | +37.9 | +17.5 |
| `confluence_gte_60` | 13 | R_REPEATER | 100.0% | 53.8% | 61.5% | 38.5% | +8.9 | 1.84 | 1.15 | +37.9 | +17.5 |
| `confluence_gte_70` | 13 | R_REPEATER | 100.0% | 53.8% | 61.5% | 38.5% | +8.9 | 1.84 | 1.15 | +37.9 | +17.5 |
| `tdi_rsi_gt_signal` | 7 | R_REPEATER | 53.8% | 57.1% | 57.1% | 42.9% | +3.1 | 1.21 | 0.90 | +44.3 | +22.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 53.8% | 42.9% | 42.9% | 14.3% | +0.3 | 1.02 | 1.36 | +47.3 | +25.6 |
| `ratio_le_2_and_asian_gte_30` | 13 | R_REPEATER | 100.0% | 53.8% | 61.5% | 38.5% | +8.9 | 1.84 | 1.15 | +37.9 | +17.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | R_REPEATER | 53.8% | 57.1% | 57.1% | 42.9% | +3.1 | 1.21 | 0.90 | +44.3 | +22.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 92.3% | 50.0% | 58.3% | 41.7% | +4.4 | 1.39 | 0.99 | +35.5 | +18.9 |
| `feature_stale_hod_exhaustion_reject` | 13 | R_REPEATER | 100.0% | 53.8% | 61.5% | 38.5% | +8.9 | 1.84 | 1.15 | +37.9 | +17.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=42.9% Avg=+0.5; out_of_sample N=5 Fav=80.0% Avg=+0.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | R_REPEATER | 100.0% | 53.8% | 53.8% | 15.4% | -2.3 | 0.81 | 0.69 | +20.3 | +25.5 |
| `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 92.3% | 58.3% | 58.3% | 16.7% | +0.7 | 1.07 | 0.76 | +21.9 | +23.9 |
| `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 92.3% | 58.3% | 58.3% | 16.7% | +0.7 | 1.07 | 0.76 | +21.9 | +23.9 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 92.3% | 58.3% | 58.3% | 16.7% | +0.7 | 1.07 | 0.76 | +21.9 | +23.9 |
| `asian_range_gte_30` | 13 | R_REPEATER | 100.0% | 53.8% | 53.8% | 15.4% | -2.3 | 0.81 | 0.69 | +20.3 | +25.5 |
| `confluence_gte_60` | 13 | R_REPEATER | 100.0% | 53.8% | 53.8% | 15.4% | -2.3 | 0.81 | 0.69 | +20.3 | +25.5 |
| `confluence_gte_70` | 13 | R_REPEATER | 100.0% | 53.8% | 53.8% | 15.4% | -2.3 | 0.81 | 0.69 | +20.3 | +25.5 |
| `tdi_rsi_gt_signal` | 3 | R_REPEATER | 23.1% | 66.7% | 66.7% | 33.3% | +13.1 | 3.47 | 1.74 | +23.4 | +12.1 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 92.3% | 50.0% | 50.0% | 8.3% | -6.7 | 0.47 | 0.47 | +17.5 | +27.3 |
| `ratio_le_2_and_asian_gte_30` | 12 | R_REPEATER | 92.3% | 58.3% | 58.3% | 16.7% | +0.7 | 1.07 | 0.76 | +21.9 | +23.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | R_REPEATER | 23.1% | 66.7% | 66.7% | 33.3% | +13.1 | 3.47 | 1.74 | +23.4 | +12.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 92.3% | 58.3% | 58.3% | 16.7% | +0.7 | 1.07 | 0.76 | +21.9 | +23.9 |
| `feature_stale_hod_exhaustion_reject` | 13 | R_REPEATER | 100.0% | 53.8% | 53.8% | 15.4% | -2.3 | 0.81 | 0.69 | +20.3 | +25.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=66.7% Avg=+18.1; validation N=4 Fav=75.0% Avg=+19.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +9.8 | 3.11 | 3.11 | +26.8 | +17.8 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -12.9 | 0.00 | 0.00 | +8.1 | +16.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +9.8 | 3.11 | 3.11 | +26.8 | +17.8 |
| `confluence_gte_60` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +9.8 | 3.11 | 3.11 | +26.8 | +17.8 |
| `confluence_gte_70` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +9.8 | 3.11 | 3.11 | +26.8 | +17.8 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 25.0% | +15.0 | 6.26 | 6.26 | +28.9 | +22.0 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 70.0% | 71.4% | 71.4% | 42.9% | +19.1 | 12.74 | 5.09 | +34.7 | +17.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +9.8 | 3.11 | 3.11 | +26.8 | +17.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+5.7; validation N=3 Fav=66.7% Avg=+30.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +9.4 | 2.16 | 2.16 | +30.7 | +16.4 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 78.6% | 45.5% | 45.5% | 18.2% | +4.7 | 1.49 | 1.79 | +28.0 | +18.0 |
| `hunt_to_ar_ratio_le_2_5` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +9.4 | 2.16 | 2.16 | +30.7 | +16.4 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 85.7% | 50.0% | 50.0% | 16.7% | +6.8 | 1.78 | 1.78 | +28.7 | +17.5 |
| `asian_range_gte_30` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +9.4 | 2.16 | 2.16 | +30.7 | +16.4 |
| `confluence_gte_60` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +9.4 | 2.16 | 2.16 | +30.7 | +16.4 |
| `confluence_gte_70` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +9.4 | 2.16 | 2.16 | +30.7 | +16.4 |
| `tdi_rsi_gt_signal` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 57.1% | 50.0% | 50.0% | 12.5% | +15.1 | 4.64 | 4.64 | +33.0 | +19.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 78.6% | 45.5% | 45.5% | 18.2% | +4.7 | 1.49 | 1.79 | +28.0 | +18.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 85.7% | 50.0% | 50.0% | 16.7% | +6.8 | 1.78 | 1.78 | +28.7 | +17.5 |
| `feature_stale_hod_exhaustion_reject` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 21.4% | +9.4 | 2.16 | 2.16 | +30.7 | +16.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=44.4% Avg=-1.1; validation N=7 Fav=57.1% Avg=+13.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 56.2% | +5.2 | 1.58 | 0.98 | +32.0 | +20.5 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 87.5% | 42.9% | 42.9% | 57.1% | +1.7 | 1.17 | 0.97 | +31.0 | +20.8 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 93.8% | 46.7% | 46.7% | 53.3% | +4.0 | 1.41 | 1.01 | +32.1 | +21.5 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 87.5% | 42.9% | 42.9% | 57.1% | +0.7 | 1.07 | 0.89 | +29.7 | +20.5 |
| `asian_range_gte_30` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 56.2% | +5.2 | 1.58 | 0.98 | +32.0 | +20.5 |
| `confluence_gte_60` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 56.2% | +5.2 | 1.58 | 0.98 | +32.0 | +20.5 |
| `confluence_gte_70` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 56.2% | +5.2 | 1.58 | 0.98 | +32.0 | +20.5 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 93.8% | 46.7% | 46.7% | 53.3% | +4.0 | 1.41 | 1.01 | +32.1 | +21.5 |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 50.0% | 50.0% | 50.0% | 37.5% | -2.1 | 0.88 | 0.88 | +33.0 | +31.5 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 87.5% | 42.9% | 42.9% | 57.1% | +1.7 | 1.17 | 0.97 | +31.0 | +20.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 87.5% | 42.9% | 42.9% | 57.1% | +1.7 | 1.17 | 0.97 | +31.0 | +20.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 87.5% | 42.9% | 42.9% | 57.1% | +0.7 | 1.07 | 0.89 | +29.7 | +20.5 |
| `feature_stale_hod_exhaustion_reject` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 56.2% | +5.2 | 1.58 | 0.98 | +32.0 | +20.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=61.5% Avg=+10.2; validation N=2 Fav=0.0% Avg=-33.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 45.7% | 54.3% | 17.1% | +8.4 | 2.09 | 1.54 | +27.5 | +15.3 |
| `hunt_to_ar_ratio_le_2_0` | 32 | S_STRANGER | 91.4% | 46.9% | 53.1% | 15.6% | +6.1 | 1.72 | 1.31 | +26.7 | +16.4 |
| `hunt_to_ar_ratio_le_2_5` | 35 | S_STRANGER | 100.0% | 45.7% | 54.3% | 17.1% | +8.4 | 2.09 | 1.54 | +27.5 | +15.3 |
| `stop_hunt_le_90` | 33 | S_STRANGER | 94.3% | 48.5% | 54.5% | 18.2% | +8.7 | 2.07 | 1.49 | +28.8 | +15.9 |
| `asian_range_gte_30` | 35 | S_STRANGER | 100.0% | 45.7% | 54.3% | 17.1% | +8.4 | 2.09 | 1.54 | +27.5 | +15.3 |
| `confluence_gte_60` | 23 | S_STRANGER | 65.7% | 47.8% | 52.2% | 26.1% | +12.7 | 2.66 | 2.00 | +30.9 | +16.3 |
| `confluence_gte_70` | 1 | R_RUNNER | 2.9% | 100.0% | 100.0% | 100.0% | +28.0 | 999.00 | 999.00 | +28.2 | +1.1 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 60.0% | 42.9% | 47.6% | 4.8% | -3.4 | 0.70 | 0.77 | +18.3 | +20.2 |
| `tdi_rsi_gte_50` | 15 | R_REPEATER | 42.9% | 53.3% | 60.0% | 20.0% | +4.4 | 1.41 | 0.78 | +30.2 | +19.4 |
| `ratio_le_2_and_asian_gte_30` | 32 | S_STRANGER | 91.4% | 46.9% | 53.1% | 15.6% | +6.1 | 1.72 | 1.31 | +26.7 | +16.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 20 | S_STRANGER | 57.1% | 45.0% | 50.0% | 5.0% | -3.5 | 0.71 | 0.71 | +19.1 | +21.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 33 | S_STRANGER | 94.3% | 48.5% | 54.5% | 18.2% | +8.7 | 2.07 | 1.49 | +28.8 | +15.9 |
| `feature_stale_hod_exhaustion_reject` | 35 | S_STRANGER | 100.0% | 45.7% | 54.3% | 17.1% | +8.4 | 2.09 | 1.54 | +27.5 | +15.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=66.7% Avg=+10.8; out_of_sample N=2 Fav=50.0% Avg=+7.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 45.0% | 45.0% | 45.0% | +3.7 | 1.52 | 1.35 | +26.0 | +14.3 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 95.0% | 47.4% | 47.4% | 42.1% | +3.8 | 1.52 | 1.35 | +25.7 | +14.9 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 95.0% | 47.4% | 47.4% | 42.1% | +3.8 | 1.52 | 1.35 | +25.7 | +14.9 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 95.0% | 47.4% | 47.4% | 42.1% | +3.8 | 1.52 | 1.35 | +25.7 | +14.9 |
| `asian_range_gte_30` | 20 | S_STRANGER | 100.0% | 45.0% | 45.0% | 45.0% | +3.7 | 1.52 | 1.35 | +26.0 | +14.3 |
| `confluence_gte_60` | 16 | S_STRANGER | 80.0% | 37.5% | 37.5% | 31.2% | +0.3 | 1.04 | 1.38 | +25.1 | +16.4 |
| `confluence_gte_70` | 5 | R_REPEATER | 25.0% | 60.0% | 60.0% | 20.0% | +9.6 | 3.61 | 2.41 | +27.7 | +12.6 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -11.7 | 0.29 | 0.88 | +21.4 | +24.1 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 50.0% | 30.0% | 30.0% | 10.0% | -6.9 | 0.49 | 1.15 | +19.8 | +22.2 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 95.0% | 47.4% | 47.4% | 42.1% | +3.8 | 1.52 | 1.35 | +25.7 | +14.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -11.7 | 0.29 | 0.88 | +21.4 | +24.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 95.0% | 47.4% | 47.4% | 42.1% | +3.8 | 1.52 | 1.35 | +25.7 | +14.9 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 45.0% | 45.0% | 45.0% | +3.7 | 1.52 | 1.35 | +26.0 | +14.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=100.0% Avg=+39.6; validation N=3 Fav=66.7% Avg=-17.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 43.8% | 50.0% | 25.0% | +3.1 | 1.28 | 0.96 | +22.1 | +16.2 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 93.8% | 40.0% | 46.7% | 26.7% | +1.0 | 1.09 | 0.93 | +21.0 | +17.3 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 43.8% | 50.0% | 25.0% | +3.1 | 1.28 | 0.96 | +22.1 | +16.2 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 87.5% | 42.9% | 50.0% | 21.4% | +1.1 | 1.09 | 0.93 | +20.9 | +18.3 |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 43.8% | 50.0% | 25.0% | +3.1 | 1.28 | 0.96 | +22.1 | +16.2 |
| `confluence_gte_60` | 8 | R_REPEATER | 50.0% | 50.0% | 50.0% | 25.0% | +4.6 | 1.29 | 0.97 | +29.5 | +25.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 50.0% | 50.0% | 50.0% | 12.5% | +0.1 | 1.01 | 0.75 | +25.2 | +26.1 |
| `tdi_rsi_gte_50` | 7 | R_RUNNER | 43.8% | 85.7% | 85.7% | 14.3% | +15.1 | 2.04 | 0.34 | +37.7 | +29.2 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 93.8% | 40.0% | 46.7% | 26.7% | +1.0 | 1.09 | 0.93 | +21.0 | +17.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 43.8% | 42.9% | 42.9% | 14.3% | -4.8 | 0.76 | 0.76 | +23.4 | +29.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 87.5% | 42.9% | 50.0% | 21.4% | +1.1 | 1.09 | 0.93 | +20.9 | +18.3 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 43.8% | 50.0% | 25.0% | +3.1 | 1.28 | 0.96 | +22.1 | +16.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=18 Fav=38.9% Avg=-1.9; out_of_sample N=12 Fav=50.0% Avg=+6.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 42.9% | 42.9% | 20.0% | -1.2 | 0.87 | 1.04 | +19.8 | +21.1 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 85.7% | 43.3% | 43.3% | 23.3% | +1.5 | 1.21 | 1.40 | +20.4 | +18.2 |
| `hunt_to_ar_ratio_le_2_5` | 33 | S_STRANGER | 94.3% | 39.4% | 39.4% | 21.2% | -1.9 | 0.80 | 1.11 | +19.6 | +21.7 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 91.4% | 40.6% | 40.6% | 21.9% | -0.8 | 0.91 | 1.19 | +20.1 | +20.9 |
| `asian_range_gte_30` | 35 | S_STRANGER | 100.0% | 42.9% | 42.9% | 20.0% | -1.2 | 0.87 | 1.04 | +19.8 | +21.1 |
| `confluence_gte_60` | 27 | S_STRANGER | 77.1% | 48.1% | 48.1% | 18.5% | -1.1 | 0.89 | 0.89 | +20.4 | +22.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 14.3% | 40.0% | 40.0% | 20.0% | -13.5 | 0.42 | 0.64 | +16.6 | +33.0 |
| `tdi_rsi_gte_50` | 22 | S_STRANGER | 62.9% | 40.9% | 40.9% | 13.6% | -4.6 | 0.62 | 0.82 | +19.3 | +26.1 |
| `ratio_le_2_and_asian_gte_30` | 30 | S_STRANGER | 85.7% | 43.3% | 43.3% | 23.3% | +1.5 | 1.21 | 1.40 | +20.4 | +18.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 14.3% | 40.0% | 40.0% | 20.0% | -13.5 | 0.42 | 0.64 | +16.6 | +33.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 91.4% | 40.6% | 40.6% | 21.9% | -0.8 | 0.91 | 1.19 | +20.1 | +20.9 |
| `feature_stale_hod_exhaustion_reject` | 35 | S_STRANGER | 100.0% | 42.9% | 42.9% | 20.0% | -1.2 | 0.87 | 1.04 | +19.8 | +21.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-35.2; validation N=6 Fav=83.3% Avg=+19.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 41.2% | 41.2% | 17.6% | -1.4 | 0.90 | 1.15 | +23.3 | +13.6 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 88.2% | 46.7% | 46.7% | 20.0% | +2.3 | 1.20 | 1.20 | +26.2 | +15.1 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 88.2% | 46.7% | 46.7% | 20.0% | +2.3 | 1.20 | 1.20 | +26.2 | +15.1 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 94.1% | 43.8% | 43.8% | 18.8% | -0.9 | 0.94 | 1.07 | +24.6 | +14.4 |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 41.2% | 41.2% | 17.6% | -1.4 | 0.90 | 1.15 | +23.3 | +13.6 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 41.2% | 41.2% | 17.6% | -1.4 | 0.90 | 1.15 | +23.3 | +13.6 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 41.2% | 41.2% | 17.6% | -1.4 | 0.90 | 1.15 | +23.3 | +13.6 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 58.8% | 40.0% | 40.0% | 10.0% | -8.4 | 0.55 | 0.83 | +20.6 | +11.1 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 41.2% | 71.4% | 71.4% | 14.3% | +11.7 | 3.13 | 1.25 | +33.4 | +15.8 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 88.2% | 46.7% | 46.7% | 20.0% | +2.3 | 1.20 | 1.20 | +26.2 | +15.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 47.1% | 50.0% | 50.0% | 12.5% | -3.2 | 0.80 | 0.80 | +25.4 | +13.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 94.1% | 43.8% | 43.8% | 18.8% | -0.9 | 0.94 | 1.07 | +24.6 | +14.4 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 41.2% | 41.2% | 17.6% | -1.4 | 0.90 | 1.15 | +23.3 | +13.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=60.0% Avg=+1.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -3.9 | 0.58 | 0.88 | +19.7 | +18.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -3.9 | 0.58 | 0.88 | +19.7 | +18.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -3.9 | 0.58 | 0.88 | +19.7 | +18.9 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -3.9 | 0.58 | 0.88 | +19.7 | +18.9 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -3.9 | 0.58 | 0.88 | +19.7 | +18.9 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -3.9 | 0.58 | 0.88 | +19.7 | +18.9 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -3.9 | 0.58 | 0.88 | +19.7 | +18.9 |
| `tdi_rsi_gt_signal` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 20.0% | +1.2 | 1.17 | 0.78 | +26.6 | +18.3 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 14.3% | -5.0 | 0.53 | 0.71 | +24.6 | +17.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -3.9 | 0.58 | 0.88 | +19.7 | +18.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 20.0% | +1.2 | 1.17 | 0.78 | +26.6 | +18.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -3.9 | 0.58 | 0.88 | +19.7 | +18.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -3.9 | 0.58 | 0.88 | +19.7 | +18.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=55.6% Avg=+13.3; validation N=6 Fav=33.3% Avg=+1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 16.7% | +5.8 | 1.99 | 3.13 | +28.4 | +15.4 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 88.9% | 43.8% | 43.8% | 18.8% | +7.6 | 2.36 | 3.04 | +29.2 | +14.6 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 16.7% | +5.8 | 1.99 | 3.13 | +28.4 | +15.4 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 83.3% | 46.7% | 46.7% | 20.0% | +8.7 | 2.64 | 3.02 | +29.3 | +14.8 |
| `asian_range_gte_30` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 16.7% | +5.8 | 1.99 | 3.13 | +28.4 | +15.4 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 16.7% | +5.8 | 1.99 | 3.13 | +28.4 | +15.4 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 16.7% | +5.8 | 1.99 | 3.13 | +28.4 | +15.4 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 33.3% | -6.7 | 0.57 | 1.13 | +21.3 | +24.2 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 72.2% | 38.5% | 38.5% | 15.4% | +5.1 | 1.79 | 2.87 | +28.5 | +17.1 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 88.9% | 43.8% | 43.8% | 18.8% | +7.6 | 2.36 | 3.04 | +29.2 | +14.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 33.3% | -6.7 | 0.57 | 1.13 | +21.3 | +24.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 83.3% | 46.7% | 46.7% | 20.0% | +8.7 | 2.64 | 3.02 | +29.3 | +14.8 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 16.7% | +5.8 | 1.99 | 3.13 | +28.4 | +15.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=25 Fav=40.0% Avg=+4.2; out_of_sample N=13 Fav=38.5% Avg=+7.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 42 | S_STRANGER | 100.0% | 38.1% | 38.1% | 21.4% | +3.7 | 1.65 | 2.47 | +22.0 | +13.7 |
| `hunt_to_ar_ratio_le_2_0` | 34 | S_STRANGER | 81.0% | 35.3% | 35.3% | 23.5% | +4.4 | 1.90 | 3.16 | +21.5 | +11.8 |
| `hunt_to_ar_ratio_le_2_5` | 38 | S_STRANGER | 90.5% | 39.5% | 39.5% | 21.1% | +5.3 | 2.13 | 2.99 | +22.1 | +12.6 |
| `stop_hunt_le_90` | 38 | S_STRANGER | 90.5% | 39.5% | 39.5% | 21.1% | +5.3 | 2.13 | 2.99 | +22.1 | +12.6 |
| `asian_range_gte_30` | 42 | S_STRANGER | 100.0% | 38.1% | 38.1% | 21.4% | +3.7 | 1.65 | 2.47 | +22.0 | +13.7 |
| `confluence_gte_60` | 38 | S_STRANGER | 90.5% | 36.8% | 36.8% | 21.1% | +3.3 | 1.59 | 2.50 | +21.2 | +13.5 |
| `confluence_gte_70` | 2 | R_REPEATER | 4.8% | 50.0% | 50.0% | 0.0% | -21.5 | 0.19 | 0.19 | +10.9 | +47.3 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 45.2% | 31.6% | 31.6% | 15.8% | +0.1 | 1.01 | 2.20 | +20.7 | +17.1 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 40.5% | 29.4% | 29.4% | 17.6% | +0.3 | 1.04 | 2.49 | +22.3 | +18.1 |
| `ratio_le_2_and_asian_gte_30` | 34 | S_STRANGER | 81.0% | 35.3% | 35.3% | 23.5% | +4.4 | 1.90 | 3.16 | +21.5 | +11.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 16 | S_STRANGER | 38.1% | 31.2% | 31.2% | 18.8% | +2.1 | 1.36 | 3.00 | +21.2 | +14.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 38 | S_STRANGER | 90.5% | 39.5% | 39.5% | 21.1% | +5.3 | 2.13 | 2.99 | +22.1 | +12.6 |
| `feature_stale_hod_exhaustion_reject` | 42 | S_STRANGER | 100.0% | 38.1% | 38.1% | 21.4% | +3.7 | 1.65 | 2.47 | +22.0 | +13.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=66.7% Avg=+16.2; out_of_sample N=2 Fav=50.0% Avg=-14.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 36.4% | 40.9% | 9.1% | -1.0 | 0.90 | 1.30 | +15.4 | +17.4 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 77.3% | 35.3% | 41.2% | 11.8% | -0.9 | 0.91 | 1.31 | +15.3 | +19.3 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 86.4% | 36.8% | 42.1% | 10.5% | -1.1 | 0.89 | 1.22 | +16.2 | +18.0 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 77.3% | 35.3% | 41.2% | 11.8% | -0.9 | 0.91 | 1.31 | +15.3 | +19.3 |
| `asian_range_gte_30` | 22 | S_STRANGER | 100.0% | 36.4% | 40.9% | 9.1% | -1.0 | 0.90 | 1.30 | +15.4 | +17.4 |
| `confluence_gte_60` | 22 | S_STRANGER | 100.0% | 36.4% | 40.9% | 9.1% | -1.0 | 0.90 | 1.30 | +15.4 | +17.4 |
| `confluence_gte_70` | 5 | R_REPEATER | 22.7% | 60.0% | 60.0% | 40.0% | +4.0 | 1.31 | 0.87 | +20.1 | +25.0 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 72.7% | 37.5% | 43.8% | 6.2% | +0.9 | 1.09 | 1.40 | +18.0 | +20.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 31.8% | 42.9% | 42.9% | 14.3% | -2.9 | 0.80 | 1.07 | +23.7 | +29.7 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 77.3% | 35.3% | 41.2% | 11.8% | -0.9 | 0.91 | 1.31 | +15.3 | +19.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 50.0% | 36.4% | 45.5% | 9.1% | +1.8 | 1.17 | 1.40 | +19.1 | +24.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 77.3% | 35.3% | 41.2% | 11.8% | -0.9 | 0.91 | 1.31 | +15.3 | +19.3 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 36.4% | 40.9% | 9.1% | -1.0 | 0.90 | 1.30 | +15.4 | +17.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=-3.4; validation N=2 Fav=100.0% Avg=+34.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 0.0% | -1.9 | 0.83 | 1.46 | +23.9 | +29.6 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 0.0% | -0.0 | 1.00 | 1.00 | +26.6 | +18.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 0.0% | -1.9 | 0.83 | 1.46 | +23.9 | +29.6 |
| `confluence_gte_60` | 8 | R_REPEATER | 72.7% | 50.0% | 50.0% | 0.0% | +5.9 | 1.85 | 1.85 | +26.4 | +24.8 |
| `confluence_gte_70` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -19.7 | 0.00 | 0.00 | +7.4 | +44.4 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 0.0% | +0.5 | 1.07 | 1.07 | +12.9 | +24.2 |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 72.7% | 50.0% | 50.0% | 0.0% | +6.0 | 1.86 | 1.86 | +24.3 | +26.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 0.0% | -1.9 | 0.83 | 1.46 | +23.9 | +29.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=14 Fav=35.7% Avg=-4.7; validation N=7 Fav=57.1% Avg=+15.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 34.6% | 34.6% | 7.7% | -2.8 | 0.73 | 1.37 | +18.6 | +19.2 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 80.8% | 33.3% | 33.3% | 9.5% | -1.0 | 0.87 | 1.73 | +17.7 | +20.7 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 92.3% | 29.2% | 29.2% | 8.3% | -5.3 | 0.52 | 1.25 | +16.5 | +19.4 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 92.3% | 37.5% | 37.5% | 8.3% | -0.7 | 0.92 | 1.54 | +19.6 | +19.6 |
| `asian_range_gte_30` | 26 | S_STRANGER | 100.0% | 34.6% | 34.6% | 7.7% | -2.8 | 0.73 | 1.37 | +18.6 | +19.2 |
| `confluence_gte_60` | 18 | S_STRANGER | 69.2% | 38.9% | 38.9% | 5.6% | -0.4 | 0.93 | 1.47 | +15.0 | +21.1 |
| `confluence_gte_70` | 5 | S_STRANGER | 19.2% | 0.0% | 0.0% | 0.0% | -12.6 | 0.00 | 0.00 | +14.1 | +31.3 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 80.8% | 42.9% | 42.9% | 9.5% | +2.2 | 1.31 | 1.75 | +20.2 | +19.7 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 53.8% | 21.4% | 21.4% | 0.0% | -4.7 | 0.49 | 1.80 | +19.6 | +25.2 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 80.8% | 33.3% | 33.3% | 9.5% | -1.0 | 0.87 | 1.73 | +17.7 | +20.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 65.4% | 41.2% | 41.2% | 11.8% | +2.4 | 1.44 | 2.05 | +19.2 | +20.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 92.3% | 37.5% | 37.5% | 8.3% | -0.7 | 0.92 | 1.54 | +19.6 | +19.6 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 34.6% | 34.6% | 7.7% | -2.8 | 0.73 | 1.37 | +18.6 | +19.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=33.3% Avg=+4.6; out_of_sample N=1 Fav=100.0% Avg=+6.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 34.3% | 37.1% | 11.4% | -0.4 | 0.95 | 1.53 | +16.4 | +14.7 |
| `hunt_to_ar_ratio_le_2_0` | 32 | S_STRANGER | 91.4% | 34.4% | 37.5% | 9.4% | +0.2 | 1.03 | 1.63 | +16.7 | +14.3 |
| `hunt_to_ar_ratio_le_2_5` | 35 | S_STRANGER | 100.0% | 34.3% | 37.1% | 11.4% | -0.4 | 0.95 | 1.53 | +16.4 | +14.7 |
| `stop_hunt_le_90` | 33 | S_STRANGER | 94.3% | 30.3% | 33.3% | 6.1% | -2.1 | 0.73 | 1.39 | +14.4 | +15.3 |
| `asian_range_gte_30` | 35 | S_STRANGER | 100.0% | 34.3% | 37.1% | 11.4% | -0.4 | 0.95 | 1.53 | +16.4 | +14.7 |
| `confluence_gte_60` | 29 | S_STRANGER | 82.9% | 31.0% | 34.5% | 13.8% | +0.5 | 1.08 | 1.95 | +16.5 | +13.3 |
| `confluence_gte_70` | 7 | S_STRANGER | 20.0% | 42.9% | 42.9% | 28.6% | +4.8 | 3.16 | 3.16 | +15.8 | +13.7 |
| `tdi_rsi_gt_signal` | 25 | S_STRANGER | 71.4% | 36.0% | 40.0% | 8.0% | -1.5 | 0.81 | 1.14 | +15.4 | +15.3 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 34.3% | 50.0% | 50.0% | 0.0% | -0.4 | 0.95 | 0.95 | +16.8 | +20.1 |
| `ratio_le_2_and_asian_gte_30` | 32 | S_STRANGER | 91.4% | 34.4% | 37.5% | 9.4% | +0.2 | 1.03 | 1.63 | +16.7 | +14.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 24 | S_STRANGER | 68.6% | 37.5% | 41.7% | 8.3% | -0.3 | 0.95 | 1.24 | +15.8 | +14.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 33 | S_STRANGER | 94.3% | 30.3% | 33.3% | 6.1% | -2.1 | 0.73 | 1.39 | +14.4 | +15.3 |
| `feature_stale_hod_exhaustion_reject` | 35 | S_STRANGER | 100.0% | 34.3% | 37.1% | 11.4% | -0.4 | 0.95 | 1.53 | +16.4 | +14.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=50.0% Avg=+4.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 23.8% | -0.9 | 0.86 | 1.36 | +19.3 | +13.5 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 23.8% | -0.9 | 0.86 | 1.36 | +19.3 | +13.5 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 23.8% | -0.9 | 0.86 | 1.36 | +19.3 | +13.5 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 23.8% | -0.9 | 0.86 | 1.36 | +19.3 | +13.5 |
| `asian_range_gte_30` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 23.8% | -0.9 | 0.86 | 1.36 | +19.3 | +13.5 |
| `confluence_gte_60` | 17 | S_STRANGER | 81.0% | 29.4% | 29.4% | 23.5% | -3.4 | 0.50 | 0.91 | +18.4 | +12.5 |
| `confluence_gte_70` | 3 | R_REPEATER | 14.3% | 66.7% | 66.7% | 0.0% | -0.2 | 0.98 | 0.49 | +17.5 | +18.7 |
| `tdi_rsi_gt_signal` | 10 | R_REPEATER | 47.6% | 50.0% | 50.0% | 30.0% | +4.9 | 2.28 | 1.37 | +26.1 | +12.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 33.3% | 42.9% | 42.9% | 14.3% | +0.2 | 1.05 | 1.05 | +20.9 | +10.8 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 23.8% | -0.9 | 0.86 | 1.36 | +19.3 | +13.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | R_REPEATER | 47.6% | 50.0% | 50.0% | 30.0% | +4.9 | 2.28 | 1.37 | +26.1 | +12.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 23.8% | -0.9 | 0.86 | 1.36 | +19.3 | +13.5 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 23.8% | -0.9 | 0.86 | 1.36 | +19.3 | +13.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=25.0% Avg=-27.7; validation N=4 Fav=50.0% Avg=-3.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | -12.2 | 0.35 | 0.62 | +13.7 | +28.9 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 91.7% | 36.4% | 36.4% | 27.3% | -11.4 | 0.39 | 0.58 | +14.8 | +28.7 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | -12.2 | 0.35 | 0.62 | +13.7 | +28.9 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 12.5% | -15.5 | 0.33 | 0.55 | +14.9 | +34.5 |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | -12.2 | 0.35 | 0.62 | +13.7 | +28.9 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | -12.2 | 0.35 | 0.62 | +13.7 | +28.9 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | -12.2 | 0.35 | 0.62 | +13.7 | +28.9 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 33.3% | -21.0 | 0.00 | 0.00 | +8.6 | +30.7 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -25.4 | 0.00 | 0.00 | +3.3 | +43.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 91.7% | 36.4% | 36.4% | 27.3% | -11.4 | 0.39 | 0.58 | +14.8 | +28.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 33.3% | -21.0 | 0.00 | 0.00 | +8.6 | +30.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 12.5% | -15.5 | 0.33 | 0.55 | +14.9 | +34.5 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | -12.2 | 0.35 | 0.62 | +13.7 | +28.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=60.0% Avg=+10.0; out_of_sample N=1 Fav=0.0% Avg=-14.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 37.5% | -8.0 | 0.56 | 0.75 | +20.8 | +15.9 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 37.5% | -8.0 | 0.56 | 0.75 | +20.8 | +15.9 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 37.5% | -8.0 | 0.56 | 0.75 | +20.8 | +15.9 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 37.5% | -8.0 | 0.56 | 0.75 | +20.8 | +15.9 |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 37.5% | -8.0 | 0.56 | 0.75 | +20.8 | +15.9 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 37.5% | -8.0 | 0.56 | 0.75 | +20.8 | +15.9 |
| `confluence_gte_70` | 6 | R_REPEATER | 37.5% | 50.0% | 50.0% | 33.3% | +5.9 | 1.79 | 1.79 | +31.5 | +15.6 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 18.8% | 0.0% | 0.0% | 0.0% | -52.3 | 0.00 | 0.00 | +10.4 | +27.0 |
| `tdi_rsi_gte_50` | 10 | R_REPEATER | 62.5% | 50.0% | 50.0% | 40.0% | +0.5 | 1.03 | 1.03 | +28.4 | +22.1 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 37.5% | -8.0 | 0.56 | 0.75 | +20.8 | +15.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 18.8% | 0.0% | 0.0% | 0.0% | -52.3 | 0.00 | 0.00 | +10.4 | +27.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 37.5% | -8.0 | 0.56 | 0.75 | +20.8 | +15.9 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 37.5% | -8.0 | 0.56 | 0.75 | +20.8 | +15.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=-9.0; validation N=6 Fav=33.3% Avg=-6.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -8.1 | 0.47 | 0.93 | +23.8 | +27.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 76.9% | 30.0% | 30.0% | 0.0% | -11.5 | 0.35 | 0.81 | +23.3 | +32.4 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -8.1 | 0.47 | 0.93 | +23.8 | +27.5 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 0.0% | -7.7 | 0.52 | 0.92 | +25.3 | +30.2 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -8.1 | 0.47 | 0.93 | +23.8 | +27.5 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -8.1 | 0.47 | 0.93 | +23.8 | +27.5 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -8.1 | 0.47 | 0.93 | +23.8 | +27.5 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 76.9% | 30.0% | 30.0% | 0.0% | -10.5 | 0.41 | 0.95 | +25.7 | +32.3 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 0.0% | -7.7 | 0.52 | 0.92 | +25.3 | +30.2 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 76.9% | 30.0% | 30.0% | 0.0% | -11.5 | 0.35 | 0.81 | +23.3 | +32.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 69.2% | 22.2% | 22.2% | 0.0% | -15.1 | 0.23 | 0.82 | +23.6 | +34.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 0.0% | -7.7 | 0.52 | 0.92 | +25.3 | +30.2 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -8.1 | 0.47 | 0.93 | +23.8 | +27.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=37.5% Avg=+2.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -0.5 | 0.95 | 1.58 | +21.7 | +10.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 33.3% | 33.3% | 22.2% | -0.1 | 0.98 | 1.31 | +19.6 | +11.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -0.5 | 0.95 | 1.58 | +21.7 | +10.4 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 25.0% | +2.3 | 1.30 | 1.30 | +20.5 | +12.1 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -0.5 | 0.95 | 1.58 | +21.7 | +10.4 |
| `confluence_gte_60` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -2.3 | 0.29 | 0.58 | +19.8 | +11.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 25.0% | +1.2 | 2.35 | 1.18 | +21.4 | +12.3 |
| `tdi_rsi_gte_50` | 2 | R_RUNNER | 20.0% | 100.0% | 100.0% | 0.0% | +38.7 | 999.00 | 999.00 | +49.4 | +20.6 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 33.3% | 33.3% | 22.2% | -0.1 | 0.98 | 1.31 | +19.6 | +11.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 33.3% | +2.7 | 999.00 | 999.00 | +15.0 | +14.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 25.0% | +2.3 | 1.30 | 1.30 | +20.5 | +12.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -0.5 | 0.95 | 1.58 | +21.7 | +10.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=+1.0; out_of_sample N=4 Fav=25.0% Avg=-9.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -3.9 | 0.67 | 1.56 | +14.8 | +10.4 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -3.9 | 0.67 | 1.56 | +14.8 | +10.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -3.9 | 0.67 | 1.56 | +14.8 | +10.4 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -3.9 | 0.67 | 1.56 | +14.8 | +10.4 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -3.9 | 0.67 | 1.56 | +14.8 | +10.4 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -3.9 | 0.67 | 1.56 | +14.8 | +10.4 |
| `confluence_gte_70` | 9 | S_STRANGER | 90.0% | 33.3% | 33.3% | 22.2% | -3.6 | 0.70 | 1.41 | +16.4 | +10.7 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +7.3 | 2.15 | 4.30 | +25.4 | +7.8 |
| `tdi_rsi_gte_50` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 33.3% | +16.7 | 12.36 | 6.18 | +29.6 | +5.1 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -3.9 | 0.67 | 1.56 | +14.8 | +10.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +7.3 | 2.15 | 4.30 | +25.4 | +7.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -3.9 | 0.67 | 1.56 | +14.8 | +10.4 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -3.9 | 0.67 | 1.56 | +14.8 | +10.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-10.5; validation N=9 Fav=44.4% Avg=+0.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 15.0% | -9.4 | 0.50 | 1.01 | +28.0 | +28.0 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 95.0% | 26.3% | 26.3% | 10.5% | -11.1 | 0.45 | 1.08 | +27.7 | +29.4 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 95.0% | 26.3% | 26.3% | 10.5% | -11.1 | 0.45 | 1.08 | +27.7 | +29.4 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 90.0% | 22.2% | 22.2% | 11.1% | -13.3 | 0.37 | 1.12 | +26.0 | +30.6 |
| `asian_range_gte_30` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 15.0% | -9.4 | 0.50 | 1.01 | +28.0 | +28.0 |
| `confluence_gte_60` | 14 | S_STRANGER | 70.0% | 35.7% | 35.7% | 21.4% | -3.1 | 0.80 | 1.12 | +33.5 | +21.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | -13.8 | 0.40 | 0.40 | +24.8 | +46.0 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 75.0% | 26.7% | 26.7% | 13.3% | -4.2 | 0.71 | 1.59 | +32.2 | +28.7 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 95.0% | 26.3% | 26.3% | 10.5% | -11.1 | 0.45 | 1.08 | +27.7 | +29.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | -13.8 | 0.40 | 0.40 | +24.8 | +46.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 90.0% | 22.2% | 22.2% | 11.1% | -13.3 | 0.37 | 1.12 | +26.0 | +30.6 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 15.0% | -9.4 | 0.50 | 1.01 | +28.0 | +28.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=1 Fav=0.0% Avg=-10.8; out_of_sample N=6 Fav=50.0% Avg=-3.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 29.2% | 29.2% | 12.5% | -3.5 | 0.53 | 1.13 | +17.5 | +17.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 41.7% | 30.0% | 30.0% | 30.0% | -2.8 | 0.26 | 0.44 | +20.1 | +16.9 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 66.7% | 37.5% | 37.5% | 18.8% | -0.4 | 0.93 | 1.24 | +20.2 | +16.7 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 79.2% | 36.8% | 36.8% | 15.8% | -0.1 | 0.98 | 1.41 | +19.8 | +16.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 21 | S_STRANGER | 87.5% | 33.3% | 33.3% | 14.3% | -2.4 | 0.65 | 1.12 | +19.0 | +17.2 |
| `confluence_gte_70` | 7 | S_STRANGER | 29.2% | 42.9% | 42.9% | 28.6% | -4.1 | 0.26 | 0.26 | +11.8 | +18.7 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 54.2% | 38.5% | 38.5% | 7.7% | -1.9 | 0.77 | 1.08 | +21.1 | +19.6 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 37.5% | 33.3% | 33.3% | 0.0% | -6.4 | 0.46 | 0.91 | +13.0 | +24.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 79.2% | 36.8% | 36.8% | 15.8% | -0.1 | 0.98 | 1.41 | +19.8 | +16.1 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 29.2% | 29.2% | 12.5% | -3.5 | 0.53 | 1.13 | +17.5 | +17.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=11 Fav=36.4% Avg=+0.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 7.1% | -2.4 | 0.63 | 1.13 | +13.4 | +19.0 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 7.1% | -2.4 | 0.63 | 1.13 | +13.4 | +19.0 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 7.1% | -2.4 | 0.63 | 1.13 | +13.4 | +19.0 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 7.1% | -2.4 | 0.63 | 1.13 | +13.4 | +19.0 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 7.1% | -2.4 | 0.63 | 1.13 | +13.4 | +19.0 |
| `confluence_gte_60` | 11 | S_STRANGER | 78.6% | 36.4% | 36.4% | 9.1% | +0.9 | 1.24 | 2.17 | +14.1 | +17.2 |
| `confluence_gte_70` | 3 | R_REPEATER | 21.4% | 66.7% | 66.7% | 33.3% | +16.5 | 71.71 | 35.86 | +23.4 | +12.9 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 85.7% | 25.0% | 33.3% | 8.3% | -2.8 | 0.62 | 1.24 | +14.3 | +19.8 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 92.9% | 30.8% | 30.8% | 7.7% | -2.9 | 0.59 | 1.33 | +13.9 | +20.3 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 7.1% | -2.4 | 0.63 | 1.13 | +13.4 | +19.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 85.7% | 25.0% | 33.3% | 8.3% | -2.8 | 0.62 | 1.24 | +14.3 | +19.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 7.1% | -2.4 | 0.63 | 1.13 | +13.4 | +19.0 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 7.1% | -2.4 | 0.63 | 1.13 | +13.4 | +19.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=11 Fav=36.4% Avg=-3.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 21.4% | -3.5 | 0.66 | 1.06 | +19.0 | +16.7 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 92.9% | 23.1% | 30.8% | 15.4% | -4.6 | 0.60 | 1.20 | +17.6 | +17.9 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 23.1% | 30.8% | 15.4% | -4.6 | 0.60 | 1.20 | +17.6 | +17.9 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 92.9% | 23.1% | 30.8% | 15.4% | -4.6 | 0.60 | 1.20 | +17.6 | +17.9 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 21.4% | -3.5 | 0.66 | 1.06 | +19.0 | +16.7 |
| `confluence_gte_60` | 11 | S_STRANGER | 78.6% | 36.4% | 36.4% | 18.2% | -3.2 | 0.73 | 1.27 | +20.8 | +18.5 |
| `confluence_gte_70` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -14.9 | 0.00 | 0.00 | +7.4 | +28.3 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 0.0% | -0.7 | 0.53 | 0.53 | +16.4 | +10.0 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 0.0% | -11.2 | 0.02 | 0.12 | +12.3 | +23.4 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 92.9% | 23.1% | 30.8% | 15.4% | -4.6 | 0.60 | 1.20 | +17.6 | +17.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 0.0% | -0.7 | 0.53 | 0.53 | +16.4 | +10.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 92.9% | 23.1% | 30.8% | 15.4% | -4.6 | 0.60 | 1.20 | +17.6 | +17.9 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 21.4% | -3.5 | 0.66 | 1.06 | +19.0 | +16.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=30.0% Avg=-22.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | -15.3 | 0.21 | 0.54 | +10.4 | +23.3 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | -15.3 | 0.21 | 0.54 | +10.4 | +23.3 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | -15.3 | 0.21 | 0.54 | +10.4 | +23.3 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | -15.3 | 0.21 | 0.54 | +10.4 | +23.3 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | -15.3 | 0.21 | 0.54 | +10.4 | +23.3 |
| `confluence_gte_60` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 8.3% | -21.7 | 0.05 | 0.24 | +7.6 | +26.0 |
| `confluence_gte_70` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -64.7 | 0.00 | 0.00 | +10.3 | +65.2 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 71.4% | 30.0% | 30.0% | 20.0% | -22.0 | 0.12 | 0.29 | +10.9 | +29.0 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 20.0% | -32.7 | 0.10 | 0.40 | +13.4 | +41.2 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | -15.3 | 0.21 | 0.54 | +10.4 | +23.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 71.4% | 30.0% | 30.0% | 20.0% | -22.0 | 0.12 | 0.29 | +10.9 | +29.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | -15.3 | 0.21 | 0.54 | +10.4 | +23.3 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | -15.3 | 0.21 | 0.54 | +10.4 | +23.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=+6.1; out_of_sample N=5 Fav=20.0% Avg=-17.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | -6.6 | 0.59 | 1.03 | +19.2 | +29.4 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 30.0% | 40.0% | 10.0% | -5.5 | 0.65 | 0.98 | +19.6 | +29.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | -6.6 | 0.59 | 1.03 | +19.2 | +29.4 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 90.9% | 30.0% | 40.0% | 10.0% | -5.5 | 0.65 | 0.98 | +19.6 | +29.2 |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | -6.6 | 0.59 | 1.03 | +19.2 | +29.4 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | -6.6 | 0.59 | 1.03 | +19.2 | +29.4 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | -6.6 | 0.59 | 1.03 | +19.2 | +29.4 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -34.7 | 0.00 | 0.00 | +0.7 | +39.9 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 0.0% | -8.9 | 0.49 | 1.15 | +19.1 | +31.1 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 90.9% | 30.0% | 40.0% | 10.0% | -5.5 | 0.65 | 0.98 | +19.6 | +29.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -34.7 | 0.00 | 0.00 | +0.7 | +39.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 90.9% | 30.0% | 40.0% | 10.0% | -5.5 | 0.65 | 0.98 | +19.6 | +29.2 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | -6.6 | 0.59 | 1.03 | +19.2 | +29.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=+17.8; out_of_sample N=1 Fav=0.0% Avg=-90.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 41.7% | 33.3% | -5.2 | 0.68 | 0.81 | +21.8 | +22.2 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 41.7% | 33.3% | -5.2 | 0.68 | 0.81 | +21.8 | +22.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 41.7% | 33.3% | -5.2 | 0.68 | 0.81 | +21.8 | +22.2 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 41.7% | 33.3% | -5.2 | 0.68 | 0.81 | +21.8 | +22.2 |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 41.7% | 33.3% | -5.2 | 0.68 | 0.81 | +21.8 | +22.2 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 41.7% | 33.3% | -5.2 | 0.68 | 0.81 | +21.8 | +22.2 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 41.7% | 33.3% | -5.2 | 0.68 | 0.81 | +21.8 | +22.2 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -17.6 | 0.00 | 0.00 | +2.3 | +31.1 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 33.3% | 50.0% | 16.7% | -0.2 | 0.99 | 0.99 | +32.5 | +32.5 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 41.7% | 33.3% | -5.2 | 0.68 | 0.81 | +21.8 | +22.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -17.6 | 0.00 | 0.00 | +2.3 | +31.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 41.7% | 33.3% | -5.2 | 0.68 | 0.81 | +21.8 | +22.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 41.7% | 33.3% | -5.2 | 0.68 | 0.81 | +21.8 | +22.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=10 Fav=30.0% Avg=-0.2; out_of_sample N=2 Fav=0.0% Avg=-17.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -3.6 | 0.67 | 2.24 | +13.7 | +29.2 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 25.0% | 25.0% | 8.3% | -3.2 | 0.72 | 2.15 | +14.8 | +29.9 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -3.6 | 0.67 | 2.24 | +13.7 | +29.2 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 92.3% | 25.0% | 25.0% | 8.3% | -3.2 | 0.72 | 2.15 | +14.8 | +29.9 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -3.6 | 0.67 | 2.24 | +13.7 | +29.2 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -3.6 | 0.67 | 2.24 | +13.7 | +29.2 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -3.6 | 0.67 | 2.24 | +13.7 | +29.2 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -19.8 | 0.00 | 0.00 | +7.2 | +38.5 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 76.9% | 20.0% | 20.0% | 10.0% | -4.5 | 0.66 | 2.64 | +14.8 | +31.5 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 92.3% | 25.0% | 25.0% | 8.3% | -3.2 | 0.72 | 2.15 | +14.8 | +29.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -19.8 | 0.00 | 0.00 | +7.2 | +38.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 92.3% | 25.0% | 25.0% | 8.3% | -3.2 | 0.72 | 2.15 | +14.8 | +29.9 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -3.6 | 0.67 | 2.24 | +13.7 | +29.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=66.7% Avg=+19.9; out_of_sample N=2 Fav=0.0% Avg=-63.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 18.2% | -17.7 | 0.19 | 0.60 | +10.7 | +23.4 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 18.2% | -17.7 | 0.19 | 0.60 | +10.7 | +23.4 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 18.2% | -17.7 | 0.19 | 0.60 | +10.7 | +23.4 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 18.2% | -17.7 | 0.19 | 0.60 | +10.7 | +23.4 |
| `asian_range_gte_30` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 18.2% | -17.7 | 0.19 | 0.60 | +10.7 | +23.4 |
| `confluence_gte_60` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 18.2% | -17.7 | 0.19 | 0.60 | +10.7 | +23.4 |
| `confluence_gte_70` | 14 | S_STRANGER | 63.6% | 28.6% | 28.6% | 21.4% | -10.7 | 0.33 | 0.75 | +11.3 | +12.0 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 63.6% | 21.4% | 21.4% | 7.1% | -19.6 | 0.20 | 0.72 | +10.2 | +32.9 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 22.7% | 40.0% | 40.0% | 0.0% | -13.4 | 0.48 | 0.72 | +19.7 | +45.1 |
| `ratio_le_2_and_asian_gte_30` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 18.2% | -17.7 | 0.19 | 0.60 | +10.7 | +23.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 63.6% | 21.4% | 21.4% | 7.1% | -19.6 | 0.20 | 0.72 | +10.2 | +32.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 18.2% | -17.7 | 0.19 | 0.60 | +10.7 | +23.4 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 18.2% | -17.7 | 0.19 | 0.60 | +10.7 | +23.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=-2.0; validation N=3 Fav=33.3% Avg=-6.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 28.6% | -5.2 | 0.21 | 0.55 | +9.5 | +12.4 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 85.7% | 8.3% | 8.3% | 33.3% | -7.3 | 0.04 | 0.35 | +8.1 | +11.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 28.6% | -5.2 | 0.21 | 0.55 | +9.5 | +12.4 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 25.0% | -7.2 | 0.06 | 0.24 | +7.0 | +12.8 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 28.6% | -5.2 | 0.21 | 0.55 | +9.5 | +12.4 |
| `confluence_gte_60` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 50.0% | -7.2 | 0.08 | 0.25 | +8.7 | +12.0 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +10.9 | +1.2 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 57.1% | 37.5% | 37.5% | 25.0% | -3.8 | 0.39 | 0.51 | +11.5 | +15.4 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 0.0% | -5.0 | 0.40 | 1.20 | +13.3 | +18.6 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 85.7% | 8.3% | 8.3% | 33.3% | -7.3 | 0.04 | 0.35 | +8.1 | +11.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 33.3% | -7.5 | 0.08 | 0.33 | +9.4 | +15.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 25.0% | -7.2 | 0.06 | 0.24 | +7.0 | +12.8 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 28.6% | -5.2 | 0.21 | 0.55 | +9.5 | +12.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+1.8; validation N=9 Fav=11.1% Avg=-38.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -24.4 | 0.13 | 0.48 | +13.1 | +23.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -24.4 | 0.13 | 0.48 | +13.1 | +23.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -24.4 | 0.13 | 0.48 | +13.1 | +23.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 20.0% | -23.8 | 0.16 | 0.66 | +9.7 | +16.7 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -24.4 | 0.13 | 0.48 | +13.1 | +23.7 |
| `confluence_gte_60` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 0.0% | -27.2 | 0.03 | 0.12 | +18.0 | +40.1 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -100.8 | 0.00 | 0.00 | +3.2 | +136.6 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -15.8 | 0.00 | 0.00 | +13.7 | +18.6 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 0.0% | -28.1 | 0.02 | 0.12 | +17.3 | +45.0 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -24.4 | 0.13 | 0.48 | +13.1 | +23.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -15.8 | 0.00 | 0.00 | +13.7 | +18.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 20.0% | -23.8 | 0.16 | 0.66 | +9.7 | +16.7 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -24.4 | 0.13 | 0.48 | +13.1 | +23.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=1 Fav=0.0% Avg=-20.3; out_of_sample N=6 Fav=33.3% Avg=-1.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 10.0% | -8.4 | 0.26 | 0.60 | +10.8 | +13.9 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 40.0% | 25.0% | 50.0% | 25.0% | -3.2 | 0.58 | 0.58 | +8.5 | +11.0 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 70.0% | 28.6% | 42.9% | 14.3% | -4.3 | 0.49 | 0.65 | +10.8 | +15.5 |
| `stop_hunt_le_90` | 7 | S_STRANGER | 70.0% | 28.6% | 42.9% | 14.3% | -4.3 | 0.49 | 0.65 | +10.8 | +15.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 10.0% | -8.4 | 0.26 | 0.60 | +10.8 | +13.9 |
| `confluence_gte_70` | 9 | S_STRANGER | 90.0% | 22.2% | 33.3% | 11.1% | -7.0 | 0.31 | 0.62 | +11.2 | +12.0 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | -11.9 | 0.19 | 0.58 | +13.0 | +15.9 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | -12.4 | 0.24 | 0.47 | +16.9 | +16.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 70.0% | 28.6% | 42.9% | 14.3% | -4.3 | 0.49 | 0.65 | +10.8 | +15.5 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 10.0% | -8.4 | 0.26 | 0.60 | +10.8 | +13.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=-0.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | -8.3 | 0.26 | 1.05 | +15.7 | +20.4 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | -8.3 | 0.26 | 1.05 | +15.7 | +20.4 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | -8.3 | 0.26 | 1.05 | +15.7 | +20.4 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 90.9% | 20.0% | 20.0% | 20.0% | -7.1 | 0.31 | 1.10 | +16.4 | +20.4 |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | -8.3 | 0.26 | 1.05 | +15.7 | +20.4 |
| `confluence_gte_60` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 28.6% | -0.9 | 0.83 | 1.66 | +17.5 | +14.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 22.2% | -8.1 | 0.31 | 0.93 | +17.5 | +20.3 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 90.9% | 20.0% | 20.0% | 20.0% | -8.4 | 0.28 | 0.98 | +16.9 | +22.2 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | -8.3 | 0.26 | 1.05 | +15.7 | +20.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 22.2% | -8.1 | 0.31 | 0.93 | +17.5 | +20.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 90.9% | 20.0% | 20.0% | 20.0% | -7.1 | 0.31 | 1.10 | +16.4 | +20.4 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | -8.3 | 0.26 | 1.05 | +15.7 | +20.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-23.8; validation N=5 Fav=40.0% Avg=+16.7; out_of_sample N=2 Fav=0.0% Avg=-1.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 16.7% | 25.0% | 20.8% | +0.4 | 1.05 | 2.80 | +17.9 | +19.5 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 83.3% | 15.0% | 25.0% | 15.0% | -0.5 | 0.93 | 2.61 | +16.7 | +22.7 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 91.7% | 18.2% | 27.3% | 22.7% | +1.4 | 1.21 | 2.81 | +19.3 | +20.9 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 87.5% | 14.3% | 23.8% | 19.0% | -0.5 | 0.93 | 2.61 | +16.9 | +21.9 |
| `asian_range_gte_30` | 24 | S_STRANGER | 100.0% | 16.7% | 25.0% | 20.8% | +0.4 | 1.05 | 2.80 | +17.9 | +19.5 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 16.7% | 25.0% | 20.8% | +0.4 | 1.05 | 2.80 | +17.9 | +19.5 |
| `confluence_gte_70` | 15 | S_STRANGER | 62.5% | 13.3% | 20.0% | 6.7% | -2.5 | 0.70 | 2.79 | +13.8 | +20.1 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 50.0% | 16.7% | 25.0% | 25.0% | -0.1 | 0.98 | 2.62 | +19.3 | +24.5 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 33.3% | 25.0% | 37.5% | 25.0% | +7.1 | 2.57 | 4.29 | +27.3 | +17.2 |
| `ratio_le_2_and_asian_gte_30` | 20 | S_STRANGER | 83.3% | 15.0% | 25.0% | 15.0% | -0.5 | 0.93 | 2.61 | +16.7 | +22.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 45.8% | 9.1% | 18.2% | 18.2% | -3.9 | 0.54 | 2.17 | +14.8 | +26.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 87.5% | 14.3% | 23.8% | 19.0% | -0.5 | 0.93 | 2.61 | +16.9 | +21.9 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 16.7% | 25.0% | 20.8% | +0.4 | 1.05 | 2.80 | +17.9 | +19.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=15 Fav=20.0% Avg=-7.0; out_of_sample N=2 Fav=0.0% Avg=-8.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 16.7% | 27.8% | 16.7% | -9.4 | 0.45 | 1.07 | +15.4 | +14.1 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 88.9% | 12.5% | 25.0% | 12.5% | -10.9 | 0.32 | 0.89 | +13.8 | +15.3 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 94.4% | 17.6% | 29.4% | 17.6% | -7.2 | 0.53 | 1.16 | +16.1 | +14.6 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 94.4% | 11.8% | 23.5% | 11.8% | -13.1 | 0.27 | 0.82 | +13.1 | +14.7 |
| `asian_range_gte_30` | 18 | S_STRANGER | 100.0% | 16.7% | 27.8% | 16.7% | -9.4 | 0.45 | 1.07 | +15.4 | +14.1 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 16.7% | 27.8% | 16.7% | -9.4 | 0.45 | 1.07 | +15.4 | +14.1 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 16.7% | 27.8% | 16.7% | -9.4 | 0.45 | 1.07 | +15.4 | +14.1 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 83.3% | 13.3% | 26.7% | 13.3% | -10.0 | 0.35 | 0.88 | +13.6 | +16.3 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +11.0 | +41.4 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 88.9% | 12.5% | 25.0% | 12.5% | -10.9 | 0.32 | 0.89 | +13.8 | +15.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 72.2% | 7.7% | 23.1% | 7.7% | -12.0 | 0.16 | 0.47 | +11.3 | +18.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 94.4% | 11.8% | 23.5% | 11.8% | -13.1 | 0.27 | 0.82 | +13.1 | +14.7 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 16.7% | 27.8% | 16.7% | -9.4 | 0.45 | 1.07 | +15.4 | +14.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-12.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=20.0% Avg=-13.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 6.7% | -20.2 | 0.06 | 0.40 | +8.4 | +23.1 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 66.7% | 10.0% | 10.0% | 0.0% | -16.6 | 0.06 | 0.53 | +7.1 | +18.9 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 6.7% | -20.2 | 0.06 | 0.40 | +8.4 | +23.1 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 86.7% | 15.4% | 15.4% | 7.7% | -13.4 | 0.10 | 0.57 | +9.3 | +17.4 |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 6.7% | -20.2 | 0.06 | 0.40 | +8.4 | +23.1 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 6.7% | -20.2 | 0.06 | 0.40 | +8.4 | +23.1 |
| `confluence_gte_70` | 8 | S_STRANGER | 53.3% | 12.5% | 12.5% | 12.5% | -15.6 | 0.07 | 0.51 | +9.4 | +8.9 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 73.3% | 9.1% | 9.1% | 0.0% | -21.3 | 0.04 | 0.43 | +9.1 | +27.7 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -8.1 | 0.00 | 0.00 | +15.5 | +15.2 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 66.7% | 10.0% | 10.0% | 0.0% | -16.6 | 0.06 | 0.53 | +7.1 | +18.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 53.3% | 12.5% | 12.5% | 0.0% | -15.5 | 0.08 | 0.54 | +7.2 | +19.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 86.7% | 15.4% | 15.4% | 7.7% | -13.4 | 0.10 | 0.57 | +9.3 | +17.4 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 6.7% | -20.2 | 0.06 | 0.40 | +8.4 | +23.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=0.0% Avg=-10.9; validation N=3 Fav=33.3% Avg=-3.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 6.2% | 31.2% | 18.8% | -7.9 | 0.42 | 0.75 | +15.0 | +9.2 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 87.5% | 7.1% | 21.4% | 21.4% | -9.9 | 0.36 | 1.09 | +15.9 | +10.2 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 6.2% | 31.2% | 18.8% | -7.9 | 0.42 | 0.75 | +15.0 | +9.2 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 87.5% | 7.1% | 21.4% | 21.4% | -9.9 | 0.36 | 1.09 | +15.9 | +10.2 |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 6.2% | 31.2% | 18.8% | -7.9 | 0.42 | 0.75 | +15.0 | +9.2 |
| `confluence_gte_60` | 5 | S_STRANGER | 31.2% | 0.0% | 0.0% | 0.0% | -21.9 | 0.00 | 0.00 | +3.7 | +11.8 |
| `confluence_gte_70` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -16.7 | 0.00 | 0.00 | +1.4 | +21.9 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 68.8% | 9.1% | 27.3% | 9.1% | -7.0 | 0.49 | 1.32 | +17.1 | +12.0 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -18.3 | 0.00 | 0.00 | +11.4 | +22.2 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 87.5% | 7.1% | 21.4% | 21.4% | -9.9 | 0.36 | 1.09 | +15.9 | +10.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 62.5% | 10.0% | 20.0% | 10.0% | -8.6 | 0.43 | 1.73 | +17.8 | +12.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 87.5% | 7.1% | 21.4% | 21.4% | -9.9 | 0.36 | 1.09 | +15.9 | +10.2 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 6.2% | 31.2% | 18.8% | -7.9 | 0.42 | 0.75 | +15.0 | +9.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
