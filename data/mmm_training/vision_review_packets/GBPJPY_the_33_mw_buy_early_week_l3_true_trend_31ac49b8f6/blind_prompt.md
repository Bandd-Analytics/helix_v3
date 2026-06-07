You are reviewing MMM trading flashcards blind. Do not use `answer_key.csv`.

Task: inspect each chart image and predict whether the setup was likely a winner or loser.

Pair: GBPJPY
Shared setup signature: THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS

Images:
- C01: `images/c01_fc4540_20240219T081500.png`
- C02: `images/c02_fc718_20240122T120000.png`
- C03: `images/c03_fc4559_20240226T124500.png`
- C04: `images/c04_fc648_20230925T110000.png`
- C05: `images/c05_fc4881_20251208T081500.png`
- C06: `images/c06_fc4412_20230925T111500.png`
- C07: `images/c07_fc513_20251208T080000.png`
- C08: `images/c08_fc4486_20231113T094500.png`
- C09: `images/c09_fc4616_20240422T121500.png`
- C10: `images/c10_fc4874_20251117T110000.png`
- C11: `images/c11_fc4690_20241014T094500.png`
- C12: `images/c12_fc4889_20251222T111500.png`
- C13: `images/c13_fc4772_20250818T080000.png`

For each image, return a JSON array. Each object must contain:
`review_id`, `predicted_label`, `confidence_0_100`, `real_mmm_stop_hunt`, `return_inside_asian_range`, `clean_w_bottom`, `second_leg_quality`, `tdi_state_visible`, `entry_timing`, `reject_reason`, and `proposed_filter`.

Use only visual evidence from the chart. Be conservative: if the entry is unclear, label it loser.
