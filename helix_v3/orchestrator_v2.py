"""Helix V3 Pipeline Orchestrator — V2 (MTF-First + Flashcard Charts).

Key differences from v1 (orchestrator.py):
  - Uses MTFAnalyzer as PRIMARY analysis engine (Weekly->4H->1H->15M per symbol)
  - Generates annotated flashcard charts with full confluence markings
  - Sends chart images with WhatsApp notifications (not text-only)
  - Saves flashcards to DB for pattern learning
  - Entry gate: confluence_score >= 50 (not just boolean pre_filter_passed)
  - Tracks multi-day structure context (support retests, weekly cycle position)

Everything else (trade management, position management, reports) is identical to v1.
"""

from __future__ import annotations

import asyncio
import signal
import time
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Set

from config.settings import settings
from helix_v3.consensus.validator import MMMConsensusValidator
from helix_v3.core.advisory_confidence import (
    AdvisorySetup,
    advisory_setup_from_mtf,
    score_advisory_setup,
)
from helix_v3.core.mtf_analyzer import MTFAnalyzer, MTFAnalysis
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.tdi import (
    compute_tdi, compute_pivots, compute_adr, compute_daily_hilo,
)
from helix_v3.core.patterns import scan_patterns
from helix_v3.core.reentry_guard import ReentryGuard
from helix_v3.execution.gatekeeper import MT5ExecutionGatekeeper
from helix_v3.journal.flashcards import FlashcardSystem
from helix_v3.notifications.whatsapp import WhatsAppNotifier
from helix_v3.notifications.telegram import TelegramNotifier
from helix_v3.scanner.market_scanner import MarketScanner
from helix_v3.utils.logger import get_logger
from helix_v3.visualization.annotated_chart import AnnotatedChartGenerator
from helix_v3.visualization.chart_exporter import MMMChartVisualizer

# Optional imports — gracefully degrade if not present
try:
    from helix_v3.backtest.vision_store import VisionBacktestStore
    _HAS_VISION_STORE = True
except ImportError:
    _HAS_VISION_STORE = False

try:
    from helix_v3.ai.model_roles import format_role_report
    _HAS_ROLE_REPORT = True
except ImportError:
    _HAS_ROLE_REPORT = False

try:
    from helix_v3.backtest.validation_library import ValidationLibrary
    from helix_v3.backtest.mmm_event_replay import replay_setup_from_mtf, ReplaySetup
    _HAS_VALIDATION = True
except ImportError:
    _HAS_VALIDATION = False

try:
    from helix_v3.consensus.validator import PROMPT_VERSION
except ImportError:
    PROMPT_VERSION = "mmm_vision_v2"

logger = get_logger("orchestrator_v2")

SCAN_INTERVAL_SECONDS = 60
MARKET_SCAN_INTERVAL_SECONDS = 900
MIN_CONFLUENCE_SCORE = 50


def _mtf_to_flashcard_context(a: MTFAnalysis) -> Dict:
    """Convert MTFAnalysis to a flat dict for flashcard storage."""
    return {
        "weekly": {
            "cycle_position": a.weekly.cycle_position.value,
            "week_phase": a.weekly.week_phase.value,
            "trend_direction": a.weekly.trend_direction.value,
            "days_since_peak": a.weekly.days_since_peak,
        },
        "four_hour": {
            "cycle_position": a.four_hour.cycle_position.value,
            "level_count": a.four_hour.level_count,
            "trend_direction": a.four_hour.trend_direction.value,
            "is_choppy": a.four_hour.is_choppy,
        },
        "one_hour": {
            "session_phase": a.one_hour.session_phase.value,
            "trend_direction": a.one_hour.trend_direction.value,
            "intraday_level": a.one_hour.intraday_level,
            "hod_locked": a.one_hour.hod_locked,
            "lod_locked": a.one_hour.lod_locked,
            "ema_50_200_cross": a.one_hour.ema_50_200_cross,
        },
        "fifteen_min": {
            "asian_range_pips": a.fifteen_min.asian_range_pips,
            "accumulation_valid": a.fifteen_min.accumulation_valid,
            "stop_hunt_detected": a.fifteen_min.stop_hunt_detected,
            "stop_hunt_direction": a.fifteen_min.stop_hunt_direction.value,
            "stop_hunt_pips": a.fifteen_min.stop_hunt_pips,
            "push_count": a.fifteen_min.push_count,
            "m_w_forming": a.fifteen_min.m_w_forming,
            "m_w_pattern": a.fifteen_min.m_w_pattern
            or _infer_m_w_pattern(a.fifteen_min.m_w_forming, a.fifteen_min.entry_direction.value),
            "rrt_detected": a.fifteen_min.rrt_detected,
            "entry_direction": a.fifteen_min.entry_direction.value,
            "entry_confidence": a.fifteen_min.entry_confidence,
        },
        "ema": {
            "ema_5_angle": a.four_hour.ema_vector.ema_5_angle,
            "ema_13_angle": a.four_hour.ema_vector.ema_13_angle,
            "ema_50_angle": a.four_hour.ema_vector.ema_50_angle,
            "ema_200_angle": a.four_hour.ema_vector.ema_200_angle,
            "ema_800_angle": a.four_hour.ema_vector.ema_800_angle,
            "fast_slow_div": a.four_hour.ema_vector.fast_slow_divergence,
        },
        "confluence_score": a.confluence_score,
        "profile": {
            "risk_tier": a.pair_profile.risk_tier,
            "max_risk_pct": a.pair_profile.max_risk_pct,
        },
    }


