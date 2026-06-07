# 07 — M-Top and W-Bottom Formations

## Overview

M/W formations are THE PRIMARY DIRECTION SIGNAL in MMM. They override the stop
hunt breach direction. The M/W tells you where market makers want price to go.

## Core Rule

```
W-bottom = BUY  (double bottom → MMs hunted lows → true trend is UP)
M-top    = SELL (double top → MMs hunted highs → true trend is DOWN)
```

The breach side is the FAKE move. The M/W shows the REAL intention.

## W-Bottom (Buy Signal)

```
     |     |
     |  ↑  |
     | / \ |
     |/   \|
 ----x     x----    ← Two troughs (within 20 pips)
       valley       ← Peak between troughs
```

### Detection (from `mtf_analyzer.py`)
- Scan last 20 M15 bars for two lows with a higher point between them
- Trough difference must be < 20 pips (two bottoms at approximately same level)
- The "valley" between the troughs confirms the pattern

```python
# W-bottom: two troughs with peak between
for i in range(2, len(lows) - 2):
    if lows[i] > lows[i-2] and lows[i] > lows[i+2]:
        trough_diff = abs(lows[i-2] - lows[i+2]) / pip_size
        if trough_diff < 20:
            m_w = True
            direction = Direction.BUY
```

### What It Means
- MMs pushed price down twice (the stop hunt)
- Price rejected both times at similar levels
- The double bottom IS the stop hunt — even if the breach was small
- True trend is UP from this formation

## M-Top (Sell Signal)

```
 ----x     x----    ← Two peaks (within 20 pips)
     |\   /|
     | \ / |
     |  v  |
     |     |
       valley       ← Trough between peaks
```

### Detection
- Scan last 20 M15 bars for two highs with a lower point between them
- Peak difference must be < 20 pips
- The trough between peaks confirms the pattern

```python
# M-top: two peaks with valley between
for i in range(2, len(highs) - 2):
    if highs[i] < highs[i-2] and highs[i] < highs[i+2]:
        peak_diff = abs(highs[i-2] - highs[i+2]) / pip_size
        if peak_diff < 20:
            m_w = True
            direction = Direction.SELL
```

## Direction Override Logic

This is CRITICAL and was a key correction in Helix V3:

```
IF M/W detected AND M/W direction is not neutral:
    → M/W direction overrides stop hunt breach direction
    → If no stop hunt was detected, the M/W itself validates it as soft hunt

IF stop hunt detected AND M/W detected:
    → hunt_direction = m_w_direction (M/W overrides)

IF no stop hunt detected AND (M/W OR RRT) AND any breach >= 1 pip:
    → Treat as soft hunt
    → Use M/W direction
```

## RRT as Compressed M/W

Railroad Tracks (RRT) = two consecutive candles of opposite direction with similar
body size. This is a "compressed M/W" — the same reversal signal in a tighter
timeframe. RRT can substitute for M/W in entry logic.

## Confluence Points

- M/W detected: +25 points (highest single bonus)
- M/W + deep stop hunt: +35 total (hunt +10, depth +10, M/W +25)
- Price already reversed past Asian range in M/W direction: +10 bonus

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| M/W is primary direction signal | UNTESTED | Win rate when following M/W vs breach |
| 20-pip trough/peak tolerance | UNTESTED | Optimize tolerance per pair |
| M/W overrides stop hunt direction | UNTESTED | Outcomes: override vs non-override |
| RRT substitutes for M/W | UNTESTED | Compare RRT vs M/W signal quality |
| M/W at Asian boundary = soft hunt | UNTESTED | Soft hunt + M/W outcomes |
