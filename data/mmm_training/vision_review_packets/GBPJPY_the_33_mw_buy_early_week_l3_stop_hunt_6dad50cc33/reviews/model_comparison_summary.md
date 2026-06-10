# GBPJPY Stop-Hunt Packet Vision Review Summary

Packet: `GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_6dad50cc33`

## Blind Accuracy

| Model | Correct | Total | Accuracy | Misses |
|---|---:|---:|---:|---|
| Codex / ChatGPT Pro | 4 | 11 | 36.4% | C01, C02, C05, C06, C08, C09, C10 |
| Claude Max | 4 | 11 | 36.4% | C01, C03, C04, C05, C08, C09, C10 |

## Shared Filter Hypotheses

- Test a GBPJPY `hunt_to_ar_ratio` cap first. Claude proposed `<= 2.0`; Codex proposed an absolute extreme cap around `90p`, but both targeted oversized hunts/trend moves.
- Test a range reacceptance requirement: close back above Asian-range low or weekly-open low after the hunt before accepting BUY.
- Test a HOD/late-chase block for BUY entries after vertical expansion without a fresh low-side reset.
- Use TDI as a soft quality booster, not a hard gate. Both reviews found TDI useful, but hard TDI gates would remove some winners.
- Test EMA structure: reject tangled/flat EMA cluster or descending EMA200 for BUY when the setup is supposed to reverse upward.

## Next Backtest Features To Encode

- `hunt_to_ar_ratio = stop_hunt_pips / asian_range_pips`
- `candles_since_hunt_low`
- `close_distance_to_ar_low_pips` and `close_distance_to_ar_mid_pips`
- `close_distance_to_hod_pips`
- `prior_8_candle_up_move_pips` and pullback from HOD
- `ema50_ema200_spread_pips` and `ema200_slope_8_bars_pips`
- `tdi_rsi_minus_signal` and short TDI slope

## Notes

- This packet has only 11 cases and 3 losers, so the filters are hypotheses, not rules.
- The next step is to encode these features and run ablations across all GBPJPY/EURJPY research candidates.
