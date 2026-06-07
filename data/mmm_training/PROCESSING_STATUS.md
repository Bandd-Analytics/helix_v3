# MMM Training Processing Status

Updated: 2026-06-07

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
- Historical study now contains 8,178 historical flashcards, including 2,159 direct-profit examples.
- No setup currently beats the scanner baseline gate of Fav >= 85.0% and AvgExit >= +10.9p
  with two split confirmations.
- Research-only candidates remain on GBPJPY BUY W-bottom early-week L3 variants and one
  EURJPY BUY W-bottom early-week L3 true-trend variant.
- Validation library was rebuilt with the strict baseline gate and currently has 0 promoted records.
- Winner-vs-loser vision review packets generated under `vision_review_packets/` for the
  GBPJPY and EURJPY research-only candidates.

## Next Commands

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

## Methodology Rule Boundary

Raw transcripts are local analysis inputs. The reusable Claude/Codex skill files should contain
timestamped, paraphrased, testable trading rules only. A rule is not promoted into the strategy
skill layer until historical replay shows it correlates with market behavior.
