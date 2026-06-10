# XAUUSD Pair Feature Ablation

Generated: 2026-06-09T15:36:29.270722+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | R_REPEATER | 70.6% | +358.7 | `ratio_le_2_asian_gte_30_tdi_positive` | 12 | R_RUNNER | 83.3% | +416.0 | 7.22 | 1.44 | 0 | 1 | watch_research |
| `RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | R_REPEATER | 63.6% | +549.0 | `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_RUNNER | 100.0% | +770.4 | 999.00 | 999.00 | 1 | 1 | research_only_split_fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | R_REPEATER | 54.5% | +233.0 | `feature_momentum_breakout_exception` | 9 | R_REPEATER | 66.7% | +394.6 | 2.49 | 0.83 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | R_REPEATER | 54.5% | +13.5 | `all` | 11 | R_REPEATER | 54.5% | +13.5 | 1.02 | 0.85 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|EARLY_WEEK|L0|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74` | 15 | R_REPEATER | 53.3% | +224.9 | `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 58.3% | +260.3 | 6.73 | 4.81 | 0 | 1 | watch_research |
| `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 12 | R_REPEATER | 50.0% | +233.4 | `tdi_rsi_gt_signal` | 7 | R_REPEATER | 57.1% | +513.0 | 51.58 | 38.68 | 0 | 2 | demo_watch_candidate |
| `STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | R_REPEATER | 50.0% | +227.2 | `tdi_rsi_gte_50` | 10 | R_REPEATER | 60.0% | +334.5 | 2.27 | 1.51 | 0 | 2 | demo_watch_candidate |
| `STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | R_REPEATER | 50.0% | +133.9 | `all` | 18 | R_REPEATER | 50.0% | +133.9 | 1.34 | 1.34 | 0 | 2 | demo_watch_candidate |
| `STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | R_REPEATER | 50.0% | +85.3 | `all` | 10 | R_REPEATER | 50.0% | +85.3 | 1.83 | 1.83 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|EARLY_WEEK|L0|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | R_REPEATER | 50.0% | +82.0 | `tdi_rsi_gt_signal` | 9 | R_REPEATER | 55.6% | +109.3 | 2.42 | 1.94 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 25 | S_STRANGER | 48.0% | +92.0 | `confluence_gte_60` | 9 | R_REPEATER | 66.7% | +113.4 | 2.49 | 0.71 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 47.8% | +147.0 | `feature_stale_hod_exhaustion_reject` | 21 | R_REPEATER | 52.4% | +187.1 | 1.77 | 1.33 | 0 | 2 | demo_watch_candidate |
| `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | S_STRANGER | 47.1% | +61.5 | `ratio_le_2_asian_gte_30_tdi_positive` | 13 | R_REPEATER | 61.5% | +317.5 | 1.65 | 1.03 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 46.7% | +206.4 | `feature_momentum_breakout_exception` | 14 | R_REPEATER | 50.0% | +287.1 | 3.15 | 3.15 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 46.2% | +112.5 | `feature_momentum_breakout_exception` | 8 | R_RUNNER | 75.0% | +281.5 | 2.58 | 0.86 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 11 | S_STRANGER | 45.5% | +135.9 | `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 50.0% | +168.7 | 2.92 | 2.92 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 44.4% | +153.4 | `tdi_rsi_gt_signal` | 17 | S_STRANGER | 47.1% | +174.5 | 2.53 | 2.85 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 16 | S_STRANGER | 43.8% | +9.0 | `confluence_gte_60` | 10 | R_REPEATER | 50.0% | +55.9 | 1.10 | 0.88 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 43.5% | +175.1 | `ratio_le_2_asian_gte_30_tdi_positive` | 14 | R_REPEATER | 50.0% | +251.7 | 4.06 | 4.06 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 23 | S_STRANGER | 43.5% | +36.2 | `tdi_rsi_gt_signal` | 13 | S_STRANGER | 46.2% | +58.0 | 1.23 | 1.23 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 28 | S_STRANGER | 42.9% | -61.1 | `confluence_gte_60` | 17 | R_REPEATER | 58.8% | +42.6 | 1.57 | 0.94 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 31 | S_STRANGER | 41.9% | +172.9 | `all` | 31 | S_STRANGER | 41.9% | +172.9 | 3.47 | 3.47 | 0 | 2 | demo_watch_candidate |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 24 | S_STRANGER | 41.7% | +957.0 | `confluence_gte_60` | 11 | R_REPEATER | 54.5% | +1771.5 | 20.91 | 5.97 | 0 | 2 | demo_watch_candidate |
| `STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 12 | S_STRANGER | 41.7% | +96.3 | `feature_momentum_breakout_exception` | 10 | R_REPEATER | 50.0% | +227.0 | 2.84 | 2.84 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 41.7% | +27.6 | `all` | 12 | S_STRANGER | 41.7% | +27.6 | 1.16 | 0.96 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 40.0% | +19.0 | `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 50.0% | +159.5 | 2.22 | 2.22 | 0 | 1 | watch_research |
| `THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 40.0% | +3.1 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 44.4% | +3.4 | 1.01 | 1.26 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 40.0% | -3.5 | `feature_momentum_breakout_exception` | 12 | R_REPEATER | 50.0% | +84.3 | 1.73 | 1.24 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 38.5% | +374.6 | `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 45.5% | +506.6 | 9.32 | 11.18 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 38.5% | +56.2 | `feature_momentum_breakout_exception` | 12 | S_STRANGER | 41.7% | +61.0 | 1.29 | 1.81 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 38.5% | -45.9 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 40.0% | +225.5 | 3.47 | 3.47 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74` | 13 | S_STRANGER | 38.5% | -46.0 | `confluence_gte_60` | 11 | S_STRANGER | 45.5% | +6.6 | 1.04 | 1.25 | 0 | 0 | watch_research |
| `STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 38.5% | -81.4 | `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 42.9% | +82.1 | 1.83 | 2.45 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 37.5% | +341.8 | `feature_momentum_breakout_exception` | 9 | S_STRANGER | 44.4% | +417.7 | 3.24 | 4.05 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 16 | S_STRANGER | 37.5% | -451.2 | `feature_momentum_breakout_exception` | 11 | R_REPEATER | 54.5% | +438.1 | 2.52 | 2.10 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 36.8% | +123.2 | `tdi_rsi_gt_signal` | 5 | R_REPEATER | 60.0% | +346.6 | 16.90 | 11.27 | 0 | 1 | watch_research |
| `STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 36.4% | +695.5 | `tdi_rsi_gt_signal` | 8 | R_REPEATER | 50.0% | +1071.8 | 8.27 | 3.31 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 36.4% | +99.6 | `all` | 11 | S_STRANGER | 36.4% | +99.6 | 1.45 | 2.53 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 36.4% | +36.5 | `tdi_rsi_gt_signal` | 6 | R_REPEATER | 50.0% | +134.5 | 3.76 | 3.76 | 0 | 1 | watch_research |
| `THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 36.4% | +25.0 | `feature_momentum_breakout_exception` | 10 | S_STRANGER | 40.0% | +56.3 | 1.83 | 2.29 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 36.4% | -4.2 | `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 40.0% | +33.1 | 1.22 | 1.53 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 11 | S_STRANGER | 36.4% | -29.1 | `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 40.0% | -28.7 | 0.90 | 0.72 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 47 | S_STRANGER | 36.2% | +68.2 | `tdi_rsi_gt_signal` | 16 | S_STRANGER | 43.8% | +109.8 | 1.80 | 1.58 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_50_74` | 14 | S_STRANGER | 35.7% | -144.5 | `feature_momentum_breakout_exception` | 10 | R_REPEATER | 50.0% | -27.9 | 0.72 | 0.48 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 14 | S_STRANGER | 35.7% | -580.6 | `feature_momentum_breakout_exception` | 10 | R_REPEATER | 50.0% | -29.1 | 0.88 | 0.88 | 0 | 1 | fail |
| `STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 35.3% | +95.6 | `tdi_rsi_gte_50` | 7 | R_REPEATER | 57.1% | +319.0 | 3.88 | 2.91 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 35.3% | +51.3 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 42.9% | +41.4 | 1.65 | 1.24 | 0 | 1 | watch_research |
| `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 17 | S_STRANGER | 35.3% | +15.0 | `confluence_gte_60` | 12 | S_STRANGER | 41.7% | +2.6 | 1.02 | 1.02 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_75_PLUS` | 26 | S_STRANGER | 34.6% | +52.7 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 50.0% | +129.5 | 3.06 | 3.06 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 41 | S_STRANGER | 34.1% | +82.9 | `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 62.5% | +450.6 | 18.42 | 7.37 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 33.3% | +258.0 | `feature_momentum_breakout_exception` | 10 | S_STRANGER | 40.0% | +478.3 | 2.62 | 3.94 | 0 | 1 | watch_research |
| `THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | +137.9 | `confluence_gte_60` | 10 | S_STRANGER | 40.0% | +178.6 | 1.75 | 1.17 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 21 | S_STRANGER | 33.3% | +115.0 | `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 41.2% | +144.7 | 2.90 | 2.58 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 18 | S_STRANGER | 33.3% | +76.3 | `confluence_gte_60` | 11 | S_STRANGER | 45.5% | +261.0 | 1.96 | 1.64 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | +27.9 | `feature_momentum_breakout_exception` | 10 | S_STRANGER | 40.0% | +93.9 | 1.79 | 2.68 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 33.3% | +6.8 | `tdi_rsi_gte_50` | 13 | S_STRANGER | 38.5% | +15.9 | 1.07 | 1.28 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 33.3% | -33.8 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 37.5% | -38.0 | 0.74 | 1.23 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 15 | S_STRANGER | 33.3% | -36.0 | `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 50.0% | +76.3 | 2.25 | 2.25 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 15 | S_STRANGER | 33.3% | -41.2 | `feature_momentum_breakout_exception` | 10 | R_REPEATER | 50.0% | +170.7 | 4.04 | 2.70 | 0 | 1 | watch_research |
| `STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 33.3% | -65.5 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 37.5% | -46.0 | 0.79 | 1.05 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | -174.2 | `feature_momentum_breakout_exception` | 10 | S_STRANGER | 40.0% | -86.8 | 0.34 | 0.50 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 31 | S_STRANGER | 32.3% | +87.2 | `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 45.5% | +205.0 | 3.74 | 4.49 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 25 | S_STRANGER | 32.0% | -32.3 | `confluence_gte_60` | 11 | S_STRANGER | 45.5% | +146.8 | 3.27 | 3.27 | 0 | 2 | demo_watch_candidate |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 25 | S_STRANGER | 32.0% | -367.6 | `tdi_rsi_gte_50` | 17 | S_STRANGER | 47.1% | +2.4 | 1.00 | 0.70 | 0 | 0 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 51 | S_STRANGER | 31.4% | +108.1 | `feature_eurjpy_tdi50_reclaim` | 15 | S_STRANGER | 33.3% | +28.6 | 1.23 | 1.85 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 31.2% | +189.1 | `all` | 16 | S_STRANGER | 31.2% | +189.1 | 1.43 | 3.16 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 31.2% | +29.4 | `feature_momentum_breakout_exception` | 15 | S_STRANGER | 33.3% | +59.3 | 1.62 | 2.43 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_50_74` | 16 | S_STRANGER | 31.2% | +29.1 | `feature_momentum_breakout_exception` | 12 | S_STRANGER | 41.7% | +114.7 | 6.12 | 2.62 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 31.2% | -237.3 | `all` | 16 | S_STRANGER | 31.2% | -237.3 | 0.52 | 1.14 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 16 | S_STRANGER | 31.2% | -293.6 | `feature_momentum_breakout_exception` | 14 | S_STRANGER | 35.7% | -55.4 | 0.90 | 0.90 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74` | 23 | S_STRANGER | 30.4% | +17.2 | `feature_momentum_breakout_exception` | 19 | S_STRANGER | 36.8% | +30.7 | 1.27 | 1.64 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 30.0% | +25.8 | `all` | 10 | S_STRANGER | 30.0% | +25.8 | 1.20 | 2.81 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | +9.4 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 33.3% | +40.2 | 1.16 | 2.32 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|EARLY_WEEK|L0|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 30.0% | -20.2 | `confluence_gte_60` | 5 | S_STRANGER | 40.0% | +185.4 | 7.57 | 7.57 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|EARLY_WEEK|L0|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | -25.7 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 20.0% | +2.0 | 1.03 | 1.54 | 0 | 0 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 30.0% | -29.5 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 28.6% | +20.1 | 1.43 | 2.15 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 30.0% | -181.6 | `all` | 10 | S_STRANGER | 30.0% | -181.6 | 0.36 | 0.84 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 14 | S_STRANGER | 28.6% | +11.9 | `feature_momentum_breakout_exception` | 13 | S_STRANGER | 30.8% | +12.8 | 1.18 | 1.41 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 28.6% | +1.0 | `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 36.4% | +42.3 | 1.44 | 1.73 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 35 | S_STRANGER | 28.6% | -89.4 | `confluence_gte_70` | 5 | R_REPEATER | 60.0% | +261.4 | 8.47 | 2.82 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 21 | S_STRANGER | 28.6% | -203.9 | `confluence_gte_60` | 20 | S_STRANGER | 30.0% | -211.2 | 0.57 | 1.32 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 36 | S_STRANGER | 27.8% | +67.4 | `feature_momentum_breakout_exception` | 33 | S_STRANGER | 30.3% | +71.4 | 1.16 | 2.31 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 36 | S_STRANGER | 27.8% | +26.4 | `confluence_gte_60` | 25 | S_STRANGER | 32.0% | +52.3 | 1.31 | 2.18 | 0 | 1 | watch_research |
| `RRT_REVERSAL|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | -46.3 | `all` | 11 | S_STRANGER | 27.3% | -46.3 | 0.85 | 1.71 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | -112.5 | `feature_momentum_breakout_exception` | 8 | S_STRANGER | 37.5% | +30.8 | 1.43 | 1.07 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 27.3% | -113.6 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 42.9% | -18.2 | 0.89 | 0.89 | 0 | 0 | fail |
| `STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | -149.6 | `feature_momentum_breakout_exception` | 10 | S_STRANGER | 30.0% | -135.5 | 0.50 | 1.17 | 0 | 0 | fail |
| `RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | -271.9 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 33.3% | -261.9 | 0.26 | 0.51 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_50_74` | 15 | S_STRANGER | 26.7% | +210.7 | `feature_momentum_breakout_exception` | 10 | S_STRANGER | 40.0% | +493.4 | 9.76 | 9.76 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 26.3% | +14.2 | `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 33.3% | +70.6 | 1.44 | 1.79 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 26.3% | -95.7 | `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 29.4% | -76.6 | 0.67 | 0.75 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 19 | S_STRANGER | 26.3% | -100.4 | `confluence_gte_60` | 12 | S_STRANGER | 41.7% | +15.2 | 1.10 | 1.10 | 0 | 1 | watch_research |
| `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 23 | S_STRANGER | 26.1% | -15.6 | `feature_momentum_breakout_exception` | 20 | S_STRANGER | 30.0% | +113.5 | 2.44 | 5.28 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | +368.7 | `confluence_gte_70` | 6 | R_REPEATER | 50.0% | +1041.6 | 7.07 | 3.54 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 25.0% | +246.0 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 28.6% | +417.4 | 2.97 | 5.94 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | +200.2 | `feature_momentum_breakout_exception` | 10 | S_STRANGER | 30.0% | +257.1 | 2.54 | 5.93 | 0 | 1 | watch_research |
| `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | +46.7 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 42.9% | +354.3 | 5.28 | 3.96 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 25.0% | +41.4 | `tdi_rsi_gt_signal` | 11 | S_STRANGER | 27.3% | +65.5 | 1.61 | 2.82 | 0 | 1 | watch_research |
| `RRT_REVERSAL|BUY|EARLY_WEEK|L0|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | -62.5 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 33.3% | -62.9 | 0.59 | 1.18 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 44 | S_STRANGER | 25.0% | -157.8 | `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 35.3% | -8.8 | 0.96 | 1.60 | 0 | 1 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 25.0% | -193.4 | `feature_momentum_breakout_exception` | 10 | S_STRANGER | 30.0% | +6.1 | 1.04 | 1.30 | 0 | 0 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 33 | S_STRANGER | 24.2% | -534.4 | `feature_momentum_breakout_exception` | 21 | S_STRANGER | 38.1% | -149.1 | 0.61 | 0.84 | 0 | 1 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 29 | S_STRANGER | 24.1% | +98.9 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 37.5% | +369.1 | 1.90 | 1.90 | 0 | 1 | watch_research |
| `STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 21 | S_STRANGER | 23.8% | +82.6 | `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 28.6% | +235.9 | 6.44 | 9.02 | 0 | 2 | demo_watch_candidate |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 42 | S_STRANGER | 23.8% | -33.0 | `feature_momentum_breakout_exception` | 31 | S_STRANGER | 32.3% | +128.9 | 1.56 | 2.69 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74` | 17 | S_STRANGER | 23.5% | -62.0 | `feature_fresh_reclaim_within_8` | 6 | R_REPEATER | 50.0% | +94.2 | 3.60 | 1.80 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 30 | S_STRANGER | 23.3% | -168.5 | `feature_momentum_breakout_exception` | 24 | S_STRANGER | 29.2% | +25.8 | 1.12 | 2.24 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 65 | S_STRANGER | 23.1% | -166.4 | `tdi_rsi_gt_signal` | 36 | S_STRANGER | 36.1% | +273.7 | 1.72 | 1.72 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 23.1% | -378.0 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 28.6% | -672.7 | 0.28 | 0.71 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 31 | S_STRANGER | 22.6% | -70.1 | `confluence_gte_60` | 15 | S_STRANGER | 26.7% | -53.5 | 0.71 | 1.76 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 31 | S_STRANGER | 22.6% | -318.5 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 14.3% | +90.7 | 1.70 | 3.40 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 54 | S_STRANGER | 22.2% | -319.9 | `feature_momentum_breakout_exception` | 36 | S_STRANGER | 30.6% | -84.2 | 0.63 | 1.22 | 0 | 0 | fail |
| `STOP_HUNT|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 23 | S_STRANGER | 21.7% | +124.2 | `feature_eurjpy_tdi50_reclaim` | 12 | S_STRANGER | 25.0% | +312.1 | 2.22 | 4.45 | 0 | 1 | watch_research |
| `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 37 | S_STRANGER | 21.6% | -54.4 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 31.2% | +79.6 | 1.52 | 1.52 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | +62.9 | `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 25.0% | +117.0 | 1.65 | 2.31 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | -131.4 | `confluence_gte_60` | 9 | S_STRANGER | 22.2% | -81.0 | 0.37 | 1.28 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | -1339.0 | `feature_momentum_breakout_exception` | 9 | S_STRANGER | 33.3% | -141.2 | 0.25 | 0.51 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 52 | S_STRANGER | 21.2% | -79.4 | `feature_momentum_breakout_exception` | 42 | S_STRANGER | 26.2% | +62.9 | 1.33 | 2.65 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_50_74` | 19 | S_STRANGER | 21.1% | -82.6 | `feature_momentum_breakout_exception` | 14 | S_STRANGER | 28.6% | +65.3 | 1.58 | 1.84 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 19 | S_STRANGER | 21.1% | -591.6 | `feature_momentum_breakout_exception` | 8 | R_REPEATER | 50.0% | +114.9 | 2.19 | 2.19 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 48 | S_STRANGER | 20.8% | -136.0 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 42.9% | +24.7 | 1.09 | 1.46 | 0 | 0 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 20.0% | -4.9 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 22.2% | +9.0 | 1.11 | 2.21 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -85.3 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 25.0% | -51.5 | 0.52 | 1.30 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 20.0% | -134.9 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | -31.8 | 0.75 | 0.75 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -204.1 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 28.6% | +44.3 | 1.15 | 2.89 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 20.0% | -241.7 | `feature_momentum_breakout_exception` | 13 | S_STRANGER | 23.1% | -200.0 | 0.26 | 0.79 | 0 | 0 | fail |
| `RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 25 | S_STRANGER | 20.0% | -437.5 | `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 40.0% | +117.7 | 1.86 | 2.79 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 20.0% | -493.5 | `tdi_rsi_gt_signal` | 10 | S_STRANGER | 30.0% | -147.8 | 0.82 | 0.82 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_75_PLUS` | 21 | S_STRANGER | 19.0% | -75.5 | `feature_momentum_breakout_exception` | 17 | S_STRANGER | 23.5% | -26.4 | 0.78 | 1.57 | 0 | 0 | fail |
| `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 27 | S_STRANGER | 18.5% | -80.9 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 27.3% | +133.1 | 2.99 | 2.00 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 33 | S_STRANGER | 18.2% | -90.5 | `confluence_gte_60` | 12 | S_STRANGER | 25.0% | +2.7 | 1.02 | 1.28 | 0 | 1 | watch_research |
| `RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 18.2% | -121.4 | `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 40.0% | +49.6 | 1.59 | 2.39 | 0 | 1 | watch_research |
| `THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -141.7 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 28.6% | -189.1 | 0.28 | 0.71 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -172.1 | `confluence_gte_60` | 8 | S_STRANGER | 25.0% | -203.6 | 0.38 | 0.64 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -214.4 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 40.0% | +390.4 | 1.48 | 0.98 | 0 | 1 | watch_research |
| `RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -1169.4 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 22.2% | -1022.6 | 0.23 | 0.47 | 0 | 0 | fail |
| `THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | S_STRANGER | 17.6% | -204.7 | `tdi_rsi_gte_50` | 6 | R_REPEATER | 50.0% | +109.2 | 2.04 | 1.02 | 0 | 2 | demo_watch_candidate |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_50_74` | 17 | S_STRANGER | 17.6% | -234.1 | `feature_momentum_breakout_exception` | 9 | S_STRANGER | 33.3% | -35.8 | 0.68 | 1.35 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 17 | S_STRANGER | 17.6% | -286.3 | `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 30.0% | -88.6 | 0.80 | 1.86 | 1 | 1 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74` | 29 | S_STRANGER | 17.2% | -140.5 | `feature_momentum_breakout_exception` | 17 | S_STRANGER | 29.4% | +50.8 | 1.37 | 2.74 | 0 | 1 | watch_research |
| `THE_33_MW|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 16.7% | -30.7 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 28.6% | +169.3 | 2.36 | 3.15 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -303.2 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 25.0% | -75.9 | 0.60 | 1.81 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -639.9 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 40.0% | +101.6 | 1.82 | 1.82 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 37 | S_STRANGER | 16.2% | -532.2 | `feature_momentum_breakout_exception` | 19 | S_STRANGER | 26.3% | -102.6 | 0.44 | 1.07 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 44 | S_STRANGER | 15.9% | -1028.4 | `feature_momentum_breakout_exception` | 18 | S_STRANGER | 38.9% | +425.7 | 2.15 | 3.37 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 15.8% | -74.6 | `feature_momentum_breakout_exception` | 18 | S_STRANGER | 16.7% | -63.6 | 0.64 | 1.66 | 0 | 1 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 57 | S_STRANGER | 15.8% | -212.4 | `confluence_gte_60` | 11 | S_STRANGER | 45.5% | +385.6 | 8.49 | 3.19 | 0 | 2 | demo_watch_candidate |
| `RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -54.0 | `confluence_gte_60` | 5 | S_STRANGER | 20.0% | +162.9 | 2.10 | 6.29 | 0 | 0 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 40 | S_STRANGER | 15.0% | -496.4 | `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 28.6% | +16.1 | 1.06 | 2.66 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -357.2 | `confluence_gte_60` | 5 | S_STRANGER | 20.0% | +23.2 | 1.11 | 2.22 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 28 | S_STRANGER | 14.3% | -410.1 | `feature_momentum_breakout_exception` | 18 | S_STRANGER | 22.2% | -84.4 | 0.37 | 1.11 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -1245.8 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 28.6% | -100.4 | 0.69 | 1.72 | 0 | 0 | fail |
| `STOP_HUNT|BUY|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 13.3% | -186.3 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 22.2% | -163.9 | 0.19 | 0.67 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 45 | S_STRANGER | 13.3% | -303.6 | `feature_momentum_breakout_exception` | 36 | S_STRANGER | 16.7% | -170.9 | 0.45 | 1.28 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 23 | S_STRANGER | 13.0% | -578.7 | `feature_momentum_breakout_exception` | 13 | S_STRANGER | 23.1% | -161.7 | 0.29 | 0.78 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 32 | S_STRANGER | 12.5% | -1085.9 | `feature_momentum_breakout_exception` | 13 | S_STRANGER | 30.8% | +103.5 | 1.38 | 1.61 | 0 | 1 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74` | 17 | S_STRANGER | 11.8% | -144.9 | `feature_momentum_breakout_exception` | 11 | S_STRANGER | 18.2% | -43.8 | 0.69 | 3.11 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 36 | S_STRANGER | 11.1% | -1445.6 | `feature_momentum_breakout_exception` | 7 | R_REPEATER | 57.1% | -20.7 | 0.95 | 0.71 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 10.0% | -74.3 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 14.3% | -24.3 | 0.89 | 2.22 | 0 | 0 | fail |
| `STOP_HUNT|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -143.6 | `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 11.1% | -39.3 | 0.81 | 2.44 | 0 | 0 | fail |
| `RRT_REVERSAL|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -1131.4 | `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 11.1% | -928.2 | 0.06 | 0.48 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 20 | S_STRANGER | 10.0% | -1376.7 | `feature_momentum_breakout_exception` | 12 | S_STRANGER | 16.7% | -573.9 | 0.24 | 1.08 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L2|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -2269.4 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 12.5% | -2692.1 | 0.03 | 0.21 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 31 | S_STRANGER | 9.7% | -483.4 | `feature_momentum_breakout_exception` | 21 | S_STRANGER | 14.3% | -22.6 | 0.91 | 3.64 | 0 | 1 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -52.8 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 12.5% | -74.1 | 0.57 | 1.15 | 0 | 1 | fail |
| `RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 11 | S_STRANGER | 9.1% | -80.2 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 14.3% | +155.7 | 1.58 | 1.18 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -182.7 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 12.5% | -229.6 | 0.21 | 1.46 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -315.3 | `feature_momentum_breakout_exception` | 9 | S_STRANGER | 11.1% | -319.7 | 0.19 | 0.38 | 0 | 0 | fail |
| `THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 11 | S_STRANGER | 9.1% | -336.0 | `feature_fresh_reclaim_within_8` | 7 | S_STRANGER | 14.3% | -421.4 | 0.01 | 0.04 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 11 | S_STRANGER | 9.1% | -1721.3 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 12.5% | -1199.1 | 0.06 | 0.39 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 56 | S_STRANGER | 8.9% | -236.3 | `feature_momentum_breakout_exception` | 34 | S_STRANGER | 14.7% | -163.8 | 0.33 | 1.80 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 24 | S_STRANGER | 8.3% | -176.3 | `feature_momentum_breakout_exception` | 15 | S_STRANGER | 13.3% | +334.1 | 1.87 | 11.21 | 0 | 1 | watch_research |
| `THE_33_MW|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 12 | S_STRANGER | 8.3% | -253.5 | `feature_momentum_breakout_exception` | 10 | S_STRANGER | 10.0% | -325.6 | 0.03 | 0.20 | 0 | 0 | fail |
| `RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 8.3% | -260.3 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 20.0% | -250.2 | 0.47 | 1.86 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 8.3% | -1092.8 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 12.5% | -1285.0 | 0.00 | 0.02 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 37 | S_STRANGER | 8.1% | -729.4 | `feature_momentum_breakout_exception` | 21 | S_STRANGER | 14.3% | -193.7 | 0.60 | 2.24 | 0 | 1 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 37 | S_STRANGER | 8.1% | -822.5 | `tdi_rsi_gt_signal` | 16 | S_STRANGER | 18.8% | -418.6 | 0.47 | 1.03 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 7.7% | -351.9 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 20.0% | +10.6 | 1.10 | 4.38 | 0 | 1 | watch_research |
| `STOP_HUNT|SELL|MID_WEEK|L2|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 7.7% | -1974.2 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 8.3% | -2127.1 | 0.03 | 0.35 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 27 | S_STRANGER | 7.4% | -349.3 | `confluence_gte_60` | 5 | S_STRANGER | 20.0% | -242.2 | 0.25 | 1.02 | 0 | 0 | fail |
| `THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 15 | S_STRANGER | 6.7% | -339.6 | `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 12.5% | +91.9 | 1.46 | 8.76 | 0 | 0 | watch_research |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 50 | S_STRANGER | 6.0% | -722.3 | `feature_momentum_breakout_exception` | 20 | S_STRANGER | 15.0% | -84.4 | 0.52 | 1.68 | 0 | 1 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74` | 17 | S_STRANGER | 5.9% | -76.5 | `confluence_gte_60` | 6 | S_STRANGER | 16.7% | -44.5 | 0.64 | 2.57 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 17 | S_STRANGER | 5.9% | -2738.4 | `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 9.1% | -1953.2 | 0.04 | 0.40 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 70 | S_STRANGER | 5.7% | -804.9 | `feature_momentum_breakout_exception` | 20 | S_STRANGER | 20.0% | -154.2 | 0.32 | 0.90 | 0 | 1 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 18 | S_STRANGER | 5.6% | -1011.4 | `all` | 18 | S_STRANGER | 5.6% | -1011.4 | 0.05 | 0.39 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 22 | S_STRANGER | 4.5% | -765.1 | `feature_momentum_breakout_exception` | 11 | S_STRANGER | 9.1% | -344.1 | 0.14 | 1.12 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 29 | S_STRANGER | 3.4% | -1070.5 | `feature_fresh_reclaim_within_8` | 7 | S_STRANGER | 14.3% | -1588.3 | 0.13 | 0.77 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 0.0% | -281.8 | `feature_momentum_breakout_exception` | 10 | S_STRANGER | 0.0% | -248.4 | 0.00 | 0.00 | 0 | 0 | fail |
| `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 24 | S_STRANGER | 0.0% | -1311.6 | `all` | 24 | S_STRANGER | 0.0% | -1311.6 | 0.01 | 0.23 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 17 | S_STRANGER | 0.0% | -2007.6 | `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 0.0% | -1853.8 | 0.00 | 0.00 | 0 | 0 | fail |
| `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -3021.0 | `feature_momentum_breakout_exception` | 7 | S_STRANGER | 0.0% | -1916.6 | 0.00 | 0.00 | 0 | 0 | fail |

## Candidate Details

### RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=83.3% Avg=+416.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

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

### RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=100.0% Avg=+867.0; validation N=2 Fav=100.0% Avg=+625.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +549.0 | 9.66 | 4.14 | +858.3 | +251.8 |
| `hunt_to_ar_ratio_le_2_0` | 6 | R_RUNNER | 54.5% | 83.3% | 83.3% | 33.3% | +623.3 | 34.39 | 6.88 | +856.0 | +280.3 |
| `hunt_to_ar_ratio_le_2_5` | 6 | R_RUNNER | 54.5% | 83.3% | 83.3% | 33.3% | +623.3 | 34.39 | 6.88 | +856.0 | +280.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +549.0 | 9.66 | 4.14 | +858.3 | +251.8 |
| `confluence_gte_60` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +549.0 | 9.66 | 4.14 | +858.3 | +251.8 |
| `confluence_gte_70` | 11 | R_REPEATER | 100.0% | 63.6% | 63.6% | 36.4% | +549.0 | 9.66 | 4.14 | +858.3 | +251.8 |
| `tdi_rsi_gt_signal` | 10 | R_REPEATER | 90.9% | 70.0% | 70.0% | 40.0% | +615.1 | 11.51 | 3.29 | +928.9 | +261.4 |
| `tdi_rsi_gte_50` | 8 | R_RUNNER | 72.7% | 75.0% | 75.0% | 25.0% | +672.6 | 10.09 | 3.36 | +1009.8 | +292.9 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_RUNNER | 54.5% | 83.3% | 83.3% | 33.3% | +623.3 | 34.39 | 6.88 | +856.0 | +280.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | R_RUNNER | 45.5% | 100.0% | 100.0% | 40.0% | +770.4 | 999.00 | 999.00 | +996.8 | +305.2 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 0.0% | +372.0 | 999.00 | 999.00 | +654.0 | +467.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 90.9% | 60.0% | 60.0% | 30.0% | +338.0 | 5.85 | 2.92 | +640.2 | +259.2 |
| `feature_momentum_breakout_exception` | 10 | R_REPEATER | 90.9% | 60.0% | 60.0% | 40.0% | +566.7 | 9.13 | 4.57 | +878.7 | +230.3 |
| `feature_eurjpy_tdi50_reclaim` | 8 | R_RUNNER | 72.7% | 75.0% | 75.0% | 25.0% | +672.6 | 10.09 | 3.36 | +1009.8 | +292.9 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=71.4% Avg=+330.9; out_of_sample N=2 Fav=50.0% Avg=+617.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `hunt_to_ar_ratio_le_2_0` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `hunt_to_ar_ratio_le_2_5` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `confluence_gte_60` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `confluence_gte_70` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 72.7% | 62.5% | 62.5% | 62.5% | +526.1 | 5.26 | 2.10 | +1566.1 | +357.7 |
| `tdi_rsi_gte_50` | 9 | R_REPEATER | 81.8% | 55.6% | 55.6% | 66.7% | +330.7 | 2.62 | 1.57 | +1343.1 | +420.0 |
| `ratio_le_2_and_asian_gte_30` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 72.7% | 62.5% | 62.5% | 62.5% | +526.1 | 5.26 | 2.10 | +1566.1 | +357.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 54.5% | +233.0 | 1.76 | 1.17 | +1282.5 | +368.5 |
| `feature_momentum_breakout_exception` | 9 | R_REPEATER | 81.8% | 66.7% | 66.7% | 66.7% | +394.6 | 2.49 | 0.83 | +1407.4 | +185.7 |
| `feature_eurjpy_tdi50_reclaim` | 9 | R_REPEATER | 81.8% | 55.6% | 55.6% | 66.7% | +330.7 | 2.62 | 1.57 | +1343.1 | +420.0 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=66.7% Avg=+398.2; out_of_sample N=5 Fav=40.0% Avg=-448.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `confluence_gte_60` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `confluence_gte_70` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 0.0% | -25.4 | 0.92 | 1.38 | +908.2 | +617.2 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 16.7% | +352.3 | 2.06 | 2.06 | +1372.3 | +552.0 |
| `ratio_le_2_and_asian_gte_30` | 11 | R_REPEATER | 100.0% | 54.5% | 54.5% | 9.1% | +13.5 | 1.02 | 0.85 | +1163.0 | +999.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 0.0% | -25.4 | 0.92 | 1.38 | +908.2 | +617.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 90.9% | 50.0% | 50.0% | 10.0% | -192.4 | 0.72 | 0.72 | +1017.5 | +1059.3 |
| `feature_momentum_breakout_exception` | 8 | R_REPEATER | 72.7% | 50.0% | 50.0% | 12.5% | -304.8 | 0.62 | 0.62 | +844.9 | +1213.4 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 16.7% | +352.3 | 2.06 | 2.06 | +1372.3 | +552.0 |

### RRT_REVERSAL|SELL|EARLY_WEEK|L0|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|EARLY_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=58.3% Avg=+260.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | R_REPEATER | 100.0% | 53.3% | 53.3% | 26.7% | +224.9 | 6.36 | 5.57 | +461.7 | +127.9 |
| `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 80.0% | 58.3% | 58.3% | 33.3% | +260.3 | 6.73 | 4.81 | +502.1 | +142.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 80.0% | 58.3% | 58.3% | 33.3% | +260.3 | 6.73 | 4.81 | +502.1 | +142.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | R_REPEATER | 100.0% | 53.3% | 53.3% | 26.7% | +224.9 | 6.36 | 5.57 | +461.7 | +127.9 |
| `confluence_gte_60` | 9 | S_STRANGER | 60.0% | 44.4% | 44.4% | 11.1% | +208.4 | 8.33 | 10.41 | +400.7 | +120.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 80.0% | 41.7% | 41.7% | 25.0% | +104.4 | 2.99 | 4.19 | +317.2 | +135.0 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -72.0 | 0.41 | 0.82 | +137.3 | +132.7 |
| `ratio_le_2_and_asian_gte_30` | 12 | R_REPEATER | 80.0% | 58.3% | 58.3% | 33.3% | +260.3 | 6.73 | 4.81 | +502.1 | +142.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | R_REPEATER | 66.7% | 50.0% | 50.0% | 30.0% | +133.7 | 3.45 | 3.45 | +357.7 | +145.3 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -358.0 | 0.00 | 0.00 | +0.0 | +191.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | R_REPEATER | 100.0% | 53.3% | 53.3% | 26.7% | +224.9 | 6.36 | 5.57 | +461.7 | +127.9 |
| `feature_momentum_breakout_exception` | 14 | R_REPEATER | 93.3% | 57.1% | 57.1% | 28.6% | +266.5 | 14.77 | 11.08 | +494.6 | +123.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -72.0 | 0.41 | 0.82 | +137.3 | +132.7 |

### THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+173.3; validation N=3 Fav=66.7% Avg=+966.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 50.0% | +233.4 | 2.82 | 2.82 | +619.0 | +137.9 |
| `hunt_to_ar_ratio_le_2_0` | 9 | R_REPEATER | 75.0% | 55.6% | 55.6% | 55.6% | +276.9 | 2.66 | 2.12 | +760.0 | +151.8 |
| `hunt_to_ar_ratio_le_2_5` | 9 | R_REPEATER | 75.0% | 55.6% | 55.6% | 55.6% | +276.9 | 2.66 | 2.12 | +760.0 | +151.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 50.0% | +233.4 | 2.82 | 2.82 | +619.0 | +137.9 |
| `confluence_gte_60` | 9 | R_REPEATER | 75.0% | 55.6% | 55.6% | 55.6% | +398.7 | 7.08 | 5.67 | +740.0 | +148.9 |
| `confluence_gte_70` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | -31.5 | 0.86 | 0.86 | +766.0 | +303.5 |
| `tdi_rsi_gt_signal` | 7 | R_REPEATER | 58.3% | 57.1% | 57.1% | 57.1% | +513.0 | 51.58 | 38.68 | +877.6 | +66.3 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 50.0% | 50.0% | 50.0% | 50.0% | +380.7 | 3.16 | 3.16 | +777.3 | +107.8 |
| `ratio_le_2_and_asian_gte_30` | 9 | R_REPEATER | 75.0% | 55.6% | 55.6% | 55.6% | +276.9 | 2.66 | 2.12 | +760.0 | +151.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_RUNNER | 33.3% | 75.0% | 75.0% | 75.0% | +820.8 | 97.56 | 32.52 | +1388.7 | +43.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 50.0% | +233.4 | 2.82 | 2.82 | +619.0 | +137.9 |
| `feature_momentum_breakout_exception` | 11 | R_REPEATER | 91.7% | 54.5% | 54.5% | 54.5% | +339.0 | 7.07 | 5.89 | +670.6 | +143.1 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 50.0% | 50.0% | 50.0% | 50.0% | +380.7 | 3.16 | 3.16 | +777.3 | +107.8 |

### STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=57.1% Avg=+319.9; out_of_sample N=3 Fav=66.7% Avg=+368.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 16.7% | +227.2 | 1.84 | 1.84 | +1005.1 | +608.3 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 14.3% | +141.1 | 1.72 | 2.30 | +871.9 | +352.0 |
| `hunt_to_ar_ratio_le_2_5` | 9 | R_REPEATER | 75.0% | 55.6% | 55.6% | 11.1% | +429.8 | 3.83 | 3.06 | +1117.6 | +515.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 16.7% | +227.2 | 1.84 | 1.84 | +1005.1 | +608.3 |
| `confluence_gte_60` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 16.7% | +227.2 | 1.84 | 1.84 | +1005.1 | +608.3 |
| `confluence_gte_70` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 16.7% | +227.2 | 1.84 | 1.84 | +1005.1 | +608.3 |
| `tdi_rsi_gt_signal` | 6 | R_REPEATER | 50.0% | 50.0% | 50.0% | 16.7% | +399.8 | 2.17 | 2.17 | +1159.0 | +773.7 |
| `tdi_rsi_gte_50` | 10 | R_REPEATER | 83.3% | 60.0% | 60.0% | 20.0% | +334.5 | 2.27 | 1.51 | +1139.9 | +631.5 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 14.3% | +141.1 | 1.72 | 2.30 | +871.9 | +352.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 33.3% | +299.3 | 2.33 | 4.66 | +990.0 | +338.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 9.1% | +180.8 | 1.61 | 1.93 | +937.8 | +623.6 |
| `feature_momentum_breakout_exception` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 16.7% | +227.2 | 1.84 | 1.84 | +1005.1 | +608.3 |
| `feature_eurjpy_tdi50_reclaim` | 10 | R_REPEATER | 83.3% | 60.0% | 60.0% | 20.0% | +334.5 | 2.27 | 1.51 | +1139.9 | +631.5 |

### STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=14 Fav=50.0% Avg=+147.4; out_of_sample N=4 Fav=50.0% Avg=+86.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 27.8% | +133.9 | 1.34 | 1.34 | +813.2 | +709.9 |
| `hunt_to_ar_ratio_le_2_0` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 27.8% | +133.9 | 1.34 | 1.34 | +813.2 | +709.9 |
| `hunt_to_ar_ratio_le_2_5` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 27.8% | +133.9 | 1.34 | 1.34 | +813.2 | +709.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 27.8% | +133.9 | 1.34 | 1.34 | +813.2 | +709.9 |
| `confluence_gte_60` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 27.8% | +133.9 | 1.34 | 1.34 | +813.2 | +709.9 |
| `confluence_gte_70` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 27.8% | +133.9 | 1.34 | 1.34 | +813.2 | +709.9 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 0.0% | -275.7 | 0.51 | 1.02 | +544.3 | +1212.7 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 66.7% | 50.0% | 50.0% | 16.7% | -43.4 | 0.91 | 0.91 | +718.7 | +892.4 |
| `ratio_le_2_and_asian_gte_30` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 27.8% | +133.9 | 1.34 | 1.34 | +813.2 | +709.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 0.0% | -275.7 | 0.51 | 1.02 | +544.3 | +1212.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 18 | R_REPEATER | 100.0% | 50.0% | 50.0% | 27.8% | +133.9 | 1.34 | 1.34 | +813.2 | +709.9 |
| `feature_momentum_breakout_exception` | 17 | S_STRANGER | 94.4% | 47.1% | 47.1% | 29.4% | +91.0 | 1.22 | 1.37 | +805.5 | +734.7 |
| `feature_eurjpy_tdi50_reclaim` | 12 | R_REPEATER | 66.7% | 50.0% | 50.0% | 16.7% | -43.4 | 0.91 | 0.91 | +718.7 | +892.4 |

### STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=50.0% Avg=+85.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 20.0% | +85.3 | 1.83 | 1.83 | +473.9 | +210.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 20.0% | +85.3 | 1.83 | 1.83 | +473.9 | +210.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 20.0% | +85.3 | 1.83 | 1.83 | +473.9 | +210.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 20.0% | +85.3 | 1.83 | 1.83 | +473.9 | +210.0 |
| `confluence_gte_60` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 20.0% | +85.3 | 1.83 | 1.83 | +473.9 | +210.0 |
| `confluence_gte_70` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 20.0% | +85.3 | 1.83 | 1.83 | +473.9 | +210.0 |
| `tdi_rsi_gt_signal` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gte_50` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 50.0% | +119.7 | 3.16 | 3.16 | +300.5 | +141.8 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 20.0% | +85.3 | 1.83 | 1.83 | +473.9 | +210.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -127.0 | 0.00 | 0.00 | +85.0 | +170.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 20.0% | +85.3 | 1.83 | 1.83 | +473.9 | +210.0 |
| `feature_momentum_breakout_exception` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 20.0% | +85.3 | 1.83 | 1.83 | +473.9 | +210.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | -65.7 | 0.11 | 0.23 | +121.7 | +168.3 |

### STOP_HUNT|SELL|EARLY_WEEK|L0|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|EARLY_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=55.6% Avg=+109.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 33.3% | +82.0 | 2.36 | 2.36 | +240.7 | +105.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 83.3% | 50.0% | 50.0% | 30.0% | +82.2 | 2.14 | 2.14 | +260.3 | +106.2 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 83.3% | 50.0% | 50.0% | 30.0% | +82.2 | 2.14 | 2.14 | +260.3 | +106.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 33.3% | +82.0 | 2.36 | 2.36 | +240.7 | +105.0 |
| `confluence_gte_60` | 5 | S_STRANGER | 41.7% | 40.0% | 40.0% | 40.0% | +135.6 | 2.40 | 3.61 | +319.4 | +136.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | R_REPEATER | 75.0% | 55.6% | 55.6% | 44.4% | +109.3 | 2.42 | 1.94 | +271.1 | +111.4 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -233.0 | 0.00 | 0.00 | +121.0 | +207.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 83.3% | 50.0% | 50.0% | 30.0% | +82.2 | 2.14 | 2.14 | +260.3 | +106.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 66.7% | 50.0% | 50.0% | 37.5% | +102.0 | 2.18 | 2.18 | +284.0 | +122.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 33.3% | +82.0 | 2.36 | 2.36 | +240.7 | +105.0 |
| `feature_momentum_breakout_exception` | 11 | R_REPEATER | 91.7% | 54.5% | 54.5% | 36.4% | +110.6 | 3.47 | 2.89 | +251.6 | +95.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -233.0 | 0.00 | 0.00 | +121.0 | +207.0 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=66.7% Avg=+162.6; validation N=3 Fav=66.7% Avg=+15.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 48.0% | 52.0% | 56.0% | +92.0 | 2.22 | 1.20 | +295.1 | +169.5 |
| `hunt_to_ar_ratio_le_2_0` | 24 | R_REPEATER | 96.0% | 50.0% | 54.2% | 58.3% | +105.7 | 2.54 | 1.17 | +301.8 | +166.2 |
| `hunt_to_ar_ratio_le_2_5` | 24 | R_REPEATER | 96.0% | 50.0% | 54.2% | 58.3% | +105.7 | 2.54 | 1.17 | +301.8 | +166.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 25 | S_STRANGER | 100.0% | 48.0% | 52.0% | 56.0% | +92.0 | 2.22 | 1.20 | +295.1 | +169.5 |
| `confluence_gte_60` | 9 | R_REPEATER | 36.0% | 66.7% | 77.8% | 33.3% | +113.4 | 2.49 | 0.71 | +290.6 | +233.8 |
| `confluence_gte_70` | 1 | R_RUNNER | 4.0% | 100.0% | 100.0% | 0.0% | +612.0 | 999.00 | 999.00 | +831.0 | +658.0 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 52.0% | 30.8% | 30.8% | 61.5% | -40.6 | 0.70 | 0.87 | +248.2 | +200.3 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 68.0% | 41.2% | 47.1% | 52.9% | +67.3 | 1.80 | 1.13 | +283.8 | +191.7 |
| `ratio_le_2_and_asian_gte_30` | 24 | R_REPEATER | 96.0% | 50.0% | 54.2% | 58.3% | +105.7 | 2.54 | 1.17 | +301.8 | +166.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 48.0% | 33.3% | 33.3% | 66.7% | -24.2 | 0.81 | 0.81 | +257.8 | +196.3 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 4.0% | 0.0% | 0.0% | 0.0% | -237.0 | 0.00 | 0.00 | +133.0 | +248.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 96.0% | 45.8% | 50.0% | 58.3% | +70.3 | 1.90 | 1.11 | +272.8 | +149.2 |
| `feature_momentum_breakout_exception` | 24 | S_STRANGER | 96.0% | 45.8% | 50.0% | 58.3% | +70.3 | 1.90 | 1.11 | +272.8 | +149.2 |
| `feature_eurjpy_tdi50_reclaim` | 17 | S_STRANGER | 68.0% | 41.2% | 47.1% | 52.9% | +67.3 | 1.80 | 1.13 | +283.8 | +191.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=13 Fav=46.2% Avg=+49.7; validation N=8 Fav=62.5% Avg=+410.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 47.8% | 52.2% | 34.8% | +147.0 | 1.60 | 1.46 | +568.9 | +436.1 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 87.0% | 45.0% | 50.0% | 35.0% | +144.3 | 1.54 | 1.54 | +596.6 | +469.3 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 91.3% | 42.9% | 47.6% | 33.3% | +124.1 | 1.46 | 1.61 | +569.1 | +463.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 23 | S_STRANGER | 100.0% | 47.8% | 52.2% | 34.8% | +147.0 | 1.60 | 1.46 | +568.9 | +436.1 |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 47.8% | 52.2% | 34.8% | +147.0 | 1.60 | 1.46 | +568.9 | +436.1 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 47.8% | 52.2% | 34.8% | +147.0 | 1.60 | 1.46 | +568.9 | +436.1 |
| `tdi_rsi_gt_signal` | 18 | R_REPEATER | 78.3% | 50.0% | 55.6% | 38.9% | +218.3 | 1.84 | 1.47 | +652.9 | +424.7 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 78.3% | 44.4% | 50.0% | 33.3% | +145.2 | 1.50 | 1.50 | +621.3 | +496.8 |
| `ratio_le_2_and_asian_gte_30` | 20 | S_STRANGER | 87.0% | 45.0% | 50.0% | 35.0% | +144.3 | 1.54 | 1.54 | +596.6 | +469.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 16 | R_REPEATER | 69.6% | 50.0% | 56.2% | 37.5% | +219.3 | 1.80 | 1.40 | +682.7 | +451.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 21 | R_REPEATER | 91.3% | 52.4% | 57.1% | 38.1% | +187.1 | 1.77 | 1.33 | +617.9 | +440.8 |
| `feature_momentum_breakout_exception` | 16 | S_STRANGER | 69.6% | 37.5% | 43.8% | 37.5% | +1.5 | 1.01 | 1.30 | +357.5 | +375.3 |
| `feature_eurjpy_tdi50_reclaim` | 18 | S_STRANGER | 78.3% | 44.4% | 50.0% | 33.3% | +145.2 | 1.50 | 1.50 | +621.3 | +496.8 |

### STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=12 Fav=58.3% Avg=+304.2; out_of_sample N=1 Fav=100.0% Avg=+477.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 47.1% | 47.1% | 29.4% | +61.5 | 1.11 | 1.25 | +1596.2 | +773.8 |
| `hunt_to_ar_ratio_le_2_0` | 16 | R_REPEATER | 94.1% | 50.0% | 50.0% | 31.2% | +84.3 | 1.15 | 1.15 | +1509.8 | +797.2 |
| `hunt_to_ar_ratio_le_2_5` | 16 | R_REPEATER | 94.1% | 50.0% | 50.0% | 31.2% | +84.3 | 1.15 | 1.15 | +1509.8 | +797.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 47.1% | 47.1% | 29.4% | +61.5 | 1.11 | 1.25 | +1596.2 | +773.8 |
| `confluence_gte_60` | 13 | R_REPEATER | 76.5% | 53.8% | 53.8% | 38.5% | +305.4 | 1.63 | 1.40 | +1728.9 | +809.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 14 | R_REPEATER | 82.4% | 57.1% | 57.1% | 35.7% | +273.2 | 1.57 | 1.18 | +1723.9 | +789.3 |
| `tdi_rsi_gte_50` | 2 | R_RUNNER | 11.8% | 100.0% | 100.0% | 50.0% | +338.0 | 999.00 | 999.00 | +1443.0 | +105.5 |
| `ratio_le_2_and_asian_gte_30` | 16 | R_REPEATER | 94.1% | 50.0% | 50.0% | 31.2% | +84.3 | 1.15 | 1.15 | +1509.8 | +797.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | R_REPEATER | 76.5% | 61.5% | 61.5% | 38.5% | +317.5 | 1.65 | 1.03 | +1627.3 | +819.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 47.1% | 47.1% | 29.4% | +61.5 | 1.11 | 1.25 | +1596.2 | +773.8 |
| `feature_momentum_breakout_exception` | 16 | R_REPEATER | 94.1% | 50.0% | 50.0% | 31.2% | +154.7 | 1.31 | 1.31 | +1693.1 | +814.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_RUNNER | 11.8% | 100.0% | 100.0% | 50.0% | +338.0 | 999.00 | 999.00 | +1443.0 | +105.5 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=0.0% Avg=-105.8; validation N=10 Fav=70.0% Avg=+444.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 46.7% | 46.7% | 33.3% | +206.4 | 2.11 | 2.41 | +801.3 | +332.1 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 53.3% | 37.5% | 37.5% | 25.0% | -178.4 | 0.40 | 0.67 | +421.4 | +320.4 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 60.0% | 33.3% | 33.3% | 22.2% | -180.2 | 0.37 | 0.74 | +391.0 | +321.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 46.7% | 46.7% | 33.3% | +206.4 | 2.11 | 2.41 | +801.3 | +332.1 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 46.7% | 46.7% | 33.3% | +206.4 | 2.11 | 2.41 | +801.3 | +332.1 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 46.7% | 46.7% | 33.3% | +206.4 | 2.11 | 2.41 | +801.3 | +332.1 |
| `tdi_rsi_gt_signal` | 10 | R_REPEATER | 66.7% | 50.0% | 50.0% | 40.0% | +250.9 | 1.97 | 1.97 | +886.0 | +393.0 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 60.0% | 44.4% | 44.4% | 33.3% | +129.3 | 1.45 | 1.81 | +809.6 | +411.7 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 53.3% | 37.5% | 37.5% | 25.0% | -178.4 | 0.40 | 0.67 | +421.4 | +320.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 33.3% | 20.0% | 20.0% | 20.0% | -442.8 | 0.07 | 0.28 | +130.4 | +386.4 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -924.0 | 0.00 | 0.00 | +37.0 | +225.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 46.7% | 46.7% | 33.3% | +206.4 | 2.11 | 2.41 | +801.3 | +332.1 |
| `feature_momentum_breakout_exception` | 14 | R_REPEATER | 93.3% | 50.0% | 50.0% | 35.7% | +287.1 | 3.15 | 3.15 | +855.9 | +339.8 |
| `feature_eurjpy_tdi50_reclaim` | 9 | S_STRANGER | 60.0% | 44.4% | 44.4% | 33.3% | +129.3 | 1.45 | 1.81 | +809.6 | +411.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=75.0% Avg=+281.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 30.8% | +112.5 | 1.66 | 1.94 | +702.9 | +230.5 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 41.7% | 41.7% | 33.3% | +99.2 | 1.54 | 2.15 | +706.8 | +216.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 30.8% | +112.5 | 1.66 | 1.94 | +702.9 | +230.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 30.8% | +112.5 | 1.66 | 1.94 | +702.9 | +230.5 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 30.8% | +112.5 | 1.66 | 1.94 | +702.9 | +230.5 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 46.2% | 46.2% | 30.8% | +112.5 | 1.66 | 1.94 | +702.9 | +230.5 |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 100.0% | +889.0 | 999.00 | 999.00 | +2093.0 | +29.0 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 36.4% | +203.5 | 3.26 | 3.91 | +711.5 | +251.2 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 92.3% | 41.7% | 41.7% | 33.3% | +99.2 | 1.54 | 2.15 | +706.8 | +216.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 100.0% | +889.0 | 999.00 | 999.00 | +2093.0 | +29.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | R_REPEATER | 92.3% | 50.0% | 50.0% | 33.3% | +150.3 | 1.96 | 1.96 | +752.8 | +192.3 |
| `feature_momentum_breakout_exception` | 8 | R_RUNNER | 61.5% | 75.0% | 75.0% | 50.0% | +281.5 | 2.58 | 0.86 | +913.9 | +158.1 |
| `feature_eurjpy_tdi50_reclaim` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 36.4% | +203.5 | 3.26 | 3.91 | +711.5 | +251.2 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=44.4% Avg=+162.8; validation N=1 Fav=100.0% Avg=+222.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 27.3% | +135.9 | 2.40 | 2.88 | +389.3 | +186.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 90.9% | 50.0% | 50.0% | 30.0% | +168.7 | 2.92 | 2.92 | +376.8 | +175.5 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 27.3% | +135.9 | 2.40 | 2.88 | +389.3 | +186.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 27.3% | +135.9 | 2.40 | 2.88 | +389.3 | +186.5 |
| `confluence_gte_60` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 28.6% | +198.6 | 2.78 | 3.71 | +441.3 | +159.6 |
| `confluence_gte_70` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | -111.0 | 0.40 | 0.80 | +225.3 | +235.7 |
| `tdi_rsi_gt_signal` | 4 | R_RUNNER | 36.4% | 75.0% | 75.0% | 25.0% | +449.9 | 10.32 | 3.44 | +699.3 | +161.0 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 25.0% | +149.6 | 2.05 | 6.16 | +496.8 | +210.7 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 90.9% | 50.0% | 50.0% | 30.0% | +168.7 | 2.92 | 2.92 | +376.8 | +175.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | R_RUNNER | 27.3% | 100.0% | 100.0% | 33.3% | +664.2 | 999.00 | 999.00 | +761.0 | +116.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 90.9% | 50.0% | 50.0% | 30.0% | +166.7 | 2.86 | 2.86 | +428.0 | +187.0 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 81.8% | 44.4% | 44.4% | 22.2% | +58.9 | 1.61 | 2.01 | +312.3 | +187.2 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 25.0% | +149.6 | 2.05 | 6.16 | +496.8 | +210.7 |

### STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=14 Fav=50.0% Avg=+210.5; validation N=3 Fav=33.3% Avg=+6.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 16.7% | +153.4 | 2.29 | 2.86 | +502.9 | +331.7 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 72.2% | 46.2% | 46.2% | 23.1% | +206.5 | 2.78 | 3.24 | +550.2 | +364.8 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 83.3% | 46.7% | 46.7% | 20.0% | +190.9 | 2.73 | 3.12 | +511.7 | +337.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 16.7% | +153.4 | 2.29 | 2.86 | +502.9 | +331.7 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 16.7% | +153.4 | 2.29 | 2.86 | +502.9 | +331.7 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 16.7% | +153.4 | 2.29 | 2.86 | +502.9 | +331.7 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 94.4% | 47.1% | 47.1% | 17.6% | +174.5 | 2.53 | 2.85 | +511.8 | +321.4 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -159.0 | 0.00 | 0.00 | +178.7 | +437.7 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 72.2% | 46.2% | 46.2% | 23.1% | +206.5 | 2.78 | 3.24 | +550.2 | +364.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 72.2% | 46.2% | 46.2% | 23.1% | +206.5 | 2.78 | 3.24 | +550.2 | +364.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 16.7% | +153.4 | 2.29 | 2.86 | +502.9 | +331.7 |
| `feature_momentum_breakout_exception` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 16.7% | +153.4 | 2.29 | 2.86 | +502.9 | +331.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -213.5 | 0.00 | 0.00 | +126.0 | +335.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+663.0; validation N=9 Fav=44.4% Avg=-11.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 56.2% | +9.0 | 1.02 | 0.88 | +648.9 | +294.9 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 87.5% | 42.9% | 42.9% | 57.1% | +0.9 | 1.00 | 0.84 | +721.1 | +329.9 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 56.2% | +9.0 | 1.02 | 0.88 | +648.9 | +294.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 56.2% | +9.0 | 1.02 | 0.88 | +648.9 | +294.9 |
| `confluence_gte_60` | 10 | R_REPEATER | 62.5% | 50.0% | 50.0% | 50.0% | +55.9 | 1.10 | 0.88 | +937.9 | +372.4 |
| `confluence_gte_70` | 3 | R_REPEATER | 18.8% | 66.7% | 66.7% | 33.3% | +205.0 | 6.91 | 3.46 | +655.3 | +101.3 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 50.0% | 37.5% | 37.5% | 37.5% | -34.4 | 0.87 | 1.16 | +529.2 | +442.7 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 43.8% | 42.9% | 42.9% | 57.1% | +248.7 | 3.66 | 2.44 | +713.1 | +279.1 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 87.5% | 42.9% | 42.9% | 57.1% | +0.9 | 1.00 | 0.84 | +721.1 | +329.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 43.8% | 42.9% | 42.9% | 42.9% | -36.7 | 0.88 | 0.88 | +588.0 | +496.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 56.2% | +9.0 | 1.02 | 0.88 | +648.9 | +294.9 |
| `feature_momentum_breakout_exception` | 16 | S_STRANGER | 100.0% | 43.8% | 43.8% | 56.2% | +9.0 | 1.02 | 0.88 | +648.9 | +294.9 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 43.8% | 42.9% | 42.9% | 57.1% | +248.7 | 3.66 | 2.44 | +713.1 | +279.1 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=11 Fav=54.5% Avg=+346.6; validation N=3 Fav=33.3% Avg=-96.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 43.5% | 43.5% | 43.5% | +175.1 | 2.55 | 2.81 | +524.3 | +227.9 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 78.3% | 44.4% | 44.4% | 38.9% | +230.4 | 3.87 | 4.35 | +584.6 | +192.6 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 82.6% | 42.1% | 42.1% | 36.8% | +215.6 | 3.74 | 4.67 | +554.7 | +187.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 23 | S_STRANGER | 100.0% | 43.5% | 43.5% | 43.5% | +175.1 | 2.55 | 2.81 | +524.3 | +227.9 |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 43.5% | 43.5% | 43.5% | +175.1 | 2.55 | 2.81 | +524.3 | +227.9 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 43.5% | 43.5% | 43.5% | +175.1 | 2.55 | 2.81 | +524.3 | +227.9 |
| `tdi_rsi_gt_signal` | 18 | R_REPEATER | 78.3% | 50.0% | 50.0% | 44.4% | +191.9 | 2.54 | 2.25 | +540.8 | +247.1 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 82.6% | 42.1% | 42.1% | 36.8% | +180.8 | 2.48 | 3.10 | +552.1 | +236.6 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 78.3% | 44.4% | 44.4% | 38.9% | +230.4 | 3.87 | 4.35 | +584.6 | +192.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | R_REPEATER | 60.9% | 50.0% | 50.0% | 35.7% | +251.7 | 4.06 | 4.06 | +586.6 | +197.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 43.5% | 43.5% | 43.5% | +175.1 | 2.55 | 2.81 | +524.3 | +227.9 |
| `feature_momentum_breakout_exception` | 22 | S_STRANGER | 95.7% | 40.9% | 40.9% | 45.5% | +136.3 | 2.16 | 2.64 | +500.5 | +234.7 |
| `feature_eurjpy_tdi50_reclaim` | 19 | S_STRANGER | 82.6% | 42.1% | 42.1% | 36.8% | +180.8 | 2.48 | 3.10 | +552.1 | +236.6 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+78.7; validation N=10 Fav=50.0% Avg=+51.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 43.5% | 47.8% | 43.5% | +36.2 | 1.18 | 1.07 | +553.8 | +360.7 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 91.3% | 42.9% | 42.9% | 42.9% | -11.0 | 0.95 | 1.06 | +547.1 | +379.8 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 95.7% | 45.5% | 45.5% | 45.5% | +22.2 | 1.10 | 1.10 | +561.3 | +363.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 23 | S_STRANGER | 100.0% | 43.5% | 47.8% | 43.5% | +36.2 | 1.18 | 1.07 | +553.8 | +360.7 |
| `confluence_gte_60` | 19 | S_STRANGER | 82.6% | 36.8% | 42.1% | 36.8% | -29.5 | 0.88 | 0.99 | +541.6 | +421.1 |
| `confluence_gte_70` | 7 | S_STRANGER | 30.4% | 28.6% | 42.9% | 0.0% | -26.9 | 0.90 | 1.20 | +486.4 | +466.4 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 56.5% | 46.2% | 46.2% | 38.5% | +58.0 | 1.23 | 1.23 | +645.1 | +292.0 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 43.5% | 40.0% | 40.0% | 30.0% | +108.2 | 1.53 | 1.91 | +644.9 | +335.5 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 91.3% | 42.9% | 42.9% | 42.9% | -11.0 | 0.95 | 1.06 | +547.1 | +379.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 52.2% | 41.7% | 41.7% | 33.3% | +2.8 | 1.01 | 1.21 | +627.2 | +313.9 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -260.0 | 0.00 | 0.00 | +370.0 | +348.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 43.5% | 47.8% | 43.5% | +36.2 | 1.18 | 1.07 | +553.8 | +360.7 |
| `feature_momentum_breakout_exception` | 22 | S_STRANGER | 95.7% | 40.9% | 45.5% | 45.5% | +14.5 | 1.07 | 1.07 | +535.9 | +371.5 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 43.5% | 40.0% | 40.0% | 30.0% | +108.2 | 1.53 | 1.91 | +644.9 | +335.5 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=70.0% Avg=+75.3; validation N=7 Fav=42.9% Avg=-4.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 32.1% | -61.1 | 0.59 | 0.74 | +247.7 | +245.8 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 82.1% | 47.8% | 47.8% | 34.8% | -31.8 | 0.75 | 0.75 | +272.0 | +225.0 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 85.7% | 45.8% | 45.8% | 33.3% | -39.5 | 0.70 | 0.77 | +265.4 | +228.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 32.1% | -61.1 | 0.59 | 0.74 | +247.7 | +245.8 |
| `confluence_gte_60` | 17 | R_REPEATER | 60.7% | 58.8% | 58.8% | 47.1% | +42.6 | 1.57 | 0.94 | +246.2 | +219.8 |
| `confluence_gte_70` | 1 | R_RUNNER | 3.6% | 100.0% | 100.0% | 100.0% | +95.0 | 999.00 | 999.00 | +218.0 | +1.0 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 71.4% | 40.0% | 40.0% | 30.0% | -78.8 | 0.50 | 0.75 | +256.2 | +261.9 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 35.7% | 40.0% | 40.0% | 30.0% | -65.5 | 0.41 | 0.61 | +231.8 | +194.3 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 82.1% | 47.8% | 47.8% | 34.8% | -31.8 | 0.75 | 0.75 | +272.0 | +225.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 60.7% | 41.2% | 41.2% | 29.4% | -76.3 | 0.51 | 0.73 | +271.3 | +266.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 42.9% | 42.9% | 32.1% | -61.1 | 0.59 | 0.74 | +247.7 | +245.8 |
| `feature_momentum_breakout_exception` | 23 | S_STRANGER | 82.1% | 39.1% | 39.1% | 39.1% | -80.3 | 0.54 | 0.78 | +264.4 | +264.2 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 35.7% | 40.0% | 40.0% | 30.0% | -65.5 | 0.41 | 0.61 | +231.8 | +194.3 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=20 Fav=45.0% Avg=+219.9; validation N=11 Fav=36.4% Avg=+87.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 41.9% | 45.2% | 35.5% | +172.9 | 3.47 | 3.47 | +475.6 | +197.5 |
| `hunt_to_ar_ratio_le_2_0` | 28 | S_STRANGER | 90.3% | 39.3% | 39.3% | 35.7% | +178.8 | 3.30 | 4.20 | +460.1 | +190.3 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 93.5% | 41.4% | 41.4% | 37.9% | +176.5 | 3.35 | 3.91 | +462.8 | +186.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 31 | S_STRANGER | 100.0% | 41.9% | 45.2% | 35.5% | +172.9 | 3.47 | 3.47 | +475.6 | +197.5 |
| `confluence_gte_60` | 31 | S_STRANGER | 100.0% | 41.9% | 45.2% | 35.5% | +172.9 | 3.47 | 3.47 | +475.6 | +197.5 |
| `confluence_gte_70` | 31 | S_STRANGER | 100.0% | 41.9% | 45.2% | 35.5% | +172.9 | 3.47 | 3.47 | +475.6 | +197.5 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 6.5% | 0.0% | 0.0% | 50.0% | -12.0 | 0.00 | 0.00 | +240.5 | +225.0 |
| `tdi_rsi_gte_50` | 30 | S_STRANGER | 96.8% | 40.0% | 43.3% | 36.7% | +176.6 | 3.44 | 3.70 | +455.9 | +183.9 |
| `ratio_le_2_and_asian_gte_30` | 28 | S_STRANGER | 90.3% | 39.3% | 39.3% | 35.7% | +178.8 | 3.30 | 4.20 | +460.1 | +190.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 6.5% | 0.0% | 0.0% | 50.0% | -12.0 | 0.00 | 0.00 | +240.5 | +225.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 93.5% | 41.4% | 44.8% | 37.9% | +160.4 | 3.16 | 3.16 | +465.9 | +195.4 |
| `feature_momentum_breakout_exception` | 26 | S_STRANGER | 83.9% | 38.5% | 42.3% | 38.5% | +139.6 | 2.89 | 3.16 | +461.9 | +199.9 |
| `feature_eurjpy_tdi50_reclaim` | 30 | S_STRANGER | 96.8% | 40.0% | 43.3% | 36.7% | +176.6 | 3.44 | 3.70 | +455.9 | +183.9 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=42.9% Avg=+648.7; out_of_sample N=4 Fav=75.0% Avg=+3736.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 41.7% | 45.8% | 37.5% | +957.0 | 4.29 | 4.29 | +1928.2 | +754.9 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 95.8% | 43.5% | 47.8% | 39.1% | +1012.6 | 4.50 | 4.09 | +1991.0 | +740.1 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 100.0% | 41.7% | 45.8% | 37.5% | +957.0 | 4.29 | 4.29 | +1928.2 | +754.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 24 | S_STRANGER | 100.0% | 41.7% | 45.8% | 37.5% | +957.0 | 4.29 | 4.29 | +1928.2 | +754.9 |
| `confluence_gte_60` | 11 | R_REPEATER | 45.8% | 54.5% | 63.6% | 54.5% | +1771.5 | 20.91 | 5.97 | +2586.6 | +674.5 |
| `confluence_gte_70` | 7 | S_STRANGER | 29.2% | 42.9% | 42.9% | 57.1% | +269.7 | 2.93 | 1.95 | +1087.6 | +625.0 |
| `tdi_rsi_gt_signal` | 20 | R_REPEATER | 83.3% | 50.0% | 55.0% | 45.0% | +1316.8 | 8.29 | 5.27 | +2202.7 | +645.8 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -229.5 | 0.00 | 0.00 | +404.8 | +709.5 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 95.8% | 43.5% | 47.8% | 39.1% | +1012.6 | 4.50 | 4.09 | +1991.0 | +740.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 19 | R_REPEATER | 79.2% | 52.6% | 57.9% | 47.4% | +1402.9 | 9.09 | 4.96 | +2293.2 | +622.2 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +878.0 | +385.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 41.7% | 45.8% | 37.5% | +957.0 | 4.29 | 4.29 | +1928.2 | +754.9 |
| `feature_momentum_breakout_exception` | 24 | S_STRANGER | 100.0% | 41.7% | 45.8% | 37.5% | +957.0 | 4.29 | 4.29 | +1928.2 | +754.9 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -229.5 | 0.00 | 0.00 | +404.8 | +709.5 |

### STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=50.0% Avg=+227.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +96.3 | 1.49 | 2.09 | +615.4 | +224.9 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 11.1% | +68.4 | 1.30 | 1.62 | +688.9 | +255.7 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 9.1% | +122.8 | 1.63 | 1.95 | +667.0 | +237.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +96.3 | 1.49 | 2.09 | +615.4 | +224.9 |
| `confluence_gte_60` | 11 | S_STRANGER | 91.7% | 45.5% | 45.5% | 9.1% | +138.5 | 1.77 | 2.12 | +630.1 | +208.8 |
| `confluence_gte_70` | 3 | R_RUNNER | 25.0% | 100.0% | 100.0% | 0.0% | +513.3 | 999.00 | 999.00 | +725.3 | +151.7 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -557.5 | 0.00 | 0.00 | +30.0 | +216.5 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -557.5 | 0.00 | 0.00 | +30.0 | +216.5 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 11.1% | +68.4 | 1.30 | 1.62 | +688.9 | +255.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -919.0 | 0.00 | 0.00 | +12.0 | +341.0 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -557.5 | 0.00 | 0.00 | +30.0 | +216.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 8.3% | +96.3 | 1.49 | 2.09 | +615.4 | +224.9 |
| `feature_momentum_breakout_exception` | 10 | R_REPEATER | 83.3% | 50.0% | 50.0% | 10.0% | +227.0 | 2.84 | 2.84 | +732.5 | +226.6 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -557.5 | 0.00 | 0.00 | +30.0 | +216.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=12 Fav=41.7% Avg=+27.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 50.0% | 50.0% | +27.6 | 1.16 | 0.96 | +463.0 | +350.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 30.0% | 40.0% | 40.0% | +9.5 | 1.05 | 1.31 | +424.2 | +385.0 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 41.7% | 50.0% | 50.0% | +27.6 | 1.16 | 0.96 | +463.0 | +350.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 41.7% | 50.0% | 50.0% | +27.6 | 1.16 | 0.96 | +463.0 | +350.5 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 41.7% | 50.0% | 50.0% | +27.6 | 1.16 | 0.96 | +463.0 | +350.5 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 41.7% | 50.0% | 50.0% | +27.6 | 1.16 | 0.96 | +463.0 | +350.5 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 42.9% | 57.1% | 42.9% | -8.6 | 0.94 | 0.71 | +445.6 | +318.1 |
| `tdi_rsi_gte_50` | 3 | R_RUNNER | 25.0% | 100.0% | 100.0% | 66.7% | +168.0 | 999.00 | 999.00 | +605.3 | +217.7 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 83.3% | 30.0% | 40.0% | 40.0% | +9.5 | 1.05 | 1.31 | +424.2 | +385.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 41.7% | 20.0% | 40.0% | 20.0% | -59.2 | 0.71 | 1.07 | +361.0 | +374.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 41.7% | 50.0% | 50.0% | +27.6 | 1.16 | 0.96 | +463.0 | +350.5 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 100.0% | 41.7% | 50.0% | 50.0% | +27.6 | 1.16 | 0.96 | +463.0 | +350.5 |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_RUNNER | 25.0% | 100.0% | 100.0% | 66.7% | +168.0 | 999.00 | 999.00 | +605.3 | +217.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+82.2; validation N=2 Fav=50.0% Avg=+314.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 30.0% | +19.0 | 1.12 | 1.67 | +325.6 | +254.2 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +59.2 | 1.41 | 1.77 | +344.2 | +235.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 30.0% | +19.0 | 1.12 | 1.67 | +325.6 | +254.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 30.0% | +19.0 | 1.12 | 1.67 | +325.6 | +254.2 |
| `confluence_gte_60` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 66.7% | +192.7 | 2.69 | 1.34 | +496.7 | +278.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 33.3% | +217.7 | 2.90 | 1.45 | +543.7 | +243.7 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 28.6% | +111.1 | 1.81 | 2.41 | +409.1 | +235.3 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +59.2 | 1.41 | 1.77 | +344.2 | +235.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_RUNNER | 20.0% | 100.0% | 100.0% | 50.0% | +498.0 | 999.00 | 999.00 | +736.5 | +152.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 30.0% | +19.0 | 1.12 | 1.67 | +325.6 | +254.2 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 37.5% | -38.3 | 0.77 | 1.28 | +261.5 | +263.9 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 33.3% | +159.5 | 2.22 | 2.22 | +475.8 | +262.5 |

### THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+50.0; validation N=8 Fav=37.5% Avg=-2.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +3.1 | 1.01 | 1.26 | +539.1 | +429.0 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +3.4 | 1.01 | 1.26 | +573.6 | +463.4 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +3.4 | 1.01 | 1.26 | +573.6 | +463.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +3.1 | 1.01 | 1.26 | +539.1 | +429.0 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +3.1 | 1.01 | 1.26 | +539.1 | +429.0 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +3.1 | 1.01 | 1.26 | +539.1 | +429.0 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +76.3 | 1.18 | 2.37 | +756.7 | +519.3 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 50.0% | -131.5 | 0.09 | 0.17 | +235.3 | +201.8 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 33.3% | +3.4 | 1.01 | 1.26 | +573.6 | +463.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +76.3 | 1.18 | 2.37 | +756.7 | +519.3 |
| `feature_fresh_reclaim_within_8` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | -123.5 | 0.17 | 0.17 | +261.5 | +199.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +3.1 | 1.01 | 1.26 | +539.1 | +429.0 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 40.0% | +3.1 | 1.01 | 1.26 | +539.1 | +429.0 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 50.0% | -131.5 | 0.09 | 0.17 | +235.3 | +201.8 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=57.1% Avg=+155.2; validation N=5 Fav=40.0% Avg=-15.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 40.0% | 46.7% | 26.7% | -3.5 | 0.98 | 1.12 | +321.4 | +204.5 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 86.7% | 38.5% | 46.2% | 23.1% | +2.7 | 1.02 | 1.18 | +332.2 | +213.2 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 93.3% | 42.9% | 50.0% | 28.6% | +8.8 | 1.05 | 1.05 | +327.6 | +199.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 40.0% | 46.7% | 26.7% | -3.5 | 0.98 | 1.12 | +321.4 | +204.5 |
| `confluence_gte_60` | 7 | R_REPEATER | 46.7% | 57.1% | 57.1% | 42.9% | -55.1 | 0.70 | 0.52 | +341.9 | +150.1 |
| `confluence_gte_70` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 50.0% | -18.0 | 0.90 | 0.90 | +355.0 | +269.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 53.3% | 25.0% | 37.5% | 0.0% | -58.9 | 0.71 | 1.19 | +321.8 | +242.5 |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 53.3% | 50.0% | 50.0% | 25.0% | +69.2 | 1.45 | 1.45 | +388.8 | +285.4 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 86.7% | 38.5% | 46.2% | 23.1% | +2.7 | 1.02 | 1.18 | +332.2 | +213.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 46.7% | 28.6% | 42.9% | 0.0% | -42.1 | 0.80 | 1.06 | +334.1 | +238.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 40.0% | 46.7% | 26.7% | -3.5 | 0.98 | 1.12 | +321.4 | +204.5 |
| `feature_momentum_breakout_exception` | 12 | R_REPEATER | 80.0% | 50.0% | 58.3% | 33.3% | +84.3 | 1.73 | 1.24 | +373.8 | +131.8 |
| `feature_eurjpy_tdi50_reclaim` | 8 | R_REPEATER | 53.3% | 50.0% | 50.0% | 25.0% | +69.2 | 1.45 | 1.45 | +388.8 | +285.4 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+1017.5; validation N=10 Fav=40.0% Avg=+455.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +374.6 | 4.55 | 7.27 | +915.5 | +367.9 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 18.2% | +506.6 | 9.32 | 11.18 | +986.5 | +289.7 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 18.2% | +506.6 | 9.32 | 11.18 | +986.5 | +289.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +374.6 | 4.55 | 7.27 | +915.5 | +367.9 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +374.6 | 4.55 | 7.27 | +915.5 | +367.9 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 15.4% | +374.6 | 4.55 | 7.27 | +915.5 | +367.9 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -55.0 | 0.00 | 0.00 | +714.0 | +356.0 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 9.1% | +381.0 | 4.50 | 7.88 | +973.7 | +378.7 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 18.2% | +506.6 | 9.32 | 11.18 | +986.5 | +289.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -55.0 | 0.00 | 0.00 | +714.0 | +356.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 8 | S_STRANGER | 61.5% | 37.5% | 37.5% | 25.0% | +210.4 | 2.58 | 4.30 | +574.2 | +416.2 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 61.5% | 37.5% | 37.5% | 25.0% | +210.4 | 2.58 | 4.30 | +574.2 | +416.2 |
| `feature_eurjpy_tdi50_reclaim` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 9.1% | +381.0 | 4.50 | 7.88 | +973.7 | +378.7 |

### STOP_HUNT|SELL|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=50.0% Avg=+166.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=37.5% Avg=+8.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | +56.2 | 1.29 | 2.07 | +769.6 | +386.3 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 27.3% | +11.9 | 1.05 | 1.84 | +793.6 | +437.8 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 27.3% | +11.9 | 1.05 | 1.84 | +793.6 | +437.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | +56.2 | 1.29 | 2.07 | +769.6 | +386.3 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | +56.2 | 1.29 | 2.07 | +769.6 | +386.3 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | +56.2 | 1.29 | 2.07 | +769.6 | +386.3 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | +56.2 | 1.29 | 2.07 | +769.6 | +386.3 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -145.0 | 0.00 | 0.00 | +46.5 | +339.5 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 27.3% | +11.9 | 1.05 | 1.84 | +793.6 | +437.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 27.3% | +11.9 | 1.05 | 1.84 | +793.6 | +437.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 23.1% | +56.2 | 1.29 | 2.07 | +769.6 | +386.3 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 92.3% | 41.7% | 41.7% | 25.0% | +61.0 | 1.29 | 1.81 | +833.7 | +400.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -145.0 | 0.00 | 0.00 | +46.5 | +339.5 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=50.0% Avg=+384.9; validation N=1 Fav=0.0% Avg=-412.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 46.2% | -45.9 | 0.81 | 1.13 | +401.7 | +498.5 |
| `hunt_to_ar_ratio_le_2_0` | 3 | R_REPEATER | 23.1% | 66.7% | 66.7% | 66.7% | +392.3 | 2.73 | 1.37 | +1016.7 | +597.7 |
| `hunt_to_ar_ratio_le_2_5` | 3 | R_REPEATER | 23.1% | 66.7% | 66.7% | 66.7% | +392.3 | 2.73 | 1.37 | +1016.7 | +597.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 46.2% | -45.9 | 0.81 | 1.13 | +401.7 | +498.5 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 46.2% | -45.9 | 0.81 | 1.13 | +401.7 | +498.5 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 46.2% | -45.9 | 0.81 | 1.13 | +401.7 | +498.5 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 38.5% | 40.0% | 40.0% | 60.0% | +225.5 | 3.47 | 3.47 | +457.8 | +372.4 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 76.9% | 40.0% | 40.0% | 50.0% | +28.1 | 1.17 | 1.46 | +367.5 | +317.6 |
| `ratio_le_2_and_asian_gte_30` | 3 | R_REPEATER | 23.1% | 66.7% | 66.7% | 66.7% | +392.3 | 2.73 | 1.37 | +1016.7 | +597.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 100.0% | +1281.0 | 999.00 | 999.00 | +1424.0 | +0.0 |
| `feature_fresh_reclaim_within_8` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 50.0% | +607.0 | 19.12 | 19.12 | +851.0 | +57.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 46.2% | -45.9 | 0.81 | 1.13 | +401.7 | +498.5 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 46.2% | -45.9 | 0.81 | 1.13 | +401.7 | +498.5 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 76.9% | 40.0% | 40.0% | 50.0% | +28.1 | 1.17 | 1.46 | +367.5 | +317.6 |

### STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=45.5% Avg=+6.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 7.7% | -46.0 | 0.76 | 1.22 | +288.3 | +316.7 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 8.3% | -78.7 | 0.63 | 1.25 | +264.2 | +335.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 8.3% | -78.7 | 0.63 | 1.25 | +264.2 | +335.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 7.7% | -46.0 | 0.76 | 1.22 | +288.3 | +316.7 |
| `confluence_gte_60` | 11 | S_STRANGER | 84.6% | 45.5% | 45.5% | 9.1% | +6.6 | 1.04 | 1.25 | +336.9 | +311.1 |
| `confluence_gte_70` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 0.0% | -36.5 | 0.84 | 0.84 | +352.5 | +267.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 69.2% | 33.3% | 33.3% | 11.1% | -62.8 | 0.69 | 1.37 | +299.9 | +319.8 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 33.3% | -40.7 | 0.80 | 1.61 | +244.0 | +74.7 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 92.3% | 33.3% | 33.3% | 8.3% | -78.7 | 0.63 | 1.25 | +264.2 | +335.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 61.5% | 25.0% | 25.0% | 12.5% | -113.9 | 0.50 | 1.49 | +265.2 | +348.9 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -460.0 | 0.00 | 0.00 | +97.0 | +30.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 7.7% | -46.0 | 0.76 | 1.22 | +288.3 | +316.7 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 92.3% | 41.7% | 41.7% | 8.3% | -11.5 | 0.93 | 1.31 | +304.2 | +340.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 33.3% | -40.7 | 0.80 | 1.61 | +244.0 | +74.7 |

### STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=50.0% Avg=+23.0; validation N=5 Fav=40.0% Avg=+105.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | -81.4 | 0.65 | 1.04 | +378.9 | +494.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 61.5% | 37.5% | 37.5% | 37.5% | -20.6 | 0.88 | 1.47 | +379.1 | +435.1 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 69.2% | 44.4% | 44.4% | 44.4% | -1.1 | 0.99 | 1.24 | +368.0 | +400.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | -81.4 | 0.65 | 1.04 | +378.9 | +494.0 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | -81.4 | 0.65 | 1.04 | +378.9 | +494.0 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | -81.4 | 0.65 | 1.04 | +378.9 | +494.0 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 92.3% | 41.7% | 41.7% | 41.7% | -26.5 | 0.86 | 1.20 | +410.3 | +466.6 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 69.2% | 33.3% | 33.3% | 33.3% | -30.7 | 0.82 | 1.64 | +374.0 | +364.2 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 61.5% | 37.5% | 37.5% | 37.5% | -20.6 | 0.88 | 1.47 | +379.1 | +435.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 53.8% | 42.9% | 42.9% | 42.9% | +82.1 | 1.83 | 2.45 | +432.9 | +379.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | -81.4 | 0.65 | 1.04 | +378.9 | +494.0 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | -81.4 | 0.65 | 1.04 | +378.9 | +494.0 |
| `feature_eurjpy_tdi50_reclaim` | 9 | S_STRANGER | 69.2% | 33.3% | 33.3% | 33.3% | -30.7 | 0.82 | 1.64 | +374.0 | +364.2 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=-232.6; validation N=4 Fav=75.0% Avg=+1230.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 12.5% | +341.8 | 3.81 | 5.71 | +863.9 | +399.9 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 93.8% | 33.3% | 33.3% | 6.7% | +271.5 | 3.09 | 5.56 | +804.8 | +419.3 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 12.5% | +341.8 | 3.81 | 5.71 | +863.9 | +399.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 12.5% | +341.8 | 3.81 | 5.71 | +863.9 | +399.9 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 12.5% | +341.8 | 3.81 | 5.71 | +863.9 | +399.9 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 12.5% | +341.8 | 3.81 | 5.71 | +863.9 | +399.9 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 93.8% | 40.0% | 40.0% | 13.3% | +431.9 | 7.91 | 10.55 | +880.5 | +411.1 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 93.8% | 40.0% | 40.0% | 13.3% | +431.9 | 7.91 | 10.55 | +880.5 | +411.1 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 93.8% | 33.3% | 33.3% | 6.7% | +271.5 | 3.09 | 5.56 | +804.8 | +419.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 87.5% | 35.7% | 35.7% | 7.1% | +363.1 | 6.43 | 10.28 | +818.4 | +432.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 12.5% | +341.8 | 3.81 | 5.71 | +863.9 | +399.9 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 56.2% | 44.4% | 44.4% | 11.1% | +417.7 | 3.24 | 4.05 | +853.2 | +410.3 |
| `feature_eurjpy_tdi50_reclaim` | 15 | S_STRANGER | 93.8% | 40.0% | 40.0% | 13.3% | +431.9 | 7.91 | 10.55 | +880.5 | +411.1 |

### STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=55.6% Avg=+175.9; out_of_sample N=2 Fav=50.0% Avg=+1618.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 12.5% | -451.2 | 0.53 | 0.88 | +973.4 | +407.8 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 81.2% | 46.2% | 46.2% | 15.4% | +372.9 | 2.54 | 2.97 | +1049.2 | +251.3 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 81.2% | 46.2% | 46.2% | 15.4% | +372.9 | 2.54 | 2.97 | +1049.2 | +251.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 12.5% | -451.2 | 0.53 | 0.88 | +973.4 | +407.8 |
| `confluence_gte_60` | 9 | S_STRANGER | 56.2% | 44.4% | 44.4% | 0.0% | -43.2 | 0.88 | 1.10 | +824.4 | +590.3 |
| `confluence_gte_70` | 3 | S_STRANGER | 18.8% | 33.3% | 33.3% | 0.0% | -792.3 | 0.07 | 0.13 | +941.3 | +1320.0 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 43.8% | 28.6% | 28.6% | 0.0% | -834.4 | 0.25 | 0.63 | +591.0 | +128.4 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 37.5% | 0.0% | 0.0% | 0.0% | -2027.3 | 0.00 | 0.00 | +230.0 | +187.7 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 81.2% | 46.2% | 46.2% | 15.4% | +372.9 | 2.54 | 2.97 | +1049.2 | +251.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 37.5% | 33.3% | 33.3% | 0.0% | -68.7 | 0.83 | 1.65 | +529.0 | +126.3 |
| `feature_fresh_reclaim_within_8` | 6 | S_STRANGER | 37.5% | 0.0% | 0.0% | 0.0% | -2027.3 | 0.00 | 0.00 | +230.0 | +187.7 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 37.5% | 37.5% | 12.5% | -451.2 | 0.53 | 0.88 | +973.4 | +407.8 |
| `feature_momentum_breakout_exception` | 11 | R_REPEATER | 68.8% | 54.5% | 54.5% | 18.2% | +438.1 | 2.52 | 2.10 | +1305.5 | +507.2 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 37.5% | 0.0% | 0.0% | 0.0% | -2027.3 | 0.00 | 0.00 | +230.0 | +187.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=60.0% Avg=+346.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 36.8% | 47.4% | 36.8% | +123.2 | 3.47 | 3.86 | +302.8 | +147.2 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 78.9% | 26.7% | 40.0% | 40.0% | +79.4 | 2.41 | 3.61 | +254.4 | +145.7 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 94.7% | 33.3% | 44.4% | 38.9% | +125.9 | 3.40 | 4.24 | +309.6 | +144.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 19 | S_STRANGER | 100.0% | 36.8% | 47.4% | 36.8% | +123.2 | 3.47 | 3.86 | +302.8 | +147.2 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 36.8% | 47.4% | 36.8% | +123.2 | 3.47 | 3.86 | +302.8 | +147.2 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 36.8% | 47.4% | 36.8% | +123.2 | 3.47 | 3.86 | +302.8 | +147.2 |
| `tdi_rsi_gt_signal` | 5 | R_REPEATER | 26.3% | 60.0% | 60.0% | 40.0% | +346.6 | 16.90 | 11.27 | +485.4 | +181.8 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 68.4% | 30.8% | 38.5% | 38.5% | +85.8 | 2.63 | 4.20 | +295.8 | +158.0 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 78.9% | 26.7% | 40.0% | 40.0% | +79.4 | 2.41 | 3.61 | +254.4 | +145.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 15.8% | 33.3% | 33.3% | 33.3% | +186.0 | 6.12 | 12.24 | +349.0 | +213.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 94.7% | 38.9% | 50.0% | 38.9% | +131.2 | 3.55 | 3.55 | +305.1 | +149.8 |
| `feature_momentum_breakout_exception` | 16 | S_STRANGER | 84.2% | 37.5% | 50.0% | 37.5% | +87.6 | 2.62 | 2.62 | +272.9 | +154.9 |
| `feature_eurjpy_tdi50_reclaim` | 13 | S_STRANGER | 68.4% | 30.8% | 38.5% | 38.5% | +85.8 | 2.63 | 4.20 | +295.8 | +158.0 |

### STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=66.7% Avg=+402.1; out_of_sample N=2 Fav=0.0% Avg=+3081.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 45.5% | +695.5 | 4.64 | 4.64 | +1188.5 | +424.7 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 45.5% | +695.5 | 4.64 | 4.64 | +1188.5 | +424.7 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 45.5% | +695.5 | 4.64 | 4.64 | +1188.5 | +424.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 45.5% | +695.5 | 4.64 | 4.64 | +1188.5 | +424.7 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 45.5% | +695.5 | 4.64 | 4.64 | +1188.5 | +424.7 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 45.5% | +695.5 | 4.64 | 4.64 | +1188.5 | +424.7 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 72.7% | 50.0% | 62.5% | 62.5% | +1071.8 | 8.27 | 3.31 | +1518.5 | +354.4 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 72.7% | 37.5% | 50.0% | 37.5% | +870.3 | 5.14 | 5.14 | +1251.7 | +426.5 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 45.5% | +695.5 | 4.64 | 4.64 | +1188.5 | +424.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 72.7% | 50.0% | 62.5% | 62.5% | +1071.8 | 8.27 | 3.31 | +1518.5 | +354.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 45.5% | +695.5 | 4.64 | 4.64 | +1188.5 | +424.7 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 45.5% | +695.5 | 4.64 | 4.64 | +1188.5 | +424.7 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 72.7% | 37.5% | 50.0% | 37.5% | +870.3 | 5.14 | 5.14 | +1251.7 | +426.5 |

### STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=33.3% Avg=+91.2; validation N=2 Fav=50.0% Avg=+137.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +99.6 | 1.45 | 2.53 | +743.6 | +420.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 12.5% | +7.0 | 1.03 | 3.09 | +732.1 | +403.4 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 12.5% | +7.0 | 1.03 | 3.09 | +732.1 | +403.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +99.6 | 1.45 | 2.53 | +743.6 | +420.0 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +99.6 | 1.45 | 2.53 | +743.6 | +420.0 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +99.6 | 1.45 | 2.53 | +743.6 | +420.0 |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 0.0% | +1591.0 | 999.00 | 999.00 | +1879.0 | +474.0 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | -460.3 | 0.06 | 0.12 | +351.7 | +757.7 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 12.5% | +7.0 | 1.03 | 3.09 | +732.1 | +403.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -1316.0 | 0.00 | 0.00 | +568.0 | +1561.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +99.6 | 1.45 | 2.53 | +743.6 | +420.0 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +99.6 | 1.45 | 2.53 | +743.6 | +420.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | -460.3 | 0.06 | 0.12 | +351.7 | +757.7 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+134.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +36.5 | 1.31 | 2.30 | +271.9 | +195.9 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +36.5 | 1.31 | 2.30 | +271.9 | +195.9 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +36.5 | 1.31 | 2.30 | +271.9 | +195.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +36.5 | 1.31 | 2.30 | +271.9 | +195.9 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +36.5 | 1.31 | 2.30 | +271.9 | +195.9 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +36.5 | 1.31 | 2.30 | +271.9 | +195.9 |
| `tdi_rsi_gt_signal` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 16.7% | +134.5 | 3.76 | 3.76 | +297.5 | +152.5 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 20.0% | +21.8 | 1.17 | 1.76 | +282.4 | +245.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +36.5 | 1.31 | 2.30 | +271.9 | +195.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | R_REPEATER | 54.5% | 50.0% | 50.0% | 16.7% | +134.5 | 3.76 | 3.76 | +297.5 | +152.5 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -41.0 | 0.00 | 0.00 | +29.0 | +87.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 18.2% | +36.5 | 1.31 | 2.30 | +271.9 | +195.9 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 81.8% | 44.4% | 44.4% | 22.2% | +62.1 | 1.50 | 1.87 | +323.6 | +209.4 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 20.0% | +21.8 | 1.17 | 1.76 | +282.4 | +245.4 |

### THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+8.7; validation N=5 Fav=40.0% Avg=+104.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | +25.0 | 1.29 | 1.93 | +234.9 | +187.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 37.5% | +21.4 | 1.21 | 1.61 | +275.1 | +221.5 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 33.3% | +8.0 | 1.08 | 1.80 | +252.9 | +208.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | +25.0 | 1.29 | 1.93 | +234.9 | +187.0 |
| `confluence_gte_60` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 0.0% | -88.3 | 0.23 | 0.45 | +179.3 | +142.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 16.7% | -22.2 | 0.71 | 1.43 | +160.8 | +178.2 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | -72.1 | 0.42 | 1.67 | +88.2 | +137.2 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 37.5% | +21.4 | 1.21 | 1.61 | +275.1 | +221.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 0.0% | -79.3 | 0.24 | 0.49 | +194.0 | +261.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | +25.0 | 1.29 | 1.93 | +234.9 | +187.0 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 90.9% | 40.0% | 40.0% | 40.0% | +56.3 | 1.83 | 2.29 | +255.3 | +199.1 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | -72.1 | 0.42 | 1.67 | +88.2 | +137.2 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-336.0; validation N=9 Fav=44.4% Avg=+74.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | -4.2 | 0.98 | 1.46 | +329.3 | +381.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 40.0% | 40.0% | 40.0% | +33.1 | 1.22 | 1.53 | +349.5 | +320.2 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 90.9% | 40.0% | 40.0% | 40.0% | +33.1 | 1.22 | 1.53 | +349.5 | +320.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | -4.2 | 0.98 | 1.46 | +329.3 | +381.3 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | -4.2 | 0.98 | 1.46 | +329.3 | +381.3 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | -4.2 | 0.98 | 1.46 | +329.3 | +381.3 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 33.3% | -52.6 | 0.72 | 1.20 | +262.3 | +395.6 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -6.2 | 0.97 | 2.92 | +427.5 | +510.2 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 90.9% | 40.0% | 40.0% | 40.0% | +33.1 | 1.22 | 1.53 | +349.5 | +320.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 72.7% | 37.5% | 37.5% | 37.5% | -12.0 | 0.93 | 1.24 | +279.3 | +321.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | -4.2 | 0.98 | 1.46 | +329.3 | +381.3 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 100.0% | 36.4% | 36.4% | 36.4% | -4.2 | 0.98 | 1.46 | +329.3 | +381.3 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 0.0% | -6.2 | 0.97 | 2.92 | +427.5 | +510.2 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-132.0; validation N=9 Fav=44.4% Avg=-17.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 36.4% | -29.1 | 0.89 | 0.89 | +389.8 | +175.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 40.0% | 50.0% | 40.0% | -28.7 | 0.90 | 0.72 | +426.5 | +171.3 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 36.4% | -29.1 | 0.89 | 0.89 | +389.8 | +175.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 36.4% | -29.1 | 0.89 | 0.89 | +389.8 | +175.8 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 36.4% | -29.1 | 0.89 | 0.89 | +389.8 | +175.8 |
| `confluence_gte_70` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 0.0% | +290.5 | 5.84 | 5.84 | +508.0 | +179.5 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 25.0% | +56.5 | 1.18 | 1.18 | +561.0 | +138.7 |
| `tdi_rsi_gte_50` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 25.0% | +220.3 | 6.34 | 6.34 | +395.5 | +169.5 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 90.9% | 40.0% | 50.0% | 40.0% | -28.7 | 0.90 | 0.72 | +426.5 | +171.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | R_REPEATER | 27.3% | 66.7% | 66.7% | 33.3% | +86.3 | 1.21 | 0.61 | +740.3 | +111.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 36.4% | -29.1 | 0.89 | 0.89 | +389.8 | +175.8 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 100.0% | 36.4% | 45.5% | 36.4% | -29.1 | 0.89 | 0.89 | +389.8 | +175.8 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 25.0% | +220.3 | 6.34 | 6.34 | +395.5 | +169.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=11 Fav=54.5% Avg=+232.0; validation N=5 Fav=20.0% Avg=-159.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 47 | S_STRANGER | 100.0% | 36.2% | 40.4% | 31.9% | +68.2 | 1.61 | 2.03 | +336.4 | +256.6 |
| `hunt_to_ar_ratio_le_2_0` | 42 | S_STRANGER | 89.4% | 35.7% | 40.5% | 26.2% | +57.1 | 1.47 | 1.99 | +342.0 | +271.0 |
| `hunt_to_ar_ratio_le_2_5` | 45 | S_STRANGER | 95.7% | 37.8% | 42.2% | 31.1% | +75.7 | 1.67 | 2.03 | +349.0 | +258.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 47 | S_STRANGER | 100.0% | 36.2% | 40.4% | 31.9% | +68.2 | 1.61 | 2.03 | +336.4 | +256.6 |
| `confluence_gte_60` | 47 | S_STRANGER | 100.0% | 36.2% | 40.4% | 31.9% | +68.2 | 1.61 | 2.03 | +336.4 | +256.6 |
| `confluence_gte_70` | 47 | S_STRANGER | 100.0% | 36.2% | 40.4% | 31.9% | +68.2 | 1.61 | 2.03 | +336.4 | +256.6 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 34.0% | 43.8% | 50.0% | 37.5% | +109.8 | 1.80 | 1.58 | +423.7 | +277.6 |
| `tdi_rsi_gte_50` | 33 | S_STRANGER | 70.2% | 36.4% | 39.4% | 30.3% | +72.8 | 1.59 | 2.08 | +374.5 | +301.7 |
| `ratio_le_2_and_asian_gte_30` | 42 | S_STRANGER | 89.4% | 35.7% | 40.5% | 26.2% | +57.1 | 1.47 | 1.99 | +342.0 | +271.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 29.8% | 42.9% | 50.0% | 35.7% | +75.5 | 1.53 | 1.31 | +406.3 | +279.7 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 2.1% | 100.0% | 100.0% | 100.0% | +1021.0 | 999.00 | 999.00 | +1588.0 | +62.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 45 | S_STRANGER | 95.7% | 35.6% | 40.0% | 33.3% | +67.4 | 1.58 | 2.01 | +337.4 | +247.8 |
| `feature_momentum_breakout_exception` | 43 | S_STRANGER | 91.5% | 32.6% | 37.2% | 34.9% | +41.3 | 1.34 | 1.93 | +318.9 | +252.4 |
| `feature_eurjpy_tdi50_reclaim` | 33 | S_STRANGER | 70.2% | 36.4% | 39.4% | 30.3% | +72.8 | 1.59 | 2.08 | +374.5 | +301.7 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=50.0% Avg=-27.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 28.6% | -144.5 | 0.26 | 0.35 | +185.2 | +226.1 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 85.7% | 33.3% | 33.3% | 25.0% | -188.0 | 0.18 | 0.36 | +178.0 | +237.3 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 28.6% | -144.5 | 0.26 | 0.35 | +185.2 | +226.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 28.6% | -144.5 | 0.26 | 0.35 | +185.2 | +226.1 |
| `confluence_gte_60` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 14.3% | -233.1 | 0.09 | 0.52 | +137.7 | +238.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 0.0% | -382.3 | 0.00 | 0.00 | +81.2 | +379.3 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 92.9% | 38.5% | 46.2% | 30.8% | -141.2 | 0.28 | 0.33 | +192.8 | +222.8 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 85.7% | 33.3% | 33.3% | 25.0% | -188.0 | 0.18 | 0.36 | +178.0 | +237.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 0.0% | -382.3 | 0.00 | 0.00 | +81.2 | +379.3 |
| `feature_fresh_reclaim_within_8` | 5 | S_STRANGER | 35.7% | 0.0% | 20.0% | 0.0% | -320.8 | 0.08 | 0.32 | +114.6 | +252.2 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 28.6% | -144.5 | 0.26 | 0.35 | +185.2 | +226.1 |
| `feature_momentum_breakout_exception` | 10 | R_REPEATER | 71.4% | 50.0% | 60.0% | 40.0% | -27.9 | 0.72 | 0.48 | +217.4 | +217.6 |
| `feature_eurjpy_tdi50_reclaim` | 13 | S_STRANGER | 92.9% | 38.5% | 46.2% | 30.8% | -141.2 | 0.28 | 0.33 | +192.8 | +222.8 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=71.4% Avg=+125.9; out_of_sample N=3 Fav=0.0% Avg=-390.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 14.3% | -580.6 | 0.27 | 0.36 | +707.0 | +318.1 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 78.6% | 36.4% | 45.5% | 9.1% | -405.6 | 0.35 | 0.42 | +802.2 | +319.8 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 78.6% | 36.4% | 45.5% | 9.1% | -405.6 | 0.35 | 0.42 | +802.2 | +319.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 14.3% | -580.6 | 0.27 | 0.36 | +707.0 | +318.1 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 14.3% | -580.6 | 0.27 | 0.36 | +707.0 | +318.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 78.6% | 27.3% | 27.3% | 9.1% | -924.7 | 0.09 | 0.23 | +490.2 | +355.1 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 71.4% | 20.0% | 30.0% | 20.0% | -820.8 | 0.19 | 0.45 | +451.3 | +286.3 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 78.6% | 36.4% | 45.5% | 9.1% | -405.6 | 0.35 | 0.42 | +802.2 | +319.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 64.3% | 33.3% | 33.3% | 11.1% | -659.1 | 0.14 | 0.28 | +563.1 | +371.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 35.7% | 42.9% | 14.3% | -580.6 | 0.27 | 0.36 | +707.0 | +318.1 |
| `feature_momentum_breakout_exception` | 10 | R_REPEATER | 71.4% | 50.0% | 50.0% | 20.0% | -29.1 | 0.88 | 0.88 | +753.7 | +383.0 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 71.4% | 20.0% | 30.0% | 20.0% | -820.8 | 0.19 | 0.45 | +451.3 | +286.3 |

### STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=57.1% Avg=+319.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 41.2% | +95.6 | 1.40 | 1.60 | +666.4 | +484.8 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 41.2% | +95.6 | 1.40 | 1.60 | +666.4 | +484.8 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 41.2% | +95.6 | 1.40 | 1.60 | +666.4 | +484.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 41.2% | +95.6 | 1.40 | 1.60 | +666.4 | +484.8 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 41.2% | +95.6 | 1.40 | 1.60 | +666.4 | +484.8 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 41.2% | +95.6 | 1.40 | 1.60 | +666.4 | +484.8 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 29.4% | 40.0% | 40.0% | 20.0% | +355.2 | 2.42 | 3.63 | +1057.4 | +567.8 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 41.2% | 57.1% | 57.1% | 42.9% | +319.0 | 3.88 | 2.91 | +741.7 | +330.4 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 41.2% | +95.6 | 1.40 | 1.60 | +666.4 | +484.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 29.4% | 40.0% | 40.0% | 20.0% | +355.2 | 2.42 | 3.63 | +1057.4 | +567.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 41.2% | +95.6 | 1.40 | 1.60 | +666.4 | +484.8 |
| `feature_momentum_breakout_exception` | 16 | S_STRANGER | 94.1% | 37.5% | 43.8% | 43.8% | +108.3 | 1.44 | 1.44 | +651.4 | +507.6 |
| `feature_eurjpy_tdi50_reclaim` | 7 | R_REPEATER | 41.2% | 57.1% | 57.1% | 42.9% | +319.0 | 3.88 | 2.91 | +741.7 | +330.4 |

### STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=60.0% Avg=+135.7; validation N=2 Fav=0.0% Avg=-194.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 35.3% | +51.3 | 1.49 | 1.70 | +342.5 | +250.8 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 64.7% | 27.3% | 36.4% | 27.3% | +11.7 | 1.08 | 1.62 | +301.3 | +279.1 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 70.6% | 25.0% | 33.3% | 33.3% | +10.7 | 1.08 | 1.62 | +284.1 | +260.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 35.3% | +51.3 | 1.49 | 1.70 | +342.5 | +250.8 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 35.3% | +51.3 | 1.49 | 1.70 | +342.5 | +250.8 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 35.3% | +51.3 | 1.49 | 1.70 | +342.5 | +250.8 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 64.7% | 36.4% | 45.5% | 36.4% | +64.9 | 2.44 | 1.95 | +248.7 | +164.1 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 41.2% | 42.9% | 57.1% | 42.9% | +41.4 | 1.65 | 1.24 | +266.7 | +177.9 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 64.7% | 27.3% | 36.4% | 27.3% | +11.7 | 1.08 | 1.62 | +301.3 | +279.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 41.2% | 28.6% | 42.9% | 28.6% | +12.8 | 1.20 | 1.20 | +194.3 | +161.6 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -154.0 | 0.00 | 0.00 | +38.0 | +172.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 35.3% | +51.3 | 1.49 | 1.70 | +342.5 | +250.8 |
| `feature_momentum_breakout_exception` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 35.3% | +51.3 | 1.49 | 1.70 | +342.5 | +250.8 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 41.2% | 42.9% | 57.1% | 42.9% | +41.4 | 1.65 | 1.24 | +266.7 | +177.9 |

### THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=55.6% Avg=+106.1; validation N=3 Fav=0.0% Avg=-308.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 23.5% | +15.0 | 1.10 | 1.41 | +368.9 | +320.2 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 88.2% | 33.3% | 40.0% | 26.7% | +23.7 | 1.15 | 1.54 | +366.3 | +319.5 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 94.1% | 31.2% | 37.5% | 25.0% | +0.8 | 1.00 | 1.51 | +373.5 | +336.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 23.5% | +15.0 | 1.10 | 1.41 | +368.9 | +320.2 |
| `confluence_gte_60` | 12 | S_STRANGER | 70.6% | 41.7% | 50.0% | 16.7% | +2.6 | 1.02 | 1.02 | +347.9 | +300.8 |
| `confluence_gte_70` | 4 | R_REPEATER | 23.5% | 50.0% | 50.0% | 25.0% | +99.2 | 1.70 | 1.70 | +372.3 | +326.3 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 58.8% | 40.0% | 40.0% | 20.0% | -50.8 | 0.71 | 1.06 | +269.3 | +325.4 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 29.4% | 0.0% | 0.0% | 0.0% | -314.4 | 0.00 | 0.00 | +67.2 | +484.2 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 88.2% | 33.3% | 40.0% | 26.7% | +23.7 | 1.15 | 1.54 | +366.3 | +319.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 47.1% | 37.5% | 37.5% | 25.0% | -50.9 | 0.71 | 1.18 | +239.5 | +325.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 35.3% | 41.2% | 23.5% | +15.0 | 1.10 | 1.41 | +368.9 | +320.2 |
| `feature_momentum_breakout_exception` | 16 | S_STRANGER | 94.1% | 37.5% | 37.5% | 25.0% | +13.6 | 1.08 | 1.62 | +387.9 | +331.8 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 23.5% | 0.0% | 0.0% | 0.0% | -354.0 | 0.00 | 0.00 | +60.0 | +527.2 |

### STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+129.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 34.6% | 38.5% | 26.9% | +52.7 | 1.62 | 2.59 | +321.2 | +198.4 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 80.8% | 38.1% | 38.1% | 28.6% | +59.6 | 1.64 | 2.66 | +338.2 | +201.6 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 80.8% | 38.1% | 38.1% | 28.6% | +59.6 | 1.64 | 2.66 | +338.2 | +201.6 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 26 | S_STRANGER | 100.0% | 34.6% | 38.5% | 26.9% | +52.7 | 1.62 | 2.59 | +321.2 | +198.4 |
| `confluence_gte_60` | 26 | S_STRANGER | 100.0% | 34.6% | 38.5% | 26.9% | +52.7 | 1.62 | 2.59 | +321.2 | +198.4 |
| `confluence_gte_70` | 26 | S_STRANGER | 100.0% | 34.6% | 38.5% | 26.9% | +52.7 | 1.62 | 2.59 | +321.2 | +198.4 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 46.2% | 33.3% | 33.3% | 16.7% | +39.9 | 1.39 | 2.78 | +308.8 | +226.7 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 23.1% | 50.0% | 50.0% | 33.3% | +129.5 | 3.06 | 3.06 | +422.5 | +197.5 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 80.8% | 38.1% | 38.1% | 28.6% | +59.6 | 1.64 | 2.66 | +338.2 | +201.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 38.5% | 30.0% | 30.0% | 20.0% | +28.7 | 1.26 | 2.94 | +322.1 | +233.5 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 3.8% | 100.0% | 100.0% | 100.0% | +338.0 | 999.00 | 999.00 | +500.0 | +12.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 34.6% | 38.5% | 26.9% | +52.7 | 1.62 | 2.59 | +321.2 | +198.4 |
| `feature_momentum_breakout_exception` | 25 | S_STRANGER | 96.2% | 36.0% | 40.0% | 28.0% | +56.5 | 1.65 | 2.48 | +332.6 | +186.1 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 23.1% | 50.0% | 50.0% | 33.3% | +129.5 | 3.06 | 3.06 | +422.5 | +197.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=66.7% Avg=+667.0; validation N=5 Fav=60.0% Avg=+320.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 41 | S_STRANGER | 100.0% | 34.1% | 41.5% | 31.7% | +82.9 | 1.55 | 1.73 | +454.0 | +327.4 |
| `hunt_to_ar_ratio_le_2_0` | 35 | S_STRANGER | 85.4% | 37.1% | 45.7% | 31.4% | +111.3 | 1.71 | 1.60 | +512.3 | +355.5 |
| `hunt_to_ar_ratio_le_2_5` | 37 | S_STRANGER | 90.2% | 35.1% | 43.2% | 32.4% | +96.4 | 1.61 | 1.61 | +490.8 | +349.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 41 | S_STRANGER | 100.0% | 34.1% | 41.5% | 31.7% | +82.9 | 1.55 | 1.73 | +454.0 | +327.4 |
| `confluence_gte_60` | 41 | S_STRANGER | 100.0% | 34.1% | 41.5% | 31.7% | +82.9 | 1.55 | 1.73 | +454.0 | +327.4 |
| `confluence_gte_70` | 41 | S_STRANGER | 100.0% | 34.1% | 41.5% | 31.7% | +82.9 | 1.55 | 1.73 | +454.0 | +327.4 |
| `tdi_rsi_gt_signal` | 9 | R_REPEATER | 22.0% | 55.6% | 55.6% | 22.2% | +379.8 | 9.68 | 5.81 | +725.9 | +273.2 |
| `tdi_rsi_gte_50` | 38 | S_STRANGER | 92.7% | 36.8% | 42.1% | 31.6% | +87.6 | 1.55 | 1.74 | +477.0 | +344.1 |
| `ratio_le_2_and_asian_gte_30` | 35 | S_STRANGER | 85.4% | 37.1% | 45.7% | 31.4% | +111.3 | 1.71 | 1.60 | +512.3 | +355.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 19.5% | 62.5% | 62.5% | 25.0% | +450.6 | 18.42 | 7.37 | +810.0 | +283.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 90.2% | 35.1% | 43.2% | 35.1% | +139.1 | 2.45 | 2.45 | +444.4 | +278.0 |
| `feature_momentum_breakout_exception` | 32 | S_STRANGER | 78.0% | 28.1% | 37.5% | 37.5% | +97.3 | 1.93 | 2.41 | +373.0 | +266.5 |
| `feature_eurjpy_tdi50_reclaim` | 38 | S_STRANGER | 92.7% | 36.8% | 42.1% | 31.6% | +87.6 | 1.55 | 1.74 | +477.0 | +344.1 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=20.0% Avg=-425.4; out_of_sample N=5 Fav=60.0% Avg=+1382.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | +258.0 | 1.63 | 3.25 | +1336.7 | +717.9 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | +258.0 | 1.63 | 3.25 | +1336.7 | +717.9 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | +258.0 | 1.63 | 3.25 | +1336.7 | +717.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | +258.0 | 1.63 | 3.25 | +1336.7 | +717.9 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | +258.0 | 1.63 | 3.25 | +1336.7 | +717.9 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | +258.0 | 1.63 | 3.25 | +1336.7 | +717.9 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -682.0 | 0.00 | 0.00 | +424.5 | +1301.5 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 86.7% | 30.8% | 30.8% | 7.7% | +334.7 | 1.82 | 4.10 | +1428.0 | +771.7 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | +258.0 | 1.63 | 3.25 | +1336.7 | +717.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -682.0 | 0.00 | 0.00 | +424.5 | +1301.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | +258.0 | 1.63 | 3.25 | +1336.7 | +717.9 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 66.7% | 40.0% | 40.0% | 20.0% | +478.3 | 2.62 | 3.94 | +1347.0 | +556.5 |
| `feature_eurjpy_tdi50_reclaim` | 13 | S_STRANGER | 86.7% | 30.8% | 30.8% | 7.7% | +334.7 | 1.82 | 4.10 | +1428.0 | +771.7 |

### THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+257.5; validation N=8 Fav=37.5% Avg=+158.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 50.0% | 33.3% | +137.9 | 1.66 | 1.38 | +574.7 | +295.1 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 33.3% | 50.0% | 33.3% | +137.9 | 1.66 | 1.38 | +574.7 | +295.1 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 33.3% | 50.0% | 33.3% | +137.9 | 1.66 | 1.38 | +574.7 | +295.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 33.3% | 50.0% | 33.3% | +137.9 | 1.66 | 1.38 | +574.7 | +295.1 |
| `confluence_gte_60` | 10 | S_STRANGER | 83.3% | 40.0% | 60.0% | 30.0% | +178.6 | 1.75 | 1.17 | +662.9 | +316.5 |
| `confluence_gte_70` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -818.0 | 0.00 | 0.00 | +681.0 | +822.0 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 91.7% | 27.3% | 45.5% | 36.4% | +103.2 | 1.45 | 1.45 | +555.9 | +320.8 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 41.7% | 20.0% | 60.0% | 40.0% | +339.8 | 6.52 | 2.17 | +511.4 | +120.6 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 33.3% | 50.0% | 33.3% | +137.9 | 1.66 | 1.38 | +574.7 | +295.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 91.7% | 27.3% | 45.5% | 36.4% | +103.2 | 1.45 | 1.45 | +555.9 | +320.8 |
| `feature_fresh_reclaim_within_8` | 2 | R_REPEATER | 16.7% | 50.0% | 100.0% | 50.0% | +987.5 | 999.00 | 999.00 | +1126.5 | +15.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 50.0% | 33.3% | +137.9 | 1.66 | 1.38 | +574.7 | +295.1 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 83.3% | 40.0% | 50.0% | 40.0% | +156.4 | 1.71 | 1.37 | +639.9 | +317.5 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 41.7% | 20.0% | 60.0% | 40.0% | +339.8 | 6.52 | 2.17 | +511.4 | +120.6 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=38.5% Avg=+102.7; validation N=4 Fav=50.0% Avg=+281.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 33.3% | 52.4% | 28.6% | +115.0 | 2.54 | 2.31 | +385.0 | +188.6 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 90.5% | 36.8% | 52.6% | 31.6% | +132.4 | 2.73 | 2.45 | +417.5 | +181.2 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 95.2% | 35.0% | 50.0% | 30.0% | +120.1 | 2.53 | 2.53 | +398.7 | +182.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 21 | S_STRANGER | 100.0% | 33.3% | 52.4% | 28.6% | +115.0 | 2.54 | 2.31 | +385.0 | +188.6 |
| `confluence_gte_60` | 10 | S_STRANGER | 47.6% | 40.0% | 50.0% | 40.0% | +92.6 | 2.08 | 2.08 | +405.7 | +245.1 |
| `confluence_gte_70` | 1 | R_RUNNER | 4.8% | 100.0% | 100.0% | 100.0% | +444.0 | 999.00 | 999.00 | +621.0 | +111.0 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 90.5% | 36.8% | 52.6% | 31.6% | +124.2 | 2.68 | 2.41 | +407.4 | +188.1 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 57.1% | 33.3% | 33.3% | 25.0% | +129.9 | 2.42 | 4.84 | +441.5 | +234.9 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 90.5% | 36.8% | 52.6% | 31.6% | +132.4 | 2.73 | 2.45 | +417.5 | +181.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 81.0% | 41.2% | 52.9% | 35.3% | +144.7 | 2.90 | 2.58 | +446.5 | +179.7 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -73.0 | 0.00 | 0.00 | +864.0 | +691.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 33.3% | 52.4% | 28.6% | +115.0 | 2.54 | 2.31 | +385.0 | +188.6 |
| `feature_momentum_breakout_exception` | 19 | S_STRANGER | 90.5% | 31.6% | 52.6% | 26.3% | +65.9 | 1.84 | 1.65 | +302.9 | +166.2 |
| `feature_eurjpy_tdi50_reclaim` | 11 | S_STRANGER | 52.4% | 36.4% | 36.4% | 27.3% | +158.3 | 2.90 | 5.08 | +459.9 | +210.4 |

### THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-42.0; validation N=10 Fav=50.0% Avg=+291.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 27.8% | +76.3 | 1.29 | 1.85 | +748.8 | +482.4 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 94.4% | 35.3% | 41.2% | 23.5% | +80.8 | 1.29 | 1.85 | +745.6 | +489.6 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 27.8% | +76.3 | 1.29 | 1.85 | +748.8 | +482.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 27.8% | +76.3 | 1.29 | 1.85 | +748.8 | +482.4 |
| `confluence_gte_60` | 11 | S_STRANGER | 61.1% | 45.5% | 54.5% | 36.4% | +261.0 | 1.96 | 1.64 | +1042.5 | +441.6 |
| `confluence_gte_70` | 3 | R_REPEATER | 16.7% | 66.7% | 66.7% | 33.3% | +368.0 | 2.33 | 1.17 | +1267.0 | +690.3 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 55.6% | 20.0% | 30.0% | 30.0% | -113.0 | 0.65 | 1.31 | +604.3 | +542.0 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 66.7% | 16.7% | 25.0% | 25.0% | -166.3 | 0.52 | 1.38 | +524.2 | +587.8 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 94.4% | 35.3% | 41.2% | 23.5% | +80.8 | 1.29 | 1.85 | +745.6 | +489.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 50.0% | 22.2% | 33.3% | 22.2% | -125.6 | 0.65 | 1.31 | +582.2 | +562.2 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +803.0 | +360.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 27.8% | +76.3 | 1.29 | 1.85 | +748.8 | +482.4 |
| `feature_momentum_breakout_exception` | 17 | S_STRANGER | 94.4% | 35.3% | 35.3% | 29.4% | +60.3 | 1.22 | 2.03 | +766.1 | +501.6 |
| `feature_eurjpy_tdi50_reclaim` | 12 | S_STRANGER | 66.7% | 16.7% | 25.0% | 25.0% | -166.3 | 0.52 | 1.38 | +524.2 | +587.8 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+53.0; validation N=4 Fav=50.0% Avg=+155.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 33.3% | +27.9 | 1.19 | 1.66 | +333.5 | +235.1 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 30.0% | 40.0% | 30.0% | -14.0 | 0.92 | 1.38 | +295.1 | +241.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 27.3% | 36.4% | 27.3% | -18.2 | 0.89 | 1.56 | +278.9 | +234.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 33.3% | +27.9 | 1.19 | 1.66 | +333.5 | +235.1 |
| `confluence_gte_60` | 4 | S_STRANGER | 33.3% | 25.0% | 50.0% | 25.0% | -32.2 | 0.81 | 0.81 | +406.7 | +166.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 41.7% | 0.0% | 20.0% | 0.0% | -216.2 | 0.01 | 0.03 | +130.4 | +197.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 83.3% | 30.0% | 40.0% | 30.0% | +23.7 | 1.19 | 1.79 | +318.3 | +198.4 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 83.3% | 30.0% | 40.0% | 30.0% | -14.0 | 0.92 | 1.38 | +295.1 | +241.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 41.7% | 0.0% | 20.0% | 0.0% | -216.2 | 0.01 | 0.03 | +130.4 | +197.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 33.3% | +27.9 | 1.19 | 1.66 | +333.5 | +235.1 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 83.3% | 40.0% | 40.0% | 40.0% | +93.9 | 1.79 | 2.68 | +342.6 | +256.2 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 83.3% | 30.0% | 40.0% | 30.0% | +23.7 | 1.19 | 1.79 | +318.3 | +198.4 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=28.6% Avg=+35.9; validation N=6 Fav=50.0% Avg=-7.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +6.8 | 1.03 | 1.65 | +505.7 | +378.5 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +6.8 | 1.03 | 1.65 | +505.7 | +378.5 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +6.8 | 1.03 | 1.65 | +505.7 | +378.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +6.8 | 1.03 | 1.65 | +505.7 | +378.5 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +6.8 | 1.03 | 1.65 | +505.7 | +378.5 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +6.8 | 1.03 | 1.65 | +505.7 | +378.5 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -76.7 | 0.66 | 0.66 | +627.7 | +398.0 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 86.7% | 38.5% | 38.5% | 46.2% | +15.9 | 1.07 | 1.28 | +536.7 | +377.3 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +6.8 | 1.03 | 1.65 | +505.7 | +378.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -76.7 | 0.66 | 0.66 | +627.7 | +398.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 40.0% | +6.8 | 1.03 | 1.65 | +505.7 | +378.5 |
| `feature_momentum_breakout_exception` | 14 | S_STRANGER | 93.3% | 35.7% | 35.7% | 42.9% | +48.1 | 1.27 | 1.78 | +538.1 | +363.4 |
| `feature_eurjpy_tdi50_reclaim` | 13 | S_STRANGER | 86.7% | 38.5% | 38.5% | 46.2% | +15.9 | 1.07 | 1.28 | +536.7 | +377.3 |

### STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=37.5% Avg=-38.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | -33.8 | 0.72 | 1.44 | +263.1 | +236.5 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 53.3% | 37.5% | 37.5% | 12.5% | -38.0 | 0.74 | 1.23 | +290.7 | +254.1 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 73.3% | 36.4% | 36.4% | 9.1% | -42.3 | 0.68 | 1.19 | +297.9 | +234.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | -33.8 | 0.72 | 1.44 | +263.1 | +236.5 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | -33.8 | 0.72 | 1.44 | +263.1 | +236.5 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | -33.8 | 0.72 | 1.44 | +263.1 | +236.5 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 66.7% | 30.0% | 30.0% | 10.0% | -87.0 | 0.41 | 0.95 | +222.9 | +236.7 |
| `tdi_rsi_gte_50` | 1 | R_RUNNER | 6.7% | 100.0% | 100.0% | 100.0% | +332.0 | 999.00 | 999.00 | +550.0 | +197.0 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 53.3% | 37.5% | 37.5% | 12.5% | -38.0 | 0.74 | 1.23 | +290.7 | +254.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 33.3% | 20.0% | 20.0% | 0.0% | -200.2 | 0.12 | 0.48 | +151.2 | +313.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | -33.8 | 0.72 | 1.44 | +263.1 | +236.5 |
| `feature_momentum_breakout_exception` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | -33.8 | 0.72 | 1.44 | +263.1 | +236.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 6.7% | 100.0% | 100.0% | 100.0% | +332.0 | 999.00 | 999.00 | +550.0 | +197.0 |

### STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+110.4; validation N=5 Fav=40.0% Avg=+42.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | -36.0 | 0.72 | 1.44 | +395.0 | +310.7 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 66.7% | 50.0% | 50.0% | 20.0% | +76.3 | 2.25 | 2.25 | +518.5 | +224.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 73.3% | 45.5% | 45.5% | 18.2% | +47.9 | 1.62 | 1.95 | +473.7 | +269.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | -36.0 | 0.72 | 1.44 | +395.0 | +310.7 |
| `confluence_gte_60` | 8 | S_STRANGER | 53.3% | 25.0% | 25.0% | 0.0% | -34.9 | 0.61 | 1.82 | +458.0 | +323.8 |
| `confluence_gte_70` | 4 | S_STRANGER | 26.7% | 25.0% | 25.0% | 0.0% | -31.0 | 0.57 | 1.71 | +310.7 | +148.0 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -104.5 | 0.00 | 0.00 | +304.0 | +242.0 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 33.3% | 20.0% | 20.0% | 20.0% | -117.4 | 0.24 | 0.98 | +216.0 | +327.8 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 66.7% | 50.0% | 50.0% | 20.0% | +76.3 | 2.25 | 2.25 | +518.5 | +224.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 6.7% | 100.0% | 100.0% | 100.0% | +190.0 | 999.00 | 999.00 | +377.0 | +6.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | -36.0 | 0.72 | 1.44 | +395.0 | +310.7 |
| `feature_momentum_breakout_exception` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 13.3% | -36.0 | 0.72 | 1.44 | +395.0 | +310.7 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 33.3% | 20.0% | 20.0% | 20.0% | -117.4 | 0.24 | 0.98 | +216.0 | +327.8 |

### THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=44.4% Avg=+125.8; validation N=1 Fav=100.0% Avg=+575.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 33.3% | -41.2 | 0.79 | 1.18 | +293.6 | +131.1 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 73.3% | 27.3% | 36.4% | 27.3% | -114.0 | 0.49 | 0.87 | +240.1 | +118.7 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 73.3% | 27.3% | 36.4% | 27.3% | -114.0 | 0.49 | 0.87 | +240.1 | +118.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 33.3% | -41.2 | 0.79 | 1.18 | +293.6 | +131.1 |
| `confluence_gte_60` | 10 | S_STRANGER | 66.7% | 20.0% | 30.0% | 20.0% | -191.5 | 0.23 | 0.53 | +216.2 | +109.2 |
| `confluence_gte_70` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -56.0 | 0.00 | 0.00 | +159.0 | +151.0 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 26.7% | 0.0% | 25.0% | 0.0% | -267.5 | 0.08 | 0.25 | +101.3 | +87.7 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 93.3% | 35.7% | 42.9% | 35.7% | -37.0 | 0.81 | 1.09 | +296.6 | +128.9 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 73.3% | 27.3% | 36.4% | 27.3% | -114.0 | 0.49 | 0.87 | +240.1 | +118.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 26.7% | 0.0% | 25.0% | 0.0% | -267.5 | 0.08 | 0.25 | +101.3 | +87.7 |
| `feature_fresh_reclaim_within_8` | 7 | S_STRANGER | 46.7% | 14.3% | 14.3% | 14.3% | -325.4 | 0.05 | 0.29 | +139.4 | +118.3 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 33.3% | -41.2 | 0.79 | 1.18 | +293.6 | +131.1 |
| `feature_momentum_breakout_exception` | 10 | R_REPEATER | 66.7% | 50.0% | 60.0% | 50.0% | +170.7 | 4.04 | 2.70 | +400.6 | +136.7 |
| `feature_eurjpy_tdi50_reclaim` | 14 | S_STRANGER | 93.3% | 35.7% | 42.9% | 35.7% | -37.0 | 0.81 | 1.09 | +296.6 | +128.9 |

### STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=16.7% Avg=-239.2; validation N=2 Fav=100.0% Avg=+533.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 40.0% | -65.5 | 0.71 | 0.83 | +394.9 | +395.6 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 40.0% | -65.5 | 0.71 | 0.83 | +394.9 | +395.6 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 40.0% | -65.5 | 0.71 | 0.83 | +394.9 | +395.6 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 40.0% | -65.5 | 0.71 | 0.83 | +394.9 | +395.6 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 40.0% | -65.5 | 0.71 | 0.83 | +394.9 | +395.6 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 40.0% | -65.5 | 0.71 | 0.83 | +394.9 | +395.6 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 66.7% | +91.0 | 1.43 | 1.43 | +615.3 | +275.3 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 53.3% | 37.5% | 37.5% | 50.0% | -46.0 | 0.79 | 1.05 | +428.1 | +262.6 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 40.0% | -65.5 | 0.71 | 0.83 | +394.9 | +395.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 66.7% | +91.0 | 1.43 | 1.43 | +615.3 | +275.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 40.0% | -65.5 | 0.71 | 0.83 | +394.9 | +395.6 |
| `feature_momentum_breakout_exception` | 15 | S_STRANGER | 100.0% | 33.3% | 40.0% | 40.0% | -65.5 | 0.71 | 0.83 | +394.9 | +395.6 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 53.3% | 37.5% | 37.5% | 50.0% | -46.0 | 0.79 | 1.05 | +428.1 | +262.6 |

### STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=40.0% Avg=-86.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | -174.2 | 0.17 | 0.35 | +131.0 | +334.1 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 18.2% | -212.1 | 0.08 | 0.21 | +117.7 | +364.5 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 18.2% | -212.1 | 0.08 | 0.21 | +117.7 | +364.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | -174.2 | 0.17 | 0.35 | +131.0 | +334.1 |
| `confluence_gte_60` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | +42.0 | 8.00 | 8.00 | +127.5 | +330.0 |
| `confluence_gte_70` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -12.0 | 0.00 | 0.00 | +60.0 | +548.0 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | -174.2 | 0.17 | 0.35 | +131.0 | +334.1 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 16.7% | -231.0 | 0.07 | 0.13 | +141.3 | +212.3 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 18.2% | -212.1 | 0.08 | 0.21 | +117.7 | +364.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 18.2% | -212.1 | 0.08 | 0.21 | +117.7 | +364.5 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -611.0 | 0.00 | 0.00 | +127.5 | +142.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | -174.2 | 0.17 | 0.35 | +131.0 | +334.1 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 83.3% | 40.0% | 40.0% | 30.0% | -86.8 | 0.34 | 0.50 | +131.7 | +372.5 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 16.7% | -231.0 | 0.07 | 0.13 | +141.3 | +212.3 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=42.9% Avg=+154.7; validation N=4 Fav=50.0% Avg=+293.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 32.3% | 35.5% | 29.0% | +87.2 | 1.59 | 2.46 | +398.5 | +281.2 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 77.4% | 33.3% | 37.5% | 20.8% | +165.6 | 2.27 | 3.53 | +473.7 | +240.7 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 87.1% | 33.3% | 37.0% | 25.9% | +138.3 | 2.09 | 3.14 | +432.7 | +235.6 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 31 | S_STRANGER | 100.0% | 32.3% | 35.5% | 29.0% | +87.2 | 1.59 | 2.46 | +398.5 | +281.2 |
| `confluence_gte_60` | 31 | S_STRANGER | 100.0% | 32.3% | 35.5% | 29.0% | +87.2 | 1.59 | 2.46 | +398.5 | +281.2 |
| `confluence_gte_70` | 31 | S_STRANGER | 100.0% | 32.3% | 35.5% | 29.0% | +87.2 | 1.59 | 2.46 | +398.5 | +281.2 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 41.9% | 38.5% | 38.5% | 15.4% | +113.6 | 1.92 | 2.69 | +365.5 | +260.1 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 77.4% | 33.3% | 33.3% | 25.0% | +142.1 | 2.37 | 3.85 | +391.0 | +202.8 |
| `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 77.4% | 33.3% | 37.5% | 20.8% | +165.6 | 2.27 | 3.53 | +473.7 | +240.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 35.5% | 45.5% | 45.5% | 9.1% | +205.0 | 3.74 | 4.49 | +417.2 | +200.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 32.3% | 35.5% | 29.0% | +87.2 | 1.59 | 2.46 | +398.5 | +281.2 |
| `feature_momentum_breakout_exception` | 23 | S_STRANGER | 74.2% | 34.8% | 39.1% | 39.1% | +119.3 | 1.73 | 2.12 | +429.6 | +313.2 |
| `feature_eurjpy_tdi50_reclaim` | 24 | S_STRANGER | 77.4% | 33.3% | 33.3% | 25.0% | +142.1 | 2.37 | 3.85 | +391.0 | +202.8 |

### THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=50.0% Avg=+177.2; validation N=3 Fav=33.3% Avg=+65.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 32.0% | 32.0% | 32.0% | -32.3 | 0.76 | 1.52 | +288.6 | +241.3 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 76.0% | 36.8% | 36.8% | 36.8% | -5.8 | 0.95 | 1.49 | +286.4 | +246.7 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 84.0% | 38.1% | 38.1% | 38.1% | +9.8 | 1.09 | 1.63 | +326.7 | +254.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 25 | S_STRANGER | 100.0% | 32.0% | 32.0% | 32.0% | -32.3 | 0.76 | 1.52 | +288.6 | +241.3 |
| `confluence_gte_60` | 11 | S_STRANGER | 44.0% | 45.5% | 45.5% | 54.5% | +146.8 | 3.27 | 3.27 | +433.1 | +246.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 20.0% | 20.0% | 20.0% | 40.0% | -103.9 | 0.11 | 0.32 | +141.0 | +128.0 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 64.0% | 31.2% | 31.2% | 31.2% | -60.7 | 0.52 | 1.05 | +226.6 | +153.5 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 76.0% | 36.8% | 36.8% | 36.8% | -5.8 | 0.95 | 1.49 | +286.4 | +246.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 12.0% | 33.3% | 33.3% | 66.7% | -13.5 | 0.61 | 0.61 | +194.7 | +61.7 |
| `feature_fresh_reclaim_within_8` | 4 | R_REPEATER | 16.0% | 50.0% | 50.0% | 50.0% | +13.9 | 1.12 | 1.12 | +365.3 | +160.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 32.0% | 32.0% | 32.0% | -32.3 | 0.76 | 1.52 | +288.6 | +241.3 |
| `feature_momentum_breakout_exception` | 19 | S_STRANGER | 76.0% | 36.8% | 36.8% | 36.8% | +26.9 | 1.26 | 1.98 | +342.0 | +277.9 |
| `feature_eurjpy_tdi50_reclaim` | 15 | S_STRANGER | 60.0% | 26.7% | 26.7% | 33.3% | -72.1 | 0.47 | 1.18 | +212.3 | +162.9 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=17 Fav=47.1% Avg=+2.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 32.0% | 40.0% | 24.0% | -367.6 | 0.54 | 0.81 | +1006.8 | +819.0 |
| `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 100.0% | 32.0% | 40.0% | 24.0% | -367.6 | 0.54 | 0.81 | +1006.8 | +819.0 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 100.0% | 32.0% | 40.0% | 24.0% | -367.6 | 0.54 | 0.81 | +1006.8 | +819.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 25 | S_STRANGER | 100.0% | 32.0% | 40.0% | 24.0% | -367.6 | 0.54 | 0.81 | +1006.8 | +819.0 |
| `confluence_gte_60` | 12 | S_STRANGER | 48.0% | 33.3% | 41.7% | 16.7% | -756.7 | 0.26 | 0.36 | +735.0 | +673.4 |
| `confluence_gte_70` | 7 | S_STRANGER | 28.0% | 42.9% | 57.1% | 14.3% | -708.3 | 0.38 | 0.28 | +833.0 | +222.6 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 56.0% | 42.9% | 57.1% | 28.6% | +14.0 | 1.02 | 0.77 | +1129.4 | +442.0 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 68.0% | 47.1% | 58.8% | 35.3% | +2.4 | 1.00 | 0.70 | +1065.9 | +475.9 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 100.0% | 32.0% | 40.0% | 24.0% | -367.6 | 0.54 | 0.81 | +1006.8 | +819.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 56.0% | 42.9% | 57.1% | 28.6% | +14.0 | 1.02 | 0.77 | +1129.4 | +442.0 |
| `feature_fresh_reclaim_within_8` | 3 | S_STRANGER | 12.0% | 0.0% | 33.3% | 0.0% | -256.7 | 0.62 | 1.24 | +743.0 | +996.7 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 32.0% | 40.0% | 24.0% | -367.6 | 0.54 | 0.81 | +1006.8 | +819.0 |
| `feature_momentum_breakout_exception` | 21 | S_STRANGER | 84.0% | 38.1% | 42.9% | 28.6% | -91.3 | 0.84 | 1.12 | +1116.7 | +935.3 |
| `feature_eurjpy_tdi50_reclaim` | 17 | S_STRANGER | 68.0% | 47.1% | 58.8% | 35.3% | +2.4 | 1.00 | 0.70 | +1065.9 | +475.9 |

### STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=27.3% Avg=-5.3; validation N=4 Fav=50.0% Avg=+122.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 51 | S_STRANGER | 100.0% | 31.4% | 37.3% | 15.7% | +108.1 | 1.75 | 2.95 | +535.7 | +256.7 |
| `hunt_to_ar_ratio_le_2_0` | 39 | S_STRANGER | 76.5% | 30.8% | 38.5% | 17.9% | +153.6 | 2.10 | 3.36 | +593.9 | +256.6 |
| `hunt_to_ar_ratio_le_2_5` | 40 | S_STRANGER | 78.4% | 30.0% | 37.5% | 17.5% | +147.9 | 2.07 | 3.45 | +584.2 | +253.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 51 | S_STRANGER | 100.0% | 31.4% | 37.3% | 15.7% | +108.1 | 1.75 | 2.95 | +535.7 | +256.7 |
| `confluence_gte_60` | 34 | S_STRANGER | 66.7% | 32.4% | 38.2% | 11.8% | +8.6 | 1.06 | 1.71 | +449.9 | +248.4 |
| `confluence_gte_70` | 4 | S_STRANGER | 7.8% | 25.0% | 25.0% | 0.0% | +114.0 | 2.33 | 6.99 | +608.2 | +238.5 |
| `tdi_rsi_gt_signal` | 31 | S_STRANGER | 60.8% | 29.0% | 32.3% | 16.1% | +10.4 | 1.09 | 2.29 | +359.7 | +205.3 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 33.3% | 29.4% | 35.3% | 23.5% | -43.2 | 0.76 | 1.39 | +320.5 | +247.5 |
| `ratio_le_2_and_asian_gte_30` | 39 | S_STRANGER | 76.5% | 30.8% | 38.5% | 17.9% | +153.6 | 2.10 | 3.36 | +593.9 | +256.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 22 | S_STRANGER | 43.1% | 27.3% | 31.8% | 18.2% | +28.1 | 1.28 | 2.74 | +357.5 | +186.5 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 3.9% | 0.0% | 0.0% | 0.0% | -347.0 | 0.00 | 0.00 | +44.0 | +501.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 51 | S_STRANGER | 100.0% | 31.4% | 37.3% | 15.7% | +108.1 | 1.75 | 2.95 | +535.7 | +256.7 |
| `feature_momentum_breakout_exception` | 49 | S_STRANGER | 96.1% | 32.7% | 38.8% | 16.3% | +124.0 | 1.90 | 3.00 | +554.5 | +256.5 |
| `feature_eurjpy_tdi50_reclaim` | 15 | S_STRANGER | 29.4% | 33.3% | 40.0% | 26.7% | +28.6 | 1.23 | 1.85 | +310.5 | +181.8 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=16 Fav=31.2% Avg=+189.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +189.1 | 1.43 | 3.16 | +1009.7 | +746.6 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 50.0% | 37.5% | 37.5% | 37.5% | -94.7 | 0.62 | 1.04 | +290.6 | +428.5 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 50.0% | 37.5% | 37.5% | 37.5% | -94.7 | 0.62 | 1.04 | +290.6 | +428.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +189.1 | 1.43 | 3.16 | +1009.7 | +746.6 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +189.1 | 1.43 | 3.16 | +1009.7 | +746.6 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +189.1 | 1.43 | 3.16 | +1009.7 | +746.6 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 68.8% | 27.3% | 27.3% | 27.3% | +58.0 | 1.10 | 2.92 | +985.2 | +897.4 |
| `tdi_rsi_gte_50` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 50.0% | 37.5% | 37.5% | 37.5% | -94.7 | 0.62 | 1.04 | +290.6 | +428.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 31.2% | 40.0% | 40.0% | 40.0% | -128.7 | 0.62 | 0.93 | +329.6 | +532.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +189.1 | 1.43 | 3.16 | +1009.7 | +746.6 |
| `feature_momentum_breakout_exception` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 31.2% | +189.1 | 1.43 | 3.16 | +1009.7 | +746.6 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### RRT_REVERSAL|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|SELL|EARLY_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=15 Fav=33.3% Avg=+59.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 18.8% | +29.4 | 1.25 | 2.09 | +296.9 | +190.5 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 81.2% | 23.1% | 30.8% | 23.1% | -22.1 | 0.84 | 1.89 | +285.8 | +181.3 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 81.2% | 23.1% | 30.8% | 23.1% | -22.1 | 0.84 | 1.89 | +285.8 | +181.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 18.8% | +29.4 | 1.25 | 2.09 | +296.9 | +190.5 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 18.8% | +29.4 | 1.25 | 2.09 | +296.9 | +190.5 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 18.8% | +29.4 | 1.25 | 2.09 | +296.9 | +190.5 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -418.0 | 0.00 | 0.00 | +132.0 | +77.0 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 18.8% | 0.0% | 33.3% | 33.3% | -61.0 | 0.61 | 1.21 | +252.3 | +93.7 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 81.2% | 23.1% | 30.8% | 23.1% | -22.1 | 0.84 | 1.89 | +285.8 | +181.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -418.0 | 0.00 | 0.00 | +132.0 | +77.0 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 12.5% | 0.0% | 50.0% | 50.0% | -68.0 | 0.67 | 0.67 | +207.5 | +65.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 18.8% | +29.4 | 1.25 | 2.09 | +296.9 | +190.5 |
| `feature_momentum_breakout_exception` | 15 | S_STRANGER | 93.8% | 33.3% | 40.0% | 20.0% | +59.3 | 1.62 | 2.43 | +307.9 | +198.1 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 12.5% | 0.0% | 50.0% | 50.0% | -68.0 | 0.67 | 0.67 | +207.5 | +65.5 |

### STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=41.7% Avg=+114.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 43.8% | +29.1 | 1.39 | 1.39 | +199.8 | +103.7 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 75.0% | 33.3% | 41.7% | 33.3% | +19.8 | 1.20 | 1.68 | +200.6 | +118.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 87.5% | 28.6% | 42.9% | 35.7% | +19.3 | 1.23 | 1.43 | +191.0 | +114.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 43.8% | +29.1 | 1.39 | 1.39 | +199.8 | +103.7 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 43.8% | +29.1 | 1.39 | 1.39 | +199.8 | +103.7 |
| `confluence_gte_70` | 8 | S_STRANGER | 50.0% | 25.0% | 37.5% | 25.0% | -62.4 | 0.48 | 0.80 | +133.0 | +98.9 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 50.0% | -45.0 | 0.00 | 0.00 | +120.0 | +145.5 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 62.5% | 20.0% | 30.0% | 40.0% | -56.7 | 0.41 | 0.68 | +141.8 | +83.3 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 75.0% | 33.3% | 41.7% | 33.3% | +19.8 | 1.20 | 1.68 | +200.6 | +118.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -90.0 | 0.00 | 0.00 | +41.0 | +164.0 |
| `feature_fresh_reclaim_within_8` | 4 | S_STRANGER | 25.0% | 25.0% | 50.0% | 50.0% | -96.0 | 0.33 | 0.17 | +133.5 | +36.3 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 43.8% | +29.1 | 1.39 | 1.39 | +199.8 | +103.7 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 75.0% | 41.7% | 58.3% | 58.3% | +114.7 | 6.12 | 2.62 | +249.1 | +110.2 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 62.5% | 20.0% | 30.0% | 40.0% | -56.7 | 0.41 | 0.68 | +141.8 | +83.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-258.5; validation N=13 Fav=30.8% Avg=-402.3; out_of_sample N=1 Fav=100.0% Avg=+1951.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 18.8% | -237.3 | 0.52 | 1.14 | +493.2 | +637.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 81.2% | 23.1% | 23.1% | 7.7% | -263.8 | 0.44 | 1.47 | +482.2 | +612.8 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 93.8% | 26.7% | 26.7% | 13.3% | -271.0 | 0.48 | 1.33 | +498.5 | +678.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 18.8% | -237.3 | 0.52 | 1.14 | +493.2 | +637.1 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 18.8% | -237.3 | 0.52 | 1.14 | +493.2 | +637.1 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 18.8% | -237.3 | 0.52 | 1.14 | +493.2 | +637.1 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -754.3 | 0.00 | 0.00 | +135.5 | +772.8 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 50.0% | 25.0% | 25.0% | 0.0% | -334.5 | 0.48 | 1.43 | +493.1 | +905.0 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 81.2% | 23.1% | 23.1% | 7.7% | -263.8 | 0.44 | 1.47 | +482.2 | +612.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -754.3 | 0.00 | 0.00 | +135.5 | +772.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 18.8% | -237.3 | 0.52 | 1.14 | +493.2 | +637.1 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 81.2% | 30.8% | 30.8% | 23.1% | -221.0 | 0.55 | 1.25 | +485.6 | +605.9 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 50.0% | 25.0% | 25.0% | 0.0% | -334.5 | 0.48 | 1.43 | +493.1 | +905.0 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=14 Fav=35.7% Avg=-55.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 37.5% | -293.6 | 0.60 | 0.77 | +1316.7 | +934.6 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 37.5% | -293.6 | 0.60 | 0.77 | +1316.7 | +934.6 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 37.5% | -293.6 | 0.60 | 0.77 | +1316.7 | +934.6 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 37.5% | -293.6 | 0.60 | 0.77 | +1316.7 | +934.6 |
| `confluence_gte_60` | 9 | S_STRANGER | 56.2% | 33.3% | 44.4% | 44.4% | -172.9 | 0.71 | 0.89 | +1437.1 | +808.3 |
| `confluence_gte_70` | 7 | S_STRANGER | 43.8% | 14.3% | 28.6% | 28.6% | -405.3 | 0.48 | 1.19 | +1288.9 | +781.6 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 25.0% | 25.0% | 50.0% | 50.0% | -319.8 | 0.60 | 0.60 | +964.0 | +895.8 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 81.2% | 30.8% | 46.2% | 38.5% | -145.2 | 0.78 | 0.91 | +1409.1 | +750.5 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 37.5% | -293.6 | 0.60 | 0.77 | +1316.7 | +934.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 25.0% | 25.0% | 50.0% | 50.0% | -319.8 | 0.60 | 0.60 | +964.0 | +895.8 |
| `feature_fresh_reclaim_within_8` | 7 | S_STRANGER | 43.8% | 28.6% | 42.9% | 28.6% | -401.1 | 0.45 | 0.60 | +1221.0 | +511.3 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 31.2% | 43.8% | 37.5% | -293.6 | 0.60 | 0.77 | +1316.7 | +934.6 |
| `feature_momentum_breakout_exception` | 14 | S_STRANGER | 87.5% | 35.7% | 50.0% | 42.9% | -55.4 | 0.90 | 0.90 | +1423.9 | +1013.6 |
| `feature_eurjpy_tdi50_reclaim` | 13 | S_STRANGER | 81.2% | 30.8% | 46.2% | 38.5% | -145.2 | 0.78 | 0.91 | +1409.1 | +750.5 |

### STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=19 Fav=36.8% Avg=+30.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 30.4% | 39.1% | 26.1% | +17.2 | 1.16 | 1.41 | +331.5 | +214.7 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 82.6% | 26.3% | 31.6% | 26.3% | -43.2 | 0.68 | 1.24 | +311.2 | +244.0 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 91.3% | 28.6% | 33.3% | 28.6% | -20.5 | 0.83 | 1.31 | +314.3 | +231.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 23 | S_STRANGER | 100.0% | 30.4% | 39.1% | 26.1% | +17.2 | 1.16 | 1.41 | +331.5 | +214.7 |
| `confluence_gte_60` | 16 | S_STRANGER | 69.6% | 25.0% | 31.2% | 12.5% | -46.2 | 0.68 | 1.37 | +352.9 | +269.9 |
| `confluence_gte_70` | 3 | S_STRANGER | 13.0% | 0.0% | 33.3% | 0.0% | -166.0 | 0.23 | 0.46 | +190.7 | +311.7 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 52.2% | 16.7% | 33.3% | 41.7% | -17.3 | 0.84 | 1.05 | +225.8 | +174.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 30.4% | 28.6% | 57.1% | 42.9% | +118.1 | 3.86 | 1.93 | +243.6 | +86.6 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 82.6% | 26.3% | 31.6% | 26.3% | -43.2 | 0.68 | 1.24 | +311.2 | +244.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 43.5% | 20.0% | 30.0% | 40.0% | -29.0 | 0.78 | 1.30 | +242.3 | +200.4 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -198.0 | 0.00 | 0.00 | +15.0 | +99.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 30.4% | 39.1% | 26.1% | +17.2 | 1.16 | 1.41 | +331.5 | +214.7 |
| `feature_momentum_breakout_exception` | 19 | S_STRANGER | 82.6% | 36.8% | 36.8% | 31.6% | +30.7 | 1.27 | 1.64 | +345.2 | +220.8 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 26.1% | 33.3% | 66.7% | 50.0% | +152.9 | 5.63 | 1.41 | +240.8 | +53.0 |

### STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=30.0% Avg=+25.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +25.8 | 1.20 | 2.81 | +325.7 | +259.7 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 0.0% | -62.0 | 0.59 | 3.51 | +249.4 | +288.4 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 0.0% | -62.0 | 0.59 | 3.51 | +249.4 | +288.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +25.8 | 1.20 | 2.81 | +325.7 | +259.7 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +25.8 | 1.20 | 2.81 | +325.7 | +259.7 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +25.8 | 1.20 | 2.81 | +325.7 | +259.7 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -224.0 | 0.00 | 0.00 | +237.0 | +233.0 |
| `tdi_rsi_gte_50` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 0.0% | -62.0 | 0.59 | 3.51 | +249.4 | +288.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +25.8 | 1.20 | 2.81 | +325.7 | +259.7 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +25.8 | 1.20 | 2.81 | +325.7 | +259.7 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=42.9% Avg=+255.9; validation N=2 Fav=0.0% Avg=-714.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +9.4 | 1.04 | 2.42 | +467.0 | +547.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +9.4 | 1.04 | 2.42 | +467.0 | +547.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +9.4 | 1.04 | 2.42 | +467.0 | +547.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +9.4 | 1.04 | 2.42 | +467.0 | +547.9 |
| `confluence_gte_60` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 0.0% | -200.4 | 0.26 | 1.04 | +182.8 | +610.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 90.0% | 33.3% | 33.3% | 11.1% | +40.2 | 1.16 | 2.32 | +506.1 | +471.1 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -110.0 | 0.00 | 0.00 | +102.0 | +174.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +9.4 | 1.04 | 2.42 | +467.0 | +547.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 90.0% | 33.3% | 33.3% | 11.1% | +40.2 | 1.16 | 2.32 | +506.1 | +471.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +9.4 | 1.04 | 2.42 | +467.0 | +547.9 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | +9.4 | 1.04 | 2.42 | +467.0 | +547.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -110.0 | 0.00 | 0.00 | +102.0 | +174.0 |

### RRT_REVERSAL|SELL|EARLY_WEEK|L0|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|EARLY_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+185.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 30.0% | 35.0% | 35.0% | -20.2 | 0.85 | 1.34 | +289.6 | +231.7 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 22.2% | 27.8% | 27.8% | -48.7 | 0.69 | 1.51 | +278.7 | +248.1 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 90.0% | 22.2% | 27.8% | 27.8% | -48.7 | 0.69 | 1.51 | +278.7 | +248.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 20 | S_STRANGER | 100.0% | 30.0% | 35.0% | 35.0% | -20.2 | 0.85 | 1.34 | +289.6 | +231.7 |
| `confluence_gte_60` | 5 | S_STRANGER | 25.0% | 40.0% | 40.0% | 60.0% | +185.4 | 7.57 | 7.57 | +365.0 | +141.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 55.0% | 36.4% | 36.4% | 45.5% | -0.9 | 0.99 | 1.49 | +338.2 | +215.9 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 40.0% | 25.0% | 37.5% | 25.0% | -127.1 | 0.16 | 0.27 | +128.1 | +148.4 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 90.0% | 22.2% | 27.8% | 27.8% | -48.7 | 0.69 | 1.51 | +278.7 | +248.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 50.0% | 30.0% | 30.0% | 40.0% | -12.0 | 0.93 | 1.87 | +352.7 | +237.1 |
| `feature_fresh_reclaim_within_8` | 4 | S_STRANGER | 20.0% | 0.0% | 25.0% | 0.0% | -246.0 | 0.03 | 0.08 | +91.8 | +186.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 30.0% | 35.0% | 35.0% | -20.2 | 0.85 | 1.34 | +289.6 | +231.7 |
| `feature_momentum_breakout_exception` | 17 | S_STRANGER | 85.0% | 35.3% | 35.3% | 41.2% | +15.0 | 1.12 | 1.68 | +327.6 | +250.9 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 40.0% | 25.0% | 37.5% | 25.0% | -127.1 | 0.16 | 0.27 | +128.1 | +148.4 |

### STOP_HUNT|SELL|EARLY_WEEK|L0|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|EARLY_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+2.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | -25.7 | 0.82 | 1.23 | +318.9 | +258.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | -25.7 | 0.82 | 1.23 | +318.9 | +258.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | -25.7 | 0.82 | 1.23 | +318.9 | +258.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | -25.7 | 0.82 | 1.23 | +318.9 | +258.0 |
| `confluence_gte_60` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 37.5% | -17.9 | 0.89 | 1.48 | +380.1 | +278.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 20.0% | 40.0% | 20.0% | +2.0 | 1.03 | 1.54 | +287.0 | +237.6 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +56.0 | 1.80 | 3.59 | +308.0 | +159.7 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | -25.7 | 0.82 | 1.23 | +318.9 | +258.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 50.0% | 20.0% | 40.0% | 20.0% | +2.0 | 1.03 | 1.54 | +287.0 | +237.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | -25.7 | 0.82 | 1.23 | +318.9 | +258.0 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 40.0% | 30.0% | -25.7 | 0.82 | 1.23 | +318.9 | +258.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | +56.0 | 1.80 | 3.59 | +308.0 | +159.7 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=28.6% Avg=+20.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | -29.5 | 0.65 | 1.08 | +150.2 | +193.5 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 16.7% | -111.7 | 0.07 | 0.26 | +116.7 | +272.0 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 28.6% | -85.0 | 0.17 | 0.34 | +114.6 | +235.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | -29.5 | 0.65 | 1.08 | +150.2 | +193.5 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | -29.5 | 0.65 | 1.08 | +150.2 | +193.5 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | -29.5 | 0.65 | 1.08 | +150.2 | +193.5 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 42.9% | +20.1 | 1.43 | 2.15 | +188.7 | +161.7 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 50.0% | -41.5 | 0.00 | 0.00 | +254.5 | +284.0 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 16.7% | -111.7 | 0.07 | 0.26 | +116.7 | +272.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | -55.8 | 0.14 | 0.43 | +126.4 | +195.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | -29.5 | 0.65 | 1.08 | +150.2 | +193.5 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | -29.5 | 0.65 | 1.08 | +150.2 | +193.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 50.0% | -41.5 | 0.00 | 0.00 | +254.5 | +284.0 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=25.0% Avg=-236.8; validation N=2 Fav=50.0% Avg=+39.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -181.6 | 0.36 | 0.84 | +262.2 | +393.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -181.6 | 0.36 | 0.84 | +262.2 | +393.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -181.6 | 0.36 | 0.84 | +262.2 | +393.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -181.6 | 0.36 | 0.84 | +262.2 | +393.0 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -181.6 | 0.36 | 0.84 | +262.2 | +393.0 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -181.6 | 0.36 | 0.84 | +262.2 | +393.0 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | -81.0 | 0.59 | 0.59 | +164.5 | +223.5 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | -273.5 | 0.41 | 1.23 | +389.5 | +619.2 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -181.6 | 0.36 | 0.84 | +262.2 | +393.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | -81.0 | 0.59 | 0.59 | +164.5 | +223.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -181.6 | 0.36 | 0.84 | +262.2 | +393.0 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | -181.6 | 0.36 | 0.84 | +262.2 | +393.0 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | -273.5 | 0.41 | 1.23 | +389.5 | +619.2 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+55.4; validation N=6 Fav=33.3% Avg=-37.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 50.0% | +11.9 | 1.18 | 1.41 | +282.7 | +233.4 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 85.7% | 16.7% | 25.0% | 50.0% | -32.0 | 0.59 | 1.17 | +271.1 | +260.4 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 23.1% | 30.8% | 53.8% | -23.2 | 0.67 | 1.01 | +268.0 | +243.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 50.0% | +11.9 | 1.18 | 1.41 | +282.7 | +233.4 |
| `confluence_gte_60` | 10 | S_STRANGER | 71.4% | 20.0% | 30.0% | 60.0% | -22.5 | 0.68 | 0.90 | +291.4 | +274.9 |
| `confluence_gte_70` | 3 | R_REPEATER | 21.4% | 66.7% | 66.7% | 100.0% | +109.3 | 999.00 | 999.00 | +273.0 | +83.3 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 50.0% | +234.0 | 999.00 | 999.00 | +902.5 | +367.5 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 71.4% | 30.0% | 40.0% | 70.0% | +22.7 | 1.57 | 1.18 | +336.0 | +190.3 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 85.7% | 16.7% | 25.0% | 50.0% | -32.0 | 0.59 | 1.17 | +271.1 | +260.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +1331.0 | +627.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 50.0% | +11.9 | 1.18 | 1.41 | +282.7 | +233.4 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 92.9% | 30.8% | 38.5% | 46.2% | +12.8 | 1.18 | 1.41 | +202.1 | +203.2 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 71.4% | 30.0% | 40.0% | 70.0% | +22.7 | 1.57 | 1.18 | +336.0 | +190.3 |

### RRT_REVERSAL|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|SELL|EARLY_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=11 Fav=36.4% Avg=+42.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 14.3% | +1.0 | 1.01 | 1.82 | +310.4 | +197.6 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 78.6% | 36.4% | 45.5% | 18.2% | +42.3 | 1.44 | 1.73 | +365.8 | +159.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 85.7% | 33.3% | 41.7% | 16.7% | +32.7 | 1.35 | 1.89 | +340.4 | +176.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 14.3% | +1.0 | 1.01 | 1.82 | +310.4 | +197.6 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 14.3% | +1.0 | 1.01 | 1.82 | +310.4 | +197.6 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 14.3% | +1.0 | 1.01 | 1.82 | +310.4 | +197.6 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 50.0% | 14.3% | 28.6% | 14.3% | +20.4 | 1.21 | 3.04 | +340.9 | +208.9 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 28.6% | 0.0% | 25.0% | 0.0% | -95.0 | 0.33 | 1.00 | +102.8 | +195.2 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 78.6% | 36.4% | 45.5% | 18.2% | +42.3 | 1.44 | 1.73 | +365.8 | +159.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 35.7% | 20.0% | 40.0% | 20.0% | +97.0 | 2.50 | 3.75 | +451.4 | +159.6 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -149.5 | 0.00 | 0.00 | +77.0 | +229.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 28.6% | 35.7% | 14.3% | +1.0 | 1.01 | 1.82 | +310.4 | +197.6 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 78.6% | 36.4% | 36.4% | 18.2% | +11.3 | 1.10 | 1.93 | +363.9 | +207.7 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 28.6% | 0.0% | 25.0% | 0.0% | -95.0 | 0.33 | 1.00 | +102.8 | +195.2 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+495.0; validation N=3 Fav=66.7% Avg=+105.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 28.6% | 31.4% | 20.0% | -89.4 | 0.57 | 1.19 | +296.1 | +402.1 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 88.6% | 29.0% | 32.3% | 19.4% | -68.0 | 0.65 | 1.30 | +300.9 | +388.2 |
| `hunt_to_ar_ratio_le_2_5` | 32 | S_STRANGER | 91.4% | 28.1% | 31.2% | 18.8% | -75.3 | 0.62 | 1.30 | +296.5 | +387.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 35 | S_STRANGER | 100.0% | 28.6% | 31.4% | 20.0% | -89.4 | 0.57 | 1.19 | +296.1 | +402.1 |
| `confluence_gte_60` | 23 | S_STRANGER | 65.7% | 34.8% | 34.8% | 30.4% | +2.8 | 1.02 | 1.78 | +311.6 | +346.7 |
| `confluence_gte_70` | 5 | R_REPEATER | 14.3% | 60.0% | 60.0% | 40.0% | +261.4 | 8.47 | 2.82 | +405.8 | +191.4 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 17.1% | 33.3% | 33.3% | 50.0% | +174.0 | 3.38 | 5.07 | +402.3 | +234.7 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 65.7% | 26.1% | 26.1% | 13.0% | -121.7 | 0.44 | 1.17 | +257.7 | +438.9 |
| `ratio_le_2_and_asian_gte_30` | 31 | S_STRANGER | 88.6% | 29.0% | 32.3% | 19.4% | -68.0 | 0.65 | 1.30 | +300.9 | +388.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 17.1% | 33.3% | 33.3% | 50.0% | +174.0 | 3.38 | 5.07 | +402.3 | +234.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 82.9% | 31.0% | 34.5% | 24.1% | -25.7 | 0.84 | 1.52 | +317.7 | +327.7 |
| `feature_momentum_breakout_exception` | 27 | S_STRANGER | 77.1% | 33.3% | 37.0% | 25.9% | -43.5 | 0.78 | 1.24 | +321.4 | +384.4 |
| `feature_eurjpy_tdi50_reclaim` | 23 | S_STRANGER | 65.7% | 26.1% | 26.1% | 13.0% | -121.7 | 0.44 | 1.17 | +257.7 | +438.9 |

### STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=30.8% Avg=-6.2; validation N=7 Fav=28.6% Avg=-592.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 28.6% | 28.6% | 4.8% | -203.9 | 0.56 | 1.40 | +786.9 | +735.9 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 81.0% | 23.5% | 23.5% | 0.0% | -308.8 | 0.44 | 1.44 | +700.7 | +758.8 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 85.7% | 22.2% | 22.2% | 0.0% | -294.8 | 0.44 | 1.54 | +684.3 | +725.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 21 | S_STRANGER | 100.0% | 28.6% | 28.6% | 4.8% | -203.9 | 0.56 | 1.40 | +786.9 | +735.9 |
| `confluence_gte_60` | 20 | S_STRANGER | 95.2% | 30.0% | 30.0% | 5.0% | -211.2 | 0.57 | 1.32 | +806.0 | +764.8 |
| `confluence_gte_70` | 4 | S_STRANGER | 19.0% | 25.0% | 25.0% | 0.0% | -352.7 | 0.13 | 0.39 | +671.5 | +764.2 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -4299.0 | 0.00 | 0.00 | +48.0 | +4415.0 |
| `tdi_rsi_gte_50` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 81.0% | 23.5% | 23.5% | 0.0% | -308.8 | 0.44 | 1.44 | +700.7 | +758.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -4299.0 | 0.00 | 0.00 | +48.0 | +4415.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 28.6% | 28.6% | 4.8% | -203.9 | 0.56 | 1.40 | +786.9 | +735.9 |
| `feature_momentum_breakout_exception` | 21 | S_STRANGER | 100.0% | 28.6% | 28.6% | 4.8% | -203.9 | 0.56 | 1.40 | +786.9 | +735.9 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=30 Fav=30.0% Avg=+105.4; out_of_sample N=3 Fav=33.3% Avg=-269.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 36 | S_STRANGER | 100.0% | 27.8% | 36.1% | 16.7% | +67.4 | 1.15 | 2.04 | +1066.9 | +883.0 |
| `hunt_to_ar_ratio_le_2_0` | 34 | S_STRANGER | 94.4% | 29.4% | 38.2% | 17.6% | +159.3 | 1.42 | 2.30 | +1121.3 | +774.1 |
| `hunt_to_ar_ratio_le_2_5` | 35 | S_STRANGER | 97.2% | 28.6% | 37.1% | 17.1% | +104.7 | 1.25 | 2.12 | +1096.7 | +822.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 36 | S_STRANGER | 100.0% | 27.8% | 36.1% | 16.7% | +67.4 | 1.15 | 2.04 | +1066.9 | +883.0 |
| `confluence_gte_60` | 23 | S_STRANGER | 63.9% | 21.7% | 30.4% | 8.7% | -217.0 | 0.55 | 1.26 | +806.5 | +1042.6 |
| `confluence_gte_70` | 1 | S_STRANGER | 2.8% | 0.0% | 100.0% | 0.0% | +1319.0 | 999.00 | 999.00 | +1390.0 | +416.0 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 52.8% | 21.1% | 36.8% | 10.5% | -94.3 | 0.82 | 1.41 | +843.7 | +878.8 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 38.9% | 28.6% | 50.0% | 21.4% | +270.1 | 1.84 | 1.84 | +1043.6 | +565.2 |
| `ratio_le_2_and_asian_gte_30` | 34 | S_STRANGER | 94.4% | 29.4% | 38.2% | 17.6% | +159.3 | 1.42 | 2.30 | +1121.3 | +774.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 18 | S_STRANGER | 50.0% | 22.2% | 38.9% | 11.1% | -2.4 | 0.99 | 1.56 | +876.1 | +790.2 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -402.0 | 0.00 | 0.00 | +225.0 | +806.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 36 | S_STRANGER | 100.0% | 27.8% | 36.1% | 16.7% | +67.4 | 1.15 | 2.04 | +1066.9 | +883.0 |
| `feature_momentum_breakout_exception` | 33 | S_STRANGER | 91.7% | 30.3% | 33.3% | 18.2% | +71.4 | 1.16 | 2.31 | +1105.9 | +934.7 |
| `feature_eurjpy_tdi50_reclaim` | 14 | S_STRANGER | 38.9% | 28.6% | 50.0% | 21.4% | +270.1 | 1.84 | 1.84 | +1043.6 | +565.2 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=18 Fav=27.8% Avg=+88.7; validation N=7 Fav=42.9% Avg=-41.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 36 | S_STRANGER | 100.0% | 27.8% | 33.3% | 19.4% | +26.4 | 1.15 | 2.02 | +430.2 | +314.8 |
| `hunt_to_ar_ratio_le_2_0` | 33 | S_STRANGER | 91.7% | 27.3% | 33.3% | 18.2% | +22.1 | 1.13 | 1.94 | +446.6 | +311.3 |
| `hunt_to_ar_ratio_le_2_5` | 33 | S_STRANGER | 91.7% | 27.3% | 33.3% | 18.2% | +22.1 | 1.13 | 1.94 | +446.6 | +311.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 36 | S_STRANGER | 100.0% | 27.8% | 33.3% | 19.4% | +26.4 | 1.15 | 2.02 | +430.2 | +314.8 |
| `confluence_gte_60` | 25 | S_STRANGER | 69.4% | 32.0% | 36.0% | 16.0% | +52.3 | 1.31 | 2.18 | +494.7 | +292.9 |
| `confluence_gte_70` | 8 | S_STRANGER | 22.2% | 25.0% | 25.0% | 0.0% | -199.8 | 0.31 | 0.92 | +421.4 | +492.1 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 8.3% | 33.3% | 33.3% | 0.0% | -114.7 | 0.37 | 0.74 | +313.0 | +288.7 |
| `tdi_rsi_gte_50` | 31 | S_STRANGER | 86.1% | 29.0% | 32.3% | 19.4% | +38.0 | 1.23 | 2.21 | +461.6 | +306.4 |
| `ratio_le_2_and_asian_gte_30` | 33 | S_STRANGER | 91.7% | 27.3% | 33.3% | 18.2% | +22.1 | 1.13 | 1.94 | +446.6 | +311.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 8.3% | 33.3% | 33.3% | 0.0% | -114.7 | 0.37 | 0.74 | +313.0 | +288.7 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 2.8% | 0.0% | 0.0% | 0.0% | -411.0 | 0.00 | 0.00 | +198.0 | +428.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 34 | S_STRANGER | 94.4% | 26.5% | 32.4% | 20.6% | -1.0 | 0.99 | 1.81 | +420.0 | +325.0 |
| `feature_momentum_breakout_exception` | 27 | S_STRANGER | 75.0% | 22.2% | 29.6% | 22.2% | +3.0 | 1.02 | 2.04 | +350.1 | +263.4 |
| `feature_eurjpy_tdi50_reclaim` | 30 | S_STRANGER | 83.3% | 30.0% | 33.3% | 20.0% | +53.0 | 1.33 | 2.27 | +471.1 | +313.4 |

### RRT_REVERSAL|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=10 Fav=30.0% Avg=+117.9; out_of_sample N=1 Fav=0.0% Avg=-1688.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 45.5% | -46.3 | 0.85 | 1.71 | +892.0 | +659.3 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 45.5% | -46.3 | 0.85 | 1.71 | +892.0 | +659.3 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 45.5% | -46.3 | 0.85 | 1.71 | +892.0 | +659.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 45.5% | -46.3 | 0.85 | 1.71 | +892.0 | +659.3 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 45.5% | -46.3 | 0.85 | 1.71 | +892.0 | +659.3 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 45.5% | -46.3 | 0.85 | 1.71 | +892.0 | +659.3 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 44.4% | -0.7 | 1.00 | 2.49 | +937.7 | +598.7 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 14.3% | 14.3% | 28.6% | -88.0 | 0.66 | 3.29 | +977.3 | +682.9 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 45.5% | -46.3 | 0.85 | 1.71 | +892.0 | +659.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 44.4% | -0.7 | 1.00 | 2.49 | +937.7 | +598.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 45.5% | -46.3 | 0.85 | 1.71 | +892.0 | +659.3 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 45.5% | -46.3 | 0.85 | 1.71 | +892.0 | +659.3 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 63.6% | 14.3% | 14.3% | 28.6% | -88.0 | 0.66 | 3.29 | +977.3 | +682.9 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-66.0; validation N=7 Fav=42.9% Avg=+44.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 36.4% | -112.5 | 0.40 | 0.60 | +448.6 | +429.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 30.0% | 40.0% | 40.0% | -98.1 | 0.45 | 0.57 | +439.0 | +406.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 90.9% | 30.0% | 40.0% | 40.0% | -98.1 | 0.45 | 0.57 | +439.0 | +406.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 36.4% | -112.5 | 0.40 | 0.60 | +448.6 | +429.3 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 36.4% | -112.5 | 0.40 | 0.60 | +448.6 | +429.3 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 36.4% | -112.5 | 0.40 | 0.60 | +448.6 | +429.3 |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 100.0% | +188.0 | 999.00 | 999.00 | +742.0 | +330.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 28.6% | -238.8 | 0.16 | 0.40 | +572.4 | +561.6 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 90.9% | 30.0% | 40.0% | 40.0% | -98.1 | 0.45 | 0.57 | +439.0 | +406.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 100.0% | +188.0 | 999.00 | 999.00 | +742.0 | +330.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 36.4% | 36.4% | -112.5 | 0.40 | 0.60 | +448.6 | +429.3 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 72.7% | 37.5% | 50.0% | 50.0% | +30.8 | 1.43 | 1.07 | +409.2 | +281.9 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 28.6% | -238.8 | 0.16 | 0.40 | +572.4 | +561.6 |

### STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=42.9% Avg=-18.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -113.6 | 0.46 | 1.08 | +269.0 | +299.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 20.0% | -124.3 | 0.47 | 0.93 | +291.5 | +320.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 20.0% | -124.3 | 0.47 | 0.93 | +291.5 | +320.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -113.6 | 0.46 | 1.08 | +269.0 | +299.5 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -113.6 | 0.46 | 1.08 | +269.0 | +299.5 |
| `confluence_gte_70` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 0.0% | -107.3 | 0.59 | 1.18 | +381.3 | +376.2 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 28.6% | -18.2 | 0.89 | 0.89 | +311.3 | +229.9 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 50.0% | -79.9 | 0.33 | 0.66 | +156.7 | +152.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 20.0% | -124.3 | 0.47 | 0.93 | +291.5 | +320.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 63.6% | 42.9% | 42.9% | 28.6% | -18.2 | 0.89 | 0.89 | +311.3 | +229.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -113.6 | 0.46 | 1.08 | +269.0 | +299.5 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -113.6 | 0.46 | 1.08 | +269.0 | +299.5 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 50.0% | -79.9 | 0.33 | 0.66 | +156.7 | +152.0 |

### STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-138.0; validation N=8 Fav=37.5% Avg=-134.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -149.6 | 0.45 | 1.20 | +408.0 | +361.7 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 22.2% | -207.2 | 0.20 | 0.70 | +314.9 | +285.7 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 22.2% | -207.2 | 0.20 | 0.70 | +314.9 | +285.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -149.6 | 0.45 | 1.20 | +408.0 | +361.7 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -149.6 | 0.45 | 1.20 | +408.0 | +361.7 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -149.6 | 0.45 | 1.20 | +408.0 | +361.7 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | -426.2 | 0.05 | 0.21 | +279.2 | +597.6 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 28.6% | -130.4 | 0.34 | 0.84 | +393.4 | +446.7 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 22.2% | -207.2 | 0.20 | 0.70 | +314.9 | +285.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 25.0% | -364.3 | 0.07 | 0.22 | +198.2 | +429.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | -149.6 | 0.45 | 1.20 | +408.0 | +361.7 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 30.0% | -135.5 | 0.50 | 1.17 | +443.9 | +349.0 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 28.6% | -130.4 | 0.34 | 0.84 | +393.4 | +446.7 |

### RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=50.0% Avg=-44.2; validation N=5 Fav=20.0% Avg=-436.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -271.9 | 0.21 | 0.57 | +368.6 | +558.3 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -271.9 | 0.21 | 0.57 | +368.6 | +558.3 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -271.9 | 0.21 | 0.57 | +368.6 | +558.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -271.9 | 0.21 | 0.57 | +368.6 | +558.3 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -271.9 | 0.21 | 0.57 | +368.6 | +558.3 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -271.9 | 0.21 | 0.57 | +368.6 | +558.3 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 22.2% | -261.9 | 0.26 | 0.51 | +430.6 | +543.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 16.7% | -273.7 | 0.18 | 0.35 | +487.0 | +628.8 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -271.9 | 0.21 | 0.57 | +368.6 | +558.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 81.8% | 33.3% | 33.3% | 22.2% | -261.9 | 0.26 | 0.51 | +430.6 | +543.3 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -1019.0 | 0.00 | 0.00 | +1071.0 | +1637.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -271.9 | 0.21 | 0.57 | +368.6 | +558.3 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -271.9 | 0.21 | 0.57 | +368.6 | +558.3 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 16.7% | -273.7 | 0.18 | 0.35 | +487.0 | +628.8 |

### STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=40.0% Avg=+493.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +210.7 | 2.35 | 4.70 | +490.3 | +125.7 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +210.7 | 2.35 | 4.70 | +490.3 | +125.7 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +210.7 | 2.35 | 4.70 | +490.3 | +125.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +210.7 | 2.35 | 4.70 | +490.3 | +125.7 |
| `confluence_gte_60` | 9 | S_STRANGER | 60.0% | 11.1% | 11.1% | 0.0% | -20.7 | 0.91 | 7.30 | +322.1 | +145.7 |
| `confluence_gte_70` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 0.0% | +904.5 | 13.56 | 13.56 | +1016.5 | +140.5 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -92.0 | 0.00 | 0.00 | +41.0 | +141.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 46.7% | 28.6% | 28.6% | 28.6% | -68.1 | 0.73 | 1.83 | +279.9 | +65.3 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +210.7 | 2.35 | 4.70 | +490.3 | +125.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -92.0 | 0.00 | 0.00 | +41.0 | +141.0 |
| `feature_fresh_reclaim_within_8` | 4 | S_STRANGER | 26.7% | 0.0% | 25.0% | 25.0% | +152.5 | 2.60 | 7.79 | +334.8 | +141.7 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 26.7% | 33.3% | 26.7% | +210.7 | 2.35 | 4.70 | +490.3 | +125.7 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 66.7% | 40.0% | 50.0% | 40.0% | +493.4 | 9.76 | 9.76 | +692.8 | +148.1 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 46.7% | 28.6% | 28.6% | 28.6% | -68.1 | 0.73 | 1.83 | +279.9 | +65.3 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+274.8; validation N=3 Fav=0.0% Avg=-338.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 26.3% | +14.2 | 1.11 | 2.40 | +264.5 | +198.8 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 73.7% | 28.6% | 35.7% | 35.7% | +27.0 | 1.20 | 2.16 | +273.4 | +206.8 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 89.5% | 23.5% | 29.4% | 29.4% | -6.2 | 0.96 | 2.29 | +246.9 | +211.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 26.3% | +14.2 | 1.11 | 2.40 | +264.5 | +198.8 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 26.3% | +14.2 | 1.11 | 2.40 | +264.5 | +198.8 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 26.3% | +14.2 | 1.11 | 2.40 | +264.5 | +198.8 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 68.4% | 30.8% | 38.5% | 30.8% | +46.2 | 1.31 | 2.09 | +342.1 | +214.7 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 78.9% | 26.7% | 33.3% | 26.7% | +37.9 | 1.29 | 2.57 | +303.5 | +204.7 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 73.7% | 28.6% | 35.7% | 35.7% | +27.0 | 1.20 | 2.16 | +273.4 | +206.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 47.4% | 33.3% | 44.4% | 44.4% | +70.6 | 1.44 | 1.79 | +363.6 | +228.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 26.3% | +14.2 | 1.11 | 2.40 | +264.5 | +198.8 |
| `feature_momentum_breakout_exception` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 26.3% | +14.2 | 1.11 | 2.40 | +264.5 | +198.8 |
| `feature_eurjpy_tdi50_reclaim` | 15 | S_STRANGER | 78.9% | 26.7% | 33.3% | 26.7% | +37.9 | 1.29 | 2.57 | +303.5 | +204.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=14 Fav=28.6% Avg=-99.1; out_of_sample N=3 Fav=33.3% Avg=+28.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 26.3% | 42.1% | 21.1% | -95.7 | 0.59 | 0.81 | +416.1 | +329.4 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 89.5% | 29.4% | 47.1% | 23.5% | -76.6 | 0.67 | 0.75 | +422.8 | +323.4 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 26.3% | 42.1% | 21.1% | -95.7 | 0.59 | 0.81 | +416.1 | +329.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 19 | S_STRANGER | 100.0% | 26.3% | 42.1% | 21.1% | -95.7 | 0.59 | 0.81 | +416.1 | +329.4 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 26.3% | 42.1% | 21.1% | -95.7 | 0.59 | 0.81 | +416.1 | +329.4 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 26.3% | 42.1% | 21.1% | -95.7 | 0.59 | 0.81 | +416.1 | +329.4 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 52.6% | 20.0% | 30.0% | 20.0% | -128.5 | 0.49 | 1.14 | +417.6 | +334.6 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 52.6% | 20.0% | 30.0% | 20.0% | -125.4 | 0.41 | 0.95 | +431.1 | +360.7 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 89.5% | 29.4% | 47.1% | 23.5% | -76.6 | 0.67 | 0.75 | +422.8 | +323.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 42.1% | 25.0% | 37.5% | 25.0% | -96.1 | 0.62 | 1.03 | +432.4 | +323.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 26.3% | 42.1% | 21.1% | -95.7 | 0.59 | 0.81 | +416.1 | +329.4 |
| `feature_momentum_breakout_exception` | 17 | S_STRANGER | 89.5% | 29.4% | 47.1% | 23.5% | -77.8 | 0.67 | 0.75 | +460.0 | +319.6 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 52.6% | 20.0% | 30.0% | 20.0% | -125.4 | 0.41 | 0.95 | +431.1 | +360.7 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=57.1% Avg=+192.2; validation N=5 Fav=20.0% Avg=-232.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 26.3% | 36.8% | 31.6% | -100.4 | 0.53 | 0.83 | +309.9 | +247.0 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 68.4% | 30.8% | 38.5% | 30.8% | -84.8 | 0.61 | 0.98 | +343.4 | +304.0 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 73.7% | 28.6% | 35.7% | 28.6% | -155.0 | 0.45 | 0.80 | +326.9 | +296.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 19 | S_STRANGER | 100.0% | 26.3% | 36.8% | 31.6% | -100.4 | 0.53 | 0.83 | +309.9 | +247.0 |
| `confluence_gte_60` | 12 | S_STRANGER | 63.2% | 41.7% | 50.0% | 41.7% | +15.2 | 1.10 | 1.10 | +389.2 | +283.2 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -121.0 | 0.00 | 0.00 | +174.0 | +181.0 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 84.2% | 31.2% | 37.5% | 31.2% | -87.3 | 0.59 | 0.99 | +320.8 | +208.6 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 42.1% | 12.5% | 25.0% | 12.5% | -82.4 | 0.47 | 1.41 | +309.0 | +280.7 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 68.4% | 30.8% | 38.5% | 30.8% | -84.8 | 0.61 | 0.98 | +343.4 | +304.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 63.2% | 33.3% | 41.7% | 33.3% | -40.7 | 0.78 | 1.09 | +350.8 | +234.7 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 5.3% | 100.0% | 100.0% | 100.0% | +290.0 | 999.00 | 999.00 | +378.0 | +70.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 26.3% | 36.8% | 31.6% | -100.4 | 0.53 | 0.83 | +309.9 | +247.0 |
| `feature_momentum_breakout_exception` | 19 | S_STRANGER | 100.0% | 26.3% | 36.8% | 31.6% | -100.4 | 0.53 | 0.83 | +309.9 | +247.0 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 42.1% | 12.5% | 25.0% | 12.5% | -82.4 | 0.47 | 1.41 | +309.0 | +280.7 |

### THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=16 Fav=31.2% Avg=+108.7; validation N=4 Fav=25.0% Avg=+133.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 30.4% | -15.6 | 0.91 | 2.44 | +366.3 | +245.4 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 82.6% | 26.3% | 26.3% | 31.6% | -45.4 | 0.78 | 2.03 | +349.5 | +227.8 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 87.0% | 25.0% | 25.0% | 30.0% | -47.1 | 0.77 | 2.15 | +353.9 | +234.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 30.4% | -15.6 | 0.91 | 2.44 | +366.3 | +245.4 |
| `confluence_gte_60` | 15 | S_STRANGER | 65.2% | 26.7% | 26.7% | 33.3% | +73.6 | 1.69 | 4.21 | +424.1 | +253.1 |
| `confluence_gte_70` | 1 | R_RUNNER | 4.3% | 100.0% | 100.0% | 100.0% | +900.0 | 999.00 | 999.00 | +1216.0 | +1.0 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 91.3% | 23.8% | 23.8% | 28.6% | -39.5 | 0.80 | 2.40 | +349.6 | +247.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 39.1% | 33.3% | 33.3% | 44.4% | -121.9 | 0.55 | 0.91 | +301.2 | +170.0 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 82.6% | 26.3% | 26.3% | 31.6% | -45.4 | 0.78 | 2.03 | +349.5 | +227.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 73.9% | 23.5% | 23.5% | 29.4% | -78.4 | 0.66 | 1.98 | +326.9 | +228.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 26.1% | 26.1% | 30.4% | -15.6 | 0.91 | 2.44 | +366.3 | +245.4 |
| `feature_momentum_breakout_exception` | 20 | S_STRANGER | 87.0% | 30.0% | 30.0% | 35.0% | +113.5 | 2.44 | 5.28 | +407.8 | +256.6 |
| `feature_eurjpy_tdi50_reclaim` | 9 | S_STRANGER | 39.1% | 33.3% | 33.3% | 44.4% | -121.9 | 0.55 | 0.91 | +301.2 | +170.0 |

### THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+242.5; validation N=5 Fav=40.0% Avg=+1201.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 41.7% | +368.7 | 2.55 | 4.46 | +877.9 | +319.0 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 41.7% | +368.7 | 2.55 | 4.46 | +877.9 | +319.0 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 41.7% | +368.7 | 2.55 | 4.46 | +877.9 | +319.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 41.7% | +368.7 | 2.55 | 4.46 | +877.9 | +319.0 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 41.7% | +368.7 | 2.55 | 4.46 | +877.9 | +319.0 |
| `confluence_gte_70` | 6 | R_REPEATER | 50.0% | 50.0% | 66.7% | 66.7% | +1041.6 | 7.07 | 3.54 | +1610.5 | +349.5 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 14.3% | 28.6% | 42.9% | +272.9 | 2.09 | 4.17 | +756.4 | +307.7 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 42.9% | -186.8 | 0.42 | 0.84 | +349.0 | +200.7 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 41.7% | +368.7 | 2.55 | 4.46 | +877.9 | +319.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 58.3% | 14.3% | 28.6% | 42.9% | +272.9 | 2.09 | 4.17 | +756.4 | +307.7 |
| `feature_fresh_reclaim_within_8` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 33.3% | -224.7 | 0.51 | 1.03 | +479.3 | +324.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 41.7% | +368.7 | 2.55 | 4.46 | +877.9 | +319.0 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 75.0% | 33.3% | 44.4% | 55.6% | +726.5 | 9.84 | 9.84 | +1158.6 | +330.8 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 42.9% | -186.8 | 0.42 | 0.84 | +349.0 | +200.7 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=28.6% Avg=+417.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +246.0 | 1.92 | 5.11 | +1411.2 | +826.3 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +246.0 | 1.92 | 5.11 | +1411.2 | +826.3 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +246.0 | 1.92 | 5.11 | +1411.2 | +826.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +246.0 | 1.92 | 5.11 | +1411.2 | +826.3 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +246.0 | 1.92 | 5.11 | +1411.2 | +826.3 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +246.0 | 1.92 | 5.11 | +1411.2 | +826.3 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 14.3% | +417.4 | 2.97 | 5.94 | +1502.0 | +864.7 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 25.0% | -323.5 | 0.00 | 0.00 | +896.0 | +1076.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +246.0 | 1.92 | 5.11 | +1411.2 | +826.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 58.3% | 28.6% | 28.6% | 14.3% | +417.4 | 2.97 | 5.94 | +1502.0 | +864.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +246.0 | 1.92 | 5.11 | +1411.2 | +826.3 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | +246.0 | 1.92 | 5.11 | +1411.2 | +826.3 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 25.0% | -323.5 | 0.00 | 0.00 | +896.0 | +1076.0 |

### STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=25.0% Avg=+13.0; validation N=2 Fav=50.0% Avg=+1233.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | +200.2 | 2.02 | 4.05 | +869.1 | +308.1 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | +200.2 | 2.02 | 4.05 | +869.1 | +308.1 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | +200.2 | 2.02 | 4.05 | +869.1 | +308.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | +200.2 | 2.02 | 4.05 | +869.1 | +308.1 |
| `confluence_gte_60` | 11 | S_STRANGER | 91.7% | 18.2% | 27.3% | 9.1% | -13.7 | 0.94 | 2.49 | +646.5 | +315.6 |
| `confluence_gte_70` | 2 | S_STRANGER | 16.7% | 0.0% | 50.0% | 0.0% | +210.5 | 5.84 | 5.84 | +592.0 | +208.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 75.0% | 22.2% | 33.3% | 22.2% | +276.7 | 2.51 | 5.02 | +974.6 | +341.2 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -677.0 | 0.00 | 0.00 | +107.0 | +234.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | +200.2 | 2.02 | 4.05 | +869.1 | +308.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 75.0% | 22.2% | 33.3% | 22.2% | +276.7 | 2.51 | 5.02 | +974.6 | +341.2 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -677.0 | 0.00 | 0.00 | +107.0 | +234.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | +200.2 | 2.02 | 4.05 | +869.1 | +308.1 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 83.3% | 30.0% | 30.0% | 20.0% | +257.1 | 2.54 | 5.93 | +978.2 | +337.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -677.0 | 0.00 | 0.00 | +107.0 | +234.0 |

### THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+469.5; validation N=1 Fav=0.0% Avg=-337.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 41.7% | +46.7 | 1.22 | 2.14 | +561.4 | +298.4 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 91.7% | 18.2% | 27.3% | 36.4% | -36.3 | 0.84 | 1.96 | +474.0 | +316.1 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 18.2% | 27.3% | 36.4% | -36.3 | 0.84 | 1.96 | +474.0 | +316.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 41.7% | +46.7 | 1.22 | 2.14 | +561.4 | +298.4 |
| `confluence_gte_60` | 6 | S_STRANGER | 50.0% | 33.3% | 50.0% | 50.0% | +295.8 | 2.78 | 2.78 | +832.5 | +225.2 |
| `confluence_gte_70` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -279.0 | 0.00 | 0.00 | +136.0 | +367.0 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 33.3% | 50.0% | 75.0% | 75.0% | +666.5 | 26.39 | 8.80 | +1073.5 | +85.5 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 42.9% | 57.1% | 57.1% | +354.3 | 5.28 | 3.96 | +740.6 | +162.6 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 91.7% | 18.2% | 27.3% | 36.4% | -36.3 | 0.84 | 1.96 | +474.0 | +316.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 25.0% | 33.3% | 66.7% | 66.7% | +569.0 | 17.26 | 8.63 | +923.7 | +79.3 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -105.0 | 0.00 | 0.00 | +44.0 | +238.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 41.7% | +46.7 | 1.22 | 2.14 | +561.4 | +298.4 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 41.7% | +46.7 | 1.22 | 2.14 | +561.4 | +298.4 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 58.3% | 42.9% | 57.1% | 57.1% | +354.3 | 5.28 | 3.96 | +740.6 | +162.6 |

### RRT_REVERSAL|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|SELL|EARLY_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=11 Fav=27.3% Avg=+65.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 25.0% | +41.4 | 1.35 | 2.71 | +350.3 | +196.4 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 20.0% | 30.0% | 20.0% | +21.5 | 1.16 | 2.71 | +366.4 | +200.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 91.7% | 18.2% | 27.3% | 18.2% | +12.6 | 1.10 | 2.93 | +344.4 | +196.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 25.0% | +41.4 | 1.35 | 2.71 | +350.3 | +196.4 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 25.0% | +41.4 | 1.35 | 2.71 | +350.3 | +196.4 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 25.0% | +41.4 | 1.35 | 2.71 | +350.3 | +196.4 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 91.7% | 27.3% | 36.4% | 27.3% | +65.5 | 1.61 | 2.82 | +377.8 | +185.2 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -516.0 | 0.00 | 0.00 | +0.0 | +534.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 83.3% | 20.0% | 30.0% | 20.0% | +21.5 | 1.16 | 2.71 | +366.4 | +200.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 75.0% | 22.2% | 33.3% | 22.2% | +48.7 | 1.40 | 2.79 | +401.8 | +187.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 25.0% | +41.4 | 1.35 | 2.71 | +350.3 | +196.4 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 25.0% | +41.4 | 1.35 | 2.71 | +350.3 | +196.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -516.0 | 0.00 | 0.00 | +0.0 | +534.0 |

### RRT_REVERSAL|BUY|EARLY_WEEK|L0|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|BUY|EARLY_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=33.3% Avg=-62.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -62.5 | 0.52 | 1.57 | +232.5 | +160.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 75.0% | 33.3% | 33.3% | 22.2% | -62.9 | 0.59 | 1.18 | +249.2 | +167.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 83.3% | 30.0% | 30.0% | 20.0% | -59.6 | 0.58 | 1.35 | +232.3 | +157.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -62.5 | 0.52 | 1.57 | +232.5 | +160.4 |
| `confluence_gte_60` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 33.3% | -32.8 | 0.70 | 1.40 | +298.7 | +194.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | +36.0 | 1.36 | 1.36 | +259.5 | +167.0 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 0.0% | +11.7 | 1.12 | 2.25 | +486.0 | +218.0 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 75.0% | 33.3% | 33.3% | 22.2% | -62.9 | 0.59 | 1.18 | +249.2 | +167.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 50.0% | +36.0 | 1.36 | 1.36 | +259.5 | +167.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 16.7% | -62.5 | 0.52 | 1.57 | +232.5 | +160.4 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 91.7% | 27.3% | 27.3% | 18.2% | -43.8 | 0.63 | 1.68 | +193.3 | +147.3 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 0.0% | +11.7 | 1.12 | 2.25 | +486.0 | +218.0 |

### STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=14 Fav=42.9% Avg=+38.0; out_of_sample N=3 Fav=0.0% Avg=-227.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 44 | S_STRANGER | 100.0% | 25.0% | 29.5% | 20.5% | -157.8 | 0.41 | 0.88 | +405.1 | +374.0 |
| `hunt_to_ar_ratio_le_2_0` | 32 | S_STRANGER | 72.7% | 28.1% | 34.4% | 18.8% | -100.2 | 0.58 | 1.00 | +479.1 | +342.7 |
| `hunt_to_ar_ratio_le_2_5` | 33 | S_STRANGER | 75.0% | 27.3% | 33.3% | 18.2% | -111.7 | 0.55 | 0.99 | +468.8 | +335.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 44 | S_STRANGER | 100.0% | 25.0% | 29.5% | 20.5% | -157.8 | 0.41 | 0.88 | +405.1 | +374.0 |
| `confluence_gte_60` | 27 | S_STRANGER | 61.4% | 29.6% | 29.6% | 22.2% | -130.2 | 0.53 | 1.12 | +368.7 | +422.7 |
| `confluence_gte_70` | 4 | S_STRANGER | 9.1% | 25.0% | 25.0% | 50.0% | -152.5 | 0.37 | 0.74 | +351.0 | +513.8 |
| `tdi_rsi_gt_signal` | 26 | S_STRANGER | 59.1% | 30.8% | 30.8% | 26.9% | -82.4 | 0.64 | 1.28 | +383.9 | +399.1 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 54.5% | 33.3% | 37.5% | 29.2% | -115.3 | 0.57 | 0.82 | +409.5 | +320.1 |
| `ratio_le_2_and_asian_gte_30` | 32 | S_STRANGER | 72.7% | 28.1% | 34.4% | 18.8% | -100.2 | 0.58 | 1.00 | +479.1 | +342.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 38.6% | 35.3% | 35.3% | 23.5% | -8.8 | 0.96 | 1.60 | +458.5 | +373.2 |
| `feature_fresh_reclaim_within_8` | 3 | S_STRANGER | 6.8% | 0.0% | 33.3% | 0.0% | -540.3 | 0.01 | 0.02 | +223.3 | +157.3 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 44 | S_STRANGER | 100.0% | 25.0% | 29.5% | 20.5% | -157.8 | 0.41 | 0.88 | +405.1 | +374.0 |
| `feature_momentum_breakout_exception` | 35 | S_STRANGER | 79.5% | 31.4% | 31.4% | 25.7% | -74.5 | 0.64 | 1.22 | +473.3 | +425.7 |
| `feature_eurjpy_tdi50_reclaim` | 23 | S_STRANGER | 52.3% | 30.4% | 34.8% | 30.4% | -170.7 | 0.38 | 0.62 | +373.6 | +322.5 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=+1.5; validation N=4 Fav=50.0% Avg=+13.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -193.4 | 0.42 | 0.73 | +448.8 | +438.8 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -193.4 | 0.42 | 0.73 | +448.8 | +438.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -193.4 | 0.42 | 0.73 | +448.8 | +438.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -193.4 | 0.42 | 0.73 | +448.8 | +438.8 |
| `confluence_gte_60` | 5 | S_STRANGER | 41.7% | 20.0% | 40.0% | 0.0% | -192.8 | 0.60 | 0.89 | +527.0 | +266.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 14.3% | 28.6% | 0.0% | -372.3 | 0.10 | 0.25 | +424.0 | +581.3 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 66.7% | 12.5% | 25.0% | 25.0% | -316.9 | 0.12 | 0.29 | +232.3 | +408.9 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -193.4 | 0.42 | 0.73 | +448.8 | +438.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 58.3% | 14.3% | 28.6% | 0.0% | -372.3 | 0.10 | 0.25 | +424.0 | +581.3 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -1567.0 | 0.00 | 0.00 | +322.0 | +165.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 33.3% | 16.7% | -193.4 | 0.42 | 0.73 | +448.8 | +438.8 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 83.3% | 30.0% | 40.0% | 20.0% | +6.1 | 1.04 | 1.30 | +503.3 | +465.4 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 66.7% | 12.5% | 25.0% | 25.0% | -316.9 | 0.12 | 0.29 | +232.3 | +408.9 |

### STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-35.0; validation N=18 Fav=44.4% Avg=+43.2; out_of_sample N=2 Fav=0.0% Avg=-1937.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | S_STRANGER | 100.0% | 24.2% | 30.3% | 21.2% | -534.4 | 0.23 | 0.47 | +433.8 | +483.3 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 69.7% | 21.7% | 30.4% | 13.0% | -682.7 | 0.18 | 0.38 | +396.2 | +516.4 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 72.7% | 20.8% | 29.2% | 12.5% | -697.7 | 0.17 | 0.39 | +385.5 | +513.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 33 | S_STRANGER | 100.0% | 24.2% | 30.3% | 21.2% | -534.4 | 0.23 | 0.47 | +433.8 | +483.3 |
| `confluence_gte_60` | 17 | S_STRANGER | 51.5% | 29.4% | 29.4% | 23.5% | -119.4 | 0.66 | 1.45 | +573.0 | +463.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 12.1% | 0.0% | 25.0% | 0.0% | -1049.5 | 0.01 | 0.04 | +127.5 | +262.0 |
| `tdi_rsi_gte_50` | 21 | S_STRANGER | 63.6% | 14.3% | 23.8% | 19.0% | -692.3 | 0.10 | 0.30 | +270.2 | +249.7 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 69.7% | 21.7% | 30.4% | 13.0% | -682.7 | 0.18 | 0.38 | +396.2 | +516.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 9.1% | 0.0% | 33.3% | 0.0% | -1357.7 | 0.01 | 0.02 | +134.0 | +169.3 |
| `feature_fresh_reclaim_within_8` | 13 | S_STRANGER | 39.4% | 7.7% | 23.1% | 15.4% | -846.1 | 0.05 | 0.15 | +265.9 | +217.7 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 33 | S_STRANGER | 100.0% | 24.2% | 30.3% | 21.2% | -534.4 | 0.23 | 0.47 | +433.8 | +483.3 |
| `feature_momentum_breakout_exception` | 21 | S_STRANGER | 63.6% | 38.1% | 38.1% | 33.3% | -149.1 | 0.61 | 0.84 | +580.0 | +636.0 |
| `feature_eurjpy_tdi50_reclaim` | 21 | S_STRANGER | 63.6% | 14.3% | 23.8% | 19.0% | -692.3 | 0.10 | 0.30 | +270.2 | +249.7 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=-488.3; out_of_sample N=3 Fav=33.3% Avg=+1798.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 24.1% | 27.6% | 20.7% | +98.9 | 1.30 | 3.26 | +821.3 | +578.9 |
| `hunt_to_ar_ratio_le_2_0` | 27 | S_STRANGER | 93.1% | 25.9% | 29.6% | 22.2% | +125.1 | 1.38 | 3.10 | +836.3 | +536.2 |
| `hunt_to_ar_ratio_le_2_5` | 28 | S_STRANGER | 96.6% | 25.0% | 28.6% | 21.4% | +103.3 | 1.31 | 3.11 | +815.2 | +560.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 29 | S_STRANGER | 100.0% | 24.1% | 27.6% | 20.7% | +98.9 | 1.30 | 3.26 | +821.3 | +578.9 |
| `confluence_gte_60` | 10 | S_STRANGER | 34.5% | 30.0% | 30.0% | 10.0% | +46.3 | 1.11 | 2.59 | +959.8 | +635.1 |
| `confluence_gte_70` | 3 | S_STRANGER | 10.3% | 33.3% | 33.3% | 33.3% | +415.0 | 2.19 | 4.38 | +1190.3 | +553.0 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 69.0% | 25.0% | 30.0% | 25.0% | +95.2 | 1.28 | 2.78 | +764.5 | +542.1 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 27.6% | 37.5% | 50.0% | 37.5% | +369.1 | 1.90 | 1.90 | +1003.5 | +705.7 |
| `ratio_le_2_and_asian_gte_30` | 27 | S_STRANGER | 93.1% | 25.9% | 29.6% | 22.2% | +125.1 | 1.38 | 3.10 | +836.3 | +536.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 19 | S_STRANGER | 65.5% | 26.3% | 31.6% | 26.3% | +125.8 | 1.38 | 2.77 | +791.7 | +507.2 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 3.4% | 0.0% | 0.0% | 0.0% | -372.0 | 0.00 | 0.00 | +149.0 | +181.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 24.1% | 27.6% | 20.7% | +98.9 | 1.30 | 3.26 | +821.3 | +578.9 |
| `feature_momentum_breakout_exception` | 26 | S_STRANGER | 89.7% | 26.9% | 30.8% | 23.1% | +217.4 | 1.85 | 3.94 | +908.5 | +550.7 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 27.6% | 37.5% | 50.0% | 37.5% | +369.1 | 1.90 | 1.90 | +1003.5 | +705.7 |

### STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=25.0% Avg=+20.0; validation N=10 Fav=30.0% Avg=+322.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +82.6 | 1.72 | 3.72 | +605.0 | +364.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 66.7% | 28.6% | 35.7% | 7.1% | +235.9 | 6.44 | 9.02 | +714.4 | +333.9 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 66.7% | 28.6% | 35.7% | 7.1% | +235.9 | 6.44 | 9.02 | +714.4 | +333.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +82.6 | 1.72 | 3.72 | +605.0 | +364.7 |
| `confluence_gte_60` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +82.6 | 1.72 | 3.72 | +605.0 | +364.7 |
| `confluence_gte_70` | 21 | S_STRANGER | 100.0% | 23.8% | 28.6% | 9.5% | +82.6 | 1.72 | 3.72 | +605.0 | +364.7 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 23.8% | 20.0% | 20.0% | 20.0% | -158.4 | 0.23 | 0.94 | +430.4 | +371.6 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 85.7% | 16.7% | 16.7% | 11.1% | -29.2 | 0.78 | 3.39 | +488.6 | +339.7 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 66.7% | 28.6% | 35.7% | 7.1% | +235.9 | 6.44 | 9.02 | +714.4 | +333.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -287.0 | 0.00 | 0.00 | +232.0 | +382.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 81.0% | 23.5% | 29.4% | 5.9% | +131.7 | 2.34 | 4.68 | +634.5 | +363.7 |
| `feature_momentum_breakout_exception` | 20 | S_STRANGER | 95.2% | 25.0% | 30.0% | 10.0% | +89.7 | 1.76 | 3.52 | +611.8 | +374.5 |
| `feature_eurjpy_tdi50_reclaim` | 18 | S_STRANGER | 85.7% | 16.7% | 16.7% | 11.1% | -29.2 | 0.78 | 3.39 | +488.6 | +339.7 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=24 Fav=33.3% Avg=+189.7; out_of_sample N=7 Fav=28.6% Avg=-79.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 42 | S_STRANGER | 100.0% | 23.8% | 31.0% | 21.4% | -33.0 | 0.90 | 1.94 | +619.9 | +411.7 |
| `hunt_to_ar_ratio_le_2_0` | 41 | S_STRANGER | 97.6% | 24.4% | 31.7% | 22.0% | -25.7 | 0.92 | 1.91 | +630.2 | +401.1 |
| `hunt_to_ar_ratio_le_2_5` | 41 | S_STRANGER | 97.6% | 24.4% | 31.7% | 22.0% | -25.7 | 0.92 | 1.91 | +630.2 | +401.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 42 | S_STRANGER | 100.0% | 23.8% | 31.0% | 21.4% | -33.0 | 0.90 | 1.94 | +619.9 | +411.7 |
| `confluence_gte_60` | 42 | S_STRANGER | 100.0% | 23.8% | 31.0% | 21.4% | -33.0 | 0.90 | 1.94 | +619.9 | +411.7 |
| `confluence_gte_70` | 2 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -312.5 | 0.00 | 0.00 | +246.5 | +263.0 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 31.0% | 15.4% | 15.4% | 15.4% | -165.0 | 0.38 | 1.88 | +342.8 | +357.5 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 57.1% | 16.7% | 25.0% | 20.8% | -159.8 | 0.50 | 1.41 | +385.2 | +277.7 |
| `ratio_le_2_and_asian_gte_30` | 41 | S_STRANGER | 97.6% | 24.4% | 31.7% | 22.0% | -25.7 | 0.92 | 1.91 | +630.2 | +401.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 31.0% | 15.4% | 15.4% | 15.4% | -165.0 | 0.38 | 1.88 | +342.8 | +357.5 |
| `feature_fresh_reclaim_within_8` | 6 | S_STRANGER | 14.3% | 16.7% | 50.0% | 16.7% | +59.4 | 1.29 | 1.29 | +472.7 | +176.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 42 | S_STRANGER | 100.0% | 23.8% | 31.0% | 21.4% | -33.0 | 0.90 | 1.94 | +619.9 | +411.7 |
| `feature_momentum_breakout_exception` | 31 | S_STRANGER | 73.8% | 32.3% | 35.5% | 29.0% | +128.9 | 1.56 | 2.69 | +715.1 | +489.1 |
| `feature_eurjpy_tdi50_reclaim` | 24 | S_STRANGER | 57.1% | 16.7% | 25.0% | 20.8% | -159.8 | 0.50 | 1.41 | +385.2 | +277.7 |

### STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|EARLY_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+94.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 23.5% | 29.4% | 23.5% | -62.0 | 0.51 | 1.23 | +178.8 | +139.8 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 82.4% | 21.4% | 28.6% | 21.4% | -67.6 | 0.45 | 1.13 | +153.1 | +143.1 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 88.2% | 20.0% | 26.7% | 20.0% | -89.3 | 0.37 | 1.01 | +147.9 | +137.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 23.5% | 29.4% | 23.5% | -62.0 | 0.51 | 1.23 | +178.8 | +139.8 |
| `confluence_gte_60` | 16 | S_STRANGER | 94.1% | 18.8% | 25.0% | 18.8% | -70.8 | 0.47 | 1.42 | +182.3 | +147.6 |
| `confluence_gte_70` | 9 | S_STRANGER | 52.9% | 33.3% | 33.3% | 33.3% | -51.9 | 0.66 | 1.33 | +246.2 | +131.4 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 70.6% | 16.7% | 25.0% | 16.7% | -98.8 | 0.30 | 0.89 | +138.6 | +111.7 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 76.5% | 30.8% | 38.5% | 30.8% | -37.7 | 0.69 | 1.11 | +198.2 | +114.0 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 82.4% | 21.4% | 28.6% | 21.4% | -67.6 | 0.45 | 1.13 | +153.1 | +143.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 52.9% | 11.1% | 22.2% | 11.1% | -119.8 | 0.14 | 0.50 | +85.2 | +107.3 |
| `feature_fresh_reclaim_within_8` | 6 | R_REPEATER | 35.3% | 50.0% | 66.7% | 50.0% | +94.2 | 3.60 | 1.80 | +215.2 | +73.8 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 23.5% | 29.4% | 23.5% | -62.0 | 0.51 | 1.23 | +178.8 | +139.8 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 64.7% | 36.4% | 36.4% | 36.4% | +13.2 | 1.17 | 2.05 | +224.4 | +171.7 |
| `feature_eurjpy_tdi50_reclaim` | 13 | S_STRANGER | 76.5% | 30.8% | 38.5% | 30.8% | -37.7 | 0.69 | 1.11 | +198.2 | +114.0 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=22 Fav=27.3% Avg=+20.7; out_of_sample N=2 Fav=50.0% Avg=+82.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 30.0% | -168.5 | 0.54 | 1.29 | +482.2 | +393.3 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 30.0% | -168.5 | 0.54 | 1.29 | +482.2 | +393.3 |
| `hunt_to_ar_ratio_le_2_5` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 30.0% | -168.5 | 0.54 | 1.29 | +482.2 | +393.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 30.0% | -168.5 | 0.54 | 1.29 | +482.2 | +393.3 |
| `confluence_gte_60` | 21 | S_STRANGER | 70.0% | 19.0% | 23.8% | 23.8% | -361.4 | 0.25 | 0.71 | +415.5 | +446.7 |
| `confluence_gte_70` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -736.0 | 0.00 | 0.00 | +507.0 | +736.0 |
| `tdi_rsi_gt_signal` | 28 | S_STRANGER | 93.3% | 21.4% | 25.0% | 25.0% | -265.4 | 0.33 | 0.89 | +393.6 | +410.1 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 43.3% | 15.4% | 15.4% | 23.1% | -465.9 | 0.11 | 0.55 | +253.6 | +305.5 |
| `ratio_le_2_and_asian_gte_30` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 30.0% | -168.5 | 0.54 | 1.29 | +482.2 | +393.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 28 | S_STRANGER | 93.3% | 21.4% | 25.0% | 25.0% | -265.4 | 0.33 | 0.89 | +393.6 | +410.1 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -197.0 | 0.00 | 0.00 | +175.0 | +509.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 30.0% | -168.5 | 0.54 | 1.29 | +482.2 | +393.3 |
| `feature_momentum_breakout_exception` | 24 | S_STRANGER | 80.0% | 29.2% | 29.2% | 37.5% | +25.8 | 1.12 | 2.24 | +548.5 | +439.2 |
| `feature_eurjpy_tdi50_reclaim` | 13 | S_STRANGER | 43.3% | 15.4% | 15.4% | 23.1% | -465.9 | 0.11 | 0.55 | +253.6 | +305.5 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=32 Fav=34.4% Avg=+263.0; out_of_sample N=4 Fav=50.0% Avg=+359.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 65 | S_STRANGER | 100.0% | 23.1% | 30.8% | 21.5% | -166.4 | 0.75 | 1.68 | +1017.2 | +734.1 |
| `hunt_to_ar_ratio_le_2_0` | 62 | S_STRANGER | 95.4% | 21.0% | 29.0% | 19.4% | -297.2 | 0.56 | 1.36 | +900.0 | +744.5 |
| `hunt_to_ar_ratio_le_2_5` | 64 | S_STRANGER | 98.5% | 21.9% | 29.7% | 20.3% | -274.0 | 0.59 | 1.39 | +923.3 | +742.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 65 | S_STRANGER | 100.0% | 23.1% | 30.8% | 21.5% | -166.4 | 0.75 | 1.68 | +1017.2 | +734.1 |
| `confluence_gte_60` | 25 | S_STRANGER | 38.5% | 20.0% | 36.0% | 16.0% | +187.8 | 1.35 | 2.39 | +1282.3 | +538.8 |
| `confluence_gte_70` | 12 | S_STRANGER | 18.5% | 25.0% | 50.0% | 16.7% | +490.6 | 2.44 | 2.44 | +1506.1 | +396.4 |
| `tdi_rsi_gt_signal` | 36 | S_STRANGER | 55.4% | 36.1% | 50.0% | 33.3% | +273.7 | 1.72 | 1.72 | +1192.6 | +528.7 |
| `tdi_rsi_gte_50` | 27 | S_STRANGER | 41.5% | 25.9% | 44.4% | 29.6% | -33.9 | 0.93 | 1.16 | +902.9 | +438.6 |
| `ratio_le_2_and_asian_gte_30` | 62 | S_STRANGER | 95.4% | 21.0% | 29.0% | 19.4% | -297.2 | 0.56 | 1.36 | +900.0 | +744.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 35 | S_STRANGER | 53.8% | 34.3% | 48.6% | 31.4% | +223.5 | 1.57 | 1.67 | +1150.6 | +542.5 |
| `feature_fresh_reclaim_within_8` | 6 | S_STRANGER | 9.2% | 0.0% | 33.3% | 16.7% | -469.5 | 0.38 | 0.76 | +698.5 | +460.2 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 65 | S_STRANGER | 100.0% | 23.1% | 30.8% | 21.5% | -166.4 | 0.75 | 1.68 | +1017.2 | +734.1 |
| `feature_momentum_breakout_exception` | 54 | S_STRANGER | 83.1% | 27.8% | 33.3% | 25.9% | -4.5 | 0.99 | 1.98 | +1138.8 | +829.0 |
| `feature_eurjpy_tdi50_reclaim` | 27 | S_STRANGER | 41.5% | 25.9% | 44.4% | 29.6% | -33.9 | 0.93 | 1.16 | +902.9 | +438.6 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=0.0% Avg=-1522.0; out_of_sample N=3 Fav=66.7% Avg=+459.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -378.0 | 0.46 | 1.53 | +1004.5 | +997.2 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -378.0 | 0.46 | 1.53 | +1004.5 | +997.2 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -378.0 | 0.46 | 1.53 | +1004.5 | +997.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -378.0 | 0.46 | 1.53 | +1004.5 | +997.2 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -378.0 | 0.46 | 1.53 | +1004.5 | +997.2 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -378.0 | 0.46 | 1.53 | +1004.5 | +997.2 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 0.0% | -171.5 | 0.65 | 0.65 | +1708.5 | +1058.5 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 92.3% | 25.0% | 25.0% | 8.3% | -63.7 | 0.85 | 2.54 | +1078.7 | +1052.6 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -378.0 | 0.46 | 1.53 | +1004.5 | +997.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 0.0% | -171.5 | 0.65 | 0.65 | +1708.5 | +1058.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 7.7% | -378.0 | 0.46 | 1.53 | +1004.5 | +997.2 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 53.8% | 28.6% | 28.6% | 14.3% | -672.7 | 0.28 | 0.71 | +750.4 | +961.6 |
| `feature_eurjpy_tdi50_reclaim` | 12 | S_STRANGER | 92.3% | 25.0% | 25.0% | 8.3% | -63.7 | 0.85 | 2.54 | +1078.7 | +1052.6 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=-48.3; validation N=8 Fav=25.0% Avg=-58.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 29.0% | -70.1 | 0.52 | 1.47 | +244.5 | +205.2 |
| `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 80.6% | 24.0% | 24.0% | 32.0% | -86.5 | 0.42 | 1.06 | +246.6 | +207.8 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 87.1% | 22.2% | 22.2% | 29.6% | -94.1 | 0.38 | 1.09 | +231.5 | +211.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 29.0% | -70.1 | 0.52 | 1.47 | +244.5 | +205.2 |
| `confluence_gte_60` | 15 | S_STRANGER | 48.4% | 26.7% | 26.7% | 20.0% | -53.5 | 0.71 | 1.76 | +279.9 | +221.4 |
| `confluence_gte_70` | 3 | S_STRANGER | 9.7% | 33.3% | 33.3% | 33.3% | -2.0 | 0.99 | 1.98 | +300.0 | +310.0 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 51.6% | 18.8% | 18.8% | 25.0% | -67.7 | 0.52 | 1.92 | +303.9 | +185.6 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 54.8% | 17.6% | 17.6% | 23.5% | -48.9 | 0.62 | 2.28 | +262.5 | +203.8 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 80.6% | 24.0% | 24.0% | 32.0% | -86.5 | 0.42 | 1.06 | +246.6 | +207.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 45.2% | 14.3% | 14.3% | 21.4% | -117.8 | 0.22 | 1.08 | +279.8 | +188.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 22.6% | 22.6% | 29.0% | -70.1 | 0.52 | 1.47 | +244.5 | +205.2 |
| `feature_momentum_breakout_exception` | 28 | S_STRANGER | 90.3% | 25.0% | 25.0% | 32.1% | -69.7 | 0.54 | 1.32 | +239.7 | +208.6 |
| `feature_eurjpy_tdi50_reclaim` | 17 | S_STRANGER | 54.8% | 17.6% | 17.6% | 23.5% | -48.9 | 0.62 | 2.28 | +262.5 | +203.8 |

### STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=20.0% Avg=+289.2; out_of_sample N=2 Fav=0.0% Avg=-405.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 22.6% | 25.8% | 16.1% | -318.5 | 0.31 | 0.82 | +556.4 | +676.4 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 83.9% | 23.1% | 26.9% | 15.4% | -227.8 | 0.42 | 1.02 | +604.5 | +602.6 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 87.1% | 22.2% | 25.9% | 14.8% | -318.0 | 0.33 | 0.86 | +607.4 | +679.6 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 31 | S_STRANGER | 100.0% | 22.6% | 25.8% | 16.1% | -318.5 | 0.31 | 0.82 | +556.4 | +676.4 |
| `confluence_gte_60` | 19 | S_STRANGER | 61.3% | 26.3% | 31.6% | 15.8% | -409.1 | 0.26 | 0.53 | +597.8 | +802.2 |
| `confluence_gte_70` | 1 | S_STRANGER | 3.2% | 0.0% | 0.0% | 0.0% | -1136.0 | 0.00 | 0.00 | +229.0 | +1920.0 |
| `tdi_rsi_gt_signal` | 24 | S_STRANGER | 77.4% | 25.0% | 29.2% | 16.7% | -178.3 | 0.46 | 0.99 | +563.7 | +551.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 22.6% | 14.3% | 28.6% | 28.6% | +90.7 | 1.70 | 3.40 | +574.9 | +224.9 |
| `ratio_le_2_and_asian_gte_30` | 26 | S_STRANGER | 83.9% | 23.1% | 26.9% | 15.4% | -227.8 | 0.42 | 1.02 | +604.5 | +602.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 20 | S_STRANGER | 64.5% | 25.0% | 30.0% | 15.0% | -149.6 | 0.54 | 1.08 | +633.9 | +531.2 |
| `feature_fresh_reclaim_within_8` | 3 | S_STRANGER | 9.7% | 0.0% | 33.3% | 0.0% | -237.7 | 0.23 | 0.46 | +224.0 | +112.7 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 22.6% | 25.8% | 16.1% | -318.5 | 0.31 | 0.82 | +556.4 | +676.4 |
| `feature_momentum_breakout_exception` | 28 | S_STRANGER | 90.3% | 25.0% | 28.6% | 17.9% | -316.6 | 0.34 | 0.75 | +601.4 | +735.4 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 22.6% | 14.3% | 28.6% | 28.6% | +90.7 | 1.70 | 3.40 | +574.9 | +224.9 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=18 Fav=38.9% Avg=-87.4; validation N=18 Fav=22.2% Avg=-81.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 54 | S_STRANGER | 100.0% | 22.2% | 27.8% | 22.2% | -319.9 | 0.25 | 0.63 | +276.3 | +289.0 |
| `hunt_to_ar_ratio_le_2_0` | 50 | S_STRANGER | 92.6% | 22.0% | 28.0% | 20.0% | -336.5 | 0.25 | 0.65 | +288.8 | +283.3 |
| `hunt_to_ar_ratio_le_2_5` | 52 | S_STRANGER | 96.3% | 23.1% | 28.8% | 21.2% | -325.4 | 0.25 | 0.62 | +282.1 | +281.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 54 | S_STRANGER | 100.0% | 22.2% | 27.8% | 22.2% | -319.9 | 0.25 | 0.63 | +276.3 | +289.0 |
| `confluence_gte_60` | 34 | S_STRANGER | 63.0% | 20.6% | 29.4% | 23.5% | -405.5 | 0.24 | 0.54 | +309.1 | +240.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 22 | S_STRANGER | 40.7% | 27.3% | 31.8% | 27.3% | -256.0 | 0.36 | 0.77 | +293.4 | +310.7 |
| `tdi_rsi_gte_50` | 36 | S_STRANGER | 66.7% | 27.8% | 36.1% | 30.6% | -311.8 | 0.29 | 0.50 | +266.5 | +164.4 |
| `ratio_le_2_and_asian_gte_30` | 50 | S_STRANGER | 92.6% | 22.0% | 28.0% | 20.0% | -336.5 | 0.25 | 0.65 | +288.8 | +283.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 19 | S_STRANGER | 35.2% | 26.3% | 31.6% | 26.3% | -273.0 | 0.37 | 0.81 | +321.4 | +286.3 |
| `feature_fresh_reclaim_within_8` | 12 | S_STRANGER | 22.2% | 25.0% | 41.7% | 25.0% | -292.6 | 0.26 | 0.36 | +245.4 | +256.6 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 54 | S_STRANGER | 100.0% | 22.2% | 27.8% | 22.2% | -319.9 | 0.25 | 0.63 | +276.3 | +289.0 |
| `feature_momentum_breakout_exception` | 36 | S_STRANGER | 66.7% | 30.6% | 33.3% | 30.6% | -84.2 | 0.63 | 1.22 | +322.7 | +375.4 |
| `feature_eurjpy_tdi50_reclaim` | 36 | S_STRANGER | 66.7% | 27.8% | 36.1% | 30.6% | -311.8 | 0.29 | 0.50 | +266.5 | +164.4 |

### STOP_HUNT|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-334.0; validation N=9 Fav=33.3% Avg=+527.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 21.7% | 34.8% | 26.1% | +124.2 | 1.41 | 2.47 | +570.5 | +395.9 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 100.0% | 21.7% | 34.8% | 26.1% | +124.2 | 1.41 | 2.47 | +570.5 | +395.9 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 21.7% | 34.8% | 26.1% | +124.2 | 1.41 | 2.47 | +570.5 | +395.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 23 | S_STRANGER | 100.0% | 21.7% | 34.8% | 26.1% | +124.2 | 1.41 | 2.47 | +570.5 | +395.9 |
| `confluence_gte_60` | 20 | S_STRANGER | 87.0% | 25.0% | 30.0% | 20.0% | +26.1 | 1.08 | 2.51 | +529.7 | +437.6 |
| `confluence_gte_70` | 3 | S_STRANGER | 13.0% | 0.0% | 0.0% | 0.0% | -495.7 | 0.00 | 0.00 | +77.3 | +880.0 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 43.5% | 20.0% | 30.0% | 30.0% | +513.5 | 2.68 | 6.25 | +950.3 | +242.3 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 56.5% | 23.1% | 30.8% | 15.4% | +242.9 | 1.87 | 4.20 | +684.8 | +549.8 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 100.0% | 21.7% | 34.8% | 26.1% | +124.2 | 1.41 | 2.47 | +570.5 | +395.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 43.5% | 20.0% | 30.0% | 30.0% | +513.5 | 2.68 | 6.25 | +950.3 | +242.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 21.7% | 34.8% | 26.1% | +124.2 | 1.41 | 2.47 | +570.5 | +395.9 |
| `feature_momentum_breakout_exception` | 21 | S_STRANGER | 91.3% | 23.8% | 38.1% | 28.6% | +162.3 | 1.53 | 2.30 | +606.7 | +399.5 |
| `feature_eurjpy_tdi50_reclaim` | 12 | S_STRANGER | 52.2% | 25.0% | 33.3% | 16.7% | +312.1 | 2.22 | 4.45 | +729.3 | +585.7 |

### THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=50.0% Avg=+167.1; validation N=8 Fav=12.5% Avg=-7.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 21.6% | 27.0% | 40.5% | -54.4 | 0.71 | 1.50 | +290.9 | +275.4 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 70.3% | 19.2% | 26.9% | 42.3% | -3.3 | 0.98 | 1.96 | +311.1 | +255.8 |
| `hunt_to_ar_ratio_le_2_5` | 30 | S_STRANGER | 81.1% | 23.3% | 30.0% | 43.3% | -9.3 | 0.94 | 1.68 | +313.1 | +242.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 37 | S_STRANGER | 100.0% | 21.6% | 27.0% | 40.5% | -54.4 | 0.71 | 1.50 | +290.9 | +275.4 |
| `confluence_gte_60` | 14 | S_STRANGER | 37.8% | 21.4% | 28.6% | 42.9% | +4.2 | 1.02 | 2.05 | +368.2 | +284.0 |
| `confluence_gte_70` | 2 | S_STRANGER | 5.4% | 0.0% | 0.0% | 50.0% | -76.0 | 0.00 | 0.00 | +64.0 | +141.0 |
| `tdi_rsi_gt_signal` | 28 | S_STRANGER | 75.7% | 28.6% | 35.7% | 46.4% | +14.4 | 1.09 | 1.52 | +331.1 | +245.3 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 43.2% | 31.2% | 43.8% | 50.0% | +79.6 | 1.52 | 1.52 | +369.7 | +186.7 |
| `ratio_le_2_and_asian_gte_30` | 26 | S_STRANGER | 70.3% | 19.2% | 26.9% | 42.3% | -3.3 | 0.98 | 1.96 | +311.1 | +255.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 19 | S_STRANGER | 51.4% | 26.3% | 36.8% | 52.6% | +118.9 | 1.98 | 2.26 | +381.6 | +188.8 |
| `feature_fresh_reclaim_within_8` | 4 | R_REPEATER | 10.8% | 50.0% | 50.0% | 50.0% | +121.0 | 1.80 | 1.80 | +460.0 | +108.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 21.6% | 27.0% | 40.5% | -54.4 | 0.71 | 1.50 | +290.9 | +275.4 |
| `feature_momentum_breakout_exception` | 33 | S_STRANGER | 89.2% | 24.2% | 27.3% | 45.5% | -28.2 | 0.84 | 1.68 | +315.2 | +291.7 |
| `feature_eurjpy_tdi50_reclaim` | 16 | S_STRANGER | 43.2% | 31.2% | 43.8% | 50.0% | +79.6 | 1.52 | 1.52 | +369.7 | +186.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-214.5; validation N=10 Fav=30.0% Avg=+183.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 35.7% | 21.4% | +62.9 | 1.33 | 2.39 | +417.4 | +307.1 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 85.7% | 25.0% | 41.7% | 25.0% | +117.0 | 1.65 | 2.31 | +473.3 | +295.4 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 23.1% | 38.5% | 23.1% | +72.6 | 1.36 | 2.18 | +444.8 | +315.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 21.4% | 35.7% | 21.4% | +62.9 | 1.33 | 2.39 | +417.4 | +307.1 |
| `confluence_gte_60` | 9 | S_STRANGER | 64.3% | 22.2% | 44.4% | 22.2% | +59.8 | 1.34 | 1.67 | +463.9 | +315.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 50.0% | +485.7 | 3.11 | 3.11 | +770.0 | +326.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 11.1% | 22.2% | 11.1% | -230.3 | 0.14 | 0.49 | +221.4 | +381.9 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 85.7% | 25.0% | 41.7% | 25.0% | +117.0 | 1.65 | 2.31 | +473.3 | +295.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 7.1% | 100.0% | 100.0% | 100.0% | +1432.5 | 999.00 | 999.00 | +1437.0 | +93.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 92.9% | 15.4% | 30.8% | 15.4% | +56.6 | 1.27 | 2.87 | +409.3 | +329.5 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 92.9% | 15.4% | 30.8% | 23.1% | +14.4 | 1.07 | 2.41 | +390.9 | +330.7 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 57.1% | 12.5% | 12.5% | 12.5% | -283.4 | 0.06 | 0.42 | +207.2 | +425.4 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=12.5% Avg=-113.4; validation N=1 Fav=100.0% Avg=+178.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -131.4 | 0.23 | 0.85 | +209.1 | +294.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 10.0% | -154.0 | 0.20 | 0.78 | +205.7 | +306.3 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 78.6% | 18.2% | 18.2% | 9.1% | -143.1 | 0.19 | 0.86 | +195.6 | +288.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -131.4 | 0.23 | 0.85 | +209.1 | +294.5 |
| `confluence_gte_60` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 11.1% | -81.0 | 0.37 | 1.28 | +208.4 | +272.9 |
| `confluence_gte_70` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 33.3% | -67.0 | 0.47 | 0.94 | +201.0 | +191.0 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 8.3% | -165.3 | 0.16 | 0.79 | +201.2 | +339.0 |
| `tdi_rsi_gte_50` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 0.0% | +63.5 | 2.10 | 2.10 | +464.5 | +295.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 10.0% | -154.0 | 0.20 | 0.78 | +205.7 | +306.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 11.1% | -167.2 | 0.20 | 0.70 | +226.4 | +335.4 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -1094.0 | 0.00 | 0.00 | +596.0 | +1306.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -131.4 | 0.23 | 0.85 | +209.1 | +294.5 |
| `feature_momentum_breakout_exception` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -131.4 | 0.23 | 0.85 | +209.1 | +294.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 0.0% | +63.5 | 2.10 | 2.10 | +464.5 | +295.0 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-88.0; validation N=6 Fav=33.3% Avg=-170.1; out_of_sample N=2 Fav=50.0% Avg=-81.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -1339.0 | 0.02 | 0.08 | +390.8 | +265.4 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 92.9% | 23.1% | 23.1% | 15.4% | -1119.7 | 0.03 | 0.10 | +394.5 | +273.4 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 23.1% | 23.1% | 15.4% | -1119.7 | 0.03 | 0.10 | +394.5 | +273.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -1339.0 | 0.02 | 0.08 | +390.8 | +265.4 |
| `confluence_gte_60` | 10 | S_STRANGER | 71.4% | 10.0% | 10.0% | 0.0% | -1889.1 | 0.01 | 0.05 | +438.7 | +333.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 20.0% | -2407.9 | 0.01 | 0.05 | +447.0 | +120.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 14.3% | -2485.1 | 0.01 | 0.06 | +418.6 | +172.9 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 92.9% | 23.1% | 23.1% | 15.4% | -1119.7 | 0.03 | 0.10 | +394.5 | +273.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 20.0% | -2407.9 | 0.01 | 0.05 | +447.0 | +120.2 |
| `feature_fresh_reclaim_within_8` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 0.0% | -3122.7 | 0.00 | 0.00 | +680.5 | +202.7 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -1339.0 | 0.02 | 0.08 | +390.8 | +265.4 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 64.3% | 33.3% | 33.3% | 22.2% | -141.2 | 0.25 | 0.51 | +303.2 | +293.2 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 14.3% | -2485.1 | 0.01 | 0.06 | +418.6 | +172.9 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=40 Fav=27.5% Avg=+78.9; out_of_sample N=2 Fav=0.0% Avg=-256.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 52 | S_STRANGER | 100.0% | 21.2% | 28.8% | 21.2% | -79.4 | 0.72 | 1.64 | +516.7 | +380.9 |
| `hunt_to_ar_ratio_le_2_0` | 41 | S_STRANGER | 78.8% | 22.0% | 29.3% | 19.5% | -38.3 | 0.86 | 1.93 | +572.0 | +385.0 |
| `hunt_to_ar_ratio_le_2_5` | 43 | S_STRANGER | 82.7% | 20.9% | 27.9% | 20.9% | -66.1 | 0.77 | 1.79 | +559.3 | +372.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 52 | S_STRANGER | 100.0% | 21.2% | 28.8% | 21.2% | -79.4 | 0.72 | 1.64 | +516.7 | +380.9 |
| `confluence_gte_60` | 29 | S_STRANGER | 55.8% | 24.1% | 34.5% | 17.2% | -38.2 | 0.85 | 1.53 | +492.0 | +353.9 |
| `confluence_gte_70` | 10 | S_STRANGER | 19.2% | 20.0% | 20.0% | 10.0% | -107.1 | 0.71 | 2.82 | +607.9 | +508.3 |
| `tdi_rsi_gt_signal` | 25 | S_STRANGER | 48.1% | 20.0% | 28.0% | 24.0% | -51.1 | 0.81 | 1.96 | +596.1 | +427.3 |
| `tdi_rsi_gte_50` | 28 | S_STRANGER | 53.8% | 21.4% | 32.1% | 25.0% | -122.6 | 0.60 | 1.13 | +502.9 | +326.0 |
| `ratio_le_2_and_asian_gte_30` | 41 | S_STRANGER | 78.8% | 22.0% | 29.3% | 19.5% | -38.3 | 0.86 | 1.93 | +572.0 | +385.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 22 | S_STRANGER | 42.3% | 22.7% | 31.8% | 27.3% | +5.8 | 1.02 | 2.05 | +665.3 | +426.1 |
| `feature_fresh_reclaim_within_8` | 6 | S_STRANGER | 11.5% | 0.0% | 16.7% | 0.0% | -690.5 | 0.01 | 0.06 | +176.7 | +332.8 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 51 | S_STRANGER | 98.1% | 21.6% | 27.5% | 21.6% | -85.0 | 0.71 | 1.72 | +522.7 | +378.5 |
| `feature_momentum_breakout_exception` | 42 | S_STRANGER | 80.8% | 26.2% | 31.0% | 26.2% | +62.9 | 1.33 | 2.65 | +605.3 | +421.3 |
| `feature_eurjpy_tdi50_reclaim` | 28 | S_STRANGER | 53.8% | 21.4% | 32.1% | 25.0% | -122.6 | 0.60 | 1.13 | +502.9 | +326.0 |

### STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=14 Fav=28.6% Avg=+65.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 21.1% | 31.6% | 26.3% | -82.6 | 0.61 | 1.23 | +280.1 | +235.3 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 94.7% | 22.2% | 33.3% | 27.8% | -53.0 | 0.72 | 1.33 | +287.6 | +245.6 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 21.1% | 31.6% | 26.3% | -82.6 | 0.61 | 1.23 | +280.1 | +235.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 19 | S_STRANGER | 100.0% | 21.1% | 31.6% | 26.3% | -82.6 | 0.61 | 1.23 | +280.1 | +235.3 |
| `confluence_gte_60` | 7 | S_STRANGER | 36.8% | 14.3% | 42.9% | 14.3% | -73.6 | 0.62 | 0.83 | +292.1 | +133.4 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -76.0 | 0.00 | 0.00 | +220.0 | +261.0 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 21.1% | 25.0% | 25.0% | 25.0% | -436.8 | 0.04 | 0.11 | +263.8 | +50.7 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 78.9% | 13.3% | 26.7% | 20.0% | -194.2 | 0.16 | 0.41 | +197.6 | +237.3 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 94.7% | 22.2% | 33.3% | 27.8% | -53.0 | 0.72 | 1.33 | +287.6 | +245.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 15.8% | 33.3% | 33.3% | 33.3% | -377.3 | 0.06 | 0.11 | +303.3 | +51.0 |
| `feature_fresh_reclaim_within_8` | 8 | S_STRANGER | 42.1% | 0.0% | 12.5% | 12.5% | -283.5 | 0.05 | 0.29 | +131.7 | +277.1 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 21.1% | 31.6% | 26.3% | -82.6 | 0.61 | 1.23 | +280.1 | +235.3 |
| `feature_momentum_breakout_exception` | 14 | S_STRANGER | 73.7% | 28.6% | 42.9% | 35.7% | +65.3 | 1.58 | 1.84 | +310.3 | +279.9 |
| `feature_eurjpy_tdi50_reclaim` | 15 | S_STRANGER | 78.9% | 13.3% | 26.7% | 20.0% | -194.2 | 0.16 | 0.41 | +197.6 | +237.3 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=-4.2; validation N=3 Fav=66.7% Avg=+313.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 21.1% | 21.1% | 0.0% | -591.6 | 0.13 | 0.49 | +327.9 | +213.6 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 94.7% | 22.2% | 22.2% | 0.0% | -621.9 | 0.13 | 0.46 | +333.4 | +189.3 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 94.7% | 22.2% | 22.2% | 0.0% | -621.9 | 0.13 | 0.46 | +333.4 | +189.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 19 | S_STRANGER | 100.0% | 21.1% | 21.1% | 0.0% | -591.6 | 0.13 | 0.49 | +327.9 | +213.6 |
| `confluence_gte_60` | 4 | S_STRANGER | 21.1% | 25.0% | 25.0% | 0.0% | -124.7 | 0.14 | 0.42 | +173.2 | +299.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 57.9% | 9.1% | 9.1% | 0.0% | -729.9 | 0.01 | 0.10 | +187.5 | +179.6 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 63.2% | 0.0% | 0.0% | 0.0% | -1027.0 | 0.00 | 0.00 | +195.2 | +170.6 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 94.7% | 22.2% | 22.2% | 0.0% | -621.9 | 0.13 | 0.46 | +333.4 | +189.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 57.9% | 9.1% | 9.1% | 0.0% | -729.9 | 0.01 | 0.10 | +187.5 | +179.6 |
| `feature_fresh_reclaim_within_8` | 12 | S_STRANGER | 63.2% | 0.0% | 0.0% | 0.0% | -1027.0 | 0.00 | 0.00 | +195.2 | +170.6 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 21.1% | 21.1% | 0.0% | -591.6 | 0.13 | 0.49 | +327.9 | +213.6 |
| `feature_momentum_breakout_exception` | 8 | R_REPEATER | 42.1% | 50.0% | 50.0% | 0.0% | +114.9 | 2.19 | 2.19 | +493.6 | +284.0 |
| `feature_eurjpy_tdi50_reclaim` | 12 | S_STRANGER | 63.2% | 0.0% | 0.0% | 0.0% | -1027.0 | 0.00 | 0.00 | +195.2 | +170.6 |

### STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=-132.7; validation N=1 Fav=100.0% Avg=+969.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 48 | S_STRANGER | 100.0% | 20.8% | 20.8% | 10.4% | -136.0 | 0.52 | 1.93 | +486.5 | +440.5 |
| `hunt_to_ar_ratio_le_2_0` | 36 | S_STRANGER | 75.0% | 22.2% | 22.2% | 11.1% | -81.8 | 0.70 | 2.35 | +472.7 | +419.5 |
| `hunt_to_ar_ratio_le_2_5` | 37 | S_STRANGER | 77.1% | 24.3% | 24.3% | 10.8% | -72.5 | 0.72 | 2.17 | +480.9 | +411.6 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 48 | S_STRANGER | 100.0% | 20.8% | 20.8% | 10.4% | -136.0 | 0.52 | 1.93 | +486.5 | +440.5 |
| `confluence_gte_60` | 40 | S_STRANGER | 83.3% | 15.0% | 15.0% | 5.0% | -172.7 | 0.46 | 2.51 | +508.9 | +468.0 |
| `confluence_gte_70` | 9 | S_STRANGER | 18.8% | 11.1% | 11.1% | 0.0% | -328.7 | 0.05 | 0.42 | +492.4 | +542.9 |
| `tdi_rsi_gt_signal` | 41 | S_STRANGER | 85.4% | 17.1% | 17.1% | 9.8% | -182.6 | 0.36 | 1.69 | +451.4 | +434.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 14.6% | 42.9% | 42.9% | 42.9% | +24.7 | 1.09 | 1.46 | +663.1 | +172.3 |
| `ratio_le_2_and_asian_gte_30` | 36 | S_STRANGER | 75.0% | 22.2% | 22.2% | 11.1% | -81.8 | 0.70 | 2.35 | +472.7 | +419.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 32 | S_STRANGER | 66.7% | 18.8% | 18.8% | 9.4% | -154.3 | 0.45 | 1.89 | +408.9 | +413.9 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 2.1% | 0.0% | 0.0% | 0.0% | -1542.0 | 0.00 | 0.00 | +706.0 | +57.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 48 | S_STRANGER | 100.0% | 20.8% | 20.8% | 10.4% | -136.0 | 0.52 | 1.93 | +486.5 | +440.5 |
| `feature_momentum_breakout_exception` | 47 | S_STRANGER | 97.9% | 21.3% | 21.3% | 10.6% | -106.1 | 0.59 | 2.11 | +481.9 | +448.7 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 14.6% | 42.9% | 42.9% | 42.9% | +24.7 | 1.09 | 1.46 | +663.1 | +172.3 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=22.2% Avg=+9.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 10.0% | -4.9 | 0.94 | 2.20 | +165.4 | +192.7 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 12.5% | -26.4 | 0.72 | 2.16 | +163.5 | +206.9 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 12.5% | -26.4 | 0.72 | 2.16 | +163.5 | +206.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 10.0% | -4.9 | 0.94 | 2.20 | +165.4 | +192.7 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 10.0% | -4.9 | 0.94 | 2.20 | +165.4 | +192.7 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 10.0% | -4.9 | 0.94 | 2.20 | +165.4 | +192.7 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 90.0% | 22.2% | 33.3% | 11.1% | +9.0 | 1.11 | 2.21 | +183.3 | +195.6 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 10.0% | 0.0% | 100.0% | 0.0% | +292.0 | 999.00 | 999.00 | +342.0 | +105.0 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 12.5% | -26.4 | 0.72 | 2.16 | +163.5 | +206.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 12.5% | -26.4 | 0.72 | 2.16 | +163.5 | +206.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 10.0% | -4.9 | 0.94 | 2.20 | +165.4 | +192.7 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 10.0% | -4.9 | 0.94 | 2.20 | +165.4 | +192.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 100.0% | 0.0% | +292.0 | 999.00 | 999.00 | +342.0 | +105.0 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-168.6; validation N=3 Fav=66.7% Avg=+143.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -85.3 | 0.34 | 1.20 | +257.1 | +241.6 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 37.5% | -51.5 | 0.52 | 1.30 | +291.3 | +232.1 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 37.5% | -51.5 | 0.52 | 1.30 | +291.3 | +232.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -85.3 | 0.34 | 1.20 | +257.1 | +241.6 |
| `confluence_gte_60` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 25.0% | -57.0 | 0.00 | 0.00 | +301.0 | +245.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -109.5 | 0.38 | 1.13 | +179.5 | +266.8 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | -168.3 | 0.26 | 0.53 | +199.7 | +299.0 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 37.5% | -51.5 | 0.52 | 1.30 | +291.3 | +232.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -109.5 | 0.38 | 1.13 | +179.5 | +266.8 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +264.0 | 999.00 | 999.00 | +618.0 | +46.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -85.3 | 0.34 | 1.20 | +257.1 | +241.6 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -85.3 | 0.34 | 1.20 | +257.1 | +241.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | -168.3 | 0.26 | 0.53 | +199.7 | +299.0 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=33.3% Avg=-31.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 40.0% | 20.0% | -134.9 | 0.32 | 0.47 | +252.7 | +318.3 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 22.2% | 44.4% | 22.2% | -132.0 | 0.34 | 0.43 | +231.7 | +310.8 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 22.2% | 44.4% | 22.2% | -132.0 | 0.34 | 0.43 | +231.7 | +310.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 20.0% | 40.0% | 20.0% | -134.9 | 0.32 | 0.47 | +252.7 | +318.3 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 40.0% | 20.0% | -134.9 | 0.32 | 0.47 | +252.7 | +318.3 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 20.0% | 40.0% | 20.0% | -134.9 | 0.32 | 0.47 | +252.7 | +318.3 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -325.5 | 0.00 | 0.00 | +100.0 | +393.5 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 33.3% | 50.0% | 33.3% | -31.8 | 0.75 | 0.75 | +316.5 | +220.3 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 22.2% | 44.4% | 22.2% | -132.0 | 0.34 | 0.43 | +231.7 | +310.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -325.5 | 0.00 | 0.00 | +100.0 | +393.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 40.0% | 20.0% | -134.9 | 0.32 | 0.47 | +252.7 | +318.3 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 80.0% | 25.0% | 50.0% | 25.0% | -94.8 | 0.45 | 0.45 | +283.0 | +302.0 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 60.0% | 33.3% | 50.0% | 33.3% | -31.8 | 0.75 | 0.75 | +316.5 | +220.3 |

### STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+303.4; validation N=2 Fav=0.0% Avg=-603.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -204.1 | 0.53 | 2.13 | +613.0 | +393.2 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -204.1 | 0.53 | 2.13 | +613.0 | +393.2 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -204.1 | 0.53 | 2.13 | +613.0 | +393.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -204.1 | 0.53 | 2.13 | +613.0 | +393.2 |
| `confluence_gte_60` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 0.0% | -106.6 | 0.71 | 2.48 | +673.7 | +285.1 |
| `confluence_gte_70` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -688.0 | 0.00 | 0.00 | +8.0 | +1342.0 |
| `tdi_rsi_gt_signal` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -711.6 | 0.00 | 0.00 | +289.2 | +392.4 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -204.1 | 0.53 | 2.13 | +613.0 | +393.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -613.0 | 0.00 | 0.00 | +318.7 | +184.3 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -204.1 | 0.53 | 2.13 | +613.0 | +393.2 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 0.0% | +44.3 | 1.15 | 2.89 | +735.3 | +523.0 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -711.6 | 0.00 | 0.00 | +289.2 | +392.4 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=-42.0; validation N=10 Fav=20.0% Avg=-247.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -241.7 | 0.20 | 0.75 | +420.8 | +375.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 66.7% | 10.0% | 10.0% | 0.0% | -265.6 | 0.02 | 0.17 | +185.4 | +293.7 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 66.7% | 10.0% | 10.0% | 0.0% | -265.6 | 0.02 | 0.17 | +185.4 | +293.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -241.7 | 0.20 | 0.75 | +420.8 | +375.0 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -241.7 | 0.20 | 0.75 | +420.8 | +375.0 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -241.7 | 0.20 | 0.75 | +420.8 | +375.0 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 25.0% | -385.8 | 0.00 | 0.00 | +120.2 | +285.0 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 33.3% | 0.0% | 0.0% | 20.0% | -262.4 | 0.00 | 0.00 | +184.2 | +204.6 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 66.7% | 10.0% | 10.0% | 0.0% | -265.6 | 0.02 | 0.17 | +185.4 | +293.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -566.5 | 0.00 | 0.00 | +54.5 | +367.0 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -245.5 | 0.00 | 0.00 | +88.0 | +242.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -241.7 | 0.20 | 0.75 | +420.8 | +375.0 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 86.7% | 23.1% | 23.1% | 23.1% | -200.0 | 0.26 | 0.79 | +480.1 | +388.2 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 33.3% | 0.0% | 0.0% | 20.0% | -262.4 | 0.00 | 0.00 | +184.2 | +204.6 |

### RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=50.0% Avg=+213.3; validation N=2 Fav=0.0% Avg=-265.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 25 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -437.5 | 0.25 | 0.94 | +298.2 | +253.3 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 84.0% | 23.8% | 23.8% | 23.8% | -301.2 | 0.36 | 1.09 | +320.0 | +232.7 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 84.0% | 23.8% | 23.8% | 23.8% | -301.2 | 0.36 | 1.09 | +320.0 | +232.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 25 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -437.5 | 0.25 | 0.94 | +298.2 | +253.3 |
| `confluence_gte_60` | 11 | S_STRANGER | 44.0% | 18.2% | 18.2% | 27.3% | -418.5 | 0.19 | 0.75 | +284.5 | +335.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 68.0% | 5.9% | 5.9% | 11.8% | -623.1 | 0.09 | 1.33 | +206.6 | +286.9 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 48.0% | 33.3% | 33.3% | 25.0% | +19.5 | 1.10 | 2.20 | +331.5 | +293.9 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 84.0% | 23.8% | 23.8% | 23.8% | -301.2 | 0.36 | 1.09 | +320.0 | +232.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 52.0% | 7.7% | 7.7% | 15.4% | -460.0 | 0.15 | 1.62 | +213.5 | +264.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -437.5 | 0.25 | 0.94 | +298.2 | +253.3 |
| `feature_momentum_breakout_exception` | 23 | S_STRANGER | 92.0% | 17.4% | 17.4% | 21.7% | -493.0 | 0.22 | 0.97 | +296.8 | +261.7 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 40.0% | 40.0% | 40.0% | 30.0% | +117.7 | 1.86 | 2.79 | +382.4 | +314.4 |

### STOP_HUNT|SELL|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=30.0% Avg=-147.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 20.0% | 35.0% | 25.0% | -493.5 | 0.45 | 0.70 | +1207.6 | +1041.6 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 100.0% | 20.0% | 35.0% | 25.0% | -493.5 | 0.45 | 0.70 | +1207.6 | +1041.6 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 20.0% | 35.0% | 25.0% | -493.5 | 0.45 | 0.70 | +1207.6 | +1041.6 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 20 | S_STRANGER | 100.0% | 20.0% | 35.0% | 25.0% | -493.5 | 0.45 | 0.70 | +1207.6 | +1041.6 |
| `confluence_gte_60` | 10 | S_STRANGER | 50.0% | 20.0% | 30.0% | 20.0% | -394.4 | 0.51 | 1.03 | +1360.3 | +981.7 |
| `confluence_gte_70` | 2 | S_STRANGER | 10.0% | 0.0% | 0.0% | 50.0% | -253.0 | 0.00 | 0.00 | +1681.5 | +1269.0 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 50.0% | 30.0% | 50.0% | 20.0% | -147.8 | 0.82 | 0.82 | +1164.7 | +708.1 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 60.0% | 16.7% | 41.7% | 16.7% | -564.4 | 0.39 | 0.55 | +711.1 | +635.2 |
| `ratio_le_2_and_asian_gte_30` | 20 | S_STRANGER | 100.0% | 20.0% | 35.0% | 25.0% | -493.5 | 0.45 | 0.70 | +1207.6 | +1041.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 50.0% | 30.0% | 50.0% | 20.0% | -147.8 | 0.82 | 0.82 | +1164.7 | +708.1 |
| `feature_fresh_reclaim_within_8` | 3 | S_STRANGER | 15.0% | 0.0% | 33.3% | 0.0% | -869.0 | 0.43 | 0.86 | +852.0 | +1004.3 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 20.0% | 35.0% | 25.0% | -493.5 | 0.45 | 0.70 | +1207.6 | +1041.6 |
| `feature_momentum_breakout_exception` | 15 | S_STRANGER | 75.0% | 26.7% | 33.3% | 33.3% | -361.7 | 0.50 | 0.80 | +1297.7 | +1321.5 |
| `feature_eurjpy_tdi50_reclaim` | 12 | S_STRANGER | 60.0% | 16.7% | 41.7% | 16.7% | -564.4 | 0.39 | 0.55 | +711.1 | +635.2 |

### STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=17 Fav=23.5% Avg=-26.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 19.0% | 28.6% | 19.0% | -75.5 | 0.52 | 1.12 | +245.4 | +198.2 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 90.5% | 21.1% | 31.6% | 21.1% | -51.3 | 0.63 | 1.16 | +262.4 | +183.6 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 95.2% | 20.0% | 30.0% | 20.0% | -56.0 | 0.60 | 1.20 | +251.4 | +183.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 21 | S_STRANGER | 100.0% | 19.0% | 28.6% | 19.0% | -75.5 | 0.52 | 1.12 | +245.4 | +198.2 |
| `confluence_gte_60` | 21 | S_STRANGER | 100.0% | 19.0% | 28.6% | 19.0% | -75.5 | 0.52 | 1.12 | +245.4 | +198.2 |
| `confluence_gte_70` | 21 | S_STRANGER | 100.0% | 19.0% | 28.6% | 19.0% | -75.5 | 0.52 | 1.12 | +245.4 | +198.2 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 81.0% | 17.6% | 29.4% | 23.5% | -80.6 | 0.55 | 1.10 | +245.1 | +208.7 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 42.9% | 22.2% | 44.4% | 33.3% | -20.9 | 0.86 | 0.86 | +275.4 | +111.8 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 90.5% | 21.1% | 31.6% | 21.1% | -51.3 | 0.63 | 1.16 | +262.4 | +183.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 71.4% | 20.0% | 33.3% | 26.7% | -50.6 | 0.69 | 1.10 | +266.5 | +191.7 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 9.5% | 0.0% | 0.0% | 0.0% | -410.0 | 0.00 | 0.00 | +183.0 | +64.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 19.0% | 28.6% | 19.0% | -75.5 | 0.52 | 1.12 | +245.4 | +198.2 |
| `feature_momentum_breakout_exception` | 17 | S_STRANGER | 81.0% | 23.5% | 29.4% | 23.5% | -26.4 | 0.78 | 1.57 | +256.6 | +228.4 |
| `feature_eurjpy_tdi50_reclaim` | 9 | S_STRANGER | 42.9% | 22.2% | 44.4% | 33.3% | -20.9 | 0.86 | 0.86 | +275.4 | +111.8 |

### THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=25.0% Avg=-9.5; validation N=3 Fav=33.3% Avg=+513.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 18.5% | 29.6% | 33.3% | -80.9 | 0.53 | 1.06 | +261.3 | +279.7 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 77.8% | 14.3% | 19.0% | 28.6% | -141.0 | 0.13 | 0.46 | +187.2 | +279.9 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 81.5% | 13.6% | 22.7% | 31.8% | -87.7 | 0.43 | 1.21 | +237.3 | +272.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 27 | S_STRANGER | 100.0% | 18.5% | 29.6% | 33.3% | -80.9 | 0.53 | 1.06 | +261.3 | +279.7 |
| `confluence_gte_60` | 11 | S_STRANGER | 40.7% | 9.1% | 9.1% | 18.2% | -248.8 | 0.16 | 1.41 | +217.5 | +411.5 |
| `confluence_gte_70` | 2 | S_STRANGER | 7.4% | 0.0% | 0.0% | 0.0% | -280.5 | 0.00 | 0.00 | +317.0 | +373.0 |
| `tdi_rsi_gt_signal` | 22 | S_STRANGER | 81.5% | 18.2% | 31.8% | 36.4% | +15.5 | 1.16 | 1.99 | +262.7 | +214.3 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 40.7% | 27.3% | 54.5% | 45.5% | +133.1 | 2.99 | 2.00 | +345.6 | +211.0 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 77.8% | 14.3% | 19.0% | 28.6% | -141.0 | 0.13 | 0.46 | +187.2 | +279.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 63.0% | 11.8% | 17.6% | 29.4% | -69.8 | 0.25 | 0.93 | +183.2 | +223.1 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 7.4% | 0.0% | 100.0% | 0.0% | +138.5 | 999.00 | 999.00 | +246.0 | +287.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 18.5% | 29.6% | 33.3% | -80.9 | 0.53 | 1.06 | +261.3 | +279.7 |
| `feature_momentum_breakout_exception` | 25 | S_STRANGER | 92.6% | 20.0% | 28.0% | 36.0% | -94.2 | 0.49 | 1.04 | +269.0 | +290.7 |
| `feature_eurjpy_tdi50_reclaim` | 11 | S_STRANGER | 40.7% | 27.3% | 54.5% | 45.5% | +133.1 | 2.99 | 2.00 | +345.6 | +211.0 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=25.0% Avg=-11.1; validation N=4 Fav=25.0% Avg=+30.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | S_STRANGER | 100.0% | 18.2% | 24.2% | 24.2% | -90.5 | 0.68 | 1.79 | +422.7 | +360.9 |
| `hunt_to_ar_ratio_le_2_0` | 28 | S_STRANGER | 84.8% | 14.3% | 17.9% | 21.4% | -126.5 | 0.62 | 2.48 | +407.9 | +386.4 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 87.9% | 13.8% | 20.7% | 20.7% | -119.8 | 0.63 | 2.09 | +397.3 | +388.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 33 | S_STRANGER | 100.0% | 18.2% | 24.2% | 24.2% | -90.5 | 0.68 | 1.79 | +422.7 | +360.9 |
| `confluence_gte_60` | 12 | S_STRANGER | 36.4% | 25.0% | 33.3% | 33.3% | +2.7 | 1.02 | 1.28 | +396.5 | +309.1 |
| `confluence_gte_70` | 3 | S_STRANGER | 9.1% | 33.3% | 33.3% | 100.0% | +148.7 | 999.00 | 999.00 | +348.3 | +63.3 |
| `tdi_rsi_gt_signal` | 28 | S_STRANGER | 84.8% | 14.3% | 21.4% | 28.6% | -102.8 | 0.66 | 1.98 | +392.4 | +341.4 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 21.2% | 0.0% | 14.3% | 14.3% | -658.4 | 0.08 | 0.41 | +176.0 | +305.7 |
| `ratio_le_2_and_asian_gte_30` | 28 | S_STRANGER | 84.8% | 14.3% | 17.9% | 21.4% | -126.5 | 0.62 | 2.48 | +407.9 | +386.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 24 | S_STRANGER | 72.7% | 12.5% | 16.7% | 25.0% | -139.8 | 0.60 | 2.56 | +395.2 | +354.8 |
| `feature_fresh_reclaim_within_8` | 4 | S_STRANGER | 12.1% | 0.0% | 25.0% | 25.0% | -110.5 | 0.48 | 0.96 | +167.7 | +234.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 33 | S_STRANGER | 100.0% | 18.2% | 24.2% | 24.2% | -90.5 | 0.68 | 1.79 | +422.7 | +360.9 |
| `feature_momentum_breakout_exception` | 28 | S_STRANGER | 84.8% | 21.4% | 25.0% | 28.6% | +36.4 | 1.21 | 2.93 | +474.0 | +385.3 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 21.2% | 0.0% | 14.3% | 14.3% | -658.4 | 0.08 | 0.41 | +176.0 | +305.7 |

### RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+49.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | -121.4 | 0.34 | 0.92 | +305.6 | +204.5 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 54.5% | 0.0% | 16.7% | 0.0% | -279.2 | 0.02 | 0.11 | +247.3 | +211.3 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 54.5% | 0.0% | 16.7% | 0.0% | -279.2 | 0.02 | 0.11 | +247.3 | +211.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | -121.4 | 0.34 | 0.92 | +305.6 | +204.5 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | -121.4 | 0.34 | 0.92 | +305.6 | +204.5 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | -121.4 | 0.34 | 0.92 | +305.6 | +204.5 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 40.0% | 60.0% | 40.0% | -52.8 | 0.73 | 0.48 | +419.4 | +134.0 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 54.5% | 33.3% | 50.0% | 33.3% | +47.3 | 1.68 | 1.68 | +316.5 | +188.2 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 54.5% | 0.0% | 16.7% | 0.0% | -279.2 | 0.02 | 0.11 | +247.3 | +211.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 27.3% | 0.0% | 33.3% | 0.0% | -310.3 | 0.04 | 0.07 | +186.0 | +80.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | -121.4 | 0.34 | 0.92 | +305.6 | +204.5 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 90.9% | 20.0% | 30.0% | 20.0% | -114.5 | 0.38 | 0.89 | +326.1 | +202.5 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 40.0% | +49.6 | 1.59 | 2.39 | +358.6 | +222.2 |

### THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=-178.7; validation N=3 Fav=33.3% Avg=-202.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 27.3% | -141.7 | 0.36 | 0.96 | +431.0 | +348.6 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 81.8% | 11.1% | 22.2% | 22.2% | -211.8 | 0.18 | 0.64 | +468.4 | +410.0 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 81.8% | 11.1% | 22.2% | 22.2% | -211.8 | 0.18 | 0.64 | +468.4 | +410.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 27.3% | -141.7 | 0.36 | 0.96 | +431.0 | +348.6 |
| `confluence_gte_60` | 5 | S_STRANGER | 45.5% | 0.0% | 20.0% | 20.0% | -138.6 | 0.34 | 1.35 | +421.0 | +380.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 28.6% | -189.1 | 0.28 | 0.71 | +410.4 | +363.7 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 14.3% | 28.6% | 28.6% | -54.1 | 0.68 | 1.70 | +604.4 | +313.1 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 81.8% | 11.1% | 22.2% | 22.2% | -211.8 | 0.18 | 0.64 | +468.4 | +410.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 54.5% | 16.7% | 16.7% | 16.7% | -295.2 | 0.04 | 0.20 | +402.7 | +420.8 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -376.0 | 0.00 | 0.00 | +941.0 | +570.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 27.3% | -141.7 | 0.36 | 0.96 | +431.0 | +348.6 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 90.9% | 20.0% | 30.0% | 30.0% | -90.1 | 0.49 | 1.15 | +299.6 | +285.6 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 63.6% | 14.3% | 28.6% | 28.6% | -54.1 | 0.68 | 1.70 | +604.4 | +313.1 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-25.0; validation N=7 Fav=28.6% Avg=-229.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | -172.1 | 0.35 | 0.93 | +181.0 | +337.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 20.0% | 20.0% | 20.0% | -229.8 | 0.21 | 0.84 | +146.7 | +339.1 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | -172.1 | 0.35 | 0.93 | +181.0 | +337.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | -172.1 | 0.35 | 0.93 | +181.0 | +337.3 |
| `confluence_gte_60` | 8 | S_STRANGER | 72.7% | 25.0% | 37.5% | 25.0% | -203.6 | 0.38 | 0.64 | +212.9 | +405.4 |
| `confluence_gte_70` | 3 | S_STRANGER | 27.3% | 33.3% | 66.7% | 33.3% | +125.0 | 2.97 | 1.49 | +285.3 | +542.7 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -204.0 | 0.00 | 0.00 | +166.0 | +414.0 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -294.0 | 0.00 | 0.00 | +112.0 | +459.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 90.9% | 20.0% | 20.0% | 20.0% | -229.8 | 0.21 | 0.84 | +146.7 | +339.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -204.0 | 0.00 | 0.00 | +166.0 | +414.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | -172.1 | 0.35 | 0.93 | +181.0 | +337.3 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 18.2% | -172.1 | 0.35 | 0.93 | +181.0 | +337.3 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -294.0 | 0.00 | 0.00 | +112.0 | +459.0 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=1 Fav=0.0% Avg=+305.0; out_of_sample N=4 Fav=50.0% Avg=+411.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 45.5% | 27.3% | -214.4 | 0.75 | 0.90 | +1077.9 | +901.5 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 18.2% | 45.5% | 27.3% | -214.4 | 0.75 | 0.90 | +1077.9 | +901.5 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 18.2% | 45.5% | 27.3% | -214.4 | 0.75 | 0.90 | +1077.9 | +901.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 18.2% | 45.5% | 27.3% | -214.4 | 0.75 | 0.90 | +1077.9 | +901.5 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 18.2% | 45.5% | 27.3% | -214.4 | 0.75 | 0.90 | +1077.9 | +901.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 100.0% | 18.2% | 45.5% | 27.3% | -214.4 | 0.75 | 0.90 | +1077.9 | +901.5 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 14.3% | 57.1% | 28.6% | -356.7 | 0.45 | 0.34 | +579.0 | +523.3 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 18.2% | 45.5% | 27.3% | -214.4 | 0.75 | 0.90 | +1077.9 | +901.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 100.0% | 18.2% | 45.5% | 27.3% | -214.4 | 0.75 | 0.90 | +1077.9 | +901.5 |
| `feature_fresh_reclaim_within_8` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 50.0% | -1274.0 | 0.22 | 0.22 | +584.5 | +699.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 45.5% | 27.3% | -214.4 | 0.75 | 0.90 | +1077.9 | +901.5 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 45.5% | 40.0% | 60.0% | 60.0% | +390.4 | 1.48 | 0.98 | +1873.6 | +1296.6 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 63.6% | 14.3% | 57.1% | 28.6% | -356.7 | 0.45 | 0.34 | +579.0 | +523.3 |

### RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=-2041.7; validation N=5 Fav=20.0% Avg=-207.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 9.1% | -1169.4 | 0.18 | 0.48 | +482.0 | +325.8 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 9.1% | -1169.4 | 0.18 | 0.48 | +482.0 | +325.8 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 9.1% | -1169.4 | 0.18 | 0.48 | +482.0 | +325.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 9.1% | -1169.4 | 0.18 | 0.48 | +482.0 | +325.8 |
| `confluence_gte_60` | 4 | S_STRANGER | 36.4% | 25.0% | 50.0% | 25.0% | -249.8 | 0.72 | 0.72 | +742.5 | +198.0 |
| `confluence_gte_70` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 100.0% | +1813.0 | 999.00 | 999.00 | +1910.0 | +345.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 22.2% | 33.3% | 11.1% | -1022.6 | 0.23 | 0.47 | +560.0 | +309.0 |
| `tdi_rsi_gte_50` | 2 | R_REPEATER | 18.2% | 50.0% | 100.0% | 50.0% | +1268.5 | 999.00 | 999.00 | +1340.0 | +184.5 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 9.1% | -1169.4 | 0.18 | 0.48 | +482.0 | +325.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 81.8% | 22.2% | 33.3% | 11.1% | -1022.6 | 0.23 | 0.47 | +560.0 | +309.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 9.1% | -1169.4 | 0.18 | 0.48 | +482.0 | +325.8 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 27.3% | 9.1% | -1169.4 | 0.18 | 0.48 | +482.0 | +325.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 9.1% | 100.0% | 100.0% | 100.0% | +1813.0 | 999.00 | 999.00 | +1910.0 | +345.0 |

### THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+99.7; validation N=3 Fav=33.3% Avg=+118.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 23.5% | 11.8% | -204.7 | 0.27 | 0.88 | +255.4 | +403.8 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 82.4% | 14.3% | 21.4% | 7.1% | -183.8 | 0.32 | 1.18 | +275.4 | +402.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 82.4% | 14.3% | 21.4% | 7.1% | -183.8 | 0.32 | 1.18 | +275.4 | +402.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 17.6% | 23.5% | 11.8% | -204.7 | 0.27 | 0.88 | +255.4 | +403.8 |
| `confluence_gte_60` | 9 | S_STRANGER | 52.9% | 11.1% | 22.2% | 0.0% | -150.3 | 0.15 | 0.52 | +199.7 | +287.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 88.2% | 20.0% | 26.7% | 13.3% | -157.3 | 0.35 | 0.97 | +246.3 | +340.5 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 35.3% | 50.0% | 66.7% | 33.3% | +109.2 | 2.04 | 1.02 | +339.3 | +202.8 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 82.4% | 14.3% | 21.4% | 7.1% | -183.8 | 0.32 | 1.18 | +275.4 | +402.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 70.6% | 16.7% | 25.0% | 8.3% | -121.1 | 0.46 | 1.37 | +267.4 | +323.4 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 5.9% | 100.0% | 100.0% | 100.0% | +61.0 | 999.00 | 999.00 | +275.0 | +155.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 17.6% | 23.5% | 11.8% | -204.7 | 0.27 | 0.88 | +255.4 | +403.8 |
| `feature_momentum_breakout_exception` | 16 | S_STRANGER | 94.1% | 18.8% | 18.8% | 12.5% | -223.8 | 0.25 | 1.08 | +260.8 | +423.7 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 35.3% | 50.0% | 66.7% | 33.3% | +109.2 | 2.04 | 1.02 | +339.3 | +202.8 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=33.3% Avg=-35.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 17.6% | -234.1 | 0.14 | 0.67 | +179.7 | +172.9 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 94.1% | 12.5% | 12.5% | 12.5% | -258.7 | 0.11 | 0.77 | +167.9 | +179.8 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 17.6% | -234.1 | 0.14 | 0.67 | +179.7 | +172.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 17.6% | -234.1 | 0.14 | 0.67 | +179.7 | +172.9 |
| `confluence_gte_60` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 14.3% | -257.0 | 0.08 | 0.50 | +237.9 | +202.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -266.0 | 0.00 | 0.00 | +34.5 | +343.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 52.9% | 0.0% | 0.0% | 0.0% | -392.2 | 0.00 | 0.00 | +86.2 | +169.8 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 94.1% | 12.5% | 12.5% | 12.5% | -258.7 | 0.11 | 0.77 | +167.9 | +179.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -266.0 | 0.00 | 0.00 | +34.5 | +343.5 |
| `feature_fresh_reclaim_within_8` | 8 | S_STRANGER | 47.1% | 12.5% | 12.5% | 12.5% | -433.1 | 0.04 | 0.31 | +137.9 | +120.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 17.6% | -234.1 | 0.14 | 0.67 | +179.7 | +172.9 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 52.9% | 33.3% | 33.3% | 33.3% | -35.8 | 0.68 | 1.35 | +254.4 | +209.0 |
| `feature_eurjpy_tdi50_reclaim` | 9 | S_STRANGER | 52.9% | 0.0% | 0.0% | 0.0% | -392.2 | 0.00 | 0.00 | +86.2 | +169.8 |

### STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=100.0% Avg=+1149.7; validation N=7 Fav=0.0% Avg=-619.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -286.3 | 0.41 | 1.80 | +582.8 | +688.4 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 94.1% | 18.8% | 18.8% | 12.5% | -195.0 | 0.53 | 2.10 | +602.2 | +508.8 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 94.1% | 18.8% | 18.8% | 12.5% | -195.0 | 0.53 | 2.10 | +602.2 | +508.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -286.3 | 0.41 | 1.80 | +582.8 | +688.4 |
| `confluence_gte_60` | 13 | S_STRANGER | 76.5% | 23.1% | 23.1% | 15.4% | -178.8 | 0.60 | 1.79 | +618.2 | +455.9 |
| `confluence_gte_70` | 5 | S_STRANGER | 29.4% | 20.0% | 20.0% | 0.0% | -445.0 | 0.23 | 0.91 | +523.4 | +555.6 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 64.7% | 27.3% | 27.3% | 9.1% | -239.4 | 0.57 | 1.51 | +627.5 | +600.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 35.3% | 16.7% | 16.7% | 16.7% | -297.2 | 0.56 | 2.79 | +619.7 | +229.3 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 94.1% | 18.8% | 18.8% | 12.5% | -195.0 | 0.53 | 2.10 | +602.2 | +508.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 58.8% | 30.0% | 30.0% | 10.0% | -88.6 | 0.80 | 1.86 | +663.1 | +304.1 |
| `feature_fresh_reclaim_within_8` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 33.3% | -442.7 | 0.00 | 0.00 | +463.0 | +559.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | -286.3 | 0.41 | 1.80 | +582.8 | +688.4 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 70.6% | 25.0% | 25.0% | 16.7% | -99.2 | 0.74 | 1.98 | +736.4 | +881.3 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 35.3% | 16.7% | 16.7% | 16.7% | -297.2 | 0.56 | 2.79 | +619.7 | +229.3 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=17 Fav=29.4% Avg=+50.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 17.2% | -140.5 | 0.44 | 1.94 | +214.5 | +231.6 |
| `hunt_to_ar_ratio_le_2_0` | 27 | S_STRANGER | 93.1% | 14.8% | 14.8% | 18.5% | -165.7 | 0.37 | 1.94 | +199.2 | +234.8 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 93.1% | 14.8% | 14.8% | 18.5% | -165.7 | 0.37 | 1.94 | +199.2 | +234.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 17.2% | -140.5 | 0.44 | 1.94 | +214.5 | +231.6 |
| `confluence_gte_60` | 14 | S_STRANGER | 48.3% | 28.6% | 28.6% | 21.4% | -11.7 | 0.94 | 2.11 | +289.4 | +205.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 58.6% | 17.6% | 17.6% | 11.8% | -177.1 | 0.40 | 1.86 | +222.5 | +230.6 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 69.0% | 5.0% | 5.0% | 10.0% | -268.4 | 0.13 | 2.38 | +111.6 | +257.3 |
| `ratio_le_2_and_asian_gte_30` | 27 | S_STRANGER | 93.1% | 14.8% | 14.8% | 18.5% | -165.7 | 0.37 | 1.94 | +199.2 | +234.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 51.7% | 13.3% | 13.3% | 13.3% | -227.3 | 0.29 | 1.90 | +196.1 | +236.4 |
| `feature_fresh_reclaim_within_8` | 6 | S_STRANGER | 20.7% | 0.0% | 0.0% | 16.7% | -305.5 | 0.00 | 0.00 | +120.7 | +242.2 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 17.2% | 17.2% | 17.2% | -140.5 | 0.44 | 1.94 | +214.5 | +231.6 |
| `feature_momentum_breakout_exception` | 17 | S_STRANGER | 58.6% | 29.4% | 29.4% | 29.4% | +50.8 | 1.37 | 2.74 | +313.5 | +255.6 |
| `feature_eurjpy_tdi50_reclaim` | 19 | S_STRANGER | 65.5% | 5.3% | 5.3% | 10.5% | -256.5 | 0.14 | 2.44 | +116.4 | +244.0 |

### THE_33_MW|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-93.5; validation N=4 Fav=50.0% Avg=+311.8; out_of_sample N=1 Fav=0.0% Avg=+125.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 25.0% | 16.7% | -30.7 | 0.85 | 2.54 | +316.9 | +330.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 10.0% | 20.0% | 10.0% | -107.3 | 0.46 | 1.85 | +235.5 | +299.6 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 16.7% | 25.0% | 16.7% | -30.7 | 0.85 | 2.54 | +316.9 | +330.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 16.7% | 25.0% | 16.7% | -30.7 | 0.85 | 2.54 | +316.9 | +330.5 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 16.7% | 25.0% | 16.7% | -30.7 | 0.85 | 2.54 | +316.9 | +330.5 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 16.7% | 25.0% | 16.7% | -30.7 | 0.85 | 2.54 | +316.9 | +330.5 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 58.3% | 28.6% | 42.9% | 28.6% | +169.3 | 2.36 | 3.15 | +474.4 | +236.4 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 14.3% | 28.6% | 14.3% | -88.1 | 0.60 | 1.50 | +250.1 | +310.7 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 83.3% | 10.0% | 20.0% | 10.0% | -107.3 | 0.46 | 1.85 | +235.5 | +299.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 50.0% | 16.7% | 33.3% | 16.7% | +9.0 | 1.06 | 2.12 | +313.8 | +270.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 25.0% | 16.7% | -30.7 | 0.85 | 2.54 | +316.9 | +330.5 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 20.0% | -9.8 | 0.95 | 3.81 | +354.0 | +347.6 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 58.3% | 14.3% | 28.6% | 14.3% | -88.1 | 0.60 | 1.50 | +250.1 | +310.7 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-36.0; validation N=3 Fav=33.3% Avg=-142.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -303.2 | 0.20 | 1.01 | +265.9 | +362.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 10.0% | -209.8 | 0.30 | 1.22 | +301.8 | +293.3 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 10.0% | -209.8 | 0.30 | 1.22 | +301.8 | +293.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -303.2 | 0.20 | 1.01 | +265.9 | +362.8 |
| `confluence_gte_60` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 9.1% | -286.2 | 0.23 | 1.02 | +285.7 | +364.1 |
| `confluence_gte_70` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 0.0% | -66.0 | 0.24 | 0.24 | +213.5 | +515.5 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 25.0% | 25.0% | 12.5% | -75.9 | 0.60 | 1.81 | +357.3 | +336.0 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 66.7% | 25.0% | 25.0% | 12.5% | -134.4 | 0.46 | 1.38 | +328.6 | +467.2 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 10.0% | -209.8 | 0.30 | 1.22 | +301.8 | +293.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 66.7% | 25.0% | 25.0% | 12.5% | -75.9 | 0.60 | 1.81 | +357.3 | +336.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -303.2 | 0.20 | 1.01 | +265.9 | +362.8 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 14.3% | -419.7 | 0.23 | 1.38 | +281.9 | +298.9 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 66.7% | 25.0% | 25.0% | 12.5% | -134.4 | 0.46 | 1.38 | +328.6 | +467.2 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-109.0; validation N=3 Fav=66.7% Avg=+242.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -639.9 | 0.13 | 0.57 | +307.9 | +225.7 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -639.9 | 0.13 | 0.57 | +307.9 | +225.7 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -639.9 | 0.13 | 0.57 | +307.9 | +225.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -639.9 | 0.13 | 0.57 | +307.9 | +225.7 |
| `confluence_gte_60` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 18.2% | -698.1 | 0.13 | 0.57 | +287.1 | +205.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -1212.3 | 0.00 | 0.00 | +174.3 | +184.7 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 18.2% | -698.1 | 0.13 | 0.57 | +287.1 | +205.5 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -639.9 | 0.13 | 0.57 | +307.9 | +225.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -1212.3 | 0.00 | 0.00 | +174.3 | +184.7 |
| `feature_fresh_reclaim_within_8` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -564.2 | 0.00 | 0.00 | +179.8 | +253.2 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 25.0% | -639.9 | 0.13 | 0.57 | +307.9 | +225.7 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 41.7% | 40.0% | 40.0% | 60.0% | +101.6 | 1.82 | 1.82 | +506.2 | +357.4 |
| `feature_eurjpy_tdi50_reclaim` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 18.2% | -698.1 | 0.13 | 0.57 | +287.1 | +205.5 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=15 Fav=26.7% Avg=-81.7; validation N=4 Fav=25.0% Avg=-181.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 16.2% | 24.3% | 18.9% | -532.2 | 0.10 | 0.28 | +232.3 | +234.7 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 83.8% | 19.4% | 29.0% | 19.4% | -590.8 | 0.10 | 0.24 | +253.0 | +228.7 |
| `hunt_to_ar_ratio_le_2_5` | 32 | S_STRANGER | 86.5% | 18.8% | 28.1% | 18.8% | -581.9 | 0.10 | 0.25 | +248.0 | +224.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 37 | S_STRANGER | 100.0% | 16.2% | 24.3% | 18.9% | -532.2 | 0.10 | 0.28 | +232.3 | +234.7 |
| `confluence_gte_60` | 12 | S_STRANGER | 32.4% | 25.0% | 33.3% | 25.0% | -99.3 | 0.47 | 0.95 | +280.2 | +289.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 18.9% | 0.0% | 14.3% | 28.6% | -513.7 | 0.03 | 0.11 | +175.3 | +155.9 |
| `tdi_rsi_gte_50` | 27 | S_STRANGER | 73.0% | 11.1% | 18.5% | 14.8% | -684.9 | 0.05 | 0.21 | +184.7 | +192.3 |
| `ratio_le_2_and_asian_gte_30` | 31 | S_STRANGER | 83.8% | 19.4% | 29.0% | 19.4% | -590.8 | 0.10 | 0.24 | +253.0 | +228.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 10.8% | 0.0% | 25.0% | 25.0% | -789.2 | 0.03 | 0.06 | +242.7 | +140.0 |
| `feature_fresh_reclaim_within_8` | 16 | S_STRANGER | 43.2% | 0.0% | 18.8% | 6.2% | -884.8 | 0.03 | 0.13 | +165.9 | +158.2 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 36 | S_STRANGER | 97.3% | 16.7% | 25.0% | 16.7% | -546.9 | 0.10 | 0.28 | +234.2 | +239.4 |
| `feature_momentum_breakout_exception` | 19 | S_STRANGER | 51.4% | 26.3% | 26.3% | 31.6% | -102.6 | 0.44 | 1.07 | +317.5 | +330.5 |
| `feature_eurjpy_tdi50_reclaim` | 27 | S_STRANGER | 73.0% | 11.1% | 18.5% | 14.8% | -684.9 | 0.05 | 0.21 | +184.7 | +192.3 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=50.0% Avg=+207.8; out_of_sample N=12 Fav=33.3% Avg=+534.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 44 | S_STRANGER | 100.0% | 15.9% | 22.7% | 15.9% | -1028.4 | 0.30 | 0.98 | +954.4 | +510.2 |
| `hunt_to_ar_ratio_le_2_0` | 42 | S_STRANGER | 95.5% | 16.7% | 23.8% | 16.7% | -780.3 | 0.37 | 1.14 | +994.2 | +501.8 |
| `hunt_to_ar_ratio_le_2_5` | 44 | S_STRANGER | 100.0% | 15.9% | 22.7% | 15.9% | -1028.4 | 0.30 | 0.98 | +954.4 | +510.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 44 | S_STRANGER | 100.0% | 15.9% | 22.7% | 15.9% | -1028.4 | 0.30 | 0.98 | +954.4 | +510.2 |
| `confluence_gte_60` | 42 | S_STRANGER | 95.5% | 16.7% | 23.8% | 16.7% | -1023.7 | 0.31 | 0.95 | +920.3 | +494.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 29.5% | 0.0% | 7.7% | 0.0% | -3324.3 | 0.01 | 0.09 | +333.8 | +345.7 |
| `tdi_rsi_gte_50` | 35 | S_STRANGER | 79.5% | 8.6% | 14.3% | 8.6% | -1593.9 | 0.09 | 0.49 | +595.1 | +460.0 |
| `ratio_le_2_and_asian_gte_30` | 42 | S_STRANGER | 95.5% | 16.7% | 23.8% | 16.7% | -780.3 | 0.37 | 1.14 | +994.2 | +501.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 25.0% | 0.0% | 9.1% | 0.0% | -2766.1 | 0.01 | 0.11 | +372.8 | +278.1 |
| `feature_fresh_reclaim_within_8` | 25 | S_STRANGER | 56.8% | 8.0% | 20.0% | 8.0% | -1674.6 | 0.15 | 0.60 | +746.3 | +411.1 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 44 | S_STRANGER | 100.0% | 15.9% | 22.7% | 15.9% | -1028.4 | 0.30 | 0.98 | +954.4 | +510.2 |
| `feature_momentum_breakout_exception` | 18 | S_STRANGER | 40.9% | 38.9% | 38.9% | 38.9% | +425.7 | 2.15 | 3.37 | +1365.0 | +710.3 |
| `feature_eurjpy_tdi50_reclaim` | 35 | S_STRANGER | 79.5% | 8.6% | 14.3% | 8.6% | -1593.9 | 0.09 | 0.49 | +595.1 | +460.0 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=+12.0; validation N=15 Fav=13.3% Avg=-78.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 15.8% | 26.3% | 10.5% | -74.6 | 0.59 | 1.65 | +270.8 | +311.5 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 100.0% | 15.8% | 26.3% | 10.5% | -74.6 | 0.59 | 1.65 | +270.8 | +311.5 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 15.8% | 26.3% | 10.5% | -74.6 | 0.59 | 1.65 | +270.8 | +311.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 19 | S_STRANGER | 100.0% | 15.8% | 26.3% | 10.5% | -74.6 | 0.59 | 1.65 | +270.8 | +311.5 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 15.8% | 26.3% | 10.5% | -74.6 | 0.59 | 1.65 | +270.8 | +311.5 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 15.8% | 26.3% | 10.5% | -74.6 | 0.59 | 1.65 | +270.8 | +311.5 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 42.1% | 12.5% | 25.0% | 0.0% | -182.6 | 0.22 | 0.66 | +297.0 | +369.1 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 31.6% | 16.7% | 16.7% | 0.0% | -179.0 | 0.13 | 0.66 | +196.0 | +270.8 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 100.0% | 15.8% | 26.3% | 10.5% | -74.6 | 0.59 | 1.65 | +270.8 | +311.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 42.1% | 12.5% | 25.0% | 0.0% | -182.6 | 0.22 | 0.66 | +297.0 | +369.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 15.8% | 26.3% | 10.5% | -74.6 | 0.59 | 1.65 | +270.8 | +311.5 |
| `feature_momentum_breakout_exception` | 18 | S_STRANGER | 94.7% | 16.7% | 27.8% | 11.1% | -63.6 | 0.64 | 1.66 | +280.5 | +305.8 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 31.6% | 16.7% | 16.7% | 0.0% | -179.0 | 0.13 | 0.66 | +196.0 | +270.8 |

### STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+412.0; validation N=5 Fav=40.0% Avg=+354.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 57 | S_STRANGER | 100.0% | 15.8% | 26.3% | 17.5% | -212.4 | 0.42 | 1.15 | +340.1 | +251.4 |
| `hunt_to_ar_ratio_le_2_0` | 55 | S_STRANGER | 96.5% | 16.4% | 27.3% | 18.2% | -216.2 | 0.43 | 1.11 | +349.6 | +254.7 |
| `hunt_to_ar_ratio_le_2_5` | 55 | S_STRANGER | 96.5% | 16.4% | 27.3% | 18.2% | -216.2 | 0.43 | 1.11 | +349.6 | +254.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 57 | S_STRANGER | 100.0% | 15.8% | 26.3% | 17.5% | -212.4 | 0.42 | 1.15 | +340.1 | +251.4 |
| `confluence_gte_60` | 11 | S_STRANGER | 19.3% | 45.5% | 72.7% | 54.5% | +385.6 | 8.49 | 3.19 | +595.3 | +163.5 |
| `confluence_gte_70` | 4 | R_REPEATER | 7.0% | 50.0% | 75.0% | 50.0% | +623.9 | 47.21 | 15.74 | +783.5 | +188.0 |
| `tdi_rsi_gt_signal` | 27 | S_STRANGER | 47.4% | 14.8% | 25.9% | 14.8% | -374.9 | 0.11 | 0.31 | +223.6 | +211.4 |
| `tdi_rsi_gte_50` | 35 | S_STRANGER | 61.4% | 8.6% | 22.9% | 14.3% | -443.4 | 0.08 | 0.25 | +203.5 | +194.5 |
| `ratio_le_2_and_asian_gte_30` | 55 | S_STRANGER | 96.5% | 16.4% | 27.3% | 18.2% | -216.2 | 0.43 | 1.11 | +349.6 | +254.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 26 | S_STRANGER | 45.6% | 15.4% | 26.9% | 15.4% | -387.2 | 0.11 | 0.30 | +231.8 | +214.0 |
| `feature_fresh_reclaim_within_8` | 18 | S_STRANGER | 31.6% | 0.0% | 11.1% | 5.6% | -334.4 | 0.02 | 0.12 | +178.1 | +268.6 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 57 | S_STRANGER | 100.0% | 15.8% | 26.3% | 17.5% | -212.4 | 0.42 | 1.15 | +340.1 | +251.4 |
| `feature_momentum_breakout_exception` | 33 | S_STRANGER | 57.9% | 27.3% | 30.3% | 30.3% | +73.2 | 1.42 | 3.13 | +481.2 | +316.4 |
| `feature_eurjpy_tdi50_reclaim` | 35 | S_STRANGER | 61.4% | 8.6% | 22.9% | 14.3% | -443.4 | 0.08 | 0.25 | +203.5 | +194.5 |

### RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-231.3; validation N=2 Fav=50.0% Avg=+754.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 15.4% | -54.0 | 0.70 | 2.11 | +336.4 | +311.8 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 15.4% | -54.0 | 0.70 | 2.11 | +336.4 | +311.8 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 15.4% | -54.0 | 0.70 | 2.11 | +336.4 | +311.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 15.4% | -54.0 | 0.70 | 2.11 | +336.4 | +311.8 |
| `confluence_gte_60` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 40.0% | +162.9 | 2.10 | 6.29 | +482.2 | +262.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 33.3% | -52.0 | 0.33 | 0.33 | +380.7 | +147.0 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 10.0% | -224.3 | 0.03 | 0.27 | +256.5 | +334.7 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 15.4% | -54.0 | 0.70 | 2.11 | +336.4 | +311.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 33.3% | -52.0 | 0.33 | 0.33 | +380.7 | +147.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 15.4% | -54.0 | 0.70 | 2.11 | +336.4 | +311.8 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 76.9% | 10.0% | 20.0% | 20.0% | +26.3 | 1.20 | 4.19 | +363.0 | +268.2 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 10.0% | -224.3 | 0.03 | 0.27 | +256.5 | +334.7 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-146.0; validation N=6 Fav=33.3% Avg=+43.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 40 | S_STRANGER | 100.0% | 15.0% | 25.0% | 15.0% | -496.4 | 0.28 | 0.81 | +541.7 | +312.9 |
| `hunt_to_ar_ratio_le_2_0` | 34 | S_STRANGER | 85.0% | 17.6% | 26.5% | 17.6% | -185.4 | 0.54 | 1.43 | +587.8 | +294.5 |
| `hunt_to_ar_ratio_le_2_5` | 34 | S_STRANGER | 85.0% | 17.6% | 26.5% | 17.6% | -185.4 | 0.54 | 1.43 | +587.8 | +294.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 40 | S_STRANGER | 100.0% | 15.0% | 25.0% | 15.0% | -496.4 | 0.28 | 0.81 | +541.7 | +312.9 |
| `confluence_gte_60` | 22 | S_STRANGER | 55.0% | 13.6% | 27.3% | 9.1% | -355.8 | 0.38 | 1.01 | +560.6 | +344.7 |
| `confluence_gte_70` | 5 | S_STRANGER | 12.5% | 20.0% | 20.0% | 0.0% | -114.6 | 0.12 | 0.47 | +669.4 | +274.4 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 20.0% | 25.0% | 25.0% | 25.0% | -29.3 | 0.89 | 2.67 | +537.1 | +204.7 |
| `tdi_rsi_gte_50` | 29 | S_STRANGER | 72.5% | 13.8% | 20.7% | 13.8% | -756.7 | 0.16 | 0.59 | +395.9 | +309.2 |
| `ratio_le_2_and_asian_gte_30` | 34 | S_STRANGER | 85.0% | 17.6% | 26.5% | 17.6% | -185.4 | 0.54 | 1.43 | +587.8 | +294.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 17.5% | 28.6% | 28.6% | 28.6% | +16.1 | 1.06 | 2.66 | +588.6 | +218.6 |
| `feature_fresh_reclaim_within_8` | 15 | S_STRANGER | 37.5% | 0.0% | 13.3% | 13.3% | -1303.9 | 0.16 | 0.94 | +576.3 | +351.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 39 | S_STRANGER | 97.5% | 15.4% | 25.6% | 15.4% | -500.3 | 0.28 | 0.79 | +551.0 | +318.1 |
| `feature_momentum_breakout_exception` | 26 | S_STRANGER | 65.0% | 23.1% | 30.8% | 23.1% | +68.2 | 1.36 | 2.89 | +649.2 | +369.1 |
| `feature_eurjpy_tdi50_reclaim` | 29 | S_STRANGER | 72.5% | 13.8% | 20.7% | 13.8% | -756.7 | 0.16 | 0.59 | +395.9 | +309.2 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-183.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=3 Fav=33.3% Avg=+160.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 28.6% | -357.2 | 0.24 | 0.64 | +631.2 | +442.9 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 85.7% | 8.3% | 16.7% | 16.7% | -515.9 | 0.06 | 0.23 | +495.1 | +471.1 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 15.4% | 23.1% | 23.1% | -384.7 | 0.24 | 0.64 | +636.6 | +445.6 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 28.6% | -357.2 | 0.24 | 0.64 | +631.2 | +442.9 |
| `confluence_gte_60` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 60.0% | +23.2 | 1.11 | 2.22 | +695.4 | +428.2 |
| `confluence_gte_70` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 100.0% | +595.0 | 999.00 | 999.00 | +1283.0 | +140.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 57.1% | 0.0% | 12.5% | 25.0% | -527.8 | 0.03 | 0.15 | +214.4 | +442.7 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 57.1% | 0.0% | 12.5% | 25.0% | -665.2 | 0.02 | 0.12 | +389.1 | +397.6 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 85.7% | 8.3% | 16.7% | 16.7% | -515.9 | 0.06 | 0.23 | +495.1 | +471.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 50.0% | 0.0% | 14.3% | 14.3% | -603.1 | 0.03 | 0.15 | +164.9 | +447.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 21.4% | 28.6% | -357.2 | 0.24 | 0.64 | +631.2 | +442.9 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 78.6% | 18.2% | 18.2% | 36.4% | -38.7 | 0.77 | 2.32 | +634.9 | +458.5 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 57.1% | 0.0% | 12.5% | 25.0% | -665.2 | 0.02 | 0.12 | +389.1 | +397.6 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=37.5% Avg=-18.6; validation N=10 Fav=10.0% Avg=-137.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 14.3% | 25.0% | 14.3% | -410.1 | 0.12 | 0.32 | +218.3 | +265.7 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 92.9% | 15.4% | 26.9% | 11.5% | -343.5 | 0.15 | 0.38 | +201.9 | +236.3 |
| `hunt_to_ar_ratio_le_2_5` | 28 | S_STRANGER | 100.0% | 14.3% | 25.0% | 14.3% | -410.1 | 0.12 | 0.32 | +218.3 | +265.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 28 | S_STRANGER | 100.0% | 14.3% | 25.0% | 14.3% | -410.1 | 0.12 | 0.32 | +218.3 | +265.7 |
| `confluence_gte_60` | 20 | S_STRANGER | 71.4% | 15.0% | 30.0% | 15.0% | -513.6 | 0.12 | 0.24 | +236.5 | +270.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 22 | S_STRANGER | 78.6% | 13.6% | 27.3% | 18.2% | -453.5 | 0.12 | 0.29 | +227.3 | +245.6 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 50.0% | 7.1% | 28.6% | 7.1% | -723.3 | 0.08 | 0.19 | +168.4 | +198.9 |
| `ratio_le_2_and_asian_gte_30` | 26 | S_STRANGER | 92.9% | 15.4% | 26.9% | 11.5% | -343.5 | 0.15 | 0.38 | +201.9 | +236.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 20 | S_STRANGER | 71.4% | 15.0% | 30.0% | 15.0% | -371.3 | 0.16 | 0.34 | +206.9 | +205.4 |
| `feature_fresh_reclaim_within_8` | 6 | S_STRANGER | 21.4% | 16.7% | 33.3% | 16.7% | -803.1 | 0.08 | 0.15 | +194.7 | +116.3 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 14.3% | 25.0% | 14.3% | -410.1 | 0.12 | 0.32 | +218.3 | +265.7 |
| `feature_momentum_breakout_exception` | 18 | S_STRANGER | 64.3% | 22.2% | 22.2% | 22.2% | -84.4 | 0.37 | 1.11 | +244.5 | +320.8 |
| `feature_eurjpy_tdi50_reclaim` | 14 | S_STRANGER | 50.0% | 7.1% | 28.6% | 7.1% | -723.3 | 0.08 | 0.19 | +168.4 | +198.9 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=16.7% Avg=-302.7; out_of_sample N=1 Fav=100.0% Avg=+1113.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -1245.8 | 0.08 | 0.49 | +333.4 | +487.2 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 15.4% | -1041.9 | 0.10 | 0.56 | +341.0 | +518.6 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 15.4% | -1041.9 | 0.10 | 0.56 | +341.0 | +518.6 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -1245.8 | 0.08 | 0.49 | +333.4 | +487.2 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -1245.8 | 0.08 | 0.49 | +333.4 | +487.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 14.3% | -794.0 | 0.07 | 0.44 | +321.0 | +552.0 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 15.4% | -1318.3 | 0.08 | 0.46 | +297.2 | +491.5 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 15.4% | -1041.9 | 0.10 | 0.56 | +341.0 | +518.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 14.3% | -794.0 | 0.07 | 0.44 | +321.0 | +552.0 |
| `feature_fresh_reclaim_within_8` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -2360.3 | 0.00 | 0.00 | +173.7 | +356.3 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -1245.8 | 0.08 | 0.49 | +333.4 | +487.2 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 50.0% | 28.6% | 28.6% | 28.6% | -100.4 | 0.69 | 1.72 | +539.3 | +471.4 |
| `feature_eurjpy_tdi50_reclaim` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 15.4% | -1318.3 | 0.08 | 0.46 | +297.2 | +491.5 |

### STOP_HUNT|BUY|EARLY_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|BUY|EARLY_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=22.2% Avg=-163.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 13.3% | -186.3 | 0.12 | 0.48 | +160.0 | +228.5 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 60.0% | 22.2% | 22.2% | 22.2% | -163.9 | 0.19 | 0.67 | +148.1 | +209.3 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 66.7% | 20.0% | 20.0% | 20.0% | -192.7 | 0.15 | 0.61 | +137.1 | +246.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 13.3% | -186.3 | 0.12 | 0.48 | +160.0 | +228.5 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 13.3% | -186.3 | 0.12 | 0.48 | +160.0 | +228.5 |
| `confluence_gte_70` | 6 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -289.7 | 0.00 | 0.00 | +171.5 | +305.7 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 20.0% | 33.3% | 33.3% | 33.3% | -47.0 | 0.57 | 1.13 | +335.7 | +177.0 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 0.0% | -303.0 | 0.00 | 0.00 | +216.8 | +402.7 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 60.0% | 22.2% | 22.2% | 22.2% | -163.9 | 0.19 | 0.67 | +148.1 | +209.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 50.0% | -0.5 | 0.99 | 0.99 | +175.5 | +124.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 13.3% | -186.3 | 0.12 | 0.48 | +160.0 | +228.5 |
| `feature_momentum_breakout_exception` | 15 | S_STRANGER | 100.0% | 13.3% | 20.0% | 13.3% | -186.3 | 0.12 | 0.48 | +160.0 | +228.5 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 26.7% | 0.0% | 0.0% | 0.0% | -303.0 | 0.00 | 0.00 | +216.8 | +402.7 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=+0.0; validation N=25 Fav=16.0% Avg=-233.7; out_of_sample N=10 Fav=20.0% Avg=-30.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 45 | S_STRANGER | 100.0% | 13.3% | 20.0% | 22.2% | -303.6 | 0.27 | 0.95 | +487.0 | +497.9 |
| `hunt_to_ar_ratio_le_2_0` | 45 | S_STRANGER | 100.0% | 13.3% | 20.0% | 22.2% | -303.6 | 0.27 | 0.95 | +487.0 | +497.9 |
| `hunt_to_ar_ratio_le_2_5` | 45 | S_STRANGER | 100.0% | 13.3% | 20.0% | 22.2% | -303.6 | 0.27 | 0.95 | +487.0 | +497.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 45 | S_STRANGER | 100.0% | 13.3% | 20.0% | 22.2% | -303.6 | 0.27 | 0.95 | +487.0 | +497.9 |
| `confluence_gte_60` | 28 | S_STRANGER | 62.2% | 10.7% | 17.9% | 17.9% | -456.7 | 0.10 | 0.38 | +356.0 | +479.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 46.7% | 9.5% | 19.0% | 23.8% | -241.2 | 0.29 | 1.01 | +398.0 | +473.0 |
| `tdi_rsi_gte_50` | 27 | S_STRANGER | 60.0% | 7.4% | 14.8% | 22.2% | -452.7 | 0.11 | 0.51 | +360.7 | +471.7 |
| `ratio_le_2_and_asian_gte_30` | 45 | S_STRANGER | 100.0% | 13.3% | 20.0% | 22.2% | -303.6 | 0.27 | 0.95 | +487.0 | +497.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 21 | S_STRANGER | 46.7% | 9.5% | 19.0% | 23.8% | -241.2 | 0.29 | 1.01 | +398.0 | +473.0 |
| `feature_fresh_reclaim_within_8` | 12 | S_STRANGER | 26.7% | 8.3% | 8.3% | 16.7% | -780.4 | 0.07 | 0.71 | +468.4 | +487.3 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 45 | S_STRANGER | 100.0% | 13.3% | 20.0% | 22.2% | -303.6 | 0.27 | 0.95 | +487.0 | +497.9 |
| `feature_momentum_breakout_exception` | 36 | S_STRANGER | 80.0% | 16.7% | 22.2% | 27.8% | -170.9 | 0.45 | 1.28 | +545.2 | +562.7 |
| `feature_eurjpy_tdi50_reclaim` | 27 | S_STRANGER | 60.0% | 7.4% | 14.8% | 22.2% | -452.7 | 0.11 | 0.51 | +360.7 | +471.7 |

### STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=-130.0; validation N=9 Fav=22.2% Avg=-175.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | -578.7 | 0.07 | 0.30 | +225.3 | +370.8 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | -578.7 | 0.07 | 0.30 | +225.3 | +370.8 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | -578.7 | 0.07 | 0.30 | +225.3 | +370.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | -578.7 | 0.07 | 0.30 | +225.3 | +370.8 |
| `confluence_gte_60` | 2 | S_STRANGER | 8.7% | 0.0% | 0.0% | 0.0% | -85.0 | 0.00 | 0.00 | +354.5 | +997.0 |
| `confluence_gte_70` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -12.0 | 0.00 | 0.00 | +110.0 | +883.0 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 43.5% | 20.0% | 30.0% | 20.0% | -131.0 | 0.40 | 0.94 | +216.5 | +321.5 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 73.9% | 17.6% | 23.5% | 17.6% | -648.5 | 0.08 | 0.25 | +221.1 | +241.0 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | -578.7 | 0.07 | 0.30 | +225.3 | +370.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 43.5% | 20.0% | 30.0% | 20.0% | -131.0 | 0.40 | 0.94 | +216.5 | +321.5 |
| `feature_fresh_reclaim_within_8` | 7 | S_STRANGER | 30.4% | 14.3% | 14.3% | 14.3% | -988.3 | 0.02 | 0.09 | +223.6 | +268.6 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | -578.7 | 0.07 | 0.30 | +225.3 | +370.8 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 56.5% | 23.1% | 23.1% | 30.8% | -161.7 | 0.29 | 0.78 | +273.5 | +436.5 |
| `feature_eurjpy_tdi50_reclaim` | 17 | S_STRANGER | 73.9% | 17.6% | 23.5% | 17.6% | -648.5 | 0.08 | 0.25 | +221.1 | +241.0 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-203.5; validation N=6 Fav=33.3% Avg=-247.8; out_of_sample N=5 Fav=40.0% Avg=+647.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 12.5% | 18.8% | 15.6% | -1085.9 | 0.12 | 0.54 | +440.7 | +311.8 |
| `hunt_to_ar_ratio_le_2_0` | 32 | S_STRANGER | 100.0% | 12.5% | 18.8% | 15.6% | -1085.9 | 0.12 | 0.54 | +440.7 | +311.8 |
| `hunt_to_ar_ratio_le_2_5` | 32 | S_STRANGER | 100.0% | 12.5% | 18.8% | 15.6% | -1085.9 | 0.12 | 0.54 | +440.7 | +311.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 32 | S_STRANGER | 100.0% | 12.5% | 18.8% | 15.6% | -1085.9 | 0.12 | 0.54 | +440.7 | +311.8 |
| `confluence_gte_60` | 32 | S_STRANGER | 100.0% | 12.5% | 18.8% | 15.6% | -1085.9 | 0.12 | 0.54 | +440.7 | +311.8 |
| `confluence_gte_70` | 3 | S_STRANGER | 9.4% | 0.0% | 0.0% | 0.0% | -354.0 | 0.00 | 0.00 | +98.0 | +297.3 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 34.4% | 9.1% | 18.2% | 9.1% | -1296.2 | 0.04 | 0.18 | +261.1 | +227.6 |
| `tdi_rsi_gte_50` | 30 | S_STRANGER | 93.8% | 10.0% | 16.7% | 13.3% | -1162.5 | 0.11 | 0.55 | +419.5 | +301.8 |
| `ratio_le_2_and_asian_gte_30` | 32 | S_STRANGER | 100.0% | 12.5% | 18.8% | 15.6% | -1085.9 | 0.12 | 0.54 | +440.7 | +311.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 34.4% | 9.1% | 18.2% | 9.1% | -1296.2 | 0.04 | 0.18 | +261.1 | +227.6 |
| `feature_fresh_reclaim_within_8` | 17 | S_STRANGER | 53.1% | 5.9% | 5.9% | 5.9% | -1628.6 | 0.05 | 0.74 | +341.1 | +215.8 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 12.5% | 18.8% | 15.6% | -1085.9 | 0.12 | 0.54 | +440.7 | +311.8 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 40.6% | 30.8% | 46.2% | 38.5% | +103.5 | 1.38 | 1.61 | +722.6 | +458.8 |
| `feature_eurjpy_tdi50_reclaim` | 30 | S_STRANGER | 93.8% | 10.0% | 16.7% | 13.3% | -1162.5 | 0.11 | 0.55 | +419.5 | +301.8 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=18.2% Avg=-43.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -144.9 | 0.30 | 2.27 | +172.2 | +198.6 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -144.9 | 0.30 | 2.27 | +172.2 | +198.6 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -144.9 | 0.30 | 2.27 | +172.2 | +198.6 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -144.9 | 0.30 | 2.27 | +172.2 | +198.6 |
| `confluence_gte_60` | 10 | S_STRANGER | 58.8% | 10.0% | 10.0% | 10.0% | -123.4 | 0.42 | 3.80 | +194.7 | +173.4 |
| `confluence_gte_70` | 1 | R_RUNNER | 5.9% | 100.0% | 100.0% | 100.0% | +902.5 | 999.00 | 999.00 | +911.0 | +14.0 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 14.3% | -49.1 | 0.72 | 4.35 | +188.7 | +173.0 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 58.8% | 10.0% | 10.0% | 10.0% | -112.3 | 0.45 | 4.01 | +158.9 | +170.1 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -144.9 | 0.30 | 2.27 | +172.2 | +198.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 14.3% | -49.1 | 0.72 | 4.35 | +188.7 | +173.0 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -156.0 | 0.00 | 0.00 | +94.0 | +57.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 5.9% | -144.9 | 0.30 | 2.27 | +172.2 | +198.6 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 64.7% | 18.2% | 18.2% | 9.1% | -43.8 | 0.69 | 3.11 | +229.7 | +244.0 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 58.8% | 10.0% | 10.0% | 10.0% | -112.3 | 0.45 | 4.01 | +158.9 | +170.1 |

### STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+579.0; validation N=4 Fav=50.0% Avg=-470.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 36 | S_STRANGER | 100.0% | 11.1% | 13.9% | 5.6% | -1445.6 | 0.05 | 0.30 | +257.1 | +232.5 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 83.3% | 13.3% | 16.7% | 6.7% | -1204.6 | 0.07 | 0.34 | +265.6 | +262.2 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 86.1% | 12.9% | 16.1% | 6.5% | -1192.3 | 0.07 | 0.34 | +264.4 | +254.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 36 | S_STRANGER | 100.0% | 11.1% | 13.9% | 5.6% | -1445.6 | 0.05 | 0.30 | +257.1 | +232.5 |
| `confluence_gte_60` | 3 | R_REPEATER | 8.3% | 66.7% | 66.7% | 0.0% | +257.0 | 1.71 | 0.85 | +970.3 | +56.0 |
| `confluence_gte_70` | 3 | R_REPEATER | 8.3% | 66.7% | 66.7% | 0.0% | +257.0 | 1.71 | 0.85 | +970.3 | +56.0 |
| `tdi_rsi_gt_signal` | 29 | S_STRANGER | 80.6% | 6.9% | 10.3% | 6.9% | -1438.0 | 0.02 | 0.15 | +187.1 | +172.7 |
| `tdi_rsi_gte_50` | 32 | S_STRANGER | 88.9% | 6.2% | 9.4% | 6.2% | -1604.9 | 0.01 | 0.14 | +189.2 | +164.3 |
| `ratio_le_2_and_asian_gte_30` | 30 | S_STRANGER | 83.3% | 13.3% | 16.7% | 6.7% | -1204.6 | 0.07 | 0.34 | +265.6 | +262.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 25 | S_STRANGER | 69.4% | 8.0% | 12.0% | 8.0% | -1182.8 | 0.02 | 0.18 | +187.4 | +181.5 |
| `feature_fresh_reclaim_within_8` | 31 | S_STRANGER | 86.1% | 6.5% | 9.7% | 6.5% | -1652.7 | 0.01 | 0.13 | +193.2 | +164.8 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 36 | S_STRANGER | 100.0% | 11.1% | 13.9% | 5.6% | -1445.6 | 0.05 | 0.30 | +257.1 | +232.5 |
| `feature_momentum_breakout_exception` | 7 | R_REPEATER | 19.4% | 57.1% | 57.1% | 28.6% | -20.7 | 0.95 | 0.71 | +591.4 | +467.7 |
| `feature_eurjpy_tdi50_reclaim` | 32 | S_STRANGER | 88.9% | 6.2% | 9.4% | 6.2% | -1604.9 | 0.01 | 0.14 | +189.2 | +164.3 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-47.0; validation N=6 Fav=16.7% Avg=-20.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -74.3 | 0.64 | 2.57 | +423.9 | +601.7 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 12.5% | 25.0% | 12.5% | -60.4 | 0.73 | 2.20 | +478.5 | +676.9 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 11.1% | 22.2% | 11.1% | -58.9 | 0.72 | 2.51 | +460.1 | +626.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -74.3 | 0.64 | 2.57 | +423.9 | +601.7 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -74.3 | 0.64 | 2.57 | +423.9 | +601.7 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -74.3 | 0.64 | 2.57 | +423.9 | +601.7 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -264.3 | 0.00 | 0.00 | +93.0 | +1129.0 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -74.3 | 0.64 | 2.57 | +423.9 | +601.7 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 80.0% | 12.5% | 25.0% | 12.5% | -60.4 | 0.73 | 2.20 | +478.5 | +676.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -264.3 | 0.00 | 0.00 | +93.0 | +1129.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 8 | S_STRANGER | 80.0% | 12.5% | 25.0% | 12.5% | -49.1 | 0.77 | 2.32 | +486.0 | +550.0 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 70.0% | 14.3% | 28.6% | 14.3% | -24.3 | 0.89 | 2.22 | +510.7 | +418.1 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 10.0% | -74.3 | 0.64 | 2.57 | +423.9 | +601.7 |

### STOP_HUNT|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-55.8; validation N=4 Fav=25.0% Avg=-18.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 20.0% | -143.6 | 0.52 | 1.82 | +341.4 | +470.0 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 11.1% | 22.2% | 22.2% | -39.3 | 0.81 | 2.44 | +368.0 | +323.2 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 11.1% | 22.2% | 22.2% | -39.3 | 0.81 | 2.44 | +368.0 | +323.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 20.0% | -143.6 | 0.52 | 1.82 | +341.4 | +470.0 |
| `confluence_gte_60` | 8 | S_STRANGER | 80.0% | 0.0% | 12.5% | 12.5% | -187.4 | 0.21 | 1.27 | +223.7 | +341.4 |
| `confluence_gte_70` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -300.5 | 0.00 | 0.00 | +273.5 | +444.5 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -462.5 | 0.00 | 0.00 | +180.5 | +539.5 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 14.3% | -389.7 | 0.00 | 0.00 | +191.6 | +596.7 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 11.1% | 22.2% | 22.2% | -39.3 | 0.81 | 2.44 | +368.0 | +323.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -462.5 | 0.00 | 0.00 | +180.5 | +539.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 20.0% | -143.6 | 0.52 | 1.82 | +341.4 | +470.0 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 20.0% | -143.6 | 0.52 | 1.82 | +341.4 | +470.0 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 14.3% | -389.7 | 0.00 | 0.00 | +191.6 | +596.7 |

### RRT_REVERSAL|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-358.0; validation N=8 Fav=12.5% Avg=-999.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -1131.4 | 0.04 | 0.40 | +190.3 | +181.9 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 0.0% | -1165.4 | 0.00 | 0.00 | +101.0 | +203.9 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 11.1% | -928.2 | 0.06 | 0.48 | +170.7 | +181.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -1131.4 | 0.04 | 0.40 | +190.3 | +181.9 |
| `confluence_gte_60` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -878.5 | 0.13 | 0.39 | +308.5 | +192.0 |
| `confluence_gte_70` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | -1052.0 | 0.14 | 0.29 | +398.7 | +130.7 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -981.3 | 0.00 | 0.00 | +108.2 | +213.3 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -358.0 | 0.00 | 0.00 | +38.0 | +376.0 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 0.0% | -1165.4 | 0.00 | 0.00 | +101.0 | +203.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 0.0% | -1032.4 | 0.00 | 0.00 | +85.2 | +250.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -1131.4 | 0.04 | 0.40 | +190.3 | +181.9 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -1131.4 | 0.04 | 0.40 | +190.3 | +181.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -358.0 | 0.00 | 0.00 | +38.0 | +376.0 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-150.0; validation N=4 Fav=25.0% Avg=-209.0; out_of_sample N=7 Fav=14.3% Avg=-843.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 10.0% | 10.0% | 15.0% | -1376.7 | 0.07 | 0.63 | +443.9 | +869.4 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 95.0% | 10.5% | 10.5% | 15.8% | -1075.3 | 0.10 | 0.77 | +467.3 | +895.7 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 10.0% | 10.0% | 15.0% | -1376.7 | 0.07 | 0.63 | +443.9 | +869.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 20 | S_STRANGER | 100.0% | 10.0% | 10.0% | 15.0% | -1376.7 | 0.07 | 0.63 | +443.9 | +869.4 |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 10.0% | 10.0% | 15.0% | -1376.7 | 0.07 | 0.63 | +443.9 | +869.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 35.0% | 14.3% | 14.3% | 14.3% | -1203.1 | 0.13 | 0.75 | +480.3 | +735.0 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 85.0% | 11.8% | 11.8% | 17.6% | -1376.6 | 0.09 | 0.60 | +496.5 | +572.8 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 95.0% | 10.5% | 10.5% | 15.8% | -1075.3 | 0.10 | 0.77 | +467.3 | +895.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 35.0% | 14.3% | 14.3% | 14.3% | -1203.1 | 0.13 | 0.75 | +480.3 | +735.0 |
| `feature_fresh_reclaim_within_8` | 8 | S_STRANGER | 40.0% | 12.5% | 12.5% | 25.0% | -1431.6 | 0.08 | 0.47 | +530.5 | +464.4 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 10.0% | 10.0% | 15.0% | -1376.7 | 0.07 | 0.63 | +443.9 | +869.4 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 60.0% | 16.7% | 16.7% | 25.0% | -573.9 | 0.24 | 1.08 | +618.3 | +1280.3 |
| `feature_eurjpy_tdi50_reclaim` | 17 | S_STRANGER | 85.0% | 11.8% | 11.8% | 17.6% | -1376.6 | 0.09 | 0.60 | +496.5 | +572.8 |

### STOP_HUNT|SELL|MID_WEEK|L2|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L2|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=25.0% Avg=-1399.0; out_of_sample N=4 Fav=0.0% Avg=-3985.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2269.4 | 0.03 | 0.26 | +369.9 | +568.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2269.4 | 0.03 | 0.26 | +369.9 | +568.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2269.4 | 0.03 | 0.26 | +369.9 | +568.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2269.4 | 0.03 | 0.26 | +369.9 | +568.9 |
| `confluence_gte_60` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | -541.5 | 0.39 | 0.39 | +516.5 | +529.5 |
| `confluence_gte_70` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +681.0 | 999.00 | 999.00 | +1020.0 | +318.0 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -4567.5 | 0.00 | 0.00 | +137.5 | +628.0 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 12.5% | -2692.1 | 0.03 | 0.21 | +311.1 | +421.8 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2269.4 | 0.03 | 0.26 | +369.9 | +568.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -4567.5 | 0.00 | 0.00 | +137.5 | +628.0 |
| `feature_fresh_reclaim_within_8` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -3341.2 | 0.00 | 0.00 | +213.8 | +452.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -2269.4 | 0.03 | 0.26 | +369.9 | +568.9 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 33.3% | -158.7 | 0.59 | 1.18 | +743.3 | +877.7 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 80.0% | 12.5% | 12.5% | 12.5% | -2692.1 | 0.03 | 0.21 | +311.1 | +421.8 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-5.0; validation N=9 Fav=0.0% Avg=-136.7; out_of_sample N=11 Fav=27.3% Avg=+69.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 9.7% | 12.9% | 9.7% | -483.4 | 0.24 | 1.56 | +695.9 | +536.9 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 96.8% | 10.0% | 13.3% | 10.0% | -467.7 | 0.25 | 1.58 | +719.1 | +509.5 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 100.0% | 9.7% | 12.9% | 9.7% | -483.4 | 0.24 | 1.56 | +695.9 | +536.9 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 31 | S_STRANGER | 100.0% | 9.7% | 12.9% | 9.7% | -483.4 | 0.24 | 1.56 | +695.9 | +536.9 |
| `confluence_gte_60` | 23 | S_STRANGER | 74.2% | 8.7% | 8.7% | 8.7% | -652.4 | 0.18 | 1.75 | +819.4 | +469.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 25 | S_STRANGER | 80.6% | 12.0% | 16.0% | 8.0% | -521.7 | 0.27 | 1.40 | +722.9 | +514.8 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 61.3% | 10.5% | 15.8% | 5.3% | -739.7 | 0.15 | 0.79 | +431.4 | +448.7 |
| `ratio_le_2_and_asian_gte_30` | 30 | S_STRANGER | 96.8% | 10.0% | 13.3% | 10.0% | -467.7 | 0.25 | 1.58 | +719.1 | +509.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 25 | S_STRANGER | 80.6% | 12.0% | 16.0% | 8.0% | -521.7 | 0.27 | 1.40 | +722.9 | +514.8 |
| `feature_fresh_reclaim_within_8` | 4 | S_STRANGER | 12.9% | 0.0% | 0.0% | 0.0% | -946.2 | 0.00 | 0.00 | +490.5 | +332.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 9.7% | 12.9% | 9.7% | -483.4 | 0.24 | 1.56 | +695.9 | +536.9 |
| `feature_momentum_breakout_exception` | 21 | S_STRANGER | 67.7% | 14.3% | 19.0% | 14.3% | -22.6 | 0.91 | 3.64 | +845.6 | +695.5 |
| `feature_eurjpy_tdi50_reclaim` | 19 | S_STRANGER | 61.3% | 10.5% | 15.8% | 5.3% | -739.7 | 0.15 | 0.79 | +431.4 | +448.7 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=0.0% Avg=-250.2; validation N=3 Fav=33.3% Avg=+219.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 27.3% | 18.2% | -52.8 | 0.64 | 1.28 | +259.0 | +214.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 72.7% | 12.5% | 25.0% | 25.0% | -74.1 | 0.57 | 1.15 | +211.8 | +212.3 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 81.8% | 11.1% | 22.2% | 22.2% | -83.3 | 0.52 | 1.29 | +189.6 | +209.4 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 9.1% | 27.3% | 18.2% | -52.8 | 0.64 | 1.28 | +259.0 | +214.0 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 27.3% | 18.2% | -52.8 | 0.64 | 1.28 | +259.0 | +214.0 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 27.3% | 18.2% | -52.8 | 0.64 | 1.28 | +259.0 | +214.0 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 63.6% | 0.0% | 14.3% | 28.6% | -125.1 | 0.21 | 0.82 | +214.6 | +242.1 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 45.5% | 0.0% | 40.0% | 0.0% | -22.4 | 0.80 | 1.20 | +332.8 | +217.4 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 72.7% | 12.5% | 25.0% | 25.0% | -74.1 | 0.57 | 1.15 | +211.8 | +212.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 50.0% | -222.0 | 0.00 | 0.00 | +86.7 | +259.7 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 18.2% | 0.0% | 50.0% | 0.0% | +84.5 | 3.96 | 3.96 | +571.5 | +234.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 27.3% | 18.2% | -52.8 | 0.64 | 1.28 | +259.0 | +214.0 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 81.8% | 11.1% | 22.2% | 22.2% | -83.1 | 0.52 | 1.29 | +265.1 | +226.1 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 45.5% | 0.0% | 40.0% | 0.0% | -22.4 | 0.80 | 1.20 | +332.8 | +217.4 |

### RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+10.7; validation N=4 Fav=0.0% Avg=+264.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 36.4% | 9.1% | -80.2 | 0.77 | 1.35 | +462.7 | +451.2 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 9.1% | 36.4% | 9.1% | -80.2 | 0.77 | 1.35 | +462.7 | +451.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 9.1% | 36.4% | 9.1% | -80.2 | 0.77 | 1.35 | +462.7 | +451.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 9.1% | 36.4% | 9.1% | -80.2 | 0.77 | 1.35 | +462.7 | +451.2 |
| `confluence_gte_60` | 7 | S_STRANGER | 63.6% | 0.0% | 42.9% | 0.0% | -97.9 | 0.69 | 0.92 | +316.1 | +313.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 63.6% | 14.3% | 57.1% | 14.3% | +155.7 | 1.58 | 1.18 | +588.7 | +384.6 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 36.4% | 0.0% | 25.0% | 0.0% | -439.5 | 0.07 | 0.21 | +229.8 | +596.5 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 9.1% | 36.4% | 9.1% | -80.2 | 0.77 | 1.35 | +462.7 | +451.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 63.6% | 14.3% | 57.1% | 14.3% | +155.7 | 1.58 | 1.18 | +588.7 | +384.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 36.4% | 9.1% | -80.2 | 0.77 | 1.35 | +462.7 | +451.2 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 81.8% | 11.1% | 44.4% | 11.1% | +57.6 | 1.21 | 1.51 | +499.2 | +303.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -700.0 | 0.00 | 0.00 | +298.5 | +1116.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-282.0; validation N=6 Fav=16.7% Avg=-212.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -182.7 | 0.19 | 1.74 | +266.1 | +455.5 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -182.7 | 0.19 | 1.74 | +266.1 | +455.5 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -182.7 | 0.19 | 1.74 | +266.1 | +455.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -182.7 | 0.19 | 1.74 | +266.1 | +455.5 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -182.7 | 0.19 | 1.74 | +266.1 | +455.5 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -182.7 | 0.19 | 1.74 | +266.1 | +455.5 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 12.5% | -229.6 | 0.21 | 1.46 | +296.5 | +559.6 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 14.3% | -329.6 | 0.00 | 0.00 | +283.9 | +597.7 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -182.7 | 0.19 | 1.74 | +266.1 | +455.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 12.5% | -229.6 | 0.21 | 1.46 | +296.5 | +559.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -182.7 | 0.19 | 1.74 | +266.1 | +455.5 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -182.7 | 0.19 | 1.74 | +266.1 | +455.5 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 14.3% | -329.6 | 0.00 | 0.00 | +283.9 | +597.7 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=9 Fav=11.1% Avg=-319.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 27.3% | 9.1% | -315.3 | 0.16 | 0.44 | +258.8 | +546.5 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 10.0% | 30.0% | 10.0% | -290.9 | 0.19 | 0.44 | +284.7 | +508.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 90.9% | 10.0% | 30.0% | 10.0% | -290.9 | 0.19 | 0.44 | +284.7 | +508.6 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 9.1% | 27.3% | 9.1% | -315.3 | 0.16 | 0.44 | +258.8 | +546.5 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 27.3% | 9.1% | -315.3 | 0.16 | 0.44 | +258.8 | +546.5 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 27.3% | 9.1% | -315.3 | 0.16 | 0.44 | +258.8 | +546.5 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 36.4% | 25.0% | 50.0% | 25.0% | -74.4 | 0.65 | 0.65 | +260.0 | +167.8 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 36.4% | 25.0% | 50.0% | 25.0% | -74.4 | 0.65 | 0.65 | +260.0 | +167.8 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 90.9% | 10.0% | 30.0% | 10.0% | -290.9 | 0.19 | 0.44 | +284.7 | +508.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 36.4% | 25.0% | 50.0% | 25.0% | -74.4 | 0.65 | 0.65 | +260.0 | +167.8 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -295.5 | 0.00 | 0.00 | +161.0 | +123.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 27.3% | 9.1% | -315.3 | 0.16 | 0.44 | +258.8 | +546.5 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 81.8% | 11.1% | 33.3% | 11.1% | -319.7 | 0.19 | 0.38 | +280.6 | +640.6 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 36.4% | 25.0% | 50.0% | 25.0% | -74.4 | 0.65 | 0.65 | +260.0 | +167.8 |

### THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-396.9; validation N=1 Fav=0.0% Avg=-568.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -336.0 | 0.00 | 0.04 | +223.5 | +325.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 22.2% | -227.9 | 0.01 | 0.06 | +248.3 | +335.8 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 22.2% | -227.9 | 0.01 | 0.06 | +248.3 | +335.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -336.0 | 0.00 | 0.04 | +223.5 | +325.4 |
| `confluence_gte_60` | 4 | S_STRANGER | 36.4% | 25.0% | 25.0% | 25.0% | -107.1 | 0.04 | 0.12 | +127.8 | +175.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 36.4% | 0.0% | 0.0% | 0.0% | -164.2 | 0.00 | 0.00 | +93.8 | +146.3 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 12.5% | -357.6 | 0.01 | 0.04 | +135.1 | +172.9 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 22.2% | -227.9 | 0.01 | 0.06 | +248.3 | +335.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -167.3 | 0.00 | 0.00 | +73.7 | +131.7 |
| `feature_fresh_reclaim_within_8` | 7 | S_STRANGER | 63.6% | 14.3% | 14.3% | 14.3% | -421.4 | 0.01 | 0.04 | +173.3 | +187.7 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 18.2% | -336.0 | 0.00 | 0.04 | +223.5 | +325.4 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 16.7% | -217.2 | 0.00 | 0.00 | +266.7 | +481.2 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 12.5% | -357.6 | 0.01 | 0.04 | +135.1 | +172.9 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=7 Fav=0.0% Avg=-1452.1; out_of_sample N=1 Fav=100.0% Avg=+572.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1721.3 | 0.03 | 0.29 | +314.9 | +170.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1721.3 | 0.03 | 0.29 | +314.9 | +170.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1721.3 | 0.03 | 0.29 | +314.9 | +170.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1721.3 | 0.03 | 0.29 | +314.9 | +170.0 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1721.3 | 0.03 | 0.29 | +314.9 | +170.0 |
| `confluence_gte_70` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -485.0 | 0.00 | 0.00 | +124.0 | +108.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 12.5% | -1199.1 | 0.06 | 0.39 | +385.2 | +220.4 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1721.3 | 0.03 | 0.29 | +314.9 | +170.0 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1721.3 | 0.03 | 0.29 | +314.9 | +170.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 12.5% | -1199.1 | 0.06 | 0.39 | +385.2 | +220.4 |
| `feature_fresh_reclaim_within_8` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 0.0% | -1452.1 | 0.00 | 0.00 | +312.4 | +234.4 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1721.3 | 0.03 | 0.29 | +314.9 | +170.0 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 27.3% | 33.3% | 33.3% | 33.3% | -119.5 | 0.61 | 1.23 | +485.3 | +431.0 |
| `feature_eurjpy_tdi50_reclaim` | 11 | S_STRANGER | 100.0% | 9.1% | 9.1% | 9.1% | -1721.3 | 0.03 | 0.29 | +314.9 | +170.0 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=18 Fav=11.1% Avg=-185.9; validation N=16 Fav=18.8% Avg=-139.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 56 | S_STRANGER | 100.0% | 8.9% | 19.6% | 8.9% | -236.3 | 0.25 | 0.98 | +278.8 | +328.9 |
| `hunt_to_ar_ratio_le_2_0` | 49 | S_STRANGER | 87.5% | 10.2% | 22.4% | 8.2% | -238.7 | 0.27 | 0.92 | +299.7 | +313.6 |
| `hunt_to_ar_ratio_le_2_5` | 50 | S_STRANGER | 89.3% | 10.0% | 22.0% | 8.0% | -240.7 | 0.27 | 0.93 | +295.2 | +320.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 56 | S_STRANGER | 100.0% | 8.9% | 19.6% | 8.9% | -236.3 | 0.25 | 0.98 | +278.8 | +328.9 |
| `confluence_gte_60` | 22 | S_STRANGER | 39.3% | 9.1% | 18.2% | 4.5% | -91.6 | 0.51 | 2.30 | +290.7 | +289.8 |
| `confluence_gte_70` | 3 | S_STRANGER | 5.4% | 0.0% | 0.0% | 0.0% | -42.7 | 0.00 | 0.00 | +118.3 | +256.0 |
| `tdi_rsi_gt_signal` | 32 | S_STRANGER | 57.1% | 6.2% | 18.8% | 9.4% | -213.0 | 0.26 | 1.04 | +266.7 | +285.2 |
| `tdi_rsi_gte_50` | 33 | S_STRANGER | 58.9% | 6.1% | 24.2% | 9.1% | -255.2 | 0.20 | 0.61 | +239.6 | +127.3 |
| `ratio_le_2_and_asian_gte_30` | 49 | S_STRANGER | 87.5% | 10.2% | 22.4% | 8.2% | -238.7 | 0.27 | 0.92 | +299.7 | +313.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 30 | S_STRANGER | 53.6% | 6.7% | 20.0% | 6.7% | -192.5 | 0.29 | 1.13 | +275.7 | +253.9 |
| `feature_fresh_reclaim_within_8` | 8 | S_STRANGER | 14.3% | 0.0% | 25.0% | 12.5% | -168.4 | 0.30 | 0.75 | +244.9 | +187.7 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 56 | S_STRANGER | 100.0% | 8.9% | 19.6% | 8.9% | -236.3 | 0.25 | 0.98 | +278.8 | +328.9 |
| `feature_momentum_breakout_exception` | 34 | S_STRANGER | 60.7% | 14.7% | 14.7% | 14.7% | -163.8 | 0.33 | 1.80 | +304.7 | +501.6 |
| `feature_eurjpy_tdi50_reclaim` | 33 | S_STRANGER | 58.9% | 6.1% | 24.2% | 9.1% | -255.2 | 0.20 | 0.61 | +239.6 | +127.3 |

### STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=14 Fav=14.3% Avg=+423.7; out_of_sample N=1 Fav=0.0% Avg=-920.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 8.3% | 20.8% | 12.5% | -176.3 | 0.75 | 2.71 | +936.3 | +594.2 |
| `hunt_to_ar_ratio_le_2_0` | 24 | S_STRANGER | 100.0% | 8.3% | 20.8% | 12.5% | -176.3 | 0.75 | 2.71 | +936.3 | +594.2 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 100.0% | 8.3% | 20.8% | 12.5% | -176.3 | 0.75 | 2.71 | +936.3 | +594.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 24 | S_STRANGER | 100.0% | 8.3% | 20.8% | 12.5% | -176.3 | 0.75 | 2.71 | +936.3 | +594.2 |
| `confluence_gte_60` | 11 | S_STRANGER | 45.8% | 9.1% | 18.2% | 9.1% | -521.1 | 0.33 | 1.47 | +645.1 | +703.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 33.3% | 12.5% | 25.0% | 12.5% | -450.0 | 0.27 | 0.80 | +453.8 | +562.5 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 79.2% | 5.3% | 21.1% | 10.5% | -503.2 | 0.26 | 0.89 | +497.7 | +377.2 |
| `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 100.0% | 8.3% | 20.8% | 12.5% | -176.3 | 0.75 | 2.71 | +936.3 | +594.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 33.3% | 12.5% | 25.0% | 12.5% | -450.0 | 0.27 | 0.80 | +453.8 | +562.5 |
| `feature_fresh_reclaim_within_8` | 9 | S_STRANGER | 37.5% | 0.0% | 22.2% | 0.0% | -1082.1 | 0.17 | 0.59 | +615.2 | +382.4 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 8.3% | 20.8% | 12.5% | -176.3 | 0.75 | 2.71 | +936.3 | +594.2 |
| `feature_momentum_breakout_exception` | 15 | S_STRANGER | 62.5% | 13.3% | 13.3% | 20.0% | +334.1 | 1.87 | 11.21 | +1123.2 | +746.2 |
| `feature_eurjpy_tdi50_reclaim` | 18 | S_STRANGER | 75.0% | 5.6% | 22.2% | 11.1% | -529.6 | 0.26 | 0.83 | +521.9 | +384.9 |

### THE_33_MW|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=-72.8; validation N=6 Fav=0.0% Avg=-494.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -253.5 | 0.25 | 1.14 | +232.9 | +450.8 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -253.5 | 0.25 | 1.14 | +232.9 | +450.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -253.5 | 0.25 | 1.14 | +232.9 | +450.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -253.5 | 0.25 | 1.14 | +232.9 | +450.8 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -253.5 | 0.25 | 1.14 | +232.9 | +450.8 |
| `confluence_gte_70` | 7 | S_STRANGER | 58.3% | 0.0% | 14.3% | 0.0% | -281.9 | 0.32 | 1.94 | +287.7 | +523.1 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 20.0% | -317.2 | 0.00 | 0.00 | +175.8 | +320.6 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 0.0% | 16.7% | 16.7% | -41.8 | 0.79 | 3.16 | +303.0 | +198.2 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -253.5 | 0.25 | 1.14 | +232.9 | +450.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 20.0% | -317.2 | 0.00 | 0.00 | +175.8 | +320.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -253.5 | 0.25 | 1.14 | +232.9 | +450.8 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 83.3% | 10.0% | 10.0% | 10.0% | -325.6 | 0.03 | 0.20 | +156.7 | +505.3 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 50.0% | 0.0% | 16.7% | 16.7% | -41.8 | 0.79 | 3.16 | +303.0 | +198.2 |

### RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-442.0; validation N=4 Fav=25.0% Avg=-202.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -260.3 | 0.26 | 2.59 | +456.8 | +483.7 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -260.3 | 0.26 | 2.59 | +456.8 | +483.7 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -260.3 | 0.26 | 2.59 | +456.8 | +483.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -260.3 | 0.26 | 2.59 | +456.8 | +483.7 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -260.3 | 0.26 | 2.59 | +456.8 | +483.7 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -260.3 | 0.26 | 2.59 | +456.8 | +483.7 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 25.0% | -101.0 | 0.73 | 2.19 | +613.5 | +429.8 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 20.0% | -250.2 | 0.47 | 1.86 | +630.0 | +625.8 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -260.3 | 0.26 | 2.59 | +456.8 | +483.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 25.0% | -101.0 | 0.73 | 2.19 | +613.5 | +429.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -260.3 | 0.26 | 2.59 | +456.8 | +483.7 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 16.7% | -260.3 | 0.26 | 2.59 | +456.8 | +483.7 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 20.0% | -250.2 | 0.47 | 1.86 | +630.0 | +625.8 |

### STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-1548.5; validation N=6 Fav=16.7% Avg=-1197.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -1092.8 | 0.03 | 0.13 | +341.9 | +257.3 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -1092.8 | 0.03 | 0.13 | +341.9 | +257.3 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -1092.8 | 0.03 | 0.13 | +341.9 | +257.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -1092.8 | 0.03 | 0.13 | +341.9 | +257.3 |
| `confluence_gte_60` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 12.5% | -1285.0 | 0.00 | 0.02 | +237.4 | +330.0 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 75.0% | 11.1% | 22.2% | 11.1% | -1339.9 | 0.03 | 0.10 | +263.8 | +299.8 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -1092.8 | 0.03 | 0.13 | +341.9 | +257.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 66.7% | 12.5% | 12.5% | 12.5% | -1285.0 | 0.00 | 0.02 | +237.4 | +330.0 |
| `feature_fresh_reclaim_within_8` | 4 | S_STRANGER | 33.3% | 25.0% | 50.0% | 25.0% | -670.5 | 0.11 | 0.11 | +361.5 | +184.2 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -1092.8 | 0.03 | 0.13 | +341.9 | +257.3 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 25.0% | -162.3 | 0.04 | 0.11 | +442.8 | +323.0 |
| `feature_eurjpy_tdi50_reclaim` | 9 | S_STRANGER | 75.0% | 11.1% | 22.2% | 11.1% | -1339.9 | 0.03 | 0.10 | +263.8 | +299.8 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=15 Fav=13.3% Avg=-412.3; out_of_sample N=6 Fav=16.7% Avg=+352.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 8.1% | 21.6% | 16.2% | -729.4 | 0.24 | 0.82 | +581.3 | +546.8 |
| `hunt_to_ar_ratio_le_2_0` | 35 | S_STRANGER | 94.6% | 8.6% | 22.9% | 14.3% | -714.9 | 0.26 | 0.83 | +564.1 | +482.7 |
| `hunt_to_ar_ratio_le_2_5` | 37 | S_STRANGER | 100.0% | 8.1% | 21.6% | 16.2% | -729.4 | 0.24 | 0.82 | +581.3 | +546.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 37 | S_STRANGER | 100.0% | 8.1% | 21.6% | 16.2% | -729.4 | 0.24 | 0.82 | +581.3 | +546.8 |
| `confluence_gte_60` | 11 | S_STRANGER | 29.7% | 0.0% | 18.2% | 0.0% | -799.3 | 0.15 | 0.67 | +448.8 | +599.8 |
| `confluence_gte_70` | 4 | S_STRANGER | 10.8% | 0.0% | 25.0% | 0.0% | -63.2 | 0.84 | 2.51 | +552.8 | +652.0 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 27.0% | 0.0% | 20.0% | 30.0% | -69.9 | 0.85 | 2.56 | +835.0 | +326.2 |
| `tdi_rsi_gte_50` | 30 | S_STRANGER | 81.1% | 6.7% | 23.3% | 16.7% | -792.8 | 0.24 | 0.72 | +598.3 | +484.1 |
| `ratio_le_2_and_asian_gte_30` | 35 | S_STRANGER | 94.6% | 8.6% | 22.9% | 14.3% | -714.9 | 0.26 | 0.83 | +564.1 | +482.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 24.3% | 0.0% | 22.2% | 22.2% | -77.7 | 0.85 | 2.56 | +774.2 | +266.7 |
| `feature_fresh_reclaim_within_8` | 17 | S_STRANGER | 45.9% | 0.0% | 23.5% | 0.0% | -722.9 | 0.17 | 0.57 | +401.3 | +368.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 8.1% | 21.6% | 16.2% | -729.4 | 0.24 | 0.82 | +581.3 | +546.8 |
| `feature_momentum_breakout_exception` | 21 | S_STRANGER | 56.8% | 14.3% | 19.0% | 28.6% | -193.7 | 0.60 | 2.24 | +680.7 | +782.4 |
| `feature_eurjpy_tdi50_reclaim` | 30 | S_STRANGER | 81.1% | 6.7% | 23.3% | 16.7% | -792.8 | 0.24 | 0.72 | +598.3 | +484.1 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=20.0% Avg=-33.1; out_of_sample N=11 Fav=18.2% Avg=-593.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 8.1% | 16.2% | 13.5% | -822.5 | 0.17 | 0.84 | +550.5 | +688.8 |
| `hunt_to_ar_ratio_le_2_0` | 37 | S_STRANGER | 100.0% | 8.1% | 16.2% | 13.5% | -822.5 | 0.17 | 0.84 | +550.5 | +688.8 |
| `hunt_to_ar_ratio_le_2_5` | 37 | S_STRANGER | 100.0% | 8.1% | 16.2% | 13.5% | -822.5 | 0.17 | 0.84 | +550.5 | +688.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 37 | S_STRANGER | 100.0% | 8.1% | 16.2% | 13.5% | -822.5 | 0.17 | 0.84 | +550.5 | +688.8 |
| `confluence_gte_60` | 37 | S_STRANGER | 100.0% | 8.1% | 16.2% | 13.5% | -822.5 | 0.17 | 0.84 | +550.5 | +688.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 43.2% | 18.8% | 31.2% | 18.8% | -418.6 | 0.47 | 1.03 | +637.7 | +489.6 |
| `tdi_rsi_gte_50` | 26 | S_STRANGER | 70.3% | 3.8% | 15.4% | 11.5% | -798.8 | 0.10 | 0.52 | +439.2 | +494.4 |
| `ratio_le_2_and_asian_gte_30` | 37 | S_STRANGER | 100.0% | 8.1% | 16.2% | 13.5% | -822.5 | 0.17 | 0.84 | +550.5 | +688.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 16 | S_STRANGER | 43.2% | 18.8% | 31.2% | 18.8% | -418.6 | 0.47 | 1.03 | +637.7 | +489.6 |
| `feature_fresh_reclaim_within_8` | 5 | S_STRANGER | 13.5% | 0.0% | 40.0% | 0.0% | -861.2 | 0.18 | 0.27 | +559.2 | +295.6 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 8.1% | 16.2% | 13.5% | -822.5 | 0.17 | 0.84 | +550.5 | +688.8 |
| `feature_momentum_breakout_exception` | 21 | S_STRANGER | 56.8% | 14.3% | 14.3% | 23.8% | -536.9 | 0.29 | 1.53 | +614.4 | +1033.5 |
| `feature_eurjpy_tdi50_reclaim` | 26 | S_STRANGER | 70.3% | 3.8% | 15.4% | 11.5% | -798.8 | 0.10 | 0.52 | +439.2 | +494.4 |

### STOP_HUNT|SELL|MID_WEEK|L3|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|NYC_REVERSAL|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=+10.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -351.9 | 0.12 | 1.40 | +209.9 | +425.5 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -351.9 | 0.12 | 1.40 | +209.9 | +425.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -351.9 | 0.12 | 1.40 | +209.9 | +425.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -351.9 | 0.12 | 1.40 | +209.9 | +425.5 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -351.9 | 0.12 | 1.40 | +209.9 | +425.5 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -351.9 | 0.12 | 1.40 | +209.9 | +425.5 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 20.0% | +10.6 | 1.10 | 4.38 | +254.0 | +263.0 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 20.0% | -183.6 | 0.40 | 1.59 | +225.0 | +198.2 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -351.9 | 0.12 | 1.40 | +209.9 | +425.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 20.0% | +10.6 | 1.10 | 4.38 | +254.0 | +263.0 |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -688.5 | 0.00 | 0.00 | +102.5 | +151.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -351.9 | 0.12 | 1.40 | +209.9 | +425.5 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 10.0% | -266.1 | 0.19 | 1.67 | +234.3 | +487.8 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 20.0% | -183.6 | 0.40 | 1.59 | +225.0 | +198.2 |

### STOP_HUNT|SELL|MID_WEEK|L2|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L2|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=12 Fav=8.3% Avg=-2127.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -1974.2 | 0.03 | 0.38 | +306.6 | +266.5 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -605.3 | 0.00 | 0.00 | +252.8 | +311.0 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -605.3 | 0.00 | 0.00 | +252.8 | +311.0 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -1974.2 | 0.03 | 0.38 | +306.6 | +266.5 |
| `confluence_gte_60` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -395.0 | 0.00 | 0.00 | +138.7 | +173.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -3089.0 | 0.00 | 0.00 | +183.2 | +192.3 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 92.3% | 8.3% | 8.3% | 8.3% | -2127.1 | 0.03 | 0.35 | +294.1 | +197.6 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -605.3 | 0.00 | 0.00 | +252.8 | +311.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -1017.5 | 0.00 | 0.00 | +245.5 | +163.5 |
| `feature_fresh_reclaim_within_8` | 8 | S_STRANGER | 61.5% | 0.0% | 0.0% | 0.0% | -2920.5 | 0.00 | 0.00 | +224.9 | +157.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 7.7% | -1974.2 | 0.03 | 0.38 | +306.6 | +266.5 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 50.0% | +351.5 | 6.06 | 6.06 | +899.5 | +740.5 |
| `feature_eurjpy_tdi50_reclaim` | 12 | S_STRANGER | 92.3% | 8.3% | 8.3% | 8.3% | -2127.1 | 0.03 | 0.35 | +294.1 | +197.6 |

### STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=-280.3; validation N=2 Fav=0.0% Avg=-185.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 7.4% | 14.8% | 3.7% | -349.3 | 0.12 | 0.68 | +245.8 | +296.6 |
| `hunt_to_ar_ratio_le_2_0` | 26 | S_STRANGER | 96.3% | 7.7% | 15.4% | 3.8% | -315.0 | 0.14 | 0.73 | +253.3 | +287.8 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 96.3% | 7.7% | 15.4% | 3.8% | -315.0 | 0.14 | 0.73 | +253.3 | +287.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 27 | S_STRANGER | 100.0% | 7.4% | 14.8% | 3.7% | -349.3 | 0.12 | 0.68 | +245.8 | +296.6 |
| `confluence_gte_60` | 5 | S_STRANGER | 18.5% | 20.0% | 20.0% | 0.0% | -242.2 | 0.25 | 1.02 | +463.8 | +313.8 |
| `confluence_gte_70` | 1 | S_STRANGER | 3.7% | 0.0% | 0.0% | 0.0% | -1239.0 | 0.00 | 0.00 | +50.0 | +527.0 |
| `tdi_rsi_gt_signal` | 24 | S_STRANGER | 88.9% | 8.3% | 12.5% | 4.2% | -381.3 | 0.10 | 0.66 | +228.0 | +293.2 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 48.1% | 0.0% | 7.7% | 0.0% | -571.7 | 0.03 | 0.41 | +118.9 | +281.0 |
| `ratio_le_2_and_asian_gte_30` | 26 | S_STRANGER | 96.3% | 7.7% | 15.4% | 3.8% | -315.0 | 0.14 | 0.73 | +253.3 | +287.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 23 | S_STRANGER | 85.2% | 8.7% | 13.0% | 4.3% | -344.0 | 0.11 | 0.72 | +235.8 | +283.0 |
| `feature_fresh_reclaim_within_8` | 6 | S_STRANGER | 22.2% | 0.0% | 33.3% | 16.7% | -560.0 | 0.15 | 0.22 | +214.7 | +204.3 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 7.4% | 14.8% | 3.7% | -349.3 | 0.12 | 0.68 | +245.8 | +296.6 |
| `feature_momentum_breakout_exception` | 18 | S_STRANGER | 66.7% | 11.1% | 11.1% | 5.6% | -176.7 | 0.19 | 1.43 | +299.6 | +338.9 |
| `feature_eurjpy_tdi50_reclaim` | 13 | S_STRANGER | 48.1% | 0.0% | 7.7% | 0.0% | -571.7 | 0.03 | 0.41 | +118.9 | +281.0 |

### THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|SELL|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|M_TOP|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-188.0; validation N=6 Fav=0.0% Avg=-235.3; out_of_sample N=1 Fav=100.0% Avg=+2335.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 13.3% | -339.6 | 0.35 | 2.07 | +383.1 | +446.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 86.7% | 7.7% | 15.4% | 15.4% | +25.3 | 1.14 | 5.70 | +438.5 | +420.7 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 86.7% | 7.7% | 15.4% | 15.4% | +25.3 | 1.14 | 5.70 | +438.5 | +420.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 13.3% | -339.6 | 0.35 | 2.07 | +383.1 | +446.1 |
| `confluence_gte_60` | 14 | S_STRANGER | 93.3% | 0.0% | 7.1% | 7.1% | -530.6 | 0.05 | 0.54 | +211.5 | +453.1 |
| `confluence_gte_70` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -60.0 | 0.00 | 0.00 | +42.0 | +229.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 60.0% | 11.1% | 11.1% | 22.2% | +75.0 | 1.41 | 9.85 | +519.3 | +406.4 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 93.3% | 7.1% | 14.3% | 14.3% | -358.6 | 0.35 | 1.92 | +397.1 | +456.3 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 86.7% | 7.7% | 15.4% | 15.4% | +25.3 | 1.14 | 5.70 | +438.5 | +420.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | S_STRANGER | 53.3% | 12.5% | 12.5% | 25.0% | +91.9 | 1.46 | 8.76 | +579.0 | +428.6 |
| `feature_fresh_reclaim_within_8` | 7 | S_STRANGER | 46.7% | 0.0% | 14.3% | 0.0% | -134.6 | 0.27 | 1.64 | +262.7 | +495.4 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 6.7% | 13.3% | 13.3% | -339.6 | 0.35 | 2.07 | +383.1 | +446.1 |
| `feature_momentum_breakout_exception` | 12 | S_STRANGER | 80.0% | 8.3% | 8.3% | 16.7% | +11.8 | 1.06 | 10.65 | +424.8 | +403.5 |
| `feature_eurjpy_tdi50_reclaim` | 14 | S_STRANGER | 93.3% | 7.1% | 14.3% | 14.3% | -358.6 | 0.35 | 1.92 | +397.1 | +456.3 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=+80.2; validation N=16 Fav=12.5% Avg=-125.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 50 | S_STRANGER | 100.0% | 6.0% | 16.0% | 12.0% | -722.3 | 0.06 | 0.30 | +183.5 | +280.2 |
| `hunt_to_ar_ratio_le_2_0` | 45 | S_STRANGER | 90.0% | 6.7% | 17.8% | 13.3% | -462.8 | 0.10 | 0.43 | +198.0 | +287.1 |
| `hunt_to_ar_ratio_le_2_5` | 45 | S_STRANGER | 90.0% | 6.7% | 17.8% | 13.3% | -462.8 | 0.10 | 0.43 | +198.0 | +287.1 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 50 | S_STRANGER | 100.0% | 6.0% | 16.0% | 12.0% | -722.3 | 0.06 | 0.30 | +183.5 | +280.2 |
| `confluence_gte_60` | 41 | S_STRANGER | 82.0% | 7.3% | 19.5% | 12.2% | -826.9 | 0.07 | 0.25 | +193.3 | +247.1 |
| `confluence_gte_70` | 1 | S_STRANGER | 2.0% | 0.0% | 0.0% | 0.0% | -350.0 | 0.00 | 0.00 | +47.0 | +778.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 18.0% | 0.0% | 0.0% | 22.2% | -583.9 | 0.00 | 0.00 | +124.1 | +346.8 |
| `tdi_rsi_gte_50` | 44 | S_STRANGER | 88.0% | 2.3% | 13.6% | 9.1% | -823.7 | 0.03 | 0.19 | +146.5 | +276.3 |
| `ratio_le_2_and_asian_gte_30` | 45 | S_STRANGER | 90.0% | 6.7% | 17.8% | 13.3% | -462.8 | 0.10 | 0.43 | +198.0 | +287.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 18.0% | 0.0% | 0.0% | 22.2% | -583.9 | 0.00 | 0.00 | +124.1 | +346.8 |
| `feature_fresh_reclaim_within_8` | 28 | S_STRANGER | 56.0% | 3.6% | 14.3% | 3.6% | -1064.5 | 0.03 | 0.19 | +160.0 | +277.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 49 | S_STRANGER | 98.0% | 6.1% | 16.3% | 10.2% | -737.1 | 0.06 | 0.30 | +183.4 | +284.2 |
| `feature_momentum_breakout_exception` | 20 | S_STRANGER | 40.0% | 15.0% | 20.0% | 30.0% | -84.4 | 0.52 | 1.68 | +283.4 | +400.4 |
| `feature_eurjpy_tdi50_reclaim` | 44 | S_STRANGER | 88.0% | 2.3% | 13.6% | 9.1% | -823.7 | 0.03 | 0.19 | +146.5 | +276.3 |

### STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-44.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 5.9% | 11.8% | 17.6% | -76.5 | 0.33 | 2.16 | +185.4 | +155.3 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 94.1% | 6.2% | 12.5% | 18.8% | -69.0 | 0.37 | 2.22 | +185.6 | +163.8 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 5.9% | 11.8% | 17.6% | -76.5 | 0.33 | 2.16 | +185.4 | +155.3 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 5.9% | 11.8% | 17.6% | -76.5 | 0.33 | 2.16 | +185.4 | +155.3 |
| `confluence_gte_60` | 6 | S_STRANGER | 35.3% | 16.7% | 16.7% | 33.3% | -44.5 | 0.64 | 2.57 | +280.7 | +188.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 35.3% | 0.0% | 16.7% | 0.0% | -98.8 | 0.22 | 1.10 | +85.5 | +130.5 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 58.8% | 0.0% | 10.0% | 0.0% | -90.1 | 0.16 | 1.41 | +102.1 | +106.3 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 94.1% | 6.2% | 12.5% | 18.8% | -69.0 | 0.37 | 2.22 | +185.6 | +163.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 35.3% | 0.0% | 16.7% | 0.0% | -98.8 | 0.22 | 1.10 | +85.5 | +130.5 |
| `feature_fresh_reclaim_within_8` | 3 | S_STRANGER | 17.6% | 0.0% | 33.3% | 0.0% | -15.7 | 0.78 | 1.56 | +136.7 | +62.7 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 5.9% | 11.8% | 17.6% | -76.5 | 0.33 | 2.16 | +185.4 | +155.3 |
| `feature_momentum_breakout_exception` | 13 | S_STRANGER | 76.5% | 7.7% | 15.4% | 23.1% | -40.5 | 0.55 | 2.48 | +210.9 | +172.2 |
| `feature_eurjpy_tdi50_reclaim` | 10 | S_STRANGER | 58.8% | 0.0% | 10.0% | 0.0% | -90.1 | 0.16 | 1.41 | +102.1 | +106.3 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=2 Fav=0.0% Avg=-1004.5; out_of_sample N=9 Fav=11.1% Avg=-2164.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 5.9% | -2738.4 | 0.02 | 0.30 | +352.0 | +634.7 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 94.1% | 6.2% | 6.2% | 6.2% | -2334.9 | 0.02 | 0.35 | +362.5 | +669.2 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 5.9% | -2738.4 | 0.02 | 0.30 | +352.0 | +634.7 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 5.9% | -2738.4 | 0.02 | 0.30 | +352.0 | +634.7 |
| `confluence_gte_60` | 14 | S_STRANGER | 82.4% | 7.1% | 7.1% | 7.1% | -3175.2 | 0.02 | 0.25 | +360.0 | +678.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 70.6% | 8.3% | 8.3% | 8.3% | -2556.5 | 0.03 | 0.31 | +354.4 | +484.1 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 88.2% | 6.7% | 6.7% | 6.7% | -2851.1 | 0.02 | 0.28 | +320.1 | +428.2 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 94.1% | 6.2% | 6.2% | 6.2% | -2334.9 | 0.02 | 0.35 | +362.5 | +669.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 64.7% | 9.1% | 9.1% | 9.1% | -1953.2 | 0.04 | 0.40 | +369.9 | +520.5 |
| `feature_fresh_reclaim_within_8` | 15 | S_STRANGER | 88.2% | 6.7% | 6.7% | 6.7% | -2851.1 | 0.02 | 0.28 | +320.1 | +428.2 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 5.9% | -2738.4 | 0.02 | 0.30 | +352.0 | +634.7 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 23.5% | 25.0% | 25.0% | 25.0% | -771.5 | 0.22 | 0.67 | +831.7 | +1255.0 |
| `feature_eurjpy_tdi50_reclaim` | 15 | S_STRANGER | 88.2% | 6.7% | 6.7% | 6.7% | -2851.1 | 0.02 | 0.28 | +320.1 | +428.2 |

### STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=8.3% Avg=-283.6; validation N=8 Fav=37.5% Avg=+39.7; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 70 | S_STRANGER | 100.0% | 5.7% | 15.7% | 5.7% | -804.9 | 0.06 | 0.32 | +235.7 | +243.9 |
| `hunt_to_ar_ratio_le_2_0` | 66 | S_STRANGER | 94.3% | 6.1% | 16.7% | 6.1% | -716.2 | 0.07 | 0.35 | +241.0 | +242.2 |
| `hunt_to_ar_ratio_le_2_5` | 67 | S_STRANGER | 95.7% | 6.0% | 16.4% | 6.0% | -728.2 | 0.07 | 0.35 | +238.1 | +242.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 70 | S_STRANGER | 100.0% | 5.7% | 15.7% | 5.7% | -804.9 | 0.06 | 0.32 | +235.7 | +243.9 |
| `confluence_gte_60` | 7 | S_STRANGER | 10.0% | 14.3% | 28.6% | 14.3% | -35.6 | 0.62 | 1.54 | +118.1 | +238.6 |
| `confluence_gte_70` | 2 | R_REPEATER | 2.9% | 50.0% | 50.0% | 50.0% | +51.0 | 1.37 | 1.37 | +214.0 | +94.5 |
| `tdi_rsi_gt_signal` | 30 | S_STRANGER | 42.9% | 0.0% | 6.7% | 0.0% | -1076.9 | 0.04 | 0.59 | +252.6 | +194.9 |
| `tdi_rsi_gte_50` | 63 | S_STRANGER | 90.0% | 3.2% | 12.7% | 4.8% | -871.0 | 0.05 | 0.32 | +221.1 | +218.0 |
| `ratio_le_2_and_asian_gte_30` | 66 | S_STRANGER | 94.3% | 6.1% | 16.7% | 6.1% | -716.2 | 0.07 | 0.35 | +241.0 | +242.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 29 | S_STRANGER | 41.4% | 0.0% | 6.9% | 0.0% | -998.0 | 0.05 | 0.63 | +258.2 | +181.0 |
| `feature_fresh_reclaim_within_8` | 51 | S_STRANGER | 72.9% | 5.9% | 19.6% | 7.8% | -806.3 | 0.07 | 0.27 | +244.9 | +206.8 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 68 | S_STRANGER | 97.1% | 5.9% | 14.7% | 5.9% | -814.1 | 0.06 | 0.35 | +231.8 | +249.2 |
| `feature_momentum_breakout_exception` | 20 | S_STRANGER | 28.6% | 20.0% | 25.0% | 20.0% | -154.2 | 0.32 | 0.90 | +264.3 | +377.6 |
| `feature_eurjpy_tdi50_reclaim` | 63 | S_STRANGER | 90.0% | 3.2% | 12.7% | 4.8% | -871.0 | 0.05 | 0.32 | +221.1 | +218.0 |

### STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-604.4; validation N=13 Fav=7.7% Avg=-1168.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 5.6% | 11.1% | 5.6% | -1011.4 | 0.05 | 0.39 | +256.9 | +305.5 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 100.0% | 5.6% | 11.1% | 5.6% | -1011.4 | 0.05 | 0.39 | +256.9 | +305.5 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 5.6% | 11.1% | 5.6% | -1011.4 | 0.05 | 0.39 | +256.9 | +305.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 18 | S_STRANGER | 100.0% | 5.6% | 11.1% | 5.6% | -1011.4 | 0.05 | 0.39 | +256.9 | +305.5 |
| `confluence_gte_60` | 1 | R_RUNNER | 5.6% | 100.0% | 100.0% | 0.0% | +337.0 | 999.00 | 999.00 | +994.0 | +44.0 |
| `confluence_gte_70` | 1 | R_RUNNER | 5.6% | 100.0% | 100.0% | 0.0% | +337.0 | 999.00 | 999.00 | +994.0 | +44.0 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 27.8% | 0.0% | 0.0% | 0.0% | -826.8 | 0.00 | 0.00 | +207.2 | +311.4 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 94.4% | 0.0% | 5.9% | 5.9% | -1090.8 | 0.03 | 0.52 | +213.5 | +320.9 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 100.0% | 5.6% | 11.1% | 5.6% | -1011.4 | 0.05 | 0.39 | +256.9 | +305.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 27.8% | 0.0% | 0.0% | 0.0% | -826.8 | 0.00 | 0.00 | +207.2 | +311.4 |
| `feature_fresh_reclaim_within_8` | 17 | S_STRANGER | 94.4% | 0.0% | 5.9% | 5.9% | -1090.8 | 0.03 | 0.52 | +213.5 | +320.9 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 5.6% | 11.1% | 5.6% | -1011.4 | 0.05 | 0.39 | +256.9 | +305.5 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 33.3% | -23.3 | 0.83 | 0.83 | +567.3 | +205.0 |
| `feature_eurjpy_tdi50_reclaim` | 17 | S_STRANGER | 94.4% | 0.0% | 5.9% | 5.9% | -1090.8 | 0.03 | 0.52 | +213.5 | +320.9 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-143.0; validation N=7 Fav=14.3% Avg=-318.0; out_of_sample N=3 Fav=0.0% Avg=-472.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 4.5% | 9.1% | 13.6% | -765.1 | 0.04 | 0.36 | +229.3 | +559.5 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 100.0% | 4.5% | 9.1% | 13.6% | -765.1 | 0.04 | 0.36 | +229.3 | +559.5 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 100.0% | 4.5% | 9.1% | 13.6% | -765.1 | 0.04 | 0.36 | +229.3 | +559.5 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 22 | S_STRANGER | 100.0% | 4.5% | 9.1% | 13.6% | -765.1 | 0.04 | 0.36 | +229.3 | +559.5 |
| `confluence_gte_60` | 19 | S_STRANGER | 86.4% | 5.3% | 10.5% | 15.8% | -810.5 | 0.04 | 0.32 | +252.7 | +515.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 13.6% | 0.0% | 0.0% | 0.0% | -868.0 | 0.00 | 0.00 | +138.3 | +551.3 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 68.2% | 0.0% | 6.7% | 6.7% | -908.6 | 0.01 | 0.07 | +173.7 | +526.4 |
| `ratio_le_2_and_asian_gte_30` | 22 | S_STRANGER | 100.0% | 4.5% | 9.1% | 13.6% | -765.1 | 0.04 | 0.36 | +229.3 | +559.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 13.6% | 0.0% | 0.0% | 0.0% | -868.0 | 0.00 | 0.00 | +138.3 | +551.3 |
| `feature_fresh_reclaim_within_8` | 8 | S_STRANGER | 36.4% | 0.0% | 0.0% | 12.5% | -1041.2 | 0.00 | 0.00 | +260.8 | +539.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 4.5% | 9.1% | 13.6% | -765.1 | 0.04 | 0.36 | +229.3 | +559.5 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 50.0% | 9.1% | 9.1% | 27.3% | -344.1 | 0.14 | 1.12 | +266.7 | +679.6 |
| `feature_eurjpy_tdi50_reclaim` | 15 | S_STRANGER | 68.2% | 0.0% | 6.7% | 6.7% | -908.6 | 0.01 | 0.07 | +173.7 | +526.4 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=0.0% Avg=-2493.6; out_of_sample N=2 Fav=50.0% Avg=+675.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 3.4% | 6.9% | 6.9% | -1070.5 | 0.08 | 1.07 | +457.6 | +569.8 |
| `hunt_to_ar_ratio_le_2_0` | 28 | S_STRANGER | 96.6% | 3.6% | 7.1% | 7.1% | -813.5 | 0.11 | 1.36 | +461.9 | +583.7 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 100.0% | 3.4% | 6.9% | 6.9% | -1070.5 | 0.08 | 1.07 | +457.6 | +569.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 29 | S_STRANGER | 100.0% | 3.4% | 6.9% | 6.9% | -1070.5 | 0.08 | 1.07 | +457.6 | +569.8 |
| `confluence_gte_60` | 24 | S_STRANGER | 82.8% | 4.2% | 8.3% | 8.3% | -1103.3 | 0.09 | 1.00 | +467.2 | +414.3 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 37.9% | 0.0% | 0.0% | 0.0% | -782.8 | 0.00 | 0.00 | +391.8 | +465.7 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 79.3% | 4.3% | 8.7% | 4.3% | -1129.5 | 0.10 | 1.01 | +487.9 | +383.5 |
| `ratio_le_2_and_asian_gte_30` | 28 | S_STRANGER | 96.6% | 3.6% | 7.1% | 7.1% | -813.5 | 0.11 | 1.36 | +461.9 | +583.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 37.9% | 0.0% | 0.0% | 0.0% | -782.8 | 0.00 | 0.00 | +391.8 | +465.7 |
| `feature_fresh_reclaim_within_8` | 7 | S_STRANGER | 24.1% | 14.3% | 14.3% | 14.3% | -1588.3 | 0.13 | 0.77 | +648.7 | +310.6 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 3.4% | 6.9% | 6.9% | -1070.5 | 0.08 | 1.07 | +457.6 | +569.8 |
| `feature_momentum_breakout_exception` | 17 | S_STRANGER | 58.6% | 5.9% | 5.9% | 11.8% | -398.9 | 0.19 | 2.91 | +483.4 | +813.2 |
| `feature_eurjpy_tdi50_reclaim` | 23 | S_STRANGER | 79.3% | 4.3% | 8.7% | 4.3% | -1129.5 | 0.10 | 1.01 | +487.9 | +383.5 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=0.0% Avg=-208.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=0.0% Avg=-407.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -281.8 | 0.00 | 0.00 | +213.4 | +585.2 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -281.8 | 0.00 | 0.00 | +213.4 | +585.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -281.8 | 0.00 | 0.00 | +213.4 | +585.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -281.8 | 0.00 | 0.00 | +213.4 | +585.2 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -281.8 | 0.00 | 0.00 | +213.4 | +585.2 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -281.8 | 0.00 | 0.00 | +213.4 | +585.2 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -295.6 | 0.00 | 0.00 | +214.0 | +561.6 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 0.0% | 0.0% | 14.3% | -286.6 | 0.00 | 0.00 | +104.6 | +308.0 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -281.8 | 0.00 | 0.00 | +213.4 | +585.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -295.6 | 0.00 | 0.00 | +214.0 | +561.6 |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -801.0 | 0.00 | 0.00 | +48.0 | +395.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 0.0% | 0.0% | 16.7% | -281.8 | 0.00 | 0.00 | +213.4 | +585.2 |
| `feature_momentum_breakout_exception` | 10 | S_STRANGER | 83.3% | 0.0% | 0.0% | 20.0% | -248.4 | 0.00 | 0.00 | +247.9 | +656.8 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 58.3% | 0.0% | 0.0% | 14.3% | -286.6 | 0.00 | 0.00 | +104.6 | +308.0 |

### STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `STOP_HUNT|SELL|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=21 Fav=0.0% Avg=-1352.8; out_of_sample N=3 Fav=0.0% Avg=-1023.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 0.0% | 4.2% | 0.0% | -1311.6 | 0.01 | 0.23 | +404.4 | +574.5 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 95.8% | 0.0% | 4.3% | 0.0% | -1323.2 | 0.01 | 0.23 | +419.7 | +471.8 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 95.8% | 0.0% | 4.3% | 0.0% | -1323.2 | 0.01 | 0.23 | +419.7 | +471.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 24 | S_STRANGER | 100.0% | 0.0% | 4.2% | 0.0% | -1311.6 | 0.01 | 0.23 | +404.4 | +574.5 |
| `confluence_gte_60` | 18 | S_STRANGER | 75.0% | 0.0% | 5.6% | 0.0% | -1448.8 | 0.01 | 0.21 | +435.4 | +339.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 75.0% | 0.0% | 5.6% | 0.0% | -1470.8 | 0.01 | 0.20 | +355.7 | +420.9 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 79.2% | 0.0% | 5.3% | 0.0% | -1453.6 | 0.01 | 0.21 | +345.7 | +418.9 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 95.8% | 0.0% | 4.3% | 0.0% | -1323.2 | 0.01 | 0.23 | +419.7 | +471.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 70.8% | 0.0% | 5.9% | 0.0% | -1495.9 | 0.01 | 0.20 | +373.5 | +273.0 |
| `feature_fresh_reclaim_within_8` | 19 | S_STRANGER | 79.2% | 0.0% | 5.3% | 0.0% | -1453.6 | 0.01 | 0.21 | +345.7 | +418.9 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 0.0% | 4.2% | 0.0% | -1311.6 | 0.01 | 0.23 | +404.4 | +574.5 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -652.1 | 0.00 | 0.00 | +425.1 | +1162.6 |
| `feature_eurjpy_tdi50_reclaim` | 19 | S_STRANGER | 79.2% | 0.0% | 5.3% | 0.0% | -1453.6 | 0.01 | 0.21 | +345.7 | +418.9 |

### RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=11 Fav=0.0% Avg=-1891.4; out_of_sample N=5 Fav=0.0% Avg=-1771.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -2007.6 | 0.00 | 0.00 | +425.6 | +346.2 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 94.1% | 0.0% | 0.0% | 0.0% | -1853.8 | 0.00 | 0.00 | +428.9 | +346.4 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -2007.6 | 0.00 | 0.00 | +425.6 | +346.2 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -2007.6 | 0.00 | 0.00 | +425.6 | +346.2 |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -2007.6 | 0.00 | 0.00 | +425.6 | +346.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 76.5% | 0.0% | 0.0% | 0.0% | -2066.0 | 0.00 | 0.00 | +483.2 | +252.8 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 94.1% | 0.0% | 0.0% | 0.0% | -2013.4 | 0.00 | 0.00 | +420.2 | +244.8 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 94.1% | 0.0% | 0.0% | 0.0% | -1853.8 | 0.00 | 0.00 | +428.9 | +346.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 70.6% | 0.0% | 0.0% | 0.0% | -1865.8 | 0.00 | 0.00 | +492.3 | +245.4 |
| `feature_fresh_reclaim_within_8` | 15 | S_STRANGER | 88.2% | 0.0% | 0.0% | 0.0% | -2092.4 | 0.00 | 0.00 | +429.7 | +258.5 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -2007.6 | 0.00 | 0.00 | +425.6 | +346.2 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -1168.0 | 0.00 | 0.00 | +333.0 | +1249.0 |
| `feature_eurjpy_tdi50_reclaim` | 16 | S_STRANGER | 94.1% | 0.0% | 0.0% | 0.0% | -2013.4 | 0.00 | 0.00 | +420.2 | +244.8 |

### RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `RRT_REVERSAL|SELL|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=0.0% Avg=-2397.6; out_of_sample N=2 Fav=0.0% Avg=-714.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3021.0 | 0.00 | 0.00 | +737.5 | +1880.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3021.0 | 0.00 | 0.00 | +737.5 | +1880.8 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3021.0 | 0.00 | 0.00 | +737.5 | +1880.8 |
| `stop_hunt_le_90` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3021.0 | 0.00 | 0.00 | +737.5 | +1880.8 |
| `confluence_gte_60` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -2601.0 | 0.00 | 0.00 | +1034.5 | +3209.5 |
| `confluence_gte_70` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -3509.0 | 0.00 | 0.00 | +1159.5 | +4169.0 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -4548.5 | 0.00 | 0.00 | +913.7 | +2419.0 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -5598.0 | 0.00 | 0.00 | +504.7 | +491.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3021.0 | 0.00 | 0.00 | +737.5 | +1880.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -4548.5 | 0.00 | 0.00 | +913.7 | +2419.0 |
| `feature_fresh_reclaim_within_8` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -5598.0 | 0.00 | 0.00 | +504.7 | +491.0 |
| `feature_extreme_hunt_with_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3021.0 | 0.00 | 0.00 | +737.5 | +1880.8 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 0.0% | -1916.6 | 0.00 | 0.00 | +837.3 | +2476.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -5598.0 | 0.00 | 0.00 | +504.7 | +491.0 |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
