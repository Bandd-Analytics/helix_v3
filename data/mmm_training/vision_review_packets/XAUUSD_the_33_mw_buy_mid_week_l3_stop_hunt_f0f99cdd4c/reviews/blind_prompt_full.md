You are running an account-backed MMM vision packet review.
Packet directory: C:\Users\dennis.ndungu\Desktop\ClaudeMCP\Helix_V3\data\mmm_training\vision_review_packets\XAUUSD_the_33_mw_buy_mid_week_l3_stop_hunt_f0f99cdd4c

Inspect only the chart images listed below. Do not read `answer_key.csv`, `manifest.json`, or outcome labels.

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

You are reviewing MMM trading flashcards blind. Do not use `answer_key.csv`.

Task: inspect each chart image and predict whether the setup was likely a winner or loser.

Pair: XAUUSD
Shared setup signature: THE_33_MW|BUY|MID_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS

Images:
- C01: `images/c01_fc43004_20250904T081500.png`
- C02: `images/c02_fc48567_20251229T071500.png`
- C03: `images/c03_fc48529_20251222T214500.png`
- C04: `images/c04_fc43005_20250904T094500.png`
- C05: `images/c05_fc48289_20251128T081500.png`
- C06: `images/c06_fc43006_20250904T111500.png`
- C07: `images/c07_fc48771_20260127T081500.png`
- C08: `images/c08_fc42984_20250903T024500.png`
- C09: `images/c09_fc48525_20251222T170000.png`
- C10: `images/c10_fc48266_20251126T154500.png`
- C11: `images/c11_fc48632_20260107T110000.png`

For each image, return a JSON array. Each object must contain:
`review_id`, `predicted_label`, `confidence_0_100`, `real_mmm_stop_hunt`, `return_inside_asian_range`, `clean_w_bottom`, `second_leg_quality`, `tdi_state_visible`, `entry_timing`, `reject_reason`, and `proposed_filter`.

Use only visual evidence from the chart. Be conservative: if the entry is unclear, label it loser.


Return only the requested JSON array. Do not include markdown fences or prose.
