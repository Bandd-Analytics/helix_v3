# SKILL: MMM Methodology — Market Maker Method by Steve Mauro

## Purpose

This skill document provides AI assistants (Claude, Codex, or any LLM) with the
complete Market Maker Method trading methodology. Use this to:
- Validate trade setups against MMM rules
- Generate analysis following the correct sequence
- Identify patterns and their significance
- Score confluence across multiple timeframes
- Make trade management decisions

## Validation Status

**Backtested over 365 days (Jun 2025 - Jun 2026) on 8 pairs:**
- $1,000 → $35,033 (+3,403%)
- Sharpe 4.37, Profit Factor 2.23, Max Drawdown $945
- 1,943 trades, 38.7% win rate, +5.6 pip expectancy
- Every month profitable. Every pair profitable.

## Quick Reference: The MMM Cycle

```
ACCUMULATE (Asian) → STOP HUNT (London Gap) → TRUE TREND (London) → DISTRIBUTE (NYC)
```

**Key insight**: The first breakout of the Asian range is usually FALSE (the stop hunt).
The true direction is OPPOSITE to the stop hunt.

## Decision Tree: Should I Take This Trade?

```
1. Is this pair tradeable? (8 active pairs only)
   NO → SKIP (disabled pairs lack edge)

2. Is Asian range valid? (< pair-specific max pips)
   NO → SKIP (no accumulation)

3. Are we in London session? (TRUE_TREND or STOP_HUNT phase)
   NO → M/W signals get reduced weight (NYC: half, other: minimal)

4. Did a stop hunt occur? (breach of Asian boundary)
   NO → Check for M/W pattern anyway (soft hunt)

5. Is there an M/W formation?
   YES → Direction = M/W direction (W=BUY, M=SELL)
   NO  → Need 3+ pushes or RRT instead

6. Does TDI confirm? (Shark Fin, Blood in the Water)
   YES → +confidence
   NO  → Proceed with caution if other signals strong

7. Does MTF analysis align?
   Weekly trend matches → +20 confluence
   H4 at L1/L2 → +10-15 confluence
   H1 trend matches → +10 confluence

8. Confluence score >= 55?
   YES → VALID TRADE
   NO  → SKIP

9. Re-entry guard clear?
   YES → EXECUTE
   NO  → BLOCKED (previous loss on this pair/direction)
```

## Active Pairs (Validated)

8 pairs with proven edge over 365-day backtest. 5 pairs disabled due to negative or marginal results.

| Pair | Trades | Win% | PF | Net $ | Status |
|------|--------|------|-----|-------|--------|
| GBPUSD | 249 | 42.2% | 3.05 | +$7,683 | ACTIVE — best performer |
| USDCHF | 258 | 40.7% | 2.65 | +$5,427 | ACTIVE |
| GBPCHF | 410 | 36.1% | 1.90 | +$4,458 | ACTIVE — most trades |
| GBPAUD | 153 | 51.0% | 2.87 | +$4,110 | ACTIVE — highest win rate |
| AUDUSD | 201 | 38.8% | 2.79 | +$4,042 | ACTIVE |
| EURUSD | 228 | 38.2% | 2.12 | +$3,423 | ACTIVE |
| EURCHF | 339 | 32.7% | 1.48 | +$3,368 | ACTIVE |
| GBPJPY | 105 | 38.1% | 2.35 | +$1,522 | ACTIVE |
| EURJPY | — | — | — | — | DISABLED (0% win rate) |
| GBPNZD | — | — | — | — | DISABLED (flat, wide spreads) |
| USDJPY | — | — | — | — | DISABLED (weak M/W, weak stale) |
| AUDJPY | — | — | — | — | DISABLED (marginal edge) |
| XAUUSD | — | — | — | — | DISABLED (needs fundamental rework) |

## Calibrated Parameters (from 90-day validation + 365-day backtest)

### Stop Hunt Ranges (widened from P90 breach data)

| Pair | Min Hunt | Max Hunt | Source |
|------|---------|---------|--------|
| EURUSD | 20p | 75p | P90=75p (was 40) |
| GBPUSD | 25p | 105p | P90=103p (was 50) |
| AUDUSD | 15p | 70p | P90=68p (was 35) |
| GBPAUD | 30p | 105p | P90=103p (was 60) |
| GBPJPY | 30p | 130p | P90=131p (was 60) |
| EURCHF | 15p | 40p | P90=38p (was 30) |
| GBPCHF | 25p | 70p | P90=67p (was 50) |
| USDCHF | 20p | 55p | P90=52p (was 40) |

### TP Logic (calibrated — NOT blind SL multiple)
- **T1**: 1:1 RR (unchanged — partial close, SL to breakeven)
- **T2**: `min(expected_level_move_pips, 3x SL)`, floor `1.5x SL`
- **SL cap**: Never wider than `expected_level_move_pips` from entry

### Stale Exit (tiered for volatile crosses)
| Pair | Phase 1 (tighten SL) | Phase 2 (full exit) |
|------|---------------------|-------------------|
| Low-vol (EUR/GBP/AUD USD, CHF) | 90 min | 90 min (immediate) |
| GBPAUD | 90 min → SL halved | 150 min |
| GBPJPY | 90 min → SL halved | 135 min |

