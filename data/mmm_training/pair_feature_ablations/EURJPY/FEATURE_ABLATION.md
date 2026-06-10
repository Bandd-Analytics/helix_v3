# EURJPY Pair Feature Ablation

Generated: 2026-06-09T15:36:14.575496+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 20 | R_REPEATER | 55.0% | +17.2 | `asian_range_gte_30` | 17 | R_REPEATER | 58.8% | +20.2 | 5.57 | 3.90 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 13 | R_REPEATER | 53.8% | +3.9 | `tdi_rsi_gte_50` | 8 | R_REPEATER | 62.5% | +12.0 | 5.05 | 2.02 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 25 | R_REPEATER | 52.0% | +7.7 | `asian_range_gte_30` | 19 | R_REPEATER | 68.4% | +11.6 | 11.65 | 2.69 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 22 | R_REPEATER | 50.0% | +10.8 | `ratio_le_2_asian_gte_30_tdi_positive` | 13 | R_REPEATER | 53.8% | +13.5 | 6.09 | 5.22 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L2|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 10 | R_REPEATER | 50.0% | +6.7 | `feature_eurjpy_tdi50_reclaim` | 5 | R_REPEATER | 60.0% | +9.1 | 2.94 | 1.96 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | R_REPEATER | 50.0% | +5.6 | `asian_range_gte_30` | 6 | R_REPEATER | 66.7% | +9.1 | 3.34 | 1.67 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | R_REPEATER | 50.0% | -2.1 | `tdi_rsi_gt_signal` | 6 | R_RUNNER | 83.3% | +13.6 | 7.21 | 1.44 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 21 | S_STRANGER | 47.6% | +10.1 | `feature_eurjpy_tdi50_reclaim` | 9 | R_REPEATER | 66.7% | +17.2 | 12.90 | 6.45 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 21 | S_STRANGER | 47.6% | +2.6 | `tdi_rsi_gt_signal` | 5 | R_RUNNER | 80.0% | +17.2 | 11.02 | 2.76 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | S_STRANGER | 47.1% | +16.3 | `feature_eurjpy_tdi50_reclaim` | 7 | R_REPEATER | 71.4% | +26.3 | 8.64 | 3.46 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 46.2% | +2.6 | `tdi_rsi_gte_50` | 10 | R_REPEATER | 60.0% | +8.8 | 15.60 | 10.40 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 11 | S_STRANGER | 45.5% | +1.4 | `confluence_gte_60` | 7 | R_REPEATER | 57.1% | +8.9 | 2.37 | 0.95 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 42.9% | +10.6 | `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 66.7% | +12.7 | 4.69 | 2.35 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 14 | S_STRANGER | 42.9% | +10.1 | `hunt_to_ar_ratio_le_2_0` | 8 | R_REPEATER | 62.5% | +20.1 | 3.28 | 1.31 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 21 | S_STRANGER | 42.9% | +5.8 | `all` | 21 | S_STRANGER | 42.9% | +5.8 | 2.82 | 3.77 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 28 | S_STRANGER | 42.9% | +1.1 | `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 44.0% | +3.4 | 1.99 | 2.17 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 41.7% | +9.0 | `hunt_to_ar_ratio_le_2_0` | 8 | R_REPEATER | 62.5% | +17.5 | 37.00 | 22.20 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 41.7% | +3.8 | `ratio_le_2_asian_gte_30_tdi_positive` | 11 | R_REPEATER | 63.6% | +11.7 | 6.82 | 3.90 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 38.5% | +3.7 | `tdi_rsi_gte_50` | 8 | R_REPEATER | 62.5% | +5.4 | 2.44 | 1.46 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 37.5% | +9.6 | `confluence_gte_70` | 6 | R_REPEATER | 50.0% | +24.9 | 20.92 | 20.92 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 36.8% | +7.7 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 44.4% | +13.3 | 5.98 | 5.98 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 36.4% | +6.6 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 40.0% | +8.1 | 6.21 | 6.21 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 22 | S_STRANGER | 36.4% | +4.7 | `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 43.8% | +6.2 | 2.01 | 2.01 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 11 | S_STRANGER | 36.4% | +2.6 | `confluence_gte_60` | 9 | S_STRANGER | 44.4% | +3.6 | 3.29 | 4.11 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 36.4% | +0.1 | `tdi_rsi_gt_signal` | 7 | R_REPEATER | 57.1% | +3.6 | 1.84 | 1.38 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 34 | S_STRANGER | 35.3% | +5.4 | `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 40.0% | +8.8 | 2.84 | 4.26 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 33.3% | -0.5 | `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 42.9% | +1.9 | 1.45 | 1.94 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 33.3% | -6.0 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 44.4% | -3.8 | 0.55 | 0.68 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 25 | S_STRANGER | 32.0% | +0.8 | `tdi_rsi_gt_signal` | 10 | R_REPEATER | 70.0% | +13.7 | 8.12 | 3.48 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 31.6% | +3.0 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 36.4% | +5.1 | 2.17 | 3.80 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 38 | S_STRANGER | 31.6% | -5.2 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 25.0% | +3.9 | 1.82 | 3.64 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 30.4% | +6.3 | `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 33.3% | +7.0 | 3.40 | 3.82 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 29.4% | -1.8 | `tdi_rsi_gte_50` | 13 | S_STRANGER | 38.5% | -1.1 | 0.88 | 1.03 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 41 | S_STRANGER | 29.3% | +3.0 | `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 40.0% | +4.1 | 1.83 | 2.75 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 29.2% | +1.3 | `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 40.0% | +3.2 | 1.59 | 2.38 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 18 | S_STRANGER | 27.8% | -5.7 | `confluence_gte_70` | 5 | R_REPEATER | 60.0% | +7.5 | 2.65 | 0.66 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 22 | S_STRANGER | 27.3% | -6.2 | `tdi_rsi_gte_50` | 15 | S_STRANGER | 33.3% | +2.4 | 1.32 | 2.64 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 11 | S_STRANGER | 27.3% | -19.0 | `tdi_rsi_gte_50` | 5 | R_REPEATER | 60.0% | +7.0 | 4.03 | 2.69 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 31 | S_STRANGER | 25.8% | +1.0 | `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 33.3% | +2.9 | 1.54 | 2.40 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | +6.9 | `all` | 12 | S_STRANGER | 25.0% | +6.9 | 2.46 | 7.37 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 25.0% | +1.6 | `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 26.7% | +3.3 | 1.44 | 2.60 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 25.0% | +1.3 | `asian_range_gte_30` | 13 | S_STRANGER | 30.8% | +2.9 | 1.73 | 3.47 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | -5.5 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 33.3% | +1.0 | 1.30 | 1.74 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 17 | S_STRANGER | 23.5% | -13.3 | `asian_range_gte_30` | 9 | S_STRANGER | 33.3% | -0.7 | 0.93 | 1.87 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 60 | S_STRANGER | 23.3% | -0.8 | `tdi_rsi_gte_50` | 42 | S_STRANGER | 26.2% | -1.5 | 0.72 | 1.98 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 23 | S_STRANGER | 21.7% | -12.4 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 44.4% | -1.5 | 0.86 | 1.07 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 37 | S_STRANGER | 21.6% | +2.6 | `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 26.9% | +4.5 | 1.62 | 4.17 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 21.4% | -0.9 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 25.0% | +0.2 | 1.08 | 3.23 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 42 | S_STRANGER | 21.4% | -2.5 | `asian_range_gte_30` | 40 | S_STRANGER | 22.5% | -2.6 | 0.58 | 1.68 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 39 | S_STRANGER | 20.5% | -5.1 | `confluence_gte_70` | 12 | S_STRANGER | 33.3% | +9.1 | 4.51 | 5.41 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 30 | S_STRANGER | 20.0% | +1.9 | `tdi_rsi_gt_signal` | 21 | S_STRANGER | 28.6% | +6.3 | 2.37 | 4.75 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -6.1 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 40.0% | +0.7 | 1.10 | 1.65 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 22 | S_STRANGER | 18.2% | -0.9 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 25.0% | +1.4 | 1.24 | 3.11 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 17.6% | -2.5 | `feature_momentum_breakout_exception` | 6 | R_REPEATER | 50.0% | +10.6 | 5.66 | 5.66 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -3.8 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 20.0% | +1.5 | 1.66 | 3.32 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -14.1 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 22.2% | -15.9 | 0.14 | 0.50 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -14.2 | `confluence_gte_60` | 7 | S_STRANGER | 28.6% | -12.8 | 0.35 | 0.87 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 15.8% | -2.9 | `stop_hunt_le_90` | 16 | S_STRANGER | 18.8% | -1.0 | 0.82 | 3.57 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 26 | S_STRANGER | 15.4% | -7.4 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 33.3% | +11.4 | 4.24 | 5.65 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 14.3% | -1.2 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 22.2% | +0.8 | 1.49 | 4.46 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -9.6 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 20.0% | -9.8 | 0.19 | 0.74 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 26 | S_STRANGER | 11.5% | -13.0 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 20.0% | -2.1 | 0.68 | 2.73 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 35 | S_STRANGER | 11.4% | -5.2 | `confluence_gte_60` | 12 | S_STRANGER | 16.7% | +1.4 | 1.55 | 4.64 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 32 | S_STRANGER | 9.4% | -11.5 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 18.8% | -3.1 | 0.32 | 1.27 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 9.1% | -2.3 | `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 16.7% | +1.3 | 1.66 | 6.62 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 9.1% | -5.3 | `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 14.3% | -1.2 | 0.72 | 1.80 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 8.3% | -5.7 | `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 10.0% | -5.5 | 0.21 | 1.67 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 12 | S_STRANGER | 8.3% | -7.7 | `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 16.7% | -4.2 | 0.65 | 3.27 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 7.7% | -4.6 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 16.7% | +1.4 | 1.82 | 3.63 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 6.7% | -2.6 | `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 10.0% | -2.6 | 0.43 | 3.88 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 6.7% | -4.8 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 11.1% | -5.1 | 0.29 | 2.29 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 15 | S_STRANGER | 6.7% | -8.2 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 10.0% | -6.7 | 0.15 | 1.20 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 17 | S_STRANGER | 5.9% | -6.0 | `tdi_rsi_gt_signal` | 11 | S_STRANGER | 9.1% | -4.6 | 0.34 | 1.36 | 0 | 1 | fail |

