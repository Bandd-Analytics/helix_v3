{
  "summary": "In this small GBPJPY sample, winners were not separated by visual prettiness of the W-bottom alone. The better separator was whether the BUY snapshot occurred after price had re-accepted the Asian range or weekly-open band with tolerable stop-hunt size, while losers were either oversized trend-move hunts or late/chase entries near HOD after expansion.",
  "winner_traits": [
    "Price usually reclaimed or was very near AR low / weekly open low before the snapshot.",
    "Best winners had max adverse under 6p, suggesting entry after support acceptance rather than before the low finished forming.",
    "Winners tolerated ugly or bearish-looking right-edge TDI if price was sitting at LOD/AR-low support after a prior expansion.",
    "Several winners had stop-hunt size roughly 38p-63p; GBPJPY can still win slightly above 60p, so a hard 60p reject is too strict.",
    "Winning continuations often occurred after L3 expansion then pullback into AR low / EMA200 / weekly-open support, not only from textbook W-bottoms."
  ],
  "loser_traits": [
    "C02/C06 shared the same 115p stop-hunt reading, likely too large for a GBPJPY MMM hunt and closer to trend displacement.",
    "Losers showed weak follow-through despite apparent AR reclaim; MFE stayed modest and no T1 hit.",
    "C04 was a late BUY after a vertical run into/near HOD with no fresh low-side reset, producing stale exit rather than continuation.",
    "Losers were more often entries after the move had already expanded, without a nearby support retest holding."
  ],
  "filters_to_test": [
    {
      "name": "cap_extreme_hunt_size",
      "rule": "For GBPJPY BUY THE_33 stop-hunt setups, reject if stop_hunt_pips >= 90p.",
      "rationale": "Both 115p examples lost; winners reached only 63p max in this set."
    },
    {
      "name": "prefer_low_adverse_acceptance",
      "rule": "Require current close to be within 12p above AR low or weekly_open_low after reclaim, or within 8p above current LOD after a bullish close.",
      "rationale": "Most higher-quality winners had MAE <= 6p; avoid entries too far from the support being defended."
    },
    {
      "name": "block_hod_chase",
      "rule": "Reject BUY if current close is within 20p of current HOD and price has moved >= 0.75 * asian_range_pips upward from AR low in the prior 8 M15 candles, unless a pullback of at least 0.35 * asian_range_pips has held above AR mid.",
      "rationale": "C04 failed as a late HOD/vertical-push entry."
    },
    {
      "name": "range_reacceptance",
      "rule": "Require at least one M15 candle close back above AR low or weekly_open_low within the last 4 candles after the stop-hunt low.",
      "rationale": "Winners generally had price back at/inside the working range before follow-through."
    },
    {
      "name": "freshness_of_hunt",
      "rule": "Require stop-hunt low to occur within the last 24 M15 candles, or require a later retest of AR low/weekly_open_low within 10p before entry.",
      "rationale": "Avoid stale signals where expansion has already completed and the current edge is unrelated to the hunt."
    },
    {
      "name": "tdi_bullish_recovery_soft_gate",
      "rule": "Score up, not hard-gate, when TDI green is rising and either crosses red upward or is above 50 within last 3 candles.",
      "rationale": "TDI helped in C07/C11 but would wrongly reject winners like C08/C10 if used as a hard filter."
    }
  ],
  "filters_to_reject": [
    {
      "name": "hard_reject_tdi_below_50",
      "reason": "Would reject winners C08 and C10."
    },
    {
      "name": "hard_reject_stop_hunt_over_60p",
      "reason": "Would reject winner C08/C10 at 63p; use a higher cap around 90p for GBPJPY research."
    },
    {
      "name": "require_textbook_clean_w_bottom",
      "reason": "Several winners were not visually clean W-bottoms at the right edge."
    },
    {
      "name": "reject_all_entries_below_ar_mid",
      "reason": "Some winners formed from AR-low/LOD support before reclaiming AR mid."
    }
  ],
  "pair_specific_notes": [
    "GBPJPY volatility makes 40p-65p hunts viable; 100p+ hunts look suspect for this signature.",
    "Because GBPJPY often expands fast after London/early-week stop hunts, support retest location appears more useful than TDI neatness.",
    "Use EAT session labels in reports, but encode rules from UTC snapshot/candle data consistently."
  ],
  "uncertain_items": [
    "Sample is only 11 examples with 3 losers, so thresholds should be treated as hypotheses.",
    "C04 was flat stale exit, not a meaningful adverse loser; it may represent opportunity-cost filtering more than risk filtering.",
    "Need OHLC-derived measurements for exact AR position, candle count since hunt, and distance from HOD/LOD before finalizing."
  ],
  "next_backtest_spec": {
    "dataset": "GBPJPY flashcards matching THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74",
    "labels": "favorable if exit_pips > 0 or t1_hit true; failed if exit_pips <= 0",
    "features_to_add": [
      "stop_hunt_pips",
      "candles_since_hunt_low",
      "close_distance_to_ar_low_pips",
      "close_distance_to_ar_mid_pips",
      "close_distance_to_hod_pips",
      "prior_8_candle_up_move_pips",
      "pullback_from_hod_pips",
      "tdi_green_slope_3",
      "tdi_green_minus_red",
      "close_above_weekly_open_low"
    ],
    "test_grid": {
      "stop_hunt_cap_pips": [70, 80, 90, 100],
      "max_distance_above_ar_low_pips": [8, 12, 16],
      "freshness_candles": [12, 24, 36],
      "hod_chase_distance_pips": [15, 20, 25]
    },
    "primary_metric": "favorable_rate with min_total >= 20",
    "secondary_metrics": ["avg_exit_pips", "median_mae_pips", "t1_hit_rate"]
  }
}