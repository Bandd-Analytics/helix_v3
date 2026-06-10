# MMM Training Processing Status

Updated: 2026-06-09

## Current Assets

| Video ID | Lesson | Duration | Audio | Keyframes | Transcript |
|---|---|---:|---|---:|---|
| `video_001` | MMM 8-2-2011 Day 1 | 03:51:15 | `audio/video_001.wav` | 463 | complete |
| `video_002` | MMM 8-3-2011 Day 2 | 04:11:21 | `audio/video_002.wav` | 503 | complete |
| `video_003` | MMM 8-4-2011 Day 3 | 04:02:27 | `audio/video_003.wav` | 485 | complete |
| `video_004` | MMM 8-4-2011 Day 4 | 03:58:04 | `audio/video_004.wav` | 476 | complete |

## Completed

- Local source manifest created at `manifest.json`.
- Source index created at `source_index.md`.
- Per-video methodology note templates created under `notes/`.
- Rule-card and methodology templates created under `rules/`.
- Claude/Codex strategy-skill drafts created under `skills/`.
- Market-reality validation plan created under `validation/`.
- ffmpeg 8.1.1 installed via WinGet.
- Audio extracted to 16 kHz mono WAV.
- Keyframes extracted every 30 seconds.
- Whisper.cpp base English model downloaded to `models/ggml-base.en.bin`.
- One-minute transcription sample generated at `transcripts/video_001_sample.json`.
- Colab GPU transcription script created at `scripts/colab_transcribe_mmm.py`.
- Colab launcher notebook created at `notebooks/colab_transcribe_mmm.ipynb`.
- All four JSON transcripts are present locally under `transcripts/`.
- Transcript methodology pointer index created at `transcript_index.md`.
- First-pass candidate rule cards created at `rules/candidate_rule_cards.md`.
- First-pass taught-rule validator created at `helix_v3/training/taught_rule_validator.py`.
- Historical taught-rule replay recorded to `logs/taught_rule_validation.db`.
- Validation report exported to `validation/taught_rule_validation_report.md`.
- Claude/Codex strategy-skill drafts updated with watchlist-only validation state.
- Three-year pair-specific historical study completed for EURUSD, GBPUSD, GBPJPY, USDJPY,
  EURJPY, GBPCHF, and AUDUSD.
- Pair research archive exported to `pair_research/` with setup-performance JSON and
  direct-profit flashcard manifests per pair.
- Dense three-year M15 pair replay completed with `step-bars=1`, pair-specific profiles,
  `min-total=10`, scanner-baseline qualification, and train/validation/out-of-sample splits.
- Expanded historical study now contains 19,373 historical flashcards and 19,853 MMM event
  replay outcomes after broadening the search toward a five-year window.
- Strict validation-library rebuild after expanded mining produced one promoted GBPJPY BUY setup
  record with N=10, Fav=90.0%, AvgExit=+18.4p. Treat this as supervised demo/watchdog material,
  not live auto-entry approval.
- Research-only candidates remain on GBPJPY BUY W-bottom early-week L3 variants and one
  EURJPY BUY W-bottom early-week L3 true-trend variant.
- Validation library was rebuilt with the strict baseline gate and currently has 1 promoted record.
- Winner-vs-loser vision review packets generated under `vision_review_packets/` for the
  GBPJPY and EURJPY research-only candidates.
- All four GBPJPY/EURJPY vision review packets reviewed through Codex/ChatGPT Pro and
  Claude Max account CLIs without API keys.
- Account model review index saved at `vision_review_packets/MODEL_REVIEW_INDEX.md`; blind
  classification remains research-only and is not strong enough for promotion by itself.
- OHLC-derived vision feature columns added to flashcards and backfilled for 50 packet-signature
  flashcards, then broadened to 2,019 GBPJPY/EURJPY historical flashcards.
- Feature-aware ablations regenerated under `vision_review_packets/`; no packet setup is promoted.
- Pair-level feature ablations generated under `pair_feature_ablations/` for EURUSD, GBPUSD,
  GBPJPY, USDJPY, EURJPY, GBPCHF, and AUDUSD with `min-total=10`.
- GBPJPY produced one research-only raw baseline pass after filtering to 5 kept cases, but split
  testing failed: train N=2, validation N=2, out-of-sample N=1, so it has 0 valid split passes.
- Setup-intelligence database and report created from historical flashcards plus MMM event
  outcomes at `logs/setup_intelligence.db` and `setup_intelligence/REPORT.md`.
- Scanner-first alert-only watchlist CLI added at `helix_v3.scanner.watchlist`. It defaults to
  the seven research pairs, reads setup-intelligence context when available, requires an exact
  promoted validation setup for entry-eligible status, and otherwise reports watch-only or blocked
  scanner candidates without touching live MT5 execution.
