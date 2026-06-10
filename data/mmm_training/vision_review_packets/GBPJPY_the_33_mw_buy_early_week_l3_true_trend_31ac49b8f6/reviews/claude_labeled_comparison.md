Now I have all 13 charts and the answer key. Let me compile the analysis.

**Answer Key Summary:**
- **Winners (8):** C03 (+11.6p), C04 (+13.1p), C05 (+16p), C06 (+17.5p, T1 hit), C07 (+21.6p), C08 (+17.6p), C10 (+45.6p), C11 (+29.6p)
- **Losers (5):** C01 (-12.2p), C02 (-17.6p), C09 (-23.5p), C12 (-12.9p), C13 (-22p)
- **Win rate:** 62% (8/13)

**Blind review accuracy:** Codex 7/13 (54%), Claude 7/13 (54%) — both barely above random.

Key observations from charts:

| ID | Label | AR(p) | TDR/ADR% | RSI | Entry Position | MAE |
|----|-------|-------|----------|-----|----------------|-----|
| C01 | L | 36 | 21% | 54 | After HOD rejection, dropping | 29p |
| C02 | L | 61 | 39% | 51 | Mid-range chop, AR oversized | 24p |
| C03 | W | 46 | 70% | 61 | Recovered from LOD, impulsive | 7p |
| C04 | W | 39 | 30% | 52 | Near AR high, Weekly BUY | 23p |
| C05 | W | 45 | 38% | 54 | After LOD reclaim, room to HOD | 14p |
| C06 | W | 39 | 30% | 48 | Lower range, Weekly BUY | 17p |
| C07 | W | 45 | 38% | 54 | After LOD reclaim, below HOD | 4p |
| C08 | W | 73 | 68% | 68 | At HOD, strong trend continuation | 7p |
| C09 | L | 69 | 55% | 41 | Massive collapse, below all EMAs | 29p |
| C10 | W | 41 | 53% | 58 | V-shape from LOD sweep | 5p |
| C11 | W | 46 | 23% | 55 | Above WK OPEN, higher low | 7p |
| C12 | L | 48 | 67% | 64 | HOD after full trend expansion | 46p |
| C13 | L | 67 | 50% | 57 | AR oversized, deep recovery fail | 51p |