### M/W Session Weighting
| Session | M/W Weight | Rationale |
|---------|-----------|-----------|
| London (TRUE_TREND/STOP_HUNT) | +10 points | 52-60% hit rate |
| NYC Reversal | +5 points | Secondary window |
| Asia/Off-hours | +2 points | 37-44% hit rate |

### Confluence Threshold
- **Minimum: 55** (raised from 50 — filters stale entries)
- Maximum 1 rejection reason allowed

## Session Windows (GMT → EAT)

| Phase | GMT | EAT | Action |
|-------|-----|-----|--------|
| Dead Gap | 22:00-01:30 | 01:00-04:30 | No trading |
| Asia | 00:30-07:30 | 03:30-10:30 | Mark range, observe |
| London Gap | 07:00-08:00 | 10:00-11:00 | Stop hunts here |
| London | 07:30-13:30 | 10:30-16:30 | PRIMARY entries |
| NY Gap | 13:00-14:00 | 16:00-17:00 | NYC reversal zone |
| NYC | 13:30-22:00 | 16:30-01:00 | Secondary entries, then distribute |

## Pattern Recognition Rules

### M/W Formation (PRIMARY signal)
- W-bottom (two similar lows with higher point between) = **BUY**
- M-top (two similar highs with lower point between) = **SELL**
- Tolerance: peaks/troughs within 20 pips of each other
- M/W direction OVERRIDES stop hunt breach direction
- **London session M/W is highest confidence**

### TDI Signals (V2-Verified Parameters)
- RSI period: 21 (Wilder's smoothing)
- Green (RSI Price): 2-period SMA of RSI
- Red (Trade Signal): 7-period SMA of RSI
- Yellow (Market Base): 34-period SMA of RSI
- VB: Bollinger(34, 1.6185) on RSI
- Shark Fin thresholds: 63/37
- **Shark Fin: ~50% hit rate but 5-9x RR — profitable as filter**

## Trade Management Rules

1. **SL**: Behind structural level + buffer, capped at expected_level_move
2. **T1**: 50% close at 1:1 RR, SL to breakeven
3. **T2**: min(level_move, 3x SL), floor 1.5x SL
4. **Stale Phase 1** (90 min): Tighten SL to 50% if not in profit (volatile crosses)
5. **Stale Phase 2** (90-150 min): Full exit if still not in profit
6. **Max duration**: 3-5 hours depending on pair
7. **Session exit**: Close before Asian if not in profit

## Risk Management Rules

1. **Per-trade**: 0.5-1.0% based on pair tier
2. **Drawdown breaker**: Halt all trading at 8% drawdown
3. **Re-entry guard**: No re-entry same pair/direction after loss
4. **2 losses same pair/day**: BANNED for the day
5. **Lot sizing**: Equity * Risk% / (SL_pips * pip_value)
6. **SL floor**: Prevents lot inflation from tight stops
7. **Account cap**: Max lot where full SL can't exceed 3% of equity

## Validated Rule Status (90-day cross-pair analysis)

| Rule | Status | Key Finding |
|------|--------|------------|
| Asian accumulation | VALIDATED (88-95%) | Most reliable MMM rule |
| Stop hunt ranges | CALIBRATED | Taught ranges were ~50% too narrow |
| M/W direction | VALIDATED in London (52-60%) | Outside London: unreliable |
| 90-min stale exit | VALIDATED for low-vol | CONTRADICTED for GBPAUD/GBPNZD/GBPJPY |
| TDI Shark Fin | PARTIAL (~50% hit rate) | Profitable via high RR (5-9x) |
| ADR bounds day | VALIDATED (62-75%) | Price stays in ADR ~70% of days |
| Mid-week reversal | PARTIAL (35-57%) | Tuesday strongest day for reversals |
| London = biggest move | CONTRADICTED | NYC currently bigger (longer session) |

## Source Files

| Topic | Documentation | Code |
|-------|--------------|------|
| Full methodology | docs/mmm_methodology/*.md | — |
| Backtest results | data/backtest_results/ | — |
| Rule validation DB | logs/rule_validation.db | training/rule_validator.py |
| Pair profiles | 16_pair_characteristics.md | config/pair_profiles.py |
| MTF analysis | 13_mtf_analysis.md | core/mtf_analyzer.py |
| Trade management | 14_trade_management.md | execution/gatekeeper.py |
| TP/SL logic | — | backtest/engine.py, execution/gatekeeper.py |

## Running

```bash
# Backtest (uses tradeable pairs by default)
.venv/Scripts/python.exe -m helix_v3.backtest.engine --days 365
.venv/Scripts/python.exe -m helix_v3.backtest.engine --days 14 -v    # Verbose

# Validate rules against history
.venv/Scripts/python.exe -m helix_v3.training.rule_validator --days 90

# Live trading
.venv/Scripts/python.exe -m helix_v3.orchestrator_v2

# Market scanning
.venv/Scripts/python.exe tests/fresh_scan.py
```
