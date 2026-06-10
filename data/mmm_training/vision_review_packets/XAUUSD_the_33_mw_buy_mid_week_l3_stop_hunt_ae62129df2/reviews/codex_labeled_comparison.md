{
  "summary": "Winners were not defined by stop-hunt size; they either entered before daily expansion was exhausted or came from a fresh LOD/lower-range reclaim. Losers were mostly late top-side buys after HOD/ADR exhaustion, stale re-entries after the original W had already paid, or outright counter-bias breakdowns.",
  "winner_traits": [
    "Weekly and H4 context stayed BUY with confluence >= 95; H1 could be NEUTRAL and still work.",
    "Most winners had TDR <= 4400p and ADR% < 85 at snapshot.",
    "Continuation winners held above a rising 50 EMA with 5/13 EMA stacked or re-stacking upward.",
    "Late-session winners showed a fresh lower-range reclaim: sharp bullish close back above LOD/AR-low or EMA cluster after a flush.",
    "Small XAUUSD stop hunts still worked when reclaim quality was strong; C01 and C11 won with 413p and 612p hunts."
  ],
  "loser_traits": [
    "C02 and C09 were high-range exhaustion buys: ADR% > 100, large TDR, price near HOD/AR high, TDI overbought or curling down.",
    "C03 and C05 were late after a completed HOD run; the original W-bottom had already paid and current structure was chop/re-entry.",
    "C08 was a structural invalidation: H1/H4 SELL, weekly NEUTRAL, confluence 80, price breaking below LOD with bearish EMA structure.",
    "Losers often had price in the upper quarter of the visible range while TDI green/red were rolling down or below the yellow baseline."
  ],
  "filters_to_test": [
    {
      "name": "higher_tf_alignment_floor",
      "rule": "For BUY, reject if weekly_trend != BUY or h4_trend != BUY or confluence_score < 95.",
      "targets": ["C08"]
    },
    {
      "name": "large_range_exhaustion",
      "rule": "Reject BUY if TDR >= 5000p or ADR_pct >= 100, unless the last 4 candles include a bullish reclaim close from below LOD/AR-low back above EMA13 and EMA50.",
      "targets": ["C02", "C08", "C09"]
    },
    {
      "name": "stale_upper_quarter_buy",
      "rule": "Reject BUY when close_position_in_day_range >= 0.75, bars_since_hod_sweep <= 12, no fresh high breakout in last 3 candles, and either EMA5 <= EMA13 or TDI_green_slope_3 <= 0.",
      "targets": ["C02", "C03", "C09"]
    },
    {
      "name": "post_hod_reentry_requires_reclaim",
      "rule": "If price dropped >= 0.30 * asian_range from HOD after the stop-hunt run, allow BUY only when a candle within the last 4 bars closes above EMA13 and EMA50 with body >= 0.5 * ATR14 and TDI_green_slope_3 > 0.",
      "targets": ["C05"],
      "keeps": ["C01", "C11"]
    },
    {
      "name": "below_lod_bear_stack_reject",
      "rule": "Reject BUY if close < LOD - 0.05 * asian_range and EMA5 < EMA13 < EMA50 with EMA13_slope_5 < 0.",
      "targets": ["C08"]
    }
  ],
  "filters_to_reject": [
    "Do not reject solely on small stop_hunt_pips; C01 and C11 were profitable with sub-1000p hunts.",
    "Do not reject all Friday entries; C11 was a Friday winner when weekly/H4 stayed BUY.",
    "Do not reject all RSI_OVERBOUGHT or TDI divergence; C07 and C06 still won.",
    "Do not reject solely on asian_range_pips > 5000; C04, C10, and C11 show range size alone is not enough."
  ],
  "pair_specific_notes": [
    "For XAUUSD, raw stop-hunt size is less useful than current-day exhaustion. TDR >= 5000p and ADR% >= 100 were stronger warning signals in this packet.",
    "The main visual split is not W-bottom detection; it is whether the current BUY is fresh/reclaiming or stale after the HOD expansion.",
    "Use EAT reporting for session buckets; loser snapshots clustered around 12:00-18:30 EAT, but late entries can still win when they reclaim LOD cleanly."
  ],
  "uncertain_items": [
    "C05 hit T1 then breakeven, so it may be more of a management failure than a bad entry.",
    "C01 was profitable without T1 and visually late; treat it as a weak winner when optimizing.",
    "C10 winner versus C03 loser on the same large-hunt day suggests bars_since_original_W and bars_since_HOD_sweep are critical features."
  ],
  "next_backtest_spec": {
    "scope": "XAUUSD only, same normalized setup signature, archived pair-study records plus this packet.",
    "features": [
      "TDR_pips",
      "ADR_pct",
      "close_position_in_day_range",
      "close_position_in_asian_range",
      "bars_since_hod_sweep",
      "bars_since_lod_reclaim",
      "bars_since_first_close_above_ema50_after_hunt",
      "EMA5_EMA13_EMA50_stack",
      "EMA13_slope_5",
      "TDI_green_slope_3",
      "TDI_green_vs_red",
      "TDI_green_vs_yellow",
      "last_4_bars_reclaim_body_ATR_ratio"
    ],
    "tests": [
      "baseline signature",
      "higher_tf_alignment_floor",
      "large_range_exhaustion",
      "stale_upper_quarter_buy",
      "post_hod_reentry_requires_reclaim",
      "all_filters_combined"
    ],
    "metrics": [
      "favorable_rate",
      "avg_exit_pips",
      "t1_rate",
      "avg_mae",
      "validation_split_passes",
      "out_of_sample_passes"
    ]
  }
}