# Helix V3 - MMM Algorithmic Execution System

## Project Overview
Enterprise-grade Market Maker Method (MMM) algorithmic execution system trading on MetaTrader 5 via Python. Based on Steve Mauro's MMM methodology with quantitative pre-filtering, advisory confidence scoring, dual-LLM vision consensus, pair-gated risk management, validation library feedback loop, and automated notifications (WhatsApp/Telegram).

**Account**: ICMarketsKE-Demo (52846409)
**Timezone**: All user-facing timestamps in EAT (UTC+3, Kenyan time)
**Risk Target**: Sharpe Ratio > 1.5, Max Drawdown < 8%

## Architecture — Unified Pipeline

```
                    Weekly (D1/H4)
                         |
                    4-Hour (H4)        <- MTF Top-Down Analysis
                         |                (mtf_analyzer.py)
                    1-Hour (H1)
                         |
                    15-Min (M15)
                         |
              +----------+----------+
              |                     |
     Quant Pre-Filter        Chart Export
     (quant_engine.py)    (chart_exporter.py)
              |                     |
              +----------+----------+
                         |
                  Advisory Confidence    <- Grades A/B/C/D/AVOID
                  (advisory_confidence)     Blocks D and AVOID
                         |
                  Validation Library     <- Checks proven patterns
                  (validation_library)      Blocks <30% win rate
                         |
                  Vision Consensus       <- local / anthropic / dual-api
                  (validator.py)
                         |
                  Pair-Gated Risk        <- pair_profiles.py
                  (gatekeeper.py)           SL floor + account cap
                         |
              +----------+----------+
              |          |          |
         MT5 Execute  Journal   Notifications
                    (trade_journal) (WhatsApp/Telegram)
                         |
              +----------+----------+
              |                     |
         Flashcards          Replay Store
         (flashcards.py)     (mmm_event_replay)
                                    |
                             Validation Library  <- Auto-promote proven
                             (promote at EOD)       patterns for reuse
```

## File Map

### Core Trading Logic
| File | Purpose |
|------|---------|
| `helix_v3/core/types.py` | Shared dataclasses: Direction, CycleLevel, QuantSignal, ConsensusResult, ExecutionOrder |
| `helix_v3/core/quant_engine.py` | MT5 data fetch, EMA vectors, Asian accumulation, stop-hunt detection |
| `helix_v3/core/mtf_analyzer.py` | Multi-timeframe analysis: Weekly->4H->1H->15M with confluence scoring. M/W pattern drives direction. |
| `helix_v3/core/tdi.py` | TDI (V2-verified RSI=21), pivots (R3/S3/M1-M4 + day-type), ADR (Wilder ATR), NewHUD dashboard, crossover arrows, daily HiLo |
| `helix_v3/core/patterns.py` | Context-aware candlestick patterns: spike, hammer, doji, RRT, evening/morning star, high/low test, M/W, half batman. Trade type classification. |
| `helix_v3/core/sessions.py` | MMM session classification (Asia/London/NYC per Book p.8), per-day Asian range, session boundaries, weekly open range |
| `helix_v3/core/reentry_guard.py` | SQLite-backed re-entry guard: loss tracking, cooldowns, day bans, 2hr entry cooldown after ANY exit, exposure check. Survives restarts. |
| `helix_v3/core/advisory_confidence.py` | Setup confidence scoring: grades entries A/B/C/D/AVOID using M/W, TDI, convergence, push count, pair-normalized ranges. Cross-pair theme matching. |

### Visualization
| File | Purpose |
|------|---------|
| `helix_v3/visualization/chart_exporter.py` | 1024x1024 clean charts for vision model consumption |
| `helix_v3/visualization/annotated_chart.py` | Charts with confluence markings (Asian box, HOD/LOD, entry/SL/TP, TDI panel, worktime ribbon, pattern markers, HUD overlay) |

### Consensus
| File | Purpose |
|------|---------|
| `helix_v3/consensus/validator.py` | Multi-mode vision verification. `local`: single Anthropic API call (cheapest). `anthropic`: two Claude queries (self-consensus). `dual-api`: Claude+GPT. Stale verdict guard rejects files >30min old. |

