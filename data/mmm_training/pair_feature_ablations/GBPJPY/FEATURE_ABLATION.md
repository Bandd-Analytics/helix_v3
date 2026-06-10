# GBPJPY Pair Feature Ablation

Generated: 2026-06-09T15:36:12.666281+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | R_RUNNER | 90.0% | +18.4 | `hunt_to_ar_ratio_le_2_5` | 6 | R_RUNNER | 100.0% | +25.5 | 999.00 | 999.00 | 1 | 1 | research_only_split_fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 20 | R_RUNNER | 85.0% | +8.8 | `ratio_le_2_asian_gte_30_tdi_positive` | 11 | R_RUNNER | 100.0% | +9.8 | 999.00 | 999.00 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | R_REPEATER | 70.0% | +18.5 | `confluence_gte_60` | 8 | R_RUNNER | 87.5% | +27.2 | 9.28 | 1.33 | 1 | 1 | research_only_split_fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | R_REPEATER | 70.0% | +9.5 | `tdi_rsi_gte_50` | 7 | R_RUNNER | 85.7% | +12.9 | 46.15 | 7.69 | 1 | 1 | research_only_split_fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 10 | R_REPEATER | 70.0% | +7.2 | `hunt_to_ar_ratio_le_2_0` | 5 | R_RUNNER | 100.0% | +25.0 | 999.00 | 999.00 | 1 | 1 | research_only_split_fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 15 | R_REPEATER | 66.7% | +14.7 | `asian_range_gte_30` | 14 | R_REPEATER | 71.4% | +17.9 | 7.29 | 2.92 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 21 | R_REPEATER | 66.7% | +10.8 | `tdi_rsi_gt_signal` | 13 | R_RUNNER | 84.6% | +17.5 | 6.61 | 1.20 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | R_REPEATER | 66.7% | +6.3 | `all` | 15 | R_REPEATER | 66.7% | +6.3 | 3.94 | 1.97 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 22 | R_REPEATER | 63.6% | +7.6 | `feature_extreme_hunt_with_exception` | 18 | R_RUNNER | 77.8% | +13.7 | 5.56 | 1.59 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 16 | R_REPEATER | 62.5% | +15.0 | `tdi_rsi_gt_signal` | 6 | R_RUNNER | 100.0% | +26.8 | 999.00 | 999.00 | 1 | 1 | research_only_split_fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 18 | R_REPEATER | 61.1% | +5.6 | `hunt_to_ar_ratio_le_2_5` | 13 | R_REPEATER | 61.5% | +4.2 | 1.46 | 0.91 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 37 | R_REPEATER | 59.5% | +10.0 | `hunt_to_ar_ratio_le_2_0` | 32 | R_REPEATER | 62.5% | +11.2 | 4.07 | 2.24 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 17 | R_REPEATER | 58.8% | +8.1 | `tdi_rsi_gt_signal` | 12 | R_REPEATER | 66.7% | +13.3 | 3.34 | 1.67 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 41 | R_REPEATER | 58.5% | +7.5 | `hunt_to_ar_ratio_le_2_5` | 38 | R_REPEATER | 63.2% | +9.1 | 2.52 | 1.26 | 0 | 3 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 12 | R_REPEATER | 58.3% | +12.9 | `confluence_gte_60` | 5 | R_RUNNER | 80.0% | +32.3 | 999.00 | 999.00 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | R_REPEATER | 58.3% | +12.2 | `tdi_rsi_gt_signal` | 8 | R_REPEATER | 62.5% | +16.8 | 5.47 | 3.28 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | R_REPEATER | 57.9% | +3.9 | `tdi_rsi_gte_50` | 11 | R_RUNNER | 81.8% | +15.5 | 16.66 | 3.70 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 23 | R_REPEATER | 56.5% | +8.5 | `hunt_to_ar_ratio_le_2_0` | 11 | R_REPEATER | 72.7% | +13.0 | 5.75 | 2.16 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 16 | R_REPEATER | 56.2% | +5.5 | `all` | 16 | R_REPEATER | 56.2% | +5.5 | 2.09 | 1.25 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 33 | R_REPEATER | 54.5% | +9.3 | `asian_range_gte_30` | 24 | R_REPEATER | 58.3% | +15.1 | 3.36 | 1.92 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 30 | R_REPEATER | 53.3% | +9.1 | `hunt_to_ar_ratio_le_2_5` | 23 | R_REPEATER | 60.9% | +11.4 | 3.95 | 1.73 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | R_REPEATER | 52.9% | -3.2 | `tdi_rsi_gte_50` | 8 | R_REPEATER | 62.5% | -1.4 | 0.86 | 0.52 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 19 | R_REPEATER | 52.6% | +3.8 | `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 70.0% | +5.5 | 2.46 | 0.70 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 50 | R_REPEATER | 52.0% | +7.3 | `ratio_le_2_asian_gte_30_tdi_positive` | 13 | R_REPEATER | 53.8% | +1.5 | 1.31 | 1.13 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | R_REPEATER | 50.0% | +9.2 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 66.7% | +20.4 | 11.12 | 5.56 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 16 | R_REPEATER | 50.0% | +8.3 | `tdi_rsi_gt_signal` | 7 | R_REPEATER | 57.1% | +8.5 | 1.98 | 1.49 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 20 | R_REPEATER | 50.0% | +0.5 | `feature_momentum_breakout_exception` | 6 | R_RUNNER | 100.0% | +22.0 | 999.00 | 999.00 | 1 | 1 | research_only_split_fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 46.7% | +4.0 | `tdi_rsi_gte_50` | 11 | R_REPEATER | 54.5% | +5.3 | 1.58 | 1.32 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 46.2% | +14.6 | `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 66.7% | +29.1 | 45.83 | 9.17 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 13 | S_STRANGER | 46.2% | +7.7 | `tdi_rsi_gte_50` | 11 | R_REPEATER | 54.5% | +13.7 | 3.03 | 2.53 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 46.2% | +3.3 | `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 66.7% | +2.7 | 1.12 | 0.56 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 45.5% | +7.4 | `asian_range_gte_30` | 7 | R_REPEATER | 57.1% | +12.1 | 2.70 | 2.02 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 43.8% | +4.1 | `hunt_to_ar_ratio_le_2_0` | 8 | R_RUNNER | 75.0% | +14.4 | 8.37 | 2.79 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 43.8% | -1.2 | `feature_eurjpy_tdi50_reclaim` | 9 | R_REPEATER | 55.6% | +0.5 | 1.07 | 0.86 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 43.8% | -2.6 | `hunt_to_ar_ratio_le_2_0` | 6 | R_RUNNER | 83.3% | +11.3 | 2.81 | 0.56 | 1 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 41.7% | +0.7 | `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 50.0% | +5.7 | 2.68 | 2.68 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 40.0% | +4.0 | `feature_eurjpy_tdi50_reclaim` | 8 | R_REPEATER | 50.0% | +10.4 | 2.32 | 2.32 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 15 | S_STRANGER | 40.0% | +2.1 | `feature_eurjpy_tdi50_reclaim` | 5 | R_REPEATER | 60.0% | +11.4 | 999.00 | 999.00 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 28 | S_STRANGER | 39.3% | +0.8 | `feature_momentum_breakout_exception` | 5 | R_RUNNER | 80.0% | +13.4 | 4.65 | 1.16 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 28 | S_STRANGER | 39.3% | -2.9 | `confluence_gte_70` | 11 | R_REPEATER | 63.6% | +11.3 | 4.48 | 1.68 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 23 | S_STRANGER | 39.1% | -4.6 | `confluence_gte_70` | 7 | R_REPEATER | 71.4% | +2.3 | 1.23 | 0.49 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 38.5% | -1.5 | `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 50.0% | +3.1 | 1.69 | 1.12 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 38.5% | -5.5 | `confluence_gte_70` | 6 | R_REPEATER | 50.0% | +5.4 | 1.98 | 1.32 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 24 | S_STRANGER | 37.5% | +2.8 | `tdi_rsi_gt_signal` | 6 | R_RUNNER | 83.3% | +16.9 | 11.81 | 2.36 | 1 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 19 | S_STRANGER | 36.8% | +11.3 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 60.0% | +29.0 | 8.87 | 5.92 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 22 | S_STRANGER | 36.4% | -2.3 | `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 42.9% | +2.4 | 1.63 | 2.17 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 22 | S_STRANGER | 36.4% | -5.3 | `feature_momentum_breakout_exception` | 11 | S_STRANGER | 45.5% | +7.3 | 1.99 | 1.99 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 11 | S_STRANGER | 36.4% | -23.6 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 50.0% | -12.0 | 0.46 | 0.46 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 28 | S_STRANGER | 35.7% | -4.7 | `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 46.7% | +1.2 | 1.14 | 1.14 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 17 | S_STRANGER | 35.3% | -7.2 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 50.0% | +9.2 | 3.54 | 2.36 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 33 | S_STRANGER | 33.3% | -5.1 | `confluence_gte_70` | 8 | R_REPEATER | 62.5% | +2.9 | 1.38 | 0.83 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 33.3% | -11.9 | `all` | 15 | S_STRANGER | 33.3% | -11.9 | 0.48 | 0.95 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 30.0% | -3.1 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 40.0% | -6.4 | 0.53 | 0.80 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -1.3 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 25.0% | +0.5 | 1.12 | 1.50 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 20.0% | -8.2 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 40.0% | +9.9 | 3.57 | 5.35 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 20.0% | -12.5 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 40.0% | +4.3 | 3.22 | 3.22 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 30 | S_STRANGER | 16.7% | -6.8 | `tdi_rsi_gt_signal` | 12 | S_STRANGER | 25.0% | -9.6 | 0.46 | 0.92 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 14 | S_STRANGER | 7.1% | -42.7 | `stop_hunt_le_90` | 11 | S_STRANGER | 9.1% | -41.6 | 0.01 | 0.08 | 0 | 0 | fail |

## Candidate Details

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+34.8; validation N=4 Fav=100.0% Avg=+21.9; out_of_sample N=1 Fav=100.0% Avg=+30.5.

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
| `feature_extreme_hunt_with_exception` | 7 | R_RUNNER | 70.0% | 100.0% | 100.0% | 71.4% | +23.1 | 999.00 | 999.00 | +30.5 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_RUNNER | 100.0% | 90.0% | 90.0% | 50.0% | +18.4 | 69.22 | 7.69 | +25.7 | +7.2 |
| `feature_momentum_breakout_exception` | 7 | R_RUNNER | 70.0% | 85.7% | 85.7% | 42.9% | +17.3 | 45.91 | 7.65 | +25.1 | +7.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +21.9 | 999.00 | 999.00 | +33.1 | +1.3 |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=100.0% Avg=+9.4; validation N=3 Fav=100.0% Avg=+11.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | R_RUNNER | 100.0% | 85.0% | 85.0% | 35.0% | +8.8 | 11.74 | 1.38 | +20.2 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 16 | R_RUNNER | 80.0% | 93.8% | 93.8% | 31.2% | +9.0 | 999.00 | 999.00 | +19.8 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 16 | R_RUNNER | 80.0% | 93.8% | 93.8% | 31.2% | +9.0 | 999.00 | 999.00 | +19.8 | +4.8 |
| `stop_hunt_le_90` | 18 | R_RUNNER | 90.0% | 94.4% | 94.4% | 38.9% | +10.7 | 999.00 | 999.00 | +21.2 | +4.7 |
| `asian_range_gte_30` | 16 | R_RUNNER | 80.0% | 93.8% | 93.8% | 31.2% | +9.0 | 999.00 | 999.00 | +19.8 | +4.8 |
| `confluence_gte_60` | 19 | R_RUNNER | 95.0% | 84.2% | 84.2% | 36.8% | +8.8 | 11.19 | 1.40 | +20.1 | +5.3 |
| `confluence_gte_70` | 5 | R_RUNNER | 25.0% | 100.0% | 100.0% | 0.0% | +6.4 | 999.00 | 999.00 | +16.5 | +6.6 |
| `tdi_rsi_gt_signal` | 13 | R_RUNNER | 65.0% | 84.6% | 84.6% | 30.8% | +7.1 | 6.60 | 1.20 | +19.7 | +6.3 |
| `tdi_rsi_gte_50` | 9 | R_RUNNER | 45.0% | 77.8% | 77.8% | 0.0% | +4.7 | 3.57 | 1.02 | +16.0 | +8.1 |
| `ratio_le_2_and_asian_gte_30` | 16 | R_RUNNER | 80.0% | 93.8% | 93.8% | 31.2% | +9.0 | 999.00 | 999.00 | +19.8 | +4.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | R_RUNNER | 55.0% | 100.0% | 100.0% | 36.4% | +9.8 | 999.00 | 999.00 | +21.3 | +5.7 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 5.0% | 100.0% | 100.0% | 0.0% | +9.0 | 999.00 | 999.00 | +20.4 | +4.5 |
| `feature_extreme_hunt_with_exception` | 16 | R_RUNNER | 80.0% | 93.8% | 93.8% | 31.2% | +9.0 | 999.00 | 999.00 | +19.8 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 20 | R_RUNNER | 100.0% | 85.0% | 85.0% | 35.0% | +8.8 | 11.74 | 1.38 | +20.2 | +5.2 |
| `feature_momentum_breakout_exception` | 14 | R_RUNNER | 70.0% | 78.6% | 78.6% | 28.6% | +7.3 | 7.21 | 1.31 | +19.6 | +5.5 |
| `feature_eurjpy_tdi50_reclaim` | 7 | R_REPEATER | 35.0% | 71.4% | 71.4% | 0.0% | +3.5 | 2.51 | 1.00 | +14.9 | +8.7 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=100.0% Avg=+34.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-26.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 70.0% | 70.0% | 40.0% | +18.5 | 4.11 | 1.76 | +32.4 | +17.6 |
| `hunt_to_ar_ratio_le_2_0` | 9 | R_REPEATER | 90.0% | 66.7% | 66.7% | 44.4% | +15.6 | 3.37 | 1.68 | +30.7 | +17.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 70.0% | 70.0% | 40.0% | +18.5 | 4.11 | 1.76 | +32.4 | +17.6 |
| `stop_hunt_le_90` | 9 | R_REPEATER | 90.0% | 66.7% | 66.7% | 44.4% | +15.6 | 3.37 | 1.68 | +30.7 | +17.4 |
| `asian_range_gte_30` | 10 | R_REPEATER | 100.0% | 70.0% | 70.0% | 40.0% | +18.5 | 4.11 | 1.76 | +32.4 | +17.6 |
| `confluence_gte_60` | 8 | R_RUNNER | 80.0% | 87.5% | 87.5% | 50.0% | +27.2 | 9.28 | 1.33 | +37.0 | +16.7 |
| `confluence_gte_70` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +16.1 | 2.22 | 2.22 | +44.6 | +24.5 |
| `tdi_rsi_gt_signal` | 6 | R_RUNNER | 60.0% | 83.3% | 83.3% | 33.3% | +21.3 | 5.54 | 1.11 | +32.3 | +17.8 |
| `tdi_rsi_gte_50` | 6 | R_RUNNER | 60.0% | 83.3% | 83.3% | 33.3% | +21.3 | 5.54 | 1.11 | +32.3 | +17.8 |
| `ratio_le_2_and_asian_gte_30` | 9 | R_REPEATER | 90.0% | 66.7% | 66.7% | 44.4% | +15.6 | 3.37 | 1.68 | +30.7 | +17.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_RUNNER | 50.0% | 80.0% | 80.0% | 40.0% | +16.8 | 3.98 | 1.00 | +29.1 | +17.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | R_REPEATER | 90.0% | 66.7% | 66.7% | 44.4% | +15.6 | 3.37 | 1.68 | +30.7 | +17.4 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 70.0% | 70.0% | 40.0% | +18.5 | 4.11 | 1.76 | +32.4 | +17.6 |
| `feature_momentum_breakout_exception` | 4 | R_RUNNER | 40.0% | 75.0% | 75.0% | 50.0% | +20.4 | 4.10 | 1.37 | +36.0 | +18.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_RUNNER | 20.0% | 100.0% | 100.0% | 50.0% | +37.0 | 999.00 | 999.00 | +43.6 | +12.6 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=100.0% Avg=+17.6; validation N=2 Fav=50.0% Avg=+1.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 70.0% | 70.0% | 30.0% | +9.5 | 18.89 | 8.09 | +18.3 | +8.7 |
| `hunt_to_ar_ratio_le_2_0` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 50.0% | +10.5 | 12.30 | 12.30 | +20.6 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 40.0% | +9.3 | 13.51 | 9.01 | +18.0 | +7.7 |
| `stop_hunt_le_90` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 33.3% | +7.5 | 9.43 | 9.43 | +15.0 | +7.6 |
| `asian_range_gte_30` | 6 | R_REPEATER | 60.0% | 66.7% | 66.7% | 33.3% | +11.0 | 19.36 | 9.68 | +18.9 | +7.2 |
| `confluence_gte_60` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | R_REPEATER | 70.0% | 71.4% | 71.4% | 14.3% | +7.3 | 15.17 | 6.07 | +15.7 | +9.4 |
| `tdi_rsi_gte_50` | 7 | R_RUNNER | 70.0% | 85.7% | 85.7% | 28.6% | +12.9 | 46.15 | 7.69 | +21.1 | +8.1 |
| `ratio_le_2_and_asian_gte_30` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 66.7% | +14.5 | 22.75 | 11.37 | +24.4 | +3.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -2.0 | 0.00 | 0.00 | +9.8 | +7.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | R_REPEATER | 80.0% | 62.5% | 62.5% | 37.5% | +8.8 | 14.32 | 8.59 | +17.8 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 70.0% | 70.0% | 30.0% | +9.5 | 18.89 | 8.09 | +18.3 | +8.7 |
| `feature_momentum_breakout_exception` | 4 | R_RUNNER | 40.0% | 75.0% | 75.0% | 25.0% | +7.2 | 17.91 | 5.97 | +16.0 | +11.1 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_RUNNER | 30.0% | 100.0% | 100.0% | 33.3% | +10.2 | 999.00 | 999.00 | +18.3 | +8.3 |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=100.0% Avg=+24.7; validation N=2 Fav=100.0% Avg=+25.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 70.0% | 70.0% | 0.0% | +7.2 | 2.08 | 0.89 | +20.3 | +19.8 |
| `hunt_to_ar_ratio_le_2_0` | 5 | R_RUNNER | 50.0% | 100.0% | 100.0% | 0.0% | +25.0 | 999.00 | 999.00 | +32.2 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 70.0% | 70.0% | 0.0% | +7.2 | 2.08 | 0.89 | +20.3 | +19.8 |
| `stop_hunt_le_90` | 3 | R_RUNNER | 30.0% | 100.0% | 100.0% | 0.0% | +24.7 | 999.00 | 999.00 | +31.8 | +2.3 |
| `asian_range_gte_30` | 10 | R_REPEATER | 100.0% | 70.0% | 70.0% | 0.0% | +7.2 | 2.08 | 0.89 | +20.3 | +19.8 |
| `confluence_gte_60` | 10 | R_REPEATER | 100.0% | 70.0% | 70.0% | 0.0% | +7.2 | 2.08 | 0.89 | +20.3 | +19.8 |
| `confluence_gte_70` | 10 | R_REPEATER | 100.0% | 70.0% | 70.0% | 0.0% | +7.2 | 2.08 | 0.89 | +20.3 | +19.8 |
| `tdi_rsi_gt_signal` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 0.0% | +15.2 | 9.13 | 4.56 | +22.7 | +23.0 |
| `tdi_rsi_gte_50` | 9 | R_RUNNER | 90.0% | 77.8% | 77.8% | 0.0% | +13.9 | 9.49 | 2.71 | +22.2 | +14.6 |
| `ratio_le_2_and_asian_gte_30` | 5 | R_RUNNER | 50.0% | 100.0% | 100.0% | 0.0% | +25.0 | 999.00 | 999.00 | +32.2 | +8.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_RUNNER | 20.0% | 100.0% | 100.0% | 0.0% | +25.6 | 999.00 | 999.00 | +32.7 | +18.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 3 | R_RUNNER | 30.0% | 100.0% | 100.0% | 0.0% | +24.7 | 999.00 | 999.00 | +31.8 | +2.3 |
| `feature_stale_hod_exhaustion_reject` | 9 | R_REPEATER | 90.0% | 66.7% | 66.7% | 0.0% | +5.5 | 1.74 | 0.87 | +19.0 | +20.2 |
| `feature_momentum_breakout_exception` | 7 | R_REPEATER | 70.0% | 57.1% | 57.1% | 0.0% | +2.5 | 1.27 | 0.95 | +18.2 | +21.9 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 60.0% | 66.7% | 66.7% | 0.0% | +11.7 | 5.78 | 2.89 | +20.8 | +14.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=100.0% Avg=+38.7; validation N=6 Fav=50.0% Avg=+3.2; out_of_sample N=6 Fav=83.3% Avg=+25.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | R_REPEATER | 100.0% | 66.7% | 66.7% | 26.7% | +14.7 | 4.14 | 2.07 | +26.8 | +15.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | R_REPEATER | 73.3% | 63.6% | 63.6% | 18.2% | +10.7 | 2.84 | 1.62 | +23.8 | +17.6 |
| `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 80.0% | 58.3% | 58.3% | 16.7% | +9.2 | 2.58 | 1.84 | +22.2 | +17.5 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 80.0% | 58.3% | 58.3% | 16.7% | +9.2 | 2.58 | 1.84 | +22.2 | +17.5 |
| `asian_range_gte_30` | 14 | R_REPEATER | 93.3% | 71.4% | 71.4% | 28.6% | +17.9 | 7.29 | 2.92 | +28.2 | +12.2 |
| `confluence_gte_60` | 15 | R_REPEATER | 100.0% | 66.7% | 66.7% | 26.7% | +14.7 | 4.14 | 2.07 | +26.8 | +15.0 |
| `confluence_gte_70` | 9 | R_REPEATER | 60.0% | 66.7% | 66.7% | 33.3% | +14.8 | 3.20 | 1.60 | +29.6 | +16.0 |
| `tdi_rsi_gt_signal` | 11 | R_REPEATER | 73.3% | 54.5% | 54.5% | 18.2% | +7.5 | 2.18 | 1.82 | +21.2 | +18.3 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 80.0% | 66.7% | 66.7% | 25.0% | +18.3 | 6.53 | 3.27 | +29.7 | +12.6 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 66.7% | 70.0% | 70.0% | 20.0% | +14.8 | 5.44 | 2.33 | +25.4 | +14.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | R_REPEATER | 46.7% | 57.1% | 57.1% | 0.0% | +6.0 | 2.27 | 1.70 | +18.1 | +18.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 80.0% | 58.3% | 58.3% | 16.7% | +9.2 | 2.58 | 1.84 | +22.2 | +17.5 |
| `feature_stale_hod_exhaustion_reject` | 15 | R_REPEATER | 100.0% | 66.7% | 66.7% | 26.7% | +14.7 | 4.14 | 2.07 | +26.8 | +15.0 |
| `feature_momentum_breakout_exception` | 3 | R_RUNNER | 20.0% | 100.0% | 100.0% | 66.7% | +30.8 | 999.00 | 999.00 | +38.6 | +3.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_RUNNER | 20.0% | 100.0% | 100.0% | 66.7% | +30.8 | 999.00 | 999.00 | +38.6 | +3.6 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=100.0% Avg=+33.3; validation N=6 Fav=66.7% Avg=+4.5; out_of_sample N=2 Fav=100.0% Avg=+17.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | R_REPEATER | 100.0% | 66.7% | 66.7% | 38.1% | +10.8 | 3.18 | 0.91 | +25.9 | +11.1 |
| `hunt_to_ar_ratio_le_2_0` | 16 | R_REPEATER | 76.2% | 62.5% | 62.5% | 43.8% | +9.5 | 2.77 | 0.83 | +25.7 | +11.5 |
| `hunt_to_ar_ratio_le_2_5` | 18 | R_REPEATER | 85.7% | 66.7% | 66.7% | 44.4% | +9.6 | 3.01 | 0.75 | +25.5 | +10.8 |
| `stop_hunt_le_90` | 16 | R_REPEATER | 76.2% | 62.5% | 62.5% | 43.8% | +9.5 | 2.77 | 0.83 | +25.7 | +11.5 |
| `asian_range_gte_30` | 17 | R_REPEATER | 81.0% | 58.8% | 58.8% | 41.2% | +5.9 | 1.96 | 0.78 | +21.9 | +11.8 |
| `confluence_gte_60` | 21 | R_REPEATER | 100.0% | 66.7% | 66.7% | 38.1% | +10.8 | 3.18 | 0.91 | +25.9 | +11.1 |
| `confluence_gte_70` | 21 | R_REPEATER | 100.0% | 66.7% | 66.7% | 38.1% | +10.8 | 3.18 | 0.91 | +25.9 | +11.1 |
| `tdi_rsi_gt_signal` | 13 | R_RUNNER | 61.9% | 84.6% | 84.6% | 23.1% | +17.5 | 6.61 | 1.20 | +29.7 | +8.0 |
| `tdi_rsi_gte_50` | 13 | R_RUNNER | 61.9% | 76.9% | 76.9% | 30.8% | +14.7 | 3.81 | 0.76 | +30.1 | +10.5 |
| `ratio_le_2_and_asian_gte_30` | 12 | R_REPEATER | 57.1% | 50.0% | 50.0% | 50.0% | +2.2 | 1.30 | 0.65 | +20.0 | +12.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_RUNNER | 28.6% | 83.3% | 83.3% | 50.0% | +13.3 | 4.45 | 0.89 | +25.4 | +5.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | R_REPEATER | 76.2% | 62.5% | 62.5% | 43.8% | +9.5 | 2.77 | 0.83 | +25.7 | +11.5 |
| `feature_stale_hod_exhaustion_reject` | 21 | R_REPEATER | 100.0% | 66.7% | 66.7% | 38.1% | +10.8 | 3.18 | 0.91 | +25.9 | +11.1 |
| `feature_momentum_breakout_exception` | 4 | R_RUNNER | 19.0% | 100.0% | 100.0% | 50.0% | +38.4 | 999.00 | 999.00 | +48.0 | +6.0 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_RUNNER | 19.0% | 100.0% | 100.0% | 50.0% | +38.4 | 999.00 | 999.00 | +48.0 | +6.0 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=12 Fav=58.3% Avg=+5.8; validation N=3 Fav=100.0% Avg=+8.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | R_REPEATER | 100.0% | 66.7% | 66.7% | 13.3% | +6.3 | 3.94 | 1.97 | +21.5 | +11.2 |
| `hunt_to_ar_ratio_le_2_0` | 11 | R_REPEATER | 73.3% | 63.6% | 63.6% | 9.1% | +6.2 | 3.33 | 1.90 | +22.0 | +10.6 |
| `hunt_to_ar_ratio_le_2_5` | 13 | R_REPEATER | 86.7% | 61.5% | 61.5% | 7.7% | +5.2 | 3.12 | 1.95 | +21.5 | +11.3 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 80.0% | 66.7% | 66.7% | 8.3% | +7.0 | 3.90 | 1.95 | +22.4 | +11.3 |
| `asian_range_gte_30` | 14 | R_REPEATER | 93.3% | 64.3% | 64.3% | 14.3% | +5.5 | 3.42 | 1.90 | +21.1 | +10.7 |
| `confluence_gte_60` | 15 | R_REPEATER | 100.0% | 66.7% | 66.7% | 13.3% | +6.3 | 3.94 | 1.97 | +21.5 | +11.2 |
| `confluence_gte_70` | 15 | R_REPEATER | 100.0% | 66.7% | 66.7% | 13.3% | +6.3 | 3.94 | 1.97 | +21.5 | +11.2 |
| `tdi_rsi_gt_signal` | 2 | R_RUNNER | 13.3% | 100.0% | 100.0% | 50.0% | +22.1 | 999.00 | 999.00 | +35.1 | +3.4 |
| `tdi_rsi_gte_50` | 9 | R_REPEATER | 60.0% | 55.6% | 55.6% | 0.0% | +4.7 | 2.51 | 2.01 | +21.0 | +13.9 |
| `ratio_le_2_and_asian_gte_30` | 11 | R_REPEATER | 73.3% | 63.6% | 63.6% | 9.1% | +6.2 | 3.33 | 1.90 | +22.0 | +10.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_RUNNER | 13.3% | 100.0% | 100.0% | 50.0% | +22.1 | 999.00 | 999.00 | +35.1 | +3.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 80.0% | 66.7% | 66.7% | 8.3% | +7.0 | 3.90 | 1.95 | +22.4 | +11.3 |
| `feature_stale_hod_exhaustion_reject` | 15 | R_REPEATER | 100.0% | 66.7% | 66.7% | 13.3% | +6.3 | 3.94 | 1.97 | +21.5 | +11.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=11 Fav=72.7% Avg=+10.6; validation N=6 Fav=100.0% Avg=+23.8; out_of_sample N=1 Fav=0.0% Avg=-12.9.

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

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=100.0% Avg=+28.6; validation N=2 Fav=100.0% Avg=+19.2; out_of_sample N=1 Fav=100.0% Avg=+36.5.

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

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=71.4% Avg=+2.7; out_of_sample N=6 Fav=50.0% Avg=+5.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | R_REPEATER | 100.0% | 61.1% | 61.1% | 16.7% | +5.6 | 1.71 | 1.09 | +22.0 | +18.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 55.6% | 60.0% | 60.0% | 20.0% | +1.6 | 1.14 | 0.76 | +18.8 | +24.9 |
| `hunt_to_ar_ratio_le_2_5` | 13 | R_REPEATER | 72.2% | 61.5% | 61.5% | 15.4% | +4.2 | 1.46 | 0.91 | +21.4 | +20.7 |
| `stop_hunt_le_90` | 11 | R_REPEATER | 61.1% | 54.5% | 54.5% | 18.2% | +1.3 | 1.12 | 0.94 | +19.1 | +23.3 |
| `asian_range_gte_30` | 15 | R_REPEATER | 83.3% | 60.0% | 60.0% | 20.0% | +7.2 | 1.96 | 1.31 | +22.9 | +15.5 |
| `confluence_gte_60` | 18 | R_REPEATER | 100.0% | 61.1% | 61.1% | 16.7% | +5.6 | 1.71 | 1.09 | +22.0 | +18.3 |
| `confluence_gte_70` | 18 | R_REPEATER | 100.0% | 61.1% | 61.1% | 16.7% | +5.6 | 1.71 | 1.09 | +22.0 | +18.3 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 33.3% | 33.3% | 33.3% | 0.0% | -12.0 | 0.28 | 0.56 | +13.8 | +22.8 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 61.1% | 45.5% | 45.5% | 0.0% | -5.2 | 0.56 | 0.67 | +16.6 | +23.7 |
| `ratio_le_2_and_asian_gte_30` | 7 | R_REPEATER | 38.9% | 57.1% | 57.1% | 28.6% | +3.4 | 1.27 | 0.95 | +19.4 | +21.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 0.0% | -18.2 | 0.28 | 0.56 | +12.3 | +33.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | R_REPEATER | 61.1% | 54.5% | 54.5% | 18.2% | +1.3 | 1.12 | 0.94 | +19.1 | +23.3 |
| `feature_stale_hod_exhaustion_reject` | 18 | R_REPEATER | 100.0% | 61.1% | 61.1% | 16.7% | +5.6 | 1.71 | 1.09 | +22.0 | +18.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=50.0% Avg=+5.6; validation N=17 Fav=64.7% Avg=+7.6; out_of_sample N=13 Fav=61.5% Avg=+16.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | R_REPEATER | 100.0% | 59.5% | 59.5% | 27.0% | +10.0 | 3.22 | 2.05 | +24.4 | +13.1 |
| `hunt_to_ar_ratio_le_2_0` | 32 | R_REPEATER | 86.5% | 62.5% | 62.5% | 31.2% | +11.2 | 4.07 | 2.24 | +25.3 | +11.9 |
| `hunt_to_ar_ratio_le_2_5` | 36 | R_REPEATER | 97.3% | 58.3% | 58.3% | 27.8% | +9.9 | 3.12 | 2.08 | +24.4 | +13.3 |
| `stop_hunt_le_90` | 34 | R_REPEATER | 91.9% | 61.8% | 61.8% | 29.4% | +11.5 | 3.95 | 2.26 | +25.3 | +12.0 |
| `asian_range_gte_30` | 31 | R_REPEATER | 83.8% | 58.1% | 58.1% | 32.3% | +9.5 | 2.94 | 1.96 | +24.5 | +13.6 |
| `confluence_gte_60` | 37 | R_REPEATER | 100.0% | 59.5% | 59.5% | 27.0% | +10.0 | 3.22 | 2.05 | +24.4 | +13.1 |
| `confluence_gte_70` | 37 | R_REPEATER | 100.0% | 59.5% | 59.5% | 27.0% | +10.0 | 3.22 | 2.05 | +24.4 | +13.1 |
| `tdi_rsi_gt_signal` | 16 | R_REPEATER | 43.2% | 56.2% | 56.2% | 18.8% | +12.0 | 3.70 | 2.87 | +26.6 | +15.6 |
| `tdi_rsi_gte_50` | 19 | R_REPEATER | 51.4% | 52.6% | 52.6% | 10.5% | +8.7 | 2.64 | 2.38 | +24.8 | +17.7 |
| `ratio_le_2_and_asian_gte_30` | 28 | R_REPEATER | 75.7% | 60.7% | 60.7% | 35.7% | +11.2 | 3.69 | 2.17 | +25.6 | +12.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | R_REPEATER | 29.7% | 54.5% | 54.5% | 27.3% | +13.2 | 4.90 | 4.09 | +26.6 | +14.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 34 | R_REPEATER | 91.9% | 61.8% | 61.8% | 29.4% | +11.5 | 3.95 | 2.26 | +25.3 | +12.0 |
| `feature_stale_hod_exhaustion_reject` | 37 | R_REPEATER | 100.0% | 59.5% | 59.5% | 27.0% | +10.0 | 3.22 | 2.05 | +24.4 | +13.1 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 2.7% | 0.0% | 0.0% | 0.0% | -14.4 | 0.00 | 0.00 | +11.5 | +17.9 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=75.0% Avg=+13.4; validation N=4 Fav=50.0% Avg=+13.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | R_REPEATER | 100.0% | 58.8% | 58.8% | 35.3% | +8.1 | 1.92 | 1.34 | +23.2 | +16.6 |
| `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 70.6% | 66.7% | 66.7% | 33.3% | +12.6 | 3.21 | 1.60 | +24.6 | +14.6 |
| `hunt_to_ar_ratio_le_2_5` | 17 | R_REPEATER | 100.0% | 58.8% | 58.8% | 35.3% | +8.1 | 1.92 | 1.34 | +23.2 | +16.6 |
| `stop_hunt_le_90` | 13 | R_REPEATER | 76.5% | 61.5% | 61.5% | 30.8% | +11.5 | 3.15 | 1.97 | +23.7 | +13.8 |
| `asian_range_gte_30` | 16 | R_REPEATER | 94.1% | 62.5% | 62.5% | 37.5% | +8.7 | 1.93 | 1.16 | +23.8 | +17.4 |
| `confluence_gte_60` | 17 | R_REPEATER | 100.0% | 58.8% | 58.8% | 35.3% | +8.1 | 1.92 | 1.34 | +23.2 | +16.6 |
| `confluence_gte_70` | 17 | R_REPEATER | 100.0% | 58.8% | 58.8% | 35.3% | +8.1 | 1.92 | 1.34 | +23.2 | +16.6 |
| `tdi_rsi_gt_signal` | 12 | R_REPEATER | 70.6% | 66.7% | 66.7% | 33.3% | +13.3 | 3.34 | 1.67 | +25.3 | +14.7 |
| `tdi_rsi_gte_50` | 15 | R_REPEATER | 88.2% | 66.7% | 66.7% | 40.0% | +10.9 | 2.31 | 1.16 | +26.0 | +15.7 |
| `ratio_le_2_and_asian_gte_30` | 12 | R_REPEATER | 70.6% | 66.7% | 66.7% | 33.3% | +12.6 | 3.21 | 1.60 | +24.6 | +14.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | R_REPEATER | 64.7% | 63.6% | 63.6% | 27.3% | +11.3 | 2.83 | 1.61 | +24.4 | +15.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | R_REPEATER | 76.5% | 61.5% | 61.5% | 30.8% | +11.5 | 3.15 | 1.97 | +23.7 | +13.8 |
| `feature_stale_hod_exhaustion_reject` | 17 | R_REPEATER | 100.0% | 58.8% | 58.8% | 35.3% | +8.1 | 1.92 | 1.34 | +23.2 | +16.6 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 11.8% | 50.0% | 50.0% | 50.0% | +12.1 | 3.79 | 3.79 | +17.3 | +12.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 5.9% | 100.0% | 100.0% | 100.0% | +33.0 | 999.00 | 999.00 | +33.1 | +0.1 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=66.7% Avg=+6.2; validation N=22 Fav=59.1% Avg=+7.3; out_of_sample N=10 Fav=70.0% Avg=+14.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 41 | R_REPEATER | 100.0% | 58.5% | 58.5% | 19.5% | +7.5 | 2.14 | 1.34 | +24.8 | +16.7 |
| `hunt_to_ar_ratio_le_2_0` | 31 | R_REPEATER | 75.6% | 58.1% | 58.1% | 22.6% | +9.2 | 2.65 | 1.62 | +26.1 | +14.6 |
| `hunt_to_ar_ratio_le_2_5` | 38 | R_REPEATER | 92.7% | 63.2% | 63.2% | 21.1% | +9.1 | 2.52 | 1.26 | +26.0 | +15.9 |
| `stop_hunt_le_90` | 35 | R_REPEATER | 85.4% | 60.0% | 60.0% | 20.0% | +7.5 | 2.14 | 1.23 | +25.2 | +16.1 |
| `asian_range_gte_30` | 39 | R_REPEATER | 95.1% | 59.0% | 59.0% | 17.9% | +7.4 | 2.10 | 1.28 | +24.7 | +16.4 |
| `confluence_gte_60` | 41 | R_REPEATER | 100.0% | 58.5% | 58.5% | 19.5% | +7.5 | 2.14 | 1.34 | +24.8 | +16.7 |
| `confluence_gte_70` | 41 | R_REPEATER | 100.0% | 58.5% | 58.5% | 19.5% | +7.5 | 2.14 | 1.34 | +24.8 | +16.7 |
| `tdi_rsi_gt_signal` | 11 | R_REPEATER | 26.8% | 54.5% | 54.5% | 0.0% | +5.9 | 1.83 | 1.52 | +24.7 | +15.8 |
| `tdi_rsi_gte_50` | 36 | R_REPEATER | 87.8% | 58.3% | 58.3% | 16.7% | +8.2 | 2.37 | 1.47 | +25.1 | +17.1 |
| `ratio_le_2_and_asian_gte_30` | 29 | R_REPEATER | 70.7% | 58.6% | 58.6% | 20.7% | +9.1 | 2.61 | 1.53 | +26.1 | +14.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 19.5% | 62.5% | 62.5% | 0.0% | +11.1 | 2.84 | 1.70 | +31.0 | +11.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 35 | R_REPEATER | 85.4% | 60.0% | 60.0% | 20.0% | +7.5 | 2.14 | 1.23 | +25.2 | +16.1 |
| `feature_stale_hod_exhaustion_reject` | 41 | R_REPEATER | 100.0% | 58.5% | 58.5% | 19.5% | +7.5 | 2.14 | 1.34 | +24.8 | +16.7 |
| `feature_momentum_breakout_exception` | 4 | R_RUNNER | 9.8% | 100.0% | 100.0% | 50.0% | +15.3 | 999.00 | 999.00 | +23.3 | +3.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_RUNNER | 4.9% | 100.0% | 100.0% | 50.0% | +17.7 | 999.00 | 999.00 | +26.1 | +3.6 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+19.6; validation N=2 Fav=100.0% Avg=+51.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 58.3% | +12.9 | 7.53 | 1.08 | +30.3 | +11.3 |
| `hunt_to_ar_ratio_le_2_0` | 9 | R_RUNNER | 75.0% | 77.8% | 77.8% | 44.4% | +17.3 | 7.53 | 1.08 | +35.5 | +12.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 83.3% | 70.0% | 70.0% | 50.0% | +15.5 | 7.53 | 1.08 | +33.2 | +11.8 |
| `stop_hunt_le_90` | 9 | R_RUNNER | 75.0% | 77.8% | 77.8% | 44.4% | +17.3 | 7.53 | 1.08 | +35.5 | +12.1 |
| `asian_range_gte_30` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 58.3% | +12.9 | 7.53 | 1.08 | +30.3 | +11.3 |
| `confluence_gte_60` | 5 | R_RUNNER | 41.7% | 80.0% | 80.0% | 60.0% | +32.3 | 999.00 | 999.00 | +49.9 | +14.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 10 | R_REPEATER | 83.3% | 60.0% | 60.0% | 50.0% | +14.6 | 7.14 | 1.19 | +32.5 | +12.4 |
| `tdi_rsi_gte_50` | 8 | R_RUNNER | 66.7% | 75.0% | 75.0% | 62.5% | +13.7 | 999.00 | 999.00 | +32.3 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 9 | R_RUNNER | 75.0% | 77.8% | 77.8% | 44.4% | +17.3 | 7.53 | 1.08 | +35.5 | +12.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_RUNNER | 66.7% | 75.0% | 75.0% | 37.5% | +18.3 | 7.14 | 1.19 | +36.7 | +13.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | R_RUNNER | 75.0% | 77.8% | 77.8% | 44.4% | +17.3 | 7.53 | 1.08 | +35.5 | +12.1 |
| `feature_stale_hod_exhaustion_reject` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 58.3% | +12.9 | 7.53 | 1.08 | +30.3 | +11.3 |
| `feature_momentum_breakout_exception` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 0.0% | -5.1 | 0.36 | 0.18 | +12.4 | +13.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_RUNNER | 16.7% | 100.0% | 100.0% | 0.0% | +4.3 | 999.00 | 999.00 | +16.8 | +8.5 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+16.0; validation N=3 Fav=66.7% Avg=+18.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 41.7% | +12.2 | 3.19 | 2.28 | +28.6 | +14.5 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 42.9% | +2.9 | 1.31 | 1.75 | +27.1 | +16.5 |
| `hunt_to_ar_ratio_le_2_5` | 9 | R_REPEATER | 75.0% | 55.6% | 55.6% | 44.4% | +10.4 | 2.45 | 1.96 | +29.8 | +14.1 |
| `stop_hunt_le_90` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 44.4% | +7.3 | 1.98 | 2.48 | +28.8 | +14.0 |
| `asian_range_gte_30` | 9 | R_REPEATER | 75.0% | 55.6% | 55.6% | 44.4% | +10.4 | 2.45 | 1.96 | +29.8 | +14.1 |
| `confluence_gte_60` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 41.7% | +12.2 | 3.19 | 2.28 | +28.6 | +14.5 |
| `confluence_gte_70` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 33.3% | +17.6 | 26.12 | 13.06 | +25.0 | +15.8 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 66.7% | 62.5% | 62.5% | 37.5% | +16.8 | 5.47 | 3.28 | +32.7 | +12.8 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -14.8 | 0.00 | 0.00 | +17.3 | +22.5 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 42.9% | +2.9 | 1.31 | 1.75 | +27.1 | +16.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 33.3% | 50.0% | 50.0% | 50.0% | +12.1 | 2.74 | 2.74 | +37.3 | +14.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | R_REPEATER | 91.7% | 54.5% | 54.5% | 45.5% | +11.0 | 2.80 | 2.34 | +28.8 | +14.9 |
| `feature_stale_hod_exhaustion_reject` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 41.7% | +12.2 | 3.19 | 2.28 | +28.6 | +14.5 |
| `feature_momentum_breakout_exception` | 6 | R_REPEATER | 50.0% | 50.0% | 50.0% | 16.7% | +8.4 | 2.35 | 2.35 | +21.9 | +16.6 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=100.0% Avg=+23.0; out_of_sample N=7 Fav=71.4% Avg=+11.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | R_REPEATER | 100.0% | 57.9% | 57.9% | 10.5% | +3.9 | 1.49 | 1.08 | +19.5 | +15.5 |
| `hunt_to_ar_ratio_le_2_0` | 15 | R_REPEATER | 78.9% | 53.3% | 53.3% | 13.3% | +3.2 | 1.34 | 1.17 | +20.9 | +13.1 |
| `hunt_to_ar_ratio_le_2_5` | 16 | R_REPEATER | 84.2% | 56.2% | 56.2% | 12.5% | +3.7 | 1.43 | 1.11 | +20.5 | +13.8 |
| `stop_hunt_le_90` | 15 | R_REPEATER | 78.9% | 53.3% | 53.3% | 13.3% | +3.2 | 1.34 | 1.17 | +20.9 | +13.1 |
| `asian_range_gte_30` | 17 | R_REPEATER | 89.5% | 58.8% | 58.8% | 11.8% | +3.7 | 1.44 | 1.01 | +20.2 | +16.3 |
| `confluence_gte_60` | 19 | R_REPEATER | 100.0% | 57.9% | 57.9% | 10.5% | +3.9 | 1.49 | 1.08 | +19.5 | +15.5 |
| `confluence_gte_70` | 19 | R_REPEATER | 100.0% | 57.9% | 57.9% | 10.5% | +3.9 | 1.49 | 1.08 | +19.5 | +15.5 |
| `tdi_rsi_gt_signal` | 5 | R_RUNNER | 26.3% | 80.0% | 80.0% | 20.0% | +15.4 | 8.12 | 2.03 | +23.1 | +16.5 |
| `tdi_rsi_gte_50` | 11 | R_RUNNER | 57.9% | 81.8% | 81.8% | 9.1% | +15.5 | 16.66 | 3.70 | +26.2 | +14.7 |
| `ratio_le_2_and_asian_gte_30` | 13 | R_REPEATER | 68.4% | 53.8% | 53.8% | 15.4% | +2.9 | 1.28 | 1.10 | +22.1 | +13.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_RUNNER | 10.5% | 100.0% | 100.0% | 50.0% | +31.5 | 999.00 | 999.00 | +36.4 | +4.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | R_REPEATER | 78.9% | 53.3% | 53.3% | 13.3% | +3.2 | 1.34 | 1.17 | +20.9 | +13.1 |
| `feature_stale_hod_exhaustion_reject` | 19 | R_REPEATER | 100.0% | 57.9% | 57.9% | 10.5% | +3.9 | 1.49 | 1.08 | +19.5 | +15.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=70.0% Avg=+9.3; validation N=1 Fav=100.0% Avg=+49.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | R_REPEATER | 100.0% | 56.5% | 56.5% | 21.7% | +8.5 | 3.10 | 2.39 | +25.3 | +10.5 |
| `hunt_to_ar_ratio_le_2_0` | 11 | R_REPEATER | 47.8% | 72.7% | 72.7% | 36.4% | +13.0 | 5.75 | 2.16 | +28.3 | +10.1 |
| `hunt_to_ar_ratio_le_2_5` | 22 | R_REPEATER | 95.7% | 59.1% | 59.1% | 22.7% | +9.0 | 3.27 | 2.26 | +25.7 | +10.4 |
| `stop_hunt_le_90` | 14 | R_REPEATER | 60.9% | 64.3% | 64.3% | 28.6% | +11.6 | 6.23 | 3.46 | +25.6 | +9.7 |
| `asian_range_gte_30` | 18 | R_REPEATER | 78.3% | 61.1% | 61.1% | 27.8% | +9.6 | 2.98 | 1.90 | +27.8 | +10.9 |
| `confluence_gte_60` | 23 | R_REPEATER | 100.0% | 56.5% | 56.5% | 21.7% | +8.5 | 3.10 | 2.39 | +25.3 | +10.5 |
| `confluence_gte_70` | 23 | R_REPEATER | 100.0% | 56.5% | 56.5% | 21.7% | +8.5 | 3.10 | 2.39 | +25.3 | +10.5 |
| `tdi_rsi_gt_signal` | 4 | R_RUNNER | 17.4% | 75.0% | 75.0% | 0.0% | +2.3 | 2.13 | 0.71 | +18.2 | +10.7 |
| `tdi_rsi_gte_50` | 20 | R_REPEATER | 87.0% | 50.0% | 50.0% | 10.0% | +3.6 | 1.77 | 1.77 | +22.2 | +11.7 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 43.5% | 70.0% | 70.0% | 40.0% | +13.5 | 5.49 | 2.35 | +29.3 | +10.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -8.2 | 0.00 | 0.00 | +5.1 | +23.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | R_REPEATER | 60.9% | 64.3% | 64.3% | 28.6% | +11.6 | 6.23 | 3.46 | +25.6 | +9.7 |
| `feature_stale_hod_exhaustion_reject` | 23 | R_REPEATER | 100.0% | 56.5% | 56.5% | 21.7% | +8.5 | 3.10 | 2.39 | +25.3 | +10.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=77.8% Avg=+10.4; out_of_sample N=7 Fav=28.6% Avg=-0.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | R_REPEATER | 100.0% | 56.2% | 62.5% | 25.0% | +5.5 | 2.09 | 1.25 | +21.4 | +11.9 |
| `hunt_to_ar_ratio_le_2_0` | 13 | R_REPEATER | 81.2% | 53.8% | 61.5% | 23.1% | +2.2 | 1.37 | 0.85 | +18.1 | +14.0 |
| `hunt_to_ar_ratio_le_2_5` | 15 | R_REPEATER | 93.8% | 53.3% | 60.0% | 20.0% | +5.4 | 1.99 | 1.33 | +21.0 | +12.4 |
| `stop_hunt_le_90` | 14 | R_REPEATER | 87.5% | 50.0% | 57.1% | 21.4% | +1.9 | 1.34 | 1.00 | +18.4 | +13.3 |
| `asian_range_gte_30` | 11 | R_REPEATER | 68.8% | 54.5% | 54.5% | 18.2% | +6.2 | 1.86 | 1.55 | +22.6 | +15.3 |
| `confluence_gte_60` | 16 | R_REPEATER | 100.0% | 56.2% | 62.5% | 25.0% | +5.5 | 2.09 | 1.25 | +21.4 | +11.9 |
| `confluence_gte_70` | 16 | R_REPEATER | 100.0% | 56.2% | 62.5% | 25.0% | +5.5 | 2.09 | 1.25 | +21.4 | +11.9 |
| `tdi_rsi_gt_signal` | 16 | R_REPEATER | 100.0% | 56.2% | 62.5% | 25.0% | +5.5 | 2.09 | 1.25 | +21.4 | +11.9 |
| `tdi_rsi_gte_50` | 10 | R_REPEATER | 62.5% | 50.0% | 50.0% | 20.0% | +6.0 | 1.75 | 1.75 | +23.6 | +13.9 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 62.5% | 50.0% | 50.0% | 20.0% | +1.5 | 1.19 | 1.19 | +19.1 | +16.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | R_REPEATER | 62.5% | 50.0% | 50.0% | 20.0% | +1.5 | 1.19 | 1.19 | +19.1 | +16.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | R_REPEATER | 87.5% | 50.0% | 57.1% | 21.4% | +1.9 | 1.34 | 1.00 | +18.4 | +13.3 |
| `feature_stale_hod_exhaustion_reject` | 16 | R_REPEATER | 100.0% | 56.2% | 62.5% | 25.0% | +5.5 | 2.09 | 1.25 | +21.4 | +11.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=100.0% Avg=+59.7; validation N=11 Fav=63.6% Avg=+16.4; out_of_sample N=11 Fav=45.5% Avg=+5.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | R_REPEATER | 100.0% | 54.5% | 54.5% | 12.1% | +9.3 | 2.15 | 1.55 | +30.3 | +17.9 |
| `hunt_to_ar_ratio_le_2_0` | 21 | R_REPEATER | 63.6% | 52.4% | 52.4% | 9.5% | +7.0 | 1.77 | 1.28 | +27.6 | +19.3 |
| `hunt_to_ar_ratio_le_2_5` | 28 | R_REPEATER | 84.8% | 50.0% | 50.0% | 14.3% | +6.4 | 1.67 | 1.43 | +27.6 | +18.8 |
| `stop_hunt_le_90` | 25 | R_REPEATER | 75.8% | 52.0% | 52.0% | 12.0% | +5.8 | 1.57 | 1.21 | +27.3 | +19.9 |
| `asian_range_gte_30` | 24 | R_REPEATER | 72.7% | 58.3% | 58.3% | 12.5% | +15.1 | 3.36 | 1.92 | +34.5 | +15.1 |
| `confluence_gte_60` | 33 | R_REPEATER | 100.0% | 54.5% | 54.5% | 12.1% | +9.3 | 2.15 | 1.55 | +30.3 | +17.9 |
| `confluence_gte_70` | 33 | R_REPEATER | 100.0% | 54.5% | 54.5% | 12.1% | +9.3 | 2.15 | 1.55 | +30.3 | +17.9 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 9.1% | 33.3% | 33.3% | 0.0% | +3.0 | 1.41 | 2.83 | +21.9 | +20.6 |
| `tdi_rsi_gte_50` | 28 | R_REPEATER | 84.8% | 57.1% | 57.1% | 10.7% | +14.2 | 3.49 | 2.18 | +32.6 | +15.2 |
| `ratio_le_2_and_asian_gte_30` | 17 | R_REPEATER | 51.5% | 52.9% | 52.9% | 11.8% | +9.9 | 2.20 | 1.47 | +30.6 | +16.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | R_REPEATER | 78.8% | 53.8% | 53.8% | 11.5% | +5.6 | 1.57 | 1.12 | +26.7 | +20.1 |
| `feature_stale_hod_exhaustion_reject` | 33 | R_REPEATER | 100.0% | 54.5% | 54.5% | 12.1% | +9.3 | 2.15 | 1.55 | +30.3 | +17.9 |
| `feature_momentum_breakout_exception` | 2 | R_RUNNER | 6.1% | 100.0% | 100.0% | 0.0% | +59.7 | 999.00 | 999.00 | +85.2 | +5.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_RUNNER | 6.1% | 100.0% | 100.0% | 0.0% | +59.7 | 999.00 | 999.00 | +85.2 | +5.3 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=19 Fav=63.2% Avg=+14.6; validation N=4 Fav=50.0% Avg=-4.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | R_REPEATER | 100.0% | 53.3% | 60.0% | 20.0% | +9.1 | 3.09 | 1.89 | +21.8 | +12.8 |
| `hunt_to_ar_ratio_le_2_0` | 16 | R_REPEATER | 53.3% | 56.2% | 62.5% | 18.8% | +8.1 | 2.54 | 1.52 | +22.5 | +12.2 |
| `hunt_to_ar_ratio_le_2_5` | 23 | R_REPEATER | 76.7% | 60.9% | 69.6% | 21.7% | +11.4 | 3.95 | 1.73 | +22.7 | +12.3 |
| `stop_hunt_le_90` | 20 | R_REPEATER | 66.7% | 55.0% | 60.0% | 15.0% | +11.1 | 5.77 | 3.85 | +21.7 | +9.0 |
| `asian_range_gte_30` | 24 | R_REPEATER | 80.0% | 58.3% | 66.7% | 25.0% | +10.7 | 3.72 | 1.63 | +22.9 | +12.0 |
| `confluence_gte_60` | 30 | R_REPEATER | 100.0% | 53.3% | 60.0% | 20.0% | +9.1 | 3.09 | 1.89 | +21.8 | +12.8 |
| `confluence_gte_70` | 30 | R_REPEATER | 100.0% | 53.3% | 60.0% | 20.0% | +9.1 | 3.09 | 1.89 | +21.8 | +12.8 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 56.7% | 41.2% | 47.1% | 11.8% | +2.1 | 1.29 | 1.45 | +17.3 | +17.6 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 63.3% | 42.1% | 42.1% | 15.8% | +2.6 | 1.41 | 1.76 | +18.6 | +15.9 |
| `ratio_le_2_and_asian_gte_30` | 16 | R_REPEATER | 53.3% | 56.2% | 62.5% | 18.8% | +8.1 | 2.54 | 1.52 | +22.5 | +12.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 30.0% | 33.3% | 44.4% | 11.1% | -0.5 | 0.95 | 1.19 | +17.3 | +16.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | R_REPEATER | 66.7% | 55.0% | 60.0% | 15.0% | +11.1 | 5.77 | 3.85 | +21.7 | +9.0 |
| `feature_stale_hod_exhaustion_reject` | 30 | R_REPEATER | 100.0% | 53.3% | 60.0% | 20.0% | +9.1 | 3.09 | 1.89 | +21.8 | +12.8 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 3.3% | 100.0% | 100.0% | 0.0% | +24.7 | 999.00 | 999.00 | +27.9 | +6.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 3.3% | 100.0% | 100.0% | 0.0% | +24.7 | 999.00 | 999.00 | +27.9 | +6.6 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=100.0% Avg=+16.5; validation N=4 Fav=50.0% Avg=-13.0; out_of_sample N=2 Fav=50.0% Avg=+4.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | R_REPEATER | 100.0% | 52.9% | 52.9% | 11.8% | -3.2 | 0.74 | 0.66 | +15.8 | +17.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 64.7% | 45.5% | 45.5% | 0.0% | -7.1 | 0.46 | 0.55 | +14.5 | +19.5 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 82.4% | 42.9% | 42.9% | 7.1% | -8.3 | 0.44 | 0.58 | +13.8 | +18.7 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 70.6% | 41.7% | 41.7% | 0.0% | -7.5 | 0.42 | 0.59 | +13.7 | +20.9 |
| `asian_range_gte_30` | 16 | R_REPEATER | 94.1% | 56.2% | 56.2% | 12.5% | -2.6 | 0.78 | 0.61 | +16.5 | +15.8 |
| `confluence_gte_60` | 16 | R_REPEATER | 94.1% | 50.0% | 50.0% | 12.5% | -4.5 | 0.65 | 0.65 | +15.3 | +17.7 |
| `confluence_gte_70` | 11 | R_REPEATER | 64.7% | 54.5% | 54.5% | 9.1% | -1.8 | 0.82 | 0.68 | +16.1 | +16.1 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -23.7 | 0.00 | 0.00 | +1.9 | +40.4 |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 47.1% | 62.5% | 62.5% | 0.0% | -1.4 | 0.86 | 0.52 | +16.0 | +18.8 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 64.7% | 45.5% | 45.5% | 0.0% | -7.1 | 0.46 | 0.55 | +14.5 | +19.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -23.7 | 0.00 | 0.00 | +1.9 | +40.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 64.7% | 45.5% | 45.5% | 0.0% | -7.1 | 0.46 | 0.55 | +14.5 | +19.5 |
| `feature_stale_hod_exhaustion_reject` | 17 | R_REPEATER | 100.0% | 52.9% | 52.9% | 11.8% | -3.2 | 0.74 | 0.66 | +15.8 | +17.0 |
| `feature_momentum_breakout_exception` | 4 | R_RUNNER | 23.5% | 75.0% | 75.0% | 25.0% | +14.2 | 5.83 | 1.94 | +21.4 | +14.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 5.9% | 100.0% | 100.0% | 0.0% | +21.1 | 999.00 | 999.00 | +24.0 | +9.6 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=75.0% Avg=+4.0; validation N=2 Fav=50.0% Avg=+11.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | R_REPEATER | 100.0% | 52.6% | 57.9% | 15.8% | +3.8 | 1.53 | 0.83 | +19.2 | +18.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 52.6% | 70.0% | 70.0% | 20.0% | +5.5 | 2.46 | 0.70 | +18.1 | +16.3 |
| `hunt_to_ar_ratio_le_2_5` | 16 | R_REPEATER | 84.2% | 56.2% | 62.5% | 18.8% | +4.7 | 1.68 | 0.67 | +19.8 | +18.1 |
| `stop_hunt_le_90` | 13 | R_REPEATER | 68.4% | 53.8% | 53.8% | 23.1% | +2.1 | 1.42 | 0.81 | +16.1 | +16.3 |
| `asian_range_gte_30` | 15 | R_REPEATER | 78.9% | 60.0% | 66.7% | 13.3% | +5.8 | 1.80 | 0.72 | +21.1 | +20.3 |
| `confluence_gte_60` | 19 | R_REPEATER | 100.0% | 52.6% | 57.9% | 15.8% | +3.8 | 1.53 | 0.83 | +19.2 | +18.8 |
| `confluence_gte_70` | 19 | R_REPEATER | 100.0% | 52.6% | 57.9% | 15.8% | +3.8 | 1.53 | 0.83 | +19.2 | +18.8 |
| `tdi_rsi_gt_signal` | 16 | R_REPEATER | 84.2% | 56.2% | 62.5% | 6.2% | +4.6 | 1.86 | 0.93 | +18.5 | +17.7 |
| `tdi_rsi_gte_50` | 14 | R_REPEATER | 73.7% | 57.1% | 57.1% | 7.1% | +0.5 | 1.05 | 0.66 | +19.3 | +21.8 |
| `ratio_le_2_and_asian_gte_30` | 9 | R_REPEATER | 47.4% | 66.7% | 66.7% | 22.2% | +4.7 | 2.12 | 0.71 | +18.0 | +17.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | R_REPEATER | 36.8% | 71.4% | 71.4% | 0.0% | -1.0 | 0.81 | 0.33 | +14.2 | +20.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | R_REPEATER | 68.4% | 53.8% | 53.8% | 23.1% | +2.1 | 1.42 | 0.81 | +16.1 | +16.3 |
| `feature_stale_hod_exhaustion_reject` | 19 | R_REPEATER | 100.0% | 52.6% | 57.9% | 15.8% | +3.8 | 1.53 | 0.83 | +19.2 | +18.8 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 5.3% | 100.0% | 100.0% | 0.0% | +31.1 | 999.00 | 999.00 | +31.2 | +4.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 5.3% | 100.0% | 100.0% | 0.0% | +31.1 | 999.00 | 999.00 | +31.2 | +4.6 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=50.0% Avg=+0.8; out_of_sample N=5 Fav=60.0% Avg=+2.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 50 | R_REPEATER | 100.0% | 52.0% | 52.0% | 12.0% | +7.3 | 2.33 | 2.15 | +23.8 | +15.1 |
| `hunt_to_ar_ratio_le_2_0` | 36 | S_STRANGER | 72.0% | 47.2% | 47.2% | 8.3% | +2.2 | 1.37 | 1.54 | +19.0 | +16.1 |
| `hunt_to_ar_ratio_le_2_5` | 46 | R_REPEATER | 92.0% | 50.0% | 50.0% | 13.0% | +4.2 | 1.71 | 1.71 | +20.5 | +15.7 |
| `stop_hunt_le_90` | 43 | S_STRANGER | 86.0% | 48.8% | 48.8% | 11.6% | +3.9 | 1.66 | 1.74 | +20.6 | +15.5 |
| `asian_range_gte_30` | 36 | R_REPEATER | 72.0% | 52.8% | 52.8% | 11.1% | +7.1 | 2.21 | 1.98 | +24.3 | +15.5 |
| `confluence_gte_60` | 50 | R_REPEATER | 100.0% | 52.0% | 52.0% | 12.0% | +7.3 | 2.33 | 2.15 | +23.8 | +15.1 |
| `confluence_gte_70` | 50 | R_REPEATER | 100.0% | 52.0% | 52.0% | 12.0% | +7.3 | 2.33 | 2.15 | +23.8 | +15.1 |
| `tdi_rsi_gt_signal` | 24 | R_REPEATER | 48.0% | 50.0% | 50.0% | 4.2% | +8.1 | 2.42 | 2.42 | +25.4 | +17.5 |
| `tdi_rsi_gte_50` | 27 | S_STRANGER | 54.0% | 48.1% | 48.1% | 7.4% | +7.5 | 2.15 | 2.32 | +27.1 | +17.2 |
| `ratio_le_2_and_asian_gte_30` | 27 | S_STRANGER | 54.0% | 48.1% | 48.1% | 11.1% | +1.4 | 1.25 | 1.34 | +18.6 | +15.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | R_REPEATER | 26.0% | 53.8% | 53.8% | 0.0% | +1.5 | 1.31 | 1.13 | +16.8 | +17.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 43 | S_STRANGER | 86.0% | 48.8% | 48.8% | 11.6% | +3.9 | 1.66 | 1.74 | +20.6 | +15.5 |
| `feature_stale_hod_exhaustion_reject` | 50 | R_REPEATER | 100.0% | 52.0% | 52.0% | 12.0% | +7.3 | 2.33 | 2.15 | +23.8 | +15.1 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 2.0% | 100.0% | 100.0% | 0.0% | +62.7 | 999.00 | 999.00 | +66.4 | +10.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 2.0% | 100.0% | 100.0% | 0.0% | +62.7 | 999.00 | 999.00 | +66.4 | +10.0 |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+9.0; validation N=5 Fav=60.0% Avg=+22.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +9.2 | 3.03 | 3.03 | +29.4 | +11.6 |
| `hunt_to_ar_ratio_le_2_0` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 0.0% | +27.5 | 10.23 | 10.23 | +49.4 | +10.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +9.2 | 3.03 | 3.03 | +29.4 | +11.6 |
| `stop_hunt_le_90` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 0.0% | -6.3 | 0.06 | 0.24 | +11.9 | +14.5 |
| `asian_range_gte_30` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +9.2 | 3.03 | 3.03 | +29.4 | +11.6 |
| `confluence_gte_60` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +9.2 | 3.03 | 3.03 | +29.4 | +11.6 |
| `confluence_gte_70` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +9.2 | 3.03 | 3.03 | +29.4 | +11.6 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.8 | 0.00 | 0.00 | +24.8 | +7.2 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 60.0% | 66.7% | 66.7% | 0.0% | +20.4 | 11.12 | 5.56 | +43.2 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 0.0% | +27.5 | 10.23 | 10.23 | +49.4 | +10.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.8 | 0.00 | 0.00 | +24.8 | +7.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +19.7 | +13.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +9.2 | 3.03 | 3.03 | +29.4 | +11.6 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 0.0% | +4.9 | 2.01 | 2.68 | +22.6 | +12.1 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 0.0% | +21.7 | 82.25 | 41.12 | +41.2 | +6.4 |

### THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+2.8; validation N=3 Fav=66.7% Avg=+16.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 31.2% | +8.3 | 1.99 | 1.74 | +28.6 | +18.9 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 56.2% | 44.4% | 44.4% | 11.1% | +1.8 | 1.15 | 1.44 | +23.5 | +19.2 |
| `hunt_to_ar_ratio_le_2_5` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 31.2% | +8.3 | 1.99 | 1.74 | +28.6 | +18.9 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 68.8% | 36.4% | 36.4% | 9.1% | -1.5 | 0.88 | 1.54 | +21.4 | +25.0 |
| `asian_range_gte_30` | 14 | R_REPEATER | 87.5% | 50.0% | 50.0% | 35.7% | +9.2 | 2.04 | 1.75 | +29.8 | +19.4 |
| `confluence_gte_60` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 31.2% | +8.3 | 1.99 | 1.74 | +28.6 | +18.9 |
| `confluence_gte_70` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 50.0% | -10.3 | 0.00 | 0.00 | +11.7 | +14.4 |
| `tdi_rsi_gt_signal` | 7 | R_REPEATER | 43.8% | 57.1% | 57.1% | 0.0% | +8.5 | 1.98 | 1.49 | +29.7 | +18.9 |
| `tdi_rsi_gte_50` | 13 | R_REPEATER | 81.2% | 53.8% | 53.8% | 23.1% | +9.0 | 1.98 | 1.69 | +30.6 | +22.5 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 50.0% | 37.5% | 37.5% | 12.5% | +0.1 | 1.01 | 1.68 | +23.4 | +21.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 25.0% | 50.0% | 50.0% | 0.0% | +4.9 | 1.40 | 1.40 | +30.8 | +23.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 68.8% | 36.4% | 36.4% | 9.1% | -1.5 | 0.88 | 1.54 | +21.4 | +25.0 |
| `feature_stale_hod_exhaustion_reject` | 13 | R_REPEATER | 81.2% | 53.8% | 53.8% | 38.5% | +11.3 | 2.78 | 1.98 | +29.9 | +16.7 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 12.5% | 50.0% | 50.0% | 50.0% | +5.9 | 1.57 | 1.57 | +22.7 | +15.1 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 18.8% | 33.3% | 33.3% | 0.0% | -4.7 | 0.73 | 1.46 | +22.8 | +28.3 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=100.0% Avg=+22.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=100.0% Avg=+20.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | R_REPEATER | 100.0% | 50.0% | 55.0% | 35.0% | +0.5 | 1.05 | 0.86 | +16.5 | +17.6 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 55.0% | 36.4% | 36.4% | 36.4% | -3.1 | 0.81 | 1.42 | +19.5 | +23.8 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 65.0% | 38.5% | 38.5% | 30.8% | -3.1 | 0.79 | 1.26 | +16.9 | +21.9 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 85.0% | 47.1% | 52.9% | 29.4% | -0.6 | 0.95 | 0.85 | +17.5 | +19.2 |
| `asian_range_gte_30` | 15 | S_STRANGER | 75.0% | 46.7% | 53.3% | 26.7% | -1.9 | 0.86 | 0.75 | +15.5 | +19.2 |
| `confluence_gte_60` | 7 | S_STRANGER | 35.0% | 28.6% | 28.6% | 28.6% | -14.5 | 0.33 | 0.81 | +14.8 | +27.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 95.0% | 47.4% | 52.6% | 31.6% | -1.3 | 0.88 | 0.80 | +15.5 | +18.4 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 30.0% | 33.3% | 33.3% | 16.7% | -15.3 | 0.18 | 0.37 | +13.4 | +28.9 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 45.0% | 44.4% | 44.4% | 44.4% | -3.0 | 0.85 | 1.06 | +22.0 | +24.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 40.0% | 37.5% | 37.5% | 37.5% | -7.6 | 0.65 | 1.09 | +20.1 | +27.7 |
| `feature_fresh_reclaim_within_8` | 2 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +38.5 | 999.00 | 999.00 | +39.8 | +0.5 |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 70.0% | 35.7% | 42.9% | 28.6% | -3.5 | 0.75 | 1.00 | +16.1 | +21.2 |
| `feature_stale_hod_exhaustion_reject` | 20 | R_REPEATER | 100.0% | 50.0% | 55.0% | 35.0% | +0.5 | 1.05 | 0.86 | +16.5 | +17.6 |
| `feature_momentum_breakout_exception` | 6 | R_RUNNER | 30.0% | 100.0% | 100.0% | 66.7% | +22.0 | 999.00 | 999.00 | +27.8 | +6.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 5.0% | 100.0% | 100.0% | 100.0% | +20.4 | 999.00 | 999.00 | +48.3 | +14.1 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=50.0% Avg=+2.0; out_of_sample N=7 Fav=57.1% Avg=+7.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 46.7% | 46.7% | 20.0% | +4.0 | 1.45 | 1.66 | +25.3 | +17.5 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 53.3% | 25.0% | 25.0% | 12.5% | -8.7 | 0.37 | 1.11 | +15.0 | +26.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 66.7% | 40.0% | 40.0% | 30.0% | +1.1 | 1.10 | 1.65 | +23.3 | +21.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 66.7% | 40.0% | 40.0% | 20.0% | +3.6 | 1.32 | 1.99 | +26.0 | +21.5 |
| `asian_range_gte_30` | 12 | R_REPEATER | 80.0% | 50.0% | 50.0% | 25.0% | +2.4 | 1.26 | 1.26 | +23.1 | +17.3 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 46.7% | 46.7% | 20.0% | +4.0 | 1.45 | 1.66 | +25.3 | +17.5 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 46.7% | 46.7% | 20.0% | +4.0 | 1.45 | 1.66 | +25.3 | +17.5 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -22.2 | 0.00 | 0.00 | +6.7 | +32.4 |
| `tdi_rsi_gte_50` | 11 | R_REPEATER | 73.3% | 54.5% | 54.5% | 18.2% | +5.3 | 1.58 | 1.32 | +26.8 | +19.6 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 40.0% | 33.3% | 33.3% | 16.7% | -8.1 | 0.45 | 0.91 | +15.0 | +25.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -27.0 | 0.00 | 0.00 | +3.3 | +41.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 66.7% | 40.0% | 40.0% | 20.0% | +3.6 | 1.32 | 1.99 | +26.0 | +21.5 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 46.7% | 46.7% | 20.0% | +4.0 | 1.45 | 1.66 | +25.3 | +17.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=100.0% Avg=+17.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=50.0% Avg=+35.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 46.2% | 53.8% | 46.2% | +14.6 | 5.03 | 3.59 | +24.0 | +9.3 |
| `hunt_to_ar_ratio_le_2_0` | 8 | R_REPEATER | 61.5% | 62.5% | 75.0% | 62.5% | +25.7 | 53.71 | 8.95 | +33.4 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 92.3% | 41.7% | 50.0% | 41.7% | +13.5 | 4.46 | 3.71 | +23.7 | +9.7 |
| `stop_hunt_le_90` | 9 | R_REPEATER | 69.2% | 55.6% | 66.7% | 55.6% | +22.6 | 34.34 | 11.45 | +30.9 | +4.4 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 46.2% | 53.8% | 46.2% | +14.6 | 5.03 | 3.59 | +24.0 | +9.3 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 46.2% | 53.8% | 46.2% | +14.6 | 5.03 | 3.59 | +24.0 | +9.3 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 46.2% | 53.8% | 46.2% | +14.6 | 5.03 | 3.59 | +24.0 | +9.3 |
| `tdi_rsi_gt_signal` | 7 | R_REPEATER | 53.8% | 57.1% | 71.4% | 42.9% | +24.7 | 29.30 | 11.72 | +33.4 | +5.2 |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 61.5% | 62.5% | 62.5% | 37.5% | +15.8 | 5.60 | 3.36 | +25.2 | +10.8 |
| `ratio_le_2_and_asian_gte_30` | 8 | R_REPEATER | 61.5% | 62.5% | 75.0% | 62.5% | +25.7 | 53.71 | 8.95 | +33.4 | +4.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 46.2% | 66.7% | 83.3% | 50.0% | +29.1 | 45.83 | 9.17 | +37.3 | +5.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | R_REPEATER | 69.2% | 55.6% | 66.7% | 55.6% | +22.6 | 34.34 | 11.45 | +30.9 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 46.2% | 53.8% | 46.2% | +14.6 | 5.03 | 3.59 | +24.0 | +9.3 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 50.0% | +9.7 | 2.81 | 2.81 | +16.5 | +10.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 100.0% | +30.1 | 999.00 | 999.00 | +30.8 | +4.3 |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+18.8; validation N=5 Fav=20.0% Avg=-8.7; out_of_sample N=3 Fav=100.0% Avg=+46.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 0.0% | +7.7 | 1.80 | 2.10 | +27.2 | +17.9 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 53.8% | 14.3% | 14.3% | 0.0% | -13.5 | 0.03 | 0.15 | +12.4 | +14.8 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 0.0% | +1.4 | 1.12 | 1.96 | +23.1 | +16.6 |
| `stop_hunt_le_90` | 7 | S_STRANGER | 53.8% | 14.3% | 14.3% | 0.0% | -13.5 | 0.03 | 0.15 | +12.4 | +14.8 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 0.0% | +7.7 | 1.80 | 2.10 | +27.2 | +17.9 |
| `confluence_gte_60` | 4 | R_RUNNER | 30.8% | 75.0% | 75.0% | 0.0% | +30.4 | 8.33 | 2.78 | +42.3 | +14.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 30.8% | 50.0% | 50.0% | 0.0% | +3.2 | 1.35 | 1.35 | +24.0 | +20.2 |
| `tdi_rsi_gte_50` | 11 | R_REPEATER | 84.6% | 54.5% | 54.5% | 0.0% | +13.7 | 3.03 | 2.53 | +31.1 | +19.2 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 53.8% | 14.3% | 14.3% | 0.0% | -13.5 | 0.03 | 0.15 | +12.4 | +14.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 0.0% | -2.8 | 0.30 | 0.30 | +14.2 | +11.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 53.8% | 14.3% | 14.3% | 0.0% | -13.5 | 0.03 | 0.15 | +12.4 | +14.8 |
| `feature_stale_hod_exhaustion_reject` | 9 | S_STRANGER | 69.2% | 44.4% | 44.4% | 0.0% | +10.5 | 2.16 | 2.70 | +28.7 | +15.3 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 0.0% | -2.8 | 0.30 | 0.30 | +14.2 | +11.8 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 30.8% | 50.0% | 50.0% | 0.0% | +1.3 | 1.12 | 1.12 | +23.8 | +23.9 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=75.0% Avg=-4.8; validation N=1 Fav=0.0% Avg=-8.1; out_of_sample N=1 Fav=100.0% Avg=+43.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 23.1% | +3.3 | 1.26 | 1.26 | +27.0 | +21.5 |
| `hunt_to_ar_ratio_le_2_0` | 7 | R_REPEATER | 53.8% | 57.1% | 57.1% | 42.9% | +23.3 | 10.38 | 5.19 | +37.2 | +10.4 |
| `hunt_to_ar_ratio_le_2_5` | 9 | R_REPEATER | 69.2% | 55.6% | 55.6% | 33.3% | +6.4 | 1.39 | 0.84 | +33.9 | +25.2 |
| `stop_hunt_le_90` | 8 | R_REPEATER | 61.5% | 50.0% | 50.0% | 37.5% | +4.3 | 1.23 | 0.92 | +34.2 | +26.8 |
| `asian_range_gte_30` | 11 | R_REPEATER | 84.6% | 54.5% | 54.5% | 27.3% | +16.4 | 8.10 | 5.40 | +30.2 | +10.9 |
| `confluence_gte_60` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 27.3% | +2.6 | 1.19 | 1.19 | +28.7 | +22.4 |
| `confluence_gte_70` | 3 | R_REPEATER | 23.1% | 66.7% | 66.7% | 66.7% | +33.9 | 16.39 | 8.20 | +49.4 | +9.9 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 61.5% | 50.0% | 50.0% | 25.0% | +13.5 | 5.25 | 5.25 | +27.4 | +12.2 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 92.3% | 50.0% | 50.0% | 16.7% | +3.6 | 1.26 | 1.26 | +27.0 | +22.3 |
| `ratio_le_2_and_asian_gte_30` | 7 | R_REPEATER | 53.8% | 57.1% | 57.1% | 42.9% | +23.3 | 10.38 | 5.19 | +37.2 | +10.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 30.8% | 50.0% | 50.0% | 50.0% | +22.7 | 6.22 | 6.22 | +36.7 | +12.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | R_REPEATER | 53.8% | 57.1% | 57.1% | 42.9% | +23.3 | 10.38 | 5.19 | +37.2 | +10.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 92.3% | 41.7% | 41.7% | 25.0% | -0.0 | 1.00 | 1.20 | +24.5 | +23.2 |
| `feature_momentum_breakout_exception` | 7 | R_REPEATER | 53.8% | 57.1% | 57.1% | 42.9% | +2.3 | 1.12 | 0.56 | +36.1 | +27.8 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 46.2% | 66.7% | 66.7% | 33.3% | +2.7 | 1.12 | 0.56 | +37.6 | +30.4 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+7.9; validation N=2 Fav=50.0% Avg=+22.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 36.4% | +7.4 | 2.33 | 2.33 | +20.0 | +19.0 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 33.3% | +5.5 | 1.61 | 3.23 | +20.0 | +22.5 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 37.5% | +3.2 | 1.42 | 3.56 | +18.0 | +21.0 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 37.5% | +3.2 | 1.42 | 3.56 | +18.0 | +21.0 |
| `asian_range_gte_30` | 7 | R_REPEATER | 63.6% | 57.1% | 57.1% | 42.9% | +12.1 | 2.70 | 2.02 | +24.5 | +22.8 |
| `confluence_gte_60` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +21.6 | +5.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | R_RUNNER | 36.4% | 75.0% | 75.0% | 50.0% | +23.2 | 7.15 | 2.38 | +31.2 | +16.4 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 33.3% | +13.3 | 3.79 | 3.79 | +22.1 | +19.2 |
| `ratio_le_2_and_asian_gte_30` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 50.0% | +11.1 | 2.04 | 2.04 | +28.2 | +24.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 50.0% | +22.7 | 4.01 | 4.01 | +34.0 | +15.8 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 0.0% | +8.3 | 999.00 | 999.00 | +19.8 | +7.3 |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 37.5% | +5.2 | 1.77 | 2.36 | +20.2 | +18.5 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 36.4% | +7.4 | 2.33 | 2.33 | +20.0 | +19.0 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 28.6% | +5.3 | 3.02 | 3.02 | +15.4 | +15.7 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 25.0% | +8.5 | 3.54 | 3.54 | +16.2 | +21.0 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=80.0% Avg=+6.4; validation N=3 Fav=66.7% Avg=+27.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 6.2% | +4.1 | 1.69 | 1.93 | +20.1 | +19.1 |
| `hunt_to_ar_ratio_le_2_0` | 8 | R_RUNNER | 50.0% | 75.0% | 75.0% | 0.0% | +14.4 | 8.37 | 2.79 | +28.8 | +13.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | R_REPEATER | 81.2% | 53.8% | 53.8% | 7.7% | +7.2 | 2.35 | 1.68 | +22.8 | +16.6 |
| `stop_hunt_le_90` | 11 | R_REPEATER | 68.8% | 63.6% | 63.6% | 9.1% | +13.1 | 8.69 | 3.72 | +26.1 | +12.2 |
| `asian_range_gte_30` | 12 | R_REPEATER | 75.0% | 50.0% | 50.0% | 8.3% | +5.1 | 1.89 | 1.57 | +21.2 | +16.5 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 6.2% | +4.1 | 1.69 | 1.93 | +20.1 | +19.1 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 6.2% | +4.1 | 1.69 | 1.93 | +20.1 | +19.1 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 31.2% | 40.0% | 40.0% | 0.0% | +11.6 | 3.07 | 4.61 | +23.5 | +26.4 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 75.0% | 50.0% | 50.0% | 0.0% | +7.4 | 2.30 | 2.30 | +23.8 | +21.2 |
| `ratio_le_2_and_asian_gte_30` | 8 | R_RUNNER | 50.0% | 75.0% | 75.0% | 0.0% | +14.4 | 8.37 | 2.79 | +28.8 | +13.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 12.5% | 50.0% | 50.0% | 0.0% | +20.6 | 4.23 | 4.23 | +30.8 | +25.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | R_REPEATER | 56.2% | 66.7% | 66.7% | 11.1% | +12.8 | 8.37 | 2.79 | +26.7 | +12.2 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 6.2% | +4.1 | 1.69 | 1.93 | +20.1 | +19.1 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 43.8% | 28.6% | 28.6% | 0.0% | +0.1 | 1.02 | 2.54 | +16.4 | +18.7 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 37.5% | 50.0% | 50.0% | 0.0% | +13.8 | 5.05 | 5.05 | +27.2 | +16.9 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=33.3% Avg=-7.1; validation N=2 Fav=100.0% Avg=+14.8; out_of_sample N=1 Fav=100.0% Avg=+17.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 0.0% | -1.2 | 0.83 | 1.07 | +16.9 | +19.6 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 81.2% | 46.2% | 46.2% | 0.0% | +1.3 | 1.25 | 1.45 | +17.2 | +17.2 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 93.8% | 46.7% | 46.7% | 0.0% | +1.7 | 1.35 | 1.54 | +16.6 | +16.4 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 87.5% | 42.9% | 42.9% | 0.0% | +0.9 | 1.17 | 1.56 | +16.5 | +16.4 |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 0.0% | -1.2 | 0.83 | 1.07 | +16.9 | +19.6 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 0.0% | -1.2 | 0.83 | 1.07 | +16.9 | +19.6 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 0.0% | -1.2 | 0.83 | 1.07 | +16.9 | +19.6 |
| `tdi_rsi_gt_signal` | 9 | R_REPEATER | 56.2% | 55.6% | 55.6% | 0.0% | -4.3 | 0.63 | 0.50 | +15.7 | +23.5 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 75.0% | 58.3% | 58.3% | 0.0% | -0.8 | 0.91 | 0.65 | +17.4 | +22.6 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 81.2% | 46.2% | 46.2% | 0.0% | +1.3 | 1.25 | 1.45 | +17.2 | +17.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | R_REPEATER | 43.8% | 57.1% | 57.1% | 0.0% | -1.0 | 0.88 | 0.66 | +14.7 | +18.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 87.5% | 42.9% | 42.9% | 0.0% | +0.9 | 1.17 | 1.56 | +16.5 | +16.4 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 93.8% | 40.0% | 40.0% | 0.0% | -2.9 | 0.63 | 0.94 | +15.0 | +19.6 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 56.2% | 22.2% | 22.2% | 0.0% | -6.1 | 0.18 | 0.64 | +10.6 | +21.0 |
| `feature_eurjpy_tdi50_reclaim` | 9 | R_REPEATER | 56.2% | 55.6% | 55.6% | 0.0% | +0.5 | 1.07 | 0.86 | +15.4 | +21.5 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=100.0% Avg=+21.5; validation N=2 Fav=50.0% Avg=-9.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 18.8% | -2.6 | 0.75 | 0.75 | +22.1 | +17.9 |
| `hunt_to_ar_ratio_le_2_0` | 6 | R_RUNNER | 37.5% | 83.3% | 83.3% | 16.7% | +11.3 | 2.81 | 0.56 | +31.6 | +16.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 68.8% | 45.5% | 45.5% | 9.1% | -2.7 | 0.78 | 0.94 | +23.5 | +17.5 |
| `stop_hunt_le_90` | 9 | R_REPEATER | 56.2% | 66.7% | 66.7% | 11.1% | +4.5 | 1.60 | 0.80 | +25.0 | +14.9 |
| `asian_range_gte_30` | 13 | S_STRANGER | 81.2% | 38.5% | 38.5% | 15.4% | -4.4 | 0.65 | 0.90 | +22.8 | +17.5 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 18.8% | -2.6 | 0.75 | 0.75 | +22.1 | +17.9 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 18.8% | -2.6 | 0.75 | 0.75 | +22.1 | +17.9 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 93.8% | 46.7% | 46.7% | 13.3% | -2.8 | 0.75 | 0.75 | +22.5 | +18.6 |
| `tdi_rsi_gte_50` | 10 | R_REPEATER | 62.5% | 50.0% | 50.0% | 10.0% | -3.0 | 0.71 | 0.57 | +25.3 | +20.7 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_RUNNER | 37.5% | 83.3% | 83.3% | 16.7% | +11.3 | 2.81 | 0.56 | +31.6 | +16.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_RUNNER | 37.5% | 83.3% | 83.3% | 16.7% | +11.3 | 2.81 | 0.56 | +31.6 | +16.2 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 6.2% | 100.0% | 100.0% | 0.0% | +3.7 | 999.00 | 999.00 | +25.6 | +18.5 |
| `feature_extreme_hunt_with_exception` | 9 | R_RUNNER | 56.2% | 77.8% | 77.8% | 11.1% | +7.8 | 2.38 | 0.68 | +26.4 | +16.6 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 18.8% | -2.6 | 0.75 | 0.75 | +22.1 | +17.9 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 62.5% | 40.0% | 40.0% | 10.0% | -10.1 | 0.32 | 0.41 | +17.4 | +24.3 |
| `feature_eurjpy_tdi50_reclaim` | 8 | R_REPEATER | 50.0% | 50.0% | 50.0% | 12.5% | -6.4 | 0.50 | 0.38 | +19.6 | +24.3 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=2 Fav=0.0% Avg=-8.8; out_of_sample N=4 Fav=75.0% Avg=+12.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 16.7% | +0.7 | 1.09 | 1.31 | +17.9 | +19.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 83.3% | 50.0% | 50.0% | 20.0% | +5.0 | 2.03 | 1.62 | +18.4 | +14.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 18.2% | +2.8 | 1.45 | 1.45 | +16.7 | +17.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 18.2% | +2.5 | 1.39 | 1.39 | +19.5 | +17.1 |
| `asian_range_gte_30` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 18.2% | +2.8 | 1.45 | 1.45 | +16.7 | +17.0 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 16.7% | +0.7 | 1.09 | 1.31 | +17.9 | +19.0 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 16.7% | +0.7 | 1.09 | 1.31 | +17.9 | +19.0 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 0.0% | +1.6 | 1.27 | 1.69 | +20.3 | +24.8 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 0.0% | +2.4 | 1.35 | 1.68 | +19.2 | +24.6 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 83.3% | 50.0% | 50.0% | 20.0% | +5.0 | 2.03 | 1.62 | +18.4 | +14.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 50.0% | 50.0% | 50.0% | 0.0% | +5.7 | 2.68 | 2.68 | +18.6 | +21.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 18.2% | +2.5 | 1.39 | 1.39 | +19.5 | +17.1 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 16.7% | +0.7 | 1.09 | 1.31 | +17.9 | +19.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=50.0% Avg=+10.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 40.0% | 46.7% | 20.0% | +4.0 | 1.39 | 1.59 | +23.8 | +22.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 66.7% | 30.0% | 40.0% | 20.0% | -3.9 | 0.73 | 1.09 | +18.9 | +22.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 80.0% | 33.3% | 41.7% | 16.7% | -2.4 | 0.81 | 1.13 | +19.7 | +19.9 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 93.3% | 35.7% | 42.9% | 14.3% | -1.6 | 0.86 | 1.14 | +19.4 | +23.5 |
| `asian_range_gte_30` | 9 | S_STRANGER | 60.0% | 33.3% | 33.3% | 33.3% | +1.8 | 1.11 | 2.22 | +26.5 | +23.8 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 40.0% | 46.7% | 20.0% | +4.0 | 1.39 | 1.59 | +23.8 | +22.3 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 40.0% | 46.7% | 20.0% | +4.0 | 1.39 | 1.59 | +23.8 | +22.3 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 0.0% | +3.4 | 3.62 | 3.62 | +17.7 | +45.3 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 93.3% | 42.9% | 42.9% | 21.4% | +3.4 | 1.31 | 1.75 | +24.5 | +23.2 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 53.3% | 25.0% | 25.0% | 25.0% | -8.2 | 0.54 | 1.63 | +19.2 | +26.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 73.3% | 27.3% | 36.4% | 18.2% | -3.8 | 0.71 | 1.25 | +18.6 | +24.3 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 66.7% | 40.0% | 50.0% | 30.0% | +5.9 | 1.47 | 1.47 | +28.1 | +20.8 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 26.7% | 50.0% | 75.0% | 50.0% | +23.8 | 3.50 | 1.17 | +39.1 | +16.1 |
| `feature_eurjpy_tdi50_reclaim` | 8 | R_REPEATER | 53.3% | 50.0% | 50.0% | 25.0% | +10.4 | 2.32 | 2.32 | +27.3 | +22.7 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+11.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 40.0% | 46.7% | 66.7% | +2.1 | 1.31 | 0.75 | +18.1 | +10.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 66.7% | 30.0% | 40.0% | 50.0% | -2.5 | 0.76 | 0.76 | +17.6 | +13.6 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 80.0% | 41.7% | 50.0% | 58.3% | +1.3 | 1.15 | 0.76 | +18.8 | +12.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 66.7% | 30.0% | 40.0% | 50.0% | -2.5 | 0.76 | 0.76 | +17.6 | +13.6 |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 40.0% | 46.7% | 66.7% | +2.1 | 1.31 | 0.75 | +18.1 | +10.6 |
| `confluence_gte_60` | 8 | S_STRANGER | 53.3% | 25.0% | 37.5% | 50.0% | -5.3 | 0.58 | 0.58 | +18.3 | +14.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 6.7% | 100.0% | 100.0% | 100.0% | +19.5 | 999.00 | 999.00 | +24.4 | +9.0 |
| `tdi_rsi_gte_50` | 11 | R_REPEATER | 73.3% | 54.5% | 63.6% | 81.8% | +11.9 | 27.12 | 3.87 | +22.0 | +6.1 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 66.7% | 30.0% | 40.0% | 50.0% | -2.5 | 0.76 | 0.76 | +17.6 | +13.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 66.7% | 30.0% | 40.0% | 50.0% | -2.5 | 0.76 | 0.76 | +17.6 | +13.6 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 40.0% | 46.7% | 66.7% | +2.1 | 1.31 | 0.75 | +18.1 | +10.6 |
| `feature_momentum_breakout_exception` | 6 | R_REPEATER | 40.0% | 50.0% | 50.0% | 100.0% | +9.5 | 999.00 | 999.00 | +18.5 | +4.9 |
| `feature_eurjpy_tdi50_reclaim` | 5 | R_REPEATER | 33.3% | 60.0% | 60.0% | 100.0% | +11.4 | 999.00 | 999.00 | +19.4 | +4.4 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=75.0% Avg=+15.7; validation N=1 Fav=100.0% Avg=+4.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 39.3% | 39.3% | 21.4% | +0.8 | 1.10 | 1.70 | +18.0 | +14.6 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 85.7% | 45.8% | 45.8% | 25.0% | +3.2 | 1.46 | 1.73 | +19.7 | +12.7 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 96.4% | 40.7% | 40.7% | 22.2% | +1.5 | 1.20 | 1.75 | +18.3 | +14.2 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 92.9% | 42.3% | 42.3% | 23.1% | +2.7 | 1.41 | 1.92 | +19.0 | +12.8 |
| `asian_range_gte_30` | 24 | S_STRANGER | 85.7% | 33.3% | 33.3% | 12.5% | -3.5 | 0.61 | 1.23 | +14.0 | +16.2 |
| `confluence_gte_60` | 28 | S_STRANGER | 100.0% | 39.3% | 39.3% | 21.4% | +0.8 | 1.10 | 1.70 | +18.0 | +14.6 |
| `confluence_gte_70` | 28 | S_STRANGER | 100.0% | 39.3% | 39.3% | 21.4% | +0.8 | 1.10 | 1.70 | +18.0 | +14.6 |
| `tdi_rsi_gt_signal` | 26 | S_STRANGER | 92.9% | 42.3% | 42.3% | 23.1% | +2.4 | 1.34 | 1.83 | +19.2 | +13.7 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 53.6% | 40.0% | 40.0% | 13.3% | +3.8 | 1.59 | 2.38 | +21.8 | +13.8 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 75.0% | 38.1% | 38.1% | 14.3% | -1.7 | 0.79 | 1.29 | +14.7 | +14.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 19 | S_STRANGER | 67.9% | 42.1% | 42.1% | 15.8% | +0.3 | 1.05 | 1.44 | +16.0 | +13.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 92.9% | 42.3% | 42.3% | 23.1% | +2.7 | 1.41 | 1.92 | +19.0 | +12.8 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 39.3% | 39.3% | 21.4% | +0.8 | 1.10 | 1.70 | +18.0 | +14.6 |
| `feature_momentum_breakout_exception` | 5 | R_RUNNER | 17.9% | 80.0% | 80.0% | 60.0% | +13.4 | 4.65 | 1.16 | +31.3 | +8.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 7.1% | 50.0% | 50.0% | 50.0% | +10.8 | 2.17 | 2.17 | +34.9 | +10.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=83.3% Avg=+13.4; out_of_sample N=5 Fav=40.0% Avg=+8.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 39.3% | 42.9% | 21.4% | -2.9 | 0.76 | 0.95 | +17.4 | +12.5 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 71.4% | 30.0% | 35.0% | 20.0% | -7.0 | 0.56 | 0.95 | +17.1 | +14.8 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 89.3% | 36.0% | 40.0% | 24.0% | -4.4 | 0.67 | 0.93 | +17.1 | +13.6 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 78.6% | 31.8% | 36.4% | 18.2% | -6.4 | 0.57 | 0.93 | +16.9 | +14.7 |
| `asian_range_gte_30` | 26 | S_STRANGER | 92.9% | 42.3% | 46.2% | 23.1% | -2.0 | 0.83 | 0.90 | +18.3 | +11.9 |
| `confluence_gte_60` | 25 | S_STRANGER | 89.3% | 36.0% | 40.0% | 16.0% | -4.4 | 0.67 | 0.94 | +17.1 | +13.3 |
| `confluence_gte_70` | 11 | R_REPEATER | 39.3% | 63.6% | 72.7% | 27.3% | +11.3 | 4.48 | 1.68 | +22.2 | +8.9 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 28.6% | 37.5% | 37.5% | 12.5% | +8.6 | 2.56 | 4.27 | +22.6 | +11.6 |
| `tdi_rsi_gte_50` | 16 | R_REPEATER | 57.1% | 50.0% | 50.0% | 18.8% | +5.3 | 1.77 | 1.77 | +20.2 | +15.3 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 67.9% | 31.6% | 36.8% | 21.1% | -6.7 | 0.58 | 0.91 | +17.7 | +14.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 21.4% | 50.0% | 50.0% | 16.7% | +12.5 | 2.96 | 2.96 | +27.1 | +14.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 78.6% | 31.8% | 36.4% | 18.2% | -6.4 | 0.57 | 0.93 | +16.9 | +14.7 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 39.3% | 42.9% | 21.4% | -2.9 | 0.76 | 0.95 | +17.4 | +12.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=60.0% Avg=-2.7; out_of_sample N=2 Fav=100.0% Avg=+14.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 39.1% | 39.1% | 13.0% | -4.6 | 0.60 | 0.79 | +15.5 | +16.2 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 82.6% | 36.8% | 36.8% | 15.8% | -6.2 | 0.53 | 0.75 | +16.1 | +16.0 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 39.1% | 39.1% | 13.0% | -4.6 | 0.60 | 0.79 | +15.5 | +16.2 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 95.7% | 36.4% | 36.4% | 13.6% | -5.3 | 0.56 | 0.83 | +15.5 | +16.8 |
| `asian_range_gte_30` | 19 | S_STRANGER | 82.6% | 42.1% | 42.1% | 5.3% | -4.9 | 0.63 | 0.86 | +16.3 | +16.8 |
| `confluence_gte_60` | 20 | S_STRANGER | 87.0% | 45.0% | 45.0% | 15.0% | -3.9 | 0.67 | 0.67 | +17.0 | +15.5 |
| `confluence_gte_70` | 7 | R_REPEATER | 30.4% | 71.4% | 71.4% | 14.3% | +2.3 | 1.23 | 0.49 | +20.9 | +8.6 |
| `tdi_rsi_gt_signal` | 11 | R_REPEATER | 47.8% | 54.5% | 54.5% | 9.1% | +1.9 | 1.64 | 1.36 | +12.8 | +12.1 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 47.8% | 45.5% | 45.5% | 9.1% | +1.7 | 1.54 | 1.85 | +11.9 | +13.9 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 69.6% | 37.5% | 37.5% | 6.2% | -7.4 | 0.53 | 0.88 | +16.3 | +18.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 39.1% | 44.4% | 44.4% | 11.1% | +1.1 | 1.31 | 1.63 | +12.0 | +13.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 95.7% | 36.4% | 36.4% | 13.6% | -5.3 | 0.56 | 0.83 | +15.5 | +16.8 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 39.1% | 39.1% | 13.0% | -4.6 | 0.60 | 0.79 | +15.5 | +16.2 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 17.4% | 25.0% | 25.0% | 25.0% | -5.7 | 0.16 | 0.32 | +10.4 | +16.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 13.0% | 33.3% | 33.3% | 0.0% | -7.6 | 0.16 | 0.32 | +9.1 | +19.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=25.0% Avg=+0.3; validation N=2 Fav=100.0% Avg=+8.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | -1.5 | 0.83 | 1.16 | +18.0 | +19.2 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 61.5% | 37.5% | 37.5% | 25.0% | -5.6 | 0.50 | 0.67 | +13.8 | +22.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 76.9% | 40.0% | 40.0% | 20.0% | -2.5 | 0.74 | 0.92 | +15.7 | +22.3 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 76.9% | 40.0% | 40.0% | 30.0% | -2.8 | 0.70 | 0.88 | +14.7 | +20.0 |
| `asian_range_gte_30` | 10 | S_STRANGER | 76.9% | 40.0% | 40.0% | 20.0% | -3.4 | 0.67 | 0.84 | +17.3 | +22.5 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | -1.5 | 0.83 | 1.16 | +18.0 | +19.2 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | -1.5 | 0.83 | 1.16 | +18.0 | +19.2 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 27.3% | +4.0 | 1.94 | 1.94 | +20.4 | +16.0 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 61.5% | 37.5% | 37.5% | 25.0% | +3.3 | 1.82 | 2.43 | +22.1 | +18.3 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 61.5% | 37.5% | 37.5% | 25.0% | -5.6 | 0.50 | 0.67 | +13.8 | +22.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 46.2% | 50.0% | 50.0% | 33.3% | +3.1 | 1.69 | 1.12 | +16.8 | +17.9 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -42.0 | 0.00 | 0.00 | +6.3 | +50.4 |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 27.3% | -2.7 | 0.69 | 1.04 | +15.5 | +18.7 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | -1.5 | 0.83 | 1.16 | +18.0 | +19.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -42.0 | 0.00 | 0.00 | +6.3 | +50.4 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+4.3; validation N=3 Fav=66.7% Avg=+6.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | -5.5 | 0.49 | 0.59 | +16.3 | +16.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 69.2% | 33.3% | 33.3% | 22.2% | -8.1 | 0.26 | 0.35 | +15.9 | +17.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 16.7% | -9.3 | 0.20 | 0.31 | +14.0 | +16.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 76.9% | 30.0% | 30.0% | 20.0% | -7.9 | 0.25 | 0.41 | +15.0 | +16.1 |
| `asian_range_gte_30` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 18.2% | -4.1 | 0.61 | 0.61 | +17.2 | +14.5 |
| `confluence_gte_60` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 18.2% | -6.6 | 0.48 | 0.72 | +16.3 | +18.2 |
| `confluence_gte_70` | 6 | R_REPEATER | 46.2% | 50.0% | 50.0% | 33.3% | +5.4 | 1.98 | 1.32 | +22.1 | +12.7 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 18.2% | -3.5 | 0.64 | 0.64 | +16.6 | +16.1 |
| `tdi_rsi_gte_50` | 3 | R_REPEATER | 23.1% | 66.7% | 66.7% | 33.3% | +11.6 | 6.70 | 3.35 | +23.5 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 53.8% | 42.9% | 42.9% | 14.3% | -6.6 | 0.36 | 0.36 | +17.2 | +14.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 46.2% | 50.0% | 50.0% | 16.7% | -2.3 | 0.65 | 0.44 | +17.5 | +11.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 76.9% | 30.0% | 30.0% | 20.0% | -7.9 | 0.25 | 0.41 | +15.0 | +16.1 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | -5.5 | 0.49 | 0.59 | +16.3 | +16.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 50.0% | -6.5 | 0.03 | 0.03 | +13.7 | +16.4 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=100.0% Avg=+25.6; validation N=2 Fav=50.0% Avg=-0.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 37.5% | 50.0% | 16.7% | +2.8 | 1.29 | 1.19 | +17.8 | +12.4 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 58.3% | 28.6% | 42.9% | 14.3% | +1.2 | 1.13 | 1.31 | +15.7 | +12.1 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 79.2% | 31.6% | 47.4% | 10.5% | +2.9 | 1.40 | 1.40 | +15.9 | +12.6 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 75.0% | 27.8% | 38.9% | 11.1% | +1.5 | 1.18 | 1.68 | +15.2 | +14.2 |
| `asian_range_gte_30` | 20 | S_STRANGER | 83.3% | 35.0% | 50.0% | 15.0% | +2.0 | 1.20 | 1.08 | +17.9 | +11.1 |
| `confluence_gte_60` | 2 | R_RUNNER | 8.3% | 100.0% | 100.0% | 0.0% | +32.2 | 999.00 | 999.00 | +36.7 | +20.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 6 | R_RUNNER | 25.0% | 83.3% | 83.3% | 0.0% | +16.9 | 11.81 | 2.36 | +24.2 | +18.4 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 50.0% | 66.7% | 66.7% | 16.7% | +16.6 | 5.54 | 2.77 | +25.4 | +17.2 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 54.2% | 30.8% | 46.2% | 15.4% | +2.3 | 1.25 | 1.25 | +16.9 | +11.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_RUNNER | 16.7% | 75.0% | 75.0% | 0.0% | +14.7 | 7.26 | 2.42 | +20.7 | +20.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 70.8% | 35.3% | 47.1% | 17.6% | +3.4 | 1.40 | 1.40 | +16.9 | +13.1 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 95.8% | 34.8% | 47.8% | 17.4% | +1.8 | 1.18 | 1.18 | +16.7 | +12.2 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 29.2% | 42.9% | 57.1% | 14.3% | +6.9 | 3.28 | 2.46 | +15.7 | +13.1 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 20.8% | 40.0% | 40.0% | 0.0% | +4.3 | 2.03 | 3.04 | +15.2 | +17.1 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=75.0% Avg=+39.4; validation N=1 Fav=0.0% Avg=-12.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 36.8% | 36.8% | 26.3% | +11.3 | 2.51 | 3.23 | +28.8 | +19.8 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 42.1% | 37.5% | 37.5% | 62.5% | +17.7 | 7.63 | 7.63 | +33.0 | +14.8 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 57.9% | 36.4% | 36.4% | 45.5% | +9.0 | 2.32 | 2.90 | +26.5 | +19.0 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 52.6% | 40.0% | 40.0% | 50.0% | +12.2 | 3.20 | 3.20 | +30.4 | +16.2 |
| `asian_range_gte_30` | 17 | S_STRANGER | 89.5% | 35.3% | 35.3% | 29.4% | +13.9 | 3.17 | 4.23 | +29.8 | +19.6 |
| `confluence_gte_60` | 15 | S_STRANGER | 78.9% | 40.0% | 40.0% | 20.0% | +15.7 | 3.17 | 4.23 | +30.3 | +20.4 |
| `confluence_gte_70` | 4 | S_STRANGER | 21.1% | 25.0% | 25.0% | 0.0% | -4.7 | 0.36 | 1.08 | +11.8 | +26.6 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 52.6% | 30.0% | 30.0% | 30.0% | +5.8 | 1.55 | 3.61 | +23.7 | +22.5 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 84.2% | 43.8% | 43.8% | 18.8% | +15.6 | 3.30 | 3.77 | +30.0 | +19.2 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 42.1% | 37.5% | 37.5% | 62.5% | +17.7 | 7.63 | 7.63 | +33.0 | +14.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 26.3% | 60.0% | 60.0% | 60.0% | +29.0 | 8.87 | 5.92 | +42.1 | +14.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 42.1% | 37.5% | 37.5% | 62.5% | +17.7 | 7.63 | 7.63 | +33.0 | +14.8 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 36.8% | 36.8% | 26.3% | +11.3 | 2.51 | 3.23 | +28.8 | +19.8 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 42.1% | 12.5% | 12.5% | 12.5% | -13.4 | 0.12 | 0.70 | +12.4 | +28.9 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 31.6% | 16.7% | 16.7% | 0.0% | -12.1 | 0.16 | 0.81 | +9.8 | +29.4 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=60.0% Avg=+3.7; validation N=2 Fav=0.0% Avg=-0.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | -2.3 | 0.74 | 1.21 | +18.0 | +18.6 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 63.6% | 35.7% | 35.7% | 7.1% | -2.0 | 0.75 | 1.35 | +16.7 | +16.3 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 68.2% | 33.3% | 33.3% | 6.7% | -4.9 | 0.53 | 1.07 | +15.9 | +18.3 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 77.3% | 41.2% | 41.2% | 11.8% | +0.9 | 1.14 | 1.63 | +17.8 | +14.8 |
| `asian_range_gte_30` | 19 | S_STRANGER | 86.4% | 31.6% | 31.6% | 15.8% | -5.0 | 0.52 | 1.05 | +17.2 | +20.3 |
| `confluence_gte_60` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | -2.3 | 0.74 | 1.21 | +18.0 | +18.6 |
| `confluence_gte_70` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | -2.3 | 0.74 | 1.21 | +18.0 | +18.6 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 50.0% | 36.4% | 36.4% | 27.3% | -0.2 | 0.98 | 1.46 | +20.0 | +13.6 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 72.7% | 31.2% | 31.2% | 18.8% | -3.1 | 0.67 | 1.34 | +17.8 | +17.7 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 63.6% | 35.7% | 35.7% | 7.1% | -2.0 | 0.75 | 1.35 | +16.7 | +16.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 31.8% | 42.9% | 42.9% | 14.3% | +2.4 | 1.63 | 2.17 | +20.5 | +10.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 77.3% | 41.2% | 41.2% | 11.8% | +0.9 | 1.14 | 1.63 | +17.8 | +14.8 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | -2.3 | 0.74 | 1.21 | +18.0 | +18.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=37.5% Avg=+0.8; validation N=3 Fav=66.7% Avg=+24.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | -5.3 | 0.64 | 0.97 | +19.9 | +26.4 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 63.6% | 42.9% | 42.9% | 0.0% | -8.1 | 0.56 | 0.65 | +20.0 | +28.3 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | -5.3 | 0.64 | 0.97 | +19.9 | +26.4 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 59.1% | 38.5% | 38.5% | 7.7% | -3.6 | 0.64 | 0.77 | +15.5 | +20.9 |
| `asian_range_gte_30` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | -5.3 | 0.64 | 0.97 | +19.9 | +26.4 |
| `confluence_gte_60` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | -5.3 | 0.64 | 0.97 | +19.9 | +26.4 |
| `confluence_gte_70` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | -5.3 | 0.64 | 0.97 | +19.9 | +26.4 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 27.3% | 33.3% | 33.3% | 0.0% | -2.2 | 0.74 | 1.47 | +14.3 | +15.9 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 81.8% | 44.4% | 44.4% | 5.6% | -3.2 | 0.78 | 0.88 | +22.5 | +25.6 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 63.6% | 42.9% | 42.9% | 0.0% | -8.1 | 0.56 | 0.65 | +20.0 | +28.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 22.7% | 40.0% | 40.0% | 0.0% | -1.2 | 0.85 | 1.28 | +14.5 | +14.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 54.5% | 41.7% | 41.7% | 0.0% | -3.8 | 0.64 | 0.77 | +16.0 | +21.9 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 77.3% | 35.3% | 35.3% | 11.8% | -0.0 | 1.00 | 1.50 | +19.6 | +21.8 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 50.0% | 45.5% | 45.5% | 18.2% | +7.3 | 1.99 | 1.99 | +26.3 | +16.8 |
| `feature_eurjpy_tdi50_reclaim` | 12 | R_REPEATER | 54.5% | 50.0% | 50.0% | 8.3% | -4.1 | 0.78 | 0.78 | +26.7 | +26.0 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=-32.2; validation N=1 Fav=100.0% Avg=+10.8; out_of_sample N=2 Fav=50.0% Avg=+6.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 0.0% | -23.6 | 0.23 | 0.40 | +21.1 | +35.0 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 0.0% | -30.6 | 0.12 | 0.25 | +20.0 | +33.1 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 0.0% | -19.1 | 0.28 | 0.47 | +23.5 | +28.3 |
| `stop_hunt_le_90` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 0.0% | -23.8 | 0.20 | 0.27 | +20.6 | +28.6 |
| `asian_range_gte_30` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 0.0% | -27.7 | 0.18 | 0.42 | +20.8 | +38.3 |
| `confluence_gte_60` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 0.0% | -19.1 | 0.28 | 0.47 | +23.5 | +28.3 |
| `confluence_gte_70` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +20.3 | +6.1 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 0.0% | -30.0 | 0.19 | 0.37 | +22.1 | +39.8 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 0.0% | -12.0 | 0.46 | 0.46 | +25.3 | +31.8 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 0.0% | -30.6 | 0.12 | 0.25 | +20.0 | +33.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -48.3 | 0.05 | 0.16 | +21.7 | +43.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 0.0% | -30.6 | 0.12 | 0.25 | +20.0 | +33.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 90.9% | 40.0% | 40.0% | 0.0% | -25.7 | 0.23 | 0.35 | +21.2 | +37.9 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 0.0% | -16.7 | 0.23 | 0.46 | +20.5 | +32.8 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 0.0% | -22.5 | 0.20 | 0.40 | +17.3 | +31.5 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+13.5; validation N=6 Fav=50.0% Avg=+3.8; out_of_sample N=8 Fav=37.5% Avg=-2.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 14.3% | -4.7 | 0.55 | 0.88 | +15.1 | +21.0 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 71.4% | 40.0% | 40.0% | 20.0% | -1.4 | 0.84 | 1.06 | +17.8 | +20.1 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 85.7% | 37.5% | 37.5% | 16.7% | -4.4 | 0.59 | 0.85 | +15.9 | +22.0 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 85.7% | 41.7% | 41.7% | 16.7% | -3.4 | 0.66 | 0.80 | +16.2 | +21.6 |
| `asian_range_gte_30` | 23 | S_STRANGER | 82.1% | 34.8% | 34.8% | 17.4% | -5.6 | 0.54 | 0.87 | +16.3 | +23.2 |
| `confluence_gte_60` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 14.3% | -4.7 | 0.55 | 0.88 | +15.1 | +21.0 |
| `confluence_gte_70` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 14.3% | -4.7 | 0.55 | 0.88 | +15.1 | +21.0 |
| `tdi_rsi_gt_signal` | 22 | S_STRANGER | 78.6% | 40.9% | 40.9% | 13.6% | -2.5 | 0.73 | 0.98 | +17.6 | +19.1 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 64.3% | 27.8% | 27.8% | 0.0% | -9.2 | 0.39 | 1.01 | +14.5 | +26.9 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 67.9% | 42.1% | 42.1% | 21.1% | -1.2 | 0.87 | 0.98 | +17.8 | +20.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 53.6% | 46.7% | 46.7% | 20.0% | +1.2 | 1.14 | 1.14 | +20.6 | +18.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 85.7% | 41.7% | 41.7% | 16.7% | -3.4 | 0.66 | 0.80 | +16.2 | +21.6 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 14.3% | -4.7 | 0.55 | 0.88 | +15.1 | +21.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+3.4; validation N=1 Fav=100.0% Avg=+46.5; out_of_sample N=1 Fav=0.0% Avg=-4.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 17.6% | -7.2 | 0.49 | 0.82 | +17.3 | +16.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 58.8% | 20.0% | 20.0% | 10.0% | -15.4 | 0.24 | 0.95 | +14.3 | +17.1 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 76.5% | 23.1% | 23.1% | 7.7% | -12.6 | 0.32 | 1.07 | +15.6 | +19.3 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 70.6% | 16.7% | 16.7% | 8.3% | -16.1 | 0.20 | 1.00 | +13.6 | +19.4 |
| `asian_range_gte_30` | 12 | S_STRANGER | 70.6% | 25.0% | 25.0% | 16.7% | -9.0 | 0.42 | 1.11 | +17.6 | +14.5 |
| `confluence_gte_60` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -38.0 | 0.00 | 0.00 | +11.7 | +57.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 70.6% | 33.3% | 33.3% | 16.7% | -7.4 | 0.50 | 0.88 | +18.3 | +15.9 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 35.3% | 50.0% | 50.0% | 33.3% | +9.2 | 3.54 | 2.36 | +24.5 | +13.2 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 52.9% | 22.2% | 22.2% | 11.1% | -15.2 | 0.26 | 0.91 | +15.6 | +16.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 41.2% | 28.6% | 28.6% | 14.3% | -16.1 | 0.30 | 0.75 | +17.6 | +18.9 |
| `feature_fresh_reclaim_within_8` | 4 | R_REPEATER | 23.5% | 50.0% | 50.0% | 0.0% | -6.2 | 0.47 | 0.47 | +15.6 | +20.7 |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 76.5% | 30.8% | 30.8% | 7.7% | -13.0 | 0.29 | 0.66 | +15.5 | +18.7 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 88.2% | 33.3% | 33.3% | 20.0% | -9.8 | 0.38 | 0.68 | +15.8 | +16.4 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 52.9% | 44.4% | 44.4% | 11.1% | +0.0 | 1.01 | 1.26 | +16.9 | +15.3 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 17.6% | 33.3% | 33.3% | 0.0% | +2.5 | 1.34 | 2.68 | +19.7 | +17.1 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=2 Fav=50.0% Avg=+0.2; out_of_sample N=6 Fav=66.7% Avg=+3.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | S_STRANGER | 100.0% | 33.3% | 36.4% | 18.2% | -5.1 | 0.52 | 0.87 | +15.5 | +15.8 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 72.7% | 29.2% | 33.3% | 20.8% | -4.6 | 0.59 | 1.10 | +17.1 | +13.6 |
| `hunt_to_ar_ratio_le_2_5` | 30 | S_STRANGER | 90.9% | 30.0% | 33.3% | 20.0% | -5.7 | 0.50 | 0.95 | +15.6 | +16.1 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 81.8% | 25.9% | 29.6% | 18.5% | -5.0 | 0.53 | 1.20 | +16.1 | +14.1 |
| `asian_range_gte_30` | 30 | S_STRANGER | 90.9% | 30.0% | 33.3% | 16.7% | -5.1 | 0.53 | 1.00 | +15.2 | +15.8 |
| `confluence_gte_60` | 29 | S_STRANGER | 87.9% | 34.5% | 37.9% | 17.2% | -5.2 | 0.53 | 0.82 | +16.3 | +15.8 |
| `confluence_gte_70` | 8 | R_REPEATER | 24.2% | 62.5% | 62.5% | 25.0% | +2.9 | 1.38 | 0.83 | +24.9 | +17.2 |
| `tdi_rsi_gt_signal` | 28 | S_STRANGER | 84.8% | 28.6% | 32.1% | 10.7% | -8.2 | 0.35 | 0.70 | +14.2 | +17.3 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 39.4% | 23.1% | 23.1% | 7.7% | -7.6 | 0.17 | 0.56 | +10.4 | +15.2 |
| `ratio_le_2_and_asian_gte_30` | 22 | S_STRANGER | 66.7% | 27.3% | 31.8% | 18.2% | -4.1 | 0.61 | 1.23 | +17.1 | +13.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 18 | S_STRANGER | 54.5% | 22.2% | 27.8% | 11.1% | -7.5 | 0.41 | 0.99 | +15.3 | +14.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 81.8% | 25.9% | 29.6% | 18.5% | -5.0 | 0.53 | 1.20 | +16.1 | +14.1 |
| `feature_stale_hod_exhaustion_reject` | 33 | S_STRANGER | 100.0% | 33.3% | 36.4% | 18.2% | -5.1 | 0.52 | 0.87 | +15.5 | +15.8 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 6.1% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +5.5 | +13.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.0% | 0.0% | 0.0% | 0.0% | -11.9 | 0.00 | 0.00 | +5.9 | +21.7 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=20.0% Avg=-23.3; validation N=3 Fav=33.3% Avg=-2.1; out_of_sample N=2 Fav=100.0% Avg=+30.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | -11.9 | 0.48 | 0.95 | +18.8 | +21.9 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 73.3% | 18.2% | 18.2% | 9.1% | -16.9 | 0.30 | 1.35 | +16.4 | +21.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 80.0% | 25.0% | 25.0% | 8.3% | -12.3 | 0.44 | 1.33 | +18.5 | +20.1 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 80.0% | 25.0% | 25.0% | 8.3% | -13.7 | 0.38 | 1.14 | +17.0 | +19.8 |
| `asian_range_gte_30` | 14 | S_STRANGER | 93.3% | 28.6% | 28.6% | 7.1% | -14.3 | 0.41 | 1.03 | +18.5 | +23.2 |
| `confluence_gte_60` | 11 | S_STRANGER | 73.3% | 27.3% | 27.3% | 9.1% | -15.3 | 0.41 | 1.10 | +20.4 | +23.5 |
| `confluence_gte_70` | 1 | R_RUNNER | 6.7% | 100.0% | 100.0% | 0.0% | +38.6 | 999.00 | 999.00 | +41.7 | +8.1 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 26.7% | 50.0% | 50.0% | 0.0% | +3.8 | 1.54 | 1.54 | +19.5 | +14.9 |
| `tdi_rsi_gte_50` | 4 | R_REPEATER | 26.7% | 50.0% | 50.0% | 0.0% | +4.9 | 1.48 | 1.48 | +26.0 | +17.3 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 73.3% | 18.2% | 18.2% | 9.1% | -16.9 | 0.30 | 1.35 | +16.4 | +21.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -14.2 | 0.00 | 0.00 | +13.3 | +24.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 73.3% | 18.2% | 18.2% | 9.1% | -16.9 | 0.30 | 1.35 | +16.4 | +21.2 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | -11.9 | 0.48 | 0.95 | +18.8 | +21.9 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 46.7% | 28.6% | 28.6% | 14.3% | -9.9 | 0.51 | 1.28 | +18.0 | +18.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 0.0% | +4.4 | 1.68 | 1.68 | +28.8 | +15.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-15.0; validation N=3 Fav=33.3% Avg=-12.5; out_of_sample N=1 Fav=100.0% Avg=+20.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -3.1 | 0.72 | 1.56 | +14.6 | +23.0 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 75.0% | 33.3% | 33.3% | 20.0% | -3.2 | 0.70 | 1.26 | +14.4 | +25.9 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 90.0% | 27.8% | 27.8% | 16.7% | -4.2 | 0.59 | 1.42 | +13.2 | +24.3 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 80.0% | 31.2% | 31.2% | 18.8% | -2.2 | 0.76 | 1.51 | +13.8 | +22.1 |
| `asian_range_gte_30` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -3.1 | 0.72 | 1.56 | +14.6 | +23.0 |
| `confluence_gte_60` | 3 | R_REPEATER | 15.0% | 66.7% | 66.7% | 66.7% | +18.4 | 999.00 | 999.00 | +27.9 | +8.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 60.0% | 33.3% | 33.3% | 8.3% | -2.8 | 0.72 | 1.44 | +13.0 | +27.3 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | -10.3 | 0.30 | 0.89 | +11.1 | +31.7 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 75.0% | 33.3% | 33.3% | 20.0% | -3.2 | 0.70 | 1.26 | +14.4 | +25.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 50.0% | 30.0% | 30.0% | 0.0% | -7.8 | 0.34 | 0.79 | +10.4 | +30.4 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -25.6 | 0.00 | 0.00 | +6.8 | +44.1 |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 80.0% | 31.2% | 31.2% | 18.8% | -2.2 | 0.76 | 1.51 | +13.8 | +22.1 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 95.0% | 31.6% | 31.6% | 21.1% | -1.8 | 0.82 | 1.65 | +14.7 | +21.7 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 25.0% | 40.0% | 40.0% | 20.0% | -6.4 | 0.53 | 0.80 | +15.3 | +27.1 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 10.0% | 50.0% | 50.0% | 0.0% | -5.9 | 0.56 | 0.56 | +17.2 | +27.1 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-2.4; validation N=2 Fav=50.0% Avg=+9.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -1.3 | 0.76 | 1.51 | +13.2 | +15.8 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 25.0% | 37.5% | 25.0% | +0.5 | 1.12 | 1.50 | +11.9 | +11.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -1.3 | 0.76 | 1.51 | +13.2 | +15.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -1.3 | 0.76 | 1.51 | +13.2 | +15.8 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -1.3 | 0.76 | 1.51 | +13.2 | +15.8 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -1.3 | 0.76 | 1.51 | +13.2 | +15.8 |
| `confluence_gte_70` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -8.7 | 0.00 | 0.00 | +18.6 | +34.8 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 25.0% | 50.0% | 50.0% | +2.3 | 2.51 | 1.25 | +14.5 | +10.5 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 16.7% | -2.2 | 0.65 | 2.61 | +18.1 | +22.5 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 80.0% | 25.0% | 37.5% | 25.0% | +0.5 | 1.12 | 1.50 | +11.9 | +11.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 40.0% | 25.0% | 50.0% | 50.0% | +2.3 | 2.51 | 1.25 | +14.5 | +10.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 80.0% | 25.0% | 37.5% | 25.0% | +0.5 | 1.12 | 1.50 | +11.9 | +11.0 |
| `feature_stale_hod_exhaustion_reject` | 8 | S_STRANGER | 80.0% | 25.0% | 37.5% | 25.0% | +0.5 | 1.12 | 1.50 | +11.9 | +11.0 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 50.0% | 20.0% | 40.0% | 20.0% | +0.6 | 1.13 | 1.13 | +14.6 | +10.6 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 16.7% | -2.2 | 0.65 | 2.61 | +18.1 | +22.5 |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=+9.4; validation N=1 Fav=0.0% Avg=-17.7; out_of_sample N=1 Fav=100.0% Avg=+38.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 10.0% | -8.2 | 0.45 | 1.59 | +14.5 | +19.6 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +9.4 | 3.63 | 3.63 | +16.3 | +10.8 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 10.0% | -8.2 | 0.45 | 1.59 | +14.5 | +19.6 |
| `stop_hunt_le_90` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | -4.8 | 0.62 | 1.86 | +12.8 | +17.7 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 10.0% | -8.2 | 0.45 | 1.59 | +14.5 | +19.6 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 10.0% | -8.2 | 0.45 | 1.59 | +14.5 | +19.6 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 10.0% | -8.2 | 0.45 | 1.59 | +14.5 | +19.6 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -23.4 | 0.00 | 0.00 | +8.9 | +28.5 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 40.0% | 40.0% | 0.0% | +9.9 | 3.57 | 5.35 | +23.6 | +8.7 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +9.4 | 3.63 | 3.63 | +16.3 | +10.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | +0.4 | 1.04 | 2.08 | +13.9 | +15.4 |
| `feature_stale_hod_exhaustion_reject` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 11.1% | -13.4 | 0.20 | 1.38 | +11.6 | +21.2 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 0.0% | -11.4 | 0.41 | 1.62 | +15.3 | +23.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | +12.4 | 25.87 | 51.73 | +21.4 | +7.0 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+4.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -12.5 | 0.20 | 0.59 | +24.2 | +28.2 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -22.4 | 0.12 | 0.59 | +22.5 | +37.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 14.3% | -19.2 | 0.12 | 0.59 | +24.4 | +33.0 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -12.5 | 0.20 | 0.59 | +24.2 | +28.2 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -12.5 | 0.20 | 0.59 | +24.2 | +28.2 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 40.0% | 40.0% | 20.0% | +4.3 | 3.22 | 3.22 | +24.6 | +21.9 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 12.5% | -15.2 | 0.20 | 0.51 | +24.1 | +32.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +3.1 | 3.61 | 3.61 | +23.8 | +16.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -12.5 | 0.20 | 0.59 | +24.2 | +28.2 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 25.0% | -20.6 | 0.00 | 0.00 | +27.4 | +26.1 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 25.0% | -21.2 | 0.00 | 0.00 | +27.1 | +31.0 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=20.0% Avg=-5.7; out_of_sample N=7 Fav=28.6% Avg=-12.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 16.7% | 26.7% | 13.3% | -6.8 | 0.41 | 1.06 | +14.3 | +14.7 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 80.0% | 16.7% | 29.2% | 8.3% | -8.2 | 0.33 | 0.81 | +13.1 | +15.6 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 86.7% | 19.2% | 30.8% | 15.4% | -6.0 | 0.47 | 1.00 | +14.1 | +14.8 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 90.0% | 18.5% | 29.6% | 14.8% | -5.8 | 0.47 | 1.06 | +15.5 | +14.7 |
| `asian_range_gte_30` | 25 | S_STRANGER | 83.3% | 16.0% | 28.0% | 8.0% | -9.0 | 0.31 | 0.78 | +12.7 | +15.5 |
| `confluence_gte_60` | 29 | S_STRANGER | 96.7% | 17.2% | 27.6% | 13.8% | -6.8 | 0.42 | 1.04 | +14.5 | +14.9 |
| `confluence_gte_70` | 13 | S_STRANGER | 43.3% | 15.4% | 15.4% | 15.4% | -5.5 | 0.47 | 2.33 | +10.7 | +14.5 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 40.0% | 25.0% | 33.3% | 16.7% | -9.6 | 0.46 | 0.92 | +15.0 | +21.3 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 50.0% | 20.0% | 26.7% | 13.3% | -7.0 | 0.37 | 1.01 | +17.6 | +19.9 |
| `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 80.0% | 16.7% | 29.2% | 8.3% | -8.2 | 0.33 | 0.81 | +13.1 | +15.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 33.3% | 20.0% | 30.0% | 10.0% | -14.7 | 0.28 | 0.65 | +13.3 | +22.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 90.0% | 18.5% | 29.6% | 14.8% | -5.8 | 0.47 | 1.06 | +15.5 | +14.7 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 16.7% | 26.7% | 13.3% | -6.8 | 0.41 | 1.06 | +14.3 | +14.7 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -8.6 | 0.00 | 0.00 | +10.0 | +8.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=0.0% Avg=-48.9; validation N=2 Fav=0.0% Avg=-35.3; out_of_sample N=1 Fav=100.0% Avg=+3.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 0.0% | -42.7 | 0.01 | 0.08 | +10.1 | +29.1 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 71.4% | 0.0% | 0.0% | 0.0% | -46.1 | 0.00 | 0.00 | +8.6 | +22.3 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 71.4% | 0.0% | 0.0% | 0.0% | -46.1 | 0.00 | 0.00 | +8.6 | +22.3 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 78.6% | 9.1% | 9.1% | 0.0% | -41.6 | 0.01 | 0.08 | +9.0 | +21.1 |
| `asian_range_gte_30` | 13 | S_STRANGER | 92.9% | 0.0% | 0.0% | 0.0% | -46.3 | 0.00 | 0.00 | +9.8 | +30.7 |
| `confluence_gte_60` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 0.0% | -45.1 | 0.00 | 0.00 | +9.1 | +40.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 0.0% | -37.8 | 0.02 | 0.07 | +11.9 | +49.3 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 0.0% | -37.8 | 0.02 | 0.07 | +11.9 | +49.3 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 71.4% | 0.0% | 0.0% | 0.0% | -46.1 | 0.00 | 0.00 | +8.6 | +22.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -83.8 | 0.00 | 0.00 | +0.0 | +94.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 71.4% | 0.0% | 0.0% | 0.0% | -46.1 | 0.00 | 0.00 | +8.6 | +22.3 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 0.0% | -42.7 | 0.01 | 0.08 | +10.1 | +29.1 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -51.0 | 0.00 | 0.00 | +10.4 | +19.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 0.0% | -40.1 | 0.04 | 0.04 | +6.7 | +51.6 |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
