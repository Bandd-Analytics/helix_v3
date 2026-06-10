# Aligned Data Mining Plan

The full research universe is:

`EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC`

The previous 7-pair scope came from the old `DEFAULT_RESEARCH_SYMBOLS` constant. `GBPAUD`,
`GBPNZD`, and `XAUUSD` already had profiles but were omitted from that default. `EURGBP`, `US30`,
and `USTEC` now have analysis-only profiles so they do not fall back to generic FX assumptions.

MT5 symbol availability was checked on 2026-06-08. All 13 requested symbols were recognized and
selectable. `US30` and `USTEC` were initially not visible in Market Watch but `symbol_select`
succeeded.

## Shared Period

Every instrument must be mined against the same calendar window:

`2021-06-08` through `2026-06-08`

Use the chunk runner instead of one giant 5-year command:

```powershell
.\scripts\run_aligned_mining_chunks.ps1
```

Preview without running MT5 mining:

```powershell
.\scripts\run_aligned_mining_chunks.ps1 -DryRun
```

Raw mining defaults to `--no-charts` to keep the full-universe run tractable. Generate visual
flashcards later for promoted, high-opportunity, or audited setup groups.

## Chunk Windows

Each chunk runs all symbols over the same period before moving to the next period.

| Chunk | Start | End | Days |
|---:|---|---|---:|
| 1 | 2021-06-08 | 2021-09-06 | 90 |
| 2 | 2021-09-06 | 2021-12-05 | 90 |
| 3 | 2021-12-05 | 2022-03-05 | 90 |
| 4 | 2022-03-05 | 2022-06-03 | 90 |
| 5 | 2022-06-03 | 2022-09-01 | 90 |
| 6 | 2022-09-01 | 2022-11-30 | 90 |
| 7 | 2022-11-30 | 2023-02-28 | 90 |
| 8 | 2023-02-28 | 2023-05-29 | 90 |
| 9 | 2023-05-29 | 2023-08-27 | 90 |
| 10 | 2023-08-27 | 2023-11-25 | 90 |
| 11 | 2023-11-25 | 2024-02-23 | 90 |
| 12 | 2024-02-23 | 2024-05-23 | 90 |
| 13 | 2024-05-23 | 2024-08-21 | 90 |
| 14 | 2024-08-21 | 2024-11-19 | 90 |
| 15 | 2024-11-19 | 2025-02-17 | 90 |
| 16 | 2025-02-17 | 2025-05-18 | 90 |
| 17 | 2025-05-18 | 2025-08-16 | 90 |
| 18 | 2025-08-16 | 2025-11-14 | 90 |
| 19 | 2025-11-14 | 2026-02-12 | 90 |
| 20 | 2026-02-12 | 2026-05-13 | 90 |
| 21 | 2026-05-13 | 2026-06-08 | 26 |

## Final Rebuilds

After all chunks finish, the script rebuilds the full-period archive, validation library, and setup
intelligence:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.historical_flashcard_miner pair-study --archive-only --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC --days 1826 --until 2026-06-08 --min-total 10 --min-favorable-rate 55 --min-avg-exit-pips 0 --baseline-favorable-rate 85 --baseline-avg-exit-pips 10.9 --split-min-total 3 --required-split-passes 2 --validation-days 365 --out-of-sample-days 180 --max-examples 150
.venv\Scripts\python.exe -m helix_v3.backtest.validation_library rebuild --min-total 10 --min-favorable-rate 85 --min-avg-exit-pips 10.9 --min-symbols 2
.venv\Scripts\python.exe -m helix_v3.backtest.setup_intelligence rebuild
```
