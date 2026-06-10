# GBPUSD Pair Feature Ablation

Generated: 2026-06-09T15:36:12.080080+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 15 | R_REPEATER | 60.0% | +5.4 | `all` | 15 | R_REPEATER | 60.0% | +5.4 | 3.04 | 1.69 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 33 | R_REPEATER | 51.5% | +10.3 | `asian_range_gte_30` | 27 | R_REPEATER | 51.9% | +10.4 | 3.53 | 3.02 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 37 | S_STRANGER | 43.2% | +5.0 | `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 58.3% | +11.2 | 7.64 | 4.37 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 42.9% | -0.8 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 41.7% | +0.5 | 1.11 | 1.55 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 26 | S_STRANGER | 42.3% | +1.3 | `tdi_rsi_gte_50` | 13 | S_STRANGER | 46.2% | +2.4 | 1.94 | 2.26 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 41.7% | +8.1 | `tdi_rsi_gte_50` | 7 | R_REPEATER | 57.1% | +9.2 | 4.56 | 3.42 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | S_STRANGER | 41.2% | +4.3 | `confluence_gte_60` | 8 | R_REPEATER | 62.5% | +15.2 | 6.28 | 2.51 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | S_STRANGER | 40.0% | +4.3 | `confluence_gte_60` | 7 | R_REPEATER | 57.1% | +8.2 | 4.74 | 2.37 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 39.1% | +2.7 | `asian_range_gte_30` | 14 | R_REPEATER | 50.0% | +2.3 | 1.52 | 1.30 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 42 | S_STRANGER | 38.1% | +3.8 | `ratio_le_2_asian_gte_30_tdi_positive` | 15 | R_REPEATER | 53.3% | +8.9 | 3.97 | 2.48 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 37.5% | +5.2 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 43.8% | +4.7 | 2.23 | 2.23 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 36.4% | -2.4 | `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 42.9% | +1.1 | 1.11 | 1.49 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 28 | S_STRANGER | 35.7% | +7.5 | `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 41.7% | +14.6 | 9.94 | 13.92 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 35.7% | +1.9 | `stop_hunt_le_90` | 11 | S_STRANGER | 45.5% | +3.5 | 2.17 | 2.60 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 35.3% | +4.2 | `all` | 17 | S_STRANGER | 35.3% | +4.2 | 2.85 | 5.23 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 23 | S_STRANGER | 34.8% | -0.5 | `tdi_rsi_gte_50` | 7 | R_REPEATER | 57.1% | +8.8 | 2.77 | 2.08 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 33.3% | +4.6 | `asian_range_gte_30` | 13 | S_STRANGER | 38.5% | +5.3 | 3.69 | 3.07 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | +3.6 | `stop_hunt_le_90` | 9 | S_STRANGER | 44.4% | +5.9 | 9.21 | 6.91 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 18 | S_STRANGER | 33.3% | +3.3 | `asian_range_gte_30` | 12 | S_STRANGER | 41.7% | +3.6 | 1.65 | 1.98 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 33.3% | +3.3 | `all` | 15 | S_STRANGER | 33.3% | +3.3 | 3.42 | 3.42 | 0 | 3 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | +1.5 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 37.5% | +1.6 | 1.51 | 2.52 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 33.3% | -1.1 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 27.3% | +0.6 | 1.12 | 3.00 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | -6.4 | `confluence_gte_60` | 8 | S_STRANGER | 37.5% | +6.3 | 3.50 | 3.50 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 30.8% | +5.9 | `confluence_gte_70` | 7 | R_REPEATER | 57.1% | +25.5 | 9.05 | 6.79 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 30.8% | -3.4 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 44.4% | +3.0 | 1.32 | 1.66 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 36 | S_STRANGER | 30.6% | -0.5 | `confluence_gte_70` | 6 | R_REPEATER | 66.7% | +9.7 | 4.79 | 2.40 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 33 | S_STRANGER | 30.3% | +1.5 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 40.0% | +1.4 | 2.15 | 2.15 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 30.0% | +0.1 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 44.4% | +4.7 | 3.03 | 3.03 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | -6.8 | `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 40.0% | -2.5 | 0.54 | 0.81 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | -18.2 | `confluence_gte_70` | 6 | R_REPEATER | 50.0% | -17.3 | 0.29 | 0.29 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 57 | S_STRANGER | 29.8% | -0.9 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 20.0% | +1.6 | 1.34 | 5.34 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 27 | S_STRANGER | 29.6% | -0.3 | `confluence_gte_60` | 7 | R_REPEATER | 57.1% | +6.0 | 3.01 | 2.26 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 31 | S_STRANGER | 29.0% | -0.8 | `confluence_gte_60` | 27 | S_STRANGER | 29.6% | +1.7 | 1.60 | 3.01 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 38 | S_STRANGER | 28.9% | +2.1 | `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 33.3% | +2.9 | 2.11 | 3.44 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 28.6% | +3.5 | `asian_range_gte_30` | 11 | S_STRANGER | 36.4% | +5.7 | 2.19 | 2.62 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 27.8% | +3.2 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 31.2% | +4.0 | 2.18 | 4.35 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 27.3% | +3.1 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 33.3% | +6.3 | 2.05 | 4.11 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | -4.1 | `asian_range_gte_30` | 9 | S_STRANGER | 33.3% | -3.7 | 0.56 | 1.12 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 15 | S_STRANGER | 26.7% | +3.8 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 40.0% | +10.3 | 3.07 | 3.07 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 30 | S_STRANGER | 26.7% | +2.2 | `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 41.7% | +3.4 | 2.41 | 3.38 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 26.1% | +1.8 | `tdi_rsi_gte_50` | 18 | S_STRANGER | 33.3% | +3.1 | 2.17 | 4.34 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 31 | S_STRANGER | 25.8% | +0.6 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 33.3% | +5.3 | 2.58 | 3.22 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 39 | S_STRANGER | 25.6% | +4.0 | `stop_hunt_le_90` | 35 | S_STRANGER | 25.7% | +5.4 | 2.07 | 5.18 | 0 | 3 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 25.0% | +2.9 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 28.6% | +5.9 | 2.67 | 5.35 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 25.0% | +1.8 | `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 33.3% | +4.4 | 2.33 | 3.50 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | +1.3 | `confluence_gte_70` | 6 | S_STRANGER | 33.3% | +3.4 | 3.03 | 6.06 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 25.0% | -1.5 | `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 30.0% | +3.2 | 2.70 | 6.30 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 25.0% | -2.8 | `stop_hunt_le_90` | 11 | S_STRANGER | 27.3% | -2.9 | 0.39 | 0.91 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 25.0% | -3.7 | `tdi_rsi_gt_signal` | 11 | S_STRANGER | 36.4% | -0.0 | 1.00 | 1.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74` | 16 | S_STRANGER | 25.0% | -16.6 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 66.7% | +22.4 | 5.26 | 2.63 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 37 | S_STRANGER | 24.3% | -1.8 | `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 33.3% | +1.6 | 2.44 | 4.88 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 29 | S_STRANGER | 24.1% | +0.0 | `hunt_to_ar_ratio_le_2_0` | 6 | R_REPEATER | 50.0% | +1.3 | 1.33 | 1.33 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 17 | S_STRANGER | 23.5% | -2.4 | `confluence_gte_70` | 9 | S_STRANGER | 33.3% | +0.4 | 1.11 | 2.22 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 47 | S_STRANGER | 23.4% | -1.6 | `tdi_rsi_gte_50` | 13 | S_STRANGER | 38.5% | +6.7 | 3.08 | 4.31 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 31 | S_STRANGER | 22.6% | -1.9 | `confluence_gte_60` | 16 | S_STRANGER | 25.0% | -3.1 | 0.67 | 1.85 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 18 | S_STRANGER | 22.2% | -5.8 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 42.9% | +2.0 | 2.71 | 1.81 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 28 | S_STRANGER | 21.4% | -1.3 | `asian_range_gte_30` | 23 | S_STRANGER | 26.1% | +1.6 | 1.41 | 3.52 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | -9.0 | `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 28.6% | -0.7 | 0.78 | 1.94 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 29 | S_STRANGER | 20.7% | -1.3 | `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 37.5% | +12.6 | 3.21 | 5.35 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | +1.3 | `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 33.3% | +5.0 | 2.71 | 4.06 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L2|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 20.0% | +1.1 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 40.0% | +5.5 | 2.85 | 4.28 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 20.0% | +0.1 | `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 28.6% | +9.3 | 2.75 | 6.89 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 25 | S_STRANGER | 20.0% | -1.5 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 25.0% | +0.5 | 1.09 | 2.92 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 15 | S_STRANGER | 20.0% | -6.2 | `confluence_gte_60` | 6 | R_REPEATER | 50.0% | +3.0 | 1.54 | 1.03 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 20.0% | -8.0 | `feature_momentum_breakout_exception` | 8 | S_STRANGER | 37.5% | -6.6 | 0.49 | 0.25 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 36 | S_STRANGER | 19.4% | -4.2 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 27.3% | -6.3 | 0.36 | 0.97 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 26 | S_STRANGER | 19.2% | -4.7 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 30.0% | +2.5 | 1.46 | 3.42 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 18.8% | +1.9 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 22.2% | +2.1 | 3.67 | 5.51 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 18.8% | -1.4 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 22.2% | +0.5 | 1.13 | 3.40 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 18.8% | -1.8 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 25.0% | +2.5 | 1.39 | 2.79 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 27 | S_STRANGER | 18.5% | -11.6 | `tdi_rsi_gte_50` | 9 | R_REPEATER | 55.6% | +6.1 | 3.51 | 2.11 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 38 | S_STRANGER | 18.4% | -2.4 | `confluence_gte_60` | 17 | S_STRANGER | 29.4% | -2.4 | 0.56 | 1.13 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 49 | S_STRANGER | 18.4% | -1.2 | `tdi_rsi_gte_50` | 24 | S_STRANGER | 33.3% | +1.8 | 1.46 | 1.94 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | +2.5 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 25.0% | +7.5 | 2.73 | 6.82 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -3.6 | `stop_hunt_le_90` | 10 | S_STRANGER | 20.0% | -3.0 | 0.68 | 1.59 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -6.7 | `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 28.6% | -4.1 | 0.56 | 1.41 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -10.0 | `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 20.0% | -12.5 | 0.07 | 0.20 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 39 | S_STRANGER | 17.9% | -4.6 | `feature_extreme_hunt_with_exception` | 34 | S_STRANGER | 20.6% | -1.9 | 0.61 | 1.67 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 28 | S_STRANGER | 17.9% | -1.0 | `confluence_gte_70` | 8 | R_REPEATER | 50.0% | +4.8 | 4.36 | 3.27 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 28 | S_STRANGER | 17.9% | -3.8 | `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 27.3% | +0.5 | 1.12 | 2.60 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 17 | S_STRANGER | 17.6% | -2.6 | `confluence_gte_60` | 9 | S_STRANGER | 22.2% | -0.0 | 1.00 | 1.66 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 40 | S_STRANGER | 17.5% | -6.5 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 31.2% | +1.9 | 1.53 | 2.44 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 29 | S_STRANGER | 17.2% | -0.3 | `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 26.7% | +2.7 | 1.87 | 5.13 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 29 | S_STRANGER | 17.2% | -2.2 | `tdi_rsi_gt_signal` | 10 | S_STRANGER | 30.0% | -0.1 | 0.98 | 1.64 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 16.7% | -1.7 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 28.6% | +4.4 | 2.85 | 7.12 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 30 | S_STRANGER | 16.7% | -1.9 | `stop_hunt_le_90` | 27 | S_STRANGER | 18.5% | -1.4 | 0.63 | 2.76 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 30 | S_STRANGER | 16.7% | -2.2 | `tdi_rsi_gte_50` | 19 | S_STRANGER | 26.3% | -0.0 | 1.00 | 2.80 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -2.5 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 28.6% | +2.8 | 1.53 | 3.84 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 24 | S_STRANGER | 16.7% | -5.6 | `confluence_gte_70` | 7 | S_STRANGER | 28.6% | -5.3 | 0.50 | 1.24 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 24 | S_STRANGER | 16.7% | -21.1 | `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 37.5% | -9.2 | 0.38 | 0.63 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 50 | S_STRANGER | 16.0% | -1.7 | `confluence_gte_60` | 21 | S_STRANGER | 23.8% | +1.0 | 1.18 | 3.54 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 26 | S_STRANGER | 15.4% | -2.8 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | +2.1 | 2.35 | 4.70 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -3.9 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 20.0% | +1.1 | 1.36 | 4.08 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -5.3 | `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 33.3% | +0.8 | 1.29 | 1.29 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 33 | S_STRANGER | 15.2% | -2.4 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 40.0% | +5.2 | 2.30 | 3.44 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 15.0% | +2.3 | `tdi_rsi_gte_50` | 14 | S_STRANGER | 21.4% | +3.5 | 3.10 | 9.29 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 20 | S_STRANGER | 15.0% | -2.3 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 25.0% | +4.1 | 33.80 | 8.45 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -1.4 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 22.2% | +0.5 | 1.06 | 3.17 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -3.5 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | +4.8 | 2.60 | 2.60 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L2|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 14.3% | -4.4 | `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 16.7% | -4.1 | 0.27 | 0.62 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -4.7 | `asian_range_gte_30` | 8 | S_STRANGER | 25.0% | -1.8 | 0.67 | 2.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 21 | S_STRANGER | 14.3% | -5.5 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 28.6% | +2.7 | 2.04 | 4.07 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 21 | S_STRANGER | 14.3% | -21.4 | `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 42.9% | -1.5 | 0.66 | 0.88 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 13.3% | -2.8 | `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 28.6% | -1.3 | 0.62 | 1.54 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 46 | S_STRANGER | 13.0% | -5.2 | `confluence_gte_70` | 11 | S_STRANGER | 18.2% | -2.8 | 0.53 | 2.38 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 31 | S_STRANGER | 12.9% | -3.9 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 25.0% | +2.0 | 1.58 | 3.95 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 32 | S_STRANGER | 12.5% | -3.8 | `tdi_rsi_gte_50` | 18 | S_STRANGER | 16.7% | -4.6 | 0.27 | 1.07 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 12.5% | -4.0 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 20.0% | -3.1 | 0.42 | 1.27 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 17 | S_STRANGER | 11.8% | +0.3 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 22.2% | +4.6 | 5.78 | 11.57 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 11.8% | -2.1 | `asian_range_gte_30` | 10 | S_STRANGER | 20.0% | +0.0 | 1.01 | 3.03 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 34 | S_STRANGER | 11.8% | -4.2 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 25.0% | -0.4 | 0.95 | 2.86 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 18 | S_STRANGER | 11.1% | -1.7 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 16.7% | -1.0 | 0.72 | 3.62 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74` | 18 | S_STRANGER | 11.1% | -12.5 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 16.7% | +2.9 | 3.27 | 13.09 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 102 | S_STRANGER | 10.8% | -7.3 | `asian_range_gte_30` | 81 | S_STRANGER | 13.6% | -5.7 | 0.26 | 1.39 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -3.0 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 11.1% | -2.0 | 0.66 | 4.62 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -4.3 | `all` | 10 | S_STRANGER | 10.0% | -4.3 | 0.15 | 1.23 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -4.9 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 12.5% | -4.3 | 0.30 | 2.11 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 10.0% | -5.8 | `feature_extreme_hunt_with_exception` | 5 | S_STRANGER | 20.0% | -4.6 | 0.42 | 1.70 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -13.2 | `confluence_gte_60` | 6 | S_STRANGER | 16.7% | -10.3 | 0.20 | 1.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 51 | S_STRANGER | 9.8% | -4.8 | `confluence_gte_60` | 26 | S_STRANGER | 15.4% | -4.0 | 0.41 | 1.97 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 41 | S_STRANGER | 9.8% | -5.6 | `tdi_rsi_gte_50` | 15 | S_STRANGER | 13.3% | -4.2 | 0.38 | 2.30 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 21 | S_STRANGER | 9.5% | -3.9 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 25.0% | -1.2 | 0.56 | 1.39 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 21 | S_STRANGER | 9.5% | -9.8 | `tdi_rsi_gt_signal` | 12 | S_STRANGER | 16.7% | -1.4 | 0.82 | 2.19 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 11 | S_STRANGER | 9.1% | -9.1 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 14.3% | -4.1 | 0.36 | 2.14 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 78 | S_STRANGER | 9.0% | -4.9 | `feature_momentum_breakout_exception` | 9 | S_STRANGER | 11.1% | +1.3 | 1.37 | 9.59 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 8.3% | -5.8 | `stop_hunt_le_90` | 9 | S_STRANGER | 11.1% | -3.9 | 0.23 | 1.39 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 8.3% | -6.2 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 14.3% | -7.2 | 0.35 | 2.12 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 8.3% | -6.3 | `asian_range_gte_30` | 6 | S_STRANGER | 16.7% | -9.5 | 0.06 | 0.23 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 38 | S_STRANGER | 7.9% | -16.2 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 27.3% | +5.7 | 2.27 | 3.97 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 7.1% | -7.9 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 16.7% | -9.6 | 0.22 | 1.08 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 7.1% | -9.5 | `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 14.3% | -2.3 | 0.44 | 2.63 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 14 | S_STRANGER | 7.1% | -17.0 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 20.0% | -11.0 | 0.26 | 1.03 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 14 | S_STRANGER | 7.1% | -17.4 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 14.3% | -7.1 | 0.31 | 1.86 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 6.7% | -14.5 | `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 7.1% | -11.1 | 0.13 | 1.50 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 16 | S_STRANGER | 6.2% | -7.4 | `confluence_gte_60` | 10 | S_STRANGER | 10.0% | -1.9 | 0.47 | 4.25 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 17 | S_STRANGER | 5.9% | -6.1 | `all` | 17 | S_STRANGER | 5.9% | -6.1 | 0.19 | 2.66 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 5.3% | -4.8 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 14.3% | +0.2 | 1.08 | 3.23 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 19 | S_STRANGER | 5.3% | -8.4 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 16.7% | -5.8 | 0.12 | 0.62 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 22 | S_STRANGER | 4.5% | -7.8 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 11.1% | -4.6 | 0.01 | 0.06 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 26 | S_STRANGER | 3.8% | -4.9 | `tdi_rsi_gt_signal` | 15 | S_STRANGER | 6.7% | -5.3 | 0.15 | 1.94 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 27 | S_STRANGER | 3.7% | -13.0 | `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 9.1% | -6.1 | 0.25 | 2.25 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 29 | S_STRANGER | 3.4% | -8.9 | `tdi_rsi_gte_50` | 13 | S_STRANGER | 7.7% | -11.5 | 0.00 | 0.01 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -2.5 | `all` | 10 | S_STRANGER | 0.0% | -2.5 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 12 | S_STRANGER | 0.0% | -2.5 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 0.0% | -1.8 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 13 | S_STRANGER | 0.0% | -3.4 | `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 0.0% | -3.1 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -4.5 | `all` | 10 | S_STRANGER | 0.0% | -4.5 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 0.0% | -7.4 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 0.0% | -4.8 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 14 | S_STRANGER | 0.0% | -12.6 | `tdi_rsi_gt_signal` | 10 | S_STRANGER | 0.0% | -12.8 | 0.07 | 0.58 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | S_STRANGER | 0.0% | -12.7 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 0.0% | -8.0 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -12.8 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 0.0% | -9.3 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 0.0% | -18.4 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 0.0% | -12.7 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 0.0% | -23.6 | `all` | 10 | S_STRANGER | 0.0% | -23.6 | 0.04 | 0.32 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 20 | S_STRANGER | 0.0% | -30.2 | `confluence_gte_70` | 5 | S_STRANGER | 0.0% | -8.6 | 0.01 | 0.05 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 0.0% | -32.0 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 0.0% | -28.7 | 0.03 | 0.16 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -35.9 | `all` | 10 | S_STRANGER | 0.0% | -35.9 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 15 | S_STRANGER | 0.0% | -42.6 | `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 0.0% | -40.6 | 0.00 | 0.00 | 0 | 0 | fail |

## Candidate Details

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=55.6% Avg=+5.2; validation N=6 Fav=66.7% Avg=+5.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | R_REPEATER | 100.0% | 60.0% | 60.0% | 46.7% | +5.4 | 3.04 | 1.69 | +14.6 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 15 | R_REPEATER | 100.0% | 60.0% | 60.0% | 46.7% | +5.4 | 3.04 | 1.69 | +14.6 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 15 | R_REPEATER | 100.0% | 60.0% | 60.0% | 46.7% | +5.4 | 3.04 | 1.69 | +14.6 | +5.4 |
| `stop_hunt_le_90` | 15 | R_REPEATER | 100.0% | 60.0% | 60.0% | 46.7% | +5.4 | 3.04 | 1.69 | +14.6 | +5.4 |
| `asian_range_gte_30` | 15 | R_REPEATER | 100.0% | 60.0% | 60.0% | 46.7% | +5.4 | 3.04 | 1.69 | +14.6 | +5.4 |
| `confluence_gte_60` | 15 | R_REPEATER | 100.0% | 60.0% | 60.0% | 46.7% | +5.4 | 3.04 | 1.69 | +14.6 | +5.4 |
| `confluence_gte_70` | 15 | R_REPEATER | 100.0% | 60.0% | 60.0% | 46.7% | +5.4 | 3.04 | 1.69 | +14.6 | +5.4 |
| `tdi_rsi_gt_signal` | 10 | R_REPEATER | 66.7% | 50.0% | 50.0% | 30.0% | +5.3 | 4.26 | 3.41 | +13.9 | +6.9 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 40.0% | 33.3% | 33.3% | 16.7% | +2.2 | 1.83 | 2.74 | +12.2 | +7.5 |
| `ratio_le_2_and_asian_gte_30` | 15 | R_REPEATER | 100.0% | 60.0% | 60.0% | 46.7% | +5.4 | 3.04 | 1.69 | +14.6 | +5.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | R_REPEATER | 66.7% | 50.0% | 50.0% | 30.0% | +5.3 | 4.26 | 3.41 | +13.9 | +6.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | R_REPEATER | 100.0% | 60.0% | 60.0% | 46.7% | +5.4 | 3.04 | 1.69 | +14.6 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 15 | R_REPEATER | 100.0% | 60.0% | 60.0% | 46.7% | +5.4 | 3.04 | 1.69 | +14.6 | +5.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=12 Fav=41.7% Avg=+5.0; validation N=15 Fav=60.0% Avg=+14.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | R_REPEATER | 100.0% | 51.5% | 51.5% | 36.4% | +10.3 | 3.81 | 3.36 | +24.4 | +7.9 |
| `hunt_to_ar_ratio_le_2_0` | 26 | R_REPEATER | 78.8% | 50.0% | 50.0% | 38.5% | +8.3 | 2.94 | 2.71 | +24.1 | +8.9 |
| `hunt_to_ar_ratio_le_2_5` | 28 | R_REPEATER | 84.8% | 50.0% | 50.0% | 39.3% | +10.1 | 3.50 | 3.25 | +25.2 | +8.7 |
| `stop_hunt_le_90` | 30 | R_REPEATER | 90.9% | 50.0% | 50.0% | 40.0% | +9.9 | 3.61 | 3.37 | +24.6 | +8.2 |
| `asian_range_gte_30` | 27 | R_REPEATER | 81.8% | 51.9% | 51.9% | 33.3% | +10.4 | 3.53 | 3.02 | +25.7 | +8.4 |
| `confluence_gte_60` | 33 | R_REPEATER | 100.0% | 51.5% | 51.5% | 36.4% | +10.3 | 3.81 | 3.36 | +24.4 | +7.9 |
| `confluence_gte_70` | 33 | R_REPEATER | 100.0% | 51.5% | 51.5% | 36.4% | +10.3 | 3.81 | 3.36 | +24.4 | +7.9 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 21.2% | 42.9% | 42.9% | 28.6% | +4.8 | 1.84 | 2.46 | +29.2 | +12.2 |
| `tdi_rsi_gte_50` | 29 | R_REPEATER | 87.9% | 51.7% | 51.7% | 31.0% | +10.4 | 3.59 | 3.35 | +25.6 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 72.7% | 45.8% | 45.8% | 33.3% | +6.7 | 2.44 | 2.66 | +23.3 | +9.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 21.2% | 42.9% | 42.9% | 28.6% | +4.8 | 1.84 | 2.46 | +29.2 | +12.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | R_REPEATER | 90.9% | 50.0% | 50.0% | 40.0% | +9.9 | 3.61 | 3.37 | +24.6 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 33 | R_REPEATER | 100.0% | 51.5% | 51.5% | 36.4% | +10.3 | 3.81 | 3.36 | +24.4 | +7.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=66.7% Avg=+14.3; validation N=3 Fav=33.3% Avg=+1.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 43.2% | 43.2% | 21.6% | +5.0 | 3.38 | 4.23 | +12.9 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 9 | R_REPEATER | 24.3% | 55.6% | 55.6% | 44.4% | +12.1 | 6.41 | 3.84 | +19.1 | +3.9 |
| `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 32.4% | 58.3% | 58.3% | 50.0% | +11.2 | 7.64 | 4.37 | +19.4 | +3.1 |
| `stop_hunt_le_90` | 34 | S_STRANGER | 91.9% | 41.2% | 41.2% | 20.6% | +4.5 | 3.08 | 4.17 | +12.4 | +4.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 37 | S_STRANGER | 100.0% | 43.2% | 43.2% | 21.6% | +5.0 | 3.38 | 4.23 | +12.9 | +3.9 |
| `confluence_gte_70` | 37 | S_STRANGER | 100.0% | 43.2% | 43.2% | 21.6% | +5.0 | 3.38 | 4.23 | +12.9 | +3.9 |
| `tdi_rsi_gt_signal` | 24 | S_STRANGER | 64.9% | 45.8% | 45.8% | 20.8% | +3.7 | 3.16 | 3.45 | +11.8 | +3.2 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 64.9% | 45.8% | 45.8% | 16.7% | +6.1 | 3.23 | 3.82 | +14.9 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 34 | S_STRANGER | 91.9% | 41.2% | 41.2% | 20.6% | +4.5 | 3.08 | 4.17 | +12.4 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 43.2% | 43.2% | 21.6% | +5.0 | 3.38 | 4.23 | +12.9 | +3.9 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 2.7% | 100.0% | 100.0% | 100.0% | +10.4 | 999.00 | 999.00 | +21.7 | +1.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=37.5% Avg=+1.2; validation N=4 Fav=50.0% Avg=-1.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | -0.8 | 0.86 | 1.14 | +10.2 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 50.0% | -1.1 | 0.55 | 0.55 | +8.5 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 3 | R_REPEATER | 21.4% | 66.7% | 66.7% | 66.7% | +4.0 | 3.37 | 1.69 | +10.7 | +4.1 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 92.9% | 38.5% | 38.5% | 23.1% | -1.9 | 0.68 | 1.09 | +9.3 | +8.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | -0.8 | 0.86 | 1.14 | +10.2 | +8.2 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | -0.8 | 0.86 | 1.14 | +10.2 | +8.2 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 28.6% | 50.0% | 50.0% | 25.0% | +2.4 | 1.51 | 1.51 | +11.6 | +5.6 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 85.7% | 41.7% | 41.7% | 16.7% | +0.5 | 1.11 | 1.55 | +9.9 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 92.9% | 38.5% | 38.5% | 23.1% | -1.9 | 0.68 | 1.09 | +9.3 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 21.4% | -0.8 | 0.86 | 1.14 | +10.2 | +8.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +0.0 | +12.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +0.0 | +12.9 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=25.0% Avg=-1.2; out_of_sample N=5 Fav=80.0% Avg=+8.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 42.3% | 42.3% | 26.9% | +1.3 | 1.29 | 1.64 | +11.5 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 23.1% | 16.7% | 16.7% | 33.3% | -1.9 | 0.24 | 0.95 | +7.4 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 50.0% | 38.5% | 38.5% | 38.5% | +2.2 | 1.83 | 2.57 | +11.5 | +6.6 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 42.3% | 42.3% | 26.9% | +1.3 | 1.29 | 1.64 | +11.5 | +6.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 26 | S_STRANGER | 100.0% | 42.3% | 42.3% | 26.9% | +1.3 | 1.29 | 1.64 | +11.5 | +6.7 |
| `confluence_gte_70` | 26 | S_STRANGER | 100.0% | 42.3% | 42.3% | 26.9% | +1.3 | 1.29 | 1.64 | +11.5 | +6.7 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 42.3% | 36.4% | 36.4% | 18.2% | +3.4 | 2.39 | 4.18 | +10.9 | +5.4 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 50.0% | 46.2% | 46.2% | 15.4% | +2.4 | 1.94 | 2.26 | +11.0 | +7.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 42.3% | 42.3% | 26.9% | +1.3 | 1.29 | 1.64 | +11.5 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 42.3% | 42.3% | 26.9% | +1.3 | 1.29 | 1.64 | +11.5 | +6.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=57.1% Avg=+9.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 50.0% | 33.3% | +8.1 | 3.91 | 3.91 | +19.3 | +9.6 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 16.7% | +2.8 | 1.55 | 7.73 | +13.1 | +11.8 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 58.3% | 14.3% | 28.6% | 14.3% | +2.6 | 1.60 | 4.00 | +11.9 | +10.7 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 91.7% | 45.5% | 54.5% | 36.4% | +9.2 | 4.32 | 3.60 | +21.0 | +8.9 |
| `asian_range_gte_30` | 3 | S_STRANGER | 25.0% | 33.3% | 66.7% | 33.3% | +15.2 | 15.22 | 7.61 | +17.7 | +9.2 |
| `confluence_gte_60` | 8 | S_STRANGER | 66.7% | 37.5% | 50.0% | 25.0% | +7.2 | 2.97 | 2.97 | +16.9 | +8.8 |
| `confluence_gte_70` | 2 | R_REPEATER | 16.7% | 50.0% | 100.0% | 50.0% | +24.3 | 999.00 | 999.00 | +26.0 | +5.0 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 91.7% | 45.5% | 54.5% | 36.4% | +9.6 | 5.01 | 4.18 | +20.0 | +9.8 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 58.3% | 57.1% | 57.1% | 42.9% | +9.2 | 4.56 | 3.42 | +23.5 | +10.2 |
| `ratio_le_2_and_asian_gte_30` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +47.0 | 999.00 | 999.00 | +47.6 | +5.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +47.0 | 999.00 | 999.00 | +47.6 | +5.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 45.5% | 54.5% | 36.4% | +9.2 | 4.32 | 3.60 | +21.0 | +8.9 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 41.7% | 50.0% | 33.3% | +8.1 | 3.91 | 3.91 | +19.3 | +9.6 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +4.8 | +14.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +5.5 | +16.3 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=62.5% Avg=+15.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 41.2% | 41.2% | 29.4% | +4.3 | 1.81 | 2.33 | +18.2 | +9.6 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 82.4% | 42.9% | 42.9% | 28.6% | +5.0 | 2.11 | 2.47 | +18.4 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 41.2% | 41.2% | 29.4% | +4.3 | 1.81 | 2.33 | +18.2 | +9.6 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 94.1% | 37.5% | 37.5% | 25.0% | +2.7 | 1.47 | 2.21 | +17.3 | +9.8 |
| `asian_range_gte_30` | 15 | S_STRANGER | 88.2% | 46.7% | 46.7% | 33.3% | +6.5 | 2.50 | 2.50 | +19.9 | +8.4 |
| `confluence_gte_60` | 8 | R_REPEATER | 47.1% | 62.5% | 62.5% | 50.0% | +15.2 | 6.28 | 2.51 | +26.9 | +7.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | R_REPEATER | 29.4% | 60.0% | 60.0% | 20.0% | +12.9 | 3.63 | 2.42 | +29.6 | +10.8 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 64.7% | 45.5% | 45.5% | 18.2% | +4.6 | 1.89 | 2.27 | +19.7 | +10.1 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 76.5% | 46.2% | 46.2% | 30.8% | +6.3 | 2.65 | 2.65 | +19.7 | +8.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_RUNNER | 23.5% | 75.0% | 75.0% | 25.0% | +20.0 | 9.49 | 3.16 | +34.6 | +9.7 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 5.9% | 100.0% | 100.0% | 100.0% | +30.5 | 999.00 | 999.00 | +32.8 | +6.1 |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 82.4% | 42.9% | 42.9% | 28.6% | +5.0 | 2.11 | 2.47 | +18.4 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 94.1% | 43.8% | 43.8% | 31.2% | +5.3 | 2.09 | 2.39 | +18.7 | +8.9 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 29.4% | 40.0% | 40.0% | 20.0% | +3.0 | 1.64 | 2.47 | +15.6 | +7.9 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 29.4% | 20.0% | 20.0% | 0.0% | -5.5 | 0.21 | 0.83 | +10.8 | +10.9 |

### THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=57.1% Avg=+8.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +4.3 | 2.46 | 3.07 | +12.1 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +4.8 | 2.46 | 3.07 | +12.7 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +4.3 | 2.46 | 3.07 | +12.1 | +5.0 |
| `stop_hunt_le_90` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +4.8 | 2.46 | 3.07 | +12.7 | +5.4 |
| `asian_range_gte_30` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 44.4% | +5.8 | 3.56 | 3.56 | +13.4 | +4.1 |
| `confluence_gte_60` | 7 | R_REPEATER | 70.0% | 57.1% | 57.1% | 57.1% | +8.2 | 4.74 | 2.37 | +14.7 | +4.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | +1.1 | 1.23 | 3.69 | +11.1 | +7.1 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | +6.9 | 8.39 | 16.79 | +11.4 | +3.3 |
| `ratio_le_2_and_asian_gte_30` | 8 | R_REPEATER | 80.0% | 50.0% | 50.0% | 37.5% | +6.6 | 3.56 | 3.56 | +14.3 | +4.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | +1.1 | 1.23 | 3.69 | +11.1 | +7.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +4.8 | 2.46 | 3.07 | +12.7 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +4.3 | 2.46 | 3.07 | +12.1 | +5.0 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +7.7 | 11.96 | 11.96 | +15.5 | +3.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +4.5 | +3.5 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=83.3% Avg=+10.6; validation N=2 Fav=50.0% Avg=+1.8; out_of_sample N=6 Fav=16.7% Avg=-5.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 39.1% | 39.1% | 30.4% | +2.7 | 1.61 | 2.32 | +14.5 | +8.6 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 100.0% | 39.1% | 39.1% | 30.4% | +2.7 | 1.61 | 2.32 | +14.5 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 39.1% | 39.1% | 30.4% | +2.7 | 1.61 | 2.32 | +14.5 | +8.6 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 39.1% | 39.1% | 30.4% | +2.7 | 1.61 | 2.32 | +14.5 | +8.6 |
| `asian_range_gte_30` | 14 | R_REPEATER | 60.9% | 50.0% | 50.0% | 42.9% | +2.3 | 1.52 | 1.30 | +15.4 | +8.2 |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 39.1% | 39.1% | 30.4% | +2.7 | 1.61 | 2.32 | +14.5 | +8.6 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 39.1% | 39.1% | 30.4% | +2.7 | 1.61 | 2.32 | +14.5 | +8.6 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 21.7% | 40.0% | 40.0% | 40.0% | +1.2 | 1.38 | 2.07 | +12.4 | +8.5 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 78.3% | 44.4% | 44.4% | 27.8% | +4.0 | 1.86 | 2.32 | +16.9 | +9.5 |
| `ratio_le_2_and_asian_gte_30` | 14 | R_REPEATER | 60.9% | 50.0% | 50.0% | 42.9% | +2.3 | 1.52 | 1.30 | +15.4 | +8.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_RUNNER | 8.7% | 100.0% | 100.0% | 100.0% | +10.5 | 999.00 | 999.00 | +28.1 | +3.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 39.1% | 39.1% | 30.4% | +2.7 | 1.61 | 2.32 | +14.5 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 39.1% | 39.1% | 30.4% | +2.7 | 1.61 | 2.32 | +14.5 | +8.6 |
| `feature_momentum_breakout_exception` | 4 | R_RUNNER | 17.4% | 75.0% | 75.0% | 50.0% | +7.7 | 5.15 | 1.72 | +20.4 | +3.8 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_RUNNER | 13.0% | 100.0% | 100.0% | 66.7% | +12.7 | 999.00 | 999.00 | +26.5 | +2.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=-3.4; validation N=10 Fav=60.0% Avg=+15.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 42 | S_STRANGER | 100.0% | 38.1% | 38.1% | 21.4% | +3.8 | 2.22 | 2.92 | +14.4 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 37 | S_STRANGER | 88.1% | 37.8% | 37.8% | 24.3% | +3.9 | 2.21 | 2.84 | +15.0 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 41 | S_STRANGER | 97.6% | 36.6% | 36.6% | 22.0% | +3.4 | 2.07 | 2.90 | +14.2 | +7.6 |
| `stop_hunt_le_90` | 41 | S_STRANGER | 97.6% | 39.0% | 39.0% | 22.0% | +4.0 | 2.23 | 2.79 | +14.5 | +7.4 |
| `asian_range_gte_30` | 31 | S_STRANGER | 73.8% | 35.5% | 35.5% | 22.6% | +5.1 | 3.19 | 4.35 | +16.0 | +7.1 |
| `confluence_gte_60` | 42 | S_STRANGER | 100.0% | 38.1% | 38.1% | 21.4% | +3.8 | 2.22 | 2.92 | +14.4 | +7.4 |
| `confluence_gte_70` | 42 | S_STRANGER | 100.0% | 38.1% | 38.1% | 21.4% | +3.8 | 2.22 | 2.92 | +14.4 | +7.4 |
| `tdi_rsi_gt_signal` | 25 | S_STRANGER | 59.5% | 44.0% | 44.0% | 20.0% | +5.6 | 2.68 | 2.92 | +18.4 | +7.8 |
| `tdi_rsi_gte_50` | 30 | S_STRANGER | 71.4% | 43.3% | 43.3% | 13.3% | +4.9 | 2.35 | 2.53 | +16.3 | +8.5 |
| `ratio_le_2_and_asian_gte_30` | 28 | S_STRANGER | 66.7% | 35.7% | 35.7% | 25.0% | +5.2 | 3.08 | 4.01 | +16.7 | +7.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | R_REPEATER | 35.7% | 53.3% | 53.3% | 26.7% | +8.9 | 3.97 | 2.48 | +24.3 | +7.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 41 | S_STRANGER | 97.6% | 39.0% | 39.0% | 22.0% | +4.0 | 2.23 | 2.79 | +14.5 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 42 | S_STRANGER | 100.0% | 38.1% | 38.1% | 21.4% | +3.8 | 2.22 | 2.92 | +14.4 | +7.4 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 4.8% | 50.0% | 50.0% | 0.0% | +2.8 | 1.67 | 1.67 | +10.4 | +7.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 4.8% | 50.0% | 50.0% | 0.0% | +2.8 | 1.67 | 1.67 | +10.4 | +7.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=62.5% Avg=+7.5; out_of_sample N=8 Fav=25.0% Avg=+1.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 37.5% | 45.8% | 16.7% | +5.2 | 2.15 | 2.55 | +16.2 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 79.2% | 36.8% | 47.4% | 15.8% | +4.4 | 2.13 | 2.37 | +15.2 | +5.9 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 83.3% | 35.0% | 45.0% | 15.0% | +3.6 | 1.85 | 2.26 | +14.5 | +6.2 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 91.7% | 36.4% | 45.5% | 18.2% | +5.1 | 2.08 | 2.50 | +16.0 | +7.2 |
| `asian_range_gte_30` | 18 | S_STRANGER | 75.0% | 33.3% | 44.4% | 11.1% | +3.9 | 1.96 | 2.45 | +15.4 | +6.4 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 37.5% | 45.8% | 16.7% | +5.2 | 2.15 | 2.55 | +16.2 | +7.1 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 37.5% | 45.8% | 16.7% | +5.2 | 2.15 | 2.55 | +16.2 | +7.1 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 50.0% | 33.3% | 50.0% | 25.0% | +5.5 | 2.13 | 2.13 | +16.7 | +7.9 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 66.7% | 43.8% | 50.0% | 12.5% | +4.7 | 2.23 | 2.23 | +16.0 | +7.1 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 66.7% | 31.2% | 43.8% | 12.5% | +3.6 | 1.84 | 2.37 | +15.2 | +6.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 41.7% | 20.0% | 40.0% | 10.0% | -0.8 | 0.86 | 1.29 | +11.9 | +7.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 91.7% | 36.4% | 45.5% | 18.2% | +5.1 | 2.08 | 2.50 | +16.0 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 37.5% | 45.8% | 16.7% | +5.2 | 2.15 | 2.55 | +16.2 | +7.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=42.9% Avg=+1.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | -2.4 | 0.75 | 1.32 | +14.0 | +15.7 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -15.2 | 0.00 | 0.00 | +3.9 | +20.0 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 42.9% | +1.1 | 1.11 | 1.49 | +18.8 | +17.5 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | -2.4 | 0.75 | 1.32 | +14.0 | +15.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -12.6 | 0.00 | 0.00 | +8.4 | +12.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | R_REPEATER | 27.3% | 66.7% | 66.7% | 66.7% | +2.2 | 1.20 | 0.60 | +25.9 | +20.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 33.3% | -7.5 | 0.47 | 0.94 | +17.5 | +24.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 25.0% | -3.7 | 0.63 | 1.88 | +11.3 | +17.7 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | -2.4 | 0.75 | 1.32 | +14.0 | +15.7 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 33.3% | -2.8 | 0.64 | 1.28 | +11.4 | +9.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 50.0% | +0.0 | 1.00 | 1.00 | +27.7 | +15.1 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+25.7; validation N=7 Fav=42.9% Avg=+6.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 21.4% | +7.5 | 5.73 | 8.59 | +16.5 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 42.9% | 41.7% | 41.7% | 33.3% | +14.6 | 9.94 | 13.92 | +23.0 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 53.6% | 40.0% | 40.0% | 33.3% | +11.8 | 8.92 | 11.89 | +19.7 | +4.6 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 96.4% | 37.0% | 37.0% | 22.2% | +8.0 | 6.32 | 8.85 | +16.8 | +4.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 21.4% | +7.5 | 5.73 | 8.59 | +16.5 | +4.3 |
| `confluence_gte_70` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 21.4% | +7.5 | 5.73 | 8.59 | +16.5 | +4.3 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 21.4% | 33.3% | 33.3% | 33.3% | +10.8 | 4.54 | 6.80 | +18.6 | +6.0 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 85.7% | 41.7% | 41.7% | 25.0% | +9.2 | 7.21 | 7.94 | +18.3 | +4.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 96.4% | 37.0% | 37.0% | 22.2% | +8.0 | 6.32 | 8.85 | +16.8 | +4.2 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 21.4% | +7.5 | 5.73 | 8.59 | +16.5 | +4.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=11 Fav=45.5% Avg=+3.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 35.7% | +1.9 | 1.52 | 2.03 | +13.5 | +8.5 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 1 | R_RUNNER | 7.1% | 100.0% | 100.0% | 100.0% | +10.8 | 999.00 | 999.00 | +28.7 | +0.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 78.6% | 45.5% | 45.5% | 45.5% | +3.5 | 2.17 | 2.60 | +15.7 | +8.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 35.7% | +1.9 | 1.52 | 2.03 | +13.5 | +8.5 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 35.7% | +1.9 | 1.52 | 2.03 | +13.5 | +8.5 |
| `tdi_rsi_gt_signal` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 50.0% | 28.6% | 28.6% | 28.6% | +0.7 | 1.16 | 2.89 | +13.3 | +11.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 64.3% | 33.3% | 33.3% | 33.3% | -0.2 | 0.95 | 1.90 | +12.1 | +9.6 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 35.7% | +1.9 | 1.52 | 2.03 | +13.5 | +8.5 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 35.7% | 40.0% | 40.0% | 40.0% | +3.1 | 1.80 | 2.70 | +14.9 | +8.1 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 33.3% | +4.4 | 2.21 | 4.43 | +14.7 | +9.6 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+6.9; validation N=6 Fav=33.3% Avg=+2.3; out_of_sample N=10 Fav=30.0% Avg=+5.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +4.2 | 2.85 | 5.23 | +12.1 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +9.5 | +8.3 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 58.8% | 30.0% | 30.0% | 20.0% | +0.8 | 1.28 | 2.98 | +10.9 | +5.9 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +4.2 | 2.85 | 5.23 | +12.1 | +5.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +4.2 | 2.85 | 5.23 | +12.1 | +5.5 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +4.2 | 2.85 | 5.23 | +12.1 | +5.5 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 88.2% | 33.3% | 33.3% | 26.7% | +2.5 | 2.07 | 4.15 | +10.8 | +5.5 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 70.6% | 25.0% | 25.0% | 16.7% | +1.8 | 1.76 | 5.27 | +10.0 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +4.2 | 2.85 | 5.23 | +12.1 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +4.2 | 2.85 | 5.23 | +12.1 | +5.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+15.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=50.0% Avg=-8.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 34.8% | 34.8% | 34.8% | -0.5 | 0.93 | 1.63 | +13.9 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 95.7% | 36.4% | 36.4% | 31.8% | -0.5 | 0.93 | 1.63 | +14.1 | +8.5 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 95.7% | 36.4% | 36.4% | 31.8% | -0.5 | 0.93 | 1.63 | +14.1 | +8.5 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 34.8% | 34.8% | 34.8% | -0.5 | 0.93 | 1.63 | +13.9 | +8.2 |
| `asian_range_gte_30` | 19 | S_STRANGER | 82.6% | 31.6% | 31.6% | 31.6% | -0.8 | 0.90 | 1.95 | +13.4 | +8.1 |
| `confluence_gte_60` | 19 | S_STRANGER | 82.6% | 31.6% | 31.6% | 31.6% | -2.0 | 0.76 | 1.53 | +13.5 | +9.5 |
| `confluence_gte_70` | 8 | S_STRANGER | 34.8% | 37.5% | 37.5% | 25.0% | +0.1 | 1.01 | 1.68 | +17.5 | +12.4 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 73.9% | 41.2% | 41.2% | 35.3% | +1.0 | 1.13 | 1.62 | +16.9 | +8.7 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 30.4% | 57.1% | 57.1% | 42.9% | +8.8 | 2.77 | 2.08 | +24.7 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 82.6% | 31.6% | 31.6% | 31.6% | -0.8 | 0.90 | 1.95 | +13.4 | +8.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 60.9% | 35.7% | 35.7% | 35.7% | +1.0 | 1.13 | 2.03 | +16.6 | +8.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 34.8% | 34.8% | 34.8% | -0.5 | 0.93 | 1.63 | +13.9 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 34.8% | 34.8% | 34.8% | -0.5 | 0.93 | 1.63 | +13.9 | +8.2 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 30.4% | 42.9% | 42.9% | 42.9% | +1.7 | 1.37 | 1.83 | +13.5 | +7.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_RUNNER | 8.7% | 100.0% | 100.0% | 100.0% | +14.8 | 999.00 | 999.00 | +32.9 | +1.5 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=38.5% Avg=+5.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 46.7% | +4.6 | 3.69 | 3.07 | +12.6 | +5.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 86.7% | 30.8% | 38.5% | 53.8% | +4.2 | 3.14 | 3.14 | +12.4 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 46.7% | +4.6 | 3.69 | 3.07 | +12.6 | +5.1 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 46.7% | +4.6 | 3.69 | 3.07 | +12.6 | +5.1 |
| `asian_range_gte_30` | 13 | S_STRANGER | 86.7% | 38.5% | 46.2% | 38.5% | +5.3 | 3.69 | 3.07 | +12.9 | +5.3 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 46.7% | +4.6 | 3.69 | 3.07 | +12.6 | +5.1 |
| `confluence_gte_70` | 9 | S_STRANGER | 60.0% | 33.3% | 33.3% | 33.3% | +5.3 | 4.67 | 6.23 | +11.3 | +5.1 |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 6.7% | 100.0% | 100.0% | 0.0% | +14.0 | 999.00 | 999.00 | +19.9 | +8.3 |
| `tdi_rsi_gte_50` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 0.0% | +7.0 | 999.00 | 999.00 | +13.9 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 73.3% | 36.4% | 45.5% | 45.5% | +4.9 | 3.14 | 3.14 | +12.7 | +5.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 46.7% | +4.6 | 3.69 | 3.07 | +12.6 | +5.1 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 46.7% | +4.6 | 3.69 | 3.07 | +12.6 | +5.1 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 26.7% | 25.0% | 25.0% | 50.0% | +3.9 | 2.72 | 5.44 | +13.8 | +5.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=44.4% Avg=+5.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 50.0% | +3.6 | 3.52 | 4.40 | +14.4 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | +6.9 | 5.60 | 5.60 | +16.9 | +2.6 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 66.7% | +4.6 | 5.60 | 5.60 | +15.2 | +2.2 |
| `stop_hunt_le_90` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 55.6% | +5.9 | 9.21 | 6.91 | +16.2 | +2.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 4 | R_RUNNER | 33.3% | 75.0% | 75.0% | 75.0% | +11.8 | 95.50 | 31.83 | +20.4 | +2.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +5.2 | +7.9 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 33.3% | +2.6 | 2.14 | 3.21 | +14.5 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 66.7% | +13.2 | 14.18 | 7.09 | +20.0 | +2.3 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 50.0% | +3.6 | 3.52 | 4.40 | +14.4 | +4.9 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 57.1% | +2.0 | 4.94 | 4.94 | +15.6 | +4.8 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 33.3% | +3.0 | 4.03 | 4.03 | +16.8 | +8.1 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=41.7% Avg=+3.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 44.4% | +3.3 | 1.56 | 2.60 | +16.8 | +13.0 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 88.9% | 37.5% | 37.5% | 50.0% | +5.4 | 2.08 | 2.77 | +18.6 | +12.4 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 88.9% | 37.5% | 37.5% | 50.0% | +5.4 | 2.08 | 2.77 | +18.6 | +12.4 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 88.9% | 37.5% | 37.5% | 50.0% | +5.4 | 2.08 | 2.77 | +18.6 | +12.4 |
| `asian_range_gte_30` | 12 | S_STRANGER | 66.7% | 41.7% | 41.7% | 50.0% | +3.6 | 1.65 | 1.98 | +18.8 | +11.1 |
| `confluence_gte_60` | 15 | S_STRANGER | 83.3% | 33.3% | 33.3% | 40.0% | +4.3 | 1.67 | 3.01 | +17.8 | +13.7 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -41.4 | 0.00 | 0.00 | +4.0 | +47.8 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 50.0% | 22.2% | 22.2% | 22.2% | -1.5 | 0.84 | 2.93 | +14.7 | +15.4 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 61.1% | 27.3% | 27.3% | 27.3% | +0.7 | 1.08 | 2.89 | +17.0 | +14.1 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 66.7% | 41.7% | 41.7% | 50.0% | +3.6 | 1.65 | 1.98 | +18.8 | +11.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 38.9% | 14.3% | 14.3% | 14.3% | -8.1 | 0.14 | 0.86 | +10.4 | +15.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 88.9% | 37.5% | 37.5% | 50.0% | +5.4 | 2.08 | 2.77 | +18.6 | +12.4 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 44.4% | +3.3 | 1.56 | 2.60 | +16.8 | +13.0 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 66.7% | +8.5 | 10.09 | 10.09 | +16.6 | +10.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 33.3% | +14.5 | 3.99 | 7.98 | +25.5 | +11.3 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=50.0% Avg=+4.9; validation N=5 Fav=20.0% Avg=+0.4; out_of_sample N=6 Fav=33.3% Avg=+4.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 53.3% | +3.3 | 3.42 | 3.42 | +11.5 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 100.0% | +10.2 | 999.00 | 999.00 | +17.9 | +3.8 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 66.7% | +6.4 | 14.64 | 14.64 | +12.7 | +3.8 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 53.3% | +3.3 | 3.42 | 3.42 | +11.5 | +4.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 53.3% | +3.3 | 3.42 | 3.42 | +11.5 | +4.8 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 53.3% | +3.3 | 3.42 | 3.42 | +11.5 | +4.8 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 33.3% | 40.0% | 40.0% | 40.0% | -0.8 | 0.62 | 0.62 | +11.3 | +5.3 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 26.7% | 25.0% | 25.0% | 50.0% | +0.6 | 1.16 | 2.33 | +13.6 | +8.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 53.3% | +3.3 | 3.42 | 3.42 | +11.5 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 53.3% | +3.3 | 3.42 | 3.42 | +11.5 | +4.8 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +6.0 | +2.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=37.5% Avg=+1.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 33.3% | +1.5 | 1.60 | 1.91 | +6.9 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 33.3% | +1.5 | 1.60 | 1.91 | +6.9 | +5.2 |
| `confluence_gte_70` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 0.0% | -0.7 | 0.77 | 3.09 | +4.9 | +6.3 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 37.5% | 37.5% | 25.0% | +1.6 | 1.51 | 2.52 | +7.9 | +6.2 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 0.0% | -2.0 | 0.51 | 2.55 | +4.8 | +7.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 33.3% | +1.5 | 1.60 | 1.91 | +6.9 | +5.2 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 41.7% | 20.0% | 40.0% | 0.0% | +0.1 | 1.04 | 1.56 | +4.6 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 0.0% | +1.4 | 1.52 | 3.05 | +6.1 | +6.2 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=0.0% Avg=-4.8; validation N=3 Fav=33.3% Avg=+0.3; out_of_sample N=4 Fav=50.0% Avg=+6.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 16.7% | -1.1 | 0.81 | 1.49 | +11.7 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 27.8% | 20.0% | 20.0% | 0.0% | -1.5 | 0.76 | 3.04 | +13.0 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 66.7% | 25.0% | 25.0% | 8.3% | -4.4 | 0.40 | 1.20 | +10.4 | +7.0 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 16.7% | -1.1 | 0.81 | 1.49 | +11.7 | +6.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 16.7% | -1.1 | 0.81 | 1.49 | +11.7 | +6.5 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 16.7% | -1.1 | 0.81 | 1.49 | +11.7 | +6.5 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 11.1% | 50.0% | 50.0% | 0.0% | +11.5 | 3.91 | 3.91 | +21.7 | +7.8 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 61.1% | 27.3% | 27.3% | 9.1% | +0.6 | 1.12 | 3.00 | +12.7 | +7.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 94.4% | 35.3% | 35.3% | 17.6% | -1.0 | 0.84 | 1.40 | +12.3 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 16.7% | -1.1 | 0.81 | 1.49 | +11.7 | +6.5 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +1.9 | +5.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +1.9 | +5.0 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=-2.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=50.0% Avg=+15.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 33.3% | -6.4 | 0.49 | 0.69 | +9.7 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 66.7% | 37.5% | 50.0% | 37.5% | +4.7 | 2.13 | 2.13 | +10.7 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 75.0% | 33.3% | 44.4% | 33.3% | +4.0 | 2.03 | 2.53 | +10.4 | +5.0 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 33.3% | -6.4 | 0.49 | 0.69 | +9.7 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 66.7% | 37.5% | 50.0% | 37.5% | +6.3 | 3.50 | 3.50 | +11.6 | +3.5 |
| `confluence_gte_70` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 66.7% | +14.1 | 25.94 | 12.97 | +17.8 | +3.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 25.0% | 37.5% | 25.0% | -8.8 | 0.33 | 0.54 | +7.1 | +4.5 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 20.0% | +3.3 | 1.81 | 7.25 | +11.4 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 33.3% | -6.4 | 0.49 | 0.69 | +9.7 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 33.3% | -6.4 | 0.49 | 0.69 | +9.7 | +4.1 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -9.5 | 0.00 | 0.00 | +0.0 | +9.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -9.5 | 0.00 | 0.00 | +0.0 | +9.5 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=57.1% Avg=+25.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +5.9 | 1.62 | 3.24 | +23.0 | +11.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +5.9 | 1.62 | 3.24 | +23.0 | +11.1 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +5.9 | 1.62 | 3.24 | +23.0 | +11.1 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +5.9 | 1.62 | 3.24 | +23.0 | +11.1 |
| `asian_range_gte_30` | 7 | S_STRANGER | 53.8% | 28.6% | 28.6% | 28.6% | +3.5 | 1.28 | 3.20 | +23.2 | +13.0 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +5.9 | 1.62 | 3.24 | +23.0 | +11.1 |
| `confluence_gte_70` | 7 | R_REPEATER | 53.8% | 57.1% | 57.1% | 57.1% | +25.5 | 9.05 | 6.79 | +37.5 | +8.7 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 33.3% | +6.8 | 1.69 | 2.95 | +23.8 | +11.4 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 69.2% | 44.4% | 44.4% | 44.4% | +16.0 | 3.54 | 3.54 | +28.7 | +10.9 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 53.8% | 28.6% | 28.6% | 28.6% | +3.5 | 1.28 | 3.20 | +23.2 | +13.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 46.2% | 33.3% | 33.3% | 16.7% | +5.0 | 1.36 | 2.72 | +24.7 | +13.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +5.9 | 1.62 | 3.24 | +23.0 | +11.1 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 38.5% | +5.9 | 1.62 | 3.24 | +23.0 | +11.1 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 50.0% | -10.3 | 0.00 | 0.00 | +7.2 | +12.2 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 30.8% | 50.0% | 50.0% | 75.0% | +24.7 | 5.80 | 2.90 | +37.2 | +8.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=+7.1; out_of_sample N=4 Fav=50.0% Avg=-2.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -3.4 | 0.71 | 1.61 | +16.3 | +17.8 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 69.2% | 44.4% | 44.4% | 11.1% | +3.0 | 1.32 | 1.66 | +18.3 | +16.7 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 76.9% | 40.0% | 40.0% | 10.0% | +2.6 | 1.30 | 1.95 | +18.7 | +15.3 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 8.3% | -3.2 | 0.74 | 1.49 | +17.0 | +18.2 |
| `asian_range_gte_30` | 10 | S_STRANGER | 76.9% | 20.0% | 20.0% | 0.0% | -9.3 | 0.18 | 0.74 | +9.9 | +18.3 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -3.4 | 0.71 | 1.61 | +16.3 | +17.8 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -3.4 | 0.71 | 1.61 | +16.3 | +17.8 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 9.1% | -2.2 | 0.82 | 1.43 | +19.1 | +18.9 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 8.3% | -2.5 | 0.79 | 1.57 | +17.7 | +18.3 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 53.8% | 28.6% | 28.6% | 0.0% | -8.9 | 0.25 | 0.63 | +7.5 | +20.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 38.5% | 40.0% | 40.0% | 0.0% | -8.5 | 0.33 | 0.49 | +10.1 | +24.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 8.3% | -3.2 | 0.74 | 1.49 | +17.0 | +18.2 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -3.4 | 0.71 | 1.61 | +16.3 | +17.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+0.8; validation N=4 Fav=75.0% Avg=+14.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 36 | S_STRANGER | 100.0% | 30.6% | 30.6% | 22.2% | -0.5 | 0.93 | 1.86 | +12.1 | +8.9 |
| `hunt_to_ar_ratio_le_2_0` | 33 | S_STRANGER | 91.7% | 27.3% | 27.3% | 24.2% | -1.5 | 0.78 | 1.83 | +11.6 | +9.2 |
| `hunt_to_ar_ratio_le_2_5` | 36 | S_STRANGER | 100.0% | 30.6% | 30.6% | 22.2% | -0.5 | 0.93 | 1.86 | +12.1 | +8.9 |
| `stop_hunt_le_90` | 36 | S_STRANGER | 100.0% | 30.6% | 30.6% | 22.2% | -0.5 | 0.93 | 1.86 | +12.1 | +8.9 |
| `asian_range_gte_30` | 32 | S_STRANGER | 88.9% | 28.1% | 28.1% | 25.0% | -0.8 | 0.90 | 1.99 | +12.5 | +9.4 |
| `confluence_gte_60` | 17 | S_STRANGER | 47.2% | 29.4% | 29.4% | 11.8% | -1.4 | 0.76 | 1.67 | +9.3 | +9.4 |
| `confluence_gte_70` | 6 | R_REPEATER | 16.7% | 66.7% | 66.7% | 16.7% | +9.7 | 4.79 | 2.40 | +16.0 | +5.8 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 27.8% | 30.0% | 30.0% | 20.0% | -0.3 | 0.96 | 2.24 | +12.6 | +9.0 |
| `tdi_rsi_gte_50` | 27 | S_STRANGER | 75.0% | 29.6% | 29.6% | 18.5% | +0.2 | 1.03 | 2.06 | +12.9 | +9.5 |
| `ratio_le_2_and_asian_gte_30` | 31 | S_STRANGER | 86.1% | 25.8% | 25.8% | 25.8% | -2.0 | 0.73 | 1.83 | +11.6 | +9.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 22.2% | 25.0% | 25.0% | 25.0% | +0.0 | 1.00 | 3.01 | +14.2 | +10.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 36 | S_STRANGER | 100.0% | 30.6% | 30.6% | 22.2% | -0.5 | 0.93 | 1.86 | +12.1 | +8.9 |
| `feature_stale_hod_exhaustion_reject` | 36 | S_STRANGER | 100.0% | 30.6% | 30.6% | 22.2% | -0.5 | 0.93 | 1.86 | +12.1 | +8.9 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 2.8% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +5.7 | +3.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.8% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +5.7 | +3.2 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+1.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | S_STRANGER | 100.0% | 30.3% | 33.3% | 39.4% | +1.5 | 1.41 | 2.31 | +11.5 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 33.3% | 27.3% | 36.4% | 54.5% | +5.0 | 3.27 | 3.27 | +15.7 | +5.1 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 39.4% | 38.5% | 46.2% | 53.8% | +5.2 | 3.82 | 2.55 | +15.0 | +4.7 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 93.9% | 25.8% | 29.0% | 35.5% | +0.3 | 1.07 | 2.15 | +10.8 | +5.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 18.2% | 16.7% | 16.7% | 16.7% | +3.9 | 2.09 | 10.47 | +18.6 | +6.9 |
| `confluence_gte_70` | 3 | S_STRANGER | 9.1% | 33.3% | 33.3% | 33.3% | +10.0 | 3.05 | 6.11 | +26.7 | +8.2 |
| `tdi_rsi_gt_signal` | 24 | S_STRANGER | 72.7% | 29.2% | 29.2% | 29.2% | +0.8 | 1.18 | 2.70 | +11.7 | +5.4 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 48.5% | 31.2% | 31.2% | 25.0% | +3.5 | 2.23 | 4.91 | +13.2 | +5.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 87.9% | 24.1% | 27.6% | 34.5% | +0.2 | 1.05 | 2.36 | +11.0 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 97.0% | 31.2% | 34.4% | 40.6% | +1.7 | 1.46 | 2.26 | +11.8 | +5.0 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 15.2% | 40.0% | 40.0% | 40.0% | +1.4 | 2.15 | 2.15 | +6.8 | +3.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 9.1% | 33.3% | 33.3% | 0.0% | -1.0 | 0.52 | 1.03 | +3.4 | +4.5 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=50.0% Avg=-0.5; out_of_sample N=5 Fav=40.0% Avg=+8.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 15.0% | +0.1 | 1.03 | 2.23 | +8.5 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 25.0% | 0.0% | 0.0% | 20.0% | -11.4 | 0.00 | 0.00 | +3.9 | +11.2 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 35.0% | 28.6% | 28.6% | 14.3% | -6.6 | 0.19 | 0.39 | +7.9 | +9.2 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 15.0% | +0.1 | 1.03 | 2.23 | +8.5 | +7.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 15.0% | +0.1 | 1.03 | 2.23 | +8.5 | +7.0 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 15.0% | +0.1 | 1.03 | 2.23 | +8.5 | +7.0 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 85.0% | 17.6% | 17.6% | 11.8% | -2.7 | 0.49 | 2.14 | +6.5 | +8.1 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 45.0% | 44.4% | 44.4% | 11.1% | +4.7 | 3.03 | 3.03 | +13.4 | +7.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 95.0% | 26.3% | 26.3% | 10.5% | -0.6 | 0.87 | 2.25 | +8.1 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 15.0% | +0.1 | 1.03 | 2.23 | +8.5 | +7.0 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 15.0% | 33.3% | 33.3% | 33.3% | +2.8 | 2.35 | 4.70 | +6.8 | +4.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=-2.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 0.0% | -6.8 | 0.25 | 0.59 | +23.9 | +12.8 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 0.0% | -12.9 | 0.00 | 0.00 | +19.1 | +15.5 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 0.0% | -6.8 | 0.25 | 0.59 | +23.9 | +12.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 0.0% | -6.8 | 0.25 | 0.59 | +23.9 | +12.8 |
| `asian_range_gte_30` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +16.0 | +15.8 |
| `confluence_gte_60` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +12.6 | +16.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -12.3 | 0.00 | 0.00 | +29.8 | +13.2 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 0.0% | -2.3 | 0.55 | 0.92 | +26.0 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +16.0 | +15.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -12.3 | 0.00 | 0.00 | +29.8 | +13.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 0.0% | -10.3 | 0.09 | 0.60 | +21.7 | +13.7 |
| `feature_stale_hod_exhaustion_reject` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -9.2 | 0.12 | 0.62 | +20.0 | +13.3 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +12.6 | +16.4 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 50.0% | 40.0% | 40.0% | 0.0% | -2.5 | 0.54 | 0.81 | +25.8 | +10.7 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=100.0% Avg=+9.7; validation N=2 Fav=0.0% Avg=-28.0; out_of_sample N=2 Fav=50.0% Avg=-33.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -18.2 | 0.19 | 0.37 | +8.2 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 0.0% | -19.1 | 0.14 | 0.29 | +6.6 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 0.0% | -19.1 | 0.14 | 0.29 | +6.6 | +4.7 |
| `stop_hunt_le_90` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 12.5% | -14.4 | 0.14 | 0.36 | +6.1 | +3.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -18.2 | 0.19 | 0.37 | +8.2 | +3.3 |
| `confluence_gte_70` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 16.7% | -17.3 | 0.29 | 0.29 | +10.6 | +1.9 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 12.5% | -11.6 | 0.31 | 0.51 | +9.2 | +3.8 |
| `tdi_rsi_gte_50` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 0.0% | +2.7 | 2.20 | 2.20 | +9.1 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 12.5% | -14.4 | 0.14 | 0.36 | +6.1 | +3.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -18.2 | 0.19 | 0.37 | +8.2 | +3.3 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +10.7 | 999.00 | 999.00 | +11.8 | +2.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 0.0% | +10.7 | 999.00 | 999.00 | +11.8 | +2.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+1.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 57 | S_STRANGER | 100.0% | 29.8% | 29.8% | 35.1% | -0.9 | 0.84 | 1.58 | +14.0 | +8.3 |
| `hunt_to_ar_ratio_le_2_0` | 49 | S_STRANGER | 86.0% | 28.6% | 28.6% | 38.8% | -0.7 | 0.86 | 1.67 | +14.2 | +8.0 |
| `hunt_to_ar_ratio_le_2_5` | 56 | S_STRANGER | 98.2% | 28.6% | 28.6% | 35.7% | -1.0 | 0.82 | 1.63 | +13.8 | +8.3 |
| `stop_hunt_le_90` | 56 | S_STRANGER | 98.2% | 28.6% | 28.6% | 35.7% | -1.0 | 0.82 | 1.63 | +13.8 | +8.3 |
| `asian_range_gte_30` | 46 | S_STRANGER | 80.7% | 26.1% | 26.1% | 32.6% | -1.7 | 0.66 | 1.50 | +13.2 | +8.8 |
| `confluence_gte_60` | 45 | S_STRANGER | 78.9% | 28.9% | 28.9% | 37.8% | -0.2 | 0.96 | 1.77 | +15.0 | +8.2 |
| `confluence_gte_70` | 14 | S_STRANGER | 24.6% | 21.4% | 21.4% | 28.6% | -0.5 | 0.86 | 2.30 | +18.0 | +8.2 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 21.1% | 16.7% | 16.7% | 16.7% | -4.5 | 0.51 | 2.28 | +13.7 | +9.9 |
| `tdi_rsi_gte_50` | 28 | S_STRANGER | 49.1% | 28.6% | 28.6% | 21.4% | -2.7 | 0.57 | 1.28 | +15.7 | +10.2 |
| `ratio_le_2_and_asian_gte_30` | 38 | S_STRANGER | 66.7% | 23.7% | 23.7% | 36.8% | -1.6 | 0.64 | 1.56 | +13.2 | +8.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 10.5% | 16.7% | 16.7% | 16.7% | -1.8 | 0.69 | 2.76 | +14.4 | +11.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 56 | S_STRANGER | 98.2% | 28.6% | 28.6% | 35.7% | -1.0 | 0.82 | 1.63 | +13.8 | +8.3 |
| `feature_stale_hod_exhaustion_reject` | 55 | S_STRANGER | 96.5% | 30.9% | 30.9% | 36.4% | -0.6 | 0.88 | 1.56 | +14.3 | +8.3 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 8.8% | 20.0% | 20.0% | 20.0% | +1.6 | 1.34 | 5.34 | +11.5 | +5.3 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -6.7 | 0.00 | 0.00 | +5.9 | +7.5 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=80.0% Avg=+11.2; validation N=2 Fav=0.0% Avg=-6.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 29.6% | 33.3% | 40.7% | -0.3 | 0.94 | 1.56 | +10.1 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 88.9% | 29.2% | 33.3% | 37.5% | -1.3 | 0.75 | 1.32 | +8.8 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 96.3% | 26.9% | 30.8% | 38.5% | -1.3 | 0.74 | 1.38 | +8.6 | +6.2 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 96.3% | 26.9% | 30.8% | 38.5% | -1.3 | 0.74 | 1.38 | +8.6 | +6.2 |
| `asian_range_gte_30` | 22 | S_STRANGER | 81.5% | 27.3% | 31.8% | 40.9% | -1.1 | 0.78 | 1.34 | +8.0 | +6.0 |
| `confluence_gte_60` | 7 | R_REPEATER | 25.9% | 57.1% | 57.1% | 42.9% | +6.0 | 3.01 | 2.26 | +13.6 | +5.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 48.1% | 38.5% | 38.5% | 30.8% | -0.7 | 0.90 | 1.44 | +11.4 | +6.9 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 63.0% | 35.3% | 35.3% | 41.2% | +1.0 | 1.28 | 1.91 | +11.1 | +6.7 |
| `ratio_le_2_and_asian_gte_30` | 20 | S_STRANGER | 74.1% | 30.0% | 35.0% | 40.0% | -1.0 | 0.81 | 1.27 | +8.1 | +6.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 37.0% | 40.0% | 40.0% | 30.0% | -2.0 | 0.72 | 1.08 | +8.0 | +6.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 92.6% | 28.0% | 32.0% | 40.0% | -1.2 | 0.75 | 1.32 | +8.7 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 29.6% | 33.3% | 40.7% | -0.3 | 0.94 | 1.56 | +10.1 | +6.2 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 33.3% | 22.2% | 33.3% | 44.4% | -0.0 | 0.99 | 1.65 | +8.2 | +5.9 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 22.2% | 16.7% | 16.7% | 33.3% | -2.6 | 0.49 | 1.96 | +6.2 | +7.0 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=30.0% Avg=+4.4; validation N=8 Fav=50.0% Avg=+4.1; out_of_sample N=9 Fav=11.1% Avg=-3.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 29.0% | 29.0% | 35.5% | -0.8 | 0.85 | 1.69 | +10.0 | +6.0 |
| `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 80.6% | 28.0% | 28.0% | 40.0% | +2.1 | 1.88 | 3.76 | +10.1 | +6.0 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 100.0% | 29.0% | 29.0% | 35.5% | -0.8 | 0.85 | 1.69 | +10.0 | +6.0 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 29.0% | 29.0% | 35.5% | -0.8 | 0.85 | 1.69 | +10.0 | +6.0 |
| `asian_range_gte_30` | 23 | S_STRANGER | 74.2% | 26.1% | 26.1% | 34.8% | -3.1 | 0.51 | 1.20 | +8.7 | +6.5 |
| `confluence_gte_60` | 27 | S_STRANGER | 87.1% | 29.6% | 29.6% | 37.0% | +1.7 | 1.60 | 3.01 | +10.5 | +6.3 |
| `confluence_gte_70` | 4 | S_STRANGER | 12.9% | 25.0% | 25.0% | 25.0% | -1.2 | 0.66 | 1.99 | +6.7 | +9.6 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 61.3% | 26.3% | 26.3% | 21.1% | +1.5 | 1.43 | 3.72 | +11.0 | +6.6 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 64.5% | 20.0% | 20.0% | 20.0% | -0.8 | 0.79 | 2.76 | +9.2 | +6.8 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 61.3% | 21.1% | 21.1% | 36.8% | -0.5 | 0.83 | 2.48 | +8.0 | +7.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 25.8% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +6.4 | +9.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 29.0% | 29.0% | 35.5% | -0.8 | 0.85 | 1.69 | +10.0 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 29.0% | 29.0% | 35.5% | -0.8 | 0.85 | 1.69 | +10.0 | +6.0 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 12.9% | 50.0% | 50.0% | 75.0% | +13.0 | 22.60 | 11.30 | +17.8 | +3.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.2% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +11.0 | +0.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=14 Fav=28.6% Avg=+0.6; validation N=10 Fav=40.0% Avg=+6.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 38 | S_STRANGER | 100.0% | 28.9% | 31.6% | 36.8% | +2.1 | 1.78 | 3.12 | +8.5 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 34 | S_STRANGER | 89.5% | 32.4% | 35.3% | 38.2% | +2.6 | 1.94 | 2.91 | +9.2 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 38 | S_STRANGER | 100.0% | 28.9% | 31.6% | 36.8% | +2.1 | 1.78 | 3.12 | +8.5 | +5.9 |
| `stop_hunt_le_90` | 38 | S_STRANGER | 100.0% | 28.9% | 31.6% | 36.8% | +2.1 | 1.78 | 3.12 | +8.5 | +5.9 |
| `asian_range_gte_30` | 27 | S_STRANGER | 71.1% | 29.6% | 29.6% | 40.7% | +2.4 | 1.99 | 3.74 | +9.4 | +5.9 |
| `confluence_gte_60` | 14 | S_STRANGER | 36.8% | 28.6% | 28.6% | 28.6% | +2.2 | 1.72 | 4.30 | +8.6 | +6.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 60.5% | 30.4% | 30.4% | 26.1% | +1.7 | 1.51 | 3.46 | +8.7 | +6.4 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 63.2% | 25.0% | 25.0% | 29.2% | +0.7 | 1.21 | 3.22 | +7.7 | +6.5 |
| `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 63.2% | 33.3% | 33.3% | 41.7% | +2.9 | 2.11 | 3.44 | +10.1 | +6.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 39.5% | 33.3% | 33.3% | 26.7% | +1.8 | 1.62 | 3.25 | +9.5 | +6.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 37 | S_STRANGER | 97.4% | 29.7% | 32.4% | 35.1% | +2.2 | 1.78 | 3.12 | +8.6 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 100.0% | 28.9% | 31.6% | 36.8% | +2.1 | 1.78 | 3.12 | +8.5 | +5.9 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 34.2% | 23.1% | 30.8% | 46.2% | +0.0 | 1.00 | 1.25 | +7.0 | +5.1 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 26.3% | 30.0% | 30.0% | 40.0% | -0.5 | 0.84 | 1.41 | +7.0 | +5.6 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=+8.6; validation N=8 Fav=37.5% Avg=+4.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 14.3% | +3.5 | 1.72 | 3.10 | +17.6 | +10.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 57.1% | 25.0% | 37.5% | 12.5% | -1.1 | 0.82 | 1.37 | +14.7 | +12.7 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 64.3% | 22.2% | 33.3% | 11.1% | -1.6 | 0.74 | 1.48 | +13.3 | +11.9 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 78.6% | 18.2% | 27.3% | 9.1% | -2.4 | 0.61 | 1.63 | +13.3 | +12.4 |
| `asian_range_gte_30` | 11 | S_STRANGER | 78.6% | 36.4% | 45.5% | 18.2% | +5.7 | 2.19 | 2.62 | +20.8 | +10.4 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 14.3% | +3.5 | 1.72 | 3.10 | +17.6 | +10.0 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 14.3% | +3.5 | 1.72 | 3.10 | +17.6 | +10.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 64.3% | 33.3% | 33.3% | 11.1% | +3.6 | 1.57 | 3.14 | +20.1 | +11.4 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 78.6% | 27.3% | 27.3% | 9.1% | +2.6 | 1.46 | 3.90 | +19.3 | +12.1 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 57.1% | 25.0% | 37.5% | 12.5% | -1.1 | 0.82 | 1.37 | +14.7 | +12.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 0.0% | -6.1 | 0.33 | 1.32 | +12.5 | +14.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 78.6% | 18.2% | 27.3% | 9.1% | -2.4 | 0.61 | 1.63 | +13.3 | +12.4 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 14.3% | +3.5 | 1.72 | 3.10 | +17.6 | +10.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=12.5% Avg=-3.8; validation N=8 Fav=50.0% Avg=+11.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | +3.2 | 1.91 | 4.58 | +14.1 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 88.9% | 31.2% | 31.2% | 12.5% | +3.8 | 2.07 | 4.14 | +14.1 | +8.5 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 88.9% | 31.2% | 31.2% | 12.5% | +3.8 | 2.07 | 4.14 | +14.1 | +8.5 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 94.4% | 29.4% | 29.4% | 11.8% | +3.4 | 1.93 | 4.24 | +14.5 | +8.3 |
| `asian_range_gte_30` | 10 | S_STRANGER | 55.6% | 20.0% | 20.0% | 20.0% | +2.4 | 1.69 | 5.93 | +13.0 | +8.1 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | +3.2 | 1.91 | 4.58 | +14.1 | +8.2 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | +3.2 | 1.91 | 4.58 | +14.1 | +8.2 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +18.5 | +11.6 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 88.9% | 31.2% | 31.2% | 12.5% | +4.0 | 2.18 | 4.35 | +15.3 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 50.0% | 22.2% | 22.2% | 22.2% | +2.7 | 1.72 | 5.17 | +13.5 | +8.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -2.3 | 0.00 | 0.00 | +25.0 | +17.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 94.4% | 29.4% | 29.4% | 11.8% | +3.4 | 1.93 | 4.24 | +14.5 | +8.3 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | +3.2 | 1.91 | 4.58 | +14.1 | +8.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=33.3% Avg=+6.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | +3.1 | 1.44 | 3.85 | +20.4 | +12.3 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 33.3% | +6.3 | 2.05 | 4.11 | +24.9 | +11.4 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | +3.1 | 1.44 | 3.85 | +20.4 | +12.3 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | +3.1 | 1.44 | 3.85 | +20.4 | +12.3 |
| `asian_range_gte_30` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 33.3% | +6.3 | 2.05 | 4.11 | +24.9 | +11.4 |
| `confluence_gte_60` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 28.6% | +0.5 | 1.05 | 2.62 | +19.9 | +17.1 |
| `confluence_gte_70` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -11.4 | 0.00 | 0.00 | +0.1 | +16.2 |
| `tdi_rsi_gt_signal` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 22.2% | -1.3 | 0.85 | 2.96 | +19.3 | +14.5 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 33.3% | +6.3 | 2.05 | 4.11 | +24.9 | +11.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 33.3% | +6.3 | 2.05 | 4.11 | +24.9 | +11.4 |
| `feature_stale_hod_exhaustion_reject` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 33.3% | +6.3 | 2.05 | 4.11 | +24.9 | +11.4 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 50.0% | +22.9 | 58.13 | 58.13 | +25.1 | +2.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | +1.6 | 1.21 | 2.43 | +15.5 | +19.2 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=33.3% Avg=-3.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 27.3% | -4.1 | 0.50 | 0.87 | +11.1 | +10.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 27.3% | -4.1 | 0.50 | 0.87 | +11.1 | +10.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 27.3% | -4.1 | 0.50 | 0.87 | +11.1 | +10.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 27.3% | -4.1 | 0.50 | 0.87 | +11.1 | +10.0 |
| `asian_range_gte_30` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 33.3% | -3.7 | 0.56 | 1.12 | +13.0 | +9.7 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 27.3% | -4.1 | 0.50 | 0.87 | +11.1 | +10.0 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 27.3% | -4.1 | 0.50 | 0.87 | +11.1 | +10.0 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -9.4 | 0.00 | 0.00 | +5.6 | +15.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 28.6% | -5.9 | 0.46 | 1.16 | +12.1 | +12.9 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 33.3% | -3.7 | 0.56 | 1.12 | +13.0 | +9.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -9.4 | 0.00 | 0.00 | +5.6 | +15.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 27.3% | -4.1 | 0.50 | 0.87 | +11.1 | +10.0 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 90.9% | 30.0% | 40.0% | 30.0% | -2.4 | 0.65 | 0.98 | +11.9 | +8.9 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | +1.6 | 1.36 | 2.71 | +12.0 | +5.3 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 25.0% | -5.9 | 0.43 | 1.30 | +9.7 | +12.3 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+10.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 33.3% | +3.8 | 1.74 | 3.13 | +15.3 | +12.5 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 86.7% | 30.8% | 38.5% | 38.5% | +4.9 | 1.92 | 2.69 | +17.5 | +11.4 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 86.7% | 30.8% | 38.5% | 38.5% | +4.9 | 1.92 | 2.69 | +17.5 | +11.4 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 86.7% | 30.8% | 38.5% | 38.5% | +4.9 | 1.92 | 2.69 | +17.5 | +11.4 |
| `asian_range_gte_30` | 11 | S_STRANGER | 73.3% | 27.3% | 27.3% | 27.3% | +3.4 | 1.52 | 4.04 | +14.9 | +11.8 |
| `confluence_gte_60` | 12 | S_STRANGER | 80.0% | 25.0% | 33.3% | 25.0% | +3.4 | 1.56 | 3.11 | +14.0 | +12.4 |
| `confluence_gte_70` | 5 | S_STRANGER | 33.3% | 20.0% | 20.0% | 20.0% | +3.3 | 1.38 | 5.51 | +19.1 | +14.4 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +7.9 | +15.9 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 66.7% | 40.0% | 40.0% | 40.0% | +6.3 | 1.94 | 2.90 | +18.6 | +12.9 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 66.7% | 30.0% | 30.0% | 30.0% | +4.1 | 1.60 | 3.73 | +16.2 | +11.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +7.9 | +15.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 86.7% | 30.8% | 38.5% | 38.5% | +4.9 | 1.92 | 2.69 | +17.5 | +11.4 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 33.3% | +3.8 | 1.74 | 3.13 | +15.3 | +12.5 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 33.3% | 40.0% | 40.0% | 60.0% | +10.3 | 3.07 | 3.07 | +23.9 | +9.9 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 26.7% | 50.0% | 50.0% | 50.0% | +12.9 | 3.07 | 3.07 | +23.8 | +9.8 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=42.9% Avg=+2.3; validation N=2 Fav=100.0% Avg=+15.5; out_of_sample N=3 Fav=0.0% Avg=-2.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 26.7% | 30.0% | 33.3% | +2.2 | 1.98 | 3.53 | +9.2 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 29 | S_STRANGER | 96.7% | 27.6% | 31.0% | 31.0% | +2.2 | 1.98 | 3.53 | +9.3 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 96.7% | 27.6% | 31.0% | 31.0% | +2.2 | 1.98 | 3.53 | +9.3 | +4.4 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 96.7% | 27.6% | 31.0% | 31.0% | +2.2 | 1.98 | 3.53 | +9.3 | +4.4 |
| `asian_range_gte_30` | 27 | S_STRANGER | 90.0% | 29.6% | 33.3% | 37.0% | +2.8 | 2.33 | 3.36 | +9.5 | +4.1 |
| `confluence_gte_60` | 30 | S_STRANGER | 100.0% | 26.7% | 30.0% | 33.3% | +2.2 | 1.98 | 3.53 | +9.2 | +4.3 |
| `confluence_gte_70` | 30 | S_STRANGER | 100.0% | 26.7% | 30.0% | 33.3% | +2.2 | 1.98 | 3.53 | +9.2 | +4.3 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 46.7% | 35.7% | 35.7% | 14.3% | +2.3 | 1.84 | 3.32 | +10.6 | +5.0 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 60.0% | 38.9% | 38.9% | 22.2% | +4.1 | 2.71 | 4.26 | +11.3 | +4.5 |
| `ratio_le_2_and_asian_gte_30` | 26 | S_STRANGER | 86.7% | 30.8% | 34.6% | 34.6% | +2.9 | 2.33 | 3.36 | +9.7 | +4.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 40.0% | 41.7% | 41.7% | 16.7% | +3.4 | 2.41 | 3.38 | +11.6 | +4.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 96.7% | 27.6% | 31.0% | 31.0% | +2.2 | 1.98 | 3.53 | +9.3 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 26.7% | 30.0% | 33.3% | +2.2 | 1.98 | 3.53 | +9.2 | +4.3 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 33.3% | 20.0% | 20.0% | 30.0% | -0.0 | 0.99 | 2.98 | +6.4 | +4.4 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 13.3% | 50.0% | 50.0% | 25.0% | +5.4 | 6.94 | 6.94 | +9.4 | +3.2 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=22.2% Avg=+0.1; validation N=6 Fav=33.3% Avg=-0.4; out_of_sample N=3 Fav=66.7% Avg=+19.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 21.7% | +1.8 | 1.60 | 3.44 | +9.3 | +6.8 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 91.3% | 28.6% | 33.3% | 23.8% | +2.7 | 2.14 | 3.98 | +10.0 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 95.7% | 27.3% | 31.8% | 22.7% | +2.4 | 1.96 | 3.92 | +9.6 | +6.4 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 95.7% | 27.3% | 31.8% | 22.7% | +2.4 | 1.96 | 3.92 | +9.6 | +6.4 |
| `asian_range_gte_30` | 17 | S_STRANGER | 73.9% | 23.5% | 29.4% | 29.4% | +2.6 | 1.96 | 4.31 | +10.2 | +7.5 |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 21.7% | +1.8 | 1.60 | 3.44 | +9.3 | +6.8 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 21.7% | +1.8 | 1.60 | 3.44 | +9.3 | +6.8 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 8.7% | 0.0% | 0.0% | 0.0% | -0.7 | 0.00 | 0.00 | +13.6 | +8.7 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 78.3% | 33.3% | 33.3% | 22.2% | +3.1 | 2.17 | 4.34 | +10.6 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 69.6% | 25.0% | 31.2% | 31.2% | +3.6 | 2.65 | 5.30 | +10.7 | +7.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 8.7% | 0.0% | 0.0% | 0.0% | -0.7 | 0.00 | 0.00 | +13.6 | +8.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 95.7% | 27.3% | 31.8% | 22.7% | +2.4 | 1.96 | 3.92 | +9.6 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 21.7% | +1.8 | 1.60 | 3.44 | +9.3 | +6.8 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 17.4% | 25.0% | 25.0% | 25.0% | +3.1 | 2.81 | 8.43 | +12.0 | +4.8 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 17.4% | 25.0% | 25.0% | 25.0% | +3.1 | 2.81 | 8.43 | +12.0 | +4.8 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=2 Fav=50.0% Avg=+1.4; out_of_sample N=7 Fav=28.6% Avg=+6.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 25.8% | 29.0% | 12.9% | +0.6 | 1.14 | 2.65 | +9.5 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 29.0% | 33.3% | 44.4% | 22.2% | +5.3 | 2.58 | 3.22 | +13.3 | +5.3 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 45.2% | 28.6% | 35.7% | 14.3% | +2.4 | 1.57 | 2.83 | +10.6 | +6.7 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 25.8% | 29.0% | 12.9% | +0.6 | 1.14 | 2.65 | +9.5 | +6.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 31 | S_STRANGER | 100.0% | 25.8% | 29.0% | 12.9% | +0.6 | 1.14 | 2.65 | +9.5 | +6.2 |
| `confluence_gte_70` | 31 | S_STRANGER | 100.0% | 25.8% | 29.0% | 12.9% | +0.6 | 1.14 | 2.65 | +9.5 | +6.2 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 54.8% | 23.5% | 29.4% | 5.9% | -1.4 | 0.71 | 1.70 | +8.7 | +6.7 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 61.3% | 31.6% | 31.6% | 10.5% | +1.2 | 1.24 | 2.69 | +11.1 | +7.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 96.8% | 26.7% | 30.0% | 13.3% | +0.6 | 1.15 | 2.55 | +9.7 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 25.8% | 29.0% | 12.9% | +0.6 | 1.14 | 2.65 | +9.5 | +6.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 3.2% | 0.0% | 0.0% | 0.0% | -1.0 | 0.00 | 0.00 | +3.4 | +2.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.2% | 0.0% | 0.0% | 0.0% | -1.0 | 0.00 | 0.00 | +3.4 | +2.4 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=25.0% Avg=+0.7; validation N=14 Fav=28.6% Avg=+6.5; out_of_sample N=17 Fav=23.5% Avg=+5.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 39 | S_STRANGER | 100.0% | 25.6% | 28.2% | 7.7% | +4.0 | 1.70 | 4.32 | +16.2 | +9.7 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 76.9% | 20.0% | 23.3% | 6.7% | +2.0 | 1.39 | 4.56 | +12.9 | +8.9 |
| `hunt_to_ar_ratio_le_2_5` | 33 | S_STRANGER | 84.6% | 24.2% | 27.3% | 9.1% | +5.2 | 2.02 | 5.39 | +16.5 | +8.9 |
| `stop_hunt_le_90` | 35 | S_STRANGER | 89.7% | 25.7% | 28.6% | 8.6% | +5.4 | 2.07 | 5.18 | +16.7 | +9.2 |
| `asian_range_gte_30` | 33 | S_STRANGER | 84.6% | 18.2% | 21.2% | 6.1% | -0.7 | 0.89 | 3.30 | +12.0 | +10.2 |
| `confluence_gte_60` | 39 | S_STRANGER | 100.0% | 25.6% | 28.2% | 7.7% | +4.0 | 1.70 | 4.32 | +16.2 | +9.7 |
| `confluence_gte_70` | 39 | S_STRANGER | 100.0% | 25.6% | 28.2% | 7.7% | +4.0 | 1.70 | 4.32 | +16.2 | +9.7 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 23.1% | 0.0% | 11.1% | 0.0% | -3.8 | 0.21 | 1.70 | +8.4 | +7.9 |
| `tdi_rsi_gte_50` | 36 | S_STRANGER | 92.3% | 25.0% | 25.0% | 5.6% | +3.6 | 1.63 | 4.89 | +16.1 | +10.1 |
| `ratio_le_2_and_asian_gte_30` | 27 | S_STRANGER | 69.2% | 14.8% | 18.5% | 7.4% | -0.1 | 0.98 | 4.30 | +11.4 | +9.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 20.5% | 0.0% | 12.5% | 0.0% | -4.1 | 0.22 | 1.53 | +8.1 | +8.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 35 | S_STRANGER | 89.7% | 25.7% | 28.6% | 8.6% | +5.4 | 2.07 | 5.18 | +16.7 | +9.2 |
| `feature_stale_hod_exhaustion_reject` | 39 | S_STRANGER | 100.0% | 25.6% | 28.2% | 7.7% | +4.0 | 1.70 | 4.32 | +16.2 | +9.7 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 2.6% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +2.4 | +5.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.6% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +2.4 | +5.6 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-1.5; validation N=6 Fav=33.3% Avg=+7.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +2.9 | 1.78 | 4.74 | +13.4 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +2.9 | 1.78 | 4.74 | +13.4 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +2.9 | 1.78 | 4.74 | +13.4 | +7.1 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +2.9 | 1.78 | 4.74 | +13.4 | +7.1 |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +2.9 | 1.78 | 4.74 | +13.4 | +7.1 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +2.9 | 1.78 | 4.74 | +13.4 | +7.1 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +2.9 | 1.78 | 4.74 | +13.4 | +7.1 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 42.9% | +5.3 | 2.29 | 4.57 | +17.3 | +7.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 42.9% | +5.9 | 2.67 | 5.35 | +16.8 | +8.7 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +2.9 | 1.78 | 4.74 | +13.4 | +7.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 42.9% | +5.3 | 2.29 | 4.57 | +17.3 | +7.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +2.9 | 1.78 | 4.74 | +13.4 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 33.3% | +2.9 | 1.78 | 4.74 | +13.4 | +7.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+16.0; validation N=5 Fav=20.0% Avg=+2.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 18.8% | +1.8 | 1.81 | 4.53 | +11.0 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 25.0% | 25.0% | 25.0% | 50.0% | +2.6 | 2.81 | 5.61 | +11.0 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 37.5% | 33.3% | 33.3% | 33.3% | +4.4 | 2.33 | 3.50 | +15.5 | +6.2 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 93.8% | 26.7% | 26.7% | 13.3% | +1.9 | 1.81 | 4.53 | +10.3 | +5.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 18.8% | +1.8 | 1.81 | 4.53 | +11.0 | +5.3 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 18.8% | +1.8 | 1.81 | 4.53 | +11.0 | +5.3 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 62.5% | 20.0% | 20.0% | 20.0% | +0.5 | 1.24 | 4.34 | +8.5 | +5.3 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 75.0% | 25.0% | 25.0% | 8.3% | +2.4 | 2.66 | 7.09 | +10.5 | +4.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 93.8% | 26.7% | 26.7% | 13.3% | +1.9 | 1.81 | 4.53 | +10.3 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 18.8% | +1.8 | 1.81 | 4.53 | +11.0 | +5.3 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 6.2% | 100.0% | 100.0% | 100.0% | +16.0 | 999.00 | 999.00 | +18.0 | +2.1 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+3.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | +1.3 | 1.47 | 3.92 | +7.7 | +6.0 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | +1.3 | 1.47 | 3.92 | +7.7 | +6.0 |
| `confluence_gte_70` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 16.7% | +3.4 | 3.03 | 6.06 | +8.9 | +4.5 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 83.3% | 30.0% | 30.0% | 30.0% | +2.8 | 2.27 | 4.54 | +8.8 | +5.8 |
| `tdi_rsi_gte_50` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | +7.7 | 9.61 | 9.61 | +13.6 | +5.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -2.7 | 0.00 | 0.00 | +3.4 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 25.0% | +1.3 | 1.47 | 3.92 | +7.7 | +6.0 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 83.3% | 30.0% | 30.0% | 30.0% | +2.6 | 2.08 | 4.16 | +8.8 | +5.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | +7.7 | 9.61 | 9.61 | +13.6 | +5.7 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=+6.4; out_of_sample N=5 Fav=20.0% Avg=+0.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 15.0% | -1.5 | 0.71 | 2.00 | +10.8 | +8.0 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 15.0% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +6.0 | +10.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 50.0% | 30.0% | 30.0% | 10.0% | +3.2 | 2.70 | 6.30 | +12.2 | +8.2 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 15.0% | -1.5 | 0.71 | 2.00 | +10.8 | +8.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 15.0% | -1.5 | 0.71 | 2.00 | +10.8 | +8.0 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 15.0% | -1.5 | 0.71 | 2.00 | +10.8 | +8.0 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 15.0% | 33.3% | 33.3% | 0.0% | -19.4 | 0.05 | 0.09 | +10.5 | +5.5 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 85.0% | 23.5% | 23.5% | 5.9% | +0.6 | 1.20 | 3.89 | +11.2 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 15.0% | -1.5 | 0.71 | 2.00 | +10.8 | +8.0 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 15.0% | -1.5 | 0.71 | 2.00 | +10.8 | +8.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=+0.0; validation N=7 Fav=28.6% Avg=-3.9; out_of_sample N=3 Fav=33.3% Avg=-1.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -2.8 | 0.38 | 1.02 | +9.5 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 14.3% | -6.9 | 0.06 | 0.31 | +5.6 | +9.9 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 12.5% | -6.2 | 0.06 | 0.36 | +5.2 | +9.2 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 18.2% | -2.9 | 0.39 | 0.91 | +9.7 | +7.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -2.8 | 0.38 | 1.02 | +9.5 | +7.4 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -2.8 | 0.38 | 1.02 | +9.5 | +7.4 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -17.9 | 0.00 | 0.00 | +6.0 | +19.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -5.6 | 0.12 | 0.59 | +7.9 | +10.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 18.2% | -2.9 | 0.39 | 0.91 | +9.7 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -2.8 | 0.38 | 1.02 | +9.5 | +7.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=36.4% Avg=-0.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 25.0% | 30.0% | 25.0% | -3.7 | 0.55 | 1.10 | +12.4 | +9.1 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 30.0% | 16.7% | 16.7% | 16.7% | -10.5 | 0.10 | 0.52 | +11.6 | +11.3 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 60.0% | 16.7% | 25.0% | 25.0% | -5.9 | 0.31 | 0.84 | +10.2 | +9.6 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 95.0% | 26.3% | 31.6% | 26.3% | -2.3 | 0.68 | 1.24 | +12.6 | +9.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 2 | R_REPEATER | 10.0% | 50.0% | 50.0% | 50.0% | +2.1 | 1.17 | 1.17 | +17.9 | +16.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 55.0% | 36.4% | 45.5% | 27.3% | -0.0 | 1.00 | 1.00 | +13.1 | +8.7 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 45.0% | 22.2% | 22.2% | 11.1% | -7.9 | 0.28 | 0.84 | +11.3 | +15.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 65.0% | 30.8% | 30.8% | 30.8% | -4.1 | 0.55 | 1.10 | +13.6 | +10.6 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 90.0% | 27.8% | 33.3% | 27.8% | -2.2 | 0.69 | 1.15 | +12.9 | +8.0 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 30.0% | 0.0% | 16.7% | 16.7% | -2.8 | 0.41 | 1.65 | +6.7 | +5.1 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 15.0% | 33.3% | 33.3% | 0.0% | -6.6 | 0.40 | 0.79 | +14.0 | +18.7 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=66.7% Avg=+22.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 18.8% | -16.6 | 0.38 | 1.15 | +17.4 | +10.6 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 93.8% | 26.7% | 26.7% | 20.0% | -15.7 | 0.41 | 1.14 | +18.3 | +10.7 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 93.8% | 26.7% | 26.7% | 20.0% | -15.7 | 0.41 | 1.14 | +18.3 | +10.7 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 18.8% | -16.6 | 0.38 | 1.15 | +17.4 | +10.6 |
| `asian_range_gte_30` | 14 | S_STRANGER | 87.5% | 28.6% | 28.6% | 21.4% | -15.3 | 0.44 | 1.09 | +19.1 | +11.9 |
| `confluence_gte_60` | 14 | S_STRANGER | 87.5% | 14.3% | 14.3% | 14.3% | -23.9 | 0.23 | 1.36 | +14.1 | +10.7 |
| `confluence_gte_70` | 4 | R_REPEATER | 25.0% | 50.0% | 50.0% | 50.0% | +16.5 | 3.10 | 3.10 | +35.0 | +15.7 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 56.2% | 33.3% | 33.3% | 22.2% | -7.0 | 0.67 | 1.35 | +20.7 | +11.8 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 37.5% | 66.7% | 66.7% | 50.0% | +22.4 | 5.26 | 2.63 | +36.6 | +13.6 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 81.2% | 30.8% | 30.8% | 23.1% | -14.1 | 0.47 | 1.07 | +20.3 | +12.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 43.8% | 42.9% | 42.9% | 28.6% | -1.4 | 0.93 | 1.24 | +25.5 | +13.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 18.8% | -16.6 | 0.38 | 1.15 | +17.4 | +10.6 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 18.8% | -16.6 | 0.38 | 1.15 | +17.4 | +10.6 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -32.8 | 0.00 | 0.00 | +4.5 | +10.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 18.8% | 33.3% | 33.3% | 33.3% | +7.0 | 1.66 | 3.33 | +25.6 | +17.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+1.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 24.3% | 27.0% | 24.3% | -1.8 | 0.55 | 1.43 | +4.7 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 37.8% | 21.4% | 21.4% | 21.4% | -2.4 | 0.34 | 1.24 | +4.1 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 54.1% | 30.0% | 30.0% | 30.0% | -0.4 | 0.88 | 2.05 | +5.3 | +4.5 |
| `stop_hunt_le_90` | 35 | S_STRANGER | 94.6% | 20.0% | 22.9% | 20.0% | -2.7 | 0.37 | 1.22 | +4.1 | +6.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 40.5% | 20.0% | 26.7% | 20.0% | -2.9 | 0.47 | 1.30 | +5.1 | +6.2 |
| `confluence_gte_70` | 1 | S_STRANGER | 2.7% | 0.0% | 0.0% | 0.0% | -9.5 | 0.00 | 0.00 | +0.3 | +10.3 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 45.9% | 5.9% | 5.9% | 11.8% | -5.7 | 0.10 | 1.45 | +3.2 | +7.1 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 48.6% | 27.8% | 27.8% | 22.2% | -1.1 | 0.63 | 1.65 | +4.3 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 37 | S_STRANGER | 100.0% | 24.3% | 27.0% | 24.3% | -1.8 | 0.55 | 1.43 | +4.7 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 24.3% | 27.0% | 24.3% | -1.8 | 0.55 | 1.43 | +4.7 | +5.7 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 24.3% | 22.2% | 22.2% | 22.2% | -1.7 | 0.52 | 1.82 | +4.0 | +4.2 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 16.2% | 33.3% | 33.3% | 33.3% | +1.6 | 2.44 | 4.88 | +5.6 | +2.0 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+4.4; validation N=1 Fav=0.0% Avg=-14.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 24.1% | 24.1% | 27.6% | +0.0 | 1.00 | 2.58 | +8.9 | +6.9 |
| `hunt_to_ar_ratio_le_2_0` | 6 | R_REPEATER | 20.7% | 50.0% | 50.0% | 50.0% | +1.3 | 1.33 | 1.33 | +11.6 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 31.0% | 44.4% | 44.4% | 55.6% | +1.7 | 1.50 | 1.50 | +11.3 | +7.2 |
| `stop_hunt_le_90` | 25 | S_STRANGER | 86.2% | 24.0% | 24.0% | 32.0% | +0.1 | 1.03 | 2.56 | +9.1 | +7.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 62.1% | 27.8% | 27.8% | 27.8% | +0.7 | 1.23 | 2.45 | +10.0 | +7.1 |
| `confluence_gte_70` | 3 | S_STRANGER | 10.3% | 33.3% | 33.3% | 0.0% | +0.3 | 1.34 | 1.34 | +10.5 | +4.1 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 17.2% | 20.0% | 20.0% | 20.0% | -2.6 | 0.23 | 0.70 | +11.7 | +7.9 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 69.0% | 15.0% | 15.0% | 15.0% | -1.8 | 0.53 | 2.48 | +8.2 | +8.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 86.2% | 24.0% | 24.0% | 32.0% | +0.1 | 1.03 | 2.56 | +9.1 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 96.6% | 25.0% | 25.0% | 28.6% | +0.1 | 1.03 | 2.49 | +9.2 | +7.0 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 6.9% | 50.0% | 50.0% | 50.0% | +6.2 | 7.25 | 7.25 | +8.2 | +2.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.4% | 0.0% | 0.0% | 0.0% | -2.0 | 0.00 | 0.00 | +0.7 | +3.8 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=33.3% Avg=+0.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 23.5% | -2.4 | 0.53 | 1.73 | +9.5 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 14.3% | -4.1 | 0.44 | 2.63 | +6.1 | +10.0 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 14.3% | -4.1 | 0.44 | 2.63 | +6.1 | +10.0 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 88.2% | 26.7% | 26.7% | 26.7% | -2.3 | 0.57 | 1.58 | +10.5 | +7.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 23.5% | -2.4 | 0.53 | 1.73 | +9.5 | +7.4 |
| `confluence_gte_70` | 9 | S_STRANGER | 52.9% | 33.3% | 33.3% | 33.3% | +0.4 | 1.11 | 2.22 | +11.7 | +5.6 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 94.1% | 18.8% | 18.8% | 18.8% | -3.1 | 0.43 | 1.87 | +8.3 | +7.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 41.2% | 28.6% | 28.6% | 28.6% | -3.6 | 0.55 | 1.38 | +14.3 | +10.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -9.1 | 0.00 | 0.00 | +8.0 | +10.8 |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 70.6% | 25.0% | 25.0% | 25.0% | -2.1 | 0.59 | 1.78 | +9.3 | +7.8 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 94.1% | 25.0% | 25.0% | 25.0% | -1.9 | 0.60 | 1.80 | +9.6 | +7.1 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 29.4% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +3.7 | +7.5 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 17.6% | 33.3% | 33.3% | 33.3% | -3.0 | 0.51 | 1.02 | +15.6 | +7.3 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=50.0% Avg=+9.3; validation N=3 Fav=0.0% Avg=-1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 47 | S_STRANGER | 100.0% | 23.4% | 27.7% | 29.8% | -1.6 | 0.76 | 1.80 | +10.1 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 38 | S_STRANGER | 80.9% | 18.4% | 23.7% | 26.3% | -4.0 | 0.48 | 1.38 | +8.9 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 41 | S_STRANGER | 87.2% | 19.5% | 24.4% | 26.8% | -3.2 | 0.57 | 1.59 | +9.3 | +6.4 |
| `stop_hunt_le_90` | 43 | S_STRANGER | 91.5% | 20.9% | 25.6% | 27.9% | -2.6 | 0.63 | 1.65 | +9.5 | +6.2 |
| `asian_range_gte_30` | 34 | S_STRANGER | 72.3% | 23.5% | 29.4% | 29.4% | -1.2 | 0.81 | 1.79 | +10.3 | +6.1 |
| `confluence_gte_60` | 18 | S_STRANGER | 38.3% | 33.3% | 33.3% | 44.4% | +1.4 | 1.25 | 2.08 | +13.5 | +5.9 |
| `confluence_gte_70` | 1 | S_STRANGER | 2.1% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +9.7 | +0.6 |
| `tdi_rsi_gt_signal` | 35 | S_STRANGER | 74.5% | 22.9% | 25.7% | 31.4% | -1.8 | 0.74 | 1.90 | +10.9 | +5.9 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 27.7% | 38.5% | 38.5% | 46.2% | +6.7 | 3.08 | 4.31 | +17.9 | +7.1 |
| `ratio_le_2_and_asian_gte_30` | 31 | S_STRANGER | 66.0% | 19.4% | 25.8% | 25.8% | -3.4 | 0.53 | 1.39 | +8.3 | +6.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 22 | S_STRANGER | 46.8% | 13.6% | 18.2% | 22.7% | -5.0 | 0.36 | 1.43 | +7.9 | +6.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 45 | S_STRANGER | 95.7% | 22.2% | 26.7% | 28.9% | -2.4 | 0.65 | 1.63 | +9.3 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 47 | S_STRANGER | 100.0% | 23.4% | 27.7% | 29.8% | -1.6 | 0.76 | 1.80 | +10.1 | +6.2 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 8.5% | 50.0% | 50.0% | 50.0% | +4.5 | 1.99 | 1.99 | +10.2 | +6.1 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 4.3% | 50.0% | 50.0% | 50.0% | +6.6 | 2.56 | 2.56 | +12.8 | +4.8 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=40.0% Avg=+0.2; validation N=6 Fav=0.0% Avg=-8.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 32.3% | -1.9 | 0.71 | 2.04 | +10.5 | +10.7 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 32.3% | -1.9 | 0.71 | 2.04 | +10.5 | +10.7 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 32.3% | -1.9 | 0.71 | 2.04 | +10.5 | +10.7 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 32.3% | -1.9 | 0.71 | 2.04 | +10.5 | +10.7 |
| `asian_range_gte_30` | 25 | S_STRANGER | 80.6% | 20.0% | 20.0% | 36.0% | -1.9 | 0.73 | 2.32 | +11.3 | +11.1 |
| `confluence_gte_60` | 16 | S_STRANGER | 51.6% | 25.0% | 25.0% | 25.0% | -3.1 | 0.67 | 1.85 | +13.5 | +13.4 |
| `confluence_gte_70` | 8 | S_STRANGER | 25.8% | 12.5% | 12.5% | 12.5% | -11.3 | 0.27 | 1.90 | +13.5 | +19.9 |
| `tdi_rsi_gt_signal` | 3 | R_REPEATER | 9.7% | 66.7% | 66.7% | 66.7% | +21.1 | 317.00 | 158.50 | +28.6 | +2.6 |
| `tdi_rsi_gte_50` | 21 | S_STRANGER | 67.7% | 23.8% | 23.8% | 28.6% | -1.8 | 0.78 | 2.33 | +12.8 | +11.6 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 80.6% | 20.0% | 20.0% | 36.0% | -1.9 | 0.73 | 2.32 | +11.3 | +11.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 6.5% | 50.0% | 50.0% | 50.0% | +23.3 | 234.50 | 234.50 | +32.3 | +3.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 32.3% | -1.9 | 0.71 | 2.04 | +10.5 | +10.7 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 32.3% | -1.9 | 0.71 | 2.04 | +10.5 | +10.7 |
| `feature_momentum_breakout_exception` | 4 | R_RUNNER | 12.9% | 75.0% | 75.0% | 75.0% | +9.7 | 999.00 | 999.00 | +13.2 | +3.1 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_RUNNER | 6.5% | 100.0% | 100.0% | 100.0% | +17.1 | 999.00 | 999.00 | +21.5 | +0.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+4.7; validation N=3 Fav=33.3% Avg=-1.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 33.3% | -5.8 | 0.27 | 0.74 | +6.8 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 61.1% | 9.1% | 9.1% | 0.0% | -8.4 | 0.03 | 0.35 | +3.3 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 66.7% | 8.3% | 8.3% | 8.3% | -7.7 | 0.03 | 0.35 | +3.6 | +6.7 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 88.9% | 12.5% | 12.5% | 25.0% | -7.7 | 0.14 | 0.74 | +5.2 | +5.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 5 | S_STRANGER | 27.8% | 0.0% | 0.0% | 20.0% | -11.3 | 0.00 | 0.00 | +3.5 | +5.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 66.7% | 33.3% | 33.3% | 41.7% | -2.4 | 0.58 | 0.87 | +8.9 | +3.9 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 38.9% | 42.9% | 42.9% | 57.1% | +2.0 | 2.71 | 1.81 | +10.7 | +3.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 88.9% | 12.5% | 12.5% | 25.0% | -7.7 | 0.14 | 0.74 | +5.2 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 33.3% | -5.8 | 0.27 | 0.74 | +6.8 | +4.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=0.0% Avg=-3.0; validation N=16 Fav=37.5% Avg=+3.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 25.0% | -1.3 | 0.77 | 2.58 | +12.5 | +9.7 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 85.7% | 20.8% | 20.8% | 25.0% | -1.8 | 0.67 | 2.26 | +12.9 | +8.7 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 96.4% | 18.5% | 18.5% | 22.2% | -2.8 | 0.53 | 2.12 | +11.5 | +9.8 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 96.4% | 18.5% | 18.5% | 22.2% | -2.8 | 0.53 | 2.12 | +11.5 | +9.8 |
| `asian_range_gte_30` | 23 | S_STRANGER | 82.1% | 26.1% | 26.1% | 30.4% | +1.6 | 1.41 | 3.52 | +14.9 | +9.0 |
| `confluence_gte_60` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 25.0% | -1.3 | 0.77 | 2.58 | +12.5 | +9.7 |
| `confluence_gte_70` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 25.0% | -1.3 | 0.77 | 2.58 | +12.5 | +9.7 |
| `tdi_rsi_gt_signal` | 26 | S_STRANGER | 92.9% | 19.2% | 19.2% | 23.1% | -2.0 | 0.68 | 2.72 | +12.1 | +10.1 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 71.4% | 20.0% | 20.0% | 20.0% | +0.8 | 1.19 | 4.46 | +13.1 | +9.4 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 75.0% | 23.8% | 23.8% | 28.6% | -0.1 | 0.97 | 2.72 | +14.3 | +8.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 19 | S_STRANGER | 67.9% | 21.1% | 21.1% | 26.3% | -0.9 | 0.80 | 2.80 | +13.9 | +9.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 96.4% | 18.5% | 18.5% | 22.2% | -2.8 | 0.53 | 2.12 | +11.5 | +9.8 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 21.4% | 21.4% | 25.0% | -1.3 | 0.77 | 2.58 | +12.5 | +9.7 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 3.6% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +3.8 | +8.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.6% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +3.8 | +8.2 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-3.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=40.0% Avg=+0.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | -9.0 | 0.15 | 0.54 | +7.7 | +7.5 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +5.7 | +3.9 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 50.0% | 28.6% | 28.6% | 28.6% | -0.7 | 0.78 | 1.94 | +6.9 | +5.5 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 15.4% | -10.1 | 0.11 | 0.61 | +6.1 | +7.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 20.0% | -4.2 | 0.22 | 0.87 | +8.1 | +8.6 |
| `confluence_gte_70` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +6.8 | +7.2 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -2.1 | 0.00 | 0.00 | +10.6 | +3.8 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 16.7% | -5.8 | 0.13 | 0.66 | +10.0 | +9.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 78.6% | 18.2% | 18.2% | 18.2% | -8.7 | 0.15 | 0.65 | +6.8 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | -9.0 | 0.15 | 0.54 | +7.7 | +7.5 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -17.6 | 0.00 | 0.00 | +2.1 | +19.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -12.4 | 0.00 | 0.00 | +4.9 | +14.3 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=16 Fav=37.5% Avg=+12.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 20.7% | 20.7% | 20.7% | -1.3 | 0.88 | 3.39 | +26.7 | +21.4 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 65.5% | 31.6% | 31.6% | 31.6% | +6.2 | 1.66 | 3.60 | +28.1 | +19.0 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 75.9% | 27.3% | 27.3% | 27.3% | +5.0 | 1.60 | 4.27 | +27.1 | +17.6 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 93.1% | 22.2% | 22.2% | 22.2% | -0.6 | 0.95 | 3.32 | +25.3 | +21.5 |
| `asian_range_gte_30` | 23 | S_STRANGER | 79.3% | 26.1% | 26.1% | 26.1% | +2.6 | 1.26 | 3.57 | +29.1 | +17.1 |
| `confluence_gte_60` | 11 | S_STRANGER | 37.9% | 9.1% | 9.1% | 9.1% | -13.0 | 0.24 | 2.41 | +22.1 | +31.7 |
| `confluence_gte_70` | 3 | S_STRANGER | 10.3% | 0.0% | 0.0% | 0.0% | -14.1 | 0.00 | 0.00 | +18.2 | +37.3 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 20.7% | 33.3% | 33.3% | 33.3% | -7.6 | 0.64 | 1.28 | +27.8 | +26.6 |
| `tdi_rsi_gte_50` | 25 | S_STRANGER | 86.2% | 24.0% | 24.0% | 24.0% | +0.9 | 1.08 | 3.42 | +30.0 | +23.5 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 55.2% | 37.5% | 37.5% | 37.5% | +12.6 | 3.21 | 5.35 | +31.1 | +10.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 13.8% | 50.0% | 50.0% | 50.0% | +15.4 | 4.04 | 4.04 | +39.6 | +9.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 79.3% | 26.1% | 26.1% | 26.1% | +1.7 | 1.15 | 3.26 | +26.9 | +19.9 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 75.9% | 27.3% | 27.3% | 27.3% | +2.5 | 1.23 | 3.28 | +28.1 | +19.6 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 13.8% | 50.0% | 50.0% | 50.0% | +17.9 | 4.53 | 4.53 | +29.4 | +4.7 |
| `feature_eurjpy_tdi50_reclaim` | 13 | S_STRANGER | 44.8% | 30.8% | 30.8% | 30.8% | +6.9 | 1.71 | 3.84 | +33.6 | +24.2 |

### THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+5.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +1.3 | 1.39 | 4.85 | +10.3 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 28.6% | +3.0 | 1.76 | 3.53 | +12.6 | +5.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +1.3 | 1.39 | 4.85 | +10.3 | +5.6 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | +1.3 | 1.39 | 4.85 | +10.3 | +5.6 |
| `asian_range_gte_30` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 28.6% | +4.2 | 2.58 | 5.16 | +12.3 | +4.8 |
| `confluence_gte_60` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 16.7% | +2.7 | 1.66 | 8.32 | +11.3 | +5.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 50.0% | -4.8 | 0.00 | 0.00 | +11.5 | +8.3 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 14.3% | +2.6 | 1.61 | 4.04 | +11.5 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 33.3% | +5.0 | 2.71 | 4.06 | +13.8 | +4.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +17.8 | +4.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 25.0% | +2.2 | 1.57 | 3.93 | +11.9 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 22.2% | +1.8 | 1.53 | 4.58 | +10.9 | +5.5 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | -2.3 | 0.46 | 1.37 | +4.5 | +6.1 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | -2.3 | 0.46 | 1.37 | +4.5 | +6.1 |

### THE_33_MW|BUY|MID_WEEK|L2|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L2|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=2 Fav=0.0% Avg=-2.4; out_of_sample N=3 Fav=66.7% Avg=+10.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | +1.1 | 1.37 | 5.48 | +9.2 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 0.0% | +1.8 | 1.60 | 5.59 | +8.8 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 0.0% | +1.8 | 1.60 | 5.59 | +8.8 | +5.4 |
| `stop_hunt_le_90` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 0.0% | +1.8 | 1.60 | 5.59 | +8.8 | +5.4 |
| `asian_range_gte_30` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 0.0% | +1.3 | 1.39 | 4.86 | +9.8 | +5.5 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | +1.1 | 1.37 | 5.48 | +9.2 | +5.4 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | +1.1 | 1.37 | 5.48 | +9.2 | +5.4 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | +3.3 | 3.66 | 10.98 | +9.1 | +3.4 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 40.0% | 40.0% | 0.0% | +5.5 | 2.85 | 4.28 | +14.7 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 0.0% | +2.0 | 1.62 | 4.87 | +9.4 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | +4.6 | 3.98 | 7.96 | +11.0 | +2.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 0.0% | +1.8 | 1.60 | 5.59 | +8.8 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | +1.1 | 1.37 | 5.48 | +9.2 | +5.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+9.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 15.0% | +0.1 | 1.01 | 4.04 | +16.5 | +9.2 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 16.7% | 16.7% | 16.7% | +0.5 | 1.08 | 5.38 | +15.8 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 15.0% | +0.1 | 1.01 | 4.04 | +16.5 | +9.2 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 15.0% | +0.1 | 1.01 | 4.04 | +16.5 | +9.2 |
| `asian_range_gte_30` | 13 | S_STRANGER | 65.0% | 23.1% | 23.1% | 23.1% | +2.7 | 1.40 | 4.66 | +17.4 | +8.7 |
| `confluence_gte_60` | 8 | S_STRANGER | 40.0% | 12.5% | 12.5% | 12.5% | +1.8 | 1.27 | 8.86 | +18.5 | +10.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 45.0% | 22.2% | 22.2% | 22.2% | +5.2 | 1.84 | 6.45 | +16.7 | +11.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | +2.3 | 1.29 | 5.17 | +21.1 | +13.0 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 65.0% | 23.1% | 23.1% | 23.1% | +2.7 | 1.40 | 4.66 | +17.4 | +8.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 35.0% | 28.6% | 28.6% | 28.6% | +9.3 | 2.75 | 6.89 | +21.3 | +9.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 90.0% | 16.7% | 16.7% | 16.7% | +0.5 | 1.08 | 5.38 | +15.8 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 95.0% | 21.1% | 21.1% | 15.8% | +0.8 | 1.13 | 4.25 | +16.9 | +8.7 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 30.0% | 16.7% | 16.7% | 16.7% | -2.3 | 0.61 | 3.05 | +9.5 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 15.0% | 0.0% | 0.0% | 0.0% | -9.0 | 0.00 | 0.00 | +9.5 | +13.6 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=14.3% Avg=-6.2; validation N=5 Fav=40.0% Avg=+9.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 20.0% | 24.0% | 28.0% | -1.5 | 0.74 | 1.97 | +9.6 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 88.0% | 18.2% | 22.7% | 22.7% | -2.0 | 0.69 | 2.06 | +9.6 | +9.6 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 92.0% | 17.4% | 21.7% | 26.1% | -1.9 | 0.69 | 2.06 | +9.8 | +9.4 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 96.0% | 16.7% | 20.8% | 25.0% | -1.8 | 0.68 | 2.19 | +9.6 | +9.1 |
| `asian_range_gte_30` | 15 | S_STRANGER | 60.0% | 20.0% | 26.7% | 20.0% | -1.5 | 0.78 | 1.95 | +11.5 | +7.4 |
| `confluence_gte_60` | 10 | S_STRANGER | 40.0% | 20.0% | 20.0% | 30.0% | -3.9 | 0.49 | 1.70 | +8.3 | +6.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 64.0% | 18.8% | 18.8% | 18.8% | -2.0 | 0.66 | 2.66 | +10.4 | +11.0 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 48.0% | 25.0% | 25.0% | 25.0% | +0.5 | 1.09 | 2.92 | +12.6 | +11.6 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 60.0% | 20.0% | 26.7% | 20.0% | -1.5 | 0.78 | 1.95 | +11.5 | +7.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 44.0% | 27.3% | 27.3% | 27.3% | -0.1 | 0.99 | 2.31 | +12.9 | +8.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 100.0% | 20.0% | 24.0% | 28.0% | -1.5 | 0.74 | 1.97 | +9.6 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 20.0% | 24.0% | 28.0% | -1.5 | 0.74 | 1.97 | +9.6 | +8.8 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 20.0% | 40.0% | 40.0% | 40.0% | -0.3 | 0.90 | 0.90 | +6.0 | +5.6 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 8.0% | 50.0% | 50.0% | 0.0% | -2.1 | 0.58 | 0.58 | +7.2 | +8.9 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=-9.9; validation N=3 Fav=66.7% Avg=+16.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 26.7% | -6.2 | 0.36 | 1.19 | +10.6 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -3.6 | 0.48 | 0.97 | +14.6 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -3.6 | 0.48 | 0.97 | +14.6 | +4.9 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 93.3% | 21.4% | 21.4% | 21.4% | -6.6 | 0.36 | 1.19 | +9.8 | +8.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | R_REPEATER | 40.0% | 50.0% | 50.0% | 50.0% | +3.0 | 1.54 | 1.03 | +15.6 | +4.8 |
| `confluence_gte_70` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +7.1 | +2.6 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 73.3% | 27.3% | 27.3% | 36.4% | -5.2 | 0.48 | 0.95 | +12.3 | +8.5 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 33.3% | 40.0% | 40.0% | 20.0% | +1.6 | 1.24 | 1.87 | +14.7 | +11.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 93.3% | 21.4% | 21.4% | 21.4% | -6.6 | 0.36 | 1.19 | +9.8 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 26.7% | -6.2 | 0.36 | 1.19 | +10.6 | +8.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=37.5% Avg=-6.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 35.0% | -8.0 | 0.29 | 0.70 | +11.7 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 35.0% | -8.0 | 0.29 | 0.70 | +11.7 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 35.0% | -8.0 | 0.29 | 0.70 | +11.7 | +7.1 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 35.0% | -8.0 | 0.29 | 0.70 | +11.7 | +7.1 |
| `asian_range_gte_30` | 17 | S_STRANGER | 85.0% | 17.6% | 23.5% | 29.4% | -10.1 | 0.22 | 0.61 | +10.4 | +7.3 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 35.0% | -8.0 | 0.29 | 0.70 | +11.7 | +7.1 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 35.0% | -8.0 | 0.29 | 0.70 | +11.7 | +7.1 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 90.0% | 11.1% | 16.7% | 27.8% | -10.7 | 0.15 | 0.61 | +9.9 | +7.7 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 30.0% | 16.7% | 16.7% | 33.3% | -2.4 | 0.44 | 1.76 | +13.6 | +6.8 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 85.0% | 17.6% | 23.5% | 29.4% | -10.1 | 0.22 | 0.61 | +10.4 | +7.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 16 | S_STRANGER | 80.0% | 12.5% | 18.8% | 25.0% | -11.7 | 0.16 | 0.57 | +9.7 | +7.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 35.0% | -8.0 | 0.29 | 0.70 | +11.7 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 35.0% | -8.0 | 0.29 | 0.70 | +11.7 | +7.1 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 40.0% | 37.5% | 50.0% | 62.5% | -6.6 | 0.49 | 0.25 | +17.5 | +3.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 10.0% | 50.0% | 50.0% | 100.0% | +5.6 | 999.00 | 999.00 | +23.4 | +2.9 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-4.2; validation N=7 Fav=28.6% Avg=-10.7; out_of_sample N=2 Fav=50.0% Avg=+7.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 36 | S_STRANGER | 100.0% | 19.4% | 22.2% | 22.2% | -4.2 | 0.45 | 1.41 | +8.8 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 33.3% | 16.7% | 16.7% | 25.0% | -3.5 | 0.26 | 1.03 | +7.7 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 47.2% | 17.6% | 17.6% | 23.5% | -3.5 | 0.25 | 1.01 | +9.0 | +6.5 |
| `stop_hunt_le_90` | 34 | S_STRANGER | 94.4% | 17.6% | 20.6% | 17.6% | -5.5 | 0.32 | 1.16 | +7.9 | +8.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 31 | S_STRANGER | 86.1% | 16.1% | 19.4% | 22.6% | -4.7 | 0.42 | 1.54 | +8.6 | +8.5 |
| `confluence_gte_70` | 10 | S_STRANGER | 27.8% | 20.0% | 20.0% | 40.0% | -1.2 | 0.72 | 2.16 | +10.3 | +7.6 |
| `tdi_rsi_gt_signal` | 31 | S_STRANGER | 86.1% | 22.6% | 25.8% | 25.8% | -2.1 | 0.66 | 1.65 | +9.8 | +8.9 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 30.6% | 27.3% | 27.3% | 9.1% | -6.3 | 0.36 | 0.97 | +8.5 | +14.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 35 | S_STRANGER | 97.2% | 20.0% | 22.9% | 20.0% | -4.4 | 0.45 | 1.41 | +8.8 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 36 | S_STRANGER | 100.0% | 19.4% | 22.2% | 22.2% | -4.2 | 0.45 | 1.41 | +8.8 | +8.2 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 8.3% | 33.3% | 33.3% | 66.7% | +9.3 | 4.73 | 4.73 | +15.8 | +4.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.8% | 0.0% | 0.0% | 0.0% | -7.5 | 0.00 | 0.00 | +0.2 | +10.6 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=37.5% Avg=+6.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=0.0% Avg=-11.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 19.2% | 26.9% | 19.2% | -4.7 | 0.48 | 1.17 | +10.5 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 96.2% | 20.0% | 28.0% | 20.0% | -4.5 | 0.50 | 1.14 | +9.7 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 96.2% | 20.0% | 28.0% | 20.0% | -4.5 | 0.50 | 1.14 | +9.7 | +7.0 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 19.2% | 26.9% | 19.2% | -4.7 | 0.48 | 1.17 | +10.5 | +7.4 |
| `asian_range_gte_30` | 20 | S_STRANGER | 76.9% | 20.0% | 30.0% | 20.0% | -4.4 | 0.54 | 1.08 | +11.0 | +6.7 |
| `confluence_gte_60` | 17 | S_STRANGER | 65.4% | 23.5% | 29.4% | 29.4% | -3.0 | 0.62 | 1.24 | +12.3 | +7.4 |
| `confluence_gte_70` | 8 | S_STRANGER | 30.8% | 25.0% | 25.0% | 50.0% | +4.3 | 2.17 | 4.35 | +20.3 | +10.4 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 69.2% | 22.2% | 27.8% | 16.7% | -7.0 | 0.33 | 0.79 | +10.0 | +6.7 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 38.5% | 30.0% | 30.0% | 10.0% | +2.5 | 1.46 | 3.42 | +15.6 | +12.3 |
| `ratio_le_2_and_asian_gte_30` | 20 | S_STRANGER | 76.9% | 20.0% | 30.0% | 20.0% | -4.4 | 0.54 | 1.08 | +11.0 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 50.0% | 23.1% | 30.8% | 15.4% | -7.7 | 0.34 | 0.69 | +9.7 | +5.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 19.2% | 26.9% | 19.2% | -4.7 | 0.48 | 1.17 | +10.5 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 19.2% | 26.9% | 19.2% | -4.7 | 0.48 | 1.17 | +10.5 | +7.4 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 38.5% | 10.0% | 20.0% | 20.0% | -3.8 | 0.36 | 1.25 | +6.2 | +8.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 11.5% | 0.0% | 0.0% | 0.0% | -6.5 | 0.00 | 0.00 | +2.7 | +12.6 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=14.3% Avg=+0.6; validation N=2 Fav=50.0% Avg=+7.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | +1.9 | 3.48 | 9.27 | +8.4 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 37.5% | 16.7% | 16.7% | 16.7% | +2.2 | 17.63 | 52.88 | +8.1 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 50.0% | 12.5% | 12.5% | 25.0% | +1.6 | 11.75 | 47.00 | +9.8 | +3.4 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | +1.9 | 3.48 | 9.27 | +8.4 | +4.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | +1.9 | 3.48 | 9.27 | +8.4 | +4.3 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | +1.9 | 3.48 | 9.27 | +8.4 | +4.3 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 56.2% | 22.2% | 22.2% | 44.4% | +2.1 | 3.67 | 5.51 | +8.8 | +3.2 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 87.5% | 14.3% | 14.3% | 35.7% | +1.4 | 4.16 | 14.55 | +8.3 | +3.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 31.2% | +1.9 | 3.48 | 9.27 | +8.4 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 93.8% | 20.0% | 20.0% | 33.3% | +2.1 | 3.50 | 8.18 | +8.9 | +4.3 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 50.0% | -0.0 | 0.00 | 0.00 | +5.2 | +3.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 50.0% | -0.0 | 0.00 | 0.00 | +5.2 | +3.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-2.2; validation N=4 Fav=25.0% Avg=+1.0; out_of_sample N=4 Fav=25.0% Avg=+0.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | -1.4 | 0.70 | 2.58 | +9.3 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 18.8% | 33.3% | 33.3% | 66.7% | +5.1 | 2.35 | 2.35 | +18.2 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 68.8% | 18.2% | 18.2% | 18.2% | -1.0 | 0.79 | 3.17 | +9.9 | +7.8 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | -1.4 | 0.70 | 2.58 | +9.3 | +7.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | -1.4 | 0.70 | 2.58 | +9.3 | +7.1 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | -1.4 | 0.70 | 2.58 | +9.3 | +7.1 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 56.2% | 22.2% | 22.2% | 22.2% | +0.2 | 1.06 | 3.18 | +10.5 | +5.3 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 56.2% | 22.2% | 22.2% | 22.2% | +0.5 | 1.13 | 3.40 | +10.6 | +6.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | -1.4 | 0.70 | 2.58 | +9.3 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | -1.4 | 0.70 | 2.58 | +9.3 | +7.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=50.0% Avg=+7.4; validation N=6 Fav=33.3% Avg=+7.9; out_of_sample N=4 Fav=0.0% Avg=-8.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 18.8% | 25.0% | 12.5% | -1.8 | 0.78 | 2.35 | +12.5 | +10.0 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 87.5% | 21.4% | 28.6% | 14.3% | +0.4 | 1.06 | 2.66 | +13.8 | +9.2 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 93.8% | 20.0% | 26.7% | 13.3% | -0.7 | 0.91 | 2.51 | +13.0 | +10.2 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 93.8% | 20.0% | 26.7% | 13.3% | -0.7 | 0.91 | 2.51 | +13.0 | +10.2 |
| `asian_range_gte_30` | 12 | S_STRANGER | 75.0% | 16.7% | 25.0% | 8.3% | -3.5 | 0.62 | 1.85 | +11.8 | +9.4 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 18.8% | 25.0% | 12.5% | -1.8 | 0.78 | 2.35 | +12.5 | +10.0 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 18.8% | 25.0% | 12.5% | -1.8 | 0.78 | 2.35 | +12.5 | +10.0 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 25.0% | 25.0% | 25.0% | 0.0% | +2.6 | 1.35 | 4.04 | +15.0 | +16.6 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 75.0% | 25.0% | 33.3% | 16.7% | +2.5 | 1.39 | 2.79 | +15.3 | +11.7 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 68.8% | 18.2% | 27.3% | 9.1% | -2.1 | 0.75 | 1.99 | +12.3 | +9.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 18.8% | 33.3% | 33.3% | 0.0% | +8.9 | 2.91 | 5.83 | +19.7 | +13.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 93.8% | 20.0% | 26.7% | 13.3% | -0.7 | 0.91 | 2.51 | +13.0 | +10.2 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 18.8% | 25.0% | 12.5% | -1.8 | 0.78 | 2.35 | +12.5 | +10.0 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -4.2 | 0.00 | 0.00 | +2.9 | +5.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -4.2 | 0.00 | 0.00 | +2.9 | +5.1 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-6.9; validation N=4 Fav=75.0% Avg=+9.8; out_of_sample N=4 Fav=50.0% Avg=+5.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 18.5% | 18.5% | 14.8% | -11.6 | 0.20 | 0.79 | +6.9 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 74.1% | 20.0% | 20.0% | 20.0% | -4.8 | 0.43 | 1.51 | +7.6 | +6.8 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 88.9% | 16.7% | 16.7% | 16.7% | -10.4 | 0.23 | 1.02 | +6.7 | +6.1 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 88.9% | 20.8% | 20.8% | 16.7% | -9.0 | 0.26 | 0.89 | +7.3 | +6.2 |
| `asian_range_gte_30` | 23 | S_STRANGER | 85.2% | 21.7% | 21.7% | 17.4% | -8.0 | 0.29 | 0.94 | +7.7 | +6.6 |
| `confluence_gte_60` | 27 | S_STRANGER | 100.0% | 18.5% | 18.5% | 14.8% | -11.6 | 0.20 | 0.79 | +6.9 | +5.9 |
| `confluence_gte_70` | 16 | S_STRANGER | 59.3% | 12.5% | 12.5% | 12.5% | -14.3 | 0.17 | 1.04 | +7.7 | +5.3 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 59.3% | 25.0% | 25.0% | 12.5% | -11.7 | 0.27 | 0.73 | +9.0 | +5.7 |
| `tdi_rsi_gte_50` | 9 | R_REPEATER | 33.3% | 55.6% | 55.6% | 33.3% | +6.1 | 3.51 | 2.11 | +14.1 | +6.3 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 70.4% | 21.1% | 21.1% | 21.1% | -4.8 | 0.44 | 1.44 | +7.9 | +7.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 40.7% | 27.3% | 27.3% | 18.2% | -4.7 | 0.55 | 1.29 | +10.1 | +6.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 88.9% | 20.8% | 20.8% | 16.7% | -9.0 | 0.26 | 0.89 | +7.3 | +6.2 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 18.5% | 18.5% | 14.8% | -11.6 | 0.20 | 0.79 | +6.9 | +5.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=10.0% Avg=-6.4; validation N=7 Fav=57.1% Avg=+3.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 38 | S_STRANGER | 100.0% | 18.4% | 23.7% | 21.1% | -2.4 | 0.47 | 1.32 | +8.0 | +6.8 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 47.4% | 11.1% | 16.7% | 27.8% | -5.2 | 0.20 | 0.73 | +6.6 | +9.9 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 57.9% | 9.1% | 13.6% | 22.7% | -5.8 | 0.15 | 0.77 | +6.9 | +8.7 |
| `stop_hunt_le_90` | 36 | S_STRANGER | 94.7% | 13.9% | 19.4% | 19.4% | -3.4 | 0.31 | 1.11 | +7.5 | +7.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 44.7% | 29.4% | 29.4% | 29.4% | -2.4 | 0.56 | 1.13 | +9.9 | +8.6 |
| `confluence_gte_70` | 4 | S_STRANGER | 10.5% | 25.0% | 25.0% | 0.0% | -9.5 | 0.18 | 0.53 | +13.8 | +17.9 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 18.4% | 14.3% | 14.3% | 0.0% | -8.4 | 0.12 | 0.73 | +8.2 | +13.5 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 60.5% | 17.4% | 17.4% | 13.0% | -2.5 | 0.47 | 2.00 | +9.0 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 37 | S_STRANGER | 97.4% | 16.2% | 21.6% | 21.6% | -2.6 | 0.44 | 1.39 | +7.9 | +7.0 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 100.0% | 18.4% | 23.7% | 21.1% | -2.4 | 0.47 | 1.32 | +8.0 | +6.8 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 5.3% | 0.0% | 0.0% | 50.0% | -2.1 | 0.00 | 0.00 | +4.8 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=41.7% Avg=-1.0; validation N=12 Fav=25.0% Avg=+4.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 49 | S_STRANGER | 100.0% | 18.4% | 24.5% | 16.3% | -1.2 | 0.76 | 1.96 | +9.2 | +8.7 |
| `hunt_to_ar_ratio_le_2_0` | 47 | S_STRANGER | 95.9% | 19.1% | 25.5% | 17.0% | -1.3 | 0.76 | 1.84 | +9.1 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 49 | S_STRANGER | 100.0% | 18.4% | 24.5% | 16.3% | -1.2 | 0.76 | 1.96 | +9.2 | +8.7 |
| `stop_hunt_le_90` | 49 | S_STRANGER | 100.0% | 18.4% | 24.5% | 16.3% | -1.2 | 0.76 | 1.96 | +9.2 | +8.7 |
| `asian_range_gte_30` | 38 | S_STRANGER | 77.6% | 18.4% | 26.3% | 15.8% | -1.3 | 0.76 | 1.82 | +9.4 | +7.7 |
| `confluence_gte_60` | 14 | S_STRANGER | 28.6% | 21.4% | 28.6% | 7.1% | -1.6 | 0.78 | 1.95 | +12.3 | +10.8 |
| `confluence_gte_70` | 2 | R_REPEATER | 4.1% | 50.0% | 50.0% | 0.0% | +10.9 | 44.60 | 44.60 | +21.5 | +6.0 |
| `tdi_rsi_gt_signal` | 28 | S_STRANGER | 57.1% | 28.6% | 32.1% | 17.9% | +0.7 | 1.14 | 2.02 | +11.8 | +9.6 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 49.0% | 33.3% | 37.5% | 16.7% | +1.8 | 1.46 | 1.94 | +11.8 | +10.2 |
| `ratio_le_2_and_asian_gte_30` | 37 | S_STRANGER | 75.5% | 18.9% | 27.0% | 16.2% | -1.4 | 0.76 | 1.75 | +9.5 | +7.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 21 | S_STRANGER | 42.9% | 33.3% | 38.1% | 14.3% | +1.0 | 1.17 | 1.75 | +13.1 | +8.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 49 | S_STRANGER | 100.0% | 18.4% | 24.5% | 16.3% | -1.2 | 0.76 | 1.96 | +9.2 | +8.7 |
| `feature_stale_hod_exhaustion_reject` | 49 | S_STRANGER | 100.0% | 18.4% | 24.5% | 16.3% | -1.2 | 0.76 | 1.96 | +9.2 | +8.7 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 18.4% | 11.1% | 22.2% | 0.0% | -3.0 | 0.30 | 1.05 | +4.1 | +6.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 6.1% | 33.3% | 33.3% | 0.0% | -1.0 | 0.77 | 1.54 | +7.1 | +6.8 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=25.0% Avg=+7.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 36.4% | +2.5 | 1.40 | 3.28 | +21.7 | +12.7 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 36.4% | +2.5 | 1.40 | 3.28 | +21.7 | +12.7 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 36.4% | +2.5 | 1.40 | 3.28 | +21.7 | +12.7 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 36.4% | +2.5 | 1.40 | 3.28 | +21.7 | +12.7 |
| `asian_range_gte_30` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 50.0% | +4.9 | 1.71 | 4.27 | +28.2 | +13.6 |
| `confluence_gte_60` | 7 | S_STRANGER | 63.6% | 14.3% | 14.3% | 42.9% | +5.4 | 1.76 | 8.80 | +27.8 | +10.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 50.0% | -2.8 | 0.39 | 0.77 | +20.1 | +14.6 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 50.0% | +7.5 | 2.73 | 6.82 | +28.2 | +11.8 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 50.0% | +4.9 | 1.71 | 4.27 | +28.2 | +13.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 50.0% | -2.8 | 0.39 | 0.77 | +20.1 | +14.6 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -2.0 | 0.00 | 0.00 | +0.0 | +16.2 |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 36.4% | +2.5 | 1.40 | 3.28 | +21.7 | +12.7 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 90.9% | 20.0% | 30.0% | 40.0% | +3.3 | 1.53 | 3.05 | +23.5 | +12.6 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -12.0 | 0.00 | 0.00 | +2.5 | +19.2 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 50.0% | +21.7 | 12.59 | 12.59 | +32.0 | +14.4 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=20.0% Avg=-3.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 9.1% | -3.6 | 0.62 | 1.64 | +11.8 | +10.4 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 54.5% | 0.0% | 16.7% | 0.0% | -8.8 | 0.07 | 0.36 | +5.2 | +8.4 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 63.6% | 0.0% | 14.3% | 0.0% | -9.0 | 0.06 | 0.37 | +4.9 | +8.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 90.9% | 20.0% | 30.0% | 10.0% | -3.0 | 0.68 | 1.59 | +12.7 | +10.4 |
| `asian_range_gte_30` | 5 | S_STRANGER | 45.5% | 0.0% | 20.0% | 0.0% | -8.7 | 0.09 | 0.35 | +4.9 | +8.1 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 9.1% | -3.6 | 0.62 | 1.64 | +11.8 | +10.4 |
| `confluence_gte_70` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 0.0% | -2.6 | 0.59 | 1.19 | +12.4 | +10.6 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 25.0% | +8.8 | 2.45 | 2.45 | +21.4 | +12.8 |
| `tdi_rsi_gte_50` | 2 | R_RUNNER | 18.2% | 100.0% | 100.0% | 50.0% | +29.8 | 999.00 | 999.00 | +40.1 | +12.2 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 36.4% | 0.0% | 25.0% | 0.0% | -8.3 | 0.11 | 0.33 | +5.5 | +7.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -14.0 | 0.00 | 0.00 | +2.7 | +16.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 90.9% | 20.0% | 30.0% | 10.0% | -3.0 | 0.68 | 1.59 | +12.7 | +10.4 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 9.1% | -3.6 | 0.62 | 1.64 | +11.8 | +10.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -9.4 | 0.00 | 0.00 | +4.0 | +11.0 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-15.9; validation N=4 Fav=50.0% Avg=+4.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | -6.7 | 0.34 | 1.51 | +9.3 | +12.1 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 20.0% | 20.0% | 0.0% | -5.3 | 0.41 | 1.66 | +10.2 | +11.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 90.9% | 20.0% | 20.0% | 0.0% | -5.3 | 0.41 | 1.66 | +10.2 | +11.1 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | -6.7 | 0.34 | 1.51 | +9.3 | +12.1 |
| `asian_range_gte_30` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 0.0% | -5.8 | 0.42 | 1.46 | +10.7 | +11.2 |
| `confluence_gte_60` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 0.0% | -4.6 | 0.35 | 1.39 | +9.4 | +11.9 |
| `confluence_gte_70` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -10.8 | 0.00 | 0.00 | +2.8 | +15.8 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 0.0% | -5.6 | 0.42 | 1.48 | +10.5 | +14.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 0.0% | -5.6 | 0.42 | 1.48 | +10.5 | +14.2 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 0.0% | -5.8 | 0.42 | 1.46 | +10.7 | +11.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 0.0% | -4.1 | 0.56 | 1.41 | +12.7 | +13.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | -6.7 | 0.34 | 1.51 | +9.3 | +12.1 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | -6.7 | 0.34 | 1.51 | +9.3 | +12.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=1 Fav=0.0% Avg=-16.5; out_of_sample N=4 Fav=25.0% Avg=-11.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -10.0 | 0.12 | 0.49 | +6.9 | +5.8 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 40.0% | -12.5 | 0.07 | 0.20 | +7.5 | +2.7 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 54.5% | 16.7% | 16.7% | 33.3% | -11.7 | 0.06 | 0.24 | +6.7 | +2.9 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -10.0 | 0.12 | 0.49 | +6.9 | +5.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -10.0 | 0.12 | 0.49 | +6.9 | +5.8 |
| `confluence_gte_70` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 50.0% | -7.1 | 0.13 | 0.27 | +9.1 | +3.0 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 50.0% | +1.8 | 5.50 | 5.50 | +10.1 | +2.9 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -0.8 | 0.00 | 0.00 | +7.4 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -10.0 | 0.12 | 0.49 | +6.9 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -10.0 | 0.12 | 0.49 | +6.9 | +5.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=22 Fav=22.7% Avg=-0.9; validation N=12 Fav=16.7% Avg=-3.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 39 | S_STRANGER | 100.0% | 17.9% | 20.5% | 20.5% | -4.6 | 0.35 | 1.19 | +7.3 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 38.5% | 13.3% | 20.0% | 26.7% | -2.4 | 0.60 | 2.00 | +8.9 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 53.8% | 19.0% | 23.8% | 19.0% | -3.1 | 0.49 | 1.38 | +7.5 | +6.0 |
| `stop_hunt_le_90` | 35 | S_STRANGER | 89.7% | 20.0% | 22.9% | 20.0% | -1.8 | 0.61 | 1.83 | +7.6 | +5.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 22 | S_STRANGER | 56.4% | 18.2% | 22.7% | 27.3% | -5.2 | 0.42 | 1.17 | +8.0 | +5.0 |
| `confluence_gte_70` | 1 | S_STRANGER | 2.6% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +10.9 | +8.6 |
| `tdi_rsi_gt_signal` | 32 | S_STRANGER | 82.1% | 15.6% | 18.8% | 18.8% | -4.8 | 0.32 | 1.17 | +7.3 | +5.3 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 41.0% | 12.5% | 12.5% | 6.2% | -2.3 | 0.19 | 1.24 | +7.2 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 34 | S_STRANGER | 87.2% | 20.6% | 23.5% | 23.5% | -1.9 | 0.61 | 1.67 | +7.9 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 39 | S_STRANGER | 100.0% | 17.9% | 20.5% | 20.5% | -4.6 | 0.35 | 1.19 | +7.3 | +5.3 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 12.8% | 0.0% | 0.0% | 0.0% | -0.7 | 0.00 | 0.00 | +3.4 | +2.5 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -0.6 | 0.00 | 0.00 | +4.1 | +1.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=66.7% Avg=+3.6; out_of_sample N=5 Fav=40.0% Avg=+5.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 17.9% | 17.9% | 28.6% | -1.0 | 0.72 | 2.61 | +6.7 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 35.7% | 0.0% | 0.0% | 30.0% | -3.8 | 0.00 | 0.00 | +4.4 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 60.7% | 5.9% | 5.9% | 23.5% | -3.9 | 0.11 | 1.28 | +4.6 | +5.2 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 92.9% | 11.5% | 11.5% | 26.9% | -2.2 | 0.41 | 2.49 | +5.4 | +4.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 22 | S_STRANGER | 78.6% | 22.7% | 22.7% | 31.8% | +0.1 | 1.05 | 2.72 | +7.6 | +4.5 |
| `confluence_gte_70` | 8 | R_REPEATER | 28.6% | 50.0% | 50.0% | 37.5% | +4.8 | 4.36 | 3.27 | +9.3 | +5.6 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 57.1% | 25.0% | 25.0% | 18.8% | +1.1 | 1.41 | 3.87 | +7.4 | +4.8 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 46.4% | 23.1% | 23.1% | 15.4% | +0.6 | 1.29 | 3.87 | +6.4 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 17.9% | 17.9% | 28.6% | -1.0 | 0.72 | 2.61 | +6.7 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 17.9% | 17.9% | 28.6% | -1.0 | 0.72 | 2.61 | +6.7 | +4.6 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 10.7% | 0.0% | 0.0% | 33.3% | -2.5 | 0.00 | 0.00 | +5.2 | +4.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +3.0 | +5.8 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=33.3% Avg=+1.0; out_of_sample N=2 Fav=0.0% Avg=-1.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 17.9% | 17.9% | 21.4% | -3.8 | 0.43 | 1.65 | +8.5 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 39.3% | 27.3% | 27.3% | 9.1% | +0.5 | 1.12 | 2.60 | +8.8 | +8.5 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 57.1% | 25.0% | 25.0% | 12.5% | -0.9 | 0.83 | 2.28 | +9.5 | +9.7 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 96.4% | 14.8% | 14.8% | 18.5% | -4.5 | 0.36 | 1.71 | +8.3 | +9.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 22 | S_STRANGER | 78.6% | 13.6% | 13.6% | 18.2% | -5.8 | 0.25 | 1.32 | +6.9 | +9.8 |
| `confluence_gte_70` | 9 | S_STRANGER | 32.1% | 22.2% | 22.2% | 22.2% | -5.2 | 0.38 | 1.14 | +8.5 | +10.3 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 21.4% | 16.7% | 16.7% | 16.7% | -4.8 | 0.38 | 1.91 | +7.5 | +11.4 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 71.4% | 20.0% | 20.0% | 10.0% | -2.3 | 0.60 | 2.23 | +9.0 | +9.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 17.9% | 17.9% | 21.4% | -3.8 | 0.43 | 1.65 | +8.5 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 17.9% | 17.9% | 21.4% | -3.8 | 0.43 | 1.65 | +8.5 | +8.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=22.2% Avg=-0.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 29.4% | 17.6% | -2.6 | 0.68 | 1.50 | +12.0 | +12.0 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 76.5% | 15.4% | 30.8% | 23.1% | -2.7 | 0.71 | 1.41 | +12.4 | +13.1 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 94.1% | 18.8% | 31.2% | 18.8% | -2.2 | 0.73 | 1.46 | +12.3 | +11.9 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 17.6% | 29.4% | 17.6% | -2.6 | 0.68 | 1.50 | +12.0 | +12.0 |
| `asian_range_gte_30` | 10 | S_STRANGER | 58.8% | 20.0% | 30.0% | 30.0% | -5.3 | 0.51 | 1.02 | +12.4 | +14.4 |
| `confluence_gte_60` | 9 | S_STRANGER | 52.9% | 22.2% | 33.3% | 22.2% | -0.0 | 1.00 | 1.66 | +12.5 | +10.5 |
| `confluence_gte_70` | 1 | R_RUNNER | 5.9% | 100.0% | 100.0% | 100.0% | +24.9 | 999.00 | 999.00 | +29.2 | +0.1 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 52.9% | 11.1% | 22.2% | 11.1% | -5.4 | 0.53 | 1.84 | +14.3 | +14.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 35.3% | 0.0% | 0.0% | 0.0% | -16.8 | 0.00 | 0.00 | +9.7 | +20.6 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 58.8% | 20.0% | 30.0% | 30.0% | -5.3 | 0.51 | 1.02 | +12.4 | +14.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 29.4% | 20.0% | 20.0% | 20.0% | -11.6 | 0.30 | 1.20 | +13.6 | +19.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 17.6% | 29.4% | 17.6% | -2.6 | 0.68 | 1.50 | +12.0 | +12.0 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 17.6% | 29.4% | 17.6% | -2.6 | 0.68 | 1.50 | +12.0 | +12.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=12 Fav=33.3% Avg=+0.1; out_of_sample N=4 Fav=25.0% Avg=+7.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 40 | S_STRANGER | 100.0% | 17.5% | 20.0% | 20.0% | -6.5 | 0.32 | 1.02 | +9.9 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 37 | S_STRANGER | 92.5% | 18.9% | 21.6% | 21.6% | -5.7 | 0.36 | 1.04 | +10.5 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 40 | S_STRANGER | 100.0% | 17.5% | 20.0% | 20.0% | -6.5 | 0.32 | 1.02 | +9.9 | +6.6 |
| `stop_hunt_le_90` | 38 | S_STRANGER | 95.0% | 18.4% | 21.1% | 18.4% | -5.8 | 0.35 | 1.10 | +9.8 | +6.8 |
| `asian_range_gte_30` | 26 | S_STRANGER | 65.0% | 3.8% | 7.7% | 19.2% | -10.8 | 0.13 | 1.25 | +7.9 | +6.0 |
| `confluence_gte_60` | 40 | S_STRANGER | 100.0% | 17.5% | 20.0% | 20.0% | -6.5 | 0.32 | 1.02 | +9.9 | +6.6 |
| `confluence_gte_70` | 40 | S_STRANGER | 100.0% | 17.5% | 20.0% | 20.0% | -6.5 | 0.32 | 1.02 | +9.9 | +6.6 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 45.0% | 11.1% | 16.7% | 16.7% | -14.8 | 0.12 | 0.47 | +9.4 | +7.6 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 40.0% | 31.2% | 31.2% | 25.0% | +1.9 | 1.53 | 2.44 | +15.2 | +8.0 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 57.5% | 4.3% | 8.7% | 21.7% | -10.1 | 0.15 | 1.26 | +8.5 | +6.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 27.5% | 0.0% | 9.1% | 18.2% | -19.4 | 0.04 | 0.36 | +7.9 | +7.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 38 | S_STRANGER | 95.0% | 18.4% | 21.1% | 18.4% | -5.8 | 0.35 | 1.10 | +9.8 | +6.8 |
| `feature_stale_hod_exhaustion_reject` | 40 | S_STRANGER | 100.0% | 17.5% | 20.0% | 20.0% | -6.5 | 0.32 | 1.02 | +9.9 | +6.6 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +3.3 | +4.1 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=12.5% Avg=+0.2; validation N=1 Fav=100.0% Avg=+38.2; out_of_sample N=6 Fav=33.3% Avg=+0.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 17.2% | -0.3 | 0.93 | 4.29 | +9.9 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 28 | S_STRANGER | 96.6% | 17.9% | 17.9% | 17.9% | +0.3 | 1.08 | 4.75 | +10.1 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 28 | S_STRANGER | 96.6% | 17.9% | 17.9% | 17.9% | +0.3 | 1.08 | 4.75 | +10.1 | +6.1 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 17.2% | -0.3 | 0.93 | 4.29 | +9.9 | +7.3 |
| `asian_range_gte_30` | 20 | S_STRANGER | 69.0% | 20.0% | 20.0% | 20.0% | +0.6 | 1.17 | 4.38 | +10.8 | +5.9 |
| `confluence_gte_60` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 17.2% | -0.3 | 0.93 | 4.29 | +9.9 | +7.3 |
| `confluence_gte_70` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 17.2% | -0.3 | 0.93 | 4.29 | +9.9 | +7.3 |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 79.3% | 21.7% | 21.7% | 17.4% | +0.9 | 1.25 | 4.50 | +11.4 | +7.7 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 48.3% | 14.3% | 14.3% | 7.1% | -1.7 | 0.65 | 3.89 | +9.9 | +10.4 |
| `ratio_le_2_and_asian_gte_30` | 20 | S_STRANGER | 69.0% | 20.0% | 20.0% | 20.0% | +0.6 | 1.17 | 4.38 | +10.8 | +5.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 51.7% | 26.7% | 26.7% | 20.0% | +2.7 | 1.87 | 5.13 | +12.9 | +6.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 17.2% | -0.3 | 0.93 | 4.29 | +9.9 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 17.2% | -0.3 | 0.93 | 4.29 | +9.9 | +7.3 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 17.2% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +4.9 | +3.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.4% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +9.6 | +1.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=50.0% Avg=-1.1; validation N=6 Fav=16.7% Avg=+0.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 20.7% | -2.2 | 0.67 | 2.80 | +11.0 | +11.0 |
| `hunt_to_ar_ratio_le_2_0` | 28 | S_STRANGER | 96.6% | 14.3% | 14.3% | 21.4% | -2.8 | 0.58 | 3.06 | +10.7 | +11.2 |
| `hunt_to_ar_ratio_le_2_5` | 28 | S_STRANGER | 96.6% | 14.3% | 14.3% | 21.4% | -2.8 | 0.58 | 3.06 | +10.7 | +11.2 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 20.7% | -2.2 | 0.67 | 2.80 | +11.0 | +11.0 |
| `asian_range_gte_30` | 25 | S_STRANGER | 86.2% | 8.0% | 8.0% | 16.0% | -7.1 | 0.06 | 0.63 | +6.3 | +12.2 |
| `confluence_gte_60` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 20.7% | -2.2 | 0.67 | 2.80 | +11.0 | +11.0 |
| `confluence_gte_70` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 20.7% | -2.2 | 0.67 | 2.80 | +11.0 | +11.0 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 34.5% | 30.0% | 30.0% | 40.0% | -0.1 | 0.98 | 1.64 | +14.0 | +8.8 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 51.7% | 20.0% | 20.0% | 20.0% | -3.2 | 0.50 | 1.67 | +10.7 | +9.7 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 86.2% | 8.0% | 8.0% | 16.0% | -7.1 | 0.06 | 0.63 | +6.3 | +12.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 31.0% | 22.2% | 22.2% | 33.3% | -3.0 | 0.31 | 0.77 | +10.5 | +9.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 20.7% | -2.2 | 0.67 | 2.80 | +11.0 | +11.0 |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 20.7% | -2.2 | 0.67 | 2.80 | +11.0 | +11.0 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 6.9% | 0.0% | 0.0% | 0.0% | -8.1 | 0.00 | 0.00 | +0.4 | +8.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.4% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +0.7 | +6.1 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-1.5; validation N=4 Fav=50.0% Avg=+10.5; out_of_sample N=2 Fav=0.0% Avg=-5.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 33.3% | 8.3% | -1.7 | 0.73 | 1.45 | +11.0 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 16.7% | 33.3% | 8.3% | -1.7 | 0.73 | 1.45 | +11.0 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 16.7% | 33.3% | 8.3% | -1.7 | 0.73 | 1.45 | +11.0 | +5.4 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 33.3% | 8.3% | -1.7 | 0.73 | 1.45 | +11.0 | +5.4 |
| `asian_range_gte_30` | 10 | S_STRANGER | 83.3% | 20.0% | 40.0% | 10.0% | -1.5 | 0.78 | 1.18 | +13.0 | +5.5 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 16.7% | 33.3% | 8.3% | -1.7 | 0.73 | 1.45 | +11.0 | +5.4 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 16.7% | 33.3% | 8.3% | -1.7 | 0.73 | 1.45 | +11.0 | +5.4 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 75.0% | 11.1% | 33.3% | 0.0% | -1.6 | 0.39 | 0.78 | +5.0 | +3.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 14.3% | +4.4 | 2.85 | 7.12 | +15.0 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 83.3% | 20.0% | 40.0% | 10.0% | -1.5 | 0.78 | 1.18 | +13.0 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 58.3% | 14.3% | 42.9% | 0.0% | -1.3 | 0.51 | 0.67 | +6.1 | +3.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 16.7% | 33.3% | 8.3% | -1.7 | 0.73 | 1.45 | +11.0 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 33.3% | 8.3% | -1.7 | 0.73 | 1.45 | +11.0 | +5.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=14 Fav=21.4% Avg=+0.6; validation N=13 Fav=15.4% Avg=-3.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 16.7% | 16.7% | 20.0% | -1.9 | 0.54 | 2.59 | +5.4 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 43.3% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +2.1 | +8.0 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 53.3% | 6.2% | 6.2% | 6.2% | -4.0 | 0.17 | 2.51 | +3.3 | +7.3 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 90.0% | 18.5% | 18.5% | 18.5% | -1.4 | 0.63 | 2.76 | +5.6 | +6.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 20.0% | 16.7% | 16.7% | 16.7% | -2.7 | 0.52 | 2.59 | +5.7 | +8.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 50.0% | 13.3% | 13.3% | 13.3% | -3.2 | 0.39 | 2.51 | +4.3 | +7.4 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 63.3% | 5.3% | 5.3% | 5.3% | -3.9 | 0.19 | 3.37 | +3.7 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 100.0% | 16.7% | 16.7% | 20.0% | -1.9 | 0.54 | 2.59 | +5.4 | +6.2 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 16.7% | 16.7% | 20.0% | -1.9 | 0.54 | 2.59 | +5.4 | +6.2 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 20.0% | 16.7% | 16.7% | 16.7% | -0.9 | 0.72 | 3.58 | +4.7 | +4.4 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -4.2 | 0.00 | 0.00 | +1.8 | +5.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-1.9; validation N=12 Fav=41.7% Avg=+6.1; out_of_sample N=6 Fav=0.0% Avg=-11.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 16.7% | 20.0% | 20.0% | -2.2 | 0.65 | 2.16 | +11.2 | +7.9 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 86.7% | 15.4% | 19.2% | 11.5% | -2.7 | 0.62 | 2.47 | +10.7 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 86.7% | 15.4% | 19.2% | 11.5% | -2.7 | 0.62 | 2.47 | +10.7 | +8.6 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 96.7% | 13.8% | 17.2% | 20.7% | -2.5 | 0.62 | 2.47 | +11.3 | +8.2 |
| `asian_range_gte_30` | 21 | S_STRANGER | 70.0% | 14.3% | 14.3% | 4.8% | -5.3 | 0.38 | 2.26 | +9.6 | +9.8 |
| `confluence_gte_60` | 30 | S_STRANGER | 100.0% | 16.7% | 20.0% | 20.0% | -2.2 | 0.65 | 2.16 | +11.2 | +7.9 |
| `confluence_gte_70` | 30 | S_STRANGER | 100.0% | 16.7% | 20.0% | 20.0% | -2.2 | 0.65 | 2.16 | +11.2 | +7.9 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 50.0% | 6.7% | 6.7% | 6.7% | -7.6 | 0.05 | 0.60 | +5.3 | +8.3 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 63.3% | 26.3% | 26.3% | 10.5% | -0.0 | 1.00 | 2.80 | +13.1 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 70.0% | 14.3% | 14.3% | 4.8% | -5.3 | 0.38 | 2.26 | +9.6 | +9.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 36.7% | 0.0% | 0.0% | 0.0% | -10.3 | 0.00 | 0.00 | +5.2 | +10.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 96.7% | 13.8% | 17.2% | 20.7% | -2.5 | 0.62 | 2.47 | +11.3 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 16.7% | 20.0% | 20.0% | -2.2 | 0.65 | 2.16 | +11.2 | +7.9 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +11.5 | +12.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +11.5 | +12.4 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-16.7; validation N=5 Fav=40.0% Avg=+10.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -2.5 | 0.65 | 3.25 | +7.6 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -18.5 | 0.00 | 0.00 | +3.7 | +9.2 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -13.1 | 0.00 | 0.00 | +3.8 | +7.4 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -2.5 | 0.65 | 3.25 | +7.6 | +5.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -1.0 | 0.00 | 0.00 | +4.8 | +2.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 28.6% | +2.8 | 1.53 | 3.84 | +10.1 | +4.7 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -3.3 | 0.00 | 0.00 | +4.4 | +5.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -2.5 | 0.65 | 3.25 | +7.6 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -2.5 | 0.65 | 3.25 | +7.6 | +5.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+5.7; validation N=1 Fav=0.0% Avg=-3.3; out_of_sample N=2 Fav=0.0% Avg=-28.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 20.8% | -5.6 | 0.36 | 1.69 | +7.0 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 20.8% | 0.0% | 0.0% | 20.0% | -5.4 | 0.00 | 0.00 | +4.2 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 41.7% | 0.0% | 0.0% | 10.0% | -5.4 | 0.00 | 0.00 | +3.1 | +6.7 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 91.7% | 9.1% | 9.1% | 13.6% | -7.8 | 0.18 | 1.73 | +5.3 | +6.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 20.8% | -5.6 | 0.36 | 1.69 | +7.0 | +6.3 |
| `confluence_gte_70` | 7 | S_STRANGER | 29.2% | 28.6% | 28.6% | 28.6% | -5.3 | 0.50 | 1.24 | +9.4 | +5.2 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 79.2% | 10.5% | 10.5% | 15.8% | -7.6 | 0.16 | 1.31 | +5.8 | +6.9 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +2.4 | +10.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 91.7% | 9.1% | 9.1% | 13.6% | -7.8 | 0.18 | 1.73 | +5.3 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 20.8% | -5.6 | 0.36 | 1.69 | +7.0 | +6.3 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 8.3% | 50.0% | 50.0% | 50.0% | +8.6 | 3.90 | 3.90 | +12.7 | +6.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +0.2 | +7.1 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=50.0% Avg=-7.1; out_of_sample N=2 Fav=0.0% Avg=-15.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 16.7% | 20.8% | 16.7% | -21.1 | 0.12 | 0.47 | +7.2 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 75.0% | 22.2% | 27.8% | 22.2% | -12.1 | 0.25 | 0.65 | +8.4 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 87.5% | 19.0% | 23.8% | 19.0% | -16.4 | 0.17 | 0.55 | +7.5 | +4.5 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 91.7% | 18.2% | 22.7% | 18.2% | -16.7 | 0.16 | 0.56 | +7.7 | +4.5 |
| `asian_range_gte_30` | 15 | S_STRANGER | 62.5% | 26.7% | 33.3% | 26.7% | -13.5 | 0.26 | 0.53 | +9.4 | +4.4 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 16.7% | 20.8% | 16.7% | -21.1 | 0.12 | 0.47 | +7.2 | +4.4 |
| `confluence_gte_70` | 17 | S_STRANGER | 70.8% | 17.6% | 17.6% | 17.6% | -27.0 | 0.08 | 0.37 | +7.7 | +4.1 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 66.7% | 18.8% | 18.8% | 18.8% | -16.9 | 0.14 | 0.62 | +6.8 | +4.3 |
| `tdi_rsi_gte_50` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 58.3% | 28.6% | 35.7% | 28.6% | -10.7 | 0.32 | 0.58 | +10.1 | +4.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 33.3% | 37.5% | 37.5% | 37.5% | -9.2 | 0.38 | 0.63 | +10.8 | +4.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 91.7% | 18.2% | 22.7% | 18.2% | -16.7 | 0.16 | 0.56 | +7.7 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 16.7% | 20.8% | 16.7% | -21.1 | 0.12 | 0.47 | +7.2 | +4.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=22.2% Avg=-0.7; validation N=12 Fav=25.0% Avg=+2.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 50 | S_STRANGER | 100.0% | 16.0% | 18.0% | 16.0% | -1.7 | 0.75 | 3.16 | +9.9 | +8.1 |
| `hunt_to_ar_ratio_le_2_0` | 44 | S_STRANGER | 88.0% | 15.9% | 18.2% | 18.2% | -1.5 | 0.79 | 3.26 | +10.4 | +8.5 |
| `hunt_to_ar_ratio_le_2_5` | 48 | S_STRANGER | 96.0% | 16.7% | 18.8% | 16.7% | -1.5 | 0.77 | 3.09 | +10.1 | +8.1 |
| `stop_hunt_le_90` | 49 | S_STRANGER | 98.0% | 16.3% | 18.4% | 16.3% | -1.7 | 0.75 | 3.09 | +10.0 | +8.2 |
| `asian_range_gte_30` | 36 | S_STRANGER | 72.0% | 19.4% | 22.2% | 22.2% | +0.0 | 1.01 | 3.14 | +12.0 | +8.2 |
| `confluence_gte_60` | 21 | S_STRANGER | 42.0% | 23.8% | 23.8% | 19.0% | +1.0 | 1.18 | 3.54 | +10.8 | +6.8 |
| `confluence_gte_70` | 3 | S_STRANGER | 6.0% | 33.3% | 33.3% | 0.0% | -3.9 | 0.21 | 0.43 | +5.5 | +8.5 |
| `tdi_rsi_gt_signal` | 28 | S_STRANGER | 56.0% | 10.7% | 10.7% | 7.1% | -3.4 | 0.53 | 4.28 | +8.6 | +8.6 |
| `tdi_rsi_gte_50` | 28 | S_STRANGER | 56.0% | 21.4% | 21.4% | 17.9% | +2.7 | 1.61 | 5.65 | +13.9 | +10.0 |
| `ratio_le_2_and_asian_gte_30` | 36 | S_STRANGER | 72.0% | 19.4% | 22.2% | 22.2% | +0.0 | 1.01 | 3.14 | +12.0 | +8.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 19 | S_STRANGER | 38.0% | 15.8% | 15.8% | 10.5% | -1.3 | 0.81 | 4.06 | +11.1 | +7.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 48 | S_STRANGER | 96.0% | 16.7% | 18.8% | 16.7% | -1.7 | 0.75 | 3.02 | +10.1 | +8.3 |
| `feature_stale_hod_exhaustion_reject` | 50 | S_STRANGER | 100.0% | 16.0% | 18.0% | 16.0% | -1.7 | 0.75 | 3.16 | +9.9 | +8.1 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -4.2 | 0.00 | 0.00 | +1.2 | +5.9 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 6.0% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +1.3 | +7.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=0.0% Avg=-2.4; out_of_sample N=3 Fav=66.7% Avg=+6.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 15.4% | 23.1% | 30.8% | -2.8 | 0.52 | 1.29 | +10.8 | +4.5 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 88.5% | 13.0% | 21.7% | 30.4% | -1.9 | 0.61 | 1.58 | +11.2 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 100.0% | 15.4% | 23.1% | 30.8% | -2.8 | 0.52 | 1.29 | +10.8 | +4.5 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 15.4% | 23.1% | 30.8% | -2.8 | 0.52 | 1.29 | +10.8 | +4.5 |
| `asian_range_gte_30` | 18 | S_STRANGER | 69.2% | 16.7% | 27.8% | 38.9% | -2.5 | 0.59 | 1.05 | +12.7 | +4.3 |
| `confluence_gte_60` | 26 | S_STRANGER | 100.0% | 15.4% | 23.1% | 30.8% | -2.8 | 0.52 | 1.29 | +10.8 | +4.5 |
| `confluence_gte_70` | 16 | S_STRANGER | 61.5% | 18.8% | 25.0% | 31.2% | -3.8 | 0.51 | 1.15 | +11.9 | +4.0 |
| `tdi_rsi_gt_signal` | 22 | S_STRANGER | 84.6% | 13.6% | 22.7% | 27.3% | -2.8 | 0.40 | 1.03 | +9.2 | +4.7 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 23.1% | 33.3% | 33.3% | 16.7% | +2.1 | 2.35 | 4.70 | +12.2 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 65.4% | 11.8% | 23.5% | 35.3% | -3.2 | 0.50 | 1.12 | +12.6 | +4.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 53.8% | 7.1% | 21.4% | 28.6% | -3.9 | 0.24 | 0.63 | +10.0 | +4.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 15.4% | 23.1% | 30.8% | -2.8 | 0.52 | 1.29 | +10.8 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 15.4% | 23.1% | 30.8% | -2.8 | 0.52 | 1.29 | +10.8 | +4.5 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 15.4% | 0.0% | 0.0% | 25.0% | -1.3 | 0.00 | 0.00 | +7.9 | +3.4 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+1.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 30.8% | -3.9 | 0.44 | 1.99 | +11.6 | +12.0 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 66.7% | +5.6 | 8.02 | 8.02 | +15.3 | +10.4 |
| `hunt_to_ar_ratio_le_2_5` | 4 | R_REPEATER | 30.8% | 50.0% | 50.0% | 75.0% | +9.5 | 16.85 | 8.43 | +17.9 | +9.6 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 30.8% | -3.9 | 0.44 | 1.99 | +11.6 | +12.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 53.8% | 14.3% | 14.3% | 28.6% | -8.2 | 0.25 | 1.26 | +11.1 | +16.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -25.8 | 0.00 | 0.00 | +13.4 | +28.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 69.2% | 11.1% | 11.1% | 33.3% | -3.9 | 0.38 | 2.26 | +12.2 | +11.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 61.5% | 12.5% | 12.5% | 37.5% | -4.1 | 0.37 | 1.86 | +12.8 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 84.6% | 18.2% | 18.2% | 36.4% | -2.2 | 0.62 | 2.18 | +11.9 | +11.2 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 40.0% | +1.1 | 1.36 | 4.08 | +10.2 | +17.9 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 40.0% | -2.9 | 0.60 | 1.79 | +14.1 | +14.2 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+6.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=25.0% Avg=-1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 15.4% | -5.3 | 0.24 | 0.71 | +8.3 | +8.6 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 46.2% | 33.3% | 50.0% | 16.7% | +0.8 | 1.29 | 1.29 | +8.6 | +5.8 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 69.2% | 22.2% | 33.3% | 11.1% | -3.1 | 0.43 | 0.86 | +6.9 | +7.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 84.6% | 18.2% | 27.3% | 18.2% | -2.7 | 0.41 | 0.97 | +6.8 | +6.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 76.9% | 20.0% | 30.0% | 20.0% | -5.8 | 0.27 | 0.54 | +10.1 | +9.6 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -31.6 | 0.00 | 0.00 | +7.2 | +31.8 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 46.2% | 33.3% | 33.3% | 16.7% | -7.7 | 0.27 | 0.55 | +13.3 | +13.6 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 46.2% | 33.3% | 33.3% | 16.7% | -7.7 | 0.27 | 0.55 | +13.3 | +13.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 76.9% | 20.0% | 30.0% | 20.0% | -2.1 | 0.50 | 1.00 | +6.9 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 15.4% | -5.3 | 0.24 | 0.71 | +8.3 | +8.6 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -7.7 | 0.00 | 0.00 | +16.2 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +26.3 | +7.6 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+32.2; validation N=2 Fav=50.0% Avg=-2.7; out_of_sample N=2 Fav=0.0% Avg=-0.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | S_STRANGER | 100.0% | 15.2% | 18.2% | 18.2% | -2.4 | 0.57 | 2.26 | +10.5 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 78.8% | 15.4% | 15.4% | 19.2% | -1.6 | 0.64 | 3.22 | +10.5 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 93.9% | 16.1% | 19.4% | 19.4% | -2.2 | 0.61 | 2.22 | +11.0 | +6.1 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 97.0% | 15.6% | 18.8% | 18.8% | -2.1 | 0.61 | 2.32 | +10.8 | +6.1 |
| `asian_range_gte_30` | 22 | S_STRANGER | 66.7% | 18.2% | 18.2% | 18.2% | -1.3 | 0.73 | 3.08 | +9.7 | +7.0 |
| `confluence_gte_60` | 29 | S_STRANGER | 87.9% | 13.8% | 17.2% | 17.2% | -3.4 | 0.42 | 1.76 | +9.4 | +6.5 |
| `confluence_gte_70` | 6 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -16.2 | 0.00 | 0.00 | +7.4 | +10.2 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 15.2% | 40.0% | 40.0% | 40.0% | +5.2 | 2.30 | 3.44 | +18.6 | +7.5 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 60.6% | 25.0% | 25.0% | 15.0% | +1.4 | 1.38 | 4.15 | +13.7 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 20 | S_STRANGER | 60.6% | 20.0% | 20.0% | 20.0% | -0.8 | 0.82 | 3.08 | +10.4 | +6.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | R_REPEATER | 9.1% | 66.7% | 66.7% | 66.7% | +9.0 | 2.43 | 1.22 | +25.4 | +10.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 97.0% | 15.6% | 18.8% | 18.8% | -2.1 | 0.61 | 2.32 | +10.8 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 33 | S_STRANGER | 100.0% | 15.2% | 18.2% | 18.2% | -2.4 | 0.57 | 2.26 | +10.5 | +6.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 12.1% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +10.0 | +6.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +11.8 | +5.3 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=14.3% Avg=+2.2; validation N=7 Fav=28.6% Avg=+4.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 35.0% | +2.3 | 2.81 | 11.24 | +10.0 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 2 | R_REPEATER | 10.0% | 50.0% | 50.0% | 50.0% | +14.4 | 13.57 | 13.57 | +22.3 | +4.1 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 30.0% | 16.7% | 16.7% | 50.0% | +4.5 | 7.43 | 22.29 | +12.3 | +3.1 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 95.0% | 15.8% | 15.8% | 36.8% | +2.5 | 2.90 | 10.63 | +10.3 | +4.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 35.0% | +2.3 | 2.81 | 11.24 | +10.0 | +4.4 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 35.0% | +2.3 | 2.81 | 11.24 | +10.0 | +4.4 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 80.0% | 18.8% | 18.8% | 37.5% | +3.2 | 3.50 | 10.51 | +11.0 | +4.3 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 70.0% | 21.4% | 21.4% | 28.6% | +3.5 | 3.10 | 9.29 | +11.1 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 85.0% | 17.6% | 17.6% | 29.4% | +2.8 | 2.88 | 10.55 | +10.7 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 35.0% | +2.3 | 2.81 | 11.24 | +10.0 | +4.4 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 25.0% | 0.0% | 0.0% | 60.0% | -0.5 | 0.00 | 0.00 | +7.0 | +2.9 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 15.0% | 0.0% | 0.0% | 33.3% | -0.9 | 0.00 | 0.00 | +6.1 | +3.2 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=25.0% Avg=+4.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 15.0% | 25.0% | 30.0% | -2.3 | 0.48 | 1.06 | +10.5 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 40.0% | 25.0% | 50.0% | 62.5% | +4.1 | 33.80 | 8.45 | +13.2 | +3.3 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 40.0% | 25.0% | 50.0% | 62.5% | +4.1 | 33.80 | 8.45 | +13.2 | +3.3 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 85.0% | 17.6% | 29.4% | 35.3% | -0.8 | 0.76 | 1.21 | +11.8 | +4.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 35.0% | 28.6% | 42.9% | 28.6% | -1.0 | 0.82 | 0.82 | +10.7 | +6.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 85.0% | 11.8% | 23.5% | 29.4% | -2.7 | 0.43 | 1.07 | +10.1 | +5.7 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 30.0% | 16.7% | 16.7% | 16.7% | -1.1 | 0.70 | 3.52 | +11.8 | +7.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -6.9 | 0.00 | 0.00 | +14.0 | +9.3 |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 85.0% | 17.6% | 29.4% | 35.3% | -0.6 | 0.80 | 1.27 | +11.2 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 15.0% | 25.0% | 30.0% | -2.3 | 0.48 | 1.06 | +10.5 | +6.7 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 35.0% | 0.0% | 28.6% | 14.3% | -1.4 | 0.54 | 1.08 | +9.5 | +4.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 15.0% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +9.0 | +6.9 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=22.2% Avg=+0.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -1.4 | 0.79 | 3.94 | +12.0 | +11.4 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 71.4% | 10.0% | 10.0% | 10.0% | -3.9 | 0.51 | 4.09 | +10.7 | +10.1 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -1.4 | 0.79 | 3.94 | +12.0 | +11.4 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 71.4% | 10.0% | 10.0% | 10.0% | -3.9 | 0.51 | 4.09 | +10.7 | +10.1 |
| `asian_range_gte_30` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 25.0% | -0.1 | 0.98 | 3.92 | +13.5 | +11.7 |
| `confluence_gte_60` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 14.3% | -3.4 | 0.63 | 3.15 | +14.4 | +10.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +3.4 | +22.0 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 22.2% | +0.5 | 1.06 | 3.17 | +16.3 | +14.0 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 57.1% | 12.5% | 12.5% | 12.5% | -2.6 | 0.67 | 4.00 | +12.6 | +10.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 50.0% | +16.1 | 15.64 | 15.64 | +23.6 | +17.7 |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 71.4% | 10.0% | 10.0% | 10.0% | -3.9 | 0.51 | 4.09 | +10.7 | +10.1 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -1.4 | 0.79 | 3.94 | +12.0 | +11.4 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 16.7% | -2.9 | 0.66 | 3.30 | +9.4 | +13.5 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 20.0% | -1.7 | 0.80 | 3.19 | +11.2 | +18.1 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+14.4; validation N=3 Fav=0.0% Avg=-4.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 14.3% | -3.5 | 0.49 | 1.78 | +8.3 | +9.6 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 14.3% | -3.5 | 0.49 | 1.78 | +8.3 | +9.6 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 14.3% | -3.5 | 0.49 | 1.78 | +8.3 | +9.6 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 14.3% | -3.5 | 0.49 | 1.78 | +8.3 | +9.6 |
| `asian_range_gte_30` | 10 | S_STRANGER | 71.4% | 20.0% | 30.0% | 20.0% | -2.7 | 0.64 | 1.48 | +10.5 | +11.5 |
| `confluence_gte_60` | 6 | S_STRANGER | 42.9% | 16.7% | 33.3% | 16.7% | -0.0 | 0.99 | 1.99 | +9.2 | +6.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 64.3% | 22.2% | 33.3% | 22.2% | -1.2 | 0.82 | 1.64 | +11.0 | +9.2 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 42.9% | 33.3% | 50.0% | 33.3% | +4.8 | 2.60 | 2.60 | +15.1 | +7.2 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 71.4% | 20.0% | 30.0% | 20.0% | -2.7 | 0.64 | 1.48 | +10.5 | +11.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 50.0% | 28.6% | 42.9% | 28.6% | -0.4 | 0.94 | 1.25 | +13.6 | +10.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 14.3% | -3.5 | 0.49 | 1.78 | +8.3 | +9.6 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 14.3% | -3.5 | 0.49 | 1.78 | +8.3 | +9.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L2|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L2|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=20.0% Avg=-1.1; out_of_sample N=7 Fav=14.3% Avg=-6.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -4.4 | 0.23 | 0.68 | +11.0 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 85.7% | 16.7% | 25.0% | 25.0% | -4.1 | 0.27 | 0.62 | +11.7 | +8.9 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 15.4% | 23.1% | 23.1% | -4.1 | 0.25 | 0.68 | +11.6 | +8.6 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 92.9% | 15.4% | 23.1% | 23.1% | -4.1 | 0.25 | 0.68 | +11.6 | +8.6 |
| `asian_range_gte_30` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 14.3% | -8.3 | 0.00 | 0.00 | +13.0 | +12.4 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -4.4 | 0.23 | 0.68 | +11.0 | +8.8 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -4.4 | 0.23 | 0.68 | +11.0 | +8.8 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 33.3% | -5.3 | 0.00 | 0.00 | +12.1 | +8.4 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 0.0% | -8.7 | 0.00 | 0.00 | +13.7 | +13.0 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 42.9% | 0.0% | 0.0% | 16.7% | -8.3 | 0.00 | 0.00 | +14.7 | +12.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -8.0 | 0.00 | 0.00 | +13.5 | +12.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 92.9% | 15.4% | 23.1% | 23.1% | -4.1 | 0.25 | 0.68 | +11.6 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 21.4% | -4.4 | 0.23 | 0.68 | +11.0 | +8.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=25.0% Avg=-1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -4.7 | 0.31 | 1.83 | +7.8 | +10.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 20.0% | -3.4 | 0.46 | 1.85 | +8.5 | +10.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 78.6% | 18.2% | 18.2% | 18.2% | -4.3 | 0.38 | 1.71 | +9.1 | +10.5 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -4.7 | 0.31 | 1.83 | +7.8 | +10.6 |
| `asian_range_gte_30` | 8 | S_STRANGER | 57.1% | 25.0% | 25.0% | 25.0% | -1.8 | 0.67 | 2.00 | +9.7 | +9.4 |
| `confluence_gte_60` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +6.8 | +9.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -9.2 | 0.00 | 0.00 | +0.5 | +12.6 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 57.1% | 0.0% | 0.0% | 0.0% | -7.8 | 0.00 | 0.00 | +6.0 | +11.6 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 57.1% | 25.0% | 25.0% | 25.0% | -1.8 | 0.67 | 2.00 | +9.7 | +9.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -4.7 | 0.31 | 1.83 | +7.8 | +10.6 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -4.7 | 0.31 | 1.83 | +7.8 | +10.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+2.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 23.8% | -5.5 | 0.26 | 1.31 | +11.1 | +12.3 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 23.8% | -5.5 | 0.26 | 1.31 | +11.1 | +12.3 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 23.8% | -5.5 | 0.26 | 1.31 | +11.1 | +12.3 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 23.8% | -5.5 | 0.26 | 1.31 | +11.1 | +12.3 |
| `asian_range_gte_30` | 18 | S_STRANGER | 85.7% | 16.7% | 16.7% | 22.2% | -5.1 | 0.31 | 1.35 | +11.5 | +12.8 |
| `confluence_gte_60` | 19 | S_STRANGER | 90.5% | 10.5% | 10.5% | 26.3% | -5.2 | 0.27 | 1.92 | +10.5 | +12.9 |
| `confluence_gte_70` | 11 | S_STRANGER | 52.4% | 18.2% | 18.2% | 36.4% | -3.5 | 0.49 | 1.72 | +12.6 | +11.7 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 14.3% | 33.3% | 33.3% | 33.3% | +1.1 | 3.91 | 3.91 | +22.8 | +7.1 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 57.1% | 25.0% | 25.0% | 25.0% | -3.0 | 0.53 | 1.42 | +14.2 | +12.6 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 85.7% | 16.7% | 16.7% | 22.2% | -5.1 | 0.31 | 1.35 | +11.5 | +12.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 14.3% | 33.3% | 33.3% | 33.3% | +1.1 | 3.91 | 3.91 | +22.8 | +7.1 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -4.3 | 0.00 | 0.00 | +4.9 | +17.1 |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 23.8% | -5.5 | 0.26 | 1.31 | +11.1 | +12.3 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 14.3% | 14.3% | 23.8% | -5.5 | 0.26 | 1.31 | +11.1 | +12.3 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 33.3% | 28.6% | 28.6% | 42.9% | +2.7 | 2.04 | 4.07 | +15.1 | +10.1 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 19.0% | 50.0% | 50.0% | 50.0% | +7.8 | 6.28 | 6.28 | +18.9 | +7.4 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=42.9% Avg=-1.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 14.3% | 19.0% | 0.0% | -21.4 | 0.06 | 0.24 | +12.4 | +11.3 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 95.2% | 15.0% | 20.0% | 0.0% | -21.2 | 0.06 | 0.24 | +12.6 | +11.8 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 95.2% | 15.0% | 20.0% | 0.0% | -21.2 | 0.06 | 0.24 | +12.6 | +11.8 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 14.3% | 19.0% | 0.0% | -21.4 | 0.06 | 0.24 | +12.4 | +11.3 |
| `asian_range_gte_30` | 18 | S_STRANGER | 85.7% | 16.7% | 22.2% | 0.0% | -22.6 | 0.06 | 0.22 | +13.6 | +11.7 |
| `confluence_gte_60` | 11 | S_STRANGER | 52.4% | 27.3% | 27.3% | 0.0% | -15.3 | 0.10 | 0.28 | +16.5 | +13.5 |
| `confluence_gte_70` | 4 | S_STRANGER | 19.0% | 25.0% | 25.0% | 0.0% | -18.2 | 0.03 | 0.10 | +16.3 | +27.7 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 42.9% | 33.3% | 33.3% | 0.0% | -2.2 | 0.49 | 0.99 | +22.0 | +9.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 47.6% | 30.0% | 30.0% | 0.0% | -8.6 | 0.19 | 0.44 | +21.3 | +16.4 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 81.0% | 17.6% | 23.5% | 0.0% | -22.4 | 0.07 | 0.21 | +14.0 | +12.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 33.3% | 42.9% | 42.9% | 0.0% | -1.5 | 0.66 | 0.88 | +26.8 | +9.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 14.3% | 19.0% | 0.0% | -21.4 | 0.06 | 0.24 | +12.4 | +11.3 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 14.3% | 19.0% | 0.0% | -21.4 | 0.06 | 0.24 | +12.4 | +11.3 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 28.6% | 0.0% | 16.7% | 0.0% | -35.6 | 0.03 | 0.17 | +4.6 | +5.3 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 19.0% | 50.0% | 50.0% | 0.0% | +3.3 | 4.50 | 4.50 | +27.5 | +5.0 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+0.4; validation N=4 Fav=25.0% Avg=-2.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 20.0% | -2.8 | 0.30 | 1.10 | +7.1 | +8.6 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 80.0% | 16.7% | 16.7% | 16.7% | -3.6 | 0.25 | 1.26 | +7.5 | +8.3 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 80.0% | 16.7% | 16.7% | 16.7% | -3.6 | 0.25 | 1.26 | +7.5 | +8.3 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 93.3% | 14.3% | 14.3% | 21.4% | -3.2 | 0.24 | 1.32 | +7.2 | +8.8 |
| `asian_range_gte_30` | 13 | S_STRANGER | 86.7% | 15.4% | 23.1% | 23.1% | -3.0 | 0.32 | 0.95 | +7.9 | +8.4 |
| `confluence_gte_60` | 7 | S_STRANGER | 46.7% | 0.0% | 14.3% | 0.0% | -3.5 | 0.12 | 0.74 | +6.8 | +8.7 |
| `confluence_gte_70` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +3.3 | +10.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 60.0% | 22.2% | 22.2% | 33.3% | -1.3 | 0.55 | 1.66 | +7.4 | +8.0 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 33.3% | 20.0% | 20.0% | 20.0% | -2.2 | 0.32 | 1.28 | +7.5 | +7.5 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 73.3% | 18.2% | 18.2% | 18.2% | -3.8 | 0.26 | 1.15 | +8.2 | +7.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 46.7% | 28.6% | 28.6% | 28.6% | -1.3 | 0.62 | 1.54 | +8.0 | +6.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 93.3% | 14.3% | 14.3% | 21.4% | -3.2 | 0.24 | 1.32 | +7.2 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 20.0% | -2.8 | 0.30 | 1.10 | +7.1 | +8.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.3; validation N=7 Fav=14.3% Avg=-6.1; out_of_sample N=3 Fav=33.3% Avg=+4.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 46 | S_STRANGER | 100.0% | 13.0% | 17.4% | 8.7% | -5.2 | 0.29 | 1.29 | +6.2 | +8.3 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 39.1% | 16.7% | 22.2% | 11.1% | -3.5 | 0.48 | 1.69 | +6.6 | +8.0 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 52.2% | 12.5% | 16.7% | 8.3% | -4.0 | 0.38 | 1.90 | +5.5 | +7.8 |
| `stop_hunt_le_90` | 46 | S_STRANGER | 100.0% | 13.0% | 17.4% | 8.7% | -5.2 | 0.29 | 1.29 | +6.2 | +8.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 36 | S_STRANGER | 78.3% | 11.1% | 16.7% | 2.8% | -5.2 | 0.27 | 1.29 | +5.9 | +8.1 |
| `confluence_gte_70` | 11 | S_STRANGER | 23.9% | 18.2% | 18.2% | 9.1% | -2.8 | 0.53 | 2.38 | +6.2 | +11.1 |
| `tdi_rsi_gt_signal` | 24 | S_STRANGER | 52.2% | 4.2% | 12.5% | 0.0% | -7.6 | 0.12 | 0.78 | +4.7 | +11.1 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 43.5% | 10.0% | 15.0% | 5.0% | -6.2 | 0.19 | 1.07 | +6.1 | +10.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 46 | S_STRANGER | 100.0% | 13.0% | 17.4% | 8.7% | -5.2 | 0.29 | 1.29 | +6.2 | +8.3 |
| `feature_stale_hod_exhaustion_reject` | 46 | S_STRANGER | 100.0% | 13.0% | 17.4% | 8.7% | -5.2 | 0.29 | 1.29 | +6.2 | +8.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=20.0% Avg=+1.3; out_of_sample N=3 Fav=33.3% Avg=+3.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 12.9% | 12.9% | 16.1% | -3.9 | 0.33 | 1.92 | +5.0 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 25.8% | 25.0% | 25.0% | 37.5% | +2.0 | 1.58 | 3.95 | +10.6 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 54.8% | 23.5% | 23.5% | 23.5% | -1.0 | 0.79 | 2.36 | +6.7 | +7.0 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 12.9% | 12.9% | 16.1% | -3.9 | 0.33 | 1.92 | +5.0 | +7.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 31 | S_STRANGER | 100.0% | 12.9% | 12.9% | 16.1% | -3.9 | 0.33 | 1.92 | +5.0 | +7.3 |
| `confluence_gte_70` | 8 | S_STRANGER | 25.8% | 25.0% | 25.0% | 12.5% | +1.4 | 1.57 | 4.71 | +6.0 | +4.6 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 58.1% | 11.1% | 11.1% | 16.7% | -5.1 | 0.19 | 1.34 | +4.9 | +7.3 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 29.0% | 11.1% | 11.1% | 0.0% | -6.0 | 0.07 | 0.48 | +3.1 | +9.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 96.8% | 10.0% | 10.0% | 16.7% | -4.2 | 0.31 | 2.39 | +4.9 | +7.5 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 12.9% | 12.9% | 16.1% | -3.9 | 0.33 | 1.92 | +5.0 | +7.3 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 3.2% | 100.0% | 100.0% | 0.0% | +4.0 | 999.00 | 999.00 | +7.2 | +1.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 3.2% | 100.0% | 100.0% | 0.0% | +4.0 | 999.00 | 999.00 | +7.2 | +1.2 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=27.3% Avg=-0.8; validation N=7 Fav=0.0% Avg=-10.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 12.5% | 12.5% | 21.9% | -3.8 | 0.39 | 2.13 | +7.9 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 34.4% | 0.0% | 0.0% | 27.3% | -6.2 | 0.00 | 0.00 | +7.0 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 46.9% | 0.0% | 0.0% | 20.0% | -5.4 | 0.00 | 0.00 | +5.7 | +6.2 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 90.6% | 13.8% | 13.8% | 20.7% | -3.0 | 0.46 | 2.32 | +8.2 | +7.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 40.6% | 15.4% | 15.4% | 15.4% | -4.0 | 0.50 | 2.52 | +10.0 | +9.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 56.2% | 11.1% | 11.1% | 16.7% | -5.7 | 0.19 | 1.24 | +6.6 | +7.9 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 56.2% | 16.7% | 16.7% | 16.7% | -4.6 | 0.27 | 1.07 | +8.0 | +8.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 84.4% | 14.8% | 14.8% | 18.5% | -3.1 | 0.48 | 2.27 | +8.4 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 12.5% | 12.5% | 21.9% | -3.8 | 0.39 | 2.13 | +7.9 | +6.7 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 15.6% | 0.0% | 0.0% | 40.0% | -2.5 | 0.00 | 0.00 | +5.5 | +4.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 6.2% | 0.0% | 0.0% | 50.0% | -1.1 | 0.00 | 0.00 | +6.6 | +5.5 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-3.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 12.5% | 25.0% | 18.8% | -4.0 | 0.31 | 0.78 | +6.8 | +11.2 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 87.5% | 14.3% | 28.6% | 21.4% | -0.9 | 0.71 | 1.41 | +7.7 | +8.2 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 12.5% | 25.0% | 18.8% | -4.0 | 0.31 | 0.78 | +6.8 | +11.2 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 87.5% | 14.3% | 28.6% | 21.4% | -0.9 | 0.71 | 1.41 | +7.7 | +8.2 |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 12.5% | 25.0% | 18.8% | -4.0 | 0.31 | 0.78 | +6.8 | +11.2 |
| `confluence_gte_60` | 5 | S_STRANGER | 31.2% | 0.0% | 20.0% | 0.0% | -5.8 | 0.13 | 0.52 | +8.1 | +11.4 |
| `confluence_gte_70` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -0.2 | 0.00 | 0.00 | +16.3 | +1.4 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 43.8% | 14.3% | 14.3% | 14.3% | -9.6 | 0.15 | 0.73 | +8.1 | +18.6 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 43.8% | 14.3% | 14.3% | 0.0% | -9.6 | 0.15 | 0.88 | +7.8 | +17.1 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 87.5% | 14.3% | 28.6% | 21.4% | -0.9 | 0.71 | 1.41 | +7.7 | +8.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 20.0% | -3.1 | 0.42 | 1.27 | +10.9 | +13.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 87.5% | 14.3% | 28.6% | 21.4% | -0.9 | 0.71 | 1.41 | +7.7 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 12.5% | 25.0% | 18.8% | -4.0 | 0.31 | 0.78 | +6.8 | +11.2 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +2.8 | +9.8 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 18.8% | 0.0% | 0.0% | 0.0% | -10.9 | 0.00 | 0.00 | +3.6 | +19.2 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=22.2% Avg=+4.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 11.8% | 17.6% | 41.2% | +0.3 | 1.12 | 3.37 | +12.7 | +5.8 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 29.4% | 0.0% | 20.0% | 20.0% | -3.0 | 0.22 | 0.65 | +10.5 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 52.9% | 11.1% | 22.2% | 33.3% | +1.6 | 1.57 | 3.93 | +11.8 | +5.9 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 94.1% | 12.5% | 18.8% | 43.8% | +1.2 | 1.56 | 4.16 | +13.2 | +5.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 41.2% | 14.3% | 28.6% | 14.3% | +0.9 | 1.49 | 3.72 | +8.8 | +6.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 52.9% | 22.2% | 22.2% | 55.6% | +4.6 | 5.78 | 11.57 | +19.0 | +6.6 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 29.4% | 20.0% | 20.0% | 40.0% | +2.3 | 4.17 | 12.50 | +17.7 | +7.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 70.6% | 8.3% | 16.7% | 41.7% | -1.0 | 0.61 | 1.82 | +10.8 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 11.8% | 17.6% | 41.2% | +0.3 | 1.12 | 3.37 | +12.7 | +5.8 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 35.3% | 16.7% | 16.7% | 33.3% | +2.2 | 1.60 | 6.41 | +14.8 | +5.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +14.5 | +6.4 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=0.0% Avg=-0.9; validation N=4 Fav=25.0% Avg=+2.3; out_of_sample N=3 Fav=33.3% Avg=-2.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 23.5% | -2.1 | 0.49 | 3.16 | +7.3 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 70.6% | 8.3% | 8.3% | 16.7% | -3.7 | 0.13 | 1.30 | +6.5 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 82.4% | 14.3% | 14.3% | 21.4% | -1.6 | 0.61 | 3.34 | +7.7 | +6.5 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 88.2% | 13.3% | 13.3% | 20.0% | -1.6 | 0.58 | 3.48 | +7.4 | +6.4 |
| `asian_range_gte_30` | 10 | S_STRANGER | 58.8% | 20.0% | 20.0% | 40.0% | +0.0 | 1.01 | 3.03 | +9.3 | +5.9 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 23.5% | -2.1 | 0.49 | 3.16 | +7.3 | +6.7 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 23.5% | -2.1 | 0.49 | 3.16 | +7.3 | +6.7 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 76.5% | 7.7% | 7.7% | 7.7% | -2.9 | 0.43 | 5.10 | +6.2 | +7.9 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 58.8% | 10.0% | 10.0% | 10.0% | -2.7 | 0.51 | 4.58 | +7.1 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 28.6% | -2.3 | 0.29 | 1.47 | +7.2 | +5.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 29.4% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +3.7 | +7.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 88.2% | 13.3% | 13.3% | 20.0% | -1.6 | 0.58 | 3.48 | +7.4 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 23.5% | -2.1 | 0.49 | 3.16 | +7.3 | +6.7 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 23.5% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +4.0 | +5.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +7.2 | +3.0 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=27.3% Avg=+0.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-5.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 34 | S_STRANGER | 100.0% | 11.8% | 20.6% | 20.6% | -4.2 | 0.45 | 1.53 | +11.1 | +10.9 |
| `hunt_to_ar_ratio_le_2_0` | 33 | S_STRANGER | 97.1% | 12.1% | 21.2% | 21.2% | -3.9 | 0.47 | 1.55 | +11.2 | +10.8 |
| `hunt_to_ar_ratio_le_2_5` | 33 | S_STRANGER | 97.1% | 12.1% | 21.2% | 21.2% | -3.9 | 0.47 | 1.55 | +11.2 | +10.8 |
| `stop_hunt_le_90` | 33 | S_STRANGER | 97.1% | 12.1% | 21.2% | 21.2% | -3.9 | 0.47 | 1.55 | +11.2 | +10.8 |
| `asian_range_gte_30` | 27 | S_STRANGER | 79.4% | 7.4% | 18.5% | 18.5% | -5.2 | 0.32 | 1.22 | +9.8 | +11.3 |
| `confluence_gte_60` | 27 | S_STRANGER | 79.4% | 11.1% | 22.2% | 18.5% | -3.8 | 0.50 | 1.59 | +11.0 | +10.1 |
| `confluence_gte_70` | 13 | S_STRANGER | 38.2% | 0.0% | 15.4% | 15.4% | -6.6 | 0.10 | 0.43 | +7.7 | +7.4 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 44.1% | 13.3% | 13.3% | 20.0% | -7.1 | 0.33 | 2.00 | +13.4 | +12.1 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 35.3% | 25.0% | 25.0% | 25.0% | -0.4 | 0.95 | 2.86 | +17.9 | +13.7 |
| `ratio_le_2_and_asian_gte_30` | 27 | S_STRANGER | 79.4% | 7.4% | 18.5% | 18.5% | -5.2 | 0.32 | 1.22 | +9.8 | +11.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 32.4% | 9.1% | 9.1% | 18.2% | -8.7 | 0.14 | 1.24 | +11.5 | +12.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 33 | S_STRANGER | 97.1% | 12.1% | 21.2% | 21.2% | -3.9 | 0.47 | 1.55 | +11.2 | +10.8 |
| `feature_stale_hod_exhaustion_reject` | 34 | S_STRANGER | 100.0% | 11.8% | 20.6% | 20.6% | -4.2 | 0.45 | 1.53 | +11.1 | +10.9 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 20.6% | 0.0% | 28.6% | 14.3% | -6.9 | 0.11 | 0.22 | +6.9 | +8.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -11.6 | 0.00 | 0.00 | +8.0 | +18.3 |

### THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=16.7% Avg=-1.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 11.1% | -1.7 | 0.52 | 3.90 | +6.5 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 88.9% | 12.5% | 12.5% | 12.5% | -1.4 | 0.59 | 3.87 | +6.4 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 11.1% | -1.7 | 0.52 | 3.90 | +6.5 | +5.7 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 94.4% | 11.8% | 11.8% | 11.8% | -1.6 | 0.55 | 3.88 | +6.1 | +5.5 |
| `asian_range_gte_30` | 16 | S_STRANGER | 88.9% | 12.5% | 12.5% | 12.5% | -1.0 | 0.66 | 4.32 | +7.2 | +5.2 |
| `confluence_gte_60` | 7 | S_STRANGER | 38.9% | 14.3% | 14.3% | 0.0% | -3.5 | 0.11 | 0.69 | +5.4 | +6.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 22.2% | 25.0% | 25.0% | 0.0% | -2.2 | 0.27 | 0.80 | +7.8 | +7.4 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 66.7% | 16.7% | 16.7% | 8.3% | -1.0 | 0.72 | 3.62 | +7.9 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 83.3% | 13.3% | 13.3% | 13.3% | -0.9 | 0.72 | 4.33 | +6.8 | +4.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 0.0% | -1.6 | 0.40 | 0.79 | +6.1 | +6.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 94.4% | 11.8% | 11.8% | 11.8% | -1.6 | 0.55 | 3.88 | +6.1 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 11.1% | -1.7 | 0.52 | 3.90 | +6.5 | +5.7 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +3.7 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +4.5 | +4.8 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=+2.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 11.1% | -12.5 | 0.20 | 0.65 | +13.7 | +11.4 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 88.9% | 12.5% | 25.0% | 12.5% | -13.9 | 0.20 | 0.56 | +13.8 | +10.6 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 11.1% | -12.5 | 0.20 | 0.65 | +13.7 | +11.4 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 11.1% | -12.5 | 0.20 | 0.65 | +13.7 | +11.4 |
| `asian_range_gte_30` | 15 | S_STRANGER | 83.3% | 13.3% | 26.7% | 13.3% | -13.1 | 0.22 | 0.56 | +14.6 | +11.1 |
| `confluence_gte_60` | 7 | S_STRANGER | 38.9% | 0.0% | 0.0% | 0.0% | -18.0 | 0.00 | 0.00 | +9.7 | +11.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 83.3% | 13.3% | 20.0% | 13.3% | -11.1 | 0.23 | 0.86 | +14.6 | +12.8 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | 16.7% | 16.7% | 16.7% | +2.9 | 3.27 | 13.09 | +24.2 | +22.0 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 83.3% | 13.3% | 26.7% | 13.3% | -13.1 | 0.22 | 0.56 | +14.6 | +11.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 66.7% | 16.7% | 25.0% | 16.7% | -11.5 | 0.27 | 0.72 | +16.0 | +12.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 11.1% | -12.5 | 0.20 | 0.65 | +13.7 | +11.4 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 94.4% | 11.8% | 23.5% | 11.8% | -13.2 | 0.20 | 0.60 | +13.3 | +10.8 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 38.9% | 14.3% | 42.9% | 28.6% | -6.6 | 0.40 | 0.40 | +14.2 | +7.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 50.0% | -0.6 | 0.00 | 0.00 | +31.2 | +27.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=15 Fav=0.0% Avg=-3.8; validation N=20 Fav=25.0% Avg=-7.0; out_of_sample N=46 Fav=13.0% Avg=-5.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 102 | S_STRANGER | 100.0% | 10.8% | 12.7% | 11.8% | -7.3 | 0.18 | 1.17 | +7.4 | +8.3 |
| `hunt_to_ar_ratio_le_2_0` | 82 | S_STRANGER | 80.4% | 11.0% | 13.4% | 12.2% | -6.4 | 0.20 | 1.22 | +6.8 | +8.2 |
| `hunt_to_ar_ratio_le_2_5` | 93 | S_STRANGER | 91.2% | 10.8% | 12.9% | 11.8% | -7.7 | 0.17 | 1.11 | +6.8 | +8.4 |
| `stop_hunt_le_90` | 97 | S_STRANGER | 95.1% | 11.3% | 13.4% | 11.3% | -7.5 | 0.19 | 1.13 | +7.4 | +8.5 |
| `asian_range_gte_30` | 81 | S_STRANGER | 79.4% | 13.6% | 14.8% | 13.6% | -5.7 | 0.26 | 1.39 | +7.9 | +8.0 |
| `confluence_gte_60` | 91 | S_STRANGER | 89.2% | 11.0% | 13.2% | 13.2% | -7.8 | 0.15 | 0.92 | +7.2 | +7.9 |
| `confluence_gte_70` | 18 | S_STRANGER | 17.6% | 5.6% | 16.7% | 5.6% | -6.5 | 0.07 | 0.35 | +7.5 | +10.4 |
| `tdi_rsi_gt_signal` | 55 | S_STRANGER | 53.9% | 5.5% | 7.3% | 7.3% | -8.5 | 0.11 | 1.35 | +6.7 | +8.9 |
| `tdi_rsi_gte_50` | 43 | S_STRANGER | 42.2% | 11.6% | 11.6% | 9.3% | -5.2 | 0.25 | 1.90 | +8.5 | +11.0 |
| `ratio_le_2_and_asian_gte_30` | 71 | S_STRANGER | 69.6% | 12.7% | 14.1% | 12.7% | -6.6 | 0.22 | 1.24 | +7.1 | +8.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 37 | S_STRANGER | 36.3% | 5.4% | 8.1% | 5.4% | -8.0 | 0.11 | 1.30 | +5.5 | +8.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 97 | S_STRANGER | 95.1% | 11.3% | 13.4% | 11.3% | -7.5 | 0.19 | 1.13 | +7.4 | +8.5 |
| `feature_stale_hod_exhaustion_reject` | 102 | S_STRANGER | 100.0% | 10.8% | 12.7% | 11.8% | -7.3 | 0.18 | 1.17 | +7.4 | +8.3 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 4.9% | 0.0% | 0.0% | 40.0% | -1.0 | 0.00 | 0.00 | +5.6 | +3.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=12.5% Avg=-1.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-8.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -3.0 | 0.53 | 4.28 | +11.7 | +8.9 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 22.2% | -2.0 | 0.66 | 4.62 | +12.1 | +7.9 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 22.2% | -2.0 | 0.66 | 4.62 | +12.1 | +7.9 |
| `stop_hunt_le_90` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 22.2% | -2.0 | 0.66 | 4.62 | +12.1 | +7.9 |
| `asian_range_gte_30` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 11.1% | -7.2 | 0.00 | 0.00 | +8.3 | +9.9 |
| `confluence_gte_60` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -8.3 | 0.00 | 0.00 | +9.1 | +12.3 |
| `confluence_gte_70` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -7.3 | 0.00 | 0.00 | +11.4 | +11.5 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -9.4 | 0.00 | 0.00 | +4.4 | +11.0 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -8.0 | 0.00 | 0.00 | +10.2 | +11.5 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 12.5% | -6.6 | 0.00 | 0.00 | +8.3 | +8.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -9.4 | 0.00 | 0.00 | +4.4 | +11.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 22.2% | -2.0 | 0.66 | 4.62 | +12.1 | +7.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -3.0 | 0.53 | 4.28 | +11.7 | +8.9 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 66.7% | +9.5 | 5.52 | 5.52 | +19.3 | +4.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +13.7 | +8.4 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.1; validation N=9 Fav=11.1% Avg=-4.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -4.3 | 0.15 | 1.23 | +5.0 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -4.3 | 0.15 | 1.23 | +5.0 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -4.3 | 0.15 | 1.23 | +5.0 | +5.0 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -4.3 | 0.15 | 1.23 | +5.0 | +5.0 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -4.3 | 0.15 | 1.23 | +5.0 | +5.0 |
| `confluence_gte_60` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -8.8 | 0.00 | 0.00 | +2.3 | +4.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 12.5% | -3.7 | 0.00 | 0.00 | +4.5 | +5.4 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +3.5 | +3.9 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -4.3 | 0.15 | 1.23 | +5.0 | +5.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 12.5% | -3.7 | 0.00 | 0.00 | +4.5 | +5.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -4.3 | 0.15 | 1.23 | +5.0 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 20.0% | -4.3 | 0.15 | 1.23 | +5.0 | +5.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+5.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=0.0% Avg=-7.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -4.9 | 0.23 | 2.09 | +5.5 | +10.4 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -9.6 | 0.00 | 0.00 | +4.6 | +14.7 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 0.0% | -7.4 | 0.00 | 0.00 | +4.4 | +11.4 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -4.9 | 0.23 | 2.09 | +5.5 | +10.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 0.0% | -8.2 | 0.00 | 0.00 | +4.1 | +12.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 12.5% | -4.3 | 0.30 | 2.11 | +5.9 | +10.4 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -10.2 | 0.00 | 0.00 | +3.5 | +15.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 0.0% | -8.2 | 0.00 | 0.00 | +4.1 | +12.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -4.9 | 0.23 | 2.09 | +5.5 | +10.4 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +2.9 | 2.45 | 4.90 | +8.6 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=-4.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -5.8 | 0.23 | 2.04 | +6.8 | +9.4 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +17.0 | 999.00 | 999.00 | +28.9 | +3.5 |
| `stop_hunt_le_90` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 14.3% | -4.3 | 0.36 | 2.16 | +7.9 | +11.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -5.8 | 0.23 | 2.04 | +6.8 | +9.4 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -5.8 | 0.23 | 2.04 | +6.8 | +9.4 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 11.1% | -6.0 | 0.24 | 1.92 | +6.6 | +9.7 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +3.3 | +7.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | -4.6 | 0.42 | 1.70 | +8.8 | +13.3 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -5.8 | 0.23 | 2.04 | +6.8 | +9.4 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -7.8 | 0.00 | 0.00 | +5.1 | +8.1 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-10.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -13.2 | 0.10 | 0.94 | +6.8 | +13.5 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 12.5% | -12.7 | 0.13 | 0.92 | +7.9 | +14.0 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 11.1% | -12.1 | 0.12 | 0.99 | +7.3 | +13.5 |
| `stop_hunt_le_90` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 11.1% | -12.1 | 0.12 | 0.99 | +7.3 | +13.5 |
| `asian_range_gte_30` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -10.4 | 0.00 | 0.00 | +8.6 | +8.5 |
| `confluence_gte_60` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 16.7% | -10.3 | 0.20 | 1.00 | +9.3 | +12.5 |
| `confluence_gte_70` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.0 | 0.00 | 0.00 | +20.6 | +3.2 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 16.7% | -12.9 | 0.17 | 0.83 | +9.3 | +15.0 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -11.5 | 0.00 | 0.00 | +6.0 | +21.0 |
| `ratio_le_2_and_asian_gte_30` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.0 | 0.00 | 0.00 | +20.6 | +3.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.0 | 0.00 | 0.00 | +20.6 | +3.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 11.1% | -12.1 | 0.12 | 0.99 | +7.3 | +13.5 |
| `feature_stale_hod_exhaustion_reject` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 11.1% | -12.4 | 0.12 | 0.98 | +7.6 | +11.4 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -23.0 | 0.00 | 0.00 | +2.4 | +24.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -20.9 | 0.00 | 0.00 | +0.3 | +32.4 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=7.7% Avg=-9.0; validation N=13 Fav=23.1% Avg=+1.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 51 | S_STRANGER | 100.0% | 9.8% | 9.8% | 11.8% | -4.8 | 0.24 | 2.04 | +6.0 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 37.3% | 5.3% | 5.3% | 10.5% | -4.2 | 0.10 | 1.67 | +5.1 | +7.3 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 47.1% | 8.3% | 8.3% | 16.7% | -3.6 | 0.21 | 1.98 | +5.7 | +7.1 |
| `stop_hunt_le_90` | 49 | S_STRANGER | 96.1% | 10.2% | 10.2% | 12.2% | -4.7 | 0.26 | 2.05 | +6.2 | +7.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 26 | S_STRANGER | 51.0% | 15.4% | 15.4% | 15.4% | -4.0 | 0.41 | 1.97 | +7.6 | +6.2 |
| `confluence_gte_70` | 3 | S_STRANGER | 5.9% | 33.3% | 33.3% | 33.3% | -4.9 | 0.45 | 0.45 | +7.0 | +12.7 |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 45.1% | 4.3% | 4.3% | 13.0% | -4.6 | 0.11 | 2.23 | +5.4 | +7.5 |
| `tdi_rsi_gte_50` | 25 | S_STRANGER | 49.0% | 12.0% | 12.0% | 16.0% | -3.1 | 0.44 | 2.78 | +8.1 | +9.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 48 | S_STRANGER | 94.1% | 10.4% | 10.4% | 12.5% | -4.7 | 0.26 | 2.04 | +6.2 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 51 | S_STRANGER | 100.0% | 9.8% | 9.8% | 11.8% | -4.8 | 0.24 | 2.04 | +6.0 | +7.3 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 11.8% | 0.0% | 0.0% | 16.7% | -6.0 | 0.00 | 0.00 | +4.8 | +7.5 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 5.9% | 0.0% | 0.0% | 33.3% | -4.2 | 0.00 | 0.00 | +8.2 | +6.6 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-3.6; validation N=6 Fav=0.0% Avg=-13.7; out_of_sample N=6 Fav=33.3% Avg=+5.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 41 | S_STRANGER | 100.0% | 9.8% | 22.0% | 14.6% | -5.6 | 0.31 | 0.98 | +8.6 | +7.6 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 75.6% | 6.5% | 22.6% | 16.1% | -4.4 | 0.36 | 1.08 | +8.4 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 37 | S_STRANGER | 90.2% | 8.1% | 21.6% | 16.2% | -4.2 | 0.35 | 1.10 | +8.4 | +7.1 |
| `stop_hunt_le_90` | 39 | S_STRANGER | 95.1% | 7.7% | 20.5% | 15.4% | -4.9 | 0.30 | 1.02 | +8.1 | +7.9 |
| `asian_range_gte_30` | 33 | S_STRANGER | 80.5% | 9.1% | 21.2% | 12.1% | -5.0 | 0.34 | 1.12 | +8.6 | +8.0 |
| `confluence_gte_60` | 39 | S_STRANGER | 95.1% | 10.3% | 23.1% | 15.4% | -5.7 | 0.32 | 0.93 | +8.9 | +7.7 |
| `confluence_gte_70` | 16 | S_STRANGER | 39.0% | 0.0% | 12.5% | 18.8% | -5.6 | 0.23 | 1.25 | +6.3 | +7.0 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 48.8% | 10.0% | 25.0% | 25.0% | -6.7 | 0.29 | 0.68 | +8.7 | +6.9 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 36.6% | 13.3% | 13.3% | 13.3% | -4.2 | 0.38 | 2.30 | +9.6 | +12.6 |
| `ratio_le_2_and_asian_gte_30` | 27 | S_STRANGER | 65.9% | 3.7% | 18.5% | 14.8% | -5.3 | 0.28 | 1.06 | +8.0 | +7.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 31.7% | 7.7% | 30.8% | 23.1% | -4.9 | 0.36 | 0.63 | +8.6 | +6.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 39 | S_STRANGER | 95.1% | 7.7% | 20.5% | 15.4% | -4.9 | 0.30 | 1.02 | +8.1 | +7.9 |
| `feature_stale_hod_exhaustion_reject` | 41 | S_STRANGER | 100.0% | 9.8% | 22.0% | 14.6% | -5.6 | 0.31 | 0.98 | +8.6 | +7.6 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 9.8% | 0.0% | 0.0% | 50.0% | -0.6 | 0.00 | 0.00 | +6.5 | +2.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-2.7; validation N=5 Fav=20.0% Avg=-1.3; out_of_sample N=1 Fav=100.0% Avg=+2.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 9.5% | 9.5% | 14.3% | -3.9 | 0.13 | 1.10 | +7.0 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 38.1% | 25.0% | 25.0% | 25.0% | -1.2 | 0.56 | 1.39 | +7.9 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 61.9% | 15.4% | 15.4% | 15.4% | -2.0 | 0.32 | 1.60 | +6.4 | +5.8 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 9.5% | 9.5% | 14.3% | -3.9 | 0.13 | 1.10 | +7.0 | +6.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 20 | S_STRANGER | 95.2% | 10.0% | 10.0% | 15.0% | -3.9 | 0.14 | 1.08 | +6.9 | +6.2 |
| `confluence_gte_70` | 4 | S_STRANGER | 19.0% | 0.0% | 0.0% | 0.0% | -10.1 | 0.00 | 0.00 | +2.2 | +2.6 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +6.2 | +5.4 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 61.9% | 7.7% | 7.7% | 0.0% | -3.2 | 0.05 | 0.55 | +7.0 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 9.5% | 9.5% | 14.3% | -3.9 | 0.13 | 1.10 | +7.0 | +6.2 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 9.5% | 9.5% | 14.3% | -3.9 | 0.13 | 1.10 | +7.0 | +6.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +8.2 | +5.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +8.2 | +5.1 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=16.7% Avg=-1.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 9.5% | 14.3% | 19.0% | -9.8 | 0.27 | 1.46 | +7.6 | +9.0 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 76.2% | 6.2% | 12.5% | 18.8% | -8.3 | 0.05 | 0.29 | +4.1 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 100.0% | 9.5% | 14.3% | 19.0% | -9.8 | 0.27 | 1.46 | +7.6 | +9.0 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 85.7% | 11.1% | 16.7% | 22.2% | -8.1 | 0.35 | 1.50 | +8.1 | +7.4 |
| `asian_range_gte_30` | 20 | S_STRANGER | 95.2% | 10.0% | 15.0% | 20.0% | -6.1 | 0.39 | 1.94 | +7.8 | +9.1 |
| `confluence_gte_60` | 8 | S_STRANGER | 38.1% | 12.5% | 12.5% | 12.5% | -24.0 | 0.02 | 0.13 | +3.0 | +7.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 57.1% | 16.7% | 25.0% | 25.0% | -1.4 | 0.82 | 2.19 | +10.4 | +9.0 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 14.3% | 33.3% | 33.3% | 33.3% | +11.3 | 1.93 | 3.86 | +30.0 | +16.6 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 76.2% | 6.2% | 12.5% | 18.8% | -8.3 | 0.05 | 0.29 | +4.1 | +7.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 42.9% | 11.1% | 22.2% | 22.2% | -6.0 | 0.11 | 0.34 | +4.3 | +6.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 81.0% | 5.9% | 11.8% | 17.6% | -12.7 | 0.03 | 0.20 | +4.1 | +7.5 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 9.5% | 14.3% | 19.0% | -9.8 | 0.27 | 1.46 | +7.6 | +9.0 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 42.9% | 11.1% | 22.2% | 22.2% | -4.8 | 0.14 | 0.41 | +5.0 | +6.6 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 9.5% | 50.0% | 50.0% | 50.0% | +31.6 | 9.66 | 9.66 | +41.6 | +9.7 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=14.3% Avg=-4.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -9.1 | 0.14 | 1.37 | +14.1 | +14.2 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 0.0% | -10.0 | 0.15 | 1.20 | +13.8 | +14.3 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 0.0% | -9.6 | 0.14 | 1.28 | +14.9 | +13.9 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -9.1 | 0.14 | 1.37 | +14.1 | +14.2 |
| `asian_range_gte_30` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -3.3 | 0.55 | 1.65 | +20.0 | +24.4 |
| `confluence_gte_60` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 0.0% | -3.7 | 0.32 | 2.60 | +16.2 | +16.5 |
| `confluence_gte_70` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 0.0% | +6.5 | 5.64 | 5.64 | +29.8 | +30.1 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 63.6% | 14.3% | 14.3% | 0.0% | -4.1 | 0.36 | 2.14 | +17.4 | +18.4 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 0.0% | -3.7 | 0.32 | 2.60 | +16.2 | +16.5 |
| `ratio_le_2_and_asian_gte_30` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -3.3 | 0.55 | 1.65 | +20.0 | +24.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -3.3 | 0.55 | 1.65 | +20.0 | +24.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -9.1 | 0.14 | 1.37 | +14.1 | +14.2 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 0.0% | -9.1 | 0.14 | 1.37 | +14.1 | +14.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -21.3 | 0.00 | 0.00 | +1.5 | +6.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +8.7 | +10.0 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=11.1% Avg=+1.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 78 | S_STRANGER | 100.0% | 9.0% | 14.1% | 21.8% | -4.9 | 0.30 | 1.47 | +8.7 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 68 | S_STRANGER | 87.2% | 8.8% | 14.7% | 19.1% | -4.6 | 0.31 | 1.47 | +8.3 | +6.2 |
| `hunt_to_ar_ratio_le_2_5` | 74 | S_STRANGER | 94.9% | 9.5% | 14.9% | 21.6% | -5.1 | 0.31 | 1.42 | +8.4 | +6.1 |
| `stop_hunt_le_90` | 75 | S_STRANGER | 96.2% | 9.3% | 14.7% | 21.3% | -5.0 | 0.30 | 1.44 | +8.5 | +6.1 |
| `asian_range_gte_30` | 60 | S_STRANGER | 76.9% | 8.3% | 11.7% | 18.3% | -6.2 | 0.20 | 1.26 | +8.4 | +6.3 |
| `confluence_gte_60` | 66 | S_STRANGER | 84.6% | 6.1% | 12.1% | 21.2% | -5.7 | 0.23 | 1.28 | +8.2 | +6.0 |
| `confluence_gte_70` | 17 | S_STRANGER | 21.8% | 5.9% | 11.8% | 5.9% | -3.1 | 0.32 | 2.41 | +4.7 | +5.3 |
| `tdi_rsi_gt_signal` | 63 | S_STRANGER | 80.8% | 11.1% | 17.5% | 22.2% | -4.4 | 0.38 | 1.41 | +9.3 | +6.4 |
| `tdi_rsi_gte_50` | 22 | S_STRANGER | 28.2% | 13.6% | 13.6% | 18.2% | -1.4 | 0.66 | 3.50 | +10.9 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 57 | S_STRANGER | 73.1% | 8.8% | 12.3% | 19.3% | -5.3 | 0.24 | 1.43 | +8.1 | +6.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 45 | S_STRANGER | 57.7% | 11.1% | 15.6% | 20.0% | -4.8 | 0.30 | 1.39 | +8.8 | +6.8 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 1.3% | 0.0% | 0.0% | 0.0% | -9.2 | 0.00 | 0.00 | +6.0 | +9.9 |
| `feature_extreme_hunt_with_exception` | 75 | S_STRANGER | 96.2% | 9.3% | 14.7% | 21.3% | -5.0 | 0.30 | 1.44 | +8.5 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 78 | S_STRANGER | 100.0% | 9.0% | 14.1% | 21.8% | -4.9 | 0.30 | 1.47 | +8.7 | +6.1 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 11.5% | 11.1% | 11.1% | 22.2% | +1.3 | 1.37 | 9.59 | +8.3 | +5.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 2.6% | 0.0% | 0.0% | 0.0% | -2.9 | 0.00 | 0.00 | +3.5 | +6.4 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=11.1% Avg=-3.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 25.0% | -5.8 | 0.13 | 1.18 | +9.7 | +10.8 |
| `hunt_to_ar_ratio_le_2_0` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -13.8 | 0.00 | 0.00 | +3.0 | +16.0 |
| `hunt_to_ar_ratio_le_2_5` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -13.8 | 0.00 | 0.00 | +3.0 | +16.0 |
| `stop_hunt_le_90` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 33.3% | -3.9 | 0.23 | 1.39 | +11.7 | +8.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 25.0% | -5.8 | 0.13 | 1.18 | +9.7 | +10.8 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 25.0% | -5.8 | 0.13 | 1.18 | +9.7 | +10.8 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -4.8 | 0.00 | 0.00 | +11.5 | +9.0 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -8.0 | 0.00 | 0.00 | +5.3 | +13.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 33.3% | -4.5 | 0.21 | 1.24 | +11.6 | +9.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 25.0% | -5.8 | 0.13 | 1.18 | +9.7 | +10.8 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 25.0% | -4.1 | 0.00 | 0.00 | +7.6 | +7.3 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=14.3% Avg=-7.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -6.2 | 0.27 | 2.97 | +6.3 | +13.7 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -18.0 | 0.00 | 0.00 | +0.9 | +24.3 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 83.3% | 10.0% | 10.0% | 10.0% | -5.2 | 0.34 | 3.10 | +6.3 | +13.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -6.2 | 0.27 | 2.97 | +6.3 | +13.7 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -6.2 | 0.27 | 2.97 | +6.3 | +13.7 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 14.3% | -7.2 | 0.35 | 2.12 | +9.3 | +15.5 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 0.0% | 0.0% | 0.0% | -10.8 | 0.00 | 0.00 | +3.9 | +16.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 9.1% | -6.0 | 0.29 | 2.95 | +6.7 | +13.6 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 8.3% | -6.2 | 0.27 | 2.97 | +6.3 | +13.7 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 25.0% | -1.8 | 0.79 | 2.36 | +9.5 | +11.5 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -13.7 | 0.00 | 0.00 | +3.2 | +17.9 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=16.7% Avg=-9.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 16.7% | -6.3 | 0.11 | 0.52 | +4.9 | +10.1 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 18.2% | -7.4 | 0.04 | 0.37 | +4.4 | +10.7 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 18.2% | -7.4 | 0.04 | 0.37 | +4.4 | +10.7 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 18.2% | -7.4 | 0.04 | 0.37 | +4.4 | +10.7 |
| `asian_range_gte_30` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 33.3% | -9.5 | 0.06 | 0.23 | +5.0 | +14.5 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 16.7% | -6.3 | 0.11 | 0.52 | +4.9 | +10.1 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 16.7% | -6.3 | 0.11 | 0.52 | +4.9 | +10.1 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -7.4 | 0.00 | 0.00 | +4.2 | +6.0 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +4.7 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 33.3% | -9.5 | 0.06 | 0.23 | +5.0 | +14.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 9.1% | 9.1% | 18.2% | -7.4 | 0.04 | 0.37 | +4.4 | +10.7 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 16.7% | -6.3 | 0.11 | 0.52 | +4.9 | +10.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 33.3% | -8.2 | 0.00 | 0.00 | +4.2 | +9.3 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=0.0% Avg=-6.0; validation N=2 Fav=0.0% Avg=-1.1; out_of_sample N=6 Fav=50.0% Avg=+13.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 38 | S_STRANGER | 100.0% | 7.9% | 13.2% | 18.4% | -16.2 | 0.18 | 1.00 | +9.8 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 81.6% | 9.7% | 16.1% | 19.4% | -9.3 | 0.32 | 1.40 | +10.7 | +6.0 |
| `hunt_to_ar_ratio_le_2_5` | 35 | S_STRANGER | 92.1% | 8.6% | 14.3% | 20.0% | -12.9 | 0.23 | 1.14 | +10.0 | +5.7 |
| `stop_hunt_le_90` | 37 | S_STRANGER | 97.4% | 8.1% | 13.5% | 18.9% | -14.2 | 0.20 | 1.10 | +10.0 | +5.7 |
| `asian_range_gte_30` | 27 | S_STRANGER | 71.1% | 11.1% | 18.5% | 14.8% | -14.0 | 0.26 | 1.05 | +11.3 | +5.3 |
| `confluence_gte_60` | 38 | S_STRANGER | 100.0% | 7.9% | 13.2% | 18.4% | -16.2 | 0.18 | 1.00 | +9.8 | +5.7 |
| `confluence_gte_70` | 38 | S_STRANGER | 100.0% | 7.9% | 13.2% | 18.4% | -16.2 | 0.18 | 1.00 | +9.8 | +5.7 |
| `tdi_rsi_gt_signal` | 36 | S_STRANGER | 94.7% | 8.3% | 13.9% | 16.7% | -15.5 | 0.19 | 1.04 | +10.1 | +5.9 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 28.9% | 27.3% | 36.4% | 18.2% | +5.7 | 2.27 | 3.97 | +18.2 | +11.4 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 65.8% | 12.0% | 20.0% | 16.0% | -10.6 | 0.33 | 1.20 | +12.0 | +5.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 23 | S_STRANGER | 60.5% | 13.0% | 21.7% | 13.0% | -9.1 | 0.39 | 1.33 | +12.7 | +5.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 37 | S_STRANGER | 97.4% | 8.1% | 13.5% | 18.9% | -14.2 | 0.20 | 1.10 | +10.0 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 100.0% | 7.9% | 13.2% | 18.4% | -16.2 | 0.18 | 1.00 | +9.8 | +5.7 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 2.6% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +1.2 | +6.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.6% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +1.2 | +6.8 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-9.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 7.1% | -7.9 | 0.13 | 1.50 | +7.1 | +12.3 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 92.9% | 7.7% | 7.7% | 7.7% | -8.1 | 0.13 | 1.45 | +7.4 | +12.3 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 7.1% | -7.9 | 0.13 | 1.50 | +7.1 | +12.3 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 7.1% | -7.9 | 0.13 | 1.50 | +7.1 | +12.3 |
| `asian_range_gte_30` | 12 | S_STRANGER | 85.7% | 8.3% | 8.3% | 8.3% | -8.7 | 0.13 | 1.32 | +7.9 | +13.0 |
| `confluence_gte_60` | 9 | S_STRANGER | 64.3% | 11.1% | 11.1% | 11.1% | -6.1 | 0.22 | 1.57 | +8.7 | +11.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 0.0% | -14.1 | 0.00 | 0.00 | +7.8 | +18.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 0.0% | -9.6 | 0.22 | 1.08 | +11.2 | +16.2 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 85.7% | 8.3% | 8.3% | 8.3% | -8.7 | 0.13 | 1.32 | +7.9 | +13.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 0.0% | -14.1 | 0.00 | 0.00 | +7.8 | +18.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 92.9% | 7.7% | 7.7% | 7.7% | -8.1 | 0.13 | 1.45 | +7.4 | +12.3 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 92.9% | 7.7% | 7.7% | 7.7% | -8.1 | 0.13 | 1.45 | +7.4 | +12.3 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 0.0% | -7.2 | 0.00 | 0.00 | +7.8 | +10.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -7.9 | 0.00 | 0.00 | +10.2 | +11.7 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=14.3% Avg=-2.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 7.1% | -9.5 | 0.09 | 1.14 | +3.0 | +6.8 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 25.0% | +1.0 | 1.47 | 4.40 | +5.2 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 14.3% | -2.3 | 0.44 | 2.63 | +3.3 | +5.1 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 7.1% | -9.5 | 0.09 | 1.14 | +3.0 | +6.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 7.1% | -9.5 | 0.09 | 1.14 | +3.0 | +6.8 |
| `confluence_gte_70` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -31.3 | 0.00 | 0.00 | +7.3 | +1.4 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 64.3% | 0.0% | 0.0% | 0.0% | -13.4 | 0.00 | 0.00 | +2.1 | +8.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -7.1 | 0.00 | 0.00 | +1.7 | +7.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 7.1% | -9.5 | 0.09 | 1.14 | +3.0 | +6.8 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 7.1% | -9.5 | 0.09 | 1.14 | +3.0 | +6.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-11.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 7.1% | 14.3% | 0.0% | -17.0 | 0.11 | 0.63 | +8.5 | +11.1 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 7.1% | 14.3% | 0.0% | -17.0 | 0.11 | 0.63 | +8.5 | +11.1 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 7.1% | 14.3% | 0.0% | -17.0 | 0.11 | 0.63 | +8.5 | +11.1 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 7.1% | 14.3% | 0.0% | -17.0 | 0.11 | 0.63 | +8.5 | +11.1 |
| `asian_range_gte_30` | 12 | S_STRANGER | 85.7% | 0.0% | 8.3% | 0.0% | -19.2 | 0.04 | 0.41 | +6.3 | +12.1 |
| `confluence_gte_60` | 11 | S_STRANGER | 78.6% | 9.1% | 18.2% | 0.0% | -19.0 | 0.12 | 0.53 | +9.2 | +13.6 |
| `confluence_gte_70` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 0.0% | -26.8 | 0.00 | 0.00 | +3.6 | +23.4 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 0.0% | -11.0 | 0.26 | 1.03 | +12.5 | +20.9 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 0.0% | -11.0 | 0.26 | 1.03 | +12.5 | +20.9 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 85.7% | 0.0% | 8.3% | 0.0% | -19.2 | 0.04 | 0.41 | +6.3 | +12.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 0.0% | -18.5 | 0.00 | 0.00 | +6.7 | +23.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 7.1% | 14.3% | 0.0% | -17.0 | 0.11 | 0.63 | +8.5 | +11.1 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 7.1% | 14.3% | 0.0% | -17.0 | 0.11 | 0.63 | +8.5 | +11.1 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -26.0 | 0.00 | 0.00 | +7.4 | +0.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 7.1% | 100.0% | 100.0% | 0.0% | +19.0 | 999.00 | 999.00 | +35.9 | +9.8 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=14.3% Avg=-7.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -17.4 | 0.08 | 1.00 | +8.7 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 92.9% | 7.7% | 7.7% | 15.4% | -13.2 | 0.12 | 1.27 | +8.5 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -17.4 | 0.08 | 1.00 | +8.7 | +6.2 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 92.9% | 7.7% | 7.7% | 15.4% | -13.2 | 0.12 | 1.27 | +8.5 | +6.6 |
| `asian_range_gte_30` | 13 | S_STRANGER | 92.9% | 7.7% | 7.7% | 15.4% | -18.7 | 0.08 | 0.92 | +8.7 | +6.5 |
| `confluence_gte_60` | 10 | S_STRANGER | 71.4% | 0.0% | 0.0% | 10.0% | -23.6 | 0.00 | 0.00 | +6.8 | +5.0 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -73.1 | 0.00 | 0.00 | +11.5 | +1.0 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 14.3% | -19.9 | 0.00 | 0.00 | +6.8 | +7.4 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -10.1 | 0.00 | 0.00 | +5.0 | +12.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 85.7% | 8.3% | 8.3% | 16.7% | -14.2 | 0.12 | 1.16 | +8.5 | +6.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 14.3% | -19.9 | 0.00 | 0.00 | +6.8 | +7.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 92.9% | 7.7% | 7.7% | 15.4% | -13.2 | 0.12 | 1.27 | +8.5 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -17.4 | 0.08 | 1.00 | +8.7 | +6.2 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 14.3% | -7.1 | 0.31 | 1.86 | +10.0 | +7.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -17.6 | 0.00 | 0.00 | +6.8 | +18.0 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=13 Fav=7.7% Avg=-11.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-6.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 13.3% | -14.5 | 0.09 | 1.21 | +10.0 | +22.2 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 13.3% | -14.5 | 0.09 | 1.21 | +10.0 | +22.2 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 13.3% | -14.5 | 0.09 | 1.21 | +10.0 | +22.2 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 13.3% | -14.5 | 0.09 | 1.21 | +10.0 | +22.2 |
| `asian_range_gte_30` | 13 | S_STRANGER | 86.7% | 0.0% | 0.0% | 7.7% | -18.0 | 0.00 | 0.00 | +9.4 | +25.0 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 13.3% | -14.5 | 0.09 | 1.21 | +10.0 | +22.2 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 13.3% | -14.5 | 0.09 | 1.21 | +10.0 | +22.2 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 0.0% | -36.8 | 0.00 | 0.00 | +11.8 | +44.9 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 13.3% | -14.5 | 0.09 | 1.21 | +10.0 | +22.2 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 86.7% | 0.0% | 0.0% | 7.7% | -18.0 | 0.00 | 0.00 | +9.4 | +25.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -46.9 | 0.00 | 0.00 | +14.1 | +57.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 13.3% | -14.5 | 0.09 | 1.21 | +10.0 | +22.2 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 93.3% | 7.1% | 7.1% | 14.3% | -11.1 | 0.13 | 1.50 | +9.4 | +18.2 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 33.3% | -13.1 | 0.00 | 0.00 | +9.6 | +17.0 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 53.3% | 0.0% | 0.0% | 12.5% | -15.6 | 0.00 | 0.00 | +9.5 | +23.2 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-3.8; validation N=7 Fav=14.3% Avg=-1.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 6.2% | 6.2% | 12.5% | -7.4 | 0.13 | 1.76 | +5.1 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 68.8% | 9.1% | 9.1% | 18.2% | -2.5 | 0.38 | 3.46 | +5.5 | +6.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 68.8% | 9.1% | 9.1% | 18.2% | -2.5 | 0.38 | 3.46 | +5.5 | +6.2 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 93.8% | 6.7% | 6.7% | 13.3% | -7.6 | 0.13 | 1.69 | +5.0 | +6.1 |
| `asian_range_gte_30` | 12 | S_STRANGER | 75.0% | 0.0% | 0.0% | 8.3% | -8.5 | 0.00 | 0.00 | +3.9 | +5.9 |
| `confluence_gte_60` | 10 | S_STRANGER | 62.5% | 10.0% | 10.0% | 10.0% | -1.9 | 0.47 | 4.25 | +5.7 | +5.7 |
| `confluence_gte_70` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -11.9 | 0.00 | 0.00 | +6.5 | +2.3 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 62.5% | 10.0% | 10.0% | 10.0% | -4.8 | 0.26 | 2.35 | +5.7 | +6.2 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -6.4 | 0.00 | 0.00 | +8.5 | +8.6 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 50.0% | 0.0% | 0.0% | 12.5% | -2.4 | 0.00 | 0.00 | +4.5 | +5.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 31.2% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +3.9 | +6.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 93.8% | 6.7% | 6.7% | 13.3% | -7.6 | 0.13 | 1.69 | +5.0 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 6.2% | 6.2% | 12.5% | -7.4 | 0.13 | 1.76 | +5.1 | +6.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=10.0% Avg=-2.2; validation N=7 Fav=0.0% Avg=-11.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 17.6% | -6.1 | 0.19 | 2.66 | +6.3 | +11.6 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 52.9% | 0.0% | 0.0% | 22.2% | -5.8 | 0.00 | 0.00 | +5.6 | +7.9 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 70.6% | 0.0% | 0.0% | 16.7% | -9.3 | 0.00 | 0.00 | +4.6 | +13.4 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 17.6% | -6.1 | 0.19 | 2.66 | +6.3 | +11.6 |
| `asian_range_gte_30` | 10 | S_STRANGER | 58.8% | 0.0% | 0.0% | 20.0% | -8.6 | 0.00 | 0.00 | +4.4 | +11.1 |
| `confluence_gte_60` | 5 | S_STRANGER | 29.4% | 0.0% | 0.0% | 20.0% | -10.9 | 0.00 | 0.00 | +3.6 | +14.0 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -8.2 | 0.00 | 0.00 | +2.6 | +10.0 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 82.4% | 0.0% | 0.0% | 7.1% | -9.0 | 0.00 | 0.00 | +4.3 | +13.2 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 29.4% | 0.0% | 0.0% | 0.0% | -14.0 | 0.00 | 0.00 | +4.5 | +22.0 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 41.2% | 0.0% | 0.0% | 28.6% | -6.0 | 0.00 | 0.00 | +5.8 | +8.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 35.3% | 0.0% | 0.0% | 16.7% | -7.0 | 0.00 | 0.00 | +5.6 | +9.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 17.6% | -6.1 | 0.19 | 2.66 | +6.3 | +11.6 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 17.6% | -6.1 | 0.19 | 2.66 | +6.3 | +11.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=14.3% Avg=+0.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 5.3% | 10.5% | 21.1% | -4.8 | 0.22 | 1.52 | +8.4 | +9.8 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 100.0% | 5.3% | 10.5% | 21.1% | -4.8 | 0.22 | 1.52 | +8.4 | +9.8 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 5.3% | 10.5% | 21.1% | -4.8 | 0.22 | 1.52 | +8.4 | +9.8 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 5.3% | 10.5% | 21.1% | -4.8 | 0.22 | 1.52 | +8.4 | +9.8 |
| `asian_range_gte_30` | 16 | S_STRANGER | 84.2% | 6.2% | 12.5% | 25.0% | -4.7 | 0.25 | 1.38 | +9.0 | +10.6 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 5.3% | 10.5% | 21.1% | -4.8 | 0.22 | 1.52 | +8.4 | +9.8 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 5.3% | 10.5% | 21.1% | -4.8 | 0.22 | 1.52 | +8.4 | +9.8 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 36.8% | 14.3% | 14.3% | 42.9% | -2.0 | 0.60 | 2.41 | +14.5 | +5.5 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 36.8% | 14.3% | 14.3% | 57.1% | +0.2 | 1.08 | 3.23 | +16.8 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 84.2% | 6.2% | 12.5% | 25.0% | -4.7 | 0.25 | 1.38 | +9.0 | +10.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 36.8% | 14.3% | 14.3% | 42.9% | -2.0 | 0.60 | 2.41 | +14.5 | +5.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 5.3% | 10.5% | 21.1% | -4.8 | 0.22 | 1.52 | +8.4 | +9.8 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 5.3% | 10.5% | 21.1% | -4.8 | 0.22 | 1.52 | +8.4 | +9.8 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 31.6% | 0.0% | 0.0% | 16.7% | -7.0 | 0.00 | 0.00 | +2.7 | +12.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 15.8% | 0.0% | 0.0% | 66.7% | -4.4 | 0.00 | 0.00 | +13.6 | +6.6 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-1.9; validation N=1 Fav=0.0% Avg=-25.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 5.3% | 15.8% | 0.0% | -8.4 | 0.06 | 0.28 | +5.9 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 47.4% | 0.0% | 22.2% | 0.0% | -13.4 | 0.04 | 0.13 | +3.6 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 57.9% | 0.0% | 18.2% | 0.0% | -13.5 | 0.03 | 0.14 | +4.6 | +5.1 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 5.3% | 15.8% | 0.0% | -8.4 | 0.06 | 0.28 | +5.9 | +5.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 57.9% | 9.1% | 9.1% | 0.0% | -11.8 | 0.04 | 0.33 | +5.2 | +6.6 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -0.1 | 0.00 | 0.00 | +8.6 | +1.0 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 31.6% | 16.7% | 16.7% | 0.0% | -5.8 | 0.12 | 0.62 | +5.4 | +6.6 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 47.4% | 11.1% | 11.1% | 0.0% | -2.0 | 0.22 | 1.52 | +6.6 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 5.3% | 15.8% | 0.0% | -8.4 | 0.06 | 0.28 | +5.9 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 5.3% | 15.8% | 0.0% | -8.4 | 0.06 | 0.28 | +5.9 | +5.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-4.8; validation N=6 Fav=0.0% Avg=-5.5; out_of_sample N=2 Fav=50.0% Avg=-1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 4.5% | 4.5% | 4.5% | -7.8 | 0.00 | 0.03 | +5.5 | +5.8 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 72.7% | 6.2% | 6.2% | 6.2% | -6.7 | 0.00 | 0.04 | +6.1 | +5.9 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 81.8% | 5.6% | 5.6% | 5.6% | -6.9 | 0.00 | 0.04 | +5.9 | +5.6 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 86.4% | 5.3% | 5.3% | 5.3% | -6.5 | 0.00 | 0.04 | +5.7 | +5.5 |
| `asian_range_gte_30` | 17 | S_STRANGER | 77.3% | 0.0% | 0.0% | 5.9% | -9.1 | 0.00 | 0.00 | +5.6 | +5.8 |
| `confluence_gte_60` | 22 | S_STRANGER | 100.0% | 4.5% | 4.5% | 4.5% | -7.8 | 0.00 | 0.03 | +5.5 | +5.8 |
| `confluence_gte_70` | 22 | S_STRANGER | 100.0% | 4.5% | 4.5% | 4.5% | -7.8 | 0.00 | 0.03 | +5.5 | +5.8 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 77.3% | 0.0% | 0.0% | 5.9% | -7.7 | 0.00 | 0.00 | +5.7 | +5.0 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 40.9% | 11.1% | 11.1% | 0.0% | -4.6 | 0.01 | 0.06 | +5.7 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 59.1% | 0.0% | 0.0% | 7.7% | -7.5 | 0.00 | 0.00 | +5.9 | +5.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 50.0% | 0.0% | 0.0% | 9.1% | -7.2 | 0.00 | 0.00 | +6.3 | +5.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 86.4% | 5.3% | 5.3% | 5.3% | -6.5 | 0.00 | 0.04 | +5.7 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 4.5% | 4.5% | 4.5% | -7.8 | 0.00 | 0.03 | +5.5 | +5.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=0.0% Avg=-4.9; validation N=7 Fav=0.0% Avg=-7.7; out_of_sample N=2 Fav=50.0% Avg=+1.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 3.8% | 3.8% | 15.4% | -4.9 | 0.10 | 2.18 | +5.3 | +8.4 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 84.6% | 4.5% | 4.5% | 13.6% | -5.0 | 0.11 | 2.16 | +5.3 | +8.2 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 92.3% | 4.2% | 4.2% | 12.5% | -4.9 | 0.11 | 2.23 | +5.2 | +8.4 |
| `stop_hunt_le_90` | 25 | S_STRANGER | 96.2% | 4.0% | 4.0% | 16.0% | -4.8 | 0.11 | 2.23 | +5.4 | +8.3 |
| `asian_range_gte_30` | 18 | S_STRANGER | 69.2% | 0.0% | 0.0% | 11.1% | -5.4 | 0.00 | 0.00 | +4.3 | +7.8 |
| `confluence_gte_60` | 25 | S_STRANGER | 96.2% | 4.0% | 4.0% | 16.0% | -5.1 | 0.10 | 2.10 | +5.2 | +8.6 |
| `confluence_gte_70` | 7 | S_STRANGER | 26.9% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +5.5 | +7.8 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 57.7% | 6.7% | 6.7% | 13.3% | -5.3 | 0.15 | 1.94 | +4.3 | +8.8 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 65.4% | 5.9% | 5.9% | 17.6% | -3.4 | 0.19 | 2.72 | +6.2 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 65.4% | 0.0% | 0.0% | 11.8% | -5.3 | 0.00 | 0.00 | +4.5 | +7.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -7.5 | 0.00 | 0.00 | +2.7 | +9.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 96.2% | 4.0% | 4.0% | 16.0% | -4.8 | 0.11 | 2.23 | +5.4 | +8.3 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 3.8% | 3.8% | 15.4% | -4.9 | 0.10 | 2.18 | +5.3 | +8.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +5.3 | +4.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -2.3 | 0.00 | 0.00 | +5.7 | +2.6 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=9.1% Avg=-6.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 3.7% | 3.7% | 3.7% | -13.0 | 0.06 | 1.51 | +4.0 | +5.8 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 40.7% | 9.1% | 9.1% | 9.1% | -6.1 | 0.25 | 2.25 | +5.7 | +7.6 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 55.6% | 6.7% | 6.7% | 6.7% | -6.8 | 0.18 | 2.36 | +4.7 | +6.7 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 96.3% | 3.8% | 3.8% | 3.8% | -13.4 | 0.06 | 1.46 | +4.0 | +5.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 29.6% | 0.0% | 0.0% | 0.0% | -10.5 | 0.00 | 0.00 | +2.5 | +7.6 |
| `confluence_gte_70` | 1 | S_STRANGER | 3.7% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +2.6 | +4.7 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 66.7% | 5.6% | 5.6% | 5.6% | -12.6 | 0.09 | 1.45 | +4.9 | +5.9 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +4.8 | +6.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 96.3% | 3.8% | 3.8% | 3.8% | -13.4 | 0.06 | 1.46 | +4.0 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 3.7% | 3.7% | 3.7% | -13.0 | 0.06 | 1.51 | +4.0 | +5.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.5; validation N=3 Fav=33.3% Avg=-1.5; out_of_sample N=9 Fav=0.0% Avg=-15.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 3.4% | 3.4% | 6.9% | -8.9 | 0.00 | 0.01 | +6.0 | +11.4 |
| `hunt_to_ar_ratio_le_2_0` | 29 | S_STRANGER | 100.0% | 3.4% | 3.4% | 6.9% | -8.9 | 0.00 | 0.01 | +6.0 | +11.4 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 100.0% | 3.4% | 3.4% | 6.9% | -8.9 | 0.00 | 0.01 | +6.0 | +11.4 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 100.0% | 3.4% | 3.4% | 6.9% | -8.9 | 0.00 | 0.01 | +6.0 | +11.4 |
| `asian_range_gte_30` | 23 | S_STRANGER | 79.3% | 0.0% | 0.0% | 8.7% | -10.7 | 0.00 | 0.00 | +5.1 | +13.0 |
| `confluence_gte_60` | 29 | S_STRANGER | 100.0% | 3.4% | 3.4% | 6.9% | -8.9 | 0.00 | 0.01 | +6.0 | +11.4 |
| `confluence_gte_70` | 29 | S_STRANGER | 100.0% | 3.4% | 3.4% | 6.9% | -8.9 | 0.00 | 0.01 | +6.0 | +11.4 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 69.0% | 5.0% | 5.0% | 10.0% | -8.1 | 0.00 | 0.01 | +6.6 | +11.6 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 44.8% | 7.7% | 7.7% | 0.0% | -11.5 | 0.00 | 0.01 | +7.4 | +14.9 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 79.3% | 0.0% | 0.0% | 8.7% | -10.7 | 0.00 | 0.00 | +5.1 | +13.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 16 | S_STRANGER | 55.2% | 0.0% | 0.0% | 12.5% | -9.8 | 0.00 | 0.00 | +5.6 | +13.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 100.0% | 3.4% | 3.4% | 6.9% | -8.9 | 0.00 | 0.01 | +6.0 | +11.4 |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 3.4% | 3.4% | 6.9% | -8.9 | 0.00 | 0.01 | +6.0 | +11.4 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 6.9% | 0.0% | 0.0% | 0.0% | -2.1 | 0.00 | 0.00 | +6.6 | +8.7 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=0.0% Avg=-2.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 20.0% | -2.5 | 0.00 | 0.00 | +6.0 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +1.1 | +6.8 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -6.8 | 0.00 | 0.00 | +1.1 | +7.6 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 20.0% | -2.5 | 0.00 | 0.00 | +6.0 | +4.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 22.2% | -2.8 | 0.00 | 0.00 | +6.2 | +5.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +3.5 | +3.6 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +4.1 | +3.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 22.2% | -2.8 | 0.00 | 0.00 | +6.2 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 20.0% | -2.5 | 0.00 | 0.00 | +6.0 | +4.8 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 20.0% | -2.6 | 0.00 | 0.00 | +4.6 | +5.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | +0.0 | 0.00 | 0.00 | +4.4 | +1.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-0.8; validation N=4 Fav=0.0% Avg=-1.6; out_of_sample N=2 Fav=0.0% Avg=-3.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -2.5 | 0.00 | 0.00 | +3.4 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 50.0% | 0.0% | 0.0% | 33.3% | -2.0 | 0.00 | 0.00 | +4.5 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 83.3% | 0.0% | 0.0% | 20.0% | -2.4 | 0.00 | 0.00 | +3.9 | +4.0 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -2.5 | 0.00 | 0.00 | +3.4 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 91.7% | 0.0% | 0.0% | 18.2% | -2.7 | 0.00 | 0.00 | +3.2 | +4.4 |
| `confluence_gte_70` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +1.6 | +2.8 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 0.0% | 0.0% | 25.0% | -1.8 | 0.00 | 0.00 | +4.1 | +3.7 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 0.0% | 0.0% | 16.7% | -2.6 | 0.00 | 0.00 | +3.6 | +3.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 91.7% | 0.0% | 0.0% | 18.2% | -2.7 | 0.00 | 0.00 | +3.2 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -2.5 | 0.00 | 0.00 | +3.4 | +4.1 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +3.1 | +3.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +4.9 | +1.6 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-3.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +2.5 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +3.3 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +2.9 | +5.5 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +2.5 | +5.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +2.6 | +6.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -3.3 | 0.00 | 0.00 | +1.9 | +4.3 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +3.0 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +2.5 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +2.5 | +5.3 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 53.8% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +2.4 | +6.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -3.3 | 0.00 | 0.00 | +2.8 | +6.3 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=0.0% Avg=-2.4; validation N=4 Fav=0.0% Avg=-7.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 30.0% | -4.5 | 0.00 | 0.00 | +6.6 | +8.3 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 33.3% | -4.9 | 0.00 | 0.00 | +6.5 | +8.3 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 33.3% | -4.9 | 0.00 | 0.00 | +6.5 | +8.3 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 30.0% | -4.5 | 0.00 | 0.00 | +6.6 | +8.3 |
| `asian_range_gte_30` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 37.5% | -4.7 | 0.00 | 0.00 | +6.8 | +8.0 |
| `confluence_gte_60` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 28.6% | -5.5 | 0.00 | 0.00 | +5.5 | +9.3 |
| `confluence_gte_70` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 25.0% | -4.3 | 0.00 | 0.00 | +4.7 | +8.6 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 33.3% | -6.1 | 0.00 | 0.00 | +6.9 | +9.2 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 20.0% | -6.4 | 0.00 | 0.00 | +5.9 | +8.5 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 37.5% | -4.7 | 0.00 | 0.00 | +6.8 | +8.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 33.3% | -6.1 | 0.00 | 0.00 | +6.9 | +9.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 30.0% | -4.5 | 0.00 | 0.00 | +6.6 | +8.3 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 30.0% | -4.5 | 0.00 | 0.00 | +6.6 | +8.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=0.0% Avg=-4.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 11.8% | -7.4 | 0.00 | 0.00 | +7.0 | +10.4 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 11.8% | -7.4 | 0.00 | 0.00 | +7.0 | +10.4 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 11.8% | -7.4 | 0.00 | 0.00 | +7.0 | +10.4 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 11.8% | -7.4 | 0.00 | 0.00 | +7.0 | +10.4 |
| `asian_range_gte_30` | 10 | S_STRANGER | 58.8% | 0.0% | 0.0% | 10.0% | -8.7 | 0.00 | 0.00 | +6.2 | +9.1 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 11.8% | -7.4 | 0.00 | 0.00 | +7.0 | +10.4 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 11.8% | -7.4 | 0.00 | 0.00 | +7.0 | +10.4 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 82.4% | 0.0% | 0.0% | 14.3% | -7.5 | 0.00 | 0.00 | +7.9 | +10.6 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 47.1% | 0.0% | 0.0% | 12.5% | -5.8 | 0.00 | 0.00 | +8.8 | +12.3 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 58.8% | 0.0% | 0.0% | 10.0% | -8.7 | 0.00 | 0.00 | +6.2 | +9.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 52.9% | 0.0% | 0.0% | 11.1% | -9.3 | 0.00 | 0.00 | +6.8 | +9.2 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -4.8 | 0.00 | 0.00 | +5.3 | +8.1 |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 11.8% | -7.4 | 0.00 | 0.00 | +7.0 | +10.4 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 11.8% | -7.4 | 0.00 | 0.00 | +7.0 | +10.4 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 41.2% | 0.0% | 0.0% | 14.3% | -4.8 | 0.00 | 0.00 | +4.1 | +7.2 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 23.5% | 0.0% | 0.0% | 0.0% | -7.2 | 0.00 | 0.00 | +6.9 | +11.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=0.0% Avg=-10.7; validation N=4 Fav=0.0% Avg=-15.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 0.0% | 7.1% | 7.1% | -12.6 | 0.05 | 0.64 | +4.1 | +3.5 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -19.0 | 0.00 | 0.00 | +3.0 | +3.3 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 57.1% | 0.0% | 0.0% | 0.0% | -19.0 | 0.00 | 0.00 | +3.6 | +3.2 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 0.0% | 7.1% | 7.1% | -12.6 | 0.05 | 0.64 | +4.1 | +3.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 50.0% | -0.4 | 0.00 | 0.00 | +5.2 | +3.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 71.4% | 0.0% | 10.0% | 10.0% | -12.8 | 0.07 | 0.58 | +4.4 | +3.3 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -10.6 | 0.00 | 0.00 | +1.1 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 0.0% | 7.1% | 7.1% | -12.6 | 0.05 | 0.64 | +4.1 | +3.5 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 0.0% | 7.1% | 7.1% | -12.6 | 0.05 | 0.64 | +4.1 | +3.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=10 Fav=0.0% Avg=-8.6; out_of_sample N=1 Fav=0.0% Avg=-2.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +3.7 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 70.6% | 0.0% | 0.0% | 0.0% | -8.2 | 0.00 | 0.00 | +4.5 | +9.5 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 88.2% | 0.0% | 0.0% | 0.0% | -13.3 | 0.00 | 0.00 | +4.1 | +8.5 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +3.7 | +8.2 |
| `asian_range_gte_30` | 15 | S_STRANGER | 88.2% | 0.0% | 0.0% | 0.0% | -13.3 | 0.00 | 0.00 | +4.1 | +8.5 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +3.7 | +8.2 |
| `confluence_gte_70` | 8 | S_STRANGER | 47.1% | 0.0% | 0.0% | 0.0% | -19.3 | 0.00 | 0.00 | +3.3 | +6.9 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 23.5% | 0.0% | 0.0% | 0.0% | -8.8 | 0.00 | 0.00 | +5.7 | +4.6 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 64.7% | 0.0% | 0.0% | 0.0% | -8.0 | 0.00 | 0.00 | +4.9 | +7.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 70.6% | 0.0% | 0.0% | 0.0% | -8.2 | 0.00 | 0.00 | +4.5 | +9.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +8.2 | +3.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +3.7 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +3.7 | +8.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=0.0% Avg=-9.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.8 | 0.00 | 0.00 | +7.6 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.8 | 0.00 | 0.00 | +7.6 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.8 | 0.00 | 0.00 | +7.6 | +8.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.8 | 0.00 | 0.00 | +7.6 | +8.8 |
| `asian_range_gte_30` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -13.9 | 0.00 | 0.00 | +7.5 | +8.4 |
| `confluence_gte_60` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -9.3 | 0.00 | 0.00 | +7.9 | +11.0 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -13.8 | 0.00 | 0.00 | +14.8 | +16.5 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -13.9 | 0.00 | 0.00 | +7.5 | +8.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -9.7 | 0.00 | 0.00 | +7.9 | +11.4 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -25.7 | 0.00 | 0.00 | +6.9 | +30.1 |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.8 | 0.00 | 0.00 | +7.6 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -12.8 | 0.00 | 0.00 | +7.6 | +8.8 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -17.3 | 0.00 | 0.00 | +9.9 | +9.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -19.0 | 0.00 | 0.00 | +11.3 | +22.3 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=0.0% Avg=-12.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -18.4 | 0.00 | 0.00 | +3.3 | +12.3 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 84.6% | 0.0% | 0.0% | 0.0% | -19.3 | 0.00 | 0.00 | +3.7 | +10.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -18.4 | 0.00 | 0.00 | +3.3 | +12.3 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -18.4 | 0.00 | 0.00 | +3.3 | +12.3 |
| `asian_range_gte_30` | 9 | S_STRANGER | 69.2% | 0.0% | 0.0% | 0.0% | -13.6 | 0.00 | 0.00 | +3.5 | +15.6 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -18.4 | 0.00 | 0.00 | +3.3 | +12.3 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -18.4 | 0.00 | 0.00 | +3.3 | +12.3 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 0.0% | 0.0% | 0.0% | -15.1 | 0.00 | 0.00 | +3.4 | +13.5 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -12.7 | 0.00 | 0.00 | +3.8 | +19.0 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 53.8% | 0.0% | 0.0% | 0.0% | -13.6 | 0.00 | 0.00 | +4.0 | +13.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 53.8% | 0.0% | 0.0% | 0.0% | -13.6 | 0.00 | 0.00 | +4.0 | +13.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 84.6% | 0.0% | 0.0% | 0.0% | -19.3 | 0.00 | 0.00 | +3.7 | +10.5 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -18.4 | 0.00 | 0.00 | +3.3 | +12.3 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 53.8% | 0.0% | 0.0% | 0.0% | -16.2 | 0.00 | 0.00 | +4.0 | +12.1 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 30.8% | 0.0% | 0.0% | 0.0% | -11.7 | 0.00 | 0.00 | +4.0 | +18.1 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=0.0% Avg=-23.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -23.6 | 0.04 | 0.32 | +4.3 | +13.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -23.6 | 0.04 | 0.32 | +4.3 | +13.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -23.6 | 0.04 | 0.32 | +4.3 | +13.0 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -23.6 | 0.04 | 0.32 | +4.3 | +13.0 |
| `asian_range_gte_30` | 9 | S_STRANGER | 90.0% | 0.0% | 11.1% | 0.0% | -24.9 | 0.04 | 0.30 | +3.4 | +12.8 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -23.6 | 0.04 | 0.32 | +4.3 | +13.0 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -23.6 | 0.04 | 0.32 | +4.3 | +13.0 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -12.4 | 0.00 | 0.00 | +5.5 | +17.9 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -12.4 | 0.00 | 0.00 | +5.5 | +17.9 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 0.0% | 11.1% | 0.0% | -24.9 | 0.04 | 0.30 | +3.4 | +12.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -12.8 | 0.00 | 0.00 | +2.1 | +19.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -23.6 | 0.04 | 0.32 | +4.3 | +13.0 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 0.0% | -23.6 | 0.04 | 0.32 | +4.3 | +13.0 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -41.6 | 0.00 | 0.00 | +4.8 | +11.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -10.8 | 0.00 | 0.00 | +8.3 | +16.1 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.8; validation N=3 Fav=0.0% Avg=-8.5; out_of_sample N=1 Fav=0.0% Avg=-16.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 0.0% | 5.0% | 10.0% | -30.2 | 0.00 | 0.01 | +7.7 | +8.5 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 0.0% | 5.6% | 11.1% | -32.1 | 0.00 | 0.01 | +8.4 | +9.0 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 90.0% | 0.0% | 5.6% | 11.1% | -32.1 | 0.00 | 0.01 | +8.4 | +9.0 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 90.0% | 0.0% | 5.6% | 11.1% | -32.1 | 0.00 | 0.01 | +8.4 | +9.0 |
| `asian_range_gte_30` | 16 | S_STRANGER | 80.0% | 0.0% | 6.2% | 12.5% | -26.2 | 0.00 | 0.02 | +6.2 | +7.7 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 0.0% | 5.0% | 10.0% | -30.2 | 0.00 | 0.01 | +7.7 | +8.5 |
| `confluence_gte_70` | 5 | S_STRANGER | 25.0% | 0.0% | 20.0% | 0.0% | -8.6 | 0.01 | 0.05 | +3.9 | +9.7 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -21.2 | 0.00 | 0.00 | +5.6 | +14.8 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -11.6 | 0.00 | 0.00 | +4.8 | +18.4 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 70.0% | 0.0% | 7.1% | 14.3% | -28.1 | 0.00 | 0.01 | +6.9 | +8.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -22.3 | 0.00 | 0.00 | +5.2 | +9.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 90.0% | 0.0% | 5.6% | 11.1% | -32.1 | 0.00 | 0.01 | +8.4 | +9.0 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 0.0% | 5.0% | 10.0% | -30.2 | 0.00 | 0.01 | +7.7 | +8.5 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 15.0% | 0.0% | 0.0% | 66.7% | -0.3 | 0.00 | 0.00 | +11.0 | +2.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -0.8 | 0.00 | 0.00 | +7.6 | +4.2 |

