# MMM Vision Review Status

Updated: 2026-06-08

## Generated Packets

- Packet index: `data/mmm_training/vision_review_packets/INDEX.md`
- Account model review index: `data/mmm_training/vision_review_packets/MODEL_REVIEW_INDEX.md`
- Filter ablation index: `data/mmm_training/vision_review_packets/FILTER_ABLATION_INDEX.md`
- Pair feature ablation index: `data/mmm_training/pair_feature_ablations/INDEX.md`
- Packets generated: 4
- Scope: GBPJPY and EURJPY research-only W-bottom candidates.
- OHLC feature backfill completed for 50 packet flashcards and then broadened to 2,019
  GBPJPY/EURJPY historical flashcards.

## Reviewed With Account CLIs

Reviewed packets:

- `EURJPY_the_33_mw_buy_early_week_l3_true_trend_a6c634d982`
- `GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_6dad50cc33`
- `GBPJPY_the_33_mw_buy_early_week_l3_true_trend_31ac49b8f6`
- `GBPJPY_the_33_mw_buy_early_week_l3_true_trend_7d853c76a8`

Each packet has:

- `reviews/codex_blind.md`
- `reviews/claude_blind.md`
- `reviews/codex_labeled_comparison.md`
- `reviews/claude_labeled_comparison.md`
- `reviews/model_comparison_summary.md`
- `reviews/filter_ablation.md`

Blind accuracy:

| Pair | Packet | Codex / ChatGPT Pro | Claude Max |
|---|---|---:|---:|
| EURJPY | `EURJPY_the_33_mw_buy_early_week_l3_true_trend_a6c634d982` | 5/12 (41.7%) | 5/12 (41.7%) |
| GBPJPY | `GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_6dad50cc33` | 4/11 (36.4%) | 4/11 (36.4%) |
| GBPJPY | `GBPJPY_the_33_mw_buy_early_week_l3_true_trend_31ac49b8f6` | 7/13 (53.8%) | 6/13 (46.2%) |
| GBPJPY | `GBPJPY_the_33_mw_buy_early_week_l3_true_trend_7d853c76a8` | 7/10 (70.0%) | 5/10 (50.0%) |

Interpretation: account vision models are not reliable enough yet as direct blind classifiers.
The useful output is the labeled comparison layer, which produced deterministic filters to encode
and backtest. No reviewed setup is promoted.

## Stored-Field Filter Hypotheses

Current ablation results from fields already stored on flashcards:

| Pair | Packet | Best Variant | Kept | Fav% | AvgExit |
|---|---|---|---:|---:|---:|
| EURJPY | `EURJPY_the_33_mw_buy_early_week_l3_true_trend_a6c634d982` | `tdi_rsi_gte_50` | 9 | 66.7% | +17.2 |
| GBPJPY | `GBPJPY_the_33_mw_buy_early_week_l3_stop_hunt_6dad50cc33` | `ratio_le_2_asian_gte_30_tdi_positive` | 7 | 100.0% | +8.2 |
| GBPJPY | `GBPJPY_the_33_mw_buy_early_week_l3_true_trend_31ac49b8f6` | `feature_extreme_hunt_with_exception` | 11 | 81.8% | +13.2 |
| GBPJPY | `GBPJPY_the_33_mw_buy_early_week_l3_true_trend_7d853c76a8` | `tdi_rsi_gt_signal` | 5 | 100.0% | +30.6 |

These are small-sample hypotheses only. The high GBPJPY rows have 5 to 11 kept cases and do not
meet promotion standards.

## Pair-Level Feature Ablation

Broad scope: all archived GBPJPY and EURJPY pair-research signatures with `min-total=10`.

| Pair | Setups | Best Setup | Best Variant | Kept | Fav% | AvgExit | Status |
|---|---:|---|---|---:|---:|---:|---|
| GBPJPY | 6 | `TRUE_TREND ... NO_RRT ... TDI_NONE ... CONF_50_74` | `tdi_rsi_gt_signal` | 5 | 100.0% | +30.6 | research-only split fail |
| EURJPY | 7 | `STOP_HUNT ... NO_RRT ... TDI_NONE ... CONF_75_PLUS` | `asian_range_gte_30` | 8 | 75.0% | +11.3 | fail |

The GBPJPY row clears the raw scanner baseline gate only after filtering to 5 kept cases.
Split test result: train N=2, validation N=2, out-of-sample N=1. Because each split is below
the required split minimum sample of 3, it has 0 valid split passes and is not promoted.

## Reusable Commands

Run account model reviews without API keys:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_account_review_runner --packet-root data\mmm_training\vision_review_packets --timeout-seconds 1200
```

Run stored-field ablations:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_filter_ablation --packet-root data\mmm_training\vision_review_packets
```

Backfill OHLC-derived feature columns for packet signatures:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_feature_backfill --packet-root data\mmm_training\vision_review_packets
```

Backfill OHLC-derived feature columns for full GBPJPY/EURJPY research scope:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_feature_backfill --symbols GBPJPY,EURJPY
```

Run pair-level feature ablations:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_filter_ablation --pair-research --symbols GBPJPY,EURJPY --pair-research-root data\mmm_training\pair_research --pair-output-root data\mmm_training\pair_feature_ablations --min-total 10 --split-min-total 3 --required-split-passes 2
```

## Next Required Work

- Do not promote the current GBPJPY `tdi_rsi_gt_signal` hypothesis; it is too sparse by split.
- Expand the same OHLC-feature backfill and pair-level ablation to the remaining pairs:
  EURUSD, GBPUSD, USDJPY, GBPCHF, and AUDUSD.
- Only convert split-stable rules into strict validation-library candidates, not live rules.
- Promote nothing until the refined filter beats the scanner baseline with train/validation/out-of-sample confirmation.
