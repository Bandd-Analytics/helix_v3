You are reviewing MMM trading flashcards blind. Do not use `answer_key.csv`.

Task: inspect each chart image and predict whether the setup was likely a winner or loser.

Pair: GBPJPY
Shared setup signature: THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_NONE|THE_33|CONF_50_74

Images:
- C01: `images/c01_fc4925_20260413T080000.png`
- C02: `images/c02_fc775_20240401T110000.png`
- C03: `images/c03_fc745_20240219T110000.png`
- C04: `images/c04_fc4542_20240219T111500.png`
- C05: `images/c05_fc515_20251208T120000.png`
- C06: `images/c06_fc4818_20250915T093000.png`
- C07: `images/c07_fc514_20251208T100000.png`
- C08: `images/c08_fc4581_20240401T081500.png`
- C09: `images/c09_fc757_20240226T110000.png`
- C10: `images/c10_fc4557_20240226T094500.png`

For each image, return a JSON array. Each object must contain:
`review_id`, `predicted_label`, `confidence_0_100`, `real_mmm_stop_hunt`, `return_inside_asian_range`, `clean_w_bottom`, `second_leg_quality`, `tdi_state_visible`, `entry_timing`, `reject_reason`, and `proposed_filter`.

Use only visual evidence from the chart. Be conservative: if the entry is unclear, label it loser.