### THE_33_MW|BUY|LATE_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=0.0% Avg=-28.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 0.0% | 15.4% | 15.4% | -32.0 | 0.02 | 0.08 | +9.6 | +9.2 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 0.0% | 15.4% | 15.4% | -32.0 | 0.02 | 0.08 | +9.6 | +9.2 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 0.0% | 15.4% | 15.4% | -32.0 | 0.02 | 0.08 | +9.6 | +9.2 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 0.0% | 15.4% | 15.4% | -32.0 | 0.02 | 0.08 | +9.6 | +9.2 |
| `asian_range_gte_30` | 10 | S_STRANGER | 76.9% | 0.0% | 10.0% | 20.0% | -39.9 | 0.00 | 0.01 | +9.7 | +8.1 |
| `confluence_gte_60` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 69.2% | 0.0% | 11.1% | 22.2% | -28.7 | 0.03 | 0.16 | +10.2 | +11.2 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -16.8 | 0.00 | 0.00 | +17.9 | +30.2 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 76.9% | 0.0% | 10.0% | 20.0% | -39.9 | 0.00 | 0.01 | +9.7 | +8.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 33.3% | -40.2 | 0.00 | 0.00 | +10.7 | +10.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 0.0% | 15.4% | 15.4% | -32.0 | 0.02 | 0.08 | +9.6 | +9.2 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 0.0% | 15.4% | 15.4% | -32.0 | 0.02 | 0.08 | +9.6 | +9.2 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 46.2% | 0.0% | 16.7% | 16.7% | -16.7 | 0.01 | 0.02 | +7.0 | +8.4 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=0.0% Avg=-35.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -35.9 | 0.00 | 0.00 | +7.3 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -35.9 | 0.00 | 0.00 | +7.3 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -35.9 | 0.00 | 0.00 | +7.3 | +6.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -35.9 | 0.00 | 0.00 | +7.3 | +6.7 |
| `asian_range_gte_30` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -39.3 | 0.00 | 0.00 | +5.3 | +6.6 |
| `confluence_gte_60` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -59.4 | 0.00 | 0.00 | +4.7 | +8.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -7.3 | 0.00 | 0.00 | +16.1 | +12.8 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -7.3 | 0.00 | 0.00 | +16.1 | +12.8 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -39.3 | 0.00 | 0.00 | +5.3 | +6.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -6.3 | 0.00 | 0.00 | +5.4 | +15.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -35.9 | 0.00 | 0.00 | +7.3 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -35.9 | 0.00 | 0.00 | +7.3 | +6.7 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -30.9 | 0.00 | 0.00 | +5.5 | +1.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -8.3 | 0.00 | 0.00 | +26.8 | +10.0 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=0.0% Avg=-43.9; out_of_sample N=4 Fav=0.0% Avg=-33.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -42.6 | 0.00 | 0.00 | +6.9 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 93.3% | 0.0% | 0.0% | 0.0% | -41.1 | 0.00 | 0.00 | +6.9 | +5.1 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -42.6 | 0.00 | 0.00 | +6.9 | +5.0 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -42.6 | 0.00 | 0.00 | +6.9 | +5.0 |
| `asian_range_gte_30` | 14 | S_STRANGER | 93.3% | 0.0% | 0.0% | 0.0% | -42.3 | 0.00 | 0.00 | +6.7 | +5.1 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -42.6 | 0.00 | 0.00 | +6.9 | +5.0 |
| `confluence_gte_70` | 12 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -46.4 | 0.00 | 0.00 | +6.7 | +5.8 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +8.4 | +8.2 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +8.4 | +8.2 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 86.7% | 0.0% | 0.0% | 0.0% | -40.6 | 0.00 | 0.00 | +6.7 | +5.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +8.4 | +8.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -42.6 | 0.00 | 0.00 | +6.9 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -42.6 | 0.00 | 0.00 | +6.9 | +5.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
