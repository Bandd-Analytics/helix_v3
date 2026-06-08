# Flashcard: Helix AR/NY/LDN/EMA/ADR/Gann Indicator

## Source
- File: `mt5/indicators/Helix_AR_NY_LDN_EMA_ADR_Gann.mq5`
- Origin: Ported from PineScript "AR Box, NY/LDN, EMA, ADR, Gann 2.0"
- Status: Production MQ5 indicator for MT5 chart

## What It Shows

### 1. Asian Range Box (Cyan)
- Session: 00:30 - 07:30 GMT (matches `sessions.py`)
- Draws rectangle over Asian H/L for each day
- Pip label at box bottom ("Asia: XX.X pips")
- Rolling average of Asian range over last 20 sessions

### 2. London Opening Range Box (Blue)
- Session: 07:30 GMT, 75-minute box
- Shows the first 75 minutes of London session H/L
- This is where stop hunts start per MMM

### 3. NYC Opening Range Box (Red)
- Session: 13:30 GMT, 75-minute box
- First 75 minutes of NY session H/L
- NYC reversal zone per MMM

### 4. Gann Levels (Gray dashed)
- Drawn at Asian close: 0 (low), 0.5 (mid), 1 (high)
- Extended forward as horizontal rays for the trading day
- These are the key levels for intraday reference
- Mid-level (0.5) acts as magnet for price return

### 5. EMA Stack
- EMA 5 (Yellow) — immediate momentum
- EMA 13 (Red) — short-term
- EMA 50 (Aqua) — medium-term
- EMA 200 (White) — major S/R
- EMA 800 (Navy) — institutional bias
- All toggleable via inputs

### 6. ADR HUD (top-right)
- ADR: 14-day SMA of daily range
- 3xADR: exhaustion level
- Today: current day's range in pips
- ADR%: how much of ADR has been used today
- AvgAsia: rolling 20-session Asian range average

## MMM Alignment

| Indicator Feature | MMM Rule | Helix V3 Code |
|------------------|----------|---------------|
| Asian box | Accumulation detection | `sessions.py` asian_ranges |
| London box | Stop hunt zone | `sessions.py` LONDON_GAP |
| NYC box | NYC reversal zone | `sessions.py` NY_GAP |
| Gann 0/0.5/1 | Asian mid as target | `sessions.py` mid calculation |
| EMA stack | Trend alignment | `quant_engine.py` EMA vectors |
| ADR | Daily range expectation | `tdi.py` compute_adr_marker |
| ADR% used | Entry viability filter | Not yet in V3 — could reduce stale exits |

## Key Insight for V3

**ADR% used** is NOT currently in our entry logic. If today's range has already consumed 80%+ of ADR, entering is risky — the move may be done. This could help filter the 47.6% stale exit problem.

## Implementation Gap
- `ADR% used > 80%` → Add as rejection reason in `mtf_analyzer._compute_confluence()`
- Uses same Wilder ATR(14) we already compute in `tdi.py`