### Execution
| File | Purpose |
|------|---------|
| `helix_v3/execution/gatekeeper.py` | Pair-gated order execution with 3-layer lot sizing safety (SL floor, account-proportional cap, post-calc risk verification). T1 partial close, trailing SL, stale/time/session exits. |

### Journal & Learning
| File | Purpose |
|------|---------|
| `helix_v3/journal/trade_journal.py` | 75-field trade logging, period reports (session/EOD/weekly/monthly), performance analytics |
| `helix_v3/journal/flashcards.py` | Market structure snapshots with full MTF context, pattern-outcome learning database |

### Scanner
| File | Purpose |
|------|---------|
| `helix_v3/scanner/market_scanner.py` | 15-min recurring market condition evaluator, readiness scoring (0-100) |

### Notifications
| File | Purpose |
|------|---------|
| `helix_v3/notifications/whatsapp.py` | Twilio WhatsApp alerts: setups, entries, exits, T1 hits, period reports, flashcard charts |
| `helix_v3/notifications/telegram.py` | Telegram Bot API notifications: drop-in replacement for WhatsApp, free, no message limits |
| `helix_v3/notifications/auto_scan.py` | Scheduled market scan runner (08:00, 10:00, 15:00, 00:00 EAT) with notifications |

### AI & Model Routing
| File | Purpose |
|------|---------|
| `helix_v3/ai/model_roles.py` | Model role routing for dual-provider vision stack (Anthropic pattern reader + OpenAI JSON arbitrator) |

### Backtesting & Validation (Unified Pipeline)
| File | Purpose |
|------|---------|
| `helix_v3/backtest/data_store.py` | Pre-fetches D1/H4/H1/M15 from MT5 for offline replay. Caches all TFs in memory. |
| `helix_v3/backtest/engine.py` | **Event-driven backtester**: BacktestEngine (subclasses quant engine for historical data), TradeSimulator (bar-by-bar SL/TP/T1/trail), BacktestRunner (full V2 pipeline with advisory scoring + replay recording). CLI interface. |
| `helix_v3/backtest/report.py` | Backtest metrics: win rate, Sharpe, profit factor, max drawdown, per-pair breakdown, advisory grade breakdown, monthly P&L, equity curve |
| `helix_v3/backtest/mmm_event_replay.py` | MMM event-driven replay: normalized setup signatures, gate ablation, calibration recommendations, convergence analysis. Records outcomes from both backtest and live trading. |
| `helix_v3/backtest/validation_library.py` | SQLite library of historically proven setup signatures. Auto-promoted from replay outcomes (>=5 samples, >=55% favorable). Queried during live entry decisions. |
| `helix_v3/backtest/historical_flashcard_miner.py` | Mines historical bars for MMM setups, saves annotated flashcards, labels outcomes via replay |
| `helix_v3/backtest/vision_store.py` | Vision model prediction persistence and path labeling for offline calibration |
| `helix_v3/backtest/scanner_replay.py` | Replay scanner candidates with baseline/vision predictions |
| `helix_v3/backtest/account_cli_replay.py` | Claude Code / Codex CLI-based vision replay (no API keys needed) |

### Training & Methodology
| File | Purpose |
|------|---------|
| `helix_v3/training/video_mmm_extractor.py` | Extracts methodology from Steve Mauro MMM training videos: audio, keyframes, notes, rules, skills |
| `helix_v3/training/rule_validator.py` | Validates 8 core MMM rules against historical MT5 data with hit rates and statistical thresholds |
| `docs/mmm_methodology/` | 16-topic canonical MMM documentation (theory, cycles, sessions, patterns, TDI, pivots, EMAs, trade management, risk) |
| `data/mmm_training/` | Training data inventory: video files, transcripts, notes, rules, validation results |

### Configuration
| File | Purpose |
|------|---------|
| `config/settings.py` | Global settings loaded from .env |
| `config/pair_profiles.py` | Per-pair risk tiers, trade management rules, stop hunt ranges, SL floor, advisory calibration fields |
| `.env` | API keys, MT5 credentials, risk parameters, Twilio/Telegram config, consensus mode |

