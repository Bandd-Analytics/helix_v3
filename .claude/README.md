# Helix V3 - Claude Project Configuration

## Project Overview
Enterprise-grade MMM (Market Maker Method) algorithmic execution system trading on MetaTrader 5 via Python. Targets Sharpe Ratio > 1.5 with max drawdown < 8%.

## Architecture
```
Data Ingestion (MT5) -> Quant Pre-Filter -> Chart Export -> Vision Consensus -> Execution
                                                                |
                                                    15-min Market Scanner
                                                    Trade Journal (SQLite)
                                                    WhatsApp Alerts (Twilio)
```

## Key Modules
| Module | Path | Purpose |
|--------|------|---------|
| Quant Engine | `helix_v3/core/quant_engine.py` | EMA vectors, accumulation, stop-hunt detection |
| Chart Visualizer | `helix_v3/visualization/chart_exporter.py` | 1024x1024 vision-ready charts |
| Consensus Validator | `helix_v3/consensus/validator.py` | Multi-mode LLM chart analysis |
| Execution Gatekeeper | `helix_v3/execution/gatekeeper.py` | Risk-gated MT5 order execution |
| Trade Journal | `helix_v3/journal/trade_journal.py` | 75-field trade logging + analytics |
| Market Scanner | `helix_v3/scanner/market_scanner.py` | 15-min condition evaluator |
| WhatsApp Notifier | `helix_v3/notifications/whatsapp.py` | Twilio alerts + period reports |
| Pair Profiles | `config/pair_profiles.py` | Per-pair risk tiers and trade rules |
| Orchestrator | `helix_v3/orchestrator.py` | Main pipeline loop + report scheduler |

## Risk Tiers
- **Low** (EURUSD, GBPUSD, AUDUSD): 1% risk, tight trailing
- **Medium** (GBPAUD, GBPJPY, GBPNZD): 0.8% risk, wider thresholds
- **High** (XAUUSD): 0.5% risk, short duration, wide buffers

## Configuration
- `.env` — API keys, MT5 credentials, risk parameters, Twilio config
- `config/settings.py` — Global settings (loaded from .env)
- `config/pair_profiles.py` — Per-pair risk rules

## Databases
- `logs/trade_journal.db` — Trade history and analytics
- `logs/market_scanner.db` — Market condition snapshots

## Running
```bash
.venv/Scripts/python.exe -m helix_v3.orchestrator  # Start live system
.venv/Scripts/python.exe tests/live_test.py          # Run integration test
```
