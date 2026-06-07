# 12 — EMA Structure

## Overview

MMM uses a 5-EMA stack (5/13/50/200/800) to determine trend direction and
strength. The EMA structure is analyzed on every timeframe.

## EMA Periods

| EMA | Purpose |
|-----|---------|
| 5 | Immediate momentum (1 day of M15 bars) |
| 13 | Short-term trend |
| 50 | Medium-term trend |
| 200 | Long-term trend, major S/R level |
| 800 | Ultra-long-term, institutional bias |

## EMA Angle Calculation

Each EMA's angle measures its current slope:

```python
angle = degrees(arctan2(ema[-1] - ema[-6], 5))
```

Positive angle = trending up, negative = trending down.

## Trend Alignment

From `quant_engine.py` and `mtf_analyzer.py`:

- **All EMAs positive angle** → BUY trend (stacked bullish)
- **All EMAs negative angle** → SELL trend (stacked bearish)
- **Mixed angles** → NEUTRAL (no clear trend, reduce size)

## Fast/Slow Divergence

```
fast_slow_divergence = angle(EMA_5) - angle(EMA_200)
```

- Large positive → Strong bullish momentum (5 EMA accelerating away from 200)
- Large negative → Strong bearish momentum
- Near zero → Converging, potential trend change

## Crossover Signals

From `tdi.py` crossover arrows:

### Short-Term Cross (EMA 7/13)
- Uses shift(1) guard against repainting
- EMA 7 crosses above EMA 13 → BUY arrow
- EMA 7 crosses below EMA 13 → SELL arrow

### Long-Term Cross (EMA 50/200)
- **Golden Cross**: EMA 50 crosses above EMA 200 → Bullish trend shift
- **Death Cross**: EMA 50 crosses below EMA 200 → Bearish trend shift

## EMA 200 as S/R

The EMA 200 is a key level in MMM:
- When price is above EMA 200 → Bullish bias
- When price is below EMA 200 → Bearish bias
- Price touching EMA 200 with pin bar → EMA 200 Bounce trade type
- Bounce within 15 pips of EMA 200 qualifies

## EMA Stack on Different Timeframes

| Timeframe | EMAs Used | Purpose |
|-----------|-----------|---------|
| D1 | 5/13/50/200 | Weekly bias |
| H4 | 5/13/50/200/800 | 3-day cycle direction |
| H1 | 5/13/50/200/800 | Intraday trend |
| M15 | 5/13/50/200/800 | Entry-level momentum |

## EMA 50/200 Cross on H1

From `mtf_analyzer.py`:
- Recent bullish cross → +confluence for BUY entries
- Recent bearish cross → +confluence for SELL entries
- "Recent" = within last 3 H1 bars

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| EMA stack alignment predicts trend | UNTESTED | Trend continuation rate when fully stacked |
| EMA 200 acts as S/R | UNTESTED | Bounce rate at EMA 200 |
| Golden/Death cross timing | UNTESTED | Post-cross directional accuracy |
| Fast/slow divergence is predictive | UNTESTED | Divergence vs subsequent price move |
