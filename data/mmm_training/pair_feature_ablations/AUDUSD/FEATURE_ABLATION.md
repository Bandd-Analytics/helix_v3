# AUDUSD Pair Feature Ablation

Generated: 2026-06-09T15:36:23.807023+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 16 | R_REPEATER | 50.0% | +6.7 | `confluence_gte_60` | 9 | R_RUNNER | 77.8% | +13.2 | 27.50 | 3.93 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 14 | R_REPEATER | 50.0% | +6.2 | `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 58.3% | +7.5 | 4.31 | 2.46 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | R_REPEATER | 50.0% | +1.0 | `tdi_rsi_gt_signal` | 6 | R_REPEATER | 66.7% | +4.0 | 5.10 | 2.55 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 21 | S_STRANGER | 47.6% | +4.8 | `all` | 21 | S_STRANGER | 47.6% | +4.8 | 3.43 | 3.43 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 20 | S_STRANGER | 45.0% | +4.3 | `tdi_rsi_gt_signal` | 7 | R_REPEATER | 57.1% | +6.8 | 3.86 | 2.89 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 16 | S_STRANGER | 43.8% | +7.1 | `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 66.7% | +12.9 | 13.72 | 3.43 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 28 | S_STRANGER | 42.9% | +2.7 | `all` | 28 | S_STRANGER | 42.9% | +2.7 | 2.24 | 2.80 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 41.7% | +3.3 | `all` | 12 | S_STRANGER | 41.7% | +3.3 | 1.94 | 2.71 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 41.7% | +2.3 | `tdi_rsi_gt_signal` | 10 | R_REPEATER | 50.0% | +3.0 | 2.43 | 2.43 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 41.7% | +1.8 | `all` | 12 | S_STRANGER | 41.7% | +1.8 | 2.33 | 3.27 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 41.7% | +1.0 | `tdi_rsi_gt_signal` | 9 | R_REPEATER | 55.6% | +3.3 | 2.23 | 1.34 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 40.0% | +5.8 | `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 42.1% | +6.1 | 3.98 | 4.98 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 40.0% | +0.7 | `hunt_to_ar_ratio_le_2_5` | 6 | R_REPEATER | 66.7% | +2.4 | 2.02 | 1.01 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 40.0% | +0.3 | `asian_range_gte_30` | 6 | R_REPEATER | 50.0% | +3.8 | 2.32 | 1.55 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 40.0% | +0.1 | `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 44.4% | +0.8 | 1.48 | 1.11 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 10 | S_STRANGER | 40.0% | -0.8 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 50.0% | +5.2 | 7.72 | 7.72 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74` | 23 | S_STRANGER | 39.1% | +1.4 | `tdi_rsi_gte_50` | 9 | R_REPEATER | 66.7% | +10.0 | 26.83 | 13.41 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 38.5% | +2.7 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 42.9% | +2.4 | 3.10 | 4.13 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 37.5% | +2.7 | `asian_range_gte_30` | 5 | R_REPEATER | 60.0% | +9.1 | 29.38 | 19.58 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 43 | S_STRANGER | 37.2% | +2.8 | `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 50.0% | +4.8 | 7.30 | 4.87 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 30 | S_STRANGER | 36.7% | +1.4 | `tdi_rsi_gt_signal` | 15 | S_STRANGER | 40.0% | +1.5 | 2.50 | 3.33 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 36.4% | +4.0 | `feature_stale_hod_exhaustion_reject` | 8 | R_REPEATER | 50.0% | +7.8 | 3.21 | 3.21 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 36.4% | +2.1 | `tdi_rsi_gt_signal` | 8 | R_REPEATER | 50.0% | +5.6 | 4.05 | 3.04 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 36.4% | -2.6 | `asian_range_gte_30` | 5 | S_STRANGER | 40.0% | -2.9 | 0.38 | 0.56 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 27 | S_STRANGER | 33.3% | +0.1 | `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 44.4% | +2.8 | 2.00 | 2.50 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 33.3% | -0.3 | `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 40.0% | +1.9 | 1.88 | 2.82 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 21 | S_STRANGER | 33.3% | -0.6 | `confluence_gte_60` | 9 | R_REPEATER | 55.6% | +0.9 | 1.35 | 0.81 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 35 | S_STRANGER | 31.4% | +1.4 | `feature_momentum_breakout_exception` | 8 | R_RUNNER | 75.0% | +5.8 | 20.17 | 6.72 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 30.8% | -3.4 | `confluence_gte_70` | 5 | S_STRANGER | 40.0% | +1.5 | 1.36 | 2.05 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 46 | S_STRANGER | 30.4% | +1.4 | `hunt_to_ar_ratio_le_2_5` | 43 | S_STRANGER | 32.6% | +1.7 | 1.75 | 3.49 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | +3.8 | `all` | 10 | S_STRANGER | 30.0% | +3.8 | 2.11 | 3.51 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | +2.0 | `all` | 10 | S_STRANGER | 30.0% | +2.0 | 2.07 | 4.14 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | +0.7 | `confluence_gte_70` | 5 | R_REPEATER | 60.0% | +5.0 | 8.84 | 5.90 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 30.0% | +0.1 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 37.5% | +0.3 | 1.11 | 1.84 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 30 | S_STRANGER | 30.0% | +0.1 | `tdi_rsi_gte_50` | 7 | R_REPEATER | 57.1% | +6.9 | 4.40 | 3.30 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | -0.1 | `tdi_rsi_gte_50` | 5 | R_REPEATER | 60.0% | +9.1 | 3.81 | 2.54 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | -0.4 | `tdi_rsi_gt_signal` | 5 | R_REPEATER | 60.0% | +2.1 | 3.57 | 2.38 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 30.0% | -1.3 | `all` | 10 | S_STRANGER | 30.0% | -1.3 | 0.56 | 1.31 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 27 | S_STRANGER | 29.6% | +2.3 | `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 32.0% | +2.5 | 3.25 | 4.22 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 41 | S_STRANGER | 29.3% | +1.3 | `tdi_rsi_gte_50` | 15 | S_STRANGER | 40.0% | +0.7 | 1.12 | 1.68 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 69 | S_STRANGER | 29.0% | +1.6 | `confluence_gte_60` | 37 | S_STRANGER | 37.8% | +3.7 | 2.57 | 3.12 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 28.6% | +2.1 | `tdi_rsi_gte_50` | 13 | S_STRANGER | 30.8% | +2.3 | 1.96 | 3.42 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 28 | S_STRANGER | 28.6% | +0.4 | `asian_range_gte_30` | 7 | R_REPEATER | 71.4% | +11.2 | 8.56 | 3.43 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 25 | S_STRANGER | 28.0% | +2.0 | `asian_range_gte_30` | 5 | S_STRANGER | 40.0% | +13.9 | 9.68 | 14.51 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 18 | S_STRANGER | 27.8% | +0.1 | `confluence_gte_60` | 14 | S_STRANGER | 35.7% | +1.6 | 1.74 | 2.32 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 29 | S_STRANGER | 27.6% | +2.3 | `confluence_gte_60` | 7 | R_REPEATER | 71.4% | +9.9 | 11.82 | 4.73 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 29 | S_STRANGER | 27.6% | +0.4 | `asian_range_gte_30` | 8 | S_STRANGER | 37.5% | +1.6 | 1.29 | 2.15 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 27.3% | +2.2 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 28.6% | +2.9 | 3.39 | 6.79 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 33 | S_STRANGER | 27.3% | +0.8 | `all` | 33 | S_STRANGER | 27.3% | +0.8 | 1.29 | 3.00 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | +0.7 | `all` | 11 | S_STRANGER | 27.3% | +0.7 | 1.24 | 3.30 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | +0.6 | `all` | 11 | S_STRANGER | 27.3% | +0.6 | 1.20 | 1.20 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 27.3% | -0.2 | `all` | 11 | S_STRANGER | 27.3% | -0.2 | 0.95 | 2.53 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 26 | S_STRANGER | 26.9% | -2.1 | `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 28.0% | -2.2 | 0.60 | 1.54 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 26.7% | +2.3 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 37.5% | +4.1 | 3.25 | 4.34 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 19 | S_STRANGER | 26.3% | -0.1 | `asian_range_gte_30` | 6 | R_REPEATER | 50.0% | +4.9 | 2.48 | 2.48 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 26.3% | -2.0 | `asian_range_gte_30` | 11 | S_STRANGER | 27.3% | -0.6 | 0.75 | 1.76 | 0 | 1 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 27 | S_STRANGER | 25.9% | -0.2 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 37.5% | +2.2 | 1.68 | 2.51 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 25.0% | -0.3 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | +2.3 | 2.45 | 4.91 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 25.0% | -0.4 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 33.3% | -0.4 | 0.85 | 1.69 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 40 | S_STRANGER | 25.0% | -1.1 | `asian_range_gte_30` | 11 | S_STRANGER | 36.4% | +1.8 | 2.00 | 3.01 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 25.0% | -1.4 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 27.3% | -0.5 | 0.86 | 2.28 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | -1.5 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 42.9% | +4.6 | 2.21 | 2.94 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | -2.8 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 33.3% | +0.4 | 1.32 | 1.32 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 53 | S_STRANGER | 24.5% | -0.6 | `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 30.0% | +1.2 | 1.27 | 2.96 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 25 | S_STRANGER | 24.0% | -0.7 | `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 30.0% | +0.0 | 1.00 | 2.34 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 21 | S_STRANGER | 23.8% | +1.0 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 31.2% | +3.1 | 2.79 | 5.03 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 26 | S_STRANGER | 23.1% | -0.1 | `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 25.0% | +0.1 | 1.03 | 3.08 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 23.1% | -2.1 | `tdi_rsi_gt_signal` | 12 | S_STRANGER | 25.0% | -2.0 | 0.61 | 1.82 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 48 | S_STRANGER | 22.9% | -0.2 | `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 44.4% | +0.3 | 1.05 | 1.05 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 31 | S_STRANGER | 22.6% | -1.9 | `feature_momentum_breakout_exception` | 15 | S_STRANGER | 20.0% | +0.2 | 1.08 | 3.96 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 18 | S_STRANGER | 22.2% | -1.8 | `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 23.5% | -1.3 | 0.65 | 2.11 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 32 | S_STRANGER | 21.9% | +0.6 | `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 22.6% | +0.7 | 1.31 | 4.12 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 32 | S_STRANGER | 21.9% | -0.1 | `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 23.3% | +0.1 | 1.05 | 3.14 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 23 | S_STRANGER | 21.7% | -1.6 | `asian_range_gte_30` | 7 | S_STRANGER | 42.9% | +4.5 | 3.67 | 3.67 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 28 | S_STRANGER | 21.4% | +0.2 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | +5.1 | 2.68 | 5.36 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 28 | S_STRANGER | 21.4% | -1.7 | `asian_range_gte_30` | 9 | S_STRANGER | 33.3% | +1.8 | 1.41 | 2.81 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 21.4% | -5.8 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | +3.6 | 2.56 | 5.12 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 19 | S_STRANGER | 21.1% | -0.0 | `confluence_gte_70` | 6 | S_STRANGER | 16.7% | +0.2 | 1.06 | 5.32 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 19 | S_STRANGER | 21.1% | -2.6 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 30.0% | -2.7 | 0.47 | 1.09 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 20.0% | +2.1 | `all` | 10 | S_STRANGER | 20.0% | +2.1 | 2.75 | 9.61 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 15 | S_STRANGER | 20.0% | +0.2 | `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 30.0% | +1.7 | 1.87 | 4.37 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -1.0 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 28.6% | +0.2 | 1.04 | 2.61 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 30 | S_STRANGER | 20.0% | -1.2 | `asian_range_gte_30` | 6 | S_STRANGER | 33.3% | +3.4 | 4.47 | 6.71 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 35 | S_STRANGER | 20.0% | -2.8 | `asian_range_gte_30` | 6 | R_REPEATER | 50.0% | +1.8 | 1.35 | 0.34 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -3.0 | `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 33.3% | -1.7 | 0.65 | 0.65 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 20.0% | -3.8 | `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 23.1% | -3.4 | 0.23 | 0.61 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 42 | S_STRANGER | 19.0% | -2.1 | `tdi_rsi_gte_50` | 19 | S_STRANGER | 31.6% | +0.7 | 1.16 | 2.32 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 21 | S_STRANGER | 19.0% | -2.6 | `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 25.0% | -1.2 | 0.64 | 1.60 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 32 | S_STRANGER | 18.8% | -1.4 | `tdi_rsi_gt_signal` | 18 | S_STRANGER | 22.2% | -1.4 | 0.66 | 1.58 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 43 | S_STRANGER | 18.6% | -1.9 | `confluence_gte_70` | 5 | S_STRANGER | 40.0% | +3.1 | 3.36 | 1.68 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 18.2% | +0.5 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 28.6% | +1.5 | 2.42 | 4.84 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -1.2 | `all` | 11 | S_STRANGER | 18.2% | -1.2 | 0.57 | 2.00 | 0 | 1 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 17.6% | -2.7 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 20.0% | -0.3 | 0.89 | 3.56 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -1.9 | `asian_range_gte_30` | 7 | S_STRANGER | 28.6% | +0.8 | 1.66 | 2.49 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -2.2 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 22.2% | +0.2 | 1.07 | 3.21 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 24 | S_STRANGER | 16.7% | -2.5 | `tdi_rsi_gte_50` | 13 | S_STRANGER | 30.8% | +5.3 | 2.45 | 5.52 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 18 | S_STRANGER | 16.7% | -4.5 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | -3.6 | 0.39 | 0.78 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 38 | S_STRANGER | 15.8% | -1.7 | `tdi_rsi_gt_signal` | 18 | S_STRANGER | 27.8% | +0.0 | 1.01 | 2.43 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -2.1 | `confluence_gte_60` | 9 | S_STRANGER | 22.2% | -0.5 | 0.74 | 1.85 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -4.0 | `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 20.0% | -2.2 | 0.35 | 1.06 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 80 | S_STRANGER | 15.0% | -1.8 | `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 27.3% | +2.1 | 1.59 | 4.23 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -0.7 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 22.2% | +1.1 | 1.54 | 4.62 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 30 | S_STRANGER | 13.3% | -2.8 | `confluence_gte_70` | 9 | S_STRANGER | 44.4% | -1.5 | 0.79 | 0.99 | 0 | 1 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 31 | S_STRANGER | 12.9% | -2.7 | `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 13.8% | -2.4 | 0.47 | 2.70 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 12.5% | +0.8 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 20.0% | +1.5 | 1.87 | 7.50 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 12.5% | -2.3 | `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 33.3% | +0.1 | 1.05 | 2.10 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 25 | S_STRANGER | 12.0% | -1.8 | `asian_range_gte_30` | 5 | S_STRANGER | 20.0% | +0.2 | 1.11 | 3.32 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 11.8% | -6.3 | `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 18.2% | -7.0 | 0.28 | 1.26 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 26 | S_STRANGER | 11.5% | -2.9 | `confluence_gte_60` | 6 | S_STRANGER | 16.7% | -1.5 | 0.52 | 2.08 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 35 | S_STRANGER | 11.4% | -3.5 | `tdi_rsi_gt_signal` | 13 | S_STRANGER | 15.4% | -6.3 | 0.18 | 0.98 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 28 | S_STRANGER | 10.7% | -2.9 | `confluence_gte_70` | 6 | S_STRANGER | 16.7% | -1.8 | 0.68 | 2.71 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 48 | S_STRANGER | 10.4% | -3.9 | `tdi_rsi_gte_50` | 15 | S_STRANGER | 20.0% | +0.5 | 1.18 | 3.15 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 10.0% | -3.9 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 11.1% | -3.5 | 0.27 | 1.06 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 10.0% | -4.1 | `feature_momentum_breakout_exception` | 6 | S_STRANGER | 16.7% | -2.8 | 0.51 | 2.57 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -4.3 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 16.7% | -3.3 | 0.20 | 1.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -7.7 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 16.7% | -3.5 | 0.15 | 0.77 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 10.0% | -8.2 | `all` | 10 | S_STRANGER | 10.0% | -8.2 | 0.03 | 0.24 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -1.3 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 12.5% | -1.2 | 0.41 | 2.90 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -2.3 | `all` | 11 | S_STRANGER | 9.1% | -2.3 | 0.25 | 2.21 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 11 | S_STRANGER | 9.1% | -6.6 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 20.0% | -3.2 | 0.19 | 0.76 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 23 | S_STRANGER | 8.7% | -2.7 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 20.0% | -1.8 | 0.28 | 1.10 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 8.3% | -2.2 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 12.5% | +0.1 | 1.02 | 5.09 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 13 | S_STRANGER | 7.7% | -2.1 | `asian_range_gte_30` | 5 | S_STRANGER | 20.0% | +0.3 | 1.08 | 4.32 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 52 | S_STRANGER | 7.7% | -5.0 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 20.0% | +3.0 | 2.16 | 8.62 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 7.1% | -2.6 | `confluence_gte_60` | 7 | S_STRANGER | 14.3% | -1.1 | 0.71 | 3.53 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 20 | S_STRANGER | 5.0% | -7.3 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 14.3% | -5.5 | 0.13 | 0.66 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 21 | S_STRANGER | 4.8% | -3.1 | `confluence_gte_70` | 7 | S_STRANGER | 14.3% | -2.1 | 0.44 | 2.18 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -3.8 | `all` | 10 | S_STRANGER | 0.0% | -3.8 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -4.2 | `feature_extreme_hunt_with_exception` | 5 | S_STRANGER | 0.0% | -2.1 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 0.0% | -4.4 | `all` | 10 | S_STRANGER | 0.0% | -4.4 | 0.05 | 0.43 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 0.0% | -5.5 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 0.0% | -5.0 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -5.7 | `confluence_gte_70` | 5 | S_STRANGER | 0.0% | -1.3 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 11 | S_STRANGER | 0.0% | -5.8 | `asian_range_gte_30` | 6 | S_STRANGER | 0.0% | -4.4 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 0.0% | -7.1 | `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 0.0% | -6.8 | 0.00 | 0.00 | 0 | 0 | fail |

## Candidate Details

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=75.0% Avg=+8.8; validation N=5 Fav=80.0% Avg=+16.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 43.8% | +6.7 | 4.96 | 3.72 | +12.6 | +4.5 |
| `hunt_to_ar_ratio_le_2_0` | 7 | R_REPEATER | 43.8% | 57.1% | 57.1% | 28.6% | +8.9 | 7.99 | 6.00 | +14.1 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 62.5% | 70.0% | 70.0% | 40.0% | +10.9 | 13.22 | 5.67 | +15.5 | +3.8 |
| `stop_hunt_le_90` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 43.8% | +6.7 | 4.96 | 3.72 | +12.6 | +4.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | R_RUNNER | 56.2% | 77.8% | 77.8% | 66.7% | +13.2 | 27.50 | 3.93 | +18.6 | +3.6 |
| `confluence_gte_70` | 3 | R_REPEATER | 18.8% | 66.7% | 66.7% | 100.0% | +11.3 | 999.00 | 999.00 | +17.8 | +2.0 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 25.0% | 50.0% | 50.0% | 25.0% | +4.3 | 3.44 | 3.44 | +8.6 | +3.5 |
| `tdi_rsi_gte_50` | 11 | R_REPEATER | 68.8% | 54.5% | 54.5% | 36.4% | +6.7 | 4.22 | 2.82 | +13.5 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 43.8% | +6.7 | 4.96 | 3.72 | +12.6 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 16 | R_REPEATER | 100.0% | 50.0% | 50.0% | 43.8% | +6.7 | 4.96 | 3.72 | +12.6 | +4.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=50.0% Avg=+15.8; validation N=9 Fav=55.6% Avg=+4.6; out_of_sample N=1 Fav=100.0% Avg=+13.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 35.7% | +6.2 | 4.14 | 2.96 | +13.2 | +3.4 |
| `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 85.7% | 58.3% | 58.3% | 33.3% | +7.5 | 4.31 | 2.46 | +14.7 | +3.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | R_REPEATER | 92.9% | 53.8% | 53.8% | 38.5% | +6.8 | 4.31 | 2.46 | +14.0 | +3.6 |
| `stop_hunt_le_90` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 35.7% | +6.2 | 4.14 | 2.96 | +13.2 | +3.4 |
| `asian_range_gte_30` | 1 | R_RUNNER | 7.1% | 100.0% | 100.0% | 100.0% | +40.0 | 999.00 | 999.00 | +61.2 | +7.7 |
| `confluence_gte_60` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 35.7% | +6.2 | 4.14 | 2.96 | +13.2 | +3.4 |
| `confluence_gte_70` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 35.7% | +6.2 | 4.14 | 2.96 | +13.2 | +3.4 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 28.6% | 50.0% | 50.0% | 50.0% | +4.2 | 2.18 | 2.18 | +10.4 | +3.2 |
| `tdi_rsi_gte_50` | 3 | R_REPEATER | 21.4% | 66.7% | 66.7% | 33.3% | +10.9 | 33.65 | 16.83 | +13.8 | +0.9 |
| `ratio_le_2_and_asian_gte_30` | 1 | R_RUNNER | 7.1% | 100.0% | 100.0% | 100.0% | +40.0 | 999.00 | 999.00 | +61.2 | +7.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 35.7% | +6.2 | 4.14 | 2.96 | +13.2 | +3.4 |
| `feature_stale_hod_exhaustion_reject` | 14 | R_REPEATER | 100.0% | 50.0% | 50.0% | 35.7% | +6.2 | 4.14 | 2.96 | +13.2 | +3.4 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -8.3 | 0.00 | 0.00 | +0.9 | +8.9 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=80.0% Avg=+5.1; validation N=1 Fav=0.0% Avg=-1.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 5.6% | +1.0 | 1.32 | 1.32 | +9.1 | +6.0 |
| `hunt_to_ar_ratio_le_2_0` | 14 | R_REPEATER | 77.8% | 50.0% | 50.0% | 7.1% | +0.2 | 1.05 | 1.05 | +8.8 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 5.6% | +1.0 | 1.32 | 1.32 | +9.1 | +6.0 |
| `stop_hunt_le_90` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 5.6% | +1.0 | 1.32 | 1.32 | +9.1 | +6.0 |
| `asian_range_gte_30` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -18.3 | 0.00 | 0.00 | +0.1 | +18.6 |
| `confluence_gte_60` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 5.6% | +1.0 | 1.32 | 1.32 | +9.1 | +6.0 |
| `confluence_gte_70` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 5.6% | +1.0 | 1.32 | 1.32 | +9.1 | +6.0 |
| `tdi_rsi_gt_signal` | 6 | R_REPEATER | 33.3% | 66.7% | 66.7% | 0.0% | +4.0 | 5.10 | 2.55 | +8.2 | +5.2 |
| `tdi_rsi_gte_50` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 5.6% | +1.0 | 1.32 | 1.32 | +9.1 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -18.3 | 0.00 | 0.00 | +0.1 | +18.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 94.4% | 47.1% | 47.1% | 5.9% | +0.8 | 1.25 | 1.41 | +8.8 | +6.2 |
| `feature_stale_hod_exhaustion_reject` | 15 | R_REPEATER | 83.3% | 53.3% | 53.3% | 6.7% | +2.5 | 2.08 | 1.82 | +9.9 | +5.1 |
| `feature_momentum_breakout_exception` | 5 | R_REPEATER | 27.8% | 60.0% | 60.0% | 0.0% | -0.3 | 0.93 | 0.62 | +8.3 | +8.0 |
| `feature_eurjpy_tdi50_reclaim` | 7 | R_REPEATER | 38.9% | 57.1% | 57.1% | 0.0% | -0.7 | 0.84 | 0.63 | +9.2 | +7.2 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+0.2; validation N=2 Fav=50.0% Avg=-0.6; out_of_sample N=14 Fav=50.0% Avg=+7.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 28.6% | +4.8 | 3.43 | 3.43 | +11.1 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 76.2% | 43.8% | 43.8% | 25.0% | +5.4 | 3.27 | 3.74 | +11.9 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 90.5% | 47.4% | 47.4% | 26.3% | +5.0 | 3.40 | 3.40 | +11.4 | +4.6 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 28.6% | +4.8 | 3.43 | 3.43 | +11.1 | +4.3 |
| `asian_range_gte_30` | 6 | S_STRANGER | 28.6% | 33.3% | 33.3% | 16.7% | +1.9 | 1.67 | 3.35 | +10.2 | +5.2 |
| `confluence_gte_60` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 28.6% | +4.8 | 3.43 | 3.43 | +11.1 | +4.3 |
| `confluence_gte_70` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 28.6% | +4.8 | 3.43 | 3.43 | +11.1 | +4.3 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 52.4% | 45.5% | 45.5% | 18.2% | +0.8 | 1.44 | 1.72 | +7.6 | +4.7 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 57.1% | 33.3% | 33.3% | 0.0% | +0.3 | 1.12 | 2.24 | +7.7 | +6.1 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 28.6% | 33.3% | 33.3% | 16.7% | +1.9 | 1.67 | 3.35 | +10.2 | +5.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +1.4 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 28.6% | +4.8 | 3.43 | 3.43 | +11.1 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 28.6% | +4.8 | 3.43 | 3.43 | +11.1 | +4.3 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +2.8 | +3.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 4.8% | 100.0% | 100.0% | 0.0% | +10.1 | 999.00 | 999.00 | +10.7 | +7.0 |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=57.1% Avg=+6.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 45.0% | 45.0% | 5.0% | +4.3 | 3.20 | 3.56 | +14.9 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 100.0% | 45.0% | 45.0% | 5.0% | +4.3 | 3.20 | 3.56 | +14.9 | +7.3 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 45.0% | 45.0% | 5.0% | +4.3 | 3.20 | 3.56 | +14.9 | +7.3 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 45.0% | 45.0% | 5.0% | +4.3 | 3.20 | 3.56 | +14.9 | +7.3 |
| `asian_range_gte_30` | 8 | R_REPEATER | 40.0% | 50.0% | 50.0% | 12.5% | +5.6 | 3.45 | 3.45 | +17.5 | +8.8 |
| `confluence_gte_60` | 13 | S_STRANGER | 65.0% | 46.2% | 46.2% | 7.7% | +5.0 | 3.82 | 3.82 | +16.0 | +7.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | R_REPEATER | 35.0% | 57.1% | 57.1% | 0.0% | +6.8 | 3.86 | 2.89 | +17.3 | +9.3 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 95.0% | 42.1% | 42.1% | 0.0% | +4.2 | 3.00 | 3.75 | +14.6 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 8 | R_REPEATER | 40.0% | 50.0% | 50.0% | 12.5% | +5.6 | 3.45 | 3.45 | +17.5 | +8.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 30.0% | 50.0% | 50.0% | 0.0% | +6.4 | 3.30 | 3.30 | +17.7 | +10.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 45.0% | 45.0% | 5.0% | +4.3 | 3.20 | 3.56 | +14.9 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 95.0% | 47.4% | 47.4% | 5.3% | +4.7 | 3.41 | 3.41 | +15.0 | +7.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -10.8 | 0.00 | 0.00 | +0.1 | +18.7 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 25.0% | 20.0% | 20.0% | 0.0% | -1.5 | 0.56 | 2.23 | +10.9 | +7.6 |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=66.7% Avg=+12.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 43.8% | 50.0% | 12.5% | +7.1 | 3.22 | 2.81 | +16.9 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 81.2% | 38.5% | 46.2% | 15.4% | +8.0 | 3.99 | 3.99 | +17.1 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 43.8% | 50.0% | 12.5% | +7.1 | 3.22 | 2.81 | +16.9 | +7.2 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 43.8% | 50.0% | 12.5% | +7.1 | 3.22 | 2.81 | +16.9 | +7.2 |
| `asian_range_gte_30` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +9.0 | +4.8 |
| `confluence_gte_60` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +5.8 | +12.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 37.5% | 33.3% | 33.3% | 16.7% | +3.8 | 1.97 | 2.96 | +13.3 | +7.9 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 81.2% | 46.2% | 46.2% | 7.7% | +5.5 | 2.61 | 2.61 | +15.7 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +9.0 | +4.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 93.8% | 40.0% | 46.7% | 13.3% | +6.7 | 2.96 | 2.96 | +16.3 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 75.0% | 25.0% | 33.3% | 16.7% | +2.5 | 1.59 | 2.78 | +13.1 | +8.6 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 25.0% | 25.0% | 25.0% | 50.0% | +8.9 | 3.63 | 7.26 | +20.0 | +6.6 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 37.5% | 66.7% | 66.7% | 16.7% | +12.9 | 13.72 | 3.43 | +22.1 | +4.6 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=14 Fav=50.0% Avg=+3.7; validation N=14 Fav=35.7% Avg=+1.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 25.0% | +2.7 | 2.24 | 2.80 | +9.6 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 78.6% | 40.9% | 40.9% | 22.7% | +2.7 | 2.65 | 3.54 | +9.1 | +4.1 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 96.4% | 40.7% | 40.7% | 22.2% | +1.9 | 1.84 | 2.51 | +8.6 | +4.4 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 25.0% | +2.7 | 2.24 | 2.80 | +9.6 | +4.3 |
| `asian_range_gte_30` | 5 | S_STRANGER | 17.9% | 40.0% | 40.0% | 20.0% | +1.7 | 2.45 | 3.68 | +9.7 | +3.3 |
| `confluence_gte_60` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 25.0% | +2.7 | 2.24 | 2.80 | +9.6 | +4.3 |
| `confluence_gte_70` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 25.0% | +2.7 | 2.24 | 2.80 | +9.6 | +4.3 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 25.0% | 28.6% | 28.6% | 14.3% | -2.2 | 0.33 | 0.67 | +7.1 | +5.6 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 85.7% | 37.5% | 37.5% | 16.7% | +2.3 | 2.03 | 3.16 | +9.8 | +4.5 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 17.9% | 40.0% | 40.0% | 20.0% | +1.7 | 2.45 | 3.68 | +9.7 | +3.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 3.6% | 0.0% | 0.0% | 0.0% | -0.3 | 0.00 | 0.00 | +9.9 | +2.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 25.0% | +2.7 | 2.24 | 2.80 | +9.6 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 25.0% | +2.7 | 2.24 | 2.80 | +9.6 | +4.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+7.5; validation N=6 Fav=50.0% Avg=+2.9; out_of_sample N=1 Fav=0.0% Avg=-15.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +3.3 | 1.94 | 2.71 | +11.9 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +3.3 | 1.94 | 2.71 | +11.9 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +3.3 | 1.94 | 2.71 | +11.9 | +6.3 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +3.3 | 1.94 | 2.71 | +11.9 | +6.3 |
| `asian_range_gte_30` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 0.0% | -1.9 | 0.32 | 0.97 | +3.4 | +6.4 |
| `confluence_gte_60` | 5 | S_STRANGER | 41.7% | 40.0% | 40.0% | 40.0% | +4.3 | 3.15 | 4.72 | +9.4 | +5.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 33.3% | +1.1 | 1.25 | 2.49 | +8.1 | +8.4 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 28.6% | +0.8 | 1.20 | 3.00 | +7.5 | +7.5 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 0.0% | -1.9 | 0.32 | 0.97 | +3.4 | +6.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -2.1 | 0.00 | 0.00 | +1.5 | +5.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +3.3 | 1.94 | 2.71 | +11.9 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +3.3 | 1.94 | 2.71 | +11.9 | +6.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-12.0; validation N=5 Fav=60.0% Avg=+3.6; out_of_sample N=4 Fav=50.0% Avg=+6.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +2.3 | 2.15 | 3.00 | +8.7 | +4.2 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 30.0% | 30.0% | 10.0% | -0.5 | 0.79 | 1.85 | +5.9 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 36.4% | 36.4% | 18.2% | -0.2 | 0.93 | 1.63 | +5.8 | +4.2 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +2.3 | 2.15 | 3.00 | +8.7 | +4.2 |
| `asian_range_gte_30` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +1.4 | +7.8 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +2.3 | 2.15 | 3.00 | +8.7 | +4.2 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +2.3 | 2.15 | 3.00 | +8.7 | +4.2 |
| `tdi_rsi_gt_signal` | 10 | R_REPEATER | 83.3% | 50.0% | 50.0% | 30.0% | +3.0 | 2.43 | 2.43 | +9.8 | +3.9 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 83.3% | 30.0% | 30.0% | 10.0% | +1.2 | 1.49 | 3.48 | +8.7 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +1.4 | +7.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +2.3 | 2.15 | 3.00 | +8.7 | +4.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 25.0% | +2.3 | 2.15 | 3.00 | +8.7 | +4.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=66.7% Avg=+4.9; validation N=8 Fav=25.0% Avg=+0.3; out_of_sample N=1 Fav=100.0% Avg=+4.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +1.8 | 2.33 | 3.27 | +6.1 | +3.4 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +1.8 | 2.33 | 3.27 | +6.1 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +1.8 | 2.33 | 3.27 | +6.1 | +3.4 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +1.8 | 2.33 | 3.27 | +6.1 | +3.4 |
| `asian_range_gte_30` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 0.0% | +4.5 | 4.24 | 2.12 | +11.3 | +2.6 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +1.8 | 2.33 | 3.27 | +6.1 | +3.4 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +1.8 | 2.33 | 3.27 | +6.1 | +3.4 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 0.0% | -0.0 | 0.98 | 2.44 | +5.2 | +3.1 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 75.0% | 33.3% | 33.3% | 0.0% | +0.9 | 1.55 | 3.10 | +5.4 | +3.5 |
| `ratio_le_2_and_asian_gte_30` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 0.0% | +4.5 | 4.24 | 2.12 | +11.3 | +2.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 0.0% | +1.5 | 1.71 | 1.71 | +9.9 | +2.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +1.8 | 2.33 | 3.27 | +6.1 | +3.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +1.8 | 2.33 | 3.27 | +6.1 | +3.4 |
| `feature_momentum_breakout_exception` | 2 | R_RUNNER | 16.7% | 100.0% | 100.0% | 0.0% | +8.9 | 999.00 | 999.00 | +14.7 | +1.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 0.0% | +7.2 | 999.00 | 999.00 | +15.2 | +0.0 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=50.0% Avg=-0.0; validation N=1 Fav=100.0% Avg=+29.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 33.3% | +1.0 | 1.28 | 1.54 | +10.0 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 4 | R_REPEATER | 33.3% | 50.0% | 50.0% | 25.0% | +6.5 | 4.42 | 4.42 | +15.0 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 25.0% | +2.0 | 1.83 | 2.44 | +11.2 | +4.7 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 33.3% | +1.0 | 1.28 | 1.54 | +10.0 | +5.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 33.3% | +1.0 | 1.28 | 1.54 | +10.0 | +5.3 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 33.3% | +1.0 | 1.28 | 1.54 | +10.0 | +5.3 |
| `tdi_rsi_gt_signal` | 9 | R_REPEATER | 75.0% | 55.6% | 55.6% | 44.4% | +3.3 | 2.23 | 1.34 | +11.8 | +4.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 28.6% | +2.3 | 1.70 | 2.26 | +9.9 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 33.3% | +1.0 | 1.28 | 1.54 | +10.0 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 33.3% | +1.0 | 1.28 | 1.54 | +10.0 | +5.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=0.0% Avg=-6.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=16 Fav=50.0% Avg=+8.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +5.8 | 3.93 | 5.41 | +13.8 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 60.0% | 25.0% | 25.0% | 8.3% | -0.9 | 0.68 | 1.81 | +8.4 | +5.8 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 95.0% | 42.1% | 42.1% | 10.5% | +6.1 | 3.98 | 4.98 | +14.3 | +6.2 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +5.8 | 3.93 | 5.41 | +13.8 | +6.3 |
| `asian_range_gte_30` | 9 | S_STRANGER | 45.0% | 22.2% | 22.2% | 11.1% | -2.0 | 0.41 | 1.24 | +6.8 | +7.2 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +5.8 | 3.93 | 5.41 | +13.8 | +6.3 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +5.8 | 3.93 | 5.41 | +13.8 | +6.3 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 30.0% | 33.3% | 33.3% | 16.7% | +16.8 | 15.78 | 31.56 | +24.2 | +7.3 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 80.0% | 31.2% | 31.2% | 6.2% | +5.9 | 3.41 | 6.81 | +13.9 | +7.1 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 45.0% | 22.2% | 22.2% | 11.1% | -2.0 | 0.41 | 1.24 | +6.8 | +7.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -0.6 | 0.00 | 0.00 | +3.5 | +1.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +5.8 | 3.93 | 5.41 | +13.8 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +5.8 | 3.93 | 5.41 | +13.8 | +6.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=50.0% Avg=-1.1; out_of_sample N=2 Fav=100.0% Avg=+9.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 6.7% | +0.7 | 1.36 | 2.03 | +5.9 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 0.0% | -4.7 | 0.02 | 0.04 | +3.7 | +6.0 |
| `hunt_to_ar_ratio_le_2_5` | 6 | R_REPEATER | 40.0% | 66.7% | 66.7% | 16.7% | +2.4 | 2.02 | 1.01 | +7.1 | +3.8 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 6.7% | +0.7 | 1.36 | 2.03 | +5.9 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 6.7% | +0.7 | 1.36 | 2.03 | +5.9 | +4.1 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 6.7% | +0.7 | 1.36 | 2.03 | +5.9 | +4.1 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -0.8 | 0.00 | 0.00 | +4.3 | +1.7 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 66.7% | 40.0% | 40.0% | 0.0% | +1.0 | 1.70 | 2.55 | +7.2 | +3.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 86.7% | 46.2% | 46.2% | 7.7% | +1.2 | 1.66 | 1.94 | +6.4 | +4.2 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 86.7% | 46.2% | 46.2% | 7.7% | +1.2 | 1.66 | 1.94 | +6.4 | +4.2 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +2.8 | +3.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +2.8 | +3.4 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=75.0% Avg=+9.2; validation N=2 Fav=0.0% Avg=-7.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +0.3 | 1.08 | 1.27 | +6.6 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 93.3% | 42.9% | 42.9% | 21.4% | +0.4 | 1.11 | 1.11 | +6.7 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +0.3 | 1.08 | 1.27 | +6.6 | +7.2 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +0.3 | 1.08 | 1.27 | +6.6 | +7.2 |
| `asian_range_gte_30` | 6 | R_REPEATER | 40.0% | 50.0% | 50.0% | 16.7% | +3.8 | 2.32 | 1.55 | +10.0 | +7.8 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +0.3 | 1.08 | 1.27 | +6.6 | +7.2 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +0.3 | 1.08 | 1.27 | +6.6 | +7.2 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 26.7% | 50.0% | 50.0% | 0.0% | +0.1 | 1.01 | 1.01 | +7.4 | +8.0 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 66.7% | 30.0% | 30.0% | 0.0% | -0.7 | 0.86 | 1.71 | +6.9 | +9.8 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 40.0% | 50.0% | 50.0% | 16.7% | +3.8 | 2.32 | 1.55 | +10.0 | +7.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 0.0% | +0.2 | 1.02 | 1.02 | +9.3 | +10.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +0.3 | 1.08 | 1.27 | +6.6 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +0.3 | 1.08 | 1.27 | +6.6 | +7.2 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 0.0% | +1.5 | 1.47 | 2.94 | +7.8 | +9.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 0.0% | +1.5 | 1.47 | 2.94 | +7.8 | +9.2 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-2.7; validation N=7 Fav=57.1% Avg=+1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 50.0% | +0.1 | 1.06 | 1.06 | +7.4 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 33.3% | -2.0 | 0.18 | 0.55 | +4.8 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 33.3% | -2.0 | 0.18 | 0.55 | +4.8 | +4.5 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 50.0% | +0.1 | 1.06 | 1.06 | +7.4 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 50.0% | +0.4 | 1.16 | 1.16 | +8.0 | +3.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 37.5% | -1.0 | 0.63 | 1.25 | +7.4 | +4.3 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | +0.0 | 0.00 | 0.00 | +12.0 | +3.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 55.6% | +0.8 | 1.48 | 1.11 | +8.2 | +3.5 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 50.0% | +0.1 | 1.06 | 1.06 | +7.4 | +3.8 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | -0.6 | 0.80 | 0.80 | +6.2 | +3.3 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+1.2; validation N=3 Fav=66.7% Avg=+9.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -0.8 | 0.87 | 1.31 | +10.1 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 0.0% | -3.9 | 0.55 | 1.10 | +11.0 | +3.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -0.8 | 0.87 | 1.31 | +10.1 | +3.3 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -0.8 | 0.87 | 1.31 | +10.1 | +3.3 |
| `asian_range_gte_30` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | -14.4 | 0.14 | 0.27 | +9.3 | +2.4 |
| `confluence_gte_60` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 0.0% | +0.6 | 1.32 | 2.63 | +6.6 | +3.0 |
| `confluence_gte_70` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +4.6 | +2.6 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 14.3% | +2.0 | 1.42 | 1.90 | +11.5 | +3.7 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 0.0% | +5.2 | 7.72 | 7.72 | +10.4 | +3.7 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | -14.4 | 0.14 | 0.27 | +9.3 | +2.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | -10.4 | 0.25 | 0.25 | +9.8 | +2.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -0.8 | 0.87 | 1.31 | +10.1 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | -0.8 | 0.87 | 1.31 | +10.1 | +3.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+3.3; validation N=4 Fav=75.0% Avg=+18.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 39.1% | 43.5% | 17.4% | +1.4 | 1.27 | 1.65 | +12.3 | +4.7 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 91.3% | 38.1% | 42.9% | 14.3% | +0.8 | 1.14 | 1.52 | +12.2 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 95.7% | 36.4% | 40.9% | 13.6% | +0.8 | 1.14 | 1.65 | +12.0 | +4.8 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 39.1% | 43.5% | 17.4% | +1.4 | 1.27 | 1.65 | +12.3 | +4.7 |
| `asian_range_gte_30` | 8 | S_STRANGER | 34.8% | 25.0% | 25.0% | 12.5% | -7.3 | 0.29 | 0.87 | +11.3 | +3.4 |
| `confluence_gte_60` | 3 | R_REPEATER | 13.0% | 66.7% | 66.7% | 0.0% | +2.3 | 70.00 | 35.00 | +18.5 | +5.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 16 | R_REPEATER | 69.6% | 50.0% | 50.0% | 18.8% | +5.8 | 3.80 | 3.80 | +15.3 | +4.4 |
| `tdi_rsi_gte_50` | 9 | R_REPEATER | 39.1% | 66.7% | 66.7% | 11.1% | +10.0 | 26.83 | 13.41 | +19.2 | +5.7 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 34.8% | 25.0% | 25.0% | 12.5% | -7.3 | 0.29 | 0.87 | +11.3 | +3.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 26.1% | 33.3% | 33.3% | 16.7% | +1.1 | 1.36 | 2.73 | +14.5 | +2.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 39.1% | 43.5% | 17.4% | +1.4 | 1.27 | 1.65 | +12.3 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 39.1% | 43.5% | 17.4% | +1.4 | 1.27 | 1.65 | +12.3 | +4.7 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 21.7% | 20.0% | 20.0% | 0.0% | -3.3 | 0.27 | 1.06 | +6.1 | +4.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 8.7% | 50.0% | 50.0% | 0.0% | +3.0 | 60.00 | 60.00 | +16.4 | +3.4 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=42.9% Avg=+2.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +2.7 | 3.00 | 4.20 | +11.3 | +3.6 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 41.7% | 41.7% | 16.7% | +3.3 | 4.12 | 4.94 | +10.8 | +3.1 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +2.7 | 3.00 | 4.20 | +11.3 | +3.6 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +2.7 | 3.00 | 4.20 | +11.3 | +3.6 |
| `asian_range_gte_30` | 7 | S_STRANGER | 53.8% | 28.6% | 28.6% | 14.3% | +3.2 | 3.14 | 7.86 | +11.1 | +4.1 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +2.7 | 3.00 | 4.20 | +11.3 | +3.6 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +2.7 | 3.00 | 4.20 | +11.3 | +3.6 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 0.0% | +3.5 | 7.93 | 15.87 | +11.5 | +4.1 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 9.1% | +2.7 | 3.08 | 4.62 | +11.5 | +3.5 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 46.2% | 33.3% | 33.3% | 16.7% | +4.5 | 5.74 | 11.47 | +9.9 | +3.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 0.0% | +5.7 | 23.80 | 23.80 | +11.1 | +3.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +2.7 | 3.00 | 4.20 | +11.3 | +3.6 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +2.7 | 3.00 | 4.20 | +11.3 | +3.6 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 53.8% | 42.9% | 42.9% | 14.3% | +2.4 | 3.10 | 4.13 | +9.9 | +3.6 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 46.2% | 33.3% | 33.3% | 0.0% | +1.4 | 2.04 | 4.07 | +8.8 | +3.9 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=66.7% Avg=+13.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=50.0% Avg=+2.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 18.8% | +2.7 | 2.58 | 3.86 | +9.8 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 75.0% | 41.7% | 41.7% | 16.7% | +3.6 | 2.71 | 3.80 | +10.8 | +3.9 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 18.8% | +2.7 | 2.58 | 3.86 | +9.8 | +3.7 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 18.8% | +2.7 | 2.58 | 3.86 | +9.8 | +3.7 |
| `asian_range_gte_30` | 5 | R_REPEATER | 31.2% | 60.0% | 60.0% | 0.0% | +9.1 | 29.38 | 19.58 | +13.7 | +2.2 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 18.8% | +2.7 | 2.58 | 3.86 | +9.8 | +3.7 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 18.8% | +2.7 | 2.58 | 3.86 | +9.8 | +3.7 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 18.8% | 33.3% | 33.3% | 0.0% | +3.3 | 7.13 | 14.25 | +8.9 | +2.7 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 75.0% | 41.7% | 41.7% | 16.7% | +3.6 | 3.95 | 4.74 | +10.4 | +3.4 |
| `ratio_le_2_and_asian_gte_30` | 5 | R_REPEATER | 31.2% | 60.0% | 60.0% | 0.0% | +9.1 | 29.38 | 19.58 | +13.7 | +2.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 6.2% | 100.0% | 100.0% | 0.0% | +11.4 | 999.00 | 999.00 | +14.7 | +0.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 93.8% | 33.3% | 33.3% | 20.0% | +2.8 | 2.55 | 4.60 | +10.0 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 18.8% | +2.7 | 2.58 | 3.86 | +9.8 | +3.7 |
| `feature_momentum_breakout_exception` | 3 | R_REPEATER | 18.8% | 66.7% | 66.7% | 0.0% | +3.3 | 6.00 | 3.00 | +8.2 | +2.1 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_RUNNER | 18.8% | 100.0% | 100.0% | 0.0% | +13.9 | 999.00 | 999.00 | +17.3 | +1.0 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+4.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 43 | S_STRANGER | 100.0% | 37.2% | 37.2% | 32.6% | +2.8 | 2.34 | 3.22 | +9.6 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 42 | S_STRANGER | 97.7% | 38.1% | 38.1% | 33.3% | +2.9 | 2.37 | 3.11 | +9.8 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 42 | S_STRANGER | 97.7% | 38.1% | 38.1% | 33.3% | +2.9 | 2.37 | 3.11 | +9.8 | +4.8 |
| `stop_hunt_le_90` | 43 | S_STRANGER | 100.0% | 37.2% | 37.2% | 32.6% | +2.8 | 2.34 | 3.22 | +9.6 | +4.9 |
| `asian_range_gte_30` | 13 | S_STRANGER | 30.2% | 46.2% | 46.2% | 38.5% | +4.9 | 3.09 | 3.60 | +11.9 | +5.7 |
| `confluence_gte_60` | 33 | S_STRANGER | 76.7% | 33.3% | 33.3% | 39.4% | +2.4 | 1.98 | 3.42 | +9.5 | +5.3 |
| `confluence_gte_70` | 1 | R_RUNNER | 2.3% | 100.0% | 100.0% | 0.0% | +30.7 | 999.00 | 999.00 | +30.9 | +0.9 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 37.2% | 37.5% | 37.5% | 31.2% | +0.2 | 1.05 | 1.40 | +8.0 | +6.0 |
| `tdi_rsi_gte_50` | 14 | R_REPEATER | 32.6% | 50.0% | 50.0% | 14.3% | +6.1 | 3.53 | 2.52 | +12.1 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 30.2% | 46.2% | 46.2% | 38.5% | +4.9 | 3.09 | 3.60 | +11.9 | +5.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 18.6% | 37.5% | 37.5% | 37.5% | -0.1 | 0.97 | 1.62 | +7.9 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 43 | S_STRANGER | 100.0% | 37.2% | 37.2% | 32.6% | +2.8 | 2.34 | 3.22 | +9.6 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 43 | S_STRANGER | 100.0% | 37.2% | 37.2% | 32.6% | +2.8 | 2.34 | 3.22 | +9.6 | +4.9 |
| `feature_momentum_breakout_exception` | 23 | S_STRANGER | 53.5% | 34.8% | 34.8% | 34.8% | +1.7 | 2.17 | 3.25 | +7.9 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 14.0% | 50.0% | 50.0% | 16.7% | +4.8 | 7.30 | 4.87 | +8.8 | +4.0 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=15 Fav=40.0% Avg=+1.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 36.7% | 36.7% | 23.3% | +1.4 | 2.17 | 3.16 | +7.4 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 29 | S_STRANGER | 96.7% | 37.9% | 37.9% | 24.1% | +1.5 | 2.22 | 3.03 | +7.5 | +3.7 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 96.7% | 37.9% | 37.9% | 24.1% | +1.5 | 2.22 | 3.03 | +7.5 | +3.7 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 36.7% | 36.7% | 23.3% | +1.4 | 2.17 | 3.16 | +7.4 | +3.7 |
| `asian_range_gte_30` | 7 | S_STRANGER | 23.3% | 28.6% | 28.6% | 42.9% | +1.3 | 1.80 | 3.60 | +6.8 | +2.9 |
| `confluence_gte_60` | 30 | S_STRANGER | 100.0% | 36.7% | 36.7% | 23.3% | +1.4 | 2.17 | 3.16 | +7.4 | +3.7 |
| `confluence_gte_70` | 30 | S_STRANGER | 100.0% | 36.7% | 36.7% | 23.3% | +1.4 | 2.17 | 3.16 | +7.4 | +3.7 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 50.0% | 40.0% | 40.0% | 13.3% | +1.5 | 2.50 | 3.33 | +8.3 | +3.3 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 63.3% | 36.8% | 36.8% | 5.3% | +1.0 | 1.83 | 2.87 | +7.8 | +4.2 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 23.3% | 28.6% | 28.6% | 42.9% | +1.3 | 1.80 | 3.60 | +6.8 | +2.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +7.1 | +3.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 100.0% | 36.7% | 36.7% | 23.3% | +1.4 | 2.17 | 3.16 | +7.4 | +3.7 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 36.7% | 36.7% | 23.3% | +1.4 | 2.17 | 3.16 | +7.4 | +3.7 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +0.4 | +5.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=42.9% Avg=+5.6; validation N=1 Fav=100.0% Avg=+23.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 27.3% | +4.0 | 1.93 | 3.38 | +12.5 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 40.0% | +5.8 | 2.04 | 3.06 | +16.1 | +6.9 |
| `hunt_to_ar_ratio_le_2_5` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 50.0% | +9.4 | 3.02 | 3.02 | +18.6 | +6.3 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 27.3% | +4.0 | 1.93 | 3.38 | +12.5 | +6.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 25.0% | +0.1 | 1.02 | 3.07 | +11.0 | +8.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -5.1 | 0.00 | 0.00 | +3.9 | +7.0 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 27.3% | +4.0 | 1.93 | 3.38 | +12.5 | +6.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 25.0% | +1.9 | 1.37 | 4.12 | +11.0 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 8 | R_REPEATER | 72.7% | 50.0% | 50.0% | 37.5% | +7.8 | 3.21 | 3.21 | +15.4 | +6.4 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 28.6% | +6.0 | 2.65 | 3.53 | +13.4 | +5.6 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 28.6% | +6.0 | 2.65 | 3.53 | +13.4 | +5.6 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=100.0% Avg=+14.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=33.3% Avg=+2.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 45.5% | +2.1 | 1.62 | 2.43 | +11.8 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 50.0% | +5.8 | 3.14 | 4.71 | +13.8 | +5.7 |
| `asian_range_gte_30` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 100.0% | +5.9 | 999.00 | 999.00 | +23.9 | +1.7 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 45.5% | +2.1 | 1.62 | 2.43 | +11.8 | +6.5 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 45.5% | +2.1 | 1.62 | 2.43 | +11.8 | +6.5 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 72.7% | 50.0% | 50.0% | 62.5% | +5.6 | 4.05 | 3.04 | +15.8 | +5.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 42.9% | +0.6 | 1.15 | 1.53 | +11.9 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 42.9% | +3.3 | 1.86 | 3.72 | +11.9 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 45.5% | +2.1 | 1.62 | 2.43 | +11.8 | +6.5 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 100.0% | +5.9 | 999.00 | 999.00 | +23.9 | +1.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 100.0% | +5.9 | 999.00 | 999.00 | +23.9 | +1.7 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=40.0% Avg=-2.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | -2.6 | 0.41 | 0.72 | +6.8 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 16.7% | -5.6 | 0.20 | 0.41 | +6.8 | +10.1 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 11.1% | -4.0 | 0.20 | 0.40 | +5.6 | +9.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | -2.6 | 0.41 | 0.72 | +6.8 | +8.8 |
| `asian_range_gte_30` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 20.0% | -2.9 | 0.38 | 0.56 | +8.0 | +7.3 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | -2.6 | 0.41 | 0.72 | +6.8 | +8.8 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | -2.6 | 0.41 | 0.72 | +6.8 | +8.8 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 54.5% | 16.7% | 16.7% | 0.0% | -4.9 | 0.27 | 1.37 | +4.8 | +10.7 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 0.0% | -6.1 | 0.01 | 0.06 | +4.3 | +10.9 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 20.0% | -2.9 | 0.38 | 0.56 | +8.0 | +7.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -9.2 | 0.00 | 0.00 | +5.5 | +11.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | -2.6 | 0.41 | 0.72 | +6.8 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 9.1% | -2.6 | 0.41 | 0.72 | +6.8 | +8.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=44.4% Avg=+2.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 33.3% | 33.3% | 7.4% | +0.1 | 1.02 | 2.04 | +12.0 | +7.8 |
| `hunt_to_ar_ratio_le_2_0` | 27 | S_STRANGER | 100.0% | 33.3% | 33.3% | 7.4% | +0.1 | 1.02 | 2.04 | +12.0 | +7.8 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 100.0% | 33.3% | 33.3% | 7.4% | +0.1 | 1.02 | 2.04 | +12.0 | +7.8 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 100.0% | 33.3% | 33.3% | 7.4% | +0.1 | 1.02 | 2.04 | +12.0 | +7.8 |
| `asian_range_gte_30` | 15 | S_STRANGER | 55.6% | 40.0% | 40.0% | 13.3% | +3.5 | 2.54 | 3.80 | +13.5 | +6.3 |
| `confluence_gte_60` | 12 | S_STRANGER | 44.4% | 41.7% | 41.7% | 0.0% | +1.5 | 1.78 | 2.49 | +12.3 | +6.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 55.6% | 26.7% | 26.7% | 6.7% | -2.0 | 0.62 | 1.71 | +9.0 | +9.5 |
| `tdi_rsi_gte_50` | 22 | S_STRANGER | 81.5% | 36.4% | 36.4% | 4.5% | -0.6 | 0.87 | 1.53 | +11.6 | +8.7 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 55.6% | 40.0% | 40.0% | 13.3% | +3.5 | 2.54 | 3.80 | +13.5 | +6.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 33.3% | 44.4% | 44.4% | 11.1% | +2.8 | 2.00 | 2.50 | +11.5 | +8.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 100.0% | 33.3% | 33.3% | 7.4% | +0.1 | 1.02 | 2.04 | +12.0 | +7.8 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 92.6% | 28.0% | 28.0% | 8.0% | -0.9 | 0.80 | 2.04 | +11.1 | +8.2 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 48.1% | 30.8% | 30.8% | 15.4% | +0.3 | 1.06 | 2.39 | +11.3 | +8.7 |
| `feature_eurjpy_tdi50_reclaim` | 12 | S_STRANGER | 44.4% | 33.3% | 33.3% | 8.3% | -0.5 | 0.90 | 1.81 | +10.5 | +9.1 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=66.7% Avg=+5.3; validation N=2 Fav=0.0% Avg=-3.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.3 | 0.92 | 1.60 | +8.7 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 40.0% | 40.0% | 40.0% | +0.5 | 1.18 | 1.48 | +9.3 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.3 | 0.92 | 1.60 | +8.7 | +5.2 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.3 | 0.92 | 1.60 | +8.7 | +5.2 |
| `asian_range_gte_30` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 33.3% | +0.3 | 1.12 | 2.23 | +8.9 | +5.7 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.3 | 0.92 | 1.60 | +8.7 | +5.2 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.3 | 0.92 | 1.60 | +8.7 | +5.2 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 22.2% | -2.7 | 0.32 | 0.95 | +7.9 | +6.4 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 0.0% | -4.3 | 0.22 | 0.89 | +8.4 | +8.2 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 41.7% | 40.0% | 40.0% | 40.0% | +1.9 | 1.88 | 2.82 | +9.6 | +4.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 33.3% | -1.6 | 0.51 | 1.01 | +8.3 | +6.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.3 | 0.92 | 1.60 | +8.7 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.3 | 0.92 | 1.60 | +8.7 | +5.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=-6.1; validation N=6 Fav=66.7% Avg=+4.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.6 | 0.82 | 1.18 | +7.8 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 81.0% | 35.3% | 35.3% | 23.5% | -0.9 | 0.71 | 1.07 | +6.9 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 95.2% | 35.0% | 35.0% | 30.0% | -0.6 | 0.82 | 1.18 | +7.6 | +4.8 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.6 | 0.82 | 1.18 | +7.8 | +5.2 |
| `asian_range_gte_30` | 8 | S_STRANGER | 38.1% | 37.5% | 37.5% | 12.5% | -0.3 | 0.89 | 1.19 | +8.6 | +4.9 |
| `confluence_gte_60` | 9 | R_REPEATER | 42.9% | 55.6% | 55.6% | 22.2% | +0.9 | 1.35 | 0.81 | +10.8 | +5.0 |
| `confluence_gte_70` | 1 | R_RUNNER | 4.8% | 100.0% | 100.0% | 0.0% | +6.8 | 999.00 | 999.00 | +13.0 | +8.0 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 85.7% | 33.3% | 33.3% | 33.3% | -0.5 | 0.84 | 1.26 | +8.0 | +5.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 33.3% | 42.9% | 42.9% | 14.3% | -1.3 | 0.61 | 0.61 | +9.7 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 38.1% | 37.5% | 37.5% | 12.5% | -0.3 | 0.89 | 1.19 | +8.6 | +4.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 33.3% | 28.6% | 28.6% | 14.3% | -1.3 | 0.60 | 1.20 | +8.0 | +4.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.6 | 0.82 | 1.18 | +7.8 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.6 | 0.82 | 1.18 | +7.8 | +5.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=75.0% Avg=+5.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 31.4% | 37.1% | 31.4% | +1.4 | 1.65 | 2.28 | +7.9 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 32 | S_STRANGER | 91.4% | 31.2% | 37.5% | 31.2% | +1.3 | 1.65 | 2.20 | +7.5 | +3.7 |
| `hunt_to_ar_ratio_le_2_5` | 33 | S_STRANGER | 94.3% | 30.3% | 36.4% | 30.3% | +1.3 | 1.65 | 2.33 | +7.7 | +3.8 |
| `stop_hunt_le_90` | 35 | S_STRANGER | 100.0% | 31.4% | 37.1% | 31.4% | +1.4 | 1.65 | 2.28 | +7.9 | +3.9 |
| `asian_range_gte_30` | 10 | R_REPEATER | 28.6% | 50.0% | 50.0% | 40.0% | +3.1 | 2.65 | 2.65 | +10.8 | +4.1 |
| `confluence_gte_60` | 26 | S_STRANGER | 74.3% | 19.2% | 26.9% | 26.9% | +0.2 | 1.08 | 2.31 | +6.7 | +4.3 |
| `confluence_gte_70` | 16 | S_STRANGER | 45.7% | 25.0% | 31.2% | 31.2% | +1.2 | 1.56 | 2.49 | +7.1 | +4.0 |
| `tdi_rsi_gt_signal` | 24 | S_STRANGER | 68.6% | 41.7% | 41.7% | 33.3% | +1.6 | 1.64 | 2.14 | +8.5 | +4.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 25.7% | 44.4% | 44.4% | 22.2% | +1.4 | 1.95 | 2.44 | +8.5 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 28.6% | 50.0% | 50.0% | 40.0% | +3.1 | 2.65 | 2.65 | +10.8 | +4.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 22.9% | 62.5% | 62.5% | 50.0% | +4.8 | 4.26 | 2.56 | +11.8 | +3.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 35 | S_STRANGER | 100.0% | 31.4% | 37.1% | 31.4% | +1.4 | 1.65 | 2.28 | +7.9 | +3.9 |
| `feature_stale_hod_exhaustion_reject` | 35 | S_STRANGER | 100.0% | 31.4% | 37.1% | 31.4% | +1.4 | 1.65 | 2.28 | +7.9 | +3.9 |
| `feature_momentum_breakout_exception` | 8 | R_RUNNER | 22.9% | 75.0% | 75.0% | 50.0% | +5.8 | 20.17 | 6.72 | +12.2 | +2.1 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_RUNNER | 11.4% | 75.0% | 75.0% | 25.0% | +5.0 | 200.00 | 66.67 | +12.5 | +2.2 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=-1.6; validation N=2 Fav=50.0% Avg=+6.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | -3.4 | 0.50 | 1.12 | +6.7 | +5.1 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 25.0% | -1.6 | 0.70 | 1.40 | +7.3 | +5.1 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | -3.4 | 0.50 | 1.12 | +6.7 | +5.1 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | -3.4 | 0.50 | 1.12 | +6.7 | +5.1 |
| `asian_range_gte_30` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 50.0% | +0.4 | 1.11 | 1.11 | +5.6 | +5.1 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | -3.4 | 0.50 | 1.12 | +6.7 | +5.1 |
| `confluence_gte_70` | 5 | S_STRANGER | 38.5% | 40.0% | 40.0% | 40.0% | +1.5 | 1.36 | 2.05 | +9.2 | +5.6 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 18.2% | 18.2% | 9.1% | -6.6 | 0.18 | 0.81 | +5.0 | +5.9 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 69.2% | 22.2% | 22.2% | 11.1% | -3.3 | 0.35 | 1.23 | +6.0 | +6.6 |
| `ratio_le_2_and_asian_gte_30` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 50.0% | +0.4 | 1.11 | 1.11 | +5.6 | +5.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 50.0% | +0.4 | 1.11 | 1.11 | +5.6 | +5.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | -3.4 | 0.50 | 1.12 | +6.7 | +5.1 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | -3.4 | 0.50 | 1.12 | +6.7 | +5.1 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -9.9 | 0.00 | 0.00 | +4.4 | +12.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -9.9 | 0.00 | 0.00 | +4.4 | +12.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=24 Fav=33.3% Avg=+1.7; validation N=19 Fav=31.6% Avg=+1.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 46 | S_STRANGER | 100.0% | 30.4% | 30.4% | 13.0% | +1.4 | 1.62 | 3.59 | +8.2 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 40 | S_STRANGER | 87.0% | 27.5% | 27.5% | 15.0% | +1.0 | 1.41 | 3.59 | +7.9 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 43 | S_STRANGER | 93.5% | 32.6% | 32.6% | 14.0% | +1.7 | 1.75 | 3.49 | +8.5 | +5.0 |
| `stop_hunt_le_90` | 46 | S_STRANGER | 100.0% | 30.4% | 30.4% | 13.0% | +1.4 | 1.62 | 3.59 | +8.2 | +5.0 |
| `asian_range_gte_30` | 8 | S_STRANGER | 17.4% | 12.5% | 12.5% | 0.0% | -2.2 | 0.50 | 3.51 | +3.9 | +8.3 |
| `confluence_gte_60` | 46 | S_STRANGER | 100.0% | 30.4% | 30.4% | 13.0% | +1.4 | 1.62 | 3.59 | +8.2 | +5.0 |
| `confluence_gte_70` | 46 | S_STRANGER | 100.0% | 30.4% | 30.4% | 13.0% | +1.4 | 1.62 | 3.59 | +8.2 | +5.0 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 41.3% | 10.5% | 10.5% | 10.5% | -1.8 | 0.43 | 3.41 | +6.4 | +5.8 |
| `tdi_rsi_gte_50` | 27 | S_STRANGER | 58.7% | 25.9% | 25.9% | 7.4% | +0.3 | 1.10 | 3.15 | +8.4 | +5.4 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 17.4% | 12.5% | 12.5% | 0.0% | -2.2 | 0.50 | 3.51 | +3.9 | +8.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 8.7% | 25.0% | 25.0% | 0.0% | -0.8 | 0.85 | 2.54 | +5.5 | +9.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 46 | S_STRANGER | 100.0% | 30.4% | 30.4% | 13.0% | +1.4 | 1.62 | 3.59 | +8.2 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 46 | S_STRANGER | 100.0% | 30.4% | 30.4% | 13.0% | +1.4 | 1.62 | 3.59 | +8.2 | +5.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+5.1; validation N=4 Fav=25.0% Avg=+1.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 50.0% | +3.8 | 2.11 | 3.51 | +10.9 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 50.0% | +3.8 | 2.11 | 3.51 | +10.9 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 50.0% | +3.8 | 2.11 | 3.51 | +10.9 | +5.6 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 50.0% | +3.8 | 2.11 | 3.51 | +10.9 | +5.6 |
| `asian_range_gte_30` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 50.0% | +4.4 | 1.90 | 3.81 | +14.0 | +7.5 |
| `confluence_gte_60` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 66.7% | +18.7 | 94.58 | 47.29 | +22.6 | +2.2 |
| `confluence_gte_70` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +19.2 | 999.00 | 999.00 | +22.2 | +0.8 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -7.2 | 0.00 | 0.00 | +1.4 | +9.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 33.3% | +1.5 | 1.32 | 5.26 | +9.5 | +7.0 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 50.0% | +4.4 | 1.90 | 3.81 | +14.0 | +7.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -14.4 | 0.00 | 0.00 | +0.6 | +16.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 50.0% | +3.8 | 2.11 | 3.51 | +10.9 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 50.0% | +3.8 | 2.11 | 3.51 | +10.9 | +5.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=+1.0; validation N=3 Fav=33.3% Avg=+1.3; out_of_sample N=1 Fav=100.0% Avg=+10.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +2.0 | 2.07 | 4.14 | +7.8 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +2.0 | 2.07 | 4.14 | +7.8 | +3.7 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +2.0 | 2.07 | 4.14 | +7.8 | +3.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +2.0 | 2.07 | 4.14 | +7.8 | +3.7 |
| `asian_range_gte_30` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +1.1 | 1.50 | 3.00 | +6.6 | +6.0 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +2.0 | 2.07 | 4.14 | +7.8 | +3.7 |
| `confluence_gte_70` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 33.3% | +1.1 | 1.53 | 4.58 | +7.0 | +3.9 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | +0.8 | 1.40 | 5.62 | +6.6 | +3.4 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | -0.9 | 0.75 | 3.02 | +4.9 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +1.1 | 1.50 | 3.00 | +6.6 | +6.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -6.7 | 0.00 | 0.00 | +0.3 | +9.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +2.0 | 2.07 | 4.14 | +7.8 | +3.7 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +2.0 | 2.07 | 4.14 | +7.8 | +3.7 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 33.3% | -0.5 | 0.84 | 3.37 | +6.5 | +4.3 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +1.6 | +7.7 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+5.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | +0.7 | 1.29 | 1.94 | +6.5 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 37.5% | +1.3 | 1.55 | 2.59 | +7.7 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | +0.7 | 1.29 | 1.94 | +6.5 | +4.4 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | +0.7 | 1.29 | 1.94 | +6.5 | +4.4 |
| `asian_range_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.4 | 0.00 | 0.00 | +1.9 | +4.5 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | +0.7 | 1.29 | 1.94 | +6.5 | +4.4 |
| `confluence_gte_70` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 60.0% | +5.0 | 8.84 | 5.90 | +10.2 | +2.5 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 25.0% | -0.8 | 0.71 | 2.14 | +6.1 | +5.2 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -7.3 | 0.00 | 0.00 | +4.3 | +10.5 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.4 | 0.00 | 0.00 | +1.9 | +4.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.4 | 0.00 | 0.00 | +1.9 | +4.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | +0.7 | 1.29 | 1.94 | +6.5 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | +0.7 | 1.29 | 1.94 | +6.5 | +4.4 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 50.0% | +4.3 | 6.21 | 6.21 | +7.9 | +2.9 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.8; validation N=10 Fav=50.0% Avg=+2.6; out_of_sample N=5 Fav=20.0% Avg=-3.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +0.1 | 1.04 | 2.26 | +6.6 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 85.0% | 29.4% | 29.4% | 11.8% | +0.1 | 1.04 | 2.29 | +6.8 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 95.0% | 31.6% | 31.6% | 10.5% | +0.3 | 1.10 | 2.20 | +7.0 | +4.7 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +0.1 | 1.04 | 2.26 | +6.6 | +5.0 |
| `asian_range_gte_30` | 3 | R_RUNNER | 15.0% | 100.0% | 100.0% | 33.3% | +10.1 | 999.00 | 999.00 | +12.3 | +1.0 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +0.1 | 1.04 | 2.26 | +6.6 | +5.0 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +0.1 | 1.04 | 2.26 | +6.6 | +5.0 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 50.0% | 30.0% | 30.0% | 0.0% | -1.5 | 0.63 | 1.47 | +4.9 | +6.6 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 80.0% | 37.5% | 37.5% | 6.2% | +0.3 | 1.11 | 1.84 | +7.0 | +5.6 |
| `ratio_le_2_and_asian_gte_30` | 3 | R_RUNNER | 15.0% | 100.0% | 100.0% | 33.3% | +10.1 | 999.00 | 999.00 | +12.3 | +1.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +7.4 | 999.00 | 999.00 | +8.2 | +1.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +0.1 | 1.04 | 2.26 | +6.6 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +0.1 | 1.04 | 2.26 | +6.6 | +5.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-8.1; validation N=1 Fav=100.0% Avg=+26.4; out_of_sample N=5 Fav=60.0% Avg=+6.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 30.0% | 33.3% | 20.0% | +0.1 | 1.02 | 1.94 | +6.7 | +4.5 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 86.7% | 30.8% | 34.6% | 19.2% | +0.2 | 1.05 | 1.87 | +7.0 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 96.7% | 31.0% | 34.5% | 20.7% | +0.1 | 1.03 | 1.86 | +6.8 | +4.6 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 30.0% | 33.3% | 20.0% | +0.1 | 1.02 | 1.94 | +6.7 | +4.5 |
| `asian_range_gte_30` | 13 | S_STRANGER | 43.3% | 46.2% | 53.8% | 30.8% | +1.6 | 1.39 | 0.99 | +8.2 | +4.4 |
| `confluence_gte_60` | 25 | S_STRANGER | 83.3% | 32.0% | 32.0% | 20.0% | +0.1 | 1.01 | 2.03 | +7.3 | +4.7 |
| `confluence_gte_70` | 9 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +1.1 | 1.23 | 2.46 | +8.5 | +4.5 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 63.3% | 36.8% | 42.1% | 21.1% | +2.5 | 1.94 | 2.43 | +8.0 | +4.1 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 23.3% | 57.1% | 57.1% | 28.6% | +6.9 | 4.40 | 3.30 | +10.8 | +5.4 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 43.3% | 46.2% | 53.8% | 30.8% | +1.6 | 1.39 | 0.99 | +8.2 | +4.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 26.7% | 50.0% | 62.5% | 25.0% | +3.8 | 2.65 | 1.06 | +9.2 | +4.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 100.0% | 30.0% | 33.3% | 20.0% | +0.1 | 1.02 | 1.94 | +6.7 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 30.0% | 33.3% | 20.0% | +0.1 | 1.02 | 1.94 | +6.7 | +4.5 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 16.7% | 20.0% | 40.0% | 20.0% | -0.7 | 0.67 | 1.00 | +2.7 | +5.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -8.1 | 0.00 | 0.00 | +2.4 | +9.8 |

### THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+13.4; validation N=2 Fav=50.0% Avg=+2.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 20.0% | -0.1 | 0.98 | 1.47 | +11.7 | +7.6 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 33.3% | 44.4% | 22.2% | +2.4 | 1.52 | 1.90 | +12.1 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 20.0% | -0.1 | 0.98 | 1.47 | +11.7 | +7.6 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 20.0% | -0.1 | 0.98 | 1.47 | +11.7 | +7.6 |
| `asian_range_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -15.3 | 0.00 | 0.00 | +2.3 | +4.1 |
| `confluence_gte_60` | 8 | S_STRANGER | 80.0% | 25.0% | 37.5% | 12.5% | -2.7 | 0.57 | 0.94 | +9.8 | +9.0 |
| `confluence_gte_70` | 7 | S_STRANGER | 70.0% | 28.6% | 42.9% | 14.3% | +0.2 | 1.06 | 1.41 | +10.1 | +6.6 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 25.0% | 50.0% | 25.0% | +2.8 | 1.44 | 1.44 | +11.0 | +4.9 |
| `tdi_rsi_gte_50` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 40.0% | +9.1 | 3.81 | 2.54 | +19.8 | +4.4 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -15.3 | 0.00 | 0.00 | +2.3 | +4.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -15.3 | 0.00 | 0.00 | +2.3 | +4.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 20.0% | -0.1 | 0.98 | 1.47 | +11.7 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 20.0% | -0.1 | 0.98 | 1.47 | +11.7 | +7.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+2.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -0.4 | 0.81 | 1.22 | +4.2 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -0.4 | 0.81 | 1.22 | +4.2 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -0.4 | 0.81 | 1.22 | +4.2 | +5.0 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -0.4 | 0.81 | 1.22 | +4.2 | +5.0 |
| `asian_range_gte_30` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 0.0% | +1.9 | 5.30 | 5.30 | +5.9 | +3.7 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -0.4 | 0.81 | 1.22 | +4.2 | +5.0 |
| `confluence_gte_70` | 4 | S_STRANGER | 40.0% | 0.0% | 25.0% | 0.0% | -3.8 | 0.09 | 0.27 | +1.6 | +7.0 |
| `tdi_rsi_gt_signal` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 0.0% | +2.1 | 3.57 | 2.38 | +6.9 | +5.2 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | +0.1 | 1.05 | 2.10 | +5.5 | +5.6 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 0.0% | +1.9 | 5.30 | 5.30 | +5.9 | +3.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_RUNNER | 40.0% | 75.0% | 75.0% | 0.0% | +3.3 | 14.30 | 4.77 | +7.9 | +3.6 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +2.8 | +11.4 |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -0.4 | 0.81 | 1.22 | +4.2 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -0.4 | 0.81 | 1.22 | +4.2 | +5.0 |
| `feature_momentum_breakout_exception` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 0.0% | -0.0 | 0.99 | 0.49 | +5.4 | +5.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | +0.6 | 1.40 | 1.40 | +4.4 | +6.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=37.5% Avg=-0.3; out_of_sample N=2 Fav=0.0% Avg=-5.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 0.0% | -1.3 | 0.56 | 1.31 | +4.7 | +6.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 0.0% | -1.4 | 0.56 | 1.69 | +4.9 | +6.2 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 0.0% | -1.4 | 0.56 | 1.69 | +4.9 | +6.2 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 0.0% | -1.3 | 0.56 | 1.31 | +4.7 | +6.0 |
| `asian_range_gte_30` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +10.2 | 999.00 | 999.00 | +12.6 | +4.8 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 0.0% | -1.3 | 0.56 | 1.31 | +4.7 | +6.0 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 0.0% | -1.3 | 0.56 | 1.31 | +4.7 | +6.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 0.0% | -1.3 | 0.59 | 1.76 | +5.2 | +6.6 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 0.0% | -1.3 | 0.56 | 1.31 | +4.7 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +10.2 | 999.00 | 999.00 | +12.6 | +4.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +10.2 | 999.00 | 999.00 | +12.6 | +4.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 0.0% | -1.3 | 0.56 | 1.31 | +4.7 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 0.0% | -1.3 | 0.56 | 1.31 | +4.7 | +6.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=-0.4; validation N=17 Fav=41.2% Avg=+4.3; out_of_sample N=5 Fav=0.0% Avg=-1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 29.6% | 37.0% | 29.6% | +2.3 | 3.16 | 4.74 | +8.5 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 81.5% | 31.8% | 36.4% | 31.8% | +3.2 | 4.73 | 7.09 | +9.1 | +3.2 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 92.6% | 32.0% | 40.0% | 32.0% | +2.5 | 3.25 | 4.22 | +8.5 | +3.4 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 100.0% | 29.6% | 37.0% | 29.6% | +2.3 | 3.16 | 4.74 | +8.5 | +3.3 |
| `asian_range_gte_30` | 14 | S_STRANGER | 51.9% | 28.6% | 28.6% | 35.7% | +2.4 | 3.07 | 6.15 | +8.0 | +3.9 |
| `confluence_gte_60` | 27 | S_STRANGER | 100.0% | 29.6% | 37.0% | 29.6% | +2.3 | 3.16 | 4.74 | +8.5 | +3.3 |
| `confluence_gte_70` | 27 | S_STRANGER | 100.0% | 29.6% | 37.0% | 29.6% | +2.3 | 3.16 | 4.74 | +8.5 | +3.3 |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 85.2% | 26.1% | 30.4% | 26.1% | +2.5 | 3.20 | 6.40 | +9.1 | +3.5 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 59.3% | 25.0% | 25.0% | 12.5% | +2.4 | 3.02 | 9.05 | +8.5 | +3.9 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 51.9% | 28.6% | 28.6% | 35.7% | +2.4 | 3.07 | 6.15 | +8.0 | +3.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 44.4% | 25.0% | 25.0% | 33.3% | +2.8 | 3.57 | 8.33 | +8.3 | +3.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 100.0% | 29.6% | 37.0% | 29.6% | +2.3 | 3.16 | 4.74 | +8.5 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 29.6% | 37.0% | 29.6% | +2.3 | 3.16 | 4.74 | +8.5 | +3.3 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 7.4% | 50.0% | 50.0% | 50.0% | +1.1 | 3.75 | 3.75 | +6.8 | +2.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.7% | 0.0% | 0.0% | 0.0% | -0.8 | 0.00 | 0.00 | +3.2 | +5.0 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=37.5% Avg=+3.7; validation N=5 Fav=40.0% Avg=-4.6; out_of_sample N=2 Fav=50.0% Avg=+2.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 41 | S_STRANGER | 100.0% | 29.3% | 31.7% | 26.8% | +1.3 | 1.37 | 2.54 | +9.6 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 38 | S_STRANGER | 92.7% | 28.9% | 31.6% | 26.3% | +1.3 | 1.36 | 2.50 | +10.0 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 41 | S_STRANGER | 100.0% | 29.3% | 31.7% | 26.8% | +1.3 | 1.37 | 2.54 | +9.6 | +6.6 |
| `stop_hunt_le_90` | 41 | S_STRANGER | 100.0% | 29.3% | 31.7% | 26.8% | +1.3 | 1.37 | 2.54 | +9.6 | +6.6 |
| `asian_range_gte_30` | 18 | S_STRANGER | 43.9% | 33.3% | 38.9% | 38.9% | +1.9 | 1.62 | 1.86 | +8.9 | +5.6 |
| `confluence_gte_60` | 38 | S_STRANGER | 92.7% | 28.9% | 31.6% | 26.3% | +0.7 | 1.22 | 2.23 | +9.1 | +6.2 |
| `confluence_gte_70` | 6 | S_STRANGER | 14.6% | 0.0% | 0.0% | 0.0% | -6.5 | 0.00 | 0.00 | +5.4 | +9.3 |
| `tdi_rsi_gt_signal` | 33 | S_STRANGER | 80.5% | 27.3% | 30.3% | 24.2% | +1.7 | 1.52 | 3.03 | +10.4 | +6.7 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 36.6% | 40.0% | 40.0% | 20.0% | +0.7 | 1.12 | 1.68 | +11.9 | +8.7 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 43.9% | 33.3% | 38.9% | 38.9% | +1.9 | 1.62 | 1.86 | +8.9 | +5.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 36.6% | 26.7% | 33.3% | 33.3% | +1.1 | 1.29 | 2.07 | +8.6 | +6.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 41 | S_STRANGER | 100.0% | 29.3% | 31.7% | 26.8% | +1.3 | 1.37 | 2.54 | +9.6 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 41 | S_STRANGER | 100.0% | 29.3% | 31.7% | 26.8% | +1.3 | 1.37 | 2.54 | +9.6 | +6.6 |
| `feature_momentum_breakout_exception` | 16 | S_STRANGER | 39.0% | 31.2% | 31.2% | 31.2% | +0.7 | 1.32 | 2.37 | +6.7 | +5.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 7.3% | 33.3% | 33.3% | 0.0% | -5.9 | 0.21 | 0.41 | +3.7 | +12.1 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=16 Fav=56.2% Avg=+7.2; validation N=21 Fav=23.8% Avg=+1.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 69 | S_STRANGER | 100.0% | 29.0% | 33.3% | 39.1% | +1.6 | 1.54 | 2.34 | +9.9 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 60 | S_STRANGER | 87.0% | 28.3% | 33.3% | 40.0% | +1.7 | 1.55 | 2.41 | +10.1 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 67 | S_STRANGER | 97.1% | 29.9% | 34.3% | 40.3% | +1.7 | 1.59 | 2.28 | +10.0 | +4.6 |
| `stop_hunt_le_90` | 69 | S_STRANGER | 100.0% | 29.0% | 33.3% | 39.1% | +1.6 | 1.54 | 2.34 | +9.9 | +4.6 |
| `asian_range_gte_30` | 21 | S_STRANGER | 30.4% | 23.8% | 28.6% | 38.1% | -0.6 | 0.82 | 1.64 | +7.2 | +4.4 |
| `confluence_gte_60` | 37 | S_STRANGER | 53.6% | 37.8% | 37.8% | 43.2% | +3.7 | 2.57 | 3.12 | +12.6 | +4.3 |
| `confluence_gte_70` | 1 | S_STRANGER | 1.4% | 0.0% | 0.0% | 0.0% | -8.8 | 0.00 | 0.00 | +7.3 | +15.2 |
| `tdi_rsi_gt_signal` | 38 | S_STRANGER | 55.1% | 34.2% | 36.8% | 39.5% | +2.7 | 1.83 | 2.61 | +11.1 | +4.1 |
| `tdi_rsi_gte_50` | 32 | S_STRANGER | 46.4% | 34.4% | 34.4% | 40.6% | +2.9 | 2.31 | 3.15 | +10.3 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 30.4% | 23.8% | 28.6% | 38.1% | -0.6 | 0.82 | 1.64 | +7.2 | +4.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 13.0% | 22.2% | 22.2% | 22.2% | -1.3 | 0.74 | 2.57 | +6.3 | +4.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 69 | S_STRANGER | 100.0% | 29.0% | 33.3% | 39.1% | +1.6 | 1.54 | 2.34 | +9.9 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 69 | S_STRANGER | 100.0% | 29.0% | 33.3% | 39.1% | +1.6 | 1.54 | 2.34 | +9.9 | +4.6 |
| `feature_momentum_breakout_exception` | 4 | R_RUNNER | 5.8% | 75.0% | 75.0% | 100.0% | +12.6 | 999.00 | 999.00 | +23.3 | +0.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 2.9% | 50.0% | 50.0% | 100.0% | +7.9 | 999.00 | 999.00 | +11.1 | +0.5 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=33.3% Avg=+1.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=28.6% Avg=+2.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +2.1 | 1.91 | 3.81 | +11.0 | +6.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 78.6% | 27.3% | 27.3% | 9.1% | +2.7 | 2.03 | 4.74 | +11.8 | +5.8 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +2.1 | 1.91 | 3.81 | +11.0 | +6.0 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +2.1 | 1.91 | 3.81 | +11.0 | +6.0 |
| `asian_range_gte_30` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 16.7% | +0.9 | 1.45 | 5.79 | +9.6 | +6.4 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +2.1 | 1.91 | 3.81 | +11.0 | +6.0 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +2.1 | 1.91 | 3.81 | +11.0 | +6.0 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | +0.0 | 0.00 | 0.00 | +9.8 | +3.8 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 92.9% | 30.8% | 30.8% | 15.4% | +2.3 | 1.96 | 3.42 | +10.9 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 16.7% | +0.9 | 1.45 | 5.79 | +9.6 | +6.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | +0.0 | 0.00 | 0.00 | +9.8 | +3.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +2.1 | 1.91 | 3.81 | +11.0 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +2.1 | 1.91 | 3.81 | +11.0 | +6.0 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 50.0% | +7.3 | 5.74 | 5.74 | +18.9 | +4.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 33.3% | +4.9 | 5.74 | 5.74 | +15.9 | +4.1 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=83.3% Avg=+14.4; validation N=1 Fav=0.0% Avg=-7.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +0.4 | 1.13 | 2.54 | +9.1 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 27 | S_STRANGER | 96.4% | 25.9% | 25.9% | 11.1% | -0.1 | 0.96 | 2.47 | +8.3 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 28 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +0.4 | 1.13 | 2.54 | +9.1 | +6.1 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +0.4 | 1.13 | 2.54 | +9.1 | +6.1 |
| `asian_range_gte_30` | 7 | R_REPEATER | 25.0% | 71.4% | 71.4% | 28.6% | +11.2 | 8.56 | 3.43 | +19.9 | +5.9 |
| `confluence_gte_60` | 28 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +0.4 | 1.13 | 2.54 | +9.1 | +6.1 |
| `confluence_gte_70` | 28 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +0.4 | 1.13 | 2.54 | +9.1 | +6.1 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 17.9% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +4.7 | +5.0 |
| `tdi_rsi_gte_50` | 25 | S_STRANGER | 89.3% | 28.0% | 28.0% | 12.0% | +0.8 | 1.29 | 2.96 | +9.7 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 21.4% | 66.7% | 66.7% | 16.7% | +10.7 | 7.16 | 3.58 | +18.5 | +6.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 3.6% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +4.3 | +4.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +0.4 | 1.13 | 2.54 | +9.1 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 92.9% | 30.8% | 30.8% | 15.4% | +0.7 | 1.24 | 2.47 | +9.5 | +6.1 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 25.0% | 28.6% | 28.6% | 14.3% | -0.0 | 0.98 | 1.97 | +9.5 | +6.6 |
| `feature_eurjpy_tdi50_reclaim` | 16 | S_STRANGER | 57.1% | 18.8% | 18.8% | 6.2% | -1.6 | 0.47 | 1.72 | +6.8 | +6.6 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+17.6; validation N=1 Fav=0.0% Avg=-0.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 28.0% | 28.0% | 16.0% | +2.0 | 1.65 | 4.00 | +7.7 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 76.0% | 36.8% | 36.8% | 15.8% | +3.1 | 1.85 | 3.18 | +9.4 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 100.0% | 28.0% | 28.0% | 16.0% | +2.0 | 1.65 | 4.00 | +7.7 | +6.2 |
| `stop_hunt_le_90` | 25 | S_STRANGER | 100.0% | 28.0% | 28.0% | 16.0% | +2.0 | 1.65 | 4.00 | +7.7 | +6.2 |
| `asian_range_gte_30` | 5 | S_STRANGER | 20.0% | 40.0% | 40.0% | 40.0% | +13.9 | 9.68 | 14.51 | +17.4 | +4.3 |
| `confluence_gte_60` | 15 | S_STRANGER | 60.0% | 26.7% | 26.7% | 13.3% | +3.0 | 1.86 | 5.11 | +9.1 | +6.5 |
| `confluence_gte_70` | 5 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -2.7 | 0.00 | 0.00 | +2.0 | +4.9 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 8.0% | 50.0% | 50.0% | 0.0% | -0.9 | 0.87 | 0.87 | +7.0 | +7.0 |
| `tdi_rsi_gte_50` | 22 | S_STRANGER | 88.0% | 27.3% | 27.3% | 9.1% | +2.1 | 1.64 | 4.37 | +7.8 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 20.0% | 40.0% | 40.0% | 40.0% | +13.9 | 9.68 | 14.51 | +17.4 | +4.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 84.0% | 33.3% | 33.3% | 14.3% | +2.6 | 1.72 | 3.43 | +8.6 | +6.9 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 28.0% | 28.0% | 16.0% | +2.0 | 1.65 | 4.00 | +7.7 | +6.2 |
| `feature_momentum_breakout_exception` | 15 | S_STRANGER | 60.0% | 20.0% | 20.0% | 13.3% | -0.8 | 0.71 | 2.62 | +5.1 | +6.0 |
| `feature_eurjpy_tdi50_reclaim` | 12 | S_STRANGER | 48.0% | 16.7% | 16.7% | 0.0% | -1.4 | 0.57 | 2.85 | +4.6 | +6.2 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=33.3% Avg=+2.3; validation N=5 Fav=40.0% Avg=+0.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 27.8% | 33.3% | 22.2% | +0.1 | 1.04 | 1.90 | +7.0 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 100.0% | 27.8% | 33.3% | 22.2% | +0.1 | 1.04 | 1.90 | +7.0 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 27.8% | 33.3% | 22.2% | +0.1 | 1.04 | 1.90 | +7.0 | +5.4 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 27.8% | 33.3% | 22.2% | +0.1 | 1.04 | 1.90 | +7.0 | +5.4 |
| `asian_range_gte_30` | 12 | S_STRANGER | 66.7% | 25.0% | 25.0% | 8.3% | -2.3 | 0.38 | 1.13 | +5.7 | +6.8 |
| `confluence_gte_60` | 14 | S_STRANGER | 77.8% | 35.7% | 42.9% | 21.4% | +1.6 | 1.74 | 2.32 | +8.3 | +4.6 |
| `confluence_gte_70` | 4 | R_REPEATER | 22.2% | 50.0% | 50.0% | 25.0% | +0.2 | 1.11 | 1.11 | +7.2 | +5.2 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 66.7% | 25.0% | 33.3% | 8.3% | -1.5 | 0.57 | 1.14 | +5.5 | +6.1 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 44.4% | 37.5% | 37.5% | 12.5% | -1.1 | 0.68 | 1.14 | +6.3 | +5.5 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 66.7% | 25.0% | 25.0% | 8.3% | -2.3 | 0.38 | 1.13 | +5.7 | +6.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 50.0% | 22.2% | 22.2% | 0.0% | -3.0 | 0.27 | 0.94 | +4.9 | +7.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 27.8% | 33.3% | 22.2% | +0.1 | 1.04 | 1.90 | +7.0 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 27.8% | 33.3% | 22.2% | +0.1 | 1.04 | 1.90 | +7.0 | +5.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=83.3% Avg=+12.2; validation N=1 Fav=0.0% Avg=-4.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 37.9% | +2.3 | 2.16 | 4.59 | +8.8 | +4.0 |
| `hunt_to_ar_ratio_le_2_0` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 37.9% | +2.3 | 2.16 | 4.59 | +8.8 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 37.9% | +2.3 | 2.16 | 4.59 | +8.8 | +4.0 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 37.9% | +2.3 | 2.16 | 4.59 | +8.8 | +4.0 |
| `asian_range_gte_30` | 9 | S_STRANGER | 31.0% | 33.3% | 33.3% | 33.3% | +1.1 | 1.57 | 2.62 | +7.4 | +3.7 |
| `confluence_gte_60` | 7 | R_REPEATER | 24.1% | 71.4% | 71.4% | 57.1% | +9.9 | 11.82 | 4.73 | +19.7 | +2.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 55.2% | 31.2% | 31.2% | 25.0% | +3.4 | 2.76 | 6.07 | +10.5 | +3.6 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 55.2% | 37.5% | 37.5% | 31.2% | +3.5 | 2.23 | 3.72 | +11.0 | +4.6 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 31.0% | 33.3% | 33.3% | 33.3% | +1.1 | 1.57 | 2.62 | +7.4 | +3.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 10.3% | 33.3% | 33.3% | 0.0% | -0.8 | 0.15 | 0.30 | +6.2 | +2.5 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 3.4% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +3.7 | +4.4 |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 37.9% | +2.3 | 2.16 | 4.59 | +8.8 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 37.9% | +2.3 | 2.16 | 4.59 | +8.8 | +4.0 |
| `feature_momentum_breakout_exception` | 18 | S_STRANGER | 62.1% | 27.8% | 27.8% | 33.3% | +1.7 | 1.96 | 4.31 | +6.5 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 27.6% | 37.5% | 37.5% | 25.0% | +2.5 | 1.99 | 3.31 | +8.0 | +4.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+3.6; validation N=3 Fav=33.3% Avg=-1.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 24.1% | +0.4 | 1.13 | 2.69 | +9.4 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 79.3% | 34.8% | 34.8% | 30.4% | +2.0 | 1.72 | 2.79 | +11.3 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 93.1% | 29.6% | 29.6% | 25.9% | +0.6 | 1.16 | 2.46 | +10.1 | +6.4 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 24.1% | +0.4 | 1.13 | 2.69 | +9.4 | +6.3 |
| `asian_range_gte_30` | 8 | S_STRANGER | 27.6% | 37.5% | 37.5% | 37.5% | +1.6 | 1.29 | 2.15 | +15.5 | +7.5 |
| `confluence_gte_60` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 24.1% | +0.4 | 1.13 | 2.69 | +9.4 | +6.3 |
| `confluence_gte_70` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 24.1% | +0.4 | 1.13 | 2.69 | +9.4 | +6.3 |
| `tdi_rsi_gt_signal` | 26 | S_STRANGER | 89.7% | 26.9% | 26.9% | 23.1% | +0.2 | 1.05 | 2.54 | +9.8 | +6.4 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 55.2% | 25.0% | 25.0% | 12.5% | -1.4 | 0.63 | 1.72 | +8.3 | +7.0 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 27.6% | 37.5% | 37.5% | 37.5% | +1.6 | 1.29 | 2.15 | +15.5 | +7.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 24.1% | 28.6% | 28.6% | 28.6% | +0.0 | 1.01 | 2.51 | +15.7 | +7.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 24.1% | +0.4 | 1.13 | 2.69 | +9.4 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 27.6% | 27.6% | 24.1% | +0.4 | 1.13 | 2.69 | +9.4 | +6.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+4.1; validation N=4 Fav=25.0% Avg=+1.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 36.4% | +2.2 | 2.27 | 4.55 | +9.5 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 25.0% | +1.2 | 1.53 | 3.82 | +8.1 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 25.0% | +1.2 | 1.53 | 3.82 | +8.1 | +4.7 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 36.4% | +2.2 | 2.27 | 4.55 | +9.5 | +4.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 28.6% | +2.1 | 2.02 | 5.05 | +9.3 | +4.3 |
| `confluence_gte_70` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 50.0% | +4.7 | 2.84 | 2.84 | +10.3 | +5.2 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 33.3% | -0.5 | 0.00 | 0.00 | +8.9 | +4.1 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 42.9% | +2.9 | 3.39 | 6.79 | +10.0 | +3.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 36.4% | +2.2 | 2.27 | 4.55 | +9.5 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 36.4% | +2.2 | 2.27 | 4.55 | +9.5 | +4.3 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +0.7 | +5.9 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=-3.6; validation N=24 Fav=29.2% Avg=+1.5; out_of_sample N=4 Fav=25.0% Avg=+1.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | +0.8 | 1.29 | 3.00 | +7.7 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 90.9% | 26.7% | 26.7% | 20.0% | +0.6 | 1.21 | 2.87 | +7.7 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 93.9% | 25.8% | 25.8% | 19.4% | +0.5 | 1.19 | 2.98 | +7.6 | +6.6 |
| `stop_hunt_le_90` | 33 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | +0.8 | 1.29 | 3.00 | +7.7 | +6.7 |
| `asian_range_gte_30` | 11 | S_STRANGER | 33.3% | 18.2% | 18.2% | 18.2% | -0.1 | 0.96 | 3.36 | +7.6 | +7.4 |
| `confluence_gte_60` | 33 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | +0.8 | 1.29 | 3.00 | +7.7 | +6.7 |
| `confluence_gte_70` | 33 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | +0.8 | 1.29 | 3.00 | +7.7 | +6.7 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 30.3% | 20.0% | 20.0% | 20.0% | -0.0 | 1.00 | 2.99 | +6.8 | +4.7 |
| `tdi_rsi_gte_50` | 28 | S_STRANGER | 84.8% | 21.4% | 21.4% | 10.7% | +0.2 | 1.08 | 3.61 | +7.4 | +6.7 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 33.3% | 18.2% | 18.2% | 18.2% | -0.1 | 0.96 | 3.36 | +7.6 | +7.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +9.1 | +4.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 33 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | +0.8 | 1.29 | 3.00 | +7.7 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 33 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | +0.8 | 1.29 | 3.00 | +7.7 | +6.7 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 9.1% | 33.3% | 33.3% | 33.3% | -3.2 | 0.23 | 0.46 | +9.8 | +9.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 6.1% | 0.0% | 0.0% | 0.0% | -6.3 | 0.00 | 0.00 | +6.2 | +10.7 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=11 Fav=27.3% Avg=+0.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +0.7 | 1.24 | 3.30 | +9.1 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 0.0% | +0.1 | 1.03 | 4.11 | +9.4 | +6.8 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 0.0% | +0.3 | 1.11 | 3.32 | +9.2 | +6.4 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +0.7 | 1.24 | 3.30 | +9.1 | +6.6 |
| `asian_range_gte_30` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +6.2 | +7.9 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +0.7 | 1.24 | 3.30 | +9.1 | +6.6 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +0.7 | 1.24 | 3.30 | +9.1 | +6.6 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 11.1% | +0.7 | 1.22 | 4.26 | +9.1 | +7.2 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +4.5 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +6.2 | +7.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +6.2 | +7.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +0.7 | 1.24 | 3.30 | +9.1 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 9.1% | +0.7 | 1.24 | 3.30 | +9.1 | +6.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=10 Fav=20.0% Avg=+0.3; out_of_sample N=1 Fav=100.0% Avg=+4.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 45.5% | 27.3% | +0.6 | 1.20 | 1.20 | +7.3 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 63.6% | 14.3% | 42.9% | 14.3% | +0.7 | 1.27 | 1.27 | +6.8 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 81.8% | 22.2% | 44.4% | 22.2% | +1.5 | 1.65 | 1.65 | +7.5 | +5.1 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 45.5% | 27.3% | +0.6 | 1.20 | 1.20 | +7.3 | +5.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 45.5% | 27.3% | +0.6 | 1.20 | 1.20 | +7.3 | +5.3 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 45.5% | 27.3% | +0.6 | 1.20 | 1.20 | +7.3 | +5.3 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 22.2% | 44.4% | 11.1% | -0.6 | 0.84 | 1.05 | +6.0 | +6.2 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 0.0% | -4.7 | 0.16 | 0.64 | +3.0 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 45.5% | 27.3% | +0.6 | 1.20 | 1.20 | +7.3 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 45.5% | 27.3% | +0.6 | 1.20 | 1.20 | +7.3 | +5.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+1.4; validation N=9 Fav=22.2% Avg=-0.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -0.2 | 0.95 | 2.53 | +7.4 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 0.0% | +0.9 | 1.43 | 2.86 | +9.2 | +3.3 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 0.0% | +0.9 | 1.43 | 2.86 | +9.2 | +3.3 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -0.2 | 0.95 | 2.53 | +7.4 | +4.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 0.0% | -1.7 | 0.51 | 2.03 | +6.9 | +4.8 |
| `confluence_gte_70` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +3.4 | +7.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 12.5% | -0.8 | 0.79 | 2.37 | +7.7 | +5.7 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 11.1% | -1.0 | 0.73 | 2.56 | +7.4 | +5.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -0.2 | 0.95 | 2.53 | +7.4 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -0.2 | 0.95 | 2.53 | +7.4 | +4.8 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +0.4 | +5.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -6.3 | 0.00 | 0.00 | +0.2 | +7.0 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=11 Fav=27.3% Avg=-5.1; validation N=14 Fav=28.6% Avg=+0.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 3.8% | -2.1 | 0.60 | 1.54 | +6.8 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 96.2% | 28.0% | 28.0% | 0.0% | -2.2 | 0.60 | 1.54 | +6.8 | +8.5 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 3.8% | -2.1 | 0.60 | 1.54 | +6.8 | +8.2 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 3.8% | -2.1 | 0.60 | 1.54 | +6.8 | +8.2 |
| `asian_range_gte_30` | 5 | S_STRANGER | 19.2% | 0.0% | 0.0% | 0.0% | -8.7 | 0.00 | 0.00 | +1.8 | +12.7 |
| `confluence_gte_60` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 3.8% | -2.1 | 0.60 | 1.54 | +6.8 | +8.2 |
| `confluence_gte_70` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 3.8% | -2.1 | 0.60 | 1.54 | +6.8 | +8.2 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 23.1% | 16.7% | 16.7% | 16.7% | -2.8 | 0.48 | 1.91 | +6.6 | +9.9 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 88.5% | 26.1% | 26.1% | 4.3% | -2.2 | 0.60 | 1.59 | +6.9 | +8.5 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 19.2% | 0.0% | 0.0% | 0.0% | -8.7 | 0.00 | 0.00 | +1.8 | +12.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 3.8% | 0.0% | 0.0% | 0.0% | -17.0 | 0.00 | 0.00 | +1.5 | +21.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 3.8% | -2.1 | 0.60 | 1.54 | +6.8 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 3.8% | -2.1 | 0.60 | 1.54 | +6.8 | +8.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+5.9; validation N=2 Fav=0.0% Avg=-1.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 40.0% | +2.3 | 2.41 | 5.43 | +9.0 | +4.2 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 53.3% | 37.5% | 37.5% | 50.0% | +4.1 | 3.25 | 4.34 | +10.3 | +4.2 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 86.7% | 30.8% | 30.8% | 46.2% | +3.0 | 3.00 | 5.25 | +9.8 | +3.9 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 40.0% | +2.3 | 2.41 | 5.43 | +9.0 | +4.2 |
| `asian_range_gte_30` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +6.9 | +4.9 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 40.0% | +2.3 | 2.41 | 5.43 | +9.0 | +4.2 |
| `confluence_gte_70` | 7 | S_STRANGER | 46.7% | 14.3% | 14.3% | 28.6% | +0.4 | 1.28 | 6.38 | +7.5 | +4.2 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 46.7% | 14.3% | 14.3% | 14.3% | +1.4 | 2.05 | 12.32 | +8.2 | +5.1 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +5.5 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 80.0% | 33.3% | 33.3% | 41.7% | +3.1 | 2.76 | 4.84 | +10.3 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 40.0% | +2.3 | 2.41 | 5.43 | +9.0 | +4.2 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 53.3% | 25.0% | 25.0% | 50.0% | +2.6 | 2.39 | 4.78 | +8.9 | +4.6 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +3.3 | +7.4 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+4.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 5.3% | -0.1 | 0.98 | 2.13 | +8.7 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 89.5% | 29.4% | 35.3% | 5.9% | +0.3 | 1.09 | 2.00 | +9.1 | +5.8 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 89.5% | 29.4% | 35.3% | 5.9% | +0.3 | 1.09 | 2.00 | +9.1 | +5.8 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 5.3% | -0.1 | 0.98 | 2.13 | +8.7 | +5.9 |
| `asian_range_gte_30` | 6 | R_REPEATER | 31.6% | 50.0% | 50.0% | 16.7% | +4.9 | 2.48 | 2.48 | +14.3 | +3.7 |
| `confluence_gte_60` | 9 | S_STRANGER | 47.4% | 44.4% | 55.6% | 11.1% | +3.7 | 3.72 | 2.98 | +10.3 | +4.1 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +11.4 | +5.3 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +0.5 | +11.6 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 73.7% | 28.6% | 28.6% | 0.0% | +0.6 | 1.21 | 3.02 | +10.6 | +6.7 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 31.6% | 50.0% | 50.0% | 16.7% | +4.9 | 2.48 | 2.48 | +14.3 | +3.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 5.3% | -0.1 | 0.98 | 2.13 | +8.7 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 5.3% | -0.1 | 0.98 | 2.13 | +8.7 | +5.9 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 21.1% | 0.0% | 25.0% | 0.0% | -2.9 | 0.13 | 0.40 | +4.1 | +6.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 10.5% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +5.6 | +8.2 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=0.0% Avg=-5.7; validation N=7 Fav=42.9% Avg=+2.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 15.8% | -2.0 | 0.39 | 0.78 | +5.8 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 15.8% | -2.0 | 0.39 | 0.78 | +5.8 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 15.8% | -2.0 | 0.39 | 0.78 | +5.8 | +6.5 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 15.8% | -2.0 | 0.39 | 0.78 | +5.8 | +6.5 |
| `asian_range_gte_30` | 11 | S_STRANGER | 57.9% | 27.3% | 27.3% | 18.2% | -0.6 | 0.75 | 1.76 | +6.2 | +5.6 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 15.8% | -2.0 | 0.39 | 0.78 | +5.8 | +6.5 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 15.8% | -2.0 | 0.39 | 0.78 | +5.8 | +6.5 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 68.4% | 15.4% | 23.1% | 15.4% | -3.2 | 0.16 | 0.48 | +4.6 | +6.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 36.8% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +4.1 | +5.7 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 57.9% | 27.3% | 27.3% | 18.2% | -0.6 | 0.75 | 1.76 | +6.2 | +5.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 42.1% | 12.5% | 12.5% | 12.5% | -2.2 | 0.17 | 1.00 | +4.4 | +5.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 15.8% | -2.0 | 0.39 | 0.78 | +5.8 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 15.8% | -2.0 | 0.39 | 0.78 | +5.8 | +6.5 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 42.1% | 12.5% | 25.0% | 12.5% | -3.9 | 0.20 | 0.59 | +5.9 | +7.9 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 15.8% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +6.2 | +4.2 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=30.0% Avg=+1.1; validation N=6 Fav=50.0% Avg=+4.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 25.9% | 29.6% | 18.5% | -0.2 | 0.94 | 1.88 | +7.4 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 66.7% | 22.2% | 27.8% | 22.2% | -1.4 | 0.70 | 1.41 | +6.6 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 92.6% | 20.0% | 24.0% | 16.0% | -1.5 | 0.66 | 1.76 | +6.5 | +5.5 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 100.0% | 25.9% | 29.6% | 18.5% | -0.2 | 0.94 | 1.88 | +7.4 | +5.2 |
| `asian_range_gte_30` | 2 | S_STRANGER | 7.4% | 0.0% | 0.0% | 0.0% | -15.8 | 0.00 | 0.00 | +6.0 | +6.0 |
| `confluence_gte_60` | 27 | S_STRANGER | 100.0% | 25.9% | 29.6% | 18.5% | -0.2 | 0.94 | 1.88 | +7.4 | +5.2 |
| `confluence_gte_70` | 27 | S_STRANGER | 100.0% | 25.9% | 29.6% | 18.5% | -0.2 | 0.94 | 1.88 | +7.4 | +5.2 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 63.0% | 35.3% | 41.2% | 17.6% | +1.0 | 1.23 | 1.58 | +8.8 | +4.4 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 59.3% | 37.5% | 37.5% | 12.5% | +2.2 | 1.68 | 2.51 | +9.6 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 2 | S_STRANGER | 7.4% | 0.0% | 0.0% | 0.0% | -15.8 | 0.00 | 0.00 | +6.0 | +6.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 3.7% | 0.0% | 0.0% | 0.0% | -30.6 | 0.00 | 0.00 | +3.3 | +4.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 85.2% | 26.1% | 30.4% | 21.7% | -0.0 | 1.00 | 1.86 | +7.4 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 25.9% | 29.6% | 18.5% | -0.2 | 0.94 | 1.88 | +7.4 | +5.2 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 44.4% | 16.7% | 25.0% | 8.3% | -3.8 | 0.38 | 1.01 | +6.4 | +5.8 |
| `feature_eurjpy_tdi50_reclaim` | 9 | S_STRANGER | 33.3% | 33.3% | 33.3% | 0.0% | -0.7 | 0.85 | 1.70 | +8.3 | +7.4 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=20.0% Avg=+0.8; out_of_sample N=1 Fav=100.0% Avg=+9.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.3 | 0.89 | 2.68 | +6.9 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.57 | 2.86 | +5.8 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 14.3% | -0.0 | 1.00 | 2.49 | +7.9 | +5.5 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.3 | 0.89 | 2.68 | +6.9 | +4.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.3 | 0.89 | 2.68 | +6.9 | +4.8 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.3 | 0.89 | 2.68 | +6.9 | +4.8 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 18.2% | -0.0 | 0.99 | 2.64 | +6.6 | +4.9 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 16.7% | +2.3 | 2.45 | 4.91 | +8.7 | +3.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.3 | 0.89 | 2.68 | +6.9 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -0.3 | 0.89 | 2.68 | +6.9 | +4.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=50.0% Avg=+3.1; validation N=2 Fav=0.0% Avg=-7.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 6.2% | -0.4 | 0.85 | 2.55 | +6.9 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 6.2% | -0.4 | 0.85 | 2.55 | +6.9 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 6.2% | -0.4 | 0.85 | 2.55 | +6.9 | +4.9 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 6.2% | -0.4 | 0.85 | 2.55 | +6.9 | +4.9 |
| `asian_range_gte_30` | 8 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +5.4 | +5.7 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 6.2% | -0.4 | 0.85 | 2.55 | +6.9 | +4.9 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 6.2% | -0.4 | 0.85 | 2.55 | +6.9 | +4.9 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 37.5% | 33.3% | 33.3% | 0.0% | -0.4 | 0.85 | 1.69 | +7.4 | +5.2 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 68.8% | 27.3% | 27.3% | 9.1% | -0.4 | 0.85 | 2.28 | +7.3 | +5.4 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +5.4 | +5.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -7.5 | 0.00 | 0.00 | +7.4 | +9.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 6.2% | -0.4 | 0.85 | 2.55 | +6.9 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 6.2% | -0.4 | 0.85 | 2.55 | +6.9 | +4.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=-0.2; validation N=7 Fav=28.6% Avg=+3.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 40 | S_STRANGER | 100.0% | 25.0% | 27.5% | 25.0% | -1.1 | 0.72 | 1.71 | +7.4 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 37 | S_STRANGER | 92.5% | 24.3% | 27.0% | 24.3% | -1.1 | 0.72 | 1.72 | +7.6 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 38 | S_STRANGER | 95.0% | 23.7% | 26.3% | 23.7% | -1.1 | 0.71 | 1.77 | +7.5 | +6.3 |
| `stop_hunt_le_90` | 40 | S_STRANGER | 100.0% | 25.0% | 27.5% | 25.0% | -1.1 | 0.72 | 1.71 | +7.4 | +6.3 |
| `asian_range_gte_30` | 11 | S_STRANGER | 27.5% | 36.4% | 36.4% | 36.4% | +1.8 | 2.00 | 3.01 | +8.4 | +4.8 |
| `confluence_gte_60` | 24 | S_STRANGER | 60.0% | 29.2% | 33.3% | 29.2% | +0.7 | 1.20 | 2.26 | +8.8 | +5.8 |
| `confluence_gte_70` | 2 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +6.5 | +5.7 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 10.0% | 25.0% | 25.0% | 25.0% | -1.6 | 0.64 | 1.92 | +6.4 | +9.9 |
| `tdi_rsi_gte_50` | 29 | S_STRANGER | 72.5% | 20.7% | 20.7% | 17.2% | -2.0 | 0.57 | 2.09 | +7.5 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 27.5% | 36.4% | 36.4% | 36.4% | +1.8 | 2.00 | 3.01 | +8.4 | +4.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 40 | S_STRANGER | 100.0% | 25.0% | 27.5% | 25.0% | -1.1 | 0.72 | 1.71 | +7.4 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 40 | S_STRANGER | 100.0% | 25.0% | 27.5% | 25.0% | -1.1 | 0.72 | 1.71 | +7.4 | +6.3 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +4.0 | +8.1 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +4.0 | +8.1 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=22.2% Avg=-1.0; out_of_sample N=2 Fav=50.0% Avg=+1.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.4 | 0.64 | 1.93 | +6.5 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 0.0% | -4.1 | 0.14 | 0.57 | +4.9 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 9.1% | -1.5 | 0.65 | 1.75 | +6.7 | +5.7 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.4 | 0.64 | 1.93 | +6.5 | +5.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.4 | 0.64 | 1.93 | +6.5 | +5.4 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.4 | 0.64 | 1.93 | +6.5 | +5.4 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 0.0% | -2.5 | 0.48 | 0.48 | +6.3 | +8.3 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 9.1% | -0.5 | 0.86 | 2.28 | +6.6 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.4 | 0.64 | 1.93 | +6.5 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.4 | 0.64 | 1.93 | +6.5 | +5.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-11.7; validation N=5 Fav=60.0% Avg=+10.3; out_of_sample N=1 Fav=0.0% Avg=-8.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -1.5 | 0.77 | 2.04 | +9.2 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -1.5 | 0.77 | 2.04 | +9.2 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -1.5 | 0.77 | 2.04 | +9.2 | +5.0 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -1.5 | 0.77 | 2.04 | +9.2 | +5.0 |
| `asian_range_gte_30` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 20.0% | -8.9 | 0.19 | 0.58 | +4.4 | +4.6 |
| `confluence_gte_60` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 10.0% | -2.9 | 0.63 | 2.50 | +9.2 | +5.4 |
| `confluence_gte_70` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +3.5 | +8.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 12.5% | -1.2 | 0.85 | 1.42 | +10.6 | +5.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 14.3% | +4.6 | 2.21 | 2.94 | +13.1 | +5.5 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 20.0% | -8.9 | 0.19 | 0.58 | +4.4 | +4.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 0.0% | -11.2 | 0.19 | 0.58 | +3.9 | +4.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -1.5 | 0.77 | 2.04 | +9.2 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -1.5 | 0.77 | 2.04 | +9.2 | +5.0 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +6.2 | +5.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+3.4; validation N=3 Fav=0.0% Avg=-2.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | -2.8 | 0.31 | 0.73 | +8.2 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 33.3% | -1.5 | 0.41 | 1.02 | +8.0 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | -2.8 | 0.31 | 0.73 | +8.2 | +4.3 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | -2.8 | 0.31 | 0.73 | +8.2 | +4.3 |
| `asian_range_gte_30` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 66.7% | +1.6 | 2.07 | 1.03 | +16.1 | +2.9 |
| `confluence_gte_60` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 28.6% | -5.7 | 0.10 | 0.48 | +5.4 | +5.1 |
| `confluence_gte_70` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +4.2 | 999.00 | 999.00 | +16.6 | +0.9 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 50.0% | +0.4 | 1.32 | 1.32 | +9.6 | +2.9 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 33.3% | -0.7 | 0.73 | 1.09 | +10.1 | +4.1 |
| `ratio_le_2_and_asian_gte_30` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 66.7% | +1.6 | 2.07 | 1.03 | +16.1 | +2.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +4.2 | 999.00 | 999.00 | +16.6 | +0.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 27.3% | -3.6 | 0.19 | 0.66 | +7.1 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | -2.8 | 0.31 | 0.73 | +8.2 | +4.3 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 33.3% | 50.0% | 50.0% | 50.0% | +1.4 | 2.29 | 1.14 | +13.3 | +2.4 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 33.3% | 50.0% | 50.0% | 50.0% | +1.4 | 2.29 | 1.14 | +13.3 | +2.4 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=22.2% Avg=-2.2; validation N=1 Fav=100.0% Avg=+31.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 53 | S_STRANGER | 100.0% | 24.5% | 28.3% | 11.3% | -0.6 | 0.83 | 2.04 | +6.8 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 49 | S_STRANGER | 92.5% | 24.5% | 28.6% | 12.2% | -0.9 | 0.76 | 1.85 | +6.5 | +5.8 |
| `hunt_to_ar_ratio_le_2_5` | 53 | S_STRANGER | 100.0% | 24.5% | 28.3% | 11.3% | -0.6 | 0.83 | 2.04 | +6.8 | +5.6 |
| `stop_hunt_le_90` | 53 | S_STRANGER | 100.0% | 24.5% | 28.3% | 11.3% | -0.6 | 0.83 | 2.04 | +6.8 | +5.6 |
| `asian_range_gte_30` | 19 | S_STRANGER | 35.8% | 5.3% | 10.5% | 5.3% | -3.8 | 0.18 | 1.44 | +3.9 | +6.7 |
| `confluence_gte_60` | 44 | S_STRANGER | 83.0% | 22.7% | 27.3% | 11.4% | -1.3 | 0.66 | 1.71 | +6.1 | +5.4 |
| `confluence_gte_70` | 9 | S_STRANGER | 17.0% | 22.2% | 22.2% | 0.0% | -0.1 | 0.96 | 3.34 | +7.1 | +5.3 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 39.6% | 14.3% | 14.3% | 4.8% | -3.7 | 0.25 | 1.48 | +4.4 | +6.8 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 35.8% | 26.3% | 26.3% | 5.3% | +0.5 | 1.16 | 3.24 | +7.9 | +6.3 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 35.8% | 5.3% | 10.5% | 5.3% | -3.8 | 0.18 | 1.44 | +3.9 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 13.2% | 0.0% | 0.0% | 0.0% | -6.7 | 0.00 | 0.00 | +2.1 | +8.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 51 | S_STRANGER | 96.2% | 23.5% | 27.5% | 11.8% | -0.9 | 0.74 | 1.91 | +6.5 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 52 | S_STRANGER | 98.1% | 23.1% | 26.9% | 9.6% | -1.2 | 0.66 | 1.73 | +6.1 | +5.5 |
| `feature_momentum_breakout_exception` | 19 | S_STRANGER | 35.8% | 26.3% | 31.6% | 10.5% | -0.6 | 0.80 | 1.59 | +6.1 | +5.2 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 18.9% | 30.0% | 30.0% | 10.0% | +1.2 | 1.27 | 2.96 | +9.8 | +7.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+4.6; validation N=15 Fav=13.3% Avg=-1.3; out_of_sample N=4 Fav=75.0% Avg=+3.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 24.0% | 24.0% | 8.0% | -0.7 | 0.77 | 2.18 | +5.5 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 80.0% | 30.0% | 30.0% | 5.0% | +0.0 | 1.00 | 2.34 | +6.1 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 84.0% | 28.6% | 28.6% | 4.8% | -0.4 | 0.88 | 2.20 | +5.8 | +5.0 |
| `stop_hunt_le_90` | 25 | S_STRANGER | 100.0% | 24.0% | 24.0% | 8.0% | -0.7 | 0.77 | 2.18 | +5.5 | +4.8 |
| `asian_range_gte_30` | 3 | S_STRANGER | 12.0% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +4.3 | +3.8 |
| `confluence_gte_60` | 25 | S_STRANGER | 100.0% | 24.0% | 24.0% | 8.0% | -0.7 | 0.77 | 2.18 | +5.5 | +4.8 |
| `confluence_gte_70` | 25 | S_STRANGER | 100.0% | 24.0% | 24.0% | 8.0% | -0.7 | 0.77 | 2.18 | +5.5 | +4.8 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 8.0% | 50.0% | 50.0% | 0.0% | +1.8 | 7.00 | 7.00 | +7.6 | +5.4 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 96.0% | 25.0% | 25.0% | 8.3% | -0.5 | 0.83 | 2.20 | +5.7 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 12.0% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +4.3 | +3.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.0% | 0.0% | 0.0% | 0.0% | -0.6 | 0.00 | 0.00 | +6.2 | +4.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 100.0% | 24.0% | 24.0% | 8.0% | -0.7 | 0.77 | 2.18 | +5.5 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 24.0% | 24.0% | 8.0% | -0.7 | 0.77 | 2.18 | +5.5 | +4.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=0.0% Avg=-3.2; validation N=10 Fav=50.0% Avg=+6.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 23.8% | 23.8% | 9.5% | +1.0 | 1.36 | 3.54 | +7.8 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 61.9% | 23.1% | 23.1% | 0.0% | -0.5 | 0.86 | 2.88 | +6.6 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 90.5% | 26.3% | 26.3% | 5.3% | +1.1 | 1.36 | 3.54 | +7.6 | +5.5 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 23.8% | 23.8% | 9.5% | +1.0 | 1.36 | 3.54 | +7.8 | +5.2 |
| `asian_range_gte_30` | 3 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +5.0 | +11.8 |
| `confluence_gte_60` | 19 | S_STRANGER | 90.5% | 26.3% | 26.3% | 10.5% | +1.4 | 1.51 | 3.33 | +8.4 | +4.9 |
| `confluence_gte_70` | 7 | S_STRANGER | 33.3% | 14.3% | 14.3% | 14.3% | -1.5 | 0.44 | 1.77 | +6.0 | +4.1 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 28.6% | 16.7% | 16.7% | 16.7% | -1.6 | 0.46 | 1.83 | +6.6 | +7.8 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 76.2% | 31.2% | 31.2% | 6.2% | +3.1 | 2.79 | 5.03 | +9.5 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +5.0 | +11.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +5.0 | +11.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 95.2% | 25.0% | 25.0% | 10.0% | +1.1 | 1.39 | 3.33 | +7.8 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 23.8% | 23.8% | 9.5% | +1.0 | 1.36 | 3.54 | +7.8 | +5.2 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 9.5% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +7.1 | +6.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 9.5% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +7.1 | +6.5 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-2.0; validation N=16 Fav=31.2% Avg=+0.8; out_of_sample N=7 Fav=14.3% Avg=-1.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 23.1% | 23.1% | 11.5% | -0.1 | 0.97 | 3.23 | +5.7 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 42.3% | 9.1% | 9.1% | 9.1% | -2.2 | 0.26 | 2.61 | +3.4 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 61.5% | 25.0% | 25.0% | 18.8% | -0.2 | 0.90 | 2.71 | +6.1 | +6.0 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 23.1% | 23.1% | 11.5% | -0.1 | 0.97 | 3.23 | +5.7 | +5.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 26 | S_STRANGER | 100.0% | 23.1% | 23.1% | 11.5% | -0.1 | 0.97 | 3.23 | +5.7 | +5.4 |
| `confluence_gte_70` | 26 | S_STRANGER | 100.0% | 23.1% | 23.1% | 11.5% | -0.1 | 0.97 | 3.23 | +5.7 | +5.4 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 53.8% | 21.4% | 21.4% | 7.1% | -0.2 | 0.90 | 3.31 | +5.8 | +5.5 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 53.8% | 14.3% | 14.3% | 7.1% | -1.4 | 0.48 | 2.86 | +4.9 | +5.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 92.3% | 25.0% | 25.0% | 12.5% | +0.1 | 1.03 | 3.08 | +5.9 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 96.2% | 24.0% | 24.0% | 12.0% | +0.0 | 1.00 | 3.17 | +5.8 | +5.6 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +3.4 | +2.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +3.4 | +2.2 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=10.0% Avg=-5.6; validation N=2 Fav=100.0% Avg=+15.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -2.1 | 0.57 | 1.90 | +5.7 | +8.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -2.1 | 0.57 | 1.90 | +5.7 | +8.1 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -2.1 | 0.57 | 1.90 | +5.7 | +8.1 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -2.1 | 0.57 | 1.90 | +5.7 | +8.1 |
| `asian_range_gte_30` | 12 | S_STRANGER | 92.3% | 16.7% | 16.7% | 16.7% | -4.2 | 0.21 | 1.06 | +4.0 | +8.6 |
| `confluence_gte_60` | 10 | S_STRANGER | 76.9% | 20.0% | 20.0% | 20.0% | -4.5 | 0.23 | 0.94 | +4.2 | +9.0 |
| `confluence_gte_70` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -9.1 | 0.00 | 0.00 | +3.8 | +14.2 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 92.3% | 25.0% | 25.0% | 25.0% | -2.0 | 0.61 | 1.82 | +5.9 | +8.3 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -8.0 | 0.00 | 0.00 | +3.6 | +12.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 92.3% | 16.7% | 16.7% | 16.7% | -4.2 | 0.21 | 1.06 | +4.0 | +8.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 84.6% | 18.2% | 18.2% | 18.2% | -4.3 | 0.22 | 1.01 | +4.1 | +8.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -2.1 | 0.57 | 1.90 | +5.7 | +8.1 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -2.1 | 0.57 | 1.90 | +5.7 | +8.1 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 46.2% | 16.7% | 16.7% | 16.7% | -2.8 | 0.24 | 1.18 | +5.5 | +6.8 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -9.9 | 0.00 | 0.00 | +5.5 | +13.7 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+2.8; validation N=4 Fav=50.0% Avg=-2.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 48 | S_STRANGER | 100.0% | 22.9% | 25.0% | 29.2% | -0.2 | 0.96 | 2.40 | +7.6 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 42 | S_STRANGER | 87.5% | 26.2% | 28.6% | 33.3% | +0.4 | 1.11 | 2.22 | +8.4 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 47 | S_STRANGER | 97.9% | 23.4% | 25.5% | 29.8% | -0.0 | 0.99 | 2.39 | +7.7 | +4.8 |
| `stop_hunt_le_90` | 48 | S_STRANGER | 100.0% | 22.9% | 25.0% | 29.2% | -0.2 | 0.96 | 2.40 | +7.6 | +4.8 |
| `asian_range_gte_30` | 10 | S_STRANGER | 20.8% | 40.0% | 40.0% | 50.0% | +0.3 | 1.05 | 1.05 | +11.5 | +3.3 |
| `confluence_gte_60` | 23 | S_STRANGER | 47.9% | 30.4% | 34.8% | 30.4% | +1.1 | 1.27 | 2.07 | +9.7 | +4.0 |
| `confluence_gte_70` | 2 | R_REPEATER | 4.2% | 50.0% | 50.0% | 0.0% | +1.8 | 2.54 | 2.54 | +8.5 | +3.3 |
| `tdi_rsi_gt_signal` | 39 | S_STRANGER | 81.2% | 25.6% | 28.2% | 25.6% | +0.5 | 1.15 | 2.62 | +7.6 | +4.4 |
| `tdi_rsi_gte_50` | 25 | S_STRANGER | 52.1% | 32.0% | 32.0% | 32.0% | +1.4 | 1.58 | 2.76 | +8.4 | +4.6 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 20.8% | 40.0% | 40.0% | 50.0% | +0.3 | 1.05 | 1.05 | +11.5 | +3.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 18.8% | 44.4% | 44.4% | 44.4% | +0.3 | 1.05 | 1.05 | +12.4 | +3.5 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +3.8 | +3.9 |
| `feature_extreme_hunt_with_exception` | 47 | S_STRANGER | 97.9% | 23.4% | 25.5% | 29.8% | -0.1 | 0.97 | 2.34 | +7.8 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 47 | S_STRANGER | 97.9% | 23.4% | 25.5% | 27.7% | -0.2 | 0.96 | 2.40 | +7.6 | +4.9 |
| `feature_momentum_breakout_exception` | 14 | S_STRANGER | 29.2% | 28.6% | 28.6% | 28.6% | +1.8 | 1.84 | 4.14 | +7.9 | +4.3 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 20.8% | 30.0% | 30.0% | 30.0% | +1.6 | 1.71 | 3.42 | +8.4 | +4.4 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=30.0% Avg=+1.4; validation N=5 Fav=0.0% Avg=-2.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 16.1% | -1.9 | 0.54 | 1.71 | +7.2 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 16.1% | -1.9 | 0.54 | 1.71 | +7.2 | +7.4 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 16.1% | -1.9 | 0.54 | 1.71 | +7.2 | +7.4 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 16.1% | -1.9 | 0.54 | 1.71 | +7.2 | +7.4 |
| `asian_range_gte_30` | 13 | S_STRANGER | 41.9% | 15.4% | 15.4% | 0.0% | -4.9 | 0.19 | 1.03 | +6.7 | +9.3 |
| `confluence_gte_60` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 16.1% | -1.9 | 0.54 | 1.71 | +7.2 | +7.4 |
| `confluence_gte_70` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 16.1% | -1.9 | 0.54 | 1.71 | +7.2 | +7.4 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 41.9% | 23.1% | 23.1% | 7.7% | -4.4 | 0.30 | 0.99 | +6.7 | +9.8 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 51.6% | 18.8% | 18.8% | 0.0% | -2.3 | 0.42 | 1.83 | +7.4 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 41.9% | 15.4% | 15.4% | 0.0% | -4.9 | 0.19 | 1.03 | +6.7 | +9.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 12.9% | 25.0% | 25.0% | 0.0% | -9.2 | 0.04 | 0.13 | +6.7 | +12.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 16.1% | -1.9 | 0.54 | 1.71 | +7.2 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 16.1% | -1.9 | 0.54 | 1.71 | +7.2 | +7.4 |
| `feature_momentum_breakout_exception` | 15 | S_STRANGER | 48.4% | 20.0% | 20.0% | 20.0% | +0.2 | 1.08 | 3.96 | +6.5 | +4.1 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 25.8% | 0.0% | 0.0% | 0.0% | -2.0 | 0.00 | 0.00 | +5.9 | +4.1 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=15 Fav=20.0% Avg=-2.1; validation N=2 Fav=50.0% Avg=+4.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | -1.8 | 0.56 | 1.97 | +6.0 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 83.3% | 13.3% | 13.3% | 13.3% | -2.6 | 0.38 | 2.48 | +5.0 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 94.4% | 17.6% | 17.6% | 11.8% | -2.5 | 0.42 | 1.94 | +5.3 | +6.6 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | -1.8 | 0.56 | 1.97 | +6.0 | +6.3 |
| `asian_range_gte_30` | 6 | S_STRANGER | 33.3% | 16.7% | 16.7% | 16.7% | -1.9 | 0.49 | 2.43 | +6.6 | +6.2 |
| `confluence_gte_60` | 8 | S_STRANGER | 44.4% | 12.5% | 12.5% | 12.5% | -4.1 | 0.25 | 1.73 | +3.9 | +8.4 |
| `confluence_gte_70` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -7.3 | 0.00 | 0.00 | +2.1 | +10.7 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 83.3% | 13.3% | 13.3% | 0.0% | -3.2 | 0.26 | 1.70 | +5.2 | +6.8 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 77.8% | 14.3% | 14.3% | 0.0% | -3.2 | 0.27 | 1.63 | +5.4 | +7.0 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 33.3% | 16.7% | 16.7% | 16.7% | -1.9 | 0.49 | 2.43 | +6.6 | +6.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 27.8% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +5.0 | +7.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 94.4% | 23.5% | 23.5% | 11.8% | -1.3 | 0.65 | 2.11 | +6.3 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | -1.8 | 0.56 | 1.97 | +6.0 | +6.3 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 50.0% | 11.1% | 11.1% | 11.1% | -3.8 | 0.24 | 1.92 | +5.5 | +6.8 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 38.9% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +4.9 | +7.3 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=11.1% Avg=-2.2; validation N=18 Fav=16.7% Avg=-0.7; out_of_sample N=4 Fav=75.0% Avg=+13.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 6.2% | +0.6 | 1.24 | 4.09 | +6.7 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 96.9% | 22.6% | 22.6% | 6.5% | +0.7 | 1.31 | 4.12 | +6.9 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 96.9% | 22.6% | 22.6% | 6.5% | +0.7 | 1.31 | 4.12 | +6.9 | +4.8 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 6.2% | +0.6 | 1.24 | 4.09 | +6.7 | +4.8 |
| `asian_range_gte_30` | 15 | S_STRANGER | 46.9% | 6.7% | 6.7% | 6.7% | -1.8 | 0.32 | 4.20 | +5.3 | +5.1 |
| `confluence_gte_60` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 6.2% | +0.6 | 1.24 | 4.09 | +6.7 | +4.8 |
| `confluence_gte_70` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 6.2% | +0.6 | 1.24 | 4.09 | +6.7 | +4.8 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 18.8% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +2.9 | +6.2 |
| `tdi_rsi_gte_50` | 25 | S_STRANGER | 78.1% | 20.0% | 20.0% | 0.0% | +0.3 | 1.12 | 4.25 | +6.4 | +5.1 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 46.9% | 6.7% | 6.7% | 6.7% | -1.8 | 0.32 | 4.20 | +5.3 | +5.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +0.1 | +8.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 6.2% | +0.6 | 1.24 | 4.09 | +6.7 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 6.2% | +0.6 | 1.24 | 4.09 | +6.7 | +4.8 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +2.5 | +6.4 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +2.5 | +6.4 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=-2.8; validation N=24 Fav=25.0% Avg=+0.8; out_of_sample N=1 Fav=0.0% Avg=-1.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 15.6% | -0.1 | 0.97 | 3.20 | +6.2 | +5.1 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 93.8% | 23.3% | 23.3% | 16.7% | +0.1 | 1.05 | 3.14 | +6.6 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 15.6% | -0.1 | 0.97 | 3.20 | +6.2 | +5.1 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 15.6% | -0.1 | 0.97 | 3.20 | +6.2 | +5.1 |
| `asian_range_gte_30` | 10 | S_STRANGER | 31.2% | 10.0% | 10.0% | 30.0% | -2.7 | 0.28 | 1.98 | +5.1 | +6.7 |
| `confluence_gte_60` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 15.6% | -0.1 | 0.97 | 3.20 | +6.2 | +5.1 |
| `confluence_gte_70` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 15.6% | -0.1 | 0.97 | 3.20 | +6.2 | +5.1 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 46.9% | 13.3% | 13.3% | 6.7% | -3.5 | 0.25 | 1.61 | +3.7 | +7.3 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 62.5% | 20.0% | 20.0% | 10.0% | -0.9 | 0.73 | 2.74 | +5.8 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 31.2% | 10.0% | 10.0% | 30.0% | -2.7 | 0.28 | 1.98 | +5.1 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 21.9% | 14.3% | 14.3% | 14.3% | -3.8 | 0.29 | 1.72 | +3.8 | +7.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 15.6% | -0.1 | 0.97 | 3.20 | +6.2 | +5.1 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 21.9% | 21.9% | 15.6% | -0.1 | 0.97 | 3.20 | +6.2 | +5.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 9.4% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +1.8 | +10.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 9.4% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +1.8 | +10.0 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+5.7; validation N=1 Fav=0.0% Avg=-2.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 13.0% | -1.6 | 0.64 | 2.19 | +6.4 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 87.0% | 20.0% | 20.0% | 15.0% | -1.5 | 0.67 | 2.51 | +7.0 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 13.0% | -1.6 | 0.64 | 2.19 | +6.4 | +7.4 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 13.0% | -1.6 | 0.64 | 2.19 | +6.4 | +7.4 |
| `asian_range_gte_30` | 7 | S_STRANGER | 30.4% | 42.9% | 42.9% | 42.9% | +4.5 | 3.67 | 3.67 | +12.5 | +4.7 |
| `confluence_gte_60` | 15 | S_STRANGER | 65.2% | 20.0% | 20.0% | 6.7% | -4.6 | 0.22 | 0.87 | +5.2 | +8.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 21.7% | 40.0% | 40.0% | 0.0% | +0.0 | 1.01 | 1.52 | +7.4 | +6.4 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 52.2% | 33.3% | 33.3% | 8.3% | +0.8 | 1.19 | 2.39 | +7.9 | +7.7 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 30.4% | 42.9% | 42.9% | 42.9% | +4.5 | 3.67 | 3.67 | +12.5 | +4.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 4.3% | 100.0% | 100.0% | 0.0% | +12.2 | 999.00 | 999.00 | +18.8 | +4.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 95.7% | 22.7% | 22.7% | 13.6% | -1.5 | 0.67 | 2.15 | +6.6 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 13.0% | -1.6 | 0.64 | 2.19 | +6.4 | +7.4 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 34.8% | 12.5% | 12.5% | 12.5% | -4.8 | 0.08 | 0.53 | +5.0 | +7.1 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 13.0% | 0.0% | 0.0% | 0.0% | -7.6 | 0.00 | 0.00 | +2.6 | +9.7 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+3.5; validation N=4 Fav=25.0% Avg=+5.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | +0.2 | 1.04 | 3.46 | +9.1 | +4.7 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 85.7% | 20.8% | 20.8% | 20.8% | -0.1 | 0.98 | 3.33 | +9.2 | +4.1 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 92.9% | 23.1% | 23.1% | 23.1% | +0.4 | 1.11 | 3.33 | +9.5 | +4.5 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | +0.2 | 1.04 | 3.46 | +9.1 | +4.7 |
| `asian_range_gte_30` | 11 | S_STRANGER | 39.3% | 18.2% | 18.2% | 18.2% | -3.9 | 0.26 | 1.05 | +5.6 | +5.3 |
| `confluence_gte_60` | 26 | S_STRANGER | 92.9% | 19.2% | 19.2% | 23.1% | -0.4 | 0.89 | 3.39 | +8.7 | +4.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 71.4% | 30.0% | 30.0% | 30.0% | +2.5 | 1.82 | 3.64 | +11.0 | +4.7 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 21.4% | 33.3% | 33.3% | 16.7% | +5.1 | 2.68 | 5.36 | +10.2 | +7.1 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 39.3% | 18.2% | 18.2% | 18.2% | -3.9 | 0.26 | 1.05 | +5.6 | +5.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 28.6% | 25.0% | 25.0% | 25.0% | -2.4 | 0.44 | 1.10 | +6.5 | +5.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | +0.2 | 1.04 | 3.46 | +9.1 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | +0.2 | 1.04 | 3.46 | +9.1 | +4.7 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 35.7% | 20.0% | 20.0% | 20.0% | -1.8 | 0.45 | 1.58 | +4.8 | +4.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.6% | 0.0% | 0.0% | 0.0% | -9.5 | 0.00 | 0.00 | +1.8 | +10.0 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=33.3% Avg=+1.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 7.1% | -1.7 | 0.66 | 2.32 | +7.8 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 78.6% | 22.7% | 22.7% | 9.1% | -2.2 | 0.60 | 1.93 | +8.4 | +8.3 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 96.4% | 22.2% | 22.2% | 7.4% | -1.6 | 0.68 | 2.28 | +8.1 | +7.7 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 7.1% | -1.7 | 0.66 | 2.32 | +7.8 | +7.7 |
| `asian_range_gte_30` | 9 | S_STRANGER | 32.1% | 33.3% | 33.3% | 0.0% | +1.8 | 1.41 | 2.81 | +10.2 | +7.5 |
| `confluence_gte_60` | 26 | S_STRANGER | 92.9% | 23.1% | 23.1% | 7.7% | -1.7 | 0.68 | 2.15 | +8.1 | +7.7 |
| `confluence_gte_70` | 7 | S_STRANGER | 25.0% | 14.3% | 14.3% | 0.0% | -4.6 | 0.35 | 2.08 | +7.8 | +7.8 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 32.1% | 22.2% | 22.2% | 0.0% | -1.4 | 0.75 | 2.63 | +9.0 | +8.2 |
| `tdi_rsi_gte_50` | 21 | S_STRANGER | 75.0% | 19.0% | 19.0% | 0.0% | -1.8 | 0.68 | 2.90 | +8.1 | +8.1 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 32.1% | 33.3% | 33.3% | 0.0% | +1.8 | 1.41 | 2.81 | +10.2 | +7.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 7.1% | 50.0% | 50.0% | 0.0% | +10.1 | 16.54 | 16.54 | +17.1 | +4.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 96.4% | 22.2% | 22.2% | 7.4% | -1.6 | 0.68 | 2.27 | +8.0 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 82.1% | 21.7% | 21.7% | 8.7% | -2.3 | 0.58 | 1.99 | +7.8 | +8.5 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 17.9% | 20.0% | 20.0% | 20.0% | -4.1 | 0.13 | 0.52 | +7.7 | +8.0 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 28.6% | 12.5% | 12.5% | 0.0% | -3.0 | 0.41 | 2.88 | +7.5 | +6.5 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=25.0% Avg=+1.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=50.0% Avg=+8.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -5.8 | 0.38 | 1.41 | +7.3 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 11.1% | -3.8 | 0.44 | 1.53 | +6.9 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 7.7% | -8.0 | 0.20 | 1.11 | +5.9 | +4.6 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -5.8 | 0.38 | 1.41 | +7.3 | +4.3 |
| `asian_range_gte_30` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 0.0% | -18.5 | 0.11 | 0.44 | +5.9 | +5.8 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -5.8 | 0.38 | 1.41 | +7.3 | +4.3 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -5.8 | 0.38 | 1.41 | +7.3 | +4.3 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 78.6% | 18.2% | 18.2% | 9.1% | -7.4 | 0.30 | 1.36 | +7.1 | +4.1 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 42.9% | 33.3% | 33.3% | 16.7% | +3.6 | 2.56 | 5.12 | +9.7 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 0.0% | -8.4 | 0.25 | 0.76 | +6.4 | +7.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 0.0% | -8.4 | 0.25 | 0.76 | +6.4 | +7.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 92.9% | 23.1% | 23.1% | 15.4% | -6.1 | 0.39 | 1.30 | +7.4 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -5.8 | 0.38 | 1.41 | +7.3 | +4.3 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 0.0% | +0.9 | 1.30 | 2.60 | +6.8 | +4.9 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 0.0% | +2.4 | 2.69 | 5.38 | +9.3 | +5.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=33.3% Avg=+4.8; out_of_sample N=3 Fav=0.0% Avg=-4.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 5.3% | -0.0 | 0.99 | 2.77 | +5.8 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 36.8% | 14.3% | 14.3% | 0.0% | -3.3 | 0.22 | 1.33 | +3.6 | +8.1 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 63.2% | 8.3% | 16.7% | 0.0% | -2.3 | 0.27 | 1.36 | +3.1 | +7.2 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 5.3% | -0.0 | 0.99 | 2.77 | +5.8 | +5.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 5.3% | -0.0 | 0.99 | 2.77 | +5.8 | +5.6 |
| `confluence_gte_70` | 6 | S_STRANGER | 31.6% | 16.7% | 16.7% | 16.7% | +0.2 | 1.06 | 5.32 | +8.1 | +6.1 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 57.9% | 18.2% | 18.2% | 0.0% | -2.3 | 0.24 | 1.07 | +4.7 | +6.6 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 47.4% | 22.2% | 22.2% | 0.0% | -1.6 | 0.35 | 1.21 | +5.6 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 5.3% | -0.0 | 0.99 | 2.77 | +5.8 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 5.3% | -0.0 | 0.99 | 2.77 | +5.8 | +5.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=-1.2; validation N=6 Fav=16.7% Avg=-3.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 26.3% | -2.6 | 0.41 | 1.06 | +5.1 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 68.4% | 15.4% | 23.1% | 15.4% | -3.6 | 0.18 | 0.59 | +5.1 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 84.2% | 18.8% | 25.0% | 25.0% | -2.8 | 0.30 | 0.82 | +5.1 | +6.6 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 26.3% | -2.6 | 0.41 | 1.06 | +5.1 | +6.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 63.2% | 16.7% | 25.0% | 16.7% | -3.2 | 0.39 | 1.17 | +4.1 | +6.6 |
| `confluence_gte_70` | 2 | S_STRANGER | 10.5% | 0.0% | 0.0% | 0.0% | -3.3 | 0.00 | 0.00 | +3.1 | +7.4 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 57.9% | 18.2% | 18.2% | 27.3% | -4.5 | 0.15 | 0.62 | +5.0 | +8.3 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 52.6% | 30.0% | 30.0% | 30.0% | -2.7 | 0.47 | 1.09 | +6.4 | +8.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 26.3% | -2.6 | 0.41 | 1.06 | +5.1 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 26.3% | -2.6 | 0.41 | 1.06 | +5.1 | +6.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 15.8% | 33.3% | 33.3% | 33.3% | -1.6 | 0.47 | 0.93 | +6.8 | +4.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 5.3% | 100.0% | 100.0% | 100.0% | +4.2 | 999.00 | 999.00 | +15.6 | +3.2 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.4; validation N=5 Fav=40.0% Avg=+5.6; out_of_sample N=4 Fav=0.0% Avg=-1.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +2.1 | 2.75 | 9.61 | +10.3 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +2.1 | 2.75 | 9.61 | +10.3 | +3.3 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +2.1 | 2.75 | 9.61 | +10.3 | +3.3 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +2.1 | 2.75 | 9.61 | +10.3 | +3.3 |
| `asian_range_gte_30` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +4.1 | 7.31 | 7.31 | +18.3 | +4.5 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +2.1 | 2.75 | 9.61 | +10.3 | +3.3 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +2.1 | 2.75 | 9.61 | +10.3 | +3.3 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +6.0 | +3.9 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 16.7% | +0.6 | 1.61 | 6.44 | +9.6 | +3.3 |
| `ratio_le_2_and_asian_gte_30` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +4.1 | 7.31 | 7.31 | +18.3 | +4.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +8.2 | +8.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +2.1 | 2.75 | 9.61 | +10.3 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +2.1 | 2.75 | 9.61 | +10.3 | +3.3 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.4 | 0.00 | 0.00 | +3.1 | +2.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.4 | 0.00 | 0.00 | +3.1 | +2.3 |

### THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=30.0% Avg=+1.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +0.2 | 1.08 | 4.33 | +5.5 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 66.7% | 30.0% | 30.0% | 30.0% | +1.7 | 1.87 | 4.37 | +7.2 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +0.2 | 1.08 | 4.33 | +5.5 | +3.9 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +0.2 | 1.08 | 4.33 | +5.5 | +3.9 |
| `asian_range_gte_30` | 5 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -2.9 | 0.00 | 0.00 | +2.9 | +4.9 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +0.2 | 1.08 | 4.33 | +5.5 | +3.9 |
| `confluence_gte_70` | 6 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +3.6 | +4.0 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 46.7% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +3.7 | +5.4 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 46.7% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +3.7 | +5.4 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -2.9 | 0.00 | 0.00 | +2.9 | +4.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +3.4 | +6.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 93.3% | 21.4% | 21.4% | 21.4% | +0.4 | 1.21 | 4.42 | +5.8 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +0.2 | 1.08 | 4.33 | +5.5 | +3.9 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 53.3% | 25.0% | 25.0% | 25.0% | +0.4 | 1.14 | 3.42 | +5.9 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +4.2 | +6.2 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+0.2; validation N=1 Fav=0.0% Avg=-0.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -1.0 | 0.75 | 3.00 | +5.0 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 0.0% | -0.7 | 0.84 | 2.53 | +6.1 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -1.0 | 0.75 | 3.00 | +5.0 | +6.1 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -1.0 | 0.75 | 3.00 | +5.0 | +6.1 |
| `asian_range_gte_30` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -2.3 | 0.63 | 3.15 | +5.2 | +7.8 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -1.0 | 0.75 | 3.00 | +5.0 | +6.1 |
| `confluence_gte_70` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +0.3 | +5.0 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 0.0% | +0.2 | 1.04 | 2.61 | +6.8 | +6.5 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 0.0% | +0.2 | 1.04 | 2.61 | +6.8 | +6.5 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -2.3 | 0.63 | 3.15 | +5.2 | +7.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | -0.6 | 0.92 | 1.85 | +9.6 | +10.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 0.0% | -0.7 | 0.82 | 2.88 | +5.5 | +6.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -1.0 | 0.75 | 3.00 | +5.0 | +6.1 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -0.4 | 0.91 | 4.57 | +5.8 | +6.4 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | +1.5 | 1.35 | 4.04 | +8.4 | +6.8 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+4.5; validation N=1 Fav=0.0% Avg=-2.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 23.3% | -1.2 | 0.71 | 2.13 | +7.7 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 27 | S_STRANGER | 90.0% | 22.2% | 22.2% | 25.9% | +1.0 | 1.45 | 3.62 | +7.8 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 96.7% | 20.7% | 20.7% | 24.1% | +0.6 | 1.23 | 3.49 | +7.4 | +5.0 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 23.3% | -1.2 | 0.71 | 2.13 | +7.7 | +7.0 |
| `asian_range_gte_30` | 6 | S_STRANGER | 20.0% | 33.3% | 33.3% | 16.7% | +3.4 | 4.47 | 6.71 | +11.2 | +5.6 |
| `confluence_gte_60` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 23.3% | -1.2 | 0.71 | 2.13 | +7.7 | +7.0 |
| `confluence_gte_70` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 23.3% | -1.2 | 0.71 | 2.13 | +7.7 | +7.0 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 50.0% | 20.0% | 20.0% | 26.7% | +0.5 | 1.20 | 3.59 | +8.3 | +5.2 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 60.0% | 22.2% | 22.2% | 27.8% | -1.7 | 0.65 | 1.63 | +9.6 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 20.0% | 33.3% | 33.3% | 16.7% | +3.4 | 4.47 | 6.71 | +11.2 | +5.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 10.0% | 0.0% | 0.0% | 33.3% | -1.3 | 0.00 | 0.00 | +8.1 | +3.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 23.3% | -1.2 | 0.71 | 2.13 | +7.7 | +7.0 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 20.0% | 20.0% | 23.3% | -1.2 | 0.71 | 2.13 | +7.7 | +7.0 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -5.1 | 0.00 | 0.00 | +2.2 | +5.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+9.2; validation N=3 Fav=33.3% Avg=-5.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 20.0% | 22.9% | 20.0% | -2.8 | 0.50 | 1.38 | +7.3 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 28 | S_STRANGER | 80.0% | 21.4% | 25.0% | 21.4% | -3.2 | 0.50 | 1.21 | +7.5 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 33 | S_STRANGER | 94.3% | 21.2% | 24.2% | 21.2% | -2.7 | 0.53 | 1.32 | +7.6 | +5.1 |
| `stop_hunt_le_90` | 35 | S_STRANGER | 100.0% | 20.0% | 22.9% | 20.0% | -2.8 | 0.50 | 1.38 | +7.3 | +5.0 |
| `asian_range_gte_30` | 6 | R_REPEATER | 17.1% | 50.0% | 66.7% | 50.0% | +1.8 | 1.35 | 0.34 | +11.7 | +1.6 |
| `confluence_gte_60` | 16 | S_STRANGER | 45.7% | 31.2% | 37.5% | 25.0% | +0.5 | 1.10 | 1.47 | +9.7 | +5.0 |
| `confluence_gte_70` | 2 | R_REPEATER | 5.7% | 50.0% | 50.0% | 0.0% | +0.2 | 1.03 | 1.03 | +10.1 | +13.5 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 20.0% | 28.6% | 28.6% | 28.6% | +2.0 | 1.62 | 4.05 | +9.7 | +5.2 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 57.1% | 30.0% | 30.0% | 20.0% | +1.5 | 1.59 | 2.91 | +9.7 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 17.1% | 50.0% | 66.7% | 50.0% | +1.8 | 1.35 | 0.34 | +11.7 | +1.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 2.9% | 100.0% | 100.0% | 100.0% | +7.1 | 999.00 | 999.00 | +19.3 | +3.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 34 | S_STRANGER | 97.1% | 20.6% | 23.5% | 20.6% | -2.7 | 0.51 | 1.34 | +7.4 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 34 | S_STRANGER | 97.1% | 17.6% | 20.6% | 17.6% | -3.4 | 0.40 | 1.25 | +6.9 | +5.1 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 14.3% | 40.0% | 40.0% | 40.0% | +6.4 | 2.75 | 4.12 | +12.0 | +5.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_RUNNER | 5.7% | 100.0% | 100.0% | 100.0% | +25.0 | 999.00 | 999.00 | +26.1 | +0.9 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+9.8; validation N=5 Fav=20.0% Avg=-4.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -3.0 | 0.39 | 0.92 | +4.7 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 60.0% | 33.3% | 50.0% | 33.3% | -1.7 | 0.65 | 0.65 | +6.3 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 70.0% | 28.6% | 42.9% | 28.6% | -1.6 | 0.63 | 0.84 | +5.8 | +5.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -3.0 | 0.39 | 0.92 | +4.7 | +5.6 |
| `asian_range_gte_30` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +9.1 | 999.00 | 999.00 | +15.4 | +8.3 |
| `confluence_gte_60` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +2.2 | +9.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | -3.1 | 0.37 | 1.49 | +4.7 | +8.0 |
| `ratio_le_2_and_asian_gte_30` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +9.1 | 999.00 | 999.00 | +15.4 | +8.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -3.0 | 0.39 | 0.92 | +4.7 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | -3.0 | 0.39 | 0.92 | +4.7 | +5.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=25.0% Avg=-3.9; validation N=2 Fav=0.0% Avg=-0.8; out_of_sample N=3 Fav=33.3% Avg=-3.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 33.3% | -3.8 | 0.19 | 0.62 | +6.3 | +5.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 86.7% | 23.1% | 23.1% | 38.5% | -3.4 | 0.23 | 0.61 | +6.5 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 93.3% | 21.4% | 21.4% | 35.7% | -3.2 | 0.23 | 0.68 | +6.8 | +5.2 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 33.3% | -3.8 | 0.19 | 0.62 | +6.3 | +5.1 |
| `asian_range_gte_30` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -5.1 | 0.16 | 0.32 | +9.3 | +8.5 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 33.3% | -3.8 | 0.19 | 0.62 | +6.3 | +5.1 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 33.3% | -3.8 | 0.19 | 0.62 | +6.3 | +5.1 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 73.3% | 9.1% | 9.1% | 27.3% | -4.2 | 0.06 | 0.47 | +6.3 | +5.7 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 26.7% | 25.0% | 25.0% | 25.0% | -2.4 | 0.24 | 0.71 | +11.3 | +4.5 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -5.1 | 0.16 | 0.32 | +9.3 | +8.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 50.0% | -4.0 | 0.27 | 0.27 | +12.7 | +7.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 33.3% | -3.8 | 0.19 | 0.62 | +6.3 | +5.1 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 33.3% | -3.8 | 0.19 | 0.62 | +6.3 | +5.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 33.3% | -5.3 | 0.00 | 0.00 | +2.8 | +6.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +9.8 | +1.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=42.9% Avg=+6.9; validation N=9 Fav=22.2% Avg=-4.5; out_of_sample N=3 Fav=33.3% Avg=+1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 42 | S_STRANGER | 100.0% | 19.0% | 19.0% | 31.0% | -2.1 | 0.58 | 1.89 | +7.9 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 73.8% | 19.4% | 19.4% | 35.5% | -2.0 | 0.61 | 1.84 | +8.4 | +6.0 |
| `hunt_to_ar_ratio_le_2_5` | 36 | S_STRANGER | 85.7% | 19.4% | 19.4% | 33.3% | -2.0 | 0.62 | 1.96 | +8.2 | +5.8 |
| `stop_hunt_le_90` | 42 | S_STRANGER | 100.0% | 19.0% | 19.0% | 31.0% | -2.1 | 0.58 | 1.89 | +7.9 | +6.1 |
| `asian_range_gte_30` | 7 | S_STRANGER | 16.7% | 28.6% | 28.6% | 42.9% | +3.2 | 2.99 | 4.49 | +13.5 | +4.0 |
| `confluence_gte_60` | 38 | S_STRANGER | 90.5% | 15.8% | 15.8% | 28.9% | -3.2 | 0.41 | 1.65 | +7.4 | +6.2 |
| `confluence_gte_70` | 6 | S_STRANGER | 14.3% | 16.7% | 16.7% | 33.3% | +2.5 | 2.59 | 7.77 | +9.9 | +5.8 |
| `tdi_rsi_gt_signal` | 32 | S_STRANGER | 76.2% | 21.9% | 21.9% | 28.1% | -1.2 | 0.76 | 2.17 | +8.9 | +6.1 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 45.2% | 31.6% | 31.6% | 26.3% | +0.7 | 1.16 | 2.32 | +11.0 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 16.7% | 28.6% | 28.6% | 42.9% | +3.2 | 2.99 | 4.49 | +13.5 | +4.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 16.7% | 28.6% | 28.6% | 42.9% | +3.2 | 2.99 | 4.49 | +13.5 | +4.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 42 | S_STRANGER | 100.0% | 19.0% | 19.0% | 31.0% | -2.1 | 0.58 | 1.89 | +7.9 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 41 | S_STRANGER | 97.6% | 19.5% | 19.5% | 31.7% | -2.0 | 0.60 | 1.87 | +8.0 | +6.0 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 9.5% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +6.1 | +6.1 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +7.0 | +6.1 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=20.0% Avg=-2.2; validation N=6 Fav=33.3% Avg=+0.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 19.0% | 19.0% | 23.8% | -2.6 | 0.38 | 1.44 | +4.4 | +5.1 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 76.2% | 25.0% | 25.0% | 31.2% | -1.2 | 0.64 | 1.60 | +4.9 | +3.8 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 90.5% | 21.1% | 21.1% | 26.3% | -1.9 | 0.48 | 1.57 | +4.5 | +4.4 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 19.0% | 19.0% | 23.8% | -2.6 | 0.38 | 1.44 | +4.4 | +5.1 |
| `asian_range_gte_30` | 2 | R_REPEATER | 9.5% | 50.0% | 50.0% | 50.0% | +3.6 | 2.28 | 2.28 | +7.1 | +5.7 |
| `confluence_gte_60` | 13 | S_STRANGER | 61.9% | 15.4% | 15.4% | 15.4% | -1.7 | 0.47 | 2.36 | +4.0 | +5.5 |
| `confluence_gte_70` | 4 | S_STRANGER | 19.0% | 25.0% | 25.0% | 25.0% | +2.1 | 2.89 | 8.67 | +5.5 | +4.5 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 9.5% | 0.0% | 0.0% | 0.0% | -7.1 | 0.00 | 0.00 | +0.5 | +7.6 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 52.4% | 18.2% | 18.2% | 18.2% | -1.2 | 0.52 | 2.07 | +4.7 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 2 | R_REPEATER | 9.5% | 50.0% | 50.0% | 50.0% | +3.6 | 2.28 | 2.28 | +7.1 | +5.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +1.0 | +6.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 19.0% | 19.0% | 23.8% | -2.6 | 0.38 | 1.44 | +4.4 | +5.1 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 19.0% | 19.0% | 23.8% | -2.6 | 0.38 | 1.44 | +4.4 | +5.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=14.3% Avg=-1.7; validation N=11 Fav=27.3% Avg=-1.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 18.8% | 21.9% | 21.9% | -1.4 | 0.57 | 1.88 | +6.3 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 62.5% | 15.0% | 20.0% | 20.0% | -2.2 | 0.40 | 1.40 | +5.2 | +5.3 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 68.8% | 18.2% | 22.7% | 22.7% | -1.8 | 0.48 | 1.45 | +5.5 | +5.0 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 100.0% | 18.8% | 21.9% | 21.9% | -1.4 | 0.57 | 1.88 | +6.3 | +5.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 50.0% | 18.8% | 25.0% | 18.8% | -1.0 | 0.72 | 1.99 | +5.2 | +5.3 |
| `confluence_gte_70` | 4 | R_REPEATER | 12.5% | 50.0% | 50.0% | 25.0% | +3.1 | 1.78 | 1.78 | +10.1 | +5.9 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 56.2% | 22.2% | 27.8% | 22.2% | -1.4 | 0.66 | 1.58 | +6.1 | +4.9 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 56.2% | 22.2% | 22.2% | 22.2% | -1.2 | 0.65 | 2.11 | +7.6 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 3.1% | 0.0% | 0.0% | 0.0% | -7.4 | 0.00 | 0.00 | +1.3 | +7.6 |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 96.9% | 19.4% | 22.6% | 22.6% | -1.3 | 0.61 | 1.93 | +6.5 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 18.8% | 21.9% | 21.9% | -1.4 | 0.57 | 1.88 | +6.3 | +5.0 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 9.4% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +2.0 | +4.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.1% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +0.8 | +3.8 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=25.0% Avg=+1.8; out_of_sample N=1 Fav=100.0% Avg=+8.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 43 | S_STRANGER | 100.0% | 18.6% | 20.9% | 23.3% | -1.9 | 0.49 | 1.48 | +5.6 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 72.1% | 16.1% | 19.4% | 22.6% | -1.8 | 0.47 | 1.50 | +4.9 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 37 | S_STRANGER | 86.0% | 16.2% | 18.9% | 24.3% | -2.5 | 0.40 | 1.32 | +4.9 | +4.8 |
| `stop_hunt_le_90` | 43 | S_STRANGER | 100.0% | 18.6% | 20.9% | 23.3% | -1.9 | 0.49 | 1.48 | +5.6 | +4.8 |
| `asian_range_gte_30` | 3 | S_STRANGER | 7.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +4.0 | +7.8 |
| `confluence_gte_60` | 38 | S_STRANGER | 88.4% | 18.4% | 21.1% | 23.7% | -1.5 | 0.56 | 1.68 | +5.6 | +4.1 |
| `confluence_gte_70` | 5 | S_STRANGER | 11.6% | 40.0% | 40.0% | 80.0% | +3.1 | 3.36 | 1.68 | +7.9 | +3.1 |
| `tdi_rsi_gt_signal` | 25 | S_STRANGER | 58.1% | 20.0% | 24.0% | 12.0% | -2.7 | 0.46 | 1.38 | +6.3 | +4.9 |
| `tdi_rsi_gte_50` | 21 | S_STRANGER | 48.8% | 28.6% | 33.3% | 9.5% | -0.7 | 0.81 | 1.63 | +7.3 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 7.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +4.0 | +7.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 7.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +4.0 | +7.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 43 | S_STRANGER | 100.0% | 18.6% | 20.9% | 23.3% | -1.9 | 0.49 | 1.48 | +5.6 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 43 | S_STRANGER | 100.0% | 18.6% | 20.9% | 23.3% | -1.9 | 0.49 | 1.48 | +5.6 | +4.8 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 4.7% | 50.0% | 50.0% | 0.0% | +5.2 | 999.00 | 999.00 | +8.3 | +2.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 2.3% | 100.0% | 100.0% | 0.0% | +10.5 | 999.00 | 999.00 | +12.6 | +0.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=28.6% Avg=+1.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | +0.5 | 1.38 | 3.23 | +4.7 | +4.5 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 36.4% | 25.0% | 50.0% | 0.0% | +0.2 | 1.20 | 1.20 | +2.7 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 54.5% | 16.7% | 33.3% | 0.0% | -0.7 | 0.54 | 1.09 | +1.8 | +5.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | +0.5 | 1.38 | 3.23 | +4.7 | +4.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | +0.5 | 1.38 | 3.23 | +4.7 | +4.5 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | +0.5 | 1.38 | 3.23 | +4.7 | +4.5 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 54.5% | 16.7% | 16.7% | 16.7% | -1.4 | 0.18 | 0.72 | +3.4 | +6.3 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 28.6% | +1.5 | 2.42 | 4.84 | +6.8 | +3.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | +0.5 | 1.38 | 3.23 | +4.7 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | +0.5 | 1.38 | 3.23 | +4.7 | +4.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=12.5% Avg=-2.9; validation N=3 Fav=33.3% Avg=+3.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -1.2 | 0.57 | 2.00 | +7.5 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 16.7% | -3.3 | 0.00 | 0.00 | +6.6 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 22.2% | -2.3 | 0.13 | 0.79 | +7.2 | +4.7 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -1.2 | 0.57 | 2.00 | +7.5 | +4.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 20.0% | -2.9 | 0.10 | 0.70 | +6.7 | +5.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +6.4 | +5.6 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +5.4 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 20.0% | -1.7 | 0.47 | 3.30 | +7.0 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -1.2 | 0.57 | 2.00 | +7.5 | +4.9 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 50.0% | -1.9 | 0.30 | 0.59 | +7.8 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=0.0% Avg=-3.9; validation N=1 Fav=100.0% Avg=+13.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -2.7 | 0.39 | 1.84 | +6.4 | +7.8 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -2.7 | 0.39 | 1.84 | +6.4 | +7.8 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -2.7 | 0.39 | 1.84 | +6.4 | +7.8 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -2.7 | 0.39 | 1.84 | +6.4 | +7.8 |
| `asian_range_gte_30` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 14.3% | -3.4 | 0.37 | 2.20 | +7.2 | +8.2 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -2.7 | 0.39 | 1.84 | +6.4 | +7.8 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -2.7 | 0.39 | 1.84 | +6.4 | +7.8 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 14.3% | -5.2 | 0.10 | 0.62 | +3.9 | +7.8 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 52.9% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +5.9 | +8.6 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 14.3% | -3.4 | 0.37 | 2.20 | +7.2 | +8.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 0.0% | -9.0 | 0.00 | 0.00 | +3.6 | +10.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -2.7 | 0.39 | 1.84 | +6.4 | +7.8 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -2.7 | 0.39 | 1.84 | +6.4 | +7.8 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 29.4% | 20.0% | 20.0% | 20.0% | -0.3 | 0.89 | 3.56 | +6.2 | +7.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +1.2 | +10.1 |

### THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-0.7; validation N=2 Fav=50.0% Avg=+4.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -1.9 | 0.37 | 1.48 | +5.4 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -1.9 | 0.37 | 1.48 | +5.4 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -1.9 | 0.37 | 1.48 | +5.4 | +5.6 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -1.9 | 0.37 | 1.48 | +5.4 | +5.6 |
| `asian_range_gte_30` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 28.6% | +0.8 | 1.66 | 2.49 | +8.6 | +4.7 |
| `confluence_gte_60` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 16.7% | -0.8 | 0.74 | 1.11 | +8.5 | +5.9 |
| `confluence_gte_70` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +1.7 | 999.00 | 999.00 | +16.2 | +2.3 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 0.0% | -0.0 | 0.99 | 1.98 | +5.7 | +6.6 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 0.0% | -2.1 | 0.49 | 2.46 | +5.1 | +7.1 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 28.6% | +0.8 | 1.66 | 2.49 | +8.6 | +4.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 0.0% | +4.5 | 4.10 | 4.10 | +8.5 | +5.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -1.9 | 0.37 | 1.48 | +5.4 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -1.9 | 0.37 | 1.48 | +5.4 | +5.6 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 58.3% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +3.2 | +6.5 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +3.8 | +8.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=22.2% Avg=+0.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -2.2 | 0.44 | 2.00 | +5.5 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +5.2 | +8.0 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 58.3% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +4.4 | +8.0 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -2.2 | 0.44 | 2.00 | +5.5 | +6.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 10.0% | -2.5 | 0.46 | 1.60 | +5.6 | +7.0 |
| `confluence_gte_70` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +6.9 | +3.8 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -0.2 | 0.00 | 0.00 | +2.0 | +7.6 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 11.1% | +0.2 | 1.07 | 3.21 | +6.5 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -2.2 | 0.44 | 2.00 | +5.5 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -2.2 | 0.44 | 2.00 | +5.5 | +6.6 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -0.1 | 0.00 | 0.00 | +2.5 | +4.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -0.1 | 0.00 | 0.00 | +2.5 | +4.9 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=37.5% Avg=+8.0; validation N=4 Fav=25.0% Avg=+2.2; out_of_sample N=1 Fav=0.0% Avg=-3.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -2.5 | 0.66 | 3.30 | +8.0 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -2.5 | 0.66 | 3.30 | +8.0 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -2.5 | 0.66 | 3.30 | +8.0 | +6.7 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -2.5 | 0.66 | 3.30 | +8.0 | +6.7 |
| `asian_range_gte_30` | 12 | S_STRANGER | 50.0% | 25.0% | 25.0% | 0.0% | -1.2 | 0.87 | 2.62 | +11.5 | +5.3 |
| `confluence_gte_60` | 20 | S_STRANGER | 83.3% | 20.0% | 20.0% | 0.0% | -1.1 | 0.85 | 3.39 | +9.2 | +6.9 |
| `confluence_gte_70` | 4 | S_STRANGER | 16.7% | 25.0% | 25.0% | 0.0% | +3.2 | 1.72 | 5.15 | +10.7 | +6.4 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 45.8% | 27.3% | 27.3% | 0.0% | +4.7 | 2.47 | 6.59 | +11.8 | +8.1 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 54.2% | 30.8% | 30.8% | 0.0% | +5.3 | 2.45 | 5.52 | +12.5 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 50.0% | 25.0% | 25.0% | 0.0% | -1.2 | 0.87 | 2.62 | +11.5 | +5.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 16.7% | 50.0% | 50.0% | 0.0% | +13.9 | 6.05 | 6.05 | +22.3 | +7.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -2.5 | 0.66 | 3.30 | +8.0 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -2.5 | 0.66 | 3.30 | +8.0 | +6.7 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 20.8% | 0.0% | 0.0% | 0.0% | -8.5 | 0.00 | 0.00 | +2.6 | +4.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -4.8 | 0.00 | 0.00 | +2.6 | +7.8 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-2.8; validation N=4 Fav=50.0% Avg=-4.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -4.5 | 0.23 | 1.00 | +4.3 | +5.8 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 88.9% | 18.8% | 18.8% | 18.8% | -2.9 | 0.35 | 1.27 | +4.5 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -4.5 | 0.23 | 1.00 | +4.3 | +5.8 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -4.5 | 0.23 | 1.00 | +4.3 | +5.8 |
| `asian_range_gte_30` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 66.7% | +3.2 | 9.73 | 9.73 | +8.4 | +12.2 |
| `confluence_gte_60` | 14 | S_STRANGER | 77.8% | 14.3% | 14.3% | 7.1% | -6.2 | 0.14 | 0.76 | +3.6 | +6.0 |
| `confluence_gte_70` | 7 | S_STRANGER | 38.9% | 14.3% | 14.3% | 0.0% | -9.3 | 0.01 | 0.08 | +1.9 | +2.6 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 55.6% | 10.0% | 10.0% | 0.0% | -5.5 | 0.19 | 1.71 | +4.2 | +4.4 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | 33.3% | 33.3% | 0.0% | -3.6 | 0.39 | 0.78 | +5.6 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 66.7% | +3.2 | 9.73 | 9.73 | +8.4 | +12.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +5.0 | +8.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -4.5 | 0.23 | 1.00 | +4.3 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -4.5 | 0.23 | 1.00 | +4.3 | +5.8 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 66.7% | +3.2 | 9.73 | 9.73 | +8.0 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +5.0 | +8.6 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+4.9; validation N=12 Fav=16.7% Avg=-2.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 38 | S_STRANGER | 100.0% | 15.8% | 18.4% | 15.8% | -1.7 | 0.56 | 2.33 | +5.4 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 27 | S_STRANGER | 71.1% | 7.4% | 7.4% | 11.1% | -4.0 | 0.10 | 1.14 | +3.7 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 33 | S_STRANGER | 86.8% | 12.1% | 15.2% | 12.1% | -2.4 | 0.39 | 2.02 | +4.9 | +4.9 |
| `stop_hunt_le_90` | 38 | S_STRANGER | 100.0% | 15.8% | 18.4% | 15.8% | -1.7 | 0.56 | 2.33 | +5.4 | +4.9 |
| `asian_range_gte_30` | 10 | S_STRANGER | 26.3% | 0.0% | 0.0% | 10.0% | -3.8 | 0.00 | 0.00 | +5.0 | +7.3 |
| `confluence_gte_60` | 11 | S_STRANGER | 28.9% | 0.0% | 0.0% | 18.2% | -2.5 | 0.00 | 0.00 | +5.2 | +5.8 |
| `confluence_gte_70` | 2 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +3.0 | +8.9 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 47.4% | 27.8% | 27.8% | 22.2% | +0.0 | 1.01 | 2.43 | +6.8 | +5.7 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 23.7% | 11.1% | 11.1% | 0.0% | -1.5 | 0.49 | 3.91 | +5.3 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 26.3% | 0.0% | 0.0% | 10.0% | -3.8 | 0.00 | 0.00 | +5.0 | +7.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 15.8% | 0.0% | 0.0% | 16.7% | -4.9 | 0.00 | 0.00 | +4.3 | +8.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 38 | S_STRANGER | 100.0% | 15.8% | 18.4% | 15.8% | -1.7 | 0.56 | 2.33 | +5.4 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 100.0% | 15.8% | 18.4% | 15.8% | -1.7 | 0.56 | 2.33 | +5.4 | +4.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-4.2; validation N=3 Fav=66.7% Avg=+4.0; out_of_sample N=2 Fav=0.0% Avg=-0.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -2.1 | 0.34 | 1.52 | +7.0 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -2.1 | 0.34 | 1.52 | +7.0 | +5.3 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -2.1 | 0.34 | 1.52 | +7.0 | +5.3 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -2.1 | 0.34 | 1.52 | +7.0 | +5.3 |
| `asian_range_gte_30` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 0.0% | -3.2 | 0.14 | 0.55 | +7.8 | +4.6 |
| `confluence_gte_60` | 9 | S_STRANGER | 69.2% | 22.2% | 22.2% | 33.3% | -0.5 | 0.74 | 1.85 | +8.5 | +4.3 |
| `confluence_gte_70` | 6 | S_STRANGER | 46.2% | 16.7% | 16.7% | 33.3% | -2.4 | 0.15 | 0.46 | +7.6 | +5.6 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 46.2% | 16.7% | 16.7% | 33.3% | -2.1 | 0.48 | 1.91 | +7.2 | +7.3 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 69.2% | 22.2% | 22.2% | 11.1% | -2.9 | 0.35 | 1.23 | +6.8 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 0.0% | -3.2 | 0.14 | 0.55 | +7.8 | +4.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -2.0 | 0.00 | 0.00 | +8.5 | +2.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -2.1 | 0.34 | 1.52 | +7.0 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -2.1 | 0.34 | 1.52 | +7.0 | +5.3 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 30.8% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +4.3 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +4.0 | +7.7 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-1.1; validation N=4 Fav=25.0% Avg=-4.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 30.8% | -4.0 | 0.19 | 0.76 | +5.4 | +7.6 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 61.5% | 0.0% | 0.0% | 25.0% | -4.3 | 0.00 | 0.00 | +3.2 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 76.9% | 20.0% | 20.0% | 30.0% | -2.2 | 0.35 | 1.06 | +4.4 | +4.8 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 30.8% | -4.0 | 0.19 | 0.76 | +5.4 | +7.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 66.7% | +1.5 | 1.77 | 1.77 | +8.9 | +4.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 92.3% | 16.7% | 16.7% | 25.0% | -4.4 | 0.19 | 0.76 | +5.3 | +7.9 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 46.2% | 16.7% | 16.7% | 33.3% | -6.0 | 0.23 | 0.91 | +6.4 | +12.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 30.8% | -4.0 | 0.19 | 0.76 | +5.4 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 30.8% | -4.0 | 0.19 | 0.76 | +5.4 | +7.6 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 66.7% | -1.2 | 0.00 | 0.00 | +5.1 | +3.5 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-1.7; validation N=8 Fav=37.5% Avg=+3.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 80 | S_STRANGER | 100.0% | 15.0% | 20.0% | 16.2% | -1.8 | 0.59 | 2.19 | +6.2 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 71 | S_STRANGER | 88.8% | 15.5% | 19.7% | 16.9% | -1.7 | 0.63 | 2.33 | +6.6 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 77 | S_STRANGER | 96.2% | 15.6% | 20.8% | 16.9% | -1.7 | 0.62 | 2.18 | +6.3 | +5.3 |
| `stop_hunt_le_90` | 80 | S_STRANGER | 100.0% | 15.0% | 20.0% | 16.2% | -1.8 | 0.59 | 2.19 | +6.2 | +5.3 |
| `asian_range_gte_30` | 25 | S_STRANGER | 31.2% | 16.0% | 20.0% | 12.0% | -2.5 | 0.51 | 1.82 | +6.2 | +5.2 |
| `confluence_gte_60` | 37 | S_STRANGER | 46.2% | 27.0% | 32.4% | 16.2% | -0.1 | 0.98 | 2.04 | +8.7 | +6.6 |
| `confluence_gte_70` | 3 | S_STRANGER | 3.8% | 0.0% | 0.0% | 0.0% | -7.9 | 0.00 | 0.00 | +2.8 | +8.7 |
| `tdi_rsi_gt_signal` | 40 | S_STRANGER | 50.0% | 17.5% | 20.0% | 15.0% | +0.2 | 1.06 | 3.96 | +7.1 | +4.5 |
| `tdi_rsi_gte_50` | 46 | S_STRANGER | 57.5% | 21.7% | 21.7% | 15.2% | +0.0 | 1.01 | 3.53 | +7.7 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 31.2% | 16.0% | 20.0% | 12.0% | -2.5 | 0.51 | 1.82 | +6.2 | +5.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 13.8% | 27.3% | 27.3% | 9.1% | +2.1 | 1.59 | 4.23 | +9.8 | +3.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 79 | S_STRANGER | 98.8% | 15.2% | 20.3% | 16.5% | -1.8 | 0.60 | 2.17 | +6.2 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 80 | S_STRANGER | 100.0% | 15.0% | 20.0% | 16.2% | -1.8 | 0.59 | 2.19 | +6.2 | +5.3 |
| `feature_momentum_breakout_exception` | 15 | S_STRANGER | 18.8% | 6.7% | 6.7% | 33.3% | +0.5 | 1.31 | 13.10 | +5.3 | +3.5 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 12.5% | 10.0% | 10.0% | 20.0% | +1.2 | 1.69 | 13.48 | +5.4 | +3.0 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-2.3; validation N=5 Fav=40.0% Avg=+3.4; out_of_sample N=1 Fav=0.0% Avg=-0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -0.7 | 0.74 | 3.70 | +5.0 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 33.3% | +0.8 | 1.34 | 3.36 | +6.6 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 25.0% | -0.1 | 0.98 | 3.90 | +5.7 | +4.5 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -0.7 | 0.74 | 3.70 | +5.0 | +4.8 |
| `asian_range_gte_30` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 50.0% | +6.3 | 10.07 | 10.07 | +11.8 | +4.6 |
| `confluence_gte_60` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 15.4% | -0.7 | 0.74 | 3.70 | +4.8 | +5.1 |
| `confluence_gte_70` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +0.0 | +7.1 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 42.9% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +2.4 | +5.3 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 22.2% | +1.1 | 1.54 | 4.62 | +5.9 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 50.0% | +6.3 | 10.07 | 10.07 | +11.8 | +4.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 23.1% | -0.4 | 0.84 | 3.77 | +5.3 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -0.7 | 0.74 | 3.70 | +5.0 | +4.8 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -4.3 | 0.00 | 0.00 | +1.0 | +5.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -4.3 | 0.00 | 0.00 | +1.0 | +5.2 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+6.5; validation N=1 Fav=100.0% Avg=+12.7; out_of_sample N=5 Fav=20.0% Avg=-9.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 13.3% | 16.7% | 10.0% | -2.8 | 0.45 | 1.97 | +8.6 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 80.0% | 12.5% | 16.7% | 8.3% | -3.3 | 0.41 | 1.73 | +8.5 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 30 | S_STRANGER | 100.0% | 13.3% | 16.7% | 10.0% | -2.8 | 0.45 | 1.97 | +8.6 | +5.9 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 13.3% | 16.7% | 10.0% | -2.8 | 0.45 | 1.97 | +8.6 | +5.9 |
| `asian_range_gte_30` | 14 | S_STRANGER | 46.7% | 21.4% | 21.4% | 14.3% | -2.8 | 0.49 | 1.64 | +10.2 | +6.5 |
| `confluence_gte_60` | 27 | S_STRANGER | 90.0% | 14.8% | 18.5% | 7.4% | -2.7 | 0.48 | 1.93 | +8.6 | +5.1 |
| `confluence_gte_70` | 9 | S_STRANGER | 30.0% | 44.4% | 44.4% | 22.2% | -1.5 | 0.79 | 0.99 | +12.0 | +5.1 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 13.3% | 25.0% | 25.0% | 25.0% | -0.8 | 0.85 | 2.56 | +9.4 | +3.6 |
| `tdi_rsi_gte_50` | 22 | S_STRANGER | 73.3% | 13.6% | 13.6% | 4.5% | -1.0 | 0.64 | 3.60 | +8.6 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 43.3% | 23.1% | 23.1% | 15.4% | -2.5 | 0.54 | 1.61 | +10.6 | +6.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 6.7% | 50.0% | 50.0% | 50.0% | +7.8 | 8.38 | 8.38 | +14.1 | +4.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 96.7% | 13.8% | 17.2% | 10.3% | -2.7 | 0.46 | 1.95 | +8.4 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 13.3% | 16.7% | 10.0% | -2.8 | 0.45 | 1.97 | +8.6 | +5.9 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +8.2 | +8.8 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 23.3% | 14.3% | 14.3% | 0.0% | -1.7 | 0.40 | 2.01 | +11.5 | +7.5 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=23 Fav=13.0% Avg=-3.0; validation N=5 Fav=20.0% Avg=+0.3; out_of_sample N=1 Fav=0.0% Avg=-0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 12.9% | 12.9% | 19.4% | -2.7 | 0.42 | 2.60 | +5.9 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 83.9% | 11.5% | 11.5% | 19.2% | -3.0 | 0.35 | 2.44 | +5.7 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 28 | S_STRANGER | 90.3% | 10.7% | 10.7% | 17.9% | -3.3 | 0.31 | 2.40 | +5.4 | +6.8 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 12.9% | 12.9% | 19.4% | -2.7 | 0.42 | 2.60 | +5.9 | +6.7 |
| `asian_range_gte_30` | 11 | S_STRANGER | 35.5% | 9.1% | 9.1% | 27.3% | -2.8 | 0.37 | 2.92 | +5.9 | +6.9 |
| `confluence_gte_60` | 15 | S_STRANGER | 48.4% | 13.3% | 13.3% | 13.3% | -3.9 | 0.35 | 2.26 | +5.9 | +7.5 |
| `confluence_gte_70` | 5 | S_STRANGER | 16.1% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +4.0 | +7.2 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 29.0% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +3.2 | +7.7 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 51.6% | 6.2% | 6.2% | 6.2% | -4.6 | 0.14 | 2.06 | +4.9 | +7.7 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 35.5% | 9.1% | 9.1% | 27.3% | -2.8 | 0.37 | 2.92 | +5.9 | +6.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 3.2% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +7.9 | +5.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 93.5% | 13.8% | 13.8% | 20.7% | -2.4 | 0.47 | 2.70 | +6.1 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 12.9% | 12.9% | 19.4% | -2.7 | 0.42 | 2.60 | +5.9 | +6.7 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 41.9% | 0.0% | 0.0% | 7.7% | -5.9 | 0.00 | 0.00 | +3.3 | +8.1 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 22.6% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +3.2 | +8.3 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+16.5; validation N=2 Fav=0.0% Avg=-3.7; out_of_sample N=2 Fav=0.0% Avg=-0.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | +0.8 | 1.25 | 4.57 | +7.9 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 93.8% | 6.7% | 13.3% | 13.3% | -2.1 | 0.39 | 2.16 | +5.3 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 93.8% | 6.7% | 13.3% | 13.3% | -2.1 | 0.39 | 2.16 | +5.3 | +5.6 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | +0.8 | 1.25 | 4.57 | +7.9 | +5.4 |
| `asian_range_gte_30` | 10 | S_STRANGER | 62.5% | 0.0% | 0.0% | 20.0% | -3.8 | 0.00 | 0.00 | +4.4 | +6.7 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | +0.8 | 1.25 | 4.57 | +7.9 | +5.4 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | +0.8 | 1.25 | 4.57 | +7.9 | +5.4 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 0.0% | +1.5 | 1.87 | 7.50 | +6.4 | +4.8 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 37.5% | 16.7% | 16.7% | 0.0% | -1.5 | 0.65 | 3.27 | +5.5 | +6.7 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 62.5% | 0.0% | 0.0% | 20.0% | -3.8 | 0.00 | 0.00 | +4.4 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +3.3 | +5.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | +0.8 | 1.25 | 4.57 | +7.9 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 12.5% | 18.8% | 18.8% | +0.8 | 1.25 | 4.57 | +7.9 | +5.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+11.9; validation N=5 Fav=20.0% Avg=-2.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 12.5% | 12.5% | 4.2% | -2.3 | 0.31 | 2.05 | +4.2 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 95.8% | 13.0% | 13.0% | 4.3% | -2.2 | 0.33 | 2.10 | +4.3 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 95.8% | 13.0% | 13.0% | 4.3% | -2.2 | 0.33 | 2.10 | +4.3 | +5.5 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 12.5% | 12.5% | 4.2% | -2.3 | 0.31 | 2.05 | +4.2 | +5.6 |
| `asian_range_gte_30` | 8 | S_STRANGER | 33.3% | 25.0% | 25.0% | 12.5% | -0.3 | 0.87 | 2.18 | +5.4 | +5.5 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 12.5% | 12.5% | 4.2% | -2.3 | 0.31 | 2.05 | +4.2 | +5.6 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 12.5% | 12.5% | 4.2% | -2.3 | 0.31 | 2.05 | +4.2 | +5.6 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 79.2% | 15.8% | 15.8% | 0.0% | -2.5 | 0.34 | 1.80 | +4.0 | +6.2 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 62.5% | 20.0% | 20.0% | 0.0% | -2.3 | 0.42 | 1.67 | +5.0 | +6.6 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 33.3% | 25.0% | 25.0% | 12.5% | -0.3 | 0.87 | 2.18 | +5.4 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 25.0% | 33.3% | 33.3% | 0.0% | +0.1 | 1.05 | 2.10 | +4.6 | +6.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 12.5% | 12.5% | 4.2% | -2.3 | 0.31 | 2.05 | +4.2 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 12.5% | 12.5% | 4.2% | -2.3 | 0.31 | 2.05 | +4.2 | +5.6 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +3.5 | +7.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +3.5 | +7.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.4; validation N=4 Fav=25.0% Avg=+0.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 12.0% | 20.0% | 20.0% | -1.8 | 0.47 | 1.69 | +4.8 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 92.0% | 13.0% | 21.7% | 21.7% | -1.9 | 0.48 | 1.54 | +5.0 | +6.2 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 92.0% | 13.0% | 21.7% | 21.7% | -1.9 | 0.48 | 1.54 | +5.0 | +6.2 |
| `stop_hunt_le_90` | 25 | S_STRANGER | 100.0% | 12.0% | 20.0% | 20.0% | -1.8 | 0.47 | 1.69 | +4.8 | +6.1 |
| `asian_range_gte_30` | 5 | S_STRANGER | 20.0% | 20.0% | 20.0% | 40.0% | +0.2 | 1.11 | 3.32 | +7.4 | +3.3 |
| `confluence_gte_60` | 15 | S_STRANGER | 60.0% | 20.0% | 33.3% | 26.7% | -0.1 | 0.97 | 1.75 | +5.2 | +5.1 |
| `confluence_gte_70` | 6 | S_STRANGER | 24.0% | 16.7% | 33.3% | 33.3% | -2.5 | 0.35 | 0.52 | +5.5 | +6.7 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 80.0% | 15.0% | 20.0% | 20.0% | -1.8 | 0.51 | 1.92 | +5.0 | +6.4 |
| `tdi_rsi_gte_50` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 20.0% | 20.0% | 20.0% | 40.0% | +0.2 | 1.11 | 3.32 | +7.4 | +3.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 16.0% | 25.0% | 25.0% | 50.0% | +0.9 | 1.40 | 2.81 | +9.0 | +3.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 100.0% | 12.0% | 20.0% | 20.0% | -1.8 | 0.47 | 1.69 | +4.8 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 12.0% | 20.0% | 20.0% | -1.8 | 0.47 | 1.69 | +4.8 | +6.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=11.1% Avg=-9.8; validation N=1 Fav=0.0% Avg=-3.6; out_of_sample N=1 Fav=100.0% Avg=+14.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -6.3 | 0.22 | 1.63 | +6.8 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 64.7% | 18.2% | 18.2% | 0.0% | -7.0 | 0.28 | 1.26 | +8.6 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -6.3 | 0.22 | 1.63 | +6.8 | +8.8 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -6.3 | 0.22 | 1.63 | +6.8 | +8.8 |
| `asian_range_gte_30` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -37.6 | 0.00 | 0.00 | +13.6 | +1.8 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -6.3 | 0.22 | 1.63 | +6.8 | +8.8 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -6.3 | 0.22 | 1.63 | +6.8 | +8.8 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 0.0% | -7.5 | 0.22 | 1.35 | +7.3 | +7.6 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 70.6% | 16.7% | 16.7% | 0.0% | -2.9 | 0.46 | 2.32 | +7.3 | +8.5 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -37.6 | 0.00 | 0.00 | +13.6 | +1.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -37.6 | 0.00 | 0.00 | +13.6 | +1.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 76.5% | 15.4% | 15.4% | 0.0% | -7.0 | 0.25 | 1.37 | +7.9 | +8.7 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -6.3 | 0.22 | 1.63 | +6.8 | +8.8 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 47.1% | 12.5% | 12.5% | 0.0% | -9.1 | 0.17 | 1.18 | +5.7 | +8.9 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 0.0% | -3.1 | 0.40 | 2.42 | +5.7 | +9.0 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-6.0; validation N=4 Fav=25.0% Avg=+0.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 11.5% | 11.5% | 26.9% | -2.9 | 0.37 | 2.36 | +5.5 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 100.0% | 11.5% | 11.5% | 26.9% | -2.9 | 0.37 | 2.36 | +5.5 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 100.0% | 11.5% | 11.5% | 26.9% | -2.9 | 0.37 | 2.36 | +5.5 | +5.5 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 11.5% | 11.5% | 26.9% | -2.9 | 0.37 | 2.36 | +5.5 | +5.5 |
| `asian_range_gte_30` | 4 | S_STRANGER | 15.4% | 0.0% | 0.0% | 75.0% | -2.7 | 0.00 | 0.00 | +5.7 | +5.8 |
| `confluence_gte_60` | 6 | S_STRANGER | 23.1% | 16.7% | 16.7% | 16.7% | -1.5 | 0.52 | 2.08 | +6.0 | +5.9 |
| `confluence_gte_70` | 1 | S_STRANGER | 3.8% | 0.0% | 0.0% | 0.0% | -11.2 | 0.00 | 0.00 | +0.6 | +14.6 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 38.5% | 10.0% | 10.0% | 10.0% | -3.5 | 0.40 | 3.64 | +5.0 | +5.8 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 30.8% | 12.5% | 12.5% | 37.5% | -1.3 | 0.70 | 3.49 | +8.0 | +7.1 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 15.4% | 0.0% | 0.0% | 75.0% | -2.7 | 0.00 | 0.00 | +5.7 | +5.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 3.8% | 0.0% | 0.0% | 0.0% | -10.8 | 0.00 | 0.00 | +0.7 | +10.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 11.5% | 11.5% | 26.9% | -2.9 | 0.37 | 2.36 | +5.5 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 11.5% | 11.5% | 26.9% | -2.9 | 0.37 | 2.36 | +5.5 | +5.5 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 15.4% | 25.0% | 25.0% | 25.0% | -1.2 | 0.70 | 2.10 | +5.4 | +5.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.8% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +7.5 | +2.1 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=-6.4; validation N=6 Fav=0.0% Avg=-6.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 11.4% | 14.3% | 20.0% | -3.5 | 0.29 | 1.47 | +4.5 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 85.7% | 13.3% | 16.7% | 20.0% | -3.6 | 0.32 | 1.35 | +4.6 | +7.3 |
| `hunt_to_ar_ratio_le_2_5` | 32 | S_STRANGER | 91.4% | 12.5% | 15.6% | 18.8% | -3.6 | 0.31 | 1.41 | +4.5 | +7.2 |
| `stop_hunt_le_90` | 35 | S_STRANGER | 100.0% | 11.4% | 14.3% | 20.0% | -3.5 | 0.29 | 1.47 | +4.5 | +7.1 |
| `asian_range_gte_30` | 7 | S_STRANGER | 20.0% | 14.3% | 14.3% | 28.6% | -2.5 | 0.45 | 2.23 | +5.3 | +6.7 |
| `confluence_gte_60` | 14 | S_STRANGER | 40.0% | 7.1% | 14.3% | 14.3% | -3.5 | 0.16 | 0.82 | +5.2 | +7.0 |
| `confluence_gte_70` | 4 | S_STRANGER | 11.4% | 0.0% | 25.0% | 0.0% | -1.5 | 0.50 | 1.49 | +4.5 | +6.5 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 37.1% | 15.4% | 15.4% | 7.7% | -6.3 | 0.18 | 0.98 | +4.0 | +8.4 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 37.1% | 7.7% | 7.7% | 15.4% | -5.2 | 0.05 | 0.50 | +3.4 | +9.9 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 20.0% | 14.3% | 14.3% | 28.6% | -2.5 | 0.45 | 2.23 | +5.3 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 5.7% | 50.0% | 50.0% | 50.0% | +1.0 | 1.17 | 1.17 | +11.9 | +7.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 35 | S_STRANGER | 100.0% | 11.4% | 14.3% | 20.0% | -3.5 | 0.29 | 1.47 | +4.5 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 35 | S_STRANGER | 100.0% | 11.4% | 14.3% | 20.0% | -3.5 | 0.29 | 1.47 | +4.5 | +7.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-6.9; validation N=1 Fav=0.0% Avg=-22.5; out_of_sample N=4 Fav=25.0% Avg=+4.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 10.7% | 14.3% | 14.3% | -2.9 | 0.39 | 2.15 | +5.6 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 85.7% | 12.5% | 16.7% | 16.7% | -2.1 | 0.51 | 2.30 | +6.0 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 96.4% | 11.1% | 14.8% | 14.8% | -2.2 | 0.47 | 2.47 | +5.5 | +5.6 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 10.7% | 14.3% | 14.3% | -2.9 | 0.39 | 2.15 | +5.6 | +5.4 |
| `asian_range_gte_30` | 5 | S_STRANGER | 17.9% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +4.0 | +7.4 |
| `confluence_gte_60` | 24 | S_STRANGER | 85.7% | 12.5% | 12.5% | 16.7% | -2.9 | 0.42 | 2.67 | +5.9 | +5.4 |
| `confluence_gte_70` | 6 | S_STRANGER | 21.4% | 16.7% | 16.7% | 33.3% | -1.8 | 0.68 | 2.71 | +9.1 | +6.1 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 25.0% | 14.3% | 14.3% | 14.3% | -1.6 | 0.57 | 3.44 | +5.1 | +6.2 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 50.0% | 14.3% | 14.3% | 7.1% | -1.6 | 0.54 | 3.25 | +4.5 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 17.9% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +4.0 | +7.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +2.9 | +9.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 10.7% | 14.3% | 14.3% | -2.9 | 0.39 | 2.15 | +5.6 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 10.7% | 14.3% | 14.3% | -2.9 | 0.39 | 2.15 | +5.6 | +5.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +2.8 | +8.3 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 10.7% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +3.5 | +8.6 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=12.5% Avg=-2.5; validation N=5 Fav=20.0% Avg=+0.1; out_of_sample N=2 Fav=50.0% Avg=+13.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 48 | S_STRANGER | 100.0% | 10.4% | 14.6% | 27.1% | -3.9 | 0.28 | 1.26 | +5.8 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 43 | S_STRANGER | 89.6% | 11.6% | 16.3% | 27.9% | -2.8 | 0.37 | 1.50 | +5.9 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 48 | S_STRANGER | 100.0% | 10.4% | 14.6% | 27.1% | -3.9 | 0.28 | 1.26 | +5.8 | +4.6 |
| `stop_hunt_le_90` | 48 | S_STRANGER | 100.0% | 10.4% | 14.6% | 27.1% | -3.9 | 0.28 | 1.26 | +5.8 | +4.6 |
| `asian_range_gte_30` | 25 | S_STRANGER | 52.1% | 8.0% | 16.0% | 32.0% | -3.2 | 0.36 | 1.36 | +6.0 | +4.6 |
| `confluence_gte_60` | 21 | S_STRANGER | 43.8% | 19.0% | 23.8% | 28.6% | -4.3 | 0.39 | 1.01 | +6.4 | +4.4 |
| `confluence_gte_70` | 1 | R_RUNNER | 2.1% | 100.0% | 100.0% | 0.0% | +12.9 | 999.00 | 999.00 | +17.2 | +4.1 |
| `tdi_rsi_gt_signal` | 40 | S_STRANGER | 83.3% | 12.5% | 15.0% | 27.5% | -3.1 | 0.36 | 1.60 | +6.3 | +4.9 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 31.2% | 20.0% | 20.0% | 40.0% | +0.5 | 1.18 | 3.15 | +10.1 | +5.4 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 52.1% | 8.0% | 16.0% | 32.0% | -3.2 | 0.36 | 1.36 | +6.0 | +4.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 21 | S_STRANGER | 43.8% | 9.5% | 14.3% | 38.1% | -2.1 | 0.50 | 2.00 | +6.8 | +4.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 48 | S_STRANGER | 100.0% | 10.4% | 14.6% | 27.1% | -3.9 | 0.28 | 1.26 | +5.8 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 48 | S_STRANGER | 100.0% | 10.4% | 14.6% | 27.1% | -3.9 | 0.28 | 1.26 | +5.8 | +4.6 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 10.4% | 0.0% | 0.0% | 40.0% | -0.9 | 0.00 | 0.00 | +7.5 | +2.5 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 8.3% | 0.0% | 0.0% | 50.0% | -0.7 | 0.00 | 0.00 | +8.7 | +1.8 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=-3.3; validation N=4 Fav=0.0% Avg=-3.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 50.0% | -3.9 | 0.23 | 1.13 | +7.2 | +8.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 55.6% | -3.5 | 0.27 | 1.06 | +7.5 | +8.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 50.0% | -3.9 | 0.23 | 1.13 | +7.2 | +8.4 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 50.0% | -3.9 | 0.23 | 1.13 | +7.2 | +8.4 |
| `asian_range_gte_30` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -16.7 | 0.00 | 0.00 | +5.2 | +21.1 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 50.0% | -3.9 | 0.23 | 1.13 | +7.2 | +8.4 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 50.0% | -3.9 | 0.23 | 1.13 | +7.2 | +8.4 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 40.0% | -4.3 | 0.00 | 0.00 | +8.2 | +5.8 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 37.5% | -6.3 | 0.00 | 0.00 | +6.4 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -25.7 | 0.00 | 0.00 | +5.5 | +30.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 55.6% | -3.5 | 0.27 | 1.06 | +7.5 | +8.0 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 50.0% | -3.9 | 0.23 | 1.13 | +7.2 | +8.4 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -7.6 | 0.00 | 0.00 | +4.9 | +12.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -7.6 | 0.00 | 0.00 | +4.9 | +12.0 |

### THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=-2.9; validation N=1 Fav=0.0% Avg=-2.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.1 | 0.30 | 2.72 | +3.7 | +8.3 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 0.0% | -3.5 | 0.37 | 2.92 | +4.0 | +8.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.1 | 0.30 | 2.72 | +3.7 | +8.3 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.1 | 0.30 | 2.72 | +3.7 | +8.3 |
| `asian_range_gte_30` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +1.4 | +7.4 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.1 | 0.30 | 2.72 | +3.7 | +8.3 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.1 | 0.30 | 2.72 | +3.7 | +8.3 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 0.0% | -4.8 | 0.32 | 2.23 | +4.3 | +8.9 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | +3.0 | 1.99 | 3.98 | +7.9 | +4.4 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +1.4 | +7.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -6.7 | 0.00 | 0.00 | +1.4 | +8.2 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -8.9 | 0.00 | 0.00 | +1.9 | +11.3 |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 0.0% | -3.5 | 0.37 | 2.92 | +4.0 | +8.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.1 | 0.30 | 2.72 | +3.7 | +8.3 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -2.8 | 0.51 | 2.57 | +5.3 | +7.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | +7.2 | 5.11 | 5.11 | +11.8 | +3.5 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+0.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=0.0% Avg=-5.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.3 | 0.10 | 0.93 | +3.1 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.3 | 0.10 | 0.93 | +3.1 | +7.3 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.3 | 0.10 | 0.93 | +3.1 | +7.3 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.3 | 0.10 | 0.93 | +3.1 | +7.3 |
| `asian_range_gte_30` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +1.1 | +8.3 |
| `confluence_gte_60` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 0.0% | -4.6 | 0.11 | 0.84 | +3.2 | +7.1 |
| `confluence_gte_70` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +2.4 | +8.4 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -3.3 | 0.20 | 1.00 | +3.4 | +7.7 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | -3.4 | 0.27 | 0.80 | +3.8 | +8.2 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +1.1 | +8.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +1.3 | +9.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.3 | 0.10 | 0.93 | +3.1 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -4.3 | 0.10 | 0.93 | +3.1 | +7.3 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +4.9 | 999.00 | 999.00 | +11.7 | +4.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +4.9 | 999.00 | 999.00 | +11.7 | +4.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-6.1; validation N=4 Fav=25.0% Avg=-2.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -7.7 | 0.05 | 0.42 | +5.4 | +7.8 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -8.9 | 0.00 | 0.00 | +5.2 | +8.0 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -8.9 | 0.00 | 0.00 | +5.2 | +8.0 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -7.7 | 0.05 | 0.42 | +5.4 | +7.8 |
| `asian_range_gte_30` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -13.1 | 0.00 | 0.00 | +7.3 | +11.5 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -7.7 | 0.05 | 0.42 | +5.4 | +7.8 |
| `confluence_gte_70` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +3.8 | 999.00 | 999.00 | +10.1 | +0.2 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -3.5 | 0.15 | 0.77 | +7.2 | +8.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -3.5 | 0.15 | 0.77 | +7.2 | +8.3 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -13.1 | 0.00 | 0.00 | +7.3 | +11.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +10.4 | +15.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -7.7 | 0.05 | 0.42 | +5.4 | +7.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -7.7 | 0.05 | 0.42 | +5.4 | +7.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=12.5% Avg=-9.9; validation N=2 Fav=0.0% Avg=-1.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -8.2 | 0.03 | 0.24 | +4.2 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -8.2 | 0.03 | 0.24 | +4.2 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -8.2 | 0.03 | 0.24 | +4.2 | +4.3 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -8.2 | 0.03 | 0.24 | +4.2 | +4.3 |
| `asian_range_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.7 | 0.00 | 0.00 | +4.1 | +5.0 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -8.2 | 0.03 | 0.24 | +4.2 | +4.3 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -8.2 | 0.03 | 0.24 | +4.2 | +4.3 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | -4.0 | 0.12 | 0.36 | +6.7 | +7.0 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | -4.0 | 0.12 | 0.36 | +6.7 | +7.0 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.7 | 0.00 | 0.00 | +4.1 | +5.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.7 | 0.00 | 0.00 | +4.1 | +5.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -8.2 | 0.03 | 0.24 | +4.2 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -8.2 | 0.03 | 0.24 | +4.2 | +4.3 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -11.8 | 0.00 | 0.00 | +3.0 | +1.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -17.4 | 0.00 | 0.00 | +1.5 | +17.7 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=0.0% Avg=-2.2; out_of_sample N=1 Fav=100.0% Avg=+6.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.3 | 0.32 | 2.88 | +4.3 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.3 | 0.32 | 2.88 | +4.3 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.3 | 0.32 | 2.88 | +4.3 | +4.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.3 | 0.32 | 2.88 | +4.3 | +4.6 |
| `asian_range_gte_30` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 33.3% | -1.0 | 0.00 | 0.00 | +3.0 | +3.6 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.3 | 0.32 | 2.88 | +4.3 | +4.6 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.3 | 0.32 | 2.88 | +4.3 | +4.6 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +2.9 | +6.0 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 0.0% | -1.2 | 0.41 | 2.90 | +4.9 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 33.3% | -1.0 | 0.00 | 0.00 | +3.0 | +3.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +2.8 | +3.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.3 | 0.32 | 2.88 | +4.3 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.3 | 0.32 | 2.88 | +4.3 | +4.6 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 50.0% | -1.5 | 0.00 | 0.00 | +3.2 | +3.0 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=-0.2; validation N=6 Fav=0.0% Avg=-4.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -2.3 | 0.25 | 2.21 | +4.6 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -2.0 | 0.00 | 0.00 | +2.2 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 20.0% | -1.6 | 0.00 | 0.00 | +4.1 | +4.9 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -2.3 | 0.25 | 2.21 | +4.6 | +5.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -2.3 | 0.25 | 2.21 | +4.6 | +5.5 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -2.3 | 0.25 | 2.21 | +4.6 | +5.5 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -2.3 | 0.25 | 2.21 | +4.6 | +5.5 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +3.4 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -2.3 | 0.25 | 2.21 | +4.6 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -2.3 | 0.25 | 2.21 | +4.6 | +5.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=33.3% Avg=+0.7; out_of_sample N=2 Fav=0.0% Avg=-9.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -6.6 | 0.05 | 0.48 | +2.4 | +6.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 0.0% | -6.2 | 0.07 | 0.49 | +2.3 | +6.9 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 0.0% | -5.6 | 0.07 | 0.55 | +2.2 | +6.8 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -6.6 | 0.05 | 0.48 | +2.4 | +6.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 72.7% | 0.0% | 0.0% | 0.0% | -9.4 | 0.00 | 0.00 | +1.3 | +6.9 |
| `confluence_gte_70` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +2.4 | +3.7 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 0.0% | -3.7 | 0.10 | 0.81 | +2.8 | +6.9 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 0.0% | -3.2 | 0.19 | 0.76 | +3.6 | +7.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -6.6 | 0.05 | 0.48 | +2.4 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -6.6 | 0.05 | 0.48 | +2.4 | +6.0 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +5.1 | +2.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=-0.7; validation N=1 Fav=0.0% Avg=-6.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 8.7% | 13.0% | 13.0% | -2.7 | 0.18 | 1.11 | +4.2 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 87.0% | 10.0% | 15.0% | 15.0% | -1.9 | 0.25 | 1.34 | +4.4 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 91.3% | 9.5% | 14.3% | 14.3% | -2.6 | 0.19 | 1.09 | +4.2 | +5.9 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 8.7% | 13.0% | 13.0% | -2.7 | 0.18 | 1.11 | +4.2 | +6.3 |
| `asian_range_gte_30` | 11 | S_STRANGER | 47.8% | 9.1% | 9.1% | 9.1% | -1.9 | 0.25 | 2.55 | +5.1 | +5.2 |
| `confluence_gte_60` | 14 | S_STRANGER | 60.9% | 7.1% | 14.3% | 14.3% | -1.9 | 0.26 | 1.45 | +4.8 | +6.3 |
| `confluence_gte_70` | 5 | S_STRANGER | 21.7% | 0.0% | 0.0% | 0.0% | -2.0 | 0.00 | 0.00 | +5.6 | +5.9 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 47.8% | 0.0% | 0.0% | 9.1% | -3.9 | 0.00 | 0.00 | +3.6 | +6.8 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 39.1% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +3.2 | +6.7 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 47.8% | 9.1% | 9.1% | 9.1% | -1.9 | 0.25 | 2.55 | +5.1 | +5.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 17.4% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +4.8 | +3.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 95.7% | 9.1% | 13.6% | 13.6% | -2.1 | 0.22 | 1.34 | +4.3 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 8.7% | 13.0% | 13.0% | -2.7 | 0.18 | 1.11 | +4.2 | +6.3 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 21.7% | 20.0% | 20.0% | 20.0% | -1.8 | 0.28 | 1.10 | +3.8 | +4.3 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 17.4% | 0.0% | 0.0% | 0.0% | -5.1 | 0.00 | 0.00 | +4.6 | +6.8 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=14.3% Avg=+2.7; validation N=1 Fav=0.0% Avg=-18.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 25.0% | -2.2 | 0.52 | 4.66 | +6.8 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 66.7% | 0.0% | 0.0% | 0.0% | -6.4 | 0.00 | 0.00 | +4.4 | +8.4 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 25.0% | -2.2 | 0.52 | 4.66 | +6.8 | +7.0 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 25.0% | -2.2 | 0.52 | 4.66 | +6.8 | +7.0 |
| `asian_range_gte_30` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -6.3 | 0.00 | 0.00 | +1.7 | +11.8 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 25.0% | -2.2 | 0.52 | 4.66 | +6.8 | +7.0 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 25.0% | -2.2 | 0.52 | 4.66 | +6.8 | +7.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 37.5% | +0.1 | 1.02 | 5.09 | +8.9 | +6.9 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +6.2 | +9.7 |
| `ratio_le_2_and_asian_gte_30` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -6.3 | 0.00 | 0.00 | +1.7 | +11.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +0.9 | +11.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 75.0% | 0.0% | 0.0% | 11.1% | -5.7 | 0.00 | 0.00 | +4.8 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 25.0% | -2.2 | 0.52 | 4.66 | +6.8 | +7.0 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 28.6% | -0.4 | 0.91 | 4.54 | +6.5 | +7.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +1.6 | +9.5 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+3.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=0.0% Avg=-4.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -2.1 | 0.44 | 5.26 | +6.5 | +8.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 69.2% | 11.1% | 11.1% | 11.1% | -2.6 | 0.49 | 3.89 | +7.2 | +9.2 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 10.0% | -2.4 | 0.47 | 4.27 | +6.5 | +9.8 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -2.1 | 0.44 | 5.26 | +6.5 | +8.4 |
| `asian_range_gte_30` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 20.0% | +0.3 | 1.08 | 4.32 | +9.2 | +7.9 |
| `confluence_gte_60` | 9 | S_STRANGER | 69.2% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +5.7 | +8.4 |
| `confluence_gte_70` | 4 | S_STRANGER | 30.8% | 0.0% | 0.0% | 0.0% | -2.7 | 0.00 | 0.00 | +5.9 | +5.0 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 25.0% | +4.6 | 6.81 | 20.44 | +11.2 | +4.9 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 10.0% | -1.0 | 0.69 | 6.23 | +6.2 | +8.2 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 20.0% | +0.3 | 1.08 | 4.32 | +9.2 | +7.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 50.0% | +10.0 | 12.82 | 12.82 | +15.1 | +6.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 92.3% | 8.3% | 8.3% | 8.3% | -2.2 | 0.45 | 4.94 | +7.0 | +7.8 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 92.3% | 8.3% | 8.3% | 8.3% | -2.2 | 0.45 | 4.94 | +7.0 | +7.8 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 100.0% | +21.8 | 999.00 | 999.00 | +27.4 | +2.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 50.0% | +10.3 | 18.17 | 18.17 | +13.8 | +9.1 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+27.8; validation N=1 Fav=0.0% Avg=-4.0; out_of_sample N=3 Fav=0.0% Avg=-3.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 52 | S_STRANGER | 100.0% | 7.7% | 11.5% | 13.5% | -5.0 | 0.15 | 1.04 | +4.6 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 43 | S_STRANGER | 82.7% | 9.3% | 14.0% | 14.0% | -4.0 | 0.21 | 1.18 | +4.7 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 51 | S_STRANGER | 98.1% | 7.8% | 11.8% | 13.7% | -4.9 | 0.15 | 1.05 | +4.7 | +7.8 |
| `stop_hunt_le_90` | 52 | S_STRANGER | 100.0% | 7.7% | 11.5% | 13.5% | -5.0 | 0.15 | 1.04 | +4.6 | +7.7 |
| `asian_range_gte_30` | 16 | S_STRANGER | 30.8% | 6.2% | 12.5% | 6.2% | -3.0 | 0.37 | 2.61 | +6.6 | +6.8 |
| `confluence_gte_60` | 40 | S_STRANGER | 76.9% | 2.5% | 7.5% | 10.0% | -5.7 | 0.03 | 0.34 | +4.0 | +7.4 |
| `confluence_gte_70` | 9 | S_STRANGER | 17.3% | 0.0% | 0.0% | 11.1% | -4.8 | 0.00 | 0.00 | +4.5 | +4.3 |
| `tdi_rsi_gt_signal` | 24 | S_STRANGER | 46.2% | 8.3% | 8.3% | 16.7% | -2.4 | 0.33 | 3.09 | +4.9 | +6.1 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 46.2% | 8.3% | 8.3% | 12.5% | -4.2 | 0.22 | 2.21 | +5.2 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 28.8% | 6.7% | 13.3% | 6.7% | -2.9 | 0.39 | 2.55 | +6.8 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 9.6% | 20.0% | 20.0% | 20.0% | +3.0 | 2.16 | 8.62 | +9.0 | +4.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 48 | S_STRANGER | 92.3% | 8.3% | 12.5% | 14.6% | -4.1 | 0.19 | 1.18 | +4.8 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 52 | S_STRANGER | 100.0% | 7.7% | 11.5% | 13.5% | -5.0 | 0.15 | 1.04 | +4.6 | +7.7 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 25.0% | 15.4% | 15.4% | 15.4% | -6.0 | 0.33 | 1.80 | +7.4 | +11.9 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 15.4% | 12.5% | 12.5% | 12.5% | -3.6 | 0.49 | 3.44 | +7.1 | +10.0 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=14.3% Avg=-1.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -2.6 | 0.33 | 3.93 | +7.1 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 57.1% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +3.4 | +9.2 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 64.3% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +4.0 | +8.5 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -2.6 | 0.33 | 3.93 | +7.1 | +6.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 28.6% | -1.1 | 0.71 | 3.53 | +10.8 | +5.7 |
| `confluence_gte_70` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -1.7 | 0.00 | 0.00 | +9.0 | +3.2 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -5.1 | 0.00 | 0.00 | +5.1 | +9.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +7.1 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -2.6 | 0.33 | 3.93 | +7.1 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -2.6 | 0.33 | 3.93 | +7.1 | +6.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-5.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-3.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 5.0% | 10.0% | 15.0% | -7.3 | 0.04 | 0.34 | +4.4 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 100.0% | 5.0% | 10.0% | 15.0% | -7.3 | 0.04 | 0.34 | +4.4 | +7.3 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 5.0% | 10.0% | 15.0% | -7.3 | 0.04 | 0.34 | +4.4 | +7.3 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 5.0% | 10.0% | 15.0% | -7.3 | 0.04 | 0.34 | +4.4 | +7.3 |
| `asian_range_gte_30` | 9 | S_STRANGER | 45.0% | 0.0% | 0.0% | 11.1% | -10.4 | 0.00 | 0.00 | +4.1 | +10.6 |
| `confluence_gte_60` | 11 | S_STRANGER | 55.0% | 0.0% | 0.0% | 9.1% | -10.5 | 0.00 | 0.00 | +4.4 | +7.9 |
| `confluence_gte_70` | 4 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -11.6 | 0.00 | 0.00 | +5.7 | +10.1 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 80.0% | 6.2% | 6.2% | 18.8% | -8.3 | 0.04 | 0.55 | +4.9 | +7.9 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 20.0% | 25.0% | 25.0% | 25.0% | -8.1 | 0.15 | 0.46 | +6.6 | +10.9 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 45.0% | 0.0% | 0.0% | 11.1% | -10.4 | 0.00 | 0.00 | +4.1 | +10.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 35.0% | 0.0% | 0.0% | 14.3% | -11.7 | 0.00 | 0.00 | +5.2 | +11.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 5.0% | 10.0% | 15.0% | -7.3 | 0.04 | 0.34 | +4.4 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 5.0% | 10.0% | 15.0% | -7.3 | 0.04 | 0.34 | +4.4 | +7.3 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 35.0% | 14.3% | 14.3% | 28.6% | -5.5 | 0.13 | 0.66 | +5.3 | +9.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 15.0% | 33.3% | 33.3% | 33.3% | -7.8 | 0.20 | 0.40 | +8.0 | +11.4 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=2 Fav=0.0% Avg=-3.2; out_of_sample N=5 Fav=20.0% Avg=-1.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 4.8% | 4.8% | 4.8% | -3.1 | 0.15 | 2.64 | +3.6 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 47.6% | 0.0% | 0.0% | 10.0% | -3.3 | 0.00 | 0.00 | +4.0 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 71.4% | 6.7% | 6.7% | 6.7% | -2.7 | 0.22 | 2.61 | +4.3 | +5.3 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 4.8% | 4.8% | 4.8% | -3.1 | 0.15 | 2.64 | +3.6 | +5.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 19 | S_STRANGER | 90.5% | 5.3% | 5.3% | 5.3% | -3.1 | 0.16 | 2.55 | +3.6 | +5.5 |
| `confluence_gte_70` | 7 | S_STRANGER | 33.3% | 14.3% | 14.3% | 14.3% | -2.1 | 0.44 | 2.18 | +5.8 | +5.3 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 38.1% | 12.5% | 12.5% | 0.0% | -1.3 | 0.53 | 3.17 | +4.0 | +5.1 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 42.9% | 11.1% | 11.1% | 0.0% | -1.6 | 0.44 | 3.07 | +4.5 | +5.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 4.8% | 4.8% | 4.8% | -3.1 | 0.15 | 2.64 | +3.6 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 4.8% | 4.8% | 4.8% | -3.1 | 0.15 | 2.64 | +3.6 | +5.3 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +0.7 | +6.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=0.0% Avg=-3.8; validation N=1 Fav=0.0% Avg=-4.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -3.8 | 0.00 | 0.00 | +3.8 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -3.8 | 0.00 | 0.00 | +3.8 | +7.3 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -3.8 | 0.00 | 0.00 | +3.8 | +7.3 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -3.8 | 0.00 | 0.00 | +3.8 | +7.3 |
| `asian_range_gte_30` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +3.4 | +7.4 |
| `confluence_gte_60` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 11.1% | -4.0 | 0.00 | 0.00 | +4.2 | +7.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +1.3 | +7.0 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -4.8 | 0.00 | 0.00 | +3.2 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +3.4 | +7.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +0.3 | +6.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -3.8 | 0.00 | 0.00 | +3.8 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -3.8 | 0.00 | 0.00 | +3.8 | +7.3 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 33.3% | -2.4 | 0.00 | 0.00 | +5.9 | +6.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-1.7; validation N=2 Fav=0.0% Avg=-2.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -4.2 | 0.00 | 0.00 | +3.3 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +1.2 | +7.6 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 14.3% | -4.9 | 0.00 | 0.00 | +3.9 | +7.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -4.2 | 0.00 | 0.00 | +3.3 | +6.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +4.8 | +4.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 16.7% | -4.8 | 0.00 | 0.00 | +4.3 | +7.7 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +3.7 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 20.0% | -2.1 | 0.00 | 0.00 | +4.0 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -4.2 | 0.00 | 0.00 | +3.3 | +6.7 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -6.3 | 0.00 | 0.00 | +2.7 | +9.2 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -6.9 | 0.00 | 0.00 | +3.1 | +9.2 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=0.0% Avg=-6.8; validation N=4 Fav=0.0% Avg=-3.4; out_of_sample N=2 Fav=0.0% Avg=-1.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -4.4 | 0.05 | 0.43 | +3.0 | +6.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -4.4 | 0.05 | 0.43 | +3.0 | +6.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -4.4 | 0.05 | 0.43 | +3.0 | +6.9 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -4.4 | 0.05 | 0.43 | +3.0 | +6.9 |
| `asian_range_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -7.2 | 0.00 | 0.00 | +2.1 | +12.3 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -4.4 | 0.05 | 0.43 | +3.0 | +6.9 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -4.4 | 0.05 | 0.43 | +3.0 | +6.9 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +2.0 | +6.7 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +1.2 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -7.2 | 0.00 | 0.00 | +2.1 | +12.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -7.2 | 0.00 | 0.00 | +2.1 | +12.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -4.4 | 0.05 | 0.43 | +3.0 | +6.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -4.4 | 0.05 | 0.43 | +3.0 | +6.9 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +2.2 | +8.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +1.4 | +8.7 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=0.0% Avg=-5.7; validation N=2 Fav=0.0% Avg=-1.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +3.7 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +3.7 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +3.7 | +6.7 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +3.7 | +6.7 |
| `asian_range_gte_30` | 10 | S_STRANGER | 83.3% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +3.9 | +6.1 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +3.7 | +6.7 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +3.7 | +6.7 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +4.4 | +6.0 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 91.7% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +4.0 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 83.3% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +3.9 | +6.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +5.0 | +4.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +3.7 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +3.7 | +6.7 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +4.1 | +7.0 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +4.1 | +7.0 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-1.7; validation N=2 Fav=0.0% Avg=-0.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +4.5 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +4.5 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +4.5 | +6.6 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +4.5 | +6.6 |
| `asian_range_gte_30` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -6.3 | 0.00 | 0.00 | +5.4 | +6.6 |
| `confluence_gte_60` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +4.9 | +7.0 |
| `confluence_gte_70` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +5.7 | +6.3 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +5.8 | +8.1 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -3.6 | 0.00 | 0.00 | +6.2 | +7.4 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -6.3 | 0.00 | 0.00 | +5.4 | +6.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +5.8 | +8.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +4.5 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +4.5 | +6.6 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -13.3 | 0.00 | 0.00 | +0.7 | +3.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +7.8 | +9.2 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-3.5; validation N=2 Fav=0.0% Avg=-6.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -5.8 | 0.00 | 0.00 | +3.2 | +8.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -5.8 | 0.00 | 0.00 | +3.2 | +8.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -5.8 | 0.00 | 0.00 | +3.2 | +8.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -5.8 | 0.00 | 0.00 | +3.2 | +8.0 |
| `asian_range_gte_30` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 16.7% | -4.4 | 0.00 | 0.00 | +3.2 | +5.5 |
| `confluence_gte_60` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 14.3% | -5.6 | 0.00 | 0.00 | +3.7 | +8.3 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 20.0% | -5.1 | 0.00 | 0.00 | +5.3 | +8.2 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -8.4 | 0.00 | 0.00 | +4.8 | +11.8 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 16.7% | -4.4 | 0.00 | 0.00 | +3.2 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 33.3% | -4.0 | 0.00 | 0.00 | +3.8 | +5.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -5.8 | 0.00 | 0.00 | +3.2 | +8.0 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -5.8 | 0.00 | 0.00 | +3.2 | +8.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=0.0% Avg=-7.2; validation N=1 Fav=0.0% Avg=-2.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -7.1 | 0.00 | 0.00 | +4.0 | +8.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 0.0% | 0.0% | 20.0% | -6.8 | 0.00 | 0.00 | +4.6 | +7.9 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -7.1 | 0.00 | 0.00 | +4.0 | +8.3 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -7.1 | 0.00 | 0.00 | +4.0 | +8.3 |
| `asian_range_gte_30` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 66.7% | -2.7 | 0.00 | 0.00 | +10.4 | +4.2 |
| `confluence_gte_60` | 9 | S_STRANGER | 75.0% | 0.0% | 0.0% | 22.2% | -7.3 | 0.00 | 0.00 | +4.3 | +8.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 0.0% | 0.0% | 12.5% | -7.5 | 0.00 | 0.00 | +3.5 | +8.6 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -8.8 | 0.00 | 0.00 | +2.8 | +10.2 |
| `ratio_le_2_and_asian_gte_30` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 66.7% | -2.7 | 0.00 | 0.00 | +10.4 | +4.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +11.8 | +1.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 0.0% | 0.0% | 18.2% | -7.0 | 0.00 | 0.00 | +4.3 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -7.1 | 0.00 | 0.00 | +4.0 | +8.3 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 20.0% | -8.9 | 0.00 | 0.00 | +3.6 | +9.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -20.4 | 0.00 | 0.00 | +0.0 | +21.8 |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