- Current setup validation run on 2026-06-08 19:32 EAT across EURUSD, GBPUSD, GBPJPY, USDJPY,
  EURJPY, GBPCHF, and AUDUSD found 0 exact validation-library matches. No live orders were sent.
- Research mining scope expanded to EURUSD, GBPUSD, GBPJPY, USDJPY, EURJPY, GBPCHF, AUDUSD,
  GBPAUD, GBPNZD, EURGBP, XAUUSD, US30, and USTEC. The aligned five-year mining plan is documented
  at `docs/aligned_data_mining_plan.md` and uses 21 shared calendar chunks from 2021-06-08 through
  2026-06-08.
- MT5 symbol availability check passed for all 13 requested instruments. US30 and USTEC were
  selectable but initially not visible in Market Watch; they remain analysis-only pending replay
  calibration.
- Full aligned raw mining completed across 21 shared calendar chunks. Confirmed chunk saves:
  36,054 historical flashcards. Full-period archive rebuild wrote 40 files. Setup intelligence
  now contains 54,075 occurrences, 13,441 setup stats, 127 price-level stats, 438 day/session
  stats, and 2,345 cross-pair stats. Strict validation-library rebuild still has 1 promoted
  record.
- RRS performance grading added to setup intelligence. `R_RUNNER` means Fav >= 75%,
  `R_REPEATER` means Fav >= 50% and < 75%, and `S_STRANGER` means Fav < 50%.
  For setup rows with N >= 10, the current report shows 3 R_RUNNER rows, 90 R_REPEATER rows,
  and 1,181 S_STRANGER rows. Positive-expectancy exceptions below the old 85% scanner gate are
  now visible in `setup_intelligence/REPORT.md`; these are research candidates, not live approval.
- Baseline distinction documented at `docs/rrs_performance_grading.md`: the old two-year
  trading-pipeline result and the strict scanner/promotion gate measure different things. Future
  promotion should use expectancy, payoff, drawdown/adverse-excursion behavior, split stability,
  and RRS band instead of favorable rate alone.
- Expectancy-led research candidate layer added to setup intelligence. The latest rebuild produced
  380 research-only candidates: 83 demo candidates across R_RUNNER/R_REPEATER, 69 S_STRANGER
  asymmetric exceptions, and 228 watch candidates. These are stored in
  `logs/setup_intelligence.db` table `expectancy_candidates`; they are not inserted into
  `validation_setups` and are not live-entry approval.
- Scanner watchlist context now surfaces expectancy tier, RRS, profit factor, payoff ratio, and
  split pass count for historical matches. A 2026-06-09 13:03 EAT alert-only run showed 0 promoted
  entries and preserved strict blocking while displaying expectancy memory for GBPNZD, GBPCHF, and
  GBPAUD candidates.
- Instrument calibration audit completed for XAUUSD, US30, and USTEC. XAUUSD resolved to
  `pip_size=0.01` and `pip_value_per_lot=1.00`; US30/USTEC also resolved to `pip_size=0.01` but
  remain broker-contract/risk blocked. All three stay research-only and execution-blocked.
- XAUUSD winner-vs-loser vision packets generated for five high-expectancy research setups with
  `--include-non-w-bottom`. A targeted chart backfill rendered and attached 61 historical chart
  images, and all five XAUUSD packet manifests now have 0 missing images.
- XAUUSD account-CLI packet reviews completed for all five packets using Codex/ChatGPT Pro and
  Claude Max. Blind scores ranged from Codex `46.7%` to `76.9%` and Claude `36.4%` to `72.7%`;
  the strongest single-model results were Codex `10/13` on the RRT sell mid-week packet and Claude
  `8/11` on both THE_33 M/W buy stop-hunt packets. Treat these as filter-hypothesis evidence only,
  not promotion or live-entry approval.
- OHLC feature backfill completed for 7,788 XAUUSD historical flashcards. Packet and pair-level
  feature ablations were regenerated. Best XAUUSD pair-level variant is
  `ratio_le_2_asian_gte_30_tdi_positive` on the RRT BUY mid-week L3 accumulation setup: kept `5`,
  Fav `100.0%`, AvgExit `+770.4p`, but only `1` split pass, so decision remains
  `research_only_split_fail`.
- RRS-aware ablation reporting added. Packet and pair-level feature ablation reports now expose
  base/filtered RRS, profit factor, payoff ratio, scanner-baseline split passes, and
  expectancy-split passes. Regenerated all packet ablations and all 13 pair-feature ablation
  reports.
- Alert-only demo basket report generated at `setup_intelligence/ALERT_ONLY_BASKET.md`. The top
  ranked observation row is the strict GBPJPY BUY `DEMO_ALERT` candidate with `R_RUNNER`, `N=10`,
  Fav `90.0%`, AvgExit `+18.4p`, PF `69.22`, and `3/3` splits. XAUUSD and other analysis-only
  profiles are explicitly marked `RESEARCH_ONLY`.