### Orchestrator
| File | Purpose |
|------|---------|
| `helix_v3/orchestrator_v2.py` | **V2 PRIMARY** — Unified pipeline: MTF analysis -> advisory scoring -> validation library lookup -> vision consensus -> gatekeeper -> execute -> record to replay store -> auto-promote at EOD |
| `tools/trash.py` / `tools/trash_review.py` | Temporary recycle bin: `put`/`list`/`restore`, reviewer classifies (referenced/junk/unsure) and permanently deletes junk after 2h grace. V1 orchestrator lives here now. |
| `docs/AUDIT_FIX_PLAN.md` | Tiered remediation roadmap from the 2026-06-12 quantitative audit (Tier 0 = live-loss bugs, no live sessions until complete) |

### Tests & Tools
| File | Purpose |
|------|---------|
| `tests/full_market_scan.py` | Full 13-pair scan with all indicators, generates charts + notifications |
| `tests/fresh_scan.py` | Quick scan with narrative output for manual review |
| `tests/compare_orchestrators.py` | V1 vs V2 side-by-side evaluation |
| `tools/manual/live_test.py` | Manual integration test (dry-run, no trades) — connects to live MT5, run by hand only, never via pytest |
| `tests/test_reentry_guard.py` | Tests ban scope and cooldown logic |
| `tests/test_advisory_confidence.py` | Tests scoring, TDI states, convergence, hard blockers |
| `tests/test_mmm_event_replay.py` | Tests event path labeling |
| `tests/test_validation_library.py` | Tests signature promotion |
| `tests/send_flashcards.py` | Manual Telegram flashcard test |

### Updates
| File | Purpose |
|------|---------|
| `updates/CHANGELOG.md` | Version history with all changes and evaluation results |

## MMM Trading Rules (from Steve Mauro methodology)

### Multi-Timeframe Analysis Sequence
1. **Weekly (D1/H4)**: Where in the 3-day/weekly cycle? Peak high/low? Mid-week reversal due?
2. **4-Hour (H4)**: Level count (L1/L2/L3). Peak formation? Choppy (L3)?
3. **1-Hour (H1)**: Session phase. HOD/LOD locked? EMA 50/200 cross?
4. **15-Min (M15)**: Asian range < 50 pips? Stop hunt 25-50p with 3 pushes? M/W? RRT?

### Entry Requirements (V2 — unified pipeline)
- Asian range < pair-specific max (accumulation valid)
- M/W formation detected: **W-bottom = BUY, M-top = SELL** (PRIMARY direction signal)
- Stop hunt confirmed (even 1-5 pip breach if M/W confirms — "soft hunt")
- M/W pattern OVERRIDES stop hunt breach side (the breach is the fake move, M/W is the real signal)
- Confluence score >= 50/100 from MTF alignment
- Advisory confidence grade >= C (D and AVOID are blocked)
- Validation library check: block if matching pattern has <30% win rate (n>=5)
- TDI confirmation (Shark Fin, Blood in the Water, VB Squeeze)
- Vision consensus (local=1 API call, anthropic=2 calls, dual-api=Claude+GPT)
- Re-entry guard: no re-entry same pair/direction after loss (persistent SQLite)
- Entry cooldown: 2 hours after ANY trade exit on same symbol (prevents same-setup churn)
- Exposure check: no new entry if pair already has open position

### Lot Sizing (3-layer safety)
1. **SL floor**: If structural SL < `min_sl_pips`, uses floor for sizing (prevents lot inflation from tight stops)
2. **Account-proportional cap**: Max lot where full SL hit can't exceed 3% of equity
3. **Post-calc verification**: Final check rejects if actual risk still exceeds limit

### Trade Management
- **Universal**: 90 min max if NOT in profit -> close (stale exit)
- **If in profit**: Trail SL, never exit early
- **T1**: 50% close at 1:1 RR, SL to breakeven
- **Trailing SL**: Activates at pair-specific threshold, trails at pair distance
- **Max duration**: Pair-specific hard cap (3-5 hours)
- **Session exit**: Close before Asian session if not profitable

