# Helix V3 - Codex Project Guide

## Project Overview

Helix V3 is a Python-based Market Maker Method (MMM) trading system for MetaTrader 5. It combines quantitative pre-filtering, multi-timeframe analysis, chart rendering, dual-provider vision review, SQLite journals, WhatsApp notifications, and pair-gated risk controls.

User-facing timestamps should be in EAT (UTC+3). Treat this as a live-trading codebase even when working on tests or backtests.

## Safety Rules

- Do not place, modify, or close live MT5 trades unless the user explicitly asks for live execution.
- Do not start the live orchestrator casually. The live commands are `start_helix.py` and `python -m helix_v3.orchestrator_v2` (V1 orchestrator was retired to `trash/` on 2026-06-12).
- Do not edit `.env` unless the user explicitly asks. Update `.env.example` for configuration documentation.
- Do not print API keys, MT5 passwords, auth tokens, `~/.codex/auth.json`, or full credential-bearing logs.
- Prefer offline backtests, scanner replay, and unit tests before touching execution logic.
- Keep live-trading changes narrow and verify risk behavior before reporting success.

## Model Roles

The project is designed for both Anthropic and OpenAI models.

- Anthropic primary role: visual chart geometry, MMM pattern reading, discretionary chart-structure challenge.
- OpenAI primary role: strict JSON verdicts, schema-normalized labels, arbitration-ready output, embeddings for retrieval.
- Scanner baseline role: quantify whether model verdicts beat the existing rule/scanner signal.

Important auth boundary: Codex ChatGPT login is not the same as `OPENAI_API_KEY`. Python API calls in this repo require `OPENAI_API_KEY` in the environment. ChatGPT Pro/Codex login may allow Codex itself to work, but it does not give project code an API key.

## Key Files

- `CLAUDE.md`: full project architecture and MMM rules.
- `config/settings.py`: environment-backed settings.
- `config/pair_profiles.py`: per-pair risk parameters.
- `helix_v3/core/quant_engine.py`: MT5 rates, EMA vectors, accumulation, stop hunt.
- `helix_v3/core/mtf_analyzer.py`: Weekly/H4/H1/M15 top-down analysis.
- `helix_v3/core/advisory_confidence.py`: convergence-weighted MMM advisory scoring for live scans and replay reports.
- `helix_v3/consensus/validator.py`: local, Anthropic, OpenAI, and dual-provider vision verdicts.
- `helix_v3/ai/model_roles.py`: provider/model role routing.
- `helix_v3/backtest/vision_store.py`: prediction and outcome storage.
- `helix_v3/backtest/scanner_replay.py`: offline scanner baseline and model replay.
- `helix_v3/backtest/mmm_event_replay.py`: MMM event-based replay, setup signatures, pair-normalized reports, and convergence mining.
- `helix_v3/backtest/historical_flashcard_miner.py`: backdated MMM setup miner that creates historical flashcards and event labels.
- `helix_v3/backtest/validation_library.py`: promoted profitable setup signatures for validating new entries.
- `helix_v3/journal/flashcards.py`: market-structure flashcards with M/W type, TDI, pattern, and convergence metadata.
- `helix_v3/execution/gatekeeper.py`: live order construction and trade management.
- `helix_v3/training/taught_rule_validator.py`: validates paraphrased Steve Mauro candidate rule cards against historical OHLC.

## Databases

SQLite files live under `logs/` and should be treated as runtime artifacts:

- `logs/trade_journal.db`: live/demo trade records.
- `logs/market_scanner.db`: scanner snapshots.
- `logs/flashcards.db`: pattern learning snapshots.
- `logs/vision_backtests.db`: offline model predictions and replay outcomes.

Do not delete or reset these databases unless the user explicitly asks.

## Common Commands

Run focused tests:

```powershell
.venv\Scripts\python.exe -m pytest tests\test_vision_backtest_store.py tests\test_scanner_replay.py
```

Run lint on touched backtest files:

```powershell
.venv\Scripts\python.exe -m ruff check helix_v3\backtest tests\test_scanner_replay.py tests\test_vision_backtest_store.py
```

Compile touched modules:

```powershell
.venv\Scripts\python.exe -m compileall helix_v3\backtest helix_v3\consensus helix_v3\ai
```

Show scanner candidates:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.scanner_replay candidates --min-readiness 50 --timeframe M15 --limit 20
```

Seed scanner baseline predictions:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.scanner_replay baseline --min-readiness 50 --timeframe M15 --limit 100 --policy stop_hunt_then_bias
```

Evaluate pending predictions against MT5 history. This is a diagnostic only; do not treat fixed
`30/90/240` horizons as the primary MMM benchmark:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.scanner_replay evaluate --limit 100 --horizons 30,90,240
```

Report model performance:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.scanner_replay report --horizon 90
```

