Now I have all 15 charts inspected alongside the answer key. Let me compile the analysis.

**Winners (8):** C04 (+322p), C06 (+710p), C07 (+501p), C08 (+722p), C09 (+199p), C10 (+150p), C12 (+1065p), C13 (+333p)
**Losers (7):** C01 (-41p), C02 (-123p), C03 (-15p), C05 (-39p), C11 (-8p), C14 (-358p), C15 (-45p)

```json
{
  "summary": "XAUUSD RRT sell setups with TDI_CONFLICT and NO_MW show 8/15 win rate (53%) but winners massively outpace losers on R:R (avg winner +500p vs avg loser -90p). The primary separator is NOT TDI state or divergence (present in both camps) but entry position relative to the Asian range and whether the bearish displacement is active vs exhausted. Winners enter at or above AR mid/high after a fresh HOD rejection or lower-high formation. Losers enter at or below AR low into exhausted moves where price is basing at support. RSI above 52 with bullish TDI cross while selling is the single strongest loser predictor (C14: -358p). Both blind reviews scored poorly (Codex 53%, Claude 47%), confirming this signature is genuinely hard to classify without positional context.",
  "winner_traits": [
    "Entry at or above Asian range midpoint — price is rejecting from AR high/HOD, not basing at AR low",
    "Fresh bearish displacement candles visible at entry (large-body red candles from highs, not small-body chop at lows)",
    "Price just formed a lower-high below prior HOD or AR high within the last 2-4 candles before entry",
    "Short EMAs (yellow 21/red 8) crossing DOWN through or already below cyan 50 EMA at entry",
    "ADR% under 60% at entry time (room for continuation) OR displacement happening in real-time (ADR% rising with price falling)",
    "Stop hunt sweep above AR high followed by rejection candle back inside range (C12: +1065p, C06: +710p)",
    "Weekly context SELL (MID_WEEK) aligned with the entry direction in 7/8 winners",
    "RSI 36-48 typical at entry but position matters more than absolute level"
  ],
  "loser_traits": [
    "Entry at or below Asian range low — selling into existing support/LOD with no fresh breakdown",
    "TDI green line curling upward from oversold (32-40 zone) at entry — momentum reverting against the sell",
    "RSI above 50 while selling (C14: RSI 57 = -358p loss, C10 exception at RSI 56 won because it was AT the HOD not below it)",
    "Price compressed in tight sideways base at LOD after a completed markdown — exhaustion, not continuation",
    "No clear bearish displacement candle in the 2 candles preceding entry — choppy dojis/small bodies only",
    "Wide-wick whipsaw candles dominating the Asian range (C15: Friday noise, -45p)",
    "TDI VB Squeeze + Signal Cross Bullish at entry = worst outcomes (C14: -358p)",
    "Friday entries with no clean breakdown structure (C15 stale exit)"
  ],
  "filters_to_test": [
    {
      "id": "F1_ENTRY_VS_AR_MID",
      "description": "Reject RRT sell if entry price is below Asian range midpoint AND last 3 candles show no bearish displacement (no candle body > 150p)",
      "threshold": "entry_price < AR_mid AND max_candle_body_last_3 < 150 pips",
      "rationale": "5/7 losers entered below AR mid into support. Winners at or above AR mid entered during active displacement.",
      "expected_impact": "Blocks C01, C05, C11, C15. Preserves all 8 winners."
    },
    {
      "id": "F2_TDI_BULLISH_CROSS_BLOCK",
      "description": "Reject RRT sell if TDI shows Signal Cross Bullish AND RSI > 52 at entry",
      "threshold": "tdi_state == SIGNAL_CROSS_BULLISH AND rsi > 52",
      "rationale": "C14 (RSI 57, Signal Cross Bullish) = worst loss at -358p. Selling into confirmed bullish TDI momentum.",
      "expected_impact": "Blocks C14. No winners had this combination."
    },
    {
      "id": "F3_TDI_RECOVERY_FROM_OVERSOLD",
      "description": "Reject sell if TDI green is rising (current > 2 bars ago) AND RSI was below 36 within last 4 bars AND current RSI > 40",
      "threshold": "tdi_green_rising_3bar AND rsi_min_last_4 < 36 AND rsi_current > 40",
      "rationale": "Losers C01, C03, C05 showed TDI snapping back from deep oversold. Winners with low RSI were still in active decline, not recovering.",
      "expected_impact": "Blocks C01, C05. May also catch C03 (stale exit despite 312p MFE)."
    },
    {
      "id": "F4_LOWER_HIGH_REQUIRED",
      "description": "Require that price formed a lower-high within last 6 M15 candles (a candle high is below the highest high of the prior 8 candles by at least 100p, then price fell)",
      "threshold": "lower_high_formed_in_last_6_bars AND lower_high_delta >= 100 pips below swing high",
      "rationale": "Winners consistently showed a lower-high rejection pattern before entry (C04, C06, C08, C10, C12, C13). Losers entered flat/basing zones or rising sequences.",
      "expected_impact": "Preserves C04, C06, C07, C08, C10, C12, C13. May block C02, C11, C15."
    },
    {
      "id": "F5_ADR_PCT_EXHAUSTION",
      "description": "Reject sell if ADR% > 70% AND entry price is below AR low (move already consumed, selling at the floor)",
      "threshold": "adr_pct > 70 AND entry_price < ar_low",
      "rationale": "When >70% of ADR is consumed and price is already at lows, continuation probability drops. C04 at 73% ADR% won but entered ABOVE AR mid (recovery sell).",
      "expected_impact": "Blocks C03 (stale exit), C05. Preserves C04 (above AR mid), C06 (63% ADR% at AR mid)."
    },
    {
      "id": "F6_FRIDAY_RRT_SELL_BLOCK",
      "description": "Block RRT sell entries on Friday unless a clean AR low break occurred (close below AR low within last 3 candles)",
      "threshold": "day_of_week == FRIDAY AND no_close_below_ar_low_last_3_bars",
      "rationale": "C15 (Friday) had wide-wick chop with no directional commitment. End-of-week positioning creates noise.",
      "expected_impact": "Blocks C15 (-45p). No winners in this set were Friday entries."
    },
    {
      "id": "F7_FRESH_DISPLACEMENT_CANDLE",
      "description": "Require at least one bearish candle with body >= 200p in the 4 candles before entry (confirms active selling pressure)",
      "threshold": "max_bearish_body_last_4_bars >= 200 pips",
      "rationale": "Winners show decisive bearish candles before/at entry. Losers show indecisive small bodies. C08 (+722p) had massive displacement. C11 (-8p) had flat compression.",
      "expected_impact": "Preserves C04, C06, C07, C08, C09, C12, C13. Blocks C01, C02, C11, C15."
    }
  ],
  "filters_to_reject": [
    {
      "id": "R1_BLOCK_ALL_TDI_BULLISH_DIVERGENCE",
      "description": "Blanket block on TDI bullish divergence for sells",
      "reason": "Winners C06 (+710p), C08 (+722p), and C13 (+333p) all had TDI bullish divergence at entry yet were among the best performers. The divergence was overridden by strong positional context (HOD rejection, fresh displacement). Blocking all divergence sells would cut 3 of the 8 winners (37.5%)."
    },
    {
      "id": "R2_BLOCK_RSI_BELOW_40",
      "description": "Blanket block on RSI below 40 for sells",
      "reason": "Winners C08 (RSI 36, +722p), C09 (RSI 42 but near 40), C12 (RSI 38, +1065p) entered with RSI in the 36-42 range. Low RSI during active displacement is valid. The key is whether RSI is falling (good) or recovering (bad), not the absolute level."
    },
    {
      "id": "R3_BLOCK_WIDE_ASIAN_RANGE_GT_1000",
      "description": "Hard block on Asian range above 1000p",
      "reason": "C04 (AR 1091p, +322p) and C10 (AR 1170p, +150p) both won with wide Asian ranges. The wide range correlates with large price moves which can still produce profitable sells if entry is at the upper portion of the range."
    },
    {
      "id": "R4_BLOCK_IF_PRICE_BELOW_ASIAN_LOW",
      "description": "Blanket block if entry price is below Asian low",
      "reason": "C07 (+501p) and C08 (+722p) entered below the Asian low during heavy displacement and caught massive continuation. The filter is too broad — what matters is whether the displacement is active (good) or exhausted (bad)."
    }
  ],
  "pair_specific_notes": [
    "XAUUSD RRT sells with TDI_CONFLICT are inherently noisy — 53% win rate but positive expectancy due to outsized winners (avg +500p vs avg -90p losers). Manage for R:R, not hit rate.",
    "Gold's pip scale (200-500p hunt range) means 'tight' Asian ranges of 460-600p produce the cleanest setups. Ranges >800p often coincide with prior displacement already consumed.",
    "Stop hunt sizes of 377-795p on winners vs 593-1772p on losers suggest moderate hunt sizes (300-800p) are more reliable than extreme hunts (>1000p) which indicate prior volatility exhaustion.",
    "THE 33 setup type is present on all 15 charts — this signature fires frequently on XAUUSD and needs positional filtering to be useful.",
    "Weekly context SELL with MID_WEEK timing produced best results. Weekly NEUTRAL context (C01, C03, C04, C13) was mixed."
  ],
  "uncertain_items": [
    "C03 had max_favorable of 312p but exited as STALE_EXIT at -15p. The entry may have been valid but trade management (90-min stale rule) killed it. Unclear if this is an entry quality issue or a management issue specific to high-volatility gold.",
    "C10 won (+150p) despite RSI 56, bullish TDI, and wide AR 1170p — because it entered at the HOD. One example is insufficient to validate 'sell at HOD despite bullish TDI' as a reliable pattern for XAUUSD.",
    "TDI bullish divergence appeared in 3 winners and 3 losers — it has no predictive power for this signature. May need a secondary qualifier (e.g., divergence + price above AR mid = keep, divergence + price below AR low = block).",
    "C07 blind reviews both predicted loser but it won +501p. Entry was after a massive drop with price at LOD and TDI MBL Cross Bullish — looks like a loser visually but caught a fresh continuation leg. ADR% of only 22.6% (early in the day's range) may be the key differentiator."
  ],
  "next_backtest_spec": {
    "pair": "XAUUSD",
    "signature": "RRT_REVERSAL|SELL|EARLY_WEEK|L0|RETURN_ACCUM",
    "test_period": "2022-01-01 to 2024-12-31",
    "sample_target": 50,
    "filters_to_ablate": [
      {
        "filter_id": "F1_ENTRY_VS_AR_MID",
        "implementation": "if entry_price < asian_range_mid and max(abs(c.close - c.open) for c in last_3_candles) < 150_pips_in_points: REJECT",
        "metric": "compare win_rate and avg_favorable_pips with/without filter"
      },
      {
        "filter_id": "F2_TDI_BULLISH_CROSS_BLOCK",
        "implementation": "if tdi_state == 'SIGNAL_CROSS_BULLISH' and rsi > 52: REJECT",
        "metric": "losses_avoided vs winners_lost"
      },
      {
        "filter_id": "F4_LOWER_HIGH_REQUIRED",
        "implementation": "scan last 6 M15 bars for swing_high that is >= 100p below the highest high of prior 8 bars, followed by a lower close",
        "metric": "precision improvement on entry quality"
      },
      {
        "filter_id": "F7_FRESH_DISPLACEMENT_CANDLE",
        "implementation": "if max(bearish_body for c in last_4_candles) < 200_pips_in_points: REJECT",
        "metric": "stale_exit_rate reduction and avg_max_favorable improvement"
      }
    ],
    "combined_filter_test": "Apply F1 + F2 + F7 together and measure: (a) remaining sample size, (b) win rate change, (c) expectancy per trade change, (d) max consecutive loss reduction",
    "control_group": "Unfiltered signature baseline from same period"
  }
}
```
