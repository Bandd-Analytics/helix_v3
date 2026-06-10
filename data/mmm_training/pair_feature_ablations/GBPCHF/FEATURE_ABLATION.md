# GBPCHF Pair Feature Ablation

Generated: 2026-06-09T15:36:21.077785+00:00
Minimum setup sample: 10
Scanner baseline gate: Fav >= 85.0% and AvgExit >= +10.9; split pass requirement = 2 with split N >= 3

| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |
|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 19 | R_REPEATER | 52.6% | +11.1 | `confluence_gte_70` | 5 | R_REPEATER | 60.0% | +24.1 | 6.27 | 4.18 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | R_REPEATER | 50.0% | +8.5 | `tdi_rsi_gt_signal` | 5 | R_REPEATER | 60.0% | +14.6 | 7.23 | 4.82 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 12 | R_REPEATER | 50.0% | +8.1 | `all` | 12 | R_REPEATER | 50.0% | +8.1 | 6.07 | 4.33 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | R_REPEATER | 50.0% | +7.1 | `confluence_gte_60` | 8 | R_REPEATER | 62.5% | +10.2 | 2.45 | 1.47 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | R_REPEATER | 50.0% | +4.8 | `tdi_rsi_gt_signal` | 8 | R_REPEATER | 50.0% | +5.2 | 4.32 | 4.32 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 21 | S_STRANGER | 47.6% | +3.7 | `tdi_rsi_gte_50` | 14 | R_REPEATER | 50.0% | +5.2 | 3.51 | 3.51 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 38 | S_STRANGER | 47.4% | +4.3 | `all` | 38 | S_STRANGER | 47.4% | +4.3 | 3.37 | 3.56 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 45.5% | +1.0 | `all` | 11 | S_STRANGER | 45.5% | +1.0 | 1.28 | 1.54 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 44.4% | +3.5 | `all` | 18 | S_STRANGER | 44.4% | +3.5 | 2.05 | 2.56 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 42.1% | +4.3 | `hunt_to_ar_ratio_le_2_5` | 8 | R_REPEATER | 62.5% | +8.8 | 236.00 | 47.20 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 41.7% | +3.2 | `confluence_gte_60` | 5 | R_RUNNER | 80.0% | +13.6 | 999.00 | 999.00 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 40.0% | +5.5 | `tdi_rsi_gte_50` | 12 | R_REPEATER | 50.0% | +7.7 | 3.24 | 3.24 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 40.0% | +4.1 | `confluence_gte_70` | 8 | R_REPEATER | 50.0% | +10.5 | 9.51 | 9.51 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 20 | S_STRANGER | 40.0% | +2.1 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 40.0% | +5.8 | 3.71 | 4.64 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | S_STRANGER | 40.0% | +1.1 | `tdi_rsi_gt_signal` | 5 | R_RUNNER | 80.0% | +5.5 | 3.13 | 0.78 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 15 | S_STRANGER | 40.0% | +0.8 | `tdi_rsi_gte_50` | 5 | R_RUNNER | 80.0% | +7.2 | 2.96 | 0.74 | 1 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 40.0% | +0.4 | `confluence_gte_70` | 6 | R_REPEATER | 50.0% | +0.5 | 1.13 | 1.13 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 38.5% | +6.9 | `tdi_rsi_gt_signal` | 7 | R_REPEATER | 57.1% | +17.9 | 4.26 | 3.19 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 38.5% | +5.3 | `tdi_rsi_gt_signal` | 6 | R_RUNNER | 83.3% | +18.9 | 8.81 | 1.76 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 32 | S_STRANGER | 37.5% | +1.1 | `ratio_le_2_asian_gte_30_tdi_positive` | 21 | S_STRANGER | 42.9% | +2.9 | 1.96 | 2.62 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 38 | S_STRANGER | 36.8% | +3.2 | `tdi_rsi_gte_50` | 27 | S_STRANGER | 44.4% | +3.5 | 2.19 | 2.74 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 22 | S_STRANGER | 36.4% | -6.4 | `all` | 22 | S_STRANGER | 36.4% | -6.4 | 0.37 | 0.65 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 36 | S_STRANGER | 36.1% | +2.6 | `asian_range_gte_30` | 26 | S_STRANGER | 38.5% | +3.6 | 1.90 | 2.85 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 35.3% | +2.7 | `hunt_to_ar_ratio_le_2_5` | 5 | R_REPEATER | 60.0% | +5.4 | 15.16 | 10.11 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 32 | S_STRANGER | 34.4% | -0.0 | `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 42.9% | +3.0 | 2.85 | 2.45 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | +10.9 | `asian_range_gte_30` | 6 | R_REPEATER | 50.0% | +22.1 | 10.77 | 10.77 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 33.3% | +3.4 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 44.4% | +6.0 | 2.93 | 3.66 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 33.3% | +3.3 | `all` | 18 | S_STRANGER | 33.3% | +3.3 | 1.76 | 3.22 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | +2.3 | `hunt_to_ar_ratio_le_2_5` | 8 | R_REPEATER | 50.0% | +5.1 | 1.95 | 1.95 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | +2.1 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 42.9% | +6.3 | 2.07 | 2.76 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 21 | S_STRANGER | 33.3% | +0.8 | `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 45.5% | +9.2 | 4.95 | 5.94 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 15 | S_STRANGER | 33.3% | +0.2 | `all` | 15 | S_STRANGER | 33.3% | +0.2 | 1.05 | 2.09 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 33.3% | +0.1 | `tdi_rsi_gt_signal` | 11 | S_STRANGER | 36.4% | +1.0 | 1.38 | 2.42 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 15 | S_STRANGER | 33.3% | +0.1 | `confluence_gte_60` | 14 | S_STRANGER | 35.7% | +0.1 | 1.05 | 0.90 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 33.3% | -0.5 | `all` | 18 | S_STRANGER | 33.3% | -0.5 | 0.89 | 1.27 | 0 | 1 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 18 | S_STRANGER | 33.3% | -0.6 | `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 41.7% | +4.4 | 1.84 | 1.84 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 33.3% | -0.8 | `feature_momentum_breakout_exception` | 6 | R_REPEATER | 66.7% | +10.1 | 4.05 | 2.02 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 33.3% | -1.0 | `asian_range_gte_30` | 8 | S_STRANGER | 37.5% | +0.1 | 1.02 | 1.36 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 33.3% | -1.1 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 37.5% | +0.0 | 1.01 | 1.68 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 24 | S_STRANGER | 33.3% | -2.6 | `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 41.7% | +0.9 | 1.21 | 1.69 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 31 | S_STRANGER | 32.3% | +2.2 | `feature_momentum_breakout_exception` | 6 | R_REPEATER | 50.0% | +7.2 | 6.09 | 6.09 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 22 | S_STRANGER | 31.8% | +0.0 | `all` | 22 | S_STRANGER | 31.8% | +0.0 | 1.01 | 1.73 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 16 | S_STRANGER | 31.2% | +4.5 | `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 40.0% | +3.4 | 1.59 | 2.38 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 31.2% | +0.4 | `asian_range_gte_30` | 12 | S_STRANGER | 33.3% | +0.2 | 1.05 | 2.10 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 16 | S_STRANGER | 31.2% | -3.3 | `tdi_rsi_gt_signal` | 6 | R_REPEATER | 50.0% | +0.4 | 1.11 | 1.11 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 30.8% | +9.2 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 33.3% | +9.6 | 4.10 | 8.21 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 26 | S_STRANGER | 30.8% | +1.8 | `confluence_gte_70` | 5 | R_REPEATER | 60.0% | +7.1 | 2.57 | 1.71 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 30.8% | +0.9 | `all` | 13 | S_STRANGER | 30.8% | +0.9 | 1.29 | 2.89 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 30.8% | -0.5 | `stop_hunt_le_90` | 8 | R_REPEATER | 50.0% | +0.7 | 1.18 | 1.18 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 30.8% | -1.9 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 33.3% | -1.3 | 0.58 | 1.17 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 23 | S_STRANGER | 30.4% | +2.7 | `confluence_gte_70` | 6 | R_REPEATER | 66.7% | +14.3 | 11.73 | 5.86 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 23 | S_STRANGER | 30.4% | +2.0 | `confluence_gte_60` | 22 | S_STRANGER | 31.8% | +2.5 | 1.64 | 3.04 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 46 | S_STRANGER | 30.4% | +1.2 | `all` | 46 | S_STRANGER | 30.4% | +1.2 | 1.34 | 2.67 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 46 | S_STRANGER | 30.4% | -1.4 | `confluence_gte_70` | 7 | S_STRANGER | 42.9% | +0.5 | 1.56 | 2.08 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 43 | S_STRANGER | 30.2% | +2.0 | `all` | 43 | S_STRANGER | 30.2% | +2.0 | 1.85 | 3.56 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 30.0% | +5.2 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 42.9% | +10.1 | 4.04 | 5.39 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 30.0% | +4.8 | `all` | 10 | S_STRANGER | 30.0% | +4.8 | 5.00 | 10.00 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 30.0% | +2.6 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 37.5% | +4.1 | 3.05 | 5.09 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 30.0% | +0.8 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 37.5% | +1.3 | 1.65 | 2.76 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 30.0% | -2.5 | `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 40.0% | +2.5 | 1.94 | 2.91 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 31 | S_STRANGER | 29.0% | +2.4 | `tdi_rsi_gt_signal` | 8 | R_REPEATER | 62.5% | +3.9 | 2.85 | 1.14 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 35 | S_STRANGER | 28.6% | +0.4 | `feature_eurjpy_tdi50_reclaim` | 5 | R_REPEATER | 60.0% | +15.1 | 16.40 | 10.93 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 42 | S_STRANGER | 28.6% | +0.2 | `tdi_rsi_gte_50` | 25 | S_STRANGER | 32.0% | +1.8 | 1.50 | 2.81 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 28 | S_STRANGER | 28.6% | -0.3 | `tdi_rsi_gt_signal` | 26 | S_STRANGER | 30.8% | +0.6 | 1.22 | 2.59 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 27.8% | -0.5 | `all` | 18 | S_STRANGER | 27.8% | -0.5 | 0.84 | 2.19 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 18 | S_STRANGER | 27.8% | -3.3 | `all` | 18 | S_STRANGER | 27.8% | -3.3 | 0.32 | 0.83 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 58 | S_STRANGER | 27.6% | +0.4 | `feature_eurjpy_tdi50_reclaim` | 5 | R_REPEATER | 60.0% | +4.0 | 7.93 | 2.64 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 33 | S_STRANGER | 27.3% | +1.2 | `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 33.3% | +5.6 | 4.14 | 8.28 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 22 | S_STRANGER | 27.3% | +0.9 | `tdi_rsi_gt_signal` | 12 | S_STRANGER | 41.7% | +3.1 | 1.81 | 2.53 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 22 | S_STRANGER | 27.3% | +0.2 | `hunt_to_ar_ratio_le_2_0` | 9 | R_REPEATER | 55.6% | +7.1 | 4.55 | 3.64 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 27.3% | -8.5 | `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 30.0% | -9.4 | 0.16 | 0.36 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 26 | S_STRANGER | 26.9% | +1.9 | `confluence_gte_60` | 19 | S_STRANGER | 31.6% | +2.9 | 3.27 | 6.55 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 26 | S_STRANGER | 26.9% | +1.9 | `asian_range_gte_30` | 18 | S_STRANGER | 33.3% | +3.4 | 1.80 | 3.60 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 30 | S_STRANGER | 26.7% | +2.1 | `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 31.2% | +3.0 | 1.76 | 2.93 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 15 | S_STRANGER | 26.7% | +1.2 | `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 30.8% | +2.4 | 1.43 | 3.23 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 19 | S_STRANGER | 26.3% | +2.7 | `asian_range_gte_30` | 13 | S_STRANGER | 38.5% | +4.9 | 4.61 | 7.38 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 38 | S_STRANGER | 26.3% | -0.8 | `tdi_rsi_gte_50` | 20 | S_STRANGER | 35.0% | +1.3 | 1.44 | 2.48 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 26.3% | -0.8 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 37.5% | -2.1 | 0.64 | 1.07 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 57 | S_STRANGER | 26.3% | -1.7 | `confluence_gte_70` | 9 | S_STRANGER | 44.4% | +1.7 | 1.77 | 2.22 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 39 | S_STRANGER | 25.6% | +0.2 | `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 33.3% | +2.9 | 2.96 | 5.91 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 24 | S_STRANGER | 25.0% | +2.1 | `confluence_gte_70` | 8 | R_REPEATER | 50.0% | +6.7 | 7.23 | 7.23 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 56 | S_STRANGER | 25.0% | -0.1 | `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 50.0% | +5.9 | 4.79 | 4.79 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 56 | S_STRANGER | 25.0% | -0.2 | `confluence_gte_70` | 10 | S_STRANGER | 40.0% | +3.3 | 2.45 | 3.67 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 25.0% | -1.3 | `tdi_rsi_gte_50` | 15 | S_STRANGER | 26.7% | -0.4 | 0.82 | 2.27 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 25.0% | -1.5 | `all` | 12 | S_STRANGER | 25.0% | -1.5 | 0.51 | 1.36 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 25.0% | -1.5 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 22.2% | +1.7 | 1.53 | 5.36 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 24 | S_STRANGER | 25.0% | -5.6 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 37.5% | +2.9 | 2.03 | 3.38 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 41 | S_STRANGER | 24.4% | -0.0 | `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 26.3% | -1.6 | 0.56 | 1.13 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 78 | S_STRANGER | 24.4% | +0.8 | `confluence_gte_70` | 5 | R_RUNNER | 80.0% | +16.2 | 28.86 | 7.22 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 17 | S_STRANGER | 23.5% | +2.1 | `tdi_rsi_gt_signal` | 14 | S_STRANGER | 28.6% | +3.3 | 1.46 | 2.34 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 17 | S_STRANGER | 23.5% | -9.0 | `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 25.0% | -7.8 | 0.27 | 0.80 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 30 | S_STRANGER | 23.3% | -0.9 | `tdi_rsi_gte_50` | 13 | S_STRANGER | 30.8% | +1.1 | 1.22 | 2.75 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 23.1% | +3.1 | `tdi_rsi_gte_50` | 11 | S_STRANGER | 27.3% | +5.0 | 2.26 | 5.27 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 39 | S_STRANGER | 23.1% | -0.1 | `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 31.6% | +2.5 | 1.75 | 3.21 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 23.1% | -3.0 | `feature_momentum_breakout_exception` | 6 | R_REPEATER | 50.0% | +8.0 | 3.08 | 3.08 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 22.2% | +0.9 | `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 23.5% | +1.0 | 1.48 | 4.43 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 22.2% | -1.2 | `asian_range_gte_30` | 12 | S_STRANGER | 25.0% | -1.6 | 0.59 | 1.76 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 22.2% | -2.3 | `all` | 18 | S_STRANGER | 22.2% | -2.3 | 0.41 | 1.43 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 23 | S_STRANGER | 21.7% | +2.1 | `tdi_rsi_gt_signal` | 14 | S_STRANGER | 28.6% | +5.9 | 5.27 | 10.55 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 21.7% | +1.3 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 28.6% | +1.1 | 1.72 | 4.31 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 21.7% | -0.5 | `tdi_rsi_gte_50` | 17 | S_STRANGER | 29.4% | +0.4 | 1.13 | 2.72 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 23 | S_STRANGER | 21.7% | -4.2 | `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 22.7% | -4.1 | 0.42 | 1.34 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 37 | S_STRANGER | 21.6% | -0.9 | `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 46.2% | +6.9 | 3.32 | 2.85 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 37 | S_STRANGER | 21.6% | -2.0 | `tdi_rsi_gte_50` | 23 | S_STRANGER | 26.1% | +0.7 | 1.41 | 3.53 | 0 | 3 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | +2.7 | `tdi_rsi_gt_signal` | 11 | S_STRANGER | 27.3% | +5.2 | 2.89 | 7.72 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 21.4% | +1.6 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 33.3% | +3.6 | 3.91 | 6.51 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | -6.3 | `confluence_gte_70` | 10 | S_STRANGER | 30.0% | -7.0 | 0.13 | 0.27 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 14 | S_STRANGER | 21.4% | -7.0 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 37.5% | -2.0 | 0.73 | 1.22 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 19 | S_STRANGER | 21.1% | -2.6 | `tdi_rsi_gte_50` | 15 | S_STRANGER | 26.7% | -1.9 | 0.41 | 1.14 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 64 | S_STRANGER | 20.3% | -1.3 | `tdi_rsi_gt_signal` | 30 | S_STRANGER | 26.7% | +0.6 | 1.15 | 3.15 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | +0.4 | `confluence_gte_60` | 7 | S_STRANGER | 28.6% | +1.2 | 1.22 | 2.43 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | +0.1 | `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 33.3% | +1.8 | 1.48 | 1.48 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 20.0% | -1.1 | `confluence_gte_60` | 15 | S_STRANGER | 20.0% | -0.8 | 0.88 | 1.98 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -1.7 | `all` | 10 | S_STRANGER | 20.0% | -1.7 | 0.66 | 2.32 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 20.0% | -1.9 | `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 28.6% | -4.1 | 0.52 | 1.30 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 20.0% | -3.6 | `asian_range_gte_30` | 11 | S_STRANGER | 27.3% | -1.9 | 0.69 | 1.60 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 20 | S_STRANGER | 20.0% | -3.7 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 28.6% | +3.1 | 2.47 | 6.17 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -3.9 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 28.6% | +0.1 | 1.05 | 2.11 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 20.0% | -3.9 | `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 21.4% | -3.3 | 0.38 | 1.39 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -4.5 | `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 25.0% | -5.2 | 0.22 | 0.65 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 15 | S_STRANGER | 20.0% | -4.8 | `confluence_gte_70` | 8 | S_STRANGER | 25.0% | -1.8 | 0.71 | 1.19 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 20.0% | -4.8 | `asian_range_gte_30` | 9 | S_STRANGER | 22.2% | -4.3 | 0.34 | 0.68 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 20.0% | -5.2 | `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 40.0% | +0.6 | 1.34 | 1.34 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -5.2 | `confluence_gte_60` | 6 | S_STRANGER | 16.7% | +0.8 | 1.30 | 5.18 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 20.0% | -14.8 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 33.3% | -8.7 | 0.26 | 0.52 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 36 | S_STRANGER | 19.4% | -2.4 | `asian_range_gte_30` | 23 | S_STRANGER | 26.1% | -2.2 | 0.57 | 1.44 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 31 | S_STRANGER | 19.4% | -1.0 | `feature_momentum_breakout_exception` | 9 | R_REPEATER | 55.6% | +5.2 | 6.33 | 3.80 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 31 | S_STRANGER | 19.4% | -4.7 | `all` | 31 | S_STRANGER | 19.4% | -4.7 | 0.26 | 0.55 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 26 | S_STRANGER | 19.2% | -0.4 | `confluence_gte_60` | 5 | R_REPEATER | 60.0% | +8.8 | 4.45 | 2.97 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 16 | S_STRANGER | 18.8% | +2.6 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 25.0% | +4.5 | 1.99 | 5.98 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 16 | S_STRANGER | 18.8% | +2.1 | `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 20.0% | +2.4 | 1.76 | 7.04 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 27 | S_STRANGER | 18.5% | -1.0 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 25.0% | +1.5 | 1.59 | 4.24 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | +0.6 | `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 28.6% | +1.7 | 2.18 | 4.36 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 22 | S_STRANGER | 18.2% | -0.2 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 33.3% | +0.5 | 1.07 | 2.14 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -1.0 | `tdi_rsi_gt_signal` | 5 | S_STRANGER | 40.0% | +1.0 | 3.12 | 3.12 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 11 | S_STRANGER | 18.2% | -8.3 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 25.0% | +0.1 | 1.04 | 3.12 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 39 | S_STRANGER | 17.9% | -0.9 | `feature_momentum_breakout_exception` | 6 | S_STRANGER | 33.3% | +1.0 | 1.30 | 2.61 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 17.6% | +1.8 | `tdi_rsi_gt_signal` | 11 | S_STRANGER | 18.2% | +3.5 | 2.43 | 9.73 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 17 | S_STRANGER | 17.6% | -1.3 | `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 25.0% | +1.0 | 1.56 | 3.12 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 35 | S_STRANGER | 17.1% | -4.9 | `confluence_gte_70` | 7 | S_STRANGER | 28.6% | +1.6 | 1.39 | 2.08 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 47 | S_STRANGER | 17.0% | -3.3 | `tdi_rsi_gte_50` | 28 | S_STRANGER | 21.4% | -0.3 | 0.92 | 3.37 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 18 | S_STRANGER | 16.7% | -0.7 | `confluence_gte_60` | 14 | S_STRANGER | 21.4% | +0.2 | 1.05 | 3.86 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 16.7% | -1.7 | `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 18.2% | -1.7 | 0.60 | 2.70 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 16.7% | -3.3 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 33.3% | -1.5 | 0.53 | 1.07 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -6.2 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | -2.7 | 0.30 | 0.59 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74` | 12 | S_STRANGER | 16.7% | -6.3 | `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 33.3% | +1.2 | 1.21 | 2.42 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 18 | S_STRANGER | 16.7% | -10.3 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 40.0% | +2.3 | 1.60 | 2.40 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 15.8% | -1.1 | `tdi_rsi_gt_signal` | 10 | S_STRANGER | 20.0% | -0.6 | 0.86 | 3.43 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 19 | S_STRANGER | 15.8% | -2.4 | `confluence_gte_60` | 14 | S_STRANGER | 21.4% | -2.2 | 0.49 | 1.81 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 32 | S_STRANGER | 15.6% | -3.2 | `confluence_gte_60` | 22 | S_STRANGER | 22.7% | -1.4 | 0.75 | 2.55 | 0 | 1 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | +5.8 | `tdi_rsi_gt_signal` | 10 | S_STRANGER | 20.0% | +8.6 | 3.65 | 4.87 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 15.4% | -1.1 | `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 25.0% | +1.9 | 1.48 | 4.43 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -3.1 | `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 25.0% | +0.1 | 1.01 | 3.04 | 0 | 0 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -5.8 | `confluence_gte_70` | 8 | S_STRANGER | 25.0% | -3.8 | 0.35 | 0.71 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -7.2 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | +2.3 | 1.86 | 3.71 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 15.4% | -9.0 | `all` | 13 | S_STRANGER | 15.4% | -9.0 | 0.17 | 0.95 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 20 | S_STRANGER | 15.0% | -0.1 | `all` | 20 | S_STRANGER | 15.0% | -0.1 | 0.96 | 3.62 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 20 | S_STRANGER | 15.0% | -0.9 | `tdi_rsi_gt_signal` | 9 | S_STRANGER | 22.2% | -0.3 | 0.84 | 2.93 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 20 | S_STRANGER | 15.0% | -3.5 | `confluence_gte_60` | 12 | S_STRANGER | 25.0% | -0.2 | 0.91 | 1.58 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -0.5 | `confluence_gte_60` | 8 | S_STRANGER | 25.0% | +3.1 | 2.60 | 6.51 | 0 | 2 | demo_watch_candidate |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -0.6 | `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 28.6% | +5.9 | 1.71 | 4.26 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 14.3% | -0.8 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 33.3% | +0.9 | 1.77 | 3.53 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 14 | S_STRANGER | 14.3% | -0.9 | `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 20.0% | +1.8 | 5.14 | 20.55 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 14.3% | -1.4 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 16.7% | -2.2 | 0.34 | 1.72 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 28 | S_STRANGER | 14.3% | -3.5 | `tdi_rsi_gt_signal` | 17 | S_STRANGER | 23.5% | -1.7 | 0.70 | 2.09 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 28 | S_STRANGER | 14.3% | -3.6 | `tdi_rsi_gte_50` | 16 | S_STRANGER | 18.8% | -4.1 | 0.37 | 1.60 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 14.3% | -4.7 | `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 28.6% | -5.3 | 0.31 | 0.78 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74` | 22 | S_STRANGER | 13.6% | -17.9 | `asian_range_gte_30` | 16 | S_STRANGER | 18.8% | -17.7 | 0.16 | 0.48 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 13.3% | -1.6 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 14.3% | -0.2 | 0.89 | 5.36 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 15 | S_STRANGER | 13.3% | -1.7 | `feature_momentum_breakout_exception` | 6 | S_STRANGER | 16.7% | +0.9 | 1.33 | 2.65 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 13.0% | +0.4 | `asian_range_gte_30` | 17 | S_STRANGER | 17.6% | +1.2 | 1.24 | 3.73 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 23 | S_STRANGER | 13.0% | -1.6 | `asian_range_gte_30` | 16 | S_STRANGER | 18.8% | -0.8 | 0.77 | 2.81 | 0 | 1 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 16 | S_STRANGER | 12.5% | +0.4 | `confluence_gte_70` | 6 | S_STRANGER | 16.7% | +4.0 | 3.14 | 4.70 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 16 | S_STRANGER | 12.5% | -4.8 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 20.0% | -5.9 | 0.02 | 0.07 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 24 | S_STRANGER | 12.5% | -5.6 | `tdi_rsi_gt_signal` | 13 | S_STRANGER | 15.4% | -3.6 | 0.45 | 2.23 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 41 | S_STRANGER | 12.2% | -3.4 | `confluence_gte_70` | 6 | S_STRANGER | 16.7% | -0.2 | 0.96 | 1.93 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | S_STRANGER | 11.8% | -3.3 | `all` | 17 | S_STRANGER | 11.8% | -3.3 | 0.20 | 1.51 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 35 | S_STRANGER | 11.4% | -8.0 | `tdi_rsi_gte_50` | 12 | S_STRANGER | 25.0% | -0.7 | 0.84 | 2.53 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 11.1% | -0.4 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 28.6% | +1.8 | 1.66 | 4.16 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 11.1% | -1.6 | `feature_momentum_breakout_exception` | 11 | S_STRANGER | 18.2% | +0.1 | 1.06 | 4.76 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 27 | S_STRANGER | 11.1% | -3.0 | `asian_range_gte_30` | 24 | S_STRANGER | 12.5% | -3.4 | 0.46 | 1.29 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 18 | S_STRANGER | 11.1% | -3.7 | `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 18.2% | -2.0 | 0.47 | 0.82 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 27 | S_STRANGER | 11.1% | -7.8 | `tdi_rsi_gte_50` | 8 | S_STRANGER | 12.5% | -7.5 | 0.10 | 0.71 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 19 | S_STRANGER | 10.5% | -3.9 | `asian_range_gte_30` | 15 | S_STRANGER | 13.3% | -2.7 | 0.51 | 3.08 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74` | 19 | S_STRANGER | 10.5% | -7.9 | `confluence_gte_60` | 10 | S_STRANGER | 20.0% | -6.0 | 0.37 | 0.85 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 29 | S_STRANGER | 10.3% | -1.1 | `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 20.0% | -0.1 | 0.99 | 3.94 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 29 | S_STRANGER | 10.3% | -8.2 | `ratio_le_2_asian_gte_30_tdi_positive` | 20 | S_STRANGER | 15.0% | -10.0 | 0.18 | 0.71 | 0 | 1 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | +2.1 | `confluence_gte_70` | 5 | S_STRANGER | 20.0% | +8.8 | 25.47 | 12.74 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 10.0% | -2.7 | `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 16.7% | -1.9 | 0.39 | 1.94 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 10.0% | -3.0 | `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 20.0% | -3.3 | 0.27 | 1.10 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS` | 11 | S_STRANGER | 9.1% | -1.6 | `tdi_rsi_gte_50` | 6 | S_STRANGER | 16.7% | -0.4 | 0.79 | 3.96 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS` | 12 | S_STRANGER | 8.3% | -3.1 | `asian_range_gte_30` | 9 | S_STRANGER | 11.1% | -2.9 | 0.07 | 0.56 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74` | 12 | S_STRANGER | 8.3% | -3.2 | `tdi_rsi_gte_50` | 7 | S_STRANGER | 14.3% | -3.0 | 0.22 | 1.35 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 24 | S_STRANGER | 8.3% | -7.2 | `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 15.4% | -6.2 | 0.22 | 0.58 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74` | 13 | S_STRANGER | 7.7% | -0.7 | `tdi_rsi_gt_signal` | 8 | S_STRANGER | 12.5% | -1.4 | 0.41 | 2.44 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS` | 13 | S_STRANGER | 7.7% | -3.5 | `asian_range_gte_30` | 10 | S_STRANGER | 10.0% | -1.0 | 0.53 | 3.73 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74` | 13 | S_STRANGER | 7.7% | -5.6 | `feature_stale_hod_exhaustion_reject` | 8 | S_STRANGER | 12.5% | -3.8 | 0.36 | 2.51 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74` | 42 | S_STRANGER | 7.1% | -3.8 | `ratio_le_2_asian_gte_30_tdi_positive` | 21 | S_STRANGER | 9.5% | +0.2 | 1.05 | 6.32 | 0 | 1 | watch_research |
| `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 15 | S_STRANGER | 6.7% | -1.3 | `feature_momentum_breakout_exception` | 5 | S_STRANGER | 20.0% | -1.3 | 0.15 | 0.46 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 17 | S_STRANGER | 5.9% | -2.7 | `tdi_rsi_gte_50` | 10 | S_STRANGER | 10.0% | -3.0 | 0.29 | 2.59 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74` | 17 | S_STRANGER | 5.9% | -3.9 | `tdi_rsi_gt_signal` | 6 | S_STRANGER | 16.7% | -2.1 | 0.29 | 1.47 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74` | 17 | S_STRANGER | 5.9% | -8.7 | `confluence_gte_60` | 13 | S_STRANGER | 7.7% | -7.4 | 0.09 | 0.48 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 18 | S_STRANGER | 5.6% | -3.9 | `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 11.1% | -4.6 | 0.21 | 0.75 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 18 | S_STRANGER | 5.6% | -4.8 | `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 16.7% | -3.2 | 0.48 | 2.39 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 18 | S_STRANGER | 5.6% | -9.4 | `ratio_le_2_asian_gte_30_tdi_positive` | 16 | S_STRANGER | 6.2% | -9.7 | 0.07 | 1.02 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 0.0% | -1.8 | `all` | 10 | S_STRANGER | 0.0% | -1.8 | 0.20 | 1.21 | 0 | 1 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74` | 11 | S_STRANGER | 0.0% | -3.9 | `confluence_gte_60` | 5 | S_STRANGER | 0.0% | -2.8 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS` | 14 | S_STRANGER | 0.0% | -3.9 | `tdi_rsi_gte_50` | 9 | S_STRANGER | 0.0% | -3.8 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74` | 13 | S_STRANGER | 0.0% | -5.6 | `tdi_rsi_gte_50` | 5 | S_STRANGER | 0.0% | -3.3 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74` | 10 | S_STRANGER | 0.0% | -6.6 | `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 0.0% | -3.4 | 0.00 | 0.00 | 0 | 0 | fail |
| `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` | 10 | S_STRANGER | 0.0% | -13.4 | `tdi_rsi_gt_signal` | 7 | S_STRANGER | 0.0% | -11.4 | 0.00 | 0.00 | 0 | 0 | fail |

## Candidate Details

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+43.7; validation N=4 Fav=50.0% Avg=+19.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | R_REPEATER | 100.0% | 52.6% | 52.6% | 31.6% | +11.1 | 5.07 | 4.06 | +17.8 | +6.0 |
| `hunt_to_ar_ratio_le_2_0` | 19 | R_REPEATER | 100.0% | 52.6% | 52.6% | 31.6% | +11.1 | 5.07 | 4.06 | +17.8 | +6.0 |
| `hunt_to_ar_ratio_le_2_5` | 19 | R_REPEATER | 100.0% | 52.6% | 52.6% | 31.6% | +11.1 | 5.07 | 4.06 | +17.8 | +6.0 |
| `stop_hunt_le_90` | 19 | R_REPEATER | 100.0% | 52.6% | 52.6% | 31.6% | +11.1 | 5.07 | 4.06 | +17.8 | +6.0 |
| `asian_range_gte_30` | 18 | R_REPEATER | 94.7% | 55.6% | 55.6% | 33.3% | +12.1 | 5.93 | 4.15 | +18.6 | +5.9 |
| `confluence_gte_60` | 13 | S_STRANGER | 68.4% | 38.5% | 38.5% | 23.1% | +10.2 | 4.01 | 5.62 | +17.7 | +6.8 |
| `confluence_gte_70` | 5 | R_REPEATER | 26.3% | 60.0% | 60.0% | 40.0% | +24.1 | 6.27 | 4.18 | +31.5 | +8.7 |
| `tdi_rsi_gt_signal` | 3 | R_RUNNER | 15.8% | 100.0% | 100.0% | 66.7% | +21.4 | 999.00 | 999.00 | +24.7 | +2.8 |
| `tdi_rsi_gte_50` | 14 | R_REPEATER | 73.7% | 57.1% | 57.1% | 28.6% | +13.1 | 5.60 | 4.20 | +19.0 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 18 | R_REPEATER | 94.7% | 55.6% | 55.6% | 33.3% | +12.1 | 5.93 | 4.15 | +18.6 | +5.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | R_RUNNER | 15.8% | 100.0% | 100.0% | 66.7% | +21.4 | 999.00 | 999.00 | +24.7 | +2.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | R_REPEATER | 100.0% | 52.6% | 52.6% | 31.6% | +11.1 | 5.07 | 4.06 | +17.8 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 19 | R_REPEATER | 100.0% | 52.6% | 52.6% | 31.6% | +11.1 | 5.07 | 4.06 | +17.8 | +6.0 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 15.8% | 33.3% | 33.3% | 0.0% | -3.4 | 0.04 | 0.08 | +3.3 | +4.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 15.8% | 33.3% | 33.3% | 0.0% | -3.4 | 0.04 | 0.08 | +3.3 | +4.4 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.2; validation N=4 Fav=75.0% Avg=+18.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +8.5 | 6.23 | 6.23 | +16.2 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +8.5 | 6.23 | 6.23 | +16.2 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +8.5 | 6.23 | 6.23 | +16.2 | +5.4 |
| `stop_hunt_le_90` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +8.5 | 6.23 | 6.23 | +16.2 | +5.4 |
| `asian_range_gte_30` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 14.3% | +11.4 | 17.62 | 23.50 | +17.9 | +5.0 |
| `confluence_gte_60` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +8.5 | 6.23 | 6.23 | +16.2 | +5.4 |
| `confluence_gte_70` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +8.5 | 6.23 | 6.23 | +16.2 | +5.4 |
| `tdi_rsi_gt_signal` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 20.0% | +14.6 | 7.23 | 4.82 | +23.6 | +5.0 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 70.0% | 57.1% | 57.1% | 14.3% | +10.3 | 6.45 | 4.84 | +17.6 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 14.3% | +11.4 | 17.62 | 23.50 | +17.9 | +5.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_RUNNER | 40.0% | 75.0% | 75.0% | 25.0% | +21.1 | 423.00 | 141.00 | +26.3 | +2.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +8.5 | 6.23 | 6.23 | +16.2 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 10.0% | +8.5 | 6.23 | 6.23 | +16.2 | +5.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=50.0% Avg=+11.3; validation N=4 Fav=50.0% Avg=+1.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 50.0% | 58.3% | 25.0% | +8.1 | 6.07 | 4.33 | +21.5 | +8.9 |
| `hunt_to_ar_ratio_le_2_0` | 12 | R_REPEATER | 100.0% | 50.0% | 58.3% | 25.0% | +8.1 | 6.07 | 4.33 | +21.5 | +8.9 |
| `hunt_to_ar_ratio_le_2_5` | 12 | R_REPEATER | 100.0% | 50.0% | 58.3% | 25.0% | +8.1 | 6.07 | 4.33 | +21.5 | +8.9 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 100.0% | 50.0% | 58.3% | 25.0% | +8.1 | 6.07 | 4.33 | +21.5 | +8.9 |
| `asian_range_gte_30` | 9 | S_STRANGER | 75.0% | 44.4% | 55.6% | 22.2% | +4.9 | 3.53 | 2.82 | +18.5 | +10.4 |
| `confluence_gte_60` | 12 | R_REPEATER | 100.0% | 50.0% | 58.3% | 25.0% | +8.1 | 6.07 | 4.33 | +21.5 | +8.9 |
| `confluence_gte_70` | 12 | R_REPEATER | 100.0% | 50.0% | 58.3% | 25.0% | +8.1 | 6.07 | 4.33 | +21.5 | +8.9 |
| `tdi_rsi_gt_signal` | 3 | R_RUNNER | 25.0% | 100.0% | 100.0% | 33.3% | +19.2 | 999.00 | 999.00 | +31.3 | +3.2 |
| `tdi_rsi_gte_50` | 10 | R_REPEATER | 83.3% | 50.0% | 50.0% | 30.0% | +7.0 | 4.68 | 4.68 | +21.9 | +10.0 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 75.0% | 44.4% | 55.6% | 22.2% | +4.9 | 3.53 | 2.82 | +18.5 | +10.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 0.0% | +3.2 | 999.00 | 999.00 | +12.2 | +2.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 100.0% | 50.0% | 58.3% | 25.0% | +8.1 | 6.07 | 4.33 | +21.5 | +8.9 |
| `feature_stale_hod_exhaustion_reject` | 12 | R_REPEATER | 100.0% | 50.0% | 58.3% | 25.0% | +8.1 | 6.07 | 4.33 | +21.5 | +8.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=62.5% Avg=+10.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +7.1 | 2.05 | 2.05 | +27.0 | +13.1 |
| `hunt_to_ar_ratio_le_2_0` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +7.1 | 2.05 | 2.05 | +27.0 | +13.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +7.1 | 2.05 | 2.05 | +27.0 | +13.1 |
| `stop_hunt_le_90` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +7.1 | 2.05 | 2.05 | +27.0 | +13.1 |
| `asian_range_gte_30` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +7.1 | 2.05 | 2.05 | +27.0 | +13.1 |
| `confluence_gte_60` | 8 | R_REPEATER | 80.0% | 62.5% | 62.5% | 37.5% | +10.2 | 2.45 | 1.47 | +30.6 | +14.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | +1.7 | 1.33 | 1.33 | +16.7 | +11.3 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 12.5% | -0.9 | 0.90 | 1.50 | +22.0 | +14.4 |
| `ratio_le_2_and_asian_gte_30` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +7.1 | 2.05 | 2.05 | +27.0 | +13.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | +1.7 | 1.33 | 1.33 | +16.7 | +11.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +7.1 | 2.05 | 2.05 | +27.0 | +13.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | R_REPEATER | 100.0% | 50.0% | 50.0% | 30.0% | +7.1 | 2.05 | 2.05 | +27.0 | +13.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | +6.4 | 129.00 | 129.00 | +25.8 | +3.1 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=50.0% Avg=+5.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +4.8 | 4.30 | 4.30 | +12.9 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +5.3 | +8.6 |
| `stop_hunt_le_90` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +4.8 | 4.30 | 4.30 | +12.9 | +5.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +4.8 | 4.30 | 4.30 | +12.9 | +5.0 |
| `confluence_gte_70` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +4.8 | 4.30 | 4.30 | +12.9 | +5.0 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 66.7% | 50.0% | 50.0% | 12.5% | +5.2 | 4.32 | 4.32 | +15.7 | +5.8 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 0.0% | +3.7 | 3.08 | 4.11 | +13.3 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +4.8 | 4.30 | 4.30 | +12.9 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 12 | R_REPEATER | 100.0% | 50.0% | 50.0% | 8.3% | +4.8 | 4.30 | 4.30 | +12.9 | +5.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=66.7% Avg=+8.0; validation N=8 Fav=37.5% Avg=+3.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 4.8% | +3.7 | 3.05 | 3.05 | +11.8 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 6 | R_REPEATER | 28.6% | 50.0% | 50.0% | 0.0% | +2.0 | 2.27 | 2.27 | +10.3 | +6.8 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 42.9% | 44.4% | 44.4% | 11.1% | +4.4 | 5.07 | 5.07 | +12.9 | +5.1 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 4.8% | +3.7 | 3.05 | 3.05 | +11.8 | +6.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 4.8% | +3.7 | 3.05 | 3.05 | +11.8 | +6.5 |
| `confluence_gte_70` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 4.8% | +3.7 | 3.05 | 3.05 | +11.8 | +6.5 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 4.8% | 0.0% | 0.0% | 0.0% | -7.3 | 0.00 | 0.00 | +2.2 | +27.8 |
| `tdi_rsi_gte_50` | 14 | R_REPEATER | 66.7% | 50.0% | 50.0% | 0.0% | +5.2 | 3.51 | 3.51 | +13.6 | +8.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 4.8% | +3.7 | 3.05 | 3.05 | +11.8 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 100.0% | 47.6% | 47.6% | 4.8% | +3.7 | 3.05 | 3.05 | +11.8 | +6.5 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 4.8% | 100.0% | 100.0% | 0.0% | +3.2 | 999.00 | 999.00 | +10.7 | +1.6 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=12 Fav=58.3% Avg=+7.1; validation N=26 Fav=42.3% Avg=+3.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 38 | S_STRANGER | 100.0% | 47.4% | 47.4% | 10.5% | +4.3 | 3.37 | 3.56 | +13.1 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 15.8% | 33.3% | 33.3% | 0.0% | +1.9 | 2.21 | 4.43 | +9.7 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 60.5% | 43.5% | 43.5% | 13.0% | +3.7 | 2.95 | 3.55 | +13.9 | +5.1 |
| `stop_hunt_le_90` | 38 | S_STRANGER | 100.0% | 47.4% | 47.4% | 10.5% | +4.3 | 3.37 | 3.56 | +13.1 | +5.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 38 | S_STRANGER | 100.0% | 47.4% | 47.4% | 10.5% | +4.3 | 3.37 | 3.56 | +13.1 | +5.5 |
| `confluence_gte_70` | 38 | S_STRANGER | 100.0% | 47.4% | 47.4% | 10.5% | +4.3 | 3.37 | 3.56 | +13.1 | +5.5 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 47.4% | 27.8% | 27.8% | 11.1% | +1.2 | 1.49 | 3.58 | +10.2 | +5.8 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 50.0% | 47.4% | 47.4% | 10.5% | +3.5 | 2.84 | 2.84 | +12.0 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 38 | S_STRANGER | 100.0% | 47.4% | 47.4% | 10.5% | +4.3 | 3.37 | 3.56 | +13.1 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 100.0% | 47.4% | 47.4% | 10.5% | +4.3 | 3.37 | 3.56 | +13.1 | +5.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+31.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=40.0% Avg=-2.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 18.2% | +1.0 | 1.28 | 1.54 | +7.8 | +6.8 |
| `hunt_to_ar_ratio_le_2_0` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 0.0% | -5.3 | 0.35 | 0.35 | +4.9 | +10.7 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 20.0% | +3.6 | 1.91 | 2.87 | +10.3 | +5.9 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 18.2% | +1.0 | 1.28 | 1.54 | +7.8 | +6.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 18.2% | +1.0 | 1.28 | 1.54 | +7.8 | +6.8 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 18.2% | +1.0 | 1.28 | 1.54 | +7.8 | +6.8 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 0.0% | +0.9 | 2.23 | 2.23 | +6.3 | +3.3 |
| `tdi_rsi_gte_50` | 8 | R_REPEATER | 72.7% | 50.0% | 50.0% | 12.5% | -1.9 | 0.53 | 0.53 | +6.0 | +6.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 18.2% | +1.0 | 1.28 | 1.54 | +7.8 | +6.8 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 45.5% | 45.5% | 18.2% | +1.0 | 1.28 | 1.54 | +7.8 | +6.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.9; validation N=3 Fav=66.7% Avg=+7.3; out_of_sample N=14 Fav=42.9% Avg=+3.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 33.3% | +3.5 | 2.05 | 2.56 | +11.8 | +7.6 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 77.8% | 42.9% | 42.9% | 35.7% | +4.4 | 2.19 | 2.92 | +12.9 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 33.3% | +3.5 | 2.05 | 2.56 | +11.8 | +7.6 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 33.3% | +3.5 | 2.05 | 2.56 | +11.8 | +7.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 33.3% | +3.5 | 2.05 | 2.56 | +11.8 | +7.6 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 33.3% | +3.5 | 2.05 | 2.56 | +11.8 | +7.6 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 50.0% | 33.3% | 33.3% | 33.3% | +3.0 | 1.64 | 3.28 | +11.5 | +9.8 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 44.4% | 37.5% | 37.5% | 25.0% | +4.0 | 1.87 | 3.12 | +13.2 | +9.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 33.3% | +3.5 | 2.05 | 2.56 | +11.8 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 44.4% | 44.4% | 33.3% | +3.5 | 2.05 | 2.56 | +11.8 | +7.6 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +0.3 | +4.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +0.3 | +4.1 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=50.0% Avg=+12.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=66.7% Avg=+7.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 21.1% | +4.3 | 4.01 | 4.52 | +12.5 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 7 | R_REPEATER | 36.8% | 57.1% | 57.1% | 57.1% | +8.8 | 206.67 | 51.67 | +20.6 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 8 | R_REPEATER | 42.1% | 62.5% | 62.5% | 50.0% | +8.8 | 236.00 | 47.20 | +19.4 | +4.2 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 21.1% | +4.3 | 4.01 | 4.52 | +12.5 | +5.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 21.1% | +4.3 | 4.01 | 4.52 | +12.5 | +5.7 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 21.1% | +4.3 | 4.01 | 4.52 | +12.5 | +5.7 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 21.1% | +4.3 | 4.01 | 4.52 | +12.5 | +5.7 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 73.7% | 42.9% | 42.9% | 7.1% | +3.7 | 2.94 | 3.92 | +11.5 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 89.5% | 47.1% | 47.1% | 23.5% | +5.6 | 7.80 | 6.82 | +13.4 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 42.1% | 42.1% | 21.1% | +4.3 | 4.01 | 4.52 | +12.5 | +5.7 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 10.5% | 50.0% | 50.0% | 50.0% | +7.3 | 2.34 | 2.34 | +17.9 | +7.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 10.5% | 0.0% | 0.0% | 0.0% | -6.5 | 0.00 | 0.00 | +4.8 | +13.8 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=75.0% Avg=+7.9; validation N=1 Fav=100.0% Avg=+36.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 33.3% | +3.2 | 1.90 | 2.28 | +11.1 | +7.8 |
| `hunt_to_ar_ratio_le_2_0` | 2 | R_RUNNER | 16.7% | 100.0% | 100.0% | 100.0% | +29.4 | 999.00 | 999.00 | +31.6 | +2.5 |
| `hunt_to_ar_ratio_le_2_5` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 66.7% | +9.6 | 1.96 | 0.98 | +21.7 | +2.2 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 33.3% | +3.2 | 1.90 | 2.28 | +11.1 | +7.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 5 | R_RUNNER | 41.7% | 80.0% | 80.0% | 60.0% | +13.6 | 999.00 | 999.00 | +17.8 | +13.2 |
| `confluence_gte_70` | 2 | R_RUNNER | 16.7% | 100.0% | 100.0% | 50.0% | +21.5 | 999.00 | 999.00 | +23.3 | +5.7 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 0.0% | +2.9 | 10.67 | 10.67 | +5.8 | +4.7 |
| `tdi_rsi_gte_50` | 3 | R_REPEATER | 25.0% | 66.7% | 66.7% | 33.3% | +14.1 | 71.67 | 35.83 | +16.7 | +4.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 33.3% | +3.2 | 1.90 | 2.28 | +11.1 | +7.8 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 41.7% | 41.7% | 33.3% | +3.2 | 1.90 | 2.28 | +11.1 | +7.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+14.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=50.0% Avg=+1.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +5.5 | 2.62 | 3.93 | +16.2 | +8.4 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +5.5 | 2.62 | 3.93 | +16.2 | +8.4 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +5.5 | 2.62 | 3.93 | +16.2 | +8.4 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +5.5 | 2.62 | 3.93 | +16.2 | +8.4 |
| `asian_range_gte_30` | 11 | S_STRANGER | 73.3% | 36.4% | 36.4% | 27.3% | +6.7 | 2.69 | 4.71 | +19.5 | +8.4 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +5.5 | 2.62 | 3.93 | +16.2 | +8.4 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +5.5 | 2.62 | 3.93 | +16.2 | +8.4 |
| `tdi_rsi_gt_signal` | 3 | R_REPEATER | 20.0% | 66.7% | 66.7% | 33.3% | +18.4 | 27.33 | 13.67 | +24.4 | +9.2 |
| `tdi_rsi_gte_50` | 12 | R_REPEATER | 80.0% | 50.0% | 50.0% | 25.0% | +7.7 | 3.24 | 3.24 | +19.3 | +8.8 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 73.3% | 36.4% | 36.4% | 27.3% | +6.7 | 2.69 | 4.71 | +19.5 | +8.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 50.0% | +24.4 | 24.24 | 24.24 | +31.8 | +9.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +5.5 | 2.62 | 3.93 | +16.2 | +8.4 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 93.3% | 42.9% | 42.9% | 21.4% | +7.6 | 4.79 | 6.38 | +16.5 | +6.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 3 | R_REPEATER | 20.0% | 66.7% | 66.7% | 66.7% | +19.6 | 3.55 | 1.77 | +39.1 | +13.8 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=100.0% Avg=+26.9; validation N=5 Fav=40.0% Avg=+6.8; out_of_sample N=1 Fav=0.0% Avg=-3.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 15.0% | +4.1 | 2.96 | 4.44 | +11.7 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 90.0% | 38.9% | 38.9% | 16.7% | +3.2 | 2.40 | 3.77 | +10.9 | +5.1 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 15.0% | +4.1 | 2.96 | 4.44 | +11.7 | +4.9 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 15.0% | +4.1 | 2.96 | 4.44 | +11.7 | +4.9 |
| `asian_range_gte_30` | 14 | R_REPEATER | 70.0% | 50.0% | 50.0% | 21.4% | +6.2 | 7.21 | 7.21 | +13.1 | +4.1 |
| `confluence_gte_60` | 18 | S_STRANGER | 90.0% | 33.3% | 33.3% | 16.7% | +3.4 | 2.44 | 4.88 | +10.2 | +5.0 |
| `confluence_gte_70` | 8 | R_REPEATER | 40.0% | 50.0% | 50.0% | 25.0% | +10.5 | 9.51 | 9.51 | +15.4 | +3.2 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 45.0% | 44.4% | 44.4% | 11.1% | +5.7 | 5.15 | 6.44 | +12.6 | +4.9 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 45.0% | 33.3% | 33.3% | 0.0% | +2.8 | 2.57 | 5.15 | +8.2 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 14 | R_REPEATER | 70.0% | 50.0% | 50.0% | 21.4% | +6.2 | 7.21 | 7.21 | +13.1 | +4.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 35.0% | 42.9% | 42.9% | 14.3% | +3.8 | 3.23 | 4.31 | +10.7 | +5.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 15.0% | +4.1 | 2.96 | 4.44 | +11.7 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 15.0% | +4.1 | 2.96 | 4.44 | +11.7 | +4.9 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 5.0% | 100.0% | 100.0% | 0.0% | +6.4 | 999.00 | 999.00 | +24.8 | +4.6 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+3.5; validation N=5 Fav=40.0% Avg=+9.3; out_of_sample N=2 Fav=50.0% Avg=+0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +2.1 | 1.45 | 1.82 | +10.5 | +5.1 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 45.0% | 22.2% | 22.2% | 11.1% | -5.1 | 0.38 | 0.95 | +6.4 | +4.7 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 50.0% | 20.0% | 20.0% | 10.0% | -4.7 | 0.38 | 1.13 | +5.8 | +5.1 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +2.1 | 1.45 | 1.82 | +10.5 | +5.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 80.0% | 37.5% | 37.5% | 25.0% | +2.1 | 1.36 | 2.04 | +12.0 | +5.8 |
| `confluence_gte_70` | 2 | R_REPEATER | 10.0% | 50.0% | 50.0% | 0.0% | +1.3 | 1.26 | 1.26 | +10.7 | +9.6 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 50.0% | 40.0% | 40.0% | 0.0% | +3.4 | 2.63 | 3.29 | +7.9 | +4.4 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 50.0% | 40.0% | 40.0% | 10.0% | +5.8 | 3.71 | 4.64 | +10.5 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +2.1 | 1.45 | 1.82 | +10.5 | +5.1 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 40.0% | 40.0% | 20.0% | +2.1 | 1.45 | 1.82 | +10.5 | +5.1 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 20.0% | 25.0% | 25.0% | 0.0% | +2.1 | 3.27 | 6.54 | +4.2 | +2.9 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 15.0% | 33.3% | 33.3% | 0.0% | +3.5 | 7.56 | 7.56 | +5.6 | +2.5 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=75.0% Avg=+6.0; validation N=1 Fav=100.0% Avg=+3.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +1.1 | 1.36 | 1.70 | +7.7 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +1.1 | 1.36 | 1.70 | +7.7 | +5.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +1.1 | 1.36 | 1.70 | +7.7 | +5.9 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +1.1 | 1.36 | 1.70 | +7.7 | +5.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 5 | R_REPEATER | 50.0% | 60.0% | 60.0% | 0.0% | +1.2 | 1.28 | 0.86 | +10.8 | +8.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | R_RUNNER | 50.0% | 80.0% | 80.0% | 0.0% | +5.5 | 3.13 | 0.78 | +11.8 | +6.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 90.0% | 44.4% | 44.4% | 0.0% | +1.2 | 1.36 | 1.70 | +8.0 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +1.1 | 1.36 | 1.70 | +7.7 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 10.0% | +1.1 | 1.36 | 1.70 | +7.7 | +5.9 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 33.3% | -2.8 | 0.00 | 0.00 | +2.6 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -4.2 | 0.00 | 0.00 | +1.2 | +5.0 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=100.0% Avg=+13.5; validation N=1 Fav=0.0% Avg=-18.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 13.3% | +0.8 | 1.19 | 1.59 | +9.3 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 33.3% | 20.0% | 20.0% | 0.0% | -7.6 | 0.22 | 0.88 | +7.0 | +12.6 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 40.0% | 33.3% | 33.3% | 16.7% | -3.9 | 0.52 | 1.04 | +8.5 | +10.7 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 13.3% | +0.8 | 1.19 | 1.59 | +9.3 | +5.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 66.7% | 40.0% | 40.0% | 10.0% | -0.6 | 0.90 | 1.12 | +9.3 | +7.0 |
| `confluence_gte_70` | 2 | R_RUNNER | 13.3% | 100.0% | 100.0% | 50.0% | +12.8 | 999.00 | 999.00 | +14.7 | +4.1 |
| `tdi_rsi_gt_signal` | 2 | R_RUNNER | 13.3% | 100.0% | 100.0% | 50.0% | +15.7 | 999.00 | 999.00 | +16.4 | +1.4 |
| `tdi_rsi_gte_50` | 5 | R_RUNNER | 33.3% | 80.0% | 80.0% | 20.0% | +7.2 | 2.96 | 0.74 | +15.1 | +5.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 13.3% | +0.8 | 1.19 | 1.59 | +9.3 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 40.0% | 40.0% | 13.3% | +0.8 | 1.19 | 1.59 | +9.3 | +5.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=50.0% Avg=+0.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 0.0% | +0.4 | 1.11 | 1.66 | +10.8 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | +1.6 | 1.70 | 5.10 | +11.3 | +6.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 0.0% | -0.7 | 0.84 | 1.40 | +10.9 | +8.2 |
| `confluence_gte_70` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 0.0% | +0.5 | 1.13 | 1.13 | +11.0 | +8.3 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 0.0% | -0.9 | 0.80 | 1.06 | +8.2 | +7.4 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 60.0% | 50.0% | 50.0% | 0.0% | +0.0 | 1.01 | 1.01 | +9.4 | +8.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | +1.6 | 1.70 | 5.10 | +11.3 | +6.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 40.0% | 40.0% | 0.0% | +0.4 | 1.11 | 1.66 | +10.8 | +7.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=57.1% Avg=+17.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | +6.9 | 2.02 | 3.24 | +32.8 | +9.1 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | +6.9 | 2.02 | 3.24 | +32.8 | +9.1 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | +6.9 | 2.02 | 3.24 | +32.8 | +9.1 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | +6.9 | 2.02 | 3.24 | +32.8 | +9.1 |
| `asian_range_gte_30` | 6 | R_REPEATER | 46.2% | 50.0% | 50.0% | 50.0% | +15.4 | 5.60 | 5.60 | +53.5 | +6.5 |
| `confluence_gte_60` | 11 | S_STRANGER | 84.6% | 36.4% | 36.4% | 36.4% | +7.9 | 2.07 | 3.63 | +34.4 | +8.8 |
| `confluence_gte_70` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 25.0% | +4.3 | 1.52 | 4.55 | +36.3 | +11.3 |
| `tdi_rsi_gt_signal` | 7 | R_REPEATER | 53.8% | 57.1% | 57.1% | 57.1% | +17.9 | 4.26 | 3.19 | +53.4 | +12.5 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 53.8% | 57.1% | 57.1% | 57.1% | +17.9 | 4.26 | 3.19 | +53.4 | +12.5 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 46.2% | 50.0% | 50.0% | 50.0% | +15.4 | 5.60 | 5.60 | +53.5 | +6.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | R_RUNNER | 23.1% | 100.0% | 100.0% | 100.0% | +37.6 | 999.00 | 999.00 | +102.6 | +6.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | +6.9 | 2.02 | 3.24 | +32.8 | +9.1 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | +6.9 | 2.02 | 3.24 | +32.8 | +9.1 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 50.0% | +22.3 | 8.97 | 8.97 | +70.4 | +9.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 100.0% | +50.3 | 999.00 | 999.00 | +130.6 | +13.3 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=83.3% Avg=+18.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | +5.3 | 2.16 | 2.59 | +15.3 | +12.5 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | +5.3 | 2.16 | 2.59 | +15.3 | +12.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | +5.3 | 2.16 | 2.59 | +15.3 | +12.5 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | +5.3 | 2.16 | 2.59 | +15.3 | +12.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 69.2% | 33.3% | 33.3% | 33.3% | +2.2 | 1.35 | 2.25 | +13.9 | +13.1 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -14.5 | 0.00 | 0.00 | +12.6 | +18.0 |
| `tdi_rsi_gt_signal` | 6 | R_RUNNER | 46.2% | 83.3% | 83.3% | 50.0% | +18.9 | 8.81 | 1.76 | +28.1 | +9.6 |
| `tdi_rsi_gte_50` | 7 | R_REPEATER | 53.8% | 57.1% | 57.1% | 28.6% | +9.5 | 2.96 | 2.22 | +20.4 | +10.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 100.0% | +26.9 | 999.00 | 999.00 | +35.0 | +8.6 |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 38.5% | 38.5% | 38.5% | +5.3 | 2.16 | 2.59 | +15.3 | +12.5 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 92.3% | 41.7% | 41.7% | 41.7% | +7.2 | 3.12 | 3.12 | +16.6 | +12.0 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 40.0% | +2.7 | 1.98 | 5.93 | +11.5 | +11.9 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 38.5% | 40.0% | 40.0% | 20.0% | +3.1 | 1.46 | 2.19 | +16.7 | +11.3 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=45.5% Avg=+4.4; validation N=10 Fav=40.0% Avg=+1.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 37.5% | 37.5% | 15.6% | +1.1 | 1.29 | 2.15 | +9.5 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 93.8% | 36.7% | 36.7% | 16.7% | +1.0 | 1.26 | 2.18 | +9.5 | +8.3 |
| `hunt_to_ar_ratio_le_2_5` | 32 | S_STRANGER | 100.0% | 37.5% | 37.5% | 15.6% | +1.1 | 1.29 | 2.15 | +9.5 | +8.2 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 100.0% | 37.5% | 37.5% | 15.6% | +1.1 | 1.29 | 2.15 | +9.5 | +8.2 |
| `asian_range_gte_30` | 24 | S_STRANGER | 75.0% | 37.5% | 37.5% | 16.7% | +1.1 | 1.27 | 2.11 | +10.1 | +9.0 |
| `confluence_gte_60` | 17 | S_STRANGER | 53.1% | 35.3% | 35.3% | 17.6% | +1.0 | 1.27 | 2.33 | +10.8 | +8.8 |
| `confluence_gte_70` | 3 | S_STRANGER | 9.4% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +9.5 | +7.7 |
| `tdi_rsi_gt_signal` | 27 | S_STRANGER | 84.4% | 40.7% | 40.7% | 18.5% | +2.6 | 1.89 | 2.75 | +10.9 | +7.8 |
| `tdi_rsi_gte_50` | 21 | S_STRANGER | 65.6% | 38.1% | 38.1% | 14.3% | +2.1 | 1.71 | 2.78 | +11.4 | +8.7 |
| `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 75.0% | 37.5% | 37.5% | 16.7% | +1.1 | 1.27 | 2.11 | +10.1 | +9.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 21 | S_STRANGER | 65.6% | 42.9% | 42.9% | 19.0% | +2.9 | 1.96 | 2.62 | +11.4 | +8.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 100.0% | 37.5% | 37.5% | 15.6% | +1.1 | 1.29 | 2.15 | +9.5 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 37.5% | 37.5% | 15.6% | +1.1 | 1.29 | 2.15 | +9.5 | +8.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=20 Fav=40.0% Avg=+2.9; validation N=7 Fav=57.1% Avg=+5.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 38 | S_STRANGER | 100.0% | 36.8% | 39.5% | 15.8% | +3.2 | 2.32 | 3.40 | +10.9 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 35 | S_STRANGER | 92.1% | 40.0% | 42.9% | 14.3% | +3.6 | 2.43 | 3.24 | +11.3 | +7.3 |
| `hunt_to_ar_ratio_le_2_5` | 37 | S_STRANGER | 97.4% | 37.8% | 40.5% | 13.5% | +3.3 | 2.32 | 3.40 | +10.9 | +7.4 |
| `stop_hunt_le_90` | 38 | S_STRANGER | 100.0% | 36.8% | 39.5% | 15.8% | +3.2 | 2.32 | 3.40 | +10.9 | +7.2 |
| `asian_range_gte_30` | 29 | S_STRANGER | 76.3% | 37.9% | 41.4% | 13.8% | +2.4 | 1.82 | 2.59 | +10.5 | +6.8 |
| `confluence_gte_60` | 29 | S_STRANGER | 76.3% | 34.5% | 37.9% | 10.3% | +3.3 | 2.11 | 3.46 | +10.9 | +8.2 |
| `confluence_gte_70` | 3 | S_STRANGER | 7.9% | 33.3% | 33.3% | 0.0% | +3.8 | 4.42 | 8.85 | +15.8 | +8.0 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 13.2% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +3.4 | +6.0 |
| `tdi_rsi_gte_50` | 27 | S_STRANGER | 71.1% | 44.4% | 44.4% | 11.1% | +3.5 | 2.19 | 2.74 | +11.2 | +8.3 |
| `ratio_le_2_and_asian_gte_30` | 28 | S_STRANGER | 73.7% | 39.3% | 42.9% | 14.3% | +2.6 | 1.89 | 2.52 | +10.7 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 10.5% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +3.2 | +6.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 38 | S_STRANGER | 100.0% | 36.8% | 39.5% | 15.8% | +3.2 | 2.32 | 3.40 | +10.9 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 100.0% | 36.8% | 39.5% | 15.8% | +3.2 | 2.32 | 3.40 | +10.9 | +7.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=17 Fav=35.3% Avg=-3.2; out_of_sample N=5 Fav=40.0% Avg=-17.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 13.6% | -6.4 | 0.37 | 0.65 | +6.7 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 13.6% | 33.3% | 33.3% | 33.3% | -7.6 | 0.47 | 0.94 | +11.3 | +2.2 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 31.8% | 28.6% | 28.6% | 14.3% | -6.8 | 0.36 | 0.89 | +6.9 | +3.0 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 13.6% | -6.4 | 0.37 | 0.65 | +6.7 | +5.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 13.6% | -6.4 | 0.37 | 0.65 | +6.7 | +5.6 |
| `confluence_gte_70` | 13 | S_STRANGER | 59.1% | 23.1% | 23.1% | 0.0% | -9.3 | 0.08 | 0.28 | +4.0 | +5.7 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 68.2% | 26.7% | 26.7% | 6.7% | -3.4 | 0.48 | 1.33 | +6.2 | +4.6 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +1.4 | +3.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 13.6% | -6.4 | 0.37 | 0.65 | +6.7 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 36.4% | 36.4% | 13.6% | -6.4 | 0.37 | 0.65 | +6.7 | +5.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=19 Fav=36.8% Avg=+2.6; validation N=7 Fav=42.9% Avg=+6.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 36 | S_STRANGER | 100.0% | 36.1% | 36.1% | 25.0% | +2.6 | 1.67 | 2.70 | +13.6 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 34 | S_STRANGER | 94.4% | 35.3% | 35.3% | 26.5% | +2.3 | 1.59 | 2.64 | +13.2 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 36 | S_STRANGER | 100.0% | 36.1% | 36.1% | 25.0% | +2.6 | 1.67 | 2.70 | +13.6 | +6.3 |
| `stop_hunt_le_90` | 36 | S_STRANGER | 100.0% | 36.1% | 36.1% | 25.0% | +2.6 | 1.67 | 2.70 | +13.6 | +6.3 |
| `asian_range_gte_30` | 26 | S_STRANGER | 72.2% | 38.5% | 38.5% | 26.9% | +3.6 | 1.90 | 2.85 | +14.4 | +5.6 |
| `confluence_gte_60` | 26 | S_STRANGER | 72.2% | 34.6% | 34.6% | 26.9% | +3.6 | 2.23 | 3.71 | +14.0 | +6.9 |
| `confluence_gte_70` | 8 | S_STRANGER | 22.2% | 25.0% | 25.0% | 0.0% | -0.9 | 0.68 | 2.05 | +6.5 | +7.3 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 13.9% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +4.7 | +12.4 |
| `tdi_rsi_gte_50` | 29 | S_STRANGER | 80.6% | 34.5% | 34.5% | 20.7% | +3.6 | 2.31 | 4.15 | +14.3 | +6.7 |
| `ratio_le_2_and_asian_gte_30` | 26 | S_STRANGER | 72.2% | 38.5% | 38.5% | 26.9% | +3.6 | 1.90 | 2.85 | +14.4 | +5.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -3.6 | 0.00 | 0.00 | +2.4 | +7.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 36 | S_STRANGER | 100.0% | 36.1% | 36.1% | 25.0% | +2.6 | 1.67 | 2.70 | +13.6 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 36 | S_STRANGER | 100.0% | 36.1% | 36.1% | 25.0% | +2.6 | 1.67 | 2.70 | +13.6 | +6.3 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 2.8% | 100.0% | 100.0% | 100.0% | +12.0 | 999.00 | 999.00 | +13.7 | +1.7 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=50.0% Avg=+4.3; out_of_sample N=1 Fav=100.0% Avg=+9.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +2.7 | 3.14 | 5.75 | +8.5 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 4 | R_REPEATER | 23.5% | 50.0% | 50.0% | 50.0% | +4.3 | 10.00 | 10.00 | +8.9 | +2.4 |
| `hunt_to_ar_ratio_le_2_5` | 5 | R_REPEATER | 29.4% | 60.0% | 60.0% | 60.0% | +5.4 | 15.16 | 10.11 | +10.0 | +2.1 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +2.7 | 3.14 | 5.75 | +8.5 | +3.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +2.7 | 3.14 | 5.75 | +8.5 | +3.9 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +2.7 | 3.14 | 5.75 | +8.5 | +3.9 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 88.2% | 26.7% | 26.7% | 20.0% | +1.7 | 2.18 | 6.00 | +7.7 | +4.0 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 82.4% | 28.6% | 28.6% | 21.4% | +2.0 | 2.47 | 6.18 | +7.7 | +3.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +2.7 | 3.14 | 5.75 | +8.5 | +3.9 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 35.3% | 35.3% | 29.4% | +2.7 | 3.14 | 5.75 | +8.5 | +3.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-5.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=13 Fav=46.2% Avg=+3.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 34.4% | 37.5% | 6.2% | -0.0 | 0.99 | 1.57 | +9.3 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 43.8% | 42.9% | 50.0% | 7.1% | +3.0 | 2.85 | 2.45 | +9.5 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 59.4% | 36.8% | 42.1% | 5.3% | +1.0 | 1.32 | 1.64 | +9.0 | +4.7 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 100.0% | 34.4% | 37.5% | 6.2% | -0.0 | 0.99 | 1.57 | +9.3 | +6.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 32 | S_STRANGER | 100.0% | 34.4% | 37.5% | 6.2% | -0.0 | 0.99 | 1.57 | +9.3 | +6.4 |
| `confluence_gte_70` | 32 | S_STRANGER | 100.0% | 34.4% | 37.5% | 6.2% | -0.0 | 0.99 | 1.57 | +9.3 | +6.4 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 53.1% | 35.3% | 35.3% | 0.0% | -0.2 | 0.97 | 1.77 | +8.5 | +7.3 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 56.2% | 38.9% | 38.9% | 0.0% | +1.5 | 1.42 | 2.23 | +9.5 | +7.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 90.6% | 37.9% | 41.4% | 6.9% | +0.5 | 1.11 | 1.48 | +9.2 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 96.9% | 35.5% | 38.7% | 6.5% | +0.0 | 1.01 | 1.51 | +9.2 | +6.5 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +8.1 | +9.1 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -4.8 | 0.00 | 0.00 | +7.7 | +6.9 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+22.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 25.0% | +10.9 | 6.02 | 8.43 | +25.6 | +11.5 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 25.0% | +10.9 | 6.02 | 8.43 | +25.6 | +11.5 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 25.0% | +10.9 | 6.02 | 8.43 | +25.6 | +11.5 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 25.0% | +10.9 | 6.02 | 8.43 | +25.6 | +11.5 |
| `asian_range_gte_30` | 6 | R_REPEATER | 50.0% | 50.0% | 50.0% | 33.3% | +22.1 | 10.77 | 10.77 | +42.0 | +18.4 |
| `confluence_gte_60` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 20.0% | +11.6 | 4.45 | 17.79 | +30.0 | +13.8 |
| `confluence_gte_70` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -2.0 | 0.00 | 0.00 | +15.4 | +5.0 |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +74.7 | 999.00 | 999.00 | +94.6 | +11.1 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 28.6% | +17.7 | 6.51 | 8.68 | +37.8 | +18.0 |
| `ratio_le_2_and_asian_gte_30` | 6 | R_REPEATER | 50.0% | 50.0% | 50.0% | 33.3% | +22.1 | 10.77 | 10.77 | +42.0 | +18.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +74.7 | 999.00 | 999.00 | +94.6 | +11.1 |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +38.6 | 999.00 | 999.00 | +60.2 | +21.6 |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 25.0% | +10.9 | 6.02 | 8.43 | +25.6 | +11.5 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 25.0% | +10.9 | 6.02 | 8.43 | +25.6 | +11.5 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +10.5 | +7.1 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 20.0% | +3.2 | 1.72 | 6.86 | +22.8 | +17.8 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=66.7% Avg=+8.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=33.3% Avg=+4.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 0.0% | +3.4 | 1.77 | 2.48 | +13.7 | +8.5 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 0.0% | +4.7 | 5.37 | 10.75 | +12.4 | +9.1 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 0.0% | +4.7 | 5.37 | 10.75 | +12.4 | +9.1 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 0.0% | +3.4 | 1.77 | 2.48 | +13.7 | +8.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 0.0% | +3.4 | 1.77 | 2.48 | +13.7 | +8.5 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 0.0% | +3.4 | 1.77 | 2.48 | +13.7 | +8.5 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 0.0% | +6.0 | 2.93 | 3.66 | +14.0 | +10.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 75.0% | 44.4% | 44.4% | 0.0% | +6.0 | 2.93 | 3.66 | +14.0 | +10.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 83.3% | 30.0% | 40.0% | 0.0% | +3.3 | 1.68 | 2.53 | +14.0 | +7.9 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 41.7% | 0.0% | +3.4 | 1.77 | 2.48 | +13.7 | +8.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 16.7% | 50.0% | 50.0% | 0.0% | +4.2 | 2.53 | 2.53 | +12.3 | +12.0 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=0.0% Avg=-8.2; validation N=11 Fav=54.5% Avg=+10.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 27.8% | +3.3 | 1.76 | 3.22 | +14.1 | +9.7 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 27.8% | +3.3 | 1.76 | 3.22 | +14.1 | +9.7 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 27.8% | +3.3 | 1.76 | 3.22 | +14.1 | +9.7 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 27.8% | +3.3 | 1.76 | 3.22 | +14.1 | +9.7 |
| `asian_range_gte_30` | 15 | S_STRANGER | 83.3% | 26.7% | 26.7% | 20.0% | -1.3 | 0.74 | 1.85 | +10.9 | +10.6 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 27.8% | +3.3 | 1.76 | 3.22 | +14.1 | +9.7 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 27.8% | +3.3 | 1.76 | 3.22 | +14.1 | +9.7 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 61.1% | 18.2% | 18.2% | 9.1% | +1.8 | 1.39 | 5.55 | +12.3 | +11.7 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 66.7% | 25.0% | 25.0% | 16.7% | +2.1 | 1.42 | 3.78 | +15.5 | +10.4 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 83.3% | 26.7% | 26.7% | 20.0% | -1.3 | 0.74 | 1.85 | +10.9 | +10.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 50.0% | 11.1% | 11.1% | 0.0% | -4.3 | 0.26 | 1.81 | +7.8 | +13.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 27.8% | +3.3 | 1.76 | 3.22 | +14.1 | +9.7 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 27.8% | +3.3 | 1.76 | 3.22 | +14.1 | +9.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+8.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=50.0% Avg=+1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | +2.3 | 1.51 | 2.64 | +12.3 | +9.2 |
| `hunt_to_ar_ratio_le_2_0` | 6 | R_REPEATER | 50.0% | 50.0% | 50.0% | 33.3% | +5.2 | 1.74 | 1.74 | +17.1 | +12.6 |
| `hunt_to_ar_ratio_le_2_5` | 8 | R_REPEATER | 66.7% | 50.0% | 50.0% | 25.0% | +5.1 | 1.95 | 1.95 | +14.7 | +10.2 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | +2.3 | 1.51 | 2.64 | +12.3 | +9.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | +2.3 | 1.51 | 2.64 | +12.3 | +9.2 |
| `confluence_gte_70` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -21.7 | 0.00 | 0.00 | +6.6 | +25.7 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 16.7% | -1.2 | 0.66 | 0.99 | +7.7 | +8.8 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 41.7% | 40.0% | 40.0% | 40.0% | +5.6 | 2.40 | 2.40 | +13.3 | +9.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | +2.3 | 1.51 | 2.64 | +12.3 | +9.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 25.0% | +2.3 | 1.51 | 2.64 | +12.3 | +9.2 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 33.3% | -1.9 | 0.84 | 1.68 | +13.1 | +19.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -14.1 | 0.00 | 0.00 | +0.3 | +21.2 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=100.0% Avg=+29.6; validation N=5 Fav=20.0% Avg=-3.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 41.7% | +2.1 | 1.35 | 2.37 | +15.2 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 41.7% | +2.1 | 1.35 | 2.37 | +15.2 | +7.7 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 41.7% | +2.1 | 1.35 | 2.37 | +15.2 | +7.7 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 41.7% | +2.1 | 1.35 | 2.37 | +15.2 | +7.7 |
| `asian_range_gte_30` | 11 | S_STRANGER | 91.7% | 36.4% | 36.4% | 45.5% | +3.6 | 1.72 | 2.58 | +16.4 | +6.8 |
| `confluence_gte_60` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 30.0% | -3.4 | 0.51 | 1.79 | +10.3 | +9.1 |
| `confluence_gte_70` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 33.3% | -7.8 | 0.00 | 0.00 | +8.1 | +14.9 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 33.3% | +7.0 | 3.32 | 6.64 | +17.4 | +4.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 42.9% | 42.9% | 42.9% | +6.3 | 2.07 | 2.76 | +18.7 | +7.9 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 91.7% | 36.4% | 36.4% | 45.5% | +3.6 | 1.72 | 2.58 | +16.4 | +6.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 33.3% | +7.0 | 3.32 | 6.64 | +17.4 | +4.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 41.7% | +2.1 | 1.35 | 2.37 | +15.2 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 41.7% | +2.1 | 1.35 | 2.37 | +15.2 | +7.7 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +29.0 | 999.00 | 999.00 | +39.3 | +1.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +29.0 | 999.00 | 999.00 | +39.3 | +1.5 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=11 Fav=45.5% Avg=+9.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 19.0% | +0.8 | 1.12 | 2.09 | +17.0 | +11.1 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 33.3% | 42.9% | 42.9% | 28.6% | +8.2 | 6.54 | 8.72 | +25.6 | +6.8 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 52.4% | 45.5% | 45.5% | 36.4% | +9.2 | 4.95 | 5.94 | +23.2 | +7.4 |
| `stop_hunt_le_90` | 21 | S_STRANGER | 100.0% | 33.3% | 33.3% | 19.0% | +0.8 | 1.12 | 2.09 | +17.0 | +11.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 66.7% | 35.7% | 35.7% | 21.4% | +1.9 | 1.43 | 2.58 | +16.5 | +9.4 |
| `confluence_gte_70` | 2 | R_RUNNER | 9.5% | 100.0% | 100.0% | 100.0% | +29.4 | 999.00 | 999.00 | +33.3 | +0.8 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 9.5% | 0.0% | 0.0% | 0.0% | -6.3 | 0.00 | 0.00 | +11.2 | +12.7 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 76.2% | 31.2% | 31.2% | 12.5% | -1.9 | 0.76 | 1.67 | +17.4 | +12.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 81.0% | 41.2% | 41.2% | 23.5% | +1.7 | 1.23 | 1.76 | +18.9 | +11.1 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 85.7% | 33.3% | 33.3% | 22.2% | +1.1 | 1.15 | 2.11 | +17.4 | +11.7 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 19.0% | 50.0% | 50.0% | 25.0% | +5.9 | 5.80 | 2.90 | +14.4 | +6.5 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 14.3% | 33.3% | 33.3% | 0.0% | -0.9 | 0.63 | 1.26 | +14.6 | +7.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-2.1; validation N=9 Fav=55.6% Avg=+4.6; out_of_sample N=3 Fav=0.0% Avg=-11.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.2 | 1.05 | 2.09 | +8.0 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 40.0% | 16.7% | 16.7% | 0.0% | -2.9 | 0.19 | 0.93 | +2.6 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 53.3% | 25.0% | 25.0% | 0.0% | -2.0 | 0.35 | 1.06 | +3.6 | +6.3 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.2 | 1.05 | 2.09 | +8.0 | +6.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.2 | 1.05 | 2.09 | +8.0 | +6.5 |
| `confluence_gte_70` | 3 | R_REPEATER | 20.0% | 66.7% | 66.7% | 33.3% | +10.9 | 55.33 | 27.67 | +17.6 | +3.6 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 46.7% | 0.0% | 0.0% | 0.0% | -4.8 | 0.00 | 0.00 | +3.3 | +7.3 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 66.7% | 20.0% | 20.0% | 0.0% | -3.0 | 0.13 | 0.52 | +4.5 | +6.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.2 | 1.05 | 2.09 | +8.0 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.2 | 1.05 | 2.09 | +8.0 | +6.5 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +3.6 | +3.9 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +3.6 | +3.9 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=11 Fav=36.4% Avg=+1.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.1 | 1.05 | 2.10 | +6.7 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.1 | 1.05 | 2.10 | +6.7 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.1 | 1.05 | 2.10 | +6.7 | +4.6 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.1 | 1.05 | 2.10 | +6.7 | +4.6 |
| `asian_range_gte_30` | 13 | S_STRANGER | 86.7% | 30.8% | 30.8% | 7.7% | +0.1 | 1.02 | 2.30 | +6.9 | +4.8 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.1 | 1.05 | 2.10 | +6.7 | +4.6 |
| `confluence_gte_70` | 12 | S_STRANGER | 80.0% | 33.3% | 33.3% | 8.3% | +0.3 | 1.09 | 2.17 | +7.1 | +5.3 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 73.3% | 36.4% | 36.4% | 9.1% | +1.0 | 1.38 | 2.42 | +7.6 | +4.9 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 60.0% | 33.3% | 33.3% | 0.0% | +1.1 | 1.47 | 2.94 | +7.2 | +6.6 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 86.7% | 30.8% | 30.8% | 7.7% | +0.1 | 1.02 | 2.30 | +6.9 | +4.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 60.0% | 33.3% | 33.3% | 11.1% | +1.1 | 1.35 | 2.69 | +8.1 | +5.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.1 | 1.05 | 2.10 | +6.7 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | +0.1 | 1.05 | 2.10 | +6.7 | +4.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-3.0; validation N=10 Fav=40.0% Avg=+0.6; out_of_sample N=2 Fav=50.0% Avg=+1.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 46.7% | 20.0% | +0.1 | 1.05 | 1.05 | +6.9 | +4.5 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 33.3% | 46.7% | 20.0% | +0.1 | 1.05 | 1.05 | +6.9 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 33.3% | 46.7% | 20.0% | +0.1 | 1.05 | 1.05 | +6.9 | +4.5 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 33.3% | 46.7% | 20.0% | +0.1 | 1.05 | 1.05 | +6.9 | +4.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 93.3% | 35.7% | 50.0% | 21.4% | +0.1 | 1.05 | 0.90 | +7.3 | +4.5 |
| `confluence_gte_70` | 3 | S_STRANGER | 20.0% | 33.3% | 66.7% | 0.0% | -2.1 | 0.50 | 0.25 | +7.1 | +5.8 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 80.0% | 33.3% | 41.7% | 25.0% | -0.3 | 0.90 | 1.08 | +7.8 | +4.9 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 33.3% | 40.0% | 40.0% | 0.0% | -2.5 | 0.32 | 0.48 | +7.9 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 33.3% | 46.7% | 20.0% | +0.1 | 1.05 | 1.05 | +6.9 | +4.5 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 33.3% | 46.7% | 20.0% | +0.1 | 1.05 | 1.05 | +6.9 | +4.5 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +1.5 | +5.2 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +1.0 | +5.6 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=44.4% Avg=+4.4; validation N=9 Fav=22.2% Avg=-5.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 33.3% | -0.5 | 0.89 | 1.27 | +13.4 | +6.8 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 33.3% | -0.5 | 0.89 | 1.27 | +13.4 | +6.8 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 33.3% | -0.5 | 0.89 | 1.27 | +13.4 | +6.8 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 33.3% | -0.5 | 0.89 | 1.27 | +13.4 | +6.8 |
| `asian_range_gte_30` | 16 | S_STRANGER | 88.9% | 31.2% | 37.5% | 31.2% | -1.0 | 0.77 | 1.16 | +13.7 | +7.5 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 33.3% | -0.5 | 0.89 | 1.27 | +13.4 | +6.8 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 33.3% | -0.5 | 0.89 | 1.27 | +13.4 | +6.8 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 27.8% | 0.0% | 0.0% | 0.0% | -8.9 | 0.00 | 0.00 | +7.6 | +13.1 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 66.7% | 33.3% | 33.3% | 41.7% | -1.2 | 0.76 | 1.33 | +14.8 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 88.9% | 31.2% | 37.5% | 31.2% | -1.0 | 0.77 | 1.16 | +13.7 | +7.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 27.8% | 0.0% | 0.0% | 0.0% | -8.9 | 0.00 | 0.00 | +7.6 | +13.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 33.3% | -0.5 | 0.89 | 1.27 | +13.4 | +6.8 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 33.3% | -0.5 | 0.89 | 1.27 | +13.4 | +6.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=12 Fav=41.7% Avg=+4.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 22.2% | -0.6 | 0.92 | 1.45 | +16.7 | +11.9 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 33.3% | -2.8 | 0.83 | 1.66 | +18.5 | +19.2 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 38.9% | 28.6% | 28.6% | 28.6% | -1.6 | 0.82 | 2.06 | +18.3 | +12.3 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 33.3% | 38.9% | 22.2% | -0.6 | 0.92 | 1.45 | +16.7 | +11.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 88.9% | 37.5% | 37.5% | 25.0% | -0.5 | 0.93 | 1.55 | +17.2 | +12.2 |
| `confluence_gte_70` | 5 | S_STRANGER | 27.8% | 20.0% | 20.0% | 20.0% | -14.6 | 0.16 | 0.65 | +13.9 | +19.9 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 22.2% | 50.0% | 50.0% | 0.0% | -6.4 | 0.31 | 0.31 | +13.8 | +12.9 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 77.8% | 35.7% | 35.7% | 21.4% | -1.6 | 0.78 | 1.41 | +16.6 | +12.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 72.2% | 23.1% | 30.8% | 15.4% | -4.7 | 0.52 | 1.17 | +13.7 | +14.5 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 66.7% | 41.7% | 50.0% | 33.3% | +4.4 | 1.84 | 1.84 | +18.9 | +9.8 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 27.8% | 40.0% | 40.0% | 40.0% | +1.8 | 1.22 | 1.83 | +21.7 | +12.9 |
| `feature_eurjpy_tdi50_reclaim` | 8 | S_STRANGER | 44.4% | 25.0% | 25.0% | 12.5% | -6.5 | 0.33 | 0.99 | +14.7 | +13.7 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=66.7% Avg=+10.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.8 | 0.90 | 1.79 | +15.4 | +10.5 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 33.3% | -0.2 | 0.97 | 1.95 | +14.7 | +14.6 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 33.3% | -0.2 | 0.97 | 1.95 | +14.7 | +14.6 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.8 | 0.90 | 1.79 | +15.4 | +10.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 83.3% | 40.0% | 40.0% | 40.0% | -0.5 | 0.94 | 1.41 | +15.8 | +11.3 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.8 | 0.90 | 1.79 | +15.4 | +10.5 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -7.3 | 0.00 | 0.00 | +11.8 | +15.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 22.2% | -4.3 | 0.55 | 1.94 | +13.7 | +11.5 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 33.3% | 33.3% | 33.3% | -0.8 | 0.90 | 1.79 | +15.4 | +10.5 |
| `feature_momentum_breakout_exception` | 6 | R_REPEATER | 50.0% | 66.7% | 66.7% | 66.7% | +10.1 | 4.05 | 2.02 | +19.5 | +7.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +2.6 | +8.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=50.0% Avg=+1.8; validation N=3 Fav=0.0% Avg=-6.4; out_of_sample N=1 Fav=100.0% Avg=+12.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | -1.0 | 0.79 | 1.43 | +10.4 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 93.3% | 28.6% | 28.6% | 7.1% | -1.9 | 0.62 | 1.39 | +9.9 | +7.8 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | -1.0 | 0.79 | 1.43 | +10.4 | +7.7 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | -1.0 | 0.79 | 1.43 | +10.4 | +7.7 |
| `asian_range_gte_30` | 8 | S_STRANGER | 53.3% | 37.5% | 37.5% | 12.5% | +0.1 | 1.02 | 1.36 | +11.2 | +5.9 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | -1.0 | 0.79 | 1.43 | +10.4 | +7.7 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | -1.0 | 0.79 | 1.43 | +10.4 | +7.7 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -16.0 | 0.00 | 0.00 | +3.9 | +21.3 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 86.7% | 38.5% | 38.5% | 0.0% | -0.5 | 0.89 | 1.43 | +11.4 | +7.5 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 53.3% | 37.5% | 37.5% | 12.5% | +0.1 | 1.02 | 1.36 | +11.2 | +5.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 33.3% | 33.3% | 6.7% | -1.0 | 0.79 | 1.43 | +10.4 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 93.3% | 35.7% | 35.7% | 7.1% | -1.0 | 0.80 | 1.29 | +10.9 | +8.1 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 0.0% | +2.3 | 5.50 | 5.50 | +13.7 | +2.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 13.3% | 50.0% | 50.0% | 0.0% | +2.3 | 5.50 | 5.50 | +13.7 | +2.8 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=25.0% Avg=-1.7; validation N=2 Fav=50.0% Avg=+7.6; out_of_sample N=2 Fav=50.0% Avg=-4.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -1.1 | 0.74 | 1.48 | +6.9 | +6.9 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 44.4% | 37.5% | 37.5% | 0.0% | +0.0 | 1.01 | 1.68 | +8.8 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 55.6% | 30.0% | 30.0% | 0.0% | -0.8 | 0.83 | 1.94 | +7.4 | +7.8 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -1.1 | 0.74 | 1.48 | +6.9 | +6.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -1.1 | 0.74 | 1.48 | +6.9 | +6.9 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 33.3% | 33.3% | 0.0% | -1.1 | 0.74 | 1.48 | +6.9 | +6.9 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 44.4% | 25.0% | 25.0% | 0.0% | -4.0 | 0.17 | 0.50 | +2.7 | +7.0 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 77.8% | 28.6% | 28.6% | 0.0% | -1.6 | 0.66 | 1.65 | +6.0 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 88.9% | 31.2% | 31.2% | 0.0% | -1.2 | 0.73 | 1.62 | +6.6 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 94.4% | 29.4% | 29.4% | 0.0% | -1.4 | 0.69 | 1.65 | +7.0 | +7.2 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 27.8% | 40.0% | 40.0% | 0.0% | -0.8 | 0.63 | 0.94 | +6.9 | +4.2 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 0.0% | -0.3 | 0.83 | 1.65 | +2.3 | +4.5 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+3.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=9 Fav=44.4% Avg=+0.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 33.3% | 33.3% | 12.5% | -2.6 | 0.59 | 1.17 | +8.9 | +7.9 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 50.0% | 41.7% | 41.7% | 25.0% | +0.9 | 1.21 | 1.69 | +11.7 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 62.5% | 40.0% | 40.0% | 20.0% | -1.3 | 0.79 | 1.19 | +10.7 | +7.3 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 33.3% | 33.3% | 12.5% | -2.6 | 0.59 | 1.17 | +8.9 | +7.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 23 | S_STRANGER | 95.8% | 34.8% | 34.8% | 13.0% | -2.6 | 0.60 | 1.12 | +9.2 | +7.9 |
| `confluence_gte_70` | 13 | S_STRANGER | 54.2% | 30.8% | 30.8% | 15.4% | -3.3 | 0.58 | 1.31 | +9.3 | +9.1 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 66.7% | 25.0% | 25.0% | 6.2% | -5.6 | 0.28 | 0.83 | +7.8 | +8.1 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 37.5% | 33.3% | 33.3% | 22.2% | +1.0 | 1.23 | 2.46 | +12.1 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -18.0 | 0.00 | 0.00 | +7.4 | +27.0 |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 95.8% | 34.8% | 34.8% | 13.0% | -1.9 | 0.66 | 1.25 | +8.9 | +7.0 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 33.3% | 33.3% | 12.5% | -2.6 | 0.59 | 1.17 | +8.9 | +7.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -18.0 | 0.00 | 0.00 | +7.4 | +27.0 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+7.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 32.3% | 32.3% | 16.1% | +2.2 | 1.91 | 3.63 | +8.8 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 28 | S_STRANGER | 90.3% | 35.7% | 35.7% | 17.9% | +2.8 | 2.27 | 3.86 | +9.3 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 100.0% | 32.3% | 32.3% | 16.1% | +2.2 | 1.91 | 3.63 | +8.8 | +5.4 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 32.3% | 32.3% | 16.1% | +2.2 | 1.91 | 3.63 | +8.8 | +5.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 24 | S_STRANGER | 77.4% | 37.5% | 37.5% | 16.7% | +3.1 | 2.22 | 3.46 | +9.6 | +5.3 |
| `confluence_gte_70` | 3 | S_STRANGER | 9.7% | 33.3% | 33.3% | 0.0% | -0.4 | 0.87 | 1.75 | +4.3 | +5.6 |
| `tdi_rsi_gt_signal` | 24 | S_STRANGER | 77.4% | 29.2% | 29.2% | 12.5% | +2.1 | 1.87 | 4.27 | +8.3 | +5.1 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 32.3% | 10.0% | 10.0% | 0.0% | -2.4 | 0.16 | 1.40 | +3.1 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 32.3% | 32.3% | 16.1% | +2.2 | 1.91 | 3.63 | +8.8 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 32.3% | 32.3% | 16.1% | +2.2 | 1.91 | 3.63 | +8.8 | +5.4 |
| `feature_momentum_breakout_exception` | 6 | R_REPEATER | 19.4% | 50.0% | 50.0% | 50.0% | +7.2 | 6.09 | 6.09 | +14.9 | +3.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 6.5% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +2.5 | +3.0 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=16.7% Avg=-3.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=16 Fav=37.5% Avg=+1.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 31.8% | 31.8% | 9.1% | +0.0 | 1.01 | 1.73 | +10.6 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 18.2% | 0.0% | 0.0% | 25.0% | -2.4 | 0.00 | 0.00 | +9.1 | +4.5 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 31.8% | 14.3% | 14.3% | 14.3% | -0.0 | 0.99 | 4.97 | +9.4 | +6.5 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 31.8% | 31.8% | 9.1% | +0.0 | 1.01 | 1.73 | +10.6 | +7.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 22 | S_STRANGER | 100.0% | 31.8% | 31.8% | 9.1% | +0.0 | 1.01 | 1.73 | +10.6 | +7.3 |
| `confluence_gte_70` | 22 | S_STRANGER | 100.0% | 31.8% | 31.8% | 9.1% | +0.0 | 1.01 | 1.73 | +10.6 | +7.3 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 18.2% | 25.0% | 25.0% | 0.0% | -0.6 | 0.76 | 1.51 | +7.4 | +6.7 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 63.6% | 21.4% | 21.4% | 7.1% | -0.7 | 0.80 | 2.40 | +9.5 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 21 | S_STRANGER | 95.5% | 28.6% | 28.6% | 9.5% | -0.3 | 0.91 | 1.82 | +10.3 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 21 | S_STRANGER | 95.5% | 28.6% | 28.6% | 9.5% | -0.3 | 0.91 | 1.82 | +10.3 | +7.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 4.5% | 100.0% | 100.0% | 0.0% | +7.4 | 999.00 | 999.00 | +18.5 | +0.7 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+3.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 25.0% | +4.5 | 2.08 | 4.17 | +16.1 | +9.1 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 18.8% | 33.3% | 33.3% | 33.3% | +2.3 | 1.40 | 2.79 | +13.8 | +9.6 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 37.5% | 16.7% | 16.7% | 16.7% | -2.0 | 0.66 | 3.32 | +10.6 | +10.2 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 25.0% | +4.5 | 2.08 | 4.17 | +16.1 | +9.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 62.5% | 30.0% | 30.0% | 30.0% | +5.6 | 2.51 | 5.03 | +17.9 | +8.2 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 43.8% | 14.3% | 14.3% | 28.6% | -2.1 | 0.61 | 3.07 | +13.2 | +12.2 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 50.0% | 25.0% | 25.0% | 25.0% | +1.0 | 1.20 | 3.01 | +14.4 | +11.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 81.2% | 23.1% | 23.1% | 23.1% | +3.0 | 1.72 | 5.15 | +14.5 | +9.0 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 93.8% | 26.7% | 26.7% | 26.7% | +3.3 | 1.75 | 4.37 | +15.6 | +9.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 25.0% | 25.0% | 25.0% | 0.0% | +2.6 | 1.87 | 5.60 | +13.1 | +7.5 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 31.2% | 40.0% | 40.0% | 20.0% | +3.4 | 1.59 | 2.38 | +14.4 | +12.7 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+2.3; validation N=9 Fav=33.3% Avg=-0.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 12.5% | +0.4 | 1.12 | 2.47 | +10.1 | +8.7 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 93.8% | 26.7% | 26.7% | 13.3% | -0.7 | 0.78 | 2.16 | +9.4 | +9.1 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 12.5% | +0.4 | 1.12 | 2.47 | +10.1 | +8.7 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 12.5% | +0.4 | 1.12 | 2.47 | +10.1 | +8.7 |
| `asian_range_gte_30` | 12 | S_STRANGER | 75.0% | 33.3% | 33.3% | 16.7% | +0.2 | 1.05 | 2.10 | +9.9 | +9.5 |
| `confluence_gte_60` | 4 | R_REPEATER | 25.0% | 50.0% | 50.0% | 25.0% | +3.9 | 6.06 | 6.06 | +8.9 | +5.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 50.0% | 12.5% | 12.5% | 12.5% | -1.7 | 0.35 | 2.47 | +9.0 | +11.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 56.2% | 22.2% | 22.2% | 11.1% | -0.9 | 0.71 | 2.47 | +9.6 | +11.4 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 68.8% | 27.3% | 27.3% | 18.2% | -1.3 | 0.64 | 1.71 | +8.9 | +10.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 20.0% | -1.0 | 0.60 | 2.41 | +9.9 | +14.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 12.5% | +0.4 | 1.12 | 2.47 | +10.1 | +8.7 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 31.2% | 31.2% | 12.5% | +0.4 | 1.12 | 2.47 | +10.1 | +8.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-12.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=75.0% Avg=+6.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 12.5% | -3.3 | 0.51 | 0.85 | +10.1 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 56.2% | 22.2% | 33.3% | 0.0% | -6.6 | 0.30 | 0.60 | +8.7 | +6.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 68.8% | 18.2% | 27.3% | 0.0% | -6.3 | 0.27 | 0.72 | +8.6 | +5.6 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 12.5% | -3.3 | 0.51 | 0.85 | +10.1 | +4.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 75.0% | 33.3% | 41.7% | 8.3% | -1.7 | 0.67 | 0.93 | +10.2 | +4.3 |
| `confluence_gte_70` | 2 | R_REPEATER | 12.5% | 50.0% | 50.0% | 0.0% | -0.0 | 0.80 | 0.80 | +11.5 | +2.4 |
| `tdi_rsi_gt_signal` | 6 | R_REPEATER | 37.5% | 50.0% | 50.0% | 0.0% | +0.4 | 1.11 | 1.11 | +14.7 | +6.3 |
| `tdi_rsi_gte_50` | 6 | R_REPEATER | 37.5% | 50.0% | 50.0% | 0.0% | +0.4 | 1.11 | 1.11 | +14.7 | +6.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 12.5% | -3.3 | 0.51 | 0.85 | +10.1 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 31.2% | 37.5% | 12.5% | -3.3 | 0.51 | 0.85 | +10.1 | +4.8 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 25.0% | 0.0% | 25.0% | 0.0% | -13.5 | 0.05 | 0.15 | +4.3 | +3.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -12.0 | 0.00 | 0.00 | +10.6 | +13.3 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=0.0% Avg=-3.1; validation N=6 Fav=50.0% Avg=+16.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | +9.2 | 4.70 | 9.41 | +16.7 | +6.0 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | +9.2 | 4.70 | 9.41 | +16.7 | +6.0 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | +9.2 | 4.70 | 9.41 | +16.7 | +6.0 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | +9.2 | 4.70 | 9.41 | +16.7 | +6.0 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | +9.2 | 4.70 | 9.41 | +16.7 | +6.0 |
| `confluence_gte_60` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 20.0% | +2.8 | 1.60 | 6.41 | +14.2 | +7.7 |
| `confluence_gte_70` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 100.0% | +37.0 | 999.00 | 999.00 | +40.0 | +3.1 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 27.3% | 27.3% | 18.2% | +7.5 | 3.60 | 8.40 | +15.8 | +6.6 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 69.2% | 33.3% | 33.3% | 22.2% | +9.6 | 4.10 | 8.21 | +18.9 | +7.2 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | +9.2 | 4.70 | 9.41 | +16.7 | +6.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 84.6% | 27.3% | 27.3% | 18.2% | +7.5 | 3.60 | 8.40 | +15.8 | +6.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | +9.2 | 4.70 | 9.41 | +16.7 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 23.1% | +9.2 | 4.70 | 9.41 | +16.7 | +6.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+6.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=100.0% Avg=+8.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 30.8% | 34.6% | 23.1% | +1.8 | 1.36 | 2.58 | +14.5 | +7.6 |
| `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 96.2% | 32.0% | 36.0% | 24.0% | +2.0 | 1.40 | 2.49 | +14.3 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 100.0% | 30.8% | 34.6% | 23.1% | +1.8 | 1.36 | 2.58 | +14.5 | +7.6 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 30.8% | 34.6% | 23.1% | +1.8 | 1.36 | 2.58 | +14.5 | +7.6 |
| `asian_range_gte_30` | 21 | S_STRANGER | 80.8% | 23.8% | 28.6% | 23.8% | +0.5 | 1.09 | 2.73 | +13.4 | +8.2 |
| `confluence_gte_60` | 23 | S_STRANGER | 88.5% | 30.4% | 34.8% | 21.7% | +0.2 | 1.05 | 1.96 | +11.8 | +8.3 |
| `confluence_gte_70` | 5 | R_REPEATER | 19.2% | 60.0% | 60.0% | 40.0% | +7.1 | 2.57 | 1.71 | +18.6 | +6.5 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 80.8% | 28.6% | 33.3% | 19.0% | +1.6 | 1.31 | 2.62 | +14.6 | +8.4 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 61.5% | 25.0% | 25.0% | 18.8% | -0.9 | 0.83 | 2.50 | +13.9 | +9.8 |
| `ratio_le_2_and_asian_gte_30` | 20 | S_STRANGER | 76.9% | 25.0% | 30.0% | 25.0% | +0.7 | 1.12 | 2.62 | +13.2 | +7.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 16 | S_STRANGER | 61.5% | 18.8% | 25.0% | 18.8% | -0.2 | 0.96 | 2.88 | +13.0 | +8.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 30.8% | 34.6% | 23.1% | +1.8 | 1.36 | 2.58 | +14.5 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 25 | S_STRANGER | 96.2% | 32.0% | 36.0% | 24.0% | +2.0 | 1.42 | 2.53 | +14.5 | +7.6 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 3.8% | 100.0% | 100.0% | 100.0% | +19.9 | 999.00 | 999.00 | +30.0 | +0.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 11.5% | 33.3% | 33.3% | 33.3% | +2.0 | 1.44 | 2.88 | +18.8 | +5.8 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=20.0% Avg=-0.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=37.5% Avg=+1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | +0.9 | 1.29 | 2.89 | +13.9 | +10.2 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 92.3% | 25.0% | 25.0% | 8.3% | +0.1 | 1.04 | 3.12 | +14.2 | +10.9 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 92.3% | 25.0% | 25.0% | 8.3% | +0.1 | 1.04 | 3.12 | +14.2 | +10.9 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | +0.9 | 1.29 | 2.89 | +13.9 | +10.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | +0.9 | 1.29 | 2.89 | +13.9 | +10.2 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | +0.9 | 1.29 | 2.89 | +13.9 | +10.2 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 18.2% | 18.2% | 9.1% | -0.5 | 0.88 | 3.95 | +14.2 | +11.5 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -6.5 | 0.00 | 0.00 | +6.3 | +14.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | +0.9 | 1.29 | 2.89 | +13.9 | +10.2 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | +0.9 | 1.29 | 2.89 | +13.9 | +10.2 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -6.3 | 0.00 | 0.00 | +9.0 | +16.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -6.3 | 0.00 | 0.00 | +9.0 | +16.0 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+3.3; validation N=2 Fav=50.0% Avg=-7.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 15.4% | -0.5 | 0.84 | 1.47 | +6.5 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 8 | R_REPEATER | 61.5% | 50.0% | 50.0% | 12.5% | +0.7 | 1.18 | 1.18 | +7.2 | +6.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 15.4% | -0.5 | 0.84 | 1.47 | +6.5 | +5.9 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 15.4% | -0.5 | 0.84 | 1.47 | +6.5 | +5.9 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 53.8% | 28.6% | 28.6% | 14.3% | +2.3 | 2.50 | 5.00 | +7.7 | +3.8 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 61.5% | 25.0% | 25.0% | 0.0% | -2.7 | 0.22 | 0.56 | +4.7 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | R_REPEATER | 61.5% | 50.0% | 50.0% | 12.5% | +0.7 | 1.18 | 1.18 | +7.2 | +6.8 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 15.4% | -0.5 | 0.84 | 1.47 | +6.5 | +5.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=3 Fav=66.7% Avg=+5.0; out_of_sample N=6 Fav=16.7% Avg=-4.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -1.9 | 0.49 | 1.10 | +5.3 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 76.9% | 20.0% | 20.0% | 0.0% | -3.6 | 0.17 | 0.67 | +4.0 | +8.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 92.3% | 25.0% | 25.0% | 8.3% | -2.6 | 0.36 | 1.07 | +5.0 | +7.7 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -1.9 | 0.49 | 1.10 | +5.3 | +7.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -1.9 | 0.49 | 1.10 | +5.3 | +7.3 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -1.9 | 0.49 | 1.10 | +5.3 | +7.3 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 0.0% | -2.9 | 0.05 | 0.05 | +5.3 | +6.7 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 69.2% | 33.3% | 33.3% | 11.1% | -1.3 | 0.58 | 1.17 | +5.6 | +6.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -1.9 | 0.49 | 1.10 | +5.3 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 30.8% | 30.8% | 7.7% | -1.9 | 0.49 | 1.10 | +5.3 | +7.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=100.0% Avg=+10.5; validation N=4 Fav=50.0% Avg=+12.3; out_of_sample N=1 Fav=100.0% Avg=+26.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 30.4% | 30.4% | 21.7% | +2.7 | 1.72 | 3.45 | +12.7 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 91.3% | 28.6% | 28.6% | 19.0% | +1.2 | 1.30 | 2.82 | +11.4 | +7.6 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 30.4% | 30.4% | 21.7% | +2.7 | 1.72 | 3.45 | +12.7 | +7.7 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 30.4% | 30.4% | 21.7% | +2.7 | 1.72 | 3.45 | +12.7 | +7.7 |
| `asian_range_gte_30` | 12 | S_STRANGER | 52.2% | 33.3% | 33.3% | 16.7% | -0.0 | 0.99 | 1.98 | +10.5 | +8.7 |
| `confluence_gte_60` | 19 | S_STRANGER | 82.6% | 31.6% | 31.6% | 21.1% | +2.9 | 1.71 | 3.13 | +13.4 | +8.4 |
| `confluence_gte_70` | 6 | R_REPEATER | 26.1% | 66.7% | 66.7% | 33.3% | +14.3 | 11.73 | 5.86 | +21.0 | +6.6 |
| `tdi_rsi_gt_signal` | 2 | R_REPEATER | 8.7% | 50.0% | 50.0% | 50.0% | +11.8 | 3.88 | 3.88 | +28.9 | +8.4 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 78.3% | 27.8% | 27.8% | 16.7% | +3.2 | 1.84 | 4.41 | +12.6 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 52.2% | 33.3% | 33.3% | 16.7% | -0.0 | 0.99 | 1.98 | +10.5 | +8.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -8.2 | 0.00 | 0.00 | +25.5 | +9.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 30.4% | 30.4% | 21.7% | +2.7 | 1.72 | 3.45 | +12.7 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 30.4% | 30.4% | 21.7% | +2.7 | 1.72 | 3.45 | +12.7 | +7.7 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 13.0% | 33.3% | 33.3% | 33.3% | +2.9 | 2.42 | 4.84 | +11.1 | +5.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 8.7% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +3.3 | +6.6 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=30.0% Avg=+5.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=12 Fav=33.3% Avg=+0.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 30.4% | 30.4% | 21.7% | +2.0 | 1.47 | 2.94 | +14.3 | +7.6 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 100.0% | 30.4% | 30.4% | 21.7% | +2.0 | 1.47 | 2.94 | +14.3 | +7.6 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 30.4% | 30.4% | 21.7% | +2.0 | 1.47 | 2.94 | +14.3 | +7.6 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 30.4% | 30.4% | 21.7% | +2.0 | 1.47 | 2.94 | +14.3 | +7.6 |
| `asian_range_gte_30` | 21 | S_STRANGER | 91.3% | 28.6% | 28.6% | 23.8% | +1.9 | 1.47 | 3.19 | +14.0 | +7.6 |
| `confluence_gte_60` | 22 | S_STRANGER | 95.7% | 31.8% | 31.8% | 22.7% | +2.5 | 1.64 | 3.04 | +14.9 | +7.5 |
| `confluence_gte_70` | 13 | S_STRANGER | 56.5% | 30.8% | 30.8% | 23.1% | +3.8 | 2.13 | 4.27 | +14.0 | +7.9 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 13.0% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +2.0 | +4.2 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 56.5% | 30.8% | 30.8% | 7.7% | +1.9 | 1.61 | 3.22 | +12.5 | +7.7 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 91.3% | 28.6% | 28.6% | 23.8% | +1.9 | 1.47 | 3.19 | +14.0 | +7.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 13.0% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +2.0 | +4.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 30.4% | 30.4% | 21.7% | +2.0 | 1.47 | 2.94 | +14.3 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 95.7% | 31.8% | 31.8% | 22.7% | +2.2 | 1.51 | 2.80 | +14.1 | +7.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +18.2 | +2.7 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=29 Fav=27.6% Avg=-0.8; validation N=17 Fav=35.3% Avg=+4.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 46 | S_STRANGER | 100.0% | 30.4% | 32.6% | 8.7% | +1.2 | 1.34 | 2.67 | +10.6 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 43.5% | 25.0% | 25.0% | 10.0% | -0.1 | 0.98 | 2.75 | +9.0 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 56.5% | 23.1% | 23.1% | 7.7% | -1.0 | 0.74 | 2.35 | +8.6 | +7.2 |
| `stop_hunt_le_90` | 46 | S_STRANGER | 100.0% | 30.4% | 32.6% | 8.7% | +1.2 | 1.34 | 2.67 | +10.6 | +6.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 27 | S_STRANGER | 58.7% | 25.9% | 25.9% | 7.4% | +1.7 | 1.48 | 4.02 | +11.4 | +7.5 |
| `confluence_gte_70` | 6 | S_STRANGER | 13.0% | 16.7% | 16.7% | 0.0% | -2.7 | 0.44 | 2.21 | +6.7 | +11.1 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 21.7% | 10.0% | 10.0% | 20.0% | +2.4 | 1.68 | 13.42 | +12.0 | +6.5 |
| `tdi_rsi_gte_50` | 25 | S_STRANGER | 54.3% | 24.0% | 24.0% | 4.0% | -0.8 | 0.81 | 2.43 | +9.6 | +8.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 46 | S_STRANGER | 100.0% | 30.4% | 32.6% | 8.7% | +1.2 | 1.34 | 2.67 | +10.6 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 46 | S_STRANGER | 100.0% | 30.4% | 32.6% | 8.7% | +1.2 | 1.34 | 2.67 | +10.6 | +6.6 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 6.5% | 33.3% | 33.3% | 0.0% | +0.3 | 1.10 | 2.19 | +5.5 | +5.6 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 4.3% | 50.0% | 50.0% | 0.0% | +0.8 | 1.21 | 1.21 | +6.9 | +7.2 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=2 Fav=0.0% Avg=-3.0; out_of_sample N=5 Fav=60.0% Avg=+2.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 46 | S_STRANGER | 100.0% | 30.4% | 30.4% | 6.5% | -1.4 | 0.67 | 1.53 | +7.9 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 42 | S_STRANGER | 91.3% | 26.2% | 26.2% | 7.1% | -2.0 | 0.56 | 1.59 | +7.7 | +7.9 |
| `hunt_to_ar_ratio_le_2_5` | 45 | S_STRANGER | 97.8% | 28.9% | 28.9% | 6.7% | -1.5 | 0.65 | 1.59 | +7.9 | +7.5 |
| `stop_hunt_le_90` | 46 | S_STRANGER | 100.0% | 30.4% | 30.4% | 6.5% | -1.4 | 0.67 | 1.53 | +7.9 | +7.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 37 | S_STRANGER | 80.4% | 27.0% | 27.0% | 5.4% | -1.2 | 0.68 | 1.84 | +7.6 | +7.0 |
| `confluence_gte_70` | 7 | S_STRANGER | 15.2% | 42.9% | 42.9% | 0.0% | +0.5 | 1.56 | 2.08 | +7.5 | +5.4 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 43.5% | 20.0% | 20.0% | 0.0% | -2.7 | 0.38 | 1.52 | +5.8 | +7.2 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 39.1% | 27.8% | 27.8% | 0.0% | -2.9 | 0.41 | 1.08 | +6.9 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 46 | S_STRANGER | 100.0% | 30.4% | 30.4% | 6.5% | -1.4 | 0.67 | 1.53 | +7.9 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 46 | S_STRANGER | 100.0% | 30.4% | 30.4% | 6.5% | -1.4 | 0.67 | 1.53 | +7.9 | +7.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+8.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=37 Fav=27.0% Avg=+1.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 43 | S_STRANGER | 100.0% | 30.2% | 30.2% | 27.9% | +2.0 | 1.85 | 3.56 | +9.7 | +5.3 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 34.9% | 26.7% | 26.7% | 26.7% | +2.8 | 2.20 | 4.95 | +10.5 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 41.9% | 27.8% | 27.8% | 27.8% | +2.4 | 1.98 | 3.96 | +10.9 | +5.0 |
| `stop_hunt_le_90` | 43 | S_STRANGER | 100.0% | 30.2% | 30.2% | 27.9% | +2.0 | 1.85 | 3.56 | +9.7 | +5.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 43 | S_STRANGER | 100.0% | 30.2% | 30.2% | 27.9% | +2.0 | 1.85 | 3.56 | +9.7 | +5.3 |
| `confluence_gte_70` | 43 | S_STRANGER | 100.0% | 30.2% | 30.2% | 27.9% | +2.0 | 1.85 | 3.56 | +9.7 | +5.3 |
| `tdi_rsi_gt_signal` | 20 | S_STRANGER | 46.5% | 30.0% | 30.0% | 15.0% | +1.7 | 1.74 | 3.48 | +10.4 | +4.2 |
| `tdi_rsi_gte_50` | 25 | S_STRANGER | 58.1% | 24.0% | 24.0% | 16.0% | +0.9 | 1.38 | 3.92 | +9.2 | +5.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 41 | S_STRANGER | 95.3% | 29.3% | 29.3% | 26.8% | +1.6 | 1.63 | 3.26 | +9.3 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 43 | S_STRANGER | 100.0% | 30.2% | 30.2% | 27.9% | +2.0 | 1.85 | 3.56 | +9.7 | +5.3 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 4.7% | 50.0% | 50.0% | 50.0% | +8.3 | 3.44 | 3.44 | +23.5 | +7.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 7.0% | 33.3% | 33.3% | 33.3% | +5.4 | 3.21 | 6.41 | +17.3 | +5.6 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=50.0% Avg=+12.3; validation N=1 Fav=0.0% Avg=-3.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +5.2 | 2.24 | 4.48 | +16.8 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 90.0% | 33.3% | 33.3% | 33.3% | +5.8 | 2.24 | 4.48 | +17.3 | +6.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +5.2 | 2.24 | 4.48 | +16.8 | +5.5 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +5.2 | 2.24 | 4.48 | +16.8 | +5.5 |
| `asian_range_gte_30` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 37.5% | +4.3 | 1.95 | 4.88 | +16.5 | +4.7 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +5.2 | 2.24 | 4.48 | +16.8 | +5.5 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +5.2 | 2.24 | 4.48 | +16.8 | +5.5 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +5.2 | 2.24 | 4.48 | +16.8 | +5.5 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 42.9% | 42.9% | 42.9% | +10.1 | 4.04 | 5.39 | +21.4 | +6.3 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 28.6% | +4.9 | 1.95 | 4.88 | +17.1 | +5.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 28.6% | +4.9 | 1.95 | 4.88 | +17.1 | +5.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +5.2 | 2.24 | 4.48 | +16.8 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 40.0% | +5.2 | 2.24 | 4.48 | +16.8 | +5.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=33.3% Avg=+9.9; validation N=7 Fav=28.6% Avg=+2.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +4.8 | 5.00 | 10.00 | +12.5 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +4.8 | 5.00 | 10.00 | +12.5 | +5.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +4.8 | 5.00 | 10.00 | +12.5 | +5.0 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +4.8 | 5.00 | 10.00 | +12.5 | +5.0 |
| `asian_range_gte_30` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 40.0% | +0.8 | 2.23 | 6.68 | +8.8 | +4.1 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +4.8 | 5.00 | 10.00 | +12.5 | +5.0 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +4.8 | 5.00 | 10.00 | +12.5 | +5.0 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 40.0% | +5.3 | 6.72 | 20.15 | +15.4 | +4.4 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 42.9% | +4.0 | 3.78 | 7.56 | +13.0 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 40.0% | +0.8 | 2.23 | 6.68 | +8.8 | +4.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 50.0% | -0.8 | 0.00 | 0.00 | +14.6 | +2.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +4.8 | 5.00 | 10.00 | +12.5 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 30.0% | +4.8 | 5.00 | 10.00 | +12.5 | +5.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=33.3% Avg=+2.4; validation N=2 Fav=50.0% Avg=+9.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +2.6 | 2.12 | 4.96 | +12.6 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +2.6 | 2.12 | 4.96 | +12.6 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +2.6 | 2.12 | 4.96 | +12.6 | +5.6 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +2.6 | 2.12 | 4.96 | +12.6 | +5.6 |
| `asian_range_gte_30` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 16.7% | +2.3 | 2.13 | 10.64 | +11.1 | +5.5 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +2.6 | 2.12 | 4.96 | +12.6 | +5.6 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +2.6 | 2.12 | 4.96 | +12.6 | +5.6 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 37.5% | 37.5% | 25.0% | +4.1 | 3.05 | 5.09 | +15.7 | +4.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -2.6 | 0.03 | 0.16 | +8.6 | +5.1 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 16.7% | +2.3 | 2.13 | 10.64 | +11.1 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | +2.9 | 2.24 | 8.96 | +13.3 | +3.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +2.6 | 2.12 | 4.96 | +12.6 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 20.0% | +2.6 | 2.12 | 4.96 | +12.6 | +5.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=37.5% Avg=+1.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 5.0% | +0.8 | 1.27 | 2.96 | +9.1 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 40.0% | 37.5% | 37.5% | 12.5% | +1.3 | 1.65 | 2.76 | +10.3 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 60.0% | 25.0% | 25.0% | 8.3% | -0.9 | 0.71 | 2.13 | +8.8 | +8.1 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 5.0% | +0.8 | 1.27 | 2.96 | +9.1 | +7.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 5.0% | +0.8 | 1.27 | 2.96 | +9.1 | +7.2 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 5.0% | +0.8 | 1.27 | 2.96 | +9.1 | +7.2 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 25.0% | 40.0% | 40.0% | 0.0% | -1.1 | 0.63 | 0.95 | +8.1 | +5.4 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 70.0% | 21.4% | 21.4% | 0.0% | -1.0 | 0.72 | 2.65 | +7.1 | +8.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 5.0% | +0.8 | 1.27 | 2.96 | +9.1 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 30.0% | 30.0% | 5.0% | +0.8 | 1.27 | 2.96 | +9.1 | +7.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+2.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | -2.5 | 0.64 | 1.50 | +19.2 | +12.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | -2.5 | 0.64 | 1.50 | +19.2 | +12.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | -2.5 | 0.64 | 1.50 | +19.2 | +12.6 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | -2.5 | 0.64 | 1.50 | +19.2 | +12.6 |
| `asian_range_gte_30` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 14.3% | -8.3 | 0.10 | 0.59 | +19.0 | +15.3 |
| `confluence_gte_60` | 9 | S_STRANGER | 90.0% | 33.3% | 33.3% | 11.1% | -2.1 | 0.70 | 1.41 | +20.4 | +12.6 |
| `confluence_gte_70` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -37.1 | 0.00 | 0.00 | +4.1 | +59.0 |
| `tdi_rsi_gt_signal` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 90.0% | 33.3% | 33.3% | 11.1% | -2.3 | 0.69 | 1.38 | +20.3 | +12.9 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 14.3% | -8.3 | 0.10 | 0.59 | +19.0 | +15.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.2 | 0.00 | 0.00 | +34.0 | +8.3 |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 30.0% | 30.0% | 10.0% | -2.5 | 0.64 | 1.50 | +19.2 | +12.6 |
| `feature_stale_hod_exhaustion_reject` | 9 | S_STRANGER | 90.0% | 22.2% | 22.2% | 11.1% | -5.0 | 0.36 | 1.28 | +18.5 | +13.8 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -2.9 | 0.35 | 1.04 | +11.8 | +8.1 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 50.0% | 40.0% | 40.0% | 20.0% | +2.5 | 1.94 | 2.91 | +19.4 | +6.6 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=71.4% Avg=+6.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-11.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 29.0% | 32.3% | 22.6% | +2.4 | 1.82 | 2.74 | +15.2 | +8.3 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 96.8% | 26.7% | 30.0% | 20.0% | +1.3 | 1.41 | 2.36 | +14.1 | +7.9 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 100.0% | 29.0% | 32.3% | 22.6% | +2.4 | 1.82 | 2.74 | +15.2 | +8.3 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 29.0% | 32.3% | 22.6% | +2.4 | 1.82 | 2.74 | +15.2 | +8.3 |
| `asian_range_gte_30` | 26 | S_STRANGER | 83.9% | 34.6% | 38.5% | 15.4% | +3.1 | 1.90 | 2.47 | +15.3 | +8.5 |
| `confluence_gte_60` | 23 | S_STRANGER | 74.2% | 34.8% | 39.1% | 13.0% | +2.2 | 1.73 | 2.12 | +15.1 | +8.7 |
| `confluence_gte_70` | 11 | S_STRANGER | 35.5% | 27.3% | 27.3% | 18.2% | +1.2 | 1.28 | 2.56 | +17.3 | +12.0 |
| `tdi_rsi_gt_signal` | 8 | R_REPEATER | 25.8% | 62.5% | 62.5% | 0.0% | +3.9 | 2.85 | 1.14 | +18.3 | +5.3 |
| `tdi_rsi_gte_50` | 22 | S_STRANGER | 71.0% | 31.8% | 36.4% | 18.2% | +2.6 | 1.90 | 2.61 | +15.7 | +8.5 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 80.6% | 32.0% | 36.0% | 12.0% | +1.7 | 1.47 | 2.13 | +14.1 | +8.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 8 | R_REPEATER | 25.8% | 62.5% | 62.5% | 0.0% | +3.9 | 2.85 | 1.14 | +18.3 | +5.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 29.0% | 32.3% | 22.6% | +2.4 | 1.82 | 2.74 | +15.2 | +8.3 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 96.8% | 26.7% | 30.0% | 23.3% | +1.9 | 1.62 | 2.70 | +14.4 | +8.5 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 19.4% | 33.3% | 33.3% | 33.3% | +6.9 | 4.94 | 7.41 | +21.0 | +5.5 |
| `feature_eurjpy_tdi50_reclaim` | 7 | S_STRANGER | 22.6% | 28.6% | 28.6% | 14.3% | +0.7 | 1.25 | 2.50 | +14.3 | +7.4 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+15.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +0.4 | 1.10 | 2.65 | +9.6 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 37.1% | 38.5% | 38.5% | 23.1% | +2.3 | 1.33 | 2.13 | +14.9 | +7.7 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 48.6% | 41.2% | 41.2% | 17.6% | +2.9 | 1.54 | 2.21 | +15.0 | +7.5 |
| `stop_hunt_le_90` | 35 | S_STRANGER | 100.0% | 28.6% | 28.6% | 14.3% | +0.4 | 1.10 | 2.65 | +9.6 | +7.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 31 | S_STRANGER | 88.6% | 32.3% | 32.3% | 16.1% | +2.8 | 2.18 | 4.36 | +10.1 | +7.0 |
| `confluence_gte_70` | 7 | S_STRANGER | 20.0% | 28.6% | 28.6% | 0.0% | +2.7 | 2.50 | 6.25 | +7.9 | +4.2 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 22.9% | 25.0% | 25.0% | 0.0% | +2.8 | 2.03 | 6.10 | +10.4 | +8.4 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 65.7% | 30.4% | 30.4% | 13.0% | +2.4 | 1.66 | 3.80 | +11.8 | +8.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 91.4% | 28.1% | 28.1% | 15.6% | +0.0 | 1.01 | 2.46 | +8.8 | +7.7 |
| `feature_stale_hod_exhaustion_reject` | 33 | S_STRANGER | 94.3% | 27.3% | 27.3% | 15.2% | -0.0 | 0.99 | 2.53 | +8.7 | +7.5 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 20.0% | 28.6% | 28.6% | 42.9% | +2.2 | 1.34 | 2.67 | +12.9 | +7.3 |
| `feature_eurjpy_tdi50_reclaim` | 5 | R_REPEATER | 14.3% | 60.0% | 60.0% | 40.0% | +15.1 | 16.40 | 10.93 | +25.2 | +7.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=30.8% Avg=+2.1; validation N=12 Fav=33.3% Avg=+1.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 42 | S_STRANGER | 100.0% | 28.6% | 28.6% | 16.7% | +0.2 | 1.04 | 2.34 | +11.8 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 42 | S_STRANGER | 100.0% | 28.6% | 28.6% | 16.7% | +0.2 | 1.04 | 2.34 | +11.8 | +8.2 |
| `hunt_to_ar_ratio_le_2_5` | 42 | S_STRANGER | 100.0% | 28.6% | 28.6% | 16.7% | +0.2 | 1.04 | 2.34 | +11.8 | +8.2 |
| `stop_hunt_le_90` | 42 | S_STRANGER | 100.0% | 28.6% | 28.6% | 16.7% | +0.2 | 1.04 | 2.34 | +11.8 | +8.2 |
| `asian_range_gte_30` | 38 | S_STRANGER | 90.5% | 26.3% | 26.3% | 13.2% | -1.0 | 0.78 | 2.02 | +10.9 | +8.1 |
| `confluence_gte_60` | 22 | S_STRANGER | 52.4% | 27.3% | 27.3% | 4.5% | +0.8 | 1.21 | 3.03 | +12.6 | +7.7 |
| `confluence_gte_70` | 2 | R_REPEATER | 4.8% | 50.0% | 50.0% | 0.0% | +9.4 | 6.22 | 6.22 | +15.2 | +2.9 |
| `tdi_rsi_gt_signal` | 18 | S_STRANGER | 42.9% | 27.8% | 27.8% | 5.6% | +0.4 | 1.11 | 2.88 | +11.5 | +7.2 |
| `tdi_rsi_gte_50` | 25 | S_STRANGER | 59.5% | 32.0% | 32.0% | 12.0% | +1.8 | 1.50 | 2.81 | +14.8 | +9.0 |
| `ratio_le_2_and_asian_gte_30` | 38 | S_STRANGER | 90.5% | 26.3% | 26.3% | 13.2% | -1.0 | 0.78 | 2.02 | +10.9 | +8.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 40.5% | 23.5% | 23.5% | 5.9% | -0.9 | 0.79 | 2.56 | +10.5 | +7.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 42 | S_STRANGER | 100.0% | 28.6% | 28.6% | 16.7% | +0.2 | 1.04 | 2.34 | +11.8 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 42 | S_STRANGER | 100.0% | 28.6% | 28.6% | 16.7% | +0.2 | 1.04 | 2.34 | +11.8 | +8.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 2.4% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +1.3 | +5.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.4% | 0.0% | 0.0% | 0.0% | -3.5 | 0.00 | 0.00 | +1.3 | +5.3 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=22.2% Avg=-1.1; validation N=17 Fav=35.3% Avg=+1.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -0.3 | 0.90 | 2.15 | +8.0 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 17.9% | 20.0% | 20.0% | 20.0% | -6.9 | 0.21 | 0.84 | +7.6 | +9.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 50.0% | 21.4% | 21.4% | 14.3% | -1.0 | 0.81 | 2.95 | +10.1 | +6.1 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -0.3 | 0.90 | 2.15 | +8.0 | +5.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 28 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -0.3 | 0.90 | 2.15 | +8.0 | +5.0 |
| `confluence_gte_70` | 28 | S_STRANGER | 100.0% | 28.6% | 28.6% | 7.1% | -0.3 | 0.90 | 2.15 | +8.0 | +5.0 |
| `tdi_rsi_gt_signal` | 26 | S_STRANGER | 92.9% | 30.8% | 30.8% | 7.7% | +0.6 | 1.22 | 2.59 | +8.1 | +4.2 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 67.9% | 21.1% | 21.1% | 5.3% | -0.8 | 0.78 | 2.73 | +7.2 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 92.9% | 30.8% | 30.8% | 7.7% | -0.3 | 0.92 | 1.96 | +8.4 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 96.4% | 29.6% | 29.6% | 7.4% | -0.3 | 0.92 | 2.06 | +8.2 | +5.1 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -0.8 | 0.00 | 0.00 | +2.7 | +1.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -0.8 | 0.00 | 0.00 | +2.7 | +1.3 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+0.9; validation N=13 Fav=23.1% Avg=-1.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -0.5 | 0.84 | 2.19 | +7.4 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 22.2% | 25.0% | 25.0% | 25.0% | +1.8 | 1.54 | 4.62 | +9.7 | +13.9 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 50.0% | 22.2% | 22.2% | 11.1% | -1.6 | 0.64 | 2.25 | +8.5 | +10.9 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -0.5 | 0.84 | 2.19 | +7.4 | +8.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -0.5 | 0.84 | 2.19 | +7.4 | +8.2 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -0.5 | 0.84 | 2.19 | +7.4 | +8.2 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 50.0% | 11.1% | 11.1% | 0.0% | -1.9 | 0.27 | 2.12 | +4.8 | +7.0 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 72.2% | 15.4% | 15.4% | 0.0% | -3.3 | 0.16 | 0.85 | +5.8 | +9.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -0.5 | 0.84 | 2.19 | +7.4 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -0.5 | 0.84 | 2.19 | +7.4 | +8.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=15 Fav=33.3% Avg=-3.6; out_of_sample N=3 Fav=0.0% Avg=-2.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -3.3 | 0.32 | 0.83 | +6.0 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 22.2% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +3.9 | +9.0 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -3.3 | 0.32 | 0.83 | +6.0 | +8.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -3.3 | 0.32 | 0.83 | +6.0 | +8.2 |
| `confluence_gte_70` | 11 | S_STRANGER | 61.1% | 27.3% | 27.3% | 0.0% | -5.3 | 0.14 | 0.36 | +6.4 | +9.7 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 38.9% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +3.1 | +8.5 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 22.2% | 25.0% | 25.0% | 0.0% | -0.6 | 0.62 | 1.85 | +5.5 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -3.3 | 0.32 | 0.83 | +6.0 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 27.8% | 27.8% | 11.1% | -3.3 | 0.32 | 0.83 | +6.0 | +8.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=60.0% Avg=+4.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 58 | S_STRANGER | 100.0% | 27.6% | 27.6% | 17.2% | +0.4 | 1.10 | 2.54 | +8.6 | +4.2 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 19.0% | 18.2% | 18.2% | 18.2% | -3.3 | 0.40 | 1.60 | +8.9 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 35 | S_STRANGER | 60.3% | 22.9% | 22.9% | 17.1% | -1.5 | 0.68 | 1.95 | +8.4 | +4.7 |
| `stop_hunt_le_90` | 58 | S_STRANGER | 100.0% | 27.6% | 27.6% | 17.2% | +0.4 | 1.10 | 2.54 | +8.6 | +4.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 31 | S_STRANGER | 53.4% | 29.0% | 29.0% | 29.0% | +2.9 | 1.99 | 4.20 | +11.0 | +4.9 |
| `confluence_gte_70` | 1 | S_STRANGER | 1.7% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +21.5 | +0.6 |
| `tdi_rsi_gt_signal` | 47 | S_STRANGER | 81.0% | 29.8% | 29.8% | 19.1% | +1.1 | 1.34 | 2.78 | +9.3 | +4.2 |
| `tdi_rsi_gte_50` | 26 | S_STRANGER | 44.8% | 38.5% | 38.5% | 11.5% | +2.0 | 1.98 | 2.78 | +9.2 | +3.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 1.7% | 0.0% | 0.0% | 0.0% | +0.0 | 0.00 | 0.00 | +6.9 | +2.5 |
| `feature_extreme_hunt_with_exception` | 56 | S_STRANGER | 96.6% | 26.8% | 26.8% | 17.9% | +0.2 | 1.07 | 2.63 | +8.6 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 58 | S_STRANGER | 100.0% | 27.6% | 27.6% | 17.2% | +0.4 | 1.10 | 2.54 | +8.6 | +4.2 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 12.1% | 42.9% | 42.9% | 0.0% | +2.9 | 7.67 | 5.11 | +7.0 | +1.7 |
| `feature_eurjpy_tdi50_reclaim` | 5 | R_REPEATER | 8.6% | 60.0% | 60.0% | 0.0% | +4.0 | 7.93 | 2.64 | +7.1 | +1.8 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=33.3% Avg=+5.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 33 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | +1.2 | 1.43 | 3.49 | +10.1 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 24.2% | 12.5% | 12.5% | 0.0% | -1.7 | 0.41 | 2.90 | +5.4 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 39.4% | 30.8% | 30.8% | 15.4% | +0.6 | 1.27 | 2.86 | +8.4 | +4.2 |
| `stop_hunt_le_90` | 33 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | +1.2 | 1.43 | 3.49 | +10.1 | +7.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 33 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | +1.2 | 1.43 | 3.49 | +10.1 | +7.0 |
| `confluence_gte_70` | 33 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | +1.2 | 1.43 | 3.49 | +10.1 | +7.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 27.3% | 22.2% | 22.2% | 11.1% | -0.3 | 0.91 | 2.72 | +8.7 | +9.3 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 69.7% | 26.1% | 26.1% | 8.7% | +1.3 | 1.46 | 3.89 | +9.5 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 78.8% | 23.1% | 23.1% | 7.7% | -0.2 | 0.93 | 2.93 | +8.6 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 87.9% | 27.6% | 27.6% | 17.2% | +1.0 | 1.34 | 3.19 | +9.7 | +6.8 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 12.1% | 50.0% | 50.0% | 75.0% | +6.9 | 5.62 | 2.81 | +17.7 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 18.2% | 33.3% | 33.3% | 33.3% | +5.6 | 4.14 | 8.28 | +13.3 | +7.0 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=44.4% Avg=+2.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=3 Fav=33.3% Avg=+4.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | +0.9 | 1.23 | 3.08 | +11.7 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | +0.9 | 1.23 | 3.08 | +11.7 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | +0.9 | 1.23 | 3.08 | +11.7 | +7.0 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | +0.9 | 1.23 | 3.08 | +11.7 | +7.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 72.7% | 18.8% | 18.8% | 18.8% | -0.4 | 0.90 | 3.60 | +8.8 | +6.4 |
| `confluence_gte_70` | 3 | S_STRANGER | 13.6% | 0.0% | 0.0% | 0.0% | -7.0 | 0.00 | 0.00 | +6.9 | +9.8 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 54.5% | 41.7% | 41.7% | 33.3% | +3.1 | 1.81 | 2.53 | +15.9 | +8.0 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 45.5% | 30.0% | 30.0% | 20.0% | -0.2 | 0.96 | 2.23 | +13.3 | +10.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | +0.9 | 1.23 | 3.08 | +11.7 | +7.0 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 27.3% | 27.3% | 27.3% | +0.9 | 1.23 | 3.08 | +11.7 | +7.0 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 9.1% | 50.0% | 50.0% | 50.0% | +8.7 | 7.18 | 7.18 | +15.9 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.5% | 0.0% | 0.0% | 0.0% | -15.6 | 0.00 | 0.00 | +6.8 | +16.5 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-1.6; validation N=8 Fav=62.5% Avg=+8.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 27.3% | 31.8% | 18.2% | +0.2 | 1.04 | 2.08 | +9.7 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | R_REPEATER | 40.9% | 55.6% | 55.6% | 33.3% | +7.1 | 4.55 | 3.64 | +15.9 | +7.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | R_REPEATER | 45.5% | 50.0% | 50.0% | 30.0% | +6.0 | 3.72 | 3.72 | +14.5 | +7.8 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 27.3% | 31.8% | 18.2% | +0.2 | 1.04 | 2.08 | +9.7 | +7.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 27.3% | 33.3% | 33.3% | 16.7% | +1.9 | 1.86 | 3.72 | +8.4 | +4.9 |
| `confluence_gte_70` | 2 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +4.5 | +7.5 |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 68.2% | 26.7% | 33.3% | 13.3% | +0.5 | 1.14 | 2.06 | +10.0 | +7.7 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 27.3% | 33.3% | 33.3% | 0.0% | +1.3 | 1.57 | 3.14 | +9.2 | +9.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 100.0% | 27.3% | 31.8% | 18.2% | +0.2 | 1.04 | 2.08 | +9.7 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 27.3% | 31.8% | 18.2% | +0.2 | 1.04 | 2.08 | +9.7 | +7.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-5.4; validation N=6 Fav=50.0% Avg=+0.7; out_of_sample N=3 Fav=0.0% Avg=-30.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -8.5 | 0.15 | 0.41 | +6.8 | +4.0 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | -17.8 | 0.06 | 0.23 | +4.6 | +6.0 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 54.5% | 16.7% | 16.7% | 16.7% | -16.7 | 0.05 | 0.26 | +5.1 | +5.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -8.5 | 0.15 | 0.41 | +6.8 | +4.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -8.5 | 0.15 | 0.41 | +6.8 | +4.0 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -8.5 | 0.15 | 0.41 | +6.8 | +4.0 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 81.8% | 11.1% | 11.1% | 11.1% | -11.6 | 0.06 | 0.48 | +5.2 | +4.7 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 0.0% | -5.2 | 0.00 | 0.00 | +2.2 | +7.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 90.9% | 30.0% | 30.0% | 20.0% | -9.4 | 0.16 | 0.36 | +7.3 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 27.3% | 27.3% | 18.2% | -8.5 | 0.15 | 0.41 | +6.8 | +4.0 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -0.2 | 0.00 | 0.00 | +1.0 | +2.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -0.2 | 0.00 | 0.00 | +1.0 | +2.5 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=20.0% Avg=+1.7; validation N=9 Fav=44.4% Avg=+4.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 26.9% | 30.8% | 15.4% | +1.9 | 2.53 | 5.37 | +8.6 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 96.2% | 28.0% | 32.0% | 16.0% | +2.1 | 2.74 | 5.48 | +8.6 | +3.7 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 100.0% | 26.9% | 30.8% | 15.4% | +1.9 | 2.53 | 5.37 | +8.6 | +3.8 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 26.9% | 30.8% | 15.4% | +1.9 | 2.53 | 5.37 | +8.6 | +3.8 |
| `asian_range_gte_30` | 22 | S_STRANGER | 84.6% | 22.7% | 22.7% | 9.1% | +1.2 | 1.90 | 6.06 | +7.4 | +4.1 |
| `confluence_gte_60` | 19 | S_STRANGER | 73.1% | 31.6% | 31.6% | 21.1% | +2.9 | 3.27 | 6.55 | +9.6 | +4.1 |
| `confluence_gte_70` | 3 | S_STRANGER | 11.5% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +7.6 | +3.8 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 53.8% | 21.4% | 21.4% | 7.1% | +0.3 | 1.26 | 4.63 | +7.2 | +3.5 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 69.2% | 27.8% | 27.8% | 11.1% | +1.9 | 2.42 | 6.29 | +8.9 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 22 | S_STRANGER | 84.6% | 22.7% | 22.7% | 9.1% | +1.2 | 1.90 | 6.06 | +7.4 | +4.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 50.0% | 23.1% | 23.1% | 7.7% | +0.6 | 1.48 | 4.93 | +7.0 | +3.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 26.9% | 30.8% | 15.4% | +1.9 | 2.53 | 5.37 | +8.6 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 26.9% | 30.8% | 15.4% | +1.9 | 2.53 | 5.37 | +8.6 | +3.8 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +5.3 | +2.8 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 11.5% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +5.1 | +3.2 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=+0.1; validation N=4 Fav=0.0% Avg=-14.0; out_of_sample N=8 Fav=62.5% Avg=+14.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 23.1% | +1.9 | 1.49 | 3.82 | +13.0 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 25 | S_STRANGER | 96.2% | 28.0% | 28.0% | 24.0% | +2.0 | 1.50 | 3.65 | +13.5 | +5.1 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 23.1% | +1.9 | 1.49 | 3.82 | +13.0 | +5.2 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 23.1% | +1.9 | 1.49 | 3.82 | +13.0 | +5.2 |
| `asian_range_gte_30` | 18 | S_STRANGER | 69.2% | 33.3% | 33.3% | 33.3% | +3.4 | 1.80 | 3.60 | +15.6 | +4.6 |
| `confluence_gte_60` | 25 | S_STRANGER | 96.2% | 24.0% | 24.0% | 20.0% | +1.4 | 1.34 | 4.03 | +12.2 | +5.4 |
| `confluence_gte_70` | 11 | S_STRANGER | 42.3% | 9.1% | 9.1% | 9.1% | -2.1 | 0.44 | 4.43 | +6.8 | +6.5 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 23.1% | 16.7% | 16.7% | 16.7% | -5.0 | 0.44 | 1.78 | +14.1 | +7.4 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 73.1% | 21.1% | 21.1% | 15.8% | +0.8 | 1.18 | 4.12 | +13.0 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 69.2% | 33.3% | 33.3% | 33.3% | +3.4 | 1.80 | 3.60 | +15.6 | +4.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 19.2% | 20.0% | 20.0% | 20.0% | -5.9 | 0.44 | 1.78 | +16.5 | +6.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 23.1% | +1.9 | 1.49 | 3.82 | +13.0 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 26.9% | 26.9% | 23.1% | +1.9 | 1.49 | 3.82 | +13.0 | +5.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 3.8% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +10.7 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.8% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +10.7 | +4.0 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=+6.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=12 Fav=33.3% Avg=+1.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 26.7% | 30.0% | 16.7% | +2.1 | 1.65 | 3.66 | +8.8 | +5.1 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 53.3% | 31.2% | 37.5% | 25.0% | +3.0 | 1.76 | 2.93 | +11.1 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 60.0% | 27.8% | 33.3% | 22.2% | +2.1 | 1.53 | 3.07 | +9.9 | +4.6 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 26.7% | 30.0% | 16.7% | +2.1 | 1.65 | 3.66 | +8.8 | +5.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 29 | S_STRANGER | 96.7% | 24.1% | 27.6% | 13.8% | +0.6 | 1.19 | 2.98 | +7.5 | +5.3 |
| `confluence_gte_70` | 20 | S_STRANGER | 66.7% | 15.0% | 20.0% | 15.0% | -1.6 | 0.62 | 2.32 | +6.3 | +5.4 |
| `tdi_rsi_gt_signal` | 27 | S_STRANGER | 90.0% | 25.9% | 29.6% | 14.8% | +1.8 | 1.50 | 3.38 | +8.1 | +5.4 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 50.0% | 20.0% | 20.0% | 6.7% | +3.1 | 1.89 | 6.95 | +10.5 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -12.9 | 0.00 | 0.00 | +3.4 | +13.2 |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 96.7% | 27.6% | 31.0% | 17.2% | +2.6 | 1.84 | 3.88 | +9.1 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 26.7% | 30.0% | 16.7% | +2.1 | 1.65 | 3.66 | +8.8 | +5.1 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 13.3% | 25.0% | 25.0% | 25.0% | -5.8 | 0.38 | 1.15 | +6.2 | +9.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -11.6 | 0.00 | 0.00 | +2.5 | +16.2 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=30.8% Avg=+2.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 13.3% | +1.2 | 1.22 | 3.35 | +18.9 | +11.8 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 13.3% | +1.2 | 1.22 | 3.35 | +18.9 | +11.8 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 13.3% | +1.2 | 1.22 | 3.35 | +18.9 | +11.8 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 13.3% | +1.2 | 1.22 | 3.35 | +18.9 | +11.8 |
| `asian_range_gte_30` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 13.3% | +1.2 | 1.22 | 3.35 | +18.9 | +11.8 |
| `confluence_gte_60` | 10 | S_STRANGER | 66.7% | 20.0% | 20.0% | 0.0% | -3.7 | 0.47 | 1.87 | +18.4 | +14.7 |
| `confluence_gte_70` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +17.4 | +17.9 |
| `tdi_rsi_gt_signal` | 4 | R_REPEATER | 26.7% | 50.0% | 50.0% | 0.0% | +6.9 | 6.98 | 6.98 | +25.6 | +9.4 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 93.3% | 21.4% | 21.4% | 7.1% | +0.8 | 1.14 | 4.17 | +19.7 | +12.6 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 13.3% | +1.2 | 1.22 | 3.35 | +18.9 | +11.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 26.7% | 50.0% | 50.0% | 0.0% | +6.9 | 6.98 | 6.98 | +25.6 | +9.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 26.7% | 26.7% | 13.3% | +1.2 | 1.22 | 3.35 | +18.9 | +11.8 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 86.7% | 30.8% | 30.8% | 15.4% | +2.4 | 1.43 | 3.23 | +19.6 | +12.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +13.5 | +9.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=37.5% Avg=+0.5; validation N=5 Fav=40.0% Avg=+11.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 21.1% | +2.7 | 2.72 | 6.52 | +8.9 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 94.7% | 27.8% | 27.8% | 16.7% | +2.8 | 2.72 | 6.52 | +8.9 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 21.1% | +2.7 | 2.72 | 6.52 | +8.9 | +4.8 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 21.1% | +2.7 | 2.72 | 6.52 | +8.9 | +4.8 |
| `asian_range_gte_30` | 13 | S_STRANGER | 68.4% | 38.5% | 38.5% | 15.4% | +4.9 | 4.61 | 7.38 | +9.6 | +4.9 |
| `confluence_gte_60` | 6 | S_STRANGER | 31.6% | 16.7% | 16.7% | 16.7% | +1.6 | 1.70 | 8.49 | +10.7 | +4.9 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 52.6% | 20.0% | 20.0% | 10.0% | +2.1 | 2.61 | 10.45 | +7.8 | +4.6 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 57.9% | 9.1% | 9.1% | 0.0% | -1.2 | 0.46 | 4.55 | +4.5 | +5.6 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 68.4% | 38.5% | 38.5% | 15.4% | +4.9 | 4.61 | 7.38 | +9.6 | +4.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 36.8% | 28.6% | 28.6% | 14.3% | +4.0 | 6.06 | 15.16 | +9.4 | +4.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 21.1% | +2.7 | 2.72 | 6.52 | +8.9 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 26.3% | 26.3% | 21.1% | +2.7 | 2.72 | 6.52 | +8.9 | +4.8 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 10.5% | 50.0% | 50.0% | 0.0% | +2.2 | 1.70 | 1.70 | +5.4 | +5.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 10.5% | 50.0% | 50.0% | 0.0% | +2.2 | 1.70 | 1.70 | +5.4 | +5.9 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=17 Fav=35.3% Avg=+1.6; validation N=3 Fav=33.3% Avg=-0.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 38 | S_STRANGER | 100.0% | 26.3% | 26.3% | 7.9% | -0.8 | 0.81 | 2.18 | +7.9 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 47.4% | 33.3% | 33.3% | 11.1% | +1.4 | 1.51 | 3.02 | +9.9 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 25 | S_STRANGER | 65.8% | 28.0% | 28.0% | 12.0% | -0.2 | 0.94 | 2.41 | +8.1 | +7.3 |
| `stop_hunt_le_90` | 38 | S_STRANGER | 100.0% | 26.3% | 26.3% | 7.9% | -0.8 | 0.81 | 2.18 | +7.9 | +7.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 19 | S_STRANGER | 50.0% | 26.3% | 26.3% | 10.5% | +0.2 | 1.06 | 2.76 | +8.9 | +8.5 |
| `confluence_gte_70` | 5 | S_STRANGER | 13.2% | 20.0% | 20.0% | 20.0% | +0.0 | 1.01 | 3.02 | +7.7 | +10.2 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 55.3% | 28.6% | 28.6% | 9.5% | -0.3 | 0.91 | 2.13 | +8.8 | +9.1 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 52.6% | 35.0% | 35.0% | 10.0% | +1.3 | 1.44 | 2.48 | +9.6 | +9.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 38 | S_STRANGER | 100.0% | 26.3% | 26.3% | 7.9% | -0.8 | 0.81 | 2.18 | +7.9 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 100.0% | 26.3% | 26.3% | 7.9% | -0.8 | 0.81 | 2.18 | +7.9 | +7.3 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 7.9% | 0.0% | 0.0% | 0.0% | -1.7 | 0.00 | 0.00 | +2.2 | +3.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -0.3 | 0.00 | 0.00 | +2.8 | +1.8 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-12.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=50.0% Avg=+1.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 10.5% | -0.8 | 0.79 | 1.59 | +8.1 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 10.5% | -0.8 | 0.79 | 1.59 | +8.1 | +7.4 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 10.5% | -0.8 | 0.79 | 1.59 | +8.1 | +7.4 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 10.5% | -0.8 | 0.79 | 1.59 | +8.1 | +7.4 |
| `asian_range_gte_30` | 10 | S_STRANGER | 52.6% | 10.0% | 20.0% | 10.0% | -2.9 | 0.33 | 1.14 | +7.5 | +9.1 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 10.5% | -0.8 | 0.79 | 1.59 | +8.1 | +7.4 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 10.5% | -0.8 | 0.79 | 1.59 | +8.1 | +7.4 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 42.1% | 37.5% | 37.5% | 0.0% | -2.1 | 0.64 | 1.07 | +8.6 | +8.7 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 57.9% | 27.3% | 27.3% | 0.0% | -2.7 | 0.50 | 1.34 | +7.5 | +9.8 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 52.6% | 10.0% | 20.0% | 10.0% | -2.9 | 0.33 | 1.14 | +7.5 | +9.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 21.1% | 25.0% | 25.0% | 0.0% | -3.4 | 0.50 | 1.51 | +10.4 | +8.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 10.5% | -0.8 | 0.79 | 1.59 | +8.1 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 26.3% | 31.6% | 10.5% | -0.8 | 0.79 | 1.59 | +8.1 | +7.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.7; validation N=6 Fav=50.0% Avg=+2.6; out_of_sample N=2 Fav=50.0% Avg=+0.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 57 | S_STRANGER | 100.0% | 26.3% | 26.3% | 5.3% | -1.7 | 0.61 | 1.68 | +6.7 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 28.1% | 18.8% | 18.8% | 12.5% | -5.2 | 0.32 | 1.38 | +6.9 | +6.9 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 42.1% | 16.7% | 16.7% | 8.3% | -5.1 | 0.29 | 1.45 | +5.8 | +7.7 |
| `stop_hunt_le_90` | 57 | S_STRANGER | 100.0% | 26.3% | 26.3% | 5.3% | -1.7 | 0.61 | 1.68 | +6.7 | +6.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 51 | S_STRANGER | 89.5% | 29.4% | 29.4% | 5.9% | -1.8 | 0.62 | 1.49 | +7.0 | +6.5 |
| `confluence_gte_70` | 9 | S_STRANGER | 15.8% | 44.4% | 44.4% | 11.1% | +1.7 | 1.77 | 2.22 | +10.2 | +4.8 |
| `tdi_rsi_gt_signal` | 22 | S_STRANGER | 38.6% | 9.1% | 9.1% | 4.5% | -3.5 | 0.17 | 1.60 | +4.6 | +6.8 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 40.4% | 13.0% | 13.0% | 0.0% | -3.5 | 0.17 | 1.14 | +4.1 | +7.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 55 | S_STRANGER | 96.5% | 27.3% | 27.3% | 5.5% | -1.6 | 0.63 | 1.63 | +6.9 | +6.2 |
| `feature_stale_hod_exhaustion_reject` | 57 | S_STRANGER | 100.0% | 26.3% | 26.3% | 5.3% | -1.7 | 0.61 | 1.68 | +6.7 | +6.2 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +1.4 | +4.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 3.5% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +1.3 | +5.6 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=0.0% Avg=-2.3; validation N=3 Fav=33.3% Avg=+5.7; out_of_sample N=7 Fav=57.1% Avg=+5.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 39 | S_STRANGER | 100.0% | 25.6% | 25.6% | 7.7% | +0.2 | 1.06 | 2.97 | +8.8 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 38.5% | 33.3% | 33.3% | 6.7% | +2.9 | 2.96 | 5.91 | +10.6 | +3.2 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 48.7% | 31.6% | 31.6% | 5.3% | +1.1 | 1.42 | 3.08 | +9.4 | +4.9 |
| `stop_hunt_le_90` | 39 | S_STRANGER | 100.0% | 25.6% | 25.6% | 7.7% | +0.2 | 1.06 | 2.97 | +8.8 | +5.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 39 | S_STRANGER | 100.0% | 25.6% | 25.6% | 7.7% | +0.2 | 1.06 | 2.97 | +8.8 | +5.6 |
| `confluence_gte_70` | 39 | S_STRANGER | 100.0% | 25.6% | 25.6% | 7.7% | +0.2 | 1.06 | 2.97 | +8.8 | +5.6 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 53.8% | 28.6% | 28.6% | 9.5% | +0.9 | 1.30 | 3.25 | +9.3 | +5.3 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 48.7% | 31.6% | 31.6% | 5.3% | +1.8 | 1.53 | 3.31 | +9.4 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 39 | S_STRANGER | 100.0% | 25.6% | 25.6% | 7.7% | +0.2 | 1.06 | 2.97 | +8.8 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 39 | S_STRANGER | 100.0% | 25.6% | 25.6% | 7.7% | +0.2 | 1.06 | 2.97 | +8.8 | +5.6 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +2.8 | +4.1 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 5.1% | 0.0% | 0.0% | 0.0% | -2.1 | 0.00 | 0.00 | +1.2 | +3.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-6.0; validation N=6 Fav=66.7% Avg=+10.0; out_of_sample N=1 Fav=0.0% Avg=-0.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 25.0% | 29.2% | 8.3% | +2.1 | 2.01 | 4.31 | +9.8 | +4.7 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 29.2% | 0.0% | 14.3% | 0.0% | -0.9 | 0.44 | 2.21 | +6.5 | +5.3 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 37.5% | 11.1% | 22.2% | 11.1% | +1.8 | 2.34 | 7.03 | +8.9 | +5.0 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 25.0% | 29.2% | 8.3% | +2.1 | 2.01 | 4.31 | +9.8 | +4.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 25.0% | 29.2% | 8.3% | +2.1 | 2.01 | 4.31 | +9.8 | +4.7 |
| `confluence_gte_70` | 8 | R_REPEATER | 33.3% | 50.0% | 50.0% | 12.5% | +6.7 | 7.23 | 7.23 | +14.5 | +3.3 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -2.0 | 0.00 | 0.00 | +2.5 | +7.9 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 66.7% | 31.2% | 31.2% | 12.5% | +4.0 | 3.58 | 7.17 | +11.9 | +4.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 25.0% | 29.2% | 8.3% | +2.1 | 2.01 | 4.31 | +9.8 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 25.0% | 29.2% | 8.3% | +2.1 | 2.01 | 4.31 | +9.8 | +4.7 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 4.2% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +0.0 | +6.4 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=50.0% Avg=+5.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 56 | S_STRANGER | 100.0% | 25.0% | 26.8% | 17.9% | -0.1 | 0.96 | 2.43 | +8.7 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 37.5% | 23.8% | 28.6% | 19.0% | -1.1 | 0.70 | 1.64 | +9.1 | +8.3 |
| `hunt_to_ar_ratio_le_2_5` | 34 | S_STRANGER | 60.7% | 23.5% | 26.5% | 17.6% | -1.1 | 0.72 | 1.85 | +8.4 | +7.5 |
| `stop_hunt_le_90` | 56 | S_STRANGER | 100.0% | 25.0% | 26.8% | 17.9% | -0.1 | 0.96 | 2.43 | +8.7 | +6.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 32 | S_STRANGER | 57.1% | 15.6% | 18.8% | 9.4% | -2.5 | 0.41 | 1.62 | +8.7 | +8.3 |
| `confluence_gte_70` | 4 | R_REPEATER | 7.1% | 50.0% | 50.0% | 25.0% | +4.5 | 6.11 | 6.11 | +15.2 | +9.5 |
| `tdi_rsi_gt_signal` | 49 | S_STRANGER | 87.5% | 26.5% | 28.6% | 16.3% | +0.5 | 1.21 | 2.84 | +8.7 | +5.6 |
| `tdi_rsi_gte_50` | 30 | S_STRANGER | 53.6% | 26.7% | 26.7% | 10.0% | -0.1 | 0.96 | 2.41 | +9.6 | +6.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | R_RUNNER | 1.8% | 100.0% | 100.0% | 100.0% | +9.6 | 999.00 | 999.00 | +11.7 | +0.3 |
| `feature_extreme_hunt_with_exception` | 49 | S_STRANGER | 87.5% | 24.5% | 26.5% | 18.4% | -0.7 | 0.81 | 2.05 | +8.6 | +7.0 |
| `feature_stale_hod_exhaustion_reject` | 55 | S_STRANGER | 98.2% | 25.5% | 27.3% | 18.2% | -0.0 | 0.99 | 2.44 | +8.9 | +6.4 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 16.1% | 44.4% | 44.4% | 22.2% | +4.6 | 4.23 | 5.29 | +9.5 | +2.2 |
| `feature_eurjpy_tdi50_reclaim` | 6 | R_REPEATER | 10.7% | 50.0% | 50.0% | 16.7% | +5.9 | 4.79 | 4.79 | +10.5 | +2.6 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+5.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=42.9% Avg=+2.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 56 | S_STRANGER | 100.0% | 25.0% | 26.8% | 8.9% | -0.2 | 0.93 | 2.36 | +6.8 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 25.0% | 28.6% | 28.6% | 14.3% | -0.3 | 0.92 | 1.85 | +8.9 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 41.1% | 26.1% | 26.1% | 8.7% | +0.2 | 1.05 | 2.63 | +8.5 | +5.8 |
| `stop_hunt_le_90` | 56 | S_STRANGER | 100.0% | 25.0% | 26.8% | 8.9% | -0.2 | 0.93 | 2.36 | +6.8 | +6.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 51 | S_STRANGER | 91.1% | 23.5% | 25.5% | 7.8% | -0.4 | 0.89 | 2.46 | +6.7 | +6.4 |
| `confluence_gte_70` | 10 | S_STRANGER | 17.9% | 40.0% | 40.0% | 20.0% | +3.3 | 2.45 | 3.67 | +9.7 | +6.4 |
| `tdi_rsi_gt_signal` | 28 | S_STRANGER | 50.0% | 25.0% | 25.0% | 7.1% | +0.2 | 1.08 | 3.09 | +7.1 | +6.3 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 41.1% | 21.7% | 21.7% | 8.7% | +0.5 | 1.19 | 4.05 | +7.1 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 54 | S_STRANGER | 96.4% | 24.1% | 25.9% | 9.3% | -0.6 | 0.81 | 2.14 | +6.5 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 56 | S_STRANGER | 100.0% | 25.0% | 26.8% | 8.9% | -0.2 | 0.93 | 2.36 | +6.8 | +6.2 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 3.6% | 50.0% | 50.0% | 0.0% | +10.4 | 6.45 | 6.45 | +14.2 | +14.9 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=25.0% Avg=-1.3; out_of_sample N=7 Fav=28.6% Avg=+0.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | -1.3 | 0.57 | 1.70 | +8.7 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 31.2% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +7.3 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 43.8% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +5.8 | +6.8 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | -1.3 | 0.57 | 1.70 | +8.7 | +6.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | -1.3 | 0.57 | 1.70 | +8.7 | +6.7 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | -1.3 | 0.57 | 1.70 | +8.7 | +6.7 |
| `tdi_rsi_gt_signal` | 3 | R_REPEATER | 18.8% | 66.7% | 66.7% | 0.0% | +6.0 | 8.78 | 4.39 | +15.0 | +4.3 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 93.8% | 26.7% | 26.7% | 0.0% | -0.4 | 0.82 | 2.27 | +9.1 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | -1.3 | 0.57 | 1.70 | +8.7 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 0.0% | -1.3 | 0.57 | 1.70 | +8.7 | +6.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=0.0% Avg=-1.4; validation N=6 Fav=33.3% Avg=-1.8; out_of_sample N=2 Fav=50.0% Avg=-0.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.5 | 0.51 | 1.36 | +6.4 | +7.9 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.5 | 0.51 | 1.36 | +6.4 | +7.9 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.5 | 0.51 | 1.36 | +6.4 | +7.9 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.5 | 0.51 | 1.36 | +6.4 | +7.9 |
| `asian_range_gte_30` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 10.0% | -0.9 | 0.66 | 2.30 | +6.6 | +6.7 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.5 | 0.51 | 1.36 | +6.4 | +7.9 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.5 | 0.51 | 1.36 | +6.4 | +7.9 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 10.0% | -1.8 | 0.49 | 1.71 | +6.5 | +8.9 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -4.2 | 0.00 | 0.00 | +8.8 | +10.1 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 83.3% | 20.0% | 20.0% | 10.0% | -0.9 | 0.66 | 2.30 | +6.6 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 11.1% | -0.9 | 0.69 | 2.06 | +7.0 | +7.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.5 | 0.51 | 1.36 | +6.4 | +7.9 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 25.0% | 25.0% | 8.3% | -1.5 | 0.51 | 1.36 | +6.4 | +7.9 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +9.2 | +3.0 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-9.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=25.0% Avg=+3.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 12.5% | -1.5 | 0.78 | 2.33 | +11.8 | +14.1 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 12.5% | -1.5 | 0.78 | 2.33 | +11.8 | +14.1 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 12.5% | -1.5 | 0.78 | 2.33 | +11.8 | +14.1 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 12.5% | -1.5 | 0.78 | 2.33 | +11.8 | +14.1 |
| `asian_range_gte_30` | 15 | S_STRANGER | 93.8% | 20.0% | 20.0% | 6.7% | -3.7 | 0.49 | 1.97 | +10.2 | +14.8 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 12.5% | -1.5 | 0.78 | 2.33 | +11.8 | +14.1 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 12.5% | -1.5 | 0.78 | 2.33 | +11.8 | +14.1 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 18.8% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +6.6 | +9.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 56.2% | 22.2% | 22.2% | 11.1% | +1.7 | 1.53 | 5.36 | +13.2 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 93.8% | 20.0% | 20.0% | 6.7% | -3.7 | 0.49 | 1.97 | +10.2 | +14.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 18.8% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +6.6 | +9.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 12.5% | -1.5 | 0.78 | 2.33 | +11.8 | +14.1 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 25.0% | 25.0% | 12.5% | -1.5 | 0.78 | 2.33 | +11.8 | +14.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 18.8% | 33.3% | 33.3% | 33.3% | -5.3 | 0.50 | 1.00 | +9.1 | +26.9 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=8 Fav=37.5% Avg=+2.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 25.0% | 29.2% | 12.5% | -5.6 | 0.39 | 0.90 | +9.4 | +6.0 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 75.0% | 11.1% | 16.7% | 5.6% | -8.6 | 0.14 | 0.64 | +6.8 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 100.0% | 25.0% | 29.2% | 12.5% | -5.6 | 0.39 | 0.90 | +9.4 | +6.0 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 25.0% | 29.2% | 12.5% | -5.6 | 0.39 | 0.90 | +9.4 | +6.0 |
| `asian_range_gte_30` | 13 | S_STRANGER | 54.2% | 30.8% | 38.5% | 15.4% | -1.7 | 0.76 | 1.06 | +10.2 | +3.8 |
| `confluence_gte_60` | 3 | S_STRANGER | 12.5% | 33.3% | 33.3% | 0.0% | -3.5 | 0.49 | 0.98 | +10.2 | +2.9 |
| `confluence_gte_70` | 2 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -10.1 | 0.00 | 0.00 | +9.3 | +3.7 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 50.0% | 33.3% | 33.3% | 8.3% | -2.4 | 0.65 | 1.31 | +9.7 | +8.2 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 33.3% | 37.5% | 37.5% | 12.5% | +2.9 | 2.03 | 3.38 | +10.5 | +10.1 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 45.8% | 18.2% | 27.3% | 9.1% | -6.0 | 0.27 | 0.63 | +6.2 | +3.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 20.8% | 40.0% | 40.0% | 0.0% | -0.7 | 0.83 | 1.24 | +5.7 | +3.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 25.0% | 29.2% | 12.5% | -5.6 | 0.39 | 0.90 | +9.4 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 25.0% | 29.2% | 12.5% | -5.6 | 0.39 | 0.90 | +9.4 | +6.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=+0.0; validation N=11 Fav=27.3% Avg=-3.1; out_of_sample N=7 Fav=28.6% Avg=+0.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 41 | S_STRANGER | 100.0% | 24.4% | 26.8% | 14.6% | -0.0 | 1.00 | 2.53 | +7.2 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 34.1% | 21.4% | 28.6% | 14.3% | -2.4 | 0.39 | 0.88 | +7.3 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 46.3% | 26.3% | 31.6% | 10.5% | -1.6 | 0.56 | 1.13 | +8.1 | +6.9 |
| `stop_hunt_le_90` | 41 | S_STRANGER | 100.0% | 24.4% | 26.8% | 14.6% | -0.0 | 1.00 | 2.53 | +7.2 | +7.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 41 | S_STRANGER | 100.0% | 24.4% | 26.8% | 14.6% | -0.0 | 1.00 | 2.53 | +7.2 | +7.1 |
| `confluence_gte_70` | 16 | S_STRANGER | 39.0% | 12.5% | 12.5% | 6.2% | -1.5 | 0.51 | 3.07 | +5.1 | +6.1 |
| `tdi_rsi_gt_signal` | 19 | S_STRANGER | 46.3% | 21.1% | 21.1% | 0.0% | -0.5 | 0.78 | 2.73 | +5.9 | +6.5 |
| `tdi_rsi_gte_50` | 24 | S_STRANGER | 58.5% | 12.5% | 12.5% | 0.0% | -2.3 | 0.32 | 2.14 | +5.0 | +8.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 41 | S_STRANGER | 100.0% | 24.4% | 26.8% | 14.6% | -0.0 | 1.00 | 2.53 | +7.2 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 41 | S_STRANGER | 100.0% | 24.4% | 26.8% | 14.6% | -0.0 | 1.00 | 2.53 | +7.2 | +7.1 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 2.4% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +4.9 | +1.1 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=80.0% Avg=+16.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 78 | S_STRANGER | 100.0% | 24.4% | 25.6% | 14.1% | +0.8 | 1.24 | 3.29 | +9.5 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 25.6% | 25.0% | 25.0% | 10.0% | +2.2 | 1.78 | 5.34 | +11.2 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 34 | S_STRANGER | 43.6% | 20.6% | 20.6% | 8.8% | -0.7 | 0.83 | 3.22 | +9.1 | +7.2 |
| `stop_hunt_le_90` | 78 | S_STRANGER | 100.0% | 24.4% | 25.6% | 14.1% | +0.8 | 1.24 | 3.29 | +9.5 | +6.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 45 | S_STRANGER | 57.7% | 28.9% | 28.9% | 8.9% | +1.5 | 1.40 | 3.45 | +10.8 | +7.2 |
| `confluence_gte_70` | 5 | R_RUNNER | 6.4% | 80.0% | 80.0% | 40.0% | +16.2 | 28.86 | 7.22 | +24.5 | +7.2 |
| `tdi_rsi_gt_signal` | 45 | S_STRANGER | 57.7% | 22.2% | 24.4% | 8.9% | +0.2 | 1.06 | 3.08 | +8.8 | +6.3 |
| `tdi_rsi_gte_50` | 46 | S_STRANGER | 59.0% | 34.8% | 34.8% | 17.4% | +3.5 | 2.11 | 3.69 | +12.9 | +6.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 69 | S_STRANGER | 88.5% | 23.2% | 24.6% | 13.0% | +0.7 | 1.18 | 3.34 | +9.8 | +7.0 |
| `feature_stale_hod_exhaustion_reject` | 78 | S_STRANGER | 100.0% | 24.4% | 25.6% | 14.1% | +0.8 | 1.24 | 3.29 | +9.5 | +6.5 |
| `feature_momentum_breakout_exception` | 9 | S_STRANGER | 11.5% | 33.3% | 33.3% | 22.2% | +1.8 | 3.22 | 5.37 | +6.6 | +2.9 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 7.7% | 33.3% | 33.3% | 16.7% | +2.1 | 2.79 | 5.58 | +6.7 | +3.5 |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=14 Fav=28.6% Avg=+3.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 23.5% | 29.4% | 35.3% | +2.1 | 1.32 | 2.64 | +16.1 | +11.1 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 94.1% | 18.8% | 25.0% | 31.2% | +1.1 | 1.17 | 2.92 | +14.8 | +11.7 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 94.1% | 18.8% | 25.0% | 31.2% | +1.1 | 1.17 | 2.92 | +14.8 | +11.7 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 23.5% | 29.4% | 35.3% | +2.1 | 1.32 | 2.64 | +16.1 | +11.1 |
| `asian_range_gte_30` | 9 | S_STRANGER | 52.9% | 22.2% | 22.2% | 22.2% | -0.5 | 0.95 | 3.31 | +15.8 | +13.9 |
| `confluence_gte_60` | 4 | S_STRANGER | 23.5% | 25.0% | 50.0% | 25.0% | +7.7 | 2.83 | 2.83 | +17.8 | +11.7 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 82.4% | 28.6% | 35.7% | 35.7% | +3.3 | 1.46 | 2.34 | +17.4 | +12.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 58.8% | 20.0% | 20.0% | 20.0% | -3.2 | 0.67 | 2.67 | +15.3 | +15.1 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 52.9% | 22.2% | 22.2% | 22.2% | -0.5 | 0.95 | 3.31 | +15.8 | +13.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 41.2% | 28.6% | 28.6% | 28.6% | +0.9 | 1.08 | 2.71 | +17.0 | +16.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 23.5% | 29.4% | 35.3% | +2.1 | 1.32 | 2.64 | +16.1 | +11.1 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 94.1% | 25.0% | 31.2% | 37.5% | +2.5 | 1.37 | 2.46 | +16.5 | +10.6 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 29.4% | 20.0% | 20.0% | 40.0% | +0.2 | 1.04 | 3.11 | +12.1 | +10.8 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 0.0% | -8.8 | 0.00 | 0.00 | +4.6 | +17.6 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=16 Fav=25.0% Avg=-7.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | -9.0 | 0.23 | 0.74 | +9.5 | +14.3 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 23.5% | 25.0% | 25.0% | 25.0% | -6.1 | 0.46 | 1.39 | +9.2 | +13.5 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 14.3% | -13.7 | 0.18 | 1.09 | +6.6 | +19.5 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 23.5% | 23.5% | 11.8% | -9.0 | 0.23 | 0.74 | +9.5 | +14.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 5 | S_STRANGER | 29.4% | 20.0% | 20.0% | 0.0% | -6.6 | 0.04 | 0.16 | +11.0 | +13.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 76.5% | 23.1% | 23.1% | 7.7% | -9.8 | 0.16 | 0.54 | +10.3 | +14.5 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 58.8% | 20.0% | 20.0% | 0.0% | -12.3 | 0.12 | 0.48 | +10.0 | +17.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 76.5% | 23.1% | 23.1% | 15.4% | -7.2 | 0.24 | 0.81 | +9.8 | +12.3 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 94.1% | 25.0% | 25.0% | 12.5% | -7.8 | 0.27 | 0.80 | +10.1 | +13.2 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 0.0% | -10.1 | 0.18 | 1.08 | +6.2 | +14.0 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 29.4% | 20.0% | 20.0% | 0.0% | -15.4 | 0.17 | 0.67 | +7.6 | +20.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=100.0% Avg=+19.0; validation N=4 Fav=25.0% Avg=-1.0; out_of_sample N=7 Fav=14.3% Avg=-2.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 16.7% | -0.9 | 0.82 | 2.14 | +9.2 | +6.0 |
| `hunt_to_ar_ratio_le_2_0` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 16.7% | -0.9 | 0.82 | 2.14 | +9.2 | +6.0 |
| `hunt_to_ar_ratio_le_2_5` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 16.7% | -0.9 | 0.82 | 2.14 | +9.2 | +6.0 |
| `stop_hunt_le_90` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 16.7% | -0.9 | 0.82 | 2.14 | +9.2 | +6.0 |
| `asian_range_gte_30` | 23 | S_STRANGER | 76.7% | 17.4% | 17.4% | 13.0% | -3.2 | 0.45 | 2.02 | +7.8 | +6.2 |
| `confluence_gte_60` | 26 | S_STRANGER | 86.7% | 23.1% | 23.1% | 15.4% | -1.7 | 0.70 | 2.32 | +8.5 | +6.1 |
| `confluence_gte_70` | 1 | S_STRANGER | 3.3% | 0.0% | 0.0% | 0.0% | -5.1 | 0.00 | 0.00 | +1.4 | +11.4 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 53.3% | 25.0% | 25.0% | 12.5% | +0.1 | 1.03 | 3.08 | +9.9 | +5.5 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 43.3% | 30.8% | 30.8% | 15.4% | +1.1 | 1.22 | 2.75 | +11.9 | +5.9 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 76.7% | 17.4% | 17.4% | 13.0% | -3.2 | 0.45 | 2.02 | +7.8 | +6.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 43.3% | 23.1% | 23.1% | 7.7% | -1.5 | 0.72 | 2.39 | +8.6 | +5.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 16.7% | -0.9 | 0.82 | 2.14 | +9.2 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 30 | S_STRANGER | 100.0% | 23.3% | 26.7% | 16.7% | -0.9 | 0.82 | 2.14 | +9.2 | +6.0 |
| `feature_momentum_breakout_exception` | 1 | R_RUNNER | 3.3% | 100.0% | 100.0% | 0.0% | +14.3 | 999.00 | 999.00 | +14.7 | +0.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 3.3% | 100.0% | 100.0% | 0.0% | +14.3 | 999.00 | 999.00 | +14.7 | +0.0 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=5 Fav=40.0% Avg=+11.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=16.7% Avg=-0.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | +3.1 | 1.69 | 5.08 | +15.9 | +9.9 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | +3.1 | 1.69 | 5.08 | +15.9 | +9.9 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | +3.1 | 1.69 | 5.08 | +15.9 | +9.9 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | +3.1 | 1.69 | 5.08 | +15.9 | +9.9 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | +3.1 | 1.69 | 5.08 | +15.9 | +9.9 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | +3.1 | 1.69 | 5.08 | +15.9 | +9.9 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | +3.1 | 1.69 | 5.08 | +15.9 | +9.9 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 33.3% | +12.0 | 28.65 | 57.31 | +19.3 | +1.9 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 84.6% | 27.3% | 27.3% | 27.3% | +5.0 | 2.26 | 5.27 | +17.9 | +9.5 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | +3.1 | 1.69 | 5.08 | +15.9 | +9.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 33.3% | +12.0 | 28.65 | 57.31 | +19.3 | +1.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | +3.1 | 1.69 | 5.08 | +15.9 | +9.9 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | +3.1 | 1.69 | 5.08 | +15.9 | +9.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=16 Fav=37.5% Avg=+3.3; validation N=3 Fav=0.0% Avg=-1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 39 | S_STRANGER | 100.0% | 23.1% | 23.1% | 17.9% | -0.1 | 0.97 | 2.81 | +7.3 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 48.7% | 31.6% | 31.6% | 21.1% | +2.5 | 1.75 | 3.21 | +9.0 | +5.8 |
| `hunt_to_ar_ratio_le_2_5` | 26 | S_STRANGER | 66.7% | 30.8% | 30.8% | 26.9% | +2.0 | 1.66 | 2.91 | +8.6 | +5.3 |
| `stop_hunt_le_90` | 39 | S_STRANGER | 100.0% | 23.1% | 23.1% | 17.9% | -0.1 | 0.97 | 2.81 | +7.3 | +5.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 23 | S_STRANGER | 59.0% | 17.4% | 17.4% | 21.7% | +0.4 | 1.11 | 4.43 | +7.6 | +6.3 |
| `confluence_gte_70` | 2 | R_REPEATER | 5.1% | 50.0% | 50.0% | 0.0% | +9.9 | 999.00 | 999.00 | +14.5 | +1.9 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 53.8% | 23.8% | 23.8% | 9.5% | +0.8 | 1.30 | 3.91 | +7.1 | +5.0 |
| `tdi_rsi_gte_50` | 21 | S_STRANGER | 53.8% | 19.0% | 19.0% | 9.5% | -0.7 | 0.83 | 3.10 | +6.7 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 39 | S_STRANGER | 100.0% | 23.1% | 23.1% | 17.9% | -0.1 | 0.97 | 2.81 | +7.3 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 97.4% | 23.7% | 23.7% | 18.4% | -0.1 | 0.98 | 2.73 | +7.4 | +5.9 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 10.3% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +1.8 | +5.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +1.2 | +6.7 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+5.4; validation N=2 Fav=50.0% Avg=+13.2; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -3.0 | 0.65 | 2.16 | +12.3 | +9.9 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -3.0 | 0.65 | 2.16 | +12.3 | +9.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 76.9% | 20.0% | 20.0% | 20.0% | -4.8 | 0.48 | 1.93 | +10.7 | +9.9 |
| `confluence_gte_70` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 25.0% | -3.0 | 0.65 | 1.96 | +13.3 | +12.9 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 27.3% | 27.3% | 27.3% | -0.5 | 0.93 | 2.48 | +13.0 | +8.3 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -14.2 | 0.00 | 0.00 | +9.0 | +17.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 53.8% | 0.0% | 0.0% | 0.0% | -12.3 | 0.00 | 0.00 | +7.4 | +14.8 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 23.1% | 23.1% | 23.1% | -3.0 | 0.65 | 2.16 | +12.3 | +9.9 |
| `feature_momentum_breakout_exception` | 6 | R_REPEATER | 46.2% | 50.0% | 50.0% | 50.0% | +8.0 | 3.08 | 3.08 | +18.1 | +4.1 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=0.0% Avg=-0.7; validation N=10 Fav=40.0% Avg=+3.0; out_of_sample N=4 Fav=0.0% Avg=-2.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +0.9 | 1.43 | 4.65 | +8.6 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 94.4% | 23.5% | 23.5% | 11.8% | +1.0 | 1.48 | 4.43 | +8.8 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +0.9 | 1.43 | 4.65 | +8.6 | +5.4 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +0.9 | 1.43 | 4.65 | +8.6 | +5.4 |
| `asian_range_gte_30` | 17 | S_STRANGER | 94.4% | 23.5% | 23.5% | 11.8% | +1.0 | 1.48 | 4.43 | +8.8 | +5.5 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +0.9 | 1.43 | 4.65 | +8.6 | +5.4 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +0.9 | 1.43 | 4.65 | +8.6 | +5.4 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +6.9 | +3.0 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 94.4% | 17.6% | 17.6% | 5.9% | -0.2 | 0.92 | 4.00 | +7.5 | +5.5 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 94.4% | 23.5% | 23.5% | 11.8% | +1.0 | 1.48 | 4.43 | +8.8 | +5.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +6.9 | +3.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +0.9 | 1.43 | 4.65 | +8.6 | +5.4 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 11.1% | +0.9 | 1.43 | 4.65 | +8.6 | +5.4 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +0.0 | +7.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +0.0 | +7.0 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-9.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=30.0% Avg=-0.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -1.2 | 0.61 | 2.14 | +7.6 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 94.4% | 23.5% | 23.5% | 0.0% | -1.3 | 0.62 | 2.01 | +7.7 | +5.4 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -1.2 | 0.61 | 2.14 | +7.6 | +5.5 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -1.2 | 0.61 | 2.14 | +7.6 | +5.5 |
| `asian_range_gte_30` | 12 | S_STRANGER | 66.7% | 25.0% | 25.0% | 0.0% | -1.6 | 0.59 | 1.76 | +8.2 | +5.7 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -1.2 | 0.61 | 2.14 | +7.6 | +5.5 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -1.2 | 0.61 | 2.14 | +7.6 | +5.5 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 16.7% | 33.3% | 33.3% | 0.0% | +0.9 | 1.59 | 3.17 | +7.2 | +3.3 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 61.1% | 9.1% | 9.1% | 0.0% | -2.6 | 0.20 | 2.03 | +7.2 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 66.7% | 25.0% | 25.0% | 0.0% | -1.6 | 0.59 | 1.76 | +8.2 | +5.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -4.1 | 0.00 | 0.00 | +0.3 | +5.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -1.2 | 0.61 | 2.14 | +7.6 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 94.4% | 23.5% | 23.5% | 0.0% | -1.0 | 0.67 | 2.17 | +7.5 | +5.1 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -13.7 | 0.00 | 0.00 | +4.2 | +2.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -4.8 | 0.00 | 0.00 | +10.9 | +12.7 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=0.0% Avg=-3.0; validation N=2 Fav=0.0% Avg=-2.8; out_of_sample N=13 Fav=30.8% Avg=-2.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -2.3 | 0.41 | 1.43 | +6.8 | +5.8 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 83.3% | 13.3% | 13.3% | 0.0% | -3.9 | 0.16 | 1.04 | +5.8 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 88.9% | 12.5% | 12.5% | 0.0% | -3.7 | 0.16 | 1.11 | +6.1 | +6.4 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -2.3 | 0.41 | 1.43 | +6.8 | +5.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -2.3 | 0.41 | 1.43 | +6.8 | +5.8 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -2.3 | 0.41 | 1.43 | +6.8 | +5.8 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 55.6% | 10.0% | 10.0% | 0.0% | -4.7 | 0.12 | 1.12 | +4.4 | +7.2 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 61.1% | 9.1% | 9.1% | 0.0% | -4.4 | 0.12 | 1.21 | +6.6 | +7.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -2.3 | 0.41 | 1.43 | +6.8 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 22.2% | 22.2% | 0.0% | -2.3 | 0.41 | 1.43 | +6.8 | +5.8 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +8.2 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -3.4 | 0.00 | 0.00 | +8.2 | +5.4 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=50.0% Avg=+9.9; validation N=10 Fav=20.0% Avg=+4.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 26.1% | +2.1 | 1.73 | 4.84 | +11.1 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 26.1% | +2.1 | 1.73 | 4.84 | +11.1 | +7.4 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 26.1% | +2.1 | 1.73 | 4.84 | +11.1 | +7.4 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 26.1% | +2.1 | 1.73 | 4.84 | +11.1 | +7.4 |
| `asian_range_gte_30` | 22 | S_STRANGER | 95.7% | 18.2% | 18.2% | 22.7% | +0.8 | 1.26 | 4.43 | +9.9 | +7.4 |
| `confluence_gte_60` | 14 | S_STRANGER | 60.9% | 21.4% | 21.4% | 28.6% | +2.6 | 2.45 | 6.53 | +10.7 | +6.8 |
| `confluence_gte_70` | 2 | S_STRANGER | 8.7% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +6.6 | +10.7 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 60.9% | 28.6% | 28.6% | 42.9% | +5.9 | 5.27 | 10.55 | +14.3 | +5.1 |
| `tdi_rsi_gte_50` | 18 | S_STRANGER | 78.3% | 27.8% | 27.8% | 27.8% | +2.9 | 1.86 | 4.10 | +13.1 | +8.0 |
| `ratio_le_2_and_asian_gte_30` | 22 | S_STRANGER | 95.7% | 18.2% | 18.2% | 22.7% | +0.8 | 1.26 | 4.43 | +9.9 | +7.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 56.5% | 23.1% | 23.1% | 38.5% | +4.0 | 3.70 | 9.86 | +12.6 | +5.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 26.1% | +2.1 | 1.73 | 4.84 | +11.1 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 26.1% | +2.1 | 1.73 | 4.84 | +11.1 | +7.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=16.7% Avg=-0.4; validation N=1 Fav=100.0% Avg=+10.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 17.4% | +1.3 | 1.52 | 4.85 | +8.7 | +5.4 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 39.1% | 22.2% | 22.2% | 44.4% | +1.1 | 1.36 | 3.40 | +11.2 | +4.9 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 60.9% | 21.4% | 21.4% | 28.6% | +1.3 | 1.52 | 4.57 | +8.6 | +4.7 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 17.4% | +1.3 | 1.52 | 4.85 | +8.7 | +5.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 17.4% | +1.3 | 1.52 | 4.85 | +8.7 | +5.4 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 17.4% | +1.3 | 1.52 | 4.85 | +8.7 | +5.4 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 30.4% | 28.6% | 28.6% | 14.3% | +1.1 | 1.72 | 4.31 | +5.7 | +3.6 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 56.5% | 15.4% | 15.4% | 7.7% | -1.4 | 0.51 | 2.80 | +5.4 | +5.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 82.6% | 26.3% | 26.3% | 21.1% | +1.8 | 1.62 | 3.89 | +9.4 | +5.8 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 17.4% | +1.3 | 1.52 | 4.85 | +8.7 | +5.4 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 30.4% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +5.2 | +3.6 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 26.1% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +5.0 | +4.0 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-1.6; validation N=6 Fav=16.7% Avg=+1.0; out_of_sample N=10 Fav=40.0% Avg=+0.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 8.7% | -0.5 | 0.82 | 2.19 | +6.2 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 95.7% | 22.7% | 27.3% | 9.1% | -0.5 | 0.84 | 2.09 | +6.4 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 8.7% | -0.5 | 0.82 | 2.19 | +6.2 | +5.7 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 8.7% | -0.5 | 0.82 | 2.19 | +6.2 | +5.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 8.7% | -0.5 | 0.82 | 2.19 | +6.2 | +5.7 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 8.7% | -0.5 | 0.82 | 2.19 | +6.2 | +5.7 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 56.5% | 15.4% | 23.1% | 7.7% | -0.4 | 0.86 | 2.87 | +6.0 | +6.3 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 73.9% | 29.4% | 29.4% | 5.9% | +0.4 | 1.13 | 2.72 | +6.7 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 8.7% | -0.5 | 0.82 | 2.19 | +6.2 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 21.7% | 26.1% | 8.7% | -0.5 | 0.82 | 2.19 | +6.2 | +5.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-18.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=18 Fav=27.8% Avg=-0.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 8.7% | -4.2 | 0.40 | 1.36 | +8.0 | +12.9 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 21.7% | 0.0% | 0.0% | 0.0% | -16.1 | 0.00 | 0.00 | +5.5 | +10.9 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 39.1% | 11.1% | 11.1% | 0.0% | -8.1 | 0.24 | 1.93 | +7.4 | +16.5 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 21.7% | 21.7% | 8.7% | -4.2 | 0.40 | 1.36 | +8.0 | +12.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 22 | S_STRANGER | 95.7% | 22.7% | 22.7% | 9.1% | -4.3 | 0.41 | 1.30 | +8.2 | +12.6 |
| `confluence_gte_70` | 13 | S_STRANGER | 56.5% | 0.0% | 0.0% | 0.0% | -10.6 | 0.00 | 0.00 | +5.0 | +17.6 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 17.4% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +8.5 | +13.5 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 65.2% | 13.3% | 13.3% | 0.0% | -2.4 | 0.54 | 3.21 | +8.7 | +15.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 95.7% | 22.7% | 22.7% | 9.1% | -4.1 | 0.42 | 1.34 | +7.6 | +13.1 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 95.7% | 22.7% | 22.7% | 9.1% | -4.1 | 0.42 | 1.34 | +7.6 | +13.1 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -28.2 | 0.00 | 0.00 | +4.3 | +3.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -6.7 | 0.00 | 0.00 | +17.0 | +7.3 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=50.0% Avg=+9.7; validation N=5 Fav=40.0% Avg=+2.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 21.6% | 27.0% | 13.5% | -0.9 | 0.84 | 2.11 | +9.6 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 35.1% | 46.2% | 53.8% | 15.4% | +6.9 | 3.32 | 2.85 | +15.3 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 21 | S_STRANGER | 56.8% | 33.3% | 38.1% | 9.5% | +1.1 | 1.19 | 1.93 | +11.7 | +6.7 |
| `stop_hunt_le_90` | 37 | S_STRANGER | 100.0% | 21.6% | 27.0% | 13.5% | -0.9 | 0.84 | 2.11 | +9.6 | +6.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 25 | S_STRANGER | 67.6% | 28.0% | 32.0% | 16.0% | -0.1 | 0.98 | 1.97 | +11.7 | +6.5 |
| `confluence_gte_70` | 3 | S_STRANGER | 8.1% | 33.3% | 33.3% | 0.0% | -6.4 | 0.31 | 0.63 | +5.4 | +10.7 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 24.3% | 11.1% | 11.1% | 0.0% | -2.6 | 0.59 | 4.72 | +6.5 | +8.8 |
| `tdi_rsi_gte_50` | 27 | S_STRANGER | 73.0% | 25.9% | 25.9% | 7.4% | -0.3 | 0.95 | 2.71 | +9.7 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 37 | S_STRANGER | 100.0% | 21.6% | 27.0% | 13.5% | -0.9 | 0.84 | 2.11 | +9.6 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 21.6% | 27.0% | 13.5% | -0.9 | 0.84 | 2.11 | +9.6 | +6.6 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 10.8% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +2.7 | +6.3 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 10.8% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +2.7 | +6.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=66.7% Avg=+2.1; validation N=15 Fav=20.0% Avg=+0.5; out_of_sample N=5 Fav=20.0% Avg=+0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 37 | S_STRANGER | 100.0% | 21.6% | 21.6% | 5.4% | -2.0 | 0.51 | 1.65 | +6.7 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 29.7% | 9.1% | 9.1% | 0.0% | -6.6 | 0.18 | 1.62 | +5.3 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 43.2% | 18.8% | 18.8% | 0.0% | -4.6 | 0.24 | 0.87 | +5.9 | +5.5 |
| `stop_hunt_le_90` | 37 | S_STRANGER | 100.0% | 21.6% | 21.6% | 5.4% | -2.0 | 0.51 | 1.65 | +6.7 | +5.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 32 | S_STRANGER | 86.5% | 18.8% | 18.8% | 3.1% | -2.3 | 0.45 | 1.72 | +6.3 | +5.0 |
| `confluence_gte_70` | 2 | S_STRANGER | 5.4% | 0.0% | 0.0% | 0.0% | -2.9 | 0.00 | 0.00 | +4.2 | +7.1 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 16.2% | 0.0% | 0.0% | 0.0% | -1.7 | 0.00 | 0.00 | +3.9 | +4.6 |
| `tdi_rsi_gte_50` | 23 | S_STRANGER | 62.2% | 26.1% | 26.1% | 4.3% | +0.7 | 1.41 | 3.53 | +7.4 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 35 | S_STRANGER | 94.6% | 17.1% | 17.1% | 5.7% | -2.3 | 0.46 | 1.99 | +6.5 | +5.3 |
| `feature_stale_hod_exhaustion_reject` | 37 | S_STRANGER | 100.0% | 21.6% | 21.6% | 5.4% | -2.0 | 0.51 | 1.65 | +6.7 | +5.0 |
| `feature_momentum_breakout_exception` | 3 | R_REPEATER | 8.1% | 66.7% | 66.7% | 0.0% | +1.7 | 3.43 | 1.71 | +8.0 | +1.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_RUNNER | 5.4% | 100.0% | 100.0% | 0.0% | +3.6 | 999.00 | 999.00 | +8.8 | +0.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=+0.4; validation N=5 Fav=20.0% Avg=+7.0; out_of_sample N=2 Fav=50.0% Avg=+10.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | +2.7 | 1.75 | 6.40 | +10.9 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | +2.7 | 1.75 | 6.40 | +10.9 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | +2.7 | 1.75 | 6.40 | +10.9 | +7.2 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | +2.7 | 1.75 | 6.40 | +10.9 | +7.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 78.6% | 9.1% | 9.1% | 9.1% | +1.1 | 1.25 | 12.49 | +9.1 | +7.8 |
| `confluence_gte_70` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -7.9 | 0.00 | 0.00 | +2.7 | +18.3 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 78.6% | 27.3% | 27.3% | 27.3% | +5.2 | 2.89 | 7.72 | +13.4 | +5.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 11.1% | 11.1% | 11.1% | +2.6 | 1.63 | 13.03 | +10.3 | +9.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | +2.7 | 1.75 | 6.40 | +10.9 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 21.4% | +2.7 | 1.75 | 6.40 | +10.9 | +7.2 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 28.6% | 50.0% | 50.0% | 50.0% | +6.3 | 12.95 | 12.95 | +13.9 | +2.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 21.4% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +4.8 | +5.9 |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=33.3% Avg=+3.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 7.1% | +1.6 | 2.04 | 6.81 | +6.4 | +3.1 |
| `hunt_to_ar_ratio_le_2_0` | 1 | R_RUNNER | 7.1% | 100.0% | 100.0% | 100.0% | +28.7 | 999.00 | 999.00 | +40.6 | +1.4 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 33.3% | +7.6 | 4.87 | 9.75 | +16.2 | +3.0 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 7.1% | +1.6 | 2.04 | 6.81 | +6.4 | +3.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 7.1% | +1.6 | 2.04 | 6.81 | +6.4 | +3.1 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 7.1% | +1.6 | 2.04 | 6.81 | +6.4 | +3.1 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 64.3% | 33.3% | 33.3% | 11.1% | +3.0 | 2.60 | 5.21 | +8.7 | +2.8 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 33.3% | 33.3% | 11.1% | +3.6 | 3.91 | 6.51 | +8.5 | +2.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 11.1% | +2.7 | 3.01 | 9.04 | +7.8 | +2.8 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 7.1% | +1.6 | 2.04 | 6.81 | +6.4 | +3.1 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 0.0% | -0.3 | 0.83 | 3.33 | +3.8 | +3.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 0.0% | +1.3 | 1.93 | 3.85 | +5.0 | +3.1 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=+0.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=9 Fav=33.3% Avg=-7.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -6.3 | 0.11 | 0.36 | +6.0 | +4.1 |
| `hunt_to_ar_ratio_le_2_0` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +13.7 | +2.8 |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 25.0% | -8.2 | 0.00 | 0.00 | +4.1 | +4.1 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -6.3 | 0.11 | 0.36 | +6.0 | +4.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -6.3 | 0.11 | 0.36 | +6.0 | +4.1 |
| `confluence_gte_70` | 10 | S_STRANGER | 71.4% | 30.0% | 30.0% | 20.0% | -7.0 | 0.13 | 0.27 | +7.8 | +3.5 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 71.4% | 10.0% | 10.0% | 10.0% | -8.6 | 0.01 | 0.12 | +4.6 | +4.3 |
| `tdi_rsi_gte_50` | 2 | R_REPEATER | 14.3% | 50.0% | 50.0% | 0.0% | -0.6 | 0.54 | 0.54 | +10.5 | +3.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -6.3 | 0.11 | 0.36 | +6.0 | +4.1 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 14.3% | -6.3 | 0.11 | 0.36 | +6.0 | +4.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=-3.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=100.0% Avg=+11.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -7.0 | 0.31 | 1.12 | +8.0 | +9.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -7.0 | 0.31 | 1.12 | +8.0 | +9.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -7.0 | 0.31 | 1.12 | +8.0 | +9.7 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -7.0 | 0.31 | 1.12 | +8.0 | +9.7 |
| `asian_range_gte_30` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 0.0% | -8.5 | 0.24 | 1.21 | +7.3 | +9.5 |
| `confluence_gte_60` | 12 | S_STRANGER | 85.7% | 25.0% | 25.0% | 0.0% | -7.0 | 0.34 | 1.03 | +8.6 | +10.2 |
| `confluence_gte_70` | 3 | R_REPEATER | 21.4% | 66.7% | 66.7% | 0.0% | +8.2 | 4.10 | 2.05 | +15.6 | +10.9 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 57.1% | 37.5% | 37.5% | 0.0% | -2.0 | 0.73 | 1.22 | +10.4 | +13.9 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 57.1% | 37.5% | 37.5% | 0.0% | -2.0 | 0.73 | 1.22 | +10.4 | +13.9 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 0.0% | -8.5 | 0.24 | 1.21 | +7.3 | +9.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 42.9% | 33.3% | 33.3% | 0.0% | -3.2 | 0.63 | 1.26 | +9.8 | +14.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -7.0 | 0.31 | 1.12 | +8.0 | +9.7 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 21.4% | 21.4% | 0.0% | -7.0 | 0.31 | 1.12 | +8.0 | +9.7 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -11.5 | 0.00 | 0.00 | +5.0 | +1.8 |
| `feature_eurjpy_tdi50_reclaim` | 4 | R_REPEATER | 28.6% | 50.0% | 50.0% | 0.0% | -3.4 | 0.70 | 0.70 | +12.8 | +17.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-1.9; validation N=11 Fav=27.3% Avg=-1.7; out_of_sample N=2 Fav=50.0% Avg=-3.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 21.1% | 21.1% | 10.5% | -2.6 | 0.29 | 0.96 | +7.2 | +7.5 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 100.0% | 21.1% | 21.1% | 10.5% | -2.6 | 0.29 | 0.96 | +7.2 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 21.1% | 21.1% | 10.5% | -2.6 | 0.29 | 0.96 | +7.2 | +7.5 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 21.1% | 21.1% | 10.5% | -2.6 | 0.29 | 0.96 | +7.2 | +7.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 94.7% | 22.2% | 22.2% | 11.1% | -1.9 | 0.38 | 1.13 | +7.1 | +7.0 |
| `confluence_gte_70` | 5 | S_STRANGER | 26.3% | 20.0% | 20.0% | 0.0% | -2.9 | 0.05 | 0.18 | +6.8 | +6.4 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 21.1% | 25.0% | 25.0% | 0.0% | -5.7 | 0.11 | 0.33 | +5.2 | +7.9 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 78.9% | 26.7% | 26.7% | 0.0% | -1.9 | 0.41 | 1.14 | +6.7 | +7.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 21.1% | 21.1% | 10.5% | -2.6 | 0.29 | 0.96 | +7.2 | +7.5 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 21.1% | 21.1% | 10.5% | -2.6 | 0.29 | 0.96 | +7.2 | +7.5 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -0.2 | 0.00 | 0.00 | +18.5 | +2.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -0.2 | 0.00 | 0.00 | +18.5 | +2.5 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=17 Fav=23.5% Avg=-0.3; validation N=13 Fav=30.8% Avg=+1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 64 | S_STRANGER | 100.0% | 20.3% | 23.4% | 9.4% | -1.3 | 0.71 | 2.21 | +8.8 | +8.1 |
| `hunt_to_ar_ratio_le_2_0` | 32 | S_STRANGER | 50.0% | 21.9% | 25.0% | 9.4% | -1.9 | 0.54 | 1.47 | +7.8 | +7.6 |
| `hunt_to_ar_ratio_le_2_5` | 44 | S_STRANGER | 68.8% | 20.5% | 22.7% | 9.1% | -3.1 | 0.37 | 1.18 | +7.0 | +8.6 |
| `stop_hunt_le_90` | 64 | S_STRANGER | 100.0% | 20.3% | 23.4% | 9.4% | -1.3 | 0.71 | 2.21 | +8.8 | +8.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 39 | S_STRANGER | 60.9% | 25.6% | 30.8% | 15.4% | -0.1 | 0.98 | 2.05 | +10.6 | +8.9 |
| `confluence_gte_70` | 9 | S_STRANGER | 14.1% | 11.1% | 11.1% | 0.0% | -5.1 | 0.37 | 2.99 | +8.1 | +14.7 |
| `tdi_rsi_gt_signal` | 30 | S_STRANGER | 46.9% | 26.7% | 26.7% | 6.7% | +0.6 | 1.15 | 3.15 | +10.8 | +8.1 |
| `tdi_rsi_gte_50` | 37 | S_STRANGER | 57.8% | 27.0% | 29.7% | 5.4% | -0.1 | 0.98 | 2.31 | +10.8 | +9.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 60 | S_STRANGER | 93.8% | 20.0% | 23.3% | 10.0% | -1.3 | 0.71 | 2.24 | +9.0 | +8.4 |
| `feature_stale_hod_exhaustion_reject` | 64 | S_STRANGER | 100.0% | 20.3% | 23.4% | 9.4% | -1.3 | 0.71 | 2.21 | +8.8 | +8.1 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 9.4% | 16.7% | 16.7% | 0.0% | -2.1 | 0.25 | 1.25 | +4.6 | +4.8 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 4.7% | 33.3% | 33.3% | 0.0% | -0.7 | 0.67 | 1.34 | +5.2 | +5.1 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=+2.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=25.0% Avg=+0.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | +0.4 | 1.08 | 2.15 | +10.6 | +12.7 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | +0.4 | 1.08 | 2.15 | +10.6 | +12.7 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | +0.4 | 1.08 | 2.15 | +10.6 | +12.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | +0.4 | 1.08 | 2.15 | +10.6 | +12.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 28.6% | +1.2 | 1.22 | 2.43 | +13.8 | +12.1 |
| `confluence_gte_70` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 50.0% | +9.3 | 4.76 | 2.38 | +22.4 | +10.2 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 33.3% | 33.3% | 66.7% | +9.7 | 17.17 | 17.17 | +22.4 | +4.9 |
| `tdi_rsi_gte_50` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 50.0% | +5.7 | 1.94 | 0.97 | +23.4 | +10.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 20.0% | +0.4 | 1.08 | 2.15 | +10.6 | +12.7 |
| `feature_stale_hod_exhaustion_reject` | 9 | S_STRANGER | 90.0% | 22.2% | 33.3% | 22.2% | +3.1 | 2.30 | 3.83 | +11.2 | +11.0 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 50.0% | 0.0% | 20.0% | 20.0% | -5.8 | 0.07 | 0.20 | +7.7 | +15.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 50.0% | -12.1 | 0.00 | 0.00 | +14.7 | +16.3 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=+0.0; validation N=4 Fav=25.0% Avg=-2.4; out_of_sample N=1 Fav=100.0% Avg=+20.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | +0.1 | 1.03 | 2.58 | +7.6 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | +0.1 | 1.03 | 2.58 | +7.6 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | +0.1 | 1.03 | 2.58 | +7.6 | +5.2 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | +0.1 | 1.03 | 2.58 | +7.6 | +5.2 |
| `asian_range_gte_30` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 42.9% | +0.5 | 1.11 | 1.67 | +10.4 | +6.1 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | +0.1 | 1.03 | 2.58 | +7.6 | +5.2 |
| `confluence_gte_70` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 14.3% | -0.6 | 0.83 | 3.32 | +5.5 | +3.4 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 37.5% | +1.1 | 1.38 | 2.06 | +9.2 | +4.8 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -4.1 | 0.00 | 0.00 | +4.6 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 42.9% | +0.5 | 1.11 | 1.67 | +10.4 | +6.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 50.0% | +1.8 | 1.48 | 1.48 | +12.0 | +5.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | +0.1 | 1.03 | 2.58 | +7.6 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | +0.1 | 1.03 | 2.58 | +7.6 | +5.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -0.6 | 0.00 | 0.00 | +1.8 | +3.0 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+4.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=10 Fav=20.0% Avg=-3.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 20.0% | -1.1 | 0.82 | 2.12 | +13.0 | +10.1 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 95.0% | 15.8% | 21.1% | 15.8% | -3.2 | 0.51 | 1.66 | +11.7 | +10.6 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 95.0% | 15.8% | 21.1% | 15.8% | -3.2 | 0.51 | 1.66 | +11.7 | +10.6 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 20.0% | -1.1 | 0.82 | 2.12 | +13.0 | +10.1 |
| `asian_range_gte_30` | 18 | S_STRANGER | 90.0% | 16.7% | 22.2% | 16.7% | -3.3 | 0.52 | 1.55 | +12.2 | +10.9 |
| `confluence_gte_60` | 15 | S_STRANGER | 75.0% | 20.0% | 26.7% | 20.0% | -0.8 | 0.88 | 1.98 | +14.3 | +11.0 |
| `confluence_gte_70` | 4 | S_STRANGER | 20.0% | 25.0% | 25.0% | 25.0% | +1.3 | 1.16 | 3.47 | +12.9 | +11.7 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 60.0% | 16.7% | 16.7% | 8.3% | -1.1 | 0.79 | 3.56 | +12.0 | +9.1 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 65.0% | 15.4% | 15.4% | 7.7% | -3.9 | 0.50 | 2.50 | +12.3 | +13.3 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 90.0% | 16.7% | 22.2% | 16.7% | -3.3 | 0.52 | 1.55 | +12.2 | +10.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 55.0% | 18.2% | 18.2% | 9.1% | -1.1 | 0.81 | 3.23 | +12.8 | +9.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 20.0% | -1.1 | 0.82 | 2.12 | +13.0 | +10.1 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 20.0% | 25.0% | 20.0% | -1.1 | 0.82 | 2.12 | +13.0 | +10.1 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -9.3 | 0.00 | 0.00 | +5.3 | +13.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -5.0 | 0.00 | 0.00 | +7.9 | +12.0 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-8.3; validation N=5 Fav=40.0% Avg=+4.9; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -1.7 | 0.66 | 2.32 | +7.3 | +12.2 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -7.6 | 0.00 | 0.00 | +5.4 | +22.0 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -6.5 | 0.00 | 0.00 | +3.9 | +16.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -1.7 | 0.66 | 2.32 | +7.3 | +12.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -2.8 | 0.55 | 2.75 | +9.0 | +16.2 |
| `confluence_gte_70` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 0.0% | +9.5 | 15.62 | 15.62 | +20.2 | +22.7 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -3.4 | 0.50 | 2.49 | +8.4 | +18.5 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -3.4 | 0.50 | 2.49 | +8.4 | +18.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -1.7 | 0.66 | 2.32 | +7.3 | +12.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -1.7 | 0.66 | 2.32 | +7.3 | +12.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=25.0% Avg=-9.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=3 Fav=33.3% Avg=+3.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 6.7% | -1.9 | 0.60 | 2.21 | +7.1 | +8.9 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 33.3% | 20.0% | 20.0% | 0.0% | -8.0 | 0.26 | 1.03 | +4.6 | +15.9 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 46.7% | 28.6% | 28.6% | 14.3% | -4.1 | 0.52 | 1.30 | +6.7 | +12.9 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 6.7% | -1.9 | 0.60 | 2.21 | +7.1 | +8.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 6.7% | -1.9 | 0.60 | 2.21 | +7.1 | +8.9 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 6.7% | -1.9 | 0.60 | 2.21 | +7.1 | +8.9 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 53.3% | 0.0% | 0.0% | 0.0% | -8.3 | 0.00 | 0.00 | +3.9 | +12.1 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 46.7% | 0.0% | 0.0% | 0.0% | -8.9 | 0.00 | 0.00 | +4.2 | +12.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 93.3% | 21.4% | 21.4% | 7.1% | -2.0 | 0.61 | 2.02 | +6.9 | +9.0 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 6.7% | -1.9 | 0.60 | 2.21 | +7.1 | +8.9 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +6.0 | +6.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -30.3 | 0.00 | 0.00 | +2.2 | +36.0 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=16.7% Avg=-4.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=40.0% Avg=+0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -3.6 | 0.46 | 1.69 | +11.5 | +9.1 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -3.6 | 0.46 | 1.69 | +11.5 | +9.1 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -3.6 | 0.46 | 1.69 | +11.5 | +9.1 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -3.6 | 0.46 | 1.69 | +11.5 | +9.1 |
| `asian_range_gte_30` | 11 | S_STRANGER | 73.3% | 27.3% | 27.3% | 27.3% | -1.9 | 0.69 | 1.60 | +13.8 | +8.8 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -3.6 | 0.46 | 1.69 | +11.5 | +9.1 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -3.6 | 0.46 | 1.69 | +11.5 | +9.1 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 80.0% | 16.7% | 16.7% | 16.7% | -4.1 | 0.40 | 1.81 | +11.3 | +9.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 40.0% | 16.7% | 16.7% | 0.0% | -3.8 | 0.44 | 2.19 | +14.0 | +10.2 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 73.3% | 27.3% | 27.3% | 27.3% | -1.9 | 0.69 | 1.60 | +13.8 | +8.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 60.0% | 22.2% | 22.2% | 22.2% | -2.1 | 0.64 | 1.91 | +13.4 | +8.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -3.6 | 0.46 | 1.69 | +11.5 | +9.1 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 20.0% | -3.6 | 0.46 | 1.69 | +11.5 | +9.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -12.4 | 0.00 | 0.00 | +6.5 | +13.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -4.4 | 0.00 | 0.00 | +13.5 | +6.1 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+3.6; validation N=1 Fav=0.0% Avg=-0.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 5.0% | -3.7 | 0.39 | 1.48 | +7.7 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 5.0% | -3.7 | 0.39 | 1.48 | +7.7 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 5.0% | -3.7 | 0.39 | 1.48 | +7.7 | +6.6 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 5.0% | -3.7 | 0.39 | 1.48 | +7.7 | +6.6 |
| `asian_range_gte_30` | 18 | S_STRANGER | 90.0% | 22.2% | 22.2% | 5.6% | -3.3 | 0.45 | 1.45 | +8.3 | +6.0 |
| `confluence_gte_60` | 11 | S_STRANGER | 55.0% | 27.3% | 27.3% | 9.1% | +0.1 | 1.02 | 2.72 | +10.6 | +6.1 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 50.0% | 10.0% | 10.0% | 0.0% | -7.6 | 0.05 | 0.49 | +6.8 | +5.6 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 35.0% | 28.6% | 28.6% | 14.3% | +3.1 | 2.47 | 6.17 | +14.0 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 90.0% | 22.2% | 22.2% | 5.6% | -3.3 | 0.45 | 1.45 | +8.3 | +6.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 50.0% | 10.0% | 10.0% | 0.0% | -7.6 | 0.05 | 0.49 | +6.8 | +5.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 5.0% | -3.7 | 0.39 | 1.48 | +7.7 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 20.0% | 20.0% | 5.0% | -3.7 | 0.39 | 1.48 | +7.7 | +6.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+0.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 10.0% | -3.9 | 0.31 | 1.09 | +10.8 | +9.7 |
| `hunt_to_ar_ratio_le_2_0` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 0.0% | +0.4 | 1.10 | 1.10 | +12.6 | +12.7 |
| `hunt_to_ar_ratio_le_2_5` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 0.0% | +0.4 | 1.10 | 1.10 | +12.6 | +12.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 10.0% | -3.9 | 0.31 | 1.09 | +10.8 | +9.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | -5.1 | 0.24 | 0.72 | +12.5 | +6.9 |
| `confluence_gte_70` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +7.6 | +11.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 0.0% | -1.2 | 0.64 | 1.92 | +10.7 | +11.4 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 14.3% | +0.1 | 1.05 | 2.11 | +14.0 | +10.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 0.0% | -4.1 | 0.35 | 1.04 | +10.9 | +11.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 10.0% | -3.9 | 0.31 | 1.09 | +10.8 | +9.7 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -0.4 | 0.87 | 1.74 | +11.3 | +8.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | +4.7 | 999.00 | 999.00 | +20.1 | +6.1 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=37.5% Avg=-0.2; validation N=6 Fav=0.0% Avg=-7.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -3.9 | 0.33 | 1.31 | +6.4 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 93.3% | 21.4% | 21.4% | 14.3% | -3.3 | 0.38 | 1.39 | +6.7 | +8.4 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -3.9 | 0.33 | 1.31 | +6.4 | +8.8 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -3.9 | 0.33 | 1.31 | +6.4 | +8.8 |
| `asian_range_gte_30` | 13 | S_STRANGER | 86.7% | 15.4% | 15.4% | 7.7% | -4.2 | 0.24 | 1.33 | +6.4 | +8.8 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -3.9 | 0.33 | 1.31 | +6.4 | +8.8 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -3.9 | 0.33 | 1.31 | +6.4 | +8.8 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 66.7% | 10.0% | 10.0% | 10.0% | -5.7 | 0.16 | 1.45 | +5.2 | +8.5 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 80.0% | 8.3% | 8.3% | 8.3% | -5.2 | 0.15 | 1.65 | +5.2 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 80.0% | 16.7% | 16.7% | 8.3% | -3.6 | 0.29 | 1.44 | +6.7 | +8.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 46.7% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +5.2 | +7.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -3.9 | 0.33 | 1.31 | +6.4 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 13.3% | -3.9 | 0.33 | 1.31 | +6.4 | +8.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-6.6; validation N=4 Fav=50.0% Avg=-6.0; out_of_sample N=3 Fav=0.0% Avg=-3.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -4.5 | 0.20 | 0.81 | +5.3 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 80.0% | 25.0% | 25.0% | 0.0% | -5.2 | 0.22 | 0.65 | +5.9 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -4.5 | 0.20 | 0.81 | +5.3 | +3.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -4.5 | 0.20 | 0.81 | +5.3 | +3.8 |
| `asian_range_gte_30` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -6.1 | 0.13 | 0.64 | +5.6 | +5.1 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -4.5 | 0.20 | 0.81 | +5.3 | +3.8 |
| `confluence_gte_70` | 6 | S_STRANGER | 60.0% | 0.0% | 0.0% | 0.0% | -8.1 | 0.00 | 0.00 | +4.1 | +2.9 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -10.7 | 0.00 | 0.00 | +8.5 | +4.6 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -8.4 | 0.00 | 0.00 | +7.4 | +4.0 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -6.1 | 0.13 | 0.64 | +5.6 | +5.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -10.7 | 0.00 | 0.00 | +8.5 | +4.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -4.5 | 0.20 | 0.81 | +5.3 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -4.5 | 0.20 | 0.81 | +5.3 | +3.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=-4.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=16.7% Avg=-0.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 26.7% | 20.0% | -4.8 | 0.38 | 0.95 | +11.2 | +8.6 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 20.0% | 26.7% | 20.0% | -4.8 | 0.38 | 0.95 | +11.2 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 20.0% | 26.7% | 20.0% | -4.8 | 0.38 | 0.95 | +11.2 | +8.6 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 20.0% | 26.7% | 20.0% | -4.8 | 0.38 | 0.95 | +11.2 | +8.6 |
| `asian_range_gte_30` | 14 | S_STRANGER | 93.3% | 21.4% | 28.6% | 14.3% | -5.1 | 0.38 | 0.95 | +10.3 | +8.6 |
| `confluence_gte_60` | 13 | S_STRANGER | 86.7% | 23.1% | 30.8% | 23.1% | -3.8 | 0.47 | 0.94 | +11.2 | +9.5 |
| `confluence_gte_70` | 8 | S_STRANGER | 53.3% | 25.0% | 37.5% | 25.0% | -1.8 | 0.71 | 1.19 | +12.0 | +6.8 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 93.3% | 21.4% | 28.6% | 21.4% | -3.6 | 0.47 | 1.05 | +11.0 | +9.2 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 40.0% | 16.7% | 16.7% | 16.7% | -8.5 | 0.13 | 0.53 | +12.0 | +16.3 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 93.3% | 21.4% | 28.6% | 14.3% | -5.1 | 0.38 | 0.95 | +10.3 | +8.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 86.7% | 23.1% | 30.8% | 15.4% | -3.9 | 0.47 | 1.05 | +10.1 | +9.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 20.0% | 26.7% | 20.0% | -4.8 | 0.38 | 0.95 | +11.2 | +8.6 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 26.7% | 20.0% | -4.8 | 0.38 | 0.95 | +11.2 | +8.6 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +8.2 | +4.9 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=22.2% Avg=-4.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.8 | 0.29 | 0.68 | +8.8 | +10.6 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.8 | 0.29 | 0.68 | +8.8 | +10.6 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.8 | 0.29 | 0.68 | +8.8 | +10.6 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.8 | 0.29 | 0.68 | +8.8 | +10.6 |
| `asian_range_gte_30` | 9 | S_STRANGER | 90.0% | 22.2% | 33.3% | 0.0% | -4.3 | 0.34 | 0.68 | +9.5 | +11.2 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.8 | 0.29 | 0.68 | +8.8 | +10.6 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.8 | 0.29 | 0.68 | +8.8 | +10.6 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 14.3% | 28.6% | 0.0% | -6.5 | 0.15 | 0.38 | +8.5 | +13.3 |
| `tdi_rsi_gte_50` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 0.0% | -3.8 | 0.56 | 0.56 | +14.8 | +16.6 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 90.0% | 22.2% | 33.3% | 0.0% | -4.3 | 0.34 | 0.68 | +9.5 | +11.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 60.0% | 16.7% | 33.3% | 0.0% | -6.0 | 0.19 | 0.37 | +9.5 | +14.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.8 | 0.29 | 0.68 | +8.8 | +10.6 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 30.0% | 0.0% | -4.8 | 0.29 | 0.68 | +8.8 | +10.6 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -4.8 | 0.00 | 0.00 | +9.7 | +10.1 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=1 Fav=0.0% Avg=+0.0; out_of_sample N=4 Fav=50.0% Avg=+0.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 6.7% | -5.2 | 0.14 | 0.52 | +7.3 | +9.8 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 33.3% | 40.0% | 40.0% | 20.0% | +0.6 | 1.34 | 1.34 | +9.5 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 40.0% | 33.3% | 33.3% | 16.7% | +0.3 | 1.21 | 1.81 | +11.7 | +8.4 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 6.7% | -5.2 | 0.14 | 0.52 | +7.3 | +9.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 6.7% | -5.2 | 0.14 | 0.52 | +7.3 | +9.8 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 6.7% | -5.2 | 0.14 | 0.52 | +7.3 | +9.8 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +1.3 | +17.1 |
| `tdi_rsi_gte_50` | 14 | S_STRANGER | 93.3% | 21.4% | 21.4% | 7.1% | -4.4 | 0.17 | 0.57 | +7.4 | +10.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 6.7% | -5.2 | 0.14 | 0.52 | +7.3 | +9.8 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 20.0% | 20.0% | 6.7% | -5.2 | 0.14 | 0.52 | +7.3 | +9.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=+0.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -5.2 | 0.38 | 1.33 | +8.4 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -5.2 | 0.38 | 1.33 | +8.4 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -5.2 | 0.38 | 1.33 | +8.4 | +8.8 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -5.2 | 0.38 | 1.33 | +8.4 | +8.8 |
| `asian_range_gte_30` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -5.2 | 0.38 | 1.33 | +8.4 | +8.8 |
| `confluence_gte_60` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 33.3% | +0.8 | 1.30 | 5.18 | +10.7 | +8.0 |
| `confluence_gte_70` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +7.4 | +10.1 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -26.1 | 0.00 | 0.00 | +1.0 | +26.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 42.9% | -0.2 | 0.97 | 1.94 | +10.8 | +9.5 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -5.2 | 0.38 | 1.33 | +8.4 | +8.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -26.1 | 0.00 | 0.00 | +1.0 | +26.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -5.2 | 0.38 | 1.33 | +8.4 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 30.0% | -5.2 | 0.38 | 1.33 | +8.4 | +8.8 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 20.0% | 50.0% | 50.0% | 50.0% | -8.7 | 0.39 | 0.39 | +6.8 | +4.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 10.0% | 100.0% | 100.0% | 100.0% | +11.0 | 999.00 | 999.00 | +13.6 | +0.0 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=4 Fav=25.0% Avg=-9.6; out_of_sample N=2 Fav=50.0% Avg=-6.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -14.8 | 0.11 | 0.45 | +5.2 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -14.8 | 0.11 | 0.45 | +5.2 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -14.8 | 0.11 | 0.45 | +5.2 | +6.1 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -14.8 | 0.11 | 0.45 | +5.2 | +6.1 |
| `asian_range_gte_30` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 0.0% | -17.5 | 0.13 | 0.33 | +6.8 | +6.8 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -14.8 | 0.11 | 0.45 | +5.2 | +6.1 |
| `confluence_gte_70` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 0.0% | -17.4 | 0.06 | 0.45 | +4.6 | +6.6 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 60.0% | 33.3% | 33.3% | 0.0% | -8.7 | 0.26 | 0.52 | +4.9 | +6.7 |
| `tdi_rsi_gte_50` | 3 | R_REPEATER | 30.0% | 66.7% | 66.7% | 0.0% | -1.5 | 0.80 | 0.40 | +8.1 | +11.3 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 28.6% | 28.6% | 0.0% | -17.5 | 0.13 | 0.33 | +6.8 | +6.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 40.0% | 50.0% | 50.0% | 0.0% | -8.7 | 0.35 | 0.35 | +7.3 | +8.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -14.8 | 0.11 | 0.45 | +5.2 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 20.0% | 20.0% | 0.0% | -14.8 | 0.11 | 0.45 | +5.2 | +6.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=16.7% Avg=-6.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=17 Fav=29.4% Avg=-0.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 36 | S_STRANGER | 100.0% | 19.4% | 19.4% | 11.1% | -2.4 | 0.48 | 1.80 | +7.3 | +6.8 |
| `hunt_to_ar_ratio_le_2_0` | 35 | S_STRANGER | 97.2% | 20.0% | 20.0% | 11.4% | -2.4 | 0.48 | 1.73 | +7.3 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 36 | S_STRANGER | 100.0% | 19.4% | 19.4% | 11.1% | -2.4 | 0.48 | 1.80 | +7.3 | +6.8 |
| `stop_hunt_le_90` | 36 | S_STRANGER | 100.0% | 19.4% | 19.4% | 11.1% | -2.4 | 0.48 | 1.80 | +7.3 | +6.8 |
| `asian_range_gte_30` | 23 | S_STRANGER | 63.9% | 26.1% | 26.1% | 13.0% | -2.2 | 0.57 | 1.44 | +8.5 | +7.3 |
| `confluence_gte_60` | 36 | S_STRANGER | 100.0% | 19.4% | 19.4% | 11.1% | -2.4 | 0.48 | 1.80 | +7.3 | +6.8 |
| `confluence_gte_70` | 36 | S_STRANGER | 100.0% | 19.4% | 19.4% | 11.1% | -2.4 | 0.48 | 1.80 | +7.3 | +6.8 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 58.3% | 9.5% | 9.5% | 9.5% | -5.4 | 0.08 | 0.64 | +5.0 | +8.5 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 44.4% | 18.8% | 18.8% | 0.0% | -2.3 | 0.58 | 2.50 | +7.1 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 23 | S_STRANGER | 63.9% | 26.1% | 26.1% | 13.0% | -2.2 | 0.57 | 1.44 | +8.5 | +7.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 38.9% | 14.3% | 14.3% | 7.1% | -5.7 | 0.10 | 0.57 | +5.8 | +9.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 36 | S_STRANGER | 100.0% | 19.4% | 19.4% | 11.1% | -2.4 | 0.48 | 1.80 | +7.3 | +6.8 |
| `feature_stale_hod_exhaustion_reject` | 36 | S_STRANGER | 100.0% | 19.4% | 19.4% | 11.1% | -2.4 | 0.48 | 1.80 | +7.3 | +6.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.8% | 0.0% | 0.0% | 0.0% | -12.9 | 0.00 | 0.00 | +1.4 | +13.7 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=55.6% Avg=+5.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 19.4% | 19.4% | 29.0% | -1.0 | 0.70 | 2.57 | +7.7 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 100.0% | 19.4% | 19.4% | 29.0% | -1.0 | 0.70 | 2.57 | +7.7 | +4.6 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 100.0% | 19.4% | 19.4% | 29.0% | -1.0 | 0.70 | 2.57 | +7.7 | +4.6 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 19.4% | 19.4% | 29.0% | -1.0 | 0.70 | 2.57 | +7.7 | +4.6 |
| `asian_range_gte_30` | 25 | S_STRANGER | 80.6% | 24.0% | 24.0% | 36.0% | -0.4 | 0.88 | 2.36 | +8.8 | +4.3 |
| `confluence_gte_60` | 14 | S_STRANGER | 45.2% | 7.1% | 7.1% | 7.1% | -4.7 | 0.23 | 3.04 | +6.1 | +6.3 |
| `confluence_gte_70` | 8 | S_STRANGER | 25.8% | 12.5% | 12.5% | 12.5% | -6.0 | 0.30 | 2.09 | +7.0 | +6.8 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 54.8% | 11.8% | 11.8% | 23.5% | -3.5 | 0.32 | 2.05 | +6.4 | +5.4 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 41.9% | 7.7% | 7.7% | 7.7% | -3.2 | 0.20 | 2.39 | +7.1 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 80.6% | 24.0% | 24.0% | 36.0% | -0.4 | 0.88 | 2.36 | +8.8 | +4.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 11 | S_STRANGER | 35.5% | 18.2% | 18.2% | 36.4% | -3.4 | 0.42 | 1.48 | +8.0 | +5.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 19.4% | 19.4% | 29.0% | -1.0 | 0.70 | 2.57 | +7.7 | +4.6 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 19.4% | 19.4% | 29.0% | -1.0 | 0.70 | 2.57 | +7.7 | +4.6 |
| `feature_momentum_breakout_exception` | 9 | R_REPEATER | 29.0% | 55.6% | 55.6% | 66.7% | +5.2 | 6.33 | 3.80 | +11.4 | +2.7 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 6.5% | 50.0% | 50.0% | 50.0% | +3.5 | 3.12 | 3.12 | +14.0 | +2.9 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-3.0; validation N=22 Fav=22.7% Avg=-1.6; out_of_sample N=8 Fav=12.5% Avg=-13.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 31 | S_STRANGER | 100.0% | 19.4% | 32.3% | 9.7% | -4.7 | 0.26 | 0.55 | +6.2 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 100.0% | 19.4% | 32.3% | 9.7% | -4.7 | 0.26 | 0.55 | +6.2 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 31 | S_STRANGER | 100.0% | 19.4% | 32.3% | 9.7% | -4.7 | 0.26 | 0.55 | +6.2 | +6.4 |
| `stop_hunt_le_90` | 31 | S_STRANGER | 100.0% | 19.4% | 32.3% | 9.7% | -4.7 | 0.26 | 0.55 | +6.2 | +6.4 |
| `asian_range_gte_30` | 21 | S_STRANGER | 67.7% | 19.0% | 28.6% | 14.3% | -4.1 | 0.32 | 0.79 | +6.4 | +4.4 |
| `confluence_gte_60` | 26 | S_STRANGER | 83.9% | 19.2% | 34.6% | 11.5% | -3.3 | 0.36 | 0.68 | +6.1 | +4.9 |
| `confluence_gte_70` | 4 | S_STRANGER | 12.9% | 25.0% | 75.0% | 0.0% | +2.6 | 4.40 | 1.47 | +5.2 | +6.1 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 67.7% | 14.3% | 28.6% | 9.5% | -3.6 | 0.34 | 0.84 | +5.7 | +6.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 22.6% | 0.0% | 0.0% | 0.0% | -6.7 | 0.00 | 0.00 | +3.1 | +9.1 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 67.7% | 19.0% | 28.6% | 14.3% | -4.1 | 0.32 | 0.79 | +6.4 | +4.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 14 | S_STRANGER | 45.2% | 14.3% | 28.6% | 14.3% | -2.3 | 0.52 | 1.30 | +5.8 | +4.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 31 | S_STRANGER | 100.0% | 19.4% | 32.3% | 9.7% | -4.7 | 0.26 | 0.55 | +6.2 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 31 | S_STRANGER | 100.0% | 19.4% | 32.3% | 9.7% | -4.7 | 0.26 | 0.55 | +6.2 | +6.4 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+0.7; validation N=3 Fav=66.7% Avg=+14.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 26 | S_STRANGER | 100.0% | 19.2% | 23.1% | 11.5% | -0.4 | 0.88 | 2.79 | +8.2 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 34.6% | 44.4% | 44.4% | 22.2% | +4.4 | 2.57 | 2.57 | +12.1 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 34.6% | 44.4% | 44.4% | 22.2% | +4.4 | 2.57 | 2.57 | +12.1 | +8.6 |
| `stop_hunt_le_90` | 26 | S_STRANGER | 100.0% | 19.2% | 23.1% | 11.5% | -0.4 | 0.88 | 2.79 | +8.2 | +7.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 5 | R_REPEATER | 19.2% | 60.0% | 60.0% | 40.0% | +8.8 | 4.45 | 2.97 | +14.7 | +2.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 15 | S_STRANGER | 57.7% | 13.3% | 13.3% | 13.3% | -2.3 | 0.55 | 3.31 | +8.3 | +7.7 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 19.2% | 40.0% | 40.0% | 0.0% | +2.5 | 2.26 | 3.39 | +10.3 | +5.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 26 | S_STRANGER | 100.0% | 19.2% | 23.1% | 11.5% | -0.4 | 0.88 | 2.79 | +8.2 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 26 | S_STRANGER | 100.0% | 19.2% | 23.1% | 11.5% | -0.4 | 0.88 | 2.79 | +8.2 | +7.3 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.4; validation N=4 Fav=25.0% Avg=-2.5; out_of_sample N=3 Fav=33.3% Avg=+15.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | +2.6 | 1.73 | 7.50 | +9.6 | +6.8 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | +2.6 | 1.73 | 7.50 | +9.6 | +6.8 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | +2.6 | 1.73 | 7.50 | +9.6 | +6.8 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | +2.6 | 1.73 | 7.50 | +9.6 | +6.8 |
| `asian_range_gte_30` | 11 | S_STRANGER | 68.8% | 9.1% | 9.1% | 9.1% | -2.1 | 0.43 | 4.34 | +5.5 | +7.5 |
| `confluence_gte_60` | 15 | S_STRANGER | 93.8% | 20.0% | 20.0% | 20.0% | +2.8 | 1.74 | 6.97 | +10.1 | +7.0 |
| `confluence_gte_70` | 6 | S_STRANGER | 37.5% | 16.7% | 16.7% | 16.7% | -1.5 | 0.65 | 3.26 | +6.8 | +8.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 50.0% | 25.0% | 25.0% | 25.0% | +4.5 | 1.99 | 5.98 | +12.1 | +9.2 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 43.8% | 14.3% | 14.3% | 14.3% | -1.6 | 0.60 | 3.60 | +6.5 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 68.8% | 9.1% | 9.1% | 9.1% | -2.1 | 0.43 | 4.34 | +5.5 | +7.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 20.0% | -0.5 | 0.87 | 3.48 | +7.0 | +10.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | +2.6 | 1.73 | 7.50 | +9.6 | +6.8 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 18.8% | +2.6 | 1.73 | 7.50 | +9.6 | +6.8 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=14.3% Avg=-2.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=25.0% Avg=+6.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 6.2% | +2.1 | 1.67 | 7.25 | +8.5 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 6.2% | +2.1 | 1.67 | 7.25 | +8.5 | +6.7 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 6.2% | +2.1 | 1.67 | 7.25 | +8.5 | +6.7 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 6.2% | +2.1 | 1.67 | 7.25 | +8.5 | +6.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 81.2% | 15.4% | 15.4% | 0.0% | +0.1 | 1.02 | 5.60 | +6.9 | +7.7 |
| `confluence_gte_70` | 2 | R_REPEATER | 12.5% | 50.0% | 50.0% | 0.0% | +13.3 | 34.25 | 34.25 | +14.5 | +1.3 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 18.8% | 33.3% | 33.3% | 0.0% | +2.2 | 1.32 | 2.65 | +14.5 | +8.9 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 50.0% | 12.5% | 12.5% | 0.0% | -0.7 | 0.82 | 5.76 | +6.8 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 18.8% | 18.8% | 6.2% | +2.1 | 1.67 | 7.25 | +8.5 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 93.8% | 20.0% | 20.0% | 6.7% | +2.4 | 1.76 | 7.04 | +8.9 | +6.7 |
| `feature_momentum_breakout_exception` | 4 | R_REPEATER | 25.0% | 50.0% | 50.0% | 25.0% | +12.3 | 11.08 | 11.08 | +17.1 | +3.2 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 0.0% | -6.2 | 0.00 | 0.00 | +5.5 | +10.3 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=33.3% Avg=+5.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=16.7% Avg=-2.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 18.5% | 18.5% | 22.2% | -1.0 | 0.74 | 2.94 | +8.8 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 22.2% | 16.7% | 16.7% | 0.0% | -4.3 | 0.29 | 1.46 | +5.8 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 59.3% | 18.8% | 18.8% | 25.0% | -1.6 | 0.64 | 2.35 | +8.0 | +6.4 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 100.0% | 18.5% | 18.5% | 22.2% | -1.0 | 0.74 | 2.94 | +8.8 | +6.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 27 | S_STRANGER | 100.0% | 18.5% | 18.5% | 22.2% | -1.0 | 0.74 | 2.94 | +8.8 | +6.4 |
| `confluence_gte_70` | 27 | S_STRANGER | 100.0% | 18.5% | 18.5% | 22.2% | -1.0 | 0.74 | 2.94 | +8.8 | +6.4 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 77.8% | 19.0% | 19.0% | 23.8% | -0.1 | 0.98 | 3.67 | +9.5 | +5.5 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 44.4% | 25.0% | 25.0% | 25.0% | +1.5 | 1.59 | 4.24 | +11.6 | +4.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 81.5% | 18.2% | 18.2% | 22.7% | -1.1 | 0.70 | 2.80 | +8.7 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 18.5% | 18.5% | 22.2% | -1.0 | 0.74 | 2.94 | +8.8 | +6.4 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 18.5% | 20.0% | 20.0% | 20.0% | -0.6 | 0.86 | 3.44 | +9.0 | +8.3 |
| `feature_eurjpy_tdi50_reclaim` | 2 | R_REPEATER | 7.4% | 50.0% | 50.0% | 50.0% | +8.6 | 15.42 | 15.42 | +18.4 | +3.8 |

### THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+1.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 36.4% | +0.6 | 1.43 | 5.00 | +8.0 | +3.2 |
| `hunt_to_ar_ratio_le_2_0` | 2 | R_REPEATER | 18.2% | 50.0% | 50.0% | 50.0% | +3.2 | 2.70 | 2.70 | +6.4 | +4.0 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 63.6% | 28.6% | 28.6% | 42.9% | +1.7 | 2.18 | 4.36 | +7.7 | +4.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 36.4% | +0.6 | 1.43 | 5.00 | +8.0 | +3.2 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 90.9% | 20.0% | 20.0% | 30.0% | +0.7 | 1.43 | 5.00 | +7.5 | +3.0 |
| `confluence_gte_70` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 25.0% | +0.0 | 1.01 | 6.08 | +7.8 | +2.7 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +5.6 | +2.8 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 54.5% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +5.6 | +2.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 50.0% | +1.2 | 1.75 | 3.49 | +8.7 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 36.4% | +0.6 | 1.43 | 5.00 | +8.0 | +3.2 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 40.0% | +1.5 | 3.66 | 10.98 | +8.6 | +1.4 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 27.3% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +5.9 | +1.9 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+3.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=50.0% Avg=-10.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 18.2% | 27.3% | 13.6% | -0.2 | 0.97 | 2.42 | +11.5 | +9.3 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 95.5% | 19.0% | 28.6% | 14.3% | +0.1 | 1.01 | 2.37 | +11.7 | +9.0 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 100.0% | 18.2% | 27.3% | 13.6% | -0.2 | 0.97 | 2.42 | +11.5 | +9.3 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 18.2% | 27.3% | 13.6% | -0.2 | 0.97 | 2.42 | +11.5 | +9.3 |
| `asian_range_gte_30` | 19 | S_STRANGER | 86.4% | 15.8% | 21.1% | 10.5% | -0.8 | 0.87 | 3.27 | +12.1 | +10.4 |
| `confluence_gte_60` | 18 | S_STRANGER | 81.8% | 16.7% | 22.2% | 5.6% | -1.5 | 0.71 | 2.50 | +9.6 | +9.3 |
| `confluence_gte_70` | 8 | S_STRANGER | 36.4% | 12.5% | 25.0% | 12.5% | -0.9 | 0.83 | 2.50 | +9.8 | +10.4 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 59.1% | 23.1% | 23.1% | 15.4% | -1.9 | 0.74 | 2.22 | +14.1 | +12.0 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 40.9% | 33.3% | 33.3% | 11.1% | +0.5 | 1.07 | 2.14 | +18.5 | +13.3 |
| `ratio_le_2_and_asian_gte_30` | 18 | S_STRANGER | 81.8% | 16.7% | 22.2% | 11.1% | -0.5 | 0.91 | 3.20 | +12.4 | +10.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 45.5% | 20.0% | 20.0% | 10.0% | -2.2 | 0.75 | 3.00 | +16.3 | +13.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 100.0% | 18.2% | 27.3% | 13.6% | -0.2 | 0.97 | 2.42 | +11.5 | +9.3 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 18.2% | 27.3% | 13.6% | -0.2 | 0.97 | 2.42 | +11.5 | +9.3 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 18.2% | 25.0% | 50.0% | 50.0% | +11.5 | 39.17 | 19.58 | +19.9 | +2.3 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 13.6% | 33.3% | 33.3% | 33.3% | +2.0 | 1.18 | 2.36 | +22.6 | +15.0 |

### THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=40.0% Avg=+1.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 9.1% | -1.0 | 0.41 | 1.43 | +6.6 | +6.6 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 9.1% | -1.0 | 0.41 | 1.43 | +6.6 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 9.1% | -1.0 | 0.41 | 1.43 | +6.6 | +6.6 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 9.1% | -1.0 | 0.41 | 1.43 | +6.6 | +6.6 |
| `asian_range_gte_30` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 0.0% | +0.4 | 1.53 | 3.06 | +4.8 | +3.3 |
| `confluence_gte_60` | 9 | S_STRANGER | 81.8% | 22.2% | 22.2% | 11.1% | -1.0 | 0.45 | 1.13 | +6.8 | +7.5 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 45.5% | 40.0% | 40.0% | 0.0% | +1.0 | 3.12 | 3.12 | +5.2 | +2.8 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 0.0% | -0.8 | 0.00 | 0.00 | +4.5 | +3.6 |
| `ratio_le_2_and_asian_gte_30` | 6 | S_STRANGER | 54.5% | 33.3% | 33.3% | 0.0% | +0.4 | 1.53 | 3.06 | +4.8 | +3.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | R_REPEATER | 36.4% | 50.0% | 50.0% | 0.0% | +1.3 | 3.12 | 3.12 | +4.9 | +3.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 9.1% | -1.0 | 0.41 | 1.43 | +6.6 | +6.6 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 9.1% | -1.0 | 0.41 | 1.43 | +6.6 | +6.6 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 20.0% | +0.2 | 1.25 | 3.75 | +6.9 | +6.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +4.0 | +4.0 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=-0.6; validation N=5 Fav=20.0% Avg=+0.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | -8.3 | 0.20 | 0.91 | +11.1 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 10.0% | 10.0% | 0.0% | -10.4 | 0.09 | 0.85 | +8.1 | +7.7 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | -8.3 | 0.20 | 0.91 | +11.1 | +7.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | -8.3 | 0.20 | 0.91 | +11.1 | +7.0 |
| `asian_range_gte_30` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 0.0% | -12.5 | 0.10 | 0.68 | +8.3 | +8.1 |
| `confluence_gte_60` | 10 | S_STRANGER | 90.9% | 20.0% | 20.0% | 0.0% | -8.2 | 0.22 | 0.88 | +12.0 | +6.1 |
| `confluence_gte_70` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +7.3 | +6.3 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 0.0% | +0.1 | 1.04 | 3.12 | +14.0 | +7.5 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 72.7% | 25.0% | 25.0% | 0.0% | +0.1 | 1.04 | 3.12 | +14.0 | +7.5 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 72.7% | 12.5% | 12.5% | 0.0% | -12.5 | 0.10 | 0.68 | +8.3 | +8.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 45.5% | 20.0% | 20.0% | 0.0% | -1.6 | 0.57 | 2.29 | +11.3 | +9.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | -8.3 | 0.20 | 0.91 | +11.1 | +7.0 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 18.2% | 18.2% | 0.0% | -8.3 | 0.20 | 0.91 | +11.1 | +7.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+1.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 39 | S_STRANGER | 100.0% | 17.9% | 23.1% | 12.8% | -0.9 | 0.72 | 2.17 | +5.8 | +4.9 |
| `hunt_to_ar_ratio_le_2_0` | 9 | S_STRANGER | 23.1% | 0.0% | 22.2% | 0.0% | -3.1 | 0.16 | 0.57 | +2.4 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 46.2% | 11.1% | 22.2% | 16.7% | -0.9 | 0.69 | 2.06 | +4.7 | +4.7 |
| `stop_hunt_le_90` | 39 | S_STRANGER | 100.0% | 17.9% | 23.1% | 12.8% | -0.9 | 0.72 | 2.17 | +5.8 | +4.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 31 | S_STRANGER | 79.5% | 19.4% | 25.8% | 16.1% | -0.7 | 0.81 | 2.12 | +6.5 | +5.0 |
| `confluence_gte_70` | 3 | S_STRANGER | 7.7% | 0.0% | 33.3% | 0.0% | -2.2 | 0.40 | 0.80 | +2.9 | +6.9 |
| `tdi_rsi_gt_signal` | 30 | S_STRANGER | 76.9% | 13.3% | 16.7% | 3.3% | -1.3 | 0.55 | 2.55 | +5.0 | +4.9 |
| `tdi_rsi_gte_50` | 19 | S_STRANGER | 48.7% | 10.5% | 10.5% | 0.0% | -1.6 | 0.23 | 1.81 | +4.0 | +3.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 39 | S_STRANGER | 100.0% | 17.9% | 23.1% | 12.8% | -0.9 | 0.72 | 2.17 | +5.8 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 38 | S_STRANGER | 97.4% | 18.4% | 23.7% | 13.2% | -0.8 | 0.74 | 2.15 | +5.9 | +4.9 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 15.4% | 33.3% | 33.3% | 33.3% | +1.0 | 1.30 | 2.61 | +6.5 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 5.1% | 0.0% | 0.0% | 0.0% | -2.2 | 0.00 | 0.00 | +1.4 | +3.9 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=+0.0; validation N=5 Fav=0.0% Avg=-3.2; out_of_sample N=5 Fav=40.0% Avg=+10.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | +1.8 | 1.63 | 7.08 | +9.2 | +4.7 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 82.4% | 14.3% | 14.3% | 14.3% | +2.4 | 2.01 | 11.08 | +9.8 | +3.9 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | +1.8 | 1.63 | 7.08 | +9.2 | +4.7 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | +1.8 | 1.63 | 7.08 | +9.2 | +4.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | +1.8 | 1.63 | 7.08 | +9.2 | +4.7 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | +1.8 | 1.63 | 7.08 | +9.2 | +4.7 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 64.7% | 18.2% | 18.2% | 18.2% | +3.5 | 2.43 | 9.73 | +11.6 | +4.0 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 64.7% | 9.1% | 9.1% | 9.1% | +0.2 | 1.06 | 9.55 | +8.2 | +5.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | +1.8 | 1.63 | 7.08 | +9.2 | +4.7 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 17.6% | 17.6% | 11.8% | +1.8 | 1.63 | 7.08 | +9.2 | +4.7 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-1.2; validation N=9 Fav=22.2% Avg=+1.3; out_of_sample N=2 Fav=50.0% Avg=+0.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 17.6% | 29.4% | 5.9% | -1.3 | 0.60 | 1.45 | +4.7 | +4.4 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 17.6% | 29.4% | 5.9% | -1.3 | 0.60 | 1.45 | +4.7 | +4.4 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 17.6% | 29.4% | 5.9% | -1.3 | 0.60 | 1.45 | +4.7 | +4.4 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 17.6% | 29.4% | 5.9% | -1.3 | 0.60 | 1.45 | +4.7 | +4.4 |
| `asian_range_gte_30` | 16 | S_STRANGER | 94.1% | 18.8% | 31.2% | 6.2% | -1.4 | 0.61 | 1.35 | +4.8 | +4.5 |
| `confluence_gte_60` | 16 | S_STRANGER | 94.1% | 18.8% | 31.2% | 6.2% | -1.3 | 0.62 | 1.36 | +5.0 | +4.3 |
| `confluence_gte_70` | 6 | S_STRANGER | 35.3% | 16.7% | 50.0% | 0.0% | +0.2 | 1.18 | 1.18 | +4.6 | +4.6 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 76.5% | 23.1% | 30.8% | 7.7% | +0.9 | 1.51 | 3.39 | +5.2 | +4.5 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 23.5% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +2.9 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 94.1% | 18.8% | 31.2% | 6.2% | -1.4 | 0.61 | 1.35 | +4.8 | +4.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 70.6% | 25.0% | 33.3% | 8.3% | +1.0 | 1.56 | 3.12 | +5.3 | +4.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 17.6% | 29.4% | 5.9% | -1.3 | 0.60 | 1.45 | +4.7 | +4.4 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 17.6% | 29.4% | 5.9% | -1.3 | 0.60 | 1.45 | +4.7 | +4.4 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +0.5 | +5.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +0.5 | +5.0 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-1.1; validation N=3 Fav=33.3% Avg=+7.7; out_of_sample N=2 Fav=50.0% Avg=-4.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 17.1% | 20.0% | 20.0% | -4.9 | 0.39 | 1.35 | +8.7 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 34 | S_STRANGER | 97.1% | 14.7% | 17.6% | 20.6% | -5.2 | 0.38 | 1.53 | +8.7 | +8.4 |
| `hunt_to_ar_ratio_le_2_5` | 35 | S_STRANGER | 100.0% | 17.1% | 20.0% | 20.0% | -4.9 | 0.39 | 1.35 | +8.7 | +8.2 |
| `stop_hunt_le_90` | 35 | S_STRANGER | 100.0% | 17.1% | 20.0% | 20.0% | -4.9 | 0.39 | 1.35 | +8.7 | +8.2 |
| `asian_range_gte_30` | 29 | S_STRANGER | 82.9% | 20.7% | 24.1% | 24.1% | -4.8 | 0.45 | 1.15 | +9.2 | +7.8 |
| `confluence_gte_60` | 27 | S_STRANGER | 77.1% | 14.8% | 18.5% | 18.5% | -3.8 | 0.48 | 1.81 | +8.8 | +7.2 |
| `confluence_gte_70` | 7 | S_STRANGER | 20.0% | 28.6% | 28.6% | 42.9% | +1.6 | 1.39 | 2.08 | +12.7 | +9.3 |
| `tdi_rsi_gt_signal` | 26 | S_STRANGER | 74.3% | 23.1% | 23.1% | 26.9% | -2.6 | 0.60 | 1.61 | +10.0 | +8.2 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 45.7% | 37.5% | 37.5% | 25.0% | -0.0 | 0.99 | 1.49 | +12.5 | +11.8 |
| `ratio_le_2_and_asian_gte_30` | 28 | S_STRANGER | 80.0% | 17.9% | 21.4% | 25.0% | -5.1 | 0.43 | 1.29 | +9.2 | +8.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 21 | S_STRANGER | 60.0% | 23.8% | 23.8% | 33.3% | -2.1 | 0.69 | 1.65 | +11.4 | +8.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 35 | S_STRANGER | 100.0% | 17.1% | 20.0% | 20.0% | -4.9 | 0.39 | 1.35 | +8.7 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 35 | S_STRANGER | 100.0% | 17.1% | 20.0% | 20.0% | -4.9 | 0.39 | 1.35 | +8.7 | +8.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 2.9% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +9.2 | +3.9 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=-1.0; validation N=16 Fav=18.8% Avg=-0.2; out_of_sample N=9 Fav=22.2% Avg=-0.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 47 | S_STRANGER | 100.0% | 17.0% | 21.3% | 6.4% | -3.3 | 0.45 | 1.61 | +7.9 | +9.3 |
| `hunt_to_ar_ratio_le_2_0` | 46 | S_STRANGER | 97.9% | 17.4% | 21.7% | 6.5% | -3.3 | 0.45 | 1.57 | +8.0 | +9.3 |
| `hunt_to_ar_ratio_le_2_5` | 47 | S_STRANGER | 100.0% | 17.0% | 21.3% | 6.4% | -3.3 | 0.45 | 1.61 | +7.9 | +9.3 |
| `stop_hunt_le_90` | 47 | S_STRANGER | 100.0% | 17.0% | 21.3% | 6.4% | -3.3 | 0.45 | 1.61 | +7.9 | +9.3 |
| `asian_range_gte_30` | 33 | S_STRANGER | 70.2% | 15.2% | 18.2% | 6.1% | -4.0 | 0.40 | 1.79 | +8.3 | +9.8 |
| `confluence_gte_60` | 41 | S_STRANGER | 87.2% | 14.6% | 19.5% | 7.3% | -3.7 | 0.42 | 1.69 | +7.9 | +10.1 |
| `confluence_gte_70` | 10 | S_STRANGER | 21.3% | 20.0% | 20.0% | 10.0% | -3.8 | 0.40 | 1.40 | +7.7 | +8.9 |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 48.9% | 17.4% | 17.4% | 4.3% | -3.1 | 0.49 | 2.33 | +7.7 | +8.5 |
| `tdi_rsi_gte_50` | 28 | S_STRANGER | 59.6% | 21.4% | 21.4% | 3.6% | -0.3 | 0.92 | 3.37 | +8.9 | +6.1 |
| `ratio_le_2_and_asian_gte_30` | 33 | S_STRANGER | 70.2% | 15.2% | 18.2% | 6.1% | -4.0 | 0.40 | 1.79 | +8.3 | +9.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 15 | S_STRANGER | 31.9% | 13.3% | 13.3% | 6.7% | -5.0 | 0.38 | 2.46 | +8.2 | +9.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 47 | S_STRANGER | 100.0% | 17.0% | 21.3% | 6.4% | -3.3 | 0.45 | 1.61 | +7.9 | +9.3 |
| `feature_stale_hod_exhaustion_reject` | 47 | S_STRANGER | 100.0% | 17.0% | 21.3% | 6.4% | -3.3 | 0.45 | 1.61 | +7.9 | +9.3 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 8.5% | 25.0% | 25.0% | 25.0% | +5.0 | 3.97 | 11.91 | +11.3 | +3.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 4.3% | 0.0% | 0.0% | 0.0% | -2.7 | 0.00 | 0.00 | +7.2 | +4.5 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=12.5% Avg=-1.8; validation N=6 Fav=33.3% Avg=+2.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 11.1% | -0.7 | 0.81 | 4.06 | +7.7 | +5.9 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 11.1% | -0.7 | 0.81 | 4.06 | +7.7 | +5.9 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 11.1% | -0.7 | 0.81 | 4.06 | +7.7 | +5.9 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 11.1% | -0.7 | 0.81 | 4.06 | +7.7 | +5.9 |
| `asian_range_gte_30` | 17 | S_STRANGER | 94.4% | 11.8% | 11.8% | 5.9% | -1.6 | 0.61 | 4.60 | +7.2 | +6.1 |
| `confluence_gte_60` | 14 | S_STRANGER | 77.8% | 21.4% | 21.4% | 14.3% | +0.2 | 1.05 | 3.86 | +8.6 | +5.6 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -6.5 | 0.00 | 0.00 | +9.5 | +8.7 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 38.9% | 0.0% | 0.0% | 0.0% | -2.9 | 0.00 | 0.00 | +2.8 | +4.8 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 83.3% | 13.3% | 13.3% | 6.7% | -1.4 | 0.68 | 4.40 | +7.7 | +6.4 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 94.4% | 11.8% | 11.8% | 5.9% | -1.6 | 0.61 | 4.60 | +7.2 | +6.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 38.9% | 0.0% | 0.0% | 0.0% | -2.9 | 0.00 | 0.00 | +2.8 | +4.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 11.1% | -0.7 | 0.81 | 4.06 | +7.7 | +5.9 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 11.1% | -0.7 | 0.81 | 4.06 | +7.7 | +5.9 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +1.0 | +7.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +1.0 | +7.5 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-1.3; validation N=18 Fav=22.2% Avg=-1.6; out_of_sample N=2 Fav=0.0% Avg=-2.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.58 | 2.89 | +6.3 | +7.7 |
| `hunt_to_ar_ratio_le_2_0` | 2 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +5.6 | +7.8 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 29.2% | 14.3% | 14.3% | 0.0% | -3.1 | 0.16 | 0.94 | +7.1 | +7.4 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.58 | 2.89 | +6.3 | +7.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.58 | 2.89 | +6.3 | +7.7 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.58 | 2.89 | +6.3 | +7.7 |
| `tdi_rsi_gt_signal` | 14 | S_STRANGER | 58.3% | 14.3% | 14.3% | 0.0% | -1.7 | 0.65 | 3.91 | +6.5 | +8.7 |
| `tdi_rsi_gte_50` | 20 | S_STRANGER | 83.3% | 15.0% | 15.0% | 0.0% | -1.8 | 0.59 | 3.33 | +5.9 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 91.7% | 18.2% | 18.2% | 0.0% | -1.7 | 0.60 | 2.70 | +6.6 | +8.1 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -1.7 | 0.58 | 2.89 | +6.3 | +7.7 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +3.4 | +2.4 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +3.4 | +2.4 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-5.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=40.0% Avg=-0.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -3.3 | 0.21 | 0.95 | +6.6 | +7.5 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -3.3 | 0.21 | 0.95 | +6.6 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -3.3 | 0.21 | 0.95 | +6.6 | +7.5 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -3.3 | 0.21 | 0.95 | +6.6 | +7.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -3.3 | 0.21 | 0.95 | +6.6 | +7.5 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -3.3 | 0.21 | 0.95 | +6.6 | +7.5 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 33.3% | -1.5 | 0.53 | 1.07 | +4.3 | +6.0 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 66.7% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +6.8 | +10.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 16.7% | -3.3 | 0.21 | 0.95 | +6.6 | +7.5 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 18.2% | -3.5 | 0.21 | 0.86 | +6.6 | +7.3 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -7.4 | 0.00 | 0.00 | +15.0 | +8.3 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +8.5 | +9.9 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-7.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=50.0% Avg=-0.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -6.2 | 0.08 | 0.42 | +5.9 | +8.8 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 0.0% | -6.3 | 0.15 | 0.30 | +4.6 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 66.7% | 25.0% | 25.0% | 0.0% | -7.4 | 0.10 | 0.31 | +3.8 | +6.4 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -6.2 | 0.08 | 0.42 | +5.9 | +8.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -6.2 | 0.08 | 0.42 | +5.9 | +8.8 |
| `confluence_gte_70` | 11 | S_STRANGER | 91.7% | 18.2% | 18.2% | 0.0% | -6.4 | 0.09 | 0.40 | +6.4 | +9.1 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +0.1 | +5.9 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 0.0% | -2.7 | 0.30 | 0.59 | +5.2 | +8.0 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -6.2 | 0.08 | 0.42 | +5.9 | +8.8 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 0.0% | -6.2 | 0.08 | 0.42 | +5.9 | +8.8 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -9.3 | 0.00 | 0.00 | +4.2 | +13.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -9.3 | 0.00 | 0.00 | +4.2 | +13.7 |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=33.3% Avg=+1.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -6.3 | 0.36 | 1.78 | +13.3 | +14.8 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -6.3 | 0.36 | 1.78 | +13.3 | +14.8 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -6.3 | 0.36 | 1.78 | +13.3 | +14.8 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -6.3 | 0.36 | 1.78 | +13.3 | +14.8 |
| `asian_range_gte_30` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 11.1% | -3.0 | 0.61 | 2.13 | +16.8 | +14.2 |
| `confluence_gte_60` | 5 | S_STRANGER | 41.7% | 0.0% | 0.0% | 0.0% | -17.5 | 0.00 | 0.00 | +7.8 | +21.4 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 11.1% | -4.6 | 0.50 | 1.76 | +14.0 | +13.4 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 41.7% | 20.0% | 20.0% | 0.0% | -6.4 | 0.45 | 1.81 | +15.1 | +14.5 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 75.0% | 22.2% | 22.2% | 11.1% | -3.0 | 0.61 | 2.13 | +16.8 | +14.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 50.0% | 33.3% | 33.3% | 16.7% | +1.2 | 1.21 | 2.42 | +19.6 | +11.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -6.3 | 0.36 | 1.78 | +13.3 | +14.8 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 16.7% | 16.7% | 8.3% | -6.3 | 0.36 | 1.78 | +13.3 | +14.8 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 33.3% | 25.0% | 25.0% | 25.0% | -0.4 | 0.91 | 2.73 | +14.7 | +11.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -27.1 | 0.00 | 0.00 | +0.8 | +27.8 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+1.2; validation N=3 Fav=33.3% Avg=+3.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 11.1% | -10.3 | 0.21 | 1.06 | +7.6 | +5.0 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 44.4% | 25.0% | 25.0% | 12.5% | -0.1 | 0.98 | 2.93 | +8.4 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 61.1% | 18.2% | 18.2% | 9.1% | -9.5 | 0.23 | 1.03 | +7.5 | +6.5 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 11.1% | -10.3 | 0.21 | 1.06 | +7.6 | +5.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 66.7% | 25.0% | 25.0% | 16.7% | -2.0 | 0.68 | 2.03 | +8.4 | +5.6 |
| `confluence_gte_70` | 3 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -3.3 | 0.00 | 0.00 | +1.5 | +5.1 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 88.9% | 18.8% | 18.8% | 12.5% | -2.1 | 0.59 | 2.57 | +7.9 | +5.3 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 27.8% | 40.0% | 40.0% | 20.0% | +2.3 | 1.60 | 2.40 | +13.4 | +7.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 11.1% | -10.3 | 0.21 | 1.06 | +7.6 | +5.0 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 16.7% | 16.7% | 11.1% | -10.3 | 0.21 | 1.06 | +7.6 | +5.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=50.0% Avg=+6.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=12.5% Avg=-2.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 15.8% | -1.1 | 0.73 | 2.73 | +8.0 | +6.9 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 15.8% | -1.1 | 0.73 | 2.73 | +8.0 | +6.9 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 15.8% | -1.1 | 0.73 | 2.73 | +8.0 | +6.9 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 15.8% | -1.1 | 0.73 | 2.73 | +8.0 | +6.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 15.8% | -1.1 | 0.73 | 2.73 | +8.0 | +6.9 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 15.8% | -1.1 | 0.73 | 2.73 | +8.0 | +6.9 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 52.6% | 20.0% | 20.0% | 20.0% | -0.6 | 0.86 | 3.43 | +8.3 | +8.4 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 57.9% | 9.1% | 9.1% | 9.1% | -1.8 | 0.54 | 5.43 | +8.5 | +8.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 15.8% | -1.1 | 0.73 | 2.73 | +8.0 | +6.9 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 15.8% | -1.1 | 0.73 | 2.73 | +8.0 | +6.9 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -5.4 | 0.00 | 0.00 | +5.1 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-0.8; validation N=10 Fav=20.0% Avg=-3.1; out_of_sample N=3 Fav=33.3% Avg=+0.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -2.4 | 0.40 | 1.51 | +6.6 | +7.5 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -2.4 | 0.40 | 1.51 | +6.6 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -2.4 | 0.40 | 1.51 | +6.6 | +7.5 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -2.4 | 0.40 | 1.51 | +6.6 | +7.5 |
| `asian_range_gte_30` | 16 | S_STRANGER | 84.2% | 18.8% | 18.8% | 12.5% | -2.7 | 0.41 | 1.78 | +6.0 | +8.3 |
| `confluence_gte_60` | 14 | S_STRANGER | 73.7% | 21.4% | 21.4% | 14.3% | -2.2 | 0.49 | 1.81 | +7.2 | +7.7 |
| `confluence_gte_70` | 2 | S_STRANGER | 10.5% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +3.2 | +3.3 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 21.1% | 0.0% | 0.0% | 0.0% | -2.3 | 0.00 | 0.00 | +4.2 | +6.3 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 78.9% | 6.7% | 6.7% | 0.0% | -4.3 | 0.10 | 1.43 | +5.4 | +8.6 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 84.2% | 18.8% | 18.8% | 12.5% | -2.7 | 0.41 | 1.78 | +6.0 | +8.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 21.1% | 0.0% | 0.0% | 0.0% | -2.3 | 0.00 | 0.00 | +4.2 | +6.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -2.4 | 0.40 | 1.51 | +6.6 | +7.5 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 15.8% | 21.1% | 10.5% | -2.4 | 0.40 | 1.51 | +6.6 | +7.5 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +1.0 | +6.6 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.3% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +1.0 | +6.6 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=23.1% Avg=+1.4; validation N=9 Fav=22.2% Avg=-5.6; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 32 | S_STRANGER | 100.0% | 15.6% | 15.6% | 18.8% | -3.2 | 0.49 | 2.53 | +7.5 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 31 | S_STRANGER | 96.9% | 16.1% | 16.1% | 19.4% | -3.2 | 0.49 | 2.47 | +7.4 | +7.3 |
| `hunt_to_ar_ratio_le_2_5` | 32 | S_STRANGER | 100.0% | 15.6% | 15.6% | 18.8% | -3.2 | 0.49 | 2.53 | +7.5 | +7.2 |
| `stop_hunt_le_90` | 32 | S_STRANGER | 100.0% | 15.6% | 15.6% | 18.8% | -3.2 | 0.49 | 2.53 | +7.5 | +7.2 |
| `asian_range_gte_30` | 29 | S_STRANGER | 90.6% | 17.2% | 17.2% | 20.7% | -2.9 | 0.53 | 2.43 | +7.7 | +7.3 |
| `confluence_gte_60` | 22 | S_STRANGER | 68.8% | 22.7% | 22.7% | 22.7% | -1.4 | 0.75 | 2.55 | +8.6 | +6.2 |
| `confluence_gte_70` | 1 | S_STRANGER | 3.1% | 0.0% | 0.0% | 0.0% | -0.4 | 0.00 | 0.00 | +9.7 | +1.3 |
| `tdi_rsi_gt_signal` | 27 | S_STRANGER | 84.4% | 14.8% | 14.8% | 18.5% | -3.2 | 0.50 | 2.73 | +7.7 | +7.0 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -4.7 | 0.00 | 0.00 | +4.5 | +8.3 |
| `ratio_le_2_and_asian_gte_30` | 29 | S_STRANGER | 90.6% | 17.2% | 17.2% | 20.7% | -2.9 | 0.53 | 2.43 | +7.7 | +7.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 25 | S_STRANGER | 78.1% | 16.0% | 16.0% | 20.0% | -3.1 | 0.52 | 2.58 | +7.8 | +7.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 32 | S_STRANGER | 100.0% | 15.6% | 15.6% | 18.8% | -3.2 | 0.49 | 2.53 | +7.5 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 32 | S_STRANGER | 100.0% | 15.6% | 15.6% | 18.8% | -3.2 | 0.49 | 2.53 | +7.5 | +7.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=20.0% Avg=+8.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 53.8% | +5.8 | 2.75 | 5.50 | +18.7 | +7.3 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 53.8% | +5.8 | 2.75 | 5.50 | +18.7 | +7.3 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 53.8% | +5.8 | 2.75 | 5.50 | +18.7 | +7.3 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 53.8% | +5.8 | 2.75 | 5.50 | +18.7 | +7.3 |
| `asian_range_gte_30` | 8 | S_STRANGER | 61.5% | 12.5% | 25.0% | 50.0% | +6.9 | 3.05 | 6.10 | +21.0 | +6.8 |
| `confluence_gte_60` | 12 | S_STRANGER | 92.3% | 16.7% | 25.0% | 58.3% | +6.5 | 2.94 | 4.89 | +19.3 | +6.5 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -13.4 | 0.00 | 0.00 | +4.0 | +14.9 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 76.9% | 20.0% | 30.0% | 60.0% | +8.6 | 3.65 | 4.87 | +22.6 | +8.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 46.2% | 16.7% | 16.7% | 50.0% | +3.2 | 1.71 | 5.14 | +19.5 | +9.1 |
| `ratio_le_2_and_asian_gte_30` | 8 | S_STRANGER | 61.5% | 12.5% | 25.0% | 50.0% | +6.9 | 3.05 | 6.10 | +21.0 | +6.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 46.2% | 16.7% | 33.3% | 66.7% | +10.9 | 5.05 | 5.05 | +26.0 | +7.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 53.8% | +5.8 | 2.75 | 5.50 | +18.7 | +7.3 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 53.8% | +5.8 | 2.75 | 5.50 | +18.7 | +7.3 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 30.8% | 25.0% | 25.0% | 50.0% | +3.8 | 1.73 | 3.47 | +15.6 | +5.6 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 33.3% | -5.4 | 0.00 | 0.00 | +9.5 | +11.6 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=50.0% Avg=+10.6; validation N=3 Fav=0.0% Avg=-2.3; out_of_sample N=3 Fav=33.3% Avg=+0.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 0.0% | -1.1 | 0.78 | 2.59 | +6.8 | +9.3 |
| `hunt_to_ar_ratio_le_2_0` | 3 | R_REPEATER | 23.1% | 66.7% | 66.7% | 0.0% | +11.1 | 3.27 | 1.63 | +18.6 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 8 | S_STRANGER | 61.5% | 25.0% | 25.0% | 0.0% | +1.9 | 1.48 | 4.43 | +8.9 | +8.5 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 0.0% | -1.1 | 0.78 | 2.59 | +6.8 | +9.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 0.0% | -1.1 | 0.78 | 2.59 | +6.8 | +9.3 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 0.0% | -1.1 | 0.78 | 2.59 | +6.8 | +9.3 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 53.8% | 14.3% | 14.3% | 0.0% | +0.7 | 1.19 | 7.16 | +8.2 | +10.4 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 76.9% | 20.0% | 20.0% | 0.0% | -0.4 | 0.93 | 3.73 | +8.4 | +10.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 92.3% | 16.7% | 25.0% | 0.0% | -0.3 | 0.93 | 2.79 | +7.4 | +9.1 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 0.0% | -1.1 | 0.78 | 2.59 | +6.8 | +9.3 |
| `feature_momentum_breakout_exception` | 2 | R_REPEATER | 15.4% | 50.0% | 50.0% | 0.0% | +10.6 | 3.09 | 3.09 | +17.6 | +6.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 7.7% | 100.0% | 100.0% | 0.0% | +31.5 | 999.00 | 999.00 | +34.9 | +1.7 |

### THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=25.0% Avg=+0.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -3.1 | 0.54 | 2.95 | +14.5 | +12.7 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -16.0 | 0.00 | 0.00 | +13.1 | +22.3 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -3.1 | 0.54 | 2.95 | +14.5 | +12.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 11 | S_STRANGER | 84.6% | 18.2% | 18.2% | 9.1% | -1.4 | 0.75 | 3.38 | +16.5 | +12.2 |
| `confluence_gte_70` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 0.0% | -1.1 | 0.63 | 1.25 | +20.5 | +6.4 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 38.5% | 20.0% | 20.0% | 0.0% | -2.2 | 0.33 | 1.32 | +13.6 | +8.4 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 61.5% | 12.5% | 12.5% | 0.0% | -2.5 | 0.21 | 1.50 | +13.8 | +10.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 8 | S_STRANGER | 61.5% | 25.0% | 25.0% | 12.5% | +0.1 | 1.01 | 3.04 | +20.3 | +11.4 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -3.1 | 0.54 | 2.95 | +14.5 | +12.7 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -10.4 | 0.00 | 0.00 | +5.0 | +18.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +6.7 | +11.8 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=+1.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=25.0% Avg=-9.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -5.8 | 0.18 | 0.81 | +10.5 | +7.5 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -5.8 | 0.18 | 0.81 | +10.5 | +7.5 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -5.8 | 0.18 | 0.81 | +10.5 | +7.5 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -5.8 | 0.18 | 0.81 | +10.5 | +7.5 |
| `asian_range_gte_30` | 9 | S_STRANGER | 69.2% | 11.1% | 11.1% | 11.1% | -7.4 | 0.07 | 0.51 | +9.6 | +9.5 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -5.8 | 0.18 | 0.81 | +10.5 | +7.5 |
| `confluence_gte_70` | 8 | S_STRANGER | 61.5% | 25.0% | 25.0% | 37.5% | -3.8 | 0.35 | 0.71 | +12.6 | +6.3 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 84.6% | 18.2% | 18.2% | 27.3% | -3.3 | 0.31 | 1.09 | +11.3 | +8.6 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +7.4 | +11.6 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 69.2% | 11.1% | 11.1% | 11.1% | -7.4 | 0.07 | 0.51 | +9.6 | +9.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 53.8% | 14.3% | 14.3% | 14.3% | -4.0 | 0.16 | 0.80 | +10.7 | +11.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -5.8 | 0.18 | 0.81 | +10.5 | +7.5 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 23.1% | -5.8 | 0.18 | 0.81 | +10.5 | +7.5 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 100.0% | +0.0 | 0.00 | 0.00 | +16.5 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_NEUTRAL|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NEUTRAL|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=5 Fav=40.0% Avg=+3.0; out_of_sample N=1 Fav=0.0% Avg=-1.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 0.0% | -7.2 | 0.28 | 0.92 | +9.1 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 30.8% | 0.0% | 25.0% | 0.0% | -22.1 | 0.06 | 0.18 | +5.5 | +6.8 |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 30.8% | 0.0% | 25.0% | 0.0% | -22.1 | 0.06 | 0.18 | +5.5 | +6.8 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 0.0% | -7.2 | 0.28 | 0.92 | +9.1 | +5.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 12 | S_STRANGER | 92.3% | 16.7% | 25.0% | 0.0% | -5.9 | 0.33 | 1.00 | +9.7 | +5.3 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -10.7 | 0.00 | 0.00 | +8.3 | +2.1 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 53.8% | 28.6% | 42.9% | 0.0% | +2.8 | 2.21 | 2.95 | +11.6 | +4.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 46.2% | 33.3% | 33.3% | 0.0% | +2.3 | 1.86 | 3.71 | +12.2 | +4.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 0.0% | -7.2 | 0.28 | 0.92 | +9.1 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 23.1% | 0.0% | -7.2 | 0.28 | 0.92 | +9.1 | +5.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=0.0% Avg=-15.2; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=28.6% Avg=-3.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -9.0 | 0.17 | 0.95 | +5.1 | +14.4 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -9.0 | 0.17 | 0.95 | +5.1 | +14.4 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -9.0 | 0.17 | 0.95 | +5.1 | +14.4 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -9.0 | 0.17 | 0.95 | +5.1 | +14.4 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -9.0 | 0.17 | 0.95 | +5.1 | +14.4 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -9.0 | 0.17 | 0.95 | +5.1 | +14.4 |
| `confluence_gte_70` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -18.9 | 0.00 | 0.00 | +3.5 | +20.7 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -9.0 | 0.17 | 0.95 | +5.1 | +14.4 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 61.5% | 12.5% | 12.5% | 0.0% | -14.3 | 0.02 | 0.16 | +3.6 | +17.7 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -9.0 | 0.17 | 0.95 | +5.1 | +14.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -9.0 | 0.17 | 0.95 | +5.1 | +14.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -9.0 | 0.17 | 0.95 | +5.1 | +14.4 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 15.4% | 15.4% | 7.7% | -9.0 | 0.17 | 0.95 | +5.1 | +14.4 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -11.9 | 0.00 | 0.00 | +1.4 | +12.9 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=11 Fav=18.2% Avg=+1.6; validation N=9 Fav=11.1% Avg=-2.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 15.0% | 20.0% | 15.0% | -0.1 | 0.96 | 3.62 | +10.1 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 40.0% | 0.0% | 0.0% | 12.5% | -2.7 | 0.00 | 0.00 | +9.3 | +6.6 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 65.0% | 0.0% | 7.7% | 15.4% | -0.9 | 0.65 | 7.17 | +10.1 | +6.8 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 15.0% | 20.0% | 15.0% | -0.1 | 0.96 | 3.62 | +10.1 | +7.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 20 | S_STRANGER | 100.0% | 15.0% | 20.0% | 15.0% | -0.1 | 0.96 | 3.62 | +10.1 | +7.4 |
| `confluence_gte_70` | 20 | S_STRANGER | 100.0% | 15.0% | 20.0% | 15.0% | -0.1 | 0.96 | 3.62 | +10.1 | +7.4 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +4.6 | +5.4 |
| `tdi_rsi_gte_50` | 15 | S_STRANGER | 75.0% | 0.0% | 6.7% | 13.3% | -1.9 | 0.43 | 5.62 | +9.5 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 15.0% | 20.0% | 15.0% | -0.1 | 0.96 | 3.62 | +10.1 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 15.0% | 20.0% | 15.0% | -0.1 | 0.96 | 3.62 | +10.1 | +7.4 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +6.5 | +3.3 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +6.5 | +3.3 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-2.9; validation N=5 Fav=40.0% Avg=+1.8; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.9 | 0.67 | 3.36 | +5.5 | +4.8 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.9 | 0.67 | 3.36 | +5.5 | +4.8 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.9 | 0.67 | 3.36 | +5.5 | +4.8 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.9 | 0.67 | 3.36 | +5.5 | +4.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 16 | S_STRANGER | 80.0% | 12.5% | 12.5% | 18.8% | -1.0 | 0.67 | 4.01 | +6.1 | +5.0 |
| `confluence_gte_70` | 5 | S_STRANGER | 25.0% | 0.0% | 0.0% | 40.0% | -3.2 | 0.00 | 0.00 | +5.4 | +4.6 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 45.0% | 22.2% | 22.2% | 0.0% | -0.3 | 0.84 | 2.93 | +3.3 | +3.6 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 45.0% | 11.1% | 11.1% | 0.0% | -1.4 | 0.49 | 3.93 | +2.8 | +4.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.9 | 0.67 | 3.36 | +5.5 | +4.8 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 15.0% | 15.0% | 15.0% | -0.9 | 0.67 | 3.36 | +5.5 | +4.8 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 20.0% | 0.0% | 0.0% | 25.0% | -1.4 | 0.00 | 0.00 | +5.1 | +2.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +1.3 | +3.3 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=-1.1; validation N=9 Fav=22.2% Avg=+0.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 20 | S_STRANGER | 100.0% | 15.0% | 25.0% | 10.0% | -3.5 | 0.29 | 0.82 | +5.4 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 20 | S_STRANGER | 100.0% | 15.0% | 25.0% | 10.0% | -3.5 | 0.29 | 0.82 | +5.4 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 20 | S_STRANGER | 100.0% | 15.0% | 25.0% | 10.0% | -3.5 | 0.29 | 0.82 | +5.4 | +5.5 |
| `stop_hunt_le_90` | 20 | S_STRANGER | 100.0% | 15.0% | 25.0% | 10.0% | -3.5 | 0.29 | 0.82 | +5.4 | +5.5 |
| `asian_range_gte_30` | 19 | S_STRANGER | 95.0% | 10.5% | 21.1% | 5.3% | -3.9 | 0.24 | 0.84 | +5.0 | +5.6 |
| `confluence_gte_60` | 12 | S_STRANGER | 60.0% | 25.0% | 33.3% | 16.7% | -0.2 | 0.91 | 1.58 | +6.2 | +4.9 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -0.2 | 0.00 | 0.00 | +4.5 | +6.8 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 65.0% | 23.1% | 38.5% | 7.7% | -2.6 | 0.46 | 0.74 | +6.4 | +6.2 |
| `tdi_rsi_gte_50` | 1 | S_STRANGER | 5.0% | 0.0% | 0.0% | 0.0% | -0.2 | 0.00 | 0.00 | +4.5 | +6.8 |
| `ratio_le_2_and_asian_gte_30` | 19 | S_STRANGER | 95.0% | 10.5% | 21.1% | 5.3% | -3.9 | 0.24 | 0.84 | +5.0 | +5.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 60.0% | 16.7% | 33.3% | 0.0% | -3.2 | 0.38 | 0.76 | +5.9 | +6.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 20 | S_STRANGER | 100.0% | 15.0% | 25.0% | 10.0% | -3.5 | 0.29 | 0.82 | +5.4 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 20 | S_STRANGER | 100.0% | 15.0% | 25.0% | 10.0% | -3.5 | 0.29 | 0.82 | +5.4 | +5.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=+5.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=25.0% Avg=+0.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -0.5 | 0.85 | 4.26 | +9.2 | +7.9 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -0.5 | 0.85 | 4.26 | +9.2 | +7.9 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -0.5 | 0.85 | 4.26 | +9.2 | +7.9 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -0.5 | 0.85 | 4.26 | +9.2 | +7.9 |
| `asian_range_gte_30` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 22.2% | +2.0 | 1.81 | 5.44 | +11.7 | +7.8 |
| `confluence_gte_60` | 8 | S_STRANGER | 57.1% | 25.0% | 25.0% | 25.0% | +3.1 | 2.60 | 6.51 | +12.8 | +7.4 |
| `confluence_gte_70` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 50.0% | +5.8 | 4.85 | 9.70 | +12.4 | +5.2 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 20.0% | +1.8 | 1.44 | 5.76 | +9.7 | +10.4 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 57.1% | 12.5% | 12.5% | 12.5% | +0.1 | 1.02 | 6.13 | +9.5 | +8.0 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 64.3% | 22.2% | 22.2% | 22.2% | +2.0 | 1.81 | 5.44 | +11.7 | +7.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 25.0% | +4.3 | 2.49 | 7.46 | +10.1 | +9.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -0.5 | 0.85 | 4.26 | +9.2 | +7.9 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -0.5 | 0.85 | 4.26 | +9.2 | +7.9 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -7.0 | 0.00 | 0.00 | +2.5 | +7.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +3.7 | +2.8 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=7 Fav=28.6% Avg=+5.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -0.6 | 0.92 | 5.05 | +16.1 | +8.3 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -0.6 | 0.92 | 5.05 | +16.1 | +8.3 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -0.6 | 0.92 | 5.05 | +16.1 | +8.3 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -0.6 | 0.92 | 5.05 | +16.1 | +8.3 |
| `asian_range_gte_30` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 20.0% | +2.2 | 1.28 | 5.11 | +19.2 | +9.8 |
| `confluence_gte_60` | 12 | S_STRANGER | 85.7% | 16.7% | 16.7% | 25.0% | +1.1 | 1.15 | 5.16 | +18.0 | +8.8 |
| `confluence_gte_70` | 4 | S_STRANGER | 28.6% | 25.0% | 25.0% | 50.0% | +11.2 | 4.69 | 9.38 | +36.7 | +3.9 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 78.6% | 18.2% | 18.2% | 27.3% | +1.0 | 1.12 | 4.48 | +19.8 | +9.2 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 33.3% | +1.0 | 1.08 | 2.15 | +16.2 | +16.0 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 20.0% | +2.2 | 1.28 | 5.11 | +19.2 | +9.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 50.0% | 28.6% | 28.6% | 28.6% | +5.9 | 1.71 | 4.26 | +26.4 | +11.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -0.6 | 0.92 | 5.05 | +16.1 | +8.3 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 21.4% | -0.6 | 0.92 | 5.05 | +16.1 | +8.3 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 21.4% | 33.3% | 33.3% | 33.3% | +15.8 | 6.10 | 12.20 | +44.0 | +3.3 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_EXTENDED|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=33.3% Avg=+0.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 0.0% | -0.8 | 0.53 | 2.93 | +5.5 | +3.5 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `stop_hunt_le_90` | 10 | S_STRANGER | 71.4% | 10.0% | 10.0% | 0.0% | -0.2 | 0.73 | 5.82 | +5.1 | +3.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 0.0% | -0.8 | 0.53 | 2.93 | +5.5 | +3.5 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 0.0% | -0.8 | 0.53 | 2.93 | +5.5 | +3.5 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 42.9% | 33.3% | 33.3% | 0.0% | +0.9 | 1.77 | 3.53 | +7.8 | +2.8 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 71.4% | 20.0% | 20.0% | 0.0% | -0.6 | 0.69 | 2.77 | +6.4 | +3.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 4 | S_STRANGER | 28.6% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +4.4 | +3.6 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 0.0% | -0.7 | 0.59 | 2.96 | +5.5 | +3.4 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 50.0% | 14.3% | 14.3% | 0.0% | +0.2 | 1.31 | 7.84 | +5.6 | +3.0 |
| `feature_eurjpy_tdi50_reclaim` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 0.0% | +0.5 | 1.56 | 6.24 | +6.4 | +2.7 |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+1.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 7.1% | -0.9 | 0.57 | 3.41 | +4.1 | +4.6 |
| `hunt_to_ar_ratio_le_2_0` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 35.7% | 20.0% | 20.0% | 20.0% | +1.8 | 5.14 | 20.55 | +5.6 | +2.3 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 7.1% | -0.9 | 0.57 | 3.41 | +4.1 | +4.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 64.3% | 11.1% | 11.1% | 11.1% | -1.3 | 0.50 | 3.96 | +4.4 | +4.6 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +2.2 | +6.5 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 11.1% | 11.1% | 0.0% | -2.3 | 0.20 | 1.63 | +3.9 | +5.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 16.7% | -1.1 | 0.63 | 3.14 | +4.0 | +4.9 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 7.7% | -0.7 | 0.64 | 3.53 | +4.2 | +4.6 |
| `feature_momentum_breakout_exception` | 8 | S_STRANGER | 57.1% | 12.5% | 12.5% | 0.0% | -0.7 | 0.47 | 3.31 | +4.2 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 0.0% | -0.7 | 0.55 | 2.73 | +4.5 | +4.8 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-0.7; validation N=4 Fav=25.0% Avg=-3.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 7.1% | -1.4 | 0.62 | 3.39 | +6.4 | +6.8 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 7.1% | -1.4 | 0.62 | 3.39 | +6.4 | +6.8 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 7.1% | -1.4 | 0.62 | 3.39 | +6.4 | +6.8 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 7.1% | -1.4 | 0.62 | 3.39 | +6.4 | +6.8 |
| `asian_range_gte_30` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 7.7% | -1.4 | 0.64 | 3.20 | +6.7 | +7.1 |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 7.1% | -1.4 | 0.62 | 3.39 | +6.4 | +6.8 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 7.1% | -1.4 | 0.62 | 3.39 | +6.4 | +6.8 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 71.4% | 10.0% | 10.0% | 0.0% | -3.0 | 0.19 | 1.69 | +4.8 | +6.3 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 0.0% | -2.2 | 0.34 | 1.72 | +6.5 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 92.9% | 15.4% | 15.4% | 7.7% | -1.4 | 0.64 | 3.20 | +6.7 | +7.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 64.3% | 11.1% | 11.1% | 0.0% | -3.2 | 0.20 | 1.58 | +5.1 | +6.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 7.1% | -1.4 | 0.62 | 3.39 | +6.4 | +6.8 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 7.1% | -1.4 | 0.62 | 3.39 | +6.4 | +6.8 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 50.0% | -0.9 | 0.00 | 0.00 | +6.6 | +8.4 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=13 Fav=23.1% Avg=-2.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=25.0% Avg=+2.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 14.3% | 14.3% | 10.7% | -3.5 | 0.40 | 2.21 | +9.5 | +10.8 |
| `hunt_to_ar_ratio_le_2_0` | 28 | S_STRANGER | 100.0% | 14.3% | 14.3% | 10.7% | -3.5 | 0.40 | 2.21 | +9.5 | +10.8 |
| `hunt_to_ar_ratio_le_2_5` | 28 | S_STRANGER | 100.0% | 14.3% | 14.3% | 10.7% | -3.5 | 0.40 | 2.21 | +9.5 | +10.8 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 14.3% | 14.3% | 10.7% | -3.5 | 0.40 | 2.21 | +9.5 | +10.8 |
| `asian_range_gte_30` | 21 | S_STRANGER | 75.0% | 9.5% | 9.5% | 9.5% | -4.8 | 0.29 | 2.59 | +8.2 | +11.5 |
| `confluence_gte_60` | 25 | S_STRANGER | 89.3% | 16.0% | 16.0% | 12.0% | -3.4 | 0.44 | 2.09 | +9.5 | +10.6 |
| `confluence_gte_70` | 11 | S_STRANGER | 39.3% | 18.2% | 18.2% | 9.1% | -2.5 | 0.49 | 1.97 | +12.9 | +10.8 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 60.7% | 23.5% | 23.5% | 11.8% | -1.7 | 0.70 | 2.09 | +11.8 | +11.4 |
| `tdi_rsi_gte_50` | 22 | S_STRANGER | 78.6% | 18.2% | 18.2% | 9.1% | -2.8 | 0.51 | 2.19 | +10.7 | +10.7 |
| `ratio_le_2_and_asian_gte_30` | 21 | S_STRANGER | 75.0% | 9.5% | 9.5% | 9.5% | -4.8 | 0.29 | 2.59 | +8.2 | +11.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 42.9% | 16.7% | 16.7% | 16.7% | -2.8 | 0.55 | 2.47 | +11.5 | +12.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 14.3% | 14.3% | 10.7% | -3.5 | 0.40 | 2.21 | +9.5 | +10.8 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 14.3% | 14.3% | 10.7% | -3.5 | 0.40 | 2.21 | +9.5 | +10.8 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 10.7% | 33.3% | 33.3% | 33.3% | +2.3 | 1.50 | 2.99 | +13.9 | +12.9 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 21.4% | 16.7% | 16.7% | 16.7% | -1.6 | 0.68 | 3.42 | +12.6 | +11.5 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=0.0% Avg=-14.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=13 Fav=23.1% Avg=-1.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 28 | S_STRANGER | 100.0% | 14.3% | 17.9% | 10.7% | -3.6 | 0.34 | 1.44 | +6.9 | +9.4 |
| `hunt_to_ar_ratio_le_2_0` | 28 | S_STRANGER | 100.0% | 14.3% | 17.9% | 10.7% | -3.6 | 0.34 | 1.44 | +6.9 | +9.4 |
| `hunt_to_ar_ratio_le_2_5` | 28 | S_STRANGER | 100.0% | 14.3% | 17.9% | 10.7% | -3.6 | 0.34 | 1.44 | +6.9 | +9.4 |
| `stop_hunt_le_90` | 28 | S_STRANGER | 100.0% | 14.3% | 17.9% | 10.7% | -3.6 | 0.34 | 1.44 | +6.9 | +9.4 |
| `asian_range_gte_30` | 17 | S_STRANGER | 60.7% | 17.6% | 23.5% | 11.8% | -3.2 | 0.40 | 1.20 | +7.2 | +8.8 |
| `confluence_gte_60` | 28 | S_STRANGER | 100.0% | 14.3% | 17.9% | 10.7% | -3.6 | 0.34 | 1.44 | +6.9 | +9.4 |
| `confluence_gte_70` | 28 | S_STRANGER | 100.0% | 14.3% | 17.9% | 10.7% | -3.6 | 0.34 | 1.44 | +6.9 | +9.4 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 42.9% | 8.3% | 8.3% | 0.0% | -5.9 | 0.18 | 2.01 | +7.4 | +11.8 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 57.1% | 18.8% | 18.8% | 0.0% | -4.1 | 0.37 | 1.60 | +7.2 | +10.3 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 60.7% | 17.6% | 23.5% | 11.8% | -3.2 | 0.40 | 1.20 | +7.2 | +8.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -9.5 | 0.00 | 0.00 | +5.0 | +12.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 28 | S_STRANGER | 100.0% | 14.3% | 17.9% | 10.7% | -3.6 | 0.34 | 1.44 | +6.9 | +9.4 |
| `feature_stale_hod_exhaustion_reject` | 28 | S_STRANGER | 100.0% | 14.3% | 17.9% | 10.7% | -3.6 | 0.34 | 1.44 | +6.9 | +9.4 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 10.7% | 0.0% | 0.0% | 33.3% | -7.2 | 0.00 | 0.00 | +4.6 | +9.7 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.6% | 0.0% | 0.0% | 0.0% | -16.2 | 0.00 | 0.00 | +0.6 | +17.0 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=100.0% Avg=+8.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=0.0% Avg=-10.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -4.7 | 0.20 | 1.21 | +5.2 | +9.5 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 42.9% | 16.7% | 16.7% | 16.7% | -7.6 | 0.15 | 0.77 | +4.1 | +13.5 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 50.0% | 28.6% | 28.6% | 28.6% | -5.3 | 0.31 | 0.78 | +4.9 | +11.8 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -4.7 | 0.20 | 1.21 | +5.2 | +9.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -4.7 | 0.20 | 1.21 | +5.2 | +9.5 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -4.7 | 0.20 | 1.21 | +5.2 | +9.5 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 35.7% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +3.2 | +9.0 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 57.1% | 0.0% | 0.0% | 0.0% | -8.7 | 0.00 | 0.00 | +2.6 | +13.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -4.7 | 0.20 | 1.21 | +5.2 | +9.5 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 14.3% | 14.3% | 14.3% | -4.7 | 0.20 | 1.21 | +5.2 | +9.5 |
| `feature_momentum_breakout_exception` | 2 | R_RUNNER | 14.3% | 100.0% | 100.0% | 100.0% | +8.4 | 999.00 | 999.00 | +12.6 | +1.3 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=9 Fav=22.2% Avg=-0.9; validation N=7 Fav=14.3% Avg=-39.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 22 | S_STRANGER | 100.0% | 13.6% | 18.2% | 18.2% | -17.9 | 0.12 | 0.52 | +7.2 | +7.6 |
| `hunt_to_ar_ratio_le_2_0` | 19 | S_STRANGER | 86.4% | 15.8% | 21.1% | 15.8% | -19.8 | 0.13 | 0.47 | +7.8 | +7.7 |
| `hunt_to_ar_ratio_le_2_5` | 22 | S_STRANGER | 100.0% | 13.6% | 18.2% | 18.2% | -17.9 | 0.12 | 0.52 | +7.2 | +7.6 |
| `stop_hunt_le_90` | 22 | S_STRANGER | 100.0% | 13.6% | 18.2% | 18.2% | -17.9 | 0.12 | 0.52 | +7.2 | +7.6 |
| `asian_range_gte_30` | 16 | S_STRANGER | 72.7% | 18.8% | 25.0% | 18.8% | -17.7 | 0.16 | 0.48 | +8.6 | +6.1 |
| `confluence_gte_60` | 8 | S_STRANGER | 36.4% | 12.5% | 12.5% | 12.5% | -16.0 | 0.07 | 0.51 | +8.2 | +11.2 |
| `confluence_gte_70` | 2 | R_REPEATER | 9.1% | 50.0% | 50.0% | 50.0% | -3.5 | 0.59 | 0.59 | +12.3 | +15.0 |
| `tdi_rsi_gt_signal` | 16 | S_STRANGER | 72.7% | 6.2% | 12.5% | 6.2% | -7.8 | 0.19 | 1.32 | +6.1 | +9.1 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 22.7% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +6.6 | +10.4 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 72.7% | 18.8% | 25.0% | 18.8% | -17.7 | 0.16 | 0.48 | +8.6 | +6.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 54.5% | 8.3% | 16.7% | 8.3% | -4.8 | 0.34 | 1.68 | +7.3 | +6.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 22 | S_STRANGER | 100.0% | 13.6% | 18.2% | 18.2% | -17.9 | 0.12 | 0.52 | +7.2 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 22 | S_STRANGER | 100.0% | 13.6% | 18.2% | 18.2% | -17.9 | 0.12 | 0.52 | +7.2 | +7.6 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 4.5% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +2.3 | +4.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 4.5% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +2.3 | +4.8 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=50.0% Avg=+6.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=0.0% Avg=-2.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 0.0% | -1.6 | 0.39 | 2.56 | +3.7 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 0.0% | -1.6 | 0.39 | 2.56 | +3.7 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 0.0% | -1.6 | 0.39 | 2.56 | +3.7 | +5.5 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 0.0% | -1.6 | 0.39 | 2.56 | +3.7 | +5.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 86.7% | 7.7% | 7.7% | 0.0% | -2.8 | 0.05 | 0.65 | +2.1 | +5.3 |
| `confluence_gte_70` | 2 | S_STRANGER | 13.3% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +2.1 | +3.7 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 46.7% | 0.0% | 0.0% | 0.0% | -3.6 | 0.00 | 0.00 | +2.5 | +6.9 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 46.7% | 14.3% | 14.3% | 0.0% | -0.2 | 0.89 | 5.36 | +5.3 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 0.0% | -1.6 | 0.39 | 2.56 | +3.7 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 0.0% | -1.6 | 0.39 | 2.56 | +3.7 | +5.5 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -5.9 | 0.00 | 0.00 | +1.4 | +7.7 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=6 Fav=16.7% Avg=+0.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 26.7% | -1.7 | 0.54 | 2.68 | +8.0 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 26.7% | -1.7 | 0.54 | 2.68 | +8.0 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 26.7% | -1.7 | 0.54 | 2.68 | +8.0 | +7.1 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 26.7% | -1.7 | 0.54 | 2.68 | +8.0 | +7.1 |
| `asian_range_gte_30` | 12 | S_STRANGER | 80.0% | 16.7% | 16.7% | 25.0% | -1.2 | 0.67 | 2.67 | +9.3 | +7.5 |
| `confluence_gte_60` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 26.7% | -1.7 | 0.54 | 2.68 | +8.0 | +7.1 |
| `confluence_gte_70` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 26.7% | -1.7 | 0.54 | 2.68 | +8.0 | +7.1 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -4.2 | 0.00 | 0.00 | +7.5 | +7.2 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 60.0% | 11.1% | 11.1% | 11.1% | -3.0 | 0.20 | 1.43 | +6.2 | +7.3 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 80.0% | 16.7% | 16.7% | 25.0% | -1.2 | 0.67 | 2.67 | +9.3 | +7.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -4.2 | 0.00 | 0.00 | +7.5 | +7.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 26.7% | -1.7 | 0.54 | 2.68 | +8.0 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 15 | S_STRANGER | 100.0% | 13.3% | 13.3% | 26.7% | -1.7 | 0.54 | 2.68 | +8.0 | +7.1 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 40.0% | 16.7% | 16.7% | 66.7% | +0.9 | 1.33 | 2.65 | +13.8 | +5.0 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 33.3% | -3.4 | 0.00 | 0.00 | +11.2 | +5.7 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=10 Fav=10.0% Avg=-1.9; validation N=1 Fav=0.0% Avg=-0.8; out_of_sample N=6 Fav=33.3% Avg=+6.7.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | +0.4 | 1.10 | 4.94 | +8.7 | +10.0 |
| `hunt_to_ar_ratio_le_2_0` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | +0.4 | 1.10 | 4.94 | +8.7 | +10.0 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | +0.4 | 1.10 | 4.94 | +8.7 | +10.0 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | +0.4 | 1.10 | 4.94 | +8.7 | +10.0 |
| `asian_range_gte_30` | 17 | S_STRANGER | 73.9% | 17.6% | 23.5% | 23.5% | +1.2 | 1.24 | 3.73 | +10.2 | +11.2 |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | +0.4 | 1.10 | 4.94 | +8.7 | +10.0 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | +0.4 | 1.10 | 4.94 | +8.7 | +10.0 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 91.3% | 14.3% | 19.0% | 19.0% | +0.6 | 1.14 | 4.56 | +9.4 | +10.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 43.5% | 10.0% | 10.0% | 10.0% | -2.7 | 0.57 | 5.09 | +7.3 | +7.8 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 73.9% | 17.6% | 23.5% | 23.5% | +1.2 | 1.24 | 3.73 | +10.2 | +11.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 17 | S_STRANGER | 73.9% | 17.6% | 23.5% | 23.5% | +1.2 | 1.24 | 3.73 | +10.2 | +11.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | +0.4 | 1.10 | 4.94 | +8.7 | +10.0 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 13.0% | 17.4% | 17.4% | +0.4 | 1.10 | 4.94 | +8.7 | +10.0 |
| `feature_momentum_breakout_exception` | 7 | S_STRANGER | 30.4% | 0.0% | 14.3% | 0.0% | -3.6 | 0.08 | 0.50 | +3.9 | +7.9 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 8.7% | 0.0% | 0.0% | 0.0% | -7.7 | 0.00 | 0.00 | +6.0 | +11.0 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+12.0; validation N=11 Fav=18.2% Avg=+0.7; out_of_sample N=4 Fav=0.0% Avg=-8.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 23 | S_STRANGER | 100.0% | 13.0% | 13.0% | 17.4% | -1.6 | 0.54 | 3.25 | +6.1 | +8.7 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 95.7% | 13.6% | 13.6% | 18.2% | -1.6 | 0.55 | 3.14 | +6.3 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 23 | S_STRANGER | 100.0% | 13.0% | 13.0% | 17.4% | -1.6 | 0.54 | 3.25 | +6.1 | +8.7 |
| `stop_hunt_le_90` | 23 | S_STRANGER | 100.0% | 13.0% | 13.0% | 17.4% | -1.6 | 0.54 | 3.25 | +6.1 | +8.7 |
| `asian_range_gte_30` | 16 | S_STRANGER | 69.6% | 18.8% | 18.8% | 25.0% | -0.8 | 0.77 | 2.81 | +7.5 | +9.0 |
| `confluence_gte_60` | 23 | S_STRANGER | 100.0% | 13.0% | 13.0% | 17.4% | -1.6 | 0.54 | 3.25 | +6.1 | +8.7 |
| `confluence_gte_70` | 23 | S_STRANGER | 100.0% | 13.0% | 13.0% | 17.4% | -1.6 | 0.54 | 3.25 | +6.1 | +8.7 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 47.8% | 9.1% | 9.1% | 9.1% | -2.6 | 0.19 | 1.72 | +5.3 | +10.0 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 47.8% | 9.1% | 9.1% | 0.0% | -2.2 | 0.22 | 2.16 | +4.4 | +6.2 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 69.6% | 18.8% | 18.8% | 25.0% | -0.8 | 0.77 | 2.81 | +7.5 | +9.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 30.4% | 14.3% | 14.3% | 14.3% | -2.3 | 0.30 | 1.48 | +6.9 | +12.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 23 | S_STRANGER | 100.0% | 13.0% | 13.0% | 17.4% | -1.6 | 0.54 | 3.25 | +6.1 | +8.7 |
| `feature_stale_hod_exhaustion_reject` | 23 | S_STRANGER | 100.0% | 13.0% | 13.0% | 17.4% | -1.6 | 0.54 | 3.25 | +6.1 | +8.7 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 13.0% | 33.3% | 33.3% | 33.3% | +3.3 | 5.45 | 10.91 | +5.6 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 8.7% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +1.5 | +5.6 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=+4.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 12.5% | 31.2% | 25.0% | +0.4 | 1.14 | 2.05 | +9.9 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -8.1 | 0.00 | 0.00 | +18.6 | +11.8 |
| `hunt_to_ar_ratio_le_2_5` | 2 | S_STRANGER | 12.5% | 0.0% | 0.0% | 50.0% | -4.0 | 0.00 | 0.00 | +13.4 | +8.7 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 12.5% | 31.2% | 25.0% | +0.4 | 1.14 | 2.05 | +9.9 | +7.0 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 15 | S_STRANGER | 93.8% | 13.3% | 33.3% | 26.7% | +0.6 | 1.19 | 1.91 | +10.5 | +6.9 |
| `confluence_gte_70` | 6 | S_STRANGER | 37.5% | 16.7% | 33.3% | 33.3% | +4.0 | 3.14 | 4.70 | +11.3 | +5.9 |
| `tdi_rsi_gt_signal` | 1 | R_RUNNER | 6.2% | 100.0% | 100.0% | 100.0% | +30.0 | 999.00 | 999.00 | +38.1 | +2.8 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 25.0% | 25.0% | 25.0% | 25.0% | +3.8 | 2.01 | 6.04 | +15.6 | +6.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 68.8% | 9.1% | 27.3% | 27.3% | +1.7 | 1.86 | 3.73 | +10.4 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 12.5% | 31.2% | 25.0% | +0.4 | 1.14 | 2.05 | +9.9 | +7.0 |
| `feature_momentum_breakout_exception` | 6 | S_STRANGER | 37.5% | 16.7% | 33.3% | 33.3% | -2.0 | 0.52 | 0.78 | +8.7 | +8.8 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +3.1 | +8.4 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=20.0% Avg=-5.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 6.2% | -4.8 | 0.22 | 1.40 | +7.1 | +9.5 |
| `hunt_to_ar_ratio_le_2_0` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 6.2% | -4.8 | 0.22 | 1.40 | +7.1 | +9.5 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 6.2% | -4.8 | 0.22 | 1.40 | +7.1 | +9.5 |
| `stop_hunt_le_90` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 6.2% | -4.8 | 0.22 | 1.40 | +7.1 | +9.5 |
| `asian_range_gte_30` | 15 | S_STRANGER | 93.8% | 6.7% | 6.7% | 6.7% | -5.2 | 0.21 | 2.74 | +6.3 | +9.1 |
| `confluence_gte_60` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 6.2% | -4.8 | 0.22 | 1.40 | +7.1 | +9.5 |
| `confluence_gte_70` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 6.2% | -4.8 | 0.22 | 1.40 | +7.1 | +9.5 |
| `tdi_rsi_gt_signal` | 12 | S_STRANGER | 75.0% | 8.3% | 8.3% | 8.3% | -4.6 | 0.27 | 2.71 | +7.0 | +10.4 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 31.2% | 20.0% | 20.0% | 0.0% | -5.9 | 0.02 | 0.07 | +5.6 | +9.4 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 93.8% | 6.7% | 6.7% | 6.7% | -5.2 | 0.21 | 2.74 | +6.3 | +9.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 12 | S_STRANGER | 75.0% | 8.3% | 8.3% | 8.3% | -4.6 | 0.27 | 2.71 | +7.0 | +10.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 6.2% | -4.8 | 0.22 | 1.40 | +7.1 | +9.5 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 100.0% | 12.5% | 12.5% | 6.2% | -4.8 | 0.22 | 1.40 | +7.1 | +9.5 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 6.2% | 0.0% | 0.0% | 0.0% | -10.0 | 0.00 | 0.00 | +7.3 | +18.0 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=0.0% Avg=-11.8; validation N=7 Fav=28.6% Avg=+3.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 12.5% | 20.8% | 12.5% | -5.6 | 0.38 | 1.37 | +8.0 | +7.2 |
| `hunt_to_ar_ratio_le_2_0` | 21 | S_STRANGER | 87.5% | 14.3% | 23.8% | 14.3% | -5.2 | 0.43 | 1.29 | +8.5 | +6.9 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 100.0% | 12.5% | 20.8% | 12.5% | -5.6 | 0.38 | 1.37 | +8.0 | +7.2 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 12.5% | 20.8% | 12.5% | -5.6 | 0.38 | 1.37 | +8.0 | +7.2 |
| `asian_range_gte_30` | 18 | S_STRANGER | 75.0% | 11.1% | 22.2% | 16.7% | -4.9 | 0.45 | 1.46 | +8.3 | +7.3 |
| `confluence_gte_60` | 11 | S_STRANGER | 45.8% | 9.1% | 18.2% | 9.1% | -4.9 | 0.40 | 1.82 | +7.9 | +6.6 |
| `confluence_gte_70` | 1 | R_RUNNER | 4.2% | 100.0% | 100.0% | 100.0% | +28.0 | 999.00 | 999.00 | +29.0 | +2.1 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 54.2% | 15.4% | 15.4% | 15.4% | -3.6 | 0.45 | 2.23 | +8.0 | +8.9 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 33.3% | 12.5% | 12.5% | 25.0% | -0.5 | 0.88 | 5.26 | +10.6 | +10.6 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 70.8% | 11.8% | 23.5% | 17.6% | -4.8 | 0.47 | 1.41 | +8.3 | +7.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 37.5% | 11.1% | 11.1% | 22.2% | -2.1 | 0.59 | 4.11 | +7.4 | +10.6 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 12.5% | 20.8% | 12.5% | -5.6 | 0.38 | 1.37 | +8.0 | +7.2 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 12.5% | 20.8% | 12.5% | -5.6 | 0.38 | 1.37 | +8.0 | +7.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=2 Fav=0.0% Avg=-4.6; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=25.0% Avg=+2.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 41 | S_STRANGER | 100.0% | 12.2% | 19.5% | 12.2% | -3.4 | 0.38 | 1.39 | +6.8 | +7.8 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 26.8% | 9.1% | 18.2% | 18.2% | -3.7 | 0.38 | 1.52 | +8.8 | +9.7 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 31.7% | 15.4% | 30.8% | 15.4% | -2.1 | 0.58 | 1.15 | +8.7 | +8.6 |
| `stop_hunt_le_90` | 41 | S_STRANGER | 100.0% | 12.2% | 19.5% | 12.2% | -3.4 | 0.38 | 1.39 | +6.8 | +7.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 38 | S_STRANGER | 92.7% | 10.5% | 18.4% | 10.5% | -4.2 | 0.28 | 1.10 | +6.6 | +7.8 |
| `confluence_gte_70` | 6 | S_STRANGER | 14.6% | 16.7% | 33.3% | 0.0% | -0.2 | 0.96 | 1.93 | +9.5 | +7.7 |
| `tdi_rsi_gt_signal` | 29 | S_STRANGER | 70.7% | 6.9% | 13.8% | 10.3% | -4.5 | 0.24 | 1.28 | +6.8 | +7.3 |
| `tdi_rsi_gte_50` | 16 | S_STRANGER | 39.0% | 12.5% | 12.5% | 6.2% | -3.3 | 0.32 | 1.93 | +7.6 | +8.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 40 | S_STRANGER | 97.6% | 12.5% | 17.5% | 12.5% | -3.8 | 0.32 | 1.31 | +6.6 | +7.9 |
| `feature_stale_hod_exhaustion_reject` | 41 | S_STRANGER | 100.0% | 12.2% | 19.5% | 12.2% | -3.4 | 0.38 | 1.39 | +6.8 | +7.8 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 9.8% | 0.0% | 50.0% | 50.0% | +4.3 | 999.00 | 999.00 | +14.6 | +2.4 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 2.4% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +9.9 | +15.5 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-2.6; validation N=15 Fav=13.3% Avg=-3.4; out_of_sample N=1 Fav=0.0% Avg=-2.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -3.3 | 0.20 | 1.51 | +4.8 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -3.3 | 0.20 | 1.51 | +4.8 | +7.1 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -3.3 | 0.20 | 1.51 | +4.8 | +7.1 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -3.3 | 0.20 | 1.51 | +4.8 | +7.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -3.3 | 0.20 | 1.51 | +4.8 | +7.1 |
| `confluence_gte_70` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +4.1 | +3.2 |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -2.4 | 0.00 | 0.00 | +6.3 | +7.2 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 58.8% | 0.0% | 0.0% | 0.0% | -4.9 | 0.00 | 0.00 | +4.6 | +7.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -3.3 | 0.20 | 1.51 | +4.8 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 11.8% | 11.8% | 0.0% | -3.3 | 0.20 | 1.51 | +4.8 | +7.1 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=11 Fav=27.3% Avg=-0.7; out_of_sample N=1 Fav=0.0% Avg=-0.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 35 | S_STRANGER | 100.0% | 11.4% | 14.3% | 2.9% | -8.0 | 0.17 | 1.00 | +5.1 | +7.1 |
| `hunt_to_ar_ratio_le_2_0` | 14 | S_STRANGER | 40.0% | 0.0% | 7.1% | 0.0% | -15.2 | 0.03 | 0.38 | +3.2 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 16 | S_STRANGER | 45.7% | 0.0% | 6.2% | 0.0% | -14.0 | 0.03 | 0.42 | +2.9 | +7.2 |
| `stop_hunt_le_90` | 35 | S_STRANGER | 100.0% | 11.4% | 14.3% | 2.9% | -8.0 | 0.17 | 1.00 | +5.1 | +7.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 35 | S_STRANGER | 100.0% | 11.4% | 14.3% | 2.9% | -8.0 | 0.17 | 1.00 | +5.1 | +7.1 |
| `confluence_gte_70` | 14 | S_STRANGER | 40.0% | 21.4% | 21.4% | 7.1% | -1.8 | 0.64 | 2.14 | +7.1 | +6.6 |
| `tdi_rsi_gt_signal` | 29 | S_STRANGER | 82.9% | 13.8% | 17.2% | 0.0% | -8.1 | 0.20 | 0.96 | +5.4 | +6.7 |
| `tdi_rsi_gte_50` | 12 | S_STRANGER | 34.3% | 25.0% | 25.0% | 0.0% | -0.7 | 0.84 | 2.53 | +8.2 | +7.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 35 | S_STRANGER | 100.0% | 11.4% | 14.3% | 2.9% | -8.0 | 0.17 | 1.00 | +5.1 | +7.1 |
| `feature_stale_hod_exhaustion_reject` | 35 | S_STRANGER | 100.0% | 11.4% | 14.3% | 2.9% | -8.0 | 0.17 | 1.00 | +5.1 | +7.1 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 5.7% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +3.1 | +2.1 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-1.9; validation N=6 Fav=33.3% Avg=+2.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 27.8% | -0.4 | 0.83 | 4.95 | +9.0 | +3.8 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 61.1% | 18.2% | 18.2% | 36.4% | +0.8 | 1.38 | 4.14 | +12.1 | +3.5 |
| `hunt_to_ar_ratio_le_2_5` | 15 | S_STRANGER | 83.3% | 13.3% | 13.3% | 26.7% | -0.3 | 0.88 | 4.39 | +10.1 | +4.1 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 27.8% | -0.4 | 0.83 | 4.95 | +9.0 | +3.8 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 27.8% | -0.4 | 0.83 | 4.95 | +9.0 | +3.8 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 27.8% | -0.4 | 0.83 | 4.95 | +9.0 | +3.8 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 44.4% | 12.5% | 12.5% | 25.0% | -1.4 | 0.53 | 3.19 | +7.5 | +4.9 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 38.9% | 28.6% | 28.6% | 28.6% | +1.8 | 1.66 | 4.16 | +12.5 | +4.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 27.8% | -0.4 | 0.83 | 4.95 | +9.0 | +3.8 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 27.8% | -0.4 | 0.83 | 4.95 | +9.0 | +3.8 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | +0.0 | 0.00 | 0.00 | +9.0 | +0.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=11 Fav=18.2% Avg=+0.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 0.0% | -1.6 | 0.41 | 3.29 | +5.5 | +4.5 |
| `hunt_to_ar_ratio_le_2_0` | 2 | S_STRANGER | 11.1% | 0.0% | 0.0% | 0.0% | -2.7 | 0.00 | 0.00 | +6.3 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -2.6 | 0.00 | 0.00 | +6.7 | +4.8 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 0.0% | -1.6 | 0.41 | 3.29 | +5.5 | +4.5 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 0.0% | -1.6 | 0.41 | 3.29 | +5.5 | +4.5 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 11.1% | 11.1% | 0.0% | -1.6 | 0.41 | 3.29 | +5.5 | +4.5 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 38.9% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +5.6 | +5.1 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 50.0% | 11.1% | 11.1% | 0.0% | -2.7 | 0.33 | 2.61 | +6.4 | +5.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 7 | S_STRANGER | 38.9% | 0.0% | 0.0% | 0.0% | -4.3 | 0.00 | 0.00 | +5.3 | +6.1 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 94.4% | 5.9% | 5.9% | 0.0% | -2.4 | 0.17 | 2.76 | +4.9 | +4.6 |
| `feature_momentum_breakout_exception` | 11 | S_STRANGER | 61.1% | 18.2% | 18.2% | 0.0% | +0.1 | 1.06 | 4.76 | +5.6 | +3.5 |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 33.3% | 16.7% | 16.7% | 0.0% | -0.3 | 0.86 | 4.30 | +6.5 | +4.2 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-5.4; validation N=20 Fav=15.0% Avg=-3.2; out_of_sample N=3 Fav=0.0% Avg=-4.1.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 11.1% | 22.2% | 22.2% | -3.0 | 0.45 | 1.36 | +7.8 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 27 | S_STRANGER | 100.0% | 11.1% | 22.2% | 22.2% | -3.0 | 0.45 | 1.36 | +7.8 | +8.2 |
| `hunt_to_ar_ratio_le_2_5` | 27 | S_STRANGER | 100.0% | 11.1% | 22.2% | 22.2% | -3.0 | 0.45 | 1.36 | +7.8 | +8.2 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 100.0% | 11.1% | 22.2% | 22.2% | -3.0 | 0.45 | 1.36 | +7.8 | +8.2 |
| `asian_range_gte_30` | 24 | S_STRANGER | 88.9% | 12.5% | 25.0% | 16.7% | -3.4 | 0.46 | 1.29 | +7.7 | +8.9 |
| `confluence_gte_60` | 27 | S_STRANGER | 100.0% | 11.1% | 22.2% | 22.2% | -3.0 | 0.45 | 1.36 | +7.8 | +8.2 |
| `confluence_gte_70` | 24 | S_STRANGER | 88.9% | 4.2% | 16.7% | 16.7% | -4.6 | 0.24 | 1.01 | +6.9 | +8.6 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 63.0% | 5.9% | 17.6% | 11.8% | -5.4 | 0.23 | 1.00 | +6.7 | +10.1 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 40.7% | 0.0% | 0.0% | 9.1% | -9.7 | 0.00 | 0.00 | +6.8 | +14.8 |
| `ratio_le_2_and_asian_gte_30` | 24 | S_STRANGER | 88.9% | 12.5% | 25.0% | 16.7% | -3.4 | 0.46 | 1.29 | +7.7 | +8.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 16 | S_STRANGER | 59.3% | 6.2% | 18.8% | 12.5% | -5.7 | 0.23 | 0.93 | +6.9 | +10.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 100.0% | 11.1% | 22.2% | 22.2% | -3.0 | 0.45 | 1.36 | +7.8 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 11.1% | 22.2% | 22.2% | -3.0 | 0.45 | 1.36 | +7.8 | +8.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 3.7% | 0.0% | 0.0% | 0.0% | -5.8 | 0.00 | 0.00 | +6.2 | +8.5 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-3.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=6 Fav=33.3% Avg=-1.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 0.0% | -3.7 | 0.23 | 0.80 | +4.4 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 33.3% | 16.7% | 16.7% | 0.0% | -2.2 | 0.41 | 2.06 | +5.4 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 61.1% | 18.2% | 36.4% | 0.0% | -2.0 | 0.47 | 0.82 | +5.0 | +4.3 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 0.0% | -3.7 | 0.23 | 0.80 | +4.4 | +5.7 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 0.0% | -3.7 | 0.23 | 0.80 | +4.4 | +5.7 |
| `confluence_gte_70` | 15 | S_STRANGER | 83.3% | 13.3% | 26.7% | 0.0% | -2.5 | 0.35 | 0.96 | +5.0 | +4.7 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 38.9% | 0.0% | 0.0% | 0.0% | -7.1 | 0.00 | 0.00 | +3.3 | +7.4 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 33.3% | 16.7% | 16.7% | 0.0% | -0.8 | 0.66 | 3.30 | +5.0 | +3.9 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 94.4% | 11.8% | 17.6% | 0.0% | -4.0 | 0.23 | 1.06 | +4.6 | +6.0 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 11.1% | 22.2% | 0.0% | -3.7 | 0.23 | 0.80 | +4.4 | +5.7 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 16.7% | 0.0% | 33.3% | 0.0% | -3.1 | 0.02 | 0.04 | +5.9 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 5.6% | 0.0% | 0.0% | 0.0% | -2.1 | 0.00 | 0.00 | +10.5 | +4.3 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-9.5; validation N=4 Fav=25.0% Avg=-5.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 27 | S_STRANGER | 100.0% | 11.1% | 14.8% | 7.4% | -7.8 | 0.14 | 0.79 | +4.4 | +7.9 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 29.6% | 0.0% | 0.0% | 0.0% | -3.7 | 0.00 | 0.00 | +3.4 | +8.6 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +3.2 | +8.4 |
| `stop_hunt_le_90` | 27 | S_STRANGER | 100.0% | 11.1% | 14.8% | 7.4% | -7.8 | 0.14 | 0.79 | +4.4 | +7.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 51.9% | 7.1% | 7.1% | 0.0% | -8.2 | 0.06 | 0.72 | +3.2 | +7.7 |
| `confluence_gte_70` | 1 | S_STRANGER | 3.7% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +1.7 | +6.2 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 63.0% | 5.9% | 5.9% | 0.0% | -8.9 | 0.04 | 0.68 | +2.8 | +8.6 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 29.6% | 12.5% | 12.5% | 0.0% | -7.5 | 0.10 | 0.71 | +2.4 | +11.6 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 27 | S_STRANGER | 100.0% | 11.1% | 14.8% | 7.4% | -7.8 | 0.14 | 0.79 | +4.4 | +7.9 |
| `feature_stale_hod_exhaustion_reject` | 27 | S_STRANGER | 100.0% | 11.1% | 14.8% | 7.4% | -7.8 | 0.14 | 0.79 | +4.4 | +7.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=+0.0; validation N=11 Fav=9.1% Avg=-5.6; out_of_sample N=3 Fav=33.3% Avg=+6.9.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 10.5% | 10.5% | 10.5% | -3.9 | 0.36 | 2.92 | +7.1 | +8.0 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 94.7% | 11.1% | 11.1% | 11.1% | -3.9 | 0.38 | 2.82 | +7.0 | +8.1 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 10.5% | 10.5% | 10.5% | -3.9 | 0.36 | 2.92 | +7.1 | +8.0 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 10.5% | 10.5% | 10.5% | -3.9 | 0.36 | 2.92 | +7.1 | +8.0 |
| `asian_range_gte_30` | 15 | S_STRANGER | 78.9% | 13.3% | 13.3% | 13.3% | -2.7 | 0.51 | 3.08 | +7.9 | +7.9 |
| `confluence_gte_60` | 19 | S_STRANGER | 100.0% | 10.5% | 10.5% | 10.5% | -3.9 | 0.36 | 2.92 | +7.1 | +8.0 |
| `confluence_gte_70` | 19 | S_STRANGER | 100.0% | 10.5% | 10.5% | 10.5% | -3.9 | 0.36 | 2.92 | +7.1 | +8.0 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 36.8% | 0.0% | 0.0% | 0.0% | -6.1 | 0.00 | 0.00 | +3.8 | +8.9 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 52.6% | 10.0% | 10.0% | 0.0% | -3.8 | 0.27 | 2.41 | +5.6 | +8.4 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 78.9% | 13.3% | 13.3% | 13.3% | -2.7 | 0.51 | 3.08 | +7.9 | +7.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 31.6% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +3.9 | +10.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 10.5% | 10.5% | 10.5% | -3.9 | 0.36 | 2.92 | +7.1 | +8.0 |
| `feature_stale_hod_exhaustion_reject` | 19 | S_STRANGER | 100.0% | 10.5% | 10.5% | 10.5% | -3.9 | 0.36 | 2.92 | +7.1 | +8.0 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|NYC_REVERSAL|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=20.0% Avg=-6.0; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 19 | S_STRANGER | 100.0% | 10.5% | 15.8% | 5.3% | -7.9 | 0.19 | 0.94 | +13.3 | +16.4 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 94.7% | 11.1% | 16.7% | 5.6% | -8.3 | 0.19 | 0.88 | +12.2 | +17.2 |
| `hunt_to_ar_ratio_le_2_5` | 19 | S_STRANGER | 100.0% | 10.5% | 15.8% | 5.3% | -7.9 | 0.19 | 0.94 | +13.3 | +16.4 |
| `stop_hunt_le_90` | 19 | S_STRANGER | 100.0% | 10.5% | 15.8% | 5.3% | -7.9 | 0.19 | 0.94 | +13.3 | +16.4 |
| `asian_range_gte_30` | 16 | S_STRANGER | 84.2% | 12.5% | 18.8% | 6.2% | -8.1 | 0.21 | 0.85 | +14.8 | +17.2 |
| `confluence_gte_60` | 10 | S_STRANGER | 52.6% | 20.0% | 30.0% | 0.0% | -6.0 | 0.37 | 0.85 | +13.5 | +19.0 |
| `confluence_gte_70` | 4 | R_REPEATER | 21.1% | 50.0% | 50.0% | 0.0% | -0.4 | 0.94 | 0.94 | +18.9 | +15.4 |
| `tdi_rsi_gt_signal` | 5 | S_STRANGER | 26.3% | 20.0% | 20.0% | 0.0% | -9.2 | 0.17 | 0.66 | +20.3 | +19.5 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 57.9% | 9.1% | 9.1% | 0.0% | -10.2 | 0.07 | 0.75 | +14.9 | +18.4 |
| `ratio_le_2_and_asian_gte_30` | 15 | S_STRANGER | 78.9% | 13.3% | 20.0% | 6.7% | -8.6 | 0.21 | 0.78 | +13.6 | +18.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 21.1% | 25.0% | 25.0% | 0.0% | -11.4 | 0.17 | 0.50 | +17.3 | +23.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 19 | S_STRANGER | 100.0% | 10.5% | 15.8% | 5.3% | -7.9 | 0.19 | 0.94 | +13.3 | +16.4 |
| `feature_stale_hod_exhaustion_reject` | 16 | S_STRANGER | 84.2% | 12.5% | 18.8% | 6.2% | -7.3 | 0.23 | 0.92 | +14.4 | +16.0 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 15.8% | 0.0% | 0.0% | 0.0% | -14.4 | 0.00 | 0.00 | +4.1 | +11.5 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 10.5% | 0.0% | 0.0% | 0.0% | -11.8 | 0.00 | 0.00 | +9.3 | +15.7 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+27.9; validation N=0 Fav=0.0% Avg=-; out_of_sample N=9 Fav=11.1% Avg=-3.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 10.3% | 10.3% | 10.3% | -1.1 | 0.69 | 5.77 | +7.0 | +6.5 |
| `hunt_to_ar_ratio_le_2_0` | 29 | S_STRANGER | 100.0% | 10.3% | 10.3% | 10.3% | -1.1 | 0.69 | 5.77 | +7.0 | +6.5 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 100.0% | 10.3% | 10.3% | 10.3% | -1.1 | 0.69 | 5.77 | +7.0 | +6.5 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 100.0% | 10.3% | 10.3% | 10.3% | -1.1 | 0.69 | 5.77 | +7.0 | +6.5 |
| `asian_range_gte_30` | 20 | S_STRANGER | 69.0% | 10.0% | 10.0% | 10.0% | -1.9 | 0.52 | 4.45 | +6.9 | +7.1 |
| `confluence_gte_60` | 29 | S_STRANGER | 100.0% | 10.3% | 10.3% | 10.3% | -1.1 | 0.69 | 5.77 | +7.0 | +6.5 |
| `confluence_gte_70` | 29 | S_STRANGER | 100.0% | 10.3% | 10.3% | 10.3% | -1.1 | 0.69 | 5.77 | +7.0 | +6.5 |
| `tdi_rsi_gt_signal` | 13 | S_STRANGER | 44.8% | 15.4% | 15.4% | 7.7% | -0.5 | 0.86 | 4.75 | +8.3 | +6.8 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 58.6% | 11.8% | 11.8% | 5.9% | -0.4 | 0.85 | 6.36 | +7.2 | +5.8 |
| `ratio_le_2_and_asian_gte_30` | 20 | S_STRANGER | 69.0% | 10.0% | 10.0% | 10.0% | -1.9 | 0.52 | 4.45 | +6.9 | +7.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 10 | S_STRANGER | 34.5% | 20.0% | 20.0% | 10.0% | -0.1 | 0.99 | 3.94 | +9.8 | +7.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 100.0% | 10.3% | 10.3% | 10.3% | -1.1 | 0.69 | 5.77 | +7.0 | +6.5 |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 10.3% | 10.3% | 10.3% | -1.1 | 0.69 | 5.77 | +7.0 | +6.5 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 3.4% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +3.5 | +6.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | R_RUNNER | 3.4% | 100.0% | 100.0% | 100.0% | +27.9 | 999.00 | 999.00 | +40.3 | +1.9 |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+3.4; validation N=10 Fav=20.0% Avg=-19.7; out_of_sample N=5 Fav=0.0% Avg=-4.2.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 29 | S_STRANGER | 100.0% | 10.3% | 13.8% | 10.3% | -8.2 | 0.15 | 0.92 | +7.2 | +6.2 |
| `hunt_to_ar_ratio_le_2_0` | 29 | S_STRANGER | 100.0% | 10.3% | 13.8% | 10.3% | -8.2 | 0.15 | 0.92 | +7.2 | +6.2 |
| `hunt_to_ar_ratio_le_2_5` | 29 | S_STRANGER | 100.0% | 10.3% | 13.8% | 10.3% | -8.2 | 0.15 | 0.92 | +7.2 | +6.2 |
| `stop_hunt_le_90` | 29 | S_STRANGER | 100.0% | 10.3% | 13.8% | 10.3% | -8.2 | 0.15 | 0.92 | +7.2 | +6.2 |
| `asian_range_gte_30` | 25 | S_STRANGER | 86.2% | 12.0% | 16.0% | 12.0% | -9.0 | 0.16 | 0.81 | +7.4 | +5.8 |
| `confluence_gte_60` | 26 | S_STRANGER | 89.7% | 11.5% | 15.4% | 11.5% | -9.0 | 0.16 | 0.82 | +7.2 | +6.6 |
| `confluence_gte_70` | 11 | S_STRANGER | 37.9% | 9.1% | 18.2% | 9.1% | -2.6 | 0.53 | 2.38 | +7.0 | +5.1 |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 79.3% | 13.0% | 17.4% | 8.7% | -9.1 | 0.17 | 0.81 | +7.3 | +6.4 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 31.0% | 11.1% | 11.1% | 0.0% | -5.0 | 0.08 | 0.60 | +5.6 | +10.6 |
| `ratio_le_2_and_asian_gte_30` | 25 | S_STRANGER | 86.2% | 12.0% | 16.0% | 12.0% | -9.0 | 0.16 | 0.81 | +7.4 | +5.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 20 | S_STRANGER | 69.0% | 15.0% | 20.0% | 10.0% | -10.0 | 0.18 | 0.71 | +7.4 | +6.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 29 | S_STRANGER | 100.0% | 10.3% | 13.8% | 10.3% | -8.2 | 0.15 | 0.92 | +7.2 | +6.2 |
| `feature_stale_hod_exhaustion_reject` | 29 | S_STRANGER | 100.0% | 10.3% | 13.8% | 10.3% | -8.2 | 0.15 | 0.92 | +7.2 | +6.2 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 10.3% | 0.0% | 0.0% | 0.0% | -3.1 | 0.00 | 0.00 | +6.8 | +4.1 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 3.4% | 0.0% | 0.0% | 0.0% | -6.4 | 0.00 | 0.00 | +4.9 | +8.8 |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=+8.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 40.0% | +2.1 | 1.86 | 4.64 | +13.2 | +6.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 40.0% | +2.1 | 1.86 | 4.64 | +13.2 | +6.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 40.0% | +2.1 | 1.86 | 4.64 | +13.2 | +6.9 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 40.0% | +2.1 | 1.86 | 4.64 | +13.2 | +6.9 |
| `asian_range_gte_30` | 7 | S_STRANGER | 70.0% | 14.3% | 28.6% | 28.6% | +3.3 | 2.00 | 4.00 | +12.2 | +7.6 |
| `confluence_gte_60` | 8 | S_STRANGER | 80.0% | 12.5% | 25.0% | 37.5% | +3.4 | 2.51 | 5.01 | +12.6 | +6.7 |
| `confluence_gte_70` | 5 | S_STRANGER | 50.0% | 20.0% | 40.0% | 60.0% | +8.8 | 25.47 | 12.74 | +18.5 | +5.8 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 57.1% | +5.2 | 12.42 | 37.27 | +15.6 | +5.4 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 42.9% | +3.1 | 2.17 | 8.69 | +15.0 | +6.1 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 70.0% | 14.3% | 28.6% | 28.6% | +3.3 | 2.00 | 4.00 | +12.2 | +7.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 50.0% | +9.6 | 28.39 | 56.79 | +15.6 | +5.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 40.0% | +2.1 | 1.86 | 4.64 | +13.2 | +6.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 20.0% | 40.0% | +2.1 | 1.86 | 4.64 | +13.2 | +6.9 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 33.3% | -5.2 | 0.00 | 0.00 | +4.2 | +11.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -7.8 | 0.00 | 0.00 | +2.8 | +10.4 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-4.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=4 Fav=25.0% Avg=-0.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -2.7 | 0.21 | 1.89 | +7.5 | +5.7 |
| `hunt_to_ar_ratio_le_2_0` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -1.9 | 0.39 | 1.94 | +10.0 | +5.7 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 60.0% | 16.7% | 16.7% | 0.0% | -1.9 | 0.39 | 1.94 | +10.0 | +5.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -2.7 | 0.21 | 1.89 | +7.5 | +5.7 |
| `asian_range_gte_30` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +8.0 | +3.6 |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -2.7 | 0.21 | 1.89 | +7.5 | +5.7 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -2.7 | 0.21 | 1.89 | +7.5 | +5.7 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 0.0% | -1.5 | 0.55 | 1.65 | +6.3 | +5.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 70.0% | 14.3% | 14.3% | 0.0% | -2.6 | 0.28 | 1.70 | +8.2 | +5.3 |
| `ratio_le_2_and_asian_gte_30` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -2.5 | 0.00 | 0.00 | +8.0 | +3.6 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.9 | 0.00 | 0.00 | +6.5 | +1.9 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -2.7 | 0.21 | 1.89 | +7.5 | +5.7 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 0.0% | -2.7 | 0.21 | 1.89 | +7.5 | +5.7 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -2.3 | 0.00 | 0.00 | +16.1 | +6.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -2.3 | 0.00 | 0.00 | +16.1 | +6.0 |

### THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-3.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -3.0 | 0.17 | 1.55 | +7.2 | +6.1 |
| `hunt_to_ar_ratio_le_2_0` | 4 | S_STRANGER | 40.0% | 25.0% | 25.0% | 25.0% | -2.0 | 0.44 | 1.33 | +4.4 | +5.5 |
| `hunt_to_ar_ratio_le_2_5` | 5 | S_STRANGER | 50.0% | 20.0% | 20.0% | 20.0% | -3.3 | 0.27 | 1.10 | +4.6 | +6.7 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -3.0 | 0.17 | 1.55 | +7.2 | +6.1 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -3.0 | 0.17 | 1.55 | +7.2 | +6.1 |
| `confluence_gte_70` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -3.3 | 0.00 | 0.00 | +7.2 | +5.2 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 0.0% | -4.1 | 0.00 | 0.00 | +7.1 | +6.1 |
| `tdi_rsi_gte_50` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -1.6 | 0.00 | 0.00 | +11.1 | +3.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 11.1% | 11.1% | 11.1% | -2.6 | 0.21 | 1.70 | +7.5 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 10.0% | 10.0% | 10.0% | -3.0 | 0.17 | 1.55 | +7.2 | +6.1 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -4.6 | 0.00 | 0.00 | +5.6 | +8.2 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFLICT|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`

Best-variant splits: train N=2 Fav=0.0% Avg=-4.2; validation N=2 Fav=0.0% Avg=-1.0; out_of_sample N=2 Fav=50.0% Avg=+3.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 9.1% | 18.2% | 18.2% | -1.6 | 0.52 | 2.08 | +9.3 | +6.7 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 90.9% | 10.0% | 20.0% | 20.0% | -1.6 | 0.55 | 1.91 | +9.8 | +7.2 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 9.1% | 18.2% | 18.2% | -1.6 | 0.52 | 2.08 | +9.3 | +6.7 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 9.1% | 18.2% | 18.2% | -1.6 | 0.52 | 2.08 | +9.3 | +6.7 |
| `asian_range_gte_30` | 7 | S_STRANGER | 63.6% | 14.3% | 28.6% | 14.3% | -1.1 | 0.72 | 1.79 | +11.0 | +6.9 |
| `confluence_gte_60` | 11 | S_STRANGER | 100.0% | 9.1% | 18.2% | 18.2% | -1.6 | 0.52 | 2.08 | +9.3 | +6.7 |
| `confluence_gte_70` | 11 | S_STRANGER | 100.0% | 9.1% | 18.2% | 18.2% | -1.6 | 0.52 | 2.08 | +9.3 | +6.7 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +6.3 | +6.2 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 54.5% | 16.7% | 16.7% | 16.7% | -0.4 | 0.79 | 3.96 | +10.7 | +4.4 |
| `ratio_le_2_and_asian_gte_30` | 7 | S_STRANGER | 63.6% | 14.3% | 28.6% | 14.3% | -1.1 | 0.72 | 1.79 | +11.0 | +6.9 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -0.5 | 0.00 | 0.00 | +6.3 | +6.2 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 9.1% | 18.2% | 18.2% | -1.6 | 0.52 | 2.08 | +9.3 | +6.7 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 9.1% | 18.2% | 18.2% | -1.6 | 0.52 | 2.08 | +9.3 | +6.7 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -4.2 | 0.00 | 0.00 | +3.5 | +7.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -4.2 | 0.00 | 0.00 | +3.5 | +7.0 |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=3 Fav=0.0% Avg=-2.2; validation N=4 Fav=25.0% Avg=-3.9; out_of_sample N=2 Fav=0.0% Avg=-2.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -3.1 | 0.05 | 0.56 | +5.2 | +5.2 |
| `hunt_to_ar_ratio_le_2_0` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -3.1 | 0.05 | 0.56 | +5.2 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -3.1 | 0.05 | 0.56 | +5.2 | +5.2 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -3.1 | 0.05 | 0.56 | +5.2 | +5.2 |
| `asian_range_gte_30` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 0.0% | -2.9 | 0.07 | 0.56 | +4.9 | +5.0 |
| `confluence_gte_60` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -3.1 | 0.05 | 0.56 | +5.2 | +5.2 |
| `confluence_gte_70` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -3.1 | 0.05 | 0.56 | +5.2 | +5.2 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 25.0% | 0.0% | 0.0% | 0.0% | -3.2 | 0.00 | 0.00 | +6.8 | +4.6 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 33.3% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +5.7 | +4.4 |
| `ratio_le_2_and_asian_gte_30` | 9 | S_STRANGER | 75.0% | 11.1% | 11.1% | 0.0% | -2.9 | 0.07 | 0.56 | +4.9 | +5.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -4.1 | 0.00 | 0.00 | +3.5 | +5.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -3.1 | 0.05 | 0.56 | +5.2 | +5.2 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 8.3% | 0.0% | -3.1 | 0.05 | 0.56 | +5.2 | +5.2 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +7.9 | +4.0 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +6.8 | +4.8 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=3 Fav=33.3% Avg=-2.9; validation N=4 Fav=0.0% Avg=-3.0; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -3.2 | 0.21 | 1.03 | +5.0 | +5.6 |
| `hunt_to_ar_ratio_le_2_0` | 7 | S_STRANGER | 58.3% | 0.0% | 14.3% | 0.0% | -3.9 | 0.12 | 0.75 | +4.9 | +5.3 |
| `hunt_to_ar_ratio_le_2_5` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -3.2 | 0.21 | 1.03 | +5.0 | +5.6 |
| `stop_hunt_le_90` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -3.2 | 0.21 | 1.03 | +5.0 | +5.6 |
| `asian_range_gte_30` | 8 | S_STRANGER | 66.7% | 12.5% | 25.0% | 12.5% | -3.8 | 0.25 | 0.74 | +4.2 | +6.4 |
| `confluence_gte_60` | 3 | S_STRANGER | 25.0% | 33.3% | 33.3% | 33.3% | -1.8 | 0.53 | 1.05 | +4.5 | +5.1 |
| `confluence_gte_70` | 1 | R_RUNNER | 8.3% | 100.0% | 100.0% | 100.0% | +6.0 | 999.00 | 999.00 | +7.7 | +3.4 |
| `tdi_rsi_gt_signal` | 1 | S_STRANGER | 8.3% | 0.0% | 0.0% | 0.0% | -3.0 | 0.00 | 0.00 | +8.7 | +3.0 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 58.3% | 14.3% | 14.3% | 14.3% | -3.0 | 0.22 | 1.35 | +6.9 | +6.1 |
| `ratio_le_2_and_asian_gte_30` | 5 | S_STRANGER | 41.7% | 0.0% | 20.0% | 0.0% | -4.8 | 0.14 | 0.56 | +2.8 | +6.7 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -3.2 | 0.21 | 1.03 | +5.0 | +5.6 |
| `feature_stale_hod_exhaustion_reject` | 12 | S_STRANGER | 100.0% | 8.3% | 16.7% | 8.3% | -3.2 | 0.21 | 1.03 | +5.0 | +5.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=100.0% Avg=+6.1; validation N=6 Fav=16.7% Avg=-10.7; out_of_sample N=6 Fav=0.0% Avg=-3.8.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -7.2 | 0.12 | 0.69 | +6.5 | +5.5 |
| `hunt_to_ar_ratio_le_2_0` | 22 | S_STRANGER | 91.7% | 9.1% | 13.6% | 13.6% | -7.7 | 0.12 | 0.63 | +6.7 | +5.2 |
| `hunt_to_ar_ratio_le_2_5` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -7.2 | 0.12 | 0.69 | +6.5 | +5.5 |
| `stop_hunt_le_90` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -7.2 | 0.12 | 0.69 | +6.5 | +5.5 |
| `asian_range_gte_30` | 16 | S_STRANGER | 66.7% | 12.5% | 18.8% | 12.5% | -7.9 | 0.15 | 0.55 | +7.0 | +5.4 |
| `confluence_gte_60` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -7.2 | 0.12 | 0.69 | +6.5 | +5.5 |
| `confluence_gte_70` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -7.2 | 0.12 | 0.69 | +6.5 | +5.5 |
| `tdi_rsi_gt_signal` | 21 | S_STRANGER | 87.5% | 9.5% | 14.3% | 14.3% | -6.1 | 0.15 | 0.75 | +6.8 | +5.3 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 37.5% | 11.1% | 11.1% | 11.1% | -2.0 | 0.25 | 1.78 | +8.9 | +6.3 |
| `ratio_le_2_and_asian_gte_30` | 16 | S_STRANGER | 66.7% | 12.5% | 18.8% | 12.5% | -7.9 | 0.15 | 0.55 | +7.0 | +5.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 13 | S_STRANGER | 54.2% | 15.4% | 23.1% | 15.4% | -6.2 | 0.22 | 0.58 | +7.5 | +5.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -7.2 | 0.12 | 0.69 | +6.5 | +5.5 |
| `feature_stale_hod_exhaustion_reject` | 24 | S_STRANGER | 100.0% | 8.3% | 12.5% | 12.5% | -7.2 | 0.12 | 0.69 | +6.5 | +5.5 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-3.7; validation N=3 Fav=33.3% Avg=+2.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 23.1% | 15.4% | -0.7 | 0.62 | 1.66 | +5.9 | +4.3 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 7.7% | 23.1% | 15.4% | -0.7 | 0.62 | 1.66 | +5.9 | +4.3 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 7.7% | 23.1% | 15.4% | -0.7 | 0.62 | 1.66 | +5.9 | +4.3 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 7.7% | 23.1% | 15.4% | -0.7 | 0.62 | 1.66 | +5.9 | +4.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 7.7% | 23.1% | 15.4% | -0.7 | 0.62 | 1.66 | +5.9 | +4.3 |
| `confluence_gte_70` | 9 | S_STRANGER | 69.2% | 0.0% | 11.1% | 22.2% | -1.6 | 0.31 | 1.84 | +5.2 | +5.0 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 61.5% | 12.5% | 12.5% | 12.5% | -1.4 | 0.41 | 2.44 | +4.2 | +4.7 |
| `tdi_rsi_gte_50` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 7.7% | 23.1% | 15.4% | -0.7 | 0.62 | 1.66 | +5.9 | +4.3 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 7.7% | 23.1% | 15.4% | -0.7 | 0.62 | 1.66 | +5.9 | +4.3 |
| `feature_momentum_breakout_exception` | 3 | S_STRANGER | 23.1% | 0.0% | 0.0% | 0.0% | -4.0 | 0.00 | 0.00 | +2.7 | +6.3 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=9 Fav=11.1% Avg=-0.5; validation N=1 Fav=0.0% Avg=-5.3; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 23.1% | -3.5 | 0.20 | 2.00 | +4.2 | +6.4 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 23.1% | -3.5 | 0.20 | 2.00 | +4.2 | +6.4 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 23.1% | -3.5 | 0.20 | 2.00 | +4.2 | +6.4 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 23.1% | -3.5 | 0.20 | 2.00 | +4.2 | +6.4 |
| `asian_range_gte_30` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 30.0% | -1.0 | 0.53 | 3.73 | +5.1 | +4.4 |
| `confluence_gte_60` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 23.1% | -3.5 | 0.20 | 2.00 | +4.2 | +6.4 |
| `confluence_gte_70` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 23.1% | -3.5 | 0.20 | 2.00 | +4.2 | +6.4 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 53.8% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +2.9 | +7.7 |
| `tdi_rsi_gte_50` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -6.0 | 0.00 | 0.00 | +2.4 | +8.3 |
| `ratio_le_2_and_asian_gte_30` | 10 | S_STRANGER | 76.9% | 10.0% | 10.0% | 30.0% | -1.0 | 0.53 | 3.73 | +5.1 | +4.4 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +3.4 | +5.3 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 23.1% | -3.5 | 0.20 | 2.00 | +4.2 | +6.4 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 23.1% | -3.5 | 0.20 | 2.00 | +4.2 | +6.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 30.8% | 0.0% | 0.0% | 25.0% | -3.0 | 0.00 | 0.00 | +4.1 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -1.5 | 0.00 | 0.00 | +2.2 | +2.2 |

### THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|NYC_REVERSAL|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=8 Fav=12.5% Avg=-3.8; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 0.0% | -5.6 | 0.19 | 2.29 | +9.7 | +13.3 |
| `hunt_to_ar_ratio_le_2_0` | 8 | S_STRANGER | 61.5% | 12.5% | 12.5% | 0.0% | -4.5 | 0.32 | 2.26 | +11.8 | +14.5 |
| `hunt_to_ar_ratio_le_2_5` | 9 | S_STRANGER | 69.2% | 11.1% | 11.1% | 0.0% | -4.7 | 0.29 | 2.31 | +11.4 | +14.7 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 0.0% | -5.6 | 0.19 | 2.29 | +9.7 | +13.3 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 3 | S_STRANGER | 23.1% | 33.3% | 33.3% | 0.0% | +3.3 | 2.36 | 4.71 | +15.8 | +16.8 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 0.0% | -16.7 | 0.00 | 0.00 | +5.0 | +19.3 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 100.0% | 7.7% | 7.7% | 0.0% | -5.6 | 0.19 | 2.29 | +9.7 | +13.3 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 12 | S_STRANGER | 92.3% | 8.3% | 8.3% | 0.0% | -5.8 | 0.20 | 2.19 | +10.3 | +13.6 |
| `feature_stale_hod_exhaustion_reject` | 8 | S_STRANGER | 61.5% | 12.5% | 12.5% | 0.0% | -3.8 | 0.36 | 2.51 | +10.1 | +14.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 6 | S_STRANGER | 46.2% | 0.0% | 0.0% | 0.0% | -7.2 | 0.00 | 0.00 | +10.7 | +13.0 |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=10 Fav=10.0% Avg=-0.0; validation N=11 Fav=9.1% Avg=+0.4; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 42 | S_STRANGER | 100.0% | 7.1% | 14.3% | 7.1% | -3.8 | 0.39 | 2.32 | +6.2 | +8.9 |
| `hunt_to_ar_ratio_le_2_0` | 41 | S_STRANGER | 97.6% | 7.3% | 14.6% | 7.3% | -3.6 | 0.40 | 2.35 | +6.3 | +8.8 |
| `hunt_to_ar_ratio_le_2_5` | 42 | S_STRANGER | 100.0% | 7.1% | 14.3% | 7.1% | -3.8 | 0.39 | 2.32 | +6.2 | +8.9 |
| `stop_hunt_le_90` | 42 | S_STRANGER | 100.0% | 7.1% | 14.3% | 7.1% | -3.8 | 0.39 | 2.32 | +6.2 | +8.9 |
| `asian_range_gte_30` | 38 | S_STRANGER | 90.5% | 7.9% | 13.2% | 7.9% | -3.6 | 0.40 | 2.61 | +6.3 | +9.1 |
| `confluence_gte_60` | 23 | S_STRANGER | 54.8% | 13.0% | 17.4% | 13.0% | -1.1 | 0.77 | 3.65 | +8.2 | +8.1 |
| `confluence_gte_70` | 1 | S_STRANGER | 2.4% | 0.0% | 0.0% | 0.0% | -5.7 | 0.00 | 0.00 | +3.4 | +6.1 |
| `tdi_rsi_gt_signal` | 23 | S_STRANGER | 54.8% | 8.7% | 17.4% | 8.7% | +0.3 | 1.10 | 5.22 | +7.3 | +7.9 |
| `tdi_rsi_gte_50` | 17 | S_STRANGER | 40.5% | 5.9% | 5.9% | 5.9% | -3.2 | 0.34 | 5.40 | +6.9 | +8.8 |
| `ratio_le_2_and_asian_gte_30` | 38 | S_STRANGER | 90.5% | 7.9% | 13.2% | 7.9% | -3.6 | 0.40 | 2.61 | +6.3 | +9.1 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 21 | S_STRANGER | 50.0% | 9.5% | 14.3% | 9.5% | +0.2 | 1.05 | 6.32 | +7.3 | +8.0 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 42 | S_STRANGER | 100.0% | 7.1% | 14.3% | 7.1% | -3.8 | 0.39 | 2.32 | +6.2 | +8.9 |
| `feature_stale_hod_exhaustion_reject` | 42 | S_STRANGER | 100.0% | 7.1% | 14.3% | 7.1% | -3.8 | 0.39 | 2.32 | +6.2 | +8.9 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 2.4% | 0.0% | 0.0% | 0.0% | -4.2 | 0.00 | 0.00 | +3.5 | +5.4 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|EARLY_WEEK|L0|STOP_HUNT|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=20.0% Avg=-1.3; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 0.0% | -1.3 | 0.06 | 0.78 | +4.0 | +3.9 |
| `hunt_to_ar_ratio_le_2_0` | 1 | S_STRANGER | 6.7% | 0.0% | 0.0% | 0.0% | -0.1 | 0.00 | 0.00 | +6.6 | +2.2 |
| `hunt_to_ar_ratio_le_2_5` | 6 | S_STRANGER | 40.0% | 16.7% | 16.7% | 0.0% | -1.4 | 0.12 | 0.61 | +4.5 | +5.0 |
| `stop_hunt_le_90` | 15 | S_STRANGER | 100.0% | 6.7% | 6.7% | 0.0% | -1.3 | 0.06 | 0.78 | +4.0 | +3.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 86.7% | 7.7% | 7.7% | 0.0% | -1.3 | 0.07 | 0.73 | +4.0 | +4.0 |
| `confluence_gte_70` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 53.3% | 12.5% | 12.5% | 0.0% | -1.3 | 0.11 | 0.74 | +3.2 | +4.2 |
| `tdi_rsi_gte_50` | 11 | S_STRANGER | 73.3% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +3.7 | +3.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 66.7% | 0.0% | 0.0% | 0.0% | -1.2 | 0.00 | 0.00 | +3.3 | +4.0 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 93.3% | 7.1% | 7.1% | 0.0% | -1.2 | 0.07 | 0.80 | +4.0 | +3.9 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 33.3% | 20.0% | 20.0% | 0.0% | -1.3 | 0.15 | 0.46 | +5.2 | +3.7 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -1.1 | 0.00 | 0.00 | +5.3 | +2.4 |

### THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=12.5% Avg=-2.2; validation N=2 Fav=0.0% Avg=-6.5; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -2.7 | 0.21 | 3.21 | +7.9 | +7.6 |
| `hunt_to_ar_ratio_le_2_0` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 33.3% | -4.7 | 0.00 | 0.00 | +10.9 | +6.1 |
| `hunt_to_ar_ratio_le_2_5` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 33.3% | -4.7 | 0.00 | 0.00 | +10.9 | +6.1 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -2.7 | 0.21 | 3.21 | +7.9 | +7.6 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -2.7 | 0.21 | 3.21 | +7.9 | +7.6 |
| `confluence_gte_70` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -2.7 | 0.21 | 3.21 | +7.9 | +7.6 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -2.7 | 0.21 | 3.21 | +7.9 | +7.6 |
| `tdi_rsi_gte_50` | 10 | S_STRANGER | 58.8% | 10.0% | 10.0% | 10.0% | -3.0 | 0.29 | 2.59 | +9.2 | +10.4 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +7.7 | +1.8 |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -2.7 | 0.21 | 3.21 | +7.9 | +7.6 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 5.9% | 5.9% | 11.8% | -2.7 | 0.21 | 3.21 | +7.9 | +7.6 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 11.8% | 0.0% | 0.0% | 0.0% | -1.8 | 0.00 | 0.00 | +7.7 | +1.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=6 Fav=16.7% Avg=-2.1; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 0.0% | -3.9 | 0.15 | 0.72 | +3.9 | +7.4 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 0.0% | -3.9 | 0.15 | 0.72 | +3.9 | +7.4 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 0.0% | -3.9 | 0.15 | 0.72 | +3.9 | +7.4 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 0.0% | -3.9 | 0.15 | 0.72 | +3.9 | +7.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 0.0% | -3.9 | 0.15 | 0.72 | +3.9 | +7.4 |
| `confluence_gte_70` | 13 | S_STRANGER | 76.5% | 7.7% | 15.4% | 0.0% | -2.0 | 0.26 | 1.43 | +3.8 | +5.7 |
| `tdi_rsi_gt_signal` | 6 | S_STRANGER | 35.3% | 16.7% | 16.7% | 0.0% | -2.1 | 0.29 | 1.47 | +3.6 | +8.3 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 41.2% | 14.3% | 14.3% | 0.0% | -3.8 | 0.16 | 0.97 | +3.8 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 0.0% | -3.9 | 0.15 | 0.72 | +3.9 | +7.4 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 5.9% | 17.6% | 0.0% | -3.9 | 0.15 | 0.72 | +3.9 | +7.4 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 5.9% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +2.0 | +4.8 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_CONFLICT|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFLICT|THE_33|CONF_50_74`

Best-variant splits: train N=6 Fav=16.7% Avg=-9.7; validation N=0 Fav=0.0% Avg=-; out_of_sample N=7 Fav=0.0% Avg=-5.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 17 | S_STRANGER | 100.0% | 5.9% | 11.8% | 5.9% | -8.7 | 0.06 | 0.45 | +6.2 | +13.4 |
| `hunt_to_ar_ratio_le_2_0` | 17 | S_STRANGER | 100.0% | 5.9% | 11.8% | 5.9% | -8.7 | 0.06 | 0.45 | +6.2 | +13.4 |
| `hunt_to_ar_ratio_le_2_5` | 17 | S_STRANGER | 100.0% | 5.9% | 11.8% | 5.9% | -8.7 | 0.06 | 0.45 | +6.2 | +13.4 |
| `stop_hunt_le_90` | 17 | S_STRANGER | 100.0% | 5.9% | 11.8% | 5.9% | -8.7 | 0.06 | 0.45 | +6.2 | +13.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 13 | S_STRANGER | 76.5% | 7.7% | 15.4% | 7.7% | -7.4 | 0.09 | 0.48 | +6.1 | +12.5 |
| `confluence_gte_70` | 4 | S_STRANGER | 23.5% | 0.0% | 25.0% | 0.0% | -5.2 | 0.03 | 0.08 | +4.8 | +6.6 |
| `tdi_rsi_gt_signal` | 3 | S_STRANGER | 17.6% | 0.0% | 0.0% | 0.0% | -17.5 | 0.00 | 0.00 | +5.2 | +18.6 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 76.5% | 0.0% | 0.0% | 0.0% | -11.4 | 0.00 | 0.00 | +4.8 | +16.1 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 17 | S_STRANGER | 100.0% | 5.9% | 11.8% | 5.9% | -8.7 | 0.06 | 0.45 | +6.2 | +13.4 |
| `feature_stale_hod_exhaustion_reject` | 17 | S_STRANGER | 100.0% | 5.9% | 11.8% | 5.9% | -8.7 | 0.06 | 0.45 | +6.2 | +13.4 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 23.5% | 0.0% | 25.0% | 0.0% | -10.4 | 0.01 | 0.04 | +7.6 | +14.3 |
| `feature_eurjpy_tdi50_reclaim` | 4 | S_STRANGER | 23.5% | 0.0% | 0.0% | 0.0% | -13.9 | 0.00 | 0.00 | +9.4 | +18.2 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=1 Fav=0.0% Avg=-29.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=12.5% Avg=-1.5.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 5.6% | 16.7% | 5.6% | -3.9 | 0.17 | 0.78 | +4.7 | +8.2 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 100.0% | 5.6% | 16.7% | 5.6% | -3.9 | 0.17 | 0.78 | +4.7 | +8.2 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 5.6% | 16.7% | 5.6% | -3.9 | 0.17 | 0.78 | +4.7 | +8.2 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 5.6% | 16.7% | 5.6% | -3.9 | 0.17 | 0.78 | +4.7 | +8.2 |
| `asian_range_gte_30` | 14 | S_STRANGER | 77.8% | 7.1% | 14.3% | 7.1% | -4.2 | 0.16 | 0.89 | +5.4 | +8.8 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 5.6% | 16.7% | 5.6% | -3.9 | 0.17 | 0.78 | +4.7 | +8.2 |
| `confluence_gte_70` | 14 | S_STRANGER | 77.8% | 7.1% | 21.4% | 0.0% | -2.4 | 0.29 | 1.07 | +4.7 | +6.4 |
| `tdi_rsi_gt_signal` | 11 | S_STRANGER | 61.1% | 9.1% | 18.2% | 0.0% | -4.7 | 0.18 | 0.82 | +4.4 | +9.4 |
| `tdi_rsi_gte_50` | 7 | S_STRANGER | 38.9% | 0.0% | 0.0% | 0.0% | -8.6 | 0.00 | 0.00 | +2.7 | +12.5 |
| `ratio_le_2_and_asian_gte_30` | 14 | S_STRANGER | 77.8% | 7.1% | 14.3% | 7.1% | -4.2 | 0.16 | 0.89 | +5.4 | +8.8 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 9 | S_STRANGER | 50.0% | 11.1% | 22.2% | 0.0% | -4.6 | 0.21 | 0.75 | +5.1 | +9.7 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 5.6% | 16.7% | 5.6% | -3.9 | 0.17 | 0.78 | +4.7 | +8.2 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 5.6% | 16.7% | 5.6% | -3.9 | 0.17 | 0.78 | +4.7 | +8.2 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=25.0% Avg=-1.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=2 Fav=0.0% Avg=-7.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 11.1% | -4.8 | 0.17 | 2.52 | +8.7 | +6.3 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 11.1% | -4.8 | 0.17 | 2.52 | +8.7 | +6.3 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 11.1% | -4.8 | 0.17 | 2.52 | +8.7 | +6.3 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 11.1% | -4.8 | 0.17 | 2.52 | +8.7 | +6.3 |
| `asian_range_gte_30` | 12 | S_STRANGER | 66.7% | 8.3% | 8.3% | 16.7% | -5.9 | 0.20 | 1.96 | +8.5 | +7.5 |
| `confluence_gte_60` | 15 | S_STRANGER | 83.3% | 6.7% | 6.7% | 13.3% | -5.4 | 0.18 | 2.28 | +9.7 | +7.0 |
| `confluence_gte_70` | 4 | S_STRANGER | 22.2% | 0.0% | 0.0% | 0.0% | -8.0 | 0.00 | 0.00 | +5.5 | +10.3 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 44.4% | 12.5% | 12.5% | 12.5% | -2.4 | 0.47 | 2.83 | +9.6 | +7.4 |
| `tdi_rsi_gte_50` | 13 | S_STRANGER | 72.2% | 7.7% | 7.7% | 7.7% | -3.6 | 0.27 | 2.96 | +9.7 | +6.9 |
| `ratio_le_2_and_asian_gte_30` | 12 | S_STRANGER | 66.7% | 8.3% | 8.3% | 16.7% | -5.9 | 0.20 | 1.96 | +8.5 | +7.5 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 6 | S_STRANGER | 33.3% | 16.7% | 16.7% | 16.7% | -3.2 | 0.48 | 2.39 | +12.0 | +9.1 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 11.1% | -4.8 | 0.17 | 2.52 | +8.7 | +6.3 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 11.1% | -4.8 | 0.17 | 2.52 | +8.7 | +6.3 |
| `feature_momentum_breakout_exception` | 5 | S_STRANGER | 27.8% | 0.0% | 0.0% | 20.0% | -1.6 | 0.00 | 0.00 | +6.4 | +3.1 |
| `feature_eurjpy_tdi50_reclaim` | 3 | S_STRANGER | 16.7% | 0.0% | 0.0% | 0.0% | -1.4 | 0.00 | 0.00 | +5.1 | +2.6 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=8 Fav=0.0% Avg=-15.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=8 Fav=12.5% Avg=-4.0.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 0.0% | -9.4 | 0.06 | 1.06 | +5.8 | +10.2 |
| `hunt_to_ar_ratio_le_2_0` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 0.0% | -9.4 | 0.06 | 1.06 | +5.8 | +10.2 |
| `hunt_to_ar_ratio_le_2_5` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 0.0% | -9.4 | 0.06 | 1.06 | +5.8 | +10.2 |
| `stop_hunt_le_90` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 0.0% | -9.4 | 0.06 | 1.06 | +5.8 | +10.2 |
| `asian_range_gte_30` | 17 | S_STRANGER | 94.4% | 5.9% | 5.9% | 0.0% | -9.5 | 0.07 | 1.05 | +5.6 | +10.3 |
| `confluence_gte_60` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 0.0% | -9.4 | 0.06 | 1.06 | +5.8 | +10.2 |
| `confluence_gte_70` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 0.0% | -9.4 | 0.06 | 1.06 | +5.8 | +10.2 |
| `tdi_rsi_gt_signal` | 17 | S_STRANGER | 94.4% | 5.9% | 5.9% | 0.0% | -9.6 | 0.06 | 1.03 | +6.1 | +10.3 |
| `tdi_rsi_gte_50` | 8 | S_STRANGER | 44.4% | 0.0% | 0.0% | 0.0% | -9.3 | 0.00 | 0.00 | +7.4 | +14.5 |
| `ratio_le_2_and_asian_gte_30` | 17 | S_STRANGER | 94.4% | 5.9% | 5.9% | 0.0% | -9.5 | 0.07 | 1.05 | +5.6 | +10.3 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 16 | S_STRANGER | 88.9% | 6.2% | 6.2% | 0.0% | -9.7 | 0.07 | 1.02 | +5.9 | +10.4 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 0.0% | -9.4 | 0.06 | 1.06 | +5.8 | +10.2 |
| `feature_stale_hod_exhaustion_reject` | 18 | S_STRANGER | 100.0% | 5.6% | 5.6% | 0.0% | -9.4 | 0.06 | 1.06 | +5.8 | +10.2 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 22.2% | 0.0% | 0.0% | 0.0% | -17.1 | 0.00 | 0.00 | +3.0 | +11.0 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=1 Fav=0.0% Avg=-1.2; validation N=4 Fav=0.0% Avg=+1.1; out_of_sample N=5 Fav=0.0% Avg=-4.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 30.0% | -1.8 | 0.20 | 1.21 | +6.1 | +6.9 |
| `hunt_to_ar_ratio_le_2_0` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 30.0% | -1.8 | 0.20 | 1.21 | +6.1 | +6.9 |
| `hunt_to_ar_ratio_le_2_5` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 30.0% | -1.8 | 0.20 | 1.21 | +6.1 | +6.9 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 30.0% | -1.8 | 0.20 | 1.21 | +6.1 | +6.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 30.0% | -1.8 | 0.20 | 1.21 | +6.1 | +6.9 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 30.0% | -1.8 | 0.20 | 1.21 | +6.1 | +6.9 |
| `tdi_rsi_gt_signal` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 30.0% | -1.8 | 0.20 | 1.21 | +6.1 | +6.9 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +4.1 | +9.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 30.0% | -1.8 | 0.20 | 1.21 | +6.1 | +6.9 |
| `feature_stale_hod_exhaustion_reject` | 10 | S_STRANGER | 100.0% | 0.0% | 10.0% | 30.0% | -1.8 | 0.20 | 1.21 | +6.1 | +6.9 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|...|TDI_SQUEEZE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|ACCUMULATION|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_SQUEEZE|THE_33|CONF_50_74`

Best-variant splits: train N=4 Fav=0.0% Avg=-3.1; validation N=0 Fav=0.0% Avg=-; out_of_sample N=1 Fav=0.0% Avg=-1.4.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -3.9 | 0.00 | 0.00 | +4.6 | +7.0 |
| `hunt_to_ar_ratio_le_2_0` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -3.9 | 0.00 | 0.00 | +4.6 | +7.0 |
| `hunt_to_ar_ratio_le_2_5` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -3.9 | 0.00 | 0.00 | +4.6 | +7.0 |
| `stop_hunt_le_90` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -3.9 | 0.00 | 0.00 | +4.6 | +7.0 |
| `asian_range_gte_30` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -3.9 | 0.00 | 0.00 | +4.6 | +7.0 |
| `confluence_gte_60` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +5.0 | +5.2 |
| `confluence_gte_70` | 1 | S_STRANGER | 9.1% | 0.0% | 0.0% | 0.0% | -0.7 | 0.00 | 0.00 | +1.3 | +6.1 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 0.0% | -3.6 | 0.00 | 0.00 | +4.3 | +6.5 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 45.5% | 0.0% | 0.0% | 0.0% | -2.8 | 0.00 | 0.00 | +5.0 | +5.2 |
| `ratio_le_2_and_asian_gte_30` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -3.9 | 0.00 | 0.00 | +4.6 | +7.0 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 7 | S_STRANGER | 63.6% | 0.0% | 0.0% | 0.0% | -3.6 | 0.00 | 0.00 | +4.3 | +6.5 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -3.9 | 0.00 | 0.00 | +4.6 | +7.0 |
| `feature_stale_hod_exhaustion_reject` | 11 | S_STRANGER | 100.0% | 0.0% | 0.0% | 9.1% | -3.9 | 0.00 | 0.00 | +4.6 | +7.0 |
| `feature_momentum_breakout_exception` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +4.5 | +3.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 18.2% | 0.0% | 0.0% | 0.0% | -1.3 | 0.00 | 0.00 | +4.5 | +3.0 |

### THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|...|TDI_NONE|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|MID_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|RRT|TDI_NONE|THE_33|CONF_75_PLUS`

Best-variant splits: train N=4 Fav=0.0% Avg=-6.5; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=0.0% Avg=-1.6.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +7.3 | +7.9 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 92.9% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +7.6 | +7.7 |
| `hunt_to_ar_ratio_le_2_5` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +7.3 | +7.9 |
| `stop_hunt_le_90` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +7.3 | +7.9 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +7.3 | +7.9 |
| `confluence_gte_70` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +7.3 | +7.9 |
| `tdi_rsi_gt_signal` | 9 | S_STRANGER | 64.3% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +8.1 | +6.3 |
| `tdi_rsi_gte_50` | 9 | S_STRANGER | 64.3% | 0.0% | 0.0% | 0.0% | -3.8 | 0.00 | 0.00 | +5.2 | +8.5 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -0.4 | 0.00 | 0.00 | +12.9 | +3.0 |
| `feature_extreme_hunt_with_exception` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +7.3 | +7.9 |
| `feature_stale_hod_exhaustion_reject` | 14 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -3.9 | 0.00 | 0.00 | +7.3 | +7.9 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.1% | 0.0% | 0.0% | 0.0% | -0.4 | 0.00 | 0.00 | +12.9 | +3.0 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 14.3% | 0.0% | 0.0% | 0.0% | -4.3 | 0.00 | 0.00 | +12.7 | +6.2 |

### THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|...|TDI_NONE|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|MID_WEEK|L0|TRUE_TREND|AR_VALID|HUNT_SOFT|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74`

Best-variant splits: train N=0 Fav=0.0% Avg=-; validation N=0 Fav=0.0% Avg=-; out_of_sample N=5 Fav=0.0% Avg=-3.3.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 7.7% | -5.6 | 0.00 | 0.00 | +5.6 | +9.2 |
| `hunt_to_ar_ratio_le_2_0` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 7.7% | -5.6 | 0.00 | 0.00 | +5.6 | +9.2 |
| `hunt_to_ar_ratio_le_2_5` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 7.7% | -5.6 | 0.00 | 0.00 | +5.6 | +9.2 |
| `stop_hunt_le_90` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 7.7% | -5.6 | 0.00 | 0.00 | +5.6 | +9.2 |
| `asian_range_gte_30` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 7.7% | -5.6 | 0.00 | 0.00 | +5.6 | +9.2 |
| `confluence_gte_60` | 12 | S_STRANGER | 92.3% | 0.0% | 0.0% | 8.3% | -5.7 | 0.00 | 0.00 | +5.8 | +9.6 |
| `confluence_gte_70` | 2 | S_STRANGER | 15.4% | 0.0% | 0.0% | 50.0% | -3.2 | 0.00 | 0.00 | +10.1 | +8.4 |
| `tdi_rsi_gt_signal` | 4 | S_STRANGER | 30.8% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +6.3 | +3.8 |
| `tdi_rsi_gte_50` | 5 | S_STRANGER | 38.5% | 0.0% | 0.0% | 0.0% | -3.3 | 0.00 | 0.00 | +5.1 | +6.0 |
| `ratio_le_2_and_asian_gte_30` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 7.7% | -5.6 | 0.00 | 0.00 | +5.6 | +9.2 |
| `ratio_le_2_asian_gte_30_tdi_positive` | 4 | S_STRANGER | 30.8% | 0.0% | 0.0% | 0.0% | -0.9 | 0.00 | 0.00 | +6.3 | +3.8 |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 7.7% | -5.6 | 0.00 | 0.00 | +5.6 | +9.2 |
| `feature_stale_hod_exhaustion_reject` | 13 | S_STRANGER | 100.0% | 0.0% | 0.0% | 7.7% | -5.6 | 0.00 | 0.00 | +5.6 | +9.2 |
| `feature_momentum_breakout_exception` | 1 | S_STRANGER | 7.7% | 0.0% | 0.0% | 0.0% | -4.5 | 0.00 | 0.00 | +2.9 | +4.5 |
| `feature_eurjpy_tdi50_reclaim` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |

### THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_50_74

Setup: `THE_33_MW|BUY|LATE_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Best-variant splits: train N=5 Fav=0.0% Avg=-3.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -6.6 | 0.00 | 0.00 | +4.6 | +13.4 |
| `hunt_to_ar_ratio_le_2_0` | 5 | S_STRANGER | 50.0% | 0.0% | 0.0% | 20.0% | -3.4 | 0.00 | 0.00 | +3.8 | +9.6 |
| `hunt_to_ar_ratio_le_2_5` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 14.3% | -6.5 | 0.00 | 0.00 | +4.9 | +13.5 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 10.0% | -6.6 | 0.00 | 0.00 | +4.6 | +13.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 11.1% | -5.7 | 0.00 | 0.00 | +4.3 | +12.3 |
| `confluence_gte_70` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -8.5 | 0.00 | 0.00 | +5.0 | +15.6 |
| `tdi_rsi_gt_signal` | 8 | S_STRANGER | 80.0% | 0.0% | 0.0% | 0.0% | -7.6 | 0.00 | 0.00 | +4.8 | +14.8 |
| `tdi_rsi_gte_50` | 3 | S_STRANGER | 30.0% | 0.0% | 0.0% | 0.0% | -5.5 | 0.00 | 0.00 | +4.5 | +15.2 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 11.1% | -7.2 | 0.00 | 0.00 | +4.6 | +13.6 |
| `feature_stale_hod_exhaustion_reject` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 11.1% | -7.2 | 0.00 | 0.00 | +4.6 | +13.6 |
| `feature_momentum_breakout_exception` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_eurjpy_tdi50_reclaim` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -1.0 | 0.00 | 0.00 | +4.5 | +11.6 |

### THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|...|TDI_CONFIRM|THE_33|CONF_75_PLUS

Setup: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS`

Best-variant splits: train N=7 Fav=0.0% Avg=-11.4; validation N=0 Fav=0.0% Avg=-; out_of_sample N=0 Fav=0.0% Avg=-.

| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `all` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -13.4 | 0.00 | 0.00 | +8.1 | +13.4 |
| `hunt_to_ar_ratio_le_2_0` | 1 | S_STRANGER | 10.0% | 0.0% | 0.0% | 0.0% | -5.3 | 0.00 | 0.00 | +23.4 | +5.6 |
| `hunt_to_ar_ratio_le_2_5` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -6.6 | 0.00 | 0.00 | +9.9 | +8.5 |
| `stop_hunt_le_90` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -13.4 | 0.00 | 0.00 | +8.1 | +13.4 |
| `asian_range_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `confluence_gte_60` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -13.4 | 0.00 | 0.00 | +8.1 | +13.4 |
| `confluence_gte_70` | 10 | S_STRANGER | 100.0% | 0.0% | 0.0% | 0.0% | -13.4 | 0.00 | 0.00 | +8.1 | +13.4 |
| `tdi_rsi_gt_signal` | 7 | S_STRANGER | 70.0% | 0.0% | 0.0% | 0.0% | -11.4 | 0.00 | 0.00 | +9.6 | +13.3 |
| `tdi_rsi_gte_50` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -15.2 | 0.00 | 0.00 | +8.2 | +17.7 |
| `ratio_le_2_and_asian_gte_30` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `ratio_le_2_asian_gte_30_tdi_positive` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_fresh_reclaim_within_8` | 0 | S_STRANGER | 0.0% | 0.0% | 0.0% | 0.0% | - | 0.00 | 0.00 | - | - |
| `feature_extreme_hunt_with_exception` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -16.5 | 0.00 | 0.00 | +8.8 | +12.2 |
| `feature_stale_hod_exhaustion_reject` | 9 | S_STRANGER | 90.0% | 0.0% | 0.0% | 0.0% | -14.4 | 0.00 | 0.00 | +7.4 | +14.2 |
| `feature_momentum_breakout_exception` | 4 | S_STRANGER | 40.0% | 0.0% | 0.0% | 0.0% | -10.4 | 0.00 | 0.00 | +5.1 | +12.8 |
| `feature_eurjpy_tdi50_reclaim` | 2 | S_STRANGER | 20.0% | 0.0% | 0.0% | 0.0% | -13.4 | 0.00 | 0.00 | +12.4 | +16.7 |

Research-only: a baseline-gate pass here still needs split confirmation before promotion.
