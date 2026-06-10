Now I have all the visual and quantitative data. Let me compile the comparison analysis.

```json
{
  "summary": "6 winners vs 5 losers on XAUUSD THE_33 MW BUY mid-week L3 stop-hunt setups. The primary separator is ADR exhaustion at entry: both worst losers (C02, C09) had ADR% >100%, meaning the daily move was already spent. Secondary separators are weekly bias alignment (NEUTRAL weekly killed C08), Asian range bloat (C09 at 1.78x AvgAsia), and entry position relative to the range—winners entered near LOD/weekly-open with room to expand, while losers entered near HOD into exhausted moves. Winner MAE averaged 77p vs loser MAE averaging 917p (excluding C05). TDI overbought at BUY entry correlated with failure when combined with high ADR%. Blind review accuracy: Codex 6/11 (55%), Claude 8/11 (73%). Both missed C01 (visually messy HOD-rejection appearance but entered at LOD for recovery).",
  "winner_traits": [
    "ADR% at entry <= 82% in all 6 cases (range 18.9–81.1%, mean 42.9%)",
    "Max adverse excursion (MAE) under 225p in all cases; 5/6 under 102p (mean 77p)",
    "T1 hit in 5/6 winners (83%), confirming early momentum",
    "Entry near or below LOD / weekly open level, giving 1000+ pip room to HOD",
    "EMA 5/13/50 stacked bullish or clearly recovering at entry candle",
    "TDI green recovering from lower band or crossing up through midline (RSI 49–64 range)",
    "Weekly bias = BUY in all 6 cases, no exceptions",
    "Stop hunt magnitude >= 413p in all cases; 5/6 had >= 1462p",
    "Asian range near or below AvgAsia (no bloated sessions)"
  ],
  "loser_traits": [
    "ADR% > 100% in 2/5 losers (C02=116.8%, C09=125.5%) — daily range fully consumed before entry",
    "Asian range bloated: C09 at 6731p = 1.78x AvgAsia (3780p); signals distribution not accumulation",
    "Weekly bias = NEUTRAL in C08 — only non-BUY weekly in the set, lost -1532p",
    "TDI RSI overbought (>62) at BUY entry in C02 and C09 — buying into exhausted momentum",
    "Flat/intertwined EMA structure in C03 and C08 — no directional conviction from moving averages",
    "Entry at or above Asian range high/HOD in C02, C03 — buying the top of the range",
    "RSI oversold + counter-trend in C08 (RSI 37) — knife-catching into bearish breakdown",
    "MAE exceeded 900p in 3/5 losers (C02=1390p, C03=1011p, C09=993p)",
    "Confluence only 80/100 in C08 (all other setups 95-100%) — lower alignment = weaker"
  ],
  "filters_to_test": [
    {
      "id": "F1_ADR_EXHAUSTION",
      "rule": "REJECT BUY if ADR% >= 90 at entry",
      "rationale": "Both worst losers (C02, C09) had ADR% >100%. No winner exceeded 82%. Threshold at 90% gives margin.",
      "expected_impact": "Blocks C02 (-200p) and C09 (-788p). No winners blocked. Net saved: ~988p.",
      "measurable": "adr_pct >= 90.0"
    },
    {
      "id": "F2_WEEKLY_BIAS_MISMATCH",
      "rule": "REJECT BUY if weekly_bias != BUY",
      "rationale": "C08 was the only NEUTRAL weekly setup; lost -1532p. All 6 winners had weekly BUY alignment.",
      "expected_impact": "Blocks C08 (-1532p). No winners blocked. Net saved: 1532p.",
      "measurable": "weekly_bias != 'BUY'"
    },
    {
      "id": "F3_ASIA_BLOAT",
      "rule": "REJECT BUY if asian_range > 1.5 * avg_asia",
      "rationale": "C09 Asian range was 6731p vs AvgAsia 3780p (1.78x). Bloated Asia = distribution, not accumulation.",
      "expected_impact": "Blocks C09 (already caught by F1). Redundant safety layer.",
      "measurable": "asian_range_pips / avg_asia_pips > 1.5"
    },
    {
      "id": "F4_ENTRY_ABOVE_AR_HIGH_TDI_HOT",
      "rule": "REJECT BUY if entry_price > asian_range_high AND tdi_rsi > 60",
      "rationale": "C02 entered above AR high with RSI 63 into overbought territory. Winners entering near AR had RSI 49-55.",
      "expected_impact": "Blocks C02. May overlap with F1 but independent signal.",
      "measurable": "entry_price > ar_high AND tdi_rsi > 60"
    },
    {
      "id": "F5_EMA_STACK_CHECK",
      "rule": "FLAG BUY if EMA5 < EMA13 AND EMA13 < EMA50 at entry bar (all bearish stack)",
      "rationale": "C08 had flat intertwined EMAs breaking bearish. C03 had choppy EMAs. Winners had bullish or recovering stacks.",
      "expected_impact": "Catches C08 and C03 structures. Reduces knife-catch risk.",
      "measurable": "ema5 < ema13 AND ema13 < ema50 at entry_bar"
    },
    {
      "id": "F6_CONFLUENCE_FLOOR",
      "rule": "REJECT BUY if confluence < 90 for XAUUSD THE_33 setups",
      "rationale": "C08 had confluence 80/100 and was the largest loss (-1532p). All other setups had 95-100%.",
      "expected_impact": "Blocks C08. Pair-specific tightening for high-volatility XAUUSD.",
      "measurable": "confluence_score < 90"
    },
    {
      "id": "F7_ENTRY_LOD_PROXIMITY",
      "rule": "PREFER BUY when entry is within 500p of LOD or weekly_open_low",
      "rationale": "Winners C01, C04, C06, C10, C11 all entered near LOD/weekly open. Gives maximum R:R room.",
      "expected_impact": "Scoring boost, not hard reject. Improves ranking of cleaner entries.",
      "measurable": "abs(entry_price - lod) <= 500 OR abs(entry_price - weekly_open_low) <= 500"
    }
  ],
  "filters_to_reject": [
    {
      "id": "R1_FRIDAY_BLANKET_BAN",
      "rule": "Reject all Friday XAUUSD BUY entries",
      "reason": "C11 was Friday and won +1477p with 2p MAE. C08 lost on Friday but due to NEUTRAL weekly, not the day itself. F2 already catches the real issue.",
      "evidence": "C11 proves Friday BUY can work with proper weekly alignment."
    },
    {
      "id": "R2_STOP_HUNT_SIZE_MINIMUM_1000P",
      "rule": "Reject XAUUSD BUY if stop_hunt < 1000p",
      "reason": "C11 had only 612p stop hunt (3 pushes) yet won +1477p with 2p MAE. C01 had 413p hunt and won +1119p. Small hunts work when backed by M/W pattern.",
      "evidence": "2/6 winners had sub-1000p hunts. Pattern quality matters more than hunt magnitude."
    },
    {
      "id": "R3_TDI_OVERBOUGHT_STANDALONE",
      "rule": "Reject BUY if TDI RSI > 60 alone",
      "reason": "C07 (winner, +1235p) had RSI 64. TDI overbought only fails when combined with ADR exhaustion (F1+F4 together). Standalone TDI filter has too many false positives.",
      "evidence": "C07 RSI 64 won; C04 RSI 61 won. Only losers C02 (RSI 63 + ADR 117%) and C09 (RSI 65 + ADR 126%) failed."
    },
    {
      "id": "R4_PUSH_COUNT_UNDER_5",
      "rule": "Reject if push_count < 5",
      "reason": "C11 had only 3 pushes and won +1477p. Push count is not discriminative in this sample.",
      "evidence": "C08 had 4 pushes and lost, but due to NEUTRAL weekly, not push count."
    }
  ],
  "pair_specific_notes": [
    "XAUUSD ADR is typically 5500-9400p (55-94 USD). ADR% > 90% means the daily move is nearly consumed — remaining energy insufficient for a fresh L3 buy.",
    "XAUUSD AvgAsia ranges 1564-4857p across this sample. Asian range > 1.5x AvgAsia signals pre-session distribution rather than accumulation.",
    "Stop hunt magnitudes for XAUUSD winners ranged 413-6008p. The pair profile min of 200p is too loose — but tightening to 1000p would block 2 winners. Keep the 200p min and rely on F1/F2 instead.",
    "XAUUSD L3 structure with THE_33 setup works best Mon-Wed when weekly impulse is still building (5/6 winners were Mon-Wed entries).",
    "The 200 EMA (magenta line) acts as critical support for winning entries — C04, C06, C07, C10 all bounced off or held above it.",
    "C05 (breakeven after T1) is edge-case: T1 hit at +2288p favorable but ended 0. Trail-stop management for XAUUSD L3 may need review — the pair's volatility can whipsaw trailing stops."
  ],
  "uncertain_items": [
    "C01 was correctly labeled winner but both blind reviews predicted loser. The chart appears to show entry after HOD rejection, yet it gained +1119p. May have entered at LOD bounce invisible at M15 snapshot resolution. Need bar-level entry confirmation.",
    "C05 (breakeven after T1) had max_favorable +2288p — among the best initial moves — but ended flat. Is this a trade management failure rather than entry quality failure? If so, the entry filter pass is correct but trail stop needs XAUUSD-specific tuning.",
    "C06 had TDI bearish divergence flagged yet won +730p with only 8p MAE. Bearish divergence appears unreliable as a rejection signal for early-week entries with low ADR%.",
    "C03 vs C10: same date (Oct 7), same pair, same signature. C03 at 09:15 lost -844p, C10 at 06:15 won +902p. Earlier entry (London open) may be critical — need session-time filter investigation.",
    "Small sample (n=11) limits statistical confidence on all filters. F1 and F2 are the strongest signals but even they rest on 2-3 blocked losers each."
  ],
  "next_backtest_spec": {
    "pair": "XAUUSD",
    "signature": "THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT",
    "date_range": "2025-06-01 to 2026-06-01",
    "filters_to_ablate": [
      {"filter_id": "F1_ADR_EXHAUSTION", "param": "adr_pct_threshold", "values": [80, 85, 90, 95]},
      {"filter_id": "F2_WEEKLY_BIAS_MISMATCH", "param": "require_weekly_buy", "values": [true, false]},
      {"filter_id": "F3_ASIA_BLOAT", "param": "asia_ratio_max", "values": [1.3, 1.5, 1.7]},
      {"filter_id": "F4_ENTRY_ABOVE_AR_HIGH_TDI_HOT", "param": "tdi_rsi_ceiling_at_ar_high", "values": [58, 60, 62]},
      {"filter_id": "F5_EMA_STACK_CHECK", "param": "require_bullish_ema_stack", "values": [true, false]},
      {"filter_id": "F6_CONFLUENCE_FLOOR", "param": "min_confluence_xauusd", "values": [85, 90, 95]}
    ],
    "baseline_metric": "net_pips after trade management (T1 + trail)",
    "success_criteria": "filter combination that blocks >=3 of 5 losers while retaining >=5 of 6 winners",
    "control_run": "no additional filters (current signature pass-through)",
    "output": "per-filter ablation table with win_rate, avg_pips, sharpe, max_drawdown, and count",
    "notes": "Also log C03-vs-C10 entry_hour to test session-time sub-filter. Track C05-style breakeven-after-T1 separately to evaluate trail-stop tuning."
  }
}
```
