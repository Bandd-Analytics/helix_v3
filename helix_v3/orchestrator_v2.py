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
import os
import re
import signal
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set

from config.settings import settings
from helix_v3.consensus.validator import MMMConsensusValidator
from helix_v3.core.types import ConsensusResult, Direction
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
from helix_v3.core.regime import assess_regime
from helix_v3.execution.mt5_watchdog import MT5Watchdog
from helix_v3.execution.gatekeeper import MT5ExecutionGatekeeper
from helix_v3.journal.flashcards import FlashcardSystem
# Notifier backends are selected via notifications.base.create_notifier (Tier 3.5)
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
    from helix_v3.backtest.mmm_event_replay import replay_setup_from_mtf
    _HAS_VALIDATION = True
except ImportError:
    _HAS_VALIDATION = False

try:
    from helix_v3.consensus.validator import PROMPT_VERSION
except ImportError:
    PROMPT_VERSION = "mmm_vision_v2"

try:
    __import__("helix_v3.backtest.setup_intelligence")
    _HAS_SETUP_INTEL = True
except ImportError:
    _HAS_SETUP_INTEL = False

logger = get_logger("orchestrator_v2")

SCAN_INTERVAL_SECONDS = 60
MARKET_SCAN_INTERVAL_SECONDS = 900
MIN_CONFLUENCE_SCORE = 50
# Fast position-management cadence (Tier 3.2) — trailing/T1/stale/news/session
# exits run on this clock, decoupled from the scan cycle.
MANAGE_INTERVAL_SECONDS = int(os.getenv("MANAGE_INTERVAL_SEC", "10"))

# Gatekeeper action strings that mean the position was CLOSED. Everything else
# (TRAIL:, T1 HIT:, STALE TIGHTEN:) manages a position that is still open and
# must never trigger re-entry guard exits or loss bans.
EXIT_ACTION_PREFIXES = ("TIME EXIT:", "STALE EXIT:", "SESSION EXIT:")

# Matches the signed pips figure in exit actions: "pips=+3.4" / "pips=-12.0"
# (TIME/SESSION EXIT) or "-3.4 pips" (STALE EXIT).
_ACTION_PIPS_RE = re.compile(r"pips=([+-]?\d+(?:\.\d+)?)|([+-]\d+(?:\.\d+)?)\s+pips")

_ACTION_DIRECTION_RE = re.compile(r"\b(BUY|SELL)\b")


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
        # Setup intelligence DB for RRS grading
        self._setup_intel_conn = None
        if _HAS_SETUP_INTEL:
            try:
                import sqlite3
                intel_path = Path(settings.log_dir) / "setup_intelligence.db"
                if intel_path.exists():
                    self._setup_intel_conn = sqlite3.connect(str(intel_path))
                    self._setup_intel_conn.row_factory = sqlite3.Row
                    count = self._setup_intel_conn.execute(
                        "SELECT COUNT(*) FROM setup_stats WHERE rrs_grade IN ('R_RUNNER','R_REPEATER') AND positive_expectancy = 1"
                    ).fetchone()[0]
                    logger.info("Setup intelligence loaded: %d R_RUNNER/R_REPEATER setups", count)
            except Exception as e:
                logger.warning("Setup intelligence DB not available: %s", e)
        # Track replay setups for open trades (keyed by symbol)
        self._live_replay_setups: Dict[str, object] = {}
        self.notifier = self._create_notifier()
        # Kill-switch trips alert once per trading day
        self.gatekeeper.kill_switch_callback = self.notifier._send
        # MT5 watchdog (Tier 3.1): reconnect with backoff + dead-man alert.
        # Shared with the gatekeeper so a None positions_get feeds it too.
        self.watchdog = MT5Watchdog(alert_callback=self.notifier._send)
        self.gatekeeper.watchdog = self.watchdog
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
        """Single notifier interface (Tier 3.5): Telegram primary,
        WhatsApp adapter — see notifications/base.py."""
        from helix_v3.notifications.base import create_notifier
        return create_notifier()

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

            # Step 0.5: Regime filter (Tier 2.8) — are MMM conditions even
            # present on this symbol today? Decided BEFORE any pair-level
            # logic; changes at most once per D1 bar (cached).
            if settings.risk.regime_filter_enabled:
                regime = assess_regime(self.engine, symbol)
                if not regime.mmm_present:
                    logger.info("REGIME SKIP %s: %s", symbol, regime.reason)
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

            # Per-setup signature cooldown: catches setups that persist across many
            # M15 cycles (e.g. confluence-97 BUY re-detecting every cycle for hours).
            setup_signature = _setup_signature(analysis)
            sig_cooldown = self.guard.check_setup_cooldown(
                symbol, analysis.trade_direction.value, setup_signature
            )
            if sig_cooldown:
                logger.warning("SETUP COOLDOWN: %s — %s", symbol, sig_cooldown)
                return

            # P0 SESSION GATE: don't open in a session we'd immediately close in.
            # Without this, manage_open_positions session-exits the trade ~30s after
            # entry while we're still inside pair_profile.close_before_session.
            from config.pair_profiles import get_pair_profile
            from helix_v3.scanner.market_scanner import _get_session_name
            current_session = _get_session_name()
            pair_profile = get_pair_profile(symbol)
            if current_session == pair_profile.close_before_session:
                logger.warning(
                    "SESSION GATE: %s — skipping entry, current session %s matches "
                    "close_before_session (would immediately session-exit)",
                    symbol, current_session,
                )
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

            # Forward Plan Track 1.1: the advisory grade is hand-tuned MMM
            # weights that Edge Discovery Phase 1 disproved — it has no
            # measured directional edge, so it is a LOGGER, not a gate (same
            # demotion as vision in audit Tier 2.7). The grade is still
            # computed and journaled for research. It only blocks when the
            # ADVISORY_GATE toggle is explicitly on (for the Track 1.2 A/B).
            if advisory.grade in ("D", "AVOID"):
                if settings.risk.advisory_gate_enabled:
                    logger.warning(
                        "ADVISORY BLOCK: %s grade=%s score=%.0f — skipping (gate on)",
                        symbol, advisory.grade, advisory.final_score,
                    )
                    return
                logger.info(
                    "ADVISORY %s grade=%s score=%.0f — would block, but gate "
                    "demoted to logger (no validated edge); proceeding",
                    symbol, advisory.grade, advisory.final_score,
                )

            # Validation library lookup — check if this pattern has historical backing
            validation_match = None
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
                    validation_match = best
                    logger.info(
                        "VALIDATION %s: MATCH found — %s win=%.0f%% n=%d score=%.0f target=%.1fp",
                        symbol, best.setup_family, best.favorable_rate,
                        best.total, best.confidence_score, best.realistic_target_pips or 0,
                    )
                    # Block entry if best matching pattern has <30% win rate with enough samples
                    # favorable_rate is stored as percentage (0-100)
                    if best.total >= 5 and best.favorable_rate < 30.0:
                        logger.warning(
                            "VALIDATION BLOCK: %s pattern has %.0f%% win rate (%d samples) — skipping",
                            symbol, best.favorable_rate, best.total,
                        )
                        return
                    # Check graveyard: warn if this setup has been demoted before
                    grave_rows = self.validation_lib._conn.execute(
                        """SELECT times_demoted, peak_favorable_rate, favorable_rate
                           FROM setup_graveyard
                           WHERE normalized_key = ? AND (symbol = ? OR symbol = '')
                           ORDER BY times_demoted DESC LIMIT 1""",
                        (best.normalized_key, symbol),
                    ).fetchall()
                    if grave_rows:
                        g = grave_rows[0]
                        logger.warning(
                            "VALIDATION %s: GRAVEYARD WARNING — demoted %dx, "
                            "peak was %.0f%%, last fav was %.0f%%",
                            symbol, g[0], g[1] or 0, g[2] or 0,
                        )
                else:
                    logger.debug("VALIDATION %s: No matching historical pattern", symbol)

            # RRS setup intelligence lookup
            rrs_tag = ""
            if self._setup_intel_conn and _HAS_VALIDATION:
                try:
                    sig = replay_setup_from_mtf(
                        analysis, snapshot_at=datetime.now(timezone.utc),
                        tdi_result=tdi_result, patterns=patterns, source="live",
                    ) if not validation_match else replay_setup
                    from helix_v3.backtest.mmm_event_replay import build_setup_signature
                    sig_obj = build_setup_signature(sig)
                    nk = sig_obj.normalized_key
                    intel_row = self._setup_intel_conn.execute(
                        """SELECT rrs_grade, favorable_rate, total, avg_exit_pips, positive_expectancy
                           FROM setup_stats
                           WHERE normalized_key = ? AND symbol = ? AND total >= 5
                           ORDER BY total DESC LIMIT 1""",
                        (nk, symbol),
                    ).fetchone()
                    if not intel_row:
                        # Try cross-pair match
                        intel_row = self._setup_intel_conn.execute(
                            """SELECT rrs_grade, favorable_rate, total, avg_exit_pips, positive_expectancy
                               FROM cross_pair_stats
                               WHERE normalized_key = ? AND symbols LIKE ? AND total >= 10
                               ORDER BY total DESC LIMIT 1""",
                            (nk, f"%{symbol}%"),
                        ).fetchone()
                    if intel_row:
                        rrs_tag = intel_row["rrs_grade"]
                        logger.info(
                            "RRS %s: %s fav=%.0f%% n=%d exit=%+.1fp pos_exp=%d",
                            symbol, rrs_tag, intel_row["favorable_rate"],
                            intel_row["total"], intel_row["avg_exit_pips"] or 0,
                            intel_row["positive_expectancy"],
                        )
                except Exception as e:
                    logger.debug("RRS lookup failed for %s: %s", symbol, e)

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

            # Step 3: Vision verdict — LOGGER, NOT A GATE (audit Tier 2.7).
            # The vision layer is non-deterministic, prompt-anchored, and its
            # 0.88 self-confidence threshold was never calibrated; keyless
            # runs used to FABRICATE agreed=True. The execution decision below
            # is built purely from the quant pipeline (MTF + advisory +
            # validation library + gatekeeper). Vision verdicts are recorded
            # to vision_store with outcomes so a measured lift over the quant
            # baseline can be demonstrated BEFORE it is ever a gate again.
            chart_path = None
            vision = None
            vision_note = "vision: not run (no API keys) — quant pipeline only"
            _has_api_key = bool(
                getattr(self.validator, '_api_cfg', None)
                and (self.validator._api_cfg.anthropic_key or self.validator._api_cfg.openai_key)
            )
            if _has_api_key:
                try:
                    image_b64, chart_path = self.visualizer.export_vision_matrix(
                        df_m15, symbol, "M15"
                    )
                    vision = await self.validator.evaluate(image_b64, symbol, "M15")
                    if self.vision_backtests:
                        self._record_vision_predictions(
                            symbol=symbol,
                            timeframe="M15",
                            analysis=analysis,
                            consensus=vision,
                            chart_path=str(chart_path) if chart_path else None,
                        )
                    vision_note = (
                        f"vision(advisory): {vision.direction.value} "
                        f"conf={vision.avg_confidence:.2f} agreed={vision.agreed}"
                    )
                    if vision.direction not in (Direction.NEUTRAL, analysis.trade_direction):
                        logger.warning(
                            "VISION DISAGREES (advisory only) %s: vision=%s quant=%s "
                            "— logged to vision_store, NOT blocking",
                            symbol, vision.direction.value,
                            analysis.trade_direction.value,
                        )
                except Exception as e:
                    logger.error(
                        "Vision logging failed for %s: %s — proceeding on quant", symbol, e
                    )
                    vision_note = f"vision: error ({e})"
            else:
                logger.info("VISION SKIPPED %s: no API keys — quant pipeline only", symbol)

            # The execution decision is the QUANT pipeline's, with the vision
            # verdict carried along as journal metadata only.
            consensus = ConsensusResult(
                agreed=True,
                direction=analysis.trade_direction,
                avg_confidence=analysis.trade_confidence,
                verdicts=list(vision.verdicts) if vision else [],
                divergence_notes=vision_note,
            )

            # Step 4: Notify with flashcard chart (not text-only)
            setup_key = f"{symbol}_{analysis.trade_direction.value}"
            if setup_key not in self._notified_setups:
                # Build intelligence notes
                notes_parts = []
                if rrs_tag:
                    notes_parts.append(f"RRS: {rrs_tag}")
                if validation_match:
                    vm = validation_match
                    notes_parts.append(
                        f"PROVEN: {vm.favorable_rate:.0f}% win ({vm.total} samples) "
                        f"target={vm.realistic_target_pips or 0:+.1f}p"
                    )
                validation_note = " | ".join(notes_parts)
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
                    notes=validation_note,
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

                # P1: cool down this exact setup signature for 60 min so the same
                # MTF pattern doesn't re-fire on the next cycle.
                self.guard.set_setup_cooldown(
                    symbol,
                    order.direction.value,
                    setup_signature,
                    minutes=60.0,
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

    @staticmethod
    def _is_exit_action(action: str) -> bool:
        """True only for actions where the gatekeeper CLOSED the position."""
        return action.startswith(EXIT_ACTION_PREFIXES)

    @staticmethod
    def _action_pips(action: str) -> Optional[float]:
        """Parse the signed pips figure embedded in an exit action string."""
        m = _ACTION_PIPS_RE.search(action)
        if not m:
            return None
        return float(m.group(1) or m.group(2))

    def _record_guard_loss_from_action(self, action: str) -> None:
        """Record a re-entry-guard loss for true loss exits ONLY.

        Open-position management actions (TRAIL, T1 HIT, STALE TIGHTEN) must
        never record a loss — the old substring matcher saw the "SL" in
        "TRAIL: ... SL->..." and day-banned winning directions after two
        trail updates.
        """
        if not self._is_exit_action(action):
            return
        pips = self._action_pips(action)
        if pips is None:
            logger.warning("GUARD: exit action without parseable pips, not recording loss: %s", action)
            return
        if pips >= 0:
            return

        for sym in self._symbols:
            if sym not in action:
                continue

            # Exit actions embed the direction ("STALE EXIT: GBPJPY SELL ...")
            direction = ""
            dir_match = _ACTION_DIRECTION_RE.search(action)
            if dir_match:
                direction = dir_match.group(1)

            if not direction:
                for order in self.gatekeeper._active_orders.values():
                    if order.symbol == sym:
                        direction = order.direction.value
                        break

            if not direction:
                try:
                    row = self.gatekeeper.journal._conn.execute(
                        "SELECT direction FROM trades WHERE symbol=? ORDER BY id DESC LIMIT 1",
                        (sym,),
                    ).fetchone()
                    if row:
                        direction = row[0]
                except Exception:
                    logger.debug("GUARD: journal direction lookup failed for %s", sym)

            if direction:
                self.guard.record_loss(sym, direction)
                logger.info("GUARD: Recorded loss for %s %s (%+.1f pips)", sym, direction, pips)
            else:
                logger.warning("GUARD: Could not determine direction for %s loss", sym)
            return

    async def _scan_cycle(self) -> None:
        """Run one scan cycle across all symbols."""
        # Tier 3.1: health poll first. If the terminal is dead, the watchdog
        # reconnects with backoff and (after MT5_DEADMAN_MIN) alerts; nothing
        # downstream this cycle can work without a broker connection.
        if not self.watchdog.poll():
            logger.warning(
                "Scan cycle skipped: MT5 unhealthy (%.1f min since last good poll)",
                self.watchdog.seconds_down() / 60,
            )
            return

        # Position management lives in its own fast loop (Tier 3.2) — the
        # scan cycle no longer touches it, so charts/vision/notifications
        # can never delay trailing, T1, or stale exits.

        # 15-minute market scan
        now = time.monotonic()
        if now - self._last_market_scan >= MARKET_SCAN_INTERVAL_SECONDS:
            self._run_market_scan()
            self._last_market_scan = now

        # Daily chart rotation (Tier 3.5)
        if now - getattr(self, "_last_chart_rotation", 0) >= 86400:
            from helix_v3.utils.chart_rotation import rotate_charts
            rotate_charts()
            self._last_chart_rotation = now

        # MTF analysis per symbol (NOT per timeframe — one top-down pass each)
        for symbol in self._symbols:
            await self._process_symbol(symbol)

        # Send MMM narrative after all symbols are analyzed
        if time.monotonic() - self._last_market_scan < 60:
            # Market scan ran this cycle — send narrative with fresh data
            self._send_mmm_narrative()

    async def _manage_loop(self) -> None:
        """Fast position-management loop (audit Tier 3.2).

        Trailing / T1 / stale / news / session exits run every
        MANAGE_INTERVAL_SECONDS, decoupled from the slow scan cycle so a
        chart render or vision call can never delay SL management. The
        mt5 calls inside are quick IPC; notification sends are
        fire-and-forget threads, so one iteration is tens of ms.
        """
        while self._running:
            try:
                actions = self.gatekeeper.manage_open_positions()
                self.gatekeeper.journal.sync_from_mt5()
                if actions:
                    self._handle_management_actions(actions)
                # If the terminal is blind, drive the reconnect from here
                # too — this loop is the position-critical path.
                if self.watchdog.seconds_down() > MANAGE_INTERVAL_SECONDS * 2:
                    self.watchdog.try_reconnect()
            except Exception as e:
                logger.error("Manage loop error: %s", e)
            await asyncio.sleep(MANAGE_INTERVAL_SECONDS)

    def _handle_management_actions(self, actions: List[str]) -> None:
        """Notify + guard/replay bookkeeping for management actions."""
        for action in actions:
            self.notifier._send(f"HELIX V3 TRADE MGMT\n{'='*25}\n{action}")
            # Entry cooldown + replay recording apply only when the position
            # actually CLOSED. TRAIL/T1/STALE TIGHTEN leave it open — firing
            # record_exit for those put live winners on a 2h cooldown.
            if not self._is_exit_action(action):
                continue
            for sym in self._symbols:
                if sym in action:
                    self.guard.record_exit(sym)
                    # Record to replay store if we have a setup for this symbol
                    if self.replay_store and _HAS_VALIDATION and sym in self._live_replay_setups:
                        try:
                            rs = self._live_replay_setups.pop(sym)
                            from helix_v3.backtest.mmm_event_replay import build_setup_signature
                            sig = build_setup_signature(rs)
                            self.replay_store.record_signature(sig)
                            # Build a minimal trade-like object from the action string
                            # Full outcome recording requires trade data from journal
                            logger.info("REPLAY: Recorded signature for %s exit", sym)
                        except Exception as e:
                            logger.debug("Replay record failed for %s: %s", sym, e)
                    break
            # Track losses for persistent re-entry guard
            self._record_guard_loss_from_action(action)

    def _run_market_scan(self) -> None:
        """Execute the 15-minute market condition scan with MTF context."""
        if not self.scanner:
            return

        try:
            self.scanner.scan_all()
            dashboard = self.scanner.print_dashboard()
            logger.info(dashboard)

            # MMM narrative is sent after MTF loop, not here

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

    def _send_mmm_narrative(self) -> None:
        """Build and send an MMM story-style market update from MTF analysis."""
        if not self._last_analysis:
            return

        # Only send when the story changes — track a signature
        story_parts = []
        for sym, a in self._last_analysis.items():
            story_parts.append(f"{sym}_{a.four_hour.level_count}_{a.one_hour.session_phase.value}_{a.trade_direction.value}")
        story_key = "|".join(sorted(story_parts))
        if story_key == getattr(self, '_last_story_key', ''):
            return
        self._last_story_key = story_key

        now = datetime.now(timezone.utc)
        eat = now + timedelta(hours=3)

        # Session phase from bar time
        h = now.hour
        if 1 <= h < 5:
            session = "ACCUMULATION"
            session_eat = "04:00-08:00 EAT"
            session_desc = "Asia is building the range. Market makers accumulating quietly."
        elif 5 <= h < 8:
            session = "STOP HUNT"
            session_eat = "08:00-11:00 EAT"
            session_desc = "London is breaking the Asian range. This is the fake move — watch for reversals."
        elif 8 <= h < 13:
            session = "TRUE TREND"
            session_eat = "11:00-16:00 EAT"
            session_desc = "The real move is underway. If stop hunt reversed, price should be running in the true direction."
        elif 13 <= h < 17:
            session = "NYC REVERSAL"
            session_eat = "16:00-20:00 EAT"
            session_desc = "New York session. Potential reversal of the London move. Late entries only with high conviction."
        else:
            session = "RETURN TO ACCUMULATION"
            session_eat = "20:00-04:00 EAT"
            session_desc = "Session is done. Price drifting back to center. No new entries."

        # Weekly structure
        dow = eat.strftime("%A")
        day_num = eat.weekday()
        if day_num in (6, 0):
            week_phase = "EARLY WEEK"
            week_desc = "Fresh weekly cycle. Monday/Sunday sets the first direction — the stop hunt from here defines the week's bias."
        elif day_num in (1, 2):
            week_phase = "MID WEEK"
            week_desc = "Mid-week reversal zone. If early week pushed one direction, expect the turn. Wednesday is historically the strongest reversal day."
        elif day_num == 3:
            week_phase = "MID-TO-LATE WEEK"
            week_desc = "Thursday follow-through. If the reversal happened Wednesday, today should confirm the direction."
        else:
            week_phase = "LATE WEEK"
            week_desc = "Friday wind-down. Take profits, tighten stops. No new exposure before the weekend."

        lines = [
            "HELIX V3 — THE MMM STORY",
            f"{'='*30}",
            f"{dow} {eat.strftime('%d %b %Y')} | {eat.strftime('%H:%M')} EAT",
            "",
            f"WEEKLY: {week_phase}",
            week_desc,
            "",
            f"SESSION: {session} ({session_eat})",
            session_desc,
        ]

        # Per-pair narrative — group by what's interesting
        active_setups = []
        watching = []
        dead = []

        for sym in sorted(self._last_analysis.keys()):
            a = self._last_analysis[sym]
            m15 = a.fifteen_min
            h4 = a.four_hour
            wk = a.weekly

            level = h4.level_count
            level_desc = {0: "no clear structure", 1: "1st push (building)", 2: "2nd push (momentum)", 3: "3rd push (exhaustion/reversal)"}
            h4_dir = h4.trend_direction.value
            wk_dir = wk.trend_direction.value
            wk_phase = wk.week_phase.value

            # Build the story for this pair
            pair_lines = [f"{sym} — H4 Level {level}"]

            # Weekly context
            if wk_dir != "NEUTRAL":
                pair_lines.append(f"  Weekly: {wk_dir} ({wk_phase})")
            else:
                pair_lines.append(f"  Weekly: Ranging ({wk_phase})")

            # H4 cycle position
            pair_lines.append(f"  H4: {level_desc.get(level, '?')} trending {h4_dir}")

            # Today's structure
            ar = m15.asian_range_pips or 0
            hunt = m15.stop_hunt_detected
            hunt_dir = m15.stop_hunt_direction.value if m15.stop_hunt_direction else ""
            hunt_pips = m15.stop_hunt_pips or 0
            mw = m15.m_w_forming
            mw_pat = m15.m_w_pattern or ""
            pushes = m15.push_count

            if hunt and hunt_pips > 0:
                real_dir = "SELL" if hunt_dir == "BUY" else "BUY" if hunt_dir == "SELL" else "?"
                pair_lines.append(f"  Today: Asian range {ar:.0f}p. Stop hunt {hunt_dir} {hunt_pips:.0f}p — expecting {real_dir}")
                if mw:
                    pair_lines.append(f"  {mw_pat} forming with {pushes} pushes — reversal signal")
            elif ar > 0:
                pair_lines.append(f"  Today: Asian range {ar:.0f}p. No stop hunt yet.")
            else:
                pair_lines.append("  Today: No clear Asian structure.")

            # Confluence verdict
            if a.trade_valid:
                pair_lines.append(f"  SETUP ACTIVE: {a.trade_direction.value} (confluence {a.confluence_score}/100)")
                active_setups.append("\n".join(pair_lines))
            elif a.confluence_score >= 40:
                if a.rejection_reasons:
                    pair_lines.append(f"  Forming but: {a.rejection_reasons[0]}")
                watching.append("\n".join(pair_lines))
            else:
                dead.append(sym)

        if active_setups:
            lines.append("\nACTIVE SETUPS")
            lines.append("-" * 25)
            for s in active_setups:
                lines.append(s)

        if watching:
            lines.append("\nWATCHING")
            lines.append("-" * 25)
            for s in watching:
                lines.append(s)

        if dead:
            lines.append(f"\nNO SETUP: {', '.join(dead)}")

        msg = "\n".join(lines)

        # Telegram caption limit is 4096
        if len(msg) > 4090:
            msg = msg[:4087] + "..."

        self.notifier._send(msg)

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

                # Weekly audit: rebuild validation library, drop underperformers
                try:
                    from helix_v3.analysis.weekly_audit import audit
                    audit_report = audit()
                    logger.info("Weekly audit completed:\n%s", audit_report)
                    self.notifier._send(audit_report)
                except Exception as e:
                    logger.warning("Weekly audit failed: %s", e)

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

        # Verify we connected to the intended account/server. With multiple MT5
        # terminals installed, mt5.initialize() can land on the wrong one.
        from helix_v3.utils.singleton import verify_connected_server
        server_err = verify_connected_server(
            expected_server=settings.mt5.server,
            expected_login=settings.mt5.login,
        )
        if server_err:
            logger.critical("REFUSING TO TRADE: %s", server_err)
            self.engine.disconnect()
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

        # Chart rotation (Tier 3.5): purge stale PNGs at startup, then daily.
        from helix_v3.utils.chart_rotation import rotate_charts
        rotate_charts()
        self._last_chart_rotation = time.monotonic()

        # Fast position-management task (Tier 3.2): trailing/T1/stale exits
        # on their own clock, never waiting for charts/vision/notifications.
        manage_task = asyncio.create_task(self._manage_loop())

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
            manage_task.cancel()
            try:
                await manage_task
            except (asyncio.CancelledError, Exception):
                pass
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


def _setup_signature(analysis) -> str:
    """Stable bucket-string identifying an MTF setup.

    Keyed on the dimensions that should NOT cause a re-entry if they recur soon:
    week phase, H4 cycle level count, H1 session phase, and a coarse confluence
    bucket. Two near-identical scans on the same minute produce the same signature.
    """
    conf = analysis.confluence_score
    conf_bucket = "75plus" if conf >= 75 else "50_74" if conf >= 50 else "lt50"
    return (
        f"{analysis.weekly.week_phase.value}"
        f"|L{analysis.four_hour.level_count}"
        f"|{analysis.one_hour.session_phase.value}"
        f"|{conf_bucket}"
    )


def main() -> None:
    import sys
    from helix_v3.utils.singleton import acquire_singleton_lock, check_mt5_account_conflict

    # Informational: two terminals on the same account aren't blocked — Python only
    # connects to one of them. The real check (verify_connected_server) runs after
    # MT5 initialization inside the orchestrator's run() loop.
    conflict = check_mt5_account_conflict(settings.mt5.login)
    if conflict:
        logger.warning("MT5 TERMINAL CHECK: %s", conflict)

    # Refuse to start if another orchestrator instance holds the lock.
    if acquire_singleton_lock("orchestrator_v2") is None:
        sys.exit(1)
    orchestrator = HelixOrchestratorV2()
    asyncio.run(orchestrator.run())


if __name__ == "__main__":
    main()