- Scanner watchlist can now require a ranked alert-basket match via `--require-alert-basket`.
  A 2026-06-09 19:33 EAT alert-only run across all 13 instruments showed 0 promoted entries,
  0 watch-only entries, and 10 blocked candidates. Basket context was attached to GBPNZD
  `#2 RESEARCH_ONLY` and GBPAUD `#13 DEMO_ALERT`, but both stayed blocked by readiness/age and
  missing strict validation.

## Next Commands

Run the alert-only scanner watchlist from stored scanner snapshots:

```powershell
.venv\Scripts\python.exe -m helix_v3.scanner.watchlist --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD --include-blocked
```

Rebuild the derived setup-intelligence DB/report from saved historical replay data:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.setup_intelligence rebuild
```

Review RRS performance grading and lower-rate positive-expectancy exceptions:

```powershell
Get-Content docs\rrs_performance_grading.md
Get-Content data\mmm_training\setup_intelligence\REPORT.md
```

Review the RRS-ranked alert-only basket:

```powershell
Get-Content data\mmm_training\setup_intelligence\ALERT_ONLY_BASKET.md
```

Review the XAUUSD visual packets:

```powershell
Get-ChildItem data\mmm_training\vision_review_packets -Directory -Filter XAUUSD*
.venv\Scripts\python.exe -m helix_v3.training.vision_account_review_runner --packet-root data\mmm_training\vision_review_packets --timeout-seconds 1200
```

Print the expectancy-led research candidate layer:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.setup_intelligence expectancy-report --limit 50
```

Run the alert-only scanner watchlist with expectancy context:

```powershell
.venv\Scripts\python.exe -m helix_v3.scanner.watchlist --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC --include-blocked --limit 20
```

Run the alert-only scanner watchlist with ranked basket gating:

```powershell
.venv\Scripts\python.exe -m helix_v3.scanner.watchlist --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC --require-alert-basket --alert-basket-limit 30 --include-blocked --limit 20
```

Run the aligned full-universe five-year mining chunks:

```powershell
.\scripts\run_aligned_mining_chunks.ps1
```

Regenerate the taught-rule validation report from the saved database:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.taught_rule_validator export-report --min-total 1 --scanner-baseline "90m scanner baseline: N=100, Fav=85.0%, AvgExit=+10.9p, MFE=+24.0p, MAE=+4.5p"
```

Run a focused refinement replay after tightening a detector:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.taught_rule_validator validate --days 180 --symbols GBPJPY,AUDUSD,USDJPY,EURJPY --rule-id MMM-TRAIN-004 --step-bars 2 --limit-per-rule 100 --min-spacing-minutes 90 --replace-scope
```

Compare against the scanner baseline before promotion:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.scanner_replay report --horizon 90
```

Regenerate the full three-year pair research archive from existing databases:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.historical_flashcard_miner pair-study --archive-only --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD --days 1095 --min-total 10 --min-favorable-rate 55 --min-avg-exit-pips 0 --baseline-favorable-rate 85 --baseline-avg-exit-pips 10.9 --split-min-total 3 --required-split-passes 2 --validation-days 365 --out-of-sample-days 180 --max-examples 150
```

Rebuild the validation library strictly from replay signatures:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.validation_library rebuild --min-total 10 --min-favorable-rate 85 --min-avg-exit-pips 10.9 --min-symbols 2
```

Regenerate winner-vs-loser vision review packets:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_review_packet_builder --symbols GBPJPY,EURJPY --min-total 10 --min-favorable-rate 55 --min-avg-exit-pips 0 --max-setups-per-pair 3 --winners-per-setup 8 --losers-per-setup 8
```

Run stored-field ablations for generated vision-review packets:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_filter_ablation --packet-root data\mmm_training\vision_review_packets
```

Run paid-account Codex/Claude packet reviews without API keys:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_account_review_runner --packet-root data\mmm_training\vision_review_packets --timeout-seconds 1200
```

Backfill OHLC-derived vision features for packet signatures:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_feature_backfill --packet-root data\mmm_training\vision_review_packets
```

Backfill OHLC-derived vision features for the full research scope:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_feature_backfill --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD
```

Run pair-level feature ablations across all research pairs:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_filter_ablation --pair-research --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD --pair-research-root data\mmm_training\pair_research --pair-output-root data\mmm_training\pair_feature_ablations --min-total 10 --split-min-total 3 --required-split-passes 2
```

## Methodology Rule Boundary

Raw transcripts are local analysis inputs. The reusable Claude/Codex skill files should contain
timestamped, paraphrased, testable trading rules only. A rule is not promoted into the strategy
skill layer until historical replay shows it correlates with market behavior.
