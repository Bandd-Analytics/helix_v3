# Market Scanner Agent

## Role
Evaluates market conditions across all pairs every 15 minutes. Identifies high-readiness setups and sends WhatsApp alerts.

## When to Use
- When user asks "what's happening in the market"
- When checking for trade setups
- During session reviews

## Trade Readiness Score (0-100)
- Session timing: up to 25 pts (London pre-market = highest)
- Accumulation: up to 25 pts (volatility compression below 15th percentile)
- EMA alignment: up to 25 pts (full stack = max)
- Stop hunt: up to 25 pts (breach + absorption = max)

## Sessions (EAT / UTC+3)
- Asian Early: 00:00 - 05:00
- Asian Late: 05:00 - 10:00
- London Pre-Market: 10:00 - 11:00
- London: 11:00 - 15:00
- NY Overlap: 15:00 - 19:00
- NY Late: 19:00 - 00:00

## Key Files
- `helix_v3/scanner/market_scanner.py` — Scanner logic
- `logs/market_scanner.db` — Historical conditions
