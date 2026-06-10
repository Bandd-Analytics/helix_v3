Now I have all 13 charts reviewed. Let me synthesize the answer key against both blind reviews and the visual evidence.

**Answer Key Summary:**
- **Winners (8/13 = 61.5%):** C02 (+1321p), C03 (+1346p), C05 (+257p), C07 (+540p), C08 (+426p), C09 (+291p), C10 (+1644p), C12 (+945p)
- **Losers (5/13 = 38.5%):** C01 (0p BE), C04 (-389p), C06 (-60p), C11 (-341p), C13 (-414p)

**Blind Review Accuracy:** Codex 10/13 (77%), Claude 8/13 (62%). Both over-predicted losers — Claude especially penalized TDI conflict which was present in 5/8 actual winners.

```json
{
  "summary": "XAUUSD RRT_REVERSAL SELL mid-week with TDI_CONFLICT and NO_MW shows 61.5% win rate (8/13) with outsized winners (avg +846p) vs moderate losers (avg -241p). The TDI conflict flag is noise for this signature — 5 of 8 winners had shark_fin_long or signal_cross_bullish at entry. The dominant separator is whether price is breaking DOWN from HOD/AR_high through AR_mid with bearish displacement candles (winners) versus selling into exhaustion near LOD or into a bullish recovery bounce (losers). Both blind reviewers systematically over-weighted TDI conflict as a reject signal and missed that price structure overrides lagging TDI on XAUUSD RRT reversals.",
  "winner_traits": [
    "Price touched or breached HOD/AR_high earlier in session before sell entry — visible in C02, C03, C07, C08, C09, C10, C12",
    "Bearish displacement candle(s) breaking below AR_mid or 50 EMA at or just before entry — C03, C07, C09, C10, C12 show clean breakdown bars",
    "Price is at or below AR_mid at entry with bearish candle bodies (not just wicks) — all 8 winners",
    "Low MAE relative to MFE: winner avg MAE 106p vs avg MFE 943p (ratio ~0.11), meaning initial adverse excursion was controlled",
    "ADR% between 29-85% — no ADR% ceiling killed winners; C10 won +1644p at ADR% 85.4%",
    "TDI RSI 37-48 at entry (below 50) with green line trending down or flat — even when HUD labels shark_fin_long",
    "Entry during London or early NYC session after Asian range has been established and breached on high side",
    "C12 vs C11 (same day, 90min apart): later entry after spike noise settled and orderly lower-high formed was the winner"
  ],
  "loser_traits": [
    "Price rebounding FROM LOD or near AR_low at entry — C04 (V-recovery from LOD), C06 (near LOD after completed drop), C13 (LOD sweep then bounce)",
    "Green/bullish candles at right edge of chart at entry — C01 (pressing back toward HOD), C04 (sharp green bars), C11 (parabolic bullish spike)",
    "TDI RSI >= 55 at entry for sells — C01 had RSI 59, only loser with RSI clearly above 50; but RSI alone is not the separator",
    "Entry after impulsive move already exhausted — C06 entered after main selloff completed, C13 after LOD sweep, C11 into explosive bullish move",
    "High MAE relative to MFE: loser avg MAE 356p vs avg MFE 89p (ratio ~4.0) — adverse excursion overwhelmed any favorable move immediately",
    "Asian range oversized (C01: 945p vs 878p avg; C04: 1777p vs 1553p avg) correlated with choppier price action but was not decisive alone"
  ],
  "filters_to_test": [
    {
      "id": "F1_PRICE_BELOW_AR_MID_WITH_BEARISH_BODY",
      "description": "At entry, the last closed M15 candle body must close below AR_mid AND the candle must be bearish (close < open). Rejects sells where price is still above AR_mid or candle is green.",
      "threshold": "candle_close < ar_mid AND candle_close < candle_open",
      "expected_impact": "Would have rejected C01 (price pressing above AR mid with green candles), C04 (green candles above AR mid at bounce), C11 (price above AR mid after spike). Keeps all 8 winners where price was at/below AR mid with red candles.",
      "winners_kept": 8,
      "losers_rejected": 3
    },
    {
      "id": "F2_NO_SELL_INTO_LOD_BOUNCE",
      "description": "Reject sell if price touched current LOD within last 6 M15 candles AND the last 2 candles made higher lows. Prevents selling into V-recovery from LOD.",
      "threshold": "if any of last 6 candles made LOD AND last_2_candles_higher_lows: reject",
      "expected_impact": "Would reject C04 (LOD sweep then higher lows), C06 (at LOD after drop, bouncing), C13 (LOD sweep then partial recovery). No winners had this pattern.",
      "winners_kept": 8,
      "losers_rejected": 3
    },
    {
      "id": "F3_HOD_TOUCHED_SAME_SESSION",
      "description": "Require that price touched within 200p of current HOD during the same trading session (London or NYC) before accepting sell. Confirms high-side liquidity was taken.",
      "threshold": "session_high >= (current_hod - 200) within current London/NYC session",
      "expected_impact": "Winners C02,C03,C07,C08,C09,C10,C12 all show HOD touch in session. C05 also touched. Losers C06 (entered after selloff, no fresh HOD touch) and C13 (entered after LOD sweep, HOD was earlier) would be rejected.",
      "winners_kept": 8,
      "losers_rejected": 2
    },
    {
      "id": "F4_REJECT_IMPULSIVE_BULLISH_CANDLE",
      "description": "Reject sell if any of the last 3 M15 candles has a bullish body > 300p (XAUUSD pips). Prevents entering against parabolic spikes.",
      "threshold": "max(bullish_body_size, last_3_candles) < 300 pips",
      "expected_impact": "Would reject C11 (massive bullish spike candle > 500p body). Might also flag C04. No winners had impulsive bullish candles of this magnitude at entry.",
      "winners_kept": 8,
      "losers_rejected": 2
    },
    {
      "id": "F5_CONSECUTIVE_BEARISH_CLOSE_BELOW_EMA50",
      "description": "Require at least 2 of the last 3 M15 candles to close below EMA50 before accepting sell. Confirms momentum has shifted below the fast average.",
      "threshold": "count(candle_close < ema50, last_3_candles) >= 2",
      "expected_impact": "Winners show price below EMA50 with continuation. C01 (price above EMA50 pressing toward HOD), C04 (bouncing above EMA50), C11 (above EMA50 after spike) would be rejected.",
      "winners_kept": 7,
      "losers_rejected": 3
    },
    {
      "id": "F6_RSI_BELOW_55_FOR_SELL",
      "description": "Reject sell entries when TDI RSI > 55. High RSI on a sell = momentum still favors bulls.",
      "threshold": "tdi_rsi <= 55",
      "expected_impact": "Rejects C01 (RSI 59), C05 (RSI 57). But C05 was a winner (+257p TARGET_2), so this filter has a false positive. Net effect uncertain.",
      "winners_kept": 7,
      "losers_rejected": 1
    }
  ],
  "filters_to_reject": [
    {
      "id": "REJECT_TDI_CONFLICT_AS_HARD_BLOCK",
      "reason": "TDI conflict (shark_fin_long, signal_cross_bullish) was present in 5 of 8 winners. Using TDI conflict as a hard blocker would have eliminated 62.5% of profitable trades including the largest winners (C10: +1644p, C03: +1346p, C02: +1321p). TDI lags XAUUSD RRT reversals — the price displacement from HOD is the leading signal, TDI catches up later."
    },
    {
      "id": "REJECT_ADR_PCT_ABOVE_80_AS_HARD_BLOCK",
      "reason": "C10 won +1644p at ADR% 85.4%. XAUUSD can extend well beyond 1x ADR on reversal days. ADR% ceiling is not a valid rejection threshold for this signature."
    },
    {
      "id": "REJECT_RETURN_INSIDE_ASIAN_RANGE_AS_REQUIREMENT",
      "reason": "Both Codex and Claude disagreed on this field across examples. Asian range is extremely wide on XAUUSD (628-2339p), making 'inside Asian range' an unreliable binary. Price position relative to AR_mid is the useful derivative, not the boolean."
    }
  ],
  "pair_specific_notes": [
    "XAUUSD Asian ranges in this sample averaged 700-2800p — far wider than any forex pair. The AR_mid level is the actionable reference, not AR_high/low boundaries.",
    "Stop hunt magnitudes ranged 200-3600p — the system-detected stop hunt size does not correlate with outcome. Small hunts (C09: 205p) and large hunts (C08: 3607p) both won.",
    "XAUUSD RRT sells can produce extreme MFE (C10: 2292p, C03: 1981p) suggesting trailing stops should be wider than default 100/80p profile. Consider 200/150p for this signature.",
    "TDI shark_fin_long was present on 4/5 losers BUT also on 4/8 winners. It is not a separator — it reflects the upside leg that precedes the RRT reversal. The RRT turn invalidates the shark fin.",
    "C11 vs C12 same-day case study: the 90-minute later entry (C12) after the impulsive spike settled produced +945p vs -341p. For spike-type RRT, waiting for post-spike compression is critical on XAUUSD."
  ],
  "uncertain_items": [
    "F6 (RSI < 55 for sell) rejected one winner (C05 at RSI 57 won +257p). Need larger sample to determine if RSI 55-60 is genuinely dangerous or if C05 was an outlier where weekly SELL bias overrode.",
    "Whether 'return_inside_asian_range' should be measured relative to AR_mid or AR_low — both blind reviewers disagreed frequently on this flag.",
    "C08 won +426p despite dual TDI conflict (signal_cross_bullish + shark_fin_long) and no clean stop hunt per Codex. Need to determine if the HOD-to-EMA50 breakdown is sufficient without a formal stop hunt breach.",
    "Whether Asian range size > 2x AvgAsia should be a soft penalty rather than a hard blocker — C01 (945p, AvgAsia 878p) and C04 (1777p, AvgAsia 1553p) both lost but sample is too small."
  ],
  "next_backtest_spec": {
    "pair": "XAUUSD",
    "signature": "RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM",
    "filters_to_implement": ["F1_PRICE_BELOW_AR_MID_WITH_BEARISH_BODY", "F2_NO_SELL_INTO_LOD_BOUNCE", "F3_HOD_TOUCHED_SAME_SESSION", "F4_REJECT_IMPULSIVE_BULLISH_CANDLE"],
    "filters_deferred": ["F5_CONSECUTIVE_BEARISH_CLOSE_BELOW_EMA50", "F6_RSI_BELOW_55_FOR_SELL"],
    "test_period_days": 365,
    "minimum_sample_target": 30,
    "metrics_to_track": ["win_rate_with_each_filter", "profit_factor", "avg_mae_reduction", "winners_preserved_pct", "sharpe_ratio"],
    "control_group": "same signature without new filters",
    "trail_stop_override": {"activate_pips": 200, "trail_pips": 150},
    "notes": "F1+F2 together should eliminate the 3 worst losers (C04, C06, C13) while preserving all 8 winners. F3+F4 provide secondary protection against C11-type spike entries. Test each filter independently first, then combine. Do NOT use TDI conflict as a hard blocker."
  }
}
```
