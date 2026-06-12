# Helix V3 — Audit Remediation Plan

Source: full quantitative/execution/architecture audit, 2026-06-12.
Rule of engagement: **no live (demo or real) trading sessions until Tier 0 is complete.**
Nothing gets deleted — superseded code goes through `tools/trash.py` (see bottom).

Status legend: `[ ]` todo · `[~]` in progress · `[x]` done

---

## Tier 0 — Stop the bleeding (live-loss bugs, ~1 day)

- [x] **0.1 Repoint launcher to V2.** `start_helix.py:19` and `pyproject.toml` `[project.scripts]` ran legacy V1. Both now point at `helix_v3.orchestrator_v2`. (Done 2026-06-12.)
- [x] **0.2 Fix false-loss action classification.** (Done 2026-06-12: exit actions classified by explicit prefix `TIME EXIT:`/`STALE EXIT:`/`SESSION EXIT:`; `record_loss` only on parsed negative pips; `record_exit` + replay recording skip TRAIL/T1/STALE TIGHTEN; direction parsed from the action string with active-order/journal fallback. Regression tests cover all 9 action shapes in `tests/test_execution_gatekeeper.py`.) `orchestrator_v2.py:777-810` matches loss markers by substring — `"TRAIL: ... SL->..."` contains `"sl"`, so profitable trail updates record losses and 2 trails = persistent DAY_BAN of a winning direction. Fix: match explicit prefixes only (`"STALE EXIT:"`, `"TIME EXIT:"`, `"SESSION EXIT:"`, SL-hit exits). Also stop calling `guard.record_exit()` for TRAIL/T1/TIGHTEN actions while the position is still open (`orchestrator_v2.py:818-839`). Add regression tests for every action string `gatekeeper` can emit.
- [x] **0.3 Make the order retry loop idempotent.** (Done 2026-06-12: pre-send snapshot of Helix tickets on the symbol; on `None` result the server is reconciled before any retry (full fill → adopt ticket, partial → resend remainder only); `DONE_PARTIAL` resends only the unfilled remainder; `PLACED` never resends (status PENDING, orphan adoption registers a late fill). 4 retry-matrix tests.) `gatekeeper.py:367-433`: on `result is None` or `TRADE_RETCODE_DONE_PARTIAL`, query `mt5.positions_get` filtered by magic+symbol BEFORE any resend; resend only unfilled remainder; treat `TRADE_RETCODE_PLACED` (10008) as success-pending, not failure.
- [ ] **0.4 Real kill switch.** `gatekeeper.py:92-106` uses `(balance-equity)/balance` — blind to realized losses. Add: balance high-water mark persisted to SQLite, max realized daily loss (e.g. 4%), max total drawdown from HWM (8%) → halt new entries + notify. Realized losses must trip it.
- [ ] **0.5 Lot-sizing layer 3 must actually reject.** `gatekeeper.py:181-191` clamps to `vol_min` and sends anyway. If even `vol_min` exceeds the risk cap → return None, abort the order, log + notify. Also add `mt5.order_check()` margin pre-check, and clamp (not round) lot to step so it can't round up past the cap (`gatekeeper.py:177-179`).
- [ ] **0.6 Fix orphan adoption double-T1.** `gatekeeper.py:469-488`: if adopted position's SL ≈ entry (breakeven), set status `T1_HIT` and resume trailing — do not reconstruct `take_profit_1 = entry` (which fires a second 50% partial close on every restart).
- [ ] **0.7 Quarantine live-firing "tests".** Move `tests/execute_gbpjpy.py` (places a real trade) out of pytest's path; rename `tests/live_test.py` functions so pytest can't collect them against live MT5 (or move to `tools/manual/`).
- [ ] **0.8 Stop uploading charts to tmpfiles.org.** `whatsapp.py:185-209` publishes annotated strategy charts (entry/SL/TP) to a public unauthenticated host. Use Telegram's native photo upload (already implemented) or Twilio media via a private bucket; until then, send text-only on WhatsApp.

## Tier 1 — Make the backtest tell the truth (~1-2 weeks)

