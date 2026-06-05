# Vision Analysis Skill

## Description
Analyze MMM chart images for structural patterns. Used when Claude Code acts as the vision engine in `local` consensus mode.

## Input
- 1024x1024 PNG chart with candlesticks and color-coded EMAs
- Dark background, no text labels or gridlines

## Analysis Checklist
1. **EMA Stack Order**: Which EMAs are above/below price? (5-Red, 13-Yellow, 50-Aqua, 200-Magenta, 800-White)
2. **M/W Formations**: W-bottom = BUY (double trough). M-top = SELL (double peak). This is the PRIMARY direction signal.
3. **Railroad Tracks (RRT)**: Opposing candles of similar size near 50/200 EMA? Compressed M/W.
4. **Pin Bars**: Long wicks rejecting off key EMAs?
5. **Cycle Level**: Count pushes from 800 EMA (1, 2, or 3). L3 = exhaustion/reversal zone.
6. **Stop Hunt**: Price spiked beyond Asian range then reversed? Even 1-5 pip breach counts if M/W confirms.
7. **TDI Confirmation**: RSI(21) position, Shark Fin, Blood in the Water, VB Squeeze.
8. **Direction**: M/W pattern determines direction. W=BUY, M=SELL. Stop hunt side does NOT override M/W.
9. **Confidence**: 0.0-1.0 based on clarity of signal.

## Direction Rules (CRITICAL)
- W-bottom detected → direction = BUY (market makers hunted lows, true trend is up)
- M-top detected → direction = SELL (market makers hunted highs, true trend is down)
- The stop hunt confirms liquidity grab but does NOT determine direction
- If M/W says BUY but breach was above Asian high → the breach was the fake move, M/W is the real signal

## TDI Signals (V2-Verified Parameters)
- RSI Period = 21 (NOT 13)
- Signal Line = 7-period SMA (NOT 2)
- Shark Fin levels = 63/37 (NOT 68/32)
- VB Squeeze = accumulation/breakout pending
- Shark Fin Short: RSI broke above VB then re-entered = sell confirmation
- Shark Fin Long: RSI broke below VB then re-entered = buy confirmation
- Blood in the Water: RSI crosses market baseline after shark fin = entry

## Confidence Guidelines
- 0.90+: Perfect setup, M/W clear, all TFs aligned, TDI confirms
- 0.85-0.89: Strong setup, minor conflicting signals (1 TF disagrees)
- 0.75-0.84: Moderate setup, weekly or H4 conflicts
- Below 0.75: Weak/neutral, do not enter

## Context Matters
- Patterns at HOD/LOD are significant. Same pattern mid-trend is meaningless.
- Late week (Thu/Fri) setups are lower probability — profit taking phase.
- A hammer at the Asian low has significance. A hammer in the middle of London trend run does not.