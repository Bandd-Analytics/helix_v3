# 04 — Session Structure

## Overview

Per MMM Book p.8, the trading day is divided into distinct sessions. Each session
has a specific role in the market maker cycle. Understanding which session you're
in determines what price action to expect.

## Session Boundaries (GMT)

| Session | GMT Start | GMT End | Role |
|---------|-----------|---------|------|
| Dead Gap | 22:00 | 01:30 | No trading. Day reset at 22:00 GMT (17:00 ET) |
| Asia | 00:30 | 07:30 | Accumulation. Tight range. Building positions. |
| London Gap | 07:00 | 08:00 | Changeover zone. Stop hunts likely here. |
| London | 07:30 | 13:30 | True trend session. Biggest moves. |
| NY Gap | 13:00 | 14:00 | Changeover zone. NYC reversal setups. |
| US/NYC | 13:30 | 22:00 | NYC reversal, then distribution. |

## Session Phases (MMM Cycle)

### 1. Accumulation (Asian Session)
- **Time**: 00:30-07:30 GMT (03:30-10:30 EAT)
- **What happens**: MMs trade in circles, building positions. Price stays in a
  tight range ("Asian box").
- **What to look for**: Range width. Valid accumulation = range < pair-specific max
  (e.g., < 50 pips for GBPUSD, < 40 pips for EURUSD)
- **Trading**: DO NOT trade. Mark the range. Wait.

### 2. Stop Hunt (London Gap / Early London)
- **Time**: 07:00-10:00 GMT approximately
- **What happens**: MMs spike price beyond the Asian range to trigger retail stops.
  Typically 25-50 pips beyond Asian high or low (pair-dependent).
- **What to look for**: Breach of Asian boundary with 1-3 pushes. Spike candles.
  Pin bars at extremes.
- **Trading**: DO NOT trade yet. Wait for reversal confirmation (M/W, RRT).

### 3. True Trend (London Session)
- **Time**: 08:00-13:30 GMT
- **What happens**: After the stop hunt completes, price reverses and runs in the
  true direction. This is the main move of the day.
- **What to look for**: M/W formation confirms direction. RRT at the extreme.
  TDI confirms with Shark Fin or Blood in the Water.
- **Trading**: PRIMARY ENTRY WINDOW. Enter after confirmation.

### 4. NYC Reversal (NY Gap / Early NYC)
- **Time**: 13:00-17:00 GMT
- **What happens**: Price may reverse the London move (partial retrace) or
  continue if momentum is strong.
- **What to look for**: Reversal at NYC open. New M/W opposite to London direction.
- **Trading**: Secondary entry window. Only if London move was strong and
  reversal is clear.

### 5. Return to Accumulation (Late NYC)
- **Time**: 17:00-22:00 GMT
- **What happens**: Distribution. MMs taking profit. Price drifts back toward
  center of the day's range.
- **Trading**: EXIT existing positions. No new entries.

## Session in H1 Analysis

From `mtf_analyzer.py`:
```python
hour_utc = now_utc().hour
if 1 <= hour_utc < 5:    ACCUMULATION
if 5 <= hour_utc < 8:    STOP_HUNT
if 8 <= hour_utc < 13:   TRUE_TREND      # Best entry window
if 13 <= hour_utc < 17:  NYC_REVERSAL
else:                     RETURN_TO_ACCUM  # No new entries
```

## HOD/LOD Locking

- **HOD (High of Day)**: Locked when the stop hunt high has been made and price
  reversed. Confirmed when recent 3 H1 bars are below the HOD.
- **LOD (Low of Day)**: Locked when stop hunt low confirmed. Recent bars above LOD.
- Locked HOD/LOD adds +5 confluence points (confirms stop hunt completion).

## Session Exit Rule

From `pair_profiles.py`:
- `close_before_session: "ASIAN_EARLY"` — Close any position not in profit before
  the Asian session begins. If in profit, the trailing stop handles it.

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| Asian session is accumulation | UNTESTED | Measure Asian range vs ADR ratio |
| Stop hunt occurs at London Gap | UNTESTED | Time distribution of Asian breaches |
| True trend is London session | UNTESTED | Largest move by session analysis |
| NYC reversal frequency | UNTESTED | How often does NYC reverse London? |
| Late NYC is distribution | UNTESTED | Reduced volatility confirmation |
