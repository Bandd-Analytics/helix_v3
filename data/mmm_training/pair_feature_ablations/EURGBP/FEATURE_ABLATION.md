# EURGBP Pair Feature Ablation

Generated: 2026-06-09T15:36:27.397156+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | R_REPEATER | 63.6% | +5.3 | `tdi_rsi_gt_signal` | 9 | R_REPEATER | 66.7% | +4.6 | 47.28 | 15.76 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | R_REPEATER | 50.0% | +8.4 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 66.7% | +12.9 | 19.87 | 9.93 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 42.9% | +2.3 | `hunt_to_ar_ratio_le_2_5` | 7 | R_REPEATER | 57.1% | +3.8 | 3.11 | 2.33 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 42.9% | +1.8 | `all` | 14 | S_STRANGER | 42.9% | +1.8 | 1.89 | 2.51 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 42.1% | +3.9 | `hunt_to_ar_ratio_le_2_0` | 6 | R_REPEATER | 66.7% | +9.0 | 109.40 | 27.35 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 38.9% | +0.2 | `all` | 18 | S_STRANGER | 38.9% | +0.2 | 1.07 | 1.38 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 38.5% | +1.4 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 40.0% | +4.6 | 3.47 | 5.21 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 37.5% | +1.9 | `all` | 16 | S_STRANGER | 37.5% | +1.9 | 2.81 | 3.21 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 16 | S_STRANGER | 37.5% | +0.6 | `tdi_rsi_gt_signal` | 5 | R_REPEATER | 60.0% | +0.7 | 1.82 | 1.22 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 36.4% | +3.0 | `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 42.9% | +3.8 | 2.83 | 3.77 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 36.4% | +2.4 | `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 42.9% | +3.3 | 4.14 | 4.14 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 28 | S_STRANGER | 35.7% | +1.9 | `tdi_rsi_gte_50` | 17 | S_STRANGER | 47.1% | +3.2 | 4.43 | 4.98 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 37 | S_STRANGER | 35.1% | +0.7 | `tdi_rsi_gte_50` | 28 | S_STRANGER | 35.7% | +0.6 | 1.58 | 2.15 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 34.8% | -1.0 | `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 45.5% | -1.6 | 0.47 | 0.57 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 25 | S_STRANGER | 32.0% | +1.0 | `tdi_rsi_gt_signal` | 11 | S_STRANGER | 36.4% | +1.6 | 3.13 | 4.69 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 31.2% | +6.0 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 44.4% | +10.7 | 13.40 | 16.75 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 31.2% | +1.1 | `tdi_rsi_gte_50` | 15 | S_STRANGER | 33.3% | +1.2 | 1.38 | 2.76 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | +2.3 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 42.9% | +3.6 | 2.79 | 3.72 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | +1.6 | `confluence_gte_60` | 8 | S_STRANGER | 37.5% | +2.3 | 2.00 | 3.33 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | +0.0 | `confluence_gte_60` | 8 | S_STRANGER | 37.5% | +0.3 | 1.40 | 1.86 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 30.0% | -2.5 | `all` | 10 | S_STRANGER | 30.0% | -2.5 | 0.44 | 0.66 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 44 | S_STRANGER | 29.5% | -1.9 | `hunt_to_ar_ratio_le_2_0` | 17 | R_REPEATER | 52.9% | +2.5 | 3.52 | 2.47 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 17 | S_STRANGER | 29.4% | +1.3 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 36.4% | +2.7 | 4.55 | 6.83 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 28.6% | +2.6 | `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 33.3% | +3.1 | 3.51 | 6.14 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 28.6% | +1.0 | `all` | 14 | S_STRANGER | 28.6% | +1.0 | 1.58 | 3.94 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | +1.2 | `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 33.3% | +2.6 | 2.56 | 5.12 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L2|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 11 | S_STRANGER | 27.3% | -0.7 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 37.5% | -1.2 | 0.61 | 1.02 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 48 | S_STRANGER | 27.1% | -0.5 | `tdi_rsi_gt_signal` | 41 | S_STRANGER | 26.8% | +0.2 | 1.12 | 2.32 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 30 | S_STRANGER | 26.7% | -0.0 | `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 20.0% | +2.9 | 2.80 | 3.49 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 26.3% | +0.6 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 42.9% | +1.8 | 1.49 | 1.99 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 26.1% | +0.8 | `all` | 23 | S_STRANGER | 26.1% | +0.8 | 1.35 | 3.16 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 23 | S_STRANGER | 26.1% | +0.4 | `confluence_gte_70` | 5 | S_STRANGER | 40.0% | +5.3 | 7.15 | 4.77 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 46 | S_STRANGER | 26.1% | +0.2 | `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 28.6% | +0.3 | 1.26 | 2.52 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 26.1% | -2.5 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 40.0% | -0.3 | 0.82 | 1.24 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | +0.9 | `all` | 12 | S_STRANGER | 25.0% | +0.9 | 1.35 | 2.02 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 25.0% | -0.3 | `all` | 16 | S_STRANGER | 25.0% | -0.3 | 0.84 | 1.84 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 25.0% | -0.8 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 28.6% | +0.0 | 1.00 | 2.00 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 25.0% | -3.8 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 33.3% | +1.1 | 3.03 | 4.55 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 57 | S_STRANGER | 24.6% | -0.1 | `tdi_rsi_gte_50` | 31 | S_STRANGER | 35.5% | +0.0 | 1.02 | 1.76 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 21 | S_STRANGER | 23.8% | +1.0 | `confluence_gte_60` | 14 | S_STRANGER | 28.6% | +1.7 | 1.82 | 2.91 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 21 | S_STRANGER | 23.8% | +0.7 | `all` | 21 | S_STRANGER | 23.8% | +0.7 | 1.50 | 3.50 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 21 | S_STRANGER | 23.8% | +0.4 | `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 31.2% | +1.0 | 1.77 | 2.66 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | S_STRANGER | 23.5% | +0.8 | `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 25.0% | +0.9 | 1.28 | 2.55 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 26 | S_STRANGER | 23.1% | +0.5 | `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 41.7% | +2.9 | 5.17 | 4.31 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 26 | S_STRANGER | 23.1% | -1.5 | `tdi_rsi_gt_signal` | 14 | S_STRANGER | 21.4% | +0.3 | 1.31 | 4.38 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 39 | S_STRANGER | 23.1% | -2.4 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 18.2% | +0.3 | 1.20 | 3.20 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 22 | S_STRANGER | 22.7% | +2.2 | `all` | 22 | S_STRANGER | 22.7% | +2.2 | 2.39 | 6.70 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 44 | S_STRANGER | 22.7% | +0.5 | `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 35.7% | +3.8 | 5.00 | 8.99 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 31 | S_STRANGER | 22.6% | -0.6 | `confluence_gte_60` | 22 | S_STRANGER | 22.7% | -0.0 | 0.98 | 3.15 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 22.2% | +1.4 | `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 28.6% | +2.5 | 3.54 | 8.86 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 22.2% | -1.1 | `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 36.4% | +1.2 | 1.88 | 2.82 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 22.2% | -1.1 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 27.3% | -0.6 | 0.75 | 1.75 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L2|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 18 | S_STRANGER | 22.2% | -1.4 | `tdi_rsi_gt_signal` | 11 | S_STRANGER | 36.4% | -0.5 | 0.80 | 1.40 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 36 | S_STRANGER | 22.2% | -2.4 | `confluence_gte_70` | 6 | S_STRANGER | 33.3% | -0.1 | 0.95 | 1.42 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 54 | S_STRANGER | 22.2% | -2.4 | `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 30.4% | -1.5 | 0.52 | 1.19 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 21.7% | +0.8 | `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 26.7% | +2.8 | 2.68 | 5.36 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 23 | S_STRANGER | 21.7% | +0.3 | `confluence_gte_70` | 5 | R_REPEATER | 60.0% | +6.7 | 10.79 | 7.20 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | -2.9 | `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 30.0% | -1.5 | 0.39 | 0.91 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 61 | S_STRANGER | 21.3% | -1.1 | `confluence_gte_70` | 11 | S_STRANGER | 27.3% | -0.0 | 0.99 | 2.32 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 38 | S_STRANGER | 21.1% | -0.2 | `confluence_gte_60` | 21 | S_STRANGER | 38.1% | +2.4 | 3.36 | 3.73 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 19 | S_STRANGER | 21.1% | -0.6 | `tdi_rsi_gt_signal` | 12 | S_STRANGER | 25.0% | -0.2 | 0.89 | 1.78 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 43 | S_STRANGER | 20.9% | -4.0 | `tdi_rsi_gt_signal` | 26 | S_STRANGER | 30.8% | -3.3 | 0.26 | 0.52 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 24 | S_STRANGER | 20.8% | +0.8 | `confluence_gte_60` | 9 | S_STRANGER | 22.2% | +1.4 | 3.37 | 11.80 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 20.8% | -4.4 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 50.0% | -1.5 | 0.61 | 0.61 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 63 | S_STRANGER | 20.6% | -1.3 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 22.2% | +0.5 | 1.49 | 5.23 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 88 | S_STRANGER | 20.5% | -0.2 | `confluence_gte_70` | 13 | S_STRANGER | 23.1% | +0.9 | 2.18 | 2.62 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 49 | S_STRANGER | 20.4% | -0.7 | `confluence_gte_60` | 31 | S_STRANGER | 22.6% | +0.2 | 1.08 | 2.79 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 31 | S_STRANGER | 19.4% | -1.2 | `confluence_gte_60` | 12 | S_STRANGER | 33.3% | +1.9 | 2.05 | 3.59 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 21 | S_STRANGER | 19.0% | -0.7 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 25.0% | +0.8 | 1.43 | 3.81 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 16 | S_STRANGER | 18.8% | -1.3 | `confluence_gte_60` | 12 | S_STRANGER | 25.0% | -0.2 | 0.90 | 2.41 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 32 | S_STRANGER | 18.8% | -1.3 | `confluence_gte_70` | 21 | S_STRANGER | 19.0% | -1.5 | 0.34 | 1.35 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 27 | S_STRANGER | 18.5% | -0.6 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 40.0% | +2.7 | 2.61 | 3.26 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -1.9 | `confluence_gte_70` | 5 | S_STRANGER | 20.0% | +1.4 | 2.47 | 9.87 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -5.1 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 22.2% | -6.1 | 0.11 | 0.34 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 17.6% | +0.3 | `all` | 17 | S_STRANGER | 17.6% | +0.3 | 1.19 | 5.56 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 17.6% | -1.5 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 20.0% | -1.9 | 0.64 | 2.54 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 57 | S_STRANGER | 17.5% | -1.3 | `confluence_gte_60` | 25 | S_STRANGER | 28.0% | +0.3 | 1.16 | 2.82 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 16.7% | -1.2 | `all` | 12 | S_STRANGER | 16.7% | -1.2 | 0.50 | 2.26 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 30 | S_STRANGER | 16.7% | -1.5 | `tdi_rsi_gte_50` | 15 | S_STRANGER | 20.0% | -1.7 | 0.21 | 0.71 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 16.7% | -1.7 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 20.0% | -0.7 | 0.03 | 0.06 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 18 | S_STRANGER | 16.7% | -2.2 | `confluence_gte_60` | 6 | S_STRANGER | 33.3% | +0.8 | 1.64 | 2.47 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 16.7% | -5.8 | `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 16.7% | -4.1 | 0.15 | 0.73 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -1.6 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 20.0% | -2.4 | 0.31 | 1.23 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 15.4% | -2.6 | `tdi_rsi_gt_signal` | 11 | S_STRANGER | 18.2% | -1.2 | 0.34 | 1.18 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 33 | S_STRANGER | 15.2% | -0.5 | `confluence_gte_70` | 7 | S_STRANGER | 14.3% | +0.8 | 1.95 | 9.73 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 73 | S_STRANGER | 15.1% | -3.5 | `hunt_to_ar_ratio_le_2_5` | 37 | S_STRANGER | 18.9% | -2.2 | 0.31 | 1.07 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 20 | S_STRANGER | 15.0% | +0.9 | `tdi_rsi_gt_signal` | 11 | S_STRANGER | 18.2% | +1.8 | 2.35 | 10.57 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 15.0% | -0.5 | `tdi_rsi_gte_50` | 15 | S_STRANGER | 20.0% | +0.4 | 1.09 | 4.00 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 20 | S_STRANGER | 15.0% | -1.7 | `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 16.7% | -1.7 | 0.48 | 2.41 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 27 | S_STRANGER | 14.8% | -4.0 | `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 16.0% | -4.3 | 0.15 | 0.62 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 15 | S_STRANGER | 13.3% | -1.0 | `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 20.0% | -0.5 | 0.82 | 1.90 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 54 | S_STRANGER | 13.0% | -2.8 | `tdi_rsi_gte_50` | 18 | S_STRANGER | 27.8% | +0.4 | 1.32 | 2.65 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 31 | S_STRANGER | 12.9% | -4.8 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 20.0% | -2.9 | 0.21 | 0.84 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 17 | S_STRANGER | 11.8% | -0.0 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 14.3% | +0.4 | 1.26 | 6.31 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 11.8% | -2.1 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 12.5% | -2.2 | 0.22 | 1.54 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 44 | S_STRANGER | 11.4% | -3.0 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 16.7% | -0.2 | 0.79 | 2.76 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 28 | S_STRANGER | 10.7% | -0.8 | `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 11.8% | +0.2 | 1.08 | 7.04 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -1.2 | `all` | 10 | S_STRANGER | 10.0% | -1.2 | 0.64 | 5.75 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 30 | S_STRANGER | 10.0% | -1.9 | `confluence_gte_70` | 11 | S_STRANGER | 18.2% | +0.4 | 1.16 | 4.05 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 10.0% | -2.1 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 14.3% | -2.2 | 0.28 | 1.68 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 10.0% | -3.0 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 12.5% | -2.2 | 0.34 | 2.39 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L2|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -3.0 | `confluence_gte_60` | 8 | S_STRANGER | 12.5% | -1.8 | 0.16 | 0.95 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -3.1 | `all` | 10 | S_STRANGER | 10.0% | -3.1 | 0.02 | 0.14 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -1.7 | `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 10.0% | -1.5 | 0.38 | 2.63 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -3.8 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 20.0% | -1.5 | 0.04 | 0.15 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 8.3% | +0.0 | `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 16.7% | +1.5 | 2.09 | 8.38 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 24 | S_STRANGER | 8.3% | -1.9 | `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 18.2% | -0.2 | 0.92 | 2.15 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 8.3% | -3.1 | `confluence_gte_60` | 7 | S_STRANGER | 14.3% | -3.3 | 0.19 | 1.16 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 37 | S_STRANGER | 8.1% | -4.1 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 25.0% | -0.1 | 0.94 | 2.34 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 7.7% | -1.5 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 12.5% | -0.7 | 0.42 | 2.50 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 7.7% | -1.7 | `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 20.0% | +0.8 | 1.71 | 5.13 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 7.7% | -2.5 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 12.5% | -1.2 | 0.35 | 2.12 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 7.7% | -3.7 | `tdi_rsi_gt_signal` | 10 | S_STRANGER | 10.0% | -5.3 | 0.02 | 0.17 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 14 | S_STRANGER | 7.1% | -9.8 | `all` | 14 | S_STRANGER | 7.1% | -9.8 | 0.01 | 0.17 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 6.7% | -1.1 | `all` | 15 | S_STRANGER | 6.7% | -1.1 | 0.31 | 0.94 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 6.2% | -2.1 | `confluence_gte_60` | 13 | S_STRANGER | 7.7% | -2.1 | 0.24 | 0.64 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 5.9% | -3.8 | `tdi_rsi_gt_signal` | 16 | S_STRANGER | 6.2% | -3.1 | 0.13 | 1.86 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 34 | S_STRANGER | 5.9% | -4.1 | `confluence_gte_70` | 7 | S_STRANGER | 14.3% | -0.3 | 0.87 | 5.19 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 36 | S_STRANGER | 5.6% | -6.2 | `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 5.6% | -5.7 | 0.10 | 1.36 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 23 | S_STRANGER | 4.3% | -3.5 | `confluence_gte_70` | 5 | S_STRANGER | 20.0% | -8.5 | 0.18 | 0.53 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 25 | S_STRANGER | 4.0% | -9.8 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 16.7% | -1.4 | 0.36 | 1.82 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 0.0% | -1.9 | `confluence_gte_60` | 9 | S_STRANGER | 0.0% | -1.4 | 0.01 | 0.05 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -2.1 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 0.0% | -1.2 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 11 | S_STRANGER | 0.0% | -3.1 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 0.0% | -0.7 | 0.37 | 1.48 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 0.0% | -5.1 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 0.0% | -1.8 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 15 | S_STRANGER | 0.0% | -5.2 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 0.0% | -2.4 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 17 | S_STRANGER | 0.0% | -5.6 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 0.0% | -3.7 | 0.00 | 0.00 | 0 | 0 | fail |

