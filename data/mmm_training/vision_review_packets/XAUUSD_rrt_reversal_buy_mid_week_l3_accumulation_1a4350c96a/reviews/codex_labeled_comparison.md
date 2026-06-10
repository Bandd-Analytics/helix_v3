{
  "summary": "Keyed separation is mostly weekly alignment plus enough XAU intraday expansion, not simple visual lateness. In this packet, weekly_trend=BUY plus ADR% >= 35 kept all 7 winners and rejected all 4 losers; the lone weekly-BUY loser, C09, was a low-expansion HOD squeeze/stall.",
  "winner_traits": [
    "All winners had weekly_trend=BUY and h4_trend=BUY.",
    "All winners had confluence_score >= 80 and advisory_confidence_score >= 75.",
    "Winners tolerated visually extended entries near HOD when the day had already expanded enough.",
    "TDI state varied: overbought, shark-fin-long, MBL cross, and sub-50 RSI all appeared in winners, so TDI context mattered more than raw RSI level.",
    "Winners generally had larger XAU range context: manifest asian_range_pips >= 1280."
  ],
  "loser_traits": [
    "Three of four losers had weekly_trend=NEUTRAL: C05, C07, C11.",
    "Neutral-week losers were recycled same-day XAU buy attempts around HOD/weekly-open resistance or after distribution.",
    "C09 was the exception: weekly BUY, but ADR% was only 28.4 with VB squeeze and visible HOD exhaustion/stall.",
    "Small manifest asian_range_pips separated C05, C07, and C11, but not C09.",
    "Low RSI alone did not define losers; C10 won with RSI 45/42."
  ],
  "filters_to_test": [
    {
      "name": "primary_xau_weekly_expansion_gate",
      "rule": "For this BUY signature, keep only rows where weekly_trend == 'BUY' and adr_percent_at_snapshot >= 35.0.",
      "sample_effect": "Kept C01,C02,C03,C04,C06,C08,C10; rejected C05,C07,C09,C11."
    },
    {
      "name": "xau_asian_range_floor",
      "rule": "Require asian_range_pips >= 1200 for XAUUSD.",
      "sample_effect": "Kept all winners; rejected C05,C07,C11; C09 still passed."
    },
    {
      "name": "score_floor_raise",
      "rule": "Raise gate from CONF_75_PLUS to confluence_score >= 80 and advisory_confidence_score >= 75.0.",
      "sample_effect": "Kept all winners; rejected C05 and C11; needs weekly/expansion filters for C07 and C09."
    },
    {
      "name": "stale_hod_squeeze_reject",
      "rule": "Reject when tdi_vb_squeeze == true, range_position >= 0.75, and failed_hod_rejection_count_last_12 >= 3. range_position = (close - day_lod) / (day_hod - day_lod). Count a failed HOD rejection when high is within 0.10 * asian_range_pips of day_hod and the candle closes in its lower half or has upper_wick >= 1.5 * body.",
      "sample_effect": "Targets C09-style weekly-BUY stall without rejecting the visible winners."
    },
    {
      "name": "low_rsi_context_gate",
      "rule": "Do not reject tdi_rsi < 50 by itself. If tdi_rsi < 50, allow only when weekly_trend == 'BUY' and range_position <= 0.45 or a BUY stop_hunt_detected reclaim is active; otherwise reject.",
      "sample_effect": "Protects C10 while rejecting neutral low-RSI failures like C05 and C11."
    }
  ],
  "filters_to_reject": [
    "Rejecting RSI > 65 or TDI overbought for buys: C01 was the largest winner.",
    "Rejecting RSI < 48 for buys: C10 was a winner.",
    "Rejecting wide Asian ranges above 1400p or 2000p: multiple winners had large XAU range context.",
    "Requiring h1_trend == BUY: several winners had h1_trend=NEUTRAL, while C07 lost with h1_trend=BUY.",
    "Requiring a clean W-bottom or M/W pattern: the shared signature is NO_MW and still produced winners."
  ],
  "pair_specific_notes": [
    "Use XAUUSD pip scale; do not port forex thresholds directly.",
    "For this XAU signature, insufficient daily expansion looked worse than visual extension.",
    "Weekly NEUTRAL was the clearest structural warning in this packet.",
    "C05 is labeled loser despite T1_hit and breakeven exit, so report both net-profit and T1-hit variants."
  ],
  "uncertain_items": [
    "Only 11 examples and 4 losers; C09 is the only weekly-BUY loser, so the VB/HOD-stall rule may overfit.",
    "Some chart text labels overlap; prefer manifest fields and OHLC recomputation for asian_range_pips and ADR%.",
    "Failed-HOD rejection count must be encoded from candles if arrow annotations are not stored."
  ],
  "next_backtest_spec": {
    "selection": "XAUUSD only, exact shared setup signature, M15 snapshots.",
    "labeling": "Primary favorable = exit_pips > 0; secondary report includes t1_hit and breakeven-after-T1 as separate class.",
    "features": [
      "weekly_trend",
      "h4_trend",
      "h1_trend",
      "confluence_score",
      "advisory_confidence_score",
      "asian_range_pips",
      "adr_percent_at_snapshot",
      "tdi_vb_squeeze",
      "tdi_rsi",
      "range_position",
      "failed_hod_rejection_count_last_12"
    ],
    "threshold_sweeps": {
      "adr_percent_at_snapshot": [30, 35, 40, 45],
      "asian_range_pips": [1000, 1200, 1400, 1800],
      "failed_hod_rejection_count_last_12": [2, 3, 4],
      "range_position": [0.7, 0.75, 0.8]
    },
    "ablation_order": [
      "baseline exact signature",
      "weekly_trend == BUY",
      "weekly_trend == BUY and adr_percent_at_snapshot >= 35",
      "add asian_range_pips >= 1200",
      "add score_floor_raise",
      "add stale_hod_squeeze_reject"
    ],
    "report": "For each gate, output N, favorable_rate, avg_exit_pips, median_exit_pips, avg_MFE, avg_MAE, T1_rate, and retained_examples."
  }
}