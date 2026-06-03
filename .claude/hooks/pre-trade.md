# Pre-Trade Hook

## Trigger
Before any order is sent to MT5.

## Checks
1. Drawdown circuit breaker (equity vs balance)
2. Position limit (max concurrent positions)
3. Pair-specific spread check
4. Pair-specific lot size validation
5. Risk tier verification

## Block Conditions
- Drawdown >= 8%
- Positions >= 3
- Spread > pair max spread
- Market closed
- AutoTrading disabled in MT5
