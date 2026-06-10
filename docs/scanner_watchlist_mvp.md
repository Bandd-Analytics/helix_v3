# Scanner Watchlist MVP

This is the production-safe first step for Helix V3: scanner-first, alert-only, and gated by
the validation library. It also reads the offline setup-intelligence database when available, so
watchlist rows can show the best historical all-pair setup context without relaxing the entry gate.

It does not place, modify, or close MT5 trades. It reads stored scanner snapshots from
`logs/market_scanner.db`, checks readiness/risk gates, and prints or sends a watchlist report.

## Run

Console only:

```powershell
.venv\Scripts\python.exe -m helix_v3.scanner.watchlist --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC
```

Send through the configured `NOTIFICATION_BACKEND`:

```powershell
.venv\Scripts\python.exe -m helix_v3.scanner.watchlist --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC --notify
```

Show blocked candidates while tuning gates:

```powershell
.venv\Scripts\python.exe -m helix_v3.scanner.watchlist --symbols EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC --include-blocked
```

Refresh the historical intelligence layer before using the watchdog report for supervised review:

```powershell
.venv\Scripts\python.exe -m helix_v3.backtest.setup_intelligence rebuild
```

## Gate Meaning

- `PROMOTED_ENTRY`: scanner candidate passed readiness/risk gates and matched a promoted
  validation-library record.
- `WATCH_ONLY`: scanner candidate is interesting, but it is not allowed to be treated as an entry.
- `BLOCKED`: readiness, age, spread, direction, pair profile, or stop-hunt requirements failed.

Default behavior requires an exact promoted setup signature. Current scanner rows usually do not
contain that signature, so the safe default is watch-only until promoted setup data is wired in.
When `logs/setup_intelligence.db` exists, watch-only rows include the strongest historical
symbol/direction match with recurrence, profitability, price-level, day, and session context.
The report hides historical context below the default sample floor of N=10 to avoid over-weighting
single-event coincidences.

The CLI has an explicit looser mode:

```powershell
.venv\Scripts\python.exe -m helix_v3.scanner.watchlist --symbols GBPJPY --allow-symbol-direction-promotion
```

Use that only for supervised research. It allows symbol/direction validation records without an
exact setup-key match.

## Recommended Operating Mode

1. Keep live orchestrator and order execution off.
2. Populate scanner snapshots using the existing scanner/report workflow.
3. Rebuild setup intelligence from historical flashcards and MMM event outcomes.
4. Run this watchlist across the full research universe.
5. Track 20-50 watchlist alerts manually in demo or paper trading.
6. Promote nothing until the validation library contains split-stable records that beat the scanner
   baseline.

Current project state: the expanded historical archive has one strict promoted GBPJPY BUY setup
with small sample size. Treat it as supervised demo/watchdog material, not live auto-entry approval.
