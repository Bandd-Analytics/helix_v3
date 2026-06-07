You are reviewing MMM trading flashcards blind. Do not use `answer_key.csv`.

Task: inspect each chart image and predict whether the setup was likely a winner or loser.

Pair: EURJPY
Shared setup signature: THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_75_PLUS

Images:
- C01: `images/c01_fc6208_20241014T110000.png`
- C02: `images/c02_fc6365_20250915T083000.png`
- C03: `images/c03_fc1804_20240408T111500.png`
- C04: `images/c04_fc6470_20260216T080000.png`
- C05: `images/c05_fc6097_20240513T083000.png`
- C06: `images/c06_fc6366_20250915T100000.png`
- C07: `images/c07_fc6385_20250922T120000.png`
- C08: `images/c08_fc6207_20241014T093000.png`
- C09: `images/c09_fc6354_20250901T083000.png`
- C10: `images/c10_fc6057_20240408T110000.png`
- C11: `images/c11_fc6045_20240318T083000.png`
- C12: `images/c12_fc5942_20231218T080000.png`

For each image, return a JSON array. Each object must contain:
`review_id`, `predicted_label`, `confidence_0_100`, `real_mmm_stop_hunt`, `return_inside_asian_range`, `clean_w_bottom`, `second_leg_quality`, `tdi_state_visible`, `entry_timing`, `reject_reason`, and `proposed_filter`.

Use only visual evidence from the chart. Be conservative: if the entry is unclear, label it loser.
