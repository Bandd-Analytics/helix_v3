{
  "summary": "Winners were not simply the cleanest-looking charts. The stronger separator was a fresh low-side sweep followed by reclaim or stabilization with TDI turning up. Losers were mostly buys after upper-range/HOD rejection, bearish TDI rollover, or an oversized hunt relative to a tight Asian range.",
  "winner_traits": [
    "Stop hunt size stayed pair-normalized: winners were 32p-62p and <=1.45x Asian range.",
    "Price showed low-side sweep/reclaim or basing before entry, even when the W was visually imperfect.",
    "TDI green was rising, crossing up, or at least not sharply falling at entry.",
    "Upper-range winners still had bullish momentum confirmation: fast EMA reclaim and TDI support.",
    "Most winners had low early adverse excursion, suggesting entries were near a defended low or fresh reclaim."
  ],
  "loser_traits": [
    "C03/C04 had 115p hunts against a 26p Asian range, an overextended displacement rather than a controlled GBPJPY hunt.",
    "C02/C03/C04/C08 showed TDI rollover or sharp green-line decline at the signal.",
    "Losers often triggered after HOD/upper-range rejection instead of after a fresh low-side reclaim.",
    "Several loser entries were below or losing the fast EMA cluster with bearish short-term candle structure.",
    "The W-bottom label alone was not reliable when the current leg was already rolling down."
  ],
  "filters_to_test": [
    {
      "name": "oversized_hunt_block",
      "rule": "Reject GBPJPY BUY if stop_hunt_pips > 80 OR stop_hunt_pips / asian_range_pips > 2.0.",
      "evidence": "Blocks C03/C04; keeps all labeled winners including the 62p winner C06."
    },
    {
      "name": "tdi_upturn_gate",
      "rule": "Require TDI green current >= 45 and either green_slope_3bars >= 0 or green crossed above red within the last 3 closed M15 candles. Reject if green_slope_3bars < 0 and green < red.",
      "evidence": "Losers had visible TDI rollover; winners had rising, crossing, or stable recovery."
    },
    {
      "name": "fresh_low_reclaim_gate",
      "rule": "Require a low-side sweep below Asian low or current LOD within the last 24 M15 candles, followed by at least 2 closes back above Asian low and current close >= Asian_low + 0.10 * Asian_range_pips.",
      "evidence": "Separates low-reclaim winners from C02-style entries still breaking down at LOD."
    },
    {
      "name": "post_hod_rollover_block",
      "rule": "Reject BUY if price tagged HOD, Asian high, or R1 within the last 12 M15 candles, then made a lower high/lower low sequence and closed below EMA13 and EMA34 while TDI green_slope_3bars < 0.",
      "evidence": "Targets C02/C03/C04/C08 without rejecting upper-range winners that still had momentum."
    },
    {
      "name": "upper_range_momentum_condition",
      "rule": "If close_position_in_asian_range > 0.70, require close > EMA13 and EMA34, EMA13_slope_3bars > 0, EMA34_slope_3bars >= 0, and TDI green >= red.",
      "evidence": "Upper-zone buys worked only when momentum was still supportive."
    },
    {
      "name": "w_or_base_confirmation",
      "rule": "After the low sweep, require either two swing lows separated by 3-20 candles with second_low >= first_low - 0.25 * Asian_range_pips, or at least 3 consecutive candles with non-lower lows before entry.",
      "evidence": "Keeps early but constructive winners like C10 while rejecting single-sweep/no-reclaim attempts."
    }
  ],
  "filters_to_reject": [
    "Do not require stop_hunt_pips <= 45; C06 won with 62p and C09/C10 won near 46p.",
    "Do not reject all neutral-looking TDI; C01/C06 were profitable despite not being strongly bullish.",
    "Do not require a fully completed textbook W-bottom; C10 was early but profitable.",
    "Do not block every upper-range or HOD-adjacent BUY; C01/C05/C07 still worked when recovery/momentum conditions held.",
    "Do not reject solely because Weekly is SELL; the whole packet is counter-weekly and still contains six winners."
  ],
  "pair_specific_notes": [
    "GBPJPY needs pair-normalized hunt filters: 30p-60p can be normal, but 115p against a 26p Asian range was structurally abnormal.",
    "Use both absolute pips and hunt_to_asian_range ratio; pips alone would misclassify valid wider GBPJPY setups.",
    "For this signature, TDI_NONE in the stored label hides useful signal quality; visible TDI slope should be encoded as a derived feature."
  ],
  "uncertain_items": [
    "C01 and C06 were visually weak but profitable, so filters should avoid overfitting to textbook W-bottom appearance.",
    "Exact EMA names/colors must be mapped from chart code before encoding EMA13/EMA34/EMA50 conditions.",
    "The sample is small; thresholds should be validated on all GBPJPY matches before promotion."
  ],
  "next_backtest_spec": {
    "universe": "All GBPJPY flashcards matching THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND and close variants.",
    "features": [
      "stop_hunt_pips",
      "asian_range_pips",
      "hunt_to_ar_ratio",
      "bars_since_low_sweep",
      "close_position_in_asian_range",
      "reclaim_close_count",
      "bars_since_hod_or_ar_high_tag",
      "EMA13/EMA34 close relation and 3-bar slopes",
      "TDI green/red values, cross state, and 3-bar slopes",
      "two-swing-low or 3-candle-base confirmation"
    ],
    "tests": [
      "Run each proposed filter as a single ablation.",
      "Run stacked gates: oversized_hunt_block + tdi_upturn_gate + fresh_low_reclaim_gate.",
      "Run conditional upper-range gate only when close_position_in_asian_range > 0.70."
    ],
    "metrics": [
      "N",
      "favorable_rate",
      "avg_exit_pips",
      "median_exit_pips",
      "avg_MFE",
      "avg_MAE",
      "T1_hit_rate"
    ],
    "validation": "Use chronological split with out-of-sample report; promote only if favorable_rate and avg_exit_pips improve without collapsing sample size."
  }
}