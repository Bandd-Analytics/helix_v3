# 11 — Pivot Points and Day-Type Prediction

## Overview

MMM uses standard pivot points with additional mid-pivots (M1-M4) to identify
expected price zones for HOD/LOD. The previous day's candle color predicts which
mid-pivot zone to target.

## Pivot Calculation

From previous day's High (H), Low (L), Close (C):

```
PP = (H + L + C) / 3

R1 = 2 * PP - L
R2 = PP + (H - L)
R3 = H + 2 * (PP - L)

S1 = 2 * PP - H
S2 = PP - (H - L)
S3 = L - 2 * (H - PP)
```

## MMM Mid-Pivots (Book pp. 42-43)

```
M1 = (S2 + S1) / 2
M2 = (S1 + PP) / 2
M3 = (PP + R1) / 2
M4 = (R1 + R2) / 2
```

These mid-pivots define the expected HOD/LOD zones based on day type.

## Day-Type Prediction

Based on previous day's candle:

### Red Prior Candle → M1/M3 Day
- HOD expected between S2/S1 (M1 zone) or PP/R1 (M3 zone)
- Bearish continuation from previous day

### Green Prior Candle → M2/M4 Day
- HOD expected between S1/PP (M2 zone) or R1/R2 (M4 zone)
- Bullish continuation from previous day

```python
day_type = "M2_M4" if prev_candle_bullish else "M1_M3"
```

## Using Pivots in Trading

1. **Entry zones**: Enter near S1/S2 for buys, R1/R2 for sells
2. **Target levels**: Use opposite pivots as TP targets
3. **Confluence**: Pivot levels that align with Asian range boundaries or
   M/W pattern levels add confidence
4. **Day type**: If day type says M3 day, look for HOD around PP-R1 zone

## ADR Marker

From `tdi.py` — Wilder ATR(14) based:

```
ADR = Wilder_ATR(14) on daily bars
Marker_High = today_open + ADR/2
Marker_Low = today_open - ADR/2
```

ADR defines the expected range for the day. Price approaching marker_high/low
suggests the daily range is nearly exhausted.

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| M1/M3 vs M2/M4 day type accuracy | UNTESTED | Backtest candle color → next day HOD zone |
| Pivot levels as S/R | UNTESTED | How often does price react at pivots? |
| Mid-pivots add precision | UNTESTED | Compare mid-pivot accuracy vs standard |
| ADR marker bounds the day | UNTESTED | How often does price stay within ADR? |
