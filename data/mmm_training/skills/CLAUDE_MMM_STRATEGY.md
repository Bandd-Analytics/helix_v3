# Claude MMM Strategy Skill

Status: draft. No training-derived rule is promoted for live enforcement yet.

## Claude Role

- Review Steve Mauro methodology notes for chart-structure meaning and missing MMM context.
- Challenge Codex-generated detectors when they simplify discretionary concepts too far.
- Help refine visual pattern descriptions for M/W, stop hunt, TDI shark-fin, HOD/LOD, session, and pivot-map context.
- Keep methodology summaries paraphrased and timestamped; do not recreate full course transcripts.
- Do not treat training material as market truth without replay evidence.

## Operating Rules

- Use MMM top-down context: Weekly/D1/H4 -> H1 -> M15.
- Pair behavior is unique until cross-pair convergence is proven.
- Prefer exact setup parameters: timeframe, session, range, liquidity level, entry confirmation, invalidation, and exit logic.
- Require market replay before a teaching becomes a strategy rule.
- Keep live execution out of the training-review loop.

## Current Validation State

Source report: `data/mmm_training/validation/taught_rule_validation_report.md`.
Pair research archive: `data/mmm_training/pair_research/INDEX.md`.
Vision review packets: `data/mmm_training/vision_review_packets/INDEX.md`.

- Promoted training-derived taught rules: none.
- Scanner baseline gate: 90m baseline currently reports N=100, Fav=85.0%, AvgExit=+10.9p.
- Watchlist only: `MMM-TRAIN-004` on GBPJPY, AUDUSD, USDJPY, and low-sample EURJPY; `MMM-TRAIN-002` on GBPJPY is weak pair-specific evidence.
- `MMM-TRAIN-003` and `MMM-TRAIN-006` underperform as naive detectors and should be treated as unproven until refined.
- `MMM-TRAIN-005` needs a dedicated pivot/day-map interpretation before Codex can backtest it properly.
- Dense historical pair research currently leaves GBPJPY BUY W-bottom early-week L3 variants and one EURJPY BUY W-bottom early-week L3 true-trend variant as research-only review candidates.
- No researched pair has a repeated setup signature that beats the scanner baseline gate with split confirmation.
- The strict validation library currently has 0 promoted records.
- Winner-vs-loser chart packets are ready for paid-account ChatGPT/Claude review.

## Next Claude Review Work

- Review the GBPJPY and EURJPY profitable flashcard archives for visual commonality before Codex hardens their filters.
- Use the packet `blind_prompt.md` first, then `labeled_comparison_prompt.md` with `answer_key.csv`.
- Review the `MMM-TRAIN-004` source windows and clarify the required visual order: Asian box, stop hunt, TDI band excursion, return inside, M/W confirmation, and entry close.
- Review `MMM-TRAIN-005` for exact M3/M1 day-map rules and invalidation conditions.
- Identify where the taught setup depends on discretionary chart geometry that cannot be captured by price-only OHLC detectors.
- Produce concise rule refinements for Codex to encode and replay.