## Candidate Details

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=66.7% Avg=+4.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 27.3% | +5.3 | 33.42 | 14.32 | +10.5 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +13.7 | +16.5 |
| `hunt_to_ar_ratio_le_2_5` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 50.0% | +5.4 | 999.00 | 999.00 | +12.8 | +10.6 |
| `stop_hunt_le_90` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 27.3% | +5.3 | 33.42 | 14.32 | +10.5 | +3.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 27.3% | +5.3 | 33.42 | 14.32 | +10.5 | +3.3 |
| `confluence_gte_70` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 27.3% | +5.3 | 33.42 | 14.32 | +10.5 | +3.3 |
| `tdi_rsi_gt_signal` | 9 | R_REPEATER | 81.8% | 66.7% | 66.7% | 22.2% | +4.6 | 47.28 | 15.76 | +8.5 | +3.9 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 54.5% | 66.7% | 66.7% | 16.7% | +4.5 | 39.71 | 9.93 | +9.1 | +4.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 27.3% | +5.3 | 33.42 | 14.32 | +10.5 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 27.3% | +5.3 | 33.42 | 14.32 | +10.5 | +3.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=66.7% Avg=+12.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.4 | 9.06 | 9.06 | +15.9 | +2.8 |
| `hunt_to_ar_ratio_le_2_0` | 9 | R_REPEATER | 90.0% | 55.6% | 55.6% | 33.3% | +9.6 | 11.78 | 9.43 | +17.5 | +2.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.4 | 9.06 | 9.06 | +15.9 | +2.8 |
| `stop_hunt_le_90` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.4 | 9.06 | 9.06 | +15.9 | +2.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.4 | 9.06 | 9.06 | +15.9 | +2.8 |
| `confluence_gte_70` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.4 | 9.06 | 9.06 | +15.9 | +2.8 |
| `tdi_rsi_gt_signal` | 7 | R_REPEATER | 70.0% | 57.1% | 57.1% | 42.9% | +10.9 | 15.37 | 11.53 | +19.8 | +2.4 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 60.0% | 66.7% | 66.7% | 50.0% | +12.9 | 19.87 | 9.93 | +22.5 | +2.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.4 | 9.06 | 9.06 | +15.9 | +2.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +8.4 | 9.06 | 9.06 | +15.9 | +2.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=60.0% Avg=+3.4; out_of_sample N=2 Fav=50.0% Avg=+4.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 35.7% | +2.3 | 2.65 | 3.09 | +7.1 | +3.1 |
| `hunt_to_ar_ratio_le_2_0` | 6 | R_REPEATER | 42.9% | 50.0% | 50.0% | 33.3% | +3.6 | 2.72 | 2.72 | +10.2 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 7 | R_REPEATER | 50.0% | 57.1% | 57.1% | 28.6% | +3.8 | 3.11 | 2.33 | +9.8 | +3.1 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 35.7% | +2.3 | 2.65 | 3.09 | +7.1 | +3.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 35.7% | +2.3 | 2.65 | 3.09 | +7.1 | +3.1 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 35.7% | +2.3 | 2.65 | 3.09 | +7.1 | +3.1 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 42.9% | 33.3% | 33.3% | 33.3% | +1.6 | 2.42 | 3.63 | +7.5 | +3.3 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 35.7% | 40.0% | 40.0% | 20.0% | +1.7 | 1.61 | 2.41 | +10.2 | +4.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 35.7% | +2.3 | 2.65 | 3.09 | +7.1 | +3.1 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 35.7% | +2.3 | 2.65 | 3.09 | +7.1 | +3.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.5; validation N=9 Fav=55.6% Avg=+0.1; out_of_sample N=4 Fav=25.0% Avg=+6.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 7.1% | +1.8 | 1.89 | 2.51 | +7.5 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 7.1% | +1.8 | 1.89 | 2.51 | +7.5 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 7.1% | +1.8 | 1.89 | 2.51 | +7.5 | +6.5 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 7.1% | +1.8 | 1.89 | 2.51 | +7.5 | +6.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 7.1% | +1.8 | 1.89 | 2.51 | +7.5 | +6.5 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 7.1% | +1.8 | 1.89 | 2.51 | +7.5 | +6.5 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 0.0% | +1.1 | 2.10 | 2.10 | +3.6 | +5.7 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 78.6% | 36.4% | 36.4% | 9.1% | +1.8 | 1.75 | 3.07 | +8.2 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 7.1% | +1.8 | 1.89 | 2.51 | +7.5 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 42.9% | 42.9% | 7.1% | +1.8 | 1.89 | 2.51 | +7.5 | +6.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=66.7% Avg=+9.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 31.6% | +3.9 | 5.01 | 4.38 | +8.3 | +3.4 |
| `hunt_to_ar_ratio_le_2_0` | 6 | R_REPEATER | 31.6% | 66.7% | 66.7% | 50.0% | +9.0 | 109.40 | 27.35 | +12.5 | +3.2 |
| `hunt_to_ar_ratio_le_2_5` | 8 | R_REPEATER | 42.1% | 62.5% | 62.5% | 37.5% | +6.8 | 11.44 | 4.58 | +10.1 | +3.5 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 31.6% | +3.9 | 5.01 | 4.38 | +8.3 | +3.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 31.6% | +3.9 | 5.01 | 4.38 | +8.3 | +3.4 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 31.6% | +3.9 | 5.01 | 4.38 | +8.3 | +3.4 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 36.8% | 28.6% | 28.6% | 28.6% | +2.0 | 2.97 | 4.46 | +7.1 | +3.9 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 47.4% | 22.2% | 22.2% | 11.1% | +0.8 | 1.68 | 4.20 | +6.0 | +3.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 31.6% | +3.9 | 5.01 | 4.38 | +8.3 | +3.4 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 31.6% | +3.9 | 5.01 | 4.38 | +8.3 | +3.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-0.5; validation N=16 Fav=43.8% Avg=+0.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 11.1% | +0.2 | 1.07 | 1.38 | +6.1 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 27.8% | 40.0% | 40.0% | 0.0% | -0.4 | 0.85 | 1.28 | +4.4 | +3.6 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 50.0% | 22.2% | 22.2% | 0.0% | -3.3 | 0.29 | 0.87 | +4.0 | +5.8 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 11.1% | +0.2 | 1.07 | 1.38 | +6.1 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 11.1% | +0.2 | 1.07 | 1.38 | +6.1 | +4.1 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 11.1% | +0.2 | 1.07 | 1.38 | +6.1 | +4.1 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -7.9 | 0.00 | 0.00 | +1.5 | +9.6 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 77.8% | 28.6% | 28.6% | 0.0% | -1.7 | 0.50 | 1.13 | +4.6 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 11.1% | +0.2 | 1.07 | 1.38 | +6.1 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 38.9% | 38.9% | 11.1% | +0.2 | 1.07 | 1.38 | +6.1 | +4.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=33.3% Avg=+3.7; out_of_sample N=2 Fav=50.0% Avg=+5.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +1.4 | 1.76 | 2.82 | +6.0 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 16.7% | +1.3 | 1.64 | 3.28 | +6.1 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +1.4 | 1.76 | 2.82 | +6.0 | +3.7 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +1.4 | 1.76 | 2.82 | +6.0 | +3.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +1.4 | 1.76 | 2.82 | +6.0 | +3.7 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +1.4 | 1.76 | 2.82 | +6.0 | +3.7 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 76.9% | 30.0% | 30.0% | 20.0% | +1.1 | 1.46 | 3.42 | +6.5 | +4.0 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 38.5% | 40.0% | 40.0% | 40.0% | +4.6 | 3.47 | 5.21 | +10.2 | +3.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +1.4 | 1.76 | 2.82 | +6.0 | +3.7 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +1.4 | 1.76 | 2.82 | +6.0 | +3.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=0.0% Avg=+2.4; validation N=13 Fav=46.2% Avg=+1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 12.5% | +1.9 | 2.81 | 3.21 | +6.5 | +4.7 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 31.2% | 20.0% | 40.0% | 0.0% | +1.9 | 2.73 | 4.10 | +6.3 | +3.2 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 50.0% | 25.0% | 37.5% | 0.0% | +0.9 | 1.68 | 2.80 | +5.2 | +3.3 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 12.5% | +1.9 | 2.81 | 3.21 | +6.5 | +4.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 12.5% | +1.9 | 2.81 | 3.21 | +6.5 | +4.7 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 12.5% | +1.9 | 2.81 | 3.21 | +6.5 | +4.7 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 18.8% | 33.3% | 33.3% | 0.0% | +0.5 | 3.33 | 6.67 | +5.2 | +2.7 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 68.8% | 36.4% | 36.4% | 9.1% | +0.9 | 1.64 | 2.46 | +6.0 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 12.5% | +1.9 | 2.81 | 3.21 | +6.5 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 37.5% | 43.8% | 12.5% | +1.9 | 2.81 | 3.21 | +6.5 | +4.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-2.3; validation N=4 Fav=75.0% Avg=+1.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 25.0% | +0.6 | 1.91 | 2.87 | +4.8 | +2.0 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 25.0% | +0.6 | 1.91 | 2.87 | +4.8 | +2.0 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 25.0% | +0.6 | 1.91 | 2.87 | +4.8 | +2.0 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 25.0% | +0.6 | 1.91 | 2.87 | +4.8 | +2.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 50.0% | 37.5% | 37.5% | 25.0% | +1.1 | 2.47 | 4.11 | +5.2 | +1.8 |
| `confluence_gte_70` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -1.7 | 0.00 | 0.00 | +2.2 | +1.9 |
| `tdi_rsi_gt_signal` | 5 | R_REPEATER | 31.2% | 60.0% | 60.0% | 20.0% | +0.7 | 1.82 | 1.22 | +5.4 | +1.9 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 50.0% | 37.5% | 37.5% | 25.0% | +0.7 | 1.73 | 2.89 | +5.0 | +1.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 25.0% | +0.6 | 1.91 | 2.87 | +4.8 | +2.0 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 25.0% | +0.6 | 1.91 | 2.87 | +4.8 | +2.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+5.0; validation N=6 Fav=33.3% Avg=+3.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +3.0 | 2.93 | 4.39 | +10.0 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 14.3% | +3.8 | 2.83 | 3.77 | +10.4 | +3.9 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +3.0 | 2.93 | 4.39 | +10.0 | +3.3 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +3.0 | 2.93 | 4.39 | +10.0 | +3.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +3.0 | 2.93 | 4.39 | +10.0 | +3.3 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +3.0 | 2.93 | 4.39 | +10.0 | +3.3 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 0.0% | +3.4 | 3.67 | 3.67 | +9.6 | +3.0 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 11.1% | +0.1 | 1.07 | 3.22 | +7.5 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +3.0 | 2.93 | 4.39 | +10.0 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +3.0 | 2.93 | 4.39 | +10.0 | +3.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-3.2; validation N=5 Fav=60.0% Avg=+5.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +2.4 | 3.47 | 5.21 | +7.3 | +3.2 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 28.6% | +3.3 | 4.14 | 4.14 | +9.2 | +3.9 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +2.4 | 3.47 | 5.21 | +7.3 | +3.2 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +2.4 | 3.47 | 5.21 | +7.3 | +3.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +2.4 | 3.47 | 5.21 | +7.3 | +3.2 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +2.4 | 3.47 | 5.21 | +7.3 | +3.2 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +2.2 | +2.9 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 0.0% | +3.1 | 3.56 | 5.94 | +6.6 | +3.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +2.4 | 3.47 | 5.21 | +7.3 | +3.2 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +2.4 | 3.47 | 5.21 | +7.3 | +3.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-2.3; validation N=15 Fav=53.3% Avg=+3.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 7.1% | +1.9 | 2.85 | 5.13 | +5.7 | +2.7 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 10.7% | 33.3% | 33.3% | 0.0% | +5.8 | 10.21 | 20.42 | +9.1 | +2.6 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 32.1% | 11.1% | 11.1% | 0.0% | +1.0 | 1.92 | 15.37 | +4.5 | +2.4 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 7.1% | +1.9 | 2.85 | 5.13 | +5.7 | +2.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 7.1% | +1.9 | 2.85 | 5.13 | +5.7 | +2.7 |
| `confluence_gte_70` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 7.1% | +1.9 | 2.85 | 5.13 | +5.7 | +2.7 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 42.9% | 41.7% | 41.7% | 0.0% | +2.6 | 3.92 | 5.48 | +6.2 | +2.2 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 60.7% | 47.1% | 47.1% | 5.9% | +3.2 | 4.43 | 4.98 | +6.8 | +2.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 7.1% | +1.9 | 2.85 | 5.13 | +5.7 | +2.7 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 35.7% | 35.7% | 7.1% | +1.9 | 2.85 | 5.13 | +5.7 | +2.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=20 Fav=40.0% Avg=+0.8; validation N=8 Fav=25.0% Avg=-0.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 35.1% | 37.8% | 16.2% | +0.7 | 1.70 | 2.42 | +3.6 | +2.4 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 37.8% | 28.6% | 35.7% | 14.3% | +0.7 | 1.75 | 2.79 | +2.7 | +2.9 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 40.5% | 26.7% | 33.3% | 13.3% | +0.2 | 1.15 | 2.07 | +2.6 | +3.2 |
| `stop_hunt_le_90` | 37 | S_STRANGER | 100.0% | 35.1% | 37.8% | 16.2% | +0.7 | 1.70 | 2.42 | +3.6 | +2.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 21 | S_STRANGER | 56.8% | 28.6% | 28.6% | 9.5% | -0.2 | 0.82 | 1.91 | +3.2 | +2.2 |
| `confluence_gte_70` | 2 | R_REPEATER | 5.4% | 50.0% | 50.0% | 0.0% | +0.4 | 5.50 | 5.50 | +4.0 | +1.3 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 51.4% | 21.1% | 26.3% | 5.3% | -0.2 | 0.80 | 2.09 | +2.6 | +1.8 |
| `tdi_rsi_gte_50` | 28 | S_STRANGER | 75.7% | 35.7% | 39.3% | 10.7% | +0.6 | 1.58 | 2.15 | +3.3 | +1.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 37 | S_STRANGER | 100.0% | 35.1% | 37.8% | 16.2% | +0.7 | 1.70 | 2.42 | +3.6 | +2.4 |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 35.1% | 37.8% | 16.2% | +0.7 | 1.70 | 2.42 | +3.6 | +2.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=11 Fav=45.5% Avg=-1.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 34.8% | 34.8% | 17.4% | -1.0 | 0.59 | 1.03 | +4.6 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 47.8% | 45.5% | 45.5% | 18.2% | -1.6 | 0.47 | 0.57 | +4.5 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 69.6% | 37.5% | 37.5% | 12.5% | -1.6 | 0.44 | 0.74 | +4.3 | +5.0 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 34.8% | 34.8% | 17.4% | -1.0 | 0.59 | 1.03 | +4.6 | +4.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 34.8% | 34.8% | 17.4% | -1.0 | 0.59 | 1.03 | +4.6 | +4.6 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 34.8% | 34.8% | 17.4% | -1.0 | 0.59 | 1.03 | +4.6 | +4.6 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 43.5% | 40.0% | 40.0% | 0.0% | -1.2 | 0.45 | 0.67 | +5.1 | +4.9 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 56.5% | 30.8% | 30.8% | 7.7% | -1.8 | 0.29 | 0.58 | +4.3 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 34.8% | 34.8% | 17.4% | -1.0 | 0.59 | 1.03 | +4.6 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 34.8% | 34.8% | 17.4% | -1.0 | 0.59 | 1.03 | +4.6 | +4.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+3.4; validation N=6 Fav=33.3% Avg=+0.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 32.0% | 32.0% | 24.0% | +1.0 | 1.90 | 3.55 | +5.0 | +2.4 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 16.0% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +2.3 | +3.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 40.0% | 10.0% | 10.0% | 20.0% | -0.7 | 0.37 | 2.60 | +2.8 | +2.4 |
| `stop_hunt_le_90` | 25 | S_STRANGER | 100.0% | 32.0% | 32.0% | 24.0% | +1.0 | 1.90 | 3.55 | +5.0 | +2.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 60.0% | 33.3% | 33.3% | 33.3% | +1.5 | 2.69 | 4.30 | +6.0 | +2.5 |
| `confluence_gte_70` | 3 | S_STRANGER | 12.0% | 33.3% | 33.3% | 0.0% | -0.7 | 0.53 | 0.53 | +3.0 | +3.0 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 44.0% | 36.4% | 36.4% | 18.2% | +1.6 | 3.13 | 4.69 | +6.1 | +2.0 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 52.0% | 30.8% | 30.8% | 15.4% | +1.1 | 2.13 | 4.26 | +5.6 | +2.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 100.0% | 32.0% | 32.0% | 24.0% | +1.0 | 1.90 | 3.55 | +5.0 | +2.4 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 32.0% | 32.0% | 24.0% | +1.0 | 1.90 | 3.55 | +5.0 | +2.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.2; validation N=8 Fav=50.0% Avg=+12.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +6.0 | 5.24 | 10.49 | +15.3 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 87.5% | 35.7% | 35.7% | 35.7% | +7.0 | 5.76 | 9.21 | +16.9 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +6.0 | 5.24 | 10.49 | +15.3 | +4.3 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +6.0 | 5.24 | 10.49 | +15.3 | +4.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +6.0 | 5.24 | 10.49 | +15.3 | +4.3 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +6.0 | 5.24 | 10.49 | +15.3 | +4.3 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 93.8% | 26.7% | 26.7% | 33.3% | +2.9 | 2.92 | 7.30 | +10.0 | +4.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 56.2% | 44.4% | 44.4% | 33.3% | +10.7 | 13.40 | 16.75 | +21.9 | +3.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +6.0 | 5.24 | 10.49 | +15.3 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +6.0 | 5.24 | 10.49 | +15.3 | +4.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=13 Fav=30.8% Avg=+2.0; out_of_sample N=2 Fav=50.0% Avg=-3.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 12.5% | +1.1 | 1.35 | 2.97 | +7.2 | +6.0 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -4.3 | 0.00 | 0.00 | +1.2 | +5.3 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 0.0% | -2.8 | 0.19 | 0.77 | +2.1 | +5.9 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 12.5% | +1.1 | 1.35 | 2.97 | +7.2 | +6.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 12.5% | +1.1 | 1.35 | 2.97 | +7.2 | +6.0 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 12.5% | +1.1 | 1.35 | 2.97 | +7.2 | +6.0 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 25.0% | 25.0% | 25.0% | 0.0% | -4.2 | 0.17 | 0.50 | +3.4 | +9.0 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 93.8% | 33.3% | 33.3% | 13.3% | +1.2 | 1.38 | 2.76 | +7.6 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 12.5% | +1.1 | 1.35 | 2.97 | +7.2 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 12.5% | +1.1 | 1.35 | 2.97 | +7.2 | +6.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=42.9% Avg=+3.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 20.0% | +2.3 | 2.28 | 2.85 | +6.1 | +3.2 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 20.0% | +2.3 | 2.28 | 2.85 | +6.1 | +3.2 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 20.0% | +2.3 | 2.28 | 2.85 | +6.1 | +3.2 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 20.0% | +2.3 | 2.28 | 2.85 | +6.1 | +3.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 28.6% | +3.3 | 2.37 | 2.37 | +7.3 | +3.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 28.6% | +1.8 | 1.91 | 3.82 | +6.2 | +3.6 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 14.3% | +3.6 | 2.79 | 3.72 | +7.3 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 20.0% | +2.3 | 2.28 | 2.85 | +6.1 | +3.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 20.0% | +2.3 | 2.28 | 2.85 | +6.1 | +3.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+3.5; validation N=5 Fav=20.0% Avg=+1.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +1.6 | 1.76 | 4.11 | +6.6 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -2.7 | 0.00 | 0.00 | +2.7 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -3.3 | 0.00 | 0.00 | +2.1 | +4.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +1.6 | 1.76 | 4.11 | +6.6 | +4.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 25.0% | +2.3 | 2.00 | 3.33 | +7.4 | +4.6 |
| `confluence_gte_70` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +9.4 | 9.17 | 9.17 | +11.2 | +2.5 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 22.2% | +1.2 | 1.54 | 5.38 | +6.7 | +4.1 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +1.6 | 1.76 | 4.11 | +6.6 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +1.6 | 1.76 | 4.11 | +6.6 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +1.6 | 1.76 | 4.11 | +6.6 | +4.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=37.5% Avg=+0.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.0 | 1.03 | 1.71 | +2.9 | +2.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.0 | 1.03 | 1.71 | +2.9 | +2.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.0 | 1.03 | 1.71 | +2.9 | +2.0 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.0 | 1.03 | 1.71 | +2.9 | +2.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 37.5% | +0.3 | 1.40 | 1.86 | +3.5 | +1.9 |
| `confluence_gte_70` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.6 | 0.00 | 0.00 | +1.7 | +2.6 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +0.9 | +3.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 0.0% | -0.9 | 0.10 | 0.49 | +1.5 | +2.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.0 | 1.03 | 1.71 | +2.9 | +2.0 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +0.0 | 1.03 | 1.71 | +2.9 | +2.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=-1.1; out_of_sample N=5 Fav=20.0% Avg=-3.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -2.5 | 0.44 | 0.66 | +3.5 | +3.4 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -2.5 | 0.44 | 0.66 | +3.5 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -2.5 | 0.44 | 0.66 | +3.5 | +3.4 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -2.5 | 0.44 | 0.66 | +3.5 | +3.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -2.5 | 0.44 | 0.66 | +3.5 | +3.4 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -2.5 | 0.44 | 0.66 | +3.5 | +3.4 |
| `tdi_rsi_gt_signal` | 4 | R_RUNNER | 40.0% | 75.0% | 75.0% | 0.0% | -1.6 | 0.74 | 0.25 | +6.5 | +1.7 |
| `tdi_rsi_gte_50` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 0.0% | +2.5 | 1.84 | 0.92 | +6.7 | +3.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -2.5 | 0.44 | 0.66 | +3.5 | +3.4 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 0.0% | -2.5 | 0.44 | 0.66 | +3.5 | +3.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=12 Fav=58.3% Avg=+3.2; out_of_sample N=5 Fav=40.0% Avg=+0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 44 | S_STRANGER | 100.0% | 29.5% | 31.8% | 13.6% | -1.9 | 0.49 | 0.94 | +4.9 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 17 | R_REPEATER | 38.6% | 52.9% | 58.8% | 17.6% | +2.5 | 3.52 | 2.47 | +7.1 | +1.8 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 43.2% | 47.4% | 52.6% | 15.8% | +2.1 | 3.16 | 2.84 | +6.5 | +2.1 |
| `stop_hunt_le_90` | 44 | S_STRANGER | 100.0% | 29.5% | 31.8% | 13.6% | -1.9 | 0.49 | 0.94 | +4.9 | +4.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 44 | S_STRANGER | 100.0% | 29.5% | 31.8% | 13.6% | -1.9 | 0.49 | 0.94 | +4.9 | +4.4 |
| `confluence_gte_70` | 10 | S_STRANGER | 22.7% | 40.0% | 40.0% | 10.0% | -4.6 | 0.34 | 0.43 | +5.4 | +5.5 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 18.2% | 12.5% | 12.5% | 0.0% | -5.3 | 0.20 | 1.39 | +3.1 | +6.0 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 54.5% | 41.7% | 41.7% | 8.3% | +0.2 | 1.06 | 1.49 | +6.3 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 44 | S_STRANGER | 100.0% | 29.5% | 31.8% | 13.6% | -1.9 | 0.49 | 0.94 | +4.9 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 44 | S_STRANGER | 100.0% | 29.5% | 31.8% | 13.6% | -1.9 | 0.49 | 0.94 | +4.9 | +4.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=33.3% Avg=+2.4; validation N=2 Fav=50.0% Avg=+4.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 29.4% | +1.3 | 1.80 | 3.60 | +5.3 | +2.6 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 94.1% | 31.2% | 31.2% | 31.2% | +1.5 | 1.93 | 3.48 | +5.6 | +2.6 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 29.4% | +1.3 | 1.80 | 3.60 | +5.3 | +2.6 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 29.4% | +1.3 | 1.80 | 3.60 | +5.3 | +2.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 52.9% | 11.1% | 11.1% | 33.3% | +0.3 | 1.27 | 7.64 | +4.6 | +2.7 |
| `confluence_gte_70` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +2.1 | +3.2 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 64.7% | 36.4% | 36.4% | 27.3% | +2.1 | 2.61 | 3.91 | +5.9 | +2.9 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 64.7% | 36.4% | 36.4% | 27.3% | +2.7 | 4.55 | 6.83 | +6.1 | +3.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 29.4% | +1.3 | 1.80 | 3.60 | +5.3 | +2.6 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 29.4% | 29.4% | 29.4% | +1.3 | 1.80 | 3.60 | +5.3 | +2.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-4.3; validation N=10 Fav=40.0% Avg=+4.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +2.6 | 3.13 | 7.04 | +6.9 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 85.7% | 33.3% | 33.3% | 25.0% | +3.1 | 3.51 | 6.14 | +7.0 | +3.6 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 30.8% | 30.8% | 23.1% | +2.8 | 3.29 | 6.58 | +7.3 | +3.6 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +2.6 | 3.13 | 7.04 | +6.9 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +2.6 | 3.13 | 7.04 | +6.9 | +3.8 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +2.6 | 3.13 | 7.04 | +6.9 | +3.8 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 85.7% | 25.0% | 25.0% | 8.3% | +0.7 | 1.52 | 4.57 | +4.9 | +4.1 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 92.9% | 23.1% | 23.1% | 15.4% | +2.2 | 2.73 | 8.18 | +6.6 | +4.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +2.6 | 3.13 | 7.04 | +6.9 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +2.6 | 3.13 | 7.04 | +6.9 | +3.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-4.4; validation N=12 Fav=33.3% Avg=+1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +1.0 | 1.58 | 3.94 | +7.3 | +2.8 |
| `hunt_to_ar_ratio_le_2_0` | 4 | R_REPEATER | 28.6% | 50.0% | 50.0% | 25.0% | +0.7 | 1.28 | 1.28 | +8.5 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 4 | R_REPEATER | 28.6% | 50.0% | 50.0% | 25.0% | +0.7 | 1.28 | 1.28 | +8.5 | +4.0 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +1.0 | 1.58 | 3.94 | +7.3 | +2.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +1.0 | 1.58 | 3.94 | +7.3 | +2.8 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +1.0 | 1.58 | 3.94 | +7.3 | +2.8 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 71.4% | 30.0% | 30.0% | 20.0% | -0.5 | 0.78 | 1.82 | +6.1 | +3.1 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 11.1% | -1.7 | 0.30 | 1.03 | +4.0 | +3.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +1.0 | 1.58 | 3.94 | +7.3 | +2.8 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 28.6% | 21.4% | +1.0 | 1.58 | 3.94 | +7.3 | +2.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-7.2; validation N=2 Fav=0.0% Avg=-0.7; out_of_sample N=3 Fav=66.7% Avg=+8.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 0.0% | +1.2 | 1.75 | 3.06 | +6.1 | +4.7 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 0.0% | +2.6 | 2.56 | 5.12 | +9.0 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 0.0% | +2.6 | 2.56 | 5.12 | +9.0 | +4.8 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 0.0% | +1.2 | 1.75 | 3.06 | +6.1 | +4.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 0.0% | +1.2 | 1.75 | 3.06 | +6.1 | +4.7 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 0.0% | +1.2 | 1.75 | 3.06 | +6.1 | +4.7 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 90.9% | 30.0% | 40.0% | 0.0% | +1.6 | 2.01 | 3.01 | +6.6 | +5.0 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 0.0% | +1.6 | 1.89 | 3.78 | +7.0 | +5.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 0.0% | +1.2 | 1.75 | 3.06 | +6.1 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 0.0% | +1.2 | 1.75 | 3.06 | +6.1 | +4.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L2|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L2|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=-2.0; validation N=1 Fav=100.0% Avg=+4.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 18.2% | -0.7 | 0.74 | 1.11 | +5.1 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +0.3 | +9.0 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | -2.8 | 0.47 | 0.94 | +3.6 | +4.1 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 18.2% | -0.7 | 0.74 | 1.11 | +5.1 | +3.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 25.0% | +2.1 | 3.37 | 3.37 | +4.8 | +1.8 |
| `confluence_gte_70` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +0.8 | +2.8 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 12.5% | -1.2 | 0.61 | 1.02 | +3.5 | +3.5 |
| `tdi_rsi_gte_50` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 0.0% | +1.5 | 3.31 | 3.31 | +4.5 | +1.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 18.2% | -0.7 | 0.74 | 1.11 | +5.1 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 18.2% | -0.7 | 0.74 | 1.11 | +5.1 | +3.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=41 Fav=26.8% Avg=+0.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 48 | S_STRANGER | 100.0% | 27.1% | 31.2% | 18.8% | -0.5 | 0.78 | 1.62 | +5.1 | +2.3 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 50.0% | 20.8% | 29.2% | 20.8% | -2.6 | 0.37 | 0.85 | +4.6 | +2.9 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 64.6% | 22.6% | 29.0% | 25.8% | -1.6 | 0.50 | 1.12 | +4.8 | +2.8 |
| `stop_hunt_le_90` | 48 | S_STRANGER | 100.0% | 27.1% | 31.2% | 18.8% | -0.5 | 0.78 | 1.62 | +5.1 | +2.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 35 | S_STRANGER | 72.9% | 20.0% | 25.7% | 20.0% | -0.1 | 0.92 | 2.44 | +5.0 | +2.5 |
| `confluence_gte_70` | 9 | S_STRANGER | 18.8% | 11.1% | 22.2% | 22.2% | +1.6 | 3.52 | 10.55 | +5.0 | +2.3 |
| `tdi_rsi_gt_signal` | 41 | S_STRANGER | 85.4% | 26.8% | 31.7% | 14.6% | +0.2 | 1.12 | 2.32 | +5.0 | +2.3 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 31.2% | 13.3% | 13.3% | 0.0% | -1.0 | 0.36 | 2.31 | +3.7 | +2.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 48 | S_STRANGER | 100.0% | 27.1% | 31.2% | 18.8% | -0.5 | 0.78 | 1.62 | +5.1 | +2.3 |
| `feature_stale_hod_exhaustion_reject` | 48 | S_STRANGER | 100.0% | 27.1% | 31.2% | 18.8% | -0.5 | 0.78 | 1.62 | +5.1 | +2.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=10 Fav=20.0% Avg=+2.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 26.7% | 33.3% | 6.7% | -0.0 | 0.99 | 1.88 | +6.0 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 16.7% | 0.0% | 40.0% | 0.0% | -2.1 | 0.31 | 0.47 | +4.1 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 33.3% | 20.0% | 40.0% | 10.0% | +2.9 | 2.80 | 3.49 | +7.5 | +4.9 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 26.7% | 33.3% | 6.7% | -0.0 | 0.99 | 1.88 | +6.0 | +5.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 30 | S_STRANGER | 100.0% | 26.7% | 33.3% | 6.7% | -0.0 | 0.99 | 1.88 | +6.0 | +5.4 |
| `confluence_gte_70` | 30 | S_STRANGER | 100.0% | 26.7% | 33.3% | 6.7% | -0.0 | 0.99 | 1.88 | +6.0 | +5.4 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 56.7% | 23.5% | 29.4% | 11.8% | -0.1 | 0.98 | 2.16 | +7.2 | +6.1 |
| `tdi_rsi_gte_50` | 21 | S_STRANGER | 70.0% | 28.6% | 28.6% | 9.5% | -0.1 | 0.96 | 2.25 | +6.8 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 100.0% | 26.7% | 33.3% | 6.7% | -0.0 | 0.99 | 1.88 | +6.0 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 26.7% | 33.3% | 6.7% | -0.0 | 0.99 | 1.88 | +6.0 | +5.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=42.9% Avg=+1.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 5.3% | +0.6 | 1.25 | 3.51 | +6.0 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 42.1% | 37.5% | 37.5% | 12.5% | +1.0 | 1.36 | 2.27 | +6.9 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 42.1% | 37.5% | 37.5% | 12.5% | +1.0 | 1.36 | 2.27 | +6.9 | +4.4 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 5.3% | +0.6 | 1.25 | 3.51 | +6.0 | +3.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 5.3% | +0.6 | 1.25 | 3.51 | +6.0 | +3.9 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 5.3% | +0.6 | 1.25 | 3.51 | +6.0 | +3.9 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 36.8% | 42.9% | 42.9% | 0.0% | +1.8 | 1.49 | 1.99 | +10.5 | +5.7 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 89.5% | 23.5% | 23.5% | 5.9% | +0.5 | 1.20 | 3.90 | +6.0 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 5.3% | +0.6 | 1.25 | 3.51 | +6.0 | +3.9 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 5.3% | +0.6 | 1.25 | 3.51 | +6.0 | +3.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=16 Fav=25.0% Avg=+0.4; out_of_sample N=7 Fav=28.6% Avg=+1.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 21.7% | +0.8 | 1.35 | 3.16 | +7.3 | +4.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 43.5% | 20.0% | 20.0% | 10.0% | +0.0 | 1.01 | 3.54 | +7.7 | +3.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 52.2% | 25.0% | 25.0% | 16.7% | +1.4 | 2.03 | 4.74 | +8.7 | +2.8 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 21.7% | +0.8 | 1.35 | 3.16 | +7.3 | +4.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 21.7% | +0.8 | 1.35 | 3.16 | +7.3 | +4.0 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 21.7% | +0.8 | 1.35 | 3.16 | +7.3 | +4.0 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 21.7% | 20.0% | 20.0% | 0.0% | -0.4 | 0.86 | 3.43 | +5.0 | +8.5 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 82.6% | 21.1% | 21.1% | 15.8% | +1.0 | 1.50 | 4.88 | +7.6 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 21.7% | +0.8 | 1.35 | 3.16 | +7.3 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 21.7% | +0.8 | 1.35 | 3.16 | +7.3 | +4.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=25.0% Avg=+3.9; out_of_sample N=1 Fav=100.0% Avg=+10.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 17.4% | +0.4 | 1.21 | 2.60 | +5.7 | +2.9 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 17.4% | +0.4 | 1.21 | 2.60 | +5.7 | +2.9 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 17.4% | +0.4 | 1.21 | 2.60 | +5.7 | +2.9 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 17.4% | +0.4 | 1.21 | 2.60 | +5.7 | +2.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 78.3% | 22.2% | 27.8% | 16.7% | -0.2 | 0.90 | 2.16 | +5.3 | +3.2 |
| `confluence_gte_70` | 5 | S_STRANGER | 21.7% | 40.0% | 60.0% | 40.0% | +5.3 | 7.15 | 4.77 | +8.1 | +2.1 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 17.4% | 25.0% | 25.0% | 25.0% | +3.1 | 2.97 | 8.91 | +5.7 | +3.3 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 73.9% | 29.4% | 29.4% | 17.6% | +0.9 | 1.79 | 3.95 | +6.0 | +3.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 17.4% | +0.4 | 1.21 | 2.60 | +5.7 | +2.9 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 26.1% | 30.4% | 17.4% | +0.4 | 1.21 | 2.60 | +5.7 | +2.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+1.4; validation N=9 Fav=11.1% Avg=-0.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 46 | S_STRANGER | 100.0% | 26.1% | 28.3% | 15.2% | +0.2 | 1.14 | 2.37 | +4.5 | +2.9 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 30.4% | 28.6% | 28.6% | 28.6% | +0.3 | 1.26 | 2.52 | +5.3 | +3.1 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 43.5% | 20.0% | 20.0% | 25.0% | -0.2 | 0.85 | 2.55 | +4.4 | +3.2 |
| `stop_hunt_le_90` | 46 | S_STRANGER | 100.0% | 26.1% | 28.3% | 15.2% | +0.2 | 1.14 | 2.37 | +4.5 | +2.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 39.1% | 27.8% | 27.8% | 22.2% | +1.9 | 2.74 | 4.93 | +5.7 | +2.5 |
| `confluence_gte_70` | 2 | R_RUNNER | 4.3% | 100.0% | 100.0% | 50.0% | +11.2 | 999.00 | 999.00 | +12.4 | +0.4 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 15.2% | 14.3% | 14.3% | 0.0% | -0.5 | 0.54 | 2.70 | +3.3 | +2.2 |
| `tdi_rsi_gte_50` | 34 | S_STRANGER | 73.9% | 23.5% | 23.5% | 11.8% | +0.5 | 1.32 | 3.80 | +4.9 | +3.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 46 | S_STRANGER | 100.0% | 26.1% | 28.3% | 15.2% | +0.2 | 1.14 | 2.37 | +4.5 | +2.9 |
| `feature_stale_hod_exhaustion_reject` | 46 | S_STRANGER | 100.0% | 26.1% | 28.3% | 15.2% | +0.2 | 1.14 | 2.37 | +4.5 | +2.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=66.7% Avg=+1.6; out_of_sample N=2 Fav=0.0% Avg=-3.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 8.7% | -2.5 | 0.45 | 1.26 | +4.7 | +4.7 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 26.1% | 33.3% | 33.3% | 0.0% | -6.7 | 0.15 | 0.31 | +5.4 | +3.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 56.5% | 23.1% | 23.1% | 0.0% | -4.1 | 0.16 | 0.53 | +3.4 | +3.8 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 8.7% | -2.5 | 0.45 | 1.26 | +4.7 | +4.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 8.7% | -2.5 | 0.45 | 1.26 | +4.7 | +4.7 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 8.7% | -2.5 | 0.45 | 1.26 | +4.7 | +4.7 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 21.7% | 40.0% | 40.0% | 0.0% | -0.3 | 0.82 | 1.24 | +3.5 | +3.7 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 87.0% | 30.0% | 30.0% | 10.0% | -0.7 | 0.76 | 1.77 | +5.3 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 8.7% | -2.5 | 0.45 | 1.26 | +4.7 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 8.7% | -2.5 | 0.45 | 1.26 | +4.7 | +4.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=12 Fav=25.0% Avg=+0.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 33.3% | +0.9 | 1.35 | 2.02 | +5.5 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 41.7% | 0.0% | 20.0% | 20.0% | -1.6 | 0.21 | 0.62 | +3.1 | +5.1 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 75.0% | 22.2% | 33.3% | 33.3% | +0.1 | 1.05 | 1.40 | +4.4 | +4.4 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 33.3% | +0.9 | 1.35 | 2.02 | +5.5 | +4.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 33.3% | +0.9 | 1.35 | 2.02 | +5.5 | +4.3 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 33.3% | +0.9 | 1.35 | 2.02 | +5.5 | +4.3 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 33.3% | -5.3 | 0.00 | 0.00 | +2.8 | +6.1 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -7.9 | 0.00 | 0.00 | +1.1 | +8.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 33.3% | +0.9 | 1.35 | 2.02 | +5.5 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 33.3% | +0.9 | 1.35 | 2.02 | +5.5 | +4.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=16 Fav=25.0% Avg=-0.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 25.0% | 31.2% | 6.2% | -0.3 | 0.84 | 1.84 | +4.0 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +1.7 | +6.2 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 81.2% | 15.4% | 23.1% | 0.0% | -1.7 | 0.24 | 0.78 | +3.2 | +4.4 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 25.0% | 31.2% | 6.2% | -0.3 | 0.84 | 1.84 | +4.0 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 25.0% | 31.2% | 6.2% | -0.3 | 0.84 | 1.84 | +4.0 | +4.1 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 25.0% | 31.2% | 6.2% | -0.3 | 0.84 | 1.84 | +4.0 | +4.1 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 18.8% | 0.0% | 0.0% | 0.0% | -2.1 | 0.00 | 0.00 | +2.8 | +3.2 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 75.0% | 25.0% | 33.3% | 0.0% | -0.6 | 0.63 | 1.25 | +3.4 | +3.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 25.0% | 31.2% | 6.2% | -0.3 | 0.84 | 1.84 | +4.0 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 25.0% | 31.2% | 6.2% | -0.3 | 0.84 | 1.84 | +4.0 | +4.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=33.3% Avg=+0.4; out_of_sample N=1 Fav=0.0% Avg=-2.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -0.8 | 0.62 | 0.93 | +5.1 | +3.5 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -0.8 | 0.62 | 0.93 | +5.1 | +3.5 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -0.8 | 0.62 | 0.93 | +5.1 | +3.5 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -0.8 | 0.62 | 0.93 | +5.1 | +3.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -0.8 | 0.62 | 0.93 | +5.1 | +3.5 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -0.8 | 0.62 | 0.93 | +5.1 | +3.5 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 0.0% | -3.6 | 0.20 | 0.80 | +2.7 | +3.7 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 28.6% | +0.0 | 1.00 | 2.00 | +6.5 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -0.8 | 0.62 | 0.93 | +5.1 | +3.5 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -0.8 | 0.62 | 0.93 | +5.1 | +3.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-0.4; validation N=10 Fav=40.0% Avg=+1.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 5.0% | -3.8 | 0.26 | 0.66 | +4.8 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 5.0% | -3.8 | 0.26 | 0.66 | +4.8 | +4.1 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 5.0% | -3.8 | 0.26 | 0.66 | +4.8 | +4.1 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 5.0% | -3.8 | 0.26 | 0.66 | +4.8 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 50.0% | 10.0% | 10.0% | 10.0% | -0.9 | 0.42 | 2.97 | +5.9 | +3.1 |
| `confluence_gte_70` | 2 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +4.0 | +2.8 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 65.0% | 23.1% | 23.1% | 7.7% | -6.3 | 0.15 | 0.44 | +4.7 | +5.2 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 60.0% | 33.3% | 33.3% | 8.3% | +1.1 | 3.03 | 4.55 | +5.7 | +3.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 5.0% | -3.8 | 0.26 | 0.66 | +4.8 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 25.0% | 25.0% | 5.0% | -3.8 | 0.26 | 0.66 | +4.8 | +4.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=22 Fav=36.4% Avg=-0.2; validation N=9 Fav=33.3% Avg=+0.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 57 | S_STRANGER | 100.0% | 24.6% | 33.3% | 10.5% | -0.1 | 0.94 | 1.73 | +4.1 | +3.2 |
| `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 43.9% | 16.0% | 32.0% | 8.0% | -0.8 | 0.64 | 1.21 | +3.6 | +3.3 |
| `hunt_to_ar_ratio_le_2_5` | 33 | S_STRANGER | 57.9% | 21.2% | 33.3% | 12.1% | -0.1 | 0.94 | 1.72 | +4.2 | +3.3 |
| `stop_hunt_le_90` | 57 | S_STRANGER | 100.0% | 24.6% | 33.3% | 10.5% | -0.1 | 0.94 | 1.73 | +4.1 | +3.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 33 | S_STRANGER | 57.9% | 30.3% | 33.3% | 12.1% | +0.5 | 1.54 | 2.93 | +5.0 | +3.1 |
| `confluence_gte_70` | 1 | S_STRANGER | 1.8% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +7.4 | +3.4 |
| `tdi_rsi_gt_signal` | 29 | S_STRANGER | 50.9% | 27.6% | 37.9% | 10.3% | +0.2 | 1.11 | 1.72 | +4.7 | +3.3 |
| `tdi_rsi_gte_50` | 31 | S_STRANGER | 54.4% | 35.5% | 35.5% | 9.7% | +0.0 | 1.02 | 1.76 | +4.7 | +3.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 57 | S_STRANGER | 100.0% | 24.6% | 33.3% | 10.5% | -0.1 | 0.94 | 1.73 | +4.1 | +3.2 |
| `feature_stale_hod_exhaustion_reject` | 57 | S_STRANGER | 100.0% | 24.6% | 33.3% | 10.5% | -0.1 | 0.94 | 1.73 | +4.1 | +3.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=+0.6; validation N=10 Fav=30.0% Avg=+2.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 33.3% | +1.0 | 1.56 | 2.87 | +7.3 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 95.2% | 20.0% | 25.0% | 30.0% | +0.1 | 1.07 | 2.35 | +6.1 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 33.3% | +1.0 | 1.56 | 2.87 | +7.3 | +3.8 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 33.3% | +1.0 | 1.56 | 2.87 | +7.3 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 66.7% | 28.6% | 35.7% | 28.6% | +1.7 | 1.82 | 2.91 | +7.6 | +3.8 |
| `confluence_gte_70` | 2 | R_REPEATER | 9.5% | 50.0% | 50.0% | 50.0% | +5.4 | 2.52 | 2.52 | +16.1 | +4.8 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 47.6% | 20.0% | 30.0% | 20.0% | +1.0 | 1.60 | 2.66 | +7.0 | +3.5 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 66.7% | 7.1% | 14.3% | 7.1% | -0.8 | 0.61 | 3.06 | +4.2 | +4.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 33.3% | +1.0 | 1.56 | 2.87 | +7.3 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 33.3% | +1.0 | 1.56 | 2.87 | +7.3 | +3.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=42.9% Avg=+3.5; validation N=14 Fav=14.3% Avg=-0.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +0.7 | 1.50 | 3.50 | +6.1 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 90.5% | 21.1% | 26.3% | 5.3% | +0.2 | 1.15 | 2.98 | +5.9 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 95.2% | 20.0% | 25.0% | 5.0% | +0.2 | 1.13 | 3.16 | +5.7 | +3.9 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +0.7 | 1.50 | 3.50 | +6.1 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 52.4% | 9.1% | 18.2% | 0.0% | -1.4 | 0.39 | 1.57 | +5.6 | +5.0 |
| `confluence_gte_70` | 3 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +2.6 | +7.6 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 14.3% | 33.3% | 33.3% | 0.0% | +0.6 | 7.33 | 7.33 | +10.8 | +2.6 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 81.0% | 23.5% | 23.5% | 11.8% | +0.9 | 1.80 | 5.40 | +6.3 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +0.7 | 1.50 | 3.50 | +6.1 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +0.7 | 1.50 | 3.50 | +6.1 | +3.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=16 Fav=31.2% Avg=+1.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +0.4 | 1.32 | 2.63 | +5.8 | +3.2 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 76.2% | 31.2% | 37.5% | 6.2% | +1.0 | 1.77 | 2.66 | +6.6 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 76.2% | 31.2% | 37.5% | 6.2% | +1.0 | 1.77 | 2.66 | +6.6 | +3.4 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +0.4 | 1.32 | 2.63 | +5.8 | +3.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +0.4 | 1.32 | 2.63 | +5.8 | +3.2 |
| `confluence_gte_70` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +0.4 | 1.32 | 2.63 | +5.8 | +3.2 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 28.6% | 16.7% | 16.7% | 16.7% | +0.5 | 1.36 | 5.45 | +4.8 | +4.0 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 76.2% | 25.0% | 31.2% | 12.5% | +1.0 | 1.87 | 3.00 | +5.7 | +3.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +0.4 | 1.32 | 2.63 | +5.8 | +3.2 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +0.4 | 1.32 | 2.63 | +5.8 | +3.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=22.2% Avg=-1.6; validation N=7 Fav=28.6% Avg=+4.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 23.5% | 29.4% | 23.5% | +0.8 | 1.24 | 2.73 | +7.1 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 94.1% | 25.0% | 31.2% | 25.0% | +0.9 | 1.28 | 2.55 | +7.4 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 23.5% | 29.4% | 23.5% | +0.8 | 1.24 | 2.73 | +7.1 | +5.5 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 23.5% | 29.4% | 23.5% | +0.8 | 1.24 | 2.73 | +7.1 | +5.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 35.3% | 33.3% | 33.3% | 33.3% | -1.1 | 0.63 | 1.26 | +4.6 | +4.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -0.6 | 0.00 | 0.00 | +5.0 | +3.4 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 47.1% | 12.5% | 12.5% | 12.5% | -5.1 | 0.06 | 0.39 | +5.1 | +8.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 23.5% | 29.4% | 23.5% | +0.8 | 1.24 | 2.73 | +7.1 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 23.5% | 29.4% | 23.5% | +0.8 | 1.24 | 2.73 | +7.1 | +5.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=36.4% Avg=+2.7; validation N=1 Fav=100.0% Avg=+5.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 23.1% | 26.9% | 15.4% | +0.5 | 1.39 | 3.36 | +4.4 | +2.4 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 46.2% | 41.7% | 50.0% | 25.0% | +2.9 | 5.17 | 4.31 | +6.2 | +1.6 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 61.5% | 31.2% | 37.5% | 25.0% | +1.8 | 2.86 | 3.81 | +5.8 | +2.0 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 23.1% | 26.9% | 15.4% | +0.5 | 1.39 | 3.36 | +4.4 | +2.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 34.6% | 33.3% | 33.3% | 22.2% | +0.1 | 1.06 | 1.77 | +4.1 | +2.4 |
| `confluence_gte_70` | 1 | S_STRANGER | 3.8% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +0.8 | +2.8 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 7.7% | 50.0% | 50.0% | 0.0% | +1.1 | 6.50 | 6.50 | +2.5 | +1.5 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 46.2% | 25.0% | 25.0% | 8.3% | +1.7 | 3.12 | 9.37 | +4.7 | +2.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 23.1% | 26.9% | 15.4% | +0.5 | 1.39 | 3.36 | +4.4 | +2.4 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 23.1% | 26.9% | 15.4% | +0.5 | 1.39 | 3.36 | +4.4 | +2.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=14 Fav=21.4% Avg=+0.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 23.1% | 23.1% | 26.9% | -1.5 | 0.51 | 1.35 | +4.3 | +1.7 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 42.3% | 36.4% | 36.4% | 45.5% | -1.8 | 0.58 | 0.73 | +5.8 | +1.6 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 73.1% | 21.1% | 21.1% | 26.3% | -1.4 | 0.51 | 1.39 | +4.3 | +1.7 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 23.1% | 23.1% | 26.9% | -1.5 | 0.51 | 1.35 | +4.3 | +1.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 19 | S_STRANGER | 73.1% | 15.8% | 15.8% | 21.1% | -1.5 | 0.47 | 1.89 | +3.9 | +1.8 |
| `confluence_gte_70` | 4 | R_REPEATER | 15.4% | 50.0% | 50.0% | 25.0% | +4.8 | 12.38 | 6.19 | +8.0 | +2.1 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 53.8% | 21.4% | 21.4% | 14.3% | +0.3 | 1.31 | 4.38 | +3.1 | +1.9 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +1.8 | +2.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 23.1% | 23.1% | 26.9% | -1.5 | 0.51 | 1.35 | +4.3 | +1.7 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 23.1% | 23.1% | 26.9% | -1.5 | 0.51 | 1.35 | +4.3 | +1.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=12.5% Avg=+0.0; out_of_sample N=3 Fav=33.3% Avg=+1.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 39 | S_STRANGER | 100.0% | 23.1% | 28.2% | 15.4% | -2.4 | 0.36 | 0.92 | +3.7 | +2.9 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 33.3% | 23.1% | 23.1% | 15.4% | -1.5 | 0.47 | 1.57 | +3.6 | +3.1 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 41.0% | 18.8% | 18.8% | 12.5% | -1.6 | 0.42 | 1.81 | +3.3 | +3.0 |
| `stop_hunt_le_90` | 39 | S_STRANGER | 100.0% | 23.1% | 28.2% | 15.4% | -2.4 | 0.36 | 0.92 | +3.7 | +2.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 39 | S_STRANGER | 100.0% | 23.1% | 28.2% | 15.4% | -2.4 | 0.36 | 0.92 | +3.7 | +2.9 |
| `confluence_gte_70` | 7 | S_STRANGER | 17.9% | 14.3% | 14.3% | 0.0% | -5.0 | 0.13 | 0.75 | +2.3 | +5.5 |
| `tdi_rsi_gt_signal` | 31 | S_STRANGER | 79.5% | 25.8% | 29.0% | 16.1% | -2.1 | 0.41 | 1.01 | +4.0 | +2.8 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 28.2% | 18.2% | 27.3% | 27.3% | +0.3 | 1.20 | 3.20 | +5.5 | +2.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 39 | S_STRANGER | 100.0% | 23.1% | 28.2% | 15.4% | -2.4 | 0.36 | 0.92 | +3.7 | +2.9 |
| `feature_stale_hod_exhaustion_reject` | 39 | S_STRANGER | 100.0% | 23.1% | 28.2% | 15.4% | -2.4 | 0.36 | 0.92 | +3.7 | +2.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-1.5; validation N=20 Fav=25.0% Avg=+2.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 22.7% | +2.2 | 2.39 | 6.70 | +6.6 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 40.9% | 22.2% | 22.2% | 33.3% | +2.2 | 2.33 | 6.99 | +6.9 | +3.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 45.5% | 20.0% | 20.0% | 30.0% | +1.7 | 2.01 | 7.02 | +6.3 | +3.5 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 22.7% | +2.2 | 2.39 | 6.70 | +6.6 | +3.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 22.7% | +2.2 | 2.39 | 6.70 | +6.6 | +3.3 |
| `confluence_gte_70` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 22.7% | +2.2 | 2.39 | 6.70 | +6.6 | +3.3 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 81.8% | 22.2% | 22.2% | 22.2% | +2.3 | 2.31 | 6.35 | +7.1 | +3.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 40.9% | 22.2% | 22.2% | 11.1% | -0.4 | 0.85 | 2.55 | +5.3 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 22.7% | +2.2 | 2.39 | 6.70 | +6.6 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 22.7% | 22.7% | 22.7% | +2.2 | 2.39 | 6.70 | +6.6 | +3.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-2.7; validation N=9 Fav=55.6% Avg=+6.6; out_of_sample N=4 Fav=0.0% Avg=-1.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 44 | S_STRANGER | 100.0% | 22.7% | 22.7% | 9.1% | +0.5 | 1.28 | 4.24 | +4.0 | +3.5 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 31.8% | 35.7% | 35.7% | 7.1% | +3.8 | 5.00 | 8.99 | +6.7 | +2.7 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 54.5% | 20.8% | 20.8% | 8.3% | +1.7 | 2.74 | 9.85 | +5.0 | +3.2 |
| `stop_hunt_le_90` | 44 | S_STRANGER | 100.0% | 22.7% | 22.7% | 9.1% | +0.5 | 1.28 | 4.24 | +4.0 | +3.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 41 | S_STRANGER | 93.2% | 24.4% | 24.4% | 9.8% | +0.6 | 1.38 | 4.14 | +4.2 | +3.5 |
| `confluence_gte_70` | 17 | S_STRANGER | 38.6% | 23.5% | 23.5% | 11.8% | -1.1 | 0.52 | 1.68 | +2.7 | +2.8 |
| `tdi_rsi_gt_signal` | 26 | S_STRANGER | 59.1% | 19.2% | 19.2% | 3.8% | +0.0 | 1.02 | 4.08 | +3.5 | +4.0 |
| `tdi_rsi_gte_50` | 30 | S_STRANGER | 68.2% | 20.0% | 20.0% | 6.7% | +0.3 | 1.24 | 4.76 | +3.5 | +3.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 44 | S_STRANGER | 100.0% | 22.7% | 22.7% | 9.1% | +0.5 | 1.28 | 4.24 | +4.0 | +3.5 |
| `feature_stale_hod_exhaustion_reject` | 44 | S_STRANGER | 100.0% | 22.7% | 22.7% | 9.1% | +0.5 | 1.28 | 4.24 | +4.0 | +3.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=37.5% Avg=-1.0; validation N=14 Fav=14.3% Avg=+0.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 12.9% | -0.6 | 0.74 | 2.42 | +4.3 | +4.0 |
| `hunt_to_ar_ratio_le_2_0` | 29 | S_STRANGER | 93.5% | 20.7% | 20.7% | 10.3% | -1.5 | 0.38 | 1.47 | +3.4 | +4.1 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 12.9% | -0.6 | 0.74 | 2.42 | +4.3 | +4.0 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 12.9% | -0.6 | 0.74 | 2.42 | +4.3 | +4.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 22 | S_STRANGER | 71.0% | 22.7% | 22.7% | 13.6% | -0.0 | 0.98 | 3.15 | +4.5 | +3.5 |
| `confluence_gte_70` | 3 | R_REPEATER | 9.7% | 66.7% | 66.7% | 66.7% | +9.8 | 294.00 | 147.00 | +13.8 | +2.4 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 19.4% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +1.1 | +6.0 |
| `tdi_rsi_gte_50` | 27 | S_STRANGER | 87.1% | 18.5% | 18.5% | 7.4% | -1.7 | 0.31 | 1.30 | +3.4 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 12.9% | -0.6 | 0.74 | 2.42 | +4.3 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 12.9% | -0.6 | 0.74 | 2.42 | +4.3 | +4.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=33.3% Avg=+5.2; out_of_sample N=4 Fav=25.0% Avg=+0.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +1.4 | 1.59 | 5.55 | +6.2 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 33.3% | 16.7% | 16.7% | 0.0% | -0.2 | 0.81 | 4.04 | +4.3 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 38.9% | 28.6% | 28.6% | 14.3% | +2.5 | 3.54 | 8.86 | +6.5 | +4.4 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +1.4 | 1.59 | 5.55 | +6.2 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +1.4 | 1.59 | 5.55 | +6.2 | +3.8 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +1.4 | 1.59 | 5.55 | +6.2 | +3.8 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 88.9% | 25.0% | 25.0% | 12.5% | +2.0 | 1.88 | 5.63 | +6.7 | +3.3 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 83.3% | 26.7% | 26.7% | 13.3% | +2.8 | 2.63 | 7.25 | +6.9 | +3.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +1.4 | 1.59 | 5.55 | +6.2 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +1.4 | 1.59 | 5.55 | +6.2 | +3.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=44.4% Avg=+1.6; out_of_sample N=2 Fav=0.0% Avg=-0.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | -1.1 | 0.60 | 1.96 | +4.1 | +3.2 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 27.8% | 20.0% | 20.0% | 20.0% | +0.5 | 1.26 | 3.78 | +5.9 | +2.9 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 61.1% | 36.4% | 36.4% | 18.2% | +1.2 | 1.88 | 2.82 | +6.0 | +3.0 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | -1.1 | 0.60 | 1.96 | +4.1 | +3.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | -1.1 | 0.60 | 1.96 | +4.1 | +3.2 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | -1.1 | 0.60 | 1.96 | +4.1 | +3.2 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 94.4% | 23.5% | 23.5% | 11.8% | -0.8 | 0.68 | 2.04 | +4.2 | +3.1 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 38.9% | 28.6% | 28.6% | 14.3% | +0.7 | 1.50 | 2.99 | +5.1 | +2.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | -1.1 | 0.60 | 1.96 | +4.1 | +3.2 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | -1.1 | 0.60 | 1.96 | +4.1 | +3.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=11 Fav=27.3% Avg=-0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 16.7% | -1.1 | 0.61 | 1.84 | +4.4 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 77.8% | 14.3% | 14.3% | 14.3% | -1.9 | 0.35 | 1.73 | +2.9 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 88.9% | 18.8% | 18.8% | 18.8% | -1.3 | 0.58 | 2.11 | +4.5 | +4.6 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 16.7% | -1.1 | 0.61 | 1.84 | +4.4 | +4.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 16.7% | -1.1 | 0.61 | 1.84 | +4.4 | +4.4 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 16.7% | -1.1 | 0.61 | 1.84 | +4.4 | +4.4 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 83.3% | 20.0% | 20.0% | 13.3% | -1.3 | 0.52 | 1.75 | +4.4 | +4.7 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 61.1% | 27.3% | 27.3% | 9.1% | -0.6 | 0.75 | 1.75 | +5.2 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 16.7% | -1.1 | 0.61 | 1.84 | +4.4 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 16.7% | -1.1 | 0.61 | 1.84 | +4.4 | +4.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L2|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L2|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=22.2% Avg=-2.0; validation N=2 Fav=100.0% Avg=+6.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 22.2% | 27.8% | 11.1% | -1.4 | 0.48 | 1.14 | +3.4 | +3.1 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 22.2% | 0.0% | 0.0% | 0.0% | -4.1 | 0.00 | 0.00 | +2.0 | +2.3 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 27.8% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +1.9 | +3.3 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 22.2% | 27.8% | 11.1% | -1.4 | 0.48 | 1.14 | +3.4 | +3.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 38.9% | 14.3% | 28.6% | 14.3% | -1.6 | 0.39 | 0.97 | +3.0 | +3.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 61.1% | 36.4% | 36.4% | 9.1% | -0.5 | 0.80 | 1.40 | +3.7 | +2.8 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 55.6% | 30.0% | 30.0% | 10.0% | -0.5 | 0.74 | 1.72 | +2.8 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 22.2% | 27.8% | 11.1% | -1.4 | 0.48 | 1.14 | +3.4 | +3.1 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 22.2% | 27.8% | 11.1% | -1.4 | 0.48 | 1.14 | +3.4 | +3.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-2.3; validation N=4 Fav=50.0% Avg=+1.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 36 | S_STRANGER | 100.0% | 22.2% | 27.8% | 13.9% | -2.4 | 0.37 | 0.86 | +4.1 | +2.8 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 41.7% | 6.7% | 20.0% | 13.3% | -0.5 | 0.75 | 2.50 | +4.5 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 61.1% | 13.6% | 22.7% | 9.1% | -1.6 | 0.46 | 1.39 | +4.3 | +3.4 |
| `stop_hunt_le_90` | 36 | S_STRANGER | 100.0% | 22.2% | 27.8% | 13.9% | -2.4 | 0.37 | 0.86 | +4.1 | +2.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 44.4% | 25.0% | 31.2% | 12.5% | -0.2 | 0.91 | 1.83 | +5.0 | +2.4 |
| `confluence_gte_70` | 6 | S_STRANGER | 16.7% | 33.3% | 33.3% | 0.0% | -0.1 | 0.95 | 1.42 | +4.5 | +3.5 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 19.4% | 28.6% | 28.6% | 0.0% | -4.1 | 0.24 | 0.48 | +3.3 | +2.3 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 36.1% | 23.1% | 23.1% | 7.7% | -0.7 | 0.65 | 1.74 | +4.0 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 36 | S_STRANGER | 100.0% | 22.2% | 27.8% | 13.9% | -2.4 | 0.37 | 0.86 | +4.1 | +2.8 |
| `feature_stale_hod_exhaustion_reject` | 36 | S_STRANGER | 100.0% | 22.2% | 27.8% | 13.9% | -2.4 | 0.37 | 0.86 | +4.1 | +2.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=17 Fav=35.3% Avg=-1.3; out_of_sample N=6 Fav=16.7% Avg=-2.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 54 | S_STRANGER | 100.0% | 22.2% | 24.1% | 13.0% | -2.4 | 0.37 | 1.04 | +3.3 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 27.8% | 20.0% | 20.0% | 6.7% | -3.3 | 0.22 | 0.86 | +2.5 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 42.6% | 30.4% | 30.4% | 13.0% | -1.5 | 0.52 | 1.19 | +3.6 | +4.6 |
| `stop_hunt_le_90` | 54 | S_STRANGER | 100.0% | 22.2% | 24.1% | 13.0% | -2.4 | 0.37 | 1.04 | +3.3 | +3.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 54 | S_STRANGER | 100.0% | 22.2% | 24.1% | 13.0% | -2.4 | 0.37 | 1.04 | +3.3 | +3.9 |
| `confluence_gte_70` | 17 | S_STRANGER | 31.5% | 23.5% | 29.4% | 5.9% | -1.7 | 0.44 | 0.97 | +3.8 | +3.5 |
| `tdi_rsi_gt_signal` | 28 | S_STRANGER | 51.9% | 17.9% | 17.9% | 14.3% | -2.9 | 0.37 | 1.54 | +3.4 | +3.7 |
| `tdi_rsi_gte_50` | 22 | S_STRANGER | 40.7% | 22.7% | 22.7% | 13.6% | -0.6 | 0.74 | 2.37 | +3.8 | +4.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 54 | S_STRANGER | 100.0% | 22.2% | 24.1% | 13.0% | -2.4 | 0.37 | 1.04 | +3.3 | +3.9 |
| `feature_stale_hod_exhaustion_reject` | 54 | S_STRANGER | 100.0% | 22.2% | 24.1% | 13.0% | -2.4 | 0.37 | 1.04 | +3.3 | +3.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=11 Fav=27.3% Avg=+2.0; out_of_sample N=4 Fav=25.0% Avg=+5.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 13.0% | +0.8 | 1.37 | 3.89 | +5.5 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 47.8% | 18.2% | 27.3% | 9.1% | -0.8 | 0.47 | 1.24 | +3.7 | +3.1 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 65.2% | 26.7% | 33.3% | 20.0% | +2.8 | 2.68 | 5.36 | +7.1 | +3.7 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 13.0% | +0.8 | 1.37 | 3.89 | +5.5 | +4.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 13.0% | +0.8 | 1.37 | 3.89 | +5.5 | +4.4 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 13.0% | +0.8 | 1.37 | 3.89 | +5.5 | +4.4 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 30.4% | 14.3% | 14.3% | 0.0% | -1.6 | 0.29 | 1.73 | +3.2 | +3.5 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 82.6% | 21.1% | 21.1% | 15.8% | +1.3 | 1.55 | 5.82 | +6.2 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 13.0% | +0.8 | 1.37 | 3.89 | +5.5 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 13.0% | +0.8 | 1.37 | 3.89 | +5.5 | +4.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=75.0% Avg=+8.4; out_of_sample N=1 Fav=0.0% Avg=-0.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 13.0% | +0.3 | 1.16 | 4.18 | +4.2 | +2.8 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 30.4% | 42.9% | 42.9% | 42.9% | +4.2 | 5.10 | 6.80 | +8.4 | +2.7 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 47.8% | 27.3% | 27.3% | 27.3% | +1.8 | 2.13 | 5.69 | +5.9 | +3.0 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 13.0% | +0.3 | 1.16 | 4.18 | +4.2 | +2.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 13.0% | +0.3 | 1.16 | 4.18 | +4.2 | +2.8 |
| `confluence_gte_70` | 5 | R_REPEATER | 21.7% | 60.0% | 60.0% | 60.0% | +6.7 | 10.79 | 7.20 | +11.4 | +2.2 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 30.4% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +2.5 | +3.1 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 52.2% | 25.0% | 25.0% | 16.7% | +1.7 | 2.21 | 6.64 | +6.0 | +2.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 13.0% | +0.3 | 1.16 | 4.18 | +4.2 | +2.8 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 13.0% | +0.3 | 1.16 | 4.18 | +4.2 | +2.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=30.0% Avg=-1.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | -2.9 | 0.19 | 0.65 | +3.8 | +5.1 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 50.0% | 28.6% | 28.6% | 28.6% | -1.0 | 0.54 | 1.35 | +4.5 | +3.7 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 71.4% | 30.0% | 30.0% | 20.0% | -1.5 | 0.39 | 0.91 | +3.7 | +4.4 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | -2.9 | 0.19 | 0.65 | +3.8 | +5.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | -2.9 | 0.19 | 0.65 | +3.8 | +5.1 |
| `confluence_gte_70` | 8 | S_STRANGER | 57.1% | 0.0% | 0.0% | 12.5% | -4.7 | 0.00 | 0.00 | +2.7 | +5.2 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +2.0 | +5.5 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 42.9% | 0.0% | 0.0% | 16.7% | -4.9 | 0.00 | 0.00 | +3.9 | +6.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | -2.9 | 0.19 | 0.65 | +3.8 | +5.1 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | -2.9 | 0.19 | 0.65 | +3.8 | +5.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+6.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=20.0% Avg=-0.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 61 | S_STRANGER | 100.0% | 21.3% | 26.2% | 11.5% | -1.1 | 0.48 | 1.23 | +3.8 | +3.5 |
| `hunt_to_ar_ratio_le_2_0` | 36 | S_STRANGER | 59.0% | 11.1% | 16.7% | 11.1% | -2.0 | 0.24 | 1.08 | +3.7 | +3.5 |
| `hunt_to_ar_ratio_le_2_5` | 46 | S_STRANGER | 75.4% | 15.2% | 19.6% | 10.9% | -1.6 | 0.33 | 1.25 | +3.7 | +3.3 |
| `stop_hunt_le_90` | 61 | S_STRANGER | 100.0% | 21.3% | 26.2% | 11.5% | -1.1 | 0.48 | 1.23 | +3.8 | +3.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 48 | S_STRANGER | 78.7% | 14.6% | 18.8% | 8.3% | -1.7 | 0.28 | 1.14 | +3.2 | +3.6 |
| `confluence_gte_70` | 11 | S_STRANGER | 18.0% | 27.3% | 27.3% | 9.1% | -0.0 | 0.99 | 2.32 | +5.2 | +2.8 |
| `tdi_rsi_gt_signal` | 30 | S_STRANGER | 49.2% | 20.0% | 23.3% | 6.7% | -2.1 | 0.28 | 0.81 | +4.1 | +4.1 |
| `tdi_rsi_gte_50` | 28 | S_STRANGER | 45.9% | 17.9% | 17.9% | 3.6% | -2.2 | 0.24 | 1.04 | +3.9 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 61 | S_STRANGER | 100.0% | 21.3% | 26.2% | 11.5% | -1.1 | 0.48 | 1.23 | +3.8 | +3.5 |
| `feature_stale_hod_exhaustion_reject` | 61 | S_STRANGER | 100.0% | 21.3% | 26.2% | 11.5% | -1.1 | 0.48 | 1.23 | +3.8 | +3.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=15 Fav=46.7% Avg=+3.5; validation N=6 Fav=16.7% Avg=-0.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 38 | S_STRANGER | 100.0% | 21.1% | 26.3% | 21.1% | -0.2 | 0.91 | 2.28 | +4.6 | +3.0 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 50.0% | 10.5% | 10.5% | 10.5% | -2.2 | 0.33 | 2.61 | +3.4 | +3.6 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 63.2% | 12.5% | 12.5% | 16.7% | -1.6 | 0.41 | 2.63 | +3.7 | +3.2 |
| `stop_hunt_le_90` | 38 | S_STRANGER | 100.0% | 21.1% | 26.3% | 21.1% | -0.2 | 0.91 | 2.28 | +4.6 | +3.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 21 | S_STRANGER | 55.3% | 38.1% | 42.9% | 33.3% | +2.4 | 3.36 | 3.73 | +6.2 | +2.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 33 | S_STRANGER | 86.8% | 24.2% | 30.3% | 21.2% | +0.1 | 1.06 | 2.22 | +4.8 | +3.2 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 44.7% | 23.5% | 23.5% | 23.5% | +1.2 | 1.57 | 4.71 | +5.8 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 38 | S_STRANGER | 100.0% | 21.1% | 26.3% | 21.1% | -0.2 | 0.91 | 2.28 | +4.6 | +3.0 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 100.0% | 21.1% | 26.3% | 21.1% | -0.2 | 0.91 | 2.28 | +4.6 | +3.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-3.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=30.0% Avg=+0.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 10.5% | -0.6 | 0.73 | 1.91 | +3.8 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 10.5% | -0.6 | 0.73 | 1.91 | +3.8 | +3.3 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 10.5% | -0.6 | 0.73 | 1.91 | +3.8 | +3.3 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 10.5% | -0.6 | 0.73 | 1.91 | +3.8 | +3.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 89.5% | 11.8% | 17.6% | 11.8% | -1.1 | 0.54 | 2.33 | +3.7 | +3.6 |
| `confluence_gte_70` | 3 | S_STRANGER | 15.8% | 0.0% | 0.0% | 0.0% | -3.3 | 0.00 | 0.00 | +2.5 | +4.4 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 63.2% | 25.0% | 33.3% | 8.3% | -0.2 | 0.89 | 1.78 | +4.0 | +3.9 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 42.1% | 12.5% | 12.5% | 0.0% | -1.8 | 0.20 | 1.37 | +2.3 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 10.5% | -0.6 | 0.73 | 1.91 | +3.8 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 21.1% | 26.3% | 10.5% | -0.6 | 0.73 | 1.91 | +3.8 | +3.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=10 Fav=30.0% Avg=-1.2; out_of_sample N=16 Fav=31.2% Avg=-4.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 43 | S_STRANGER | 100.0% | 20.9% | 20.9% | 14.0% | -4.0 | 0.18 | 0.64 | +3.3 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 41.9% | 22.2% | 22.2% | 27.8% | -2.2 | 0.41 | 1.23 | +4.9 | +3.8 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 58.1% | 16.0% | 16.0% | 20.0% | -2.6 | 0.29 | 1.40 | +3.9 | +4.0 |
| `stop_hunt_le_90` | 43 | S_STRANGER | 100.0% | 20.9% | 20.9% | 14.0% | -4.0 | 0.18 | 0.64 | +3.3 | +3.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 43 | S_STRANGER | 100.0% | 20.9% | 20.9% | 14.0% | -4.0 | 0.18 | 0.64 | +3.3 | +3.7 |
| `confluence_gte_70` | 23 | S_STRANGER | 53.5% | 17.4% | 17.4% | 8.7% | -7.0 | 0.05 | 0.24 | +2.5 | +3.4 |
| `tdi_rsi_gt_signal` | 26 | S_STRANGER | 60.5% | 30.8% | 30.8% | 19.2% | -3.3 | 0.26 | 0.52 | +3.9 | +2.7 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 44.2% | 21.1% | 21.1% | 26.3% | -1.0 | 0.54 | 1.76 | +4.7 | +3.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 43 | S_STRANGER | 100.0% | 20.9% | 20.9% | 14.0% | -4.0 | 0.18 | 0.64 | +3.3 | +3.7 |
| `feature_stale_hod_exhaustion_reject` | 43 | S_STRANGER | 100.0% | 20.9% | 20.9% | 14.0% | -4.0 | 0.18 | 0.64 | +3.3 | +3.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+0.5; validation N=4 Fav=25.0% Avg=+2.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 20.8% | 20.8% | 25.0% | +0.8 | 1.89 | 5.67 | +4.6 | +2.9 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 25.0% | 16.7% | 16.7% | 33.3% | +0.2 | 1.18 | 3.53 | +3.8 | +3.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 58.3% | 14.3% | 14.3% | 21.4% | -0.1 | 0.90 | 4.04 | +3.3 | +3.4 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 20.8% | 20.8% | 25.0% | +0.8 | 1.89 | 5.67 | +4.6 | +2.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 37.5% | 22.2% | 22.2% | 11.1% | +1.4 | 3.37 | 11.80 | +4.6 | +1.9 |
| `confluence_gte_70` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +3.3 | +1.2 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 70.8% | 17.6% | 17.6% | 23.5% | +0.3 | 1.27 | 5.07 | +3.8 | +3.4 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 25.0% | 16.7% | 16.7% | 33.3% | -0.0 | 0.96 | 2.87 | +4.1 | +4.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 20.8% | 20.8% | 25.0% | +0.8 | 1.89 | 5.67 | +4.6 | +2.9 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 20.8% | 20.8% | 25.0% | +0.8 | 1.89 | 5.67 | +4.6 | +2.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=66.7% Avg=-0.7; out_of_sample N=3 Fav=33.3% Avg=-2.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 20.8% | 25.0% | 8.3% | -4.4 | 0.21 | 0.56 | +3.7 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 50.0% | 16.7% | 25.0% | 8.3% | -3.2 | 0.26 | 0.78 | +3.7 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 54.2% | 15.4% | 23.1% | 7.7% | -3.1 | 0.25 | 0.83 | +3.6 | +4.6 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 20.8% | 25.0% | 8.3% | -4.4 | 0.21 | 0.56 | +3.7 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 20.8% | 25.0% | 8.3% | -4.4 | 0.21 | 0.56 | +3.7 | +4.1 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 20.8% | 25.0% | 8.3% | -4.4 | 0.21 | 0.56 | +3.7 | +4.1 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 50.0% | 8.3% | 8.3% | 8.3% | -8.5 | 0.04 | 0.40 | +3.5 | +5.4 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 25.0% | 50.0% | 50.0% | 0.0% | -1.5 | 0.61 | 0.61 | +6.5 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 20.8% | 25.0% | 8.3% | -4.4 | 0.21 | 0.56 | +3.7 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 20.8% | 25.0% | 8.3% | -4.4 | 0.21 | 0.56 | +3.7 | +4.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=0.0% Avg=-1.5; out_of_sample N=4 Fav=50.0% Avg=+3.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 63 | S_STRANGER | 100.0% | 20.6% | 23.8% | 12.7% | -1.3 | 0.50 | 1.42 | +4.0 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 33.3% | 14.3% | 19.0% | 9.5% | -0.2 | 0.85 | 3.39 | +4.4 | +3.9 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 39.7% | 16.0% | 20.0% | 8.0% | -0.4 | 0.80 | 3.03 | +4.3 | +4.3 |
| `stop_hunt_le_90` | 63 | S_STRANGER | 100.0% | 20.6% | 23.8% | 12.7% | -1.3 | 0.50 | 1.42 | +4.0 | +3.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 57 | S_STRANGER | 90.5% | 19.3% | 21.1% | 14.0% | -1.4 | 0.50 | 1.66 | +4.0 | +3.8 |
| `confluence_gte_70` | 15 | S_STRANGER | 23.8% | 13.3% | 13.3% | 20.0% | -0.6 | 0.67 | 3.67 | +4.4 | +3.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 14.3% | 22.2% | 22.2% | 11.1% | +0.5 | 1.49 | 5.23 | +3.9 | +2.9 |
| `tdi_rsi_gte_50` | 37 | S_STRANGER | 58.7% | 18.9% | 18.9% | 8.1% | -0.7 | 0.65 | 2.61 | +4.2 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 63 | S_STRANGER | 100.0% | 20.6% | 23.8% | 12.7% | -1.3 | 0.50 | 1.42 | +4.0 | +3.7 |
| `feature_stale_hod_exhaustion_reject` | 63 | S_STRANGER | 100.0% | 20.6% | 23.8% | 12.7% | -1.3 | 0.50 | 1.42 | +4.0 | +3.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=20.0% Avg=-0.8; out_of_sample N=8 Fav=25.0% Avg=+1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 88 | S_STRANGER | 100.0% | 20.5% | 26.1% | 17.0% | -0.2 | 0.87 | 2.20 | +4.2 | +3.0 |
| `hunt_to_ar_ratio_le_2_0` | 37 | S_STRANGER | 42.0% | 18.9% | 29.7% | 24.3% | -0.0 | 0.99 | 2.07 | +5.0 | +3.5 |
| `hunt_to_ar_ratio_le_2_5` | 47 | S_STRANGER | 53.4% | 19.1% | 27.7% | 21.3% | -0.3 | 0.85 | 1.97 | +4.7 | +3.2 |
| `stop_hunt_le_90` | 88 | S_STRANGER | 100.0% | 20.5% | 26.1% | 17.0% | -0.2 | 0.87 | 2.20 | +4.2 | +3.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 76 | S_STRANGER | 86.4% | 19.7% | 25.0% | 15.8% | -0.6 | 0.73 | 1.96 | +4.2 | +3.0 |
| `confluence_gte_70` | 13 | S_STRANGER | 14.8% | 23.1% | 38.5% | 30.8% | +0.9 | 2.18 | 2.62 | +6.6 | +2.7 |
| `tdi_rsi_gt_signal` | 43 | S_STRANGER | 48.9% | 23.3% | 27.9% | 14.0% | -0.1 | 0.97 | 2.17 | +4.4 | +2.8 |
| `tdi_rsi_gte_50` | 34 | S_STRANGER | 38.6% | 20.6% | 20.6% | 17.6% | +0.2 | 1.11 | 3.80 | +4.7 | +3.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 88 | S_STRANGER | 100.0% | 20.5% | 26.1% | 17.0% | -0.2 | 0.87 | 2.20 | +4.2 | +3.0 |
| `feature_stale_hod_exhaustion_reject` | 88 | S_STRANGER | 100.0% | 20.5% | 26.1% | 17.0% | -0.2 | 0.87 | 2.20 | +4.2 | +3.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=18 Fav=33.3% Avg=+1.8; validation N=13 Fav=7.7% Avg=-2.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 49 | S_STRANGER | 100.0% | 20.4% | 20.4% | 12.2% | -0.7 | 0.71 | 2.28 | +5.4 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 38.8% | 21.1% | 21.1% | 15.8% | -1.8 | 0.39 | 1.07 | +5.0 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 42.9% | 23.8% | 23.8% | 19.0% | -0.5 | 0.82 | 1.98 | +5.8 | +4.4 |
| `stop_hunt_le_90` | 49 | S_STRANGER | 100.0% | 20.4% | 20.4% | 12.2% | -0.7 | 0.71 | 2.28 | +5.4 | +4.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 31 | S_STRANGER | 63.3% | 22.6% | 22.6% | 16.1% | +0.2 | 1.08 | 2.79 | +6.2 | +5.1 |
| `confluence_gte_70` | 2 | R_REPEATER | 4.1% | 50.0% | 50.0% | 0.0% | +2.8 | 999.00 | 999.00 | +4.0 | +2.3 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 28.6% | 7.1% | 7.1% | 7.1% | -2.9 | 0.12 | 1.24 | +3.7 | +4.6 |
| `tdi_rsi_gte_50` | 43 | S_STRANGER | 87.8% | 23.3% | 23.3% | 9.3% | -0.3 | 0.88 | 2.55 | +5.4 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 49 | S_STRANGER | 100.0% | 20.4% | 20.4% | 12.2% | -0.7 | 0.71 | 2.28 | +5.4 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 49 | S_STRANGER | 100.0% | 20.4% | 20.4% | 12.2% | -0.7 | 0.71 | 2.28 | +5.4 | +4.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+6.0; validation N=6 Fav=16.7% Avg=-2.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 19.4% | 19.4% | 12.9% | -1.2 | 0.63 | 2.54 | +4.1 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 45.2% | 0.0% | 0.0% | 0.0% | -2.9 | 0.00 | 0.00 | +2.7 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 61.3% | 10.5% | 10.5% | 10.5% | -0.8 | 0.66 | 5.31 | +3.9 | +4.2 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 19.4% | 19.4% | 12.9% | -1.2 | 0.63 | 2.54 | +4.1 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 38.7% | 33.3% | 33.3% | 16.7% | +1.9 | 2.05 | 3.59 | +6.5 | +2.9 |
| `confluence_gte_70` | 5 | S_STRANGER | 16.1% | 20.0% | 20.0% | 0.0% | +0.1 | 1.07 | 3.21 | +6.2 | +2.7 |
| `tdi_rsi_gt_signal` | 27 | S_STRANGER | 87.1% | 22.2% | 22.2% | 14.8% | -0.1 | 0.95 | 3.16 | +4.5 | +4.0 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 61.3% | 21.1% | 21.1% | 10.5% | -1.1 | 0.63 | 2.21 | +4.5 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 19.4% | 19.4% | 12.9% | -1.2 | 0.63 | 2.54 | +4.1 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 19.4% | 19.4% | 12.9% | -1.2 | 0.63 | 2.54 | +4.1 | +3.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=25.0% Avg=+1.3; validation N=4 Fav=25.0% Avg=-0.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 19.0% | 19.0% | 19.0% | -0.7 | 0.69 | 2.77 | +4.1 | +3.4 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 95.2% | 20.0% | 20.0% | 20.0% | -0.6 | 0.73 | 2.72 | +4.2 | +3.5 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 100.0% | 19.0% | 19.0% | 19.0% | -0.7 | 0.69 | 2.77 | +4.1 | +3.4 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 19.0% | 19.0% | 19.0% | -0.7 | 0.69 | 2.77 | +4.1 | +3.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 42.9% | 22.2% | 22.2% | 22.2% | +0.3 | 1.11 | 3.90 | +5.4 | +2.8 |
| `confluence_gte_70` | 1 | R_RUNNER | 4.8% | 100.0% | 100.0% | 100.0% | +14.5 | 999.00 | 999.00 | +16.0 | +1.6 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 81.0% | 23.5% | 23.5% | 23.5% | -0.3 | 0.87 | 2.61 | +4.6 | +3.8 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 57.1% | 25.0% | 25.0% | 25.0% | +0.8 | 1.43 | 3.81 | +5.8 | +4.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 19.0% | 19.0% | 19.0% | -0.7 | 0.69 | 2.77 | +4.1 | +3.4 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 19.0% | 19.0% | 19.0% | -0.7 | 0.69 | 2.77 | +4.1 | +3.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=12 Fav=25.0% Avg=-0.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 25.0% | -1.3 | 0.50 | 1.68 | +3.7 | +3.4 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 25.0% | -1.3 | 0.50 | 1.68 | +3.7 | +3.4 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 25.0% | -1.3 | 0.50 | 1.68 | +3.7 | +3.4 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 25.0% | -1.3 | 0.50 | 1.68 | +3.7 | +3.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 75.0% | 25.0% | 25.0% | 25.0% | -0.2 | 0.90 | 2.41 | +3.9 | +2.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 87.5% | 21.4% | 21.4% | 28.6% | -0.7 | 0.66 | 1.77 | +3.9 | +3.4 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 0.0% | -3.1 | 0.24 | 0.95 | +2.4 | +5.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 25.0% | -1.3 | 0.50 | 1.68 | +3.7 | +3.4 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 25.0% | -1.3 | 0.50 | 1.68 | +3.7 | +3.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=21 Fav=19.0% Avg=-1.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | -1.3 | 0.40 | 1.53 | +3.3 | +3.5 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 40.6% | 7.7% | 7.7% | 7.7% | -1.6 | 0.10 | 1.12 | +2.3 | +3.1 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 59.4% | 15.8% | 15.8% | 10.5% | -1.4 | 0.31 | 1.57 | +2.7 | +3.4 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | -1.3 | 0.40 | 1.53 | +3.3 | +3.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 32 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | -1.3 | 0.40 | 1.53 | +3.3 | +3.5 |
| `confluence_gte_70` | 21 | S_STRANGER | 65.6% | 19.0% | 19.0% | 14.3% | -1.5 | 0.34 | 1.35 | +3.2 | +3.2 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 56.2% | 16.7% | 16.7% | 16.7% | -1.6 | 0.36 | 1.67 | +3.1 | +3.8 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 43.8% | 7.1% | 7.1% | 0.0% | -2.3 | 0.09 | 1.16 | +2.4 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | -1.3 | 0.40 | 1.53 | +3.3 | +3.5 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | -1.3 | 0.40 | 1.53 | +3.3 | +3.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+3.7; validation N=6 Fav=33.3% Avg=+2.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 18.5% | 22.2% | 14.8% | -0.6 | 0.78 | 2.49 | +4.7 | +3.2 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 96.3% | 19.2% | 23.1% | 15.4% | -0.4 | 0.84 | 2.52 | +4.7 | +3.2 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 100.0% | 18.5% | 22.2% | 14.8% | -0.6 | 0.78 | 2.49 | +4.7 | +3.2 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 100.0% | 18.5% | 22.2% | 14.8% | -0.6 | 0.78 | 2.49 | +4.7 | +3.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 63.0% | 17.6% | 17.6% | 11.8% | -1.0 | 0.58 | 2.52 | +3.7 | +3.0 |
| `confluence_gte_70` | 5 | S_STRANGER | 18.5% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +2.7 | +3.7 |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 85.2% | 21.7% | 26.1% | 17.4% | -0.2 | 0.91 | 2.28 | +4.9 | +3.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 37.0% | 40.0% | 40.0% | 20.0% | +2.7 | 2.61 | 3.26 | +7.5 | +2.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 100.0% | 18.5% | 22.2% | 14.8% | -0.6 | 0.78 | 2.49 | +4.7 | +3.2 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 18.5% | 22.2% | 14.8% | -0.6 | 0.78 | 2.49 | +4.7 | +3.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=20.0% Avg=+1.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 9.1% | -1.9 | 0.50 | 2.24 | +4.2 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +3.0 | +2.5 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 0.0% | -1.7 | 0.00 | 0.00 | +2.5 | +3.7 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 9.1% | -1.9 | 0.50 | 2.24 | +4.2 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 9.1% | -1.9 | 0.50 | 2.24 | +4.2 | +3.8 |
| `confluence_gte_70` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | +1.4 | 2.47 | 9.87 | +4.8 | +2.0 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | +0.4 | 1.18 | 4.73 | +4.5 | +5.1 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | +1.2 | 1.43 | 2.86 | +6.1 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 9.1% | -1.9 | 0.50 | 2.24 | +4.2 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 9.1% | -1.9 | 0.50 | 2.24 | +4.2 | +3.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=9 Fav=22.2% Avg=-6.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -5.1 | 0.11 | 0.45 | +3.8 | +2.9 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 33.3% | -6.1 | 0.11 | 0.34 | +3.6 | +2.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 90.9% | 20.0% | 20.0% | 30.0% | -5.6 | 0.11 | 0.39 | +3.9 | +2.9 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -5.1 | 0.11 | 0.45 | +3.8 | +2.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 22.2% | -5.9 | 0.07 | 0.46 | +3.0 | +3.1 |
| `confluence_gte_70` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 50.0% | -0.2 | 0.00 | 0.00 | +2.0 | +5.5 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -0.3 | 0.00 | 0.00 | +3.8 | +4.1 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -0.3 | 0.00 | 0.00 | +3.8 | +4.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -5.1 | 0.11 | 0.45 | +3.8 | +2.9 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 27.3% | -5.1 | 0.11 | 0.45 | +3.8 | +2.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=17 Fav=17.6% Avg=+0.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 5.9% | +0.3 | 1.19 | 5.56 | +5.2 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 23.5% | 0.0% | 0.0% | 0.0% | -1.7 | 0.00 | 0.00 | +2.2 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 29.4% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +2.2 | +3.7 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 5.9% | +0.3 | 1.19 | 5.56 | +5.2 | +4.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 5.9% | +0.3 | 1.19 | 5.56 | +5.2 | +4.9 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 5.9% | +0.3 | 1.19 | 5.56 | +5.2 | +4.9 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 47.1% | 12.5% | 12.5% | 0.0% | -1.5 | 0.16 | 1.13 | +3.2 | +4.4 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 76.5% | 15.4% | 15.4% | 7.7% | +0.2 | 1.08 | 5.95 | +4.5 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 5.9% | +0.3 | 1.19 | 5.56 | +5.2 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 5.9% | +0.3 | 1.19 | 5.56 | +5.2 | +4.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=28.6% Avg=+0.4; out_of_sample N=3 Fav=0.0% Avg=-7.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -1.5 | 0.65 | 3.03 | +5.3 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -1.5 | 0.65 | 3.03 | +5.3 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -1.5 | 0.65 | 3.03 | +5.3 | +6.7 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -1.5 | 0.65 | 3.03 | +5.3 | +6.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -1.5 | 0.65 | 3.03 | +5.3 | +6.7 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -1.5 | 0.65 | 3.03 | +5.3 | +6.7 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 58.8% | 10.0% | 10.0% | 0.0% | -4.7 | 0.06 | 0.51 | +2.8 | +6.9 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 58.8% | 20.0% | 20.0% | 10.0% | -1.9 | 0.64 | 2.54 | +5.9 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -1.5 | 0.65 | 3.03 | +5.3 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -1.5 | 0.65 | 3.03 | +5.3 | +6.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=42.9% Avg=+1.4; validation N=18 Fav=22.2% Avg=-0.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 57 | S_STRANGER | 100.0% | 17.5% | 17.5% | 12.3% | -1.3 | 0.46 | 1.92 | +3.4 | +3.6 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 45.6% | 19.2% | 19.2% | 15.4% | -1.2 | 0.43 | 1.55 | +3.7 | +3.7 |
| `hunt_to_ar_ratio_le_2_5` | 33 | S_STRANGER | 57.9% | 24.2% | 24.2% | 18.2% | -0.4 | 0.76 | 2.10 | +4.2 | +3.5 |
| `stop_hunt_le_90` | 57 | S_STRANGER | 100.0% | 17.5% | 17.5% | 12.3% | -1.3 | 0.46 | 1.92 | +3.4 | +3.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 25 | S_STRANGER | 43.9% | 28.0% | 28.0% | 16.0% | +0.3 | 1.16 | 2.82 | +4.2 | +3.6 |
| `confluence_gte_70` | 3 | R_REPEATER | 5.3% | 66.7% | 66.7% | 33.3% | +1.7 | 2.25 | 1.13 | +5.6 | +2.8 |
| `tdi_rsi_gt_signal` | 29 | S_STRANGER | 50.9% | 20.7% | 20.7% | 6.9% | -1.0 | 0.55 | 2.12 | +3.3 | +3.7 |
| `tdi_rsi_gte_50` | 37 | S_STRANGER | 64.9% | 18.9% | 18.9% | 8.1% | -1.2 | 0.48 | 1.84 | +3.5 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 57 | S_STRANGER | 100.0% | 17.5% | 17.5% | 12.3% | -1.3 | 0.46 | 1.92 | +3.4 | +3.6 |
| `feature_stale_hod_exhaustion_reject` | 57 | S_STRANGER | 100.0% | 17.5% | 17.5% | 12.3% | -1.3 | 0.46 | 1.92 | +3.4 | +3.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=12.5% Avg=-0.2; out_of_sample N=4 Fav=25.0% Avg=-3.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -1.2 | 0.50 | 2.26 | +3.5 | +3.6 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +2.2 | +7.8 |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +1.7 | +7.1 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -1.2 | 0.50 | 2.26 | +3.5 | +3.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -1.2 | 0.50 | 2.26 | +3.5 | +3.6 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -1.2 | 0.50 | 2.26 | +3.5 | +3.6 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 0.0% | -2.3 | 0.16 | 1.15 | +2.5 | +3.8 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 12.5% | -1.4 | 0.50 | 3.48 | +4.0 | +3.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -1.2 | 0.50 | 2.26 | +3.5 | +3.6 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -1.2 | 0.50 | 2.26 | +3.5 | +3.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=15 Fav=20.0% Avg=-1.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 16.7% | 20.0% | 10.0% | -1.5 | 0.21 | 0.75 | +3.0 | +3.5 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 53.3% | 6.2% | 12.5% | 18.8% | -1.7 | 0.10 | 0.59 | +3.5 | +3.2 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 80.0% | 8.3% | 12.5% | 12.5% | -1.7 | 0.12 | 0.71 | +2.9 | +3.2 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 16.7% | 20.0% | 10.0% | -1.5 | 0.21 | 0.75 | +3.0 | +3.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 27 | S_STRANGER | 90.0% | 14.8% | 18.5% | 7.4% | -1.8 | 0.17 | 0.66 | +2.8 | +3.7 |
| `confluence_gte_70` | 8 | S_STRANGER | 26.7% | 12.5% | 25.0% | 12.5% | -0.8 | 0.28 | 0.69 | +3.4 | +1.6 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 10.0% | 33.3% | 33.3% | 0.0% | -0.3 | 0.69 | 1.38 | +4.0 | +2.0 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 50.0% | 20.0% | 20.0% | 6.7% | -1.7 | 0.21 | 0.71 | +2.8 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 100.0% | 16.7% | 20.0% | 10.0% | -1.5 | 0.21 | 0.75 | +3.0 | +3.5 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 16.7% | 20.0% | 10.0% | -1.5 | 0.21 | 0.75 | +3.0 | +3.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=25.0% Avg=+0.0; out_of_sample N=1 Fav=0.0% Avg=-3.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.26 | 1.04 | +4.0 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.26 | 1.04 | +4.0 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.26 | 1.04 | +4.0 | +6.5 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.26 | 1.04 | +4.0 | +6.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.26 | 1.04 | +4.0 | +6.5 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.26 | 1.04 | +4.0 | +6.5 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 0.0% | -1.1 | 0.61 | 1.23 | +4.1 | +10.3 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 0.0% | -0.7 | 0.03 | 0.06 | +4.3 | +5.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.26 | 1.04 | +4.0 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.26 | 1.04 | +4.0 | +6.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=100.0% Avg=+6.0; validation N=4 Fav=0.0% Avg=-1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 22.2% | -2.2 | 0.26 | 1.04 | +3.5 | +2.5 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 88.9% | 12.5% | 12.5% | 25.0% | -2.6 | 0.16 | 0.90 | +3.5 | +2.4 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 94.4% | 11.8% | 11.8% | 23.5% | -2.6 | 0.15 | 0.92 | +3.4 | +2.4 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 22.2% | -2.2 | 0.26 | 1.04 | +3.5 | +2.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 33.3% | 33.3% | 33.3% | 16.7% | +0.8 | 1.64 | 2.47 | +3.4 | +2.2 |
| `confluence_gte_70` | 2 | R_REPEATER | 11.1% | 50.0% | 50.0% | 50.0% | +1.4 | 1.80 | 1.80 | +4.5 | +1.9 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +4.7 | +1.7 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 38.9% | 14.3% | 14.3% | 0.0% | -0.9 | 0.47 | 2.36 | +3.2 | +3.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 22.2% | -2.2 | 0.26 | 1.04 | +3.5 | +2.5 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 22.2% | -2.2 | 0.26 | 1.04 | +3.5 | +2.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=16.7% Avg=-4.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -5.8 | 0.10 | 0.48 | +3.0 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 0.0% | -4.1 | 0.15 | 0.73 | +2.4 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 0.0% | -4.3 | 0.11 | 0.75 | +2.0 | +5.1 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -5.8 | 0.10 | 0.48 | +3.0 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -5.8 | 0.10 | 0.48 | +3.0 | +3.8 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -5.8 | 0.10 | 0.48 | +3.0 | +3.8 |
| `tdi_rsi_gt_signal` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 0.0% | -2.7 | 0.28 | 0.83 | +3.0 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -5.8 | 0.10 | 0.48 | +3.0 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -5.8 | 0.10 | 0.48 | +3.0 | +3.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-12.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=25.0% Avg=+0.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 7.7% | -1.6 | 0.32 | 1.08 | +4.2 | +3.2 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 16.7% | 25.0% | 8.3% | -1.3 | 0.38 | 1.15 | +4.2 | +3.1 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 7.7% | -1.6 | 0.32 | 1.08 | +4.2 | +3.2 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 7.7% | -1.6 | 0.32 | 1.08 | +4.2 | +3.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 76.9% | 10.0% | 20.0% | 0.0% | -2.3 | 0.23 | 0.94 | +2.9 | +3.6 |
| `confluence_gte_70` | 2 | S_STRANGER | 15.4% | 0.0% | 50.0% | 0.0% | -0.3 | 0.74 | 0.74 | +1.9 | +1.4 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +0.9 | +3.7 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 0.0% | -2.4 | 0.31 | 1.23 | +3.4 | +5.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 7.7% | -1.6 | 0.32 | 1.08 | +4.2 | +3.2 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 7.7% | -1.6 | 0.32 | 1.08 | +4.2 | +3.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=11 Fav=18.2% Avg=-1.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.6 | 0.17 | 0.66 | +3.8 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +3.2 | +3.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 10.0% | -1.1 | 0.29 | 1.75 | +4.0 | +3.6 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.6 | 0.17 | 0.66 | +3.8 | +3.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.6 | 0.17 | 0.66 | +3.8 | +3.7 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.6 | 0.17 | 0.66 | +3.8 | +3.7 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 18.2% | 18.2% | 9.1% | -1.2 | 0.34 | 1.18 | +4.2 | +4.0 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 0.0% | -1.0 | 0.38 | 0.76 | +3.7 | +3.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.6 | 0.17 | 0.66 | +3.8 | +3.7 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -2.6 | 0.17 | 0.66 | +3.8 | +3.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=14.3% Avg=+0.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | S_STRANGER | 100.0% | 15.2% | 15.2% | 12.1% | -0.5 | 0.76 | 4.10 | +4.0 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 45.5% | 13.3% | 13.3% | 6.7% | -0.9 | 0.53 | 3.44 | +3.4 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 69.7% | 13.0% | 13.0% | 13.0% | -0.5 | 0.76 | 4.82 | +3.9 | +4.2 |
| `stop_hunt_le_90` | 33 | S_STRANGER | 100.0% | 15.2% | 15.2% | 12.1% | -0.5 | 0.76 | 4.10 | +4.0 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 33 | S_STRANGER | 100.0% | 15.2% | 15.2% | 12.1% | -0.5 | 0.76 | 4.10 | +4.0 | +4.1 |
| `confluence_gte_70` | 7 | S_STRANGER | 21.2% | 14.3% | 14.3% | 28.6% | +0.8 | 1.95 | 9.73 | +4.4 | +3.9 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 48.5% | 12.5% | 12.5% | 6.2% | -1.2 | 0.22 | 1.43 | +2.9 | +4.2 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 39.4% | 7.7% | 7.7% | 0.0% | -1.4 | 0.18 | 2.12 | +2.7 | +4.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 33 | S_STRANGER | 100.0% | 15.2% | 15.2% | 12.1% | -0.5 | 0.76 | 4.10 | +4.0 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 33 | S_STRANGER | 100.0% | 15.2% | 15.2% | 12.1% | -0.5 | 0.76 | 4.10 | +4.0 | +4.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=26 Fav=15.4% Avg=-2.4; out_of_sample N=11 Fav=27.3% Avg=-1.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 73 | S_STRANGER | 100.0% | 15.1% | 16.4% | 8.2% | -3.5 | 0.15 | 0.68 | +2.8 | +3.6 |
| `hunt_to_ar_ratio_le_2_0` | 32 | S_STRANGER | 43.8% | 12.5% | 12.5% | 6.2% | -3.1 | 0.15 | 0.98 | +2.4 | +4.2 |
| `hunt_to_ar_ratio_le_2_5` | 37 | S_STRANGER | 50.7% | 18.9% | 21.6% | 8.1% | -2.2 | 0.31 | 1.07 | +2.9 | +3.9 |
| `stop_hunt_le_90` | 73 | S_STRANGER | 100.0% | 15.1% | 16.4% | 8.2% | -3.5 | 0.15 | 0.68 | +2.8 | +3.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 58 | S_STRANGER | 79.5% | 15.5% | 15.5% | 6.9% | -3.6 | 0.14 | 0.68 | +2.8 | +3.4 |
| `confluence_gte_70` | 17 | S_STRANGER | 23.3% | 17.6% | 17.6% | 5.9% | -2.0 | 0.24 | 1.13 | +2.8 | +3.5 |
| `tdi_rsi_gt_signal` | 59 | S_STRANGER | 80.8% | 18.6% | 20.3% | 6.8% | -2.8 | 0.21 | 0.78 | +2.9 | +3.6 |
| `tdi_rsi_gte_50` | 26 | S_STRANGER | 35.6% | 7.7% | 7.7% | 0.0% | -2.1 | 0.16 | 1.87 | +2.1 | +4.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 73 | S_STRANGER | 100.0% | 15.1% | 16.4% | 8.2% | -3.5 | 0.15 | 0.68 | +2.8 | +3.6 |
| `feature_stale_hod_exhaustion_reject` | 73 | S_STRANGER | 100.0% | 15.1% | 16.4% | 8.2% | -3.5 | 0.15 | 0.68 | +2.8 | +3.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-0.6; validation N=7 Fav=28.6% Avg=+3.5; out_of_sample N=2 Fav=0.0% Avg=-1.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 25.0% | +0.9 | 1.72 | 8.59 | +5.9 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 25.0% | +0.9 | 1.72 | 8.59 | +5.9 | +3.3 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 25.0% | +0.9 | 1.72 | 8.59 | +5.9 | +3.3 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 25.0% | +0.9 | 1.72 | 8.59 | +5.9 | +3.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 90.0% | 16.7% | 16.7% | 22.2% | +1.1 | 1.84 | 8.57 | +6.1 | +3.1 |
| `confluence_gte_70` | 6 | S_STRANGER | 30.0% | 16.7% | 16.7% | 16.7% | +3.6 | 4.08 | 20.42 | +6.5 | +2.6 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 55.0% | 18.2% | 18.2% | 18.2% | +1.8 | 2.35 | 10.57 | +7.6 | +3.1 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 65.0% | 15.4% | 15.4% | 15.4% | +1.4 | 2.13 | 11.70 | +6.3 | +2.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 25.0% | +0.9 | 1.72 | 8.59 | +5.9 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 25.0% | +0.9 | 1.72 | 8.59 | +5.9 | +3.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=12 Fav=25.0% Avg=+3.8; out_of_sample N=3 Fav=0.0% Avg=-13.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.5 | 0.87 | 4.34 | +7.7 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 5.6% | 5.6% | 16.7% | -2.7 | 0.37 | 5.49 | +5.8 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.5 | 0.87 | 4.34 | +7.7 | +7.1 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.5 | 0.87 | 4.34 | +7.7 | +7.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.5 | 0.87 | 4.34 | +7.7 | +7.1 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.5 | 0.87 | 4.34 | +7.7 | +7.1 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 30.0% | 16.7% | 16.7% | 33.3% | +3.4 | 3.56 | 14.23 | +8.9 | +6.4 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 75.0% | 20.0% | 20.0% | 13.3% | +0.4 | 1.09 | 4.00 | +8.2 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.5 | 0.87 | 4.34 | +7.7 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.5 | 0.87 | 4.34 | +7.7 | +7.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=11.1% Avg=-0.7; validation N=9 Fav=22.2% Avg=-2.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 10.0% | -1.7 | 0.46 | 2.59 | +3.4 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 16.7% | 16.7% | 11.1% | -1.7 | 0.48 | 2.41 | +3.7 | +3.3 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 10.0% | -1.7 | 0.46 | 2.59 | +3.4 | +3.3 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 10.0% | -1.7 | 0.46 | 2.59 | +3.4 | +3.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 45.0% | 11.1% | 11.1% | 0.0% | -0.3 | 0.81 | 6.49 | +3.0 | +3.3 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +1.6 | +3.2 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 75.0% | 13.3% | 13.3% | 6.7% | -1.5 | 0.49 | 3.20 | +3.6 | +3.6 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 20.0% | 25.0% | 25.0% | 0.0% | +2.0 | 3.16 | 9.47 | +4.4 | +3.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 10.0% | -1.7 | 0.46 | 2.59 | +3.4 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 10.0% | -1.7 | 0.46 | 2.59 | +3.4 | +3.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=17 Fav=11.8% Avg=-5.0; out_of_sample N=8 Fav=25.0% Avg=-2.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 14.8% | 18.5% | 14.8% | -4.0 | 0.15 | 0.64 | +4.6 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 92.6% | 16.0% | 20.0% | 12.0% | -4.3 | 0.15 | 0.62 | +4.1 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 100.0% | 14.8% | 18.5% | 14.8% | -4.0 | 0.15 | 0.64 | +4.6 | +5.2 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 100.0% | 14.8% | 18.5% | 14.8% | -4.0 | 0.15 | 0.64 | +4.6 | +5.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 22 | S_STRANGER | 81.5% | 13.6% | 18.2% | 9.1% | -3.8 | 0.17 | 0.78 | +3.7 | +5.7 |
| `confluence_gte_70` | 8 | S_STRANGER | 29.6% | 0.0% | 12.5% | 0.0% | -5.0 | 0.03 | 0.20 | +3.3 | +7.0 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 70.4% | 10.5% | 15.8% | 15.8% | -4.3 | 0.13 | 0.67 | +4.7 | +5.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 33.3% | 11.1% | 11.1% | 11.1% | -3.2 | 0.25 | 2.01 | +5.5 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 100.0% | 14.8% | 18.5% | 14.8% | -4.0 | 0.15 | 0.64 | +4.6 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 14.8% | 18.5% | 14.8% | -4.0 | 0.15 | 0.64 | +4.6 | +5.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=33.3% Avg=+4.8; out_of_sample N=7 Fav=14.3% Avg=-2.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 20.0% | -1.0 | 0.61 | 2.25 | +3.9 | +4.0 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 46.7% | 14.3% | 28.6% | 14.3% | -1.1 | 0.67 | 1.66 | +3.9 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 66.7% | 20.0% | 30.0% | 20.0% | -0.5 | 0.82 | 1.90 | +4.3 | +4.4 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 20.0% | -1.0 | 0.61 | 2.25 | +3.9 | +4.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 20.0% | -1.0 | 0.61 | 2.25 | +3.9 | +4.0 |
| `confluence_gte_70` | 6 | S_STRANGER | 40.0% | 16.7% | 16.7% | 33.3% | -0.0 | 0.96 | 3.85 | +4.6 | +2.0 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 50.0% | +3.7 | 9.17 | 9.17 | +6.8 | +1.1 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 33.3% | 0.0% | 20.0% | 20.0% | -0.9 | 0.68 | 2.03 | +5.3 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 20.0% | -1.0 | 0.61 | 2.25 | +3.9 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 20.0% | -1.0 | 0.61 | 2.25 | +3.9 | +4.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=33.3% Avg=+0.7; validation N=6 Fav=16.7% Avg=-0.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 54 | S_STRANGER | 100.0% | 13.0% | 16.7% | 13.0% | -2.8 | 0.21 | 0.93 | +2.7 | +2.3 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 42.6% | 17.4% | 26.1% | 13.0% | -0.7 | 0.63 | 1.58 | +3.0 | +2.6 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 53.7% | 17.2% | 24.1% | 10.3% | -1.0 | 0.50 | 1.44 | +2.8 | +2.4 |
| `stop_hunt_le_90` | 54 | S_STRANGER | 100.0% | 13.0% | 16.7% | 13.0% | -2.8 | 0.21 | 0.93 | +2.7 | +2.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 22 | S_STRANGER | 40.7% | 13.6% | 13.6% | 9.1% | -2.1 | 0.26 | 1.55 | +2.5 | +3.0 |
| `confluence_gte_70` | 3 | S_STRANGER | 5.6% | 33.3% | 33.3% | 0.0% | -0.3 | 0.78 | 1.56 | +4.1 | +2.9 |
| `tdi_rsi_gt_signal` | 31 | S_STRANGER | 57.4% | 19.4% | 19.4% | 12.9% | -2.3 | 0.29 | 1.10 | +2.8 | +2.3 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 33.3% | 27.8% | 33.3% | 5.6% | +0.4 | 1.32 | 2.65 | +3.3 | +2.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 54 | S_STRANGER | 100.0% | 13.0% | 16.7% | 13.0% | -2.8 | 0.21 | 0.93 | +2.7 | +2.3 |
| `feature_stale_hod_exhaustion_reject` | 54 | S_STRANGER | 100.0% | 13.0% | 16.7% | 13.0% | -2.8 | 0.21 | 0.93 | +2.7 | +2.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-2.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 12.9% | 12.9% | 6.5% | -4.8 | 0.12 | 0.76 | +2.4 | +2.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 32.3% | 10.0% | 10.0% | 0.0% | -4.9 | 0.03 | 0.30 | +1.6 | +3.7 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 64.5% | 5.0% | 5.0% | 0.0% | -6.1 | 0.01 | 0.26 | +1.8 | +2.7 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 12.9% | 12.9% | 6.5% | -4.8 | 0.12 | 0.76 | +2.4 | +2.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 4 | S_STRANGER | 12.9% | 25.0% | 25.0% | 25.0% | -0.7 | 0.52 | 1.57 | +3.1 | +2.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 64.5% | 15.0% | 15.0% | 5.0% | -3.8 | 0.10 | 0.55 | +2.2 | +2.9 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 16.1% | 20.0% | 20.0% | 0.0% | -2.9 | 0.21 | 0.84 | +2.8 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 12.9% | 12.9% | 6.5% | -4.8 | 0.12 | 0.76 | +2.4 | +2.6 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 12.9% | 12.9% | 6.5% | -4.8 | 0.12 | 0.76 | +2.4 | +2.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-3.1; validation N=5 Fav=20.0% Avg=+1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 17.6% | -0.0 | 1.00 | 5.50 | +4.2 | +3.1 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 94.1% | 12.5% | 12.5% | 18.8% | +0.1 | 1.14 | 5.68 | +4.4 | +3.1 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 17.6% | -0.0 | 1.00 | 5.50 | +4.2 | +3.1 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 17.6% | -0.0 | 1.00 | 5.50 | +4.2 | +3.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 47.1% | 12.5% | 12.5% | 12.5% | +0.1 | 1.06 | 6.34 | +5.9 | +4.4 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +4.9 | +14.7 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 70.6% | 8.3% | 8.3% | 16.7% | +0.5 | 1.60 | 12.82 | +4.3 | +2.5 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 0.0% | +0.4 | 1.26 | 6.31 | +5.2 | +3.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 17.6% | -0.0 | 1.00 | 5.50 | +4.2 | +3.1 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 17.6% | -0.0 | 1.00 | 5.50 | +4.2 | +3.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-23.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=15 Fav=13.3% Avg=-0.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -2.1 | 0.22 | 1.62 | +2.2 | +4.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 58.8% | 10.0% | 10.0% | 0.0% | -0.9 | 0.40 | 3.56 | +2.5 | +2.8 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 76.5% | 7.7% | 7.7% | 0.0% | -0.9 | 0.32 | 3.86 | +2.2 | +2.8 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -2.1 | 0.22 | 1.62 | +2.2 | +4.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -2.1 | 0.22 | 1.62 | +2.2 | +4.5 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -2.1 | 0.22 | 1.62 | +2.2 | +4.5 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +0.4 | +3.9 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 94.1% | 12.5% | 12.5% | 6.2% | -2.2 | 0.22 | 1.54 | +2.3 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -2.1 | 0.22 | 1.62 | +2.2 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -2.1 | 0.22 | 1.62 | +2.2 | +4.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=14.3% Avg=+0.3; validation N=5 Fav=20.0% Avg=-0.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 44 | S_STRANGER | 100.0% | 11.4% | 18.2% | 18.2% | -3.0 | 0.18 | 0.68 | +3.6 | +2.3 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 43.2% | 15.8% | 21.1% | 26.3% | -0.5 | 0.62 | 1.86 | +3.9 | +2.7 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 50.0% | 13.6% | 22.7% | 27.3% | -0.8 | 0.48 | 1.25 | +4.0 | +2.4 |
| `stop_hunt_le_90` | 44 | S_STRANGER | 100.0% | 11.4% | 18.2% | 18.2% | -3.0 | 0.18 | 0.68 | +3.6 | +2.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 21 | S_STRANGER | 47.7% | 9.5% | 14.3% | 9.5% | -3.6 | 0.07 | 0.40 | +3.4 | +2.4 |
| `confluence_gte_70` | 4 | S_STRANGER | 9.1% | 25.0% | 25.0% | 0.0% | -0.6 | 0.48 | 1.44 | +2.2 | +2.9 |
| `tdi_rsi_gt_signal` | 31 | S_STRANGER | 70.5% | 9.7% | 16.1% | 19.4% | -2.1 | 0.20 | 0.86 | +3.7 | +2.6 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 27.3% | 16.7% | 16.7% | 33.3% | -0.2 | 0.79 | 2.76 | +6.2 | +2.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 44 | S_STRANGER | 100.0% | 11.4% | 18.2% | 18.2% | -3.0 | 0.18 | 0.68 | +3.6 | +2.3 |
| `feature_stale_hod_exhaustion_reject` | 44 | S_STRANGER | 100.0% | 11.4% | 18.2% | 18.2% | -3.0 | 0.18 | 0.68 | +3.6 | +2.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=11 Fav=9.1% Avg=-2.2; out_of_sample N=6 Fav=16.7% Avg=+4.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 10.7% | 14.3% | 14.3% | -0.8 | 0.65 | 3.39 | +5.5 | +3.1 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 32.1% | 11.1% | 11.1% | 22.2% | -1.4 | 0.44 | 3.09 | +7.4 | +3.6 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 60.7% | 11.8% | 11.8% | 23.5% | +0.2 | 1.08 | 7.04 | +6.9 | +3.5 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 10.7% | 14.3% | 14.3% | -0.8 | 0.65 | 3.39 | +5.5 | +3.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 28 | S_STRANGER | 100.0% | 10.7% | 14.3% | 14.3% | -0.8 | 0.65 | 3.39 | +5.5 | +3.1 |
| `confluence_gte_70` | 28 | S_STRANGER | 100.0% | 10.7% | 14.3% | 14.3% | -0.8 | 0.65 | 3.39 | +5.5 | +3.1 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 42.9% | 16.7% | 25.0% | 8.3% | -0.0 | 0.98 | 2.95 | +5.3 | +2.8 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 67.9% | 10.5% | 10.5% | 15.8% | -0.1 | 0.94 | 7.07 | +6.0 | +3.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 10.7% | 14.3% | 14.3% | -0.8 | 0.65 | 3.39 | +5.5 | +3.1 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 10.7% | 14.3% | 14.3% | -0.8 | 0.65 | 3.39 | +5.5 | +3.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-3.1; validation N=6 Fav=16.7% Avg=+0.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -1.2 | 0.64 | 5.75 | +4.1 | +4.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -1.2 | 0.64 | 5.75 | +4.1 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -1.2 | 0.64 | 5.75 | +4.1 | +4.5 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -1.2 | 0.64 | 5.75 | +4.1 | +4.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | +1.8 | 1.49 | 4.47 | +6.5 | +5.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | +2.7 | 1.98 | 5.94 | +8.4 | +3.6 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | +2.7 | 1.98 | 5.94 | +8.4 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -1.2 | 0.64 | 5.75 | +4.1 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -1.2 | 0.64 | 5.75 | +4.1 | +4.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=22.2% Avg=+1.6; out_of_sample N=2 Fav=0.0% Avg=-5.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 10.0% | 13.3% | 30.0% | -1.9 | 0.35 | 1.73 | +4.5 | +4.5 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 100.0% | 10.0% | 13.3% | 30.0% | -1.9 | 0.35 | 1.73 | +4.5 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 30 | S_STRANGER | 100.0% | 10.0% | 13.3% | 30.0% | -1.9 | 0.35 | 1.73 | +4.5 | +4.5 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 10.0% | 13.3% | 30.0% | -1.9 | 0.35 | 1.73 | +4.5 | +4.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 27 | S_STRANGER | 90.0% | 11.1% | 14.8% | 29.6% | -1.9 | 0.38 | 1.70 | +4.3 | +4.5 |
| `confluence_gte_70` | 11 | S_STRANGER | 36.7% | 18.2% | 18.2% | 36.4% | +0.4 | 1.16 | 4.05 | +6.7 | +5.0 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 40.0% | 16.7% | 16.7% | 33.3% | -1.6 | 0.40 | 1.62 | +4.6 | +5.2 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 40.0% | 0.0% | 0.0% | 25.0% | -2.2 | 0.00 | 0.00 | +3.1 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 100.0% | 10.0% | 13.3% | 30.0% | -1.9 | 0.35 | 1.73 | +4.5 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 10.0% | 13.3% | 30.0% | -1.9 | 0.35 | 1.73 | +4.5 | +4.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=14.3% Avg=-2.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2.1 | 0.24 | 2.02 | +2.5 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 40.0% | 0.0% | 0.0% | 12.5% | -2.3 | 0.00 | 0.00 | +1.4 | +3.3 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 60.0% | 8.3% | 8.3% | 8.3% | -2.3 | 0.21 | 2.06 | +2.0 | +3.9 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2.1 | 0.24 | 2.02 | +2.5 | +4.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2.1 | 0.24 | 2.02 | +2.5 | +4.6 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2.1 | 0.24 | 2.02 | +2.5 | +4.6 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 35.0% | 14.3% | 14.3% | 14.3% | -2.2 | 0.28 | 1.68 | +2.0 | +5.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +1.7 | +5.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2.1 | 0.24 | 2.02 | +2.5 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2.1 | 0.24 | 2.02 | +2.5 | +4.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=16.7% Avg=-2.4; out_of_sample N=2 Fav=0.0% Avg=-1.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.0 | 0.24 | 2.15 | +3.3 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.0 | 0.24 | 2.15 | +3.3 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.0 | 0.24 | 2.15 | +3.3 | +5.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.0 | 0.24 | 2.15 | +3.3 | +5.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.0 | 0.24 | 2.15 | +3.3 | +5.7 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.0 | 0.24 | 2.15 | +3.3 | +5.7 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 0.0% | -2.2 | 0.34 | 2.39 | +3.4 | +6.7 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | +1.1 | 1.90 | 5.69 | +3.8 | +5.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.0 | 0.24 | 2.15 | +3.3 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.0 | 0.24 | 2.15 | +3.3 | +5.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L2|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L2|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-1.4; validation N=4 Fav=25.0% Avg=-2.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -3.0 | 0.08 | 0.65 | +3.5 | +5.8 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 25.0% | -1.4 | 0.00 | 0.00 | +3.0 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 20.0% | -1.3 | 0.00 | 0.00 | +3.7 | +3.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -3.0 | 0.08 | 0.65 | +3.5 | +5.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 12.5% | -1.8 | 0.16 | 0.95 | +3.8 | +4.4 |
| `confluence_gte_70` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 0.0% | -2.1 | 0.30 | 0.61 | +5.3 | +5.8 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 12.5% | -2.9 | 0.11 | 0.63 | +3.7 | +6.4 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 12.5% | -2.5 | 0.12 | 0.71 | +3.7 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -3.0 | 0.08 | 0.65 | +3.5 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -3.0 | 0.08 | 0.65 | +3.5 | +5.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=10.0% Avg=-3.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.1 | 0.02 | 0.14 | +3.1 | +4.5 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -3.6 | 0.00 | 0.00 | +3.1 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -4.1 | 0.00 | 0.00 | +3.4 | +5.0 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.1 | 0.02 | 0.14 | +3.1 | +4.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.1 | 0.02 | 0.14 | +3.1 | +4.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | -3.0 | 0.08 | 0.08 | +2.4 | +3.9 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +4.1 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.1 | 0.02 | 0.14 | +3.1 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -3.1 | 0.02 | 0.14 | +3.1 | +4.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-8.9; validation N=6 Fav=0.0% Avg=-2.0; out_of_sample N=3 Fav=33.3% Avg=+1.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.7 | 0.33 | 2.60 | +5.3 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 10.0% | -1.5 | 0.38 | 2.63 | +5.6 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.7 | 0.33 | 2.60 | +5.3 | +5.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.7 | 0.33 | 2.60 | +5.3 | +5.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.7 | 0.33 | 2.60 | +5.3 | +5.0 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.7 | 0.33 | 2.60 | +5.3 | +5.0 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +5.6 | +4.1 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 0.0% | -1.9 | 0.33 | 2.60 | +4.7 | +5.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.7 | 0.33 | 2.60 | +5.3 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1.7 | 0.33 | 2.60 | +5.3 | +5.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=20.0% Avg=-1.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -3.8 | 0.01 | 0.06 | +2.8 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 20.0% | -3.7 | 0.00 | 0.00 | +3.9 | +2.9 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 63.6% | 14.3% | 14.3% | 14.3% | -2.7 | 0.02 | 0.08 | +4.0 | +2.9 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -3.8 | 0.01 | 0.06 | +2.8 | +3.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -3.8 | 0.01 | 0.06 | +2.8 | +3.9 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -3.8 | 0.01 | 0.06 | +2.8 | +3.9 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 0.0% | -1.5 | 0.04 | 0.15 | +2.5 | +4.5 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -2.3 | 0.00 | 0.00 | +0.7 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -3.8 | 0.01 | 0.06 | +2.8 | +3.9 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -3.8 | 0.01 | 0.06 | +2.8 | +3.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=1 Fav=0.0% Avg=-0.8; out_of_sample N=5 Fav=20.0% Avg=+1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | +0.0 | 1.01 | 10.09 | +2.8 | +3.5 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 50.0% | 16.7% | 16.7% | 33.3% | +1.5 | 2.09 | 8.38 | +4.5 | +3.6 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 28.6% | +0.9 | 1.55 | 7.75 | +4.0 | +3.6 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | +0.0 | 1.01 | 10.09 | +2.8 | +3.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | +0.0 | 1.01 | 10.09 | +2.8 | +3.5 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | +0.0 | 1.01 | 10.09 | +2.8 | +3.5 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +0.9 | +3.0 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +1.1 | +4.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | +0.0 | 1.01 | 10.09 | +2.8 | +3.5 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | +0.0 | 1.01 | 10.09 | +2.8 | +3.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=11 Fav=18.2% Avg=-0.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -1.9 | 0.35 | 2.20 | +3.1 | +2.6 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 45.8% | 18.2% | 27.3% | 27.3% | -0.2 | 0.92 | 2.15 | +4.2 | +2.9 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 62.5% | 13.3% | 20.0% | 20.0% | -0.9 | 0.65 | 2.17 | +3.8 | +2.7 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -1.9 | 0.35 | 2.20 | +3.1 | +2.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -1.9 | 0.35 | 2.20 | +3.1 | +2.6 |
| `confluence_gte_70` | 12 | S_STRANGER | 50.0% | 0.0% | 8.3% | 8.3% | -4.0 | 0.05 | 0.54 | +1.9 | +2.9 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 58.3% | 7.1% | 7.1% | 14.3% | -1.2 | 0.54 | 6.43 | +3.0 | +3.0 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -2.7 | 0.00 | 0.00 | +0.4 | +2.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -1.9 | 0.35 | 2.20 | +3.1 | +2.6 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -1.9 | 0.35 | 2.20 | +3.1 | +2.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+1.9; validation N=5 Fav=0.0% Avg=-5.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 0.0% | -3.1 | 0.20 | 0.98 | +2.5 | +4.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 91.7% | 9.1% | 18.2% | 0.0% | -3.3 | 0.20 | 0.91 | +2.7 | +4.1 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 9.1% | 18.2% | 0.0% | -3.3 | 0.20 | 0.91 | +2.7 | +4.1 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 0.0% | -3.1 | 0.20 | 0.98 | +2.5 | +4.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -3.3 | 0.19 | 1.16 | +2.3 | +3.9 |
| `confluence_gte_70` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 0.0% | +5.5 | 999.00 | 999.00 | +7.4 | +3.5 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 12.5% | 25.0% | 0.0% | -2.3 | 0.33 | 0.99 | +2.8 | +3.8 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 0.0% | -0.9 | 0.60 | 1.81 | +2.9 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 0.0% | -3.1 | 0.20 | 0.98 | +2.5 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 0.0% | -3.1 | 0.20 | 0.98 | +2.5 | +4.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+0.1; validation N=1 Fav=0.0% Avg=-1.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 8.1% | 13.5% | 5.4% | -4.1 | 0.09 | 0.51 | +2.4 | +2.6 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 29.7% | 9.1% | 9.1% | 9.1% | -4.1 | 0.10 | 0.86 | +2.1 | +4.1 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 48.6% | 5.6% | 11.1% | 5.6% | -5.0 | 0.06 | 0.44 | +1.9 | +3.2 |
| `stop_hunt_le_90` | 37 | S_STRANGER | 100.0% | 8.1% | 13.5% | 5.4% | -4.1 | 0.09 | 0.51 | +2.4 | +2.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 24.3% | 0.0% | 11.1% | 0.0% | -3.3 | 0.03 | 0.21 | +2.2 | +1.9 |
| `confluence_gte_70` | 1 | S_STRANGER | 2.7% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +1.3 | +1.5 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 43.2% | 12.5% | 25.0% | 6.2% | -2.5 | 0.23 | 0.64 | +2.4 | +1.9 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 21.6% | 25.0% | 25.0% | 12.5% | -0.1 | 0.94 | 2.34 | +2.9 | +2.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 37 | S_STRANGER | 100.0% | 8.1% | 13.5% | 5.4% | -4.1 | 0.09 | 0.51 | +2.4 | +2.6 |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 8.1% | 13.5% | 5.4% | -4.1 | 0.09 | 0.51 | +2.4 | +2.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-2.0; validation N=6 Fav=16.7% Avg=-0.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -1.5 | 0.17 | 1.67 | +3.2 | +2.8 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 8.3% | 8.3% | 8.3% | -1.6 | 0.18 | 1.59 | +3.2 | +2.6 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -1.5 | 0.17 | 1.67 | +3.2 | +2.8 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -1.5 | 0.17 | 1.67 | +3.2 | +2.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -3.3 | 0.00 | 0.00 | +2.8 | +2.9 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +6.7 | +3.6 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -1.5 | 0.17 | 1.67 | +3.2 | +2.8 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 61.5% | 12.5% | 12.5% | 0.0% | -0.7 | 0.42 | 2.50 | +3.4 | +2.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -1.5 | 0.17 | 1.67 | +3.2 | +2.8 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -1.5 | 0.17 | 1.67 | +3.2 | +2.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.7; validation N=4 Fav=25.0% Avg=+1.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 15.4% | -1.7 | 0.29 | 2.94 | +4.5 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 0.0% | +1.8 | 2.35 | 4.70 | +6.7 | +2.9 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 20.0% | +0.8 | 1.71 | 5.13 | +6.6 | +2.6 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 15.4% | -1.7 | 0.29 | 2.94 | +4.5 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 15.4% | -1.7 | 0.29 | 2.94 | +4.5 | +4.1 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 15.4% | -1.7 | 0.29 | 2.94 | +4.5 | +4.1 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 20.0% | -0.7 | 0.57 | 3.99 | +5.2 | +3.5 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 53.8% | 0.0% | 0.0% | 14.3% | -1.2 | 0.00 | 0.00 | +3.7 | +3.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 15.4% | -1.7 | 0.29 | 2.94 | +4.5 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 15.4% | -1.7 | 0.29 | 2.94 | +4.5 | +4.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=0.0% Avg=-3.6; out_of_sample N=5 Fav=20.0% Avg=+0.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 0.0% | -2.5 | 0.14 | 1.57 | +2.5 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 0.0% | -2.5 | 0.14 | 1.57 | +2.5 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 0.0% | -2.5 | 0.14 | 1.57 | +2.5 | +5.2 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 0.0% | -2.5 | 0.14 | 1.57 | +2.5 | +5.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 0.0% | -2.1 | 0.20 | 1.58 | +2.8 | +5.3 |
| `confluence_gte_70` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 0.0% | +1.5 | 7.57 | 7.57 | +5.2 | +2.7 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 0.0% | -2.0 | 0.21 | 1.68 | +3.0 | +4.7 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 61.5% | 12.5% | 12.5% | 0.0% | -1.2 | 0.35 | 2.12 | +2.9 | +4.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 0.0% | -2.5 | 0.14 | 1.57 | +2.5 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 0.0% | -2.5 | 0.14 | 1.57 | +2.5 | +5.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=12.5% Avg=-4.9; out_of_sample N=2 Fav=0.0% Avg=-6.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 0.0% | -3.7 | 0.16 | 0.87 | +5.4 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 0.0% | -3.7 | 0.16 | 0.87 | +5.4 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 0.0% | -3.7 | 0.16 | 0.87 | +5.4 | +6.6 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 0.0% | -3.7 | 0.16 | 0.87 | +5.4 | +6.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 0.0% | -3.7 | 0.16 | 0.87 | +5.4 | +6.6 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 0.0% | -3.7 | 0.16 | 0.87 | +5.4 | +6.6 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 0.0% | -5.3 | 0.02 | 0.17 | +5.2 | +7.6 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 61.5% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +4.4 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 0.0% | -3.7 | 0.16 | 0.87 | +5.4 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 7.7% | 15.4% | 0.0% | -3.7 | 0.16 | 0.87 | +5.4 | +6.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=11.1% Avg=-9.2; out_of_sample N=5 Fav=0.0% Avg=-10.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -9.8 | 0.01 | 0.17 | +3.5 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -9.8 | 0.01 | 0.17 | +3.5 | +3.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -9.8 | 0.01 | 0.17 | +3.5 | +3.7 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -9.8 | 0.01 | 0.17 | +3.5 | +3.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -9.8 | 0.01 | 0.17 | +3.5 | +3.7 |
| `confluence_gte_70` | 6 | S_STRANGER | 42.9% | 0.0% | 0.0% | 0.0% | -13.5 | 0.00 | 0.00 | +1.7 | +2.4 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 71.4% | 0.0% | 0.0% | 10.0% | -8.3 | 0.00 | 0.00 | +3.6 | +3.9 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +5.1 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -9.8 | 0.01 | 0.17 | +3.5 | +3.7 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 7.1% | 7.1% | 14.3% | -9.8 | 0.01 | 0.17 | +3.5 | +3.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=15 Fav=6.7% Avg=-1.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 26.7% | -1.1 | 0.31 | 0.94 | +4.1 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 26.7% | -1.1 | 0.31 | 0.94 | +4.1 | +3.7 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 26.7% | -1.1 | 0.31 | 0.94 | +4.1 | +3.7 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 26.7% | -1.1 | 0.31 | 0.94 | +4.1 | +3.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 26.7% | -1.1 | 0.31 | 0.94 | +4.1 | +3.7 |
| `confluence_gte_70` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 50.0% | +2.2 | 999.00 | 999.00 | +7.5 | +4.2 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 46.7% | 0.0% | 0.0% | 28.6% | -1.6 | 0.00 | 0.00 | +5.6 | +4.3 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +4.9 | +4.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 26.7% | -1.1 | 0.31 | 0.94 | +4.1 | +3.7 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 26.7% | -1.1 | 0.31 | 0.94 | +4.1 | +3.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=13 Fav=7.7% Avg=-2.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 6.2% | 18.8% | 12.5% | -2.1 | 0.21 | 0.76 | +2.7 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 93.8% | 0.0% | 13.3% | 6.7% | -2.6 | 0.07 | 0.37 | +2.4 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 6.2% | 18.8% | 12.5% | -2.1 | 0.21 | 0.76 | +2.7 | +5.5 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 6.2% | 18.8% | 12.5% | -2.1 | 0.21 | 0.76 | +2.7 | +5.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 81.2% | 7.7% | 23.1% | 15.4% | -2.1 | 0.24 | 0.64 | +2.8 | +6.0 |
| `confluence_gte_70` | 5 | S_STRANGER | 31.2% | 0.0% | 20.0% | 20.0% | -3.5 | 0.09 | 0.27 | +2.5 | +8.0 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 31.2% | 0.0% | 20.0% | 0.0% | -3.9 | 0.05 | 0.21 | +1.4 | +6.1 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 43.8% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +1.5 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 6.2% | 18.8% | 12.5% | -2.1 | 0.21 | 0.76 | +2.7 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 6.2% | 18.8% | 12.5% | -2.1 | 0.21 | 0.76 | +2.7 | +5.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=16 Fav=6.2% Avg=-3.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -3.8 | 0.10 | 1.56 | +2.5 | +2.7 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 52.9% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +1.8 | +2.9 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 70.6% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +1.6 | +3.2 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -3.8 | 0.10 | 1.56 | +2.5 | +2.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -3.8 | 0.10 | 1.56 | +2.5 | +2.7 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -3.8 | 0.10 | 1.56 | +2.5 | +2.7 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 94.1% | 6.2% | 6.2% | 12.5% | -3.1 | 0.13 | 1.86 | +2.6 | +2.8 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +1.3 | +1.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -3.8 | 0.10 | 1.56 | +2.5 | +2.7 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -3.8 | 0.10 | 1.56 | +2.5 | +2.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-2.3; validation N=2 Fav=50.0% Avg=+4.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 34 | S_STRANGER | 100.0% | 5.9% | 8.8% | 8.8% | -4.1 | 0.14 | 1.40 | +2.1 | +3.3 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 35.3% | 8.3% | 8.3% | 8.3% | -1.2 | 0.37 | 4.08 | +2.2 | +3.0 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 44.1% | 6.7% | 6.7% | 6.7% | -1.3 | 0.29 | 4.09 | +1.9 | +3.0 |
| `stop_hunt_le_90` | 34 | S_STRANGER | 100.0% | 5.9% | 8.8% | 8.8% | -4.1 | 0.14 | 1.40 | +2.1 | +3.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 41.2% | 7.1% | 14.3% | 7.1% | -1.1 | 0.48 | 2.87 | +2.5 | +2.7 |
| `confluence_gte_70` | 7 | S_STRANGER | 20.6% | 14.3% | 14.3% | 14.3% | -0.3 | 0.87 | 5.19 | +4.5 | +3.8 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 58.8% | 5.0% | 10.0% | 10.0% | -2.4 | 0.23 | 1.94 | +2.2 | +3.1 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 35.3% | 0.0% | 0.0% | 0.0% | -2.7 | 0.00 | 0.00 | +0.8 | +3.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 34 | S_STRANGER | 100.0% | 5.9% | 8.8% | 8.8% | -4.1 | 0.14 | 1.40 | +2.1 | +3.3 |
| `feature_stale_hod_exhaustion_reject` | 34 | S_STRANGER | 100.0% | 5.9% | 8.8% | 8.8% | -4.1 | 0.14 | 1.40 | +2.1 | +3.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=0.0% Avg=-5.6; out_of_sample N=13 Fav=7.7% Avg=-5.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 36 | S_STRANGER | 100.0% | 5.6% | 13.9% | 11.1% | -6.2 | 0.09 | 0.52 | +3.6 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 50.0% | 5.6% | 5.6% | 11.1% | -5.7 | 0.10 | 1.36 | +4.2 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 58.3% | 4.8% | 4.8% | 9.5% | -6.2 | 0.08 | 1.32 | +3.8 | +5.7 |
| `stop_hunt_le_90` | 36 | S_STRANGER | 100.0% | 5.6% | 13.9% | 11.1% | -6.2 | 0.09 | 0.52 | +3.6 | +5.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 36 | S_STRANGER | 100.0% | 5.6% | 13.9% | 11.1% | -6.2 | 0.09 | 0.52 | +3.6 | +5.0 |
| `confluence_gte_70` | 23 | S_STRANGER | 63.9% | 4.3% | 17.4% | 8.7% | -6.8 | 0.10 | 0.42 | +4.2 | +5.1 |
| `tdi_rsi_gt_signal` | 25 | S_STRANGER | 69.4% | 4.0% | 12.0% | 12.0% | -4.4 | 0.08 | 0.52 | +3.9 | +5.1 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 25.0% | 0.0% | 11.1% | 22.2% | -6.3 | 0.02 | 0.15 | +4.8 | +9.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 36 | S_STRANGER | 100.0% | 5.6% | 13.9% | 11.1% | -6.2 | 0.09 | 0.52 | +3.6 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 36 | S_STRANGER | 100.0% | 5.6% | 13.9% | 11.1% | -6.2 | 0.09 | 0.52 | +3.6 | +5.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=20.0% Avg=-8.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 4.3% | 4.3% | 13.0% | -3.5 | 0.10 | 1.89 | +3.4 | +3.7 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 34.8% | 0.0% | 0.0% | 25.0% | -8.1 | 0.00 | 0.00 | +3.6 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 65.2% | 6.7% | 6.7% | 20.0% | -5.2 | 0.10 | 1.25 | +4.0 | +4.8 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 4.3% | 4.3% | 13.0% | -3.5 | 0.10 | 1.89 | +3.4 | +3.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 4.3% | 4.3% | 13.0% | -3.5 | 0.10 | 1.89 | +3.4 | +3.7 |
| `confluence_gte_70` | 5 | S_STRANGER | 21.7% | 20.0% | 20.0% | 40.0% | -8.5 | 0.18 | 0.53 | +4.7 | +2.4 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 91.3% | 0.0% | 0.0% | 9.5% | -2.7 | 0.00 | 0.00 | +3.2 | +3.9 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 43.5% | 0.0% | 0.0% | 10.0% | -1.5 | 0.00 | 0.00 | +3.0 | +3.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 4.3% | 4.3% | 13.0% | -3.5 | 0.10 | 1.89 | +3.4 | +3.7 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 4.3% | 4.3% | 13.0% | -3.5 | 0.10 | 1.89 | +3.4 | +3.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=25.0% Avg=-1.6; out_of_sample N=2 Fav=0.0% Avg=-0.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 4.0% | 4.0% | 0.0% | -9.8 | 0.02 | 0.45 | +2.8 | +3.2 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -4.8 | 0.00 | 0.00 | +2.9 | +3.0 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 52.0% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +2.6 | +3.3 |
| `stop_hunt_le_90` | 25 | S_STRANGER | 100.0% | 4.0% | 4.0% | 0.0% | -9.8 | 0.02 | 0.45 | +2.8 | +3.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 72.0% | 5.6% | 5.6% | 0.0% | -9.0 | 0.03 | 0.48 | +3.1 | +3.2 |
| `confluence_gte_70` | 2 | S_STRANGER | 8.0% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +1.7 | +3.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 36.0% | 11.1% | 11.1% | 0.0% | -7.0 | 0.07 | 0.56 | +5.1 | +4.1 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 24.0% | 16.7% | 16.7% | 0.0% | -1.4 | 0.36 | 1.82 | +6.6 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 25 | S_STRANGER | 100.0% | 4.0% | 4.0% | 0.0% | -9.8 | 0.02 | 0.45 | +2.8 | +3.2 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 4.0% | 4.0% | 0.0% | -9.8 | 0.02 | 0.45 | +2.8 | +3.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=9 Fav=0.0% Avg=-1.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 8.3% | -1.9 | 0.00 | 0.04 | +1.7 | +2.9 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 8.3% | -1.9 | 0.00 | 0.04 | +1.7 | +2.9 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 8.3% | -1.9 | 0.00 | 0.04 | +1.7 | +2.9 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 8.3% | -1.9 | 0.00 | 0.04 | +1.7 | +2.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 75.0% | 0.0% | 11.1% | 11.1% | -1.4 | 0.01 | 0.05 | +2.1 | +2.5 |
| `confluence_gte_70` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 50.0% | -0.9 | 0.00 | 0.00 | +3.1 | +2.1 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 83.3% | 0.0% | 10.0% | 10.0% | -1.9 | 0.01 | 0.04 | +1.7 | +2.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 0.0% | 0.0% | 14.3% | -1.6 | 0.00 | 0.00 | +2.2 | +2.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 8.3% | -1.9 | 0.00 | 0.04 | +1.7 | +2.9 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 0.0% | 8.3% | 8.3% | -1.9 | 0.00 | 0.04 | +1.7 | +2.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=0.0% Avg=-1.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 20.0% | -2.1 | 0.00 | 0.00 | +3.5 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 25.0% | -2.1 | 0.00 | 0.00 | +4.0 | +4.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 16.7% | -1.3 | 0.00 | 0.00 | +4.4 | +2.9 |
| `confluence_gte_70` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +15.8 | +2.5 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -3.6 | 0.00 | 0.00 | +1.6 | +5.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 14.3% | -1.2 | 0.00 | 0.00 | +3.9 | +3.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 25.0% | -2.1 | 0.00 | 0.00 | +4.0 | +4.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 20.0% | -2.1 | 0.00 | 0.00 | +3.5 | +3.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-2.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=0.0% Avg=-0.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -3.1 | 0.05 | 0.55 | +1.9 | +2.6 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -3.1 | 0.05 | 0.55 | +1.9 | +2.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -3.1 | 0.05 | 0.55 | +1.9 | +2.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -3.1 | 0.05 | 0.55 | +1.9 | +2.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -3.1 | 0.05 | 0.55 | +1.9 | +2.6 |
| `confluence_gte_70` | 8 | S_STRANGER | 72.7% | 0.0% | 12.5% | 0.0% | -3.7 | 0.06 | 0.44 | +2.2 | +2.2 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 72.7% | 0.0% | 12.5% | 0.0% | -3.8 | 0.06 | 0.43 | +2.2 | +2.0 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 45.5% | 0.0% | 20.0% | 0.0% | -0.7 | 0.37 | 1.48 | +2.4 | +2.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -3.1 | 0.05 | 0.55 | +1.9 | +2.6 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 0.0% | 9.1% | 0.0% | -3.1 | 0.05 | 0.55 | +1.9 | +2.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=0.0% Avg=-1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.1 | 0.00 | 0.00 | +2.9 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 52.9% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +2.0 | +3.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 58.8% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +2.8 | +3.6 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.1 | 0.00 | 0.00 | +2.9 | +3.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.1 | 0.00 | 0.00 | +2.9 | +3.9 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.1 | 0.00 | 0.00 | +2.9 | +3.9 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 82.4% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +3.0 | +3.8 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 29.4% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +2.7 | +4.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.1 | 0.00 | 0.00 | +2.9 | +3.9 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.1 | 0.00 | 0.00 | +2.9 | +3.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=0.0% Avg=-2.0; out_of_sample N=5 Fav=0.0% Avg=-3.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +5.1 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +5.1 | +3.8 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +5.1 | +3.8 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +5.1 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +5.1 | +3.8 |
| `confluence_gte_70` | 7 | S_STRANGER | 46.7% | 0.0% | 0.0% | 0.0% | -8.1 | 0.00 | 0.00 | +6.8 | +3.4 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +3.0 | +2.7 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 73.3% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +6.1 | +4.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +5.1 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +5.1 | +3.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=0.0% Avg=-3.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +2.7 | +4.2 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +2.7 | +4.2 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +2.7 | +4.2 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +2.7 | +4.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 88.2% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +2.1 | +3.9 |
| `confluence_gte_70` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +3.4 | +3.6 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 70.6% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +1.5 | +5.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 41.2% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +3.6 | +5.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +2.7 | +4.2 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -5.6 | 0.00 | 0.00 | +2.7 | +4.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
