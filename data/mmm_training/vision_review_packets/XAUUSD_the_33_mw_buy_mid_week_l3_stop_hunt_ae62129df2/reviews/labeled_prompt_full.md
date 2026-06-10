Use the Read tool to inspect the local chart images when needed.
Packet directory: C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2

You are now allowed to use `answer_key.csv` after completing the blind review.

Compare winners against losers for this exact same MMM setup signature.

Pair: XAUUSD
Shared setup signature: THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS

Goal: identify the visual/structural filters that separate profitable examples from failed examples.

Return a concise JSON object with:
`summary`, `winner_traits`, `loser_traits`, `filters_to_test`, `filters_to_reject`, `pair_specific_notes`, `uncertain_items`, and `next_backtest_spec`.

Each `filters_to_test` item must be deterministic enough for Codex to encode. Include measurable thresholds where possible, such as candles, pips, ratios, relative position to Asian range, or TDI state.

Do not recommend live trading. These are research filters only.


Local chart images:
- C01: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2\images\c01_fc48267_20251126T171500.png`
- C02: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2\images\c02_fc43353_20251008T151500.png`
- C03: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2\images\c03_fc43331_20251007T091500.png`
- C04: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2\images\c04_fc42968_20250902T040000.png`
- C05: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2\images\c05_fc48482_20251217T150000.png`
- C06: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2\images\c06_fc43051_20250909T023000.png`
- C07: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2\images\c07_fc48531_20251223T010000.png`
- C08: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2\images\c08_fc48230_20251121T090000.png`
- C09: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2\images\c09_fc48524_20251222T153000.png`
- C10: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2\images\c10_fc43329_20251007T061500.png`
- C11: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2\images\c11_fc48294_20251128T154500.png`

Answer key:
review_id,label,flashcard_id,snapshot_at,outcome,exit_pips,max_favorable_pips,max_adverse_pips,t1_hit,image_path
C01,winner,48267,2025-11-26T17:15:00+00:00,TIME_EXIT_PROFIT,1118.99999999996,1494.9999999999818,101.00000000002183,False,images/c01_fc48267_20251126T171500.png
C02,loser,43353,2025-10-08T15:15:00+00:00,STALE_EXIT,-200.0,924.0000000000236,1389.9999999999636,False,images/c02_fc43353_20251008T151500.png
C03,loser,43331,2025-10-07T09:15:00+00:00,LOSS,-844.0000000000055,44.00000000000546,1011.0000000000127,False,images/c03_fc43331_20251007T091500.png
C04,winner,42968,2025-09-02T04:00:00+00:00,TRAIL_STOP,463.99999999998727,1990.9999999999854,65.0000000000091,True,images/c04_fc42968_20250902T040000.png
C05,loser,48482,2025-12-17T15:00:00+00:00,BREAKEVEN_AFTER_T1,0.0,2288.000000000011,27.999999999974534,True,images/c05_fc48482_20251217T150000.png
C06,winner,43051,2025-09-09T02:30:00+00:00,TARGET_2,730.0000000001319,1009.9999999999909,8.000000000038199,True,images/c06_fc43051_20250909T023000.png
C07,winner,48531,2025-12-23T01:00:00+00:00,TRAIL_STOP,1235.0000000000364,1478.9999999999964,225.0,True,images/c07_fc48531_20251223T010000.png
C08,loser,48230,2025-11-21T09:00:00+00:00,LOSS,-1531.999999999971,523.9999999999782,173.00000000000182,False,images/c08_fc48230_20251121T090000.png
C09,loser,48524,2025-12-22T15:30:00+00:00,STALE_EXIT,-787.99999999992,516.0000000000764,992.9999999999382,False,images/c09_fc48524_20251222T153000.png
C10,winner,43329,2025-10-07T06:15:00+00:00,TRAIL_STOP,901.9999999999982,1194.0000000000055,57.999999999992724,True,images/c10_fc43329_20251007T061500.png
C11,winner,48294,2025-11-28T15:45:00+00:00,TRAIL_STOP,1476.9999999999527,2642.0000000000073,1.9999999999527063,True,images/c11_fc48294_20251128T154500.png


Blind Codex review:
[
  {
    "review_id": "C01",
    "predicted_label": "loser",
    "confidence_0_100": 68,
    "real_mmm_stop_hunt": "weak",
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "poor; entry appears after an extended push into HOD/THE_33 rather than at the actual W bottom",
    "tdi_state_visible": "mixed; late bullish curl from oversold but below/near midline after prior bearish drop",
    "entry_timing": "late_after_hod_rejection",
    "reject_reason": "Buy is triggered near the top of the range after a strong selloff from HOD; structure looks like late continuation/reclaim rather than a fresh low stop-hunt reversal.",
    "proposed_filter": "Reject BUY signals when the latest entry is above Asian range mid/high after a fresh HOD rejection and no fresh second-leg low is visible."
  },
  {
    "review_id": "C02",
    "predicted_label": "winner",
    "confidence_0_100": 72,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "good; clear sell-side raid followed by sustained reclaim and trend continuation",
    "tdi_state_visible": "bullish recovery after prior weakness, though slightly late/overbought",
    "entry_timing": "acceptable_continuation",
    "reject_reason": "",
    "proposed_filter": "Allow when stop hunt occurs below the range and price reclaims LOD/AR with stacked 5/13/50 EMA support."
  },
  {
    "review_id": "C03",
    "predicted_label": "loser",
    "confidence_0_100": 63,
    "real_mmm_stop_hunt": "weak",
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "poor; price is already compressed near HOD after a long prior rally",
    "tdi_state_visible": "bearish/weak; green and red are below the yellow baseline and rolling down",
    "entry_timing": "late_at_hod",
    "reject_reason": "The buy is into HOD/Asian high after trend exhaustion, with no clean recent W-bottom trigger at the entry zone.",
    "proposed_filter": "Reject BUY when TDI is below the yellow baseline and curling down while price is parked at HOD/AR high."
  },
  {
    "review_id": "C04",
    "predicted_label": "winner",
    "confidence_0_100": 66,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "fair; strong reclaim from low and later consolidation above LOD",
    "tdi_state_visible": "improving; signal cross bullish from lower band area",
    "entry_timing": "acceptable_reclaim",
    "reject_reason": "",
    "proposed_filter": "Prefer cases where the post-hunt reclaim holds above LOD/50 EMA and TDI crosses up from the lower half."
  },
  {
    "review_id": "C05",
    "predicted_label": "loser",
    "confidence_0_100": 70,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "mixed; initial reversal worked but current entry is after a sharp HOD rejection and range chop",
    "tdi_state_visible": "weak; green is below midline and only starting to curl",
    "entry_timing": "late_after_distribution",
    "reject_reason": "Entry follows a completed run into HOD and a selloff back toward AR mid/LOD, making the buy a late re-entry in chop.",
    "proposed_filter": "Reject second-chance BUYs after a full HOD run unless price forms a fresh higher-low W above the 50 EMA with TDI above midline."
  },
  {
    "review_id": "C06",
    "predicted_label": "loser",
    "confidence_0_100": 69,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "initially strong but current setup is extended after the move",
    "tdi_state_visible": "bearish divergence/rolling down from upper band",
    "entry_timing": "very_late_after_impulse",
    "reject_reason": "The actual W-bottom has already paid; the visible entry is near LOD/HOD consolidation after a large impulse with TDI divergence.",
    "proposed_filter": "Reject BUY when the stop-hunt reversal has already traveled multiple pushes and TDI shows bearish divergence."
  },
  {
    "review_id": "C07",
    "predicted_label": "winner",
    "confidence_0_100": 71,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "good; base forms below/near weekly open then pushes cleanly back through range",
    "tdi_state_visible": "bullish recovery with green turning up from lower band",
    "entry_timing": "acceptable_breakout_retest",
    "reject_reason": "",
    "proposed_filter": "Allow if price reclaims the weekly open/LOD area after the stop hunt and holds above rising 13/50 EMA."
  },
  {
    "review_id": "C08",
    "predicted_label": "loser",
    "confidence_0_100": 82,
    "real_mmm_stop_hunt": "unclear",
    "return_inside_asian_range": false,
    "clean_w_bottom": false,
    "second_leg_quality": "poor; price is breaking down hard through LOD with no bullish reclaim",
    "tdi_state_visible": "bearish; green/red falling near lower band",
    "entry_timing": "countertrend_knife_catch",
    "reject_reason": "Despite the BUY label, visual structure is a decisive bearish breakdown below the Asian range and LOD.",
    "proposed_filter": "Reject BUY if current price is below Asian range low/LOD and 5/13 EMAs are sharply bearish."
  },
  {
    "review_id": "C09",
    "predicted_label": "winner",
    "confidence_0_100": 78,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "strong; tight low base, clean reclaim, then powerful expansion toward HOD",
    "tdi_state_visible": "bullish expansion from lower half into upper band",
    "entry_timing": "good",
    "reject_reason": "",
    "proposed_filter": "Keep setups with compact base below LOD/weekly open followed by clean EMA stack and TDI expansion."
  },
  {
    "review_id": "C10",
    "predicted_label": "loser",
    "confidence_0_100": 61,
    "real_mmm_stop_hunt": "weak",
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "poor; entry is at the top-side consolidation after a long advance",
    "tdi_state_visible": "weak; TDI is under midline and recovering only late",
    "entry_timing": "late_at_hod",
    "reject_reason": "The buy is late near HOD/Asian high after multiple pushes and TDI weakness, not at the original reversal.",
    "proposed_filter": "Reject BUY when price has already completed 3+ pushes into HOD and TDI is below 50 at entry."
  },
  {
    "review_id": "C11",
    "predicted_label": "winner",
    "confidence_0_100": 64,
    "real_mmm_stop_hunt": "yes",
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "mixed; large HOD rejection but current candle reclaims sharply from LOD/200 EMA area",
    "tdi_state_visible": "bullish rebound from lower band, but still recovering",
    "entry_timing": "aggressive_reversal",
    "reject_reason": "",
    "proposed_filter": "Allow only if the LOD reclaim candle closes back inside range and TDI green crosses up from the lower band."
  }
]

Blind Claude review:
[{"review_id":"C01","predicted_label":"loser","confidence_0_100":72,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"poor","tdi_state_visible":"shark_fin_long_fading","entry_timing":"late","reject_reason":"Price already peaked at HOD with TDI green crossing below red; entry during retracement off high; ADR% 49.6 suggests move already half-spent","proposed_filter":"reject_entry_when_tdi_green_below_red_and_price_below_hod"},{"review_id":"C02","predicted_label":"loser","confidence_0_100":65,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"adequate","tdi_state_visible":"rsi_overbought_shark_fin","entry_timing":"late","reject_reason":"ADR% 116.8 massively exceeded; buying into already-exhausted daily range with RSI overbought at 63; Asian range 3826p is wide","proposed_filter":"reject_entry_when_adr_pct_gt_100"},{"review_id":"C03","predicted_label":"winner","confidence_0_100":62,"real_mmm_stop_hunt":true,"return_inside_asian_range":true,"clean_w_bottom":true,"second_leg_quality":"adequate","tdi_state_visible":"shark_fin_long","entry_timing":"on_time","reject_reason":null,"proposed_filter":null},{"review_id":"C04","predicted_label":"winner","confidence_0_100":68,"real_mmm_stop_hunt":true,"return_inside_asian_range":true,"clean_w_bottom":true,"second_leg_quality":"good","tdi_state_visible":"vb_squeeze_signal_cross_bullish","entry_timing":"on_time","reject_reason":null,"proposed_filter":null},{"review_id":"C05","predicted_label":"loser","confidence_0_100":60,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"poor","tdi_state_visible":"signal_cross_bullish_weak","entry_timing":"late","reject_reason":"Choppy two-way action with spike-and-reversal; price fell from HOD back to LOD; no clean W-bottom visible; ADR 61% with declining momentum","proposed_filter":"reject_entry_when_price_spike_reversal_within_4_bars"},{"review_id":"C06","predicted_label":"winner","confidence_0_100":55,"real_mmm_stop_hunt":true,"return_inside_asian_range":true,"clean_w_bottom":true,"second_leg_quality":"adequate","tdi_state_visible":"shark_fin_long_bearish_divergence","entry_timing":"on_time","reject_reason":null,"proposed_filter":"flag_tdi_bearish_divergence_as_caution"},{"review_id":"C07","predicted_label":"winner","confidence_0_100":70,"real_mmm_stop_hunt":true,"return_inside_asian_range":true,"clean_w_bottom":true,"second_leg_quality":"good","tdi_state_visible":"rsi_overbought_mbl_cross_bullish","entry_timing":"on_time","reject_reason":null,"proposed_filter":null},{"review_id":"C08","predicted_label":"loser","confidence_0_100":75,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"poor","tdi_state_visible":"rsi_oversold_shark_fin","entry_timing":"late","reject_reason":"Friday session with NEUTRAL weekly bias (not BUY); choppy L3 structure with flat intertwined EMAs; confluence only 80/100; 4 pushes not 5; ADR 67.8% already consumed","proposed_filter":"reject_friday_entries_with_neutral_weekly_bias"},{"review_id":"C09","predicted_label":"loser","confidence_0_100":72,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"adequate","tdi_state_visible":"rsi_overbought_shark_fin","entry_timing":"late","reject_reason":"ADR% 125.5 massively exceeded; Asian range 6731p is double AvgAsia; buying at top of exhausted move; TDI overbought curling","proposed_filter":"reject_entry_when_adr_pct_gt_100"},{"review_id":"C10","predicted_label":"winner","confidence_0_100":66,"real_mmm_stop_hunt":true,"return_inside_asian_range":true,"clean_w_bottom":true,"second_leg_quality":"good","tdi_state_visible":"shark_fin_long","entry_timing":"on_time","reject_reason":null,"proposed_filter":null},{"review_id":"C11","predicted_label":"loser","confidence_0_100":68,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"poor","tdi_state_visible":"signal_cross_bullish_mbl_cross","entry_timing":"late","reject_reason":"Friday session; stop hunt only 612p (below XAUUSD 200p minimum threshold); only 3 pushes; sharp bearish reversal from spike high with large red candles at right edge","proposed_filter":"reject_friday_xauusd_with_sub_1000p_stop_hunt"}]


Return only the requested concise JSON object. Do not recommend live trading.