## Pair Risk Profiles

| Pair | Tier | Risk% | Hunt Range | Level Move | Trail | SL Buffer | Min SL |
|------|------|-------|-----------|-----------|-------|-----------|--------|
| EURUSD | Low | 1.0% | 20-40p | 70p | 15/12p | 3p | 15p |
| GBPUSD | Low | 1.0% | 25-50p | 80p | 20/15p | 3p | 20p |
| AUDUSD | Low | 1.0% | 15-35p | 55p | 12/10p | 3p | 12p |
| GBPAUD | Medium | 0.8% | 30-60p | 100p | 30/22p | 5p | 25p |
| GBPJPY | Medium | 0.8% | 30-60p | 100p | 25/18p | 5p | 25p |
| GBPNZD | Medium | 0.8% | 30-65p | 110p | 35/25p | 5p | 25p |
| XAUUSD | High | 0.5% | 200-500p | 800p | 100/80p | 30p | 150p |

## Databases
- `logs/trade_journal.db` — Trade history (75 fields per trade)
- `logs/market_scanner.db` — 15-min market condition snapshots
- `logs/flashcards.db` — Market structure pattern learning (entry/scan/missed with full MTF context)
- `logs/reentry_guard.db` — Persistent re-entry guard: loss events, day bans, cooldowns (survives restarts)
- `logs/vision_backtests.db` — Vision model predictions for offline calibration
- `logs/mmm_event_replay.db` — Setup signatures and event outcomes (feeds validation library)
- `logs/validation_library.db` — Historically proven setup patterns with win rates

## Report Schedule (all times EAT)
- **Session reports**: Auto-sent when session transitions (Asian->London->NY)
- **EOD**: 00:00 EAT daily (also auto-promotes proven patterns to validation library)
- **Weekly**: Saturday 00:00 EAT (best/worst pair only)
- **Monthly**: 1st of month 00:00 EAT (best/worst pair only)

## Consensus Modes
- `local`: Single Anthropic API call if key available (cheapest real analysis). Falls back to verdict files if no key. Stale files >30min rejected.
- `anthropic`: Two Claude API calls with different prompts (self-consensus)
- `dual-api`: Claude + GPT-5.5 in parallel (requires both API keys)

Set via `CONSENSUS_MODE` in `.env`.

## Running
```bash
# Live trading
.venv/Scripts/python.exe -m helix_v3.orchestrator_v2       # V2 unified pipeline (PRIMARY)

# Market scanning
.venv/Scripts/python.exe tests/fresh_scan.py                # Quick scan with narrative
.venv/Scripts/python.exe tests/full_market_scan.py          # Full scan + notifications
.venv/Scripts/python.exe -m helix_v3.notifications.auto_scan # Scheduled scans (loop mode)

# Backtesting
.venv/Scripts/python.exe -m helix_v3.backtest.engine --days 14                    # All pairs, 14 days
.venv/Scripts/python.exe -m helix_v3.backtest.engine --pairs GBPJPY,EURUSD -v     # Specific pairs, verbose
.venv/Scripts/python.exe -m helix_v3.backtest.engine --start 2026-05-01 --end 2026-06-01  # Date range

# Training & validation
.venv/Scripts/python.exe -m helix_v3.training.rule_validator                      # Validate MMM rules vs history
```

Note: the V1 legacy orchestrator was moved to `trash/` on 2026-06-12 (restorable via `python tools/trash.py restore 0001`). `start_helix.py` and the `helix` console script now launch V2.

## Key Dependencies
- MetaTrader5, numpy, pandas, matplotlib, mplfinance, httpx, python-dotenv, PyMuPDF

## Reference Material
- `MMM/MMM Book.pdf` — Steve Mauro's Market Maker Method seminar notes (84 pages)
- `docs/mmm_methodology/` — 16-topic canonical MMM documentation with decision trees
- `data/mmm_training/` — Training data from Steve Mauro videos
