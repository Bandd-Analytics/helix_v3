Use the Read tool to inspect the local chart images when needed.
Packet directory: C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57

You are now allowed to use `answer_key.csv` after completing the blind review.

Compare winners against losers for this exact same MMM setup signature.

Pair: XAUUSD
Shared setup signature: RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74

Goal: identify the visual/structural filters that separate profitable examples from failed examples.

Return a concise JSON object with:
`summary`, `winner_traits`, `loser_traits`, `filters_to_test`, `filters_to_reject`, `pair_specific_notes`, `uncertain_items`, and `next_backtest_spec`.

Each `filters_to_test` item must be deterministic enough for Codex to encode. Include measurable thresholds where possible, such as candles, pips, ratios, relative position to Asian range, or TDI state.

Do not recommend live trading. These are research filters only.


Local chart images:
- C01: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c01_fc23859_20240102T070000.png`
- C02: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c02_fc24105_20240422T053000.png`
- C03: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c03_fc24106_20240422T070000.png`
- C04: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c04_fc24123_20240429T164500.png`
- C05: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c05_fc23923_20240126T140000.png`
- C06: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c06_fc21500_20220726T190000.png`
- C07: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c07_fc19823_20220517T194500.png`
- C08: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c08_fc24111_20240424T120000.png`
- C09: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c09_fc24154_20240507T191500.png`
- C10: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c10_fc24099_20240417T210000.png`
- C11: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c11_fc23885_20240111T161500.png`
- C12: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c12_fc23886_20240111T174500.png`
- C13: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_rrt_reversal_sell_mid_week_l0_return_accum_58876fba57\images\c13_fc24118_20240425T074500.png`

Answer key:
review_id,label,flashcard_id,snapshot_at,outcome,exit_pips,max_favorable_pips,max_adverse_pips,t1_hit,image_path
C01,loser,23859,2024-01-02T07:00:00+00:00,BREAKEVEN_AFTER_T1,0.0,78.00000000002001,63.99999999998727,True,images/c01_fc23859_20240102T070000.png
C02,winner,24105,2024-04-22T05:30:00+00:00,TIME_EXIT_PROFIT,1321.0000000000036,1381.00000000004,146.99999999998,False,images/c02_fc24105_20240422T053000.png
C03,winner,24106,2024-04-22T07:00:00+00:00,TIME_EXIT_PROFIT,1346.0000000000036,1980.9999999999945,155.0000000000182,True,images/c03_fc24106_20240422T070000.png
C04,loser,24123,2024-04-29T16:45:00+00:00,LOSS,-388.99999999998727,11.000000000012733,432.9999999999927,False,images/c04_fc24123_20240429T164500.png
C05,winner,23923,2024-01-26T14:00:00+00:00,TARGET_2,257.4999999999932,334.9999999999909,46.00000000000364,True,images/c05_fc23923_20240126T140000.png
C06,loser,21500,2022-07-26T19:00:00+00:00,STALE_EXIT,-59.999999999990905,127.99999999999727,199.0000000000009,False,images/c06_fc21500_20220726T190000.png
C07,winner,19823,2022-05-17T19:45:00+00:00,TIME_EXIT_PROFIT,539.9999999999864,765.9999999999854,58.00000000001546,False,images/c07_fc19823_20220517T194500.png
C08,winner,24111,2024-04-24T12:00:00+00:00,TIME_EXIT_PROFIT,425.99999999997635,579.9999999999727,96.00000000000364,False,images/c08_fc24111_20240424T120000.png
C09,winner,24154,2024-05-07T19:15:00+00:00,TIME_EXIT_PROFIT,290.99999999998545,456.9999999999709,178.00000000002,False,images/c09_fc24154_20240507T191500.png
C10,winner,24099,2024-04-17T21:00:00+00:00,OPEN_PROFIT,1644.0000000000055,2292.0000000000073,113.00000000001091,True,images/c10_fc24099_20240417T210000.png
C11,loser,23885,2024-01-11T16:15:00+00:00,LOSS,-340.99999999998545,147.00000000000273,539.9999999999864,False,images/c11_fc23885_20240111T161500.png
C12,winner,23886,2024-01-11T17:45:00+00:00,TARGET_2,944.9999999999932,1292.9999999999836,52.99999999999727,True,images/c12_fc23886_20240111T174500.png
C13,loser,24118,2024-04-25T07:45:00+00:00,STALE_EXIT,-414.00000000003274,83.99999999996908,545.0000000000273,False,images/c13_fc24118_20240425T074500.png


Blind Codex review:
[
  {
    "review_id": "C01",
    "predicted_label": "loser",
    "confidence_0_100": 62,
    "real_mmm_stop_hunt": false,
    "return_inside_asian_range": false,
    "clean_w_bottom": false,
    "second_leg_quality": "weak; sell arrives after recovery from LOD and near upper Asian range without a clean fresh high rejection",
    "tdi_state_visible": "bullish_conflict",
    "entry_timing": "late_against_current_push",
    "reject_reason": "price is pressing back toward HOD/Asian high with bullish TDI momentum, not rejecting cleanly from a completed stop hunt",
    "proposed_filter": "reject sells when current candles are closing back above AR mid/high and TDI green/red are rising"
  },
  {
    "review_id": "C02",
    "predicted_label": "winner",
    "confidence_0_100": 67,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "good; reversal follows an extended rise into HOD/weekly open area then rolls back below moving averages",
    "tdi_state_visible": "bearish_oversold_continuation",
    "entry_timing": "acceptable_after_breakdown",
    "reject_reason": "",
    "proposed_filter": "prefer sells that break back below AR mid after HOD rejection with TDI green/red both below yellow"
  },
  {
    "review_id": "C03",
    "predicted_label": "winner",
    "confidence_0_100": 78,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "strong; clear HOD rejection, lower highs, downside expansion, and weak pullback into continuation",
    "tdi_state_visible": "bearish_continuation_from_oversold",
    "entry_timing": "good_continuation_entry",
    "reject_reason": "",
    "proposed_filter": "keep sells after HOD rejection when price is below AR mid and below fast averages with TDI still bearish"
  },
  {
    "review_id": "C04",
    "predicted_label": "loser",
    "confidence_0_100": 70,
    "real_mmm_stop_hunt": false,
    "return_inside_asian_range": true,
    "clean_w_bottom": true,
    "second_leg_quality": "poor; sell appears after a deep LOD sweep and sharp bullish recovery into HOD",
    "tdi_state_visible": "bearish_pullback_but_not_clean",
    "entry_timing": "late_after_failed_high_break",
    "reject_reason": "market shows a strong W-bottom style recovery and sell is into mixed structure rather than a clean top reversal",
    "proposed_filter": "reject sells when the preceding move is a strong LOD-to-HOD reversal with higher lows intact"
  },
  {
    "review_id": "C05",
    "predicted_label": "loser",
    "confidence_0_100": 64,
    "real_mmm_stop_hunt": false,
    "return_inside_asian_range": false,
    "clean_w_bottom": false,
    "second_leg_quality": "weak; price is holding near HOD after a steady trend up and not yet breaking down",
    "tdi_state_visible": "bullish_conflict",
    "entry_timing": "early_before_reversal_confirmation",
    "reject_reason": "sell is fighting a strong bullish structure with price still above AR mid and near session highs",
    "proposed_filter": "require a decisive close back below AR mid or 50 EMA before accepting HOD sells"
  },
  {
    "review_id": "C06",
    "predicted_label": "loser",
    "confidence_0_100": 66,
    "real_mmm_stop_hunt": false,
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "poor; signal occurs in low-position consolidation after the main selloff already happened",
    "tdi_state_visible": "bearish_but_flattening",
    "entry_timing": "late_after_extension",
    "reject_reason": "entry is near LOD/AR low after a completed drop, leaving poor downside room and reversal risk",
    "proposed_filter": "reject sells when price is already near current LOD unless there is fresh high-side liquidity taken first"
  },
  {
    "review_id": "C07",
    "predicted_label": "winner",
    "confidence_0_100": 71,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "good; HOD stop hunt is followed by strong bearish displacement back through AR mid",
    "tdi_state_visible": "bearish_from_overbought",
    "entry_timing": "good_after_reversal_confirmed",
    "reject_reason": "",
    "proposed_filter": "favor sells after HOD sweep when price closes below fast averages and TDI turns sharply down"
  },
  {
    "review_id": "C08",
    "predicted_label": "loser",
    "confidence_0_100": 68,
    "real_mmm_stop_hunt": false,
    "return_inside_asian_range": false,
    "clean_w_bottom": false,
    "second_leg_quality": "weak; price is only pulling back from HOD inside a broader bullish day",
    "tdi_state_visible": "bearish_pullback",
    "entry_timing": "early_without_structure_break",
    "reject_reason": "sell lacks a convincing breakdown and remains high in a bullish Asian-range expansion",
    "proposed_filter": "reject sells while price remains above AR mid and 50 EMA after an unbroken bullish expansion"
  },
  {
    "review_id": "C09",
    "predicted_label": "loser",
    "confidence_0_100": 60,
    "real_mmm_stop_hunt": false,
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "mixed; downside trend exists but entry is after a large bearish leg and near range lows",
    "tdi_state_visible": "bearish_but_extended",
    "entry_timing": "late_after_move",
    "reject_reason": "sell appears stretched near LOD with limited room before mean reversion",
    "proposed_filter": "avoid fresh sells after a large completed leg unless pullback retests AR mid from below"
  },
  {
    "review_id": "C10",
    "predicted_label": "winner",
    "confidence_0_100": 73,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "good; repeated HOD rejection is followed by sharp breakdown through AR mid",
    "tdi_state_visible": "bearish_reversal",
    "entry_timing": "good_after_hod_failure",
    "reject_reason": "",
    "proposed_filter": "keep sells where HOD rejection produces a large bearish displacement back below AR mid"
  },
  {
    "review_id": "C11",
    "predicted_label": "loser",
    "confidence_0_100": 58,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "mixed; genuine high-side raid but immediate candles are volatile and not cleanly continuing lower",
    "tdi_state_visible": "bearish_turn_from_high",
    "entry_timing": "unclear_after_news_like_spike",
    "reject_reason": "large wick/spike behavior makes the entry noisy with no clean lower-high continuation at the snapshot",
    "proposed_filter": "reject spike candles unless followed by orderly lower-high compression below AR mid"
  },
  {
    "review_id": "C12",
    "predicted_label": "winner",
    "confidence_0_100": 69,
    "real_mmm_stop_hunt": true,
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "good; HOD raid rejects and price returns under the white/AR mid area with bearish TDI roll",
    "tdi_state_visible": "bearish_reversal",
    "entry_timing": "acceptable_after_rejection",
    "reject_reason": "",
    "proposed_filter": "prefer the later entry after the raid has closed back inside range and TDI green crosses down"
  },
  {
    "review_id": "C13",
    "predicted_label": "loser",
    "confidence_0_100": 63,
    "real_mmm_stop_hunt": false,
    "return_inside_asian_range": true,
    "clean_w_bottom": false,
    "second_leg_quality": "weak; sell follows a hard drop and partial bounce rather than a clean HOD rejection",
    "tdi_state_visible": "bullish_rebound_from_oversold",
    "entry_timing": "late_after_lod_sweep",
    "reject_reason": "setup is near low-side exhaustion with TDI rebounding, so continuation sell quality is poor",
    "proposed_filter": "reject sells when the latest impulse already swept LOD and TDI green is hooking up from oversold"
  }
]

Blind Claude review:
[{"review_id":"C01","predicted_label":"loser","confidence_0_100":72,"real_mmm_stop_hunt":false,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"SIGNAL_CROSS_BULLISH","entry_timing":"late","reject_reason":"TDI bullish cross conflicts with SELL; price near LOD after extended drop, selling into exhaustion; Asian range 945p oversized; no M/W pattern","proposed_filter":"block_sell_when_tdi_bullish_cross_and_price_at_lod"},{"review_id":"C02","predicted_label":"loser","confidence_0_100":82,"real_mmm_stop_hunt":false,"return_inside_asian_range":true,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"RSI_OVERSOLD_HOOK_BULLISH","entry_timing":"late","reject_reason":"TDI RSI oversold at 37 with bullish hook directly contradicts SELL; price chopping around EMA cluster near WK OPEN; no M/W formation; Asian range 1672p overextended","proposed_filter":"block_sell_when_tdi_rsi_below_40_with_bullish_hook"},{"review_id":"C03","predicted_label":"winner","confidence_0_100":60,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"SHARK_FIN_LONG","entry_timing":"acceptable","reject_reason":"TDI shark fin long conflicts but price visibly collapsing below WK OPEN L with strong bearish candles; momentum overriding TDI lag","proposed_filter":"none"},{"review_id":"C04","predicted_label":"loser","confidence_0_100":75,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"SHARK_FIN_LONG","entry_timing":"late","reject_reason":"Price bouncing off LOD with large green candles at right edge; TDI shark fin long = bullish; selling into buyers reclaiming Asian range low; ADR% 63.1% already consumed","proposed_filter":"block_sell_when_price_bouncing_off_lod_with_bullish_tdi"},{"review_id":"C05","predicted_label":"loser","confidence_0_100":78,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"SIGNAL_CROSS_BULLISH","entry_timing":"counter_trend","reject_reason":"Price making higher highs at right edge, clear uptrend; TDI bullish cross at RSI 57 confirms buyers; selling against visible momentum; Asian range 486p tight but breakout is upward","proposed_filter":"block_sell_when_price_making_higher_highs_above_asian_high"},{"review_id":"C06","predicted_label":"loser","confidence_0_100":80,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"BULLISH_DIVERGENCE","entry_timing":"late","reject_reason":"TDI showing bullish divergence at RSI 44 = strong reversal signal against sell; price bouncing near WK OPEN L; multiple green entry arrows at bottom suggest demand zone; ADR% 61.2% already used","proposed_filter":"hard_block_sell_when_tdi_bullish_divergence"},{"review_id":"C07","predicted_label":"winner","confidence_0_100":65,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"SHARK_FIN_LONG","entry_timing":"acceptable","reject_reason":"Despite TDI shark fin long conflict, price visibly reversing hard from HOD with large bearish candles; RRT reversal timing aligns with top formation; sharp sell-off visible at right edge","proposed_filter":"none"},{"review_id":"C08","predicted_label":"loser","confidence_0_100":65,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"SIGNAL_CROSS_BULLISH_SHARK_FIN_LONG","entry_timing":"late","reject_reason":"Dual TDI conflict: signal cross bullish AND shark fin long; price chopping around EMA cluster after HOD drop; RSI 42 with bullish TDI = likely bounce; no clean sell structure","proposed_filter":"block_sell_when_dual_tdi_bullish_signals"},{"review_id":"C09","predicted_label":"winner","confidence_0_100":58,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"SIGNAL_CROSS_BULLISH","entry_timing":"acceptable","reject_reason":"TDI bullish cross conflicts but price showing clean drop from HOD with bearish structure; 3 pushes met target; price breaking below key EMA levels; weekly SELL bias supports","proposed_filter":"none"},{"review_id":"C10","predicted_label":"loser","confidence_0_100":70,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"SHARK_FIN_LONG","entry_timing":"late","reject_reason":"ADR% 85.4% already consumed, insufficient room for sell to reach TP; price choppy at HOD with green arrows showing buyer interest; TDI shark fin long conflicts; WK OPEN range suggesting consolidation not breakdown","proposed_filter":"block_sell_when_adr_pct_above_80"},{"review_id":"C11","predicted_label":"loser","confidence_0_100":90,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"SHARK_FIN_LONG","entry_timing":"counter_trend","reject_reason":"Massive bullish spike visible at right edge to R1 level; price exploded upward destroying any sell; TDI shark fin long was correctly signaling buy; selling into parabolic move = guaranteed stop hit","proposed_filter":"hard_block_sell_when_impulsive_bullish_breakout_visible"},{"review_id":"C12","predicted_label":"loser","confidence_0_100":88,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"SHARK_FIN_LONG","entry_timing":"counter_trend","reject_reason":"Same session as C11 with massive bullish spike already printed; price elevated well above EMAs after impulsive move; selling after parabolic up-move with TDI shark fin long = chasing into strength","proposed_filter":"hard_block_sell_after_impulsive_bullish_candle_above_r1"},{"review_id":"C13","predicted_label":"winner","confidence_0_100":55,"real_mmm_stop_hunt":true,"return_inside_asian_range":false,"clean_w_bottom":false,"second_leg_quality":"none","tdi_state_visible":"MBL_CROSS_BULLISH","entry_timing":"acceptable","reject_reason":"TDI MBL cross bullish conflicts but price breaking below EMA cluster with bearish candles toward LOD/S1; momentum favoring sell at right edge despite TDI lag; ADR% 41.7% leaves room for continuation","proposed_filter":"none"}]


Return only the requested concise JSON object. Do not recommend live trading.
