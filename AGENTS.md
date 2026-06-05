# Helix V3 - Codex Project Guide

## Project Overview

Helix V3 is a Python-based Market Maker Method (MMM) trading system for MetaTrader 5. It combines quantitative pre-filtering, multi-timeframe analysis, chart rendering, dual-provider vision review, SQLite journals, WhatsApp notifications, and pair-gated risk controls.

User-facing timestamps should be in EAT (UTC+3). Treat this as a live-trading codebase even when working on tests or backtests.

## Safety Rules

- Do not place, modify, or close live MT5 trades unless the user explicitly asks for live execution.
- Do not start the live orchestrator casually. The live commands are `start_helix.py`, `python -m helix_v3.orchestrator`, and `python -m helix_v3.orchestrator_v2`.
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
- `helix_v3/consensus/validator.py`: local, Anthropic, OpenAI, and dual-provider vision verdicts.
- `helix_v3/ai/model_roles.py`: provider/model role routing.
- `helix_v3/backtest/vision_store.py`: prediction and outcome storage.
- `helix_v3/backtest/scanner_replay.py`: offline scanner baseline and model replay.
- `helix_v3/journal/flashcards.py`: market-structure flashcards.
- `helix_v3/execution/gatekeeper.py`: live order construction and trade management.

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

Evaluate pending predictions against MT5 history:

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

## Verification Expectations

For backtest/vision changes, run at least:

```powershell
.venv\Scripts\python.exe -m pytest tests\test_vision_backtest_store.py tests\test_scanner_replay.py
.venv\Scripts\python.exe -m ruff check helix_v3\backtest tests\test_scanner_replay.py tests\test_vision_backtest_store.py
```

For validator/model-role changes, also run:

```powershell
.venv\Scripts\python.exe -m compileall helix_v3\consensus helix_v3\ai helix_v3\backtest
```

For execution/gatekeeper changes, inspect risk and order behavior carefully and do not run live execution without explicit user approval.
