You are now allowed to use `answer_key.csv` after completing the blind review.

Compare winners against losers for this exact same MMM setup signature.

Pair: XAUUSD
Shared setup signature: RRT_REVERSAL|SELL|EARLY_WEEK|L0|RETURN_ACCUM|AR_TIGHT|HUNT_PAIR_RANGE|PUSH3_PLUS|NO_MW|RRT|TDI_CONFLICT|THE_33|CONF_50_74

Goal: identify the visual/structural filters that separate profitable examples from failed examples.

Return a concise JSON object with:
`summary`, `winner_traits`, `loser_traits`, `filters_to_test`, `filters_to_reject`, `pair_specific_notes`, `uncertain_items`, and `next_backtest_spec`.

Each `filters_to_test` item must be deterministic enough for Codex to encode. Include measurable thresholds where possible, such as candles, pips, ratios, relative position to Asian range, or TDI state.

Do not recommend live trading. These are research filters only.