## Candidate Details

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=11 Fav=54.5% Avg=+19.1; validation N=4 Fav=75.0% Avg=+35.5; out_of_sample N=2 Fav=50.0% Avg=-4.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | R_REPEATER | 100.0% | 55.0% | 55.0% | 15.0% | +17.2 | 5.29 | 4.33 | +30.5 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 60.0% | 50.0% | 50.0% | 8.3% | +15.1 | 3.51 | 3.51 | +28.3 | +10.3 |
| `hunt_to_ar_ratio_le_2_5` | 19 | R_REPEATER | 95.0% | 52.6% | 52.6% | 15.8% | +17.1 | 5.06 | 4.55 | +30.6 | +8.6 |
| `stop_hunt_le_90` | 16 | R_REPEATER | 80.0% | 50.0% | 50.0% | 12.5% | +12.9 | 3.67 | 3.67 | +26.2 | +8.6 |
| `asian_range_gte_30` | 17 | R_REPEATER | 85.0% | 58.8% | 58.8% | 17.6% | +20.2 | 5.57 | 3.90 | +33.7 | +9.7 |
| `confluence_gte_60` | 20 | R_REPEATER | 100.0% | 55.0% | 55.0% | 15.0% | +17.2 | 5.29 | 4.33 | +30.5 | +8.8 |
| `confluence_gte_70` | 20 | R_REPEATER | 100.0% | 55.0% | 55.0% | 15.0% | +17.2 | 5.29 | 4.33 | +30.5 | +8.8 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 25.0% | 40.0% | 40.0% | 0.0% | +2.3 | 1.92 | 2.88 | +12.5 | +9.3 |
| `tdi_rsi_gte_50` | 18 | R_REPEATER | 90.0% | 50.0% | 50.0% | 11.1% | +14.0 | 4.16 | 4.16 | +27.7 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | R_REPEATER | 60.0% | 50.0% | 50.0% | 8.3% | +15.1 | 3.51 | 3.51 | +28.3 | +10.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +3.9 | +15.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | R_REPEATER | 65.0% | 53.8% | 53.8% | 15.4% | +15.9 | 3.85 | 3.30 | +29.3 | +9.7 |
| `feature_stale_hod_exhaustion_reject` | 14 | R_REPEATER | 70.0% | 57.1% | 57.1% | 21.4% | +17.7 | 4.57 | 3.43 | +32.5 | +10.2 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 30.0% | 33.3% | 33.3% | 16.7% | +4.1 | 1.38 | 2.77 | +26.1 | +14.7 |
| `feature_eurjpy_tdi50_reclaim` | 12 | S_STRANGER | 60.0% | 41.7% | 41.7% | 8.3% | +10.1 | 2.60 | 3.64 | +26.1 | +10.2 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=66.7% Avg=+15.7; validation N=1 Fav=100.0% Avg=+8.0; out_of_sample N=1 Fav=0.0% Avg=-6.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | R_REPEATER | 100.0% | 53.8% | 53.8% | 46.2% | +3.9 | 1.41 | 1.01 | +20.9 | +6.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 76.9% | 50.0% | 50.0% | 50.0% | +6.9 | 2.40 | 1.92 | +20.5 | +7.6 |
| `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 92.3% | 50.0% | 50.0% | 41.7% | +1.4 | 1.13 | 0.94 | +19.8 | +6.9 |
| `stop_hunt_le_90` | 10 | R_REPEATER | 76.9% | 50.0% | 50.0% | 50.0% | +1.2 | 1.11 | 0.89 | +20.6 | +5.6 |
| `asian_range_gte_30` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 45.5% | -0.4 | 0.96 | 0.96 | +19.0 | +7.8 |
| `confluence_gte_60` | 4 | R_RUNNER | 30.8% | 100.0% | 100.0% | 50.0% | +27.8 | 999.00 | 999.00 | +30.6 | +4.3 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | R_REPEATER | 69.2% | 55.6% | 55.6% | 33.3% | +1.0 | 1.08 | 0.86 | +20.0 | +6.9 |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 61.5% | 62.5% | 62.5% | 50.0% | +12.0 | 5.05 | 2.02 | +21.3 | +8.2 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 61.5% | 37.5% | 37.5% | 50.0% | +1.8 | 1.28 | 1.71 | +17.7 | +8.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 38.5% | 40.0% | 40.0% | 40.0% | +1.4 | 1.17 | 1.75 | +16.9 | +10.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | R_REPEATER | 76.9% | 50.0% | 50.0% | 50.0% | +1.2 | 1.11 | 0.89 | +20.6 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 13 | R_REPEATER | 100.0% | 53.8% | 53.8% | 46.2% | +3.9 | 1.41 | 1.01 | +20.9 | +6.9 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 50.0% | +0.9 | 1.27 | 1.27 | +16.4 | +10.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 50.0% | +0.9 | 1.27 | 1.27 | +16.4 | +10.2 |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=16 Fav=68.8% Avg=+11.7; validation N=2 Fav=50.0% Avg=+2.9; out_of_sample N=1 Fav=100.0% Avg=+27.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | R_REPEATER | 100.0% | 52.0% | 52.0% | 32.0% | +7.7 | 5.03 | 3.49 | +18.5 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 44.0% | 45.5% | 45.5% | 27.3% | +5.2 | 5.14 | 3.09 | +16.4 | +5.8 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 92.0% | 47.8% | 47.8% | 30.4% | +5.9 | 3.82 | 3.12 | +16.7 | +6.7 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 64.0% | 37.5% | 37.5% | 18.8% | +3.8 | 2.69 | 3.14 | +14.1 | +6.5 |
| `asian_range_gte_30` | 19 | R_REPEATER | 76.0% | 68.4% | 68.4% | 42.1% | +11.6 | 11.65 | 2.69 | +23.2 | +6.0 |
| `confluence_gte_60` | 25 | R_REPEATER | 100.0% | 52.0% | 52.0% | 32.0% | +7.7 | 5.03 | 3.49 | +18.5 | +6.5 |
| `confluence_gte_70` | 25 | R_REPEATER | 100.0% | 52.0% | 52.0% | 32.0% | +7.7 | 5.03 | 3.49 | +18.5 | +6.5 |
| `tdi_rsi_gt_signal` | 12 | R_REPEATER | 48.0% | 58.3% | 58.3% | 33.3% | +8.6 | 9.52 | 4.08 | +21.1 | +5.2 |
| `tdi_rsi_gte_50` | 11 | R_REPEATER | 44.0% | 63.6% | 63.6% | 36.4% | +11.1 | 7.70 | 4.40 | +22.1 | +6.5 |
| `ratio_le_2_and_asian_gte_30` | 9 | R_REPEATER | 36.0% | 55.6% | 55.6% | 33.3% | +6.8 | 7.74 | 1.55 | +19.2 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 16.0% | 50.0% | 50.0% | 50.0% | +10.7 | 999.00 | 999.00 | +23.2 | +3.1 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 4.0% | 100.0% | 100.0% | 0.0% | +10.2 | 999.00 | 999.00 | +22.0 | +4.5 |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 56.0% | 42.9% | 42.9% | 21.4% | +5.4 | 4.29 | 3.57 | +15.7 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 25 | R_REPEATER | 100.0% | 52.0% | 52.0% | 32.0% | +7.7 | 5.03 | 3.49 | +18.5 | +6.5 |
| `feature_momentum_breakout_exception` | 12 | R_REPEATER | 48.0% | 50.0% | 50.0% | 33.3% | +6.0 | 3.97 | 3.31 | +16.7 | +6.6 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 24.0% | 66.7% | 66.7% | 50.0% | +9.4 | 6.79 | 3.39 | +20.4 | +6.6 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=50.0% Avg=+6.6; validation N=1 Fav=100.0% Avg=+67.2; out_of_sample N=4 Fav=50.0% Avg=+14.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | R_REPEATER | 100.0% | 50.0% | 50.0% | 40.9% | +10.8 | 6.39 | 5.81 | +20.6 | +5.1 |
| `hunt_to_ar_ratio_le_2_0` | 18 | R_REPEATER | 81.8% | 50.0% | 50.0% | 50.0% | +11.7 | 6.68 | 5.94 | +21.5 | +5.1 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 95.5% | 47.6% | 47.6% | 42.9% | +10.5 | 6.03 | 6.03 | +20.8 | +5.0 |
| `stop_hunt_le_90` | 17 | R_REPEATER | 77.3% | 52.9% | 52.9% | 52.9% | +13.2 | 10.77 | 8.38 | +22.8 | +4.6 |
| `asian_range_gte_30` | 21 | R_REPEATER | 95.5% | 52.4% | 52.4% | 42.9% | +11.3 | 6.47 | 5.29 | +21.5 | +4.8 |
| `confluence_gte_60` | 22 | R_REPEATER | 100.0% | 50.0% | 50.0% | 40.9% | +10.8 | 6.39 | 5.81 | +20.6 | +5.1 |
| `confluence_gte_70` | 22 | R_REPEATER | 100.0% | 50.0% | 50.0% | 40.9% | +10.8 | 6.39 | 5.81 | +20.6 | +5.1 |
| `tdi_rsi_gt_signal` | 16 | R_REPEATER | 72.7% | 50.0% | 50.0% | 43.8% | +11.7 | 5.50 | 5.50 | +22.5 | +5.1 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 81.8% | 38.9% | 38.9% | 33.3% | +8.1 | 4.32 | 6.17 | +19.0 | +5.5 |
| `ratio_le_2_and_asian_gte_30` | 17 | R_REPEATER | 77.3% | 52.9% | 52.9% | 52.9% | +12.4 | 6.78 | 5.27 | +22.7 | +4.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | R_REPEATER | 59.1% | 53.8% | 53.8% | 53.8% | +13.5 | 6.09 | 5.22 | +24.0 | +5.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | R_REPEATER | 77.3% | 52.9% | 52.9% | 52.9% | +13.2 | 10.77 | 8.38 | +22.8 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 22 | R_REPEATER | 100.0% | 50.0% | 50.0% | 40.9% | +10.8 | 6.39 | 5.81 | +20.6 | +5.1 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 40.9% | 44.4% | 44.4% | 44.4% | +5.1 | 2.41 | 3.01 | +18.4 | +5.5 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 31.8% | 28.6% | 28.6% | 28.6% | +0.5 | 1.11 | 2.77 | +14.9 | +6.5 |

### THE_33_MW|BUY|EARLY_WEEK|L2|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L2|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-7.3; validation N=4 Fav=75.0% Avg=+13.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +6.7 | 2.90 | 2.90 | +32.7 | +9.1 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +6.7 | 2.90 | 2.90 | +32.7 | +9.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +6.7 | 2.90 | 2.90 | +32.7 | +9.1 |
| `stop_hunt_le_90` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +6.7 | 2.90 | 2.90 | +32.7 | +9.1 |
| `asian_range_gte_30` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +6.7 | 2.90 | 2.90 | +32.7 | +9.1 |
| `confluence_gte_60` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +6.7 | 2.90 | 2.90 | +32.7 | +9.1 |
| `confluence_gte_70` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +6.7 | 2.90 | 2.90 | +32.7 | +9.1 |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +6.4 | 999.00 | 999.00 | +21.6 | +4.6 |
| `tdi_rsi_gte_50` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +6.7 | 2.90 | 2.90 | +32.7 | +9.1 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +6.7 | 2.90 | 2.90 | +32.7 | +9.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +6.4 | 999.00 | 999.00 | +21.6 | +4.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 0.0% | +6.7 | 2.90 | 2.90 | +32.7 | +9.1 |
| `feature_stale_hod_exhaustion_reject` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 0.0% | +2.3 | 1.73 | 3.46 | +29.1 | +10.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 0.0% | +9.1 | 2.94 | 1.96 | +31.2 | +11.1 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+3.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=100.0% Avg=+20.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +5.6 | 2.96 | 2.37 | +18.0 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +5.6 | 2.96 | 2.37 | +18.0 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +5.6 | 2.96 | 2.37 | +18.0 | +6.1 |
| `stop_hunt_le_90` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +5.6 | 2.96 | 2.37 | +18.0 | +6.1 |
| `asian_range_gte_30` | 6 | R_REPEATER | 60.0% | 66.7% | 66.7% | 16.7% | +9.1 | 3.34 | 1.67 | +18.9 | +7.4 |
| `confluence_gte_60` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 0.0% | +5.3 | 2.26 | 0.75 | +15.8 | +8.8 |
| `confluence_gte_70` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 0.0% | +4.8 | 1.91 | 0.95 | +15.2 | +10.8 |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +7.3 | 999.00 | 999.00 | +18.3 | +0.6 |
| `tdi_rsi_gte_50` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 0.0% | +8.1 | 6.90 | 4.60 | +19.0 | +4.4 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 60.0% | 66.7% | 66.7% | 16.7% | +9.1 | 3.34 | 1.67 | +18.9 | +7.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +7.3 | 999.00 | 999.00 | +18.3 | +0.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +5.6 | 2.96 | 2.37 | +18.0 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +5.6 | 2.96 | 2.37 | +18.0 | +6.1 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 25.0% | +8.5 | 15.12 | 15.12 | +21.1 | +2.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -2.1 | 0.00 | 0.00 | +9.7 | +5.7 |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=75.0% Avg=+15.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=100.0% Avg=+10.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | -2.1 | 0.82 | 0.82 | +19.6 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | -2.1 | 0.82 | 0.82 | +19.6 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | -2.1 | 0.82 | 0.82 | +19.6 | +4.8 |
| `stop_hunt_le_90` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | -2.1 | 0.82 | 0.82 | +19.6 | +4.8 |
| `asian_range_gte_30` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | -2.1 | 0.82 | 0.82 | +19.6 | +4.8 |
| `confluence_gte_60` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 6 | R_RUNNER | 60.0% | 83.3% | 83.3% | 50.0% | +13.6 | 7.21 | 1.44 | +26.0 | +5.9 |
| `tdi_rsi_gte_50` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | -2.1 | 0.82 | 0.82 | +19.6 | +4.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_RUNNER | 60.0% | 83.3% | 83.3% | 50.0% | +13.6 | 7.21 | 1.44 | +26.0 | +5.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | -2.1 | 0.82 | 0.82 | +19.6 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | -2.1 | 0.82 | 0.82 | +19.6 | +4.8 |
| `feature_momentum_breakout_exception` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 33.3% | -2.4 | 0.78 | 0.78 | +17.5 | +4.6 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+11.5; validation N=2 Fav=100.0% Avg=+21.4; out_of_sample N=1 Fav=100.0% Avg=+42.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 14.3% | +10.1 | 5.96 | 5.96 | +19.5 | +8.0 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 66.7% | 42.9% | 42.9% | 14.3% | +8.3 | 5.09 | 5.94 | +16.8 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 18 | R_REPEATER | 85.7% | 50.0% | 50.0% | 11.1% | +10.8 | 7.53 | 6.69 | +19.3 | +8.0 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 81.0% | 47.1% | 47.1% | 11.8% | +9.9 | 6.62 | 6.62 | +18.6 | +8.3 |
| `asian_range_gte_30` | 20 | S_STRANGER | 95.2% | 45.0% | 45.0% | 15.0% | +9.6 | 5.50 | 6.11 | +19.3 | +8.1 |
| `confluence_gte_60` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 14.3% | +10.1 | 5.96 | 5.96 | +19.5 | +8.0 |
| `confluence_gte_70` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 14.3% | +10.1 | 5.96 | 5.96 | +19.5 | +8.0 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 71.4% | 46.7% | 46.7% | 13.3% | +9.9 | 4.92 | 4.92 | +19.1 | +9.8 |
| `tdi_rsi_gte_50` | 15 | R_REPEATER | 71.4% | 53.3% | 53.3% | 0.0% | +11.1 | 5.94 | 5.20 | +20.5 | +8.6 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 61.9% | 38.5% | 38.5% | 15.4% | +7.4 | 4.40 | 6.16 | +16.3 | +8.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 47.6% | 40.0% | 40.0% | 20.0% | +8.2 | 4.25 | 5.31 | +16.2 | +10.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 66.7% | 42.9% | 42.9% | 14.3% | +8.3 | 5.09 | 5.94 | +16.8 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 14.3% | +10.1 | 5.96 | 5.96 | +19.5 | +8.0 |
| `feature_momentum_breakout_exception` | 10 | R_REPEATER | 47.6% | 60.0% | 60.0% | 20.0% | +14.5 | 8.99 | 4.50 | +22.8 | +7.6 |
| `feature_eurjpy_tdi50_reclaim` | 9 | R_REPEATER | 42.9% | 66.7% | 66.7% | 0.0% | +17.2 | 12.90 | 6.45 | +25.2 | +7.4 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=75.0% Avg=+18.8; validation N=1 Fav=100.0% Avg=+11.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 19.0% | +2.6 | 1.28 | 1.28 | +21.8 | +17.5 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 61.9% | 38.5% | 38.5% | 23.1% | -2.5 | 0.79 | 1.11 | +19.3 | +23.2 |
| `hunt_to_ar_ratio_le_2_5` | 20 | R_REPEATER | 95.2% | 50.0% | 50.0% | 20.0% | +3.2 | 1.34 | 1.21 | +22.8 | +17.8 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 81.0% | 47.1% | 47.1% | 23.5% | +4.2 | 1.46 | 1.46 | +23.6 | +18.6 |
| `asian_range_gte_30` | 20 | R_REPEATER | 95.2% | 50.0% | 50.0% | 15.0% | +2.8 | 1.28 | 1.28 | +21.4 | +17.5 |
| `confluence_gte_60` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 19.0% | +2.6 | 1.28 | 1.28 | +21.8 | +17.5 |
| `confluence_gte_70` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 19.0% | +2.6 | 1.28 | 1.28 | +21.8 | +17.5 |
| `tdi_rsi_gt_signal` | 5 | R_RUNNER | 23.8% | 80.0% | 80.0% | 20.0% | +17.2 | 11.02 | 2.76 | +28.3 | +7.1 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 85.7% | 44.4% | 44.4% | 11.1% | -0.8 | 0.93 | 1.04 | +20.4 | +20.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 57.1% | 41.7% | 41.7% | 16.7% | -2.7 | 0.79 | 1.11 | +18.4 | +23.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | R_RUNNER | 14.3% | 100.0% | 100.0% | 0.0% | +16.9 | 999.00 | 999.00 | +27.8 | +5.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 71.4% | 46.7% | 46.7% | 26.7% | +2.7 | 1.26 | 1.26 | +22.6 | +20.8 |
| `feature_stale_hod_exhaustion_reject` | 16 | R_REPEATER | 76.2% | 56.2% | 56.2% | 25.0% | +8.0 | 2.40 | 1.60 | +23.8 | +13.8 |
| `feature_momentum_breakout_exception` | 6 | R_REPEATER | 28.6% | 50.0% | 50.0% | 33.3% | +9.1 | 16.12 | 10.75 | +22.3 | +11.2 |
| `feature_eurjpy_tdi50_reclaim` | 12 | S_STRANGER | 57.1% | 41.7% | 41.7% | 8.3% | -0.9 | 0.90 | 1.08 | +19.4 | +18.3 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=75.0% Avg=+32.3; validation N=1 Fav=100.0% Avg=+39.0; out_of_sample N=2 Fav=50.0% Avg=+7.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 47.1% | 47.1% | 17.6% | +16.3 | 4.20 | 4.20 | +34.6 | +12.3 |
| `hunt_to_ar_ratio_le_2_0` | 15 | R_REPEATER | 88.2% | 53.3% | 53.3% | 20.0% | +18.6 | 4.28 | 3.21 | +37.6 | +12.6 |
| `hunt_to_ar_ratio_le_2_5` | 16 | R_REPEATER | 94.1% | 50.0% | 50.0% | 18.8% | +17.4 | 4.25 | 3.72 | +35.8 | +12.2 |
| `stop_hunt_le_90` | 14 | R_REPEATER | 82.4% | 50.0% | 50.0% | 21.4% | +13.6 | 3.35 | 2.87 | +30.8 | +11.7 |
| `asian_range_gte_30` | 15 | S_STRANGER | 88.2% | 46.7% | 46.7% | 13.3% | +17.3 | 4.03 | 4.03 | +36.8 | +13.0 |
| `confluence_gte_60` | 14 | R_REPEATER | 82.4% | 50.0% | 50.0% | 21.4% | +21.9 | 8.63 | 7.40 | +39.4 | +10.7 |
| `confluence_gte_70` | 5 | R_REPEATER | 29.4% | 60.0% | 60.0% | 20.0% | +31.7 | 62.00 | 41.33 | +42.1 | +4.8 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 35.3% | 33.3% | 33.3% | 0.0% | +3.1 | 1.34 | 2.67 | +25.0 | +12.8 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 70.6% | 58.3% | 58.3% | 8.3% | +25.6 | 9.15 | 6.54 | +42.6 | +9.6 |
| `ratio_le_2_and_asian_gte_30` | 14 | R_REPEATER | 82.4% | 50.0% | 50.0% | 14.3% | +18.6 | 4.06 | 3.48 | +38.8 | +13.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 35.3% | 33.3% | 33.3% | 0.0% | +3.1 | 1.34 | 2.67 | +25.0 | +12.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | R_REPEATER | 76.5% | 53.8% | 53.8% | 23.1% | +14.7 | 3.38 | 2.41 | +32.5 | +12.1 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 70.6% | 33.3% | 33.3% | 16.7% | +7.1 | 2.00 | 3.50 | +29.8 | +14.6 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 29.4% | 40.0% | 40.0% | 20.0% | +6.2 | 2.27 | 2.27 | +22.9 | +12.8 |
| `feature_eurjpy_tdi50_reclaim` | 7 | R_REPEATER | 41.2% | 71.4% | 71.4% | 14.3% | +26.3 | 8.64 | 3.46 | +37.6 | +9.4 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=57.1% Avg=+8.1; validation N=2 Fav=50.0% Avg=+4.8; out_of_sample N=1 Fav=100.0% Avg=+21.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 0.0% | +2.6 | 1.58 | 1.84 | +16.4 | +9.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 61.5% | 25.0% | 25.0% | 0.0% | -3.9 | 0.47 | 1.41 | +10.8 | +10.8 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 76.9% | 30.0% | 30.0% | 0.0% | -3.0 | 0.49 | 1.14 | +12.9 | +9.7 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 61.5% | 25.0% | 25.0% | 0.0% | -3.9 | 0.47 | 1.41 | +10.8 | +10.8 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 0.0% | +2.6 | 1.58 | 1.84 | +16.4 | +9.0 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 0.0% | +2.6 | 1.58 | 1.84 | +16.4 | +9.0 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 0.0% | +2.6 | 1.58 | 1.84 | +16.4 | +9.0 |
| `tdi_rsi_gt_signal` | 12 | R_REPEATER | 92.3% | 50.0% | 50.0% | 0.0% | +3.0 | 1.63 | 1.63 | +17.2 | +9.5 |
| `tdi_rsi_gte_50` | 10 | R_REPEATER | 76.9% | 60.0% | 60.0% | 0.0% | +8.8 | 15.60 | 10.40 | +19.8 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 61.5% | 25.0% | 25.0% | 0.0% | -3.9 | 0.47 | 1.41 | +10.8 | +10.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 53.8% | 28.6% | 28.6% | 0.0% | -4.2 | 0.48 | 1.21 | +11.3 | +11.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 61.5% | 25.0% | 25.0% | 0.0% | -3.9 | 0.47 | 1.41 | +10.8 | +10.8 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 0.0% | +2.6 | 1.58 | 1.84 | +16.4 | +9.0 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 0.0% | -4.8 | 0.48 | 1.90 | +9.6 | +13.7 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 30.8% | 50.0% | 50.0% | 0.0% | +7.8 | 11.47 | 11.47 | +15.7 | +5.2 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+2.6; validation N=1 Fav=100.0% Avg=+23.2; out_of_sample N=2 Fav=50.0% Avg=+14.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 45.5% | 54.5% | 36.4% | +1.4 | 1.14 | 0.95 | +22.0 | +14.0 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 28.6% | -1.9 | 0.83 | 1.11 | +18.9 | +15.8 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 90.9% | 50.0% | 60.0% | 40.0% | +4.7 | 1.61 | 1.07 | +23.9 | +12.0 |
| `stop_hunt_le_90` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 28.6% | -1.9 | 0.83 | 1.11 | +18.9 | +15.8 |
| `asian_range_gte_30` | 9 | R_REPEATER | 81.8% | 55.6% | 66.7% | 44.4% | +6.8 | 1.95 | 0.97 | +25.9 | +11.5 |
| `confluence_gte_60` | 7 | R_REPEATER | 63.6% | 57.1% | 71.4% | 42.9% | +8.9 | 2.37 | 0.95 | +27.9 | +11.1 |
| `confluence_gte_70` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 100.0% | +31.4 | 999.00 | 999.00 | +56.7 | +3.6 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 90.9% | 40.0% | 50.0% | 30.0% | -0.2 | 0.98 | 0.98 | +20.7 | +15.2 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 16.7% | -6.5 | 0.50 | 0.99 | +14.5 | +17.4 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 33.3% | +0.1 | 1.01 | 1.01 | +21.1 | +15.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 20.0% | -3.3 | 0.74 | 1.11 | +18.4 | +18.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 25.0% | -5.6 | 0.59 | 0.98 | +16.9 | +18.1 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 45.5% | 54.5% | 36.4% | +1.4 | 1.14 | 0.95 | +22.0 | +14.0 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 54.5% | 16.7% | 33.3% | 16.7% | -9.7 | 0.39 | 0.79 | +12.5 | +19.7 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -10.3 | 0.36 | 1.08 | +11.7 | +21.1 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=-6.7; validation N=2 Fav=100.0% Avg=+29.0; out_of_sample N=1 Fav=100.0% Avg=+38.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 28.6% | +10.6 | 4.32 | 5.77 | +22.0 | +7.8 |
| `hunt_to_ar_ratio_le_2_0` | 9 | R_REPEATER | 64.3% | 55.6% | 55.6% | 33.3% | +13.4 | 5.78 | 4.62 | +26.3 | +7.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | R_REPEATER | 78.6% | 54.5% | 54.5% | 36.4% | +15.0 | 6.95 | 5.79 | +26.3 | +7.7 |
| `stop_hunt_le_90` | 11 | R_REPEATER | 78.6% | 54.5% | 54.5% | 36.4% | +15.0 | 6.95 | 5.79 | +26.3 | +7.7 |
| `asian_range_gte_30` | 10 | R_REPEATER | 71.4% | 50.0% | 50.0% | 30.0% | +10.8 | 3.96 | 3.96 | +23.2 | +8.4 |
| `confluence_gte_60` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 14.3% | +1.1 | 1.19 | 7.14 | +11.0 | +9.5 |
| `confluence_gte_70` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 25.0% | +7.9 | 2.94 | 8.83 | +16.5 | +8.9 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 71.4% | 40.0% | 40.0% | 20.0% | +7.5 | 3.35 | 5.02 | +19.9 | +7.4 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 71.4% | 30.0% | 30.0% | 20.0% | +6.1 | 2.38 | 5.56 | +18.0 | +8.5 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 42.9% | 66.7% | 66.7% | 33.3% | +12.7 | 4.69 | 2.35 | +27.9 | +8.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 35.7% | 60.0% | 60.0% | 20.0% | +7.6 | 2.84 | 1.90 | +23.2 | +8.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | R_REPEATER | 78.6% | 54.5% | 54.5% | 36.4% | +15.0 | 6.95 | 5.79 | +26.3 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 28.6% | +10.6 | 4.32 | 5.77 | +22.0 | +7.8 |
| `feature_momentum_breakout_exception` | 6 | R_REPEATER | 42.9% | 50.0% | 50.0% | 50.0% | +14.6 | 3.87 | 3.87 | +27.7 | +8.4 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 25.0% | +0.2 | 1.02 | 3.07 | +16.0 | +9.6 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+8.3; validation N=4 Fav=75.0% Avg=+43.3; out_of_sample N=1 Fav=0.0% Avg=-37.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 7.1% | +10.1 | 2.03 | 2.37 | +28.5 | +18.3 |
| `hunt_to_ar_ratio_le_2_0` | 8 | R_REPEATER | 57.1% | 62.5% | 62.5% | 12.5% | +20.1 | 3.28 | 1.31 | +37.6 | +19.3 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 71.4% | 50.0% | 50.0% | 10.0% | +10.9 | 1.90 | 1.52 | +30.6 | +21.9 |
| `stop_hunt_le_90` | 8 | R_REPEATER | 57.1% | 62.5% | 62.5% | 12.5% | +20.1 | 3.28 | 1.31 | +37.6 | +19.3 |
| `asian_range_gte_30` | 13 | S_STRANGER | 92.9% | 46.2% | 46.2% | 7.7% | +11.6 | 2.17 | 2.17 | +29.7 | +18.5 |
| `confluence_gte_60` | 9 | S_STRANGER | 64.3% | 44.4% | 44.4% | 0.0% | +9.4 | 1.70 | 1.70 | +28.9 | +22.2 |
| `confluence_gte_70` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -25.8 | 0.00 | 0.00 | +5.8 | +32.6 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 28.6% | 50.0% | 50.0% | 0.0% | +28.3 | 13.58 | 6.79 | +41.0 | +9.0 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 85.7% | 50.0% | 50.0% | 8.3% | +16.1 | 3.23 | 2.70 | +32.8 | +15.9 |
| `ratio_le_2_and_asian_gte_30` | 8 | R_REPEATER | 57.1% | 62.5% | 62.5% | 12.5% | +20.1 | 3.28 | 1.31 | +37.6 | +19.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | R_REPEATER | 21.4% | 66.7% | 66.7% | 0.0% | +40.7 | 999.00 | 999.00 | +50.5 | +6.9 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -9.0 | 0.00 | 0.00 | +12.6 | +15.1 |
| `feature_extreme_hunt_with_exception` | 8 | R_REPEATER | 57.1% | 62.5% | 62.5% | 12.5% | +20.1 | 3.28 | 1.31 | +37.6 | +19.3 |
| `feature_stale_hod_exhaustion_reject` | 11 | R_REPEATER | 78.6% | 54.5% | 54.5% | 9.1% | +13.5 | 2.14 | 1.78 | +32.0 | +21.0 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -24.8 | 0.00 | 0.00 | +6.6 | +34.7 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 0.0% | +0.5 | 1.06 | 4.25 | +19.7 | +15.9 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=50.0% Avg=+3.7; validation N=11 Fav=36.4% Avg=+7.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 42.9% | 42.9% | 38.1% | +5.8 | 2.82 | 3.77 | +17.5 | +9.0 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 66.7% | 28.6% | 28.6% | 21.4% | +4.3 | 1.97 | 4.91 | +17.4 | +11.8 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 76.2% | 31.2% | 31.2% | 25.0% | +4.1 | 2.02 | 4.45 | +16.9 | +10.9 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 71.4% | 26.7% | 26.7% | 20.0% | +3.8 | 1.90 | 5.24 | +17.1 | +11.3 |
| `asian_range_gte_30` | 18 | S_STRANGER | 85.7% | 38.9% | 38.9% | 33.3% | +5.0 | 2.91 | 4.58 | +16.0 | +8.5 |
| `confluence_gte_60` | 21 | S_STRANGER | 100.0% | 42.9% | 42.9% | 38.1% | +5.8 | 2.82 | 3.77 | +17.5 | +9.0 |
| `confluence_gte_70` | 21 | S_STRANGER | 100.0% | 42.9% | 42.9% | 38.1% | +5.8 | 2.82 | 3.77 | +17.5 | +9.0 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 23.8% | 20.0% | 20.0% | 20.0% | +3.5 | 2.01 | 8.02 | +15.4 | +10.2 |
| `tdi_rsi_gte_50` | 21 | S_STRANGER | 100.0% | 42.9% | 42.9% | 38.1% | +5.8 | 2.82 | 3.77 | +17.5 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 57.1% | 25.0% | 25.0% | 16.7% | +3.6 | 2.02 | 6.07 | +15.8 | +10.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +8.4 | +13.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 76.2% | 31.2% | 31.2% | 25.0% | +4.5 | 2.14 | 4.70 | +17.7 | +10.7 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 42.9% | 42.9% | 38.1% | +5.8 | 2.82 | 3.77 | +17.5 | +9.0 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 4.8% | 100.0% | 100.0% | 100.0% | +7.5 | 999.00 | 999.00 | +14.3 | +3.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 4.8% | 100.0% | 100.0% | 100.0% | +7.5 | 999.00 | 999.00 | +14.3 | +3.6 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=37.5% Avg=+3.7; out_of_sample N=17 Fav=47.1% Avg=+3.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +1.1 | 1.22 | 1.42 | +17.4 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 78.6% | 40.9% | 40.9% | 18.2% | +1.8 | 1.46 | 1.95 | +16.4 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 89.3% | 44.0% | 44.0% | 20.0% | +3.4 | 1.99 | 2.17 | +17.9 | +6.6 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +1.1 | 1.22 | 1.42 | +17.4 | +8.2 |
| `asian_range_gte_30` | 22 | S_STRANGER | 78.6% | 36.4% | 36.4% | 18.2% | +1.6 | 1.42 | 2.12 | +16.7 | +7.2 |
| `confluence_gte_60` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +1.1 | 1.22 | 1.42 | +17.4 | +8.2 |
| `confluence_gte_70` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +1.1 | 1.22 | 1.42 | +17.4 | +8.2 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 7.1% | 0.0% | 0.0% | 50.0% | -0.2 | 0.00 | 0.00 | +13.5 | +5.2 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 67.9% | 36.8% | 36.8% | 5.3% | +0.6 | 1.10 | 1.73 | +17.7 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 67.9% | 31.6% | 31.6% | 15.8% | -0.5 | 0.89 | 1.78 | +14.9 | +7.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 3.6% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +9.4 | +3.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +1.1 | 1.22 | 1.42 | +17.4 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | +1.1 | 1.22 | 1.42 | +17.4 | +8.2 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 3.6% | 100.0% | 100.0% | 0.0% | +9.0 | 999.00 | 999.00 | +16.1 | +3.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 3.6% | 100.0% | 100.0% | 0.0% | +9.0 | 999.00 | 999.00 | +16.1 | +3.6 |

### THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=100.0% Avg=+33.6; validation N=4 Fav=25.0% Avg=+1.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 0.0% | +9.0 | 3.99 | 5.58 | +19.5 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | R_REPEATER | 66.7% | 62.5% | 62.5% | 0.0% | +17.5 | 37.00 | 22.20 | +26.9 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 0.0% | +9.0 | 3.99 | 5.58 | +19.5 | +7.0 |
| `stop_hunt_le_90` | 8 | R_REPEATER | 66.7% | 62.5% | 62.5% | 0.0% | +17.5 | 37.00 | 22.20 | +26.9 | +4.8 |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 0.0% | +9.0 | 3.99 | 5.58 | +19.5 | +7.0 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 0.0% | +9.0 | 3.99 | 5.58 | +19.5 | +7.0 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 0.0% | +9.0 | 3.99 | 5.58 | +19.5 | +7.0 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 0.0% | +14.5 | 15.50 | 15.50 | +18.8 | +5.6 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 0.0% | +9.0 | 3.99 | 5.58 | +19.5 | +7.0 |
| `ratio_le_2_and_asian_gte_30` | 8 | R_REPEATER | 66.7% | 62.5% | 62.5% | 0.0% | +17.5 | 37.00 | 22.20 | +26.9 | +4.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 0.0% | +31.0 | 999.00 | 999.00 | +35.0 | +2.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | R_REPEATER | 66.7% | 62.5% | 62.5% | 0.0% | +17.5 | 37.00 | 22.20 | +26.9 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 83.3% | 40.0% | 40.0% | 0.0% | +8.1 | 3.26 | 4.89 | +17.9 | +7.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -1.0 | 0.00 | 0.00 | +13.4 | +7.5 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 0.0% | +6.0 | 3.13 | 7.82 | +16.9 | +7.9 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=50.0% Avg=+10.6; validation N=5 Fav=60.0% Avg=+10.7; out_of_sample N=4 Fav=75.0% Avg=+13.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 41.7% | 45.8% | 25.0% | +3.8 | 1.86 | 1.86 | +15.0 | +10.6 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 79.2% | 47.4% | 52.6% | 26.3% | +6.6 | 3.16 | 2.53 | +16.3 | +7.9 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 87.5% | 47.6% | 52.4% | 23.8% | +5.9 | 2.68 | 2.19 | +15.8 | +8.4 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 91.7% | 45.5% | 50.0% | 22.7% | +4.7 | 2.08 | 1.89 | +15.1 | +10.3 |
| `asian_range_gte_30` | 19 | S_STRANGER | 79.2% | 47.4% | 52.6% | 26.3% | +6.3 | 2.87 | 2.01 | +17.2 | +8.8 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 41.7% | 45.8% | 25.0% | +3.8 | 1.86 | 1.86 | +15.0 | +10.6 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 41.7% | 45.8% | 25.0% | +3.8 | 1.86 | 1.86 | +15.0 | +10.6 |
| `tdi_rsi_gt_signal` | 18 | R_REPEATER | 75.0% | 50.0% | 50.0% | 22.2% | +5.7 | 2.33 | 2.07 | +16.3 | +11.7 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 58.3% | 42.9% | 42.9% | 14.3% | +3.0 | 1.54 | 2.05 | +13.5 | +12.6 |
| `ratio_le_2_and_asian_gte_30` | 16 | R_REPEATER | 66.7% | 50.0% | 56.2% | 25.0% | +7.6 | 3.50 | 2.33 | +17.7 | +8.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | R_REPEATER | 45.8% | 63.6% | 63.6% | 18.2% | +11.7 | 6.82 | 3.90 | +19.6 | +8.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 91.7% | 45.5% | 50.0% | 22.7% | +4.7 | 2.08 | 1.89 | +15.1 | +10.3 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 41.7% | 45.8% | 25.0% | +3.8 | 1.86 | 1.86 | +15.0 | +10.6 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 12.5% | 33.3% | 33.3% | 33.3% | +3.0 | 2.38 | 2.38 | +16.1 | +5.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 8.3% | 50.0% | 50.0% | 0.0% | +4.5 | 2.38 | 2.38 | +16.3 | +4.6 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=62.5% Avg=+5.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 53.8% | 0.0% | +3.7 | 2.29 | 1.96 | +10.9 | +6.9 |
| `hunt_to_ar_ratio_le_2_0` | 3 | R_RUNNER | 23.1% | 100.0% | 100.0% | 0.0% | +12.1 | 999.00 | 999.00 | +22.5 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 4 | R_RUNNER | 30.8% | 100.0% | 100.0% | 0.0% | +16.0 | 999.00 | 999.00 | +24.2 | +4.0 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 38.5% | 53.8% | 0.0% | +3.7 | 2.29 | 1.96 | +10.9 | +6.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 38.5% | 53.8% | 0.0% | +3.7 | 2.29 | 1.96 | +10.9 | +6.9 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 38.5% | 53.8% | 0.0% | +3.7 | 2.29 | 1.96 | +10.9 | +6.9 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 38.5% | 20.0% | 40.0% | 0.0% | -3.0 | 0.50 | 0.75 | +6.6 | +8.0 |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 61.5% | 62.5% | 62.5% | 0.0% | +5.4 | 2.44 | 1.46 | +15.4 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 38.5% | 53.8% | 0.0% | +3.7 | 2.29 | 1.96 | +10.9 | +6.9 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 92.3% | 33.3% | 50.0% | 0.0% | +3.1 | 1.99 | 1.99 | +9.9 | +7.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 0.0% | +11.0 | 999.00 | 999.00 | +23.7 | +5.5 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+93.4; validation N=2 Fav=0.0% Avg=-3.6; out_of_sample N=3 Fav=66.7% Avg=+21.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 12.5% | +9.6 | 3.12 | 5.20 | +26.7 | +9.5 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 56.2% | 33.3% | 33.3% | 11.1% | +13.5 | 4.33 | 8.65 | +32.3 | +9.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 81.2% | 23.1% | 23.1% | 7.7% | +6.5 | 2.17 | 7.22 | +25.1 | +11.2 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 75.0% | 25.0% | 25.0% | 8.3% | +8.9 | 3.08 | 9.25 | +27.1 | +9.3 |
| `asian_range_gte_30` | 15 | S_STRANGER | 93.8% | 33.3% | 33.3% | 6.7% | +9.9 | 3.04 | 6.07 | +26.9 | +10.0 |
| `confluence_gte_60` | 12 | S_STRANGER | 75.0% | 41.7% | 41.7% | 16.7% | +13.1 | 4.18 | 5.85 | +29.3 | +8.7 |
| `confluence_gte_70` | 6 | R_REPEATER | 37.5% | 50.0% | 50.0% | 16.7% | +24.9 | 20.92 | 20.92 | +35.0 | +4.6 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 0.0% | +2.6 | 1.43 | 5.72 | +22.6 | +11.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 43.8% | 28.6% | 28.6% | 14.3% | +14.6 | 3.91 | 9.79 | +31.3 | +9.5 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 56.2% | 33.3% | 33.3% | 11.1% | +13.5 | 4.33 | 8.65 | +32.3 | +9.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 0.0% | +2.6 | 1.43 | 5.72 | +22.6 | +11.0 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +25.5 | +6.1 |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 68.8% | 27.3% | 27.3% | 9.1% | +9.9 | 3.26 | 8.68 | +28.0 | +9.9 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 12.5% | +9.6 | 3.12 | 5.20 | +26.7 | +9.5 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 0.0% | +5.8 | 7.70 | 30.79 | +21.0 | +5.6 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -0.7 | 0.00 | 0.00 | +17.2 | +6.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=80.0% Avg=+28.6; validation N=4 Fav=0.0% Avg=-5.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 36.8% | 36.8% | 26.3% | +7.7 | 3.36 | 5.28 | +18.6 | +9.6 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 89.5% | 29.4% | 29.4% | 23.5% | +6.2 | 2.70 | 5.93 | +16.7 | +10.3 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 36.8% | 36.8% | 26.3% | +7.7 | 3.36 | 5.28 | +18.6 | +9.6 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 36.8% | 36.8% | 26.3% | +7.7 | 3.36 | 5.28 | +18.6 | +9.6 |
| `asian_range_gte_30` | 17 | S_STRANGER | 89.5% | 29.4% | 29.4% | 23.5% | +6.2 | 2.70 | 5.93 | +16.7 | +10.3 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 36.8% | 36.8% | 26.3% | +7.7 | 3.36 | 5.28 | +18.6 | +9.6 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 36.8% | 36.8% | 26.3% | +7.7 | 3.36 | 5.28 | +18.6 | +9.6 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 47.4% | 44.4% | 44.4% | 44.4% | +13.3 | 5.98 | 5.98 | +24.7 | +8.5 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 84.2% | 37.5% | 37.5% | 25.0% | +8.7 | 4.40 | 6.60 | +19.2 | +8.6 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 89.5% | 29.4% | 29.4% | 23.5% | +6.2 | 2.70 | 5.93 | +16.7 | +10.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 47.4% | 44.4% | 44.4% | 44.4% | +13.3 | 5.98 | 5.98 | +24.7 | +8.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 36.8% | 36.8% | 26.3% | +7.7 | 3.36 | 5.28 | +18.6 | +9.6 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 36.8% | 36.8% | 26.3% | +7.7 | 3.36 | 5.28 | +18.6 | +9.6 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +12.5 | +6.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +12.5 | +6.3 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=25.0% Avg=+1.7; validation N=1 Fav=100.0% Avg=+28.4; out_of_sample N=1 Fav=100.0% Avg=+38.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 54.5% | +6.6 | 4.11 | 5.14 | +18.1 | +7.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 50.0% | +6.3 | 3.69 | 6.15 | +18.0 | +8.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 50.0% | +6.3 | 3.69 | 6.15 | +18.0 | +8.1 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 50.0% | +6.3 | 3.69 | 6.15 | +18.0 | +8.1 |
| `asian_range_gte_30` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 50.0% | +5.8 | 3.31 | 6.62 | +19.6 | +8.2 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 54.5% | +6.6 | 4.11 | 5.14 | +18.1 | +7.6 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 54.5% | +6.6 | 4.11 | 5.14 | +18.1 | +7.6 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 75.0% | +6.5 | 9.16 | 4.58 | +13.4 | +5.5 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 90.9% | 40.0% | 40.0% | 60.0% | +8.1 | 6.21 | 6.21 | +19.2 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 50.0% | +5.8 | 3.31 | 6.62 | +19.6 | +8.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +11.7 | +3.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 54.5% | +6.6 | 4.11 | 5.14 | +18.1 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 50.0% | +3.4 | 2.47 | 4.11 | +15.7 | +7.5 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 66.7% | +10.6 | 5.75 | 5.75 | +22.0 | +8.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 66.7% | +10.6 | 5.75 | 5.75 | +22.0 | +8.2 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=57.1% Avg=+7.7; validation N=8 Fav=37.5% Avg=+6.9; out_of_sample N=1 Fav=0.0% Avg=-10.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 40.9% | +4.7 | 1.81 | 2.72 | +18.7 | +10.2 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 86.4% | 42.1% | 42.1% | 47.4% | +6.6 | 2.19 | 2.46 | +20.7 | +9.8 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 95.5% | 38.1% | 38.1% | 42.9% | +5.1 | 1.86 | 2.56 | +19.4 | +10.2 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 90.9% | 40.0% | 40.0% | 45.0% | +5.6 | 1.95 | 2.43 | +19.7 | +10.5 |
| `asian_range_gte_30` | 19 | S_STRANGER | 86.4% | 36.8% | 36.8% | 42.1% | +4.1 | 1.64 | 2.35 | +19.0 | +10.7 |
| `confluence_gte_60` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 40.9% | +4.7 | 1.81 | 2.72 | +18.7 | +10.2 |
| `confluence_gte_70` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 40.9% | +4.7 | 1.81 | 2.72 | +18.7 | +10.2 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 90.9% | 35.0% | 35.0% | 40.0% | +5.3 | 2.17 | 3.40 | +18.6 | +9.1 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 81.8% | 27.8% | 27.8% | 33.3% | +1.8 | 1.27 | 2.80 | +16.5 | +11.3 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 72.7% | 43.8% | 43.8% | 50.0% | +6.2 | 2.01 | 2.01 | +21.4 | +10.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 63.6% | 42.9% | 42.9% | 50.0% | +7.2 | 2.66 | 2.66 | +21.7 | +8.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 86.4% | 42.1% | 42.1% | 47.4% | +6.6 | 2.19 | 2.46 | +20.7 | +9.8 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 95.5% | 38.1% | 38.1% | 42.9% | +5.2 | 1.89 | 2.60 | +19.3 | +10.3 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -9.2 | 0.00 | 0.00 | +3.4 | +15.6 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -9.2 | 0.00 | 0.00 | +3.4 | +15.6 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=9 Fav=44.4% Avg=+3.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +2.6 | 2.66 | 4.66 | +9.0 | +3.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 40.0% | 40.0% | 10.0% | +3.0 | 2.88 | 4.32 | +8.9 | +3.5 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +2.6 | 2.66 | 4.66 | +9.0 | +3.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +2.6 | 2.66 | 4.66 | +9.0 | +3.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 81.8% | 44.4% | 44.4% | 11.1% | +3.6 | 3.29 | 4.11 | +10.3 | +3.5 |
| `confluence_gte_70` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +7.0 | +7.6 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | +1.9 | 4.70 | 14.10 | +8.6 | +3.3 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 14.3% | +5.2 | 14.54 | 19.38 | +10.8 | +2.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +2.6 | 2.66 | 4.66 | +9.0 | +3.6 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +2.6 | 2.66 | 4.66 | +9.0 | +3.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=75.0% Avg=+4.4; validation N=2 Fav=50.0% Avg=+4.6; out_of_sample N=1 Fav=0.0% Avg=-1.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +0.1 | 1.02 | 1.54 | +11.9 | +8.6 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 33.3% | -1.4 | 0.72 | 1.08 | +12.4 | +10.3 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 81.8% | 44.4% | 44.4% | 22.2% | +1.3 | 1.27 | 1.27 | +13.4 | +8.8 |
| `stop_hunt_le_90` | 9 | S_STRANGER | 81.8% | 44.4% | 44.4% | 22.2% | +2.7 | 1.80 | 1.80 | +13.4 | +8.3 |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +0.1 | 1.02 | 1.54 | +11.9 | +8.6 |
| `confluence_gte_60` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 0.0% | -0.1 | 0.99 | 0.99 | +11.3 | +11.7 |
| `confluence_gte_70` | 2 | R_RUNNER | 18.2% | 100.0% | 100.0% | 0.0% | +16.9 | 999.00 | 999.00 | +20.5 | +3.3 |
| `tdi_rsi_gt_signal` | 7 | R_REPEATER | 63.6% | 57.1% | 57.1% | 14.3% | +3.6 | 1.84 | 1.38 | +15.5 | +9.6 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 0.0% | +1.1 | 1.18 | 1.18 | +12.1 | +10.2 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 33.3% | -1.4 | 0.72 | 1.08 | +12.4 | +10.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 20.0% | -1.7 | 0.72 | 1.08 | +13.6 | +12.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 25.0% | +0.6 | 1.14 | 1.52 | +12.2 | +8.7 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +0.1 | 1.02 | 1.54 | +11.9 | +8.6 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 0.0% | +20.3 | 999.00 | 999.00 | +22.9 | +5.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 0.0% | +20.3 | 999.00 | 999.00 | +22.9 | +5.1 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=66.7% Avg=+13.3; validation N=7 Fav=28.6% Avg=+6.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 34 | S_STRANGER | 100.0% | 35.3% | 38.2% | 38.2% | +5.4 | 2.59 | 3.39 | +17.2 | +9.5 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 91.2% | 35.5% | 38.7% | 32.3% | +5.2 | 2.41 | 3.41 | +17.2 | +9.8 |
| `hunt_to_ar_ratio_le_2_5` | 33 | S_STRANGER | 97.1% | 33.3% | 36.4% | 36.4% | +4.9 | 2.41 | 3.41 | +16.9 | +9.5 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 94.1% | 37.5% | 40.6% | 34.4% | +5.7 | 2.59 | 3.39 | +17.3 | +9.2 |
| `asian_range_gte_30` | 24 | S_STRANGER | 70.6% | 37.5% | 41.7% | 37.5% | +6.7 | 2.92 | 3.22 | +19.1 | +9.3 |
| `confluence_gte_60` | 34 | S_STRANGER | 100.0% | 35.3% | 38.2% | 38.2% | +5.4 | 2.59 | 3.39 | +17.2 | +9.5 |
| `confluence_gte_70` | 34 | S_STRANGER | 100.0% | 35.3% | 38.2% | 38.2% | +5.4 | 2.59 | 3.39 | +17.2 | +9.5 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 41.2% | 28.6% | 28.6% | 14.3% | +4.2 | 1.75 | 4.38 | +16.8 | +12.3 |
| `tdi_rsi_gte_50` | 22 | S_STRANGER | 64.7% | 31.8% | 31.8% | 27.3% | +4.0 | 2.00 | 3.71 | +18.2 | +11.1 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 67.6% | 39.1% | 43.5% | 34.8% | +7.0 | 2.92 | 3.22 | +19.4 | +9.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 29.4% | 40.0% | 40.0% | 20.0% | +8.8 | 2.84 | 4.26 | +20.2 | +11.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 91.2% | 35.5% | 38.7% | 32.3% | +5.2 | 2.41 | 3.41 | +17.0 | +9.3 |
| `feature_stale_hod_exhaustion_reject` | 34 | S_STRANGER | 100.0% | 35.3% | 38.2% | 38.2% | +5.4 | 2.59 | 3.39 | +17.2 | +9.5 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 5.9% | 50.0% | 50.0% | 100.0% | +10.4 | 999.00 | 999.00 | +17.1 | +4.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=75.0% Avg=+10.0; validation N=1 Fav=0.0% Avg=-10.3; out_of_sample N=2 Fav=0.0% Avg=-8.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -0.5 | 0.90 | 1.81 | +11.4 | +9.2 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -0.5 | 0.90 | 1.81 | +11.4 | +9.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -0.5 | 0.90 | 1.81 | +11.4 | +9.2 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -0.5 | 0.90 | 1.81 | +11.4 | +9.2 |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -0.5 | 0.90 | 1.81 | +11.4 | +9.2 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -0.5 | 0.90 | 1.81 | +11.4 | +9.2 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -0.5 | 0.90 | 1.81 | +11.4 | +9.2 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +5.7 | +6.0 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -0.5 | 0.90 | 1.81 | +11.4 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -0.5 | 0.90 | 1.81 | +11.4 | +9.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +5.7 | +6.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -0.5 | 0.90 | 1.81 | +11.4 | +9.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 83.3% | 30.0% | 30.0% | 0.0% | -0.6 | 0.89 | 2.07 | +11.4 | +9.0 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 33.3% | 50.0% | 50.0% | 0.0% | +3.9 | 1.93 | 1.93 | +11.6 | +6.3 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 0.0% | +1.9 | 1.45 | 1.94 | +11.5 | +7.6 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=25.0% Avg=-11.9; validation N=3 Fav=33.3% Avg=+1.1; out_of_sample N=2 Fav=100.0% Avg=+5.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 0.0% | -6.0 | 0.42 | 0.58 | +15.4 | +13.9 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 58.3% | 28.6% | 42.9% | 0.0% | -13.2 | 0.18 | 0.24 | +17.5 | +17.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 0.0% | -6.0 | 0.42 | 0.58 | +15.4 | +13.9 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 91.7% | 36.4% | 45.5% | 0.0% | -6.0 | 0.44 | 0.53 | +16.1 | +13.2 |
| `asian_range_gte_30` | 11 | S_STRANGER | 91.7% | 36.4% | 45.5% | 0.0% | -6.4 | 0.42 | 0.51 | +15.7 | +14.8 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 0.0% | -6.0 | 0.42 | 0.58 | +15.4 | +13.9 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 0.0% | -6.0 | 0.42 | 0.58 | +15.4 | +13.9 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 0.0% | -3.8 | 0.55 | 0.68 | +17.5 | +17.7 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 0.0% | -3.8 | 0.55 | 0.68 | +17.5 | +17.7 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 58.3% | 28.6% | 42.9% | 0.0% | -13.2 | 0.18 | 0.24 | +17.5 | +17.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 33.3% | 50.0% | 50.0% | 0.0% | -13.7 | 0.15 | 0.15 | +23.8 | +29.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 83.3% | 30.0% | 40.0% | 0.0% | -7.9 | 0.33 | 0.49 | +16.2 | +14.1 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 0.0% | -6.0 | 0.42 | 0.58 | +15.4 | +13.9 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -28.4 | 0.00 | 0.00 | +8.8 | +1.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 0.0% | +5.3 | 3.48 | 1.74 | +21.0 | +10.1 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=66.7% Avg=+14.8; validation N=4 Fav=75.0% Avg=+11.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 32.0% | 32.0% | 28.0% | +0.8 | 1.11 | 2.22 | +16.4 | +10.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 56.0% | 21.4% | 21.4% | 14.3% | -3.8 | 0.61 | 2.05 | +15.6 | +11.3 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 96.0% | 33.3% | 33.3% | 29.2% | +1.1 | 1.15 | 2.16 | +17.0 | +10.2 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 80.0% | 35.0% | 35.0% | 30.0% | -0.1 | 0.98 | 1.68 | +17.1 | +10.6 |
| `asian_range_gte_30` | 22 | S_STRANGER | 88.0% | 36.4% | 36.4% | 27.3% | +2.0 | 1.28 | 2.24 | +17.5 | +9.9 |
| `confluence_gte_60` | 8 | R_REPEATER | 32.0% | 50.0% | 50.0% | 50.0% | +6.3 | 2.47 | 1.86 | +23.1 | +9.9 |
| `confluence_gte_70` | 2 | R_REPEATER | 8.0% | 50.0% | 50.0% | 100.0% | +3.5 | 999.00 | 999.00 | +21.8 | +11.1 |
| `tdi_rsi_gt_signal` | 10 | R_REPEATER | 40.0% | 70.0% | 70.0% | 60.0% | +13.7 | 8.12 | 3.48 | +27.8 | +7.9 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 56.0% | 42.9% | 42.9% | 28.6% | +6.9 | 2.69 | 3.59 | +19.1 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 48.0% | 25.0% | 25.0% | 8.3% | -3.0 | 0.70 | 2.10 | +16.2 | +10.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 16.0% | 50.0% | 50.0% | 25.0% | +6.7 | 2.41 | 2.41 | +25.0 | +9.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 80.0% | 35.0% | 35.0% | 30.0% | -0.1 | 0.98 | 1.68 | +17.1 | +10.6 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 96.0% | 33.3% | 33.3% | 29.2% | +1.1 | 1.15 | 2.16 | +17.0 | +10.9 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 24.0% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +2.6 | +10.8 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 16.0% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +2.6 | +8.8 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=20.0% Avg=-0.7; out_of_sample N=6 Fav=50.0% Avg=+10.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 31.6% | 31.6% | 10.5% | +3.0 | 1.59 | 3.18 | +15.0 | +12.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 68.4% | 15.4% | 15.4% | 7.7% | -1.8 | 0.73 | 3.64 | +11.1 | +14.8 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 89.5% | 29.4% | 29.4% | 11.8% | +2.4 | 1.48 | 3.25 | +14.5 | +12.7 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 89.5% | 29.4% | 29.4% | 11.8% | +2.4 | 1.48 | 3.25 | +14.5 | +12.7 |
| `asian_range_gte_30` | 18 | S_STRANGER | 94.7% | 27.8% | 27.8% | 5.6% | +2.3 | 1.42 | 3.41 | +14.4 | +12.6 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 31.6% | 31.6% | 10.5% | +3.0 | 1.59 | 3.18 | +15.0 | +12.1 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 31.6% | 31.6% | 10.5% | +3.0 | 1.59 | 3.18 | +15.0 | +12.1 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 52.6% | 30.0% | 30.0% | 20.0% | +3.8 | 2.13 | 4.27 | +13.8 | +9.6 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 57.9% | 36.4% | 36.4% | 9.1% | +5.1 | 2.17 | 3.80 | +17.5 | +11.6 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 68.4% | 15.4% | 15.4% | 7.7% | -1.8 | 0.73 | 3.64 | +11.1 | +14.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 31.6% | 16.7% | 16.7% | 16.7% | +1.1 | 1.33 | 5.30 | +11.3 | +10.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 89.5% | 29.4% | 29.4% | 11.8% | +2.4 | 1.48 | 3.25 | +14.5 | +12.7 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 31.6% | 31.6% | 10.5% | +3.0 | 1.59 | 3.18 | +15.0 | +12.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=0.0% Avg=-6.7; out_of_sample N=3 Fav=66.7% Avg=+21.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 38 | S_STRANGER | 100.0% | 31.6% | 31.6% | 36.8% | -5.2 | 0.58 | 1.06 | +16.2 | +8.7 |
| `hunt_to_ar_ratio_le_2_0` | 29 | S_STRANGER | 76.3% | 34.5% | 34.5% | 44.8% | -2.7 | 0.74 | 1.11 | +17.4 | +7.8 |
| `hunt_to_ar_ratio_le_2_5` | 36 | S_STRANGER | 94.7% | 33.3% | 33.3% | 38.9% | -4.8 | 0.61 | 1.02 | +16.9 | +8.4 |
| `stop_hunt_le_90` | 33 | S_STRANGER | 86.8% | 30.3% | 30.3% | 39.4% | -5.4 | 0.55 | 1.04 | +15.9 | +9.0 |
| `asian_range_gte_30` | 36 | S_STRANGER | 94.7% | 30.6% | 30.6% | 36.1% | -6.2 | 0.51 | 0.97 | +15.2 | +8.6 |
| `confluence_gte_60` | 34 | S_STRANGER | 89.5% | 29.4% | 29.4% | 35.3% | -5.7 | 0.56 | 1.13 | +16.4 | +8.3 |
| `confluence_gte_70` | 12 | S_STRANGER | 31.6% | 25.0% | 25.0% | 41.7% | +2.4 | 1.62 | 3.23 | +19.1 | +10.6 |
| `tdi_rsi_gt_signal` | 27 | S_STRANGER | 71.1% | 29.6% | 29.6% | 33.3% | -1.6 | 0.83 | 1.66 | +17.2 | +9.7 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 21.1% | 25.0% | 25.0% | 25.0% | +3.9 | 1.82 | 3.64 | +19.5 | +9.8 |
| `ratio_le_2_and_asian_gte_30` | 28 | S_STRANGER | 73.7% | 32.1% | 32.1% | 42.9% | -4.3 | 0.59 | 0.99 | +15.7 | +8.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 18 | S_STRANGER | 47.4% | 27.8% | 27.8% | 38.9% | -0.5 | 0.93 | 1.86 | +16.3 | +8.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 33 | S_STRANGER | 86.8% | 30.3% | 30.3% | 39.4% | -5.4 | 0.55 | 1.04 | +15.9 | +9.0 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 100.0% | 31.6% | 31.6% | 36.8% | -5.2 | 0.58 | 1.06 | +16.2 | +8.7 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 5.3% | 50.0% | 50.0% | 100.0% | +12.4 | 999.00 | 999.00 | +24.3 | +10.7 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=44.4% Avg=+10.0; validation N=9 Fav=0.0% Avg=-5.1; out_of_sample N=3 Fav=100.0% Avg=+34.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 30.4% | 34.8% | 47.8% | +6.3 | 3.35 | 4.19 | +19.3 | +5.8 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 87.0% | 30.0% | 35.0% | 45.0% | +4.9 | 2.60 | 3.34 | +16.7 | +6.0 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 91.3% | 33.3% | 38.1% | 47.6% | +7.0 | 3.40 | 3.82 | +18.7 | +6.0 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 91.3% | 28.6% | 33.3% | 47.6% | +4.6 | 2.60 | 3.34 | +17.0 | +5.9 |
| `asian_range_gte_30` | 19 | S_STRANGER | 82.6% | 26.3% | 31.6% | 47.4% | +5.7 | 2.78 | 4.17 | +18.1 | +6.2 |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 30.4% | 34.8% | 47.8% | +6.3 | 3.35 | 4.19 | +19.3 | +5.8 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 30.4% | 34.8% | 47.8% | +6.3 | 3.35 | 4.19 | +19.3 | +5.8 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 82.6% | 26.3% | 31.6% | 47.4% | +6.7 | 4.44 | 5.92 | +19.8 | +5.7 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 47.8% | 18.2% | 18.2% | 45.5% | +5.4 | 4.01 | 12.02 | +18.2 | +5.7 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 78.3% | 22.2% | 27.8% | 44.4% | +3.3 | 1.98 | 3.56 | +15.9 | +6.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 65.2% | 20.0% | 26.7% | 46.7% | +4.5 | 2.86 | 5.01 | +16.4 | +5.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 91.3% | 28.6% | 33.3% | 42.9% | +4.6 | 2.56 | 3.65 | +17.3 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 30.4% | 34.8% | 47.8% | +6.3 | 3.35 | 4.19 | +19.3 | +5.8 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 13.0% | 33.3% | 33.3% | 100.0% | +12.0 | 999.00 | 999.00 | +27.1 | +3.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +13.4 | +5.4 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=50.0% Avg=-1.8; out_of_sample N=7 Fav=28.6% Avg=-0.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 29.4% | 35.3% | 17.6% | -1.8 | 0.77 | 1.28 | +11.9 | +14.9 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 76.5% | 30.8% | 30.8% | 23.1% | -3.9 | 0.59 | 1.18 | +11.1 | +17.6 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 94.1% | 31.2% | 37.5% | 18.8% | -1.8 | 0.78 | 1.16 | +11.9 | +15.4 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 94.1% | 31.2% | 37.5% | 18.8% | -1.8 | 0.78 | 1.16 | +11.9 | +15.4 |
| `asian_range_gte_30` | 14 | S_STRANGER | 82.4% | 35.7% | 35.7% | 21.4% | -2.0 | 0.78 | 1.25 | +13.4 | +16.2 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 29.4% | 35.3% | 17.6% | -1.8 | 0.77 | 1.28 | +11.9 | +14.9 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 29.4% | 35.3% | 17.6% | -1.8 | 0.77 | 1.28 | +11.9 | +14.9 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 23.5% | 25.0% | 25.0% | 0.0% | -14.9 | 0.24 | 0.73 | +9.4 | +30.6 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 76.5% | 38.5% | 46.2% | 15.4% | -1.1 | 0.88 | 1.03 | +13.6 | +16.1 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 70.6% | 33.3% | 33.3% | 25.0% | -4.1 | 0.60 | 1.05 | +12.0 | +17.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 17.6% | 33.3% | 33.3% | 0.0% | -19.5 | 0.25 | 0.49 | +8.1 | +38.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 94.1% | 31.2% | 37.5% | 18.8% | -1.8 | 0.78 | 1.16 | +11.9 | +15.4 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 29.4% | 35.3% | 17.6% | -1.8 | 0.77 | 1.28 | +11.9 | +14.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+4.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 41 | S_STRANGER | 100.0% | 29.3% | 29.3% | 24.4% | +3.0 | 1.74 | 4.05 | +15.0 | +9.0 |
| `hunt_to_ar_ratio_le_2_0` | 34 | S_STRANGER | 82.9% | 29.4% | 29.4% | 26.5% | +2.7 | 1.61 | 3.71 | +15.2 | +9.2 |
| `hunt_to_ar_ratio_le_2_5` | 39 | S_STRANGER | 95.1% | 30.8% | 30.8% | 25.6% | +3.2 | 1.78 | 3.86 | +15.3 | +9.2 |
| `stop_hunt_le_90` | 36 | S_STRANGER | 87.8% | 33.3% | 33.3% | 27.8% | +4.6 | 2.32 | 4.45 | +16.1 | +8.6 |
| `asian_range_gte_30` | 35 | S_STRANGER | 85.4% | 28.6% | 28.6% | 25.7% | +2.8 | 1.62 | 3.88 | +15.2 | +9.5 |
| `confluence_gte_60` | 41 | S_STRANGER | 100.0% | 29.3% | 29.3% | 24.4% | +3.0 | 1.74 | 4.05 | +15.0 | +9.0 |
| `confluence_gte_70` | 41 | S_STRANGER | 100.0% | 29.3% | 29.3% | 24.4% | +3.0 | 1.74 | 4.05 | +15.0 | +9.0 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 4.9% | 50.0% | 50.0% | 50.0% | +3.8 | 3.48 | 3.48 | +16.2 | +3.1 |
| `tdi_rsi_gte_50` | 32 | S_STRANGER | 78.0% | 25.0% | 25.0% | 18.8% | +3.6 | 1.99 | 5.72 | +14.8 | +9.1 |
| `ratio_le_2_and_asian_gte_30` | 30 | S_STRANGER | 73.2% | 30.0% | 30.0% | 26.7% | +2.4 | 1.51 | 3.36 | +15.3 | +9.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 4.9% | 50.0% | 50.0% | 50.0% | +3.8 | 3.48 | 3.48 | +16.2 | +3.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 36 | S_STRANGER | 87.8% | 33.3% | 33.3% | 27.8% | +4.6 | 2.32 | 4.45 | +16.1 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 41 | S_STRANGER | 100.0% | 29.3% | 29.3% | 24.4% | +3.0 | 1.74 | 4.05 | +15.0 | +9.0 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 14.6% | 33.3% | 33.3% | 16.7% | -0.3 | 0.96 | 1.92 | +13.4 | +12.1 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 12.2% | 40.0% | 40.0% | 20.0% | +4.1 | 1.83 | 2.75 | +15.6 | +9.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=75.0% Avg=+12.0; validation N=10 Fav=30.0% Avg=+0.5; out_of_sample N=1 Fav=0.0% Avg=-4.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 29.2% | 29.2% | 20.8% | +1.3 | 1.30 | 2.98 | +15.3 | +10.5 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 83.3% | 35.0% | 35.0% | 20.0% | +2.0 | 1.41 | 2.62 | +15.4 | +11.4 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 91.7% | 31.8% | 31.8% | 18.2% | +1.6 | 1.34 | 2.87 | +14.8 | +10.8 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 95.8% | 30.4% | 30.4% | 21.7% | +1.5 | 1.34 | 2.87 | +15.1 | +10.5 |
| `asian_range_gte_30` | 17 | S_STRANGER | 70.8% | 35.3% | 35.3% | 23.5% | +2.6 | 1.50 | 2.75 | +17.3 | +11.5 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 29.2% | 29.2% | 20.8% | +1.3 | 1.30 | 2.98 | +15.3 | +10.5 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 29.2% | 29.2% | 20.8% | +1.3 | 1.30 | 2.98 | +15.3 | +10.5 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 37.5% | 11.1% | 11.1% | 0.0% | -4.5 | 0.12 | 1.00 | +11.8 | +10.9 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -3.6 | 0.24 | 1.41 | +9.9 | +10.6 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 62.5% | 40.0% | 40.0% | 26.7% | +3.2 | 1.59 | 2.38 | +17.9 | +11.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -9.5 | 0.00 | 0.00 | +15.6 | +13.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 95.8% | 30.4% | 30.4% | 21.7% | +1.5 | 1.34 | 2.87 | +15.1 | +10.5 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 29.2% | 29.2% | 20.8% | +1.3 | 1.30 | 2.98 | +15.3 | +10.5 |
| `feature_momentum_breakout_exception` | 3 | R_REPEATER | 12.5% | 66.7% | 66.7% | 66.7% | +14.0 | 9.95 | 4.97 | +19.4 | +2.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +6.0 | +6.2 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=1 Fav=100.0% Avg=+8.4; out_of_sample N=4 Fav=50.0% Avg=+7.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 27.8% | 33.3% | 33.3% | -5.7 | 0.49 | 0.90 | +14.7 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 88.9% | 31.2% | 31.2% | 31.2% | -1.1 | 0.85 | 1.69 | +15.8 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 27.8% | 33.3% | 33.3% | -5.7 | 0.49 | 0.90 | +14.7 | +6.3 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 88.9% | 31.2% | 31.2% | 31.2% | -1.1 | 0.85 | 1.69 | +15.8 | +6.1 |
| `asian_range_gte_30` | 14 | S_STRANGER | 77.8% | 21.4% | 28.6% | 35.7% | -10.1 | 0.28 | 0.64 | +11.0 | +7.0 |
| `confluence_gte_60` | 13 | S_STRANGER | 72.2% | 30.8% | 38.5% | 38.5% | -8.4 | 0.42 | 0.59 | +15.0 | +6.4 |
| `confluence_gte_70` | 5 | R_REPEATER | 27.8% | 60.0% | 80.0% | 80.0% | +7.5 | 2.65 | 0.66 | +26.2 | +2.9 |
| `tdi_rsi_gt_signal` | 6 | R_REPEATER | 33.3% | 50.0% | 50.0% | 66.7% | +3.3 | 1.50 | 1.00 | +22.6 | +8.6 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 44.4% | 25.0% | 25.0% | 37.5% | -2.4 | 0.64 | 1.60 | +18.8 | +8.9 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 66.7% | 25.0% | 25.0% | 33.3% | -4.7 | 0.49 | 1.30 | +11.9 | +6.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 27.8% | 40.0% | 40.0% | 60.0% | -1.1 | 0.86 | 0.86 | +16.8 | +9.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 88.9% | 31.2% | 31.2% | 31.2% | -1.1 | 0.85 | 1.69 | +15.8 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 27.8% | 33.3% | 33.3% | -5.7 | 0.49 | 0.90 | +14.7 | +6.3 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 11.1% | 50.0% | 50.0% | 0.0% | +7.8 | 7.46 | 7.46 | +20.0 | +2.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +18.6 | +3.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=44.4% Avg=+5.5; validation N=5 Fav=20.0% Avg=+2.2; out_of_sample N=1 Fav=0.0% Avg=-24.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -6.2 | 0.57 | 1.32 | +15.9 | +12.3 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 72.7% | 25.0% | 25.0% | 25.0% | -3.8 | 0.69 | 1.72 | +15.2 | +10.3 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 86.4% | 26.3% | 26.3% | 26.3% | -4.3 | 0.66 | 1.57 | +15.6 | +12.7 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 81.8% | 27.8% | 27.8% | 27.8% | -4.3 | 0.67 | 1.46 | +15.0 | +13.0 |
| `asian_range_gte_30` | 21 | S_STRANGER | 95.5% | 23.8% | 23.8% | 23.8% | -7.6 | 0.49 | 1.38 | +15.2 | +12.1 |
| `confluence_gte_60` | 12 | S_STRANGER | 54.5% | 41.7% | 41.7% | 25.0% | -3.4 | 0.79 | 1.11 | +20.2 | +12.8 |
| `confluence_gte_70` | 4 | R_REPEATER | 18.2% | 50.0% | 50.0% | 50.0% | +12.1 | 5.93 | 5.93 | +19.2 | +9.5 |
| `tdi_rsi_gt_signal` | 3 | R_RUNNER | 13.6% | 100.0% | 100.0% | 66.7% | +30.0 | 999.00 | 999.00 | +37.3 | +10.8 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 68.2% | 33.3% | 33.3% | 20.0% | +2.4 | 1.32 | 2.64 | +18.5 | +14.7 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 72.7% | 25.0% | 25.0% | 25.0% | -3.8 | 0.69 | 1.72 | +15.2 | +10.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_RUNNER | 9.1% | 100.0% | 100.0% | 50.0% | +32.9 | 999.00 | 999.00 | +35.8 | +7.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 81.8% | 27.8% | 27.8% | 27.8% | -4.3 | 0.67 | 1.46 | +15.0 | +13.0 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -6.2 | 0.57 | 1.32 | +15.9 | +12.3 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 9.1% | 0.0% | 0.0% | 50.0% | -12.1 | 0.00 | 0.00 | +5.3 | +14.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.5% | 0.0% | 0.0% | 0.0% | -24.2 | 0.00 | 0.00 | +3.9 | +28.0 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=60.0% Avg=+7.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 0.0% | -19.0 | 0.18 | 0.48 | +10.7 | +9.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 0.0% | -12.3 | 0.27 | 0.64 | +10.7 | +10.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 0.0% | -19.0 | 0.18 | 0.48 | +10.7 | +9.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 0.0% | -12.3 | 0.27 | 0.64 | +10.7 | +10.2 |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 0.0% | -19.0 | 0.18 | 0.48 | +10.7 | +9.8 |
| `confluence_gte_60` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 0.0% | -14.1 | 0.27 | 0.54 | +12.5 | +7.8 |
| `confluence_gte_70` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +2.6 | +13.7 |
| `tdi_rsi_gt_signal` | 4 | R_RUNNER | 36.4% | 75.0% | 75.0% | 0.0% | +9.9 | 6.63 | 2.21 | +20.9 | +6.3 |
| `tdi_rsi_gte_50` | 5 | R_REPEATER | 45.5% | 60.0% | 60.0% | 0.0% | +7.0 | 4.03 | 2.69 | +16.7 | +8.3 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 0.0% | -12.3 | 0.27 | 0.64 | +10.7 | +10.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_RUNNER | 36.4% | 75.0% | 75.0% | 0.0% | +9.9 | 6.63 | 2.21 | +20.9 | +6.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 0.0% | -12.3 | 0.27 | 0.64 | +10.7 | +10.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 0.0% | -20.4 | 0.19 | 0.43 | +11.7 | +9.1 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -19.6 | 0.18 | 0.55 | +12.7 | +7.8 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_REPEATER | 27.3% | 66.7% | 66.7% | 0.0% | +5.8 | 4.87 | 2.43 | +16.3 | +8.3 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=+10.0; validation N=12 Fav=33.3% Avg=+5.3; out_of_sample N=9 Fav=33.3% Avg=-2.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 25.8% | 29.0% | 19.4% | +1.0 | 1.19 | 2.77 | +15.5 | +9.9 |
| `hunt_to_ar_ratio_le_2_0` | 27 | S_STRANGER | 87.1% | 29.6% | 33.3% | 22.2% | +1.7 | 1.30 | 2.46 | +16.6 | +10.1 |
| `hunt_to_ar_ratio_le_2_5` | 28 | S_STRANGER | 90.3% | 28.6% | 32.1% | 21.4% | +1.3 | 1.23 | 2.45 | +16.2 | +10.1 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 90.3% | 28.6% | 32.1% | 21.4% | +1.3 | 1.23 | 2.45 | +16.2 | +10.1 |
| `asian_range_gte_30` | 27 | S_STRANGER | 87.1% | 29.6% | 33.3% | 22.2% | +2.4 | 1.48 | 2.80 | +16.7 | +8.8 |
| `confluence_gte_60` | 31 | S_STRANGER | 100.0% | 25.8% | 29.0% | 19.4% | +1.0 | 1.19 | 2.77 | +15.5 | +9.9 |
| `confluence_gte_70` | 31 | S_STRANGER | 100.0% | 25.8% | 29.0% | 19.4% | +1.0 | 1.19 | 2.77 | +15.5 | +9.9 |
| `tdi_rsi_gt_signal` | 31 | S_STRANGER | 100.0% | 25.8% | 29.0% | 19.4% | +1.0 | 1.19 | 2.77 | +15.5 | +9.9 |
| `tdi_rsi_gte_50` | 22 | S_STRANGER | 71.0% | 27.3% | 27.3% | 18.2% | -0.1 | 0.99 | 2.46 | +15.4 | +10.9 |
| `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 77.4% | 33.3% | 37.5% | 25.0% | +2.9 | 1.54 | 2.40 | +17.6 | +8.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 24 | S_STRANGER | 77.4% | 33.3% | 37.5% | 25.0% | +2.9 | 1.54 | 2.40 | +17.6 | +8.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 90.3% | 28.6% | 32.1% | 21.4% | +1.3 | 1.23 | 2.45 | +16.2 | +10.1 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 25.8% | 29.0% | 19.4% | +1.0 | 1.19 | 2.77 | +15.5 | +9.9 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 6.5% | 0.0% | 0.0% | 0.0% | -1.0 | 0.00 | 0.00 | +15.4 | +1.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.2% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +12.0 | +1.2 |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=20.0% Avg=+3.4; validation N=2 Fav=50.0% Avg=+24.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +6.9 | 2.46 | 7.37 | +41.7 | +13.4 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +6.9 | 2.46 | 7.37 | +41.7 | +13.4 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +6.9 | 2.46 | 7.37 | +41.7 | +13.4 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 0.0% | +2.5 | 1.48 | 6.66 | +38.8 | +14.1 |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +6.9 | 2.46 | 7.37 | +41.7 | +13.4 |
| `confluence_gte_60` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -8.8 | 0.00 | 0.00 | +37.3 | +23.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +60.9 | +14.8 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +6.9 | 2.46 | 7.37 | +41.7 | +13.4 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +6.9 | 2.46 | 7.37 | +41.7 | +13.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +60.9 | +14.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 0.0% | +2.5 | 1.48 | 6.66 | +38.8 | +14.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 0.0% | +3.6 | 1.65 | 6.59 | +33.0 | +13.5 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +16.0 | +4.1 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 0.0% | +15.0 | 12.56 | 25.13 | +62.3 | +9.8 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=12.5% Avg=-1.7; validation N=6 Fav=33.3% Avg=+7.1; out_of_sample N=1 Fav=100.0% Avg=+20.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 25.0% | 31.2% | 31.2% | +1.6 | 1.19 | 2.37 | +18.1 | +10.9 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 87.5% | 21.4% | 28.6% | 28.6% | -1.2 | 0.85 | 1.90 | +15.4 | +9.9 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 93.8% | 26.7% | 33.3% | 33.3% | +3.3 | 1.44 | 2.60 | +19.2 | +9.4 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 93.8% | 26.7% | 33.3% | 33.3% | +3.3 | 1.44 | 2.60 | +19.2 | +9.4 |
| `asian_range_gte_30` | 15 | S_STRANGER | 93.8% | 20.0% | 26.7% | 26.7% | -2.8 | 0.69 | 1.74 | +14.5 | +11.4 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 25.0% | 31.2% | 31.2% | +1.6 | 1.19 | 2.37 | +18.1 | +10.9 |
| `confluence_gte_70` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 20.0% | -0.7 | 0.95 | 3.79 | +21.2 | +18.6 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 43.8% | 14.3% | 14.3% | 14.3% | -1.2 | 0.89 | 4.46 | +14.5 | +14.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 43.8% | 0.0% | 0.0% | 0.0% | -10.7 | 0.00 | 0.00 | +7.7 | +14.3 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 87.5% | 21.4% | 28.6% | 28.6% | -1.2 | 0.85 | 1.90 | +15.4 | +9.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 37.5% | 0.0% | 0.0% | 0.0% | -12.4 | 0.00 | 0.00 | +4.9 | +15.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 93.8% | 26.7% | 33.3% | 33.3% | +3.3 | 1.44 | 2.60 | +19.2 | +9.4 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 25.0% | 31.2% | 31.2% | +1.6 | 1.19 | 2.37 | +18.1 | +10.9 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 62.5% | 20.0% | 20.0% | 20.0% | -4.1 | 0.60 | 2.39 | +13.2 | +14.2 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 31.2% | 0.0% | 0.0% | 0.0% | -11.8 | 0.00 | 0.00 | +8.3 | +15.2 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-2.7; validation N=5 Fav=60.0% Avg=+11.5; out_of_sample N=6 Fav=16.7% Avg=-2.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | +1.3 | 1.29 | 3.56 | +13.0 | +8.6 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 87.5% | 21.4% | 21.4% | 28.6% | -0.2 | 0.95 | 3.18 | +12.0 | +9.5 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 93.8% | 20.0% | 20.0% | 26.7% | -0.3 | 0.94 | 3.46 | +11.9 | +9.0 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 93.8% | 20.0% | 20.0% | 26.7% | -0.3 | 0.94 | 3.46 | +11.9 | +9.0 |
| `asian_range_gte_30` | 13 | S_STRANGER | 81.2% | 30.8% | 30.8% | 30.8% | +2.9 | 1.73 | 3.47 | +14.2 | +8.1 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | +1.3 | 1.29 | 3.56 | +13.0 | +8.6 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | +1.3 | 1.29 | 3.56 | +13.0 | +8.6 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 56.2% | 11.1% | 11.1% | 11.1% | -1.9 | 0.64 | 5.09 | +11.8 | +10.1 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 75.0% | 16.7% | 16.7% | 16.7% | +0.1 | 1.03 | 4.65 | +13.0 | +9.8 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 75.0% | 25.0% | 25.0% | 33.3% | +1.1 | 1.27 | 3.38 | +12.9 | +8.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 37.5% | 16.7% | 16.7% | 16.7% | +0.0 | 1.00 | 5.02 | +13.8 | +9.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 93.8% | 20.0% | 20.0% | 26.7% | -0.3 | 0.94 | 3.46 | +11.9 | +9.0 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | +1.3 | 1.29 | 3.56 | +13.0 | +8.6 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -7.4 | 0.00 | 0.00 | +0.8 | +10.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +0.7 | +11.0 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+3.5; validation N=2 Fav=50.0% Avg=+5.0; out_of_sample N=1 Fav=0.0% Avg=-21.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 41.7% | -5.5 | 0.38 | 0.89 | +12.7 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 75.0% | 33.3% | 33.3% | 55.6% | +1.0 | 1.30 | 1.74 | +16.0 | +3.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 45.5% | -5.6 | 0.40 | 0.79 | +13.7 | +3.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 45.5% | +0.0 | 1.00 | 2.00 | +13.6 | +4.1 |
| `asian_range_gte_30` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 45.5% | -5.6 | 0.40 | 0.79 | +13.7 | +3.6 |
| `confluence_gte_60` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 37.5% | -7.6 | 0.40 | 0.66 | +13.7 | +2.8 |
| `confluence_gte_70` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -21.8 | 0.00 | 0.00 | +2.8 | +1.1 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 50.0% | -2.6 | 0.49 | 1.46 | +13.5 | +4.5 |
| `tdi_rsi_gte_50` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 66.7% | +7.3 | 6.95 | 3.47 | +19.5 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 75.0% | 33.3% | 33.3% | 55.6% | +1.0 | 1.30 | 1.74 | +16.0 | +3.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 50.0% | -2.6 | 0.49 | 1.46 | +13.5 | +4.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 45.5% | +0.0 | 1.00 | 2.00 | +13.6 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 41.7% | -5.5 | 0.38 | 0.89 | +12.7 | +3.8 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 60.0% | +2.5 | 3.73 | 7.47 | +14.0 | +4.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | +6.6 | 4.54 | 4.54 | +15.2 | +5.3 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+4.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=20.0% Avg=-4.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 17.6% | -13.3 | 0.30 | 0.98 | +11.0 | +13.2 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 88.2% | 20.0% | 20.0% | 13.3% | -15.5 | 0.27 | 1.09 | +11.3 | +13.9 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 88.2% | 20.0% | 20.0% | 13.3% | -15.5 | 0.27 | 1.09 | +11.3 | +13.9 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 17.6% | -13.3 | 0.30 | 0.98 | +11.0 | +13.2 |
| `asian_range_gte_30` | 9 | S_STRANGER | 52.9% | 33.3% | 33.3% | 22.2% | -0.7 | 0.93 | 1.87 | +16.4 | +14.1 |
| `confluence_gte_60` | 15 | S_STRANGER | 88.2% | 26.7% | 26.7% | 20.0% | -14.6 | 0.31 | 0.85 | +12.3 | +13.5 |
| `confluence_gte_70` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -23.7 | 0.00 | 0.00 | +7.6 | +19.8 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 94.1% | 25.0% | 25.0% | 18.8% | -7.7 | 0.44 | 1.33 | +11.7 | +13.3 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 47.1% | 12.5% | 12.5% | 0.0% | -12.1 | 0.10 | 0.73 | +8.7 | +18.0 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 52.9% | 33.3% | 33.3% | 22.2% | -0.7 | 0.93 | 1.87 | +16.4 | +14.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 52.9% | 33.3% | 33.3% | 22.2% | -0.7 | 0.93 | 1.87 | +16.4 | +14.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 17.6% | -13.3 | 0.30 | 0.98 | +11.0 | +13.2 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 17.6% | -13.3 | 0.30 | 0.98 | +11.0 | +13.2 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 17.6% | 33.3% | 33.3% | 33.3% | +2.1 | 1.19 | 2.37 | +16.8 | +18.6 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -16.8 | 0.00 | 0.00 | +4.0 | +22.8 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-14.7; validation N=26 Fav=26.9% Avg=-1.0; out_of_sample N=14 Fav=28.6% Avg=-0.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 60 | S_STRANGER | 100.0% | 23.3% | 25.0% | 10.0% | -0.8 | 0.84 | 2.34 | +13.1 | +9.9 |
| `hunt_to_ar_ratio_le_2_0` | 48 | S_STRANGER | 80.0% | 22.9% | 25.0% | 8.3% | -0.5 | 0.89 | 2.51 | +13.3 | +9.8 |
| `hunt_to_ar_ratio_le_2_5` | 52 | S_STRANGER | 86.7% | 23.1% | 25.0% | 9.6% | -0.4 | 0.92 | 2.56 | +13.2 | +9.8 |
| `stop_hunt_le_90` | 58 | S_STRANGER | 96.7% | 20.7% | 22.4% | 8.6% | -1.4 | 0.74 | 2.38 | +12.6 | +10.2 |
| `asian_range_gte_30` | 53 | S_STRANGER | 88.3% | 24.5% | 26.4% | 9.4% | -0.3 | 0.94 | 2.49 | +13.6 | +9.7 |
| `confluence_gte_60` | 60 | S_STRANGER | 100.0% | 23.3% | 25.0% | 10.0% | -0.8 | 0.84 | 2.34 | +13.1 | +9.9 |
| `confluence_gte_70` | 60 | S_STRANGER | 100.0% | 23.3% | 25.0% | 10.0% | -0.8 | 0.84 | 2.34 | +13.1 | +9.9 |
| `tdi_rsi_gt_signal` | 35 | S_STRANGER | 58.3% | 20.0% | 22.9% | 8.6% | -4.1 | 0.41 | 1.33 | +11.2 | +10.9 |
| `tdi_rsi_gte_50` | 42 | S_STRANGER | 70.0% | 26.2% | 26.2% | 7.1% | -1.5 | 0.72 | 1.98 | +13.2 | +10.1 |
| `ratio_le_2_and_asian_gte_30` | 46 | S_STRANGER | 76.7% | 21.7% | 23.9% | 8.7% | -0.8 | 0.83 | 2.50 | +13.0 | +9.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 27 | S_STRANGER | 45.0% | 18.5% | 22.2% | 7.4% | -4.1 | 0.38 | 1.27 | +10.9 | +10.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 58 | S_STRANGER | 96.7% | 20.7% | 22.4% | 8.6% | -1.4 | 0.74 | 2.38 | +12.6 | +10.2 |
| `feature_stale_hod_exhaustion_reject` | 60 | S_STRANGER | 100.0% | 23.3% | 25.0% | 10.0% | -0.8 | 0.84 | 2.34 | +13.1 | +9.9 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -15.1 | 0.00 | 0.00 | +8.0 | +17.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 1.7% | 0.0% | 0.0% | 0.0% | -27.6 | 0.00 | 0.00 | +1.6 | +30.1 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.1; validation N=1 Fav=0.0% Avg=-27.3; out_of_sample N=7 Fav=57.1% Avg=+2.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 4.3% | -12.4 | 0.28 | 0.80 | +10.5 | +9.4 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 52.2% | 8.3% | 16.7% | 8.3% | -11.5 | 0.19 | 0.97 | +7.9 | +8.0 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 87.0% | 25.0% | 30.0% | 5.0% | -8.3 | 0.40 | 0.94 | +11.6 | +9.2 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 65.2% | 13.3% | 20.0% | 6.7% | -14.2 | 0.14 | 0.57 | +8.1 | +8.5 |
| `asian_range_gte_30` | 22 | S_STRANGER | 95.7% | 22.7% | 27.3% | 4.5% | -11.8 | 0.30 | 0.81 | +10.9 | +8.5 |
| `confluence_gte_60` | 19 | S_STRANGER | 82.6% | 21.1% | 26.3% | 0.0% | -10.8 | 0.30 | 0.85 | +10.3 | +10.5 |
| `confluence_gte_70` | 3 | S_STRANGER | 13.0% | 33.3% | 33.3% | 0.0% | -11.0 | 0.07 | 0.13 | +7.3 | +4.9 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 17.4% | 50.0% | 50.0% | 0.0% | +3.6 | 1.97 | 1.97 | +13.6 | +5.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 39.1% | 44.4% | 44.4% | 0.0% | -1.5 | 0.86 | 1.07 | +14.9 | +15.1 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 52.2% | 8.3% | 16.7% | 8.3% | -11.5 | 0.19 | 0.97 | +7.9 | +8.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 8.7% | 0.0% | 0.0% | 0.0% | -7.4 | 0.00 | 0.00 | +2.9 | +9.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 65.2% | 13.3% | 20.0% | 6.7% | -14.2 | 0.14 | 0.57 | +8.1 | +8.5 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 4.3% | -12.4 | 0.28 | 0.80 | +10.5 | +9.4 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +5.5 | +5.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +5.5 | +5.8 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=13 Fav=30.8% Avg=+1.4; validation N=13 Fav=23.1% Avg=+7.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 21.6% | 21.6% | 16.2% | +2.6 | 1.44 | 5.05 | +17.2 | +13.2 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 70.3% | 26.9% | 26.9% | 23.1% | +4.5 | 1.62 | 4.17 | +19.8 | +15.4 |
| `hunt_to_ar_ratio_le_2_5` | 35 | S_STRANGER | 94.6% | 22.9% | 22.9% | 17.1% | +2.8 | 1.45 | 4.72 | +17.3 | +13.5 |
| `stop_hunt_le_90` | 34 | S_STRANGER | 91.9% | 23.5% | 23.5% | 17.6% | +3.1 | 1.51 | 4.71 | +17.3 | +13.5 |
| `asian_range_gte_30` | 28 | S_STRANGER | 75.7% | 25.0% | 25.0% | 21.4% | +3.7 | 1.53 | 4.38 | +19.2 | +15.2 |
| `confluence_gte_60` | 37 | S_STRANGER | 100.0% | 21.6% | 21.6% | 16.2% | +2.6 | 1.44 | 5.05 | +17.2 | +13.2 |
| `confluence_gte_70` | 37 | S_STRANGER | 100.0% | 21.6% | 21.6% | 16.2% | +2.6 | 1.44 | 5.05 | +17.2 | +13.2 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 21.6% | 25.0% | 25.0% | 0.0% | -0.7 | 0.84 | 2.51 | +14.2 | +14.9 |
| `tdi_rsi_gte_50` | 32 | S_STRANGER | 86.5% | 15.6% | 15.6% | 12.5% | -0.1 | 0.99 | 5.16 | +15.2 | +14.1 |
| `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 64.9% | 25.0% | 25.0% | 25.0% | +4.2 | 1.54 | 4.36 | +19.5 | +16.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 10.8% | 0.0% | 0.0% | 0.0% | -8.9 | 0.00 | 0.00 | +6.9 | +24.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 34 | S_STRANGER | 91.9% | 23.5% | 23.5% | 17.6% | +3.1 | 1.51 | 4.71 | +17.3 | +13.5 |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 21.6% | 21.6% | 16.2% | +2.6 | 1.44 | 5.05 | +17.2 | +13.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-0.3; validation N=2 Fav=0.0% Avg=-3.8; out_of_sample N=8 Fav=37.5% Avg=+1.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -0.9 | 0.74 | 2.71 | +9.9 | +9.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 78.6% | 18.2% | 18.2% | 0.0% | -1.0 | 0.73 | 3.30 | +10.9 | +8.9 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 0.0% | -1.4 | 0.63 | 3.45 | +9.9 | +9.3 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 0.0% | -1.4 | 0.63 | 3.45 | +9.9 | +9.3 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -0.9 | 0.74 | 2.71 | +9.9 | +9.0 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -0.9 | 0.74 | 2.71 | +9.9 | +9.0 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -0.9 | 0.74 | 2.71 | +9.9 | +9.0 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 0.0% | -2.6 | 0.66 | 0.66 | +8.9 | +17.5 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 85.7% | 25.0% | 25.0% | 0.0% | +0.2 | 1.08 | 3.23 | +9.2 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 78.6% | 18.2% | 18.2% | 0.0% | -1.0 | 0.73 | 3.30 | +10.9 | +8.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 0.0% | -2.6 | 0.66 | 0.66 | +8.9 | +17.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 0.0% | -1.4 | 0.63 | 3.45 | +9.9 | +9.3 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -0.9 | 0.74 | 2.71 | +9.9 | +9.0 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +4.6 | +7.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +4.6 | +7.4 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.9; validation N=21 Fav=38.1% Avg=+2.2; out_of_sample N=18 Fav=5.6% Avg=-8.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 42 | S_STRANGER | 100.0% | 21.4% | 23.8% | 14.3% | -2.5 | 0.57 | 1.77 | +13.0 | +11.0 |
| `hunt_to_ar_ratio_le_2_0` | 40 | S_STRANGER | 95.2% | 20.0% | 22.5% | 12.5% | -3.5 | 0.42 | 1.39 | +12.5 | +11.0 |
| `hunt_to_ar_ratio_le_2_5` | 41 | S_STRANGER | 97.6% | 19.5% | 22.0% | 12.2% | -3.6 | 0.41 | 1.40 | +12.2 | +11.0 |
| `stop_hunt_le_90` | 41 | S_STRANGER | 97.6% | 19.5% | 22.0% | 12.2% | -3.6 | 0.41 | 1.40 | +12.2 | +11.0 |
| `asian_range_gte_30` | 40 | S_STRANGER | 95.2% | 22.5% | 25.0% | 15.0% | -2.6 | 0.58 | 1.68 | +13.2 | +11.2 |
| `confluence_gte_60` | 42 | S_STRANGER | 100.0% | 21.4% | 23.8% | 14.3% | -2.5 | 0.57 | 1.77 | +13.0 | +11.0 |
| `confluence_gte_70` | 42 | S_STRANGER | 100.0% | 21.4% | 23.8% | 14.3% | -2.5 | 0.57 | 1.77 | +13.0 | +11.0 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 47.6% | 10.0% | 15.0% | 10.0% | -6.4 | 0.19 | 1.02 | +12.9 | +12.8 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 47.6% | 10.0% | 10.0% | 0.0% | -5.9 | 0.07 | 0.64 | +9.9 | +13.2 |
| `ratio_le_2_and_asian_gte_30` | 38 | S_STRANGER | 90.5% | 21.1% | 23.7% | 13.2% | -3.6 | 0.42 | 1.32 | +12.7 | +11.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 19 | S_STRANGER | 45.2% | 10.5% | 15.8% | 10.5% | -6.4 | 0.20 | 0.99 | +13.5 | +12.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 41 | S_STRANGER | 97.6% | 19.5% | 22.0% | 12.2% | -3.6 | 0.41 | 1.40 | +12.2 | +11.0 |
| `feature_stale_hod_exhaustion_reject` | 42 | S_STRANGER | 100.0% | 21.4% | 23.8% | 14.3% | -2.5 | 0.57 | 1.77 | +13.0 | +11.0 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 2.4% | 100.0% | 100.0% | 100.0% | +20.0 | 999.00 | 999.00 | +28.7 | +6.4 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=25.0% Avg=+0.3; out_of_sample N=8 Fav=37.5% Avg=+13.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 39 | S_STRANGER | 100.0% | 20.5% | 25.6% | 23.1% | -5.1 | 0.52 | 1.29 | +11.2 | +8.9 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 76.9% | 20.0% | 23.3% | 26.7% | -4.7 | 0.48 | 1.31 | +10.4 | +8.9 |
| `hunt_to_ar_ratio_le_2_5` | 36 | S_STRANGER | 92.3% | 19.4% | 22.2% | 22.2% | -7.4 | 0.35 | 1.04 | +9.8 | +9.4 |
| `stop_hunt_le_90` | 34 | S_STRANGER | 87.2% | 20.6% | 26.5% | 23.5% | -4.1 | 0.51 | 1.19 | +10.3 | +8.8 |
| `asian_range_gte_30` | 35 | S_STRANGER | 89.7% | 17.1% | 20.0% | 20.0% | -7.5 | 0.36 | 1.23 | +10.3 | +9.3 |
| `confluence_gte_60` | 33 | S_STRANGER | 84.6% | 21.2% | 27.3% | 24.2% | -4.5 | 0.58 | 1.29 | +11.6 | +7.3 |
| `confluence_gte_70` | 12 | S_STRANGER | 30.8% | 33.3% | 41.7% | 33.3% | +9.1 | 4.51 | 5.41 | +16.1 | +6.3 |
| `tdi_rsi_gt_signal` | 22 | S_STRANGER | 56.4% | 18.2% | 22.7% | 22.7% | -4.9 | 0.48 | 1.45 | +8.8 | +10.5 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 35.9% | 21.4% | 21.4% | 7.1% | -3.1 | 0.62 | 2.27 | +8.8 | +14.0 |
| `ratio_le_2_and_asian_gte_30` | 28 | S_STRANGER | 71.8% | 14.3% | 17.9% | 21.4% | -7.2 | 0.26 | 1.00 | +8.9 | +9.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 38.5% | 13.3% | 20.0% | 20.0% | -6.3 | 0.30 | 1.00 | +7.2 | +10.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 34 | S_STRANGER | 87.2% | 20.6% | 26.5% | 23.5% | -4.1 | 0.51 | 1.19 | +10.3 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 39 | S_STRANGER | 100.0% | 20.5% | 25.6% | 23.1% | -5.1 | 0.52 | 1.29 | +11.2 | +8.9 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 2.6% | 0.0% | 0.0% | 0.0% | -27.5 | 0.00 | 0.00 | +4.0 | +27.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.6% | 0.0% | 0.0% | 0.0% | -27.5 | 0.00 | 0.00 | +4.0 | +27.6 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=27.3% Avg=+11.8; validation N=8 Fav=37.5% Avg=+4.5; out_of_sample N=2 Fav=0.0% Avg=-17.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 43.3% | +1.9 | 1.34 | 3.79 | +17.4 | +11.5 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 56.7% | 23.5% | 23.5% | 29.4% | -1.1 | 0.88 | 2.65 | +18.5 | +15.6 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 80.0% | 20.8% | 20.8% | 41.7% | +1.0 | 1.16 | 3.23 | +17.6 | +12.9 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 73.3% | 22.7% | 22.7% | 36.4% | +0.9 | 1.12 | 3.14 | +18.3 | +13.0 |
| `asian_range_gte_30` | 27 | S_STRANGER | 90.0% | 22.2% | 22.2% | 40.7% | +2.2 | 1.35 | 3.60 | +18.1 | +12.4 |
| `confluence_gte_60` | 10 | S_STRANGER | 33.3% | 20.0% | 20.0% | 40.0% | +8.1 | 5.38 | 16.14 | +20.3 | +6.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 70.0% | 28.6% | 28.6% | 42.9% | +6.3 | 2.37 | 4.75 | +21.3 | +11.1 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 53.3% | 18.8% | 18.8% | 37.5% | +2.9 | 1.45 | 4.84 | +18.1 | +12.4 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 56.7% | 23.5% | 23.5% | 29.4% | -1.1 | 0.88 | 2.65 | +18.5 | +15.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 46.7% | 28.6% | 28.6% | 35.7% | +3.8 | 1.64 | 3.70 | +21.4 | +13.1 |
| `feature_fresh_reclaim_within_8` | 4 | S_STRANGER | 13.3% | 25.0% | 25.0% | 25.0% | -9.0 | 0.28 | 0.85 | +12.6 | +20.5 |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 70.0% | 23.8% | 23.8% | 38.1% | +1.1 | 1.15 | 2.98 | +19.1 | +13.2 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 43.3% | +1.9 | 1.34 | 3.79 | +17.4 | +11.5 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 40.0% | 16.7% | 16.7% | 41.7% | +0.3 | 1.07 | 3.75 | +13.1 | +9.5 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 13.3% | 25.0% | 25.0% | 50.0% | +5.3 | 1.81 | 3.63 | +17.9 | +12.2 |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+11.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=0.0% Avg=-15.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -6.1 | 0.39 | 1.56 | +12.6 | +12.4 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 0.0% | +1.3 | 1.24 | 2.48 | +18.6 | +10.4 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 0.0% | -2.8 | 0.64 | 1.91 | +15.5 | +12.8 |
| `stop_hunt_le_90` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 0.0% | +1.3 | 1.24 | 2.48 | +18.6 | +10.4 |
| `asian_range_gte_30` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 0.0% | -2.8 | 0.64 | 1.91 | +15.5 | +12.8 |
| `confluence_gte_60` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | +8.1 | 2.03 | 2.03 | +34.8 | +12.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | -7.6 | 0.24 | 0.47 | +9.9 | +16.5 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 40.0% | 40.0% | 0.0% | +0.7 | 1.10 | 1.65 | +20.9 | +12.3 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 0.0% | +1.3 | 1.24 | 2.48 | +18.6 | +10.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +7.1 | 999.00 | 999.00 | +17.8 | +9.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 0.0% | +1.3 | 1.24 | 2.48 | +18.6 | +10.4 |
| `feature_stale_hod_exhaustion_reject` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 0.0% | -6.2 | 0.41 | 1.44 | +13.6 | +12.5 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -13.5 | 0.00 | 0.00 | +6.7 | +13.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | -4.8 | 0.33 | 0.66 | +12.1 | +11.2 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=11.1% Avg=-0.1; validation N=7 Fav=42.9% Avg=+3.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 18.2% | 22.7% | 27.3% | -0.9 | 0.86 | 2.24 | +16.3 | +9.3 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 59.1% | 15.4% | 15.4% | 23.1% | -1.4 | 0.81 | 3.67 | +19.8 | +11.0 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 77.3% | 11.8% | 11.8% | 23.5% | -2.2 | 0.68 | 4.09 | +16.4 | +9.8 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 72.7% | 18.8% | 18.8% | 25.0% | -1.3 | 0.81 | 2.70 | +17.0 | +9.8 |
| `asian_range_gte_30` | 20 | S_STRANGER | 90.9% | 15.0% | 20.0% | 30.0% | -0.8 | 0.88 | 2.63 | +16.5 | +9.8 |
| `confluence_gte_60` | 7 | S_STRANGER | 31.8% | 14.3% | 14.3% | 14.3% | -0.4 | 0.80 | 3.98 | +18.3 | +7.6 |
| `confluence_gte_70` | 1 | S_STRANGER | 4.5% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +4.0 | +11.0 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 18.2% | 25.0% | 25.0% | 0.0% | -3.0 | 0.48 | 1.45 | +10.7 | +6.3 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 72.7% | 25.0% | 25.0% | 25.0% | +1.4 | 1.24 | 3.11 | +19.6 | +9.8 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 59.1% | 15.4% | 15.4% | 23.1% | -1.4 | 0.81 | 3.67 | +19.8 | +11.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.5% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +4.0 | +11.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 72.7% | 18.8% | 18.8% | 25.0% | -1.3 | 0.81 | 2.70 | +17.0 | +9.8 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 18.2% | 22.7% | 27.3% | -0.9 | 0.86 | 2.24 | +16.3 | +9.3 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 13.6% | 33.3% | 33.3% | 66.7% | +4.4 | 6.30 | 6.30 | +18.9 | +2.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 9.1% | 50.0% | 50.0% | 50.0% | +6.6 | 6.30 | 6.30 | +20.3 | +4.2 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=60.0% Avg=+13.6; validation N=1 Fav=0.0% Avg=-4.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 5.9% | -2.5 | 0.65 | 3.01 | +13.2 | +13.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 58.8% | 10.0% | 10.0% | 0.0% | -5.8 | 0.21 | 1.87 | +11.1 | +16.3 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 94.1% | 12.5% | 12.5% | 0.0% | -5.3 | 0.29 | 2.03 | +11.3 | +14.5 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 82.4% | 7.1% | 7.1% | 0.0% | -6.2 | 0.15 | 1.92 | +10.2 | +15.1 |
| `asian_range_gte_30` | 11 | S_STRANGER | 64.7% | 27.3% | 27.3% | 9.1% | -0.2 | 0.97 | 2.58 | +14.6 | +14.1 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 5.9% | -2.5 | 0.65 | 3.01 | +13.2 | +13.6 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 5.9% | -2.5 | 0.65 | 3.01 | +13.2 | +13.6 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 35.3% | 33.3% | 33.3% | 0.0% | -4.3 | 0.57 | 1.15 | +17.7 | +15.4 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 5.9% | -2.5 | 0.65 | 3.01 | +13.2 | +13.6 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 47.1% | 12.5% | 12.5% | 0.0% | -6.0 | 0.24 | 1.69 | +9.9 | +16.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 17.6% | 33.3% | 33.3% | 0.0% | -6.9 | 0.42 | 0.84 | +13.8 | +17.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 64.7% | 9.1% | 9.1% | 0.0% | -5.7 | 0.20 | 1.95 | +10.8 | +15.5 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 76.5% | 23.1% | 23.1% | 7.7% | -1.1 | 0.84 | 2.80 | +15.1 | +14.1 |
| `feature_momentum_breakout_exception` | 6 | R_REPEATER | 35.3% | 50.0% | 50.0% | 16.7% | +10.6 | 5.66 | 5.66 | +24.4 | +9.2 |
| `feature_eurjpy_tdi50_reclaim` | 11 | S_STRANGER | 64.7% | 27.3% | 27.3% | 9.1% | +1.7 | 1.33 | 3.53 | +16.6 | +11.2 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+19.1; validation N=3 Fav=0.0% Avg=-1.6; out_of_sample N=1 Fav=0.0% Avg=-6.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 33.3% | -3.8 | 0.36 | 1.42 | +14.4 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 30.0% | -4.5 | 0.36 | 1.27 | +13.9 | +9.2 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 30.0% | -4.5 | 0.36 | 1.27 | +13.9 | +9.2 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 30.0% | -4.5 | 0.36 | 1.27 | +13.9 | +9.2 |
| `asian_range_gte_30` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 27.3% | -5.9 | 0.09 | 0.71 | +13.8 | +9.1 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 33.3% | -3.8 | 0.36 | 1.42 | +14.4 | +8.8 |
| `confluence_gte_70` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +17.2 | +12.1 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 30.0% | -4.2 | 0.38 | 1.32 | +15.1 | +9.0 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -10.5 | 0.00 | 0.00 | +15.7 | +16.5 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 22.2% | -7.1 | 0.09 | 0.63 | +13.1 | +9.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 14.3% | -8.5 | 0.10 | 0.57 | +13.6 | +9.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 30.0% | -4.5 | 0.36 | 1.27 | +13.9 | +9.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 33.3% | -3.8 | 0.36 | 1.42 | +14.4 | +8.8 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 60.0% | +1.5 | 1.66 | 3.32 | +15.8 | +7.6 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=33.3% Avg=-12.0; out_of_sample N=6 Fav=16.7% Avg=-17.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -14.1 | 0.12 | 0.62 | +7.8 | +10.6 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 22.2% | -15.9 | 0.14 | 0.50 | +8.3 | +9.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -14.1 | 0.12 | 0.62 | +7.8 | +10.6 |
| `stop_hunt_le_90` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 22.2% | -15.9 | 0.14 | 0.50 | +8.3 | +9.8 |
| `asian_range_gte_30` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 9.1% | -16.3 | 0.07 | 0.69 | +7.4 | +11.5 |
| `confluence_gte_60` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 12.5% | -13.1 | 0.09 | 0.64 | +8.9 | +8.4 |
| `confluence_gte_70` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | +1.7 | 1.46 | 1.46 | +6.4 | +5.8 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -13.8 | 0.00 | 0.00 | +7.5 | +15.3 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -13.9 | 0.00 | 0.00 | +6.8 | +15.3 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 12.5% | -19.2 | 0.08 | 0.56 | +7.7 | +10.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -18.1 | 0.00 | 0.00 | +4.4 | +19.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 22.2% | -15.9 | 0.14 | 0.50 | +8.3 | +9.8 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -14.1 | 0.12 | 0.62 | +7.8 | +10.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=-14.5; validation N=1 Fav=0.0% Avg=-2.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -14.2 | 0.22 | 1.10 | +13.5 | +22.2 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 18.2% | -15.3 | 0.22 | 1.00 | +14.1 | +23.4 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -14.2 | 0.22 | 1.10 | +13.5 | +22.2 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -14.2 | 0.22 | 1.10 | +13.5 | +22.2 |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -14.2 | 0.22 | 1.10 | +13.5 | +22.2 |
| `confluence_gte_60` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 28.6% | -12.8 | 0.35 | 0.87 | +19.6 | +22.8 |
| `confluence_gte_70` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | -8.2 | 0.60 | 0.60 | +35.7 | +33.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 11.1% | -20.3 | 0.12 | 0.95 | +12.1 | +26.3 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 11.1% | -16.4 | 0.14 | 1.14 | +12.2 | +27.3 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 18.2% | -15.3 | 0.22 | 1.00 | +14.1 | +23.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 12.5% | -22.6 | 0.12 | 0.84 | +12.8 | +28.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 18.2% | -15.3 | 0.22 | 1.00 | +14.1 | +23.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -14.2 | 0.22 | 1.10 | +13.5 | +22.2 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 16.7% | -6.3 | 0.38 | 1.91 | +11.5 | +16.6 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -14.6 | 0.00 | 0.00 | +5.6 | +20.9 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=0.0% Avg=-5.9; out_of_sample N=10 Fav=30.0% Avg=+1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 15.8% | 15.8% | 5.3% | -2.9 | 0.58 | 3.08 | +12.2 | +10.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 47.4% | 11.1% | 11.1% | 11.1% | -1.1 | 0.78 | 6.23 | +14.5 | +10.4 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 89.5% | 17.6% | 17.6% | 5.9% | -1.7 | 0.72 | 3.38 | +13.4 | +9.7 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 84.2% | 18.8% | 18.8% | 6.2% | -1.0 | 0.82 | 3.57 | +13.7 | +10.3 |
| `asian_range_gte_30` | 18 | S_STRANGER | 94.7% | 11.1% | 11.1% | 0.0% | -5.0 | 0.31 | 2.50 | +9.6 | +10.9 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 15.8% | 15.8% | 5.3% | -2.9 | 0.58 | 3.08 | +12.2 | +10.4 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 15.8% | 15.8% | 5.3% | -2.9 | 0.58 | 3.08 | +12.2 | +10.4 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 47.4% | 11.1% | 11.1% | 0.0% | -5.8 | 0.33 | 2.62 | +10.0 | +13.4 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 78.9% | 6.7% | 6.7% | 0.0% | -6.1 | 0.22 | 3.02 | +8.6 | +11.9 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 42.1% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +9.0 | +11.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 26.3% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +9.8 | +12.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 84.2% | 18.8% | 18.8% | 6.2% | -1.0 | 0.82 | 3.57 | +13.7 | +10.3 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 15.8% | 15.8% | 5.3% | -2.9 | 0.58 | 3.08 | +12.2 | +10.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+7.2; validation N=1 Fav=100.0% Avg=+55.1; out_of_sample N=1 Fav=0.0% Avg=-2.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 15.4% | 15.4% | 30.8% | -7.4 | 0.44 | 1.87 | +16.4 | +10.3 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 80.8% | 9.5% | 9.5% | 19.0% | -11.4 | 0.30 | 2.38 | +14.9 | +11.2 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 96.2% | 16.0% | 16.0% | 28.0% | -7.7 | 0.44 | 1.87 | +16.1 | +10.5 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 84.6% | 9.1% | 9.1% | 22.7% | -10.9 | 0.30 | 2.38 | +15.3 | +11.0 |
| `asian_range_gte_30` | 26 | S_STRANGER | 100.0% | 15.4% | 15.4% | 30.8% | -7.4 | 0.44 | 1.87 | +16.4 | +10.3 |
| `confluence_gte_60` | 4 | S_STRANGER | 15.4% | 25.0% | 25.0% | 25.0% | -0.6 | 0.87 | 2.61 | +19.6 | +10.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 22 | S_STRANGER | 84.6% | 18.2% | 18.2% | 36.4% | -4.6 | 0.60 | 1.95 | +18.1 | +10.0 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 34.6% | 33.3% | 33.3% | 44.4% | +11.4 | 4.24 | 5.65 | +26.7 | +9.9 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 80.8% | 9.5% | 9.5% | 19.0% | -11.4 | 0.30 | 2.38 | +14.9 | +11.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 65.4% | 11.8% | 11.8% | 23.5% | -8.7 | 0.41 | 2.45 | +16.7 | +10.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 84.6% | 9.1% | 9.1% | 22.7% | -10.9 | 0.30 | 2.38 | +15.3 | +11.0 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 15.4% | 15.4% | 30.8% | -7.4 | 0.44 | 1.87 | +16.4 | +10.3 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 7.7% | 50.0% | 50.0% | 50.0% | +12.1 | 3.81 | 3.81 | +23.3 | +9.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 3.8% | 100.0% | 100.0% | 100.0% | +32.7 | 999.00 | 999.00 | +38.6 | +4.0 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=28.6% Avg=+1.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=0.0% Avg=-1.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -1.2 | 0.58 | 1.74 | +12.5 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -1.2 | 0.58 | 1.74 | +12.5 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -1.2 | 0.58 | 1.74 | +12.5 | +8.8 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -1.2 | 0.58 | 1.74 | +12.5 | +8.8 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -1.2 | 0.58 | 1.74 | +12.5 | +8.8 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -1.2 | 0.58 | 1.74 | +12.5 | +8.8 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -1.2 | 0.58 | 1.74 | +12.5 | +8.8 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 20.0% | -4.3 | 0.00 | 0.00 | +9.4 | +9.0 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 22.2% | +0.8 | 1.49 | 4.46 | +14.5 | +10.7 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -1.2 | 0.58 | 1.74 | +12.5 | +8.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 20.0% | -4.3 | 0.00 | 0.00 | +9.4 | +9.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -1.2 | 0.58 | 1.74 | +12.5 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -1.2 | 0.58 | 1.74 | +12.5 | +8.8 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 21.4% | 0.0% | 33.3% | 33.3% | -0.1 | 0.90 | 0.90 | +11.7 | +9.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 33.3% | -1.5 | 0.00 | 0.00 | +13.4 | +11.2 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-17.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=28.6% Avg=-6.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 0.0% | -9.6 | 0.18 | 0.66 | +7.8 | +12.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 0.0% | -9.6 | 0.18 | 0.66 | +7.8 | +12.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 0.0% | -9.6 | 0.18 | 0.66 | +7.8 | +12.7 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 0.0% | -9.6 | 0.18 | 0.66 | +7.8 | +12.7 |
| `asian_range_gte_30` | 11 | S_STRANGER | 78.6% | 9.1% | 18.2% | 0.0% | -9.8 | 0.15 | 0.66 | +7.2 | +11.6 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 0.0% | -9.6 | 0.18 | 0.66 | +7.8 | +12.7 |
| `confluence_gte_70` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -14.2 | 0.00 | 0.00 | +4.7 | +17.5 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -4.8 | 0.00 | 0.00 | +4.9 | +11.5 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 0.0% | -9.8 | 0.19 | 0.74 | +8.6 | +15.6 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 78.6% | 9.1% | 18.2% | 0.0% | -9.8 | 0.15 | 0.66 | +7.2 | +11.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -4.8 | 0.00 | 0.00 | +4.9 | +11.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 0.0% | -9.6 | 0.18 | 0.66 | +7.8 | +12.7 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 0.0% | -9.6 | 0.18 | 0.66 | +7.8 | +12.7 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 28.6% | 0.0% | 25.0% | 0.0% | -14.8 | 0.11 | 0.33 | +5.5 | +18.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -22.2 | 0.00 | 0.00 | +3.3 | +23.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-2.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 11.5% | 11.5% | 7.7% | -13.0 | 0.10 | 0.77 | +7.4 | +9.9 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 88.5% | 13.0% | 13.0% | 8.7% | -9.0 | 0.16 | 1.02 | +7.9 | +9.7 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 100.0% | 11.5% | 11.5% | 7.7% | -13.0 | 0.10 | 0.77 | +7.4 | +9.9 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 88.5% | 13.0% | 13.0% | 8.7% | -9.0 | 0.16 | 1.02 | +7.9 | +9.7 |
| `asian_range_gte_30` | 26 | S_STRANGER | 100.0% | 11.5% | 11.5% | 7.7% | -13.0 | 0.10 | 0.77 | +7.4 | +9.9 |
| `confluence_gte_60` | 20 | S_STRANGER | 76.9% | 10.0% | 10.0% | 5.0% | -16.8 | 0.05 | 0.44 | +7.2 | +10.6 |
| `confluence_gte_70` | 9 | S_STRANGER | 34.6% | 0.0% | 0.0% | 0.0% | -16.5 | 0.00 | 0.00 | +5.1 | +7.8 |
| `tdi_rsi_gt_signal` | 22 | S_STRANGER | 84.6% | 13.6% | 13.6% | 9.1% | -12.4 | 0.13 | 0.76 | +7.3 | +9.9 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 19.2% | 20.0% | 20.0% | 0.0% | -2.1 | 0.68 | 2.73 | +5.6 | +9.8 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 88.5% | 13.0% | 13.0% | 8.7% | -9.0 | 0.16 | 1.02 | +7.9 | +9.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 19 | S_STRANGER | 73.1% | 15.8% | 15.8% | 10.5% | -7.4 | 0.22 | 1.10 | +7.9 | +9.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 88.5% | 13.0% | 13.0% | 8.7% | -9.0 | 0.16 | 1.02 | +7.9 | +9.7 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 11.5% | 11.5% | 7.7% | -13.0 | 0.10 | 0.77 | +7.4 | +9.9 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 26.9% | 0.0% | 0.0% | 14.3% | -6.2 | 0.00 | 0.00 | +6.8 | +9.3 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 11.5% | 0.0% | 0.0% | 0.0% | -8.0 | 0.00 | 0.00 | +0.8 | +11.5 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-2.8; validation N=9 Fav=22.2% Avg=+2.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 11.4% | 14.3% | 14.3% | -5.2 | 0.42 | 2.34 | +12.1 | +14.9 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 68.6% | 8.3% | 12.5% | 12.5% | -7.5 | 0.21 | 1.31 | +10.1 | +16.3 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 77.1% | 7.4% | 11.1% | 11.1% | -7.1 | 0.20 | 1.45 | +9.7 | +15.3 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 80.0% | 7.1% | 10.7% | 10.7% | -7.9 | 0.17 | 1.34 | +9.9 | +15.4 |
| `asian_range_gte_30` | 29 | S_STRANGER | 82.9% | 13.8% | 17.2% | 17.2% | -3.0 | 0.60 | 2.64 | +12.8 | +12.9 |
| `confluence_gte_60` | 12 | S_STRANGER | 34.3% | 16.7% | 25.0% | 16.7% | +1.4 | 1.55 | 4.64 | +10.7 | +12.8 |
| `confluence_gte_70` | 2 | S_STRANGER | 5.7% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +4.1 | +25.7 |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 65.7% | 13.0% | 13.0% | 17.4% | -7.2 | 0.34 | 2.18 | +12.0 | +16.4 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 48.6% | 0.0% | 0.0% | 0.0% | -9.3 | 0.00 | 0.00 | +6.9 | +18.4 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 60.0% | 9.5% | 14.3% | 14.3% | -5.7 | 0.28 | 1.49 | +10.1 | +14.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 42.9% | 13.3% | 13.3% | 20.0% | -7.2 | 0.26 | 1.56 | +11.4 | +15.0 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 2.9% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +14.6 | +4.9 |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 80.0% | 7.1% | 10.7% | 10.7% | -7.9 | 0.17 | 1.34 | +9.9 | +15.4 |
| `feature_stale_hod_exhaustion_reject` | 35 | S_STRANGER | 100.0% | 11.4% | 14.3% | 14.3% | -5.2 | 0.42 | 2.34 | +12.1 | +14.9 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 20.0% | 0.0% | 0.0% | 14.3% | -5.5 | 0.00 | 0.00 | +8.2 | +15.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.9% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +4.2 | +6.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-2.8; validation N=5 Fav=40.0% Avg=+0.2; out_of_sample N=8 Fav=12.5% Avg=-5.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 9.4% | 9.4% | 15.6% | -11.5 | 0.06 | 0.52 | +7.6 | +10.2 |
| `hunt_to_ar_ratio_le_2_0` | 28 | S_STRANGER | 87.5% | 10.7% | 10.7% | 17.9% | -9.6 | 0.08 | 0.60 | +7.8 | +9.8 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 96.9% | 9.7% | 9.7% | 16.1% | -11.4 | 0.06 | 0.52 | +7.3 | +9.9 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 87.5% | 10.7% | 10.7% | 17.9% | -9.6 | 0.08 | 0.60 | +7.8 | +9.8 |
| `asian_range_gte_30` | 29 | S_STRANGER | 90.6% | 10.3% | 10.3% | 17.2% | -12.5 | 0.06 | 0.47 | +8.0 | +10.5 |
| `confluence_gte_60` | 27 | S_STRANGER | 84.4% | 11.1% | 11.1% | 14.8% | -13.0 | 0.06 | 0.46 | +8.0 | +10.6 |
| `confluence_gte_70` | 7 | S_STRANGER | 21.9% | 0.0% | 0.0% | 0.0% | -18.0 | 0.00 | 0.00 | +5.3 | +4.6 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 62.5% | 5.0% | 5.0% | 10.0% | -14.7 | 0.03 | 0.62 | +6.3 | +11.5 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 50.0% | 18.8% | 18.8% | 25.0% | -3.1 | 0.32 | 1.27 | +8.7 | +9.8 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 78.1% | 12.0% | 12.0% | 20.0% | -10.5 | 0.08 | 0.53 | +8.4 | +10.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 40.6% | 7.7% | 7.7% | 15.4% | -14.2 | 0.05 | 0.59 | +7.2 | +12.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 87.5% | 10.7% | 10.7% | 17.9% | -9.6 | 0.08 | 0.60 | +7.8 | +9.8 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 9.4% | 9.4% | 15.6% | -11.5 | 0.06 | 0.52 | +7.6 | +10.2 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 21.9% | 14.3% | 14.3% | 28.6% | -2.4 | 0.25 | 1.27 | +8.1 | +7.7 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 12.5% | 25.0% | 25.0% | 25.0% | -1.1 | 0.56 | 1.68 | +9.2 | +7.1 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+1.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-1.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 27.3% | -2.3 | 0.43 | 3.47 | +12.9 | +8.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 20.0% | -2.6 | 0.43 | 3.47 | +12.7 | +9.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 20.0% | -2.6 | 0.43 | 3.47 | +12.7 | +9.4 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 20.0% | -2.6 | 0.43 | 3.47 | +12.7 | +9.4 |
| `asian_range_gte_30` | 7 | S_STRANGER | 63.6% | 14.3% | 14.3% | 42.9% | +1.1 | 1.66 | 6.62 | +15.3 | +7.1 |
| `confluence_gte_60` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 16.7% | -4.7 | 0.00 | 0.00 | +11.8 | +8.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 25.0% | -2.7 | 0.47 | 2.85 | +12.6 | +9.8 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 11.1% | -2.9 | 0.43 | 3.47 | +12.5 | +10.1 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 54.5% | 16.7% | 16.7% | 33.3% | +1.3 | 1.66 | 6.62 | +15.4 | +7.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | +3.9 | 2.46 | 4.92 | +17.0 | +8.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 20.0% | -2.6 | 0.43 | 3.47 | +12.7 | +9.4 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 27.3% | -2.3 | 0.43 | 3.47 | +12.9 | +8.9 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 40.0% | -0.1 | 0.97 | 2.90 | +15.4 | +8.2 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 54.5% | 16.7% | 16.7% | 16.7% | -2.9 | 0.53 | 2.67 | +11.9 | +10.5 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-7.3; validation N=3 Fav=33.3% Avg=+7.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 18.2% | 9.1% | -5.3 | 0.27 | 1.20 | +14.8 | +12.9 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 72.7% | 12.5% | 25.0% | 12.5% | -2.3 | 0.54 | 1.61 | +16.4 | +12.1 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 72.7% | 12.5% | 25.0% | 12.5% | -2.3 | 0.54 | 1.61 | +16.4 | +12.1 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 72.7% | 12.5% | 25.0% | 12.5% | -2.3 | 0.54 | 1.61 | +16.4 | +12.1 |
| `asian_range_gte_30` | 8 | S_STRANGER | 72.7% | 12.5% | 25.0% | 12.5% | -4.1 | 0.39 | 1.18 | +14.6 | +9.5 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 18.2% | 9.1% | -5.3 | 0.27 | 1.20 | +14.8 | +12.9 |
| `confluence_gte_70` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 0.0% | -8.1 | 0.00 | 0.00 | +15.3 | +16.1 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -7.0 | 0.00 | 0.00 | +12.4 | +11.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 0.0% | -7.0 | 0.00 | 0.00 | +14.1 | +17.2 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 63.6% | 14.3% | 28.6% | 14.3% | -1.2 | 0.72 | 1.80 | +15.3 | +10.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -7.0 | 0.00 | 0.00 | +12.4 | +11.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 72.7% | 12.5% | 25.0% | 12.5% | -2.3 | 0.54 | 1.61 | +16.4 | +12.1 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 18.2% | 9.1% | -5.3 | 0.27 | 1.20 | +14.8 | +12.9 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 45.5% | 0.0% | 20.0% | 0.0% | -4.5 | 0.34 | 1.37 | +11.6 | +10.9 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -9.4 | 0.00 | 0.00 | +10.0 | +12.2 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=0.0% Avg=-7.1; validation N=1 Fav=0.0% Avg=-12.7; out_of_sample N=2 Fav=50.0% Avg=+4.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.7 | 0.17 | 1.74 | +9.1 | +13.1 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 9.1% | -5.6 | 0.19 | 1.71 | +9.9 | +12.5 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.7 | 0.17 | 1.74 | +9.1 | +13.1 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.7 | 0.17 | 1.74 | +9.1 | +13.1 |
| `asian_range_gte_30` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 9.1% | -5.6 | 0.19 | 1.71 | +9.9 | +12.5 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.7 | 0.17 | 1.74 | +9.1 | +13.1 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.7 | 0.17 | 1.74 | +9.1 | +13.1 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -8.5 | 0.00 | 0.00 | +8.5 | +11.3 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 9.1% | -5.7 | 0.19 | 1.70 | +9.8 | +13.6 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 9.1% | -5.6 | 0.19 | 1.71 | +9.9 | +12.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -8.5 | 0.00 | 0.00 | +8.5 | +11.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 9.1% | -5.6 | 0.19 | 1.71 | +9.9 | +12.5 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 83.3% | 10.0% | 10.0% | 10.0% | -5.5 | 0.21 | 1.67 | +10.5 | +12.6 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -9.8 | 0.00 | 0.00 | +4.2 | +14.9 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -7.3 | 0.00 | 0.00 | +6.8 | +13.2 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+13.8; validation N=2 Fav=0.0% Avg=-11.6; out_of_sample N=1 Fav=0.0% Avg=-43.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -7.7 | 0.34 | 3.75 | +16.2 | +14.9 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 0.0% | -8.5 | 0.41 | 2.89 | +21.0 | +16.2 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 0.0% | -8.5 | 0.41 | 2.89 | +21.0 | +16.2 |
| `stop_hunt_le_90` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -9.5 | 0.42 | 2.50 | +20.5 | +16.1 |
| `asian_range_gte_30` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 0.0% | -7.9 | 0.35 | 3.53 | +17.5 | +15.5 |
| `confluence_gte_60` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 0.0% | -5.1 | 0.51 | 4.08 | +17.0 | +15.6 |
| `confluence_gte_70` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -6.4 | 0.00 | 0.00 | +12.2 | +10.0 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 0.0% | -4.9 | 0.47 | 4.67 | +15.8 | +14.9 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 0.0% | -4.9 | 0.47 | 4.67 | +15.8 | +14.9 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -9.0 | 0.43 | 2.58 | +23.8 | +17.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 0.0% | -4.2 | 0.65 | 3.27 | +24.3 | +17.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -9.5 | 0.42 | 2.50 | +20.5 | +16.1 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -7.7 | 0.34 | 3.75 | +16.2 | +14.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -3.7 | 0.65 | 3.89 | +14.4 | +15.7 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-1.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=25.0% Avg=+3.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 15.4% | -4.6 | 0.24 | 1.07 | +7.4 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 15.4% | -4.6 | 0.24 | 1.07 | +7.4 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 15.4% | -4.6 | 0.24 | 1.07 | +7.4 | +5.0 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 15.4% | -4.6 | 0.24 | 1.07 | +7.4 | +5.0 |
| `asian_range_gte_30` | 12 | S_STRANGER | 92.3% | 8.3% | 16.7% | 16.7% | -4.5 | 0.26 | 1.03 | +7.7 | +4.6 |
| `confluence_gte_60` | 11 | S_STRANGER | 84.6% | 9.1% | 18.2% | 0.0% | -5.5 | 0.24 | 1.07 | +6.3 | +5.3 |
| `confluence_gte_70` | 8 | S_STRANGER | 61.5% | 12.5% | 25.0% | 0.0% | -6.2 | 0.27 | 0.82 | +5.7 | +5.4 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 61.5% | 0.0% | 12.5% | 12.5% | -6.7 | 0.02 | 0.13 | +6.0 | +6.0 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 46.2% | 16.7% | 33.3% | 0.0% | +1.4 | 1.82 | 3.63 | +8.8 | +6.7 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 92.3% | 8.3% | 16.7% | 16.7% | -4.5 | 0.26 | 1.03 | +7.7 | +4.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 61.5% | 0.0% | 12.5% | 12.5% | -6.7 | 0.02 | 0.13 | +6.0 | +6.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 15.4% | -4.6 | 0.24 | 1.07 | +7.4 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 15.4% | -4.6 | 0.24 | 1.07 | +7.4 | +5.0 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +13.3 | +3.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +10.2 | +2.4 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.5; validation N=4 Fav=25.0% Avg=+2.8; out_of_sample N=5 Fav=0.0% Avg=-6.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -2.6 | 0.39 | 2.33 | +7.9 | +11.5 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 93.3% | 7.1% | 14.3% | 7.1% | -2.3 | 0.44 | 2.41 | +8.0 | +11.4 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -2.6 | 0.39 | 2.33 | +7.9 | +11.5 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -2.6 | 0.39 | 2.33 | +7.9 | +11.5 |
| `asian_range_gte_30` | 14 | S_STRANGER | 93.3% | 7.1% | 14.3% | 7.1% | -2.7 | 0.40 | 2.19 | +8.3 | +11.8 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -2.6 | 0.39 | 2.33 | +7.9 | +11.5 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -2.6 | 0.39 | 2.33 | +7.9 | +11.5 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 80.0% | 8.3% | 8.3% | 0.0% | -2.9 | 0.36 | 3.97 | +8.7 | +12.6 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 80.0% | 8.3% | 8.3% | 0.0% | -2.9 | 0.36 | 3.97 | +8.7 | +12.6 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 86.7% | 7.7% | 15.4% | 7.7% | -2.3 | 0.45 | 2.25 | +8.4 | +11.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 66.7% | 10.0% | 10.0% | 0.0% | -2.6 | 0.43 | 3.88 | +9.4 | +13.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -2.6 | 0.39 | 2.33 | +7.9 | +11.5 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -2.6 | 0.39 | 2.33 | +7.9 | +11.5 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +1.8 | +10.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +1.8 | +10.6 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=-0.2; validation N=3 Fav=0.0% Avg=-12.0; out_of_sample N=1 Fav=0.0% Avg=-8.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -4.8 | 0.23 | 1.36 | +7.6 | +11.5 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -4.8 | 0.23 | 1.36 | +7.6 | +11.5 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -4.8 | 0.23 | 1.36 | +7.6 | +11.5 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 73.3% | 9.1% | 9.1% | 9.1% | -5.5 | 0.23 | 2.10 | +9.3 | +13.0 |
| `asian_range_gte_30` | 14 | S_STRANGER | 93.3% | 7.1% | 14.3% | 0.0% | -5.1 | 0.23 | 1.36 | +7.5 | +12.2 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -4.8 | 0.23 | 1.36 | +7.6 | +11.5 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -4.8 | 0.23 | 1.36 | +7.6 | +11.5 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -7.9 | 0.00 | 0.00 | +8.4 | +12.7 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 60.0% | 11.1% | 11.1% | 0.0% | -5.1 | 0.29 | 2.29 | +9.9 | +13.6 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 93.3% | 7.1% | 14.3% | 0.0% | -5.1 | 0.23 | 1.36 | +7.5 | +12.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -7.9 | 0.00 | 0.00 | +8.4 | +12.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 73.3% | 9.1% | 9.1% | 9.1% | -5.5 | 0.23 | 2.10 | +9.3 | +13.0 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -4.8 | 0.23 | 1.36 | +7.6 | +11.5 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -9.2 | 0.00 | 0.00 | +4.3 | +13.5 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 0.0% | -8.7 | 0.00 | 0.00 | +5.6 | +13.8 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-1.6; validation N=3 Fav=0.0% Avg=-12.1; out_of_sample N=3 Fav=33.3% Avg=-8.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 13.3% | -8.2 | 0.09 | 1.15 | +10.3 | +13.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 86.7% | 7.7% | 7.7% | 15.4% | -8.5 | 0.10 | 1.07 | +10.6 | +13.9 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 13.3% | -8.2 | 0.09 | 1.15 | +10.3 | +13.1 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 93.3% | 0.0% | 0.0% | 7.1% | -9.6 | 0.00 | 0.00 | +8.5 | +13.6 |
| `asian_range_gte_30` | 13 | S_STRANGER | 86.7% | 7.7% | 7.7% | 15.4% | -8.0 | 0.10 | 1.13 | +10.8 | +12.9 |
| `confluence_gte_60` | 13 | S_STRANGER | 86.7% | 7.7% | 7.7% | 15.4% | -7.6 | 0.11 | 1.19 | +11.0 | +12.4 |
| `confluence_gte_70` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -9.4 | 0.00 | 0.00 | +7.1 | +14.8 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 0.0% | -15.1 | 0.00 | 0.00 | +6.5 | +20.7 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 66.7% | 10.0% | 10.0% | 20.0% | -6.7 | 0.15 | 1.20 | +11.7 | +12.1 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 73.3% | 9.1% | 9.1% | 18.2% | -8.3 | 0.12 | 1.04 | +11.2 | +13.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 0.0% | -15.1 | 0.00 | 0.00 | +6.5 | +20.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 93.3% | 0.0% | 0.0% | 7.1% | -9.6 | 0.00 | 0.00 | +8.5 | +13.6 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 13.3% | -8.2 | 0.09 | 1.15 | +10.3 | +13.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 33.3% | -0.6 | 0.00 | 0.00 | +13.0 | +4.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 50.0% | -0.2 | 0.00 | 0.00 | +15.9 | +3.8 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=+5.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=0.0% Avg=-10.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 5.9% | -6.0 | 0.28 | 1.23 | +7.5 | +9.5 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 5.9% | -6.0 | 0.28 | 1.23 | +7.5 | +9.5 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 5.9% | -6.0 | 0.28 | 1.23 | +7.5 | +9.5 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 5.9% | -6.0 | 0.28 | 1.23 | +7.5 | +9.5 |
| `asian_range_gte_30` | 15 | S_STRANGER | 88.2% | 6.7% | 20.0% | 6.7% | -4.8 | 0.36 | 1.30 | +7.4 | +7.0 |
| `confluence_gte_60` | 13 | S_STRANGER | 76.5% | 7.7% | 23.1% | 7.7% | -6.0 | 0.34 | 1.13 | +5.9 | +8.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 64.7% | 9.1% | 18.2% | 9.1% | -4.6 | 0.34 | 1.36 | +7.8 | +6.9 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 47.1% | 0.0% | 12.5% | 0.0% | -7.2 | 0.03 | 0.18 | +7.0 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 88.2% | 6.7% | 20.0% | 6.7% | -4.8 | 0.36 | 1.30 | +7.4 | +7.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 64.7% | 9.1% | 18.2% | 9.1% | -4.6 | 0.34 | 1.36 | +7.8 | +6.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 5.9% | -6.0 | 0.28 | 1.23 | +7.5 | +9.5 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 5.9% | -6.0 | 0.28 | 1.23 | +7.5 | +9.5 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 5.9% | 100.0% | 100.0% | 100.0% | +24.5 | 999.00 | 999.00 | +26.3 | +1.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -0.4 | 0.00 | 0.00 | +13.0 | +3.6 |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
