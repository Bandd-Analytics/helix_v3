# Codex MMM Strategy Skill

Status: draft. No training-derived rule is promoted for live enforcement yet.

## Codex Role

- Build deterministic extractors, validators, replay reports, and flashcard mining tools.
- Convert taught MMM ideas into timestamped, paraphrased, testable rule cards.
- Validate every rule against historical OHLC before it can affect scanner, advisory, or execution logic.
- Preserve pair-specific evidence first; only create cross-pair convergence rules after replay proves them.
- Treat scanner baseline as the minimum promotion gate.

## Operating Rules

- Use MMM top-down context: Weekly/D1/H4 -> H1 -> M15.
- Use M15 as the execution replay surface unless a candidate rule explicitly concerns exits, D1/H1 day maps, or higher-timeframe context.
- Store setup evidence as flashcards with chart path, timestamp, rule ID, pair, direction, entry, invalidation, and outcome.
- Do not accept training claims as rules until historical replay supports them.
- Do not place or modify live trades from this training workflow.

## Current Validation State

Source report: `data/mmm_training/validation/taught_rule_validation_report.md`.
Pair research archive: `data/mmm_training/pair_research/INDEX.md`.
Vision review packets: `data/mmm_training/vision_review_packets/INDEX.md`.

- Promoted training-derived taught rules: none.
- Scanner baseline gate: 90m baseline currently reports N=100, Fav=85.0%, AvgExit=+10.9p.
- First-pass taught-rule detectors do not beat the scanner baseline.
- Watchlist only: `MMM-TRAIN-004` on GBPJPY, AUDUSD, USDJPY, and low-sample EURJPY; `MMM-TRAIN-002` on GBPJPY is weak pair-specific evidence.
- Needs stricter filters before reuse: `MMM-TRAIN-003`, `MMM-TRAIN-006`, and all weak pair variants.
- Not yet directly validated: `MMM-TRAIN-001`, `MMM-TRAIN-005`, `MMM-TRAIN-007`, `MMM-TRAIN-008`.
- Dense 3-year pair study archived 8,178 historical flashcards and 2,159 direct-profit examples.
- No mined setup currently beats the scanner baseline gate of Fav >= 85.0%, AvgExit >= +10.9p, and two split confirmations.
- Research-only mined setups: GBPJPY BUY W-bottom early-week L3 variants and one EURJPY BUY W-bottom early-week L3 true-trend variant.
- The strict validation library rebuild currently leaves 0 promoted records.
- Winner-vs-loser chart packets are ready for paid-account ChatGPT/Claude review.

## Next Codex Work

- Treat pair-research setup records as validation candidates, not live rules; the active validation library is intentionally empty until a setup beats the scanner baseline.
- Tighten `MMM-TRAIN-004` and the GBPJPY/EURJPY research candidates with pair-specific Asian range, session, return-inside, M/W confirmation, and TDI filters.
- Convert agreed vision-review findings into deterministic filters and replay them before promotion.
- Build a pivot/day-map validator for `MMM-TRAIN-005`.
- Export annotated validation flashcards only for candidates that survive pair-specific replay.
- Promote rules into the validation library only after sample size, favorable rate, T1 rate, average exit, and scanner-baseline comparison pass.
