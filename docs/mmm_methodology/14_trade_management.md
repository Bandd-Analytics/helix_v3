# 14 — Trade Management

## Overview

Once entered, MMM has strict rules for managing the trade. The core principle:
PROTECT CAPITAL. Never let a winning trade become a loser. Exit losers quickly.

## Stop Loss Placement

### Structural SL
- Place SL behind the structural level that invalidates the trade
- For BUY: SL below the M/W formation low + buffer
- For SELL: SL above the M/W formation high + buffer
- Buffer = pair-specific `sl_buffer_pips` (3-5 pips)

### Minimum SL Floor
- Each pair has a `min_sl_pips` to prevent lot inflation from tight stops
- If structural SL < min_sl_pips, widen to min_sl_pips
- This prevents dangerously large lot sizes from fractional Kelly sizing

| Pair | Min SL | Buffer |
|------|--------|--------|
| EURUSD | 15 pips | 3 pips |
| GBPUSD | 20 pips | 3 pips |
| AUDUSD | 12 pips | 3 pips |
| GBPAUD | 25 pips | 5 pips |
| GBPJPY | 25 pips | 5 pips |
| XAUUSD | 150 pips | 30 pips |

## T1 Partial Close

At 1:1 risk-reward ratio:
1. Close 50% of the position (`partial_close_ratio = 0.50`)
2. Move SL to breakeven on remaining position
3. Let the remainder run with trailing stop

## Trailing Stop

Activates at pair-specific `trail_activation_pips` (when trade is in profit by that amount):
- SL moves to follow price at `trail_distance_pips` behind

| Pair | Activation | Distance |
|------|-----------|----------|
| EURUSD | 15 pips | 12 pips |
| GBPUSD | 20 pips | 15 pips |
| AUDUSD | 12 pips | 10 pips |
| GBPAUD | 30 pips | 22 pips |
| GBPJPY | 25 pips | 18 pips |
| XAUUSD | 100 pips | 80 pips |

## 90-Minute Stale Exit (UNIVERSAL)

This is THE most important trade management rule:

```
IF time_in_trade >= 90 minutes AND profit_pips <= 0:
    → CLOSE IMMEDIATELY (stale exit)
```

- Applies to ALL pairs universally
- If the trade hasn't moved in your direction after 90 minutes, the setup failed
- The M/W formation window is 30-90 minutes — if it hasn't worked by then, exit
- **Exception**: If the trade IS in profit, it stays open and trails

## Max Duration (Hard Cap)

Even profitable trades have a session-based time limit:

| Pair | Max Duration |
|------|-------------|
| Low tier (EUR/GBP/AUD USD) | 240 min (4h) |
| Medium tier (crosses) | 240-300 min (4-5h) |
| XAUUSD | 180 min (3h) |

## Session Exit

```
close_before_session: "ASIAN_EARLY"
```

- Close any position not in profit before Asian session begins
- If in profit, the trailing stop handles exit naturally
- Prevents holding through the low-volatility accumulation phase

## Lot Sizing

Fractional Kelly formula:
```
lot_size = (Equity * Risk%) / (SL_pips * pip_value_per_lot)
```

With constraints:
- Floor: min_sl_pips prevents lot inflation
- Cap: max_lot_size per pair (1.0 low tier, 0.5 medium, 0.1 gold)
- Account-proportional: lot size scales with equity

## Validation Status

| Rule | Status | Notes |
|------|--------|-------|
| 90-min stale exit saves capital | UNTESTED | Compare outcomes: stale exits vs holding |
| T1 at 1:1 RR is optimal | UNTESTED | Test different T1 ratios (0.8, 1.0, 1.2) |
| Trailing stop parameters per pair | UNTESTED | Optimize activation/distance from data |
| Min SL floor prevents lot inflation | UNTESTED | Verify sizing behavior at extremes |
| Session exit protects profits | UNTESTED | Outcomes of positions held into Asian |