- [ ] **1.1 Kill higher-TF look-ahead.** `backtest/data_store.py:144-149` serves the forming H4/H1/D1 bar with its final OHLC (MT5 indexes by open time). Filter to bars where `open_time + tf_duration <= as_of`. In live mode, drop the forming bar from all pattern/indicator windows (`quant_engine.py:97` `copy_rates_from_pos(..., 0, ...)` includes bar 0).
- [ ] **1.2 One canonical timezone module.** `quant_engine.py:104` / `data_store.py:118` stamp MT5 broker server time (ICMarkets GMT+2/+3, DST-switching) as UTC; three contradictory session definitions exist (`quant_engine` vs `sessions.py` vs `mtf_analyzer.py:348-357`). Build `core/market_time.py` with `zoneinfo`, convert server→UTC properly, define Asian/London/NY windows ONCE, import everywhere.
- [ ] **1.3 Walk-forward separation for the learning loop.** `engine.py:922-940` promotes patterns from a run's own trades into `validation_library.db`, then `engine.py:585-627` queries it on the same data. Add date partitioning: promotion may only use outcomes strictly before the evaluation window; embargo ≥ 1 week between calibration and test. Fix replay `source_id` collisions (`engine.py:702` uses `len(closed_trades)` at entry time).
- [ ] **1.4 Honest P&L accounting.** `engine.py:347-359`: use the actual computed lot (step/cap/margin constrained), book T1 partial closes at closed size (currently $0 booked, then full-size TP2 → winners inflated ~43%, `engine.py:304-317`), risk from equity at ENTRY not exit.
- [ ] **1.5 Real cost model.** Full per-pair spread on both sides (sample live spreads from MT5 at signal time and store), commission per lot, swap for overnight, slippage parameter with 0×/1×/2× stress runs. Currently: max_spread/4 on entry only, zero on exits (`engine.py:638-645`).
- [ ] **1.6 Gap-aware fills + mark-to-market.** SL fills at bar open when gapped through (`engine.py:237` fills at the stop). `_unrealized_pnl` is hardcoded 0.0 (`engine.py:362-364`) — mark open positions to market so drawdown and the 8% breaker see floating excursions. Resolve same-bar T1-vs-TP2 ordering conservatively (T1 first; currently TP2 checked first, `engine.py:229-261`).
- [ ] **1.7 Correct statistics.** `report.py:34-37` computes Sharpe from per-trade pips × √252. Replace with daily dollar-return Sharpe; add Deflated Sharpe Ratio given the number of configurations tried; report max DD from mark-to-market equity.
- [ ] **1.8 Fix the stale-tighten no-op.** `engine.py:294-301`: `pip_size` computes to 1.0 always, and it writes `trade.stop_loss` while exits read `trade.current_sl`. Align with the replay labeler's correct implementation (`mmm_event_replay.py:592-601`).
- [ ] **1.9 RE-RUN the 365-day backtest with 1.1–1.8 in place and accept the number.** This is the moment of truth. All prior calibration conclusions (pair disables, P90 hunt ranges, stale timings) are void until re-derived on the fixed simulator.

## Tier 2 — Re-derive the edge honestly (~2-4 weeks)

- [ ] **2.1 Restore a real stop-hunt gate.** `mtf_analyzer.py:506-511` fabricates `hunt_detected=True` whenever M/W exists (hunt_pips can be negative). Require an actual breach of the Asian range (soft hunts = small but POSITIVE breach + M/W). Fix the contradictory breach-direction semantics (`:439-441` vs `:523-524`).
- [ ] **2.2 Re-specify M/W detection.** `mtf_analyzer.py:463-476` is an unanchored 5-bar fractal that fires on noise. Add: amplitude floor (×ATR), anchoring to Asian range/HOD/LOD, neckline-break confirmation, recency bound (pattern within last N bars), and exclude the forming bar.
- [ ] **2.3 ATR-normalize every gate.** Replace fixed pips (Asian range max, hunt min/max, level move, trail, min SL) with ratios of ATR(20, D1). Collapse ~320 per-pair magic numbers to ~10 universal ratios + true per-instrument facts. XAUUSD's 8000/15000-pip vacuous gates disappear by construction (`pair_profiles.py:404-406`).
- [ ] **2.4 Rebuild rule validation.** `rule_validator.py:381-389, 633-642` scores hits via MFE>MAE without path ordering (stop-out-then-rally counts as HIT). Use first-touch labeling, non-overlapping samples, binomial tests vs base rates, Benjamini-Hochberg across the rule×pair grid. Rules that fail die.
- [ ] **2.5 News blackout.** No entries ±30min around high-impact events (NFP/CPI/central banks); flatten or widen management around them. A stop-hunt strategy without this is the hunted.
- [ ] **2.6 Portfolio currency-exposure cap.** Max 2× single-trade risk per base currency across open positions (3 GBP longs = one news candle = ~9% correlated loss today). Remove the advisory bonus for correlated "cross-pair themes" or cap it.
- [ ] **2.7 Demote vision LLM from gate to logger.** Non-deterministic (no temperature/seed, `validator.py:159-177`), anchored prompts, uncalibrated 0.88 self-confidence threshold, fabricated `agreed=True` when keyless (`orchestrator_v2.py:558-570`). Log verdicts + outcomes via `vision_store`; only re-enable as a gate after measured lift over the quant baseline. Remove the file-based verdict bypass for live orders.
- [ ] **2.8 Simple regime filter.** Two-state gate (realized-vol percentile + trendiness) deciding "MMM conditions present/absent" before any pair-level logic.

