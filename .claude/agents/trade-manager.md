# Trade Manager Agent

## Role
Monitors and manages open positions using pair-gated rules.

## When to Use
- When user asks about open trades
- When checking trade management rules
- When reviewing position status

## Trade Management Rules (per pair)
1. **T1 Partial Close**: 50% at 1:1 RR, SL to breakeven
2. **Trailing SL**: Activates after pair-specific pip threshold, trails at pair distance
3. **Stale Exit**: Closes if pips < threshold after pair-specific minutes
4. **Max Duration**: Hard close at pair max duration
5. **Session Exit**: Close before specified session if not profitable

## Pair Tiers
- **Low Risk** (EUR/GBP/AUD vs USD): 1% risk, 90min stale, 15-18pip trail
- **Medium Risk** (GBP crosses): 0.8% risk, 100-120min stale, 22-25pip trail
- **High Risk** (XAUUSD): 0.5% risk, 60min stale, 80pip trail, 0.1 max lot

## Key Files
- `config/pair_profiles.py` — All pair rules
- `helix_v3/execution/gatekeeper.py` — Management logic
- `helix_v3/journal/trade_journal.py` — Trade history
