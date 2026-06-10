Use the Read tool to inspect the local chart images when needed.
Packet directory: C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a

You are now allowed to use `answer_key.csv` after completing the blind review.

Compare winners against losers for this exact same MMM setup signature.

Pair: XAUUSD
Shared setup signature: RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS

Goal: identify the visual/structural filters that separate profitable examples from failed examples.

Return a concise JSON object with:
`summary`, `winner_traits`, `loser_traits`, `filters_to_test`, `filters_to_reject`, `pair_specific_notes`, `uncertain_items`, and `next_backtest_spec`.

Each `filters_to_test` item must be deterministic enough for Codex to encode. Include measurable thresholds where possible, such as candles, pips, ratios, relative position to Asian range, or TDI state.

Do not recommend live trading. These are research filters only.


Local chart images:
- C01: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a\images\c01_fc34706_20250421T030000.png`
- C02: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a\images\c02_fc29763_20240923T154500.png`
- C03: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a\images\c03_fc30046_20241029T150000.png`
- C04: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a\images\c04_fc29585_20240829T174500.png`
- C05: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a\images\c05_fc27122_20240708T071500.png`
- C06: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a\images\c06_fc34469_20250313T120000.png`
- C07: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a\images\c07_fc27120_20240708T041500.png`
- C08: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a\images\c08_fc34690_20250415T190000.png`
- C09: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a\images\c09_fc32525_20250116T050000.png`
- C10: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a\images\c10_fc27411_20240814T071500.png`
- C11: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_buy_mid_week_l3_accumulation_1a4350c96a\images\c11_fc27124_20240708T101500.png`

Answer key:
review_id,label,flashcard_id,snapshot_at,outcome,exit_pips,max_favorable_pips,max_adverse_pips,t1_hit,image_path
C01,winner,34706,2025-04-21T03:00:00+00:00,TRAIL_STOP,2658.999999999969,3038.9999999999873,178.00000000002,True,images/c01_fc34706_20250421T030000.png
C02,winner,29763,2024-09-23T15:45:00+00:00,TIME_EXIT_PROFIT,225.0,780.0000000000182,142.99999999998363,False,images/c02_fc29763_20240923T154500.png
C03,winner,30046,2024-10-29T15:00:00+00:00,TRAIL_STOP,1465.9999999999854,1863.000000000011,483.9999999999691,True,images/c03_fc30046_20241029T150000.png
C04,winner,29585,2024-08-29T17:45:00+00:00,TIME_EXIT_PROFIT,372.00000000002547,653.9999999999964,466.9999999999618,False,images/c04_fc29585_20240829T174500.png
C05,loser,27122,2024-07-08T07:15:00+00:00,BREAKEVEN_AFTER_T1,0.0,342.99999999998363,75.0,True,images/c05_fc27122_20240708T071500.png
C06,winner,34469,2025-03-13T12:00:00+00:00,TIME_EXIT_PROFIT,373.0000000000018,698.0000000000018,19.000000000005457,False,images/c06_fc34469_20250313T120000.png
C07,loser,27120,2024-07-08T04:15:00+00:00,LOSS,-480.0000000000182,11.000000000012733,548.9999999999782,False,images/c07_fc27120_20240708T041500.png
C08,winner,34690,2025-04-15T19:00:00+00:00,TIME_EXIT_PROFIT,877.9999999999745,880.9999999999945,347.00000000002547,False,images/c08_fc34690_20250415T190000.png
C09,loser,32525,2025-01-16T05:00:00+00:00,STALE_EXIT,-112.00000000003456,151.99999999999818,156.00000000004002,False,images/c09_fc32525_20250116T050000.png
C10,winner,27411,2024-08-14T07:15:00+00:00,TRAIL_STOP,763.0000000000109,888.0000000000109,208.99999999996908,True,images/c10_fc27411_20240814T071500.png
C11,loser,27124,2024-07-08T10:15:00+00:00,AMBIGUOUS,-104.99999999997272,132.00000000001637,142.99999999998363,False,images/c11_fc27124_20240708T101500.png


Blind Codex review:
[
  {
    "review_id": "C01",
    "predicted_label": "loser",
    "confidence_0_100": 68,
    "real_mmm_stop_hunt": "weak",
    "return_inside_asian_range": "yes_after_deep_drop",
    "clean_w_bottom": "no",
    "second_leg_quality": "late_recovery_after_breakdown",
    "tdi_state_visible": "overbought_after_late_cross",
    "entry_timing": "late_chasing_into_hod_area",
    "reject_reason": "Buy appears after a major sell leg and sharp recovery into overhead HOD/weekly-open resistance, without a clean W-bottom base.",
    "proposed_filter": "Reject buys when entry is late above the Asian range after a deep same-session breakdown unless a clean W-bottom and pullback hold are visible."
  },
  {
    "review_id": "C02",
    "predicted_label": "winner",
    "confidence_0_100": 72,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": "yes",
    "clean_w_bottom": "adequate",
    "second_leg_quality": "strong_push_to_hod",
    "tdi_state_visible": "bullish_cross_recovering",
    "entry_timing": "acceptable_after_pullback",
    "reject_reason": "",
    "proposed_filter": "Prefer buys that reclaim the range after a stop hunt and hold above the 50 EMA during the second leg."
  },
  {
    "review_id": "C03",
    "predicted_label": "winner",
    "confidence_0_100": 78,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": "yes",
    "clean_w_bottom": "yes",
    "second_leg_quality": "strong",
    "tdi_state_visible": "bullish_long_after_reset",
    "entry_timing": "good_continuation_after_breakout",
    "reject_reason": "",
    "proposed_filter": "Keep buys with visible stop-hunt low, range reclaim, rising 50 EMA, and TDI strength above midline."
  },
  {
    "review_id": "C04",
    "predicted_label": "winner",
    "confidence_0_100": 70,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": "yes",
    "clean_w_bottom": "adequate",
    "second_leg_quality": "strong_but_extended",
    "tdi_state_visible": "bullish_cross",
    "entry_timing": "slightly_late_but_supported",
    "reject_reason": "",
    "proposed_filter": "Allow extended buys only when price holds above 50/200 EMA and the pullback does not close back below range mid."
  },
  {
    "review_id": "C05",
    "predicted_label": "loser",
    "confidence_0_100": 76,
    "real_mmm_stop_hunt": "unclear",
    "return_inside_asian_range": "yes_but_flat",
    "clean_w_bottom": "no",
    "second_leg_quality": "stalled_sideways",
    "tdi_state_visible": "bearish_rollover",
    "entry_timing": "late_at_hod_after_exhaustion",
    "reject_reason": "Entry sits after an already completed trend leg, with price flattening at HOD and TDI rolling down.",
    "proposed_filter": "Reject buys when THE 33 appears in Asian-range chop after the first impulse is exhausted and TDI is declining."
  },
  {
    "review_id": "C06",
    "predicted_label": "winner",
    "confidence_0_100": 67,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": "yes",
    "clean_w_bottom": "adequate",
    "second_leg_quality": "constructive",
    "tdi_state_visible": "bullish_rebound_from_oversold",
    "entry_timing": "acceptable_pullback_entry",
    "reject_reason": "",
    "proposed_filter": "Favor buys after stop-hunt recovery when the pullback holds above the 50 EMA and TDI hooks up from oversold."
  },
  {
    "review_id": "C07",
    "predicted_label": "loser",
    "confidence_0_100": 74,
    "real_mmm_stop_hunt": "unclear",
    "return_inside_asian_range": "yes_but_late",
    "clean_w_bottom": "no",
    "second_leg_quality": "exhausted",
    "tdi_state_visible": "bearish_rollover",
    "entry_timing": "late_after_full_impulse",
    "reject_reason": "The setup is a chase after a large vertical move into HOD/weekly-open resistance, followed by lower momentum and TDI rollover.",
    "proposed_filter": "Reject buys after a near-vertical second leg if entry occurs at the top of the box with TDI already rolling over."
  },
  {
    "review_id": "C08",
    "predicted_label": "loser",
    "confidence_0_100": 71,
    "real_mmm_stop_hunt": "weak",
    "return_inside_asian_range": "yes",
    "clean_w_bottom": "no",
    "second_leg_quality": "choppy_failed_continuation",
    "tdi_state_visible": "mixed_flat",
    "entry_timing": "late_inside_distribution",
    "reject_reason": "Price is trapped in broad chop near the 200 EMA with no clean W-bottom and no clean second-leg continuation.",
    "proposed_filter": "Reject buys when entry is inside post-breakout distribution around the 200 EMA instead of after a clean range reclaim and hold."
  },
  {
    "review_id": "C09",
    "predicted_label": "winner",
    "confidence_0_100": 73,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": "yes",
    "clean_w_bottom": "yes",
    "second_leg_quality": "strong",
    "tdi_state_visible": "bullish_recovery",
    "entry_timing": "good_after_reset",
    "reject_reason": "",
    "proposed_filter": "Keep buys where a stop hunt is followed by a clean reclaim, EMA alignment, and sustained candles above LOD."
  },
  {
    "review_id": "C10",
    "predicted_label": "loser",
    "confidence_0_100": 82,
    "real_mmm_stop_hunt": "no",
    "return_inside_asian_range": "no_clear_reclaim",
    "clean_w_bottom": "no",
    "second_leg_quality": "failed_bearish",
    "tdi_state_visible": "weak_from_oversold",
    "entry_timing": "countertrend_into_selloff",
    "reject_reason": "Chart shows a broad bearish structure with price breaking down near the right edge and no convincing bullish reversal base.",
    "proposed_filter": "Reject buys when price is below falling short EMAs and the latest impulse is a fresh sell leg rather than a reclaimed stop hunt."
  },
  {
    "review_id": "C11",
    "predicted_label": "loser",
    "confidence_0_100": 80,
    "real_mmm_stop_hunt": "unclear",
    "return_inside_asian_range": "failed",
    "clean_w_bottom": "no",
    "second_leg_quality": "failed_after_hod_distribution",
    "tdi_state_visible": "bearish_shark_fin",
    "entry_timing": "late_after_distribution_breakdown",
    "reject_reason": "After a strong prior run, price distributes near HOD, loses the range, and TDI is bearish into the entry area.",
    "proposed_filter": "Reject buys after HOD distribution when price closes below the Asian range floor and TDI slopes down."
  }
]

Blind Claude review:
[{"review_id":"C01","predicted_label":"loser","confidence_0_100":72,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"RSI overbought 68, signal cross bullish but at ceiling","entry_timing":"late — price already rallied massively from lows, RSI at overbought ceiling","reject_reason":"Entry at exhaustion; RSI 68 overbought; no visible M/W; massive prior rally already consumed ADR","proposed_filter":"reject_rsi_above_65_on_buy"},{"review_id":"C02","predicted_label":"loser","confidence_0_100":75,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"Signal cross bullish but RSI dropping from 68 zone at right edge; TDI panel shows rollover","entry_timing":"late — multiple red arrows at HOD, price already peaked and reversing with red candles","reject_reason":"Price peaked at HOD with reversal candles; TDI rolling over from overbought; Asian range 1505p extremely wide; L3 chop","proposed_filter":"reject_wide_asian_range_above_1400p_xau"},{"review_id":"C03","predicted_label":"loser","confidence_0_100":65,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"Shark Fin Long at 53/50 — mid-range, not strong momentum","entry_timing":"late — price already rallied from stop hunt zone; right edge shows red reversal candles from HOD","reject_reason":"Stop hunt was valid but entry comes after the move played out; reversal candles at HOD; Asian range 1781p very wide; TDI losing momentum","proposed_filter":"reject_entry_after_move_exceeds_1x_adr"},{"review_id":"C04","predicted_label":"winner","confidence_0_100":62,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"moderate","tdi_state_visible":"MBL cross bullish at 55/51 — healthy mid-range bullish cross","entry_timing":"reasonable — clean uptrend with pullback into EMA support, continuation structure intact","reject_reason":"none","proposed_filter":"none"},{"review_id":"C05","predicted_label":"loser","confidence_0_100":70,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"Shark Fin Long but RSI 48/47 below midline — weak for a buy","entry_timing":"poor — Friday into Monday; price at WK OPEN H resistance; RSI below 50 contradicts bullish bias","reject_reason":"Weekly NEUTRAL not bullish; RSI sub-50 conflicts with BUY; price stalling at weekly open high resistance; weekend transition","proposed_filter":"reject_buy_when_rsi_below_50"},{"review_id":"C06","predicted_label":"loser","confidence_0_100":78,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"Shark Fin Long at 56/53 but TDI panel dropping from 68 zone","entry_timing":"late — strong reversal candles dropping from HOD visible at right edge; the buy move already played out","reject_reason":"Heavy bearish reversal candles at HOD; TDI rolling over from overbought 68 zone; entry at top of the impulse","proposed_filter":"reject_entry_with_large_bearish_candle_at_hod"},{"review_id":"C07","predicted_label":"winner","confidence_0_100":58,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"weak","tdi_state_visible":"Shark Fin Long at 59/56 — above midline, momentum intact","entry_timing":"acceptable — price breaking above prior HOD into new Monday range; continuation momentum visible","reject_reason":"none — momentum still carries despite weekly NEUTRAL","proposed_filter":"none"},{"review_id":"C08","predicted_label":"loser","confidence_0_100":68,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"Signal + MBL cross bullish at 51/50 but flat — no thrust above midline","entry_timing":"poor — choppy L3 zone; EMAs tangled; large red candle at right edge","reject_reason":"Choppy L3 consolidation; Asian range 2013p extremely wide; big bearish candle at entry edge; TDI flat at midline with no momentum","proposed_filter":"reject_when_asian_range_exceeds_2000p_xau"},{"review_id":"C09","predicted_label":"loser","confidence_0_100":60,"real_mmm_stop_hunt":true,"return_inside_asian_range":true,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"VB Squeeze + Shark Fin Long at 57/57 — compressed but multiple red arrows at HOD","entry_timing":"marginal — stop hunt was clean and Asian range tight (908p), but multiple exhaustion arrows at HOD suggest reversal starting","reject_reason":"Multiple red down-arrows at HOD = exhaustion; choppy into Thursday; despite tight Asian range the follow-through stalls","proposed_filter":"reject_when_3_plus_red_arrows_at_hod"},{"review_id":"C10","predicted_label":"loser","confidence_0_100":77,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"Shark Fin Long at 45/42 — well below midline, bearish for a BUY signal","entry_timing":"poor — RSI 45/42 directly contradicts BUY; heavy selling with large red candles into Wednesday","reject_reason":"RSI 45/42 is bearish — contradicts BUY direction; heavy red candles at right edge; Asian range 1716p wide","proposed_filter":"reject_buy_when_rsi_below_48"},{"review_id":"C11","predicted_label":"loser","confidence_0_100":66,"real_mmm_stop_hunt":false,"return_inside_asian_range":true,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"Signal cross bullish + Shark Fin Long at 43/43 — deeply below midline, very weak","entry_timing":"poor — RSI 43 severely contradicts BUY bias; weekly NEUTRAL; price near WK OPEN H resistance with fading momentum","reject_reason":"RSI 43/43 far below midline contradicts bullish entry; weekly NEUTRAL; resistance at weekly open high; momentum fading at right edge","proposed_filter":"reject_buy_when_rsi_below_45_and_weekly_neutral"}]


Return only the requested concise JSON object. Do not recommend live trading.