```json
{
  "summary": "GBPJPY THE_33 MW BUY at L3 in early week has a 62% base win rate (8W/5L). Winners average +21.6p MFE with 10.4p MAE; losers average -17.5p with 35.7p MAE. The primary separator is NOT TDI state (both models over-weighted bearish TDI and achieved only 54% blind accuracy). Instead, three measurable structural filters catch 4 of 5 losers while preserving 7 of 8 winners: oversized Asian range (>50p), exhausted TDR/ADR ratio at entry (<22%), and weak RSI (<45). A fourth filter targeting late entries above AR high with TDI signal cross bearish catches the remaining loser (C12) without blocking the visually similar winner (C08) that lacked the bearish crossover.",
  "winner_traits": [
    "Entry near or below Asian range midpoint with room to HOD (C03, C05, C07, C10, C11 all entered from LOD/lower-half side)",
    "Low MAE: 7 of 8 winners had MAE < 17p, meaning price did not retrace significantly against entry",
    "Asian range within pair-specific 50p max (7 of 8 winners; only C08 at 73p violated but was a strong trend continuation)",
    "Stop hunt reclaim was FRESH and price had not yet traveled to HOD (C05, C07, C10, C11 had live or recent LOD sweep + impulsive reclaim)",
    "TDI RSI at or above 50 at entry (all 8 winners had RSI >= 48, averaging 55)",
    "Price held above EMA50 or was impulsively reclaiming it at entry (C03, C04, C06, C08, C10, C11)",
    "Weekly BUY alignment improved quality significantly (C04, C06 both won despite choppy L3 and VB squeeze TDI)"
  ],
  "loser_traits": [
    "Asian range > 50p: C02 (61p), C09 (69p), C13 (67p) — 3 of 5 losers exceeded GBPJPY pair max",
    "Extreme MAE: all 5 losers had MAE > 23p, averaging 35.7p — price moved decisively against the entry",
    "Entry after HOD exhaustion or full trend expansion (C01 entered after HOD rejection, C12 entered at HOD after full day trend from bottom)",
    "Very low TDR/ADR ratio: C01 had TDR 26p vs ADR 122p (21%) — day had barely moved, no momentum",
    "RSI < 45: C09 had RSI 41 during a massive bearish collapse — buying into structural weakness",
    "No fresh stop hunt reclaim: C01 and C02 had no clean LOD sweep; C12 had a stale hunt with full expansion already played out",
    "Multiple bearish TDI states simultaneously (signal cross bearish + MBL cross bearish on C01, C09, C13)"
  ],
  "filters_to_test": [
    {
      "id": "F1_AR_OVERSIZED",
      "description": "Block GBPJPY THE_33 BUY when Asian range exceeds pair-specific max (50p)",
      "threshold": "asian_range_pips > 50",
      "expected_impact": "Blocks 3 losers (C02, C09, C13), blocks 1 winner (C08). Net: 7W/2L = 78% win rate vs 62% baseline",
      "confidence": "high",
      "codex_encodable": true
    },
    {
      "id": "F2_TDR_ADR_FLOOR",
      "description": "Block when today's range is less than 22% of ADR — insufficient momentum for directional follow-through",
      "threshold": "tdr_pips / adr_pips < 0.22",
      "expected_impact": "Blocks 1 loser (C01 at 21%). No winners blocked. Net improvement: clean filter",
      "confidence": "medium_high",
      "codex_encodable": true
    },
    {
      "id": "F3_RSI_FLOOR_BUY",
      "description": "Block buy entries when TDI RSI is below 45 — buying into structural collapse",
      "threshold": "tdi_rsi < 45",
      "expected_impact": "Blocks 1 loser (C09 at RSI 41). No winners blocked",
      "confidence": "high",
      "codex_encodable": true
    },
    {
      "id": "F4_HOD_EXHAUSTION",
      "description": "Block buy when price is above AR high AND TDR/ADR > 60% AND TDI signal cross bearish — trend expansion exhausted",
      "threshold": "price > asian_high AND tdr_pips / adr_pips > 0.60 AND tdi_signal_cross_bearish == true",
      "expected_impact": "Blocks 1 loser (C12: TDR/ADR=67%, at HOD, signal cross bearish). Preserves C08 winner (same area but NO signal cross bearish at entry)",
      "confidence": "medium",
      "codex_encodable": true
    },
    {
      "id": "F5_ENTRY_POSITION_RATIO",
      "description": "Prefer entries in lower 60% of the Asian range. Flag (soft penalty, not hard block) when entry is in upper 25% of Asian range without a fresh LOD sweep within last 6 candles",
      "threshold": "(entry_price - asian_low) / (asian_high - asian_low) > 0.75 AND candles_since_lod_sweep > 6",
      "expected_impact": "Would flag C01, C12 as elevated risk. Most winners entered from lower half. Soft filter only",
      "confidence": "medium",
      "codex_encodable": true
    },
    {
      "id": "F6_MAE_EARLY_WARNING",
      "description": "If unrealized MAE exceeds 20p within first 30 minutes, probability of recovery is low for this signature — consider early cut",
      "threshold": "mae_pips > 20 AND minutes_since_entry <= 30",
      "expected_impact": "Post-entry management filter. All 5 losers exceeded 23p MAE; only 1 winner (C04) exceeded 20p MAE. Early cut would limit damage",
      "confidence": "medium",
      "codex_encodable": true
    }
  ],
  "filters_to_reject": [
    {
      "id": "R1_TDI_BEARISH_BLANKET_BLOCK",
      "description": "Both blind reviewers used bearish TDI states (signal cross bearish, shark fin short) as primary rejection criteria. This produced 54% accuracy — worse than the 62% base rate. TDI bearish states at L3 during THE_33 setups are often the TURNING POINT, not continuation signals.",
      "reason": "Winners C03 (shark fin short), C05 (shark fin short), C06 (VB squeeze + MBL cross bearish), C07 (signal cross bearish + shark fin short), C11 (signal cross bearish) all had bearish TDI and still won. TDI bearish is NOT a valid standalone rejection for this signature."
    },
    {
      "id": "R2_PRICE_BELOW_EMA200_BLOCK",
      "description": "Claude proposed blocking buys when price is below EMA200. Winners C04 and C06 were both below/near EMA200 in a falling 200 context and still won (+13.1p, +17.5p with T1 hit).",
      "reason": "EMA200 position is not decisive for THE_33 buys when Weekly direction is BUY and W-bottom structure is forming"
    },
    {
      "id": "R3_WEEKLY_SELL_CONFLICT_BLOCK",
      "description": "Claude flagged Weekly SELL vs BUY entry as a conflict. But 6 of 8 winners had Weekly=SELL — this signature RELIES on early-week counter-trend buys against weekly direction.",
      "reason": "Weekly SELL is the norm for this signature, not an exception. Blocking it would eliminate most winners."
    },
    {
      "id": "R4_OVERBOUGHT_TDI_BLOCK",
      "description": "Codex proposed blocking buys when TDI is overbought or shark-fin short. Winner C08 (RSI 68 overbought + shark fin short) gained +17.6p, and C10 (+45.6p) had shark fin short recovering.",
      "reason": "Overbought TDI at L3 can signal momentum continuation, not exhaustion, especially when the trend day structure is intact"
    }
  ],
  "pair_specific_notes": [
    "GBPJPY Asian range max of 50p is critical — 3/5 losers violated it. This is the single highest-value filter for this pair.",
    "GBPJPY ADR averaging 133p across samples gives substantial room for THE_33 moves. TDR/ADR ratio below 22% means the day hasn't started moving — avoid.",
    "Stop hunt magnitudes varied widely (33p to 115p). Hunt size alone was not predictive — both large hunts (C04: 104p winner, C09: 113p loser) and small hunts (C11: 33p winner) appeared in both categories.",
    "GBPJPY L3 + THE_33 combination is inherently choppy. The 62% win rate with avg +21.6p MFE on winners vs -17.5p on losers gives marginal positive expectancy (~+6.8p/trade) even before filtering.",
    "The trailing stop exit on C06 (only T1 hit in the sample) suggests GBPJPY THE_33 buys rarely reach 1:1 RR fast enough — consider reducing T1 target from 1:1 to 0.8:1 for this signature."
  ],
  "uncertain_items": [
    "C08 is an outlier winner: AR=73p (violates 50p max), RSI=68 (overbought), at HOD after trend continuation. Filter F1 would block it. Is this a genuine THE_33 or a trend continuation misclassified? Sample size too small to separate.",
    "C04 and C06 are same-day entries (2023-09-25) with Weekly BUY — the only samples with bullish weekly alignment. Unknown if Weekly BUY is a genuine quality boost or just coincidence from 2 correlated samples.",
    "Whether F4 (HOD exhaustion) would hold on a larger sample is uncertain. C12 is the only example and it was a STALE_EXIT loser that actually had 28.5p MFE before reversing — timing rather than direction was wrong.",
    "The blind models disagreed on C10 and C11 (both winners): Codex predicted loser for both, Claude predicted winner for C10 but loser for C11. The structural quality of the stop hunt reclaim (impulsive V-shape) may be the key differentiator that both models fail to encode reliably.",
    "TDI CONFLICT is in the shared signature for all 13 samples. Unable to evaluate if TDI alignment (no conflict) would produce better results since no such samples exist in this packet."
  ],
  "next_backtest_spec": {
    "pair": "GBPJPY",
    "signature": "THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND",
    "filters_to_encode": ["F1_AR_OVERSIZED", "F2_TDR_ADR_FLOOR", "F3_RSI_FLOOR_BUY", "F4_HOD_EXHAUSTION"],
    "baseline_win_rate": 0.62,
    "baseline_n": 13,
    "target_win_rate": 0.78,
    "minimum_n_for_significance": 30,
    "backtest_period": "2023-01-01 to 2026-06-01",
    "metrics_to_capture": [
      "win_rate_with_each_filter_individually",
      "win_rate_with_F1_plus_F2_plus_F3_combined",
      "win_rate_with_all_four_filters",
      "avg_mfe_winners_filtered_vs_unfiltered",
      "avg_mae_losers_blocked_vs_passed",
      "false_positive_rate_per_filter",
      "entry_position_ratio_distribution_winners_vs_losers",
      "time_to_mfe_distribution"
    ],
    "control_group": "unfiltered THE_33 MW BUY EARLY_WEEK L3 TRUE_TREND entries",
    "notes": "If combined F1+F2+F3 achieves >=70% win rate on n>=30, promote to validation_library. F4 requires separate evaluation due to compound condition. Also capture T1 hit rate to evaluate whether 0.8:1 RR target improves partial close frequency."
  }
}
```