def _infer_m_w_pattern(m_w_forming: bool, direction: str) -> str:
    if not m_w_forming:
        return ""
    if direction == "BUY":
        return "W_BOTTOM"
    if direction == "SELL":
        return "M_TOP"
    return ""


def _tdi_to_flashcard_context(tdi_result) -> Dict:
    signals = [s.value for s in tdi_result.signals if s.value != "NONE"]
    return {
        "signals": signals,
        "shark_fin_active": tdi_result.shark_fin_active,
        "shark_fin_direction": tdi_result.shark_fin_direction,
        "vb_squeeze": tdi_result.vb_squeeze,
        "divergence": tdi_result.divergence,
        "crossed_signal": tdi_result.rsi_crossed_signal,
        "rsi": tdi_result.rsi,
        "signal": tdi_result.signal,
        "base": tdi_result.base,
    }


def _patterns_to_flashcard_context(patterns) -> Dict:
    return {
        "trade_type": patterns.trade_type.value,
        "pattern_count": len(patterns.patterns),
        "pattern_types": [p.pattern.value for p in patterns.patterns],
        "rrt_count": patterns.rrt_count,
        "spike_count": patterns.spike_count,
        "pin_bar_count": patterns.pin_bar_count,
        "m_w_detected": patterns.m_w_detected,
        "half_batman": patterns.half_batman,
    }


def _currency_theme_tags(symbol: str, direction: str) -> list[str]:
    if direction not in ("BUY", "SELL"):
        return []
    if symbol == "XAUUSD":
        base, quote = "XAU", "USD"
    else:
        base, quote = symbol[:3], symbol[3:6]
    if direction == "BUY":
        return [f"{base}_STRENGTH", f"{quote}_WEAKNESS"]
    return [f"{base}_WEAKNESS", f"{quote}_STRENGTH"]


def _enrich_flashcard_context(
    analysis: MTFAnalysis,
    tdi_result,
    patterns,
    advisory=None,
) -> Dict:
    context = _mtf_to_flashcard_context(analysis)
    direction = analysis.trade_direction.value
    context["tdi"] = _tdi_to_flashcard_context(tdi_result)
    context["patterns"] = _patterns_to_flashcard_context(patterns)
    context["convergence"] = {
        "themes": _currency_theme_tags(analysis.symbol, direction),
        "theme_score": advisory.convergence_score if advisory else 0.0,
    }
    if advisory:
        context["advisory"] = {
            "confidence_score": advisory.final_score,
            "grade": advisory.grade,
            "action": advisory.action,
            "reasons": advisory.reasons,
            "blockers": advisory.blockers,
            "peer_symbols": advisory.peer_symbols,
        }
    return context


