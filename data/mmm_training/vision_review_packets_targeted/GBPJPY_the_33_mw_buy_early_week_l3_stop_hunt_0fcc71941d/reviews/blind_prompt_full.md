You are running an account-backed MMM vision packet review.
Packet directory: C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets_targeted\GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_0fcc71941d

Inspect only the chart images listed below. Do not read `answer_key.csv`, `manifest.json`, or outcome labels.

Local chart images:
- C01: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets_targeted\GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_0fcc71941d\images\c01_fc12739_20240527T053000.png`
- C02: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets_targeted\GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_0fcc71941d\images\c02_fc4924_20260413T063000.png`
- C03: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets_targeted\GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_0fcc71941d\images\c03_fc811_20240527T050000.png`
- C04: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets_targeted\GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_0fcc71941d\images\c04_fc4878_20251208T050000.png`
- C05: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets_targeted\GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_0fcc71941d\images\c05_fc12740_20240527T071500.png`
- C06: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets_targeted\GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_0fcc71941d\images\c06_fc4816_20250915T063000.png`
- C07: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets_targeted\GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_0fcc71941d\images\c07_fc12958_20250915T064500.png`
- C08: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets_targeted\GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_0fcc71941d\images\c08_fc4853_20251027T050000.png`
- C09: `C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets_targeted\GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_0fcc71941d\images\c09_fc850_20241014T050000.png`

You are reviewing MMM trading flashcards blind. Do not use `answer_key.csv`.

Task: inspect each chart image and predict whether the setup was likely a winner or loser.

Pair: GBPJPY
Shared setup signature: THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74

Images:
- C01: `images/c01_fc12739_20240527T053000.png`
- C02: `images/c02_fc4924_20260413T063000.png`
- C03: `images/c03_fc811_20240527T050000.png`
- C04: `images/c04_fc4878_20251208T050000.png`
- C05: `images/c05_fc12740_20240527T071500.png`
- C06: `images/c06_fc4816_20250915T063000.png`
- C07: `images/c07_fc12958_20250915T064500.png`
- C08: `images/c08_fc4853_20251027T050000.png`
- C09: `images/c09_fc850_20241014T050000.png`

For each image, return a JSON array. Each object must contain:
`review_id`, `predicted_label`, `confidence_0_100`, `real_mmm_stop_hunt`, `return_inside_asian_range`, `clean_w_bottom`, `second_leg_quality`, `tdi_state_visible`, `entry_timing`, `reject_reason`, and `proposed_filter`.

Use only visual evidence from the chart. Be conservative: if the entry is unclear, label it loser.


Return only the requested JSON array. Do not include markdown fences or prose.
