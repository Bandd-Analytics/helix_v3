# 02 — The 3-Day Cycle

## Overview

Per Steve Mauro, market makers operate on a 3-day cycle on the H4 timeframe.
This is the structural backbone of MMM. Each cycle moves from one peak to the
next through defined levels.

## Cycle Structure

```
Peak High
  |
  L1 ←── First consolidation (pullback from peak)
  |
  L2 ←── Second consolidation (deeper pullback)
  |
  L3 ←── Third consolidation (extended, choppy)
  |
Peak Low
  |
  L1 ←── First consolidation (rally from bottom)
  |
  L2 ←── Second consolidation
  |
  ...repeats
```

## Level Characteristics

### Level 1 (L1)
- **Where**: First move from peak formation
- **Expected move**: 60-100 pips (pair dependent)
- **Character**: Clean, directional, highest probability
- **Trading**: Best entry zone. Enter after stop hunt confirms direction.
- **Duration**: Typically 1 trading day

### Level 2 (L2)
- **Where**: Second consolidation zone after L1
- **Expected move**: Similar to L1 but less predictable
- **Character**: Potential for false breaks, more volatile consolidation
- **Trading**: Can trade if L1 direction confirmed. Use tighter stops.
- **Duration**: 1-2 trading days

### Level 3 (L3)
- **Where**: Extended move, third consolidation
- **Expected move**: Smaller, price is exhausted
- **Character**: Choppy, whipsaw-prone. MMs preparing reversal.
- **Trading**: AVOID unless very strong confluence. This is where the next
  peak formation occurs.
- **Duration**: 0.5-1 trading day

## Counting Levels on H4

Implementation (from `mtf_analyzer.py`):

1. Find the most recent peak high or peak low on H4 (last 30 bars)
2. Count significant swing reversals since the peak
3. Map swing count to level:
   - 0-2 swings = L1 (still in first move)
   - 3-5 swings = L2 (consolidating/second leg)
   - 6+ swings = L3 (choppy, extended)

## Expected Level Move Sizes

From `pair_profiles.py`:

| Pair | Expected Level Move |
|------|-------------------|
| EURUSD | 70 pips |
| GBPUSD | 80 pips |
| AUDUSD | 55 pips |
| GBPAUD | 100 pips |
| GBPJPY | 100 pips |
| GBPNZD | 110 pips |
| EURJPY | 85 pips |
| EURCHF | 45 pips |
| GBPCHF | 85 pips |
| USDCHF | 60 pips |
| USDJPY | 80 pips |
| AUDJPY | 75 pips |
| XAUUSD | 800 pips ($8.00) |

## Cycle Position and Trade Decisions

| Position | H4 Signal | Action |
|----------|-----------|--------|
| PEAK_HIGH | Just made cycle high | Look for SELL setups |
| L1 (from high) | First move down confirmed | SELL if stop hunt confirms |
| L2 (from high) | Second consolidation | SELL with caution, tighter SL |
| L3 (from high) | Extended, choppy | AVOID — reversal imminent |
| PEAK_LOW | Just made cycle low | Look for BUY setups |
| L1 (from low) | First move up confirmed | BUY if stop hunt confirms |
| L2 (from low) | Second consolidation | BUY with caution |
| L3 (from low) | Extended, choppy | AVOID — reversal imminent |

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| 3-day cycle exists on H4 | UNTESTED | Measure actual peak-to-peak durations |
| L1 is most profitable | UNTESTED | Compare RR by entry level |
| L3 is choppy/dangerous | UNTESTED | Measure win rate at L3 vs L1/L2 |
| Level move sizes per pair | UNTESTED | Measure actual H4 level distances |