class HelixOrchestratorV2:
    """V2 Orchestrator — MTF-first analysis with flashcard chart notifications.

    Pipeline per symbol per scan cycle:
    1. Run full MTF analysis (Weekly->4H->1H->15M) — single top-down pass
    2. If confluence >= 50 and trade_valid, generate annotated flashcard chart
    3. Send chart to vision consensus for final confirmation
    4. On consensus, build and execute order via MT5
    5. Save flashcard to learning DB with full MTF context
    6. Send WhatsApp notification WITH chart image attached
    7. Manage open positions (partial close, trailing SL, stale exits)
    """

    def __init__(self) -> None:
        self.engine = MMMQuantitativeEngine()
        self.visualizer = MMMChartVisualizer()
        self.annotator = AnnotatedChartGenerator()
        self.validator = MMMConsensusValidator()
        self.gatekeeper = MT5ExecutionGatekeeper()
        self.scanner: Optional[MarketScanner] = None
        self.mtf: Optional[MTFAnalyzer] = None
        self.flashcards = FlashcardSystem()
        self.vision_backtests = VisionBacktestStore() if _HAS_VISION_STORE else None
        self.validation_lib = ValidationLibrary() if _HAS_VALIDATION else None
        from helix_v3.backtest.mmm_event_replay import MMMReplayStore
        self.replay_store = MMMReplayStore() if _HAS_VALIDATION else None
        # Track replay setups for open trades (keyed by symbol)
        self._live_replay_setups: Dict[str, object] = {}
        self.notifier = self._create_notifier()
        self._running = False
        # Filter to tradeable pairs only (respects PairProfile.tradeable flag)
        from config.pair_profiles import get_pair_profile
        self._symbols: List[str] = [
            s for s in settings.trading.symbols
            if get_pair_profile(s).tradeable
        ]
        self._last_market_scan: float = 0
        self._last_session: str = ""
        self._reports_sent_today: Set[str] = set()
        self._notified_setups: Set[str] = set()
        self._notified_failures: Set[str] = set()
        # Track last MTF analysis per symbol for comparison logging
        self._last_analysis: Dict[str, MTFAnalysis] = {}
        self._last_advisory_inputs: Dict[str, AdvisorySetup] = {}
        # Persistent re-entry guard (SQLite-backed, survives restarts)
        self.guard = ReentryGuard()

    @staticmethod
    def _create_notifier():
        """Pick notification backend from NOTIFICATION_BACKEND env var."""
        import os
        backend = os.getenv("NOTIFICATION_BACKEND", "whatsapp").lower()
        if backend == "telegram":
            notifier = TelegramNotifier()
            if notifier.enabled:
                return notifier
            logger.warning("Telegram not configured, falling back to WhatsApp")
        return WhatsAppNotifier()

    def _setup_signals(self) -> None:
        def _stop(signum, frame):
            logger.info("Shutdown signal received (%s)", signum)
            self._running = False

        signal.signal(signal.SIGINT, _stop)
        signal.signal(signal.SIGTERM, _stop)

    async def _process_symbol(self, symbol: str) -> None:
        """Run full MTF-first pipeline for one symbol.

        Unlike v1 which loops per-timeframe, v2 does one top-down pass per symbol
        because MTF analysis spans Weekly->4H->1H->15M inherently.
        """
        try:
            # Step 0: Check re-entry guard (persistent, survives restarts)
            guard_block = self.guard.check(symbol, "SELL")
            guard_block_buy = self.guard.check(symbol, "BUY")
            if guard_block and guard_block_buy:
                # Both directions blocked = symbol fully blocked
                return

            # Step 1: Full MTF analysis (the core difference from v1)
            analysis = self.mtf.analyze(symbol)
            self._last_analysis[symbol] = analysis

            logger.info(
                "MTF %s | Weekly=%s %s | H4=L%d %s | H1=%s %s | M15: AR=%.0fp hunt=%s pushes=%d | "
                "Confluence=%d/100 Valid=%s Dir=%s",
                symbol,
                analysis.weekly.week_phase.value,
                analysis.weekly.trend_direction.value,
                analysis.four_hour.level_count,
                analysis.four_hour.trend_direction.value,
                analysis.one_hour.session_phase.value,
                analysis.one_hour.trend_direction.value,
                analysis.fifteen_min.asian_range_pips,
                analysis.fifteen_min.stop_hunt_detected,
                analysis.fifteen_min.push_count,
                analysis.confluence_score,
                analysis.trade_valid,
                analysis.trade_direction.value,
            )

            # Gate: confluence score must reach threshold
            if analysis.confluence_score < MIN_CONFLUENCE_SCORE:
                if analysis.confluence_score >= 30:
                    logger.debug(
                        "MTF %s forming (score=%d, need %d): %s",
                        symbol, analysis.confluence_score, MIN_CONFLUENCE_SCORE,
                        "; ".join(analysis.rejection_reasons),
                    )
                return

            if not analysis.trade_valid:
                logger.info(
                    "MTF %s score=%d but NOT valid: %s",
                    symbol, analysis.confluence_score,
                    "; ".join(analysis.rejection_reasons),
                )
                return

            logger.info(
                "MTF SETUP DETECTED: %s %s confluence=%d/100 conf=%.0f%%",
                symbol, analysis.trade_direction.value,
                analysis.confluence_score, analysis.trade_confidence * 100,
            )

            # Re-entry guard: check direction + existing exposure (persistent DB)
            guard_reason = self.guard.check(symbol, analysis.trade_direction.value)
            if guard_reason:
                logger.warning("GUARD BLOCKED: %s — %s", symbol, guard_reason)
                return

            # Step 2: Generate annotated flashcard chart with full indicators
            df_m15 = self.engine.fetch_rates(symbol, "M15", count=200)
            df_d1 = self.engine.fetch_rates(symbol, "D1", count=140)

            pip_size = 0.01 if "JPY" in symbol else 0.0001
            if symbol == "XAUUSD":
                pip_size = 0.1

            # TDI (V2-verified RSI=21)
            tdi_result = compute_tdi(df_m15)

            # Pivots with day-type
            prev_d = df_d1.iloc[-2]
            prev_bullish = prev_d["Close"] > prev_d["Open"]
            pivots = compute_pivots(prev_d["High"], prev_d["Low"], prev_d["Close"], prev_bullish)

            # ADR (Wilder ATR)
            adr_val = compute_adr(df_d1)

            # Daily HiLo (14-day snake)
            hilo = compute_daily_hilo(df_d1)

            # Pattern scan
            patterns = scan_patterns(
                df_m15.iloc[-50:], pip_size,
                prev_hod=hilo["phod"], prev_lod=hilo["plod"],
                asian_high=analysis.fifteen_min.asian_range_high,
                asian_low=analysis.fifteen_min.asian_range_low,
            )

            advisory_setup = advisory_setup_from_mtf(
                analysis,
                tdi_result=tdi_result,
                patterns=patterns,
            )
            advisory = score_advisory_setup(
                advisory_setup,
                self._last_advisory_inputs.values(),
            )
            self._last_advisory_inputs[symbol] = advisory_setup
            logger.info(
                "ADVISORY %s %s score=%.1f grade=%s action=%s convergence=%.1f peers=%s",
                symbol,
                analysis.trade_direction.value,
                advisory.final_score,
                advisory.grade,
                advisory.action,
                advisory.convergence_score,
                ",".join(advisory.peer_symbols) or "-",
            )
            if advisory.blockers:
                logger.info("ADVISORY %s blockers: %s", symbol, "; ".join(advisory.blockers))

            # Validation library lookup — check if this pattern has historical backing
            if self.validation_lib and _HAS_VALIDATION:
                replay_setup = replay_setup_from_mtf(
                    analysis,
                    snapshot_at=datetime.now(timezone.utc),
                    tdi_result=tdi_result,
                    patterns=patterns,
                    source="live",
                )
                matches = self.validation_lib.validate_setup(replay_setup)
                if matches:
                    best = matches[0]
                    logger.info(
                        "VALIDATION %s: MATCH found — %s win=%.0f%% n=%d target=%.1fp",
                        symbol, best.setup_family, best.favorable_rate * 100,
                        best.total, best.realistic_target_pips or 0,
                    )
                    # Block entry if best matching pattern has <30% win rate with enough samples
                    if best.total >= 5 and best.favorable_rate < 0.30:
                        logger.warning(
                            "VALIDATION BLOCK: %s pattern has %.0f%% win rate (%d samples) — skipping",
                            symbol, best.favorable_rate * 100, best.total,
                        )
                        return
                else:
                    logger.debug("VALIDATION %s: No matching historical pattern", symbol)

            # Generate annotated chart with everything
            _, annotated_path = self.annotator.generate_from_mtf(
                df_m15, symbol, "M15", analysis,
                tdi_result=tdi_result,
                pattern_scan=patterns,
                pivots=pivots,
                adr=adr_val,
                prev_hod=hilo["phod"],
                prev_lod=hilo["plod"],
            )

            # Log TDI signals
            tdi_sigs = [s.value for s in tdi_result.signals if s.value != "NONE"]
            if tdi_sigs:
                logger.info("TDI %s: %s | RSI=%.0f Sig=%.0f Base=%.0f",
                            symbol, ", ".join(tdi_sigs), tdi_result.rsi, tdi_result.signal, tdi_result.base)

            # Step 3: Vision consensus on the chart
            image_b64, chart_path = self.visualizer.export_vision_matrix(
                df_m15, symbol, "M15"
            )
            consensus = await self.validator.evaluate(image_b64, symbol, "M15")
            if self.vision_backtests:
                self._record_vision_predictions(
                    symbol=symbol,
                    timeframe="M15",
                    analysis=analysis,
                    consensus=consensus,
                    chart_path=str(chart_path) if chart_path else None,
                )

            if not consensus.agreed:
                logger.info(
                    "No consensus for %s: %s", symbol, consensus.divergence_notes,
                )
                # Save as "missed" flashcard for learning
                self.flashcards.save_missed_flashcard(
                    symbol=symbol,
                    timeframe="M15",
                    chart_path=str(annotated_path),
                    mtf_context=_enrich_flashcard_context(analysis, tdi_result, patterns, advisory),
                    reason=f"Vision declined: {consensus.divergence_notes}",
                    tags=["missed", "no_consensus", analysis.weekly.week_phase.value],
                )
                return

            # Step 4: Notify with flashcard chart (not text-only)
            setup_key = f"{symbol}_{analysis.trade_direction.value}"
            if setup_key not in self._notified_setups:
                self.notifier.notify_setup_with_chart(
                    symbol=symbol,
                    timeframe="M15",
                    direction=analysis.trade_direction.value,
                    confidence=consensus.avg_confidence,
                    confluence_score=analysis.confluence_score,
                    cycle_level=analysis.four_hour.level_count,
                    session=analysis.one_hour.session_phase.value,
                    weekly_trend=f"{analysis.weekly.trend_direction.value} ({analysis.weekly.week_phase.value})",
                    asian_range_pips=analysis.fifteen_min.asian_range_pips,
                    stop_hunt_pips=analysis.fifteen_min.stop_hunt_pips,
                    m_w=analysis.fifteen_min.m_w_forming,
                    rrt=analysis.fifteen_min.rrt_detected,
                    push_count=analysis.fifteen_min.push_count,
                    chart_path=str(annotated_path),
                )
                self._notified_setups.add(setup_key)

            # Step 5: Build and execute order
            # We need a QuantSignal for the gatekeeper — generate from M15
            quant_signal = self.engine.generate_signal(symbol, "M15")
            order = self.gatekeeper.build_order(symbol, quant_signal, consensus)

            if order is None:
                logger.info("Order construction blocked for %s", symbol)
                block_key = f"block_{setup_key}"
                if block_key not in self._notified_failures:
                    self.notifier._send(
                        f"HELIX V3 ORDER BLOCKED\n{'='*25}\n"
                        f"{symbol} M15 {analysis.trade_direction.value}\n"
                        f"Confluence: {analysis.confluence_score}/100\n"
                        f"Reason: gatekeeper rejected (pair gate / risk / margin)"
                    )
                    self._notified_failures.add(block_key)

                # Save as missed flashcard
                self.flashcards.save_missed_flashcard(
                    symbol=symbol,
                    timeframe="M15",
                    chart_path=str(annotated_path),
                    mtf_context=_enrich_flashcard_context(analysis, tdi_result, patterns, advisory),
                    reason="Gatekeeper blocked",
                    tags=["missed", "blocked", analysis.weekly.week_phase.value],
                )
                return

            ticket = self.gatekeeper.execute_order(
                order,
                signal=quant_signal,
                consensus=consensus,
                consensus_mode=self.validator.mode,
                chart_path=str(chart_path) if chart_path else None,
            )

            if ticket:
                logger.info(
                    "TRADE EXECUTED: %s %s ticket=%d lots=%.2f confluence=%d",
                    order.direction.value, symbol, ticket, order.lot_size,
                    analysis.confluence_score,
                )

                # Store replay setup for outcome recording when trade closes
                if self.replay_store and _HAS_VALIDATION:
                    self._live_replay_setups[symbol] = replay_setup

                # Save entry flashcard with full MTF context
                fc_context = _enrich_flashcard_context(analysis, tdi_result, patterns, advisory)
                fc_context["profile"]["lot_size"] = order.lot_size
                self.flashcards.save_entry_flashcard(
                    symbol=symbol,
                    timeframe="M15",
                    ticket=ticket,
                    chart_path=str(annotated_path),
                    mtf_context=fc_context,
                    tags=[
                        analysis.trade_direction.value,
                        f"L{analysis.four_hour.level_count}",
                        analysis.weekly.week_phase.value,
                        analysis.one_hour.session_phase.value,
                    ],
                    notes=f"Confluence {analysis.confluence_score}/100",
                )

                # Notify trade entry with chart
                self.notifier.notify_trade_entry(
                    symbol=symbol,
                    direction=order.direction.value,
                    lot_size=order.lot_size,
                    entry_price=order.entry_price,
                    stop_loss=order.stop_loss,
                    tp1=order.take_profit_1,
                    tp2=order.take_profit_2,
                    sl_pips=order.sl_pips,
                    risk_reward=order.risk_reward,
                    ticket=ticket,
                    bias=analysis.weekly.trend_direction.value,
                    cycle_level=analysis.four_hour.level_count,
                    confidence=consensus.avg_confidence,
                )
            else:
                logger.warning("Order execution failed for %s", symbol)
                exec_key = f"exec_{setup_key}"
                if exec_key not in self._notified_failures:
                    self.notifier._send(
                        f"HELIX V3 EXEC FAILED\n{'='*25}\n"
                        f"{symbol} {order.direction.value} {order.lot_size} lots\n"
                        f"Entry: {order.entry_price}  SL: {order.stop_loss}\n"
                        f"Confluence: {analysis.confluence_score}/100\n"
                        f"MT5 returned no ticket — check terminal log"
                    )
                    self._notified_failures.add(exec_key)

        except ConnectionError as e:
            logger.error("Connection error for %s: %s", symbol, e)
        except Exception as e:
            logger.exception("Unexpected error processing %s: %s", symbol, e)

    def _record_vision_predictions(
        self,
        *,
        symbol: str,
        timeframe: str,
        analysis: MTFAnalysis,
        consensus,
        chart_path: Optional[str],
    ) -> None:
        """Persist model verdicts for offline backtesting and calibration."""
        for verdict in consensus.verdicts:
            provider, role = self._split_model_label(verdict.model_name)
            try:
                self.vision_backtests.record_prediction(
                    symbol=symbol,
                    timeframe=timeframe,
                    snapshot_at=analysis.timestamp,
                    provider=provider,
                    model_role=role,
                    verdict=verdict,
                    prompt_version=PROMPT_VERSION,
                    chart_path=chart_path,
                )
            except Exception as e:
                logger.warning("Vision prediction recording failed for %s: %s", symbol, e)

    @staticmethod
    def _split_model_label(model_name: str) -> tuple[str, str]:
        parts = model_name.split(":", 2)
        if len(parts) == 3:
            return parts[0], parts[1]
        if model_name.startswith("claude"):
            return "anthropic", "legacy_consensus"
        if model_name.startswith("gpt") or model_name.startswith("openai"):
            return "openai", "legacy_consensus"
        return "local", "local_verdict"

    async def _scan_cycle(self) -> None:
        """Run one scan cycle across all symbols."""
        # Manage existing positions and sync journal
        actions = self.gatekeeper.manage_open_positions()
        self.gatekeeper.journal.sync_from_mt5()

        for action in actions:
            self.notifier._send(f"HELIX V3 TRADE MGMT\n{'='*25}\n{action}")
            # Record entry cooldown for ANY trade exit (prevents same-setup churn)
            # Also record outcome to replay store for learning loop
            for sym in self._symbols:
                if sym in action:
                    self.guard.record_exit(sym)
                    # Record to replay store if we have a setup for this symbol
                    if self.replay_store and _HAS_VALIDATION and sym in self._live_replay_setups:
                        try:
                            rs = self._live_replay_setups.pop(sym)
                            from helix_v3.backtest.mmm_event_replay import build_setup_signature, outcome_from_closed_trade
                            sig = build_setup_signature(rs)
                            sig_id = self.replay_store.record_signature(sig)
                            # Build a minimal trade-like object from the action string
                            # Full outcome recording requires trade data from journal
                            logger.info("REPLAY: Recorded signature for %s exit", sym)
                        except Exception as e:
                            logger.debug("Replay record failed for %s: %s", sym, e)
                    break
            # Track losses for persistent re-entry guard
            action_lower = action.lower()
            if "sl" in action_lower or "stop" in action_lower or "loss" in action_lower or "stale" in action_lower:
                for sym in self._symbols:
                    if sym in action:
                        direction = "SELL" if "sell" in action_lower else "BUY" if "buy" in action_lower else ""
                        if direction:
                            self.guard.record_loss(sym, direction)
                        break

        # 15-minute market scan
        now = time.monotonic()
        if now - self._last_market_scan >= MARKET_SCAN_INTERVAL_SECONDS:
            self._run_market_scan()
            self._last_market_scan = now

        # MTF analysis per symbol (NOT per timeframe — one top-down pass each)
        for symbol in self._symbols:
            await self._process_symbol(symbol)

    def _run_market_scan(self) -> None:
        """Execute the 15-minute market condition scan with MTF context."""
        if not self.scanner:
            return

        try:
            self.scanner.scan_all()
            dashboard = self.scanner.print_dashboard()
            logger.info(dashboard)

            high = self.scanner.get_high_readiness(min_score=50)
            if high:
                self.notifier.notify_market_conditions(dashboard, high)

            from helix_v3.scanner.market_scanner import _get_session_name
            current_session = _get_session_name()
            if current_session != self._last_session and self._last_session:
                logger.info("Session transition: %s -> %s", self._last_session, current_session)
                self._send_session_report(self._last_session)
                self._notified_setups.clear()
                self._notified_failures.clear()
                # Reset cooldowns on session transition (bans persist until EOD)
                self.guard.clear_cooldowns()
            self._last_session = current_session

            self._check_scheduled_reports()

        except Exception as e:
            logger.error("Market scan failed: %s", e)

    # Session/report methods identical to v1
    SESSION_NAMES = {
        "ASIAN_EARLY": "Asian Early",
        "ASIAN_LATE": "Asian Late",
        "LONDON_PREMARKET": "London Pre-Market",
        "LONDON": "London",
        "NY_OVERLAP": "NY Overlap",
        "NY_LATE": "NY Late",
    }

    SESSION_CLOSE_MAP = {
        "ASIAN_EARLY": "02:00",
        "ASIAN_LATE": "10:00",
        "LONDON_PREMARKET": "11:00",
        "LONDON": "15:00",
        "NY_OVERLAP": "19:00",
        "NY_LATE": "00:00",
    }

    def _send_session_report(self, closed_session: str) -> None:
        journal = self.gatekeeper.journal
        stats = journal.get_session_stats()
        eat = timezone(timedelta(hours=3))
        now_eat = datetime.now(eat)

        session_label = self.SESSION_NAMES.get(closed_session, closed_session)
        close_time = self.SESSION_CLOSE_MAP.get(closed_session, "")
        period_range = f"{now_eat.strftime('%Y-%m-%d')} {session_label} (closed {close_time} EAT)"

        self.notifier.notify_period_report(
            period_name=f"{session_label} Session",
            period_range=period_range,
            total_trades=stats["total_trades"],
            wins=stats["wins"],
            losses=stats["losses"],
            breakevens=stats["breakevens"],
            total_pips=stats["total_pips"],
            net_profit=stats["net_profit"],
            win_rate=stats["win_rate"],
            profit_factor=stats["profit_factor"],
            best_trade=stats["best_trade"],
            worst_trade=stats["worst_trade"],
            by_symbol=stats["by_symbol"],
            winning_setups=stats["winning_setups"],
            equity_start=stats["equity_start"],
            equity_end=stats["equity_end"],
            max_drawdown_pips=stats["max_drawdown_pips"],
            avg_duration_min=stats["avg_duration_minutes"],
            t1_hit_count=stats["t1_hit_count"],
        )
        logger.info("Session report sent: %s", session_label)

    def _check_scheduled_reports(self) -> None:
        eat = timezone(timedelta(hours=3))
        now = datetime.now(eat)
        today_key = now.strftime("%Y-%m-%d")
        journal = self.gatekeeper.journal

        if hasattr(self, "_report_date") and self._report_date != today_key:
            self._reports_sent_today.clear()
            # Guard auto-resets on new trading day via DB check
        self._report_date = today_key

        if now.hour == 0 and now.minute < 15:
            report_key = f"eod_{(now - timedelta(days=1)).strftime('%Y-%m-%d')}"
            if report_key not in self._reports_sent_today:
                yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
                stats = journal.get_daily_stats(yesterday)
                self.notifier.notify_period_report(
                    period_name="END OF DAY", period_range=yesterday,
                    **{k: stats[k] for k in [
                        "total_trades", "wins", "losses", "breakevens",
                        "total_pips", "net_profit", "win_rate", "profit_factor",
                        "best_trade", "worst_trade", "by_symbol", "winning_setups",
                        "equity_start", "equity_end", "max_drawdown_pips",
                    ]},
                    avg_duration_min=stats["avg_duration_minutes"],
                    t1_hit_count=stats["t1_hit_count"],
                )
                self._reports_sent_today.add(report_key)

                # Auto-promote proven patterns at EOD
                if self.validation_lib:
                    try:
                        promoted = self.validation_lib.promote_from_replay(
                            min_total=5, min_favorable_rate=55.0, min_symbols=1,
                        )
                        if promoted > 0:
                            logger.info("VALIDATION: Promoted %d proven patterns at EOD", promoted)
                    except Exception as e:
                        logger.warning("Validation promotion failed at EOD: %s", e)

        if now.weekday() == 5 and now.hour == 0 and now.minute < 15:
            report_key = f"weekly_{today_key}"
            if report_key not in self._reports_sent_today:
                stats = journal.get_weekly_stats()
                monday = (now - timedelta(days=now.weekday())).strftime("%Y-%m-%d")
                friday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
                self.notifier.notify_period_report(
                    period_name="WEEKLY", period_range=f"{monday} to {friday}",
                    **{k: stats[k] for k in [
                        "total_trades", "wins", "losses", "breakevens",
                        "total_pips", "net_profit", "win_rate", "profit_factor",
                        "best_trade", "worst_trade", "by_symbol", "winning_setups",
                        "equity_start", "equity_end", "max_drawdown_pips",
                    ]},
                    avg_duration_min=stats["avg_duration_minutes"],
                    t1_hit_count=stats["t1_hit_count"],
                )
                self._reports_sent_today.add(report_key)

        if now.day == 1 and now.hour == 0 and now.minute < 15:
            report_key = f"monthly_{today_key}"
            if report_key not in self._reports_sent_today:
                stats = journal.get_monthly_stats()
                last_month = (now - timedelta(days=1)).strftime("%B %Y")
                self.notifier.notify_period_report(
                    period_name="MONTHLY", period_range=last_month,
                    **{k: stats[k] for k in [
                        "total_trades", "wins", "losses", "breakevens",
                        "total_pips", "net_profit", "win_rate", "profit_factor",
                        "best_trade", "worst_trade", "by_symbol", "winning_setups",
                        "equity_start", "equity_end", "max_drawdown_pips",
                    ]},
                    avg_duration_min=stats["avg_duration_minutes"],
                    t1_hit_count=stats["t1_hit_count"],
                )
                self._reports_sent_today.add(report_key)

    def get_analysis_summary(self) -> str:
        """Return a formatted summary of the latest MTF analysis for all symbols."""
        if not self._last_analysis:
            return "No MTF analysis available yet."

        lines = [
            "",
            "=" * 90,
            "  HELIX V2 MTF ANALYSIS SUMMARY | " + datetime.now(
                timezone(timedelta(hours=3))
            ).strftime("%Y-%m-%d %H:%M EAT"),
            "=" * 90,
            "",
            f"  {'Symbol':<10} {'Weekly':<18} {'H4 Cycle':<12} {'H1 Session':<16} "
            f"{'M15 Hunt':<12} {'Pushes':<8} {'Conf':<6} {'Valid':<6} {'Dir':<8}",
            "-" * 90,
        ]

        for sym in self._symbols:
            a = self._last_analysis.get(sym)
            if not a:
                lines.append(f"  {sym:<10} — no analysis —")
                continue

            hunt = f"{a.fifteen_min.stop_hunt_direction.value} {a.fifteen_min.stop_hunt_pips:.0f}p" if a.fifteen_min.stop_hunt_detected else "-"
            lines.append(
                f"  {sym:<10} "
                f"{a.weekly.week_phase.value:<8} {a.weekly.trend_direction.value:<8} "
                f"L{a.four_hour.level_count} {a.four_hour.trend_direction.value:<8} "
                f"{a.one_hour.session_phase.value:<16} "
                f"{hunt:<12} "
                f"{a.fifteen_min.push_count:<8} "
                f"{a.confluence_score:<6} "
                f"{'YES' if a.trade_valid else 'no':<6} "
                f"{a.trade_direction.value:<8}"
            )

            if a.rejection_reasons:
                for r in a.rejection_reasons:
                    lines.append(f"  {'':>10}   WARN: {r}")

        lines.append("=" * 90)
        return "\n".join(lines)

    async def run(self) -> None:
        """Main event loop."""
        self._setup_signals()

        if not self.engine.connect():
            logger.critical("Failed to connect to MT5. Exiting.")
            return

        self.scanner = MarketScanner(self.engine)
        self.mtf = MTFAnalyzer(self.engine)
        self._running = True
        self._last_market_scan = 0

        logger.info(
            "Helix V2 started | Symbols: %s | WhatsApp: %s | Min Confluence: %d",
            self._symbols,
            "ON" if self.notifier.enabled else "OFF",
            MIN_CONFLUENCE_SCORE,
        )
        if _HAS_ROLE_REPORT:
            logger.info("\n%s", format_role_report())

        try:
            while self._running:
                cycle_start = time.monotonic()
                await self._scan_cycle()

                # Log MTF summary every scan
                summary = self.get_analysis_summary()
                logger.info(summary)

                elapsed = time.monotonic() - cycle_start
                sleep_time = max(0, SCAN_INTERVAL_SECONDS - elapsed)
                if sleep_time > 0 and self._running:
                    await asyncio.sleep(sleep_time)
        finally:
            if self.scanner:
                self.scanner.close()
            self.flashcards.close()
            self.guard.close()
            if self.vision_backtests:
                self.vision_backtests.close()
            self.gatekeeper.journal.close()
            self.engine.disconnect()
            logger.info("Helix V2 shutdown complete.")


