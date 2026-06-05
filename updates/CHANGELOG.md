# Helix V3 Changelog

All major code changes and evaluation results are logged here.

---

## [v2.3.0] - 2026-06-05

### CRITICAL FIX — M/W Direction Override
- **W-bottom = BUY, M-top = SELL** — M/W pattern now drives trade direction
- Previously: stop hunt breach side determined direction (price above Asian high → SELL)
- This was BACKWARDS. The breach above is the fake move. The W-bottom is the real reversal signal.
- Impact: AUDUSD was being called SELL at 80/100 confluence when W-bottom clearly said BUY
- Result: 3 consecutive losing SELL trades on AUDUSD before fix was applied

### CRITICAL FIX — Persistent Re-Entry Guard
- `helix_v3/core/reentry_guard.py` — SQLite-backed loss tracking
- 1 loss → COOLDOWN (blocked until session transition)
- 2+ losses same pair/direction → BANNED for the day
- Exposure check: no new entry if pair already has open position
- **Survives restarts** — previous in-memory guard was wiped on restart, causing re-entry
- Guard DB seeded with today's actual losses on deployment

### CRITICAL FIX — Chart Asian Range Box Position
- Asian range boxes now drawn on EVERY day's Asian session (worktime ribbon style)
- Previously: box hardcoded at x=0 (3 days ago on a 200-bar chart)
- Now: per-day boxes from `sessions.py` at correct bar indices
- Today's Asian range labeled with pip count, previous days shown as shaded columns

### Added — Session Infrastructure
- `helix_v3/core/sessions.py` — session classification, per-day Asian range, weekly open range
- Session boundary vertical separators with color-coded shading
- Weekly open range (first 4h of week) as psychological S/R levels
- Asian H/L/Mid dotted lines extending across full chart width

### Fixed — WhatsApp Notifications
- Each trade recommendation now sent WITH chart image in same message (not separate)
- Messages split to stay under 1600 char limit
- Narrative analysis format (session-by-session) instead of just tables

### Updated — V2 Orchestrator Wired with Full Indicators
- TDI (V2-verified), patterns, pivots, ADR, daily HiLo, crossover arrows
- All indicators feed into annotated flashcard chart generation
- Re-entry guard integrated into `_process_symbol` pipeline

---

## [v2.2.0] - 2026-06-05

### Ported from core-helix V2 Repository
- TDI parameters corrected: RSI=21, Signal=7 SMA, SharkFin=63/37 (all verified from MT4 screenshots)
- ADR switched to Wilder ATR(14) matching MT5 output
- Pivots: added R3/S3, day-type logic (red candle→M1/M3, green→M2/M4)
- NewHUD dashboard: HOD/LOD+dist, TDR, YDR, WADR, MADR, HYADR, WR, 3xADR
- Crossover arrows: EMA 7/13 + 50/200 with shift(1) anti-repaint guard
- Daily HiLo: PHOD/PLOD with 14-day snake history

---

## [v2.1.0] - 2026-06-04

### Added — MMM Indicators & Visual Analysis
- `helix_v3/core/tdi.py` — Full TDI (Traders Dynamic Index) implementation
  - RSI line, Signal line, Market Baseline, Volatility Bands
  - Shark Fin Short/Long detection (stop hunt confirmation)
  - Blood in the Water signal (baseline cross after shark fin)
  - VB squeeze detection (Asian consolidation)
  - RSI divergence detection (bullish/bearish)
  - Pivot point calculator (PP, R1/R2, S1/S2, M1-M4 per MMM book)
  - ADR (Average Daily Range) calculator
- `helix_v3/core/patterns.py` — Context-aware candlestick pattern detection
  - Spike candles / Empire State (MM trap candles)
  - Hammers, inverted hammers, spinning tops, doji
  - Evening Star / Morning Star (45-min extended RRT)
  - Railroad Tracks (RRT) — compressed M/W
  - High Test / Low Test (prev day HOD/LOD rejection)
  - Pin bars (long wick rejections at key levels)
  - M-Top / W-Bottom geometric detection
  - Half Batman pattern
  - MMM trade type classification: Straightaway, 2nd Leg M/W, The 33, NYC Reversal, EMA 200 Bounce

### Enhanced — Annotated Flashcard Charts
- **TDI subplot** below price panel (RSI green, Signal red, Base yellow, VBs blue)
- **Pivot levels** (PP, R1, S1, M1, M3) as dotted horizontal lines
- **ADR high/low** projected levels
- **Previous day HOD/LOD** markers
- **Pattern markers** on chart (triangles, squares, stars for each pattern type)
- **Trade type badge** (top-right: "THE 33", "NYC REVERSAL", etc.)
- **Session box overlays** (Asian, NYC reversal window)
- **Info box** now includes TDI readings, divergence, and trade type

### Evaluation
- See `updates/eval_20260604_142942.txt` for V1 vs V2 comparison results

---

## [v2.0.0] - 2026-06-04

### Added
- `helix_v3/orchestrator_v2.py` — MTF-first orchestrator with full top-down analysis
- `tests/compare_orchestrators.py` — Side-by-side v1 vs v2 evaluation harness
- `updates/` directory for tracking major changes and evaluation logs

### Changed (v2 vs v1)
- **Analysis**: v1 uses flat `quant_engine.generate_signal()` per TF. v2 uses `MTFAnalyzer.analyze()` which runs Weekly->4H->1H->15M as a single top-down pass per symbol.
- **Entry gate**: v1 requires `pre_filter_passed` (accumulation + stop hunt boolean). v2 uses `confluence_score >= 50` from MTF analysis with up to 1 minor conflict allowed.
- **Charts**: v1 exports plain vision charts. v2 generates annotated flashcard charts with Asian range box, stop hunt zone, HOD/LOD, entry/SL/TP markers, and MTF info overlay.
- **Notifications**: v1 sends text-only WhatsApp alerts. v2 sends flashcard chart images with full MTF context (weekly trend, cycle level, session, 15M signals).
- **Flashcard DB**: v1 never writes flashcards. v2 saves entry/scan/missed flashcards with full MTF context for pattern learning.

### Entry Policy Comparison

| Gate | v1 (orchestrator.py) | v2 (orchestrator_v2.py) |
|------|---------------------|------------------------|
| 1. Analysis | `quant_engine.generate_signal()` per TF | `mtf.analyze()` top-down per symbol |
| 2. Pre-gate | `pre_filter_passed` (accum AND hunt AND trend) | `confluence_score >= 50` AND `trade_valid` |
| 3. Vision | Chart export + consensus (conf >= 0.88) | Same, but with annotated chart |
| 4. Risk | Drawdown/position/spread checks | Same |
| 5. Execution | MT5 market order | Same |
| 6. Notification | Text-only WhatsApp | Flashcard chart + MTF context via WhatsApp |
| 7. Learning | No flashcard saved | Flashcard saved to DB with full context |

---

## [v1.0.0] - 2026-06-04

### Initial Release
- Full pipeline: quant pre-filter -> chart export -> vision consensus -> pair-gated execution
- 13-pair portfolio with per-pair risk tiers
- Local/Anthropic/Dual-API consensus modes
- WhatsApp notifications via Twilio
- Trade journal (75 fields), market scanner, flashcard DB schema
- 60s scan loop, 15-min market dashboard, session/EOD/weekly/monthly reports
