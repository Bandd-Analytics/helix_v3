You are reviewing MMM trading flashcards blind. Do not use `answer_key.csv`.

Task: inspect each chart image and predict whether the setup was likely a winner or loser.

Pair: XAUUSD
Shared setup signature: RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFIRM|THE_33|CONF_75_PLUS

Images:
- C01: `images/c01_fc34706_20250421T030000.png`
- C02: `images/c02_fc29763_20240923T154500.png`
- C03: `images/c03_fc30046_20241029T150000.png`
- C04: `images/c04_fc29585_20240829T174500.png`
- C05: `images/c05_fc27122_20240708T071500.png`
- C06: `images/c06_fc34469_20250313T120000.png`
- C07: `images/c07_fc27120_20240708T041500.png`
- C08: `images/c08_fc34690_20250415T190000.png`
- C09: `images/c09_fc32525_20250116T050000.png`
- C10: `images/c10_fc27411_20240814T071500.png`
- C11: `images/c11_fc27124_20240708T101500.png`

For each image, return a JSON array. Each object must contain:
`review_id`, `predicted_label`, `confidence_0_100`, `real_mmm_stop_hunt`, `return_inside_asian_range`, `clean_w_bottom`, `second_leg_quality`, `tdi_state_visible`, `entry_timing`, `reject_reason`, and `proposed_filter`.

Use only visual evidence from the chart. Be conservative: if the entry is unclear, label it loser.
