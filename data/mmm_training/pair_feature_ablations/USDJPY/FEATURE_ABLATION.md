# USDJPY Pair Feature Ablation

Generated: 2026-06-09T15:36:13.428316+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | R_REPEATER | 68.4% | +14.7 | `feature_momentum_breakout_exception` | 5 | R_RUNNER | 80.0% | +22.4 | 999.00 | 999.00 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | R_REPEATER | 60.0% | +11.8 | `all` | 10 | R_REPEATER | 60.0% | +11.8 | 14.35 | 9.57 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 20 | R_REPEATER | 60.0% | +11.3 | `tdi_rsi_gte_50` | 5 | R_RUNNER | 80.0% | +27.7 | 87.41 | 21.85 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | R_REPEATER | 58.3% | +4.9 | `confluence_gte_60` | 6 | R_REPEATER | 66.7% | +8.2 | 31.66 | 15.83 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | R_REPEATER | 55.6% | +5.4 | `ratio_le_2_and_asian_gte_30` | 11 | R_REPEATER | 63.6% | +8.9 | 7.22 | 2.06 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 19 | R_REPEATER | 52.6% | +11.3 | `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_RUNNER | 75.0% | +17.0 | 11.66 | 3.89 | 1 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | R_REPEATER | 50.0% | +19.7 | `feature_momentum_breakout_exception` | 5 | R_REPEATER | 60.0% | +19.4 | 4.35 | 2.90 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | R_REPEATER | 50.0% | +9.7 | `asian_range_gte_30` | 10 | R_REPEATER | 60.0% | +12.6 | 8.66 | 5.77 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 20 | R_REPEATER | 50.0% | +8.2 | `feature_momentum_breakout_exception` | 5 | R_RUNNER | 80.0% | +27.8 | 16.80 | 4.20 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | R_REPEATER | 50.0% | +3.9 | `tdi_rsi_gte_50` | 5 | R_REPEATER | 60.0% | +11.6 | 4.16 | 2.77 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 46.2% | +8.4 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 60.0% | +17.0 | 6.82 | 4.55 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 45.5% | +10.1 | `stop_hunt_le_90` | 8 | R_REPEATER | 62.5% | +16.3 | 7.80 | 4.68 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 43.5% | +3.2 | `tdi_rsi_gt_signal` | 8 | R_REPEATER | 62.5% | +5.7 | 4.40 | 0.88 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 19 | S_STRANGER | 42.1% | +6.0 | `confluence_gte_60` | 8 | R_REPEATER | 62.5% | +11.6 | 6.79 | 4.07 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 41.7% | +8.4 | `confluence_gte_60` | 8 | R_REPEATER | 50.0% | +10.7 | 31.50 | 31.50 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 40.0% | +7.4 | `confluence_gte_60` | 9 | S_STRANGER | 44.4% | +8.3 | 2.50 | 3.13 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 40.0% | +6.7 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 44.4% | +8.5 | 3.68 | 4.60 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 40.0% | +3.7 | `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 50.0% | +8.3 | 2.30 | 2.30 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 40.0% | +2.6 | `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 44.4% | +4.4 | 2.28 | 2.57 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 43 | S_STRANGER | 39.5% | +2.7 | `feature_momentum_breakout_exception` | 6 | R_RUNNER | 83.3% | +11.7 | 44.84 | 8.97 | 1 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 31 | S_STRANGER | 38.7% | +5.7 | `tdi_rsi_gt_signal` | 5 | R_REPEATER | 60.0% | +16.0 | 4.10 | 2.73 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 36.4% | +3.7 | `feature_momentum_breakout_exception` | 5 | R_REPEATER | 60.0% | +4.2 | 5.14 | 1.71 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 25 | S_STRANGER | 36.0% | +4.1 | `tdi_rsi_gte_50` | 13 | R_REPEATER | 53.8% | +9.7 | 3.58 | 2.56 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 14 | S_STRANGER | 35.7% | +7.9 | `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 45.5% | +11.3 | 4.82 | 4.82 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 14 | S_STRANGER | 35.7% | +5.8 | `feature_momentum_breakout_exception` | 9 | S_STRANGER | 44.4% | +8.8 | 7.46 | 7.46 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 31 | S_STRANGER | 35.5% | +2.1 | `tdi_rsi_gte_50` | 17 | R_REPEATER | 52.9% | +8.1 | 5.81 | 3.87 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 35.0% | +4.8 | `stop_hunt_le_90` | 19 | S_STRANGER | 36.8% | +6.1 | 2.45 | 4.20 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 35.0% | +1.7 | `ratio_le_2_asian_gte_30_tdi_positive` | 7 | R_REPEATER | 57.1% | +4.5 | 1.47 | 1.10 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 34 | S_STRANGER | 32.4% | +2.8 | `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 40.0% | +2.9 | 1.99 | 2.32 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | +8.3 | `confluence_gte_60` | 8 | S_STRANGER | 37.5% | +9.8 | 4.53 | 4.53 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 30.0% | +6.8 | `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 31.6% | +7.3 | 3.10 | 6.71 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | +2.5 | `all` | 10 | S_STRANGER | 30.0% | +2.5 | 3.91 | 6.51 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 30.0% | +1.6 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 42.9% | +4.1 | 2.66 | 3.54 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 30 | S_STRANGER | 30.0% | -1.1 | `tdi_rsi_gte_50` | 24 | S_STRANGER | 33.3% | +0.5 | 1.07 | 2.01 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 29.4% | +3.7 | `asian_range_gte_30` | 11 | S_STRANGER | 36.4% | +6.6 | 2.47 | 4.31 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | S_STRANGER | 29.4% | +2.1 | `asian_range_gte_30` | 16 | S_STRANGER | 31.2% | +2.4 | 1.44 | 2.89 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 21 | S_STRANGER | 28.6% | +1.1 | `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 42.9% | +5.6 | 1.81 | 2.41 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 28 | S_STRANGER | 28.6% | -1.4 | `tdi_rsi_gte_50` | 13 | S_STRANGER | 46.2% | +3.7 | 2.04 | 1.70 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | +0.1 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 33.3% | +1.0 | 1.20 | 1.50 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 27.3% | -2.0 | `confluence_gte_60` | 8 | S_STRANGER | 37.5% | +1.5 | 1.47 | 2.45 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 26.7% | +3.4 | `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 33.3% | +9.6 | 5.64 | 11.28 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 15 | S_STRANGER | 26.7% | +2.5 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 40.0% | +2.3 | 1.25 | 1.88 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 26.3% | +0.6 | `tdi_rsi_gt_signal` | 16 | S_STRANGER | 31.2% | +1.4 | 1.30 | 2.33 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 25.0% | +2.4 | `asian_range_gte_30` | 5 | R_REPEATER | 60.0% | +12.5 | 4.54 | 3.03 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 25.0% | -0.4 | `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 35.7% | +3.8 | 1.90 | 3.42 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | -4.4 | `feature_momentum_breakout_exception` | 8 | S_STRANGER | 37.5% | -3.3 | 0.43 | 0.72 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 17 | S_STRANGER | 23.5% | -1.7 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 40.0% | +0.5 | 1.12 | 1.67 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 23.1% | -1.5 | `all` | 13 | S_STRANGER | 23.1% | -1.5 | 0.75 | 2.26 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 23.1% | -5.3 | `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 25.0% | -2.9 | 0.53 | 1.06 | 0 | 1 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 21.4% | -1.8 | `all` | 14 | S_STRANGER | 21.4% | -1.8 | 0.68 | 2.26 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | -3.8 | `confluence_gte_60` | 6 | R_REPEATER | 50.0% | +6.7 | 2.89 | 2.89 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | -7.0 | `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 40.0% | +4.5 | 1.80 | 2.70 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 20 | S_STRANGER | 20.0% | -0.7 | `tdi_rsi_gt_signal` | 15 | S_STRANGER | 26.7% | +1.4 | 1.40 | 2.81 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 20.0% | -0.9 | `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 25.0% | -0.0 | 0.99 | 2.65 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 15 | S_STRANGER | 20.0% | -6.0 | `confluence_gte_60` | 14 | S_STRANGER | 21.4% | -6.4 | 0.40 | 0.56 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 18.8% | -3.4 | `asian_range_gte_30` | 11 | S_STRANGER | 27.3% | -2.2 | 0.72 | 1.92 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 18.8% | -7.7 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 40.0% | +2.8 | 1.63 | 2.45 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 18.2% | +0.9 | `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 40.0% | +7.1 | 4.66 | 6.99 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -2.7 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 28.6% | -1.2 | 0.51 | 1.27 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 21 | S_STRANGER | 14.3% | -0.6 | `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 20.0% | +3.5 | 2.66 | 6.66 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 13.0% | -3.9 | `stop_hunt_le_90` | 20 | S_STRANGER | 15.0% | -2.0 | 0.57 | 2.86 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 10.0% | -1.1 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 20.0% | +1.1 | 1.30 | 3.89 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 10.0% | -4.4 | `asian_range_gte_30` | 6 | S_STRANGER | 16.7% | -2.3 | 0.31 | 0.62 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -4.8 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 14.3% | -4.8 | 0.37 | 1.86 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -5.1 | `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 14.3% | -3.8 | 0.45 | 2.73 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 8.3% | -5.5 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 16.7% | -1.7 | 0.76 | 3.81 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 7.1% | -2.1 | `asian_range_gte_30` | 13 | S_STRANGER | 7.7% | -2.2 | 0.36 | 2.90 | 0 | 1 | fail |

## Candidate Details

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=75.0% Avg=+23.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=100.0% Avg=+18.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | R_REPEATER | 100.0% | 68.4% | 73.7% | 36.8% | +14.7 | 11.24 | 4.01 | +24.0 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 19 | R_REPEATER | 100.0% | 68.4% | 73.7% | 36.8% | +14.7 | 11.24 | 4.01 | +24.0 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 19 | R_REPEATER | 100.0% | 68.4% | 73.7% | 36.8% | +14.7 | 11.24 | 4.01 | +24.0 | +5.0 |
| `stop_hunt_le_90` | 19 | R_REPEATER | 100.0% | 68.4% | 73.7% | 36.8% | +14.7 | 11.24 | 4.01 | +24.0 | +5.0 |
| `asian_range_gte_30` | 12 | R_REPEATER | 63.2% | 66.7% | 75.0% | 58.3% | +18.6 | 11.31 | 3.77 | +29.8 | +6.0 |
| `confluence_gte_60` | 19 | R_REPEATER | 100.0% | 68.4% | 73.7% | 36.8% | +14.7 | 11.24 | 4.01 | +24.0 | +5.0 |
| `confluence_gte_70` | 19 | R_REPEATER | 100.0% | 68.4% | 73.7% | 36.8% | +14.7 | 11.24 | 4.01 | +24.0 | +5.0 |
| `tdi_rsi_gt_signal` | 13 | R_REPEATER | 68.4% | 69.2% | 69.2% | 46.2% | +16.5 | 10.77 | 4.79 | +27.7 | +4.5 |
| `tdi_rsi_gte_50` | 15 | R_REPEATER | 78.9% | 66.7% | 66.7% | 26.7% | +12.9 | 8.09 | 4.04 | +23.9 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | R_REPEATER | 63.2% | 66.7% | 75.0% | 58.3% | +18.6 | 11.31 | 3.77 | +29.8 | +6.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | R_REPEATER | 47.4% | 66.7% | 66.7% | 66.7% | +18.9 | 8.83 | 4.42 | +32.7 | +5.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | R_REPEATER | 100.0% | 68.4% | 73.7% | 36.8% | +14.7 | 11.24 | 4.01 | +24.0 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 18 | R_REPEATER | 94.7% | 66.7% | 72.2% | 38.9% | +15.1 | 10.97 | 4.22 | +24.6 | +4.9 |
| `feature_momentum_breakout_exception` | 5 | R_RUNNER | 26.3% | 80.0% | 100.0% | 60.0% | +22.4 | 999.00 | 999.00 | +30.8 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 31.6% | 66.7% | 66.7% | 33.3% | +12.0 | 7.74 | 3.87 | +25.8 | +5.1 |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=75.0% Avg=+17.5; validation N=4 Fav=75.0% Avg=+12.7; out_of_sample N=2 Fav=0.0% Avg=-1.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 60.0% | 60.0% | 10.0% | +11.8 | 14.35 | 9.57 | +28.0 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 8 | R_REPEATER | 80.0% | 50.0% | 50.0% | 12.5% | +11.7 | 11.63 | 11.63 | +29.3 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 60.0% | 60.0% | 10.0% | +11.8 | 14.35 | 9.57 | +28.0 | +4.9 |
| `stop_hunt_le_90` | 10 | R_REPEATER | 100.0% | 60.0% | 60.0% | 10.0% | +11.8 | 14.35 | 9.57 | +28.0 | +4.9 |
| `asian_range_gte_30` | 10 | R_REPEATER | 100.0% | 60.0% | 60.0% | 10.0% | +11.8 | 14.35 | 9.57 | +28.0 | +4.9 |
| `confluence_gte_60` | 4 | R_RUNNER | 40.0% | 75.0% | 75.0% | 0.0% | +15.4 | 20.90 | 6.97 | +32.1 | +4.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | +12.3 | 10.20 | 20.40 | +26.2 | +2.7 |
| `tdi_rsi_gte_50` | 10 | R_REPEATER | 100.0% | 60.0% | 60.0% | 10.0% | +11.8 | 14.35 | 9.57 | +28.0 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 8 | R_REPEATER | 80.0% | 50.0% | 50.0% | 12.5% | +11.7 | 11.63 | 11.63 | +29.3 | +4.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | +12.3 | 10.20 | 20.40 | +26.2 | +2.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | R_REPEATER | 90.0% | 55.6% | 55.6% | 11.1% | +11.9 | 13.13 | 10.50 | +28.6 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 7 | R_REPEATER | 70.0% | 57.1% | 57.1% | 14.3% | +13.5 | 14.94 | 11.21 | +30.9 | +4.2 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +13.5 | 14.50 | 14.50 | +27.6 | +3.3 |
| `feature_eurjpy_tdi50_reclaim` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 20.0% | +9.7 | 10.53 | 7.02 | +27.2 | +5.3 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+4.3; validation N=2 Fav=100.0% Avg=+62.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | R_REPEATER | 100.0% | 60.0% | 60.0% | 70.0% | +11.3 | 3.91 | 1.63 | +23.8 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 15 | R_REPEATER | 75.0% | 60.0% | 60.0% | 73.3% | +12.7 | 3.97 | 1.32 | +25.0 | +4.2 |
| `hunt_to_ar_ratio_le_2_5` | 19 | R_REPEATER | 95.0% | 63.2% | 63.2% | 73.7% | +12.5 | 4.54 | 1.51 | +25.0 | +4.2 |
| `stop_hunt_le_90` | 20 | R_REPEATER | 100.0% | 60.0% | 60.0% | 70.0% | +11.3 | 3.91 | 1.63 | +23.8 | +4.6 |
| `asian_range_gte_30` | 14 | R_REPEATER | 70.0% | 57.1% | 57.1% | 71.4% | +10.5 | 3.56 | 1.33 | +25.2 | +4.9 |
| `confluence_gte_60` | 9 | R_REPEATER | 45.0% | 66.7% | 66.7% | 66.7% | +14.0 | 2.89 | 1.44 | +25.7 | +3.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 16 | R_REPEATER | 80.0% | 68.8% | 68.8% | 75.0% | +14.4 | 4.58 | 1.25 | +27.0 | +4.3 |
| `tdi_rsi_gte_50` | 5 | R_RUNNER | 25.0% | 80.0% | 80.0% | 60.0% | +27.7 | 87.41 | 21.85 | +37.7 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 50.0% | 50.0% | 50.0% | 70.0% | +10.0 | 2.84 | 1.13 | +25.3 | +5.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 40.0% | 50.0% | 50.0% | 62.5% | +11.4 | 2.66 | 1.33 | +26.9 | +5.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | R_REPEATER | 95.0% | 57.9% | 57.9% | 68.4% | +11.1 | 3.71 | 1.69 | +23.1 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 20 | R_REPEATER | 100.0% | 60.0% | 60.0% | 70.0% | +11.3 | 3.91 | 1.63 | +23.8 | +4.6 |
| `feature_momentum_breakout_exception` | 8 | R_RUNNER | 40.0% | 75.0% | 75.0% | 87.5% | +14.6 | 999.00 | 999.00 | +26.9 | +4.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_RUNNER | 15.0% | 100.0% | 100.0% | 66.7% | +17.3 | 999.00 | 999.00 | +28.1 | +5.4 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=66.7% Avg=+8.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 41.7% | +4.9 | 3.94 | 2.81 | +11.0 | +3.1 |
| `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 41.7% | +4.9 | 3.94 | 2.81 | +11.0 | +3.1 |
| `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 41.7% | +4.9 | 3.94 | 2.81 | +11.0 | +3.1 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 41.7% | +4.9 | 3.94 | 2.81 | +11.0 | +3.1 |
| `asian_range_gte_30` | 9 | R_REPEATER | 75.0% | 55.6% | 55.6% | 55.6% | +5.3 | 3.68 | 2.95 | +11.8 | +2.1 |
| `confluence_gte_60` | 6 | R_REPEATER | 50.0% | 66.7% | 66.7% | 50.0% | +8.2 | 31.66 | 15.83 | +12.7 | +3.3 |
| `confluence_gte_70` | 6 | R_REPEATER | 50.0% | 66.7% | 66.7% | 50.0% | +8.2 | 31.66 | 15.83 | +12.7 | +3.3 |
| `tdi_rsi_gt_signal` | 9 | R_REPEATER | 75.0% | 66.7% | 66.7% | 44.4% | +6.7 | 16.42 | 8.21 | +12.3 | +3.3 |
| `tdi_rsi_gte_50` | 4 | R_REPEATER | 33.3% | 50.0% | 50.0% | 25.0% | +2.7 | 4.79 | 4.79 | +9.8 | +2.9 |
| `ratio_le_2_and_asian_gte_30` | 9 | R_REPEATER | 75.0% | 55.6% | 55.6% | 55.6% | +5.3 | 3.68 | 2.95 | +11.8 | +2.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 50.0% | 66.7% | 66.7% | 66.7% | +8.1 | 31.53 | 15.77 | +14.2 | +1.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 41.7% | +4.9 | 3.94 | 2.81 | +11.0 | +3.1 |
| `feature_stale_hod_exhaustion_reject` | 12 | R_REPEATER | 100.0% | 58.3% | 58.3% | 41.7% | +4.9 | 3.94 | 2.81 | +11.0 | +3.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +1.9 | +5.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -2.3 | 0.00 | 0.00 | +2.3 | +10.0 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=100.0% Avg=+14.1; validation N=3 Fav=33.3% Avg=-4.0; out_of_sample N=4 Fav=50.0% Avg=+13.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | R_REPEATER | 100.0% | 55.6% | 55.6% | 50.0% | +5.4 | 2.96 | 1.48 | +18.2 | +8.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | R_REPEATER | 72.2% | 61.5% | 61.5% | 61.5% | +6.8 | 3.16 | 1.18 | +18.7 | +7.9 |
| `hunt_to_ar_ratio_le_2_5` | 17 | R_REPEATER | 94.4% | 52.9% | 52.9% | 52.9% | +4.9 | 2.66 | 1.48 | +18.1 | +8.4 |
| `stop_hunt_le_90` | 18 | R_REPEATER | 100.0% | 55.6% | 55.6% | 50.0% | +5.4 | 2.96 | 1.48 | +18.2 | +8.1 |
| `asian_range_gte_30` | 14 | R_REPEATER | 77.8% | 57.1% | 57.1% | 50.0% | +6.6 | 4.77 | 2.39 | +19.7 | +7.8 |
| `confluence_gte_60` | 18 | R_REPEATER | 100.0% | 55.6% | 55.6% | 50.0% | +5.4 | 2.96 | 1.48 | +18.2 | +8.1 |
| `confluence_gte_70` | 18 | R_REPEATER | 100.0% | 55.6% | 55.6% | 50.0% | +5.4 | 2.96 | 1.48 | +18.2 | +8.1 |
| `tdi_rsi_gt_signal` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 66.7% | 50.0% | 50.0% | 41.7% | +2.3 | 1.58 | 1.06 | +15.2 | +9.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | R_REPEATER | 61.1% | 63.6% | 63.6% | 63.6% | +8.9 | 7.22 | 2.06 | +20.0 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | R_REPEATER | 100.0% | 55.6% | 55.6% | 50.0% | +5.4 | 2.96 | 1.48 | +18.2 | +8.1 |
| `feature_stale_hod_exhaustion_reject` | 18 | R_REPEATER | 100.0% | 55.6% | 55.6% | 50.0% | +5.4 | 2.96 | 1.48 | +18.2 | +8.1 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 5.6% | 100.0% | 100.0% | 100.0% | +14.1 | 999.00 | 999.00 | +22.1 | +0.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 5.6% | 100.0% | 100.0% | 100.0% | +14.1 | 999.00 | 999.00 | +22.1 | +0.0 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+9.0; validation N=1 Fav=100.0% Avg=+32.7; out_of_sample N=3 Fav=100.0% Avg=+22.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | R_REPEATER | 100.0% | 52.6% | 63.2% | 57.9% | +11.3 | 4.58 | 1.91 | +23.1 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 16 | R_REPEATER | 84.2% | 56.2% | 68.8% | 50.0% | +11.5 | 4.08 | 1.86 | +23.6 | +7.8 |
| `hunt_to_ar_ratio_le_2_5` | 19 | R_REPEATER | 100.0% | 52.6% | 63.2% | 57.9% | +11.3 | 4.58 | 1.91 | +23.1 | +7.3 |
| `stop_hunt_le_90` | 19 | R_REPEATER | 100.0% | 52.6% | 63.2% | 57.9% | +11.3 | 4.58 | 1.91 | +23.1 | +7.3 |
| `asian_range_gte_30` | 18 | R_REPEATER | 94.7% | 55.6% | 61.1% | 61.1% | +11.8 | 4.57 | 2.08 | +24.0 | +7.7 |
| `confluence_gte_60` | 8 | S_STRANGER | 42.1% | 37.5% | 50.0% | 50.0% | +8.3 | 2.67 | 2.00 | +27.4 | +9.2 |
| `confluence_gte_70` | 3 | S_STRANGER | 15.8% | 33.3% | 66.7% | 66.7% | +14.4 | 10.80 | 5.40 | +19.9 | +3.5 |
| `tdi_rsi_gt_signal` | 10 | R_REPEATER | 52.6% | 70.0% | 70.0% | 60.0% | +16.6 | 13.98 | 4.00 | +28.9 | +5.6 |
| `tdi_rsi_gte_50` | 11 | R_REPEATER | 57.9% | 72.7% | 81.8% | 72.7% | +20.8 | 53.00 | 5.89 | +31.4 | +4.2 |
| `ratio_le_2_and_asian_gte_30` | 15 | R_REPEATER | 78.9% | 60.0% | 66.7% | 53.3% | +12.2 | 4.07 | 2.04 | +24.8 | +8.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_RUNNER | 42.1% | 75.0% | 75.0% | 50.0% | +17.0 | 11.66 | 3.89 | +29.4 | +5.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | R_REPEATER | 100.0% | 52.6% | 63.2% | 57.9% | +11.3 | 4.58 | 1.91 | +23.1 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 19 | R_REPEATER | 100.0% | 52.6% | 63.2% | 57.9% | +11.3 | 4.58 | 1.91 | +23.1 | +7.3 |
| `feature_momentum_breakout_exception` | 4 | R_RUNNER | 21.1% | 100.0% | 100.0% | 100.0% | +22.9 | 999.00 | 999.00 | +26.5 | +0.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_RUNNER | 10.5% | 100.0% | 100.0% | 100.0% | +25.8 | 999.00 | 999.00 | +27.0 | +0.5 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+25.0; validation N=1 Fav=100.0% Avg=+25.4; out_of_sample N=1 Fav=0.0% Avg=-3.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 41.7% | +19.7 | 5.50 | 5.50 | +29.6 | +9.2 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 75.0% | 33.3% | 33.3% | 22.2% | +10.3 | 2.77 | 5.54 | +21.3 | +10.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 41.7% | +19.7 | 5.50 | 5.50 | +29.6 | +9.2 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 41.7% | +19.7 | 5.50 | 5.50 | +29.6 | +9.2 |
| `asian_range_gte_30` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 44.4% | +19.9 | 4.76 | 5.95 | +32.1 | +11.0 |
| `confluence_gte_60` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 44.4% | +19.9 | 4.76 | 5.95 | +32.1 | +11.0 |
| `confluence_gte_70` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +83.4 | 999.00 | 999.00 | +101.9 | +0.4 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | +18.3 | 6.63 | 6.63 | +27.8 | +16.3 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 41.7% | +19.7 | 5.50 | 5.50 | +29.6 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 16.7% | +5.9 | 1.75 | 8.74 | +21.0 | +13.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -6.5 | 0.00 | 0.00 | +4.5 | +18.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 83.3% | 40.0% | 40.0% | 30.0% | +13.6 | 3.59 | 5.39 | +24.3 | +10.6 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 45.5% | +19.2 | 5.02 | 6.02 | +30.0 | +9.7 |
| `feature_momentum_breakout_exception` | 5 | R_REPEATER | 41.7% | 60.0% | 60.0% | 40.0% | +19.4 | 4.35 | 2.90 | +28.7 | +9.8 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 28.6% | +11.7 | 2.85 | 3.80 | +22.4 | +11.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=62.5% Avg=+11.6; validation N=2 Fav=50.0% Avg=+16.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +9.7 | 5.50 | 5.50 | +19.8 | +8.4 |
| `hunt_to_ar_ratio_le_2_0` | 11 | R_REPEATER | 91.7% | 54.5% | 54.5% | 9.1% | +11.3 | 7.97 | 6.65 | +20.6 | +7.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +9.7 | 5.50 | 5.50 | +19.8 | +8.4 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +9.7 | 5.50 | 5.50 | +19.8 | +8.4 |
| `asian_range_gte_30` | 10 | R_REPEATER | 83.3% | 60.0% | 60.0% | 10.0% | +12.6 | 8.66 | 5.77 | +22.3 | +8.3 |
| `confluence_gte_60` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +9.7 | 5.50 | 5.50 | +19.8 | +8.4 |
| `confluence_gte_70` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +9.7 | 5.50 | 5.50 | +19.8 | +8.4 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +2.1 | +4.2 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 0.0% | +9.4 | 5.01 | 6.01 | +19.9 | +8.8 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 83.3% | 60.0% | 60.0% | 10.0% | +12.6 | 8.66 | 5.77 | +22.3 | +8.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +0.4 | +6.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +9.7 | 5.50 | 5.50 | +19.8 | +8.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +9.7 | 5.50 | 5.50 | +19.8 | +8.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=80.0% Avg=+27.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.2 | 5.23 | 4.70 | +18.1 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 19 | R_REPEATER | 95.0% | 52.6% | 52.6% | 26.3% | +8.7 | 5.23 | 4.70 | +18.3 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.2 | 5.23 | 4.70 | +18.1 | +6.1 |
| `stop_hunt_le_90` | 19 | R_REPEATER | 95.0% | 52.6% | 52.6% | 26.3% | +8.7 | 5.23 | 4.70 | +18.3 | +6.4 |
| `asian_range_gte_30` | 13 | R_REPEATER | 65.0% | 53.8% | 53.8% | 38.5% | +11.2 | 7.30 | 5.21 | +21.8 | +5.7 |
| `confluence_gte_60` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.2 | 5.23 | 4.70 | +18.1 | +6.1 |
| `confluence_gte_70` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.2 | 5.23 | 4.70 | +18.1 | +6.1 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 70.0% | 42.9% | 42.9% | 21.4% | +7.8 | 4.16 | 4.85 | +19.1 | +6.4 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 80.0% | 43.8% | 43.8% | 18.8% | +6.9 | 3.91 | 4.47 | +17.5 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 12 | R_REPEATER | 60.0% | 58.3% | 58.3% | 33.3% | +12.2 | 7.30 | 5.21 | +22.5 | +6.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 40.0% | 50.0% | 50.0% | 25.0% | +13.2 | 5.79 | 5.79 | +25.6 | +7.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | R_REPEATER | 95.0% | 52.6% | 52.6% | 26.3% | +8.7 | 5.23 | 4.70 | +18.3 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 20 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.2 | 5.23 | 4.70 | +18.1 | +6.1 |
| `feature_momentum_breakout_exception` | 5 | R_RUNNER | 25.0% | 80.0% | 80.0% | 80.0% | +27.8 | 16.80 | 4.20 | +39.3 | +5.8 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 35.0% | 42.9% | 42.9% | 28.6% | +13.8 | 4.66 | 6.21 | +29.0 | +7.3 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+8.5; validation N=1 Fav=0.0% Avg=-13.8; out_of_sample N=1 Fav=100.0% Avg=+46.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 40.0% | +3.9 | 1.79 | 1.79 | +16.1 | +9.0 |
| `hunt_to_ar_ratio_le_2_0` | 9 | R_REPEATER | 90.0% | 55.6% | 55.6% | 44.4% | +5.1 | 2.10 | 1.68 | +17.9 | +9.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 40.0% | +3.9 | 1.79 | 1.79 | +16.1 | +9.0 |
| `stop_hunt_le_90` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 40.0% | +3.9 | 1.79 | 1.79 | +16.1 | +9.0 |
| `asian_range_gte_30` | 8 | R_REPEATER | 80.0% | 50.0% | 50.0% | 50.0% | +6.3 | 2.56 | 2.56 | +17.6 | +8.8 |
| `confluence_gte_60` | 4 | R_RUNNER | 40.0% | 75.0% | 75.0% | 75.0% | +15.7 | 5.54 | 1.85 | +24.6 | +6.5 |
| `confluence_gte_70` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -13.8 | 0.00 | 0.00 | +2.5 | +15.4 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 40.0% | 40.0% | 20.0% | +4.7 | 1.84 | 2.76 | +15.4 | +9.0 |
| `tdi_rsi_gte_50` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 80.0% | +11.6 | 4.16 | 2.77 | +23.2 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 7 | R_REPEATER | 70.0% | 57.1% | 57.1% | 57.1% | +8.3 | 3.31 | 2.48 | +20.0 | +8.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +8.7 | 2.27 | 4.54 | +20.7 | +11.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | R_REPEATER | 90.0% | 55.6% | 55.6% | 44.4% | +5.1 | 2.10 | 1.68 | +17.9 | +9.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 40.0% | +3.9 | 1.79 | 1.79 | +16.1 | +9.0 |
| `feature_momentum_breakout_exception` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 66.7% | +7.5 | 4.05 | 2.03 | +13.7 | +3.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_RUNNER | 20.0% | 100.0% | 100.0% | 100.0% | +15.0 | 999.00 | 999.00 | +20.4 | +1.4 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=+10.0; validation N=2 Fav=100.0% Avg=+27.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 38.5% | +8.4 | 3.49 | 3.49 | +18.5 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 41.7% | 41.7% | 41.7% | +8.1 | 3.22 | 3.87 | +18.7 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 92.3% | 41.7% | 41.7% | 41.7% | +8.1 | 3.22 | 3.87 | +18.7 | +6.6 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 38.5% | +8.4 | 3.49 | 3.49 | +18.5 | +6.3 |
| `asian_range_gte_30` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 45.5% | +9.7 | 4.07 | 4.07 | +19.4 | +6.3 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 38.5% | +8.4 | 3.49 | 3.49 | +18.5 | +6.3 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 38.5% | +8.4 | 3.49 | 3.49 | +18.5 | +6.3 |
| `tdi_rsi_gt_signal` | 7 | R_REPEATER | 53.8% | 57.1% | 57.1% | 28.6% | +12.5 | 4.69 | 3.52 | +23.4 | +6.8 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 92.3% | 50.0% | 50.0% | 41.7% | +9.7 | 4.17 | 3.48 | +18.9 | +6.1 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 45.5% | +9.7 | 4.07 | 4.07 | +19.4 | +6.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 38.5% | 60.0% | 60.0% | 40.0% | +17.0 | 6.82 | 4.55 | +27.5 | +7.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 38.5% | +8.4 | 3.49 | 3.49 | +18.5 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 38.5% | +8.4 | 3.49 | 3.49 | +18.5 | +6.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=57.1% Avg=+12.2; validation N=1 Fav=100.0% Avg=+45.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 27.3% | +10.1 | 3.90 | 4.68 | +20.7 | +9.3 |
| `hunt_to_ar_ratio_le_2_0` | 5 | R_REPEATER | 45.5% | 60.0% | 60.0% | 20.0% | +13.4 | 5.91 | 3.94 | +21.8 | +10.7 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 12.5% | +6.4 | 2.77 | 4.62 | +15.8 | +11.2 |
| `stop_hunt_le_90` | 8 | R_REPEATER | 72.7% | 62.5% | 62.5% | 37.5% | +16.3 | 7.80 | 4.68 | +26.2 | +8.8 |
| `asian_range_gte_30` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 11.1% | +4.7 | 2.09 | 4.19 | +14.2 | +11.2 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 27.3% | +10.1 | 3.90 | 4.68 | +20.7 | +9.3 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 27.3% | +10.1 | 3.90 | 4.68 | +20.7 | +9.3 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | +12.7 | 6.28 | 12.56 | +20.3 | +8.6 |
| `tdi_rsi_gte_50` | 10 | R_REPEATER | 90.9% | 50.0% | 50.0% | 30.0% | +11.9 | 4.96 | 4.96 | +21.8 | +8.8 |
| `ratio_le_2_and_asian_gte_30` | 5 | R_REPEATER | 45.5% | 60.0% | 60.0% | 20.0% | +13.4 | 5.91 | 3.94 | +21.8 | +10.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 100.0% | +45.2 | 999.00 | 999.00 | +53.9 | +3.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | R_REPEATER | 63.6% | 57.1% | 57.1% | 28.6% | +13.2 | 5.81 | 4.36 | +22.7 | +9.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 90.9% | 40.0% | 40.0% | 20.0% | +7.3 | 2.91 | 4.36 | +17.6 | +10.0 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 25.0% | +4.7 | 1.96 | 5.89 | +16.9 | +7.8 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | +9.0 | 3.40 | 6.80 | +19.3 | +5.6 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=57.1% Avg=+3.4; validation N=1 Fav=100.0% Avg=+21.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 43.5% | 43.5% | 43.5% | +3.2 | 1.97 | 1.58 | +18.3 | +8.4 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 91.3% | 47.6% | 47.6% | 47.6% | +4.2 | 2.39 | 1.43 | +19.9 | +8.1 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 95.7% | 45.5% | 45.5% | 45.5% | +3.7 | 2.21 | 1.55 | +19.1 | +8.2 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 95.7% | 45.5% | 45.5% | 45.5% | +3.7 | 2.21 | 1.55 | +19.1 | +8.2 |
| `asian_range_gte_30` | 17 | S_STRANGER | 73.9% | 47.1% | 47.1% | 47.1% | +3.8 | 2.31 | 1.45 | +18.3 | +8.3 |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 43.5% | 43.5% | 43.5% | +3.2 | 1.97 | 1.58 | +18.3 | +8.4 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 43.5% | 43.5% | 43.5% | +3.2 | 1.97 | 1.58 | +18.3 | +8.4 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 34.8% | 62.5% | 62.5% | 62.5% | +5.7 | 4.40 | 0.88 | +22.7 | +7.5 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 73.9% | 47.1% | 47.1% | 52.9% | +4.8 | 2.41 | 1.51 | +20.3 | +8.3 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 73.9% | 47.1% | 47.1% | 47.1% | +3.8 | 2.31 | 1.45 | +18.3 | +8.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 21.7% | 60.0% | 60.0% | 80.0% | +4.6 | 999.00 | 999.00 | +23.0 | +6.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 95.7% | 45.5% | 45.5% | 45.5% | +3.7 | 2.21 | 1.55 | +19.1 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 43.5% | 43.5% | 43.5% | +3.2 | 1.97 | 1.58 | +18.3 | +8.4 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 8.7% | 50.0% | 50.0% | 100.0% | +5.0 | 999.00 | 999.00 | +12.8 | +7.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 4.3% | 100.0% | 100.0% | 100.0% | +10.1 | 999.00 | 999.00 | +12.6 | +8.5 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+16.5; validation N=6 Fav=50.0% Avg=+7.0; out_of_sample N=1 Fav=100.0% Avg=+34.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 31.6% | +6.0 | 2.40 | 3.00 | +18.9 | +8.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 73.7% | 35.7% | 35.7% | 35.7% | +5.9 | 2.61 | 4.18 | +17.7 | +8.3 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 94.7% | 38.9% | 38.9% | 33.3% | +5.7 | 2.27 | 3.25 | +18.2 | +8.5 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 31.6% | +6.0 | 2.40 | 3.00 | +18.9 | +8.7 |
| `asian_range_gte_30` | 17 | S_STRANGER | 89.5% | 47.1% | 47.1% | 35.3% | +7.8 | 3.18 | 3.18 | +20.5 | +7.7 |
| `confluence_gte_60` | 8 | R_REPEATER | 42.1% | 62.5% | 62.5% | 37.5% | +11.6 | 6.79 | 4.07 | +22.3 | +6.8 |
| `confluence_gte_70` | 2 | R_RUNNER | 10.5% | 100.0% | 100.0% | 0.0% | +12.7 | 999.00 | 999.00 | +24.3 | +1.8 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 89.5% | 41.2% | 41.2% | 29.4% | +6.6 | 2.73 | 3.52 | +19.5 | +8.6 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 63.2% | 50.0% | 50.0% | 33.3% | +7.5 | 2.67 | 2.67 | +20.8 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 68.4% | 38.5% | 38.5% | 38.5% | +6.8 | 2.97 | 4.16 | +18.8 | +7.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 57.9% | 36.4% | 36.4% | 36.4% | +8.0 | 4.02 | 6.03 | +19.7 | +7.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 89.5% | 41.2% | 41.2% | 35.3% | +7.0 | 2.83 | 3.64 | +18.8 | +8.0 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 94.7% | 44.4% | 44.4% | 33.3% | +7.2 | 3.00 | 3.37 | +19.5 | +8.2 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 36.8% | 28.6% | 28.6% | 28.6% | +1.0 | 1.18 | 2.36 | +16.9 | +10.1 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 15.8% | 33.3% | 33.3% | 33.3% | +5.3 | 1.89 | 3.78 | +18.9 | +10.3 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+9.9; validation N=2 Fav=100.0% Avg=+13.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 33.3% | +8.4 | 5.59 | 7.82 | +17.4 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 75.0% | 33.3% | 33.3% | 22.2% | +8.4 | 4.63 | 9.27 | +19.0 | +6.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 36.4% | +9.2 | 5.88 | 7.06 | +18.1 | +5.5 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 36.4% | +9.2 | 5.88 | 7.06 | +18.1 | +5.5 |
| `asian_range_gte_30` | 10 | S_STRANGER | 83.3% | 40.0% | 40.0% | 40.0% | +6.7 | 4.24 | 6.36 | +16.0 | +5.6 |
| `confluence_gte_60` | 8 | R_REPEATER | 66.7% | 50.0% | 50.0% | 50.0% | +10.7 | 31.50 | 31.50 | +18.6 | +3.7 |
| `confluence_gte_70` | 2 | R_RUNNER | 16.7% | 100.0% | 100.0% | 100.0% | +31.1 | 999.00 | 999.00 | +34.3 | +5.4 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 25.0% | 25.0% | 25.0% | +5.2 | 2.99 | 8.97 | +16.5 | +6.4 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 25.0% | +9.6 | 4.84 | 8.07 | +19.8 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 66.7% | 25.0% | 25.0% | 25.0% | +5.2 | 2.99 | 8.97 | +16.5 | +6.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 66.7% | 25.0% | 25.0% | 25.0% | +5.2 | 2.99 | 8.97 | +16.5 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 83.3% | 40.0% | 40.0% | 30.0% | +8.8 | 5.25 | 7.87 | +18.4 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 91.7% | 36.4% | 36.4% | 36.4% | +6.0 | 4.03 | 7.05 | +15.5 | +5.3 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 25.0% | +7.0 | 3.74 | 6.23 | +16.6 | +5.8 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 16.7% | +7.3 | 3.26 | 6.53 | +18.1 | +7.0 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=33.3% Avg=+6.3; out_of_sample N=6 Fav=50.0% Avg=+9.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +7.4 | 2.50 | 3.13 | +19.8 | +18.4 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +7.4 | 2.50 | 3.13 | +19.8 | +18.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +7.4 | 2.50 | 3.13 | +19.8 | +18.4 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +7.4 | 2.50 | 3.13 | +19.8 | +18.4 |
| `asian_range_gte_30` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 42.9% | +8.9 | 2.80 | 2.80 | +22.4 | +18.6 |
| `confluence_gte_60` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +8.3 | 2.50 | 3.13 | +19.5 | +13.1 |
| `confluence_gte_70` | 2 | R_RUNNER | 20.0% | 100.0% | 100.0% | 50.0% | +23.1 | 999.00 | 999.00 | +26.8 | +4.1 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | +9.8 | 197.00 | 197.00 | +15.4 | +5.7 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 16.7% | +3.8 | 1.53 | 3.06 | +17.2 | +16.3 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 42.9% | +8.9 | 2.80 | 2.80 | +22.4 | +18.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +19.7 | 999.00 | 999.00 | +25.4 | +4.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +7.4 | 2.50 | 3.13 | +19.8 | +18.4 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +7.4 | 2.50 | 3.13 | +19.8 | +18.4 |
| `feature_momentum_breakout_exception` | 2 | R_RUNNER | 20.0% | 100.0% | 100.0% | 100.0% | +38.8 | 999.00 | 999.00 | +43.8 | +3.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +23.2 | 465.00 | 465.00 | +26.8 | +3.5 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=44.4% Avg=+8.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +6.7 | 2.75 | 4.13 | +16.7 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +6.7 | 2.75 | 4.13 | +16.7 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +6.7 | 2.75 | 4.13 | +16.7 | +6.6 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +6.7 | 2.75 | 4.13 | +16.7 | +6.6 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +6.7 | 2.75 | 4.13 | +16.7 | +6.6 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +6.7 | 2.75 | 4.13 | +16.7 | +6.6 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +6.7 | 2.75 | 4.13 | +16.7 | +6.6 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 28.6% | +9.2 | 3.60 | 4.80 | +19.3 | +6.7 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 22.2% | +8.5 | 3.68 | 4.60 | +18.2 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +6.7 | 2.75 | 4.13 | +16.7 | +6.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 28.6% | +9.2 | 3.60 | 4.80 | +19.3 | +6.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +6.7 | 2.75 | 4.13 | +16.7 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +6.7 | 2.75 | 4.13 | +16.7 | +6.6 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +53.0 | 999.00 | 999.00 | +54.2 | +0.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 33.3% | +21.7 | 17.69 | 8.85 | +25.8 | +3.5 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=75.0% Avg=+17.5; out_of_sample N=2 Fav=0.0% Avg=-10.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +3.7 | 1.57 | 1.96 | +16.0 | +14.2 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 12.5% | +3.3 | 1.42 | 1.90 | +17.6 | +16.2 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 33.3% | 33.3% | 11.1% | +2.6 | 1.36 | 2.26 | +16.1 | +15.1 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 12.5% | +3.3 | 1.42 | 1.90 | +17.6 | +16.2 |
| `asian_range_gte_30` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 11.1% | +6.7 | 2.46 | 2.46 | +17.7 | +11.3 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +3.7 | 1.57 | 1.96 | +16.0 | +14.2 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +3.7 | 1.57 | 1.96 | +16.0 | +14.2 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 0.0% | +3.7 | 1.42 | 1.90 | +17.6 | +17.9 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 0.0% | +4.1 | 1.57 | 1.96 | +15.8 | +15.3 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 14.3% | +7.1 | 2.30 | 2.30 | +20.0 | +12.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 0.0% | +8.3 | 2.30 | 2.30 | +20.4 | +14.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 12.5% | +3.3 | 1.42 | 1.90 | +17.6 | +16.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +3.7 | 1.57 | 1.96 | +16.0 | +14.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=14 Fav=50.0% Avg=+5.7; validation N=2 Fav=50.0% Avg=+7.5; out_of_sample N=2 Fav=0.0% Avg=-7.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 15.0% | +2.6 | 1.59 | 2.19 | +15.2 | +10.9 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 44.4% | 44.4% | 16.7% | +4.4 | 2.28 | 2.57 | +16.4 | +10.5 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 15.0% | +2.6 | 1.59 | 2.19 | +15.2 | +10.9 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 15.0% | +2.6 | 1.59 | 2.19 | +15.2 | +10.9 |
| `asian_range_gte_30` | 17 | S_STRANGER | 85.0% | 29.4% | 29.4% | 5.9% | -0.1 | 0.98 | 2.15 | +13.4 | +12.5 |
| `confluence_gte_60` | 19 | S_STRANGER | 95.0% | 42.1% | 42.1% | 15.8% | +3.2 | 1.77 | 2.21 | +15.7 | +10.8 |
| `confluence_gte_70` | 2 | R_RUNNER | 10.0% | 100.0% | 100.0% | 50.0% | +14.9 | 999.00 | 999.00 | +23.4 | +2.8 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 70.0% | 42.9% | 42.9% | 0.0% | +2.2 | 1.48 | 1.97 | +13.5 | +11.5 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 80.0% | 37.5% | 37.5% | 0.0% | +0.7 | 1.14 | 1.91 | +13.1 | +11.4 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 75.0% | 33.3% | 33.3% | 6.7% | +1.6 | 1.40 | 2.52 | +14.5 | +12.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 60.0% | 41.7% | 41.7% | 0.0% | +3.5 | 1.96 | 2.74 | +13.9 | +11.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 95.0% | 42.1% | 42.1% | 15.8% | +3.8 | 2.05 | 2.57 | +15.9 | +10.4 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 15.0% | +2.6 | 1.59 | 2.19 | +15.2 | +10.9 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 45.0% | 22.2% | 22.2% | 22.2% | -0.9 | 0.84 | 2.51 | +14.0 | +12.9 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 50.0% | 40.0% | 40.0% | 0.0% | +2.1 | 1.40 | 2.11 | +14.3 | +13.1 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=100.0% Avg=+15.2; validation N=2 Fav=50.0% Avg=+6.1; out_of_sample N=1 Fav=100.0% Avg=+12.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 43 | S_STRANGER | 100.0% | 39.5% | 39.5% | 30.2% | +2.7 | 1.50 | 1.95 | +15.2 | +7.6 |
| `hunt_to_ar_ratio_le_2_0` | 32 | S_STRANGER | 74.4% | 34.4% | 34.4% | 25.0% | +2.2 | 1.51 | 2.33 | +13.8 | +7.9 |
| `hunt_to_ar_ratio_le_2_5` | 42 | S_STRANGER | 97.7% | 40.5% | 40.5% | 31.0% | +4.5 | 2.23 | 2.75 | +15.6 | +7.7 |
| `stop_hunt_le_90` | 40 | S_STRANGER | 93.0% | 37.5% | 37.5% | 27.5% | +3.7 | 1.97 | 2.76 | +14.6 | +7.7 |
| `asian_range_gte_30` | 36 | S_STRANGER | 83.7% | 33.3% | 33.3% | 33.3% | +1.5 | 1.24 | 2.06 | +15.1 | +8.3 |
| `confluence_gte_60` | 35 | S_STRANGER | 81.4% | 40.0% | 40.0% | 28.6% | +2.6 | 1.44 | 1.95 | +15.9 | +7.9 |
| `confluence_gte_70` | 15 | S_STRANGER | 34.9% | 20.0% | 20.0% | 26.7% | -2.2 | 0.66 | 2.41 | +11.9 | +10.8 |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 53.5% | 34.8% | 34.8% | 21.7% | +0.1 | 1.02 | 1.65 | +15.5 | +9.3 |
| `tdi_rsi_gte_50` | 29 | S_STRANGER | 67.4% | 41.4% | 41.4% | 20.7% | +4.4 | 2.05 | 2.56 | +16.7 | +8.3 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 58.1% | 24.0% | 24.0% | 28.0% | +0.3 | 1.06 | 2.65 | +13.3 | +9.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 32.6% | 28.6% | 28.6% | 21.4% | +0.1 | 1.01 | 2.03 | +14.9 | +11.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 39 | S_STRANGER | 90.7% | 35.9% | 35.9% | 25.6% | +3.5 | 1.88 | 2.82 | +14.7 | +7.8 |
| `feature_stale_hod_exhaustion_reject` | 43 | S_STRANGER | 100.0% | 39.5% | 39.5% | 30.2% | +2.7 | 1.50 | 1.95 | +15.2 | +7.6 |
| `feature_momentum_breakout_exception` | 6 | R_RUNNER | 14.0% | 83.3% | 83.3% | 33.3% | +11.7 | 44.84 | 8.97 | +18.3 | +2.8 |
| `feature_eurjpy_tdi50_reclaim` | 5 | R_RUNNER | 11.6% | 80.0% | 80.0% | 20.0% | +11.3 | 36.25 | 9.06 | +19.2 | +2.4 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=+4.8; validation N=2 Fav=100.0% Avg=+32.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 38.7% | 38.7% | 25.8% | +5.7 | 2.74 | 3.19 | +16.0 | +8.6 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 74.2% | 39.1% | 39.1% | 21.7% | +3.9 | 1.98 | 2.43 | +14.6 | +9.8 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 87.1% | 37.0% | 37.0% | 22.2% | +3.6 | 2.04 | 2.65 | +14.3 | +9.4 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 96.8% | 40.0% | 40.0% | 26.7% | +5.9 | 2.77 | 3.00 | +16.1 | +8.4 |
| `asian_range_gte_30` | 20 | S_STRANGER | 64.5% | 40.0% | 40.0% | 20.0% | +4.8 | 2.56 | 3.20 | +15.1 | +8.5 |
| `confluence_gte_60` | 31 | S_STRANGER | 100.0% | 38.7% | 38.7% | 25.8% | +5.7 | 2.74 | 3.19 | +16.0 | +8.6 |
| `confluence_gte_70` | 31 | S_STRANGER | 100.0% | 38.7% | 38.7% | 25.8% | +5.7 | 2.74 | 3.19 | +16.0 | +8.6 |
| `tdi_rsi_gt_signal` | 5 | R_REPEATER | 16.1% | 60.0% | 60.0% | 20.0% | +16.0 | 4.10 | 2.73 | +27.7 | +6.8 |
| `tdi_rsi_gte_50` | 25 | S_STRANGER | 80.6% | 40.0% | 40.0% | 16.0% | +6.3 | 2.69 | 3.50 | +16.9 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 58.1% | 44.4% | 44.4% | 22.2% | +5.5 | 2.68 | 2.68 | +15.7 | +8.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 12.9% | 50.0% | 50.0% | 25.0% | +9.9 | 2.54 | 2.54 | +22.4 | +8.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 96.8% | 40.0% | 40.0% | 26.7% | +5.9 | 2.77 | 3.00 | +16.1 | +8.4 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 38.7% | 38.7% | 25.8% | +5.7 | 2.74 | 3.19 | +16.0 | +8.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=100.0% Avg=+11.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=3 Fav=33.3% Avg=-0.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +3.7 | 2.19 | 3.28 | +14.2 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 12.5% | +5.4 | 2.48 | 4.13 | +14.3 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +3.7 | 2.19 | 3.28 | +14.2 | +6.4 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +3.7 | 2.19 | 3.28 | +14.2 | +6.4 |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +3.7 | 2.19 | 3.28 | +14.2 | +6.4 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +3.7 | 2.19 | 3.28 | +14.2 | +6.4 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +3.7 | 2.19 | 3.28 | +14.2 | +6.4 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | +5.7 | 2.35 | 9.39 | +13.9 | +6.4 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +3.7 | 2.19 | 3.28 | +14.2 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 12.5% | +5.4 | 2.48 | 4.13 | +14.3 | +6.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | +5.7 | 2.35 | 9.39 | +13.9 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 12.5% | +5.4 | 2.48 | 4.13 | +14.3 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | +3.7 | 2.19 | 3.28 | +14.2 | +6.4 |
| `feature_momentum_breakout_exception` | 5 | R_REPEATER | 45.5% | 60.0% | 60.0% | 0.0% | +4.2 | 5.14 | 1.71 | +16.3 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 0.0% | +1.5 | 1.70 | 1.70 | +13.2 | +5.9 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=28.6% Avg=+2.1; out_of_sample N=6 Fav=83.3% Avg=+18.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 36.0% | 40.0% | 32.0% | +4.1 | 1.79 | 2.51 | +15.7 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 88.0% | 31.8% | 36.4% | 31.8% | +3.0 | 1.58 | 2.57 | +13.9 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 96.0% | 37.5% | 41.7% | 33.3% | +4.9 | 2.04 | 2.65 | +16.1 | +8.5 |
| `stop_hunt_le_90` | 25 | S_STRANGER | 100.0% | 36.0% | 40.0% | 32.0% | +4.1 | 1.79 | 2.51 | +15.7 | +8.8 |
| `asian_range_gte_30` | 23 | S_STRANGER | 92.0% | 39.1% | 43.5% | 34.8% | +5.4 | 2.15 | 2.58 | +16.7 | +8.5 |
| `confluence_gte_60` | 20 | S_STRANGER | 80.0% | 40.0% | 45.0% | 30.0% | +4.9 | 2.02 | 2.47 | +15.6 | +7.2 |
| `confluence_gte_70` | 3 | S_STRANGER | 12.0% | 33.3% | 66.7% | 0.0% | +1.1 | 1.22 | 0.61 | +13.1 | +1.9 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 84.0% | 42.9% | 42.9% | 38.1% | +6.3 | 2.36 | 2.89 | +18.1 | +9.2 |
| `tdi_rsi_gte_50` | 13 | R_REPEATER | 52.0% | 53.8% | 53.8% | 46.2% | +9.7 | 3.58 | 2.56 | +23.0 | +9.1 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 84.0% | 33.3% | 38.1% | 33.3% | +3.4 | 1.67 | 2.50 | +14.4 | +8.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 68.0% | 41.2% | 41.2% | 41.2% | +6.0 | 2.35 | 3.02 | +17.1 | +9.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 100.0% | 36.0% | 40.0% | 32.0% | +4.1 | 1.79 | 2.51 | +15.7 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 36.0% | 40.0% | 32.0% | +4.1 | 1.79 | 2.51 | +15.7 | +8.8 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 4.0% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +3.5 | +13.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.0% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +3.5 | +13.7 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=40.0% Avg=+2.5; validation N=1 Fav=100.0% Avg=+99.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 42.9% | +7.9 | 3.37 | 4.72 | +17.2 | +8.3 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 85.7% | 41.7% | 41.7% | 41.7% | +10.1 | 4.36 | 5.24 | +18.9 | +7.4 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 85.7% | 41.7% | 41.7% | 41.7% | +10.1 | 4.36 | 5.24 | +18.9 | +7.4 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 85.7% | 41.7% | 41.7% | 41.7% | +10.1 | 4.36 | 5.24 | +18.9 | +7.4 |
| `asian_range_gte_30` | 13 | S_STRANGER | 92.9% | 38.5% | 38.5% | 46.2% | +8.8 | 3.64 | 4.36 | +18.4 | +8.5 |
| `confluence_gte_60` | 13 | S_STRANGER | 92.9% | 30.8% | 30.8% | 38.5% | +7.5 | 3.09 | 5.41 | +17.4 | +8.8 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +18.8 | +10.0 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 28.6% | -4.1 | 0.00 | 0.00 | +7.4 | +10.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 71.4% | 40.0% | 40.0% | 40.0% | +9.8 | 4.39 | 5.49 | +19.5 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 78.6% | 45.5% | 45.5% | 45.5% | +11.3 | 4.82 | 4.82 | +20.4 | +7.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 20.0% | -3.7 | 0.00 | 0.00 | +7.4 | +8.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 85.7% | 41.7% | 41.7% | 41.7% | +10.1 | 4.36 | 5.24 | +18.9 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 42.9% | +7.9 | 3.37 | 4.72 | +17.2 | +8.3 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -0.2 | 0.00 | 0.00 | +13.0 | +4.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -0.2 | 0.00 | 0.00 | +13.0 | +4.3 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.6; validation N=5 Fav=40.0% Avg=+16.2; out_of_sample N=3 Fav=66.7% Avg=+0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 35.7% | +5.8 | 2.98 | 4.18 | +17.9 | +9.4 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 57.1% | 25.0% | 25.0% | 25.0% | +6.7 | 2.44 | 7.32 | +18.9 | +10.1 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 35.7% | +5.8 | 2.98 | 4.18 | +17.9 | +9.4 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 35.7% | +5.8 | 2.98 | 4.18 | +17.9 | +9.4 |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 35.7% | 35.7% | 35.7% | +5.8 | 2.98 | 4.18 | +17.9 | +9.4 |
| `confluence_gte_60` | 6 | S_STRANGER | 42.9% | 33.3% | 33.3% | 33.3% | +0.7 | 3.20 | 3.20 | +11.7 | +7.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 85.7% | 25.0% | 25.0% | 33.3% | +4.5 | 2.32 | 5.41 | +18.2 | +10.8 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 71.4% | 40.0% | 40.0% | 20.0% | +8.4 | 6.89 | 10.34 | +17.9 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 57.1% | 25.0% | 25.0% | 25.0% | +6.7 | 2.44 | 7.32 | +18.9 | +10.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 57.1% | 25.0% | 25.0% | 25.0% | +6.7 | 2.44 | 7.32 | +18.9 | +10.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 33.3% | +6.0 | 2.44 | 7.32 | +18.6 | +10.3 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 92.9% | 30.8% | 30.8% | 38.5% | +6.1 | 2.92 | 5.11 | +18.7 | +10.0 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 64.3% | 44.4% | 44.4% | 33.3% | +8.8 | 7.46 | 7.46 | +18.3 | +8.3 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 57.1% | 37.5% | 37.5% | 12.5% | +6.7 | 5.10 | 8.50 | +17.5 | +8.2 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=14 Fav=64.3% Avg=+11.3; validation N=3 Fav=0.0% Avg=-6.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 35.5% | 35.5% | 35.5% | +2.1 | 1.48 | 2.16 | +13.1 | +10.9 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 74.2% | 34.8% | 34.8% | 34.8% | +2.9 | 1.75 | 2.63 | +12.4 | +10.5 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 87.1% | 29.6% | 29.6% | 33.3% | +0.8 | 1.17 | 2.19 | +12.3 | +11.9 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 35.5% | 35.5% | 35.5% | +2.1 | 1.48 | 2.16 | +13.1 | +10.9 |
| `asian_range_gte_30` | 20 | S_STRANGER | 64.5% | 35.0% | 35.0% | 35.0% | +2.4 | 1.57 | 2.46 | +12.0 | +9.9 |
| `confluence_gte_60` | 31 | S_STRANGER | 100.0% | 35.5% | 35.5% | 35.5% | +2.1 | 1.48 | 2.16 | +13.1 | +10.9 |
| `confluence_gte_70` | 31 | S_STRANGER | 100.0% | 35.5% | 35.5% | 35.5% | +2.1 | 1.48 | 2.16 | +13.1 | +10.9 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 41.9% | 30.8% | 30.8% | 23.1% | +3.8 | 2.75 | 4.82 | +11.9 | +7.1 |
| `tdi_rsi_gte_50` | 17 | R_REPEATER | 54.8% | 52.9% | 52.9% | 41.2% | +8.1 | 5.81 | 3.87 | +16.2 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 54.8% | 41.2% | 41.2% | 41.2% | +5.4 | 3.23 | 3.69 | +12.9 | +7.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 35.5% | 27.3% | 27.3% | 27.3% | +3.2 | 2.50 | 5.00 | +11.5 | +7.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 35.5% | 35.5% | 35.5% | +2.1 | 1.48 | 2.16 | +13.1 | +10.9 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 35.5% | 35.5% | 35.5% | +2.1 | 1.48 | 2.16 | +13.1 | +10.9 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 6.5% | 50.0% | 50.0% | 100.0% | +11.2 | 999.00 | 999.00 | +17.9 | +4.1 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 6.5% | 50.0% | 50.0% | 100.0% | +11.2 | 999.00 | 999.00 | +17.9 | +4.1 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=15 Fav=46.7% Avg=+9.7; validation N=4 Fav=0.0% Avg=-7.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 30.0% | +4.8 | 1.96 | 3.63 | +15.9 | +9.6 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 75.0% | 33.3% | 33.3% | 33.3% | +6.5 | 2.26 | 4.52 | +16.9 | +9.9 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 95.0% | 31.6% | 31.6% | 26.3% | +4.3 | 1.80 | 3.91 | +15.6 | +10.0 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 95.0% | 36.8% | 36.8% | 31.6% | +6.1 | 2.45 | 4.20 | +16.6 | +9.0 |
| `asian_range_gte_30` | 16 | S_STRANGER | 80.0% | 31.2% | 31.2% | 31.2% | +4.8 | 1.79 | 3.94 | +16.0 | +10.6 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 30.0% | +4.8 | 1.96 | 3.63 | +15.9 | +9.6 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 30.0% | +4.8 | 1.96 | 3.63 | +15.9 | +9.6 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 95.0% | 36.8% | 36.8% | 31.6% | +5.7 | 2.23 | 3.81 | +16.6 | +9.4 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 75.0% | 26.7% | 26.7% | 20.0% | +1.2 | 1.24 | 3.41 | +13.3 | +10.5 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 75.0% | 33.3% | 33.3% | 33.3% | +6.5 | 2.26 | 4.52 | +16.9 | +9.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 70.0% | 35.7% | 35.7% | 35.7% | +7.8 | 2.68 | 4.82 | +17.9 | +9.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 95.0% | 36.8% | 36.8% | 31.6% | +6.1 | 2.45 | 4.20 | +16.6 | +9.0 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 30.0% | +4.8 | 1.96 | 3.63 | +15.9 | +9.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-2.1; validation N=4 Fav=75.0% Avg=+10.7; out_of_sample N=2 Fav=50.0% Avg=-4.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +1.7 | 1.28 | 1.82 | +16.2 | +6.9 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 75.0% | 33.3% | 33.3% | 33.3% | +1.5 | 1.28 | 2.05 | +14.7 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +1.7 | 1.28 | 1.82 | +16.2 | +6.9 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 95.0% | 36.8% | 36.8% | 36.8% | +2.1 | 1.34 | 1.72 | +16.9 | +6.7 |
| `asian_range_gte_30` | 17 | S_STRANGER | 85.0% | 41.2% | 41.2% | 35.3% | +2.3 | 1.33 | 1.52 | +17.7 | +7.0 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +1.7 | 1.28 | 1.82 | +16.2 | +6.9 |
| `confluence_gte_70` | 6 | R_REPEATER | 30.0% | 50.0% | 50.0% | 50.0% | +7.1 | 2.05 | 1.37 | +26.0 | +7.1 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 55.0% | 45.5% | 45.5% | 36.4% | -0.7 | 0.93 | 0.93 | +16.2 | +5.8 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 70.0% | 42.9% | 42.9% | 28.6% | +4.5 | 2.56 | 2.99 | +15.9 | +7.5 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 60.0% | 41.7% | 41.7% | 33.3% | +2.3 | 1.36 | 1.64 | +16.4 | +7.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | R_REPEATER | 35.0% | 57.1% | 57.1% | 42.9% | +4.5 | 1.47 | 1.10 | +19.4 | +7.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 95.0% | 36.8% | 36.8% | 36.8% | +2.1 | 1.34 | 1.72 | +16.9 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 35.0% | 35.0% | 35.0% | +1.7 | 1.28 | 1.82 | +16.2 | +6.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=66.7% Avg=+5.2; out_of_sample N=12 Fav=33.3% Avg=+2.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 34 | S_STRANGER | 100.0% | 32.4% | 32.4% | 32.4% | +2.8 | 1.88 | 3.42 | +13.8 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 55.9% | 31.6% | 31.6% | 36.8% | +1.6 | 1.52 | 2.53 | +14.6 | +8.4 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 76.5% | 34.6% | 34.6% | 34.6% | +2.9 | 2.01 | 3.12 | +15.0 | +7.7 |
| `stop_hunt_le_90` | 34 | S_STRANGER | 100.0% | 32.4% | 32.4% | 32.4% | +2.8 | 1.88 | 3.42 | +13.8 | +7.7 |
| `asian_range_gte_30` | 21 | S_STRANGER | 61.8% | 33.3% | 33.3% | 28.6% | +1.1 | 1.28 | 2.19 | +13.3 | +8.8 |
| `confluence_gte_60` | 34 | S_STRANGER | 100.0% | 32.4% | 32.4% | 32.4% | +2.8 | 1.88 | 3.42 | +13.8 | +7.7 |
| `confluence_gte_70` | 34 | S_STRANGER | 100.0% | 32.4% | 32.4% | 32.4% | +2.8 | 1.88 | 3.42 | +13.8 | +7.7 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 50.0% | 17.6% | 17.6% | 17.6% | -0.7 | 0.86 | 3.44 | +11.6 | +10.0 |
| `tdi_rsi_gte_50` | 22 | S_STRANGER | 64.7% | 18.2% | 18.2% | 18.2% | -0.8 | 0.80 | 3.19 | +13.4 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 44.1% | 40.0% | 40.0% | 40.0% | +2.9 | 1.99 | 2.32 | +15.0 | +8.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 20.6% | 14.3% | 14.3% | 0.0% | -4.7 | 0.20 | 0.98 | +10.9 | +11.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 33 | S_STRANGER | 97.1% | 33.3% | 33.3% | 33.3% | +2.9 | 1.89 | 3.27 | +14.1 | +7.8 |
| `feature_stale_hod_exhaustion_reject` | 34 | S_STRANGER | 100.0% | 32.4% | 32.4% | 32.4% | +2.8 | 1.88 | 3.42 | +13.8 | +7.7 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 2.9% | 0.0% | 0.0% | 0.0% | -0.6 | 0.00 | 0.00 | +1.8 | +6.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.9% | 0.0% | 0.0% | 0.0% | -0.6 | 0.00 | 0.00 | +1.8 | +6.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+15.2; validation N=3 Fav=33.3% Avg=+0.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 60.0% | +8.3 | 4.70 | 3.53 | +17.9 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 62.5% | +7.4 | 3.67 | 5.50 | +16.5 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 60.0% | +8.3 | 4.70 | 3.53 | +17.9 | +7.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 60.0% | +8.3 | 4.70 | 3.53 | +17.9 | +7.7 |
| `asian_range_gte_30` | 9 | S_STRANGER | 90.0% | 33.3% | 44.4% | 55.6% | +9.2 | 4.70 | 3.53 | +19.3 | +8.5 |
| `confluence_gte_60` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 62.5% | +9.8 | 4.53 | 4.53 | +20.4 | +8.4 |
| `confluence_gte_70` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +10.8 | +14.8 |
| `tdi_rsi_gt_signal` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 83.3% | +13.8 | 13.33 | 6.66 | +24.8 | +8.1 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 57.1% | +8.5 | 3.67 | 5.50 | +18.1 | +7.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 60.0% | +8.3 | 4.70 | 3.53 | +17.9 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 60.0% | +8.3 | 4.70 | 3.53 | +17.9 | +7.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=13 Fav=38.5% Avg=+9.1; validation N=6 Fav=16.7% Avg=+3.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +6.8 | 2.97 | 6.94 | +16.8 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 22.2% | 22.2% | 22.2% | +4.3 | 2.12 | 7.42 | +14.6 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 95.0% | 26.3% | 26.3% | 26.3% | +5.3 | 2.48 | 6.93 | +15.4 | +6.2 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +6.8 | 2.97 | 6.94 | +16.8 | +5.9 |
| `asian_range_gte_30` | 14 | S_STRANGER | 70.0% | 14.3% | 14.3% | 14.3% | +2.7 | 1.61 | 9.69 | +14.3 | +7.3 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +6.8 | 2.97 | 6.94 | +16.8 | +5.9 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +6.8 | 2.97 | 6.94 | +16.8 | +5.9 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 90.0% | 27.8% | 27.8% | 27.8% | +6.9 | 3.13 | 8.13 | +17.0 | +5.9 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 80.0% | 31.2% | 31.2% | 31.2% | +5.9 | 3.02 | 6.64 | +16.7 | +5.7 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 70.0% | 14.3% | 14.3% | 14.3% | +2.7 | 1.61 | 9.69 | +14.3 | +7.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 65.0% | 15.4% | 15.4% | 15.4% | +3.7 | 1.92 | 10.57 | +14.9 | +7.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +6.8 | 2.97 | 6.94 | +16.8 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 95.0% | 31.6% | 31.6% | 31.6% | +7.3 | 3.10 | 6.71 | +17.0 | +6.0 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 10.0% | 50.0% | 50.0% | 50.0% | +9.0 | 7.41 | 7.41 | +17.6 | +2.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 10.0% | 50.0% | 50.0% | 50.0% | +9.0 | 7.41 | 7.41 | +17.6 | +2.3 |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+1.3; validation N=2 Fav=0.0% Avg=-0.2; out_of_sample N=1 Fav=100.0% Avg=+15.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +2.5 | 3.91 | 6.51 | +12.8 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +10.6 | 999.00 | 999.00 | +20.3 | +2.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 28.6% | +2.6 | 3.34 | 6.68 | +11.8 | +4.8 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +2.5 | 3.91 | 6.51 | +12.8 | +4.6 |
| `confluence_gte_70` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 25.0% | +4.2 | 29.00 | 14.50 | +15.1 | +3.5 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +2.1 | 17.00 | 17.00 | +17.0 | +2.5 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | +1.4 | 6.80 | 13.60 | +12.3 | +3.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +2.5 | 3.91 | 6.51 | +12.8 | +4.6 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 40.0% | +1.8 | 2.36 | 7.07 | +10.9 | +5.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 50.0% | -0.2 | 0.00 | 0.00 | +12.2 | +2.5 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=42.9% Avg=+4.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +1.6 | 1.51 | 3.53 | +10.4 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +1.6 | 1.51 | 3.53 | +10.4 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +1.6 | 1.51 | 3.53 | +10.4 | +6.5 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +1.6 | 1.51 | 3.53 | +10.4 | +6.5 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +1.6 | 1.51 | 3.53 | +10.4 | +6.5 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +1.6 | 1.51 | 3.53 | +10.4 | +6.5 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +1.6 | 1.51 | 3.53 | +10.4 | +6.5 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +5.6 | +8.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 14.3% | +4.1 | 2.66 | 3.54 | +13.5 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +1.6 | 1.51 | 3.53 | +10.4 | +6.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +5.6 | +8.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +1.6 | 1.51 | 3.53 | +10.4 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +1.6 | 1.51 | 3.53 | +10.4 | +6.5 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +0.5 | +8.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +0.0 | +9.8 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+7.3; validation N=14 Fav=35.7% Avg=-1.6; out_of_sample N=8 Fav=25.0% Avg=+2.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -1.1 | 0.86 | 1.72 | +16.0 | +9.5 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 73.3% | 31.8% | 31.8% | 18.2% | -3.0 | 0.68 | 1.27 | +15.8 | +11.1 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 90.0% | 29.6% | 29.6% | 14.8% | -2.6 | 0.71 | 1.50 | +14.9 | +10.3 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 90.0% | 29.6% | 29.6% | 14.8% | -2.6 | 0.71 | 1.51 | +15.5 | +10.3 |
| `asian_range_gte_30` | 26 | S_STRANGER | 86.7% | 26.9% | 26.9% | 15.4% | -3.1 | 0.67 | 1.63 | +14.8 | +10.3 |
| `confluence_gte_60` | 21 | S_STRANGER | 70.0% | 28.6% | 28.6% | 14.3% | -0.6 | 0.90 | 1.96 | +15.4 | +6.6 |
| `confluence_gte_70` | 4 | S_STRANGER | 13.3% | 25.0% | 25.0% | 25.0% | -10.2 | 0.39 | 1.17 | +15.6 | +3.8 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 20.0% | 16.7% | 16.7% | 0.0% | -8.5 | 0.25 | 1.25 | +8.8 | +16.2 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 80.0% | 33.3% | 33.3% | 12.5% | +0.5 | 1.07 | 2.01 | +16.9 | +10.9 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 63.3% | 26.3% | 26.3% | 10.5% | -6.0 | 0.46 | 1.20 | +14.3 | +12.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 20.0% | 16.7% | 16.7% | 0.0% | -8.5 | 0.25 | 1.25 | +8.8 | +16.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 90.0% | 29.6% | 29.6% | 14.8% | -2.6 | 0.71 | 1.51 | +15.5 | +10.3 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -1.1 | 0.86 | 1.72 | +16.0 | +9.5 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 6.7% | 50.0% | 50.0% | 50.0% | +7.3 | 999.00 | 999.00 | +20.4 | +5.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 6.7% | 50.0% | 50.0% | 50.0% | +7.3 | 999.00 | 999.00 | +20.4 | +5.9 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=30.0% Avg=+3.0; validation N=1 Fav=100.0% Avg=+42.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 11.8% | +3.7 | 1.97 | 4.73 | +16.1 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 94.1% | 31.2% | 31.2% | 12.5% | +4.5 | 2.31 | 5.09 | +17.0 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 11.8% | +3.7 | 1.97 | 4.73 | +16.1 | +7.0 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 11.8% | +3.7 | 1.97 | 4.73 | +16.1 | +7.0 |
| `asian_range_gte_30` | 11 | S_STRANGER | 64.7% | 36.4% | 36.4% | 18.2% | +6.6 | 2.47 | 4.31 | +20.2 | +6.3 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 11.8% | +3.7 | 1.97 | 4.73 | +16.1 | +7.0 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 11.8% | +3.7 | 1.97 | 4.73 | +16.1 | +7.0 |
| `tdi_rsi_gt_signal` | 2 | R_RUNNER | 11.8% | 100.0% | 100.0% | 0.0% | +23.8 | 999.00 | 999.00 | +31.9 | +0.1 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 88.2% | 26.7% | 26.7% | 6.7% | +1.3 | 1.34 | 3.68 | +14.6 | +7.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 64.7% | 36.4% | 36.4% | 18.2% | +6.6 | 2.47 | 4.31 | +20.2 | +6.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_RUNNER | 11.8% | 100.0% | 100.0% | 0.0% | +23.8 | 999.00 | 999.00 | +31.9 | +0.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 11.8% | +3.7 | 1.97 | 4.73 | +16.1 | +7.0 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 88.2% | 26.7% | 26.7% | 13.3% | +1.4 | 1.35 | 3.71 | +14.2 | +7.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 17.6% | 33.3% | 33.3% | 33.3% | +13.6 | 5.38 | 10.75 | +24.4 | +4.1 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 41.2% | 28.6% | 28.6% | 0.0% | +3.7 | 2.24 | 5.60 | +17.2 | +5.2 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=10 Fav=30.0% Avg=+1.3; out_of_sample N=6 Fav=33.3% Avg=+4.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 23.5% | +2.1 | 1.38 | 3.04 | +13.2 | +9.4 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 76.5% | 23.1% | 23.1% | 15.4% | -0.1 | 0.98 | 2.93 | +10.5 | +9.8 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 82.4% | 21.4% | 21.4% | 14.3% | -1.5 | 0.77 | 2.58 | +10.2 | +10.9 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 88.2% | 26.7% | 26.7% | 20.0% | +1.6 | 1.26 | 3.15 | +13.7 | +10.3 |
| `asian_range_gte_30` | 16 | S_STRANGER | 94.1% | 31.2% | 31.2% | 25.0% | +2.4 | 1.44 | 2.89 | +14.0 | +9.6 |
| `confluence_gte_60` | 16 | S_STRANGER | 94.1% | 25.0% | 25.0% | 18.8% | +0.4 | 1.08 | 2.96 | +12.0 | +9.9 |
| `confluence_gte_70` | 6 | S_STRANGER | 35.3% | 16.7% | 16.7% | 0.0% | -7.2 | 0.11 | 0.57 | +6.0 | +13.3 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 33.3% | -4.0 | 0.00 | 0.00 | +6.1 | +8.2 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 76.5% | 23.1% | 23.1% | 23.1% | +2.9 | 1.55 | 4.65 | +13.6 | +9.6 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 70.6% | 25.0% | 25.0% | 16.7% | +0.2 | 1.04 | 2.76 | +11.3 | +10.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 33.3% | -4.0 | 0.00 | 0.00 | +6.1 | +8.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 88.2% | 26.7% | 26.7% | 20.0% | +1.6 | 1.26 | 3.15 | +13.7 | +10.3 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 23.5% | +2.1 | 1.38 | 3.04 | +13.2 | +9.4 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 11.8% | 50.0% | 50.0% | 50.0% | +12.0 | 6.83 | 6.83 | +16.8 | +4.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 11.8% | 50.0% | 50.0% | 50.0% | +12.0 | 6.83 | 6.83 | +16.8 | +4.2 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-20.0; validation N=4 Fav=75.0% Avg=+21.8; out_of_sample N=1 Fav=0.0% Avg=-7.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 28.6% | 33.3% | 14.3% | +1.1 | 1.19 | 2.38 | +14.0 | +10.0 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 90.5% | 26.3% | 31.6% | 10.5% | +0.9 | 1.17 | 2.54 | +13.4 | +10.0 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 100.0% | 28.6% | 33.3% | 14.3% | +1.1 | 1.19 | 2.38 | +14.0 | +10.0 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 28.6% | 33.3% | 14.3% | +1.1 | 1.19 | 2.38 | +14.0 | +10.0 |
| `asian_range_gte_30` | 19 | S_STRANGER | 90.5% | 31.6% | 36.8% | 15.8% | +1.3 | 1.20 | 2.06 | +15.1 | +10.8 |
| `confluence_gte_60` | 14 | S_STRANGER | 66.7% | 28.6% | 28.6% | 7.1% | -1.5 | 0.79 | 1.98 | +13.7 | +10.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 52.4% | 36.4% | 36.4% | 18.2% | +4.0 | 1.62 | 2.84 | +16.4 | +10.7 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 61.9% | 30.8% | 30.8% | 15.4% | +3.7 | 1.74 | 3.91 | +15.8 | +9.6 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 81.0% | 29.4% | 35.3% | 11.8% | +1.1 | 1.19 | 2.17 | +14.5 | +10.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 33.3% | 42.9% | 42.9% | 14.3% | +5.6 | 1.81 | 2.41 | +18.8 | +12.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 28.6% | 33.3% | 14.3% | +1.1 | 1.19 | 2.38 | +14.0 | +10.0 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 28.6% | 33.3% | 14.3% | +1.1 | 1.19 | 2.38 | +14.0 | +10.0 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 38.1% | 25.0% | 25.0% | 12.5% | -1.2 | 0.78 | 2.33 | +11.2 | +10.7 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 28.6% | 16.7% | 16.7% | 0.0% | +1.0 | 1.33 | 6.63 | +10.0 | +7.2 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=-8.0; validation N=6 Fav=50.0% Avg=+6.3; out_of_sample N=3 Fav=66.7% Avg=+14.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 28.6% | 32.1% | 35.7% | -1.4 | 0.82 | 1.45 | +14.6 | +9.7 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 82.1% | 30.4% | 34.8% | 34.8% | -1.5 | 0.83 | 1.34 | +15.6 | +9.9 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 92.9% | 30.8% | 34.6% | 38.5% | -1.2 | 0.85 | 1.32 | +15.5 | +9.5 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 96.4% | 29.6% | 33.3% | 37.0% | -1.4 | 0.82 | 1.36 | +15.0 | +9.9 |
| `asian_range_gte_30` | 22 | S_STRANGER | 78.6% | 36.4% | 40.9% | 40.9% | +1.5 | 1.24 | 1.51 | +16.3 | +9.7 |
| `confluence_gte_60` | 8 | S_STRANGER | 28.6% | 37.5% | 37.5% | 62.5% | +9.8 | 7.99 | 7.99 | +21.6 | +6.1 |
| `confluence_gte_70` | 2 | R_REPEATER | 7.1% | 50.0% | 50.0% | 50.0% | +29.8 | 597.50 | 597.50 | +34.9 | +1.4 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 50.0% | 14.3% | 14.3% | 28.6% | -8.4 | 0.28 | 1.38 | +11.5 | +12.0 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 46.4% | 46.2% | 46.2% | 53.8% | +3.7 | 2.04 | 1.70 | +19.2 | +7.1 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 64.3% | 38.9% | 44.4% | 38.9% | +1.6 | 1.22 | 1.37 | +17.3 | +10.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 25.0% | 14.3% | 14.3% | 14.3% | -8.1 | 0.38 | 2.29 | +10.6 | +16.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 85.7% | 29.2% | 33.3% | 37.5% | -1.4 | 0.83 | 1.34 | +15.6 | +10.0 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 96.4% | 25.9% | 29.6% | 33.3% | -2.3 | 0.71 | 1.42 | +14.1 | +9.8 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 39.3% | 36.4% | 45.5% | 36.4% | +1.0 | 1.15 | 1.38 | +13.3 | +12.3 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_RUNNER | 14.3% | 75.0% | 75.0% | 75.0% | +16.0 | 27.71 | 9.24 | +25.0 | +4.2 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=25.0% Avg=+2.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=40.0% Avg=+0.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | +0.1 | 1.03 | 1.80 | +11.0 | +8.7 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 81.8% | 33.3% | 44.4% | 11.1% | +1.0 | 1.20 | 1.50 | +10.1 | +8.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 90.9% | 30.0% | 40.0% | 10.0% | +0.2 | 1.03 | 1.55 | +10.4 | +8.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | +0.1 | 1.03 | 1.80 | +11.0 | +8.7 |
| `asian_range_gte_30` | 7 | S_STRANGER | 63.6% | 14.3% | 28.6% | 0.0% | -3.3 | 0.49 | 1.22 | +7.1 | +10.0 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | +0.1 | 1.03 | 1.80 | +11.0 | +8.7 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | +0.1 | 1.03 | 1.80 | +11.0 | +8.7 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | +0.1 | 1.03 | 1.80 | +11.0 | +8.7 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -1.5 | 0.67 | 2.01 | +13.5 | +11.2 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 63.6% | 14.3% | 28.6% | 0.0% | -3.3 | 0.49 | 1.22 | +7.1 | +10.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 63.6% | 14.3% | 28.6% | 0.0% | -3.3 | 0.49 | 1.22 | +7.1 | +10.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | +0.1 | 1.03 | 1.80 | +11.0 | +8.7 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 9.1% | +0.1 | 1.03 | 1.80 | +11.0 | +8.7 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -9.2 | 0.00 | 0.00 | +4.5 | +11.5 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=-0.1; validation N=3 Fav=66.7% Avg=+6.9; out_of_sample N=1 Fav=0.0% Avg=-8.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | -2.0 | 0.63 | 1.47 | +13.1 | +12.1 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 11.1% | -0.9 | 0.82 | 1.36 | +11.4 | +12.1 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | -2.0 | 0.63 | 1.47 | +13.1 | +12.1 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | -2.0 | 0.63 | 1.47 | +13.1 | +12.1 |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | -2.0 | 0.63 | 1.47 | +13.1 | +12.1 |
| `confluence_gte_60` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 0.0% | +1.5 | 1.47 | 2.45 | +16.3 | +9.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -6.1 | 0.22 | 0.67 | +8.3 | +9.4 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 0.0% | -3.0 | 0.48 | 1.44 | +13.5 | +11.9 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 11.1% | -0.9 | 0.82 | 1.36 | +11.4 | +12.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -6.1 | 0.22 | 0.67 | +8.3 | +9.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 10.0% | -1.4 | 0.73 | 1.46 | +14.3 | +11.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 10.0% | -1.4 | 0.73 | 1.46 | +14.3 | +11.9 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -14.1 | 0.00 | 0.00 | +2.1 | +17.1 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 0.0% | -6.5 | 0.18 | 0.71 | +6.9 | +10.5 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=+12.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=3 Fav=33.3% Avg=+6.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 33.3% | +3.4 | 2.13 | 4.79 | +19.0 | +6.9 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 86.7% | 23.1% | 23.1% | 30.8% | +3.2 | 2.04 | 5.43 | +20.6 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 33.3% | +3.4 | 2.13 | 4.79 | +19.0 | +6.9 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 33.3% | +3.4 | 2.13 | 4.79 | +19.0 | +6.9 |
| `asian_range_gte_30` | 14 | S_STRANGER | 93.3% | 28.6% | 28.6% | 28.6% | +3.6 | 2.13 | 4.79 | +19.0 | +7.3 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 33.3% | +3.4 | 2.13 | 4.79 | +19.0 | +6.9 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 33.3% | +3.4 | 2.13 | 4.79 | +19.0 | +6.9 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 46.7% | 28.6% | 28.6% | 42.9% | +8.2 | 5.64 | 11.28 | +29.0 | +8.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 60.0% | 22.2% | 22.2% | 33.3% | +2.9 | 2.63 | 6.57 | +24.3 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 80.0% | 25.0% | 25.0% | 25.0% | +3.4 | 2.04 | 5.43 | +20.7 | +7.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 40.0% | 33.3% | 33.3% | 33.3% | +9.6 | 5.64 | 11.28 | +30.5 | +9.5 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 6.7% | 100.0% | 100.0% | 100.0% | +38.2 | 999.00 | 999.00 | +46.5 | +4.9 |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 93.3% | 28.6% | 28.6% | 35.7% | +4.0 | 2.40 | 4.79 | +20.3 | +6.9 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 33.3% | +3.4 | 2.13 | 4.79 | +19.0 | +6.9 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 26.7% | 25.0% | 25.0% | 25.0% | +6.0 | 2.69 | 8.08 | +14.2 | +5.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -0.6 | 0.00 | 0.00 | +8.4 | +1.8 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=0.0% Avg=-15.3; out_of_sample N=2 Fav=100.0% Avg=+28.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +2.5 | 1.45 | 2.61 | +12.2 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 80.0% | 25.0% | 33.3% | 25.0% | +1.8 | 1.27 | 2.23 | +12.5 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 86.7% | 30.8% | 38.5% | 30.8% | +3.5 | 1.58 | 2.21 | +13.7 | +7.0 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 80.0% | 25.0% | 33.3% | 25.0% | +1.8 | 1.27 | 2.23 | +12.5 | +7.5 |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +2.5 | 1.45 | 2.61 | +12.2 | +6.7 |
| `confluence_gte_60` | 11 | S_STRANGER | 73.3% | 36.4% | 45.5% | 36.4% | +5.1 | 1.86 | 1.86 | +15.9 | +6.0 |
| `confluence_gte_70` | 3 | R_REPEATER | 20.0% | 66.7% | 66.7% | 66.7% | +18.9 | 8.57 | 4.28 | +27.6 | +6.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 53.3% | 37.5% | 37.5% | 25.0% | +3.6 | 1.54 | 2.56 | +13.8 | +6.4 |
| `tdi_rsi_gte_50` | 3 | R_REPEATER | 20.0% | 66.7% | 66.7% | 33.3% | +18.7 | 52.14 | 26.07 | +24.2 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 80.0% | 25.0% | 33.3% | 25.0% | +1.8 | 1.27 | 2.23 | +12.5 | +7.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 33.3% | 40.0% | 40.0% | 20.0% | +2.3 | 1.25 | 1.88 | +15.3 | +8.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 80.0% | 25.0% | 33.3% | 25.0% | +1.8 | 1.27 | 2.23 | +12.5 | +7.5 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +2.5 | 1.45 | 2.61 | +12.2 | +6.7 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +5.9 | +9.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-2.5; validation N=6 Fav=50.0% Avg=+7.1; out_of_sample N=9 Fav=22.2% Avg=-1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 26.3% | +0.6 | 1.12 | 2.70 | +15.8 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 84.2% | 25.0% | 25.0% | 31.2% | +0.8 | 1.16 | 2.89 | +15.7 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 89.5% | 29.4% | 29.4% | 29.4% | +1.2 | 1.25 | 2.50 | +15.5 | +8.2 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 94.7% | 27.8% | 27.8% | 27.8% | +0.6 | 1.13 | 2.48 | +16.0 | +8.4 |
| `asian_range_gte_30` | 17 | S_STRANGER | 89.5% | 23.5% | 23.5% | 23.5% | +0.2 | 1.04 | 2.87 | +16.3 | +8.6 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 26.3% | +0.6 | 1.12 | 2.70 | +15.8 | +8.2 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 26.3% | +0.6 | 1.12 | 2.70 | +15.8 | +8.2 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 84.2% | 31.2% | 31.2% | 31.2% | +1.4 | 1.30 | 2.33 | +16.4 | +8.4 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 52.6% | 20.0% | 20.0% | 10.0% | -0.6 | 0.91 | 3.65 | +14.4 | +11.1 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 73.7% | 21.4% | 21.4% | 28.6% | +0.4 | 1.07 | 3.20 | +16.2 | +9.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 68.4% | 23.1% | 23.1% | 30.8% | +0.5 | 1.09 | 2.90 | +17.0 | +9.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 94.7% | 27.8% | 27.8% | 27.8% | +0.6 | 1.13 | 2.48 | +16.0 | +8.4 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 26.3% | +0.6 | 1.12 | 2.70 | +15.8 | +8.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +5.3 | +3.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +5.3 | +3.1 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=50.0% Avg=+4.3; validation N=1 Fav=100.0% Avg=+45.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +2.4 | 1.58 | 4.22 | +13.1 | +9.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 30.0% | 30.0% | 0.0% | +3.5 | 1.79 | 3.58 | +12.9 | +8.4 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +2.4 | 1.58 | 4.22 | +13.1 | +9.0 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +2.4 | 1.58 | 4.22 | +13.1 | +9.0 |
| `asian_range_gte_30` | 5 | R_REPEATER | 41.7% | 60.0% | 60.0% | 0.0% | +12.5 | 4.54 | 3.03 | +21.7 | +9.6 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +2.4 | 1.58 | 4.22 | +13.1 | +9.0 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +2.4 | 1.58 | 4.22 | +13.1 | +9.0 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 0.0% | +3.7 | 2.02 | 4.72 | +14.1 | +8.6 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +2.4 | 1.58 | 4.22 | +13.1 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 5 | R_REPEATER | 41.7% | 60.0% | 60.0% | 0.0% | +12.5 | 4.54 | 3.03 | +21.7 | +9.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_REPEATER | 41.7% | 60.0% | 60.0% | 0.0% | +12.5 | 4.54 | 3.03 | +21.7 | +9.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 0.0% | +2.8 | 1.64 | 3.84 | +13.0 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | +2.4 | 1.58 | 4.22 | +13.1 | +9.0 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +15.1 | +11.0 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 0.0% | -0.7 | 0.83 | 3.33 | +10.5 | +8.2 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=100.0% Avg=+12.3; validation N=5 Fav=60.0% Avg=+15.7; out_of_sample N=7 Fav=0.0% Avg=-7.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.4 | 0.92 | 2.62 | +13.7 | +12.0 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 62.5% | 33.3% | 33.3% | 20.0% | +3.4 | 1.85 | 3.69 | +15.7 | +10.1 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 87.5% | 28.6% | 28.6% | 19.0% | +1.5 | 1.34 | 3.12 | +14.0 | +11.1 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 91.7% | 27.3% | 27.3% | 18.2% | +0.3 | 1.06 | 2.66 | +13.8 | +11.3 |
| `asian_range_gte_30` | 20 | S_STRANGER | 83.3% | 25.0% | 25.0% | 15.0% | -0.7 | 0.88 | 2.48 | +13.4 | +13.0 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.4 | 0.92 | 2.62 | +13.7 | +12.0 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.4 | 0.92 | 2.62 | +13.7 | +12.0 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 16.7% | 50.0% | 50.0% | 0.0% | +9.4 | 10.40 | 5.20 | +17.3 | +4.0 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 83.3% | 30.0% | 30.0% | 20.0% | +1.3 | 1.27 | 2.75 | +14.4 | +11.7 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 58.3% | 35.7% | 35.7% | 21.4% | +3.8 | 1.90 | 3.42 | +16.5 | +10.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_RUNNER | 8.3% | 100.0% | 100.0% | 0.0% | +20.8 | 999.00 | 999.00 | +24.7 | +3.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 87.5% | 23.8% | 23.8% | 14.3% | -0.3 | 0.94 | 2.83 | +13.0 | +11.8 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 95.8% | 21.7% | 21.7% | 13.0% | -1.5 | 0.75 | 2.55 | +12.4 | +12.1 |
| `feature_momentum_breakout_exception` | 3 | R_RUNNER | 12.5% | 100.0% | 100.0% | 100.0% | +17.4 | 999.00 | 999.00 | +30.5 | +4.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_RUNNER | 12.5% | 100.0% | 100.0% | 100.0% | +17.4 | 999.00 | 999.00 | +30.5 | +4.6 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+0.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=0.0% Avg=-13.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 8.3% | -4.4 | 0.30 | 0.60 | +5.5 | +13.4 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 50.0% | 0.0% | 16.7% | 16.7% | -10.5 | 0.05 | 0.24 | +3.2 | +16.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 8.3% | -4.4 | 0.30 | 0.60 | +5.5 | +13.4 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 8.3% | -4.4 | 0.30 | 0.60 | +5.5 | +13.4 |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 8.3% | -4.4 | 0.30 | 0.60 | +5.5 | +13.4 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 8.3% | -4.4 | 0.30 | 0.60 | +5.5 | +13.4 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 8.3% | -4.4 | 0.30 | 0.60 | +5.5 | +13.4 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 25.0% | 25.0% | 0.0% | -7.3 | 0.14 | 0.41 | +4.3 | +16.1 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -11.3 | 0.00 | 0.00 | +2.2 | +19.0 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 50.0% | 0.0% | 16.7% | 16.7% | -10.5 | 0.05 | 0.24 | +3.2 | +16.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -19.3 | 0.00 | 0.00 | +0.9 | +23.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 58.3% | 0.0% | 14.3% | 14.3% | -9.5 | 0.05 | 0.28 | +3.6 | +16.0 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 8.3% | -4.4 | 0.30 | 0.60 | +5.5 | +13.4 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 0.0% | -3.3 | 0.43 | 0.72 | +5.3 | +13.5 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -10.6 | 0.00 | 0.00 | +1.2 | +18.8 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+0.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=50.0% Avg=+1.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 5.9% | -1.7 | 0.56 | 1.68 | +7.7 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 5.9% | -1.7 | 0.56 | 1.68 | +7.7 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 5.9% | -1.7 | 0.56 | 1.68 | +7.7 | +6.3 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 5.9% | -1.7 | 0.56 | 1.68 | +7.7 | +6.3 |
| `asian_range_gte_30` | 12 | S_STRANGER | 70.6% | 25.0% | 25.0% | 8.3% | -2.0 | 0.53 | 1.41 | +8.3 | +6.1 |
| `confluence_gte_60` | 9 | S_STRANGER | 52.9% | 11.1% | 11.1% | 0.0% | -3.6 | 0.21 | 1.47 | +7.5 | +7.3 |
| `confluence_gte_70` | 6 | S_STRANGER | 35.3% | 16.7% | 16.7% | 0.0% | -1.0 | 0.59 | 2.34 | +6.5 | +5.7 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 88.2% | 26.7% | 26.7% | 6.7% | -1.2 | 0.66 | 1.65 | +7.0 | +6.1 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 88.2% | 26.7% | 26.7% | 6.7% | -0.9 | 0.73 | 1.83 | +7.6 | +5.7 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 70.6% | 25.0% | 25.0% | 8.3% | -2.0 | 0.53 | 1.41 | +8.3 | +6.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 64.7% | 27.3% | 27.3% | 9.1% | -1.6 | 0.61 | 1.41 | +8.0 | +5.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 5.9% | -1.7 | 0.56 | 1.68 | +7.7 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 5.9% | -1.7 | 0.56 | 1.68 | +7.7 | +6.3 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 29.4% | 40.0% | 40.0% | 20.0% | +0.5 | 1.12 | 1.67 | +11.1 | +6.7 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 47.1% | 37.5% | 37.5% | 12.5% | +0.4 | 1.13 | 1.88 | +9.9 | +4.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.9; validation N=8 Fav=25.0% Avg=-0.0; out_of_sample N=4 Fav=25.0% Avg=-3.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.5 | 0.75 | 2.26 | +13.1 | +8.6 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 16.7% | 16.7% | 16.7% | -3.1 | 0.52 | 2.33 | +10.8 | +7.8 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.5 | 0.75 | 2.26 | +13.1 | +8.6 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 92.3% | 16.7% | 16.7% | 16.7% | -3.1 | 0.52 | 2.33 | +10.8 | +7.8 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.5 | 0.75 | 2.26 | +13.1 | +8.6 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.5 | 0.75 | 2.26 | +13.1 | +8.6 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.5 | 0.75 | 2.26 | +13.1 | +8.6 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 0.0% | -3.2 | 0.56 | 1.12 | +11.3 | +11.0 |
| `tdi_rsi_gte_50` | 4 | R_REPEATER | 30.8% | 50.0% | 50.0% | 25.0% | +3.1 | 1.69 | 1.69 | +19.8 | +11.6 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 92.3% | 16.7% | 16.7% | 16.7% | -3.1 | 0.52 | 2.33 | +10.8 | +7.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 0.0% | -3.2 | 0.56 | 1.12 | +11.3 | +11.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 92.3% | 16.7% | 16.7% | 16.7% | -3.1 | 0.52 | 2.33 | +10.8 | +7.8 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -1.5 | 0.75 | 2.26 | +13.1 | +8.6 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +4.9 | +4.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +4.9 | +4.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=+1.9; out_of_sample N=7 Fav=14.3% Avg=-6.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 15.4% | -5.3 | 0.36 | 0.82 | +10.0 | +10.6 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 25.0% | 33.3% | 16.7% | -2.9 | 0.53 | 1.06 | +10.2 | +11.4 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 15.4% | -5.3 | 0.36 | 0.82 | +10.0 | +10.6 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 15.4% | -5.3 | 0.36 | 0.82 | +10.0 | +10.6 |
| `asian_range_gte_30` | 12 | S_STRANGER | 92.3% | 16.7% | 25.0% | 8.3% | -6.6 | 0.26 | 0.78 | +8.3 | +11.1 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 15.4% | -5.3 | 0.36 | 0.82 | +10.0 | +10.6 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 15.4% | -5.3 | 0.36 | 0.82 | +10.0 | +10.6 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 18.2% | 27.3% | 9.1% | -5.3 | 0.32 | 0.86 | +9.0 | +9.6 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 69.2% | 11.1% | 22.2% | 0.0% | -4.5 | 0.33 | 1.14 | +8.6 | +13.2 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 84.6% | 18.2% | 27.3% | 9.1% | -4.1 | 0.38 | 1.01 | +8.3 | +12.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 76.9% | 20.0% | 30.0% | 10.0% | -2.4 | 0.54 | 1.25 | +9.1 | +10.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 15.4% | -5.3 | 0.36 | 0.82 | +10.0 | +10.6 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 23.1% | 30.8% | 15.4% | -5.3 | 0.36 | 0.82 | +10.0 | +10.6 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -11.9 | 0.00 | 0.00 | +1.2 | +13.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -11.9 | 0.00 | 0.00 | +1.2 | +13.2 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=14 Fav=21.4% Avg=-1.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -1.8 | 0.68 | 2.26 | +10.7 | +9.7 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 0.0% | -3.4 | 0.46 | 2.31 | +12.4 | +10.5 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 64.3% | 11.1% | 11.1% | 0.0% | -5.0 | 0.28 | 2.25 | +10.1 | +10.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 20.0% | -1.0 | 0.81 | 2.85 | +12.2 | +9.1 |
| `asian_range_gte_30` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 7.7% | -4.1 | 0.34 | 1.70 | +9.3 | +10.3 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -1.8 | 0.68 | 2.26 | +10.7 | +9.7 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -1.8 | 0.68 | 2.26 | +10.7 | +9.7 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -8.7 | 0.00 | 0.00 | +8.6 | +13.3 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 78.6% | 9.1% | 9.1% | 0.0% | -5.7 | 0.22 | 2.21 | +9.0 | +11.4 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 0.0% | -3.4 | 0.46 | 2.31 | +12.4 | +10.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 0.0% | -7.7 | 0.00 | 0.00 | +10.8 | +12.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 57.1% | 12.5% | 12.5% | 12.5% | -4.4 | 0.33 | 2.00 | +10.2 | +10.8 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -1.8 | 0.68 | 2.26 | +10.7 | +9.7 |
| `feature_momentum_breakout_exception` | 3 | R_REPEATER | 21.4% | 66.7% | 66.7% | 33.3% | +14.4 | 21.52 | 10.76 | +20.3 | +1.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 0.0% | +7.8 | 8.48 | 8.48 | +15.5 | +1.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-8.5; validation N=4 Fav=75.0% Avg=+14.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | -3.8 | 0.54 | 1.43 | +11.3 | +14.1 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 71.4% | 30.0% | 30.0% | 10.0% | -0.0 | 1.00 | 1.99 | +13.4 | +16.7 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 23.1% | 23.1% | 23.1% | -3.5 | 0.57 | 1.33 | +11.9 | +13.7 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | -3.8 | 0.54 | 1.43 | +11.3 | +14.1 |
| `asian_range_gte_30` | 12 | S_STRANGER | 85.7% | 25.0% | 25.0% | 16.7% | -3.8 | 0.57 | 1.33 | +12.1 | +14.6 |
| `confluence_gte_60` | 6 | R_REPEATER | 42.9% | 50.0% | 50.0% | 0.0% | +6.7 | 2.89 | 2.89 | +18.8 | +6.7 |
| `confluence_gte_70` | 3 | R_REPEATER | 21.4% | 66.7% | 66.7% | 0.0% | +8.8 | 3.97 | 1.98 | +15.9 | +5.5 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -8.9 | 0.00 | 0.00 | +1.3 | +9.9 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 33.3% | 33.3% | 11.1% | +0.2 | 1.03 | 1.72 | +13.9 | +17.8 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 71.4% | 30.0% | 30.0% | 10.0% | -0.0 | 1.00 | 1.99 | +13.4 | +16.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -8.9 | 0.00 | 0.00 | +1.3 | +9.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 85.7% | 25.0% | 25.0% | 16.7% | -3.8 | 0.57 | 1.33 | +12.1 | +14.2 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | -3.8 | 0.54 | 1.43 | +11.3 | +14.1 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 50.0% | -3.5 | 0.00 | 0.00 | +6.3 | +13.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=66.7% Avg=+15.5; out_of_sample N=2 Fav=0.0% Avg=-12.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -7.0 | 0.42 | 1.54 | +11.0 | +14.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 57.1% | 25.0% | 25.0% | 0.0% | -3.3 | 0.66 | 1.98 | +12.2 | +17.0 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 0.0% | -9.7 | 0.30 | 1.52 | +9.6 | +15.7 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 0.0% | -9.1 | 0.30 | 1.65 | +9.6 | +14.8 |
| `asian_range_gte_30` | 9 | S_STRANGER | 64.3% | 33.3% | 33.3% | 0.0% | -3.6 | 0.69 | 1.38 | +12.2 | +10.7 |
| `confluence_gte_60` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 0.0% | -9.8 | 0.30 | 1.51 | +10.3 | +15.6 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -10.6 | 0.00 | 0.00 | +0.3 | +20.9 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 78.6% | 27.3% | 27.3% | 0.0% | -1.8 | 0.78 | 2.08 | +13.2 | +14.3 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 78.6% | 27.3% | 27.3% | 0.0% | -1.8 | 0.78 | 2.08 | +13.2 | +14.3 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 35.7% | 40.0% | 40.0% | 0.0% | +4.5 | 1.80 | 2.70 | +13.8 | +14.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 35.7% | 40.0% | 40.0% | 0.0% | +4.5 | 1.80 | 2.70 | +13.8 | +14.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 0.0% | -9.1 | 0.30 | 1.65 | +9.6 | +14.8 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -7.0 | 0.42 | 1.54 | +11.0 | +14.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=20.0% Avg=+0.4; validation N=2 Fav=50.0% Avg=+15.9; out_of_sample N=3 Fav=33.3% Avg=-5.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -0.7 | 0.85 | 2.75 | +9.9 | +8.0 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 16.7% | 16.7% | 22.2% | -2.5 | 0.47 | 2.04 | +8.7 | +8.7 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 95.0% | 15.8% | 15.8% | 26.3% | -2.4 | 0.47 | 2.04 | +8.5 | +8.4 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -0.7 | 0.85 | 2.75 | +9.9 | +8.0 |
| `asian_range_gte_30` | 19 | S_STRANGER | 95.0% | 15.8% | 15.8% | 26.3% | -2.4 | 0.47 | 2.04 | +8.5 | +8.4 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -0.7 | 0.85 | 2.75 | +9.9 | +8.0 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -0.7 | 0.85 | 2.75 | +9.9 | +8.0 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 75.0% | 26.7% | 26.7% | 40.0% | +1.4 | 1.40 | 2.81 | +12.0 | +7.6 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 30.0% | 16.7% | 16.7% | 33.3% | +1.2 | 1.29 | 5.16 | +13.9 | +7.4 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 90.0% | 16.7% | 16.7% | 22.2% | -2.5 | 0.47 | 2.04 | +8.7 | +8.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 65.0% | 23.1% | 23.1% | 30.8% | -0.9 | 0.78 | 2.08 | +10.7 | +8.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -0.7 | 0.85 | 2.75 | +9.9 | +8.0 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -0.7 | 0.85 | 2.75 | +9.9 | +8.0 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | -2.3 | 0.54 | 2.17 | +8.6 | +8.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -4.1 | 0.00 | 0.00 | +11.0 | +5.2 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-3.0; validation N=4 Fav=75.0% Avg=+14.1; out_of_sample N=6 Fav=0.0% Avg=-8.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -0.9 | 0.84 | 3.09 | +13.7 | +10.9 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 80.0% | 25.0% | 25.0% | 16.7% | -0.0 | 0.99 | 2.65 | +12.3 | +11.5 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -0.9 | 0.84 | 3.09 | +13.7 | +10.9 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 93.3% | 21.4% | 21.4% | 14.3% | -0.6 | 0.89 | 2.98 | +13.5 | +11.2 |
| `asian_range_gte_30` | 11 | S_STRANGER | 73.3% | 9.1% | 9.1% | 9.1% | -3.7 | 0.38 | 3.38 | +12.4 | +11.3 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -0.9 | 0.84 | 3.09 | +13.7 | +10.9 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -0.9 | 0.84 | 3.09 | +13.7 | +10.9 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | +0.0 | 0.00 | 0.00 | +3.0 | +7.1 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 86.7% | 23.1% | 23.1% | 15.4% | -0.2 | 0.96 | 2.87 | +15.6 | +10.0 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 53.3% | 12.5% | 12.5% | 12.5% | -3.5 | 0.47 | 2.82 | +10.0 | +12.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | +0.0 | 0.00 | 0.00 | +3.0 | +7.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 93.3% | 21.4% | 21.4% | 14.3% | -0.6 | 0.89 | 2.98 | +13.5 | +11.2 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -0.9 | 0.84 | 3.09 | +13.7 | +10.9 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +3.6 | +7.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +3.6 | +7.0 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=0.0% Avg=-14.5; out_of_sample N=9 Fav=33.3% Avg=-1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 33.3% | 26.7% | -6.0 | 0.40 | 0.64 | +11.0 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 73.3% | 9.1% | 27.3% | 27.3% | -3.3 | 0.54 | 1.09 | +11.6 | +7.8 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 20.0% | 33.3% | 26.7% | -6.0 | 0.40 | 0.64 | +11.0 | +7.2 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 93.3% | 14.3% | 28.6% | 21.4% | -7.2 | 0.32 | 0.64 | +10.7 | +7.7 |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 20.0% | 33.3% | 26.7% | -6.0 | 0.40 | 0.64 | +11.0 | +7.2 |
| `confluence_gte_60` | 14 | S_STRANGER | 93.3% | 21.4% | 35.7% | 28.6% | -6.4 | 0.40 | 0.56 | +11.7 | +7.5 |
| `confluence_gte_70` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 0.0% | -4.9 | 0.32 | 0.32 | +6.4 | +7.5 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 66.7% | 0.0% | 20.0% | 20.0% | -7.4 | 0.15 | 0.46 | +9.8 | +7.3 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 26.7% | 25.0% | 25.0% | 25.0% | +1.0 | 7.67 | 15.33 | +12.7 | +9.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 73.3% | 9.1% | 27.3% | 27.3% | -3.3 | 0.54 | 1.09 | +11.6 | +7.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 53.3% | 0.0% | 25.0% | 25.0% | -0.6 | 0.74 | 1.49 | +10.9 | +7.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 93.3% | 14.3% | 28.6% | 21.4% | -7.2 | 0.32 | 0.64 | +10.7 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 33.3% | 26.7% | -6.0 | 0.40 | 0.64 | +11.0 | +7.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -0.4 | 0.00 | 0.00 | +2.1 | +3.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -0.4 | 0.00 | 0.00 | +2.1 | +3.4 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=25.0% Avg=-4.8; validation N=3 Fav=33.3% Avg=+4.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 12.5% | -3.4 | 0.53 | 2.31 | +10.1 | +10.8 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 81.2% | 23.1% | 23.1% | 15.4% | -3.0 | 0.62 | 2.06 | +10.9 | +11.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 81.2% | 23.1% | 23.1% | 15.4% | -3.0 | 0.62 | 2.06 | +10.9 | +11.5 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 87.5% | 21.4% | 21.4% | 14.3% | -3.5 | 0.55 | 2.03 | +10.6 | +11.5 |
| `asian_range_gte_30` | 11 | S_STRANGER | 68.8% | 27.3% | 27.3% | 18.2% | -2.2 | 0.72 | 1.92 | +12.7 | +11.5 |
| `confluence_gte_60` | 7 | S_STRANGER | 43.8% | 14.3% | 14.3% | 14.3% | -5.0 | 0.51 | 3.05 | +12.8 | +12.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 62.5% | 20.0% | 20.0% | 10.0% | -2.4 | 0.70 | 2.79 | +9.2 | +11.9 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 68.8% | 9.1% | 9.1% | 0.0% | -7.4 | 0.18 | 1.83 | +7.2 | +13.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 68.8% | 27.3% | 27.3% | 18.2% | -2.2 | 0.72 | 1.92 | +12.7 | +11.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 50.0% | 25.0% | 25.0% | 12.5% | -1.2 | 0.85 | 2.56 | +11.2 | +11.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 81.2% | 23.1% | 23.1% | 15.4% | -3.0 | 0.62 | 2.06 | +10.9 | +11.5 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 12.5% | -3.4 | 0.53 | 2.31 | +10.1 | +10.8 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 68.8% | 18.2% | 18.2% | 9.1% | -2.4 | 0.67 | 3.02 | +10.3 | +11.1 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 50.0% | 12.5% | 12.5% | 0.0% | -6.3 | 0.27 | 1.86 | +7.8 | +12.8 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+4.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-5.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -7.7 | 0.28 | 1.04 | +9.7 | +9.4 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 93.8% | 20.0% | 20.0% | 33.3% | -7.8 | 0.29 | 0.98 | +10.2 | +9.7 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -7.7 | 0.28 | 1.04 | +9.7 | +9.4 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -7.7 | 0.28 | 1.04 | +9.7 | +9.4 |
| `asian_range_gte_30` | 15 | S_STRANGER | 93.8% | 20.0% | 20.0% | 33.3% | -7.7 | 0.30 | 0.99 | +9.2 | +9.2 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -7.7 | 0.28 | 1.04 | +9.7 | +9.4 |
| `confluence_gte_70` | 11 | S_STRANGER | 68.8% | 18.2% | 18.2% | 27.3% | -2.1 | 0.61 | 2.44 | +10.0 | +8.4 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 37.5% | 16.7% | 16.7% | 33.3% | -3.5 | 0.37 | 1.50 | +13.6 | +9.3 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 50.0% | 12.5% | 12.5% | 37.5% | -4.7 | 0.25 | 1.27 | +11.7 | +9.5 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 87.5% | 21.4% | 21.4% | 35.7% | -7.8 | 0.31 | 0.92 | +9.7 | +9.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 40.0% | -2.7 | 0.48 | 1.45 | +12.9 | +8.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -7.7 | 0.28 | 1.04 | +9.7 | +9.4 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | -7.7 | 0.28 | 1.04 | +9.7 | +9.4 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 31.2% | 40.0% | 40.0% | 40.0% | +2.8 | 1.63 | 2.45 | +13.0 | +7.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -0.8 | 0.00 | 0.00 | +7.8 | +1.2 |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=2 Fav=0.0% Avg=-2.8; out_of_sample N=3 Fav=66.7% Avg=+13.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | +0.9 | 1.29 | 5.15 | +8.9 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 0.0% | +7.1 | 4.66 | 6.99 | +13.1 | +6.2 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 0.0% | +7.1 | 4.66 | 6.99 | +13.1 | +6.2 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 0.0% | +3.1 | 2.23 | 6.68 | +10.0 | +5.9 |
| `asian_range_gte_30` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 0.0% | +4.4 | 2.40 | 3.61 | +13.3 | +7.5 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | +0.9 | 1.29 | 5.15 | +8.9 | +6.6 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | +0.9 | 1.29 | 5.15 | +8.9 | +6.6 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +4.0 | +5.6 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 90.9% | 20.0% | 20.0% | 0.0% | +2.1 | 1.88 | 6.56 | +9.4 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 3 | R_REPEATER | 27.3% | 66.7% | 66.7% | 0.0% | +13.7 | 11.30 | 5.65 | +20.7 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +6.1 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 0.0% | +4.2 | 2.86 | 7.15 | +11.1 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | +0.9 | 1.29 | 5.15 | +8.9 | +6.6 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 0.0% | -0.5 | 0.88 | 3.54 | +7.3 | +7.8 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | +2.1 | 1.67 | 5.02 | +8.2 | +6.8 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.0; validation N=2 Fav=0.0% Avg=-3.7; out_of_sample N=4 Fav=50.0% Avg=+0.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -2.7 | 0.21 | 0.95 | +13.5 | +7.9 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 33.3% | -1.5 | 0.39 | 1.18 | +15.8 | +8.1 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -2.7 | 0.21 | 0.95 | +13.5 | +7.9 |
| `confluence_gte_70` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +9.3 | +7.7 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 25.0% | 25.0% | 25.0% | -3.0 | 0.27 | 0.80 | +13.4 | +8.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 75.0% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +11.4 | +8.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -2.7 | 0.21 | 0.95 | +13.5 | +7.9 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 28.6% | -1.2 | 0.51 | 1.27 | +12.8 | +6.7 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +8.6 | +7.4 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=+7.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=20.0% Avg=-0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 38.1% | -0.6 | 0.83 | 3.31 | +10.4 | +7.5 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 66.7% | 14.3% | 14.3% | 42.9% | +2.0 | 2.03 | 7.10 | +13.0 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 95.2% | 15.0% | 15.0% | 35.0% | -0.6 | 0.83 | 3.31 | +10.4 | +7.6 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 95.2% | 10.0% | 10.0% | 35.0% | -0.9 | 0.76 | 4.58 | +10.4 | +7.9 |
| `asian_range_gte_30` | 18 | S_STRANGER | 85.7% | 16.7% | 16.7% | 33.3% | -0.6 | 0.86 | 3.14 | +10.2 | +7.7 |
| `confluence_gte_60` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 38.1% | -0.6 | 0.83 | 3.31 | +10.4 | +7.5 |
| `confluence_gte_70` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 38.1% | -0.6 | 0.83 | 3.31 | +10.4 | +7.5 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 85.7% | 11.1% | 11.1% | 33.3% | -0.7 | 0.81 | 4.45 | +11.1 | +8.3 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 33.3% | 14.3% | 14.3% | 28.6% | -4.2 | 0.34 | 1.37 | +10.5 | +12.6 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 57.1% | 16.7% | 16.7% | 41.7% | +2.6 | 2.23 | 6.69 | +13.2 | +6.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 47.6% | 20.0% | 20.0% | 40.0% | +3.5 | 2.66 | 6.66 | +14.9 | +6.8 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +1.8 | +3.9 |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 85.7% | 11.1% | 11.1% | 38.9% | -0.6 | 0.83 | 4.14 | +11.3 | +8.4 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 38.1% | -0.6 | 0.83 | 3.31 | +10.4 | +7.5 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 28.6% | 0.0% | 0.0% | 50.0% | -1.4 | 0.00 | 0.00 | +10.7 | +3.5 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=12.5% Avg=-1.8; out_of_sample N=12 Fav=16.7% Avg=-2.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 13.0% | 13.0% | 4.3% | -3.9 | 0.37 | 2.23 | +10.0 | +9.9 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 65.2% | 13.3% | 13.3% | 6.7% | -3.3 | 0.39 | 2.35 | +10.5 | +8.7 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 78.3% | 11.1% | 11.1% | 5.6% | -4.8 | 0.27 | 2.03 | +10.4 | +10.1 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 87.0% | 15.0% | 15.0% | 5.0% | -2.0 | 0.57 | 2.86 | +10.6 | +8.1 |
| `asian_range_gte_30` | 15 | S_STRANGER | 65.2% | 6.7% | 6.7% | 6.7% | -5.8 | 0.23 | 2.73 | +10.6 | +11.2 |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 13.0% | 13.0% | 4.3% | -3.9 | 0.37 | 2.23 | +10.0 | +9.9 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 13.0% | 13.0% | 4.3% | -3.9 | 0.37 | 2.23 | +10.0 | +9.9 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 39.1% | 11.1% | 11.1% | 0.0% | -4.6 | 0.35 | 2.76 | +7.5 | +11.3 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 65.2% | 13.3% | 13.3% | 0.0% | -4.0 | 0.44 | 2.86 | +9.8 | +10.6 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 47.8% | 9.1% | 9.1% | 9.1% | -4.6 | 0.34 | 3.04 | +11.0 | +10.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 17.4% | 0.0% | 0.0% | 0.0% | -8.3 | 0.00 | 0.00 | +6.0 | +12.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 87.0% | 15.0% | 15.0% | 5.0% | -2.0 | 0.57 | 2.86 | +10.6 | +8.1 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 13.0% | 13.0% | 4.3% | -3.9 | 0.37 | 2.23 | +10.0 | +9.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-1.1; validation N=3 Fav=33.3% Avg=+2.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 30.0% | -1.1 | 0.69 | 4.84 | +10.7 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 30.0% | -1.1 | 0.69 | 4.84 | +10.7 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 30.0% | -1.1 | 0.69 | 4.84 | +10.7 | +7.2 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 30.0% | -1.1 | 0.69 | 4.84 | +10.7 | +7.2 |
| `asian_range_gte_30` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 33.3% | -0.9 | 0.75 | 4.50 | +11.1 | +7.5 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 30.0% | -1.1 | 0.69 | 4.84 | +10.7 | +7.2 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 30.0% | -1.1 | 0.69 | 4.84 | +10.7 | +7.2 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 33.3% | +0.5 | 1.13 | 4.53 | +13.3 | +6.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 28.6% | -0.9 | 0.79 | 3.93 | +12.4 | +8.7 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 33.3% | -0.9 | 0.75 | 4.50 | +11.1 | +7.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 40.0% | +1.1 | 1.30 | 3.89 | +14.6 | +7.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 30.0% | -1.1 | 0.69 | 4.84 | +10.7 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 30.0% | -1.1 | 0.69 | 4.84 | +10.7 | +7.2 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 50.0% | -1.6 | 0.00 | 0.00 | +7.9 | +2.9 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=16.7% Avg=-2.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 0.0% | -4.4 | 0.12 | 0.50 | +4.6 | +9.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 0.0% | -4.4 | 0.12 | 0.50 | +4.6 | +9.8 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 0.0% | -4.4 | 0.12 | 0.50 | +4.6 | +9.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 0.0% | -4.4 | 0.12 | 0.50 | +4.6 | +9.8 |
| `asian_range_gte_30` | 6 | S_STRANGER | 60.0% | 16.7% | 33.3% | 0.0% | -2.3 | 0.31 | 0.62 | +5.5 | +6.0 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 0.0% | -4.4 | 0.12 | 0.50 | +4.6 | +9.8 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 0.0% | -4.4 | 0.12 | 0.50 | +4.6 | +9.8 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -4.3 | 0.00 | 0.00 | +2.0 | +10.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 0.0% | -3.2 | 0.14 | 0.85 | +4.6 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 60.0% | 16.7% | 33.3% | 0.0% | -2.3 | 0.31 | 0.62 | +5.5 | +6.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 0.0% | -4.4 | 0.12 | 0.50 | +4.6 | +9.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 0.0% | -4.4 | 0.12 | 0.50 | +4.6 | +9.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=+0.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=16.7% Avg=-5.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -4.8 | 0.27 | 2.45 | +9.0 | +10.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -4.8 | 0.27 | 2.45 | +9.0 | +10.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -4.8 | 0.27 | 2.45 | +9.0 | +10.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -4.8 | 0.27 | 2.45 | +9.0 | +10.0 |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -4.8 | 0.27 | 2.45 | +9.0 | +10.0 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -4.8 | 0.27 | 2.45 | +9.0 | +10.0 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -4.8 | 0.27 | 2.45 | +9.0 | +10.0 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 63.6% | 14.3% | 14.3% | 28.6% | -4.8 | 0.37 | 1.86 | +8.5 | +9.6 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 11.1% | -5.5 | 0.29 | 2.29 | +8.3 | +10.8 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -4.8 | 0.27 | 2.45 | +9.0 | +10.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 63.6% | 14.3% | 14.3% | 28.6% | -4.8 | 0.37 | 1.86 | +8.5 | +9.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -4.8 | 0.27 | 2.45 | +9.0 | +10.0 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -4.8 | 0.27 | 2.45 | +9.0 | +10.0 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +10.4 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=33.3% Avg=+3.4; out_of_sample N=4 Fav=0.0% Avg=-9.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -5.1 | 0.29 | 2.86 | +13.0 | +11.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 0.0% | -4.0 | 0.36 | 3.26 | +13.9 | +11.1 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -5.1 | 0.29 | 2.86 | +13.0 | +11.9 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 0.0% | -4.0 | 0.36 | 3.26 | +13.9 | +11.1 |
| `asian_range_gte_30` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 0.0% | -5.4 | 0.34 | 2.39 | +8.6 | +12.4 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -5.1 | 0.29 | 2.86 | +13.0 | +11.9 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -5.1 | 0.29 | 2.86 | +13.0 | +11.9 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 0.0% | -5.3 | 0.34 | 2.41 | +16.3 | +13.7 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 0.0% | -3.7 | 0.43 | 3.00 | +15.2 | +12.2 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 63.6% | 14.3% | 14.3% | 0.0% | -3.8 | 0.45 | 2.73 | +9.3 | +11.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -3.4 | 0.62 | 1.86 | +13.2 | +14.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 0.0% | -4.0 | 0.36 | 3.26 | +13.9 | +11.1 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -5.1 | 0.29 | 2.86 | +13.0 | +11.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=25.0% Avg=-0.8; out_of_sample N=2 Fav=0.0% Avg=-3.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.5 | 0.33 | 3.32 | +8.8 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 9.1% | -5.0 | 0.37 | 3.36 | +8.1 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.5 | 0.33 | 3.32 | +8.8 | +7.7 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.5 | 0.33 | 3.32 | +8.8 | +7.7 |
| `asian_range_gte_30` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 9.1% | -4.3 | 0.41 | 3.70 | +9.2 | +6.4 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.5 | 0.33 | 3.32 | +8.8 | +7.7 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.5 | 0.33 | 3.32 | +8.8 | +7.7 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 83.3% | 10.0% | 10.0% | 10.0% | -5.2 | 0.39 | 3.11 | +10.0 | +8.9 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.76 | 3.81 | +11.7 | +10.3 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 83.3% | 10.0% | 10.0% | 10.0% | -3.6 | 0.48 | 3.83 | +8.6 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 12.5% | -2.7 | 0.61 | 3.64 | +10.2 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.5 | 0.33 | 3.32 | +8.8 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -5.5 | 0.33 | 3.32 | +8.8 | +7.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=0.0% Avg=-4.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=20.0% Avg=+1.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 35.7% | -2.1 | 0.35 | 3.17 | +7.8 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 35.7% | -2.1 | 0.35 | 3.17 | +7.8 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 35.7% | -2.1 | 0.35 | 3.17 | +7.8 | +6.7 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 35.7% | -2.1 | 0.35 | 3.17 | +7.8 | +6.7 |
| `asian_range_gte_30` | 13 | S_STRANGER | 92.9% | 7.7% | 7.7% | 38.5% | -2.2 | 0.36 | 2.90 | +7.5 | +7.0 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 35.7% | -2.1 | 0.35 | 3.17 | +7.8 | +6.7 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 35.7% | -2.1 | 0.35 | 3.17 | +7.8 | +6.7 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 35.7% | -2.1 | 0.35 | 3.17 | +7.8 | +6.7 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +5.4 | +8.5 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 92.9% | 7.7% | 7.7% | 38.5% | -2.2 | 0.36 | 2.90 | +7.5 | +7.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 92.9% | 7.7% | 7.7% | 38.5% | -2.2 | 0.36 | 2.90 | +7.5 | +7.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 35.7% | -2.1 | 0.35 | 3.17 | +7.8 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 35.7% | -2.1 | 0.35 | 3.17 | +7.8 | +6.7 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 60.0% | -1.8 | 0.00 | 0.00 | +8.3 | +6.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +5.2 | +9.1 |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
