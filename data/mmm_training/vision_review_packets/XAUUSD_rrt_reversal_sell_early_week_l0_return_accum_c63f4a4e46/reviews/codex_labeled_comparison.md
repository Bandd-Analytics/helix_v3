{
  "summary": "For this XAUUSD RRT sell signature, winners were not simply the cleanest bearish-looking charts. The best separators were post-HOD/AR-high rejection with room to LOD, acceptance back below AR high/mid, and no immediate bullish reclaim after the signal. Losers clustered around late sells into exhausted lows, bullish TDI/reclaim conditions, noisy Friday/chop, or sells taken while price was still holding above AR mid/high.",
  "winner_traits": [
    "Sell appears after a HOD/AR-high/weekly-open-high sweep or rejection, then price closes back inside or below the Asian range.",
    "There is measurable downside room: entry is usually above AR low/LOD with at least 0.35x Asian range remaining to AR low or prior LOD.",
    "Post-signal candles show bearish acceptance: at least 2 of next 4 M15 candles close below signal close or below fast EMA.",
    "Short EMAs roll down or fan bearish after the signal, even when TDI initially conflicts.",
    "Profitable examples often tolerate TDI bullish-divergence labels if price has just rejected a premium level and is losing AR mid/high."
  ],
  "loser_traits": [
    "Late sell after price is already at or below AR low/LOD, especially with TDI curling up from oversold.",
    "Price holds above AR mid/high after the sell signal or reclaims cyan EMA before breaking lower.",
    "Clean bullish expansion or W-bottom/reclaim structure appears before the sell has produced continuation.",
    "Very choppy wide-wick range with no fresh bearish displacement after signal.",
    "Friday or stale late-session sells inside congestion performed poorly in this packet."
  ],
  "filters_to_test": [
    {
      "name": "require_downside_room",
      "rule": "For SELL, reject if entry_price <= asian_low + 0.15 * asian_range_pips, unless the next 2 M15 candles close below asian_low by >= 0.10 * asian_range_pips.",
      "reason": "Blocks late sells into LOD/AR-low exhaustion while allowing true breakdown continuation."
    },
    {
      "name": "premium_rejection_required",
      "rule": "Require the stop-hunt high or recent swing high within last 24 M15 candles to be >= asian_high - 0.10 * asian_range_pips or above HOD/previous HOD, followed by a close back below asian_high.",
      "reason": "Winners commonly started from a premium sweep/rejection rather than mid-range chop."
    },
    {
      "name": "post_signal_bearish_acceptance",
      "rule": "Within 4 candles after signal, require at least 2 bearish closes and lowest close <= signal_close - max(80 pips, 0.12 * asian_range_pips).",
      "reason": "Separates active markdown from stale signals that drift or reverse."
    },
    {
      "name": "block_fast_bullish_reclaim",
      "rule": "Reject if within 3 candles after signal price closes above both fast EMA and medium/cyan EMA, unless a later candle breaks below signal_low by >= 100 pips.",
      "reason": "Losers often reclaimed structure quickly after the sell."
    },
    {
      "name": "block_oversold_floor_sell",
      "rule": "Reject if TDI green is below 32 or rising from below 32 and entry_price is within 0.20 * asian_range_pips of AR low/LOD.",
      "reason": "Late oversold-floor sells underperformed."
    },
    {
      "name": "friday_chop_guard",
      "rule": "For Friday SELL signals, require a close below AR low by >= 0.10 * asian_range_pips within 3 candles; otherwise reject.",
      "reason": "The Friday packet example was range-bound and stale without clean breakdown."
    }
  ],
  "filters_to_reject": [
    {
      "name": "reject_all_tdi_bullish_divergence",
      "reason": "Too broad. Several winners carried bullish-divergence or TDI-conflict labels but still paid after premium rejection and bearish acceptance."
    },
    {
      "name": "reject_all_w_bottom_or_recovery",
      "reason": "Some profitable examples began after recovery-looking structures; require failed reclaim or fresh breakdown instead."
    },
    {
      "name": "reject_asian_range_gt_1000p",
      "reason": "Wide range alone is not decisive for XAUUSD; use range-relative location and post-signal acceptance instead."
    }
  ],
  "pair_specific_notes": [
    "XAUUSD needs larger absolute buffers than FX majors; use max(absolute pips, range-relative threshold).",
    "TDI labels are noisy on gold after stop hunts; price acceptance around HOD/AR levels is more useful than TDI label alone.",
    "Avoid selling gold at the floor unless it immediately expands below AR low."
  ],
  "uncertain_items": [
    "Whether session time itself matters beyond Friday/chop needs a larger sample.",
    "The exact EMA definitions should be taken from stored fields or chart renderer metadata before encoding EMA reclaim filters.",
    "Need verify whether HOD/LOD labels in packets are current-day only or include rolling session state."
  ],
  "next_backtest_spec": {
    "dataset": "XAUUSD signatures matching RRT_REVERSAL|SELL|EARLY_WEEK|L0|RETURN_ACCUM",
    "labels": "existing MMM event outcomes with favorable if exit_pips > 0 or t1_hit=true",
    "features": [
      "entry_position_in_asian_range",
      "distance_to_ar_low_pips",
      "distance_to_hod_or_ar_high_pips",
      "recent_stop_hunt_above_ar_high_or_hod",
      "next_4_candle_bearish_acceptance",
      "fast_and_cyan_ema_reclaim_within_3_candles",
      "tdi_green_below_32_and_rising",
      "weekday",
      "asian_range_pips"
    ],
    "test_filters": [
      "require_downside_room",
      "premium_rejection_required",
      "post_signal_bearish_acceptance",
      "block_fast_bullish_reclaim",
      "block_oversold_floor_sell",
      "friday_chop_guard"
    ],
    "metrics": [
      "kept_count",
      "filtered_count",
      "favorable_rate",
      "avg_exit_pips",
      "avg_mfe_pips",
      "avg_mae_pips",
      "t1_hit_rate"
    ]
  }
}