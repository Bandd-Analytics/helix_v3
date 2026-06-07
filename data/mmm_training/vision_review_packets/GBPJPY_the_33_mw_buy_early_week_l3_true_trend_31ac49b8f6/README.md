# GBPJPY Vision Review Packet

Generated: 2026-06-07T15:15:17.452679+00:00

Purpose: isolate visual differences between winning and losing versions of the same MMM setup signature.

## Setup

- Pair: `GBPJPY`
- Signature: `THE_33_MW|BUY|EARLY_WEEK|L3|TRUE_TREND|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|RRT|TDI_CONFLICT|THE_33|CONF_75_PLUS`
- Total replay samples: 14
- Favorable rate: 64.3%
- Average exit: +6.2 pips
- Winners in packet: 8
- Losers in packet: 5

## Review Flow

1. Open `blind_prompt.md` and attach the images from `images/`.
2. Ask ChatGPT Pro and Claude Max to classify each chart without `answer_key.csv`.
3. Then open `labeled_comparison_prompt.md` with `answer_key.csv` and ask for winner-vs-loser visual filters.
4. Convert agreed filters into deterministic replay rules before any promotion.

## Files

- `manifest.json`: full packet metadata.
- `answer_key.csv`: outcome labels; hide during blind review.
- `review_matrix.csv`: fillable model-review table.
- `blind_prompt.md`: first-pass model prompt.
- `labeled_comparison_prompt.md`: second-pass explanation prompt.
