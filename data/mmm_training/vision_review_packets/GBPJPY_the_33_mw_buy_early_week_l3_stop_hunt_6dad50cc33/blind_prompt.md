You are reviewing MMM trading flashcards blind. Do not use `answer_key.csv`.

Task: inspect each chart image and predict whether the setup was likely a winner or loser.

Pair: GBPJPY
Shared setup signature: THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74

Images:
- C01: `images/c01_fc4555_20240226T064500.png`
- C02: `images/c02_fc4539_20240219T064500.png`
- C03: `images/c03_fc512_20251208T060000.png`
- C04: `images/c04_fc4579_20240401T051500.png`
- C05: `images/c05_fc4687_20241014T051500.png`
- C06: `images/c06_fc743_20240219T070000.png`
- C07: `images/c07_fc4688_20241014T064500.png`
- C08: `images/c08_fc4636_20240527T064500.png`
- C09: `images/c09_fc772_20240401T050000.png`
- C10: `images/c10_fc812_20240527T070000.png`
- C11: `images/c11_fc777_20240408T050000.png`

For each image, return a JSON array. Each object must contain:
`review_id`, `predicted_label`, `confidence_0_100`, `real_mmm_stop_hunt`, `return_inside_asian_range`, `clean_w_bottom`, `second_leg_quality`, `tdi_state_visible`, `entry_timing`, `reject_reason`, and `proposed_filter`.

Use only visual evidence from the chart. Be conservative: if the entry is unclear, label it loser.
