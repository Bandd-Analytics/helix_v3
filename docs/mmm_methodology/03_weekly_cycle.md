# 03 — Weekly Cycle Structure

## Overview

The weekly cycle overlays the 3-day cycle. Each week has a predictable rhythm
that influences when stop hunts and trend moves occur.

## Weekly Phases

### Early Week (Sunday evening - Monday)
- **Character**: Initial direction established
- **Action**: Market sets up the week's first move. Often continues Friday's direction.
- **Trading**: Observe, identify weekly open range. Limited entries.

### Mid-Week Reversal (Tuesday - Wednesday)
- **Character**: The primary reversal zone of the week
- **Action**: If early week moved UP, expect mid-week reversal DOWN (and vice versa).
- **Trading**: Best entries of the week. Mid-week reversal setups have highest confluence.
- **Score bonus**: +10 confluence points when mid-week reversal expected

### Late Week (Thursday - Friday)
- **Character**: Continuation of mid-week reversal OR distribution
- **Action**: Profit taking. MMs closing positions. Reduced volatility by Friday afternoon.
- **Trading**: Trade early Thursday. Avoid new entries after Friday London close.

### Weekend
- **Character**: Market closed. Gap risk on Sunday open.
- **Action**: No trading. Close any remaining positions before weekend.

## Weekly Open Range

First 4 hours of the new trading week (Monday 00:00-04:00 UTC):
- Defines the initial range, similar to Asian range but for the whole week
- Breakout above/below weekly open range signals directional bias
- Measured in the orchestrator as the first 16 M15 bars on Monday

## Implementation

From `mtf_analyzer.py`:
```python
weekday = now_utc().weekday()
if weekday in (6, 0):      # Sun-Mon → EARLY_WEEK
elif weekday in (1, 2):     # Tue-Wed → MID_WEEK_REVERSAL
elif weekday in (3, 4):     # Thu-Fri → LATE_WEEK
```

## D1 EMA Stack for Weekly Bias

On the daily chart, compute EMAs 5/13/50/200 to determine overall weekly bias:
- All EMAs stacked bullish (5 > 13 > 50 > 200) → Weekly BUY bias
- All EMAs stacked bearish → Weekly SELL bias
- Mixed → NEUTRAL — reduce position size

## Peak Detection on Weekly

From D1 data (last 10 trading days):
- Find highest high → days_since_peak_high
- Find lowest low → days_since_peak_low
- If closer to peak high → trend is SELL (coming down from top)
- If closer to peak low → trend is BUY (coming up from bottom)

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| Mid-week reversal frequency | UNTESTED | Count Tue/Wed reversals vs other days |
| Early week direction persistence | UNTESTED | Does Monday direction predict the week? |
| Weekly open range breakout reliability | UNTESTED | Measure post-breakout continuation |
| Late week reduced volatility | UNTESTED | Compare ADR by day of week |
