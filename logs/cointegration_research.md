# Edge Hunt Track 3d — Cointegration / relative-value (first-pass diagnostic)

Pre-registration: `docs/EDGE_3D_COINTEGRATION.md`. D1 bars, in-sample < 2025-01-01, embargoed holdout after. Engle-Granger ADF gate at 5% crit -3.34 (MacKinnon, N=2, const). Cost = two-leg round-trip spread (rel_A + |beta|*rel_B); gross = 2.0*sigma_spread.

Spread/σ/gross/cost are in **return units (bps = 1e-4)**.

**ADVANCE to simulation: 0** (cointegrated in BOTH windows AND gross > cost).

| pair | n_in | n_hold | beta | half_life(bars) | sigma(bps) | ADF_in | coint_in | ADF_hold | coint_hold | gross(bps) | cost(bps) | gross/cost | verdict |
|---|--:|--:|--:|--:|--:|--:|:-:|--:|:-:|--:|--:|--:|---|
| AUDUSD/NZDUSD | 1222 | 378 | +0.844 | 28.8 | 144 | -4.23 | Y | 0.21 | n | 288 | 0 | 664.24 | DEAD_COINT |
| EURUSD/GBPUSD | 1222 | 378 | +0.925 | 73.3 | 240 | -2.17 | n | -2.30 | n | 481 | 0 | 6740.75 | DEAD_COINT |
| USDCHF/EURUSD | 1222 | 378 | -0.221 | 92.1 | 349 | -2.35 | n | -2.09 | n | 697 | 0 | 3149.24 | DEAD_COINT |
| XAUUSD/XAGUSD | 1224 | 376 | +0.595 | 283.2 | 816 | -0.88 | n | -1.66 | n | 1632 | 2 | 1069.87 | DEAD_COINT |
| USDCAD/USDNOK | 0 | 378 | — | — | — | — | — | — | — | — | — | — | DROPPED (split too small (in=0, hold=378)) |

## Verdict legend
- **ADVANCE** — cointegrated in both windows AND gross reversion > two-leg cost. Only these proceed to the first-touch spread simulator.
- **DEAD_COINT** — fails the Engle-Granger gate (not stationary in-sample, or stationarity does not survive the embargoed holdout with beta frozen).
- **DEAD_COST** — cointegrated, but the expected reversion does not clear the two-leg round-trip spread. Dead on arithmetic; no simulation can rescue it.
- **DROPPED** — leg unavailable on the broker feed or too little aligned data (reported, never silently swapped).

**Zero candidates cleared the gate. Per the pre-registration kill bar, Track 3d is DEAD and the relative-value category is falsified — the edge hunt is complete across all four structural categories. No simulation is written; no threshold is tuned. Door B.**