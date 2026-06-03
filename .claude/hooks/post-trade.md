# Post-Trade Hook

## Trigger
After any order fills, partial close, or position exit.

## Actions
1. Record to trade journal (75 fields including full context)
2. Send WhatsApp notification (entry/T1/exit report)
3. Sync journal with MT5 deal history
4. Update active orders tracking
