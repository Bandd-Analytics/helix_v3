Use the Read tool to inspect the local chart images when needed.
Packet directory: C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c

You are now allowed to use `answer_key.csv` after completing the blind review.

Compare winners against losers for this exact same MMM setup signature.

Pair: XAUUSD
Shared setup signature: THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS

Goal: identify the visual/structural filters that separate profitable examples from failed examples.

Return a concise JSON object with:
`summary`, `winner_traits`, `loser_traits`, `filters_to_test`, `filters_to_reject`, `pair_specific_notes`, `uncertain_items`, and `next_backtest_spec`.

Each `filters_to_test` item must be deterministic enough for Codex to encode. Include measurable thresholds where possible, such as candles, pips, ratios, relative position to Asian range, or TDI state.

Do not recommend live trading. These are research filters only.


Local chart images:
- C01: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c\images\c01_fc43004_20250904T081500.png`
- C02: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c\images\c02_fc48567_20251229T071500.png`
- C03: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c\images\c03_fc48529_20251222T214500.png`
- C04: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c\images\c04_fc43005_20250904T094500.png`
- C05: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c\images\c05_fc48289_20251128T081500.png`
- C06: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c\images\c06_fc43006_20250904T111500.png`
- C07: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c\images\c07_fc48771_20260127T081500.png`
- C08: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c\images\c08_fc42984_20250903T024500.png`
- C09: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c\images\c09_fc48525_20251222T170000.png`
- C10: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c\images\c10_fc48266_20251126T154500.png`
- C11: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c\images\c11_fc48632_20260107T110000.png`

Answer key:
review_id,label,flashcard_id,snapshot_at,outcome,exit_pips,max_favorable_pips,max_adverse_pips,t1_hit,image_path
C01,winner,43004,2025-09-04T08:15:00+00:00,TIME_EXIT_PROFIT,1214.9999999999636,1427.9999999999745,676.0000000000218,False,images/c01_fc43004_20250904T081500.png
C02,loser,48567,2025-12-29T07:15:00+00:00,LOSS,-4180.000000000018,527.9999999999745,4292.000000000007,False,images/c02_fc48567_20251229T071500.png
C03,winner,48529,2025-12-22T21:45:00+00:00,OPEN_PROFIT,998.0000000000473,1568.000000000029,177.99999999997453,False,images/c03_fc48529_20251222T214500.png
C04,winner,43005,2025-09-04T09:45:00+00:00,TIME_EXIT_PROFIT,263.99999999998727,951.9999999999982,334.00000000001455,False,images/c04_fc43005_20250904T094500.png
C05,loser,48289,2025-11-28T08:15:00+00:00,STALE_EXIT,-1042.0000000000073,377.99999999997453,1150.0,False,images/c05_fc48289_20251128T081500.png
C06,loser,43006,2025-09-04T11:15:00+00:00,STALE_EXIT,-475.0,174.00000000002365,671.99999999998,False,images/c06_fc43006_20250904T111500.png
C07,loser,48771,2026-01-27T08:15:00+00:00,STALE_EXIT,-483.9999999999236,1848.0000000000473,707.9999999999927,False,images/c07_fc48771_20260127T081500.png
C08,winner,42984,2025-09-03T02:45:00+00:00,TARGET_2,1044.999999999959,1648.0000000000018,207.99999999999272,True,images/c08_fc42984_20250903T024500.png
C09,winner,48525,2025-12-22T17:00:00+00:00,TIME_EXIT_PROFIT,2071.9999999999345,2617.999999999938,396.00000000000364,False,images/c09_fc48525_20251222T170000.png
C10,winner,48266,2025-11-26T15:45:00+00:00,TIME_EXIT_PROFIT,1382.0000000000618,1511.999999999989,1678.9999999999964,False,images/c10_fc48266_20251126T154500.png
C11,loser,48632,2026-01-07T11:00:00+00:00,LOSS,-647.0000000000255,139.00000000003274,696.0000000000036,False,images/c11_fc48632_20260107T110000.png


Blind Codex review:
[
  {
    "review_id": "C01",
    "predicted_label": "loser",
    "confidence_0_100": 70,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": false,
    "clean_w_bottom": false,
    "second_leg_quality": "weak; bounce is shallow after a heavy sell leg",
    "tdi_state_visible": "oversold recovery, still below/near midline",
    "entry_timing": "late after breakdown, not confirmed back inside range",
    "reject_reason": "Buy appears after a strong impulsive drop below prior structure with only weak reclaim evidence.",
    "proposed_filter": "Require bullish close back inside Asian range and TDI green/red cross above the lower band before accepting."
  },
  {
    "review_id": "C02",
    "predicted_label": "loser",
    "confidence_0_100": 63,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "messy; deep spike and recovery but no clean base",
    "tdi_state_visible": "recovering from oversold but below midline",
    "entry_timing": "early during post-flush recovery",
    "reject_reason": "Large rejection wick is favorable, but structure is volatile and the right edge has not built a stable W-bottom.",
    "proposed_filter": "Require two closes above the 50 EMA or a higher-low retest after the stop-hunt low."
  },
  {
    "review_id": "C03",
    "predicted_label": "winner",
    "confidence_0_100": 82,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "strong; clear higher-low continuation after base",
    "tdi_state_visible": "constructive, above lower band and curling upward",
    "entry_timing": "acceptable continuation after confirmed expansion",
    "reject_reason": "",
    "proposed_filter": "Keep when stop hunt is followed by sustained 5/13 EMA separation and price holds above the 50 EMA."
  },
  {
    "review_id": "C04",
    "predicted_label": "winner",
    "confidence_0_100": 61,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "moderate; second push is forming after reclaimed range",
    "tdi_state_visible": "oversold recovery with bullish curl",
    "entry_timing": "slightly late but after reclaim",
    "reject_reason": "",
    "proposed_filter": "Prefer entries after the first pullback holds above the reclaimed prior LOD area."
  },
  {
    "review_id": "C05",
    "predicted_label": "winner",
    "confidence_0_100": 86,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "excellent; tight base then explosive markup through HOD",
    "tdi_state_visible": "strong bullish expansion above midline",
    "entry_timing": "good; early in expansion after stop hunt",
    "reject_reason": "",
    "proposed_filter": "Prioritize this pattern when stop hunt is followed by compression at LOD and immediate 5/13/50 EMA alignment."
  },
  {
    "review_id": "C06",
    "predicted_label": "winner",
    "confidence_0_100": 68,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "good; strong reclaim from the low and higher candles into range",
    "tdi_state_visible": "bullish recovery from oversold",
    "entry_timing": "reasonable after reclaim, though not early",
    "reject_reason": "",
    "proposed_filter": "Require the post-hunt rally to close back above the 13 EMA before classifying as valid."
  },
  {
    "review_id": "C07",
    "predicted_label": "winner",
    "confidence_0_100": 73,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "solid; sharp sweep into weekly open low then strong reclaim",
    "tdi_state_visible": "bullish recovery from deeply oversold",
    "entry_timing": "good after LOD rejection and reclaim",
    "reject_reason": "",
    "proposed_filter": "Favor setups where the stop hunt sweeps below weekly/open liquidity and price reclaims LOD quickly."
  },
  {
    "review_id": "C08",
    "predicted_label": "winner",
    "confidence_0_100": 80,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "strong; base, reclaim, and sustained push to HOD",
    "tdi_state_visible": "bullish expansion above midline, later cooling",
    "entry_timing": "good if taken near L3/reclaim, late if taken at HOD",
    "reject_reason": "",
    "proposed_filter": "Accept only before HOD extension; reject fresh buys once price is pinned at HOD with TDI rolling over."
  },
  {
    "review_id": "C09",
    "predicted_label": "winner",
    "confidence_0_100": 84,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "excellent; clear accumulation low into persistent markup",
    "tdi_state_visible": "strong bullish drive then controlled pullback",
    "entry_timing": "good during early expansion after L3",
    "reject_reason": "",
    "proposed_filter": "Keep when L3 forms below range and price reclaims the 50 EMA with widening 5/13 EMAs."
  },
  {
    "review_id": "C10",
    "predicted_label": "loser",
    "confidence_0_100": 72,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": false,
    "clean_w_bottom": false,
    "second_leg_quality": "poor; rally stalls near HOD and reverses sharply",
    "tdi_state_visible": "bearish rollover from upper band",
    "entry_timing": "late into HOD resistance",
    "reject_reason": "Buy is occurring after an extended rally into HOD with TDI rolling over and no clean second-leg base.",
    "proposed_filter": "Reject buys within HOD/ADR resistance unless there is a fresh pullback, higher low, and TDI reset."
  },
  {
    "review_id": "C11",
    "predicted_label": "loser",
    "confidence_0_100": 69,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "mixed; strong rebound but after a very impulsive selloff",
    "tdi_state_visible": "rebounding from oversold but still fragile",
    "entry_timing": "early into recovery, before clean trend confirmation",
    "reject_reason": "The drop into LOD is violent and the buy signal lacks a clean W-bottom or sustained reclaim above the 50 EMA.",
    "proposed_filter": "Require a higher-low retest after the first rebound from LOD before accepting post-crash buys."
  }
]

Blind Claude review:
[{"review_id":"C01","predicted_label":"loser","confidence_0_100":78,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"poor","tdi_state_visible":"bearish_divergence","entry_timing":"late","reject_reason":"Entry into freefall from L3 peak; RSI 39 oversold with no reversal structure; ADR% 120 suggests exhaustion; price well below Asian range crashing to ADR Low","proposed_filter":"reject_if_rsi_below_40_at_entry"},{"review_id":"C02","predicted_label":"loser","confidence_0_100":72,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"poor","tdi_state_visible":"neutral_flat","entry_timing":"late","reject_reason":"Friday-to-Monday session; weekly NEUTRAL not BUY; price declining from L3 peak with no W-bottom reversal visible; RSI 49 flat; Asian range 7718p massively extended","proposed_filter":"reject_if_weekly_neutral_and_adr_pct_gt_90"},{"review_id":"C03","predicted_label":"winner","confidence_0_100":82,"real_mmm_stop_hunt":true,"return_inside_asian_range":true,"clean_w_bottom":true,"second_leg_quality":"good","tdi_state_visible":"bullish_cross","entry_timing":"on_time","reject_reason":"none","proposed_filter":"none"},{"review_id":"C04","predicted_label":"loser","confidence_0_100":80,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"poor","tdi_state_visible":"bearish_trend","entry_timing":"late","reject_reason":"Same session as C01 90 min later; price still declining from L3 peak; RSI 46 with no bullish structure; ADR% 120 blown; buying into continued selling","proposed_filter":"reject_if_adr_pct_gt_100_and_price_below_asian_low"},{"review_id":"C05","predicted_label":"winner","confidence_0_100":80,"real_mmm_stop_hunt":true,"return_inside_asian_range":true,"clean_w_bottom":true,"second_leg_quality":"good","tdi_state_visible":"bullish_cross","entry_timing":"on_time","reject_reason":"none","proposed_filter":"none"},{"review_id":"C06","predicted_label":"loser","confidence_0_100":70,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"weak","tdi_state_visible":"neutral_recovery","entry_timing":"late","reject_reason":"Third BUY attempt same day (C01/C04/C06); ADR% 120 extended; weak bounce from LOD; RSI 52 recovering but no impulsive structure; EMA 50 far above price","proposed_filter":"reject_if_third_same_day_attempt"},{"review_id":"C07","predicted_label":"loser","confidence_0_100":68,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"weak","tdi_state_visible":"bearish_trend","entry_timing":"early","reject_reason":"Violent drop from L3 peak to WK OPEN L; stop hunt 1796p visible but no W-bottom recovery; price sitting at LOD with no bullish structure; TDI still declining","proposed_filter":"reject_if_hunt_gt_1500p_no_w_recovery"},{"review_id":"C08","predicted_label":"winner","confidence_0_100":85,"real_mmm_stop_hunt":true,"return_inside_asian_range":true,"clean_w_bottom":true,"second_leg_quality":"strong","tdi_state_visible":"bullish_impulse","entry_timing":"on_time","reject_reason":"none","proposed_filter":"none"},{"review_id":"C09","predicted_label":"winner","confidence_0_100":84,"real_mmm_stop_hunt":true,"return_inside_asian_range":true,"clean_w_bottom":true,"second_leg_quality":"strong","tdi_state_visible":"bullish_impulse","entry_timing":"on_time","reject_reason":"none","proposed_filter":"none"},{"review_id":"C10","predicted_label":"winner","confidence_0_100":60,"real_mmm_stop_hunt":true,"return_inside_asian_range":true,"clean_w_bottom":true,"second_leg_quality":"moderate","tdi_state_visible":"neutral_flat","entry_timing":"on_time","reject_reason":"none","proposed_filter":"flag_if_multiple_red_arrows_post_entry"},{"review_id":"C11","predicted_label":"loser","confidence_0_100":74,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"poor","tdi_state_visible":"bearish_trend","entry_timing":"late","reject_reason":"Price crashed from L3 peak; stop hunt 495p but no W-bottom recovery visible; RSI 50/48 neutral-bearish; entry at bottom of heavy selloff with EMA 50 rolling over hard; ADR% 68.6 still has room to extend lower","proposed_filter":"reject_if_ema50_slope_negative_at_entry"}]


Return only the requested concise JSON object. Do not recommend live trading.