Run OpenAI vision replay after `OPENAI_API_KEY` is configured:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.scanner_replay openai --min-readiness 50 --timeframe M15 --limit 20
```

Run paid-account CLI replay without API keys:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.account_cli_replay --provider codex --min-readiness 50 --timeframe M15 --limit 5
.venv\Scripts\python.exe -m helix_v3.backtest.account_cli_replay --provider claude --min-readiness 50 --timeframe M15 --limit 5
```

Replay flashcards through MMM trade-management events:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.mmm_event_replay enrich-flashcards --min-confluence 30 --limit 500
.venv\Scripts\python.exe -m helix_v3.backtest.mmm_event_replay flashcards --min-confluence 50 --limit 100
```

Report pair-normalized MMM replay performance:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.mmm_event_replay pair-report --min-total 1
.venv\Scripts\python.exe -m helix_v3.backtest.mmm_event_replay setup-report --min-total 2
.venv\Scripts\python.exe -m helix_v3.backtest.mmm_event_replay convergence-report --min-symbols 2 --limit 500
.venv\Scripts\python.exe -m helix_v3.backtest.mmm_event_replay calibration-report --min-total 5
.venv\Scripts\python.exe -m helix_v3.backtest.mmm_event_replay gate-ablation-report --min-total 5
.venv\Scripts\python.exe -m helix_v3.backtest.mmm_event_replay advisory-report --min-total 3
.venv\Scripts\python.exe -m helix_v3.backtest.mmm_event_replay calibration-propose --min-total 5
```

MMM event replay is the preferred backtest frame for flashcard learning. It uses pair profiles,
structural SL from the Asian range, T1 at 1R, breakeven after T1, 90-minute stale exit only when
not in profit, pair-specific trailing, and max-duration exits. Setup signatures should include
explicit `M_TOP`/`W_BOTTOM`, TDI state, pattern trade type, pair-normalized range/hunt buckets,
and cross-pair convergence theme score.

The V2 orchestrator computes an advisory confidence score after TDI/pattern scanning and stores it
on flashcards. This is advisory-only unless a future change explicitly enforces
`PairProfile` advisory gate fields such as `min_confluence_score`, `require_tdi_confirmation`,
or `advisory_min_score`.

`REENTRY_GUARD_BAN_SCOPE=direction` matches `CLAUDE.md`: two losses ban only the same
symbol+direction for the day. Set it to `symbol` only when intentionally choosing stricter
whole-symbol bans.

Mine backdated historical flashcards and build the validation library:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.historical_flashcard_miner mine --days 180 --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC --min-confluence 50 --step-bars 4 --limit-per-symbol 100
.venv\Scripts\python.exe -m helix_v3.backtest.validation_library promote --min-total 5 --min-favorable-rate 55
.venv\Scripts\python.exe -m helix_v3.backtest.historical_flashcard_miner library-report --limit 50
.venv\Scripts\python.exe -m helix_v3.backtest.historical_flashcard_miner validate-current --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC
```

Run the aligned full-universe 5-year mining chunks. This mines all instruments over the same
calendar windows before rebuilding reports:

```powershell
.\scripts\run_aligned_mining_chunks.ps1
```

Run the per-instrument dense research archive. This mines each instrument, saves historical
flashcards, labels direct-profit outcomes, requires scanner-baseline qualification, and writes
`data/mmm_training/pair_research/<PAIR>/` artifacts:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.historical_flashcard_miner pair-study --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC --days 1826 --until 2026-06-08 --step-bars 1 --limit-per-symbol 2000 --min-confluence 50 --min-spacing-minutes 90 --min-total 10 --min-favorable-rate 55 --min-avg-exit-pips 0 --baseline-favorable-rate 85 --baseline-avg-exit-pips 10.9 --split-min-total 3 --required-split-passes 2 --validation-days 365 --out-of-sample-days 180 --max-examples 150
```

Regenerate reports without touching MT5:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.historical_flashcard_miner pair-study --archive-only --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC --days 1826 --until 2026-06-08 --min-total 10 --min-favorable-rate 55 --min-avg-exit-pips 0 --baseline-favorable-rate 85 --baseline-avg-exit-pips 10.9 --split-min-total 3 --required-split-passes 2 --validation-days 365 --out-of-sample-days 180 --max-examples 150
```

Rebuild validation records strictly from replay signatures:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.validation_library rebuild --min-total 10 --min-favorable-rate 85 --min-avg-exit-pips 10.9 --min-symbols 2
```

Build winner-vs-loser chart packets for paid-account ChatGPT/Claude vision review:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_review_packet_builder --symbols GBPJPY,EURJPY --min-total 10 --min-favorable-rate 55 --min-avg-exit-pips 0 --max-setups-per-pair 3 --winners-per-setup 8 --losers-per-setup 8
```

Run stored-field ablations for vision-review filter hypotheses:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_filter_ablation --packet-root data\mmm_training\vision_review_packets
```

