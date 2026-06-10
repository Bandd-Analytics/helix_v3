# RRS Performance Grading

RRS is a setup-performance label used for research segmentation. It does not approve live trades by
itself.

## Labels

| Grade | Favorable Rate | Meaning |
|---|---:|---|
| `R_RUNNER` | `>= 75%` | High favorable-rate setup. Review first for strict promotion. |
| `R_REPEATER` | `>= 50%` and `< 75%` | Repeatable setup that may still carry strong expectancy. |
| `S_STRANGER` | `< 50%` | Low favorable-rate setup. Only interesting when payoff is unusually asymmetric. |

## Why This Exists

The old strict validation-library rebuild used a scanner-derived promotion bar:

```text
Fav >= 85.0% and AvgExit >= +10.9p
```

That is useful as a conservative benchmark, but it is not the same as the actual trading pipeline's
profit model. The pipeline can be profitable with a lower hit rate when average winners are much
larger than average losers. RRS separates these questions:

- How often does the setup move favorably?
- Does the setup have positive expectancy?
- Does it repeat across pairs, sessions, and time splits?
- Is the payoff profile strong enough to justify a lower favorable rate?

## Current Data Basis

The current setup-intelligence report is based on the expanded aligned mining run across:

```text
EURUSD, GBPUSD, GBPJPY, USDJPY, EURJPY, GBPCHF, AUDUSD,
GBPAUD, GBPNZD, EURGBP, XAUUSD, US30, USTEC
```

The intended shared window is `2021-06-08` through `2026-06-08`. The first three 90-day chunks
saved zero qualifying raw setups, so effective qualifying occurrence coverage mostly starts in
2022.

The older `PF 1.35`, `+$686`, `679 trades` result is a separate two-year trading-pipeline
backtest. It should not be treated as the same thing as the strict scanner/promotion baseline.

## Current RRS Findings

From `logs/setup_intelligence.db`, filtering setup rows with `N >= 10`:

| RRS | Setup Rows | Occurrences | Positive-Expectancy Rows | AvgFav | AvgExit | AvgOpp |
|---|---:|---:|---:|---:|---:|---:|
| `R_RUNNER` | 3 | 41 | 3 | 85.6% | +19.1 | 51.4 |
| `R_REPEATER` | 90 | 1,609 | 87 | 55.6% | +31.4 | 40.4 |
| `S_STRANGER` | 1,181 | 24,337 | 395 | 22.5% | -38.1 | 24.0 |

This confirms that the 85% promotion bar is too narrow for discovery. It is still a valid strict
gate, but it misses lower-rate positive-expectancy candidates.

## Expectancy Candidate Layer

The setup-intelligence rebuild now writes a separate `expectancy_candidates` table. This table is
research-only and is not used by `ValidationLibrary.validate_setup`.

Candidate tiers:

| Tier | Meaning |
|---|---|
| `DEMO_CANDIDATE` | Positive expectancy, acceptable profit factor, and at least 2 of 3 chronological splits passing. |
| `WATCH_CANDIDATE` | Positive expectancy, but still needs tighter filtering or more evidence. |
| `ASYMMETRIC_EXCEPTION` | Low favorable-rate, high-payoff setup that may work through fat-tail winners. |

Current expanded-run counts:

| Tier | RRS | Rows | Occurrences | AvgFav | AvgExit | AvgPF |
|---|---|---:|---:|---:|---:|---:|
| `DEMO_CANDIDATE` | `R_RUNNER` | 3 | 41 | 85.6% | +19.1 | 31.41 |
| `DEMO_CANDIDATE` | `R_REPEATER` | 80 | 1,445 | 56.1% | +32.1 | 4.44 |
| `ASYMMETRIC_EXCEPTION` | `S_STRANGER` | 69 | 1,234 | 37.7% | +89.2 | 3.30 |
| `WATCH_CANDIDATE` | `R_REPEATER` | 6 | 113 | 50.6% | +42.2 | 1.85 |
| `WATCH_CANDIDATE` | `S_STRANGER` | 222 | 4,342 | 31.5% | +10.5 | 1.96 |

Review only this layer with:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.setup_intelligence expectancy-report --limit 50
```

The scanner watchlist displays these fields as historical context when a current scanner candidate
has a matching symbol/direction setup. This does not change entry eligibility; strict
`validation_setups` matches are still required for `PROMOTED_ENTRY`.

## Promotion Direction

The next promotion mode should be expectancy-led:

- Keep RRS as a descriptive band.
- Require minimum sample size.
- Require positive average exit.
- Add profit factor or payoff ratio.
- Require acceptable adverse excursion and drawdown behavior.
- Require train/validation/out-of-sample stability.
- Treat XAUUSD, US30, and USTEC candidates as research-only until point/pip calibration is audited.

Live gating should remain off until these candidates survive replay, visual flashcard audit, and
demo/watchdog validation.
