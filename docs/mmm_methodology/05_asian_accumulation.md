# 05 — Asian Accumulation

## Overview

The Asian session is where market makers build positions ("accumulate") within a
tight price range. This accumulation creates the "Asian box" — the foundation for
the stop hunt and true trend that follow.

## Core Rule

**Valid accumulation = Asian range below pair-specific maximum.**

If the Asian range is too wide, the accumulation phase has already been disrupted,
and the stop hunt/true trend dynamics become unreliable.

## Asian Range Detection

### Time Window
- **GMT**: 00:30 - 07:30 (from `sessions.py`)
- **EST**: 21:00 - 02:00 (used in `mtf_analyzer.py` for M15 analysis)
- **EAT**: 03:30 - 10:30

### Measurement
1. Collect all M15 bars within the Asian session window
2. Group by calendar date
3. Per day: `high = max(bar highs)`, `low = min(bar lows)`
4. `range_pips = (high - low) / pip_size`
5. `mid = (high + low) / 2`

### Validity Thresholds

From `pair_profiles.py`:

| Pair | Max Asian Range (pips) |
|------|----------------------|
| EURUSD | 40 |
| GBPUSD | 50 |
| AUDUSD | 35 |
| GBPAUD | 60 |
| GBPJPY | 50 |
| GBPNZD | 65 |
| EURJPY | 50 |
| EURCHF | 25 |
| GBPCHF | 50 |
| USDCHF | 35 |
| USDJPY | 45 |
| AUDJPY | 45 |
| XAUUSD | 400 |

## Volatility Compression Score

From `quant_engine.py`:

The volatility compression score quantifies how tight today's Asian range is
compared to historical norms:

```
vol_compression = today_range / mean(daily_session_ranges)
```

- `vol_compression < 0.3` → Very tight accumulation (ideal)
- `vol_compression = 0.3-0.7` → Normal accumulation
- `vol_compression > 1.0` → Wide range, accumulation may be invalid

The `is_accumulation` flag uses the `accumulation_percentile` config threshold.

## What the Asian Box Means

1. **Stop placement**: Retail traders place stops just outside the Asian range.
   MMs know where these are.
2. **Liquidity pools**: Stops above Asian high and below Asian low create
   liquidity that MMs will target.
3. **Directional neutrality**: During accumulation, price shows no clear direction.
   Both sides are being built.
4. **Breakout trap**: The first breakout of the Asian range is usually FALSE
   (the stop hunt). The true direction is opposite.

## Asian Mid-Line

The midpoint of the Asian range (`mid = (high + low) / 2`) serves as:
- A magnet level during the return phase
- A target for partial profit (price often returns to mid)
- A reference for measuring how far the stop hunt extended

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| Valid accumulation predicts tradeable day | UNTESTED | Win rate: valid vs invalid range |
| Tighter accumulation → better trades | UNTESTED | Correlate vol_compression with trade RR |
| Asian range thresholds are correct | UNTESTED | Optimize per-pair thresholds from data |
| First Asian breakout is usually false | UNTESTED | Count false vs true first breakouts |