async def run_single_cycle() -> dict:
    """Run a single scan cycle and return analysis results (for comparison tests)."""
    from helix_v3.core.quant_engine import MMMQuantitativeEngine

    engine = MMMQuantitativeEngine()
    if not engine.connect():
        return {"error": "MT5 connection failed"}

    try:
        mtf = MTFAnalyzer(engine)
        symbols = list(settings.trading.symbols)
        results = {}

        for symbol in symbols:
            try:
                analysis = mtf.analyze(symbol)
                results[symbol] = {
                    "weekly_trend": analysis.weekly.trend_direction.value,
                    "weekly_phase": analysis.weekly.week_phase.value,
                    "weekly_cycle": analysis.weekly.cycle_position.value,
                    "days_since_peak": analysis.weekly.days_since_peak,
                    "h4_level": analysis.four_hour.level_count,
                    "h4_trend": analysis.four_hour.trend_direction.value,
                    "h4_choppy": analysis.four_hour.is_choppy,
                    "h1_session": analysis.one_hour.session_phase.value,
                    "h1_trend": analysis.one_hour.trend_direction.value,
                    "h1_hod": analysis.one_hour.hod,
                    "h1_lod": analysis.one_hour.lod,
                    "m15_asian_pips": analysis.fifteen_min.asian_range_pips,
                    "m15_accum": analysis.fifteen_min.accumulation_valid,
                    "m15_hunt": analysis.fifteen_min.stop_hunt_detected,
                    "m15_hunt_dir": analysis.fifteen_min.stop_hunt_direction.value,
                    "m15_hunt_pips": analysis.fifteen_min.stop_hunt_pips,
                    "m15_pushes": analysis.fifteen_min.push_count,
                    "m15_mw": analysis.fifteen_min.m_w_forming,
                    "m15_rrt": analysis.fifteen_min.rrt_detected,
                    "confluence_score": analysis.confluence_score,
                    "trade_valid": analysis.trade_valid,
                    "trade_direction": analysis.trade_direction.value,
                    "trade_confidence": analysis.trade_confidence,
                    "rejection_reasons": analysis.rejection_reasons,
                }
            except Exception as e:
                results[symbol] = {"error": str(e)}

        return results
    finally:
        engine.disconnect()


def main() -> None:
    orchestrator = HelixOrchestratorV2()
    asyncio.run(orchestrator.run())


if __name__ == "__main__":
    main()
