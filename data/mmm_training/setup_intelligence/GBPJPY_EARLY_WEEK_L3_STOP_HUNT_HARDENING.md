# GBPJPY Early-Week L3 Stop-Hunt Hardening Audit

Generated: 2026-06-11 16:04 EAT

This is an offline research audit. It does not place trades, change pair profiles, or approve live
execution.

## Candidate

Setup key:

`THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|AR_VALID|HUNT_PAIR_RANGE|PUSH3_PLUS|W_BOTTOM|NO_RRT|TDI_CONFIRM|THE_33|CONF_50_74`

Interpretation:

- Pair/direction: `GBPJPY BUY`
- Family: `THE_33_MW`
- Weekly timing: `EARLY_WEEK`
- H4 level: `L3`
- H1 session/theme: `STOP_HUNT`
- Asian range: `AR_VALID`
- Hunt bucket: `HUNT_PAIR_RANGE`
- Structure: `PUSH3_PLUS`, `W_BOTTOM`
- RRT state: `NO_RRT`
- TDI state: `TDI_CONFIRM`
- Confluence bucket: `CONF_50_74`

## Stored Evidence

Source: `logs/setup_intelligence.db`

| Metric | Value |
|---|---:|
| Total occurrences | 10 |
| Favorable outcomes | 9 |
| Favorable rate | 90.0% |
| Average exit | +18.4 pips |
| Average win | +20.8 pips |
| Average loss | -2.7 pips |
| Profit factor | 69.22 |
| Payoff ratio | 7.69 |
| T1 hit rate | 50.0% |
| Average MFE | +25.7 pips |
| Average MAE | +7.2 pips |
| Split summary | train N=4 Avg=+7.9; validation N=3 Avg=+29.5; OOS N=3 Avg=+21.4 |
| Alert basket rank | #1 `DEMO_ALERT` |

Year distribution:

| Year | N | Fav | AvgExit | MinExit | MaxExit |
|---|---:|---:|---:|---:|---:|
| 2024 | 5 | 4 | +13.3 | -2.7 | +34.8 |
| 2025 | 4 | 4 | +21.9 | +11.9 | +32.8 |
| 2026 | 1 | 1 | +30.5 | +30.5 | +30.5 |

The only losing occurrence was `2024-05-27T05:00:00+00:00`, outcome `TIME_EXIT_LOSS`, exit
`-2.7p`, MFE `+4.0p`, MAE `+13.3p`, confluence `60`, price level `AR_LOWER_MID`.

## Validation-Library Status

Source: `logs/validation_library.db`

This exact setup exists as a local `PAIR` validation-library record:

| Field | Value |
|---|---:|
| Record id | 1882 |
| Scope | `PAIR` |
| Symbol | `GBPJPY` |
| Direction | `BUY` |
| Total | 10 |
| Favorable rate | 90.0% |
| Average exit | +18.4 pips |
| Confidence score | 88.4 |
| Realistic target | +18.4 pips |
| Updated | 2026-06-10 21:10 UTC |

This does not imply live approval. `GBPJPY` is tradeable in `config/pair_profiles.py`, but any
execution use still depends on the orchestrator/gatekeeper path and explicit user approval.

## Hardening Assessment

Decision: `DEMO_ALERT`, not live-auto-entry.

Rationale:

- The base setup is strong enough to keep at the top of the demo/watchdog basket.
- Evidence is still sparse: 10 total cases, with only 1 case in 2026.
- The stricter ablation variants are cleaner but too small for promotion:
  - `hunt_to_ar_ratio_le_2_5`: 6 kept, 100.0% favorable, +25.5p average exit.
  - Best-variant split sizes are only train N=1, validation N=4, OOS N=1.
- The current pair-level validation row is useful as a replay-derived candidate, not as a reason to
  widen live risk.
- Cross-pair evidence for the same normalized key is weaker than the GBPJPY pair-specific record.

## 2026-06-12 Vision and Feature Follow-Up

Targeted paid-account review packet:

`data/mmm_training/vision_review_packets_targeted/GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_0fcc71941d/`

Blind model separation was not reliable:

| Model | Correct | Total | Accuracy |
|---|---:|---:|---:|
| Codex / ChatGPT Pro | 3 | 9 | 33.3% |
| Claude Max | 3 | 9 | 33.3% |

Do not use the blind labels as a filter. The useful labeled-review hypothesis was narrower:
same-session timing and post-hunt confirmation matter more than adding a blanket clean-W,
range-reclaim, or TDI veto.

New deterministic features were backfilled for `GBPJPY,EURJPY` historical flashcards:

- `feature_cluster_index_150m`
- `feature_higher_low_after_hunt`
- `feature_close_vs_ema_fast_pips`
- `feature_reclaim_ar_mid_within_3`
- `feature_first_2_bar_mae_pips`
- `feature_first_3_bar_mfe_pips`
- `feature_first_3_bar_mfe_mae_ratio`

Targeted packet ablation highlights:

| Variant | Kept | Fav% | AvgExit | Note |
|---|---:|---:|---:|---|
| `all` | 10 | 90.0% | +18.4 | Baseline remains strong but sparse. |
| `feature_shark_fin_cluster_wait` | 9 | 100.0% | +20.8 | Removed the one known loser while keeping 9/10 cases. |
| `feature_confirmation_timing_or_quality` | 9 | 100.0% | +20.8 | Same retained set as shark-fin cluster wait. |
| `feature_tdi_quality_gte_1` | 5 | 100.0% | +25.6 | Cleaner but too restrictive for promotion. |

Pair-level ablation still blocks promotion. The exact setup's best strict variant has only
5 kept records, with train N=2, validation N=2, and out-of-sample N=1, below the configured
split minimum of 3 per segment. Decision remains `research_only_split_fail` for strict filters and
`DEMO_ALERT` for the base setup.

## Next Gates

Before using this beyond alert/demo observation:

1. Run a fresh current-snapshot scanner/watchlist pass and verify candidates only surface when the
   exact normalized key matches.
2. Forward-demo log whether `feature_shark_fin_cluster_wait` and
   `feature_confirmation_timing_or_quality` agree with the alert at decision time.
3. Re-run pair-level feature ablation after adding more GBPJPY examples, then require split N >= 3
   in all train/validation/OOS segments for any stricter sub-filter.
4. If demo-forward alerts are enabled, keep risk unchanged and log whether the stored setup key,
   TDI state, session, and H4 level match at alert time.

Reusable inspection commands:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.setup_intelligence expectancy-report --limit 80
.venv\Scripts\python.exe -m helix_v3.backtest.validation_library report --limit 20
```
