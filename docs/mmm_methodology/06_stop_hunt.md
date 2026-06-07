# 06 — Stop Hunt Mechanics

## Overview

The stop hunt is the defining moment of the MMM cycle. After Asian accumulation,
market makers spike price beyond the Asian range to trigger retail stop losses,
creating liquidity for their real position. The stop hunt is a FALSE move — the
true trend follows in the opposite direction.

## Stop Hunt Types

### Hard Stop Hunt (Classic)
- Breach of Asian range boundary by 25-50+ pips (pair-specific)
- Clear spike candle(s) beyond the range
- Z-score > 1.5 on M1 closes (mean-reversion signal)
- Absorption: price extended but starting to reverse

### Soft Stop Hunt
- Breach of Asian range by only 1-5 pips
- REQUIRES confirmation: M/W formation or RRT at the extreme
- Per MMM: "Even a 1-pip breach counts if the M/W confirms it"
- The M/W formation IS the stop hunt confirmation — the breach is the fake move

## Stop Hunt Detection Logic

From `mtf_analyzer.py`:

### Step 1: Measure post-Asian breaches
```
max_breach_above = max(post_asian_highs) - asian_high  (in pips)
max_breach_below = asian_low - min(post_asian_lows)    (in pips)
```

### Step 2: Classify hunt type
- **Hard hunt**: `stop_hunt_min_pips <= breach <= stop_hunt_max_pips`
- **Soft hunt**: Any breach >= 1 pip + (M/W confirmed OR RRT detected)

### Step 3: Direction assignment
- Breach ABOVE Asian range → Stop hunt for SELL (fake up, true down)
- Breach BELOW Asian range → Stop hunt for BUY (fake down, true up)
- BUT: **M/W pattern OVERRIDES breach direction** — see [07_mw_formations.md](07_mw_formations.md)

## Stop Hunt Range by Pair

From `pair_profiles.py`:

| Pair | Min Hunt (pips) | Max Hunt (pips) |
|------|----------------|----------------|
| EURUSD | 20 | 40 |
| GBPUSD | 25 | 50 |
| AUDUSD | 15 | 35 |
| GBPAUD | 30 | 60 |
| GBPJPY | 30 | 60 |
| GBPNZD | 30 | 65 |
| EURJPY | 25 | 50 |
| EURCHF | 15 | 30 |
| GBPCHF | 25 | 50 |
| USDCHF | 20 | 40 |
| USDJPY | 25 | 50 |
| AUDJPY | 20 | 45 |
| XAUUSD | 200 | 500 |

## The 3 Pushes

Per MMM, the ideal stop hunt has 3 pushes beyond the Asian boundary:

1. **Push 1**: Initial breach — tests the stop cluster
2. **Push 2**: Deeper breach — triggers more stops, sucks in breakout traders
3. **Push 3**: Final push — last liquidity grab, often forms the extreme

The push count is measured by counting sequential new highs (for upward hunt)
or new lows (for downward hunt) in the post-Asian bars.

From `mtf_analyzer.py`:
```python
def _count_pushes(values, direction):
    pushes = 1
    for i in range(1, len(values)):
        if direction == "up" and values[i] > values[i-1]:
            pushes += 1
        elif direction == "down" and values[i] < values[i-1]:
            pushes += 1
    return min(pushes, 5)
```

### Push Count Scoring
- 3+ pushes: +15 confluence points (ideal)
- 2 pushes: +10 confluence points
- 1 push: No bonus

## Z-Score Mean Reversion

From `quant_engine.py`:

After the stop hunt breach, calculate the Z-score on M1 closes:
```
z_score = (current_close - mean(last_60_closes)) / std(last_60_closes)
```

- `|z_score| > 1.5` → Price extended, mean reversion expected (absorption)
- Absorption confirms the stop hunt is completing

## Stop Hunt Invalidation

A stop hunt is NOT valid if:
- Breach exceeds the pair's max_hunt_range (too much momentum, likely a breakout)
- No reversal patterns form at the extreme (no M/W, no RRT, no pin bars)
- Price continues strongly beyond the hunt zone without any pullback

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| Stop hunt range per pair | UNTESTED | Actual distribution of breach sizes |
| 3 pushes is optimal | UNTESTED | Win rate by push count |
| Soft hunts with M/W are valid | UNTESTED | Compare soft vs hard hunt outcomes |
| Z-score > 1.5 predicts reversal | UNTESTED | Test z-score threshold accuracy |
| Max hunt breach = invalidation | UNTESTED | Outcomes when breach exceeds max |
