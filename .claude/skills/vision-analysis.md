# Vision Analysis Skill

## Description
Analyze MMM chart images for structural patterns. Used when Claude Code acts as the vision engine in `local` consensus mode.

## Input
- 1024x1024 PNG chart with candlesticks and color-coded EMAs
- Dark background, no text labels or gridlines

## Analysis Checklist
1. **EMA Stack Order**: Which EMAs are above/below price?
2. **M/W Formations**: Geometric peaks or troughs at extremes?
3. **Railroad Tracks**: Opposing candles of similar size near 50/200 EMA?
4. **Pin Bars**: Long wicks rejecting off key EMAs?
5. **Cycle Level**: Count pushes from 800 EMA (1, 2, or 3)
6. **Direction**: Based on stack + structure = BUY/SELL/NEUTRAL
7. **Confidence**: 0.0-1.0 based on clarity of signal

## Confidence Guidelines
- 0.90+: Perfect setup, clear structure, all confirmations
- 0.85-0.89: Strong setup, minor conflicting signals
- 0.75-0.84: Moderate setup, mixed signals
- Below 0.75: Weak/neutral, do not enter
