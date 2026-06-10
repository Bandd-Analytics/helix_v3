You are reviewing MMM trading flashcards blind. Do not use `answer_key.csv`.

Task: inspect each chart image and predict whether the setup was likely a winner or loser.

Pair: XAUUSD
Shared setup signature: RRT_REVERSAL|SELL|MID_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74

Images:
- C01: `images/c01_fc23859_20240102T070000.png`
- C02: `images/c02_fc24105_20240422T053000.png`
- C03: `images/c03_fc24106_20240422T070000.png`
- C04: `images/c04_fc24123_20240429T164500.png`
- C05: `images/c05_fc23923_20240126T140000.png`
- C06: `images/c06_fc21500_20220726T190000.png`
- C07: `images/c07_fc19823_20220517T194500.png`
- C08: `images/c08_fc24111_20240424T120000.png`
- C09: `images/c09_fc24154_20240507T191500.png`
- C10: `images/c10_fc24099_20240417T210000.png`
- C11: `images/c11_fc23885_20240111T161500.png`
- C12: `images/c12_fc23886_20240111T174500.png`
- C13: `images/c13_fc24118_20240425T074500.png`

For each image, return a JSON array. Each object must contain:
`review_id`, `predicted_label`, `confidence_0_100`, `real_mmm_stop_hunt`, `return_inside_asian_range`, `clean_w_bottom`, `second_leg_quality`, `tdi_state_visible`, `entry_timing`, `reject_reason`, and `proposed_filter`.

Use only visual evidence from the chart. Be conservative: if the entry is unclear, label it loser.
