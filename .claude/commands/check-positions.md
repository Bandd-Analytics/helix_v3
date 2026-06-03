# /check-positions

Check all open Helix positions and evaluate trade management rules.

## Usage
```
/check-positions
```

## What it does
1. Connects to MT5
2. Lists all open positions with magic number 314159
3. Shows current P&L, duration, distance to SL/TP
4. Evaluates pair-specific management rules:
   - Stale trade check (per-pair threshold)
   - Max duration check
   - Trailing SL status
   - T1 proximity
5. Reports what actions would be taken
