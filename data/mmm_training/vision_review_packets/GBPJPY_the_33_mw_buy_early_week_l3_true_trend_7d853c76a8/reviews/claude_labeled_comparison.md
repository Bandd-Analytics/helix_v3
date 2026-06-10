```json
{
  "summary": "6 winners / 4 losers across 10 GBPJPY THE_33 MW BUY setups in L3 early-week counter-weekly-SELL environments. Winners share: TDI RSI >= 53 at entry with RSI >= Signal, stop hunt within 30-62p pair range, price recovering above Asian range low with higher-low structure, and entry during London proper (09:30-12:00). Losers share: TDI RSI < 50 and below Signal, oversized stop hunts (115p, 2x pair max), price trapped below EMA cluster at LOD, or premature entries before 09:00.",
  "winner_traits": [
    "TDI RSI >= 53 at snapshot (C05:57, C07:56, C09:61, C10:57); exception C01 at 50 but with 5-push confirmed structure",
    "TDI RSI >= Signal line in 5 of 6 winners (RSI-Sig spread >= 0)",
    "Stop hunt size within pair profile range 30-60p (C05/C07: 32p, C01: 41.3p, C09/C10: 45.6p); C06 at 62p marginal but recovered",
    "Price at or above Asian range low at entry — W-bottom second leg holds above AR Low",
    "Max adverse excursion very low: median 4.5p (C06:0.7p, C09:0p, C01:6.7p, C05:6.7p, C07:2.2p); C10 outlier at 18p but had 56p favorable",
    "Entry time between 09:30-12:00 EAT in 5 of 6 winners",
    "EMA 50 (yellow) flattening or turning up at entry — not sharply declining",
    "Asian range 43-50p — moderate accumulation width consistent with pair profile"
  ],
  "loser_traits": [
    "TDI RSI < 50 in 3 of 4 losers (C02:44, C03:44, C04:43); C08 at 53 but fading",
    "TDI RSI < Signal in all 4 losers (C02: 44<47, C03: 44<51, C04: 43<49, C08: 53<54 marginal)",
    "Stop hunt 115p in C03/C04 — nearly 2x the GBPJPY pair max of 60p — extreme volatility spike, not controlled accumulation",
    "Price below EMA 200 (white) and EMA 50 (yellow) at entry in C02, C03, C04",
    "No constructive higher-low visible on M15 — price chopping or fading from failed recovery",
    "C08 entered at 08:15 — pre-London, before session liquidity confirms direction",
    "Max adverse excursion high: C08: 22.3p, C02: 14.7p, C03: 13.6p, C04: 14.5p",
    "Asian range only 26p for C03/C04 — abnormally tight range followed by 115p hunt suggests liquidity void, not accumulation"
  ],
  "filters_to_test": [
    {
      "id": "F1_TDI_RSI_FLOOR",
      "description": "Require TDI RSI >= 53 at entry for GBPJPY THE_33 BUY",
      "threshold": "RSI >= 53",
      "rationale": "5/6 winners had RSI >= 53; 3/4 losers had RSI < 50. Separates cleanly.",
      "expected_impact": "Blocks C02, C03, C04 (all losers). Also blocks C01 (winner at RSI 50) — acceptable 1 false negative for 3 true negatives."
    },
    {
      "id": "F2_RSI_ABOVE_SIGNAL",
      "description": "Require TDI RSI >= Signal line at entry (RSI - Signal >= 0)",
      "threshold": "RSI - Signal >= 0",
      "rationale": "All 4 losers had RSI < Signal. 5/6 winners had RSI >= Signal. Strong binary separator.",
      "expected_impact": "Blocks all 4 losers. C01 at RSI=Sig=50 passes on equality."
    },
    {
      "id": "F3_HUNT_SIZE_CAP",
      "description": "Reject when stop hunt exceeds 1.1x pair max hunt range (GBPJPY max 60p → cap at 66p)",
      "threshold": "hunt_pips <= pair_max_hunt * 1.1",
      "rationale": "C03/C04 at 115p hunt are extreme outliers — both losers. C06 at 62p (1.03x) passed and won. 66p cap filters 115p without hitting 62p.",
      "expected_impact": "Blocks C03, C04. No false negatives in this sample."
    },
    {
      "id": "F4_NO_ENTRY_BEFORE_0930",
      "description": "Block GBPJPY THE_33 BUY entries before 09:30 EAT (allow London session to develop)",
      "threshold": "entry_time_eat >= 09:30",
      "rationale": "C08 at 08:15 was -12p loser with 22.3p MAE. All other entries at 09:30+ had better W-bottom confirmation.",
      "expected_impact": "Blocks C08 (loser). No winners entered before 09:30 in this sample."
    },
    {
      "id": "F5_PRICE_ABOVE_AR_LOW",
      "description": "Require current price >= Asian range low at the moment of entry",
      "threshold": "price >= asian_range_low",
      "rationale": "Winners recovered into the range before entry. Losers C02, C08 were at or near LOD below AR Low.",
      "expected_impact": "Blocks entries where price hasn't reclaimed accumulation zone."
    },
    {
      "id": "F6_HUNT_TO_AR_RATIO",
      "description": "Reject when stop hunt / Asian range > 3.0 (indicates volatility spike through thin accumulation)",
      "threshold": "hunt_pips / asian_range_pips <= 3.0",
      "rationale": "C03/C04: 115p hunt / 26p AR = 4.4x — extreme. Winners ranged 0.7x to 1.4x. Losers C02/C08 at 0.88x passed, so ratio alone won't catch all, but 3.0x cap catches the extreme cases.",
      "expected_impact": "Blocks C03, C04. Complementary to F3."
    }
  ],
  "filters_to_reject": [
    {
      "id": "R1_BLOCK_ALL_L3_COUNTER_WEEKLY",
      "description": "Blanket rejection of all L3 counter-weekly buys",
      "reason": "60% win rate (6/10) in this signature — above the 55% validation threshold. L3 + THE_33 + W_BOTTOM still produces edge when TDI and hunt size are valid."
    },
    {
      "id": "R2_REQUIRE_PRICE_ABOVE_EMA200",
      "description": "Require price above EMA 200 for buy",
      "reason": "C10 (+56.3p, best winner) entered near EMA 200 at LOD. In L3 reversal context, the W-bottom forms AT the EMA cluster, not above it. Would filter best trade."
    },
    {
      "id": "R3_BLOCK_HUNT_ABOVE_50P",
      "description": "Cap hunt at 50p for GBPJPY",
      "reason": "C06 (+18.7p, trail stop) had 62p hunt and was the only T1-hit winner with 0.7p MAE. Tight cap kills a clean winner. Use 66p cap (F3) instead."
    }
  ],
  "pair_specific_notes": [
    "GBPJPY L3 THE_33 BUY works 60% of the time (6/10) in early-week counter-weekly-SELL context — marginal edge, filters critical",
    "TDI RSI is the single strongest separator: RSI >= 53 AND RSI >= Signal correctly classified 9/10 examples",
    "Stop hunt 115p (2x pair max) on 26p Asian range is a volatility void, not accumulation — both instances lost. Hunt/AR ratio > 3.0 is a red flag",
    "GBPJPY responds well to London-session timing gate (no entry before 09:30 EAT); pre-London entries lack directional commitment",
    "Best winners (C09: 0p MAE, C06: 0.7p MAE) had immediate follow-through — suggesting correct timing is more important than SL distance for this pair",
    "C05/C07 same-day entries (2025-12-08) both won — when conditions align, multiple entries are valid"
  ],
  "uncertain_items": [
    "C01 (winner +36.5p): Both blind reviewers predicted loser. RSI 50/50 is exactly at the proposed F1 threshold boundary. Needs more samples at RSI 49-53 to determine if 53 floor is too aggressive or if C01 is an outlier.",
    "C06 (winner +18.7p): 62p hunt exceeds pair max 60p. Codex and Claude both predicted loser. TDI RSI 51/Sig 48 is below F1 threshold of 53. Would be blocked by F1 despite being a winner. Need to evaluate if F1+F2 combined (RSI 51 >= Sig 48 passes F2) provides sufficient coverage.",
    "Confluence score did not separate winners from losers in this sample (winners: 60-70, losers: 60-70). May not be useful as a discriminating filter for this specific signature.",
    "Asian range width showed losers at extremes (26p too tight, 48p normal) — unclear if AR < 30p should be a hard block or if the hunt/AR ratio (F6) is sufficient."
  ],
  "next_backtest_spec": {
    "pair": "GBPJPY",
    "signature": "THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND",
    "filters_to_backtest": [
      "F1_TDI_RSI_FLOOR: RSI >= 53",
      "F2_RSI_ABOVE_SIGNAL: RSI >= Signal",
      "F3_HUNT_SIZE_CAP: hunt_pips <= 66",
      "F4_NO_ENTRY_BEFORE_0930: entry >= 09:30 EAT",
      "F6_HUNT_TO_AR_RATIO: hunt_pips / AR_pips <= 3.0"
    ],
    "ablation_order": [
      "Run baseline: no filters (expect ~60% WR from this sample)",
      "Add F2 alone (RSI >= Signal) — expected strongest single filter",
      "Add F1+F2 combined (RSI >= 53 AND RSI >= Signal)",
      "Add F1+F2+F3 (add hunt cap)",
      "Add F1+F2+F3+F4 (add time gate)",
      "Full stack F1+F2+F3+F4+F6"
    ],
    "lookback_days": 365,
    "min_samples_per_filter": 8,
    "success_criteria": "Win rate >= 70% with Sharpe improvement over baseline, max 30% sample loss from filtering"
  }
}
```
