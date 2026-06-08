# Flashcard: Volume Z-Score Candle Coloring

## Source
- PineScript: `mt5/indicators/pinescript_source/Candle_Colored_Volume_Zscore.pine` (by M0rty)
- MQ5 Port: `mt5/indicators/Helix_Volume_Zscore_Candles.mq5`

## Concept

Colors candles based on how unusual their volume/body size is compared to recent history, using Z-scores:

```
Z = (current_value - SMA(20)) / StdDev(20)
```

## Classification

| Z-Score | Category | Up Color | Down Color | Meaning |
|---------|----------|----------|------------|---------|
| < -1.0 | Low Volume | Yellow | Yellow | Accumulation / quiet market |
| < 1.5 | Normal | White | Gray | Regular market activity |
| 1.5 - 2.5 | Large | Blue | Purple | Significant move — pay attention |
| > 2.5 | Extreme | Green | Red | MM trap candle / spike — expect reversal |

## Source Modes

| Mode | Logic | Best For |
|------|-------|----------|
| Volume | Z-score of tick volume only | Standard — detects volume spikes |
| Body Size | Z-score of |close-open| | Detects oversized candles regardless of volume |
| Any | max(vol_z, body_z) | Catches either volume OR body outliers |
| All | min(vol_z, body_z) | Only flags when BOTH volume AND body are extreme |

## MMM Alignment

### Low Volume (Yellow) = Accumulation
- Z < -1.0 on volume = abnormally quiet
- Per MMM: Asian session should show low volume (accumulation phase)
- **Validation**: Use to CONFIRM accumulation is genuine, not just a narrow range with normal volume

### Extreme Volume (Green/Red) = Stop Hunt / Spike Candle
- Z > 2.5 = extreme outlier
- Per MMM: Spike candles at stop hunt = MM trap. Expect pullback.
- **Matches**: `patterns.py` SPIKE_CANDLE detection (body > 2.5x average)
- The Z-score approach is more statistically rigorous than the current 2.5x average body check

### Large Volume (Blue/Purple) = True Trend Confirmation
- Z 1.5-2.5 = significant but not extreme
- Per MMM: Volume should increase during true trend phase (London)
- Large volume confirming M/W direction = higher confidence entry

## Integration Opportunities

### 1. Improve Spike Detection in patterns.py
Current: `body > avg_body * 2.5` (hardcoded multiplier)
Better: Z-score based — adapts to pair-specific volatility automatically.

```python
# Replace hardcoded 2.5x with Z-score
z_body = (body - mean_body) / std_body
if z_body > 2.5:  # Extreme
    # spike candle
elif z_body > 1.5:  # Large
    # significant candle, not yet spike
```

### 2. Accumulation Confirmation via Volume Z
Current: Only checks Asian range width for accumulation validity.
Better: Also check that volume Z < -1.0 during Asian session — confirms genuine quiet accumulation vs narrow range with active trading (which is a different signal).

### 3. Entry Quality Filter
- Extreme volume bar AT entry = likely chasing the spike (bad entry)
- Low volume + M/W = genuine accumulation reversal (good entry)
- Large volume confirming direction after entry = hold with confidence

## Key Parameters
- Lookback: 20 bars (matches M15 = 5 hours of context)
- Z1 threshold: 1.5 (large)
- Z2 threshold: 2.5 (extreme)
- Low volume: -1.0