Run paid-account Codex/Claude packet reviews without API keys:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_account_review_runner --packet-root data\mmm_training\vision_review_packets --timeout-seconds 1200
```

Backfill OHLC-derived feature columns for packet signatures:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_feature_backfill --packet-root data\mmm_training\vision_review_packets
```

Backfill OHLC-derived feature columns for full GBPJPY/EURJPY research scope:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_feature_backfill --symbols GBPJPY,EURJPY
```

Run pair-level feature ablations across archived research signatures:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.vision_filter_ablation --pair-research --symbols GBPJPY,EURJPY --pair-research-root data\mmm_training\pair_research --pair-output-root data\mmm_training\pair_feature_ablations --min-total 10 --split-min-total 3 --required-split-passes 2
```

Historical mining uses MT5 only for candle history. It slices each timeframe at the historical
snapshot, runs the same Weekly/H4/H1/M15 analyzer, saves `HISTORICAL` flashcards with real
backdated timestamps, records MMM event outcomes, and promotes repeated profitable signatures.

Build the local Steve Mauro MMM training-material index:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.video_mmm_extractor manifest
.venv\Scripts\python.exe -m helix_v3.training.video_mmm_extractor init-md
```

The training extractor reads videos from `data/mmm_training/videos`, writes a local source manifest,
and creates timestamped note/rule/skill scaffolds under `data/mmm_training`. Keep methodology notes
as paraphrased, timestamped, testable rules with visual evidence references. Do not rebuild paid
course videos as full redistributed markdown transcripts. Raw local transcripts, if generated for
analysis, belong in `data/mmm_training/transcripts` and should feed concise rule cards.

Audio/keyframe extraction requires ffmpeg:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.video_mmm_extractor extract-audio
.venv\Scripts\python.exe -m helix_v3.training.video_mmm_extractor extract-frames --every-seconds 30
```

If ffmpeg/ffprobe is not on PATH, pass `--ffmpeg-path` or `--ffprobe-path`. Transcription can run
locally through ffmpeg's Whisper filter after a whisper.cpp ggml model is placed under
`data/mmm_training/models`:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.video_mmm_extractor transcribe --model-path data\mmm_training\models\ggml-base.en.bin
.venv\Scripts\python.exe -m helix_v3.training.video_mmm_extractor transcribe --video-id video_001 --model-path data\mmm_training\models\ggml-base.en.bin
```

For faster GPU transcription without API keys, use Google Colab with
`notebooks/colab_transcribe_mmm.ipynb` and `scripts/colab_transcribe_mmm.py`. The Colab script
uses `faster-whisper`, reads `data/mmm_training/manifest.json`, prefers `audio/video_XXX.wav`
when present, falls back to source videos, and writes JSON-line transcripts under
`data/mmm_training/transcripts`.

Promote extracted
teachings into `data/mmm_training/skills/CODEX_MMM_STRATEGY.md` and
`data/mmm_training/skills/CLAUDE_MMM_STRATEGY.md` only after market replay validates the rule.

Build a transcript pointer index without reproducing full transcripts:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.video_mmm_extractor transcript-index --window-seconds 180 --min-score 12 --top-limit 120
```

Validate taught candidate rules against historical candles:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.taught_rule_validator validate --days 180 --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD --step-bars 4 --limit-per-rule 50 --min-spacing-minutes 90 --replace-scope
```

Export the taught-rule validation report:

```powershell
.venv\Scripts\python.exe -m helix_v3.training.taught_rule_validator export-report --min-total 1 --scanner-baseline "90m scanner baseline: N=100, Fav=85.0%, AvgExit=+10.9p, MFE=+24.0p, MAE=+4.5p"
```

## Verification Expectations

For backtest/vision changes, run at least:

```powershell
.venv\Scripts\python.exe -m pytest tests\test_vision_backtest_store.py tests\test_scanner_replay.py tests\test_mmm_event_replay.py tests\test_flashcards.py tests\test_advisory_confidence.py tests\test_reentry_guard.py tests\test_validation_library.py tests\test_historical_flashcard_miner.py
.venv\Scripts\python.exe -m ruff check helix_v3\backtest\mmm_event_replay.py helix_v3\backtest\historical_flashcard_miner.py helix_v3\backtest\validation_library.py helix_v3\core\advisory_confidence.py tests\test_scanner_replay.py tests\test_vision_backtest_store.py tests\test_mmm_event_replay.py tests\test_flashcards.py tests\test_advisory_confidence.py tests\test_reentry_guard.py tests\test_validation_library.py tests\test_historical_flashcard_miner.py
```

For validator/model-role changes, also run:

```powershell
.venv\Scripts\python.exe -m compileall helix_v3\consensus helix_v3\ai helix_v3\backtest
```

For execution/gatekeeper changes, inspect risk and order behavior carefully and do not run live execution without explicit user approval.