## Tier 3 — Production hardening (ongoing)

- [ ] **3.1 MT5 watchdog.** Reconnect loop with backoff, heartbeat, dead-man alert (no successful broker poll in N minutes → Telegram alert). `positions_get()→None` must log + notify, not silently return [] (`gatekeeper.py:451-453`).
- [ ] **3.2 Decouple position management from the slow loop.** Trailing/T1/stale checks in their own fast async task (every 10-15s); charts, vision, notifications, reports must never delay SL management. Make all notification HTTP fire-and-forget (currently sync httpx, 30s timeouts, inside the trade path — `whatsapp.py:106-111`, `telegram.py:109-131`).
- [ ] **3.3 Order-send portability + safety.** Select filling mode from `symbol_info.filling_mode` (IOC hardcoded, `gatekeeper.py:364`); validate SL/TP against `trade_stops_level`/`freeze_level` before send/modify; retry failed breakeven `_modify_sl` and ALERT if a post-T1 position is left without breakeven (`gatekeeper.py:706-709`); per-symbol deviation in pips not points (`gatekeeper.py:360`).
- [ ] **3.4 Journal correctness.** `trade_journal.py:438-494`: sum ALL deals per position (T1 partial leg currently excluded from P&L, commission, swap); back-fill broker positions missing from the journal; classify Helix-initiated closes from our own comments, not broker comment substrings.
- [ ] **3.5 Repo hygiene.** Trash V1 orchestrator + dead CLI tools (done via tools/trash.py); single notifier interface (Telegram primary, WhatsApp adapter); charts/ rotation policy (3.5GB and growing); CI running the real test suite; update CLAUDE.md file map (analysis/, watchlist, setup_intelligence, 14 pairs).
- [ ] **3.6 Execution-layer test matrix.** retcode/retry matrix incl. DONE_PARTIAL/PLACED/None, lot-size math per instrument class, orphan adoption (pre/post T1), kill-switch trip conditions, action-string classification (0.2).

---

## Trash workflow (instead of deletion)

- `python tools/trash.py put <path> --reason "..."` — move into `trash/` with manifest entry.
- `python tools/trash.py list` / `restore <id>` — inspect / bring back.
- `python tools/trash_review.py review` — classify every item: still referenced → `restore-recommended`; provable junk (logs/caches/build artifacts) → `delete-candidate` (2h grace, then permanently deleted on a later `review` run); anything not provably junk → `unsure`, maintained forever until a human runs `approve <id>`.

Trashed in the first pass (2026-06-12): V1 `orchestrator.py` (superseded, launcher repointed), `backtest/account_cli_replay.py` (zero importers), `analysis/setup_miner.py` (zero importers), `tests/execute_gbpjpy.py` (live-trade script in pytest path), `hs_err_pid64036.log`, `helix_v3.egg-info/`, `.tmp/`.

Deliberately NOT trashed: `helix_v3/training/` (actively used for vision-review packets), `historical_flashcard_miner.py` / `scanner_replay.py` (active mining work), `tests/live_test.py` (documented integration test — handled in 0.7 instead).
