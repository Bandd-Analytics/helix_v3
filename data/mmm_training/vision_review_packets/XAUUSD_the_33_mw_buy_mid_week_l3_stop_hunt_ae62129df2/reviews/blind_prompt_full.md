You are running an account-backed MMM vision packet review.
Packet directory: C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_ae62129df2

Inspect only the chart images listed below. Do not read `answer_key.csv`, `manifest.json`, or outcome labels.

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

You are reviewing MMM trading flashcards blind. Do not use `answer_key.csv`.

Task: inspect each chart image and predict whether the setup was likely a winner or loser.

Pair: XAUUSD
Shared setup signature: THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS

Images:
- C01: `images/c01_fc48267_20251126T171500.png`
- C02: `images/c02_fc43353_20251008T151500.png`
- C03: `images/c03_fc43331_20251007T091500.png`
- C04: `images/c04_fc42968_20250902T040000.png`
- C05: `images/c05_fc48482_20251217T150000.png`
- C06: `images/c06_fc43051_20250909T023000.png`
- C07: `images/c07_fc48531_20251223T010000.png`
- C08: `images/c08_fc48230_20251121T090000.png`
- C09: `images/c09_fc48524_20251222T153000.png`
- C10: `images/c10_fc43329_20251007T061500.png`
- C11: `images/c11_fc48294_20251128T154500.png`

For each image, return a JSON array. Each object must contain:
`review_id`, `predicted_label`, `confidence_0_100`, `real_mmm_stop_hunt`, `return_inside_asian_range`, `clean_w_bottom`, `second_leg_quality`, `tdi_state_visible`, `entry_timing`, `reject_reason`, and `proposed_filter`.

Use only visual evidence from the chart. Be conservative: if the entry is unclear, label it loser.


Return only the requested JSON array. Do not include markdown fences or prose.
