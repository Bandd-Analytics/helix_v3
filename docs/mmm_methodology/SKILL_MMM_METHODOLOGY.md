# SKILL: MMM Methodology — Market Maker Method by Steve Mauro

## Purpose

This skill document provides AI assistants (Claude, Codex, or any LLM) with the
complete Market Maker Method trading methodology. Use this to:
- Validate trade setups against MMM rules
- Generate analysis following the correct sequence
- Identify patterns and their significance
- Score confluence across multiple timeframes
- Make trade management decisions

## Quick Reference: The MMM Cycle

```
ACCUMULATE (Asian) → STOP HUNT (London Gap) → TRUE TREND (London) → DISTRIBUTE (NYC)
```

**Key insight**: The first breakout of the Asian range is usually FALSE (the stop hunt).
The true direction is OPPOSITE to the stop hunt.

## Decision Tree: Should I Take This Trade?

```
1. Is Asian range valid? (< pair-specific max pips)
   NO → SKIP (no accumulation)

2. Did a stop hunt occur? (breach of Asian boundary)
   NO → Check for M/W pattern anyway (soft hunt)

3. Is there an M/W formation?
   YES → Direction = M/W direction (W=BUY, M=SELL)
   NO  → Need 3+ pushes or RRT instead

4. Does TDI confirm? (Shark Fin, Blood in the Water)
   YES → +confidence
   NO  → Proceed with caution if other signals strong

5. Does MTF analysis align?
   Weekly trend matches → +20 confluence
   H4 at L1/L2 → +10-15 confluence
   H1 trend matches → +10 confluence

6. Confluence score >= 50?
   YES → VALID TRADE
   NO  → SKIP

7. Re-entry guard clear?
   YES → EXECUTE
   NO  → BLOCKED (previous loss on this pair/direction)
```

## Setup Parameters by Pair

| Pair | Risk% | Asian Max | Hunt Range | Level Move | Trail Act/Dist |
|------|-------|-----------|------------|------------|----------------|
| EURUSD | 1.0% | 40p | 20-40p | 70p | 15/12p |
| GBPUSD | 1.0% | 50p | 25-50p | 80p | 20/15p |
| AUDUSD | 1.0% | 35p | 15-35p | 55p | 12/10p |
| GBPAUD | 0.8% | 60p | 30-60p | 100p | 30/22p |
| GBPJPY | 0.8% | 50p | 30-60p | 100p | 25/18p |
| GBPNZD | 0.8% | 65p | 30-65p | 110p | 35/25p |
| EURJPY | 0.8% | 50p | 25-50p | 85p | 20/15p |
| EURCHF | 1.0% | 25p | 15-30p | 45p | 10/8p |
| GBPCHF | 0.8% | 50p | 25-50p | 85p | 22/16p |
| USDCHF | 1.0% | 35p | 20-40p | 60p | 15/12p |
| USDJPY | 0.8% | 45p | 25-50p | 80p | 20/15p |
| AUDJPY | 0.8% | 45p | 20-45p | 75p | 18/14p |
| XAUUSD | 0.5% | 400p | 200-500p | 800p | 100/80p |

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

### Stop Hunt Classification
- **Hard hunt**: 25-50+ pip breach of Asian boundary (pair-specific)
- **Soft hunt**: 1-5 pip breach + M/W or RRT confirmation
- **3 pushes**: Ideal — count sequential new highs/lows past Asian boundary

### TDI Signals (V2-Verified Parameters)
- RSI period: 21 (Wilder's smoothing)
- Green (RSI Price): 2-period SMA of RSI
- Red (Trade Signal): 7-period SMA of RSI
- Yellow (Market Base): 34-period SMA of RSI
- VB: Bollinger(34, 1.6185) on RSI
- Shark Fin thresholds: 63/37

## Trade Management Rules

1. **SL**: Behind M/W extreme + pair buffer (3-5 pips). Min floor per pair.
2. **T1**: 50% close at 1:1 RR, SL to breakeven
3. **Trailing**: Activates at pair-specific threshold, trails at pair distance
4. **90-min stale exit**: NOT in profit after 90 min → CLOSE (universal)
5. **Max duration**: 3-5 hours depending on pair
6. **Session exit**: Close before Asian if not in profit

## Risk Management Rules

1. **Per-trade**: 0.5-1.0% based on pair tier
2. **Drawdown breaker**: Halt all trading at 8% drawdown
3. **Re-entry guard**: No re-entry same pair/direction after loss
4. **2 losses same pair/day**: BANNED for the day
5. **Lot sizing**: Equity * Risk% / (SL_pips * pip_value)

## Multi-Timeframe Analysis Sequence

ALWAYS follow this order — never skip levels:

### 1. Weekly (D1/H4)
- Where in 3-day cycle? Peak high or low?
- Is mid-week reversal due? (Tue/Wed)
- Weekly EMA bias (5/13/50/200 on D1)

### 2. 4-Hour (H4)
- Level count: L1 (best), L2 (OK), L3 (avoid)
- Is market choppy?
- Peak formation detected?

### 3. 1-Hour (H1)
- What session phase? (Accumulation/Stop Hunt/True Trend/NYC/Distribution)
- HOD/LOD locked?
- EMA 50/200 cross?

### 4. 15-Minute (M15)
- Asian range valid?
- Stop hunt detected? How many pushes?
- M/W forming? Direction?
- RRT detected?

## Confluence Scoring

| Factor | Points |
|--------|--------|
| Weekly trend matches entry | +20 |
| Mid-week reversal expected | +10 |
| H4 at L3 / L2 | +15 / +10 |
| H4 trend matches | +10 |
| H1 trend matches | +10 |
| HOD/LOD locked | +5 |
| Good session timing | +5 |
| Accumulation valid | +5 |
| Stop hunt detected | +10 |
| 3+ pushes | +5 |
| M/W forming | +5 |
| RRT detected | +5 |
| **Threshold** | **>= 50** |

## Validation Framework

Each rule has a validation status:
- **UNTESTED**: Documented but not backtested
- **VALIDATED**: Hit rate >= 60% with N >= 30 historical samples
- **PARTIALLY_VALIDATED**: Hit rate 40-60% or small sample
- **CONTRADICTED**: Hit rate < 40% — rule may need adjustment
- **CALIBRATED**: Validated AND parameters optimized from data

Run validation:
```bash
.venv/Scripts/python.exe -m helix_v3.training.rule_validator --days 90
.venv/Scripts/python.exe -m helix_v3.training.rule_validator --pair EURUSD --rule asian_accumulation
.venv/Scripts/python.exe -m helix_v3.training.rule_validator --report
```

## Source Files

| Topic | Documentation | Code |
|-------|--------------|------|
| Full methodology | docs/mmm_methodology/*.md | — |
| Asian range | 05_asian_accumulation.md | core/sessions.py |
| Stop hunt | 06_stop_hunt.md | core/quant_engine.py, core/mtf_analyzer.py |
| M/W patterns | 07_mw_formations.md | core/patterns.py, core/mtf_analyzer.py |
| Entry setups | 08_entry_setups.md | core/patterns.py |
| TDI | 10_tdi_indicator.md | core/tdi.py |
| Trade management | 14_trade_management.md | execution/gatekeeper.py |
| Risk management | 15_risk_management.md | core/reentry_guard.py |
| Pair profiles | 16_pair_characteristics.md | config/pair_profiles.py |
| Validation | — | training/rule_validator.py |
