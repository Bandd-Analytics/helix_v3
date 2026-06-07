# 09 — Context-Aware Candlestick Patterns

## Core Principle

Per Steve Mauro: "Candlestick patterns are ONLY significant at the right location."
A hammer mid-trend is meaningless. A hammer at HOD/LOD is critical.

Significance scoring (from `patterns.py`):
- Pattern at previous HOD/LOD: 0.9 significance
- Pattern at Asian high/low: 0.8 significance
- Pattern mid-range (no context): 0.3 significance (mostly noise)

## Patterns Detected

### Spike Candle / Empire State
- **Definition**: Body > 2.5x the average body of the last 10 bars
- **Meaning**: Market maker trap candle. Oversized move to trigger stops.
- **Expect**: Pullback after the spike. Do NOT chase.
- **Context**: Most significant at L1/stop hunt zone.

### Hammer (Bullish Reversal)
- **Definition**: Lower wick > 60% of total range, upper wick < 10%, body < 35%
- **Meaning**: Buyers rejected lower prices. Bullish reversal.
- **Context**: Only valid at LOD, Asian low, or support levels.

### Inverted Hammer (Bearish Reversal)
- **Definition**: Upper wick > 60% of total range, lower wick < 10%, body < 35%
- **Meaning**: Sellers rejected higher prices. Bearish reversal.
- **Context**: Only valid at HOD, Asian high, or resistance levels.

### Doji
- **Definition**: Body < 10% of total range, range > 3 pips
- **Meaning**: Indecision. Direction decided by next candle.
- **Significance**: Scored at 70% of context significance (less reliable alone).

### Spinning Top
- **Definition**: Body 10-35% of range, both wicks > 20%
- **Meaning**: Minor indecision. Similar to doji but with some body.
- **Significance**: Scored at 60% of context significance.

### Pin Bar (Bullish)
- **Definition**: Lower wick > 65%, body < 25%
- **Meaning**: Strong rejection of lower prices. Similar to hammer but more extreme.

### Pin Bar (Bearish)
- **Definition**: Upper wick > 65%, body < 25%
- **Meaning**: Strong rejection of higher prices.

### Railroad Tracks (RRT)
- **Definition**: Two consecutive candles of opposite direction where the smaller
  body is >= 60% of the larger body.
- **Meaning**: "Compressed M/W." Sharp reversal. Expect continuation in the
  second candle's direction.
- **Significance**: Very high at Asian boundaries and stop hunt extremes.

### Evening Star (3-candle bearish reversal)
- **Definition**: Big green → Small body → Big red (red body > 50% of green)
- **Meaning**: Extended RRT. 45-min RRT on M15. Bearish reversal.

### Morning Star (3-candle bullish reversal)
- **Definition**: Big red → Small body → Big green (green body > 50% of red)
- **Meaning**: Extended RRT. Bullish reversal.

### High Test Pattern
- **Definition**: Price approaches previous day's HOD within 10 pips, closes below
- **Meaning**: Rejection at established resistance. Bearish.
- **Significance**: 0.9 (always significant at HOD).

### Low Test Pattern
- **Definition**: Price approaches previous day's LOD within 10 pips, closes above
- **Meaning**: Rejection at established support. Bullish.
- **Significance**: 0.9 (always significant at LOD).

### Half Batman
- **Definition**: One-sided M or W pattern. Sharp drop, flat bottom, ramp up
  (or inverse). Recovery > 80% of the initial drop, drop > 15 pips.
- **Meaning**: Continuation pattern. Unlike full M/W (reversal), half batman
  suggests the trend will continue.

## Context Significance Function

```python
def _context_significance(price, prev_hod, prev_lod, asian_high, asian_low):
    sig = 0.3  # base
    if near prev_hod: sig = 0.9
    if near prev_lod: sig = 0.9
    if near asian_high: sig = 0.8
    if near asian_low: sig = 0.8
    return sig
```

"Near" = within 0.2% of the level.

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| Context-aware scoring improves accuracy | UNTESTED | Compare contextual vs non-contextual pattern hit rate |
| RRT is compressed M/W | UNTESTED | Compare RRT reversal rate to M/W |
| Spike candles predict pullback | UNTESTED | Post-spike price behavior analysis |
| High/Low test pattern reliability | UNTESTED | Test rejection rate at prev HOD/LOD |
| Half Batman continuation rate | UNTESTED | Does half batman predict continuation? |
