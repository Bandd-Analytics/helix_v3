# Backtest Results Archive

## Latest: 365-Day Calibrated Backtest (2025-06-07 to 2026-06-07)

**File**: `backtest_365d_2025-06-07_to_2026-06-07.txt`

### Configuration
- Pairs: EURUSD, GBPUSD, AUDUSD, GBPAUD, GBPJPY, EURCHF, GBPCHF, USDCHF (8 active)
- Confluence threshold: 55
- M/W filter: Full weight in London, reduced in NYC, minimal outside
- TP: min(expected_level_move, 3x SL), floor 1.5x SL
- SL: Capped at expected_level_move_pips from entry
- Stop hunt ranges: Calibrated from 90-day P90 validation data
- Stale exit: Tiered (90min tighten / pair-specific exit) for volatile crosses

### Key Metrics
| Metric | Value |
|--------|-------|
| Starting equity | $1,000 |
| Final equity | $35,033 |
| Net P&L | +$34,033 (+3,403%) |
| Sharpe Ratio | 4.37 |
| Profit Factor | 2.23 |
| Max Drawdown | $944.84 |
| Total Trades | 1,943 |
| Win Rate | 38.7% |
| Expectancy | +5.6 pips/trade |

### Calibration History
| Run | Period | Pairs | Conf | Net P&L | PF | Sharpe |
|-----|--------|-------|------|---------|-----|--------|
| Baseline (Codex) | 14d | 4 | 50 | +$124 | 2.50 | 4.65 |
| + Calibrations | 14d | 13 | 50 | +$169 | 3.04 | -2.27 |
| + TP/SL fix | 14d | 13 | 50 | +$168 | 2.71 | -2.17 |
| + Hard filters | 14d | 8 | 60 | +$6 | 1.12 | -0.73 |
| Middle ground | 60d | 8 | 55 | +$1,085 | 2.65 | 3.92 |
| **Final (1yr)** | **365d** | **8** | **55** | **+$34,033** | **2.23** | **4.37** |
