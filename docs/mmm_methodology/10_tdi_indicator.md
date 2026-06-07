# 10 — Traders Dynamic Index (TDI)

## Overview

TDI is the primary confirmation indicator in MMM. It combines RSI with Bollinger
Bands and moving averages to produce actionable signals that confirm stop hunt
completion and trend direction.

## V2-Verified Parameters

These were verified against MT4 indicator inputs on 2026-04-27:

| Component | Parameter | Value |
|-----------|-----------|-------|
| RSI Period | Wilder RSI | 21 (NOT 13) |
| RSI Price Line (Green) | SMA of RSI | 2-period |
| Trade Signal Line (Red) | SMA of RSI | 7-period |
| Market Base Line (Yellow) | SMA of RSI | 34-period |
| Volatility Bands | Bollinger on RSI | Period=34, StdDev=1.6185 |
| Shark Fin Upper | Overbought threshold | 63 (NOT 68) |
| Shark Fin Lower | Oversold threshold | 37 (NOT 32) |
| VB Squeeze Threshold | Band width | < 12 = squeeze |

**Important**: All smoothing uses SMA (rolling mean), NOT EMA. RSI uses Wilder's
smoothing: `ewm(alpha=1/period, adjust=False)`.

## TDI Lines

### Green Line (RSI Price Line)
- 2-period SMA of RSI(21)
- Shows current RSI momentum
- Fastest line — leads crossovers

### Red Line (Trade Signal Line)
- 7-period SMA of RSI(21)
- Smoother than green — filters noise
- Crossovers with green line generate entry signals

### Yellow Line (Market Base Line)
- 34-period SMA of RSI(21)
- Shows the "base" trend direction
- Green crossing yellow = significant momentum shift ("Blood in the Water")

### Volatility Bands (Upper/Lower)
- Bollinger Bands on RSI(21) with period=34 and std=1.6185
- Show RSI volatility range
- Squeeze = accumulation. Expansion = trend move.

## Signal Types

### Signal Cross (Green x Red)
- **Bullish**: Green crosses ABOVE Red → BUY confirmation
- **Bearish**: Green crosses BELOW Red → SELL confirmation
- Uses shift(1) guard to prevent repainting

### Blood in the Water (Green x Yellow / MBL Cross)
- **Bullish**: Green crosses ABOVE Yellow AND Green > Red → Strong BUY
- **Bearish**: Green crosses BELOW Yellow AND Green < Red → Strong SELL
- Higher significance than Signal Cross — confirms momentum shift

### Hook
- Green line re-enters the VB from an extreme (counter-trend)
- **Bullish Hook**: Green was below lower VB, re-enters and RSI < 40
- **Bearish Hook**: Green was above upper VB, re-enters and RSI > 60
- Signals a potential reversal from overbought/oversold

### Shark Fin
- **Key MMM Signal**: RSI broke out of VB then re-entered
- Confirms the stop hunt is complete and reversal is underway
- **Short Shark Fin**: Green was above upper VB (63+), now back inside
- **Long Shark Fin**: Green was below lower VB (37-), now back inside
- Lookback: 6 bars

### VB Squeeze
- VB width < 12 = consolidation (accumulation phase)
- Squeeze confirms Asian session characteristics
- Breakout from squeeze = potential entry signal

### RSI Divergence
- **Bullish**: Price makes lower low, RSI makes higher low
- **Bearish**: Price makes higher high, RSI makes lower high
- Measured over 20-bar lookback, split at midpoint

## TDI Trading Rules

1. **Entry confirmation**: Look for Shark Fin or Blood in the Water in the
   direction of the M/W pattern
2. **VB Squeeze during Asian**: Confirms accumulation is valid
3. **Signal Cross**: Secondary confirmation, use with other signals
4. **Divergence**: Early warning of reversal — look for M/W to form
5. **Hook**: Counter-trend signal — be cautious, use only with strong confluence

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| RSI=21 matches MT4/MT5 output | VALIDATED | Verified 2026-04-27 |
| Shark Fin confirms stop hunt | UNTESTED | Shark Fin → reversal success rate |
| Blood in the Water momentum | UNTESTED | MBL cross → trend continuation |
| VB Squeeze = accumulation | UNTESTED | Squeeze during Asian → trade quality |
| 63/37 thresholds are correct | VALIDATED | Verified from MT4 Inputs dialog |
| Divergence precedes reversal | UNTESTED | Divergence → M/W formation rate |
