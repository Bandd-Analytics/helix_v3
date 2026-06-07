# MMM Training vs Market Reality Validation Plan

Every extracted teaching must pass through this validation layer before it becomes a strategy skill rule.

## Validation Gates

1. Source reference exists: video ID and timestamp.
2. Rule is parameterized: timeframe, setup, entry, exit, invalidation.
3. Rule maps to flashcard fields and MMM replay signature components.
4. Backtest sample is pair-specific first.
5. Cross-pair convergence is considered only after pair-specific evidence.
6. Rule is promoted only if replay outcomes beat the scanner baseline.

## Metrics

- favorable rate
- T1 hit rate
- average exit pips
- average MFE/MAE
- stale-exit rate
- ambiguity rate
- pair-specific sample size

## Decisions

- `validated`: promote to skill docs and validation library.
- `watch`: keep for more samples.
- `rejected`: keep as training-only context, not live logic.

