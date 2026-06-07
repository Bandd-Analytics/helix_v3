# 08 — Entry Setups (Trade Types)

## Overview

Per MMM, there are 5 distinct trade types. Each has different entry conditions,
probabilities, and risk profiles.

## Trade Type Classification

From `patterns.py`:

### 1. Straightaway Trade
- **What**: Direct breakout from Asian range WITHOUT a stop hunt
- **Conditions**:
  - Asian range < 30 pips (very tight accumulation)
  - No M/W or spike detected
  - Price moves > 20 pips beyond Asian boundary cleanly
- **Character**: Rare but powerful. MMs skip the stop hunt and go straight.
- **Risk**: Higher — no stop hunt confirmation means less certainty.
- **When**: Usually early London on news-driven days.

### 2. 2nd Leg M/W Setup (Primary)
- **What**: Classic MMM trade. Stop hunt → M/W formation → entry on reversal.
- **Conditions**:
  - Asian accumulation valid
  - Stop hunt detected (hard or soft)
  - M/W pattern confirmed
  - TDI confirmation preferred
- **Character**: THE bread-and-butter MMM trade. Highest win rate.
- **Risk**: Moderate — well-defined SL behind M/W extreme.
- **When**: London session, after stop hunt completes.

### 3. The 33 Trade
- **What**: 3 pushes in the stop hunt zone with multiple reversal confirmations.
- **Conditions**:
  - 3+ pushes beyond Asian range
  - 2+ RRT patterns OR 3+ pin bars at the extreme
  - Multiple rejection candles
- **Character**: High-conviction setup. Three pushes = exhaustion.
- **Risk**: Lower — clear reversal zone, tight SL behind push 3.
- **When**: London Gap or early London.

### 4. NYC Reversal
- **What**: Reversal at New York open, opposite to the London direction.
- **Conditions**:
  - Session hour 13-17 UTC (NY session)
  - M/W pattern detected at the day's extreme
  - London move was extended (price at L2/L3)
- **Character**: Counter-trend against London. Second opportunity of the day.
- **Risk**: Higher — trading against established momentum.
- **When**: NY Gap (13:00-14:00 UTC) or early NYC.

### 5. EMA 200 Bounce
- **What**: Reversal off the 200-period EMA on M15.
- **Conditions**:
  - Price within 15 pips of EMA 200
  - Pin bar(s) at the EMA
  - EMA acting as support/resistance
- **Character**: Confluence trade. Uses EMA as additional confirmation.
- **Risk**: Moderate — EMA provides clear invalidation level.
- **When**: Any session, but best during London/NYC.

## Entry Requirements Checklist

For any entry:

1. Asian range valid (< pair-specific max pips)
2. M/W formation detected (W = BUY, M = SELL)
3. Stop hunt confirmed (hard breach or soft breach + M/W)
4. Confluence score >= 50/100 from MTF alignment
5. TDI confirmation (Shark Fin, Blood in the Water, or VB Squeeze)
6. Re-entry guard clear (no recent loss on same pair/direction)
7. No existing open position on same pair

## Confidence Scoring

From `mtf_analyzer.py`:

| Condition | Points |
|-----------|--------|
| Accumulation valid | +20% |
| Stop hunt detected | +20% |
| Deep hunt (>= min pips) | +10% bonus |
| 3+ pushes | +15% |
| 2 pushes | +10% |
| M/W pattern | +25% |
| RRT detected | +15% |
| Price reversed past Asian range | +10% |

Maximum confidence: 100% (capped)

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| 2nd Leg M/W is highest win rate | UNTESTED | Compare win rate by trade type |
| The 33 has lowest risk | UNTESTED | Compare SL hit rate by trade type |
| NYC Reversal is counter-trend | UNTESTED | Win rate: NYC reversal vs continuation |
| Straightaway is rare but powerful | UNTESTED | Frequency and RR of straightaway |
| Confidence scoring is predictive | UNTESTED | Correlate confidence with outcomes |
