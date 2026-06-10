# Aligned Mining Progress

Universe:

`EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC`

Target period: `2021-06-08` through `2026-06-08`

Confirmed raw chunk saves: `36,054`

Post-rebuild setup intelligence:

- Occurrences: `54,075`
- Setup stats: `13,441`
- Price-level stats: `127`
- Day/session stats: `438`
- Cross-pair stats: `2,345`
- Strict validation-library records: `1`

RRS performance grading was added after the strict rebuild. For setup rows with `N >= 10`:

- `R_RUNNER`: `3` setup rows, `41` occurrences, `3` positive-expectancy rows, AvgFav `85.6%`, AvgExit `+19.1`.
- `R_REPEATER`: `90` setup rows, `1,609` occurrences, `87` positive-expectancy rows, AvgFav `55.6%`, AvgExit `+31.4`.
- `S_STRANGER`: `1,181` setup rows, `24,337` occurrences, `395` positive-expectancy rows, AvgFav `22.5%`, AvgExit `-38.1`.

RRS is analysis-only. It exposes lower favorable-rate exceptions that the strict `85%` scanner
promotion gate misses; it is not a live-trade approval.

Expectancy-led research candidates were added after RRS. The rebuild produced `380` research-only
candidates:

- `DEMO_CANDIDATE` / `R_RUNNER`: `3` rows, `41` occurrences, AvgFav `85.6%`, AvgExit `+19.1`, AvgPF `31.41`.
- `DEMO_CANDIDATE` / `R_REPEATER`: `80` rows, `1,445` occurrences, AvgFav `56.1%`, AvgExit `+32.1`, AvgPF `4.44`.
- `ASYMMETRIC_EXCEPTION` / `S_STRANGER`: `69` rows, `1,234` occurrences, AvgFav `37.7%`, AvgExit `+89.2`, AvgPF `3.30`.
- `WATCH_CANDIDATE` / `R_REPEATER`: `6` rows, `113` occurrences, AvgFav `50.6%`, AvgExit `+42.2`, AvgPF `1.85`.
- `WATCH_CANDIDATE` / `S_STRANGER`: `222` rows, `4,342` occurrences, AvgFav `31.5%`, AvgExit `+10.5`, AvgPF `1.96`.

These records live in `logs/setup_intelligence.db`, table `expectancy_candidates`, and can be
reviewed with:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.setup_intelligence expectancy-report --limit 50
```

Instrument calibration and visual-packet follow-up:

- `XAUUSD`: MT5 metadata resolved `pip_size=0.01`, `pip_value_per_lot=1.00`, and 26 research
  candidates in setup intelligence (`8` demo, `18` asymmetric). Aggregate XAUUSD replay remains
  negative, so only exact high-expectancy setup packets should be reviewed.
- `US30` and `USTEC`: MT5 metadata resolved `pip_size=0.01`, but contract-value/risk handling is
  still execution-blocked.
- Five XAUUSD winner-vs-loser packet folders were built under `vision_review_packets/`.
  A targeted chart-path backfill rendered 61 historical PNGs; all five XAUUSD packet folders now
  have `Items == Images` and `Missing == 0`.
- Account-CLI packet reviews completed for all five XAUUSD folders:
  - RRT BUY mid-week L3 accumulation: Codex `7/11`, Claude `4/11`.
  - RRT SELL early-week L0 return accumulation: Codex `7/15`, Claude `7/15`.
  - RRT SELL mid-week L0 return accumulation: Codex `10/13`, Claude `7/13`.
  - THE_33 M/W BUY mid-week L3 stop-hunt with RRT/TDI confirm: Codex `6/11`, Claude `8/11`.
  - THE_33 M/W BUY mid-week L3 stop-hunt without RRT/TDI: Codex `6/11`, Claude `8/11`.
  These reviews are hypothesis sources only; deterministic replay and OOS split validation remain
  required before any promotion.
- XAUUSD OHLC feature backfill completed for 7,788 historical flashcards. Packet and pair-level
  feature ablations were regenerated. The strongest pair-level result is
  `RRT_REVERSAL|BUY|MID_WEEK|L3|ACCUMULATION|...|TDI_CONFIRM|THE_33|CONF_75_PLUS` filtered by
  `ratio_le_2_asian_gte_30_tdi_positive`, keeping 5 cases at `100.0%` Fav and `+770.4p` AvgExit.
  It has only 1 split pass, so it remains `research_only_split_fail`.
- RRS-aware ablation reporting added and regenerated for packet-level and all 13 pair-level
  research scopes. Reports now show base/filtered RRS, PF, payoff ratio, scanner-baseline split
  passes, and expectancy split passes.
- Alert-only basket report generated at `setup_intelligence/ALERT_ONLY_BASKET.md`. It ranks
  expectancy candidates by tier, RRS, split passes, PF, payoff, AvgExit, and sample size, while
  marking non-tradeable pair profiles as `RESEARCH_ONLY`.
- Scanner watchlist basket gating added. With `--require-alert-basket`, candidates without a
  ranked basket match are blocked before alerting. The 2026-06-09 19:33 EAT stored-snapshot run
  found basket context for GBPNZD (`#2 RESEARCH_ONLY`) and GBPAUD (`#13 DEMO_ALERT`), but 0
  promoted/watch-only candidates after readiness, age, and strict validation gates.

| Chunk | Window End | Days | Status | Saved |
|---:|---|---:|---|---:|
| 1 | 2021-09-06 | 90 | complete | 0 |
| 2 | 2021-12-05 | 90 | complete | 0 |
| 3 | 2022-03-05 | 90 | complete | 0 |
| 4 | 2022-06-03 | 90 | complete | 548 |
| 5 | 2022-09-01 | 90 | complete | 1814 |
| 6 | 2022-11-30 | 90 | complete | 1547 |
| 7 | 2023-02-28 | 90 | complete | 140 |
| 8 | 2023-05-29 | 90 | complete | 102 |
| 9 | 2023-08-27 | 90 | complete | 150 |
| 10 | 2023-11-25 | 90 | complete | 99 |
| 11 | 2024-02-23 | 90 | complete | 220 |
| 12 | 2024-05-23 | 90 | complete | 228 |
| 13 | 2024-08-21 | 90 | complete | 3276 |
| 14 | 2024-11-19 | 90 | complete | 2680 |
| 15 | 2025-02-17 | 90 | complete | 2580 |
| 16 | 2025-05-18 | 90 | complete | 2071 |
| 17 | 2025-08-16 | 90 | complete | 2974 |
| 18 | 2025-11-14 | 90 | complete | 5796 |
| 19 | 2026-02-12 | 90 | complete | 5210 |
| 20 | 2026-05-13 | 90 | complete | 4714 |
| 21 | 2026-06-08 | 26 | complete | 1905 |
