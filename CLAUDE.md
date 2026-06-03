# Helix V3 - MMM Algorithmic Execution System

## Project Overview
Enterprise-grade Market Maker Method (MMM) algorithmic execution system trading on MetaTrader 5 via Python. Based on Steve Mauro's MMM methodology with quantitative pre-filtering, dual-LLM vision consensus, pair-gated risk management, and automated WhatsApp notifications.

**Account**: ICMarketsKE-Demo (52846409)
**Timezone**: All user-facing timestamps in EAT (UTC+3, Kenyan time)
**Risk Target**: Sharpe Ratio > 1.5, Max Drawdown < 8%

## Architecture

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
                  Vision Consensus     <- local / anthropic / dual-api
                  (validator.py)
                         |
                  Pair-Gated Risk      <- pair_profiles.py
                  (gatekeeper.py)
                         |
              +----------+----------+
              |          |          |
         MT5 Execute  Journal   WhatsApp
                    (trade_journal) (Twilio)
                         |
                    Flashcards         <- Market structure learning
                    (flashcards.py)
```

## File Map

### Core Trading Logic
| File | Purpose |
|------|---------|
| `helix_v3/core/types.py` | Shared dataclasses: Direction, CycleLevel, QuantSignal, ConsensusResult, ExecutionOrder |
| `helix_v3/core/quant_engine.py` | MT5 data fetch, EMA vectors, Asian accumulation, stop-hunt detection |
| `helix_v3/core/mtf_analyzer.py` | Multi-timeframe analysis: Weekly->4H->1H->15M with confluence scoring |

### Visualization
| File | Purpose |
|------|---------|
| `helix_v3/visualization/chart_exporter.py` | 1024x1024 clean charts for vision model consumption |
| `helix_v3/visualization/annotated_chart.py` | Charts with confluence markings (Asian box, HOD/LOD, entry/SL/TP, info overlay) |

### Consensus
| File | Purpose |
|------|---------|
| `helix_v3/consensus/validator.py` | Multi-mode vision verification: local (Claude Code), anthropic (API), dual-api (Claude+GPT) |

### Execution
| File | Purpose |
|------|---------|
| `helix_v3/execution/gatekeeper.py` | Pair-gated order execution, T1 partial close, trailing SL, stale/time/session exits |

### Journal & Learning
| File | Purpose |
|------|---------|
| `helix_v3/journal/trade_journal.py` | 75-field trade logging, period reports (session/EOD/weekly/monthly), performance analytics |
| `helix_v3/journal/flashcards.py` | Market structure snapshots with MTF context, pattern-outcome learning database |

### Scanner
| File | Purpose |
|------|---------|
| `helix_v3/scanner/market_scanner.py` | 15-min recurring market condition evaluator, readiness scoring (0-100) |

### Notifications
| File | Purpose |
|------|---------|
| `helix_v3/notifications/whatsapp.py` | Twilio WhatsApp alerts: setups, entries, exits (full report), T1 hits, period reports, flashcard charts |

### Configuration
| File | Purpose |
|------|---------|
| `config/settings.py` | Global settings loaded from .env |
| `config/pair_profiles.py` | Per-pair risk tiers, trade management rules, stop hunt ranges |
| `.env` | API keys, MT5 credentials, risk parameters, Twilio config |

### Orchestrator
| File | Purpose |
|------|---------|
| `helix_v3/orchestrator.py` | Main pipeline loop: 60s trade scan, 15-min market scan, report scheduler, trade management |

## MMM Trading Rules (from Steve Mauro methodology)

### Multi-Timeframe Analysis Sequence
1. **Weekly (D1/H4)**: Where in the 3-day/weekly cycle? Peak high/low? Mid-week reversal due?
2. **4-Hour (H4)**: Level count (L1/L2/L3). Peak formation? Choppy (L3)?
3. **1-Hour (H1)**: Session phase. HOD/LOD locked? EMA 50/200 cross?
4. **15-Min (M15)**: Asian range < 50 pips? Stop hunt 25-50p with 3 pushes? M/W? RRT?

### Entry Requirements
- Asian range < pair-specific max (40-65 pips depending on pair)
- Stop hunt detected (25-50 pips beyond range, pair-adjusted)
- 3 pushes in the stop hunt zone
- M/W formation OR Railroad Tracks at reversal
- All 4 timeframes aligned (confluence score >= 50/100)

### Trade Management
- **Universal**: 90 min max if NOT in profit -> close (stale exit)
- **If in profit**: Trail SL, never exit early
- **T1**: 50% close at 1:1 RR, SL to breakeven
- **Trailing SL**: Activates at pair-specific threshold, trails at pair distance
- **Max duration**: Pair-specific hard cap (3-5 hours)
- **Session exit**: Close before Asian session if not profitable

## Pair Risk Profiles

| Pair | Tier | Risk% | Hunt Range | Level Move | Trail | SL Buffer |
|------|------|-------|-----------|-----------|-------|-----------|
| EURUSD | Low | 1.0% | 20-40p | 70p | 15/12p | 3p |
| GBPUSD | Low | 1.0% | 25-50p | 80p | 20/15p | 3p |
| AUDUSD | Low | 1.0% | 15-35p | 55p | 12/10p | 3p |
| GBPAUD | Medium | 0.8% | 30-60p | 100p | 30/22p | 5p |
| GBPJPY | Medium | 0.8% | 30-60p | 100p | 25/18p | 5p |
| GBPNZD | Medium | 0.8% | 30-65p | 110p | 35/25p | 5p |
| XAUUSD | High | 0.5% | 200-500p | 800p | 100/80p | 30p |

## Databases
- `logs/trade_journal.db` — Trade history (75 fields per trade)
- `logs/market_scanner.db` — 15-min market condition snapshots
- `logs/flashcards.db` — Market structure pattern learning

## Report Schedule (all times EAT)
- **Session reports**: Auto-sent when session transitions (Asian->London->NY)
- **EOD**: 00:00 EAT daily
- **Weekly**: Saturday 00:00 EAT (best/worst pair only)
- **Monthly**: 1st of month 00:00 EAT (best/worst pair only)

## Consensus Modes
- `local`: Claude Code analyzes charts, writes verdicts to `verdicts/`. No API cost.
- `anthropic`: Two Claude API calls with different prompts (self-consensus)
- `dual-api`: Claude + GPT-5.5 in parallel (requires both API keys)

Set via `CONSENSUS_MODE` in `.env`.

## Running
```bash
.venv/Scripts/python.exe -m helix_v3.orchestrator   # Full autonomous system
.venv/Scripts/python.exe tests/live_test.py           # Integration test
.venv/Scripts/python.exe tests/execute_gbpjpy.py      # Single pair execution
```

## Key Dependencies
- MetaTrader5, numpy, pandas, matplotlib, mplfinance, httpx, python-dotenv, PyMuPDF

## Reference Material
- `MMM/MMM Book.pdf` — Steve Mauro's Market Maker Method seminar notes (84 pages)
