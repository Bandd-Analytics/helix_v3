{
  "summary": "Winners were mostly moderate-hunt reclaim or fresh momentum-breakout buys; losers clustered around oversized hunts, stale HOD/top entries, and choppy range recovery with bearish TDI. TDI conflict alone is not enough to reject this signature.",
  "winner_traits": [
    "Best winners had stop_hunt_pips <= 60 or hunt_to_expected_level_move <= 0.60: C03, C05, C07, C08, C10, C11.",
    "Clean reclaim from LOD/AR-low with room back through the Asian range worked well: C05, C07, C10, C11.",
    "Fresh breakout can still win even with shark-fin/overbought labels when there is strong price expansion and no bearish signal/MBL cross: C03, C08, C10.",
    "Oversized hunts only survived in this packet when weekly_trend was BUY, asian_range_pips was small, and VB squeeze was present: C04, C06."
  ],
  "loser_traits": [
    "Extreme hunt size without the weekly/VB/small-range exception failed: C01, C09, C13.",
    "Late buys near HOD after a full expansion plus bearish TDI rollover were dangerous: C12, C13.",
    "Range-bound recoveries with weak second leg and bearish MBL/signal state failed: C01, C02.",
    "Large adverse losers often had little immediate upside: C09 MFE 1.8p, C13 MFE 8.4p, C02 MFE 6.3p."
  ],
  "filters_to_test": [
    {
      "name": "moderate_hunt_primary_allow",
      "rule": "For GBPJPY BUY setups, prefer stop_hunt_pips <= 60 OR hunt_to_expected_level_move <= 0.60.",
      "expected_effect": "Keeps C03,C05,C07,C08,C10,C11; needs top-exhaustion guard for C12."
    },
    {
      "name": "extreme_hunt_reject_with_exception",
      "rule": "Reject if stop_hunt_pips >= 90 OR hunt_to_expected_level_move >= 0.90, unless weekly_trend == BUY AND tdi_vb_squeeze == true AND asian_range_pips <= 30.",
      "expected_effect": "Rejects C01,C09,C13; preserves C04,C06."
    },
    {
      "name": "stale_hod_exhaustion_reject",
      "rule": "Reject BUY if close is within 10 pips of current HOD or range_pos >= 0.85, price has travelled >= 1.5 * asian_range_pips from hunt low, and TDI contains SIGNAL_CROSS_BEARISH or MBL_CROSS_BEARISH.",
      "expected_effect": "Targets C12,C13 without rejecting fresh shark-fin winners C03,C08."
    },
    {
      "name": "fresh_reclaim_required",
      "rule": "After BUY stop hunt, require within 8 M15 candles: one close back above AR_L, then one close above AR_mid or EMA50, with no close back below AR_L before entry.",
      "expected_effect": "Separates clean W/reclaim winners from C01,C02 style chop."
    },
    {
      "name": "momentum_breakout_exception",
      "rule": "Allow entries above AR_H/HOD only if bars_since_first_AR_H_break <= 6, last swing-low-to-close impulse >= 0.6 * asian_range_pips, and TDI does not contain SIGNAL_CROSS_BEARISH or MBL_CROSS_BEARISH.",
      "expected_effect": "Preserves C03,C08,C10 while rejecting stale HOD failures."
    }
  ],
  "filters_to_reject": [
    "Reject all TDI shark-fin or overbought signals: contradicted by winners C03,C04,C05,C06,C08,C10.",
    "Reject all bearish signal crosses: contradicted by winners C07 and C11.",
    "Reject all weekly SELL buys: contradicted by C03,C05,C07,C08,C10,C11.",
    "Reject all HOD/AR-high breakouts: contradicted by fresh breakout winners C03,C08,C10.",
    "Use advisory_grade == AVOID as a reject filter: all packet examples were AVOID."
  ],
  "pair_specific_notes": [
    "GBPJPY tolerates 33-60p hunts well when reclaim is clean; >90p hunts need stricter context.",
    "Use both absolute pips and range-normalized ratios because GBPJPY volatility shifts by session.",
    "C12 had +28.5p MFE but closed as a loser, so some failures may be exit-management failures rather than pure entry failures."
  ],
  "uncertain_items": [
    "Sample is small and includes same-session duplicates: C04/C06 and C05/C07.",
    "The oversized-hunt exception may be overfit until tested on more GBPJPY weeks.",
    "Clean W-bottom and second-leg quality need objective swing/close definitions before promotion."
  ],
  "next_backtest_spec": {
    "scope": "All GBPJPY samples matching this exact setup signature, then adjacent THE_33_MW BUY early-week L3 signatures.",
    "features_to_add": [
      "range_pos = (entry_close - asian_low) / asian_range",
      "distance_to_hod_pips",
      "distance_from_hunt_low_pips",
      "bars_since_stop_hunt_low",
      "bars_since_first_ar_high_break",
      "close_above_ar_mid_within_8_bars",
      "tdi_bearish_signal_count",
      "ema50_reclaim_before_entry"
    ],
    "ablations": [
      "moderate_hunt_primary_allow",
      "extreme_hunt_reject_with_exception",
      "stale_hod_exhaustion_reject",
      "fresh_reclaim_required",
      "momentum_breakout_exception",
      "combined_rule_set"
    ],
    "metrics": [
      "sample_count",
      "favorable_rate",
      "avg_exit_pips",
      "avg_mfe_pips",
      "avg_mae_pips",
      "t1_hit_rate",
      "rejected_winner_count",
      "accepted_loser_count"
    ]
  }
}