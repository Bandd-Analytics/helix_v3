# EURUSD Pair Feature Ablation

Generated: 2026-06-09T15:36:10.938500+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 17 | R_REPEATER | 52.9% | +3.0 | `tdi_rsi_gte_50` | 11 | R_REPEATER | 63.6% | +5.9 | 8.04 | 4.59 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | R_REPEATER | 52.6% | +8.3 | `tdi_rsi_gt_signal` | 8 | R_REPEATER | 62.5% | +11.7 | 5.38 | 3.23 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 12 | R_REPEATER | 50.0% | +8.8 | `hunt_to_ar_ratio_le_2_0` | 5 | R_REPEATER | 60.0% | +8.7 | 4.72 | 3.15 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 46.7% | +5.7 | `tdi_rsi_gte_50` | 10 | R_REPEATER | 60.0% | +10.9 | 3.73 | 2.49 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 44.4% | +4.5 | `asian_range_gte_30` | 7 | R_REPEATER | 57.1% | +8.1 | 9.49 | 4.74 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 42.1% | +4.3 | `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 60.0% | +7.3 | 5.77 | 3.85 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 41.7% | +7.9 | `confluence_gte_60` | 7 | R_REPEATER | 71.4% | +15.7 | 62.08 | 24.83 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 41.7% | +6.5 | `hunt_to_ar_ratio_le_2_0` | 7 | R_REPEATER | 57.1% | +9.2 | 39.00 | 19.50 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 40.0% | +4.6 | `all` | 10 | S_STRANGER | 40.0% | +4.6 | 7.12 | 8.90 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 40.0% | +3.7 | `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 44.4% | +4.2 | 5.59 | 5.59 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 40.0% | +2.3 | `feature_extreme_hunt_with_exception` | 6 | R_REPEATER | 50.0% | +5.3 | 2.76 | 2.76 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 13 | S_STRANGER | 38.5% | -7.7 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 42.9% | +1.4 | 1.38 | 1.84 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 37.5% | +6.7 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 60.0% | +15.9 | 11.30 | 7.53 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 36.4% | +4.3 | `all` | 11 | S_STRANGER | 36.4% | +4.3 | 4.10 | 4.92 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 35.7% | +7.2 | `tdi_rsi_gte_50` | 9 | R_REPEATER | 55.6% | +12.7 | 7.65 | 6.12 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | S_STRANGER | 35.3% | +0.4 | `all` | 17 | S_STRANGER | 35.3% | +0.4 | 1.15 | 1.53 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 35.0% | +3.3 | `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 50.0% | +10.2 | 18.06 | 18.06 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 29 | S_STRANGER | 34.5% | +0.8 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 60.0% | +1.3 | 1.43 | 0.95 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 15 | S_STRANGER | 33.3% | +4.3 | `feature_momentum_breakout_exception` | 9 | S_STRANGER | 44.4% | +8.1 | 8.90 | 8.90 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | +1.4 | `confluence_gte_70` | 5 | R_RUNNER | 80.0% | +9.0 | 15.44 | 3.86 | 1 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | +1.0 | `confluence_gte_70` | 5 | R_RUNNER | 80.0% | +10.2 | 5.28 | 1.32 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 30.8% | +1.2 | `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 33.3% | +1.3 | 1.53 | 2.68 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | +4.6 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 33.3% | +6.0 | 5.03 | 6.71 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 30.0% | +0.8 | `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 44.4% | +1.1 | 1.45 | 1.45 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 20 | S_STRANGER | 30.0% | -0.2 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 41.7% | +1.7 | 1.37 | 1.92 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | -0.3 | `all` | 10 | S_STRANGER | 30.0% | -0.3 | 0.94 | 2.20 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 51 | S_STRANGER | 29.4% | -3.4 | `confluence_gte_70` | 10 | S_STRANGER | 40.0% | +1.1 | 1.28 | 1.92 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 55 | S_STRANGER | 29.1% | -0.0 | `confluence_gte_60` | 26 | S_STRANGER | 38.5% | +1.0 | 1.39 | 1.81 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 38 | S_STRANGER | 28.9% | +0.5 | `tdi_rsi_gte_50` | 18 | R_REPEATER | 50.0% | +6.0 | 3.77 | 3.77 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 28.6% | -0.9 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 50.0% | +3.6 | 4.37 | 2.91 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 14 | S_STRANGER | 28.6% | -2.2 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 44.4% | +4.4 | 2.18 | 2.72 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 25 | S_STRANGER | 28.0% | +2.6 | `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 33.3% | +4.1 | 2.49 | 4.99 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 27.8% | +0.3 | `tdi_rsi_gt_signal` | 8 | R_REPEATER | 50.0% | +2.4 | 4.02 | 3.01 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 22 | S_STRANGER | 27.3% | +2.8 | `tdi_rsi_gte_50` | 15 | S_STRANGER | 40.0% | +6.3 | 3.78 | 5.67 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 22 | S_STRANGER | 27.3% | +2.5 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 37.5% | +4.5 | 3.79 | 6.32 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | -1.0 | `all` | 11 | S_STRANGER | 27.3% | -1.0 | 0.73 | 1.71 | 0 | 1 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | -1.4 | `asian_range_gte_30` | 5 | S_STRANGER | 40.0% | +0.3 | 1.17 | 1.76 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 11 | S_STRANGER | 27.3% | -6.9 | `asian_range_gte_30` | 6 | R_REPEATER | 50.0% | +5.2 | 2.85 | 2.85 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 26 | S_STRANGER | 26.9% | -0.7 | `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 28.0% | -0.6 | 0.84 | 2.16 | 0 | 1 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 26.7% | +1.6 | `tdi_rsi_gt_signal` | 5 | R_REPEATER | 60.0% | +9.9 | 8.96 | 5.97 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 15 | S_STRANGER | 26.7% | -1.4 | `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 40.0% | +0.1 | 1.04 | 0.69 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 19 | S_STRANGER | 26.3% | +2.1 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 33.3% | +2.8 | 2.71 | 5.41 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 26.1% | +0.9 | `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 28.6% | +2.0 | 1.43 | 2.85 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 25.0% | +3.2 | `tdi_rsi_gt_signal` | 12 | S_STRANGER | 33.3% | +7.3 | 3.19 | 4.78 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | +2.4 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 40.0% | +5.2 | 2.79 | 4.19 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 25.0% | +0.5 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 30.0% | +3.1 | 2.40 | 5.59 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 25.0% | -0.0 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 20.0% | +1.3 | 1.58 | 6.33 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 25.0% | -0.2 | `all` | 24 | S_STRANGER | 25.0% | -0.2 | 0.96 | 2.41 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 25.0% | -0.4 | `tdi_rsi_gte_50` | 17 | S_STRANGER | 23.5% | +0.7 | 1.19 | 3.57 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | -3.2 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 60.0% | +6.7 | 19.47 | 6.49 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 21 | S_STRANGER | 23.8% | -2.2 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 40.0% | -1.0 | 0.74 | 1.12 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 17 | S_STRANGER | 23.5% | +0.2 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 40.0% | +2.7 | 2.98 | 4.47 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 23.5% | -0.9 | `all` | 17 | S_STRANGER | 23.5% | -0.9 | 0.76 | 2.46 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 30 | S_STRANGER | 23.3% | -2.4 | `confluence_gte_60` | 9 | S_STRANGER | 33.3% | -2.0 | 0.27 | 0.53 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 13 | S_STRANGER | 23.1% | +2.8 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 50.0% | +8.0 | 4.86 | 4.86 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 23.1% | +1.7 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 33.3% | +3.1 | 3.92 | 3.92 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 23.1% | -1.0 | `asian_range_gte_30` | 5 | S_STRANGER | 20.0% | +0.8 | 1.31 | 2.61 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 23.1% | -5.9 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 40.0% | -2.8 | 0.46 | 0.69 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 35 | S_STRANGER | 22.9% | -3.4 | `tdi_rsi_gte_50` | 14 | S_STRANGER | 42.9% | -0.8 | 0.83 | 1.11 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 57 | S_STRANGER | 22.8% | +0.3 | `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 30.0% | +1.8 | 1.54 | 3.07 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 31 | S_STRANGER | 22.6% | -0.4 | `confluence_gte_70` | 7 | S_STRANGER | 28.6% | +4.1 | 5.82 | 5.82 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 23 | S_STRANGER | 21.7% | -0.0 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 42.9% | +1.5 | 1.29 | 1.71 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 37 | S_STRANGER | 21.6% | -3.9 | `hunt_to_ar_ratio_le_2_0` | 8 | R_REPEATER | 50.0% | -2.2 | 0.27 | 0.27 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 28 | S_STRANGER | 21.4% | -1.5 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 16.7% | +0.5 | 1.42 | 4.26 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 33 | S_STRANGER | 21.2% | -0.6 | `confluence_gte_60` | 12 | S_STRANGER | 33.3% | +0.9 | 1.35 | 1.62 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 44 | S_STRANGER | 20.5% | -2.5 | `tdi_rsi_gt_signal` | 23 | S_STRANGER | 30.4% | -1.7 | 0.59 | 1.26 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 20.0% | +1.4 | `tdi_rsi_gt_signal` | 12 | S_STRANGER | 25.0% | +3.6 | 3.00 | 6.01 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | +0.7 | `asian_range_gte_30` | 9 | S_STRANGER | 22.2% | +0.7 | 1.14 | 2.29 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 15 | S_STRANGER | 20.0% | +0.4 | `feature_momentum_breakout_exception` | 6 | S_STRANGER | 33.3% | +3.6 | 1.74 | 2.61 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 25 | S_STRANGER | 20.0% | -1.6 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 44.4% | +1.4 | 1.77 | 2.21 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 30 | S_STRANGER | 20.0% | -1.7 | `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 27.3% | -0.1 | 0.98 | 2.62 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -4.0 | `all` | 10 | S_STRANGER | 20.0% | -4.0 | 0.38 | 0.89 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -14.2 | `asian_range_gte_30` | 7 | S_STRANGER | 28.6% | -14.6 | 0.24 | 0.32 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 26 | S_STRANGER | 19.2% | -0.2 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 36.4% | +2.3 | 2.24 | 3.92 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 26 | S_STRANGER | 19.2% | -2.0 | `feature_momentum_breakout_exception` | 6 | S_STRANGER | 33.3% | +4.0 | 5.25 | 7.87 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 32 | S_STRANGER | 18.8% | +0.3 | `confluence_gte_70` | 7 | S_STRANGER | 28.6% | +2.1 | 1.67 | 3.34 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 18.8% | -2.5 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | +0.5 | 1.22 | 2.43 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 18.8% | -4.1 | `asian_range_gte_30` | 7 | S_STRANGER | 28.6% | -3.0 | 0.50 | 1.25 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 71 | S_STRANGER | 18.3% | -2.5 | `tdi_rsi_gte_50` | 36 | S_STRANGER | 27.8% | +1.6 | 1.41 | 3.08 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | +0.2 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | +4.0 | 6.79 | 13.57 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -2.4 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 20.0% | -1.8 | 0.33 | 0.33 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -3.3 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 40.0% | -0.6 | 0.79 | 1.18 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 28 | S_STRANGER | 17.9% | -3.1 | `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 18.5% | -3.1 | 0.43 | 1.10 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 28 | S_STRANGER | 17.9% | -6.8 | `hunt_to_ar_ratio_le_2_0` | 27 | S_STRANGER | 18.5% | -7.0 | 0.20 | 0.48 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 17 | S_STRANGER | 17.6% | +1.3 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | +8.7 | 2.83 | 5.67 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 17 | S_STRANGER | 17.6% | -2.3 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 22.2% | -2.8 | 0.52 | 1.55 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 86 | S_STRANGER | 17.4% | -3.1 | `confluence_gte_70` | 19 | S_STRANGER | 26.3% | -0.9 | 0.82 | 2.31 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 83 | S_STRANGER | 16.9% | -8.0 | `confluence_gte_70` | 18 | S_STRANGER | 33.3% | +1.8 | 1.44 | 2.16 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 16.7% | +0.7 | `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 33.3% | +4.0 | 2.44 | 4.88 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -1.2 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 20.0% | -0.3 | 0.92 | 3.69 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 24 | S_STRANGER | 16.7% | -2.4 | `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 23.1% | +0.1 | 1.04 | 3.11 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 18 | S_STRANGER | 16.7% | -2.9 | `all` | 18 | S_STRANGER | 16.7% | -2.9 | 0.39 | 1.94 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 42 | S_STRANGER | 16.7% | -3.3 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 31.2% | +2.4 | 1.99 | 4.38 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 42 | S_STRANGER | 16.7% | -4.7 | `feature_momentum_breakout_exception` | 12 | S_STRANGER | 25.0% | -0.4 | 0.86 | 2.01 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 19 | S_STRANGER | 15.8% | -7.3 | `confluence_gte_60` | 6 | S_STRANGER | 33.3% | -2.1 | 0.63 | 0.95 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 32 | S_STRANGER | 15.6% | -1.1 | `tdi_rsi_gte_50` | 26 | S_STRANGER | 19.2% | -0.5 | 0.85 | 3.55 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -1.9 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 25.0% | -1.5 | 0.67 | 2.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 15.4% | -2.4 | `tdi_rsi_gt_signal` | 12 | S_STRANGER | 16.7% | -2.6 | 0.38 | 1.88 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 15.4% | -5.7 | `asian_range_gte_30` | 6 | S_STRANGER | 16.7% | -4.9 | 0.44 | 2.20 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 15.0% | -0.2 | `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 28.6% | +2.2 | 3.18 | 6.37 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | +2.5 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 20.0% | +2.3 | 1.65 | 6.58 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | +2.3 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 33.3% | +9.4 | 3.22 | 3.22 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -0.0 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 22.2% | +1.2 | 2.57 | 6.43 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -1.6 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 20.0% | +2.0 | 1.90 | 3.79 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 14.3% | -3.3 | `asian_range_gte_30` | 10 | S_STRANGER | 20.0% | -1.2 | 0.53 | 1.86 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 21 | S_STRANGER | 14.3% | -3.5 | `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 18.8% | -4.0 | 0.39 | 1.55 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 21 | S_STRANGER | 14.3% | -14.1 | `tdi_rsi_gt_signal` | 14 | S_STRANGER | 14.3% | -9.9 | 0.14 | 0.50 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 22 | S_STRANGER | 13.6% | -0.8 | `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 40.0% | +1.9 | 4.17 | 4.17 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 30 | S_STRANGER | 13.3% | -1.7 | `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 20.0% | -3.0 | 0.45 | 1.05 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 45 | S_STRANGER | 13.3% | -3.9 | `tdi_rsi_gte_50` | 13 | S_STRANGER | 23.1% | -1.8 | 0.50 | 1.65 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 38 | S_STRANGER | 13.2% | -7.4 | `tdi_rsi_gte_50` | 14 | S_STRANGER | 21.4% | -0.6 | 0.82 | 3.00 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 23 | S_STRANGER | 13.0% | -4.0 | `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 20.0% | -1.9 | 0.60 | 1.49 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 16 | S_STRANGER | 12.5% | -0.1 | `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 33.3% | +4.0 | 8.27 | 5.52 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 12.5% | -3.2 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 20.0% | -2.8 | 0.41 | 1.63 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 32 | S_STRANGER | 12.5% | -3.7 | `confluence_gte_60` | 18 | S_STRANGER | 16.7% | -3.4 | 0.31 | 1.46 | 0 | 1 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 12.5% | -5.1 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 14.3% | -7.0 | 0.43 | 2.59 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 32 | S_STRANGER | 12.5% | -7.2 | `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 20.0% | -3.6 | 0.32 | 0.88 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 12.5% | -8.4 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 14.3% | -2.7 | 0.57 | 2.87 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 16 | S_STRANGER | 12.5% | -9.7 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 20.0% | -0.8 | 0.28 | 0.55 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 24 | S_STRANGER | 12.5% | -14.1 | `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 14.3% | -9.5 | 0.13 | 0.74 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 33 | S_STRANGER | 12.1% | -2.9 | `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 13.3% | -4.8 | 0.20 | 0.80 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 33 | S_STRANGER | 12.1% | -5.5 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 16.7% | +0.7 | 1.44 | 7.19 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 11.8% | -4.5 | `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 15.4% | -4.1 | 0.38 | 1.15 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 43 | S_STRANGER | 11.6% | -3.9 | `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 17.4% | -4.7 | 0.32 | 1.29 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 10.5% | -1.6 | `asian_range_gte_30` | 11 | S_STRANGER | 18.2% | -0.6 | 0.86 | 2.01 | 0 | 1 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -0.2 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 16.7% | +1.5 | 1.32 | 6.59 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 10.0% | -2.6 | `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 25.0% | -1.7 | 0.69 | 1.16 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 10.0% | -2.7 | `all` | 10 | S_STRANGER | 10.0% | -2.7 | 0.37 | 2.94 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -5.7 | `asian_range_gte_30` | 6 | S_STRANGER | 16.7% | -4.7 | 0.45 | 0.89 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 10.0% | -8.5 | `all` | 10 | S_STRANGER | 10.0% | -8.5 | 0.16 | 0.63 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 11 | S_STRANGER | 9.1% | -0.7 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 20.0% | +0.8 | 1.67 | 6.67 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 9.1% | -1.7 | `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 20.0% | -1.9 | 0.26 | 1.05 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 22 | S_STRANGER | 9.1% | -2.1 | `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 9.5% | -2.2 | 0.43 | 3.67 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -2.4 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 16.7% | -1.4 | 0.58 | 2.92 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -4.5 | `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 12.5% | -3.3 | 0.44 | 3.11 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 8.3% | -0.8 | `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 11.1% | +0.0 | 1.01 | 6.07 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 8.3% | -3.5 | `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 11.1% | -2.6 | 0.42 | 2.96 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 8.3% | -4.8 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 16.7% | -1.9 | 0.56 | 2.23 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 24 | S_STRANGER | 8.3% | -9.0 | `confluence_gte_60` | 11 | S_STRANGER | 18.2% | -7.7 | 0.22 | 0.76 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 12 | S_STRANGER | 8.3% | -10.5 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 14.3% | -2.9 | 0.49 | 2.94 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 37 | S_STRANGER | 8.1% | -5.1 | `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 16.7% | -1.3 | 0.40 | 1.61 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 25 | S_STRANGER | 8.0% | -9.9 | `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 8.3% | -9.5 | 0.09 | 0.99 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 7.7% | -8.7 | `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 16.7% | -5.0 | 0.45 | 2.24 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 7.7% | -9.4 | `tdi_rsi_gt_signal` | 11 | S_STRANGER | 9.1% | -5.4 | 0.37 | 3.67 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 29 | S_STRANGER | 6.9% | -4.7 | `feature_momentum_breakout_exception` | 10 | S_STRANGER | 10.0% | -1.4 | 0.51 | 1.77 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 15 | S_STRANGER | 6.7% | -5.6 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 9.1% | -7.2 | 0.06 | 0.55 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 6.7% | -6.3 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 14.3% | -6.8 | 0.10 | 0.60 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 6.2% | -2.8 | `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 20.0% | +1.3 | 1.22 | 4.88 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 13 | S_STRANGER | 0.0% | -2.2 | `feature_momentum_breakout_exception` | 9 | S_STRANGER | 0.0% | -1.8 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 0.0% | -2.4 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 0.0% | -2.0 | 0.22 | 1.31 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 0.0% | -3.6 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 0.0% | -2.8 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -4.1 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 0.0% | -3.7 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 11 | S_STRANGER | 0.0% | -4.6 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 0.0% | -2.8 | 0.22 | 1.09 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 13 | S_STRANGER | 0.0% | -5.9 | `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 0.0% | -5.5 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 13 | S_STRANGER | 0.0% | -6.6 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 0.0% | -5.6 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -8.6 | `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 0.0% | -3.0 | 0.24 | 0.98 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74` | 11 | S_STRANGER | 0.0% | -9.6 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 0.0% | -4.7 | 0.18 | 0.74 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -11.1 | `all` | 10 | S_STRANGER | 0.0% | -11.1 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 0.0% | -11.4 | `all` | 14 | S_STRANGER | 0.0% | -11.4 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74` | 11 | S_STRANGER | 0.0% | -13.9 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 0.0% | -10.1 | 0.00 | 0.00 | 0 | 0 | fail |

## Candidate Details

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=66.7% Avg=+6.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=50.0% Avg=+3.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | R_REPEATER | 100.0% | 52.9% | 58.8% | 29.4% | +3.0 | 2.40 | 1.68 | +13.4 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 7 | R_REPEATER | 41.2% | 57.1% | 71.4% | 28.6% | +4.5 | 4.88 | 1.95 | +16.1 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 11 | R_REPEATER | 64.7% | 54.5% | 63.6% | 27.3% | +1.7 | 1.56 | 0.89 | +13.1 | +3.5 |
| `stop_hunt_le_90` | 17 | R_REPEATER | 100.0% | 52.9% | 58.8% | 29.4% | +3.0 | 2.40 | 1.68 | +13.4 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | R_REPEATER | 82.4% | 50.0% | 57.1% | 28.6% | +2.9 | 2.09 | 1.57 | +14.2 | +4.0 |
| `confluence_gte_70` | 3 | R_REPEATER | 17.6% | 66.7% | 66.7% | 33.3% | +5.4 | 3.01 | 1.51 | +23.4 | +3.6 |
| `tdi_rsi_gt_signal` | 16 | R_REPEATER | 94.1% | 56.2% | 62.5% | 31.2% | +3.4 | 2.60 | 1.56 | +14.0 | +3.9 |
| `tdi_rsi_gte_50` | 11 | R_REPEATER | 64.7% | 63.6% | 63.6% | 36.4% | +5.9 | 8.04 | 4.59 | +17.4 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 2 | R_RUNNER | 11.8% | 100.0% | 100.0% | 50.0% | +11.3 | 999.00 | 999.00 | +16.3 | +5.7 |
| `feature_extreme_hunt_with_exception` | 16 | R_REPEATER | 94.1% | 50.0% | 56.2% | 25.0% | +2.1 | 1.92 | 1.49 | +12.7 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 17 | R_REPEATER | 100.0% | 52.9% | 58.8% | 29.4% | +3.0 | 2.40 | 1.68 | +13.4 | +3.8 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 5.9% | 100.0% | 100.0% | 100.0% | +15.0 | 999.00 | 999.00 | +17.8 | +11.0 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_RUNNER | 23.5% | 100.0% | 100.0% | 50.0% | +10.5 | 999.00 | 999.00 | +16.7 | +4.1 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=62.5% Avg=+11.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | R_REPEATER | 100.0% | 52.6% | 57.9% | 31.6% | +8.3 | 4.71 | 3.42 | +15.5 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 18 | R_REPEATER | 94.7% | 55.6% | 61.1% | 33.3% | +8.9 | 5.15 | 3.27 | +16.2 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 19 | R_REPEATER | 100.0% | 52.6% | 57.9% | 31.6% | +8.3 | 4.71 | 3.42 | +15.5 | +5.6 |
| `stop_hunt_le_90` | 19 | R_REPEATER | 100.0% | 52.6% | 57.9% | 31.6% | +8.3 | 4.71 | 3.42 | +15.5 | +5.6 |
| `asian_range_gte_30` | 7 | R_REPEATER | 36.8% | 57.1% | 57.1% | 28.6% | +8.5 | 5.99 | 4.49 | +17.8 | +4.1 |
| `confluence_gte_60` | 19 | R_REPEATER | 100.0% | 52.6% | 57.9% | 31.6% | +8.3 | 4.71 | 3.42 | +15.5 | +5.6 |
| `confluence_gte_70` | 19 | R_REPEATER | 100.0% | 52.6% | 57.9% | 31.6% | +8.3 | 4.71 | 3.42 | +15.5 | +5.6 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 42.1% | 62.5% | 62.5% | 50.0% | +11.7 | 5.38 | 3.23 | +18.6 | +5.9 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 63.2% | 33.3% | 33.3% | 25.0% | +4.8 | 2.37 | 4.74 | +11.8 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 7 | R_REPEATER | 36.8% | 57.1% | 57.1% | 28.6% | +8.5 | 5.99 | 4.49 | +17.8 | +4.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 10.5% | 50.0% | 50.0% | 50.0% | +14.1 | 17.65 | 17.65 | +20.6 | +4.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | R_REPEATER | 100.0% | 52.6% | 57.9% | 31.6% | +8.3 | 4.71 | 3.42 | +15.5 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 19 | R_REPEATER | 100.0% | 52.6% | 57.9% | 31.6% | +8.3 | 4.71 | 3.42 | +15.5 | +5.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=100.0% Avg=+18.7; validation N=3 Fav=33.3% Avg=+2.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 50.0% | +8.8 | 6.18 | 5.15 | +16.6 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 5 | R_REPEATER | 41.7% | 60.0% | 60.0% | 40.0% | +8.7 | 4.72 | 3.15 | +16.4 | +5.3 |
| `hunt_to_ar_ratio_le_2_5` | 8 | R_REPEATER | 66.7% | 50.0% | 50.0% | 50.0% | +9.5 | 5.72 | 4.29 | +17.5 | +4.8 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 50.0% | +8.8 | 6.18 | 5.15 | +16.6 | +5.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 50.0% | +8.8 | 6.18 | 5.15 | +16.6 | +5.0 |
| `confluence_gte_70` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 50.0% | +8.8 | 6.18 | 5.15 | +16.6 | +5.0 |
| `tdi_rsi_gt_signal` | 11 | R_REPEATER | 91.7% | 54.5% | 54.5% | 45.5% | +9.6 | 6.18 | 5.15 | +16.8 | +5.3 |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 66.7% | 50.0% | 50.0% | 50.0% | +11.8 | 10.71 | 10.71 | +17.2 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 50.0% | +8.8 | 6.18 | 5.15 | +16.6 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 50.0% | +8.8 | 6.18 | 5.15 | +16.6 | +5.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=60.0% Avg=+3.3; validation N=5 Fav=60.0% Avg=+18.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 46.7% | 53.3% | 33.3% | +5.7 | 2.18 | 1.91 | +15.0 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 13 | R_REPEATER | 86.7% | 53.8% | 61.5% | 38.5% | +8.1 | 3.03 | 1.89 | +16.6 | +5.9 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 46.7% | 53.3% | 33.3% | +5.7 | 2.18 | 1.91 | +15.0 | +6.7 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 46.7% | 53.3% | 33.3% | +5.7 | 2.18 | 1.91 | +15.0 | +6.7 |
| `asian_range_gte_30` | 7 | R_REPEATER | 46.7% | 57.1% | 71.4% | 42.9% | +9.6 | 6.57 | 2.63 | +16.6 | +4.9 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 46.7% | 53.3% | 33.3% | +5.7 | 2.18 | 1.91 | +15.0 | +6.7 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 46.7% | 53.3% | 33.3% | +5.7 | 2.18 | 1.91 | +15.0 | +6.7 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 100.0% | 46.7% | 53.3% | 33.3% | +5.7 | 2.18 | 1.91 | +15.0 | +6.7 |
| `tdi_rsi_gte_50` | 10 | R_REPEATER | 66.7% | 60.0% | 60.0% | 40.0% | +10.9 | 3.73 | 2.49 | +20.4 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 7 | R_REPEATER | 46.7% | 57.1% | 71.4% | 42.9% | +9.6 | 6.57 | 2.63 | +16.6 | +4.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | R_REPEATER | 46.7% | 57.1% | 71.4% | 42.9% | +9.6 | 6.57 | 2.63 | +16.6 | +4.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 46.7% | 53.3% | 33.3% | +5.7 | 2.18 | 1.91 | +15.0 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 46.7% | 53.3% | 33.3% | +5.7 | 2.18 | 1.91 | +15.0 | +6.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=66.7% Avg=+3.8; validation N=4 Fav=50.0% Avg=+11.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 50.0% | +4.5 | 3.51 | 3.07 | +11.2 | +4.0 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 50.0% | +4.5 | 3.51 | 3.07 | +11.2 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 50.0% | +4.5 | 3.51 | 3.07 | +11.2 | +4.0 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 50.0% | +4.5 | 3.51 | 3.07 | +11.2 | +4.0 |
| `asian_range_gte_30` | 7 | R_REPEATER | 38.9% | 57.1% | 57.1% | 71.4% | +8.1 | 9.49 | 4.74 | +13.4 | +3.1 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 50.0% | +4.5 | 3.51 | 3.07 | +11.2 | +4.0 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 50.0% | +4.5 | 3.51 | 3.07 | +11.2 | +4.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 50.0% | 33.3% | 33.3% | 33.3% | +4.0 | 2.39 | 3.98 | +13.3 | +4.4 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 55.6% | 40.0% | 40.0% | 40.0% | +3.8 | 2.27 | 2.84 | +13.2 | +4.2 |
| `ratio_le_2_and_asian_gte_30` | 7 | R_REPEATER | 38.9% | 57.1% | 57.1% | 71.4% | +8.1 | 9.49 | 4.74 | +13.4 | +3.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 11.1% | 50.0% | 50.0% | 100.0% | +13.1 | 999.00 | 999.00 | +21.7 | +1.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 50.0% | +4.5 | 3.51 | 3.07 | +11.2 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 50.0% | +4.5 | 3.51 | 3.07 | +11.2 | +4.0 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 5.6% | 100.0% | 100.0% | 0.0% | +9.4 | 999.00 | 999.00 | +12.8 | +1.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 5.6% | 100.0% | 100.0% | 0.0% | +9.4 | 999.00 | 999.00 | +12.8 | +1.0 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+16.3; validation N=1 Fav=100.0% Avg=+19.2; out_of_sample N=8 Fav=50.0% Avg=+4.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 36.8% | +4.3 | 3.32 | 4.15 | +10.1 | +3.6 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 21.1% | 25.0% | 25.0% | 25.0% | +0.6 | 1.18 | 3.54 | +8.4 | +3.8 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 52.6% | 60.0% | 60.0% | 50.0% | +7.3 | 5.77 | 3.85 | +13.9 | +3.0 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 36.8% | +4.3 | 3.32 | 4.15 | +10.1 | +3.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 36.8% | +4.3 | 3.32 | 4.15 | +10.1 | +3.6 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 36.8% | +4.3 | 3.32 | 4.15 | +10.1 | +3.6 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 63.2% | 41.7% | 41.7% | 25.0% | +3.6 | 2.91 | 4.08 | +9.8 | +3.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 47.4% | 33.3% | 33.3% | 11.1% | +2.1 | 1.97 | 3.93 | +8.2 | +4.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 94.7% | 38.9% | 38.9% | 33.3% | +3.6 | 2.85 | 4.08 | +9.5 | +3.7 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 36.8% | +4.3 | 3.32 | 4.15 | +10.1 | +3.6 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 5.3% | 100.0% | 100.0% | 100.0% | +16.3 | 999.00 | 999.00 | +20.0 | +1.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+8.7; validation N=2 Fav=100.0% Avg=+33.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 41.7% | +7.9 | 6.61 | 6.61 | +12.4 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 41.7% | +7.9 | 6.61 | 6.61 | +12.4 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 41.7% | +7.9 | 6.61 | 6.61 | +12.4 | +4.6 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 41.7% | +7.9 | 6.61 | 6.61 | +12.4 | +4.6 |
| `asian_range_gte_30` | 5 | S_STRANGER | 41.7% | 40.0% | 40.0% | 60.0% | +10.5 | 4.76 | 4.76 | +16.4 | +5.0 |
| `confluence_gte_60` | 7 | R_REPEATER | 58.3% | 71.4% | 71.4% | 42.9% | +15.7 | 62.08 | 24.83 | +18.3 | +4.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 83.3% | 40.0% | 40.0% | 30.0% | +6.8 | 5.00 | 6.25 | +11.4 | +4.7 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 58.3% | 57.1% | 57.1% | 42.9% | +14.2 | 11.82 | 8.87 | +18.0 | +4.1 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 41.7% | 40.0% | 40.0% | 60.0% | +10.5 | 4.76 | 4.76 | +16.4 | +5.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 50.0% | +6.3 | 2.81 | 5.63 | +13.1 | +5.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 41.7% | +7.9 | 6.61 | 6.61 | +12.4 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 41.7% | +7.9 | 6.61 | 6.61 | +12.4 | +4.6 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +5.4 | +4.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=50.0% Avg=+3.7; validation N=3 Fav=66.7% Avg=+16.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +6.5 | 6.79 | 6.79 | +17.2 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 7 | R_REPEATER | 58.3% | 57.1% | 57.1% | 14.3% | +9.2 | 39.00 | 19.50 | +18.5 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +6.5 | 6.79 | 6.79 | +17.2 | +4.4 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +6.5 | 6.79 | 6.79 | +17.2 | +4.4 |
| `asian_range_gte_30` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 14.3% | +9.3 | 7.52 | 7.52 | +20.0 | +3.8 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +6.5 | 6.79 | 6.79 | +17.2 | +4.4 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +6.5 | 6.79 | 6.79 | +17.2 | +4.4 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 33.3% | -3.2 | 0.00 | 0.00 | +10.6 | +6.1 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 9.1% | +7.1 | 6.94 | 5.55 | +18.4 | +4.2 |
| `ratio_le_2_and_asian_gte_30` | 4 | R_REPEATER | 33.3% | 50.0% | 50.0% | 25.0% | +12.1 | 35.64 | 17.82 | +19.3 | +2.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 50.0% | -0.7 | 0.00 | 0.00 | +10.0 | +4.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +6.5 | 6.79 | 6.79 | +17.2 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +6.5 | 6.79 | 6.79 | +17.2 | +4.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=40.0% Avg=+4.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +4.6 | 7.12 | 8.90 | +10.3 | +3.4 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +4.6 | 7.12 | 8.90 | +10.3 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +4.6 | 7.12 | 8.90 | +10.3 | +3.4 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +4.6 | 7.12 | 8.90 | +10.3 | +3.4 |
| `asian_range_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +9.2 | +12.6 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +4.6 | 7.12 | 8.90 | +10.3 | +3.4 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +4.6 | 7.12 | 8.90 | +10.3 | +3.4 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +1.1 | +2.8 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 37.5% | +4.2 | 5.69 | 7.59 | +9.9 | +2.7 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +9.2 | +12.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +4.6 | 7.12 | 8.90 | +10.3 | +3.4 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +4.6 | 7.12 | 8.90 | +10.3 | +3.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=33.3% Avg=+5.3; validation N=1 Fav=100.0% Avg=+3.5; out_of_sample N=2 Fav=50.0% Avg=+1.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 30.0% | +3.7 | 5.21 | 6.52 | +9.6 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +10.6 | 999.00 | 999.00 | +13.5 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 25.0% | +3.9 | 4.49 | 11.24 | +7.5 | +4.2 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 30.0% | +3.7 | 5.21 | 6.52 | +9.6 | +3.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 30.0% | +3.7 | 5.21 | 6.52 | +9.6 | +3.9 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 30.0% | +3.7 | 5.21 | 6.52 | +9.6 | +3.9 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 90.0% | 33.3% | 33.3% | 22.2% | +3.8 | 4.89 | 8.15 | +9.1 | +4.1 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | -0.2 | 0.87 | 0.87 | +8.9 | +7.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +4.2 | 5.59 | 5.59 | +10.2 | +4.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 30.0% | +3.7 | 5.21 | 6.52 | +9.6 | +3.9 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +2.9 | +3.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+5.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +2.3 | 1.53 | 2.29 | +10.9 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +5.2 | 1.77 | 1.77 | +14.3 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -0.7 | 0.89 | 2.68 | +8.1 | +7.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +2.3 | 1.53 | 2.29 | +10.9 | +6.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +2.3 | 1.53 | 2.29 | +10.9 | +6.1 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +2.3 | 1.53 | 2.29 | +10.9 | +6.1 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 42.9% | +4.4 | 2.01 | 2.68 | +12.0 | +6.3 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 28.6% | +0.0 | 1.01 | 2.52 | +8.2 | +8.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 50.0% | +5.3 | 2.76 | 2.76 | +13.6 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +2.3 | 1.53 | 2.29 | +10.9 | +6.1 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -6.7 | 0.00 | 0.00 | +2.0 | +8.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | -0.5 | 0.92 | 1.83 | +8.2 | +10.3 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+2.2; validation N=3 Fav=33.3% Avg=+0.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 30.8% | -7.7 | 0.34 | 0.54 | +7.1 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 76.9% | 30.0% | 30.0% | 20.0% | -0.4 | 0.88 | 2.05 | +4.8 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 30.8% | -7.7 | 0.34 | 0.54 | +7.1 | +4.3 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 30.8% | -7.7 | 0.34 | 0.54 | +7.1 | +4.3 |
| `asian_range_gte_30` | 8 | S_STRANGER | 61.5% | 37.5% | 37.5% | 25.0% | +0.5 | 1.13 | 1.89 | +7.4 | +4.8 |
| `confluence_gte_60` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 33.3% | -0.6 | 0.82 | 1.65 | +10.0 | +5.1 |
| `confluence_gte_70` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 100.0% | +8.9 | 999.00 | 999.00 | +25.5 | +0.1 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 53.8% | 42.9% | 42.9% | 28.6% | +1.4 | 1.38 | 1.84 | +7.0 | +5.2 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 46.2% | 33.3% | 33.3% | 16.7% | +0.3 | 1.12 | 2.23 | +5.3 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 53.8% | 28.6% | 28.6% | 14.3% | -0.7 | 0.81 | 2.03 | +4.8 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 38.5% | 40.0% | 40.0% | 20.0% | +0.5 | 1.14 | 1.70 | +5.9 | +5.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 30.8% | -7.7 | 0.34 | 0.54 | +7.1 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 30.8% | -7.7 | 0.34 | 0.54 | +7.1 | +4.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+15.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 56.2% | +6.7 | 5.39 | 4.62 | +15.3 | +4.2 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 56.2% | +6.7 | 5.39 | 4.62 | +15.3 | +4.2 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 56.2% | +6.7 | 5.39 | 4.62 | +15.3 | +4.2 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 56.2% | +6.7 | 5.39 | 4.62 | +15.3 | +4.2 |
| `asian_range_gte_30` | 11 | S_STRANGER | 68.8% | 45.5% | 54.5% | 54.5% | +9.8 | 7.07 | 4.72 | +18.2 | +3.7 |
| `confluence_gte_60` | 13 | S_STRANGER | 81.2% | 46.2% | 53.8% | 69.2% | +9.0 | 8.98 | 3.85 | +16.4 | +3.3 |
| `confluence_gte_70` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +15.5 | +1.4 |
| `tdi_rsi_gt_signal` | 6 | R_REPEATER | 37.5% | 50.0% | 50.0% | 50.0% | +12.3 | 6.54 | 6.54 | +19.7 | +4.4 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 37.5% | 50.0% | 50.0% | 50.0% | +11.1 | 7.40 | 7.40 | +20.8 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 68.8% | 45.5% | 54.5% | 54.5% | +9.8 | 7.07 | 4.72 | +18.2 | +3.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 31.2% | 60.0% | 60.0% | 60.0% | +15.9 | 11.30 | 7.53 | +22.6 | +4.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 56.2% | +6.7 | 5.39 | 4.62 | +15.3 | +4.2 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 56.2% | +6.7 | 5.39 | 4.62 | +15.3 | +4.2 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 31.2% | 40.0% | 40.0% | 80.0% | +7.5 | 6.13 | 3.07 | +18.1 | +1.5 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 31.2% | 40.0% | 40.0% | 40.0% | +6.9 | 4.30 | 6.45 | +17.3 | +5.5 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=+4.1; validation N=6 Fav=50.0% Avg=+7.1; out_of_sample N=2 Fav=0.0% Avg=-4.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 27.3% | +4.3 | 4.10 | 4.92 | +9.3 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | +2.0 | 2.09 | 4.18 | +9.4 | +3.1 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 54.5% | 33.3% | 50.0% | 33.3% | +3.2 | 2.91 | 2.91 | +8.7 | +3.7 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 27.3% | +4.3 | 4.10 | 4.92 | +9.3 | +3.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 27.3% | +4.3 | 4.10 | 4.92 | +9.3 | +3.9 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 27.3% | +4.3 | 4.10 | 4.92 | +9.3 | +3.9 |
| `tdi_rsi_gt_signal` | 3 | R_REPEATER | 27.3% | 66.7% | 66.7% | 33.3% | +8.9 | 27.80 | 13.90 | +13.1 | +2.7 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 54.5% | 16.7% | 33.3% | 0.0% | -0.1 | 0.93 | 1.86 | +4.8 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 27.3% | +4.3 | 4.10 | 4.92 | +9.3 | +3.9 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 27.3% | +4.3 | 4.10 | 4.92 | +9.3 | +3.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=+10.3; out_of_sample N=4 Fav=75.0% Avg=+15.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 42.9% | +7.2 | 4.27 | 5.13 | +16.1 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 57.1% | 12.5% | 12.5% | 50.0% | +0.4 | 1.12 | 4.49 | +10.3 | +7.8 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 64.3% | 11.1% | 11.1% | 44.4% | +0.4 | 1.11 | 5.56 | +9.5 | +7.6 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 42.9% | +7.2 | 4.27 | 5.13 | +16.1 | +5.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 42.9% | +7.2 | 4.27 | 5.13 | +16.1 | +5.5 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 42.9% | +7.2 | 4.27 | 5.13 | +16.1 | +5.5 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 42.9% | +1.8 | 1.68 | 6.72 | +9.8 | +6.4 |
| `tdi_rsi_gte_50` | 9 | R_REPEATER | 64.3% | 55.6% | 55.6% | 33.3% | +12.7 | 7.65 | 6.12 | +19.6 | +5.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 42.9% | +7.2 | 4.27 | 5.13 | +16.1 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 42.9% | +7.2 | 4.27 | 5.13 | +16.1 | +5.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=27.3% Avg=+0.1; validation N=6 Fav=50.0% Avg=+1.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +0.4 | 1.15 | 1.53 | +6.9 | +8.1 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 23.5% | 25.0% | 25.0% | 50.0% | +2.1 | 999.00 | 999.00 | +6.5 | +2.3 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 47.1% | 12.5% | 12.5% | 25.0% | -0.7 | 0.61 | 2.43 | +5.1 | +4.6 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +0.4 | 1.15 | 1.53 | +6.9 | +8.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 0.0% | -1.7 | 0.00 | 0.00 | +3.6 | +4.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 5.9% | 100.0% | 100.0% | 0.0% | +9.0 | 999.00 | 999.00 | +15.8 | +2.9 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 82.4% | 28.6% | 28.6% | 28.6% | -0.6 | 0.82 | 1.43 | +6.3 | +8.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +0.4 | 1.15 | 1.53 | +6.9 | +8.1 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +0.4 | 1.15 | 1.53 | +6.9 | +8.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 66.7% | -1.9 | 0.00 | 0.00 | +4.1 | +3.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 66.7% | -1.9 | 0.00 | 0.00 | +4.1 | +3.7 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+10.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +3.3 | 1.76 | 3.28 | +11.8 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +3.3 | 1.76 | 3.28 | +11.8 | +7.4 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +3.3 | 1.76 | 3.28 | +11.8 | +7.4 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +3.3 | 1.76 | 3.28 | +11.8 | +7.4 |
| `asian_range_gte_30` | 9 | S_STRANGER | 45.0% | 22.2% | 22.2% | 22.2% | +4.1 | 2.00 | 7.00 | +12.8 | +6.8 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +3.3 | 1.76 | 3.28 | +11.8 | +7.4 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +3.3 | 1.76 | 3.28 | +11.8 | +7.4 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -7.5 | 0.00 | 0.00 | +2.9 | +8.7 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 70.0% | 42.9% | 42.9% | 42.9% | +7.2 | 3.09 | 4.12 | +15.2 | +6.6 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 45.0% | 22.2% | 22.2% | 22.2% | +4.1 | 2.00 | 7.00 | +12.8 | +6.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +3.3 | 1.76 | 3.28 | +11.8 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +3.3 | 1.76 | 3.28 | +11.8 | +7.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 20.0% | 25.0% | 25.0% | 25.0% | +1.1 | 1.27 | 3.82 | +8.8 | +1.5 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 30.0% | 50.0% | 50.0% | 50.0% | +10.2 | 18.06 | 18.06 | +17.0 | +2.8 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-7.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=3 Fav=100.0% Avg=+7.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 34.5% | 37.9% | 20.7% | +0.8 | 1.21 | 1.65 | +9.4 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 29 | S_STRANGER | 100.0% | 34.5% | 37.9% | 20.7% | +0.8 | 1.21 | 1.65 | +9.4 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 100.0% | 34.5% | 37.9% | 20.7% | +0.8 | 1.21 | 1.65 | +9.4 | +4.9 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 100.0% | 34.5% | 37.9% | 20.7% | +0.8 | 1.21 | 1.65 | +9.4 | +4.9 |
| `asian_range_gte_30` | 15 | S_STRANGER | 51.7% | 40.0% | 40.0% | 26.7% | -0.9 | 0.81 | 0.95 | +8.3 | +4.8 |
| `confluence_gte_60` | 26 | S_STRANGER | 89.7% | 38.5% | 42.3% | 23.1% | +1.6 | 1.45 | 1.58 | +10.4 | +4.4 |
| `confluence_gte_70` | 17 | S_STRANGER | 58.6% | 47.1% | 47.1% | 23.5% | +3.1 | 1.80 | 1.57 | +13.4 | +5.8 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 27.6% | 50.0% | 50.0% | 0.0% | +0.9 | 1.38 | 1.38 | +7.6 | +3.8 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 62.1% | 44.4% | 44.4% | 16.7% | +3.3 | 2.22 | 2.22 | +12.0 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 51.7% | 40.0% | 40.0% | 26.7% | -0.9 | 0.81 | 0.95 | +8.3 | +4.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 17.2% | 60.0% | 60.0% | 0.0% | +1.3 | 1.43 | 0.95 | +6.3 | +5.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 100.0% | 34.5% | 37.9% | 20.7% | +0.8 | 1.21 | 1.65 | +9.4 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 34.5% | 37.9% | 20.7% | +0.8 | 1.21 | 1.65 | +9.4 | +4.9 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 6.9% | 0.0% | 0.0% | 0.0% | -7.8 | 0.00 | 0.00 | +0.6 | +8.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 6.9% | 0.0% | 0.0% | 0.0% | -7.8 | 0.00 | 0.00 | +0.6 | +8.2 |

### THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=44.4% Avg=+8.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +4.3 | 2.66 | 4.25 | +12.1 | +4.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 93.3% | 35.7% | 35.7% | 35.7% | +4.6 | 2.66 | 4.25 | +11.1 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +4.3 | 2.66 | 4.25 | +12.1 | +4.7 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +4.3 | 2.66 | 4.25 | +12.1 | +4.7 |
| `asian_range_gte_30` | 10 | S_STRANGER | 66.7% | 20.0% | 20.0% | 20.0% | +1.5 | 1.64 | 5.74 | +7.1 | +4.4 |
| `confluence_gte_60` | 6 | S_STRANGER | 40.0% | 0.0% | 0.0% | 16.7% | -2.5 | 0.00 | 0.00 | +7.8 | +5.4 |
| `confluence_gte_70` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +25.0 | +7.0 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 50.0% | +20.3 | 10.91 | 10.91 | +28.4 | +4.2 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 86.7% | 23.1% | 23.1% | 30.8% | +1.9 | 1.65 | 4.40 | +10.7 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 66.7% | 20.0% | 20.0% | 20.0% | +1.5 | 1.64 | 5.74 | +7.1 | +4.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -4.1 | 0.00 | 0.00 | +1.0 | +8.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +4.3 | 2.66 | 4.25 | +12.1 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +4.3 | 2.66 | 4.25 | +12.1 | +4.7 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 60.0% | 44.4% | 44.4% | 44.4% | +8.1 | 8.90 | 8.90 | +13.3 | +3.1 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 53.3% | 37.5% | 37.5% | 37.5% | +6.8 | 6.93 | 9.24 | +12.5 | +3.1 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=100.0% Avg=+12.4; validation N=2 Fav=50.0% Avg=+3.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | +1.4 | 1.55 | 2.72 | +7.2 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 30.0% | 30.0% | 30.0% | +0.0 | 1.01 | 2.03 | +6.1 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 27.3% | -0.3 | 0.89 | 2.07 | +5.8 | +4.8 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | +1.4 | 1.55 | 2.72 | +7.2 | +4.4 |
| `asian_range_gte_30` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -6.8 | 0.00 | 0.00 | +5.2 | +9.4 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | +1.4 | 1.55 | 2.72 | +7.2 | +4.4 |
| `confluence_gte_70` | 5 | R_RUNNER | 41.7% | 80.0% | 80.0% | 60.0% | +9.0 | 15.44 | 3.86 | +11.9 | +1.9 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 0.0% | -2.8 | 0.39 | 1.93 | +4.5 | +6.2 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 25.0% | -1.6 | 0.63 | 1.25 | +7.3 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -6.8 | 0.00 | 0.00 | +5.2 | +9.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -13.4 | 0.00 | 0.00 | +3.7 | +13.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | +1.4 | 1.55 | 2.72 | +7.2 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | +1.4 | 1.55 | 2.72 | +7.2 | +4.4 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +7.8 | 999.00 | 999.00 | +8.2 | +1.4 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=80.0% Avg=+10.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | +1.0 | 1.23 | 2.46 | +7.9 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 7 | R_REPEATER | 58.3% | 57.1% | 57.1% | 42.9% | +6.2 | 3.22 | 2.42 | +11.8 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 33.3% | +3.0 | 1.76 | 2.19 | +9.8 | +6.6 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | +1.0 | 1.23 | 2.46 | +7.9 | +6.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 83.3% | 40.0% | 40.0% | 30.0% | +1.9 | 1.44 | 2.16 | +9.2 | +6.5 |
| `confluence_gte_70` | 5 | R_RUNNER | 41.7% | 80.0% | 80.0% | 60.0% | +10.2 | 5.28 | 1.32 | +15.8 | +2.9 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 75.0% | 33.3% | 33.3% | 22.2% | +0.6 | 1.14 | 2.27 | +8.2 | +7.4 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 0.0% | -2.4 | 0.60 | 1.21 | +6.3 | +7.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | +1.0 | 1.23 | 2.46 | +7.9 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | +1.0 | 1.23 | 2.46 | +7.9 | +6.6 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 33.3% | 50.0% | 50.0% | 50.0% | +6.5 | 4.44 | 4.44 | +9.8 | +3.6 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=0.0% Avg=-1.5; validation N=8 Fav=50.0% Avg=+2.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 15.4% | +1.2 | 1.53 | 2.68 | +9.2 | +5.8 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 8.3% | +1.3 | 1.53 | 2.68 | +9.1 | +6.0 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 15.4% | +1.2 | 1.53 | 2.68 | +9.2 | +5.8 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 15.4% | +1.2 | 1.53 | 2.68 | +9.2 | +5.8 |
| `asian_range_gte_30` | 4 | S_STRANGER | 30.8% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +4.3 | +7.6 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 15.4% | +1.2 | 1.53 | 2.68 | +9.2 | +5.8 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 15.4% | +1.2 | 1.53 | 2.68 | +9.2 | +5.8 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 0.0% | -1.8 | 0.50 | 1.50 | +5.1 | +5.4 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 8.3% | +1.3 | 1.53 | 2.68 | +9.1 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 30.8% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +4.3 | +7.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -6.9 | 0.00 | 0.00 | +2.3 | +9.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 15.4% | +1.2 | 1.53 | 2.68 | +9.2 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 15.4% | +1.2 | 1.53 | 2.68 | +9.2 | +5.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=33.3% Avg=+6.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 50.0% | +4.6 | 3.20 | 5.33 | +9.8 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 66.7% | -1.3 | 0.00 | 0.00 | +6.8 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 66.7% | -1.3 | 0.00 | 0.00 | +6.8 | +6.3 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 50.0% | +4.6 | 3.20 | 5.33 | +9.8 | +5.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 3 | R_RUNNER | 30.0% | 100.0% | 100.0% | 100.0% | +22.3 | 999.00 | 999.00 | +23.8 | +0.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 90.0% | 33.3% | 33.3% | 55.6% | +6.0 | 5.03 | 6.71 | +10.8 | +4.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 50.0% | +6.0 | 3.39 | 5.09 | +11.8 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 50.0% | +4.6 | 3.20 | 5.33 | +9.8 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 50.0% | +4.6 | 3.20 | 5.33 | +9.8 | +5.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+2.3; validation N=3 Fav=33.3% Avg=-1.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.8 | 1.37 | 2.51 | +6.2 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 30.0% | 16.7% | 16.7% | 16.7% | -2.7 | 0.29 | 1.17 | +4.7 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 45.0% | 44.4% | 44.4% | 33.3% | +1.1 | 1.45 | 1.45 | +7.4 | +3.9 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.8 | 1.37 | 2.51 | +6.2 | +3.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.8 | 1.37 | 2.51 | +6.2 | +3.7 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.8 | 1.37 | 2.51 | +6.2 | +3.7 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 60.0% | 33.3% | 33.3% | 25.0% | +1.3 | 1.57 | 2.74 | +6.2 | +4.1 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 65.0% | 23.1% | 23.1% | 15.4% | +1.1 | 1.70 | 4.53 | +5.4 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.8 | 1.37 | 2.51 | +6.2 | +3.7 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.8 | 1.37 | 2.51 | +6.2 | +3.7 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +0.7 | +3.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +0.7 | +3.4 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=45.5% Avg=+2.2; validation N=1 Fav=0.0% Avg=-3.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 30.0% | 35.0% | 30.0% | -0.2 | 0.95 | 1.63 | +10.5 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +5.7 | +7.6 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 45.0% | 33.3% | 33.3% | 33.3% | +0.6 | 1.11 | 2.22 | +11.8 | +7.8 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 30.0% | 35.0% | 30.0% | -0.2 | 0.95 | 1.63 | +10.5 | +7.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 35.0% | 28.6% | 28.6% | 14.3% | +2.6 | 1.99 | 4.99 | +10.1 | +5.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | R_RUNNER | 20.0% | 75.0% | 75.0% | 50.0% | +6.3 | 2.45 | 0.82 | +17.3 | +9.0 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 60.0% | 41.7% | 41.7% | 33.3% | +1.7 | 1.37 | 1.92 | +13.2 | +8.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 75.0% | 33.3% | 40.0% | 33.3% | +2.8 | 2.00 | 2.66 | +11.7 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 85.0% | 29.4% | 35.3% | 29.4% | -0.2 | 0.95 | 1.58 | +10.3 | +7.3 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 60.0% | 25.0% | 33.3% | 33.3% | -0.9 | 0.75 | 1.31 | +10.7 | +6.3 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 40.0% | 37.5% | 37.5% | 37.5% | -1.2 | 0.80 | 1.34 | +13.4 | +9.4 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=30.0% Avg=-0.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | -0.3 | 0.94 | 2.20 | +10.0 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | -0.3 | 0.94 | 2.20 | +10.0 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | -0.3 | 0.94 | 2.20 | +10.0 | +8.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | -0.3 | 0.94 | 2.20 | +10.0 | +8.8 |
| `asian_range_gte_30` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | -2.9 | 0.41 | 1.63 | +7.2 | +8.1 |
| `confluence_gte_60` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -10.4 | 0.00 | 0.00 | +5.2 | +14.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 14.3% | -5.4 | 0.29 | 1.71 | +6.5 | +11.1 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | -2.9 | 0.41 | 1.63 | +7.2 | +8.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -7.2 | 0.00 | 0.00 | +7.0 | +12.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | -0.3 | 0.94 | 2.20 | +10.0 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | -0.3 | 0.94 | 2.20 | +10.0 | +8.8 |
| `feature_momentum_breakout_exception` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 66.7% | +6.3 | 4.10 | 2.05 | +11.3 | +3.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +2.8 | 2.24 | 4.48 | +8.2 | +5.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-6.0; validation N=6 Fav=66.7% Avg=+7.1; out_of_sample N=2 Fav=0.0% Avg=-9.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 51 | S_STRANGER | 100.0% | 29.4% | 29.4% | 23.5% | -3.4 | 0.46 | 0.99 | +8.1 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 41 | S_STRANGER | 80.4% | 29.3% | 29.3% | 22.0% | -0.3 | 0.92 | 1.92 | +8.6 | +6.2 |
| `hunt_to_ar_ratio_le_2_5` | 47 | S_STRANGER | 92.2% | 31.9% | 31.9% | 25.5% | -0.7 | 0.82 | 1.54 | +8.7 | +5.9 |
| `stop_hunt_le_90` | 51 | S_STRANGER | 100.0% | 29.4% | 29.4% | 23.5% | -3.4 | 0.46 | 0.99 | +8.1 | +5.7 |
| `asian_range_gte_30` | 22 | S_STRANGER | 43.1% | 27.3% | 27.3% | 31.8% | +0.3 | 1.10 | 2.39 | +9.0 | +6.0 |
| `confluence_gte_60` | 41 | S_STRANGER | 80.4% | 26.8% | 26.8% | 19.5% | -4.4 | 0.41 | 0.97 | +7.6 | +6.1 |
| `confluence_gte_70` | 10 | S_STRANGER | 19.6% | 40.0% | 40.0% | 20.0% | +1.1 | 1.28 | 1.92 | +7.2 | +7.1 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 21.6% | 27.3% | 27.3% | 18.2% | -6.5 | 0.23 | 0.53 | +7.8 | +7.8 |
| `tdi_rsi_gte_50` | 33 | S_STRANGER | 64.7% | 36.4% | 36.4% | 27.3% | +1.0 | 1.37 | 1.94 | +10.1 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 20 | S_STRANGER | 39.2% | 20.0% | 20.0% | 25.0% | -0.2 | 0.94 | 3.05 | +8.0 | +6.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 7.8% | 25.0% | 25.0% | 50.0% | +0.7 | 1.21 | 2.43 | +8.7 | +5.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 50 | S_STRANGER | 98.0% | 28.0% | 28.0% | 22.0% | -3.6 | 0.44 | 1.01 | +7.9 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 51 | S_STRANGER | 100.0% | 29.4% | 29.4% | 23.5% | -3.4 | 0.46 | 0.99 | +8.1 | +5.7 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 7.8% | 25.0% | 25.0% | 25.0% | -1.5 | 0.52 | 1.57 | +6.0 | +5.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 3.9% | 50.0% | 50.0% | 50.0% | +0.2 | 1.06 | 1.06 | +10.2 | +4.8 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=50.0% Avg=+3.1; validation N=16 Fav=31.2% Avg=-0.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 55 | S_STRANGER | 100.0% | 29.1% | 30.9% | 21.8% | -0.0 | 0.99 | 1.97 | +7.8 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 48 | S_STRANGER | 87.3% | 33.3% | 35.4% | 25.0% | +0.8 | 1.26 | 2.00 | +8.4 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 52 | S_STRANGER | 94.5% | 30.8% | 32.7% | 23.1% | +0.4 | 1.14 | 2.08 | +8.2 | +6.5 |
| `stop_hunt_le_90` | 55 | S_STRANGER | 100.0% | 29.1% | 30.9% | 21.8% | -0.0 | 0.99 | 1.97 | +7.8 | +6.7 |
| `asian_range_gte_30` | 29 | S_STRANGER | 52.7% | 31.0% | 34.5% | 17.2% | +1.0 | 1.36 | 2.32 | +8.8 | +7.3 |
| `confluence_gte_60` | 26 | S_STRANGER | 47.3% | 38.5% | 38.5% | 26.9% | +1.0 | 1.39 | 1.81 | +8.7 | +6.5 |
| `confluence_gte_70` | 2 | R_REPEATER | 3.6% | 50.0% | 50.0% | 0.0% | +5.1 | 13.87 | 13.87 | +10.8 | +5.3 |
| `tdi_rsi_gt_signal` | 26 | S_STRANGER | 47.3% | 19.2% | 23.1% | 7.7% | -0.9 | 0.74 | 2.33 | +6.4 | +7.2 |
| `tdi_rsi_gte_50` | 34 | S_STRANGER | 61.8% | 32.4% | 32.4% | 20.6% | -0.1 | 0.97 | 1.75 | +8.1 | +7.2 |
| `ratio_le_2_and_asian_gte_30` | 27 | S_STRANGER | 49.1% | 33.3% | 37.0% | 18.5% | +1.4 | 1.51 | 2.26 | +9.0 | +7.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 25.5% | 28.6% | 35.7% | 14.3% | +2.7 | 2.44 | 3.90 | +8.3 | +7.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 52 | S_STRANGER | 94.5% | 30.8% | 32.7% | 23.1% | +0.1 | 1.04 | 1.89 | +8.1 | +6.9 |
| `feature_stale_hod_exhaustion_reject` | 55 | S_STRANGER | 100.0% | 29.1% | 30.9% | 21.8% | -0.0 | 0.99 | 1.97 | +7.8 | +6.7 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +5.6 | +7.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 5.5% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +6.8 | +8.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=44.4% Avg=+1.9; validation N=9 Fav=55.6% Avg=+10.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 38 | S_STRANGER | 100.0% | 28.9% | 34.2% | 28.9% | +0.5 | 1.11 | 1.96 | +11.3 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 33 | S_STRANGER | 86.8% | 30.3% | 36.4% | 30.3% | +0.4 | 1.09 | 1.73 | +11.5 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 38 | S_STRANGER | 100.0% | 28.9% | 34.2% | 28.9% | +0.5 | 1.11 | 1.96 | +11.3 | +5.5 |
| `stop_hunt_le_90` | 38 | S_STRANGER | 100.0% | 28.9% | 34.2% | 28.9% | +0.5 | 1.11 | 1.96 | +11.3 | +5.5 |
| `asian_range_gte_30` | 18 | S_STRANGER | 47.4% | 27.8% | 33.3% | 22.2% | -1.5 | 0.70 | 1.39 | +10.2 | +5.3 |
| `confluence_gte_60` | 20 | S_STRANGER | 52.6% | 40.0% | 45.0% | 35.0% | +3.5 | 2.05 | 2.50 | +13.8 | +5.0 |
| `confluence_gte_70` | 3 | R_REPEATER | 7.9% | 66.7% | 66.7% | 66.7% | +5.0 | 3.73 | 1.86 | +13.3 | +5.2 |
| `tdi_rsi_gt_signal` | 27 | S_STRANGER | 71.1% | 33.3% | 37.0% | 29.6% | +2.7 | 1.91 | 3.05 | +12.1 | +5.4 |
| `tdi_rsi_gte_50` | 18 | R_REPEATER | 47.4% | 50.0% | 50.0% | 38.9% | +6.0 | 3.77 | 3.77 | +14.4 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 42.1% | 25.0% | 31.2% | 18.8% | -2.4 | 0.57 | 1.26 | +9.2 | +4.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 31.6% | 33.3% | 41.7% | 25.0% | +2.1 | 1.94 | 2.71 | +10.5 | +4.8 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 2.6% | 100.0% | 100.0% | 100.0% | +5.7 | 999.00 | 999.00 | +11.6 | +2.3 |
| `feature_extreme_hunt_with_exception` | 38 | S_STRANGER | 100.0% | 28.9% | 34.2% | 28.9% | +0.5 | 1.11 | 1.96 | +11.3 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 100.0% | 28.9% | 34.2% | 28.9% | +0.5 | 1.11 | 1.96 | +11.3 | +5.5 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 7.9% | 33.3% | 33.3% | 66.7% | +0.4 | 1.30 | 1.30 | +11.1 | +2.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.6% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +7.2 | +4.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+2.3; validation N=1 Fav=100.0% Avg=+10.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 28.6% | -0.9 | 0.75 | 1.49 | +7.6 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 33.3% | +2.9 | 6.18 | 6.18 | +13.5 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 14.3% | -1.5 | 0.50 | 2.50 | +7.9 | +4.8 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 28.6% | -0.9 | 0.75 | 1.49 | +7.6 | +4.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 28.6% | -0.9 | 0.75 | 1.49 | +7.6 | +4.9 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 28.6% | -0.9 | 0.75 | 1.49 | +7.6 | +4.9 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 78.6% | 36.4% | 36.4% | 27.3% | -0.5 | 0.86 | 1.29 | +8.0 | +4.9 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 42.9% | 50.0% | 50.0% | 33.3% | +3.6 | 4.37 | 2.91 | +11.2 | +3.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 28.6% | -0.9 | 0.75 | 1.49 | +7.6 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 28.6% | -0.9 | 0.75 | 1.49 | +7.6 | +4.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=44.4% Avg=+4.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -2.2 | 0.70 | 1.75 | +9.3 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 0.0% | +2.6 | 1.49 | 1.49 | +8.5 | +10.4 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 0.0% | -1.9 | 0.73 | 1.47 | +7.3 | +7.4 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -2.2 | 0.70 | 1.75 | +9.3 | +5.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -2.2 | 0.70 | 1.75 | +9.3 | +5.7 |
| `confluence_gte_70` | 12 | S_STRANGER | 85.7% | 33.3% | 33.3% | 8.3% | -1.3 | 0.83 | 1.66 | +10.3 | +4.5 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 64.3% | 44.4% | 44.4% | 11.1% | +4.4 | 2.18 | 2.72 | +12.3 | +7.6 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 44.4% | 44.4% | 11.1% | +4.4 | 2.18 | 2.72 | +12.3 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 71.4% | 30.0% | 30.0% | 0.0% | -1.6 | 0.76 | 1.78 | +9.3 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -2.2 | 0.70 | 1.75 | +9.3 | +5.7 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -16.9 | 0.00 | 0.00 | +1.7 | +2.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 50.0% | +9.1 | 4.87 | 4.87 | +16.9 | +4.2 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=0.0% Avg=-4.1; validation N=3 Fav=66.7% Avg=+12.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 28.0% | 28.0% | 12.0% | +2.6 | 2.07 | 5.31 | +8.4 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 2 | S_STRANGER | 8.0% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +2.5 | +3.3 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 24.0% | 33.3% | 33.3% | 0.0% | +4.1 | 2.49 | 4.99 | +10.7 | +4.2 |
| `stop_hunt_le_90` | 25 | S_STRANGER | 100.0% | 28.0% | 28.0% | 12.0% | +2.6 | 2.07 | 5.31 | +8.4 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 25 | S_STRANGER | 100.0% | 28.0% | 28.0% | 12.0% | +2.6 | 2.07 | 5.31 | +8.4 | +4.1 |
| `confluence_gte_70` | 25 | S_STRANGER | 100.0% | 28.0% | 28.0% | 12.0% | +2.6 | 2.07 | 5.31 | +8.4 | +4.1 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 56.0% | 21.4% | 21.4% | 7.1% | -0.4 | 0.90 | 3.30 | +6.2 | +4.9 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 76.0% | 15.8% | 15.8% | 5.3% | -0.6 | 0.81 | 4.33 | +5.5 | +4.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 96.0% | 29.2% | 29.2% | 12.5% | +2.8 | 2.10 | 5.09 | +8.7 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 28.0% | 28.0% | 12.0% | +2.6 | 2.07 | 5.31 | +8.4 | +4.1 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 4.0% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +1.8 | +3.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.0% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +1.8 | +3.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=57.1% Avg=+2.8; validation N=1 Fav=0.0% Avg=+0.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 22.2% | +0.3 | 1.12 | 2.70 | +8.0 | +4.7 |
| `hunt_to_ar_ratio_le_2_0` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +8.0 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 22.2% | 25.0% | 25.0% | 50.0% | +2.4 | 2.35 | 4.70 | +10.5 | +6.0 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 22.2% | +0.3 | 1.12 | 2.70 | +8.0 | +4.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 22.2% | +0.3 | 1.12 | 2.70 | +8.0 | +4.7 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 22.2% | +0.3 | 1.12 | 2.70 | +8.0 | +4.7 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 44.4% | 50.0% | 50.0% | 37.5% | +2.4 | 4.02 | 3.01 | +9.1 | +3.7 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 72.2% | 23.1% | 23.1% | 7.7% | -1.1 | 0.57 | 1.89 | +7.8 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 22.2% | +0.3 | 1.12 | 2.70 | +8.0 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 22.2% | +0.3 | 1.12 | 2.70 | +8.0 | +4.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-10.6; validation N=8 Fav=50.0% Avg=+9.1; out_of_sample N=5 Fav=40.0% Avg=+8.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +2.8 | 1.89 | 4.41 | +11.4 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 77.3% | 29.4% | 29.4% | 11.8% | +2.9 | 1.80 | 3.60 | +10.4 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 90.9% | 30.0% | 30.0% | 10.0% | +3.3 | 2.03 | 4.06 | +12.5 | +5.7 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +2.8 | 1.89 | 4.41 | +11.4 | +6.3 |
| `asian_range_gte_30` | 9 | S_STRANGER | 40.9% | 0.0% | 0.0% | 22.2% | -5.9 | 0.00 | 0.00 | +3.3 | +5.6 |
| `confluence_gte_60` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +2.8 | 1.89 | 4.41 | +11.4 | +6.3 |
| `confluence_gte_70` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +2.8 | 1.89 | 4.41 | +11.4 | +6.3 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 36.4% | 37.5% | 37.5% | 0.0% | +4.8 | 2.20 | 3.66 | +14.4 | +6.8 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 68.2% | 40.0% | 40.0% | 0.0% | +6.3 | 3.78 | 5.67 | +14.5 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 40.9% | 0.0% | 0.0% | 22.2% | -5.9 | 0.00 | 0.00 | +3.3 | +5.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 13.6% | 0.0% | 0.0% | 0.0% | -9.9 | 0.00 | 0.00 | +2.5 | +9.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +2.8 | 1.89 | 4.41 | +11.4 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +2.8 | 1.89 | 4.41 | +11.4 | +6.3 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +0.8 | +8.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.5% | 0.0% | 0.0% | 0.0% | -10.4 | 0.00 | 0.00 | +0.6 | +11.0 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=37.5% Avg=+4.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 22.7% | +2.5 | 2.30 | 5.37 | +10.6 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 36.4% | 37.5% | 37.5% | 12.5% | +4.5 | 3.79 | 6.32 | +12.6 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 36.4% | 37.5% | 37.5% | 12.5% | +4.5 | 3.79 | 6.32 | +12.6 | +4.4 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 22.7% | +2.5 | 2.30 | 5.37 | +10.6 | +4.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 22.7% | +2.5 | 2.30 | 5.37 | +10.6 | +4.4 |
| `confluence_gte_70` | 14 | S_STRANGER | 63.6% | 28.6% | 28.6% | 14.3% | +1.3 | 1.63 | 3.66 | +10.4 | +4.9 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 50.0% | 27.3% | 27.3% | 9.1% | +1.7 | 2.13 | 5.68 | +10.5 | +4.6 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 54.5% | 25.0% | 25.0% | 8.3% | +1.2 | 1.65 | 4.96 | +9.8 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 4.5% | 0.0% | 0.0% | 0.0% | -7.0 | 0.00 | 0.00 | +2.0 | +7.6 |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 68.2% | 33.3% | 33.3% | 20.0% | +4.4 | 3.32 | 6.64 | +11.7 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 22.7% | +2.5 | 2.30 | 5.37 | +10.6 | +4.4 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 22.7% | 0.0% | 0.0% | 40.0% | -2.8 | 0.00 | 0.00 | +6.8 | +5.0 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 18.2% | 25.0% | 25.0% | 0.0% | -2.1 | 0.30 | 0.89 | +6.8 | +6.2 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=0.0% Avg=-6.1; out_of_sample N=5 Fav=60.0% Avg=+5.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -1.0 | 0.73 | 1.71 | +8.1 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -1.0 | 0.73 | 1.71 | +8.1 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -1.0 | 0.73 | 1.71 | +8.1 | +7.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -1.0 | 0.73 | 1.71 | +8.1 | +7.0 |
| `asian_range_gte_30` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -8.1 | 0.00 | 0.00 | +2.9 | +10.4 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -1.0 | 0.73 | 1.71 | +8.1 | +7.0 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -1.0 | 0.73 | 1.71 | +8.1 | +7.0 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 54.5% | 16.7% | 16.7% | 16.7% | -2.4 | 0.50 | 2.49 | +8.3 | +7.3 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 0.0% | -5.1 | 0.26 | 1.03 | +6.4 | +10.0 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -8.1 | 0.00 | 0.00 | +2.9 | +10.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -1.0 | 0.73 | 1.71 | +8.1 | +7.0 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -1.0 | 0.73 | 1.71 | +8.1 | +7.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+0.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -1.4 | 0.54 | 1.45 | +4.0 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 20.0% | -0.1 | 0.95 | 2.22 | +4.3 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 20.0% | -0.1 | 0.95 | 2.22 | +4.3 | +4.4 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -1.4 | 0.54 | 1.45 | +4.0 | +5.3 |
| `asian_range_gte_30` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 20.0% | +0.3 | 1.17 | 1.76 | +4.7 | +4.3 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -1.4 | 0.54 | 1.45 | +4.0 | +5.3 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -1.4 | 0.54 | 1.45 | +4.0 | +5.3 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -4.7 | 0.20 | 0.61 | +3.5 | +7.5 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -1.4 | 0.54 | 1.45 | +4.0 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 20.0% | +0.3 | 1.17 | 1.76 | +4.7 | +4.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 0.0% | -0.9 | 0.72 | 0.72 | +6.1 | +4.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -1.4 | 0.54 | 1.45 | +4.0 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -1.4 | 0.54 | 1.45 | +4.0 | +5.3 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +1.2 | +8.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +1.2 | +8.4 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+5.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | -6.9 | 0.39 | 1.04 | +11.0 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 10.0% | -5.4 | 0.47 | 1.11 | +11.4 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | -6.9 | 0.39 | 1.04 | +11.0 | +5.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | -6.9 | 0.39 | 1.04 | +11.0 | +5.0 |
| `asian_range_gte_30` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 16.7% | +5.2 | 2.85 | 2.85 | +12.9 | +5.1 |
| `confluence_gte_60` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -12.6 | 0.00 | 0.00 | +5.4 | +7.5 |
| `confluence_gte_70` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -9.0 | 0.00 | 0.00 | +0.1 | +11.2 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 12.5% | +1.9 | 1.45 | 2.42 | +13.3 | +6.4 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 12.5% | +1.9 | 1.45 | 2.42 | +13.3 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 16.7% | +5.2 | 2.85 | 2.85 | +12.9 | +5.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 16.7% | +5.2 | 2.85 | 2.85 | +12.9 | +5.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | -6.9 | 0.39 | 1.04 | +11.0 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | -6.9 | 0.39 | 1.04 | +11.0 | +5.0 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -34.4 | 0.00 | 0.00 | +2.6 | +3.1 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 16.7% | +5.2 | 2.85 | 2.85 | +12.9 | +5.1 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=14.3% Avg=-0.1; validation N=13 Fav=30.8% Avg=-1.3; out_of_sample N=5 Fav=40.0% Avg=+0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 7.7% | -0.7 | 0.81 | 2.19 | +8.3 | +5.1 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 80.8% | 19.0% | 19.0% | 9.5% | -1.3 | 0.64 | 2.71 | +7.4 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 96.2% | 28.0% | 28.0% | 8.0% | -0.6 | 0.84 | 2.16 | +8.5 | +5.1 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 7.7% | -0.7 | 0.81 | 2.19 | +8.3 | +5.1 |
| `asian_range_gte_30` | 12 | S_STRANGER | 46.2% | 8.3% | 8.3% | 0.0% | -2.8 | 0.25 | 2.74 | +5.1 | +5.5 |
| `confluence_gte_60` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 7.7% | -0.7 | 0.81 | 2.19 | +8.3 | +5.1 |
| `confluence_gte_70` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 7.7% | -0.7 | 0.81 | 2.19 | +8.3 | +5.1 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 19.2% | 20.0% | 20.0% | 0.0% | -0.2 | 0.91 | 3.63 | +5.1 | +5.9 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 76.9% | 25.0% | 25.0% | 0.0% | -0.7 | 0.75 | 2.24 | +8.0 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 46.2% | 8.3% | 8.3% | 0.0% | -2.8 | 0.25 | 2.74 | +5.1 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +0.8 | +8.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 7.7% | -0.7 | 0.81 | 2.19 | +8.3 | +5.1 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 7.7% | -0.7 | 0.81 | 2.19 | +8.3 | +5.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 11.5% | 33.3% | 33.3% | 33.3% | +2.0 | 2.39 | 4.77 | +6.5 | +2.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +3.8 | +3.2 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+9.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +1.6 | 1.53 | 2.75 | +10.4 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +1.6 | 1.53 | 2.75 | +10.4 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +1.6 | 1.53 | 2.75 | +10.4 | +6.7 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +1.6 | 1.53 | 2.75 | +10.4 | +6.7 |
| `asian_range_gte_30` | 13 | S_STRANGER | 86.7% | 30.8% | 38.5% | 30.8% | +2.7 | 2.00 | 2.80 | +10.8 | +6.3 |
| `confluence_gte_60` | 5 | S_STRANGER | 33.3% | 20.0% | 20.0% | 20.0% | +1.3 | 1.40 | 5.60 | +9.6 | +6.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | R_REPEATER | 33.3% | 60.0% | 60.0% | 40.0% | +9.9 | 8.96 | 5.97 | +17.0 | +5.3 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 40.0% | 50.0% | 50.0% | 33.3% | +4.5 | 2.53 | 2.53 | +14.9 | +8.0 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 86.7% | 30.8% | 38.5% | 30.8% | +2.7 | 2.00 | 2.80 | +10.8 | +6.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_RUNNER | 26.7% | 75.0% | 75.0% | 50.0% | +13.8 | 277.75 | 92.58 | +19.4 | +3.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +1.6 | 1.53 | 2.75 | +10.4 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +1.6 | 1.53 | 2.75 | +10.4 | +6.7 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 25.0% | -4.0 | 0.00 | 0.00 | +3.4 | +6.4 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 26.7% | 50.0% | 50.0% | 25.0% | +5.1 | 2.76 | 2.76 | +16.3 | +8.0 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+0.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | -1.4 | 0.69 | 1.24 | +8.6 | +7.8 |
| `hunt_to_ar_ratio_le_2_0` | 3 | R_REPEATER | 20.0% | 66.7% | 66.7% | 33.3% | +2.4 | 5.87 | 2.93 | +13.3 | +5.9 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 33.3% | 40.0% | 60.0% | 20.0% | +0.1 | 1.04 | 0.69 | +10.0 | +6.0 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | -1.4 | 0.69 | 1.24 | +8.6 | +7.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | -1.4 | 0.69 | 1.24 | +8.6 | +7.8 |
| `confluence_gte_70` | 9 | S_STRANGER | 60.0% | 22.2% | 33.3% | 33.3% | +0.1 | 1.03 | 1.71 | +9.1 | +7.1 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 86.7% | 30.8% | 38.5% | 30.8% | +0.2 | 1.06 | 1.49 | +9.2 | +7.0 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 33.3% | 40.0% | 40.0% | 40.0% | -0.3 | 0.95 | 1.43 | +12.3 | +9.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 80.0% | 25.0% | 25.0% | 25.0% | -2.4 | 0.44 | 1.18 | +8.0 | +8.4 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 93.3% | 21.4% | 28.6% | 21.4% | -2.7 | 0.42 | 0.94 | +7.5 | +8.3 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 26.7% | 25.0% | 50.0% | 0.0% | -4.7 | 0.18 | 0.18 | +7.4 | +8.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 6.7% | 100.0% | 100.0% | 100.0% | +17.7 | 999.00 | 999.00 | +25.2 | +0.8 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+28.3; validation N=3 Fav=33.3% Avg=+2.8; out_of_sample N=8 Fav=25.0% Avg=-0.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 26.3% | 36.8% | 10.5% | +2.1 | 2.33 | 4.00 | +6.1 | +4.0 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 100.0% | 26.3% | 36.8% | 10.5% | +2.1 | 2.33 | 4.00 | +6.1 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 26.3% | 36.8% | 10.5% | +2.1 | 2.33 | 4.00 | +6.1 | +4.0 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 26.3% | 36.8% | 10.5% | +2.1 | 2.33 | 4.00 | +6.1 | +4.0 |
| `asian_range_gte_30` | 6 | S_STRANGER | 31.6% | 16.7% | 33.3% | 16.7% | +3.8 | 3.13 | 6.26 | +6.8 | +4.2 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 26.3% | 36.8% | 10.5% | +2.1 | 2.33 | 4.00 | +6.1 | +4.0 |
| `confluence_gte_70` | 5 | S_STRANGER | 26.3% | 20.0% | 20.0% | 0.0% | +0.5 | 1.26 | 5.05 | +6.4 | +5.1 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 15.8% | 33.3% | 33.3% | 0.0% | +1.1 | 1.62 | 3.24 | +6.0 | +3.4 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 63.2% | 33.3% | 33.3% | 8.3% | +2.8 | 2.71 | 5.41 | +7.8 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 31.6% | 16.7% | 33.3% | 16.7% | +3.8 | 3.13 | 6.26 | +6.8 | +4.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 26.3% | 36.8% | 10.5% | +2.1 | 2.33 | 4.00 | +6.1 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 26.3% | 36.8% | 10.5% | +2.1 | 2.33 | 4.00 | +6.1 | +4.0 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +0.6 | +3.5 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-16.8; validation N=12 Fav=33.3% Avg=+3.2; out_of_sample N=7 Fav=28.6% Avg=+5.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 13.0% | +0.9 | 1.18 | 2.71 | +10.9 | +8.1 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 91.3% | 28.6% | 33.3% | 14.3% | +2.0 | 1.43 | 2.85 | +11.3 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 95.7% | 27.3% | 31.8% | 13.6% | +1.8 | 1.40 | 3.01 | +11.3 | +7.0 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 13.0% | +0.9 | 1.18 | 2.71 | +10.9 | +8.1 |
| `asian_range_gte_30` | 3 | S_STRANGER | 13.0% | 33.3% | 66.7% | 33.3% | +8.5 | 7.51 | 3.76 | +15.2 | +3.7 |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 13.0% | +0.9 | 1.18 | 2.71 | +10.9 | +8.1 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 13.0% | +0.9 | 1.18 | 2.71 | +10.9 | +8.1 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 17.4% | 25.0% | 50.0% | 0.0% | +3.2 | 1.85 | 1.85 | +10.9 | +7.0 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 78.3% | 27.8% | 27.8% | 16.7% | +1.2 | 1.21 | 3.15 | +12.2 | +9.6 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 13.0% | 33.3% | 66.7% | 33.3% | +8.5 | 7.51 | 3.76 | +15.2 | +3.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.3% | 0.0% | 100.0% | 0.0% | +9.3 | 999.00 | 999.00 | +9.8 | +2.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 13.0% | +0.9 | 1.18 | 2.71 | +10.9 | +8.1 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 13.0% | +0.9 | 1.18 | 2.71 | +10.9 | +8.1 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -15.5 | 0.00 | 0.00 | +1.2 | +17.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -15.5 | 0.00 | 0.00 | +1.2 | +17.2 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=+0.0; validation N=11 Fav=36.4% Avg=+7.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +3.2 | 2.07 | 4.82 | +11.8 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 75.0% | 27.8% | 27.8% | 27.8% | +4.4 | 2.40 | 5.76 | +12.8 | +6.8 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 95.8% | 26.1% | 26.1% | 30.4% | +3.3 | 2.07 | 4.82 | +12.0 | +6.5 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +3.2 | 2.07 | 4.82 | +11.8 | +6.4 |
| `asian_range_gte_30` | 8 | S_STRANGER | 33.3% | 12.5% | 12.5% | 12.5% | -1.9 | 0.47 | 2.80 | +5.0 | +5.6 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +3.2 | 2.07 | 4.82 | +11.8 | +6.4 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +3.2 | 2.07 | 4.82 | +11.8 | +6.4 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 50.0% | 33.3% | 33.3% | 33.3% | +7.3 | 3.19 | 4.78 | +17.3 | +7.6 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 41.7% | 30.0% | 30.0% | 30.0% | +7.2 | 2.73 | 5.46 | +17.2 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 20.8% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +2.3 | +5.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +5.3 | +5.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +3.2 | 2.07 | 4.82 | +11.8 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +3.2 | 2.07 | 4.82 | +11.8 | +6.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=+4.5; validation N=1 Fav=100.0% Avg=+8.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 41.7% | +2.4 | 1.74 | 4.05 | +12.0 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 41.7% | +2.4 | 1.74 | 4.05 | +12.0 | +7.4 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 41.7% | +2.4 | 1.74 | 4.05 | +12.0 | +7.4 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 41.7% | +2.4 | 1.74 | 4.05 | +12.0 | +7.4 |
| `asian_range_gte_30` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 42.9% | +0.8 | 1.15 | 2.31 | +12.5 | +6.9 |
| `confluence_gte_60` | 4 | R_REPEATER | 33.3% | 50.0% | 50.0% | 75.0% | +8.7 | 20.42 | 10.21 | +20.1 | +9.3 |
| `confluence_gte_70` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +5.6 | +5.6 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 33.3% | -1.6 | 0.63 | 1.26 | +14.3 | +6.4 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 41.7% | 40.0% | 40.0% | 40.0% | +5.2 | 2.79 | 4.19 | +16.6 | +5.6 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 42.9% | +0.8 | 1.15 | 2.31 | +12.5 | +6.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 33.3% | -1.6 | 0.63 | 1.26 | +14.3 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 41.7% | +2.4 | 1.74 | 4.05 | +12.0 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 41.7% | +2.4 | 1.74 | 4.05 | +12.0 | +7.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.8; validation N=9 Fav=33.3% Avg=+3.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +0.5 | 1.13 | 3.03 | +11.7 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +0.5 | 1.13 | 3.03 | +11.7 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +0.5 | 1.13 | 3.03 | +11.7 | +4.3 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +0.5 | 1.13 | 3.03 | +11.7 | +4.3 |
| `asian_range_gte_30` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 20.0% | -6.2 | 0.00 | 0.00 | +8.2 | +4.1 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +0.5 | 1.13 | 3.03 | +11.7 | +4.3 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +0.5 | 1.13 | 3.03 | +11.7 | +4.3 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 9.1% | +0.6 | 1.13 | 3.03 | +12.0 | +4.7 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 83.3% | 30.0% | 30.0% | 10.0% | +3.1 | 2.40 | 5.59 | +12.1 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 20.0% | -6.2 | 0.00 | 0.00 | +8.2 | +4.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -7.8 | 0.00 | 0.00 | +8.3 | +4.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +0.5 | 1.13 | 3.03 | +11.7 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +0.5 | 1.13 | 3.03 | +11.7 | +4.3 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 50.0% | -1.9 | 0.00 | 0.00 | +7.2 | +3.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +6.5 | +6.1 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=+4.5; validation N=2 Fav=0.0% Avg=-3.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.0 | 0.99 | 2.58 | +8.8 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 25.0% | 20.0% | 20.0% | 0.0% | -3.4 | 0.22 | 0.89 | +9.1 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 30.0% | 16.7% | 16.7% | 16.7% | -2.8 | 0.22 | 0.89 | +8.1 | +6.1 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.0 | 0.99 | 2.58 | +8.8 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.0 | 0.99 | 2.58 | +8.8 | +4.1 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.0 | 0.99 | 2.58 | +8.8 | +4.1 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 25.0% | 20.0% | 20.0% | 20.0% | +1.3 | 1.58 | 6.33 | +9.1 | +4.0 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 90.0% | 16.7% | 16.7% | 22.2% | -1.0 | 0.53 | 2.30 | +8.2 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.0 | 0.99 | 2.58 | +8.8 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.0 | 0.99 | 2.58 | +8.8 | +4.1 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 5.0% | 100.0% | 100.0% | 100.0% | +17.4 | 999.00 | 999.00 | +17.8 | +0.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 5.0% | 100.0% | 100.0% | 100.0% | +17.4 | 999.00 | 999.00 | +17.8 | +0.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=0.0% Avg=-5.7; validation N=14 Fav=28.6% Avg=-0.3; out_of_sample N=7 Fav=28.6% Avg=+2.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.2 | 0.96 | 2.41 | +8.1 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.2 | 0.96 | 2.41 | +8.1 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.2 | 0.96 | 2.41 | +8.1 | +6.4 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.2 | 0.96 | 2.41 | +8.1 | +6.4 |
| `asian_range_gte_30` | 11 | S_STRANGER | 45.8% | 0.0% | 0.0% | 9.1% | -6.3 | 0.00 | 0.00 | +2.9 | +7.6 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.2 | 0.96 | 2.41 | +8.1 | +6.4 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.2 | 0.96 | 2.41 | +8.1 | +6.4 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 20.8% | 0.0% | 0.0% | 0.0% | -8.7 | 0.00 | 0.00 | +1.8 | +9.6 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 75.0% | 16.7% | 16.7% | 11.1% | -2.6 | 0.42 | 1.81 | +5.7 | +7.2 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 45.8% | 0.0% | 0.0% | 9.1% | -6.3 | 0.00 | 0.00 | +2.9 | +7.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -10.9 | 0.00 | 0.00 | +0.6 | +11.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.2 | 0.96 | 2.41 | +8.1 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -0.2 | 0.96 | 2.41 | +8.1 | +6.4 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 8.3% | 0.0% | 0.0% | 50.0% | -1.8 | 0.00 | 0.00 | +5.2 | +3.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -3.6 | 0.00 | 0.00 | +2.4 | +5.6 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-4.5; validation N=8 Fav=50.0% Avg=+5.7; out_of_sample N=7 Fav=0.0% Avg=-3.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.4 | 0.91 | 2.43 | +7.8 | +4.7 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 16.7% | 25.0% | 25.0% | 25.0% | -1.3 | 0.76 | 2.29 | +6.2 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 33.3% | 25.0% | 25.0% | 25.0% | -0.5 | 0.84 | 2.11 | +5.1 | +5.8 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.4 | 0.91 | 2.43 | +7.8 | +4.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.4 | 0.91 | 2.43 | +7.8 | +4.7 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.4 | 0.91 | 2.43 | +7.8 | +4.7 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 45.8% | 9.1% | 9.1% | 9.1% | -4.1 | 0.29 | 2.57 | +5.8 | +5.3 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 70.8% | 23.5% | 23.5% | 11.8% | +0.7 | 1.19 | 3.57 | +8.2 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.4 | 0.91 | 2.43 | +7.8 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.4 | 0.91 | 2.43 | +7.8 | +4.7 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 8.3% | 50.0% | 50.0% | 50.0% | +7.2 | 6.33 | 6.33 | +11.2 | +2.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -2.7 | 0.00 | 0.00 | +2.3 | +3.4 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+5.2; validation N=3 Fav=66.7% Avg=+7.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -3.2 | 0.47 | 1.26 | +8.9 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 27.3% | -3.3 | 0.49 | 1.14 | +9.3 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 27.3% | -3.3 | 0.49 | 1.14 | +9.3 | +6.4 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -3.2 | 0.47 | 1.26 | +8.9 | +6.2 |
| `asian_range_gte_30` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 37.5% | +1.0 | 1.28 | 1.71 | +12.4 | +5.5 |
| `confluence_gte_60` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 20.0% | -3.2 | 0.17 | 0.52 | +7.5 | +4.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 42.9% | +2.7 | 2.22 | 2.22 | +14.1 | +6.1 |
| `tdi_rsi_gte_50` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 100.0% | +9.7 | 999.00 | 999.00 | +20.9 | +1.2 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 37.5% | +1.0 | 1.28 | 1.71 | +12.4 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 41.7% | 60.0% | 60.0% | 60.0% | +6.7 | 19.47 | 6.49 | +18.4 | +4.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -3.2 | 0.47 | 1.26 | +8.9 | +6.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | -3.2 | 0.47 | 1.26 | +8.9 | +6.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-6.6; validation N=2 Fav=100.0% Avg=+7.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 23.8% | -2.2 | 0.55 | 1.38 | +7.5 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 85.7% | 16.7% | 22.2% | 16.7% | -3.6 | 0.25 | 0.89 | +6.2 | +8.4 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 95.2% | 25.0% | 30.0% | 25.0% | -1.5 | 0.65 | 1.51 | +7.7 | +7.6 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 23.8% | -2.2 | 0.55 | 1.38 | +7.5 | +7.3 |
| `asian_range_gte_30` | 8 | S_STRANGER | 38.1% | 25.0% | 37.5% | 25.0% | -4.5 | 0.29 | 0.48 | +8.4 | +10.7 |
| `confluence_gte_60` | 9 | S_STRANGER | 42.9% | 22.2% | 33.3% | 22.2% | -4.2 | 0.27 | 0.54 | +6.8 | +10.9 |
| `confluence_gte_70` | 3 | S_STRANGER | 14.3% | 0.0% | 33.3% | 0.0% | -2.5 | 0.01 | 0.03 | +3.7 | +5.4 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 33.3% | 28.6% | 28.6% | 28.6% | -3.0 | 0.41 | 1.02 | +7.7 | +10.4 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 71.4% | 13.3% | 13.3% | 13.3% | -5.5 | 0.14 | 0.94 | +6.6 | +9.4 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 38.1% | 25.0% | 37.5% | 25.0% | -4.5 | 0.29 | 0.48 | +8.4 | +10.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 23.8% | 40.0% | 40.0% | 40.0% | -1.0 | 0.74 | 1.12 | +8.9 | +9.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 23.8% | -2.2 | 0.55 | 1.38 | +7.5 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 23.8% | -2.2 | 0.55 | 1.38 | +7.5 | +7.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=40.0% Avg=+2.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | +0.2 | 1.11 | 3.32 | +6.1 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +5.1 | +5.8 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 35.3% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +4.2 | +4.4 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | +0.2 | 1.11 | 3.32 | +6.1 | +3.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | +0.2 | 1.11 | 3.32 | +6.1 | +3.9 |
| `confluence_gte_70` | 14 | S_STRANGER | 82.4% | 28.6% | 28.6% | 14.3% | +1.6 | 2.16 | 4.86 | +6.4 | +3.3 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 52.9% | 22.2% | 22.2% | 11.1% | +0.6 | 1.32 | 4.63 | +5.8 | +4.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 58.8% | 40.0% | 40.0% | 20.0% | +2.7 | 2.98 | 4.47 | +7.3 | +3.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 82.4% | 21.4% | 21.4% | 7.1% | +0.2 | 1.08 | 3.59 | +5.9 | +3.9 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | +0.2 | 1.11 | 3.32 | +6.1 | +3.9 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 47.1% | 25.0% | 25.0% | 25.0% | +1.4 | 1.57 | 3.94 | +7.7 | +3.8 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 23.5% | 50.0% | 50.0% | 50.0% | +5.8 | 4.04 | 4.04 | +10.5 | +3.4 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=14 Fav=21.4% Avg=-1.0; validation N=3 Fav=33.3% Avg=-0.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | -0.9 | 0.76 | 2.46 | +7.8 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 29.4% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +7.3 | +10.4 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 35.3% | 16.7% | 16.7% | 0.0% | -2.9 | 0.36 | 1.80 | +8.0 | +9.0 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | -0.9 | 0.76 | 2.46 | +7.8 | +6.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | -0.9 | 0.76 | 2.46 | +7.8 | +6.5 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | -0.9 | 0.76 | 2.46 | +7.8 | +6.5 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 23.5% | 50.0% | 50.0% | 25.0% | +5.0 | 3.06 | 3.06 | +11.7 | +3.9 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 82.4% | 14.3% | 14.3% | 7.1% | -2.3 | 0.48 | 2.90 | +7.5 | +7.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | -0.9 | 0.76 | 2.46 | +7.8 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | -0.9 | 0.76 | 2.46 | +7.8 | +6.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=-3.5; validation N=5 Fav=40.0% Avg=-0.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 23.3% | 23.3% | 13.3% | -2.4 | 0.27 | 0.86 | +5.1 | +3.2 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 10.0% | 33.3% | 33.3% | 0.0% | +0.5 | 1.32 | 2.64 | +5.9 | +2.5 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 40.0% | 16.7% | 16.7% | 0.0% | -2.8 | 0.16 | 0.79 | +4.7 | +3.8 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 23.3% | 23.3% | 13.3% | -2.4 | 0.27 | 0.86 | +5.1 | +3.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 30.0% | 33.3% | 33.3% | 22.2% | -2.0 | 0.27 | 0.53 | +6.4 | +4.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 63.3% | 21.1% | 21.1% | 10.5% | -1.8 | 0.30 | 1.05 | +5.2 | +3.0 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 63.3% | 26.3% | 26.3% | 5.3% | -0.8 | 0.59 | 1.65 | +5.2 | +3.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +2.3 | +3.9 |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 86.7% | 26.9% | 26.9% | 15.4% | -2.4 | 0.30 | 0.77 | +5.4 | +3.1 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 23.3% | 23.3% | 13.3% | -2.4 | 0.27 | 0.86 | +5.1 | +3.2 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -2.1 | 0.00 | 0.00 | +2.8 | +3.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +3.8 | +4.9 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+9.0; validation N=1 Fav=100.0% Avg=+17.7; out_of_sample N=1 Fav=0.0% Avg=-5.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 38.5% | +2.8 | 2.48 | 6.61 | +8.0 | +2.9 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 46.2% | 16.7% | 16.7% | 16.7% | +1.5 | 1.76 | 8.78 | +6.2 | +3.2 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 69.2% | 11.1% | 11.1% | 33.3% | +0.3 | 1.15 | 6.93 | +5.9 | +3.0 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 38.5% | +2.8 | 2.48 | 6.61 | +8.0 | +2.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 69.2% | 33.3% | 33.3% | 55.6% | +5.2 | 4.25 | 5.66 | +10.9 | +2.4 |
| `confluence_gte_70` | 2 | R_RUNNER | 15.4% | 100.0% | 100.0% | 100.0% | +21.5 | 999.00 | 999.00 | +22.2 | +0.8 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 53.8% | 14.3% | 14.3% | 14.3% | +0.7 | 1.41 | 8.45 | +6.0 | +3.1 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 46.2% | 50.0% | 50.0% | 50.0% | +8.0 | 4.86 | 4.86 | +11.1 | +3.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 38.5% | +2.8 | 2.48 | 6.61 | +8.0 | +2.9 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 38.5% | +2.8 | 2.48 | 6.61 | +8.0 | +2.9 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 20.0% | +2.2 | 2.08 | 8.33 | +5.7 | +3.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 33.3% | +4.8 | 3.08 | 6.16 | +7.9 | +4.2 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=60.0% Avg=+7.1; validation N=4 Fav=0.0% Avg=-1.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 30.8% | +1.7 | 2.12 | 3.19 | +8.2 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 30.8% | 0.0% | 25.0% | 25.0% | -0.1 | 0.94 | 1.88 | +6.2 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 38.5% | 0.0% | 20.0% | 20.0% | -0.9 | 0.42 | 1.25 | +7.0 | +4.4 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 30.8% | +1.7 | 2.12 | 3.19 | +8.2 | +5.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 30.8% | +1.7 | 2.12 | 3.19 | +8.2 | +5.2 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 30.8% | +1.7 | 2.12 | 3.19 | +8.2 | +5.2 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 40.0% | +1.0 | 1.52 | 4.56 | +9.2 | +5.9 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 69.2% | 33.3% | 33.3% | 44.4% | +3.1 | 3.92 | 3.92 | +10.0 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 30.8% | +1.7 | 2.12 | 3.19 | +8.2 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 92.3% | 16.7% | 25.0% | 25.0% | +0.6 | 1.36 | 2.72 | +7.6 | +5.6 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 100.0% | +14.7 | 999.00 | 999.00 | +15.1 | +0.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 100.0% | +14.7 | 999.00 | 999.00 | +15.1 | +0.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=20.0% Avg=+0.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.0 | 0.74 | 1.99 | +12.8 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 84.6% | 18.2% | 18.2% | 27.3% | -2.3 | 0.43 | 1.51 | +13.1 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.0 | 0.74 | 1.99 | +12.8 | +6.5 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.0 | 0.74 | 1.99 | +12.8 | +6.5 |
| `asian_range_gte_30` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 60.0% | +0.8 | 1.31 | 2.61 | +11.0 | +5.2 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.0 | 0.74 | 1.99 | +12.8 | +6.5 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.0 | 0.74 | 1.99 | +12.8 | +6.5 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 92.3% | 16.7% | 16.7% | 25.0% | -2.5 | 0.39 | 1.57 | +12.1 | +7.0 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 61.5% | 37.5% | 37.5% | 12.5% | -0.3 | 0.95 | 1.58 | +17.4 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 75.0% | +2.2 | 1.97 | 1.97 | +13.5 | +5.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 75.0% | +2.2 | 1.97 | 1.97 | +13.5 | +5.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.0 | 0.74 | 1.99 | +12.8 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.0 | 0.74 | 1.99 | +12.8 | +6.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+2.2; validation N=3 Fav=33.3% Avg=-6.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 15.4% | -5.9 | 0.19 | 0.57 | +5.6 | +8.6 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 16.7% | 16.7% | 16.7% | -6.8 | 0.13 | 0.59 | +4.9 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 15.4% | -5.9 | 0.19 | 0.57 | +5.6 | +8.6 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 15.4% | -5.9 | 0.19 | 0.57 | +5.6 | +8.6 |
| `asian_range_gte_30` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 20.0% | -10.2 | 0.00 | 0.00 | +4.2 | +4.0 |
| `confluence_gte_60` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 0.0% | -4.0 | 0.25 | 0.75 | +3.9 | +4.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 38.5% | 40.0% | 40.0% | 20.0% | -2.8 | 0.46 | 0.69 | +6.8 | +4.2 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 0.0% | -3.5 | 0.28 | 0.83 | +4.5 | +4.6 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 20.0% | -10.2 | 0.00 | 0.00 | +4.2 | +4.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -21.4 | 0.00 | 0.00 | +5.8 | +0.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 15.4% | -5.9 | 0.19 | 0.57 | +5.6 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 15.4% | -5.9 | 0.19 | 0.57 | +5.6 | +8.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=38.5% Avg=-2.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=100.0% Avg=+15.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 22.9% | 25.7% | 14.3% | -3.4 | 0.39 | 1.09 | +5.9 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 88.6% | 25.8% | 25.8% | 16.1% | -3.8 | 0.37 | 1.01 | +6.1 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 34 | S_STRANGER | 97.1% | 23.5% | 26.5% | 14.7% | -3.3 | 0.41 | 1.10 | +6.1 | +6.5 |
| `stop_hunt_le_90` | 35 | S_STRANGER | 100.0% | 22.9% | 25.7% | 14.3% | -3.4 | 0.39 | 1.09 | +5.9 | +6.6 |
| `asian_range_gte_30` | 16 | S_STRANGER | 45.7% | 25.0% | 31.2% | 25.0% | -3.8 | 0.38 | 0.76 | +7.1 | +6.9 |
| `confluence_gte_60` | 26 | S_STRANGER | 74.3% | 23.1% | 23.1% | 19.2% | -3.0 | 0.35 | 1.12 | +5.4 | +6.7 |
| `confluence_gte_70` | 8 | S_STRANGER | 22.9% | 12.5% | 12.5% | 12.5% | -5.1 | 0.06 | 0.40 | +2.8 | +8.2 |
| `tdi_rsi_gt_signal` | 24 | S_STRANGER | 68.6% | 20.8% | 25.0% | 4.2% | -2.9 | 0.49 | 1.46 | +6.9 | +8.1 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 40.0% | 42.9% | 42.9% | 14.3% | -0.8 | 0.83 | 1.11 | +9.9 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 40.0% | 28.6% | 28.6% | 28.6% | -5.0 | 0.29 | 0.64 | +7.0 | +6.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 22.9% | 25.0% | 25.0% | 12.5% | -6.4 | 0.27 | 0.82 | +8.4 | +10.4 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 2.9% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +4.2 | +7.3 |
| `feature_extreme_hunt_with_exception` | 35 | S_STRANGER | 100.0% | 22.9% | 25.7% | 14.3% | -3.4 | 0.39 | 1.09 | +5.9 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 35 | S_STRANGER | 100.0% | 22.9% | 25.7% | 14.3% | -3.4 | 0.39 | 1.09 | +5.9 | +6.6 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 25.7% | 33.3% | 33.3% | 11.1% | -2.3 | 0.60 | 1.21 | +6.0 | +4.8 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 11.4% | 50.0% | 50.0% | 0.0% | +2.1 | 1.49 | 1.49 | +10.1 | +7.4 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=14.3% Avg=-0.9; validation N=3 Fav=66.7% Avg=+8.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 57 | S_STRANGER | 100.0% | 22.8% | 24.6% | 21.1% | +0.3 | 1.08 | 2.77 | +8.6 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 51 | S_STRANGER | 89.5% | 21.6% | 23.5% | 19.6% | -0.6 | 0.82 | 2.27 | +7.6 | +6.2 |
| `hunt_to_ar_ratio_le_2_5` | 54 | S_STRANGER | 94.7% | 22.2% | 24.1% | 20.4% | -0.6 | 0.81 | 2.12 | +8.0 | +6.2 |
| `stop_hunt_le_90` | 57 | S_STRANGER | 100.0% | 22.8% | 24.6% | 21.1% | +0.3 | 1.08 | 2.77 | +8.6 | +6.1 |
| `asian_range_gte_30` | 40 | S_STRANGER | 70.2% | 25.0% | 27.5% | 17.5% | +0.6 | 1.20 | 2.74 | +7.9 | +5.8 |
| `confluence_gte_60` | 28 | S_STRANGER | 49.1% | 28.6% | 32.1% | 14.3% | +0.3 | 1.09 | 1.93 | +8.8 | +6.2 |
| `confluence_gte_70` | 9 | S_STRANGER | 15.8% | 22.2% | 22.2% | 11.1% | +2.0 | 1.68 | 5.04 | +9.9 | +5.3 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 24.6% | 28.6% | 28.6% | 28.6% | +4.5 | 2.60 | 5.19 | +12.6 | +6.5 |
| `tdi_rsi_gte_50` | 40 | S_STRANGER | 70.2% | 22.5% | 25.0% | 12.5% | +0.4 | 1.13 | 2.93 | +9.1 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 40 | S_STRANGER | 70.2% | 25.0% | 27.5% | 17.5% | +0.6 | 1.20 | 2.74 | +7.9 | +5.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 17.5% | 30.0% | 30.0% | 20.0% | +1.8 | 1.54 | 3.07 | +9.7 | +7.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 55 | S_STRANGER | 96.5% | 23.6% | 25.5% | 21.8% | +0.4 | 1.11 | 2.70 | +8.6 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 57 | S_STRANGER | 100.0% | 22.8% | 24.6% | 21.1% | +0.3 | 1.08 | 2.77 | +8.6 | +6.1 |
| `feature_momentum_breakout_exception` | 15 | S_STRANGER | 26.3% | 6.7% | 6.7% | 20.0% | -1.7 | 0.31 | 3.39 | +5.9 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 9 | S_STRANGER | 15.8% | 11.1% | 11.1% | 0.0% | -1.6 | 0.44 | 3.48 | +6.8 | +5.4 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=1 Fav=0.0% Avg=+7.1; out_of_sample N=6 Fav=33.3% Avg=+3.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 22.6% | 29.0% | 25.8% | -0.4 | 0.90 | 1.80 | +7.7 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 71.0% | 22.7% | 27.3% | 22.7% | -0.6 | 0.86 | 2.00 | +7.8 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 28 | S_STRANGER | 90.3% | 25.0% | 28.6% | 28.6% | +0.3 | 1.08 | 2.15 | +8.2 | +4.9 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 22.6% | 29.0% | 25.8% | -0.4 | 0.90 | 1.80 | +7.7 | +4.9 |
| `asian_range_gte_30` | 11 | S_STRANGER | 35.5% | 9.1% | 9.1% | 0.0% | -4.4 | 0.05 | 0.53 | +4.2 | +4.8 |
| `confluence_gte_60` | 23 | S_STRANGER | 74.2% | 26.1% | 30.4% | 30.4% | -0.0 | 0.99 | 1.84 | +8.1 | +5.1 |
| `confluence_gte_70` | 7 | S_STRANGER | 22.6% | 28.6% | 42.9% | 42.9% | +4.1 | 5.82 | 5.82 | +8.3 | +3.6 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 48.4% | 20.0% | 26.7% | 26.7% | -1.5 | 0.67 | 1.69 | +6.2 | +5.7 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 38.7% | 16.7% | 16.7% | 16.7% | -3.4 | 0.40 | 1.80 | +6.6 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 32.3% | 10.0% | 10.0% | 0.0% | -4.3 | 0.06 | 0.53 | +4.5 | +4.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 16.1% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +2.2 | +5.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 22.6% | 29.0% | 25.8% | -0.4 | 0.90 | 1.80 | +7.7 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 22.6% | 29.0% | 25.8% | -0.4 | 0.90 | 1.80 | +7.7 | +4.9 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 9.7% | 0.0% | 0.0% | 0.0% | -2.7 | 0.00 | 0.00 | +1.6 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 6.5% | 0.0% | 0.0% | 0.0% | -4.1 | 0.00 | 0.00 | +2.1 | +5.0 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+13.9; validation N=5 Fav=40.0% Avg=+3.3; out_of_sample N=1 Fav=0.0% Avg=-20.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 21.7% | 30.4% | 26.1% | -0.0 | 0.99 | 1.85 | +9.2 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 100.0% | 21.7% | 30.4% | 26.1% | -0.0 | 0.99 | 1.85 | +9.2 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 21.7% | 30.4% | 26.1% | -0.0 | 0.99 | 1.85 | +9.2 | +4.3 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 21.7% | 30.4% | 26.1% | -0.0 | 0.99 | 1.85 | +9.2 | +4.3 |
| `asian_range_gte_30` | 12 | S_STRANGER | 52.2% | 16.7% | 16.7% | 33.3% | -0.3 | 0.88 | 3.51 | +8.1 | +2.9 |
| `confluence_gte_60` | 22 | S_STRANGER | 95.7% | 22.7% | 31.8% | 27.3% | +0.0 | 1.02 | 1.74 | +9.5 | +4.3 |
| `confluence_gte_70` | 2 | S_STRANGER | 8.7% | 0.0% | 0.0% | 50.0% | -10.0 | 0.00 | 0.00 | +12.6 | +12.5 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 87.0% | 25.0% | 35.0% | 30.0% | +0.7 | 1.24 | 1.77 | +10.3 | +4.5 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 30.4% | 42.9% | 42.9% | 28.6% | +1.5 | 1.29 | 1.71 | +15.7 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 52.2% | 16.7% | 16.7% | 33.3% | -0.3 | 0.88 | 3.51 | +8.1 | +2.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 43.5% | 20.0% | 20.0% | 40.0% | +0.6 | 1.30 | 3.91 | +9.3 | +3.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 21.7% | 30.4% | 26.1% | -0.0 | 0.99 | 1.85 | +9.2 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 21.7% | 30.4% | 26.1% | -0.0 | 0.99 | 1.85 | +9.2 | +4.3 |
| `feature_momentum_breakout_exception` | 2 | R_RUNNER | 8.7% | 100.0% | 100.0% | 50.0% | +8.6 | 999.00 | 999.00 | +14.3 | +1.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 4.3% | 100.0% | 100.0% | 100.0% | +13.9 | 999.00 | 999.00 | +24.0 | +0.4 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-1.4; validation N=7 Fav=57.1% Avg=-2.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 21.6% | 24.3% | 18.9% | -3.9 | 0.25 | 0.70 | +5.2 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 8 | R_REPEATER | 21.6% | 50.0% | 50.0% | 12.5% | -2.2 | 0.27 | 0.27 | +7.1 | +4.2 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 54.1% | 25.0% | 30.0% | 20.0% | -2.8 | 0.19 | 0.39 | +4.3 | +4.4 |
| `stop_hunt_le_90` | 37 | S_STRANGER | 100.0% | 21.6% | 24.3% | 18.9% | -3.9 | 0.25 | 0.70 | +5.2 | +5.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 33 | S_STRANGER | 89.2% | 21.2% | 24.2% | 21.2% | -3.8 | 0.28 | 0.76 | +5.2 | +5.2 |
| `confluence_gte_70` | 5 | S_STRANGER | 13.5% | 20.0% | 20.0% | 20.0% | -2.3 | 0.41 | 1.65 | +4.5 | +4.7 |
| `tdi_rsi_gt_signal` | 28 | S_STRANGER | 75.7% | 21.4% | 25.0% | 17.9% | -4.0 | 0.25 | 0.68 | +5.2 | +5.7 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 27.0% | 20.0% | 20.0% | 0.0% | -2.2 | 0.26 | 1.05 | +5.6 | +6.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 37 | S_STRANGER | 100.0% | 21.6% | 24.3% | 18.9% | -3.9 | 0.25 | 0.70 | +5.2 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 21.6% | 24.3% | 18.9% | -3.9 | 0.25 | 0.70 | +5.2 | +5.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-1.0; validation N=2 Fav=50.0% Avg=+5.4; out_of_sample N=1 Fav=0.0% Avg=-4.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 28.6% | -1.5 | 0.60 | 1.81 | +5.8 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 42.9% | 25.0% | 25.0% | 25.0% | -0.2 | 0.95 | 2.85 | +5.7 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 67.9% | 15.8% | 15.8% | 21.1% | -1.3 | 0.60 | 2.78 | +4.3 | +4.9 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 28.6% | -1.5 | 0.60 | 1.81 | +5.8 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 64.3% | 27.8% | 27.8% | 27.8% | -2.3 | 0.54 | 1.30 | +6.2 | +4.8 |
| `confluence_gte_70` | 4 | R_REPEATER | 14.3% | 50.0% | 50.0% | 50.0% | -2.1 | 0.78 | 0.78 | +12.2 | +2.6 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 21.4% | 16.7% | 16.7% | 33.3% | +0.5 | 1.42 | 4.26 | +5.8 | +2.9 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 57.1% | 18.8% | 18.8% | 18.8% | -1.5 | 0.46 | 1.70 | +5.7 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 28.6% | -1.5 | 0.60 | 1.81 | +5.8 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 28.6% | -1.5 | 0.60 | 1.81 | +5.8 | +4.1 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 3.6% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +1.0 | +3.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.6% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +1.0 | +3.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=33.3% Avg=+0.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | S_STRANGER | 100.0% | 21.2% | 24.2% | 27.3% | -0.6 | 0.76 | 2.10 | +5.0 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 33.3% | 9.1% | 18.2% | 18.2% | -2.2 | 0.22 | 0.87 | +2.8 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 51.5% | 17.6% | 23.5% | 29.4% | -0.9 | 0.61 | 1.68 | +4.4 | +3.9 |
| `stop_hunt_le_90` | 33 | S_STRANGER | 100.0% | 21.2% | 24.2% | 27.3% | -0.6 | 0.76 | 2.10 | +5.0 | +4.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 36.4% | 33.3% | 41.7% | 41.7% | +0.9 | 1.35 | 1.62 | +5.5 | +4.0 |
| `confluence_gte_70` | 3 | S_STRANGER | 9.1% | 33.3% | 33.3% | 66.7% | +0.1 | 1.06 | 1.06 | +5.7 | +3.1 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 63.6% | 23.8% | 23.8% | 38.1% | -0.4 | 0.84 | 2.19 | +5.6 | +4.3 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 69.7% | 26.1% | 26.1% | 30.4% | -0.1 | 0.96 | 2.39 | +5.8 | +4.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 33 | S_STRANGER | 100.0% | 21.2% | 24.2% | 27.3% | -0.6 | 0.76 | 2.10 | +5.0 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 33 | S_STRANGER | 100.0% | 21.2% | 24.2% | 27.3% | -0.6 | 0.76 | 2.10 | +5.0 | +4.4 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +2.8 | +4.9 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 15.2% | 0.0% | 0.0% | 0.0% | -2.9 | 0.00 | 0.00 | +3.3 | +4.8 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=10 Fav=20.0% Avg=-1.2; out_of_sample N=13 Fav=38.5% Avg=-2.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 44 | S_STRANGER | 100.0% | 20.5% | 20.5% | 11.4% | -2.5 | 0.38 | 1.35 | +6.0 | +7.5 |
| `hunt_to_ar_ratio_le_2_0` | 33 | S_STRANGER | 75.0% | 15.2% | 15.2% | 12.1% | -2.6 | 0.34 | 1.68 | +5.7 | +8.0 |
| `hunt_to_ar_ratio_le_2_5` | 40 | S_STRANGER | 90.9% | 20.0% | 20.0% | 10.0% | -2.2 | 0.38 | 1.39 | +6.2 | +7.6 |
| `stop_hunt_le_90` | 44 | S_STRANGER | 100.0% | 20.5% | 20.5% | 11.4% | -2.5 | 0.38 | 1.35 | +6.0 | +7.5 |
| `asian_range_gte_30` | 21 | S_STRANGER | 47.7% | 19.0% | 19.0% | 9.5% | -3.3 | 0.25 | 0.93 | +6.7 | +7.8 |
| `confluence_gte_60` | 44 | S_STRANGER | 100.0% | 20.5% | 20.5% | 11.4% | -2.5 | 0.38 | 1.35 | +6.0 | +7.5 |
| `confluence_gte_70` | 44 | S_STRANGER | 100.0% | 20.5% | 20.5% | 11.4% | -2.5 | 0.38 | 1.35 | +6.0 | +7.5 |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 52.3% | 30.4% | 30.4% | 8.7% | -1.7 | 0.59 | 1.26 | +6.7 | +8.0 |
| `tdi_rsi_gte_50` | 26 | S_STRANGER | 59.1% | 19.2% | 19.2% | 7.7% | -3.1 | 0.33 | 1.31 | +6.4 | +9.1 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 40.9% | 16.7% | 16.7% | 11.1% | -3.7 | 0.22 | 0.95 | +6.2 | +8.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 15.9% | 28.6% | 28.6% | 0.0% | -2.7 | 0.47 | 1.17 | +6.4 | +9.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 44 | S_STRANGER | 100.0% | 20.5% | 20.5% | 11.4% | -2.5 | 0.38 | 1.35 | +6.0 | +7.5 |
| `feature_stale_hod_exhaustion_reject` | 44 | S_STRANGER | 100.0% | 20.5% | 20.5% | 11.4% | -2.5 | 0.38 | 1.35 | +6.0 | +7.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+9.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=14.3% Avg=-0.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 20.0% | +1.4 | 1.57 | 4.40 | +6.7 | +5.8 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 40.0% | 25.0% | 37.5% | 12.5% | +3.5 | 2.39 | 3.98 | +8.9 | +8.9 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 80.0% | 18.8% | 25.0% | 18.8% | +1.3 | 1.47 | 4.05 | +7.2 | +6.4 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 20.0% | +1.4 | 1.57 | 4.40 | +6.7 | +5.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 60.0% | 16.7% | 25.0% | 8.3% | +0.5 | 1.15 | 3.46 | +6.7 | +7.2 |
| `confluence_gte_70` | 2 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -3.3 | 0.00 | 0.00 | +1.3 | +9.3 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 60.0% | 25.0% | 33.3% | 16.7% | +3.6 | 3.00 | 6.01 | +8.2 | +6.1 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 60.0% | 25.0% | 25.0% | 16.7% | +2.7 | 2.51 | 7.54 | +7.5 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 20.0% | +1.4 | 1.57 | 4.40 | +6.7 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 20.0% | +1.4 | 1.57 | 4.40 | +6.7 | +5.8 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 10.0% | 0.0% | 50.0% | 0.0% | +1.7 | 2.59 | 2.59 | +5.7 | +5.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +3.7 | +4.4 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=22.2% Avg=+0.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 50.0% | +0.7 | 1.17 | 1.56 | +11.2 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 50.0% | +0.7 | 1.17 | 1.56 | +11.2 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 50.0% | +0.7 | 1.17 | 1.56 | +11.2 | +6.5 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 50.0% | +0.7 | 1.17 | 1.56 | +11.2 | +6.5 |
| `asian_range_gte_30` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 55.6% | +0.7 | 1.14 | 2.29 | +12.2 | +7.0 |
| `confluence_gte_60` | 6 | S_STRANGER | 60.0% | 16.7% | 33.3% | 50.0% | +3.7 | 2.26 | 2.26 | +12.3 | +5.3 |
| `confluence_gte_70` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 100.0% | +12.8 | 999.00 | 999.00 | +20.5 | +3.6 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -22.6 | 0.00 | 0.00 | +1.7 | +22.7 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -0.2 | 0.98 | 2.93 | +14.8 | +13.0 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 55.6% | +0.7 | 1.14 | 2.29 | +12.2 | +7.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -22.6 | 0.00 | 0.00 | +1.7 | +22.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 50.0% | +0.7 | 1.17 | 1.56 | +11.2 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 50.0% | +0.7 | 1.17 | 1.56 | +11.2 | +6.5 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 66.7% | -1.0 | 0.00 | 0.00 | +7.2 | +2.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -22.6 | 0.00 | 0.00 | +1.7 | +22.7 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+3.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 26.7% | +0.4 | 1.08 | 3.94 | +8.5 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 26.7% | +0.4 | 1.08 | 3.94 | +8.5 | +8.2 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 26.7% | +0.4 | 1.08 | 3.94 | +8.5 | +8.2 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 26.7% | +0.4 | 1.08 | 3.94 | +8.5 | +8.2 |
| `asian_range_gte_30` | 9 | S_STRANGER | 60.0% | 22.2% | 22.2% | 33.3% | +0.9 | 1.18 | 3.55 | +8.8 | +8.1 |
| `confluence_gte_60` | 10 | S_STRANGER | 66.7% | 30.0% | 30.0% | 40.0% | +3.6 | 1.95 | 3.89 | +10.9 | +7.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 93.3% | 14.3% | 14.3% | 21.4% | -1.3 | 0.74 | 4.05 | +7.4 | +8.7 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 53.3% | 12.5% | 12.5% | 12.5% | -3.2 | 0.50 | 3.47 | +7.2 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 60.0% | 22.2% | 22.2% | 33.3% | +0.9 | 1.18 | 3.55 | +8.8 | +8.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 60.0% | 22.2% | 22.2% | 33.3% | +0.9 | 1.18 | 3.55 | +8.8 | +8.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 26.7% | +0.4 | 1.08 | 3.94 | +8.5 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 86.7% | 23.1% | 23.1% | 30.8% | +2.4 | 1.73 | 5.18 | +9.2 | +7.4 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 40.0% | 33.3% | 33.3% | 50.0% | +3.6 | 1.74 | 2.61 | +11.3 | +8.0 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 33.3% | 20.0% | 20.0% | 20.0% | -3.4 | 0.59 | 2.37 | +7.9 | +10.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+3.5; validation N=6 Fav=50.0% Avg=+2.2; out_of_sample N=2 Fav=0.0% Avg=-1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 20.0% | 20.0% | 12.0% | -1.6 | 0.54 | 2.16 | +4.9 | +4.7 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 36.0% | 44.4% | 44.4% | 22.2% | +1.4 | 1.77 | 2.21 | +7.3 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 68.0% | 23.5% | 23.5% | 11.8% | -1.6 | 0.53 | 1.72 | +4.8 | +5.1 |
| `stop_hunt_le_90` | 25 | S_STRANGER | 100.0% | 20.0% | 20.0% | 12.0% | -1.6 | 0.54 | 2.16 | +4.9 | +4.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 19 | S_STRANGER | 76.0% | 26.3% | 26.3% | 15.8% | -0.1 | 0.96 | 2.69 | +5.4 | +3.8 |
| `confluence_gte_70` | 2 | R_REPEATER | 8.0% | 50.0% | 50.0% | 50.0% | +8.7 | 44.75 | 44.75 | +12.2 | +2.0 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 72.0% | 11.1% | 11.1% | 0.0% | -3.8 | 0.13 | 1.05 | +3.4 | +5.1 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 52.0% | 15.4% | 15.4% | 0.0% | -3.0 | 0.21 | 1.14 | +4.0 | +6.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 100.0% | 20.0% | 20.0% | 12.0% | -1.6 | 0.54 | 2.16 | +4.9 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 20.0% | 20.0% | 12.0% | -1.6 | 0.54 | 2.16 | +4.9 | +4.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-2.3; validation N=6 Fav=33.3% Avg=+0.7; out_of_sample N=4 Fav=25.0% Avg=-0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -1.7 | 0.51 | 1.86 | +7.2 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 86.7% | 23.1% | 23.1% | 15.4% | -1.6 | 0.56 | 1.87 | +7.4 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 86.7% | 23.1% | 23.1% | 15.4% | -1.6 | 0.56 | 1.87 | +7.4 | +5.6 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -1.7 | 0.51 | 1.86 | +7.2 | +5.5 |
| `asian_range_gte_30` | 13 | S_STRANGER | 43.3% | 23.1% | 23.1% | 15.4% | -0.8 | 0.76 | 2.54 | +9.3 | +6.3 |
| `confluence_gte_60` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -1.7 | 0.51 | 1.86 | +7.2 | +5.5 |
| `confluence_gte_70` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -1.7 | 0.51 | 1.86 | +7.2 | +5.5 |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 76.7% | 21.7% | 21.7% | 17.4% | -1.3 | 0.63 | 2.14 | +7.8 | +5.8 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 50.0% | 13.3% | 13.3% | 13.3% | -4.0 | 0.23 | 1.37 | +8.6 | +7.7 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 43.3% | 23.1% | 23.1% | 15.4% | -0.8 | 0.76 | 2.54 | +9.3 | +6.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 36.7% | 27.3% | 27.3% | 18.2% | -0.1 | 0.98 | 2.62 | +10.7 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -1.7 | 0.51 | 1.86 | +7.2 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 96.7% | 20.7% | 20.7% | 20.7% | -1.7 | 0.52 | 1.82 | +7.2 | +5.5 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -2.3 | 0.00 | 0.00 | +4.7 | +5.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -2.3 | 0.00 | 0.00 | +4.7 | +5.5 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-3.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=20.0% Avg=-4.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.0 | 0.38 | 0.89 | +4.7 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 40.0% | 25.0% | 50.0% | 0.0% | -1.9 | 0.57 | 0.57 | +5.1 | +3.0 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 70.0% | 14.3% | 28.6% | 0.0% | -5.0 | 0.22 | 0.56 | +3.7 | +4.0 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.0 | 0.38 | 0.89 | +4.7 | +5.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 80.0% | 12.5% | 25.0% | 0.0% | -5.6 | 0.25 | 0.76 | +4.1 | +6.8 |
| `confluence_gte_70` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +14.8 | 999.00 | 999.00 | +19.2 | +7.5 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 0.0% | +1.0 | 1.21 | 1.21 | +8.3 | +7.8 |
| `tdi_rsi_gte_50` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 0.0% | +1.0 | 1.21 | 1.21 | +8.3 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.0 | 0.38 | 0.89 | +4.7 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.0 | 0.38 | 0.89 | +4.7 | +5.9 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 20.0% | 0.0% | 50.0% | 0.0% | -2.2 | 0.10 | 0.10 | +3.9 | +3.1 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=33.3% Avg=-7.5; out_of_sample N=4 Fav=25.0% Avg=-19.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -14.2 | 0.19 | 0.44 | +5.6 | +2.2 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 22.2% | 33.3% | 22.2% | -12.5 | 0.23 | 0.45 | +5.9 | +2.5 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -14.2 | 0.19 | 0.44 | +5.6 | +2.2 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -14.2 | 0.19 | 0.44 | +5.6 | +2.2 |
| `asian_range_gte_30` | 7 | S_STRANGER | 70.0% | 28.6% | 42.9% | 28.6% | -14.6 | 0.24 | 0.32 | +5.5 | +2.8 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -14.2 | 0.19 | 0.44 | +5.6 | +2.2 |
| `confluence_gte_70` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -27.0 | 0.00 | 0.00 | +3.5 | +4.1 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.3 | 0.00 | 0.00 | +13.9 | +2.5 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.3 | 0.00 | 0.00 | +13.9 | +2.5 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 28.6% | 42.9% | 28.6% | -14.6 | 0.24 | 0.32 | +5.5 | +2.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -14.2 | 0.19 | 0.44 | +5.6 | +2.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -14.2 | 0.19 | 0.44 | +5.6 | +2.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-1.0; validation N=5 Fav=40.0% Avg=+3.4; out_of_sample N=5 Fav=40.0% Avg=+1.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 19.2% | 23.1% | 34.6% | -0.2 | 0.93 | 2.17 | +7.1 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 100.0% | 19.2% | 23.1% | 34.6% | -0.2 | 0.93 | 2.17 | +7.1 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 100.0% | 19.2% | 23.1% | 34.6% | -0.2 | 0.93 | 2.17 | +7.1 | +5.6 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 19.2% | 23.1% | 34.6% | -0.2 | 0.93 | 2.17 | +7.1 | +5.6 |
| `asian_range_gte_30` | 11 | S_STRANGER | 42.3% | 0.0% | 0.0% | 27.3% | -2.1 | 0.00 | 0.00 | +4.1 | +6.9 |
| `confluence_gte_60` | 24 | S_STRANGER | 92.3% | 20.8% | 25.0% | 33.3% | +0.0 | 1.00 | 2.17 | +7.3 | +5.7 |
| `confluence_gte_70` | 4 | R_REPEATER | 15.4% | 50.0% | 50.0% | 25.0% | -0.1 | 0.94 | 0.94 | +11.1 | +7.9 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 42.3% | 27.3% | 27.3% | 36.4% | +1.2 | 1.96 | 3.93 | +9.8 | +4.4 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 42.3% | 36.4% | 36.4% | 27.3% | +2.3 | 2.24 | 3.92 | +11.1 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 42.3% | 0.0% | 0.0% | 27.3% | -2.1 | 0.00 | 0.00 | +4.1 | +6.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 19.2% | 0.0% | 0.0% | 40.0% | -1.5 | 0.00 | 0.00 | +6.8 | +4.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 19.2% | 23.1% | 34.6% | -0.2 | 0.93 | 2.17 | +7.1 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 19.2% | 23.1% | 34.6% | -0.2 | 0.93 | 2.17 | +7.1 | +5.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+4.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 19.2% | 19.2% | 34.6% | -2.0 | 0.49 | 1.48 | +7.1 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 92.3% | 20.8% | 20.8% | 37.5% | -1.0 | 0.67 | 1.75 | +7.0 | +5.9 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 100.0% | 19.2% | 19.2% | 34.6% | -2.0 | 0.49 | 1.48 | +7.1 | +6.7 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 19.2% | 19.2% | 34.6% | -2.0 | 0.49 | 1.48 | +7.1 | +6.7 |
| `asian_range_gte_30` | 11 | S_STRANGER | 42.3% | 18.2% | 18.2% | 36.4% | -2.0 | 0.57 | 2.00 | +6.6 | +4.6 |
| `confluence_gte_60` | 10 | S_STRANGER | 38.5% | 0.0% | 0.0% | 20.0% | -4.8 | 0.00 | 0.00 | +6.9 | +7.2 |
| `confluence_gte_70` | 2 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +8.4 | +7.4 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 46.2% | 8.3% | 8.3% | 33.3% | -3.0 | 0.27 | 1.91 | +7.5 | +9.7 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 53.8% | 7.1% | 7.1% | 21.4% | -3.4 | 0.22 | 2.20 | +7.0 | +9.4 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 38.5% | 20.0% | 20.0% | 40.0% | -1.3 | 0.70 | 2.10 | +6.8 | +3.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 15.4% | 25.0% | 25.0% | 50.0% | +2.1 | 2.63 | 5.25 | +8.6 | +3.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 19.2% | 19.2% | 34.6% | -2.0 | 0.49 | 1.48 | +7.1 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 19.2% | 19.2% | 34.6% | -2.0 | 0.49 | 1.48 | +7.1 | +6.7 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 23.1% | 33.3% | 33.3% | 50.0% | +4.0 | 5.25 | 7.87 | +8.3 | +2.8 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 15.4% | 25.0% | 25.0% | 25.0% | +1.9 | 2.35 | 7.05 | +6.4 | +3.7 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+2.5; validation N=1 Fav=0.0% Avg=-0.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 18.8% | 31.2% | 28.1% | +0.3 | 1.10 | 1.98 | +8.4 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 27 | S_STRANGER | 84.4% | 18.5% | 29.6% | 25.9% | -0.1 | 0.97 | 1.94 | +8.2 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 96.9% | 19.4% | 32.3% | 29.0% | +0.5 | 1.14 | 1.94 | +8.4 | +6.2 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 100.0% | 18.8% | 31.2% | 28.1% | +0.3 | 1.10 | 1.98 | +8.4 | +6.1 |
| `asian_range_gte_30` | 20 | S_STRANGER | 62.5% | 25.0% | 40.0% | 35.0% | +0.9 | 1.29 | 1.45 | +9.0 | +6.2 |
| `confluence_gte_60` | 24 | S_STRANGER | 75.0% | 12.5% | 25.0% | 20.8% | -1.3 | 0.66 | 1.77 | +6.9 | +7.1 |
| `confluence_gte_70` | 7 | S_STRANGER | 21.9% | 28.6% | 28.6% | 42.9% | +2.1 | 1.67 | 3.34 | +9.1 | +6.6 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 34.4% | 27.3% | 27.3% | 27.3% | -1.1 | 0.81 | 1.89 | +12.3 | +7.8 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 40.6% | 23.1% | 23.1% | 23.1% | -1.2 | 0.78 | 2.33 | +10.9 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 53.1% | 23.5% | 35.3% | 29.4% | +0.0 | 1.01 | 1.52 | +8.3 | +6.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 15.6% | 20.0% | 20.0% | 0.0% | -7.2 | 0.21 | 0.86 | +7.5 | +10.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 90.6% | 17.2% | 27.6% | 24.1% | -0.2 | 0.93 | 2.10 | +8.0 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 18.8% | 31.2% | 28.1% | +0.3 | 1.10 | 1.98 | +8.4 | +6.1 |
| `feature_momentum_breakout_exception` | 14 | S_STRANGER | 43.8% | 14.3% | 21.4% | 35.7% | -0.5 | 0.85 | 2.28 | +8.6 | +6.8 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 21.9% | 28.6% | 28.6% | 42.9% | +0.8 | 1.15 | 2.29 | +13.5 | +7.7 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=33.3% Avg=+0.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -2.5 | 0.37 | 1.34 | +6.5 | +7.6 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -2.5 | 0.37 | 1.34 | +6.5 | +7.6 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -2.5 | 0.37 | 1.34 | +6.5 | +7.6 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -2.5 | 0.37 | 1.34 | +6.5 | +7.6 |
| `asian_range_gte_30` | 7 | S_STRANGER | 43.8% | 14.3% | 14.3% | 42.9% | -0.6 | 0.70 | 2.79 | +7.2 | +6.1 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -2.5 | 0.37 | 1.34 | +6.5 | +7.6 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -2.5 | 0.37 | 1.34 | +6.5 | +7.6 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 68.8% | 27.3% | 27.3% | 27.3% | -0.8 | 0.72 | 1.93 | +7.9 | +5.2 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 37.5% | 33.3% | 33.3% | 33.3% | +0.5 | 1.22 | 2.43 | +12.3 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 43.8% | 14.3% | 14.3% | 42.9% | -0.6 | 0.70 | 2.79 | +7.2 | +6.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 20.0% | -0.9 | 0.70 | 2.79 | +7.4 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -2.5 | 0.37 | 1.34 | +6.5 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -2.5 | 0.37 | 1.34 | +6.5 | +7.6 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 31.2% | 0.0% | 0.0% | 40.0% | -2.8 | 0.00 | 0.00 | +5.9 | +5.9 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 25.0% | 25.0% | 25.0% | 25.0% | -1.7 | 0.51 | 1.52 | +9.3 | +5.5 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=33.3% Avg=-0.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-17.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 18.8% | 25.0% | 18.8% | -4.1 | 0.30 | 0.82 | +7.7 | +8.3 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 81.2% | 7.7% | 15.4% | 7.7% | -5.8 | 0.06 | 0.32 | +5.9 | +8.2 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 18.8% | 25.0% | 18.8% | -4.1 | 0.30 | 0.82 | +7.7 | +8.3 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 18.8% | 25.0% | 18.8% | -4.1 | 0.30 | 0.82 | +7.7 | +8.3 |
| `asian_range_gte_30` | 7 | S_STRANGER | 43.8% | 28.6% | 28.6% | 28.6% | -3.0 | 0.50 | 1.25 | +11.1 | +5.6 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 18.8% | 25.0% | 18.8% | -4.1 | 0.30 | 0.82 | +7.7 | +8.3 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 18.8% | 25.0% | 18.8% | -4.1 | 0.30 | 0.82 | +7.7 | +8.3 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -7.5 | 0.00 | 0.00 | +3.8 | +8.6 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 62.5% | 20.0% | 20.0% | 20.0% | -2.4 | 0.46 | 1.62 | +9.0 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 37.5% | 16.7% | 16.7% | 16.7% | -6.3 | 0.10 | 0.51 | +9.3 | +6.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 18.8% | 25.0% | 18.8% | -4.1 | 0.30 | 0.82 | +7.7 | +8.3 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 93.8% | 20.0% | 26.7% | 20.0% | -3.7 | 0.33 | 0.83 | +8.0 | +8.1 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 31.2% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +3.4 | +8.1 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +4.1 | +8.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=17 Fav=29.4% Avg=+0.2; validation N=19 Fav=26.3% Avg=+2.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 71 | S_STRANGER | 100.0% | 18.3% | 21.1% | 18.3% | -2.5 | 0.60 | 2.04 | +8.0 | +6.8 |
| `hunt_to_ar_ratio_le_2_0` | 58 | S_STRANGER | 81.7% | 17.2% | 20.7% | 19.0% | -3.0 | 0.51 | 1.74 | +7.2 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 67 | S_STRANGER | 94.4% | 19.4% | 22.4% | 19.4% | -2.0 | 0.67 | 2.09 | +8.4 | +6.7 |
| `stop_hunt_le_90` | 71 | S_STRANGER | 100.0% | 18.3% | 21.1% | 18.3% | -2.5 | 0.60 | 2.04 | +8.0 | +6.8 |
| `asian_range_gte_30` | 43 | S_STRANGER | 60.6% | 20.9% | 23.3% | 16.3% | -2.5 | 0.63 | 1.96 | +7.6 | +6.8 |
| `confluence_gte_60` | 37 | S_STRANGER | 52.1% | 24.3% | 27.0% | 16.2% | -1.1 | 0.80 | 2.15 | +7.6 | +7.1 |
| `confluence_gte_70` | 1 | R_RUNNER | 1.4% | 100.0% | 100.0% | 100.0% | +12.0 | 999.00 | 999.00 | +16.4 | +1.4 |
| `tdi_rsi_gt_signal` | 37 | S_STRANGER | 52.1% | 13.5% | 16.2% | 10.8% | -3.6 | 0.47 | 2.34 | +7.4 | +7.0 |
| `tdi_rsi_gte_50` | 36 | S_STRANGER | 50.7% | 27.8% | 30.6% | 19.4% | +1.6 | 1.41 | 3.08 | +10.7 | +6.3 |
| `ratio_le_2_and_asian_gte_30` | 37 | S_STRANGER | 52.1% | 21.6% | 24.3% | 18.9% | -2.0 | 0.69 | 1.99 | +8.1 | +6.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 21 | S_STRANGER | 29.6% | 19.0% | 23.8% | 14.3% | -0.4 | 0.93 | 2.97 | +9.2 | +4.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 71 | S_STRANGER | 100.0% | 18.3% | 21.1% | 18.3% | -2.5 | 0.60 | 2.04 | +8.0 | +6.8 |
| `feature_stale_hod_exhaustion_reject` | 71 | S_STRANGER | 100.0% | 18.3% | 21.1% | 18.3% | -2.5 | 0.60 | 2.04 | +8.0 | +6.8 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 4.2% | 33.3% | 33.3% | 33.3% | +1.3 | 1.75 | 3.49 | +4.8 | +3.6 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 2.8% | 50.0% | 50.0% | 50.0% | +3.9 | 6.17 | 6.17 | +6.0 | +0.8 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+4.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | +0.2 | 1.09 | 4.35 | +12.3 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | +0.2 | 1.09 | 4.35 | +12.3 | +5.9 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | +0.2 | 1.09 | 4.35 | +12.3 | +5.9 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | +0.2 | 1.09 | 4.35 | +12.3 | +5.9 |
| `asian_range_gte_30` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | +0.7 | 1.97 | 5.91 | +9.8 | +4.0 |
| `confluence_gte_60` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 25.0% | +1.9 | 1.57 | 4.70 | +15.7 | +8.6 |
| `confluence_gte_70` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -11.4 | 0.00 | 0.00 | +12.0 | +17.3 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +14.2 | +3.8 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 16.7% | +4.0 | 6.79 | 13.57 | +16.5 | +4.2 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | +0.7 | 1.97 | 5.91 | +9.8 | +4.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -2.1 | 0.00 | 0.00 | +6.6 | +5.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | +0.2 | 1.09 | 4.35 | +12.3 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 18.2% | +0.2 | 1.09 | 4.35 | +12.3 | +5.9 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 25.0% | -2.7 | 0.00 | 0.00 | +6.0 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -0.3 | 0.00 | 0.00 | +16.3 | +1.2 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+0.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=3 Fav=0.0% Avg=-3.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 27.3% | -2.4 | 0.30 | 0.60 | +4.3 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 27.3% | -2.4 | 0.30 | 0.60 | +4.3 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 27.3% | -2.4 | 0.30 | 0.60 | +4.3 | +4.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 27.3% | -2.4 | 0.30 | 0.60 | +4.3 | +4.6 |
| `asian_range_gte_30` | 4 | S_STRANGER | 36.4% | 0.0% | 25.0% | 25.0% | -3.2 | 0.23 | 0.45 | +5.5 | +6.7 |
| `confluence_gte_60` | 8 | S_STRANGER | 72.7% | 0.0% | 12.5% | 0.0% | -4.2 | 0.10 | 0.60 | +2.1 | +5.6 |
| `confluence_gte_70` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -7.0 | 0.00 | 0.00 | +2.4 | +2.6 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 20.0% | 40.0% | 20.0% | -1.8 | 0.33 | 0.33 | +3.6 | +4.3 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -2.7 | 0.00 | 0.00 | +1.4 | +5.4 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 36.4% | 0.0% | 25.0% | 25.0% | -3.2 | 0.23 | 0.45 | +5.5 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 18.2% | 0.0% | 50.0% | 0.0% | -2.6 | 0.41 | 0.41 | +3.3 | +6.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 27.3% | -2.4 | 0.30 | 0.60 | +4.3 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 27.3% | -2.4 | 0.30 | 0.60 | +4.3 | +4.6 |
| `feature_momentum_breakout_exception` | 3 | R_REPEATER | 27.3% | 66.7% | 66.7% | 100.0% | +2.5 | 999.00 | 999.00 | +10.3 | +1.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=-0.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 0.0% | -3.3 | 0.28 | 0.75 | +4.4 | +8.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 0.0% | -3.3 | 0.28 | 0.75 | +4.4 | +8.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 0.0% | -3.3 | 0.28 | 0.75 | +4.4 | +8.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 0.0% | -3.3 | 0.28 | 0.75 | +4.4 | +8.0 |
| `asian_range_gte_30` | 7 | S_STRANGER | 63.6% | 14.3% | 28.6% | 0.0% | -4.4 | 0.26 | 0.66 | +3.3 | +9.4 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 0.0% | -3.3 | 0.28 | 0.75 | +4.4 | +8.0 |
| `confluence_gte_70` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 0.0% | -1.4 | 0.55 | 0.55 | +5.7 | +7.1 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 0.0% | -0.6 | 0.79 | 1.18 | +7.1 | +8.2 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 0.0% | -3.2 | 0.42 | 0.64 | +7.8 | +11.8 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 63.6% | 14.3% | 28.6% | 0.0% | -4.4 | 0.26 | 0.66 | +3.3 | +9.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 0.0% | -2.1 | 0.57 | 1.15 | +4.3 | +10.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 0.0% | -3.3 | 0.28 | 0.75 | +4.4 | +8.0 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 0.0% | -3.3 | 0.28 | 0.75 | +4.4 | +8.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=27 Fav=18.5% Avg=-3.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 17.9% | 25.0% | 21.4% | -3.1 | 0.42 | 1.13 | +6.9 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 39.3% | 0.0% | 9.1% | 0.0% | -6.7 | 0.03 | 0.30 | +2.3 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 53.6% | 13.3% | 20.0% | 13.3% | -4.7 | 0.28 | 1.13 | +4.3 | +6.8 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 17.9% | 25.0% | 21.4% | -3.1 | 0.42 | 1.13 | +6.9 | +6.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 35.7% | 0.0% | 10.0% | 0.0% | -7.5 | 0.03 | 0.27 | +3.3 | +5.3 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 75.0% | 14.3% | 19.0% | 19.0% | -3.0 | 0.45 | 1.67 | +7.4 | +7.0 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 42.9% | 16.7% | 16.7% | 8.3% | -2.7 | 0.47 | 2.36 | +7.5 | +9.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 89.3% | 16.0% | 24.0% | 12.0% | -3.8 | 0.36 | 1.13 | +6.2 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 96.4% | 18.5% | 25.9% | 22.2% | -3.1 | 0.43 | 1.10 | +7.1 | +6.4 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 28.6% | 12.5% | 12.5% | 37.5% | -4.8 | 0.19 | 0.93 | +6.3 | +6.5 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 10.7% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +1.8 | +13.8 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=25.0% Avg=-4.0; validation N=15 Fav=13.3% Avg=-9.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 17.9% | 25.0% | 25.0% | -6.8 | 0.20 | 0.50 | +6.0 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 27 | S_STRANGER | 96.4% | 18.5% | 25.9% | 25.9% | -7.0 | 0.20 | 0.48 | +6.0 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 28 | S_STRANGER | 100.0% | 17.9% | 25.0% | 25.0% | -6.8 | 0.20 | 0.50 | +6.0 | +4.1 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 17.9% | 25.0% | 25.0% | -6.8 | 0.20 | 0.50 | +6.0 | +4.1 |
| `asian_range_gte_30` | 12 | S_STRANGER | 42.9% | 8.3% | 25.0% | 16.7% | -11.4 | 0.12 | 0.31 | +7.0 | +4.7 |
| `confluence_gte_60` | 14 | S_STRANGER | 50.0% | 7.1% | 21.4% | 14.3% | -7.7 | 0.14 | 0.48 | +6.4 | +4.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 22 | S_STRANGER | 78.6% | 18.2% | 22.7% | 27.3% | -7.4 | 0.18 | 0.50 | +5.9 | +3.8 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 28.6% | 12.5% | 12.5% | 12.5% | -3.6 | 0.09 | 0.54 | +6.4 | +6.6 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 42.9% | 8.3% | 25.0% | 16.7% | -11.4 | 0.12 | 0.31 | +7.0 | +4.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 32.1% | 11.1% | 22.2% | 22.2% | -12.7 | 0.11 | 0.34 | +6.5 | +5.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 17.9% | 25.0% | 25.0% | -6.8 | 0.20 | 0.50 | +6.0 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 17.9% | 25.0% | 25.0% | -6.8 | 0.20 | 0.50 | +6.0 | +4.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+8.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 23.5% | 17.6% | +1.3 | 1.30 | 4.22 | +8.5 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 94.1% | 18.8% | 25.0% | 18.8% | +1.6 | 1.34 | 4.02 | +8.9 | +6.9 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 94.1% | 18.8% | 25.0% | 18.8% | +1.6 | 1.34 | 4.02 | +8.9 | +6.9 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 17.6% | 23.5% | 17.6% | +1.3 | 1.30 | 4.22 | +8.5 | +7.0 |
| `asian_range_gte_30` | 9 | S_STRANGER | 52.9% | 11.1% | 22.2% | 11.1% | -3.0 | 0.39 | 1.38 | +4.6 | +5.9 |
| `confluence_gte_60` | 16 | S_STRANGER | 94.1% | 12.5% | 18.8% | 12.5% | -1.0 | 0.79 | 3.43 | +6.4 | +7.2 |
| `confluence_gte_70` | 8 | S_STRANGER | 47.1% | 25.0% | 25.0% | 25.0% | +2.0 | 1.42 | 4.26 | +10.7 | +7.2 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 76.5% | 15.4% | 23.1% | 15.4% | +1.8 | 1.37 | 4.55 | +9.1 | +7.5 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 35.3% | 33.3% | 33.3% | 33.3% | +8.7 | 2.83 | 5.67 | +16.7 | +8.8 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 52.9% | 11.1% | 22.2% | 11.1% | -3.0 | 0.39 | 1.38 | +4.6 | +5.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 41.2% | 0.0% | 14.3% | 0.0% | -4.9 | 0.12 | 0.71 | +2.8 | +6.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 94.1% | 18.8% | 25.0% | 18.8% | +1.6 | 1.34 | 4.02 | +8.9 | +6.9 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 17.6% | 23.5% | 17.6% | +1.3 | 1.30 | 4.22 | +8.5 | +7.0 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 41.2% | 0.0% | 14.3% | 0.0% | -4.1 | 0.14 | 0.83 | +3.4 | +7.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -6.7 | 0.00 | 0.00 | +3.9 | +12.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-3.5; validation N=2 Fav=0.0% Avg=-6.9; out_of_sample N=5 Fav=40.0% Avg=-0.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 29.4% | -2.3 | 0.43 | 1.58 | +5.7 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 82.4% | 21.4% | 21.4% | 35.7% | -1.1 | 0.65 | 1.74 | +6.0 | +3.8 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 94.1% | 18.8% | 18.8% | 31.2% | -2.1 | 0.47 | 1.57 | +5.9 | +4.5 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 29.4% | -2.3 | 0.43 | 1.58 | +5.7 | +4.9 |
| `asian_range_gte_30` | 6 | S_STRANGER | 35.3% | 16.7% | 16.7% | 33.3% | -0.0 | 0.99 | 2.96 | +8.2 | +4.9 |
| `confluence_gte_60` | 15 | S_STRANGER | 88.2% | 20.0% | 20.0% | 33.3% | -2.2 | 0.48 | 1.43 | +6.2 | +5.0 |
| `confluence_gte_70` | 3 | S_STRANGER | 17.6% | 33.3% | 33.3% | 33.3% | +4.2 | 13.70 | 13.70 | +7.0 | +2.1 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 52.9% | 22.2% | 22.2% | 22.2% | -2.8 | 0.52 | 1.55 | +6.8 | +5.7 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 47.1% | 12.5% | 12.5% | 25.0% | -1.9 | 0.47 | 2.35 | +6.5 | +5.6 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 35.3% | 16.7% | 16.7% | 33.3% | -0.0 | 0.99 | 2.96 | +8.2 | +4.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 17.6% | 33.3% | 33.3% | 33.3% | +3.3 | 3.61 | 3.61 | +10.5 | +4.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 29.4% | -2.3 | 0.43 | 1.58 | +5.7 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 29.4% | -2.3 | 0.43 | 1.58 | +5.7 | +4.9 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +1.9 | +4.3 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=+2.7; validation N=4 Fav=0.0% Avg=-4.2; out_of_sample N=11 Fav=36.4% Avg=-1.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 86 | S_STRANGER | 100.0% | 17.4% | 19.8% | 14.0% | -3.1 | 0.47 | 1.84 | +7.2 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 75 | S_STRANGER | 87.2% | 20.0% | 21.3% | 16.0% | -2.0 | 0.61 | 2.14 | +7.6 | +7.6 |
| `hunt_to_ar_ratio_le_2_5` | 83 | S_STRANGER | 96.5% | 18.1% | 20.5% | 14.5% | -2.4 | 0.55 | 2.05 | +7.4 | +7.3 |
| `stop_hunt_le_90` | 86 | S_STRANGER | 100.0% | 17.4% | 19.8% | 14.0% | -3.1 | 0.47 | 1.84 | +7.2 | +7.1 |
| `asian_range_gte_30` | 40 | S_STRANGER | 46.5% | 22.5% | 22.5% | 15.0% | -3.1 | 0.55 | 1.83 | +8.7 | +8.4 |
| `confluence_gte_60` | 73 | S_STRANGER | 84.9% | 17.8% | 20.5% | 12.3% | -3.1 | 0.47 | 1.77 | +7.2 | +7.5 |
| `confluence_gte_70` | 19 | S_STRANGER | 22.1% | 26.3% | 26.3% | 26.3% | -0.9 | 0.82 | 2.31 | +9.6 | +8.7 |
| `tdi_rsi_gt_signal` | 48 | S_STRANGER | 55.8% | 20.8% | 22.9% | 14.6% | -3.9 | 0.39 | 1.28 | +6.9 | +7.7 |
| `tdi_rsi_gte_50` | 47 | S_STRANGER | 54.7% | 25.5% | 27.7% | 12.8% | -1.1 | 0.77 | 2.01 | +8.6 | +8.1 |
| `ratio_le_2_and_asian_gte_30` | 38 | S_STRANGER | 44.2% | 23.7% | 23.7% | 15.8% | -2.1 | 0.65 | 2.03 | +9.0 | +8.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 24 | S_STRANGER | 27.9% | 25.0% | 25.0% | 16.7% | -2.8 | 0.53 | 1.49 | +8.1 | +8.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 86 | S_STRANGER | 100.0% | 17.4% | 19.8% | 14.0% | -3.1 | 0.47 | 1.84 | +7.2 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 86 | S_STRANGER | 100.0% | 17.4% | 19.8% | 14.0% | -3.1 | 0.47 | 1.84 | +7.2 | +7.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 3.5% | 0.0% | 0.0% | 0.0% | -2.1 | 0.00 | 0.00 | +2.5 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 2.3% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +1.6 | +4.8 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+0.7; validation N=5 Fav=20.0% Avg=-1.7; out_of_sample N=8 Fav=50.0% Avg=+4.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 83 | S_STRANGER | 100.0% | 16.9% | 18.1% | 19.3% | -8.0 | 0.27 | 1.15 | +7.0 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 64 | S_STRANGER | 77.1% | 21.9% | 23.4% | 25.0% | -4.0 | 0.49 | 1.45 | +8.1 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 79 | S_STRANGER | 95.2% | 17.7% | 19.0% | 20.3% | -7.2 | 0.30 | 1.19 | +7.3 | +5.4 |
| `stop_hunt_le_90` | 83 | S_STRANGER | 100.0% | 16.9% | 18.1% | 19.3% | -8.0 | 0.27 | 1.15 | +7.0 | +5.4 |
| `asian_range_gte_30` | 39 | S_STRANGER | 47.0% | 25.6% | 25.6% | 28.2% | -4.3 | 0.51 | 1.32 | +8.2 | +5.2 |
| `confluence_gte_60` | 76 | S_STRANGER | 91.6% | 17.1% | 18.4% | 19.7% | -8.1 | 0.27 | 1.12 | +7.2 | +5.5 |
| `confluence_gte_70` | 18 | S_STRANGER | 21.7% | 33.3% | 33.3% | 44.4% | +1.8 | 1.44 | 2.16 | +11.1 | +5.3 |
| `tdi_rsi_gt_signal` | 56 | S_STRANGER | 67.5% | 19.6% | 21.4% | 21.4% | -7.3 | 0.33 | 1.09 | +7.8 | +5.7 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 27.7% | 26.1% | 26.1% | 13.0% | -1.0 | 0.81 | 2.28 | +9.2 | +7.7 |
| `ratio_le_2_and_asian_gte_30` | 34 | S_STRANGER | 41.0% | 29.4% | 29.4% | 32.4% | -1.0 | 0.83 | 1.75 | +9.0 | +5.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 27 | S_STRANGER | 32.5% | 29.6% | 29.6% | 29.6% | -1.4 | 0.79 | 1.68 | +9.2 | +5.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 82 | S_STRANGER | 98.8% | 17.1% | 18.3% | 19.5% | -8.0 | 0.28 | 1.14 | +7.1 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 83 | S_STRANGER | 100.0% | 16.9% | 18.1% | 19.3% | -8.0 | 0.27 | 1.15 | +7.0 | +5.4 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 9.6% | 12.5% | 12.5% | 25.0% | -0.6 | 0.78 | 4.67 | +5.7 | +4.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 1.2% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +1.3 | +8.2 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=+5.7; out_of_sample N=1 Fav=0.0% Avg=-4.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | +0.7 | 1.24 | 6.22 | +8.3 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 33.3% | +4.0 | 2.44 | 4.88 | +11.7 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 66.7% | 25.0% | 25.0% | 25.0% | +2.3 | 1.83 | 5.50 | +9.6 | +5.8 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | +0.7 | 1.24 | 6.22 | +8.3 | +5.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | +0.7 | 1.24 | 6.22 | +8.3 | +5.7 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | +0.7 | 1.24 | 6.22 | +8.3 | +5.7 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | +4.0 | 2.62 | 2.62 | +10.4 | +8.5 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 20.0% | +1.4 | 1.54 | 6.18 | +9.2 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 18.2% | +0.8 | 1.26 | 5.68 | +8.7 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | +0.7 | 1.24 | 6.22 | +8.3 | +5.7 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +3.8 | +2.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +3.8 | +2.6 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-0.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -1.2 | 0.65 | 3.24 | +4.0 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +5.0 | +4.8 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -1.2 | 0.65 | 3.24 | +4.0 | +4.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 9.1% | -0.9 | 0.72 | 3.24 | +4.3 | +4.8 |
| `confluence_gte_70` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +7.6 | +5.6 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 0.0% | -0.3 | 0.92 | 3.69 | +3.9 | +4.5 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -1.5 | 0.62 | 3.70 | +4.7 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 9.1% | -0.9 | 0.72 | 3.24 | +4.3 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -1.2 | 0.65 | 3.24 | +4.0 | +4.8 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +0.9 | +5.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +0.4 | +6.1 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=23.1% Avg=+0.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -2.4 | 0.47 | 2.13 | +7.7 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -2.4 | 0.47 | 2.13 | +7.7 | +7.7 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -2.4 | 0.47 | 2.13 | +7.7 | +7.7 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -2.4 | 0.47 | 2.13 | +7.7 | +7.7 |
| `asian_range_gte_30` | 18 | S_STRANGER | 75.0% | 16.7% | 16.7% | 22.2% | -2.3 | 0.52 | 2.41 | +7.8 | +7.2 |
| `confluence_gte_60` | 5 | S_STRANGER | 20.8% | 0.0% | 0.0% | 20.0% | -6.0 | 0.00 | 0.00 | +5.2 | +9.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 79.2% | 21.1% | 21.1% | 31.6% | -0.9 | 0.76 | 2.48 | +8.6 | +7.0 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 58.3% | 14.3% | 14.3% | 21.4% | -1.8 | 0.55 | 3.03 | +8.1 | +7.7 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 75.0% | 16.7% | 16.7% | 22.2% | -2.3 | 0.52 | 2.41 | +7.8 | +7.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 54.2% | 23.1% | 23.1% | 30.8% | +0.1 | 1.04 | 3.11 | +9.2 | +6.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -2.4 | 0.47 | 2.13 | +7.7 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -2.4 | 0.47 | 2.13 | +7.7 | +7.7 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 45.8% | 9.1% | 9.1% | 18.2% | -4.1 | 0.17 | 1.51 | +5.5 | +8.0 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 29.2% | 0.0% | 0.0% | 14.3% | -4.3 | 0.00 | 0.00 | +5.4 | +7.8 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=16.7% Avg=-1.2; validation N=6 Fav=16.7% Avg=-6.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -2.9 | 0.39 | 1.94 | +6.3 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 38.9% | 14.3% | 14.3% | 14.3% | -0.3 | 0.86 | 5.18 | +4.6 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 50.0% | 11.1% | 11.1% | 11.1% | -4.2 | 0.28 | 2.25 | +4.7 | +4.1 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -2.9 | 0.39 | 1.94 | +6.3 | +5.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 44.4% | 12.5% | 12.5% | 12.5% | -4.1 | 0.31 | 2.19 | +6.6 | +3.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 22.2% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +2.6 | +4.4 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 83.3% | 13.3% | 13.3% | 13.3% | -1.8 | 0.39 | 2.57 | +5.7 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -2.9 | 0.39 | 1.94 | +6.3 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -2.9 | 0.39 | 1.94 | +6.3 | +5.3 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +0.4 | +4.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +0.4 | +4.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-3.0; validation N=5 Fav=20.0% Avg=+0.4; out_of_sample N=5 Fav=60.0% Avg=+10.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 42 | S_STRANGER | 100.0% | 16.7% | 16.7% | 14.3% | -3.3 | 0.45 | 2.14 | +6.8 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 36 | S_STRANGER | 85.7% | 16.7% | 16.7% | 13.9% | -4.1 | 0.32 | 1.47 | +5.9 | +5.3 |
| `hunt_to_ar_ratio_le_2_5` | 41 | S_STRANGER | 97.6% | 17.1% | 17.1% | 14.6% | -3.0 | 0.48 | 2.20 | +6.9 | +5.3 |
| `stop_hunt_le_90` | 42 | S_STRANGER | 100.0% | 16.7% | 16.7% | 14.3% | -3.3 | 0.45 | 2.14 | +6.8 | +5.2 |
| `asian_range_gte_30` | 19 | S_STRANGER | 45.2% | 21.1% | 21.1% | 15.8% | -6.6 | 0.24 | 0.85 | +6.3 | +6.5 |
| `confluence_gte_60` | 38 | S_STRANGER | 90.5% | 15.8% | 15.8% | 13.2% | -3.5 | 0.44 | 2.18 | +6.9 | +5.3 |
| `confluence_gte_70` | 23 | S_STRANGER | 54.8% | 17.4% | 17.4% | 8.7% | -6.1 | 0.24 | 1.08 | +5.9 | +6.0 |
| `tdi_rsi_gt_signal` | 40 | S_STRANGER | 95.2% | 17.5% | 17.5% | 15.0% | -3.2 | 0.47 | 2.09 | +7.1 | +5.2 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 38.1% | 31.2% | 31.2% | 18.8% | +2.4 | 1.99 | 4.38 | +11.1 | +4.4 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 42.9% | 22.2% | 22.2% | 16.7% | -6.6 | 0.25 | 0.82 | +6.5 | +6.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 18 | S_STRANGER | 42.9% | 22.2% | 22.2% | 16.7% | -6.6 | 0.25 | 0.82 | +6.5 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 41 | S_STRANGER | 97.6% | 17.1% | 17.1% | 14.6% | -3.2 | 0.46 | 2.12 | +7.0 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 42 | S_STRANGER | 100.0% | 16.7% | 16.7% | 14.3% | -3.3 | 0.45 | 2.14 | +6.8 | +5.2 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 16.7% | 14.3% | 14.3% | 14.3% | -2.7 | 0.36 | 2.14 | +3.8 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 9.5% | 25.0% | 25.0% | 25.0% | -1.6 | 0.63 | 1.89 | +5.5 | +5.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=25.0% Avg=-0.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 42 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -4.7 | 0.26 | 1.19 | +6.1 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 33 | S_STRANGER | 78.6% | 21.2% | 21.2% | 21.2% | -1.9 | 0.52 | 1.72 | +7.6 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 42 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -4.7 | 0.26 | 1.19 | +6.1 | +5.4 |
| `stop_hunt_le_90` | 42 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -4.7 | 0.26 | 1.19 | +6.1 | +5.4 |
| `asian_range_gte_30` | 20 | S_STRANGER | 47.6% | 20.0% | 20.0% | 20.0% | -4.9 | 0.25 | 0.86 | +6.8 | +4.1 |
| `confluence_gte_60` | 35 | S_STRANGER | 83.3% | 14.3% | 14.3% | 14.3% | -6.0 | 0.17 | 0.98 | +5.3 | +6.0 |
| `confluence_gte_70` | 16 | S_STRANGER | 38.1% | 6.2% | 6.2% | 6.2% | -8.8 | 0.11 | 1.66 | +5.5 | +5.2 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 42.9% | 16.7% | 16.7% | 11.1% | -4.7 | 0.27 | 1.17 | +6.0 | +6.0 |
| `tdi_rsi_gte_50` | 21 | S_STRANGER | 50.0% | 23.8% | 23.8% | 19.0% | -1.1 | 0.64 | 1.79 | +7.9 | +5.1 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 38.1% | 25.0% | 25.0% | 25.0% | -1.9 | 0.51 | 1.27 | +8.3 | +3.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 14.3% | 16.7% | 16.7% | 16.7% | -0.5 | 0.85 | 2.54 | +9.9 | +2.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 40 | S_STRANGER | 95.2% | 17.5% | 17.5% | 17.5% | -4.6 | 0.27 | 1.18 | +6.4 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 42 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -4.7 | 0.26 | 1.19 | +6.1 | +5.4 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 28.6% | 25.0% | 25.0% | 16.7% | -0.4 | 0.86 | 2.01 | +7.2 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 19.0% | 25.0% | 25.0% | 12.5% | -1.0 | 0.51 | 1.02 | +6.6 | +3.0 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=-2.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 15.8% | 15.8% | 21.1% | -7.3 | 0.19 | 0.96 | +5.5 | +4.0 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 47.4% | 11.1% | 11.1% | 22.2% | -13.5 | 0.08 | 0.58 | +5.3 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 68.4% | 15.4% | 15.4% | 23.1% | -9.4 | 0.16 | 0.81 | +5.4 | +4.7 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 15.8% | 15.8% | 21.1% | -7.3 | 0.19 | 0.96 | +5.5 | +4.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 31.6% | 33.3% | 33.3% | 50.0% | -2.1 | 0.63 | 0.95 | +8.1 | +4.3 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +10.0 | +3.6 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 10.5% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +0.4 | +3.0 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 52.6% | 20.0% | 20.0% | 20.0% | -4.8 | 0.30 | 1.18 | +6.2 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 15.8% | 15.8% | 21.1% | -7.3 | 0.19 | 0.96 | +5.5 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 15.8% | 15.8% | 21.1% | -7.3 | 0.19 | 0.96 | +5.5 | +4.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=11 Fav=9.1% Avg=-2.6; validation N=8 Fav=12.5% Avg=-0.5; out_of_sample N=7 Fav=42.9% Avg=+2.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 15.6% | 15.6% | 6.2% | -1.1 | 0.66 | 3.57 | +7.2 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 96.9% | 16.1% | 16.1% | 6.5% | -1.1 | 0.68 | 3.53 | +7.3 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 96.9% | 16.1% | 16.1% | 6.5% | -1.1 | 0.68 | 3.53 | +7.3 | +5.7 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 100.0% | 15.6% | 15.6% | 6.2% | -1.1 | 0.66 | 3.57 | +7.2 | +5.7 |
| `asian_range_gte_30` | 15 | S_STRANGER | 46.9% | 6.7% | 6.7% | 6.7% | -2.9 | 0.34 | 4.73 | +6.7 | +6.6 |
| `confluence_gte_60` | 32 | S_STRANGER | 100.0% | 15.6% | 15.6% | 6.2% | -1.1 | 0.66 | 3.57 | +7.2 | +5.7 |
| `confluence_gte_70` | 32 | S_STRANGER | 100.0% | 15.6% | 15.6% | 6.2% | -1.1 | 0.66 | 3.57 | +7.2 | +5.7 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 34.4% | 9.1% | 9.1% | 9.1% | -1.4 | 0.64 | 6.39 | +8.2 | +6.6 |
| `tdi_rsi_gte_50` | 26 | S_STRANGER | 81.2% | 19.2% | 19.2% | 7.7% | -0.5 | 0.85 | 3.55 | +8.1 | +5.5 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 46.9% | 6.7% | 6.7% | 6.7% | -2.9 | 0.34 | 4.73 | +6.7 | +6.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 15.6% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +4.6 | +7.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 100.0% | 15.6% | 15.6% | 6.2% | -1.1 | 0.66 | 3.57 | +7.2 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 96.9% | 16.1% | 16.1% | 6.5% | -1.1 | 0.69 | 3.56 | +7.2 | +5.8 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 15.6% | 0.0% | 0.0% | 0.0% | -2.9 | 0.00 | 0.00 | +2.9 | +4.4 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 15.6% | 0.0% | 0.0% | 0.0% | -2.9 | 0.00 | 0.00 | +2.9 | +4.4 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=25.0% Avg=-1.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -1.9 | 0.52 | 1.05 | +9.2 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 16.7% | 33.3% | 16.7% | -2.0 | 0.54 | 0.95 | +7.1 | +8.2 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -1.9 | 0.52 | 1.05 | +9.2 | +8.2 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -1.9 | 0.52 | 1.05 | +9.2 | +8.2 |
| `asian_range_gte_30` | 10 | S_STRANGER | 76.9% | 10.0% | 30.0% | 10.0% | -1.9 | 0.55 | 1.10 | +6.1 | +8.9 |
| `confluence_gte_60` | 6 | S_STRANGER | 46.2% | 16.7% | 50.0% | 16.7% | -1.7 | 0.41 | 0.41 | +12.9 | +5.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 76.9% | 10.0% | 20.0% | 10.0% | -3.0 | 0.41 | 1.44 | +5.6 | +9.0 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 61.5% | 25.0% | 25.0% | 12.5% | -1.5 | 0.67 | 2.00 | +11.8 | +10.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 76.9% | 10.0% | 30.0% | 10.0% | -1.9 | 0.55 | 1.10 | +6.1 | +8.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 69.2% | 11.1% | 22.2% | 11.1% | -2.4 | 0.49 | 1.48 | +6.1 | +9.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -1.9 | 0.52 | 1.05 | +9.2 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -1.9 | 0.52 | 1.05 | +9.2 | +8.2 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +2.2 | +5.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +1.3 | +10.7 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=0.0% Avg=-6.3; out_of_sample N=7 Fav=28.6% Avg=+0.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.4 | 0.37 | 2.06 | +6.2 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 0.0% | -6.3 | 0.12 | 0.23 | +8.3 | +9.5 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.4 | 0.37 | 2.06 | +6.2 | +6.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.4 | 0.37 | 2.06 | +6.2 | +6.3 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.4 | 0.37 | 2.06 | +6.2 | +6.3 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 92.3% | 16.7% | 16.7% | 8.3% | -2.6 | 0.38 | 1.88 | +6.5 | +6.6 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 61.5% | 12.5% | 12.5% | 0.0% | -4.3 | 0.07 | 0.48 | +5.4 | +6.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.4 | 0.37 | 2.06 | +6.2 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.4 | 0.37 | 2.06 | +6.2 | +6.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=-0.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-28.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -5.7 | 0.37 | 0.84 | +6.5 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -5.7 | 0.37 | 0.84 | +6.5 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -5.7 | 0.37 | 0.84 | +6.5 | +4.4 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -5.7 | 0.37 | 0.84 | +6.5 | +4.4 |
| `asian_range_gte_30` | 6 | S_STRANGER | 46.2% | 16.7% | 16.7% | 16.7% | -4.9 | 0.44 | 2.20 | +6.6 | +4.9 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -5.7 | 0.37 | 0.84 | +6.5 | +4.4 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -5.7 | 0.37 | 0.84 | +6.5 | +4.4 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 92.3% | 8.3% | 25.0% | 8.3% | -7.3 | 0.25 | 0.75 | +5.1 | +4.6 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 33.3% | +4.6 | 2.42 | 4.84 | +11.1 | +6.1 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 46.2% | 16.7% | 16.7% | 16.7% | -4.9 | 0.44 | 2.20 | +6.6 | +4.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 46.2% | 16.7% | 16.7% | 16.7% | -4.9 | 0.44 | 2.20 | +6.6 | +4.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -5.7 | 0.37 | 0.84 | +6.5 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 30.8% | 15.4% | -5.7 | 0.37 | 0.84 | +6.5 | +4.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 25.0% | +1.3 | 1.28 | 3.85 | +9.6 | +4.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 33.3% | +4.6 | 2.42 | 4.84 | +11.1 | +6.1 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+2.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 25.0% | -0.2 | 0.90 | 3.89 | +7.6 | +3.6 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 40.0% | 12.5% | 12.5% | 37.5% | -0.5 | 0.71 | 3.53 | +8.5 | +3.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 50.0% | 20.0% | 20.0% | 30.0% | +0.7 | 1.43 | 4.29 | +9.0 | +3.5 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 25.0% | -0.2 | 0.90 | 3.89 | +7.6 | +3.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 40.0% | 12.5% | 12.5% | 37.5% | -0.4 | 0.69 | 2.75 | +7.4 | +3.6 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +15.1 | +1.6 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | +1.5 | 2.11 | 5.28 | +9.7 | +4.0 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 55.0% | 18.2% | 18.2% | 18.2% | +0.9 | 1.79 | 6.28 | +9.6 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 80.0% | 12.5% | 12.5% | 31.2% | -0.6 | 0.64 | 3.51 | +8.0 | +3.6 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 25.0% | -0.2 | 0.90 | 3.89 | +7.6 | +3.6 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 50.0% | 20.0% | 20.0% | 10.0% | +0.2 | 1.10 | 3.86 | +7.1 | +4.1 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 35.0% | 28.6% | 28.6% | 14.3% | +2.2 | 3.18 | 6.37 | +9.7 | +3.1 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=14.3% Avg=-1.2; validation N=3 Fav=33.3% Avg=+10.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 7.1% | +2.5 | 1.70 | 6.24 | +11.2 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 71.4% | 10.0% | 10.0% | 0.0% | -0.3 | 0.92 | 8.27 | +7.9 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 7.1% | +2.5 | 1.70 | 6.24 | +11.2 | +5.4 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 7.1% | +2.5 | 1.70 | 6.24 | +11.2 | +5.4 |
| `asian_range_gte_30` | 9 | S_STRANGER | 64.3% | 0.0% | 11.1% | 0.0% | -0.8 | 0.79 | 6.29 | +6.7 | +5.5 |
| `confluence_gte_60` | 5 | S_STRANGER | 35.7% | 0.0% | 20.0% | 0.0% | +1.6 | 1.40 | 5.58 | +9.3 | +4.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 0.0% | +1.3 | 1.37 | 8.21 | +11.4 | +6.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 10.0% | +2.3 | 1.65 | 6.58 | +11.0 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +2.8 | +6.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +3.1 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 92.9% | 15.4% | 23.1% | 7.7% | +3.3 | 1.99 | 6.64 | +11.2 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 7.1% | +2.5 | 1.70 | 6.24 | +11.2 | +5.4 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 42.9% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +3.9 | +7.3 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +4.2 | +8.2 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+9.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 35.7% | 21.4% | +2.3 | 1.49 | 2.39 | +15.9 | +10.0 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 14.3% | 35.7% | 21.4% | +2.3 | 1.49 | 2.39 | +15.9 | +10.0 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 14.3% | 35.7% | 21.4% | +2.3 | 1.49 | 2.39 | +15.9 | +10.0 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 35.7% | 21.4% | +2.3 | 1.49 | 2.39 | +15.9 | +10.0 |
| `asian_range_gte_30` | 9 | S_STRANGER | 64.3% | 11.1% | 44.4% | 22.2% | +1.6 | 1.46 | 1.46 | +14.8 | +10.2 |
| `confluence_gte_60` | 12 | S_STRANGER | 85.7% | 8.3% | 25.0% | 16.7% | -1.9 | 0.65 | 1.74 | +12.8 | +11.2 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +29.1 | +0.5 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 42.9% | 33.3% | 50.0% | 33.3% | +9.4 | 3.22 | 3.22 | +21.2 | +7.9 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 33.3% | +3.8 | 1.78 | 5.33 | +19.8 | +8.9 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 64.3% | 11.1% | 44.4% | 22.2% | +1.6 | 1.46 | 1.46 | +14.8 | +10.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 28.6% | 25.0% | 50.0% | 25.0% | +4.2 | 2.13 | 2.13 | +15.7 | +7.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 14.3% | 35.7% | 21.4% | +2.3 | 1.49 | 2.39 | +15.9 | +10.0 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 35.7% | 21.4% | +2.3 | 1.49 | 2.39 | +15.9 | +10.0 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +0.7 | +6.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -8.0 | 0.00 | 0.00 | +9.3 | +10.1 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=22.2% Avg=+1.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 50.0% | -0.0 | 0.99 | 3.48 | +6.9 | +3.2 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 64.3% | 0.0% | 0.0% | 44.4% | -1.9 | 0.00 | 0.00 | +6.8 | +3.0 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 64.3% | 0.0% | 0.0% | 44.4% | -1.9 | 0.00 | 0.00 | +6.8 | +3.0 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 50.0% | -0.0 | 0.99 | 3.48 | +6.9 | +3.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 25.0% | +0.7 | 1.49 | 4.47 | +5.3 | +2.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 60.0% | +1.6 | 7.31 | 14.62 | +9.8 | +2.6 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 44.4% | +1.2 | 2.57 | 6.43 | +7.2 | +3.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 50.0% | -0.0 | 0.99 | 3.48 | +6.9 | +3.2 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 50.0% | -0.0 | 0.99 | 3.48 | +6.9 | +3.2 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 71.4% | 10.0% | 10.0% | 40.0% | -0.5 | 0.64 | 3.85 | +5.3 | +3.5 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 33.3% | +1.0 | 2.57 | 10.27 | +5.7 | +3.3 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+2.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 42.9% | -1.6 | 0.54 | 2.15 | +6.3 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 66.7% | +1.2 | 3.09 | 3.09 | +5.4 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 75.0% | +0.9 | 3.09 | 3.09 | +5.5 | +3.7 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 42.9% | -1.6 | 0.54 | 2.15 | +6.3 | +5.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 42.9% | -1.6 | 0.54 | 2.15 | +6.3 | +5.6 |
| `confluence_gte_70` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 25.0% | -4.1 | 0.00 | 0.00 | +4.0 | +6.0 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 20.0% | -4.0 | 0.00 | 0.00 | +4.2 | +5.8 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 42.9% | 0.0% | 0.0% | 0.0% | -7.0 | 0.00 | 0.00 | +4.3 | +9.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 71.4% | 10.0% | 10.0% | 40.0% | -3.3 | 0.14 | 0.83 | +5.0 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 46.2% | -1.6 | 0.56 | 1.95 | +6.5 | +5.2 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 60.0% | +2.0 | 1.90 | 3.79 | +9.0 | +3.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -4.3 | 0.00 | 0.00 | +3.6 | +8.3 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=20.0% Avg=-1.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -3.3 | 0.23 | 1.28 | +8.5 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -3.3 | 0.23 | 1.28 | +8.5 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -3.3 | 0.23 | 1.28 | +8.5 | +6.3 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -3.3 | 0.23 | 1.28 | +8.5 | +6.3 |
| `asian_range_gte_30` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 20.0% | -1.2 | 0.53 | 1.86 | +10.1 | +5.9 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -3.3 | 0.23 | 1.28 | +8.5 | +6.3 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -3.3 | 0.23 | 1.28 | +8.5 | +6.3 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +3.3 | +13.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 42.9% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +5.2 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 20.0% | -1.2 | 0.53 | 1.86 | +10.1 | +5.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +1.2 | +20.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -3.3 | 0.23 | 1.28 | +8.5 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -3.3 | 0.23 | 1.28 | +8.5 | +6.3 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 50.0% | +1.1 | 1.41 | 1.41 | +13.9 | +3.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +6.5 | +6.1 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=14 Fav=21.4% Avg=-2.7; validation N=1 Fav=0.0% Avg=-12.1; out_of_sample N=1 Fav=0.0% Avg=-15.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 23.8% | -3.5 | 0.36 | 1.80 | +5.8 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 90.5% | 15.8% | 15.8% | 26.3% | -3.7 | 0.37 | 1.59 | +5.9 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 23.8% | -3.5 | 0.36 | 1.80 | +5.8 | +4.4 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 23.8% | -3.5 | 0.36 | 1.80 | +5.8 | +4.4 |
| `asian_range_gte_30` | 18 | S_STRANGER | 85.7% | 16.7% | 16.7% | 22.2% | -3.7 | 0.38 | 1.78 | +6.1 | +4.4 |
| `confluence_gte_60` | 8 | S_STRANGER | 38.1% | 12.5% | 12.5% | 37.5% | -1.4 | 0.51 | 2.05 | +5.0 | +5.8 |
| `confluence_gte_70` | 7 | S_STRANGER | 33.3% | 14.3% | 14.3% | 42.9% | -1.6 | 0.51 | 2.05 | +5.4 | +6.2 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 95.2% | 15.0% | 15.0% | 25.0% | -3.6 | 0.36 | 1.69 | +6.0 | +4.4 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 9.5% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +1.1 | +7.1 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 76.2% | 18.8% | 18.8% | 25.0% | -4.0 | 0.39 | 1.55 | +6.3 | +4.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 16 | S_STRANGER | 76.2% | 18.8% | 18.8% | 25.0% | -4.0 | 0.39 | 1.55 | +6.3 | +4.5 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +10.4 | +6.8 |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 95.2% | 15.0% | 15.0% | 25.0% | -3.6 | 0.36 | 1.69 | +6.0 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 23.8% | -3.5 | 0.36 | 1.80 | +5.8 | +4.4 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 61.9% | 15.4% | 15.4% | 23.1% | -4.0 | 0.36 | 1.80 | +6.4 | +4.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -10.5 | 0.00 | 0.00 | +0.1 | +10.9 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=-0.3; validation N=9 Fav=11.1% Avg=-10.3; out_of_sample N=2 Fav=0.0% Avg=-22.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 14.3% | 19.0% | 14.3% | -14.1 | 0.10 | 0.43 | +5.8 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 85.7% | 11.1% | 16.7% | 11.1% | -15.3 | 0.08 | 0.42 | +5.3 | +4.2 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 100.0% | 14.3% | 19.0% | 14.3% | -14.1 | 0.10 | 0.43 | +5.8 | +3.8 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 14.3% | 19.0% | 14.3% | -14.1 | 0.10 | 0.43 | +5.8 | +3.8 |
| `asian_range_gte_30` | 13 | S_STRANGER | 61.9% | 0.0% | 7.7% | 0.0% | -22.2 | 0.00 | 0.05 | +2.9 | +4.0 |
| `confluence_gte_60` | 21 | S_STRANGER | 100.0% | 14.3% | 19.0% | 14.3% | -14.1 | 0.10 | 0.43 | +5.8 | +3.8 |
| `confluence_gte_70` | 21 | S_STRANGER | 100.0% | 14.3% | 19.0% | 14.3% | -14.1 | 0.10 | 0.43 | +5.8 | +3.8 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 66.7% | 14.3% | 21.4% | 14.3% | -9.9 | 0.14 | 0.50 | +6.5 | +4.1 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 19.0% | 25.0% | 25.0% | 25.0% | -4.7 | 0.30 | 0.89 | +9.8 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 61.9% | 0.0% | 7.7% | 0.0% | -22.2 | 0.00 | 0.05 | +2.9 | +4.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 33.3% | 0.0% | 14.3% | 0.0% | -16.9 | 0.01 | 0.07 | +2.9 | +4.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 14.3% | 19.0% | 14.3% | -14.1 | 0.10 | 0.43 | +5.8 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 14.3% | 19.0% | 14.3% | -14.1 | 0.10 | 0.43 | +5.8 | +3.8 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 9.5% | 50.0% | 50.0% | 50.0% | +3.6 | 2.81 | 2.81 | +10.7 | +3.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +8.1 | +4.4 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+1.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 13.6% | 13.6% | 31.8% | -0.8 | 0.59 | 2.75 | +6.8 | +3.1 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 31.8% | 28.6% | 28.6% | 28.6% | +1.9 | 8.65 | 17.29 | +8.6 | +2.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 50.0% | 18.2% | 18.2% | 36.4% | +0.8 | 2.49 | 7.47 | +8.3 | +2.7 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 13.6% | 13.6% | 31.8% | -0.8 | 0.59 | 2.75 | +6.8 | +3.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 4 | S_STRANGER | 18.2% | 0.0% | 0.0% | 25.0% | -2.8 | 0.00 | 0.00 | +6.6 | +1.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 90.9% | 15.0% | 15.0% | 30.0% | -0.4 | 0.75 | 3.25 | +6.5 | +3.3 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 45.5% | 20.0% | 20.0% | 30.0% | +0.7 | 2.27 | 6.82 | +7.1 | +2.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 5 | S_STRANGER | 22.7% | 0.0% | 0.0% | 40.0% | -1.2 | 0.00 | 0.00 | +5.6 | +2.7 |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 77.3% | 17.6% | 17.6% | 29.4% | -0.5 | 0.73 | 2.68 | +7.1 | +3.0 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 13.6% | 13.6% | 31.8% | -0.8 | 0.59 | 2.75 | +6.8 | +3.1 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 45.5% | 20.0% | 20.0% | 40.0% | +0.3 | 1.36 | 3.40 | +6.1 | +2.3 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 22.7% | 40.0% | 40.0% | 40.0% | +1.9 | 4.17 | 4.17 | +6.6 | +2.0 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+2.0; validation N=4 Fav=0.0% Avg=-10.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 13.3% | 20.0% | 16.7% | -1.7 | 0.53 | 2.04 | +5.2 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 70.0% | 14.3% | 23.8% | 14.3% | -1.9 | 0.52 | 1.68 | +5.1 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 90.0% | 14.8% | 22.2% | 18.5% | -1.4 | 0.62 | 2.06 | +5.5 | +3.9 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 13.3% | 20.0% | 16.7% | -1.7 | 0.53 | 2.04 | +5.2 | +4.1 |
| `asian_range_gte_30` | 11 | S_STRANGER | 36.7% | 18.2% | 27.3% | 27.3% | -2.7 | 0.45 | 1.05 | +5.7 | +3.7 |
| `confluence_gte_60` | 16 | S_STRANGER | 53.3% | 12.5% | 25.0% | 12.5% | -2.4 | 0.45 | 1.36 | +5.4 | +3.9 |
| `confluence_gte_70` | 3 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +4.7 | +4.7 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 36.7% | 9.1% | 9.1% | 9.1% | -2.1 | 0.36 | 3.61 | +4.6 | +4.8 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 66.7% | 5.0% | 5.0% | 5.0% | -3.0 | 0.15 | 2.91 | +3.6 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 33.3% | 20.0% | 30.0% | 20.0% | -3.0 | 0.45 | 1.05 | +5.6 | +3.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 20.0% | 16.7% | 16.7% | 16.7% | -0.8 | 0.73 | 3.65 | +5.9 | +4.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 100.0% | 13.3% | 20.0% | 16.7% | -1.7 | 0.53 | 2.04 | +5.2 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 13.3% | 20.0% | 16.7% | -1.7 | 0.53 | 2.04 | +5.2 | +4.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +2.2 | +4.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +2.5 | +3.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-4.5; validation N=5 Fav=40.0% Avg=-0.8; out_of_sample N=4 Fav=25.0% Avg=-0.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 45 | S_STRANGER | 100.0% | 13.3% | 17.8% | 17.8% | -3.9 | 0.25 | 1.03 | +4.5 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 33.3% | 13.3% | 13.3% | 40.0% | -1.6 | 0.48 | 2.18 | +5.2 | +5.9 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 64.4% | 10.3% | 13.8% | 20.7% | -4.9 | 0.17 | 0.91 | +3.9 | +4.3 |
| `stop_hunt_le_90` | 45 | S_STRANGER | 100.0% | 13.3% | 17.8% | 17.8% | -3.9 | 0.25 | 1.03 | +4.5 | +5.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 32 | S_STRANGER | 71.1% | 15.6% | 21.9% | 21.9% | -2.9 | 0.38 | 1.19 | +5.1 | +5.3 |
| `confluence_gte_70` | 4 | R_RUNNER | 8.9% | 75.0% | 75.0% | 50.0% | +6.6 | 8.00 | 2.67 | +13.8 | +4.6 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 46.7% | 19.0% | 19.0% | 9.5% | -4.2 | 0.21 | 0.90 | +3.9 | +6.3 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 28.9% | 23.1% | 23.1% | 15.4% | -1.8 | 0.50 | 1.65 | +4.4 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 44 | S_STRANGER | 97.8% | 13.6% | 18.2% | 18.2% | -3.9 | 0.25 | 1.01 | +4.6 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 45 | S_STRANGER | 100.0% | 13.3% | 17.8% | 17.8% | -3.9 | 0.25 | 1.03 | +4.5 | +5.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 8.9% | 0.0% | 0.0% | 50.0% | -3.5 | 0.00 | 0.00 | +5.2 | +7.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 4.4% | 0.0% | 0.0% | 0.0% | -6.9 | 0.00 | 0.00 | +1.7 | +8.2 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.6; validation N=10 Fav=20.0% Avg=-2.1; out_of_sample N=3 Fav=33.3% Avg=+5.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 38 | S_STRANGER | 100.0% | 13.2% | 13.2% | 15.8% | -7.4 | 0.17 | 1.11 | +6.4 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 34 | S_STRANGER | 89.5% | 14.7% | 14.7% | 17.6% | -7.7 | 0.18 | 1.02 | +6.7 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 34 | S_STRANGER | 89.5% | 14.7% | 14.7% | 17.6% | -7.7 | 0.18 | 1.02 | +6.7 | +5.0 |
| `stop_hunt_le_90` | 38 | S_STRANGER | 100.0% | 13.2% | 13.2% | 15.8% | -7.4 | 0.17 | 1.11 | +6.4 | +5.2 |
| `asian_range_gte_30` | 17 | S_STRANGER | 44.7% | 0.0% | 0.0% | 5.9% | -14.4 | 0.00 | 0.00 | +4.8 | +3.4 |
| `confluence_gte_60` | 38 | S_STRANGER | 100.0% | 13.2% | 13.2% | 15.8% | -7.4 | 0.17 | 1.11 | +6.4 | +5.2 |
| `confluence_gte_70` | 38 | S_STRANGER | 100.0% | 13.2% | 13.2% | 15.8% | -7.4 | 0.17 | 1.11 | +6.4 | +5.2 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 39.5% | 20.0% | 20.0% | 20.0% | -8.8 | 0.22 | 0.89 | +7.9 | +4.3 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 36.8% | 21.4% | 21.4% | 21.4% | -0.6 | 0.82 | 3.00 | +7.5 | +5.5 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 44.7% | 0.0% | 0.0% | 5.9% | -14.4 | 0.00 | 0.00 | +4.8 | +3.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 18.4% | 0.0% | 0.0% | 0.0% | -20.5 | 0.00 | 0.00 | +4.7 | +3.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 38 | S_STRANGER | 100.0% | 13.2% | 13.2% | 15.8% | -7.4 | 0.17 | 1.11 | +6.4 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 100.0% | 13.2% | 13.2% | 15.8% | -7.4 | 0.17 | 1.11 | +6.4 | +5.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=15.4% Avg=-3.0; validation N=2 Fav=50.0% Avg=+5.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 8.7% | -4.0 | 0.31 | 1.40 | +4.4 | +4.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 34.8% | 12.5% | 25.0% | 12.5% | -1.1 | 0.74 | 2.22 | +6.1 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 65.2% | 20.0% | 26.7% | 13.3% | -1.9 | 0.60 | 1.49 | +5.9 | +4.2 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 8.7% | -4.0 | 0.31 | 1.40 | +4.4 | +4.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 26.1% | 16.7% | 16.7% | 0.0% | -1.6 | 0.58 | 2.92 | +5.3 | +4.7 |
| `confluence_gte_70` | 2 | R_REPEATER | 8.7% | 50.0% | 50.0% | 0.0% | +4.3 | 2.81 | 2.81 | +7.2 | +5.2 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 73.9% | 17.6% | 17.6% | 11.8% | -4.2 | 0.34 | 1.46 | +5.2 | +4.6 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 43.5% | 10.0% | 10.0% | 20.0% | -1.9 | 0.51 | 4.09 | +5.3 | +3.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 8.7% | -4.0 | 0.31 | 1.40 | +4.4 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 8.7% | -4.0 | 0.31 | 1.40 | +4.4 | +4.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+1.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=100.0% Avg=+15.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | -0.1 | 0.97 | 3.87 | +8.1 | +4.2 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 37.5% | 33.3% | 50.0% | 33.3% | +4.0 | 8.27 | 5.52 | +7.9 | +3.1 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 56.2% | 22.2% | 33.3% | 22.2% | +1.1 | 1.61 | 2.68 | +6.5 | +4.3 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | -0.1 | 0.97 | 3.87 | +8.1 | +4.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 87.5% | 7.1% | 14.3% | 14.3% | -1.2 | 0.42 | 2.31 | +8.0 | +4.6 |
| `confluence_gte_70` | 7 | S_STRANGER | 43.8% | 0.0% | 0.0% | 14.3% | -2.9 | 0.00 | 0.00 | +10.0 | +5.8 |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 6.2% | 100.0% | 100.0% | 0.0% | +11.0 | 999.00 | 999.00 | +15.8 | +2.0 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 62.5% | 10.0% | 10.0% | 10.0% | -1.4 | 0.44 | 3.98 | +9.2 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 93.8% | 13.3% | 20.0% | 13.3% | +0.0 | 1.03 | 3.76 | +6.0 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 93.8% | 13.3% | 20.0% | 13.3% | +0.0 | 1.03 | 3.76 | +6.0 | +4.4 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 50.0% | -1.0 | 0.00 | 0.00 | +4.1 | +5.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 100.0% | -1.6 | 0.00 | 0.00 | +40.0 | +2.0 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=-0.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=0.0% Avg=-6.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 25.0% | -3.2 | 0.25 | 1.48 | +6.1 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 81.2% | 15.4% | 15.4% | 30.8% | -2.9 | 0.30 | 1.36 | +7.1 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 81.2% | 15.4% | 15.4% | 30.8% | -2.9 | 0.30 | 1.36 | +7.1 | +4.3 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 25.0% | -3.2 | 0.25 | 1.48 | +6.1 | +5.4 |
| `asian_range_gte_30` | 8 | S_STRANGER | 50.0% | 12.5% | 12.5% | 37.5% | -2.9 | 0.29 | 1.45 | +7.0 | +4.6 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 25.0% | -3.2 | 0.25 | 1.48 | +6.1 | +5.4 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 25.0% | -3.2 | 0.25 | 1.48 | +6.1 | +5.4 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 81.2% | 15.4% | 15.4% | 15.4% | -3.2 | 0.29 | 1.59 | +6.0 | +5.6 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 25.0% | 0.0% | 0.0% | 25.0% | -2.0 | 0.00 | 0.00 | +7.6 | +5.1 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 50.0% | 12.5% | 12.5% | 37.5% | -2.9 | 0.29 | 1.45 | +7.0 | +4.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 20.0% | -2.8 | 0.41 | 1.63 | +7.0 | +4.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 25.0% | -3.2 | 0.25 | 1.48 | +6.1 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 25.0% | -3.2 | 0.25 | 1.48 | +6.1 | +5.4 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 6.2% | 100.0% | 100.0% | 100.0% | +9.6 | 999.00 | 999.00 | +24.6 | +1.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=30.0% Avg=+0.3; validation N=8 Fav=0.0% Avg=-8.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 12.5% | 12.5% | 25.0% | -3.7 | 0.23 | 1.34 | +5.7 | +8.6 |
| `hunt_to_ar_ratio_le_2_0` | 28 | S_STRANGER | 87.5% | 10.7% | 10.7% | 17.9% | -4.5 | 0.15 | 1.09 | +5.5 | +9.3 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 96.9% | 12.9% | 12.9% | 22.6% | -3.8 | 0.23 | 1.34 | +5.8 | +8.7 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 100.0% | 12.5% | 12.5% | 25.0% | -3.7 | 0.23 | 1.34 | +5.7 | +8.6 |
| `asian_range_gte_30` | 12 | S_STRANGER | 37.5% | 0.0% | 0.0% | 16.7% | -7.6 | 0.00 | 0.00 | +6.4 | +9.2 |
| `confluence_gte_60` | 18 | S_STRANGER | 56.2% | 16.7% | 16.7% | 16.7% | -3.4 | 0.31 | 1.46 | +5.5 | +6.7 |
| `confluence_gte_70` | 4 | S_STRANGER | 12.5% | 0.0% | 0.0% | 25.0% | -1.8 | 0.00 | 0.00 | +4.8 | +3.6 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 65.6% | 9.5% | 9.5% | 14.3% | -5.5 | 0.14 | 1.22 | +5.3 | +8.7 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 50.0% | 6.2% | 6.2% | 12.5% | -4.3 | 0.08 | 1.00 | +6.1 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 34.4% | 0.0% | 0.0% | 18.2% | -7.7 | 0.00 | 0.00 | +6.8 | +9.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -10.6 | 0.00 | 0.00 | +5.6 | +12.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 100.0% | 12.5% | 12.5% | 25.0% | -3.7 | 0.23 | 1.34 | +5.7 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 12.5% | 12.5% | 25.0% | -3.7 | 0.23 | 1.34 | +5.7 | +8.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=14.3% Avg=-7.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 12.5% | -5.1 | 0.32 | 2.25 | +7.9 | +14.6 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 93.8% | 13.3% | 13.3% | 13.3% | -5.2 | 0.33 | 2.16 | +8.3 | +15.3 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 93.8% | 13.3% | 13.3% | 13.3% | -5.2 | 0.33 | 2.16 | +8.3 | +15.3 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 12.5% | -5.1 | 0.32 | 2.25 | +7.9 | +14.6 |
| `asian_range_gte_30` | 10 | S_STRANGER | 62.5% | 10.0% | 10.0% | 10.0% | -9.0 | 0.02 | 0.17 | +7.6 | +18.7 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 12.5% | -5.1 | 0.32 | 2.25 | +7.9 | +14.6 |
| `confluence_gte_70` | 10 | S_STRANGER | 62.5% | 0.0% | 0.0% | 0.0% | -8.3 | 0.00 | 0.00 | +5.0 | +11.2 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -19.4 | 0.00 | 0.00 | +11.1 | +37.4 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 43.8% | 14.3% | 14.3% | 14.3% | -7.0 | 0.43 | 2.59 | +14.8 | +26.8 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 62.5% | 10.0% | 10.0% | 10.0% | -9.0 | 0.02 | 0.17 | +7.6 | +18.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -19.4 | 0.00 | 0.00 | +11.1 | +37.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 12.5% | -5.1 | 0.32 | 2.25 | +7.9 | +14.6 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 12.5% | -5.1 | 0.32 | 2.25 | +7.9 | +14.6 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +2.2 | +3.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +1.7 | +6.1 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.5; validation N=14 Fav=21.4% Avg=-3.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | -7.2 | 0.16 | 0.61 | +5.0 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 46.9% | 20.0% | 26.7% | 13.3% | -3.6 | 0.32 | 0.88 | +4.1 | +8.7 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 62.5% | 15.0% | 20.0% | 15.0% | -6.7 | 0.16 | 0.60 | +4.3 | +7.2 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | -7.2 | 0.16 | 0.61 | +5.0 | +6.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 31 | S_STRANGER | 96.9% | 12.9% | 19.4% | 19.4% | -7.4 | 0.16 | 0.58 | +5.1 | +6.5 |
| `confluence_gte_70` | 10 | S_STRANGER | 31.2% | 10.0% | 10.0% | 10.0% | -12.2 | 0.08 | 0.63 | +5.2 | +9.4 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 59.4% | 5.3% | 5.3% | 21.1% | -11.6 | 0.02 | 0.34 | +4.4 | +7.1 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 31.2% | 20.0% | 20.0% | 20.0% | -5.5 | 0.28 | 1.14 | +6.2 | +10.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | -7.2 | 0.16 | 0.61 | +5.0 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | -7.2 | 0.16 | 0.61 | +5.0 | +6.4 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 3.1% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +2.4 | +2.1 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=0.0% Avg=-4.0; validation N=3 Fav=33.3% Avg=+1.5; out_of_sample N=1 Fav=0.0% Avg=-11.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 12.5% | 16.7% | 16.7% | -8.4 | 0.22 | 1.03 | +5.8 | +3.6 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 91.7% | 13.6% | 18.2% | 18.2% | -8.1 | 0.24 | 1.00 | +5.8 | +3.8 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 95.8% | 13.0% | 17.4% | 17.4% | -8.7 | 0.22 | 0.97 | +5.8 | +3.7 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 12.5% | 16.7% | 16.7% | -8.4 | 0.22 | 1.03 | +5.8 | +3.6 |
| `asian_range_gte_30` | 12 | S_STRANGER | 50.0% | 0.0% | 8.3% | 0.0% | -15.0 | 0.01 | 0.12 | +3.0 | +4.3 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 12.5% | 16.7% | 16.7% | -8.4 | 0.22 | 1.03 | +5.8 | +3.6 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 12.5% | 16.7% | 16.7% | -8.4 | 0.22 | 1.03 | +5.8 | +3.6 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 75.0% | 5.6% | 11.1% | 11.1% | -10.1 | 0.13 | 0.99 | +5.1 | +4.1 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 29.2% | 14.3% | 14.3% | 28.6% | -2.7 | 0.57 | 2.87 | +7.6 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 50.0% | 0.0% | 8.3% | 0.0% | -15.0 | 0.01 | 0.12 | +3.0 | +4.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 41.7% | 0.0% | 10.0% | 0.0% | -13.7 | 0.01 | 0.12 | +3.2 | +4.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 12.5% | 16.7% | 16.7% | -8.4 | 0.22 | 1.03 | +5.8 | +3.6 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 12.5% | 16.7% | 16.7% | -8.4 | 0.22 | 1.03 | +5.8 | +3.6 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +0.8 | +5.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +0.8 | +5.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-1.8; validation N=3 Fav=33.3% Avg=-0.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 18.8% | -9.7 | 0.10 | 0.60 | +4.4 | +3.4 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 68.8% | 9.1% | 9.1% | 27.3% | -8.1 | 0.15 | 1.20 | +4.5 | +3.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 81.2% | 7.7% | 7.7% | 23.1% | -9.7 | 0.11 | 1.11 | +4.5 | +3.5 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 18.8% | -9.7 | 0.10 | 0.60 | +4.4 | +3.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 5 | S_STRANGER | 31.2% | 0.0% | 0.0% | 40.0% | -6.7 | 0.00 | 0.00 | +4.8 | +4.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 75.0% | 16.7% | 16.7% | 25.0% | -5.8 | 0.20 | 0.80 | +4.9 | +4.1 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 40.0% | -0.8 | 0.28 | 0.55 | +5.9 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 18.8% | -9.7 | 0.10 | 0.60 | +4.4 | +3.4 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 18.8% | -9.7 | 0.10 | 0.60 | +4.4 | +3.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=+0.0; validation N=11 Fav=18.2% Avg=-7.9; out_of_sample N=9 Fav=11.1% Avg=-12.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 12.5% | 12.5% | 12.5% | -14.1 | 0.08 | 0.54 | +7.3 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 70.8% | 11.8% | 11.8% | 11.8% | -9.6 | 0.12 | 0.81 | +7.6 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 87.5% | 14.3% | 14.3% | 14.3% | -9.5 | 0.13 | 0.74 | +7.2 | +5.4 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 12.5% | 12.5% | 12.5% | -14.1 | 0.08 | 0.54 | +7.3 | +4.8 |
| `asian_range_gte_30` | 3 | S_STRANGER | 12.5% | 33.3% | 33.3% | 33.3% | -2.4 | 0.55 | 1.09 | +9.1 | +11.0 |
| `confluence_gte_60` | 22 | S_STRANGER | 91.7% | 9.1% | 9.1% | 9.1% | -15.0 | 0.07 | 0.65 | +7.5 | +5.1 |
| `confluence_gte_70` | 3 | S_STRANGER | 12.5% | 0.0% | 0.0% | 33.3% | -2.3 | 0.00 | 0.00 | +5.5 | +1.1 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 33.3% | 12.5% | 12.5% | 0.0% | -6.1 | 0.24 | 1.70 | +10.9 | +4.2 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 33.3% | 12.5% | 12.5% | 0.0% | -0.9 | 0.69 | 4.84 | +10.3 | +5.5 |
| `ratio_le_2_and_asian_gte_30` | 2 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -8.0 | 0.00 | 0.00 | +5.5 | +15.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +8.2 | +1.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 12.5% | 12.5% | 12.5% | -14.1 | 0.08 | 0.54 | +7.3 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 12.5% | 12.5% | 12.5% | -14.1 | 0.08 | 0.54 | +7.3 | +4.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=20.0% Avg=-1.9; validation N=5 Fav=0.0% Avg=-10.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | S_STRANGER | 100.0% | 12.1% | 18.2% | 15.2% | -2.9 | 0.43 | 1.70 | +7.9 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 29 | S_STRANGER | 87.9% | 10.3% | 17.2% | 6.9% | -4.5 | 0.14 | 0.65 | +6.1 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 93.9% | 9.7% | 16.1% | 9.7% | -4.6 | 0.13 | 0.62 | +6.1 | +6.4 |
| `stop_hunt_le_90` | 33 | S_STRANGER | 100.0% | 12.1% | 18.2% | 15.2% | -2.9 | 0.43 | 1.70 | +7.9 | +6.2 |
| `asian_range_gte_30` | 16 | S_STRANGER | 48.5% | 12.5% | 18.8% | 6.2% | -5.4 | 0.17 | 0.76 | +5.2 | +5.9 |
| `confluence_gte_60` | 15 | S_STRANGER | 45.5% | 6.7% | 6.7% | 0.0% | -6.3 | 0.11 | 1.44 | +7.1 | +6.9 |
| `confluence_gte_70` | 1 | S_STRANGER | 3.0% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +3.3 | +4.6 |
| `tdi_rsi_gt_signal` | 26 | S_STRANGER | 78.8% | 7.7% | 11.5% | 15.4% | -2.2 | 0.49 | 3.23 | +8.0 | +6.1 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 57.6% | 10.5% | 10.5% | 5.3% | -1.9 | 0.62 | 4.98 | +9.1 | +7.4 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 45.5% | 13.3% | 20.0% | 6.7% | -4.8 | 0.20 | 0.80 | +5.3 | +6.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 36.4% | 8.3% | 16.7% | 8.3% | -4.7 | 0.10 | 0.51 | +4.4 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 97.0% | 12.5% | 18.8% | 12.5% | -3.0 | 0.43 | 1.70 | +7.9 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 33 | S_STRANGER | 100.0% | 12.1% | 18.2% | 15.2% | -2.9 | 0.43 | 1.70 | +7.9 | +6.2 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 6.1% | 0.0% | 0.0% | 50.0% | -4.1 | 0.00 | 0.00 | +5.2 | +6.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.0% | 0.0% | 0.0% | 0.0% | -8.2 | 0.00 | 0.00 | +2.4 | +10.1 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-2.4; validation N=2 Fav=0.0% Avg=-1.3; out_of_sample N=1 Fav=100.0% Avg=+14.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | S_STRANGER | 100.0% | 12.1% | 18.2% | 21.2% | -5.5 | 0.21 | 0.85 | +4.7 | +3.6 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 51.5% | 11.8% | 11.8% | 29.4% | -0.2 | 0.87 | 5.24 | +5.2 | +2.9 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 75.8% | 8.0% | 16.0% | 20.0% | -1.5 | 0.37 | 1.68 | +4.1 | +3.4 |
| `stop_hunt_le_90` | 33 | S_STRANGER | 100.0% | 12.1% | 18.2% | 21.2% | -5.5 | 0.21 | 0.85 | +4.7 | +3.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 24 | S_STRANGER | 72.7% | 12.5% | 20.8% | 12.5% | -7.2 | 0.19 | 0.73 | +4.9 | +3.8 |
| `confluence_gte_70` | 7 | S_STRANGER | 21.2% | 0.0% | 28.6% | 0.0% | -1.0 | 0.11 | 0.28 | +2.1 | +2.2 |
| `tdi_rsi_gt_signal` | 27 | S_STRANGER | 81.8% | 11.1% | 14.8% | 18.5% | -4.7 | 0.24 | 1.28 | +4.8 | +3.8 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 18.2% | 16.7% | 16.7% | 16.7% | +0.7 | 1.44 | 7.19 | +5.5 | +3.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 33 | S_STRANGER | 100.0% | 12.1% | 18.2% | 21.2% | -5.5 | 0.21 | 0.85 | +4.7 | +3.6 |
| `feature_stale_hod_exhaustion_reject` | 33 | S_STRANGER | 100.0% | 12.1% | 18.2% | 21.2% | -5.5 | 0.21 | 0.85 | +4.7 | +3.6 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 30.3% | 10.0% | 10.0% | 30.0% | -0.7 | 0.51 | 3.59 | +4.0 | +3.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 6.1% | 0.0% | 0.0% | 0.0% | -0.1 | 0.00 | 0.00 | +3.9 | +1.7 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=13 Fav=15.4% Avg=-4.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 47.1% | -4.5 | 0.30 | 1.36 | +8.0 | +5.8 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 76.5% | 15.4% | 15.4% | 53.8% | -4.1 | 0.38 | 1.15 | +9.5 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 88.2% | 13.3% | 13.3% | 46.7% | -4.6 | 0.33 | 1.30 | +8.6 | +5.7 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 47.1% | -4.5 | 0.30 | 1.36 | +8.0 | +5.8 |
| `asian_range_gte_30` | 8 | S_STRANGER | 47.1% | 12.5% | 12.5% | 62.5% | -2.4 | 0.55 | 1.66 | +12.6 | +5.5 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 47.1% | -4.5 | 0.30 | 1.36 | +8.0 | +5.8 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 47.1% | -4.5 | 0.30 | 1.36 | +8.0 | +5.8 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 88.2% | 13.3% | 13.3% | 46.7% | -4.6 | 0.32 | 1.29 | +7.5 | +6.1 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 23.5% | 25.0% | 25.0% | 50.0% | +2.2 | 1.57 | 3.14 | +13.3 | +7.4 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 47.1% | 12.5% | 12.5% | 62.5% | -2.4 | 0.55 | 1.66 | +12.6 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 57.1% | -2.8 | 0.55 | 1.66 | +11.5 | +5.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 82.4% | 14.3% | 14.3% | 57.1% | -3.8 | 0.38 | 1.15 | +9.3 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 47.1% | -4.5 | 0.30 | 1.36 | +8.0 | +5.8 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 29.4% | 0.0% | 0.0% | 20.0% | -17.1 | 0.00 | 0.00 | +3.4 | +4.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -7.7 | 0.00 | 0.00 | +1.8 | +11.8 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=25.0% Avg=-0.5; validation N=11 Fav=9.1% Avg=-9.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 43 | S_STRANGER | 100.0% | 11.6% | 14.0% | 9.3% | -3.9 | 0.26 | 1.44 | +6.1 | +8.7 |
| `hunt_to_ar_ratio_le_2_0` | 36 | S_STRANGER | 83.7% | 11.1% | 13.9% | 11.1% | -4.1 | 0.27 | 1.45 | +6.1 | +9.1 |
| `hunt_to_ar_ratio_le_2_5` | 39 | S_STRANGER | 90.7% | 12.8% | 15.4% | 10.3% | -4.0 | 0.28 | 1.34 | +6.2 | +9.0 |
| `stop_hunt_le_90` | 43 | S_STRANGER | 100.0% | 11.6% | 14.0% | 9.3% | -3.9 | 0.26 | 1.44 | +6.1 | +8.7 |
| `asian_range_gte_30` | 24 | S_STRANGER | 55.8% | 16.7% | 16.7% | 16.7% | -4.7 | 0.31 | 1.33 | +6.7 | +7.7 |
| `confluence_gte_60` | 28 | S_STRANGER | 65.1% | 14.3% | 14.3% | 10.7% | -3.2 | 0.37 | 2.02 | +7.2 | +9.6 |
| `confluence_gte_70` | 2 | R_REPEATER | 4.7% | 50.0% | 50.0% | 50.0% | +2.3 | 999.00 | 999.00 | +7.3 | +3.0 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 16.3% | 0.0% | 0.0% | 0.0% | -10.6 | 0.00 | 0.00 | +4.7 | +10.8 |
| `tdi_rsi_gte_50` | 31 | S_STRANGER | 72.1% | 12.9% | 12.9% | 9.7% | -2.4 | 0.39 | 2.23 | +6.5 | +8.1 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 53.5% | 17.4% | 17.4% | 17.4% | -4.7 | 0.32 | 1.29 | +7.0 | +7.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 7.0% | 0.0% | 0.0% | 0.0% | -18.2 | 0.00 | 0.00 | +3.9 | +12.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 43 | S_STRANGER | 100.0% | 11.6% | 14.0% | 9.3% | -3.9 | 0.26 | 1.44 | +6.1 | +8.7 |
| `feature_stale_hod_exhaustion_reject` | 43 | S_STRANGER | 100.0% | 11.6% | 14.0% | 9.3% | -3.9 | 0.26 | 1.44 | +6.1 | +8.7 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 7.0% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +1.5 | +9.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.3% | 0.0% | 0.0% | 0.0% | -11.4 | 0.00 | 0.00 | +0.8 | +12.6 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=+4.9; validation N=2 Fav=0.0% Avg=-6.6; out_of_sample N=6 Fav=16.7% Avg=-1.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 10.5% | 21.1% | 15.8% | -1.6 | 0.59 | 1.90 | +7.0 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 100.0% | 10.5% | 21.1% | 15.8% | -1.6 | 0.59 | 1.90 | +7.0 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 10.5% | 21.1% | 15.8% | -1.6 | 0.59 | 1.90 | +7.0 | +5.2 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 10.5% | 21.1% | 15.8% | -1.6 | 0.59 | 1.90 | +7.0 | +5.2 |
| `asian_range_gte_30` | 11 | S_STRANGER | 57.9% | 18.2% | 27.3% | 18.2% | -0.6 | 0.86 | 2.01 | +8.6 | +4.6 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 10.5% | 21.1% | 15.8% | -1.6 | 0.59 | 1.90 | +7.0 | +5.2 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 10.5% | 21.1% | 15.8% | -1.6 | 0.59 | 1.90 | +7.0 | +5.2 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 47.4% | 0.0% | 11.1% | 11.1% | -6.3 | 0.03 | 0.20 | +4.0 | +4.8 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 52.6% | 10.0% | 10.0% | 0.0% | -3.0 | 0.33 | 2.99 | +6.5 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 57.9% | 18.2% | 27.3% | 18.2% | -0.6 | 0.86 | 2.01 | +8.6 | +4.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 21.1% | 0.0% | 0.0% | 0.0% | -10.2 | 0.00 | 0.00 | +1.9 | +5.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 10.5% | 21.1% | 15.8% | -1.6 | 0.59 | 1.90 | +7.0 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 10.5% | 21.1% | 15.8% | -1.6 | 0.59 | 1.90 | +7.0 | +5.2 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 5.3% | 100.0% | 100.0% | 100.0% | +24.2 | 999.00 | 999.00 | +27.7 | +0.0 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+2.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-3.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 20.0% | -0.2 | 0.96 | 3.35 | +9.5 | +7.8 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 40.0% | 0.0% | 25.0% | 0.0% | -2.7 | 0.25 | 0.76 | +7.5 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 50.0% | 0.0% | 20.0% | 0.0% | -3.2 | 0.19 | 0.74 | +6.4 | +8.6 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 20.0% | -0.2 | 0.96 | 3.35 | +9.5 | +7.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 20.0% | -0.2 | 0.96 | 3.35 | +9.5 | +7.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 25.0% | -2.7 | 0.00 | 0.00 | +6.7 | +9.2 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 16.7% | +1.5 | 1.32 | 6.59 | +11.6 | +9.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 20.0% | -0.2 | 0.96 | 3.35 | +9.5 | +7.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 20.0% | -0.2 | 0.96 | 3.35 | +9.5 | +7.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +8.8 | +3.8 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=25.0% Avg=-1.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 10.0% | 20.0% | 5.0% | -2.6 | 0.38 | 1.43 | +7.3 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 11.1% | 22.2% | 5.6% | -2.2 | 0.44 | 1.42 | +7.2 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 10.0% | 20.0% | 5.0% | -2.6 | 0.38 | 1.43 | +7.3 | +7.1 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 10.0% | 20.0% | 5.0% | -2.6 | 0.38 | 1.43 | +7.3 | +7.1 |
| `asian_range_gte_30` | 11 | S_STRANGER | 55.0% | 18.2% | 27.3% | 9.1% | -2.6 | 0.51 | 1.36 | +9.2 | +8.5 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 10.0% | 20.0% | 5.0% | -2.6 | 0.38 | 1.43 | +7.3 | +7.1 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 10.0% | 20.0% | 5.0% | -2.6 | 0.38 | 1.43 | +7.3 | +7.1 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 65.0% | 15.4% | 30.8% | 7.7% | -2.4 | 0.51 | 1.14 | +9.1 | +7.6 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 75.0% | 13.3% | 13.3% | 6.7% | -3.3 | 0.32 | 1.92 | +8.4 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 55.0% | 18.2% | 27.3% | 9.1% | -2.6 | 0.51 | 1.36 | +9.2 | +8.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 40.0% | 25.0% | 37.5% | 12.5% | -1.7 | 0.69 | 1.16 | +11.1 | +8.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 10.0% | 20.0% | 5.0% | -2.6 | 0.38 | 1.43 | +7.3 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 10.0% | 20.0% | 5.0% | -2.6 | 0.38 | 1.43 | +7.3 | +7.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 15.0% | 0.0% | 33.3% | 0.0% | -3.1 | 0.11 | 0.23 | +2.3 | +4.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 10.0% | 50.0% | 50.0% | 0.0% | -3.0 | 0.02 | 0.02 | +10.1 | +5.7 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=10.0% Avg=-2.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -2.7 | 0.37 | 2.94 | +6.3 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -1.0 | 0.80 | 2.40 | +7.1 | +6.6 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -2.7 | 0.37 | 2.94 | +6.3 | +7.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -2.7 | 0.37 | 2.94 | +6.3 | +7.2 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -2.7 | 0.37 | 2.94 | +6.3 | +7.2 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +5.5 | +6.7 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +5.4 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -2.7 | 0.37 | 2.94 | +6.3 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -2.7 | 0.37 | 2.94 | +6.3 | +7.2 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 33.3% | -5.6 | 0.00 | 0.00 | +3.2 | +9.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +3.4 | +6.6 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-4.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 0.0% | -5.7 | 0.29 | 1.14 | +10.9 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 70.0% | 14.3% | 28.6% | 0.0% | -5.4 | 0.38 | 0.94 | +8.6 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 80.0% | 12.5% | 25.0% | 0.0% | -5.8 | 0.33 | 0.99 | +9.0 | +5.1 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 0.0% | -5.7 | 0.29 | 1.14 | +10.9 | +6.3 |
| `asian_range_gte_30` | 6 | S_STRANGER | 60.0% | 16.7% | 33.3% | 0.0% | -4.7 | 0.45 | 0.89 | +9.5 | +3.4 |
| `confluence_gte_60` | 8 | S_STRANGER | 80.0% | 0.0% | 12.5% | 0.0% | -9.8 | 0.01 | 0.07 | +8.4 | +7.4 |
| `confluence_gte_70` | 5 | S_STRANGER | 50.0% | 0.0% | 20.0% | 0.0% | -11.5 | 0.01 | 0.05 | +6.9 | +5.4 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -7.2 | 0.00 | 0.00 | +12.2 | +9.0 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | +2.6 | 1.86 | 5.57 | +19.4 | +6.8 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 60.0% | 16.7% | 33.3% | 0.0% | -4.7 | 0.45 | 0.89 | +9.5 | +3.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -7.1 | 0.00 | 0.00 | +11.0 | +5.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 11.1% | 22.2% | 0.0% | -5.5 | 0.32 | 1.11 | +10.7 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 0.0% | -5.7 | 0.29 | 1.14 | +10.9 | +6.3 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -8.9 | 0.00 | 0.00 | +7.6 | +10.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=10.0% Avg=-8.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -8.5 | 0.16 | 0.63 | +5.6 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -8.5 | 0.16 | 0.63 | +5.6 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -8.5 | 0.16 | 0.63 | +5.6 | +5.0 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -8.5 | 0.16 | 0.63 | +5.6 | +5.0 |
| `asian_range_gte_30` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -7.9 | 0.00 | 0.00 | +1.6 | +6.2 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -8.5 | 0.16 | 0.63 | +5.6 | +5.0 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -8.5 | 0.16 | 0.63 | +5.6 | +5.0 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | -1.5 | 0.69 | 1.38 | +10.1 | +8.9 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | -1.5 | 0.69 | 1.38 | +10.1 | +8.9 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -7.9 | 0.00 | 0.00 | +1.6 | +6.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -7.1 | 0.00 | 0.00 | +3.0 | +8.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -8.5 | 0.16 | 0.63 | +5.6 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -8.5 | 0.16 | 0.63 | +5.6 | +5.0 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 33.3% | 0.0% | -18.0 | 0.10 | 0.20 | +6.4 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +0.9 | 1.24 | 1.24 | +14.8 | +9.1 |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+0.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -0.7 | 0.58 | 5.22 | +4.6 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 50.0% | -1.7 | 0.00 | 0.00 | +5.7 | +3.7 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 20.0% | -2.1 | 0.00 | 0.00 | +4.5 | +5.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -0.7 | 0.58 | 5.22 | +4.6 | +3.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -0.7 | 0.58 | 5.22 | +4.6 | +3.9 |
| `confluence_gte_70` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 12.5% | -0.5 | 0.74 | 5.21 | +4.0 | +4.0 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 20.0% | -0.5 | 0.69 | 5.49 | +4.8 | +3.9 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 0.0% | -2.0 | 0.00 | 0.00 | +3.4 | +4.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 22.2% | -0.6 | 0.66 | 4.65 | +4.4 | +3.9 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -0.7 | 0.58 | 5.22 | +4.6 | +3.9 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | +0.8 | 1.67 | 6.67 | +5.6 | +3.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +5.8 | +4.1 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-1.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.7 | 0.15 | 1.36 | +4.5 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 100.0% | +3.4 | 999.00 | 999.00 | +18.8 | +0.9 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | -1.9 | 0.26 | 1.05 | +7.5 | +3.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.7 | 0.15 | 1.36 | +4.5 | +3.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +4.0 | +4.3 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +1.5 | +3.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 11.1% | -1.4 | 0.22 | 1.52 | +5.3 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 11.1% | -1.4 | 0.22 | 1.52 | +5.3 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 10.0% | -1.9 | 0.15 | 1.23 | +4.8 | +3.6 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 63.6% | 14.3% | 14.3% | 14.3% | -2.3 | 0.17 | 1.05 | +5.6 | +4.3 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 54.5% | 16.7% | 16.7% | 16.7% | -1.6 | 0.26 | 1.30 | +6.5 | +3.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=14 Fav=7.1% Avg=-4.2; validation N=7 Fav=14.3% Avg=+1.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -2.1 | 0.43 | 3.67 | +6.7 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +2.1 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 50.0% | 9.1% | 9.1% | 9.1% | -1.9 | 0.07 | 0.68 | +3.4 | +4.2 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -2.1 | 0.43 | 3.67 | +6.7 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 31.8% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +2.4 | +2.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 72.7% | 6.2% | 6.2% | 18.8% | -0.5 | 0.81 | 9.74 | +8.0 | +4.8 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 27.3% | 0.0% | 0.0% | 16.7% | -1.8 | 0.00 | 0.00 | +5.8 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 95.5% | 9.5% | 9.5% | 19.0% | -2.2 | 0.43 | 3.67 | +7.0 | +4.2 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -2.1 | 0.43 | 3.67 | +6.7 | +4.1 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +2.7 | +2.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-1.7; validation N=1 Fav=100.0% Avg=+11.7; out_of_sample N=4 Fav=0.0% Avg=-4.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -2.4 | 0.31 | 3.09 | +4.0 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 11.1% | -1.8 | 0.42 | 3.38 | +4.2 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -2.4 | 0.31 | 3.09 | +4.0 | +6.4 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -2.4 | 0.31 | 3.09 | +4.0 | +6.4 |
| `asian_range_gte_30` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -1.7 | 0.00 | 0.00 | +10.4 | +3.6 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -2.4 | 0.31 | 3.09 | +4.0 | +6.4 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -2.4 | 0.31 | 3.09 | +4.0 | +6.4 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +4.5 | +4.5 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 54.5% | 16.7% | 16.7% | 16.7% | -1.4 | 0.58 | 2.92 | +5.7 | +6.6 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -1.7 | 0.00 | 0.00 | +10.4 | +3.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -1.7 | 0.00 | 0.00 | +10.4 | +3.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -2.4 | 0.31 | 3.09 | +4.0 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -2.4 | 0.31 | 3.09 | +4.0 | +6.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=12.5% Avg=-3.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -4.5 | 0.30 | 3.03 | +6.0 | +11.0 |
| `hunt_to_ar_ratio_le_2_0` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -13.3 | 0.00 | 0.00 | +2.9 | +19.2 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -9.8 | 0.00 | 0.00 | +3.5 | +16.1 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -4.5 | 0.30 | 3.03 | +6.0 | +11.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -4.5 | 0.30 | 3.03 | +6.0 | +11.0 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -4.5 | 0.30 | 3.03 | +6.0 | +11.0 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -17.5 | 0.00 | 0.00 | +1.7 | +24.2 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 12.5% | -4.9 | 0.35 | 2.47 | +6.9 | +12.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 12.5% | -3.3 | 0.44 | 3.11 | +7.6 | +10.9 |
| `feature_stale_hod_exhaustion_reject` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 11.1% | -3.7 | 0.39 | 3.10 | +7.1 | +10.5 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -7.4 | 0.00 | 0.00 | +2.4 | +9.6 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -7.7 | 0.00 | 0.00 | +1.1 | +13.2 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=11.1% Avg=+0.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -0.8 | 0.49 | 4.40 | +5.0 | +3.1 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -1.0 | 0.00 | 0.00 | +9.1 | +3.5 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 58.3% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +5.9 | +3.9 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -0.8 | 0.49 | 4.40 | +5.0 | +3.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 0.0% | -0.4 | 0.69 | 5.50 | +2.8 | +2.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -2.0 | 0.00 | 0.00 | +2.2 | +3.1 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 0.0% | -0.9 | 0.52 | 3.15 | +5.6 | +3.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 0.0% | +0.0 | 1.01 | 6.07 | +6.1 | +2.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 83.3% | 10.0% | 10.0% | 0.0% | -0.4 | 0.69 | 5.50 | +4.3 | +2.7 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 0.0% | -0.7 | 0.62 | 3.74 | +4.6 | +3.2 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 0.0% | -0.8 | 0.68 | 2.05 | +5.4 | +4.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-4.1; validation N=2 Fav=50.0% Avg=+5.1; out_of_sample N=6 Fav=0.0% Avg=-4.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -3.5 | 0.29 | 2.90 | +5.2 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 50.0% | +1.5 | 1.55 | 3.11 | +7.6 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 22.2% | -2.6 | 0.42 | 2.96 | +5.0 | +6.5 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -3.5 | 0.29 | 2.90 | +5.2 | +7.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -3.5 | 0.29 | 2.90 | +5.2 | +7.4 |
| `confluence_gte_70` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 25.0% | -6.4 | 0.00 | 0.00 | +3.0 | +8.1 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +5.2 | +8.3 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 83.3% | 10.0% | 10.0% | 20.0% | -3.7 | 0.31 | 2.51 | +5.4 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -3.5 | 0.29 | 2.90 | +5.2 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -3.5 | 0.29 | 2.90 | +5.2 | +7.4 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -4.1 | 0.00 | 0.00 | +1.2 | +4.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -4.1 | 0.00 | 0.00 | +1.2 | +4.8 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-2.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-1.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -4.8 | 0.20 | 1.99 | +5.4 | +10.8 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -4.8 | 0.20 | 1.99 | +5.4 | +10.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -4.8 | 0.20 | 1.99 | +5.4 | +10.8 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -4.8 | 0.20 | 1.99 | +5.4 | +10.8 |
| `asian_range_gte_30` | 7 | S_STRANGER | 58.3% | 0.0% | 0.0% | 0.0% | -7.7 | 0.00 | 0.00 | +3.4 | +12.7 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -4.8 | 0.20 | 1.99 | +5.4 | +10.8 |
| `confluence_gte_70` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | +6.9 | 23.83 | 23.83 | +8.4 | +1.7 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 0.0% | 0.0% | 0.0% | -9.0 | 0.00 | 0.00 | +4.1 | +15.6 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 33.3% | -1.9 | 0.56 | 2.23 | +7.1 | +8.6 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 58.3% | 0.0% | 0.0% | 0.0% | -7.7 | 0.00 | 0.00 | +3.4 | +12.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -11.3 | 0.00 | 0.00 | +4.1 | +18.4 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -9.8 | 0.00 | 0.00 | +1.0 | +10.7 |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -4.8 | 0.20 | 1.99 | +5.4 | +10.8 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -4.8 | 0.20 | 1.99 | +5.4 | +10.8 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 25.0% | -6.1 | 0.00 | 0.00 | +5.8 | +11.7 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 25.0% | -6.1 | 0.00 | 0.00 | +5.8 | +11.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-12.3; validation N=5 Fav=20.0% Avg=-2.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 16.7% | -9.0 | 0.11 | 0.64 | +4.1 | +4.5 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 37.5% | 0.0% | 0.0% | 11.1% | -4.7 | 0.00 | 0.00 | +3.2 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 41.7% | 0.0% | 0.0% | 10.0% | -7.0 | 0.00 | 0.00 | +3.2 | +4.6 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 16.7% | -9.0 | 0.11 | 0.64 | +4.1 | +4.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 45.8% | 18.2% | 18.2% | 27.3% | -7.7 | 0.22 | 0.76 | +5.2 | +5.6 |
| `confluence_gte_70` | 4 | S_STRANGER | 16.7% | 25.0% | 25.0% | 50.0% | -9.9 | 0.33 | 0.65 | +9.1 | +6.8 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 62.5% | 13.3% | 20.0% | 20.0% | -2.3 | 0.44 | 1.32 | +4.6 | +5.7 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 16.7% | 25.0% | 50.0% | 25.0% | -1.6 | 0.78 | 0.78 | +7.3 | +10.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 16.7% | -9.0 | 0.11 | 0.64 | +4.1 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 16.7% | -9.0 | 0.11 | 0.64 | +4.1 | +4.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-3.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-0.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -10.5 | 0.13 | 1.47 | +8.0 | +6.9 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -8.1 | 0.26 | 1.53 | +6.6 | +9.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 83.3% | 10.0% | 10.0% | 0.0% | -8.5 | 0.19 | 1.68 | +8.6 | +7.6 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -10.5 | 0.13 | 1.47 | +8.0 | +6.9 |
| `asian_range_gte_30` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -7.8 | 0.00 | 0.00 | +12.8 | +11.3 |
| `confluence_gte_60` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -20.6 | 0.00 | 0.00 | +5.2 | +1.9 |
| `confluence_gte_70` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -20.7 | 0.00 | 0.00 | +4.9 | +2.5 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -2.9 | 0.49 | 2.94 | +10.8 | +9.7 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -2.9 | 0.49 | 2.94 | +10.8 | +9.7 |
| `ratio_le_2_and_asian_gte_30` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -12.2 | 0.00 | 0.00 | +7.9 | +16.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -12.2 | 0.00 | 0.00 | +7.9 | +16.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 0.0% | -11.0 | 0.14 | 1.38 | +6.7 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -10.5 | 0.13 | 1.47 | +8.0 | +6.9 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -21.6 | 0.00 | 0.00 | +3.0 | +3.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +12.5 | +10.1 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-1.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 8.1% | 8.1% | 10.8% | -5.1 | 0.09 | 0.88 | +3.7 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 16.2% | 16.7% | 16.7% | 16.7% | -1.3 | 0.40 | 1.61 | +4.0 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 40.5% | 6.7% | 6.7% | 6.7% | -3.9 | 0.08 | 1.08 | +4.1 | +5.5 |
| `stop_hunt_le_90` | 37 | S_STRANGER | 100.0% | 8.1% | 8.1% | 10.8% | -5.1 | 0.09 | 0.88 | +3.7 | +6.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 37.8% | 14.3% | 14.3% | 14.3% | -5.6 | 0.16 | 0.87 | +3.8 | +2.3 |
| `confluence_gte_70` | 4 | S_STRANGER | 10.8% | 25.0% | 25.0% | 25.0% | +2.0 | 7.12 | 14.23 | +5.2 | +0.8 |
| `tdi_rsi_gt_signal` | 22 | S_STRANGER | 59.5% | 4.5% | 4.5% | 0.0% | -6.1 | 0.03 | 0.52 | +3.7 | +8.6 |
| `tdi_rsi_gte_50` | 27 | S_STRANGER | 73.0% | 7.4% | 7.4% | 3.7% | -3.7 | 0.11 | 1.30 | +3.9 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 86.5% | 9.4% | 9.4% | 12.5% | -5.4 | 0.09 | 0.79 | +3.7 | +6.9 |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 8.1% | 8.1% | 10.8% | -5.1 | 0.09 | 0.88 | +3.7 | +6.4 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 16.2% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +3.4 | +3.5 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 13.5% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +3.6 | +3.3 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=0.0% Avg=-10.3; out_of_sample N=17 Fav=11.8% Avg=-9.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 8.0% | 8.0% | 8.0% | -9.9 | 0.08 | 0.96 | +3.9 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 96.0% | 8.3% | 8.3% | 8.3% | -9.5 | 0.09 | 0.99 | +3.8 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 100.0% | 8.0% | 8.0% | 8.0% | -9.9 | 0.08 | 0.96 | +3.9 | +6.1 |
| `stop_hunt_le_90` | 25 | S_STRANGER | 100.0% | 8.0% | 8.0% | 8.0% | -9.9 | 0.08 | 0.96 | +3.9 | +6.1 |
| `asian_range_gte_30` | 16 | S_STRANGER | 64.0% | 6.2% | 6.2% | 6.2% | -10.4 | 0.05 | 0.69 | +3.6 | +6.2 |
| `confluence_gte_60` | 25 | S_STRANGER | 100.0% | 8.0% | 8.0% | 8.0% | -9.9 | 0.08 | 0.96 | +3.9 | +6.1 |
| `confluence_gte_70` | 15 | S_STRANGER | 60.0% | 6.7% | 6.7% | 6.7% | -12.7 | 0.07 | 0.99 | +4.0 | +6.8 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 56.0% | 7.1% | 7.1% | 7.1% | -9.0 | 0.10 | 1.34 | +4.7 | +5.9 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 32.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +2.6 | +8.2 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 64.0% | 6.2% | 6.2% | 6.2% | -10.4 | 0.05 | 0.69 | +3.6 | +6.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 24.0% | 0.0% | 0.0% | 0.0% | -11.0 | 0.00 | 0.00 | +4.1 | +5.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 100.0% | 8.0% | 8.0% | 8.0% | -9.9 | 0.08 | 0.96 | +3.9 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 8.0% | 8.0% | 8.0% | -9.9 | 0.08 | 0.96 | +3.9 | +6.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-13.0; validation N=2 Fav=50.0% Avg=+10.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -8.7 | 0.18 | 2.14 | +5.0 | +8.6 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -8.8 | 0.00 | 0.00 | +3.6 | +2.7 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 46.2% | 16.7% | 16.7% | 16.7% | -5.0 | 0.45 | 2.24 | +8.8 | +2.0 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -8.7 | 0.18 | 2.14 | +5.0 | +8.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 25.0% | -4.8 | 0.56 | 1.69 | +11.0 | +14.2 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +8.5 | +1.3 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 69.2% | 0.0% | 0.0% | 0.0% | -11.1 | 0.00 | 0.00 | +3.7 | +10.9 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -7.5 | 0.00 | 0.00 | +2.7 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -8.7 | 0.18 | 2.14 | +5.0 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -8.7 | 0.18 | 2.14 | +5.0 | +8.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=10.0% Avg=-5.5; validation N=1 Fav=0.0% Avg=-3.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -9.4 | 0.22 | 2.62 | +7.2 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -31.6 | 0.00 | 0.00 | +1.0 | +2.9 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -23.4 | 0.00 | 0.00 | +1.3 | +2.6 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -9.4 | 0.22 | 2.62 | +7.2 | +4.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 9.1% | 9.1% | 9.1% | -5.4 | 0.37 | 3.67 | +8.3 | +5.2 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 25.0% | +4.9 | 2.38 | 7.15 | +14.5 | +7.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 84.6% | 9.1% | 9.1% | 9.1% | -9.7 | 0.24 | 2.42 | +8.2 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -9.4 | 0.22 | 2.62 | +7.2 | +4.8 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -21.3 | 0.00 | 0.00 | +1.2 | +2.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +2.1 | +7.2 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=10.0% Avg=-1.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 6.9% | 10.3% | 17.2% | -4.7 | 0.19 | 1.45 | +5.3 | +7.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 34.5% | 0.0% | 0.0% | 20.0% | -4.4 | 0.00 | 0.00 | +4.9 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 51.7% | 0.0% | 6.7% | 20.0% | -4.0 | 0.03 | 0.37 | +4.8 | +5.2 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 100.0% | 6.9% | 10.3% | 17.2% | -4.7 | 0.19 | 1.45 | +5.3 | +7.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 20.7% | 0.0% | 0.0% | 0.0% | -7.8 | 0.00 | 0.00 | +3.5 | +9.6 |
| `confluence_gte_70` | 1 | S_STRANGER | 3.4% | 0.0% | 0.0% | 0.0% | -23.8 | 0.00 | 0.00 | +0.1 | +25.4 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 37.9% | 9.1% | 9.1% | 18.2% | -7.0 | 0.14 | 1.23 | +5.9 | +11.5 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 37.9% | 0.0% | 0.0% | 0.0% | -8.8 | 0.00 | 0.00 | +5.0 | +11.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 72.4% | 4.8% | 4.8% | 19.0% | -5.2 | 0.14 | 2.38 | +5.2 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 6.9% | 10.3% | 17.2% | -4.7 | 0.19 | 1.45 | +5.3 | +7.9 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 34.5% | 10.0% | 20.0% | 20.0% | -1.4 | 0.51 | 1.77 | +5.8 | +4.7 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 17.2% | 0.0% | 0.0% | 0.0% | -6.7 | 0.00 | 0.00 | +6.1 | +9.9 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=10.0% Avg=-7.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-1.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -5.6 | 0.18 | 1.10 | +6.5 | +9.2 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -5.6 | 0.18 | 1.10 | +6.5 | +9.2 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -5.6 | 0.18 | 1.10 | +6.5 | +9.2 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -5.6 | 0.18 | 1.10 | +6.5 | +9.2 |
| `asian_range_gte_30` | 12 | S_STRANGER | 80.0% | 8.3% | 16.7% | 8.3% | -6.3 | 0.20 | 0.89 | +7.0 | +10.3 |
| `confluence_gte_60` | 13 | S_STRANGER | 86.7% | 7.7% | 7.7% | 7.7% | -5.8 | 0.06 | 0.71 | +6.3 | +8.6 |
| `confluence_gte_70` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 0.0% | -9.4 | 0.00 | 0.00 | +3.0 | +10.7 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 33.3% | 0.0% | 0.0% | 20.0% | -9.6 | 0.00 | 0.00 | +6.5 | +14.3 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 73.3% | 9.1% | 9.1% | 9.1% | -7.2 | 0.06 | 0.55 | +7.0 | +11.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 80.0% | 8.3% | 16.7% | 8.3% | -6.3 | 0.20 | 0.89 | +7.0 | +10.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 25.0% | -11.6 | 0.00 | 0.00 | +6.1 | +16.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -5.6 | 0.18 | 1.10 | +6.5 | +9.2 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 6.7% | -5.6 | 0.18 | 1.10 | +6.5 | +9.2 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 13.3% | 0.0% | 50.0% | 0.0% | +2.5 | 1.60 | 1.60 | +7.9 | +4.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -11.4 | 0.00 | 0.00 | +4.5 | +12.3 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=14.3% Avg=-6.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 13.3% | -6.3 | 0.11 | 0.65 | +6.4 | +9.1 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -9.8 | 0.00 | 0.00 | +5.7 | +11.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 80.0% | 0.0% | 8.3% | 0.0% | -8.1 | 0.06 | 0.65 | +5.7 | +10.4 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 13.3% | -6.3 | 0.11 | 0.65 | +6.4 | +9.1 |
| `asian_range_gte_30` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +11.3 | +9.9 |
| `confluence_gte_60` | 8 | S_STRANGER | 53.3% | 12.5% | 12.5% | 25.0% | -4.6 | 0.12 | 0.74 | +7.1 | +7.4 |
| `confluence_gte_70` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +6.0 | +9.9 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 0.0% | -8.5 | 0.00 | 0.00 | +6.2 | +11.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 46.7% | 0.0% | 0.0% | 0.0% | -7.4 | 0.00 | 0.00 | +7.5 | +11.2 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +11.3 | +9.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +11.3 | +9.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 86.7% | 0.0% | 7.7% | 7.7% | -7.4 | 0.06 | 0.66 | +6.8 | +10.0 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 93.3% | 7.1% | 14.3% | 14.3% | -6.2 | 0.11 | 0.63 | +6.6 | +9.0 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 46.7% | 14.3% | 14.3% | 14.3% | -6.8 | 0.10 | 0.60 | +4.3 | +8.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -7.6 | 0.00 | 0.00 | +6.4 | +9.8 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+1.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 6.2% | 6.2% | 12.5% | -2.8 | 0.44 | 6.18 | +9.7 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 93.8% | 6.7% | 6.7% | 13.3% | -2.5 | 0.48 | 6.26 | +9.7 | +6.8 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 6.2% | 6.2% | 12.5% | -2.8 | 0.44 | 6.18 | +9.7 | +7.0 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 6.2% | 6.2% | 12.5% | -2.8 | 0.44 | 6.18 | +9.7 | +7.0 |
| `asian_range_gte_30` | 13 | S_STRANGER | 81.2% | 7.7% | 7.7% | 15.4% | -1.7 | 0.62 | 6.77 | +11.5 | +6.9 |
| `confluence_gte_60` | 10 | S_STRANGER | 62.5% | 10.0% | 10.0% | 20.0% | -0.7 | 0.84 | 6.72 | +10.3 | +7.2 |
| `confluence_gte_70` | 6 | S_STRANGER | 37.5% | 0.0% | 0.0% | 16.7% | -5.2 | 0.00 | 0.00 | +7.5 | +8.6 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 75.0% | 8.3% | 8.3% | 16.7% | -1.4 | 0.67 | 6.70 | +11.3 | +7.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 62.5% | 10.0% | 10.0% | 20.0% | -0.6 | 0.85 | 6.83 | +14.0 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 75.0% | 8.3% | 8.3% | 16.7% | -1.3 | 0.70 | 6.96 | +11.7 | +6.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 56.2% | 11.1% | 11.1% | 22.2% | -0.5 | 0.89 | 6.24 | +13.7 | +6.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 6.2% | 6.2% | 12.5% | -2.8 | 0.44 | 6.18 | +9.7 | +7.0 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 6.2% | 6.2% | 12.5% | -2.8 | 0.44 | 6.18 | +9.7 | +7.0 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 18.8% | 0.0% | 0.0% | 0.0% | -8.6 | 0.00 | 0.00 | +9.6 | +10.8 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 20.0% | +1.3 | 1.22 | 4.88 | +16.0 | +9.7 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=0.0% Avg=-1.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 38.5% | -2.2 | 0.00 | 0.00 | +5.0 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 30.8% | 0.0% | 0.0% | 50.0% | -2.9 | 0.00 | 0.00 | +5.1 | +4.3 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 38.5% | -2.2 | 0.00 | 0.00 | +5.0 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +1.7 | +6.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 30.8% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +1.5 | +6.8 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +1.2 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 38.5% | -2.2 | 0.00 | 0.00 | +5.0 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 38.5% | -2.2 | 0.00 | 0.00 | +5.0 | +3.8 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 69.2% | 0.0% | 0.0% | 44.4% | -1.8 | 0.00 | 0.00 | +5.4 | +3.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +2.7 | +7.4 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.8; validation N=5 Fav=0.0% Avg=-1.4; out_of_sample N=3 Fav=0.0% Avg=-3.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 25.0% | -2.4 | 0.15 | 1.21 | +3.7 | +4.0 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 25.0% | -2.4 | 0.15 | 1.21 | +3.7 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 25.0% | -2.4 | 0.15 | 1.21 | +3.7 | +4.0 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 25.0% | -2.4 | 0.15 | 1.21 | +3.7 | +4.0 |
| `asian_range_gte_30` | 6 | S_STRANGER | 50.0% | 0.0% | 0.0% | 50.0% | -3.5 | 0.00 | 0.00 | +3.7 | +3.6 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 25.0% | -2.4 | 0.15 | 1.21 | +3.7 | +4.0 |
| `confluence_gte_70` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 50.0% | -2.1 | 0.00 | 0.00 | +3.7 | +1.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 75.0% | 0.0% | 11.1% | 22.2% | -2.0 | 0.22 | 1.31 | +3.6 | +4.6 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +3.1 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 50.0% | 0.0% | 0.0% | 50.0% | -3.5 | 0.00 | 0.00 | +3.7 | +3.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 50.0% | -3.3 | 0.00 | 0.00 | +2.8 | +5.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 25.0% | -2.4 | 0.15 | 1.21 | +3.7 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 25.0% | -2.4 | 0.15 | 1.21 | +3.7 | +4.0 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 50.0% | -0.4 | 0.00 | 0.00 | +2.8 | +1.1 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=0.0% Avg=-2.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 18.2% | -3.6 | 0.00 | 0.00 | +4.3 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 66.7% | -0.7 | 0.00 | 0.00 | +9.0 | +3.2 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 18.2% | -3.6 | 0.00 | 0.00 | +4.3 | +5.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 81.8% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +2.6 | +5.3 |
| `confluence_gte_70` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +2.1 | +6.5 |
| `tdi_rsi_gt_signal` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 16.7% | -2.8 | 0.00 | 0.00 | +4.1 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 81.8% | 0.0% | 0.0% | 22.2% | -4.2 | 0.00 | 0.00 | +4.4 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 18.2% | -3.6 | 0.00 | 0.00 | +4.3 | +5.0 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +3.4 | +2.9 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -1.7 | 0.00 | 0.00 | +3.2 | +3.0 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-3.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -4.1 | 0.00 | 0.00 | +4.5 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +3.5 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +4.9 | +6.0 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -4.1 | 0.00 | 0.00 | +4.5 | +5.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +0.0 | +7.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 12.5% | -4.0 | 0.00 | 0.00 | +5.6 | +5.4 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +6.1 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +3.8 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -4.1 | 0.00 | 0.00 | +4.5 | +5.3 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 50.0% | -2.3 | 0.00 | 0.00 | +6.6 | +3.6 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=0.0% Avg=-0.1; validation N=1 Fav=0.0% Avg=-24.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 36.4% | -4.6 | 0.12 | 0.86 | +8.0 | +7.5 |
| `hunt_to_ar_ratio_le_2_0` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +6.4 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +3.2 | +4.9 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 36.4% | -4.6 | 0.12 | 0.86 | +8.0 | +7.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 36.4% | -4.6 | 0.12 | 0.86 | +8.0 | +7.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 0.0% | 11.1% | 44.4% | -2.8 | 0.22 | 1.09 | +9.1 | +7.4 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -9.9 | 0.00 | 0.00 | +4.3 | +14.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +5.7 | +9.1 |
| `feature_extreme_hunt_with_exception` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 33.3% | -8.4 | 0.00 | 0.00 | +7.3 | +10.5 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 36.4% | -4.6 | 0.12 | 0.86 | +8.0 | +7.5 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 36.4% | 0.0% | 25.0% | 50.0% | +1.0 | 2.45 | 4.90 | +9.5 | +2.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +5.7 | +9.1 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=0.0% Avg=-5.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 7.7% | -5.9 | 0.00 | 0.00 | +5.6 | +9.0 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 0.0% | 0.0% | 8.3% | -5.5 | 0.00 | 0.00 | +5.8 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 7.7% | -5.9 | 0.00 | 0.00 | +5.6 | +9.0 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 7.7% | -5.9 | 0.00 | 0.00 | +5.6 | +9.0 |
| `asian_range_gte_30` | 9 | S_STRANGER | 69.2% | 0.0% | 0.0% | 11.1% | -6.3 | 0.00 | 0.00 | +6.1 | +9.5 |
| `confluence_gte_60` | 7 | S_STRANGER | 53.8% | 0.0% | 0.0% | 14.3% | -5.9 | 0.00 | 0.00 | +4.1 | +9.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -15.8 | 0.00 | 0.00 | +0.6 | +16.9 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 84.6% | 0.0% | 0.0% | 9.1% | -5.9 | 0.00 | 0.00 | +6.3 | +8.9 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 69.2% | 0.0% | 0.0% | 11.1% | -6.3 | 0.00 | 0.00 | +6.1 | +9.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -15.8 | 0.00 | 0.00 | +0.6 | +16.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 92.3% | 0.0% | 0.0% | 8.3% | -5.5 | 0.00 | 0.00 | +5.8 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 84.6% | 0.0% | 0.0% | 9.1% | -5.7 | 0.00 | 0.00 | +5.5 | +9.1 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +2.5 | +10.1 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -7.8 | 0.00 | 0.00 | +3.3 | +10.9 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=0.0% Avg=-5.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +4.6 | +6.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 76.9% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +4.2 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 84.6% | 0.0% | 0.0% | 0.0% | -6.7 | 0.00 | 0.00 | +5.3 | +7.3 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +4.6 | +6.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 4 | S_STRANGER | 30.8% | 0.0% | 0.0% | 0.0% | -6.4 | 0.00 | 0.00 | +2.7 | +7.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +7.9 | +10.2 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +7.9 | +10.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 84.6% | 0.0% | 0.0% | 0.0% | -6.5 | 0.00 | 0.00 | +3.9 | +6.8 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +4.6 | +6.8 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -9.2 | 0.00 | 0.00 | +1.6 | +6.1 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +8.9 | +8.9 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=0.0% Avg=-3.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -8.6 | 0.06 | 0.51 | +11.2 | +13.7 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 60.0% | 0.0% | 16.7% | 0.0% | -3.0 | 0.24 | 0.98 | +8.8 | +6.9 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 0.0% | 11.1% | 0.0% | -9.2 | 0.07 | 0.47 | +10.0 | +13.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -8.6 | 0.06 | 0.51 | +11.2 | +13.7 |
| `asian_range_gte_30` | 3 | S_STRANGER | 30.0% | 0.0% | 33.3% | 0.0% | -2.5 | 0.44 | 0.44 | +6.7 | +9.1 |
| `confluence_gte_60` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -12.1 | 0.00 | 0.00 | +7.0 | +17.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -24.5 | 0.00 | 0.00 | +1.9 | +25.4 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 0.0% | -11.6 | 0.00 | 0.00 | +13.0 | +17.9 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 30.0% | 0.0% | 33.3% | 0.0% | -2.5 | 0.44 | 0.44 | +6.7 | +9.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 70.0% | 0.0% | 14.3% | 0.0% | -5.8 | 0.13 | 0.63 | +7.9 | +10.6 |
| `feature_stale_hod_exhaustion_reject` | 7 | S_STRANGER | 70.0% | 0.0% | 14.3% | 0.0% | -5.8 | 0.13 | 0.63 | +7.9 | +10.6 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 33.3% | 0.0% | -1.5 | 0.57 | 0.57 | +7.0 | +3.9 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -11.3 | 0.00 | 0.00 | +17.5 | +17.9 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-4.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -9.6 | 0.05 | 0.48 | +3.9 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -9.6 | 0.05 | 0.48 | +3.9 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -9.6 | 0.05 | 0.48 | +3.9 | +6.3 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -9.6 | 0.05 | 0.48 | +3.9 | +6.3 |
| `asian_range_gte_30` | 7 | S_STRANGER | 63.6% | 0.0% | 14.3% | 0.0% | -5.9 | 0.11 | 0.69 | +4.0 | +7.7 |
| `confluence_gte_60` | 9 | S_STRANGER | 81.8% | 0.0% | 11.1% | 0.0% | -10.4 | 0.05 | 0.43 | +3.5 | +5.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 72.7% | 0.0% | 12.5% | 0.0% | -8.3 | 0.07 | 0.52 | +4.3 | +7.6 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -7.6 | 0.00 | 0.00 | +6.2 | +14.6 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 63.6% | 0.0% | 14.3% | 0.0% | -5.9 | 0.11 | 0.69 | +4.0 | +7.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 45.5% | 0.0% | 20.0% | 0.0% | -4.7 | 0.18 | 0.74 | +4.3 | +9.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -9.6 | 0.05 | 0.48 | +3.9 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -9.6 | 0.05 | 0.48 | +3.9 | +6.3 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 0.0% | -12.4 | 0.00 | 0.00 | +3.9 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -9.8 | 0.00 | 0.00 | +7.6 | +10.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-17.0; validation N=9 Fav=0.0% Avg=-10.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -11.1 | 0.00 | 0.00 | +4.4 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -30.5 | 0.00 | 0.00 | +3.8 | +11.3 |
| `stop_hunt_le_90` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -26.0 | 0.00 | 0.00 | +2.9 | +8.4 |
| `asian_range_gte_30` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 12.5% | -11.3 | 0.00 | 0.00 | +5.2 | +6.2 |
| `confluence_gte_60` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -15.9 | 0.00 | 0.00 | +4.9 | +2.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 11.1% | -12.1 | 0.00 | 0.00 | +4.8 | +5.6 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -7.4 | 0.00 | 0.00 | +5.1 | +11.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -26.0 | 0.00 | 0.00 | +2.9 | +8.4 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -11.1 | 0.00 | 0.00 | +4.4 | +5.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=10 Fav=0.0% Avg=-9.5; out_of_sample N=4 Fav=0.0% Avg=-16.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 14.3% | -11.4 | 0.00 | 0.00 | +2.6 | +3.4 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 25.0% | -17.8 | 0.00 | 0.00 | +1.8 | +2.4 |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 25.0% | -17.8 | 0.00 | 0.00 | +1.8 | +2.4 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 14.3% | -11.4 | 0.00 | 0.00 | +2.6 | +3.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 14.3% | -11.4 | 0.00 | 0.00 | +2.6 | +3.4 |
| `confluence_gte_70` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 0.0% | -11.8 | 0.00 | 0.00 | +2.6 | +2.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 57.1% | 0.0% | 0.0% | 25.0% | -13.5 | 0.00 | 0.00 | +3.3 | +3.8 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 25.0% | -3.6 | 0.00 | 0.00 | +4.6 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 14.3% | -11.4 | 0.00 | 0.00 | +2.6 | +3.4 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 14.3% | -11.4 | 0.00 | 0.00 | +2.6 | +3.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-10.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -13.9 | 0.00 | 0.00 | +2.6 | +9.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 81.8% | 0.0% | 0.0% | 0.0% | -10.7 | 0.00 | 0.00 | +2.7 | +10.0 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 81.8% | 0.0% | 0.0% | 0.0% | -10.7 | 0.00 | 0.00 | +2.7 | +10.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -13.9 | 0.00 | 0.00 | +2.6 | +9.4 |
| `asian_range_gte_30` | 9 | S_STRANGER | 81.8% | 0.0% | 0.0% | 0.0% | -10.7 | 0.00 | 0.00 | +2.7 | +10.0 |
| `confluence_gte_60` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 0.0% | -15.0 | 0.00 | 0.00 | +1.7 | +7.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 0.0% | -11.6 | 0.00 | 0.00 | +2.6 | +12.4 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -18.7 | 0.00 | 0.00 | +4.8 | +23.1 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 81.8% | 0.0% | 0.0% | 0.0% | -10.7 | 0.00 | 0.00 | +2.7 | +10.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 0.0% | -10.1 | 0.00 | 0.00 | +2.6 | +13.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -13.9 | 0.00 | 0.00 | +2.6 | +9.4 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -13.9 | 0.00 | 0.00 | +2.6 | +9.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -10.3 | 0.00 | 0.00 | +2.6 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
