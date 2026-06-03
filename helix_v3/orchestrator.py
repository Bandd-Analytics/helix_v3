"""Helix V3 Pipeline Orchestrator.

Connects all system modules into a continuous execution loop:
  Data Ingestion -> Quant Pre-Filter -> Chart Export -> Vision Consensus -> Execution

Includes:
  - 15-minute market condition scanner
  - WhatsApp notifications via Twilio
  - Trade journal auto-sync

Runs as a persistent service polling for setups across configured symbols.
"""

from __future__ import annotations

import asyncio
import signal
import time
from datetime import datetime, timedelta, timezone
from typing import List, Set

from config.settings import settings
from helix_v3.consensus.validator import MMMConsensusValidator
from helix_v3.core.mtf_analyzer import MTFAnalyzer
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.types import Direction
from helix_v3.execution.gatekeeper import MT5ExecutionGatekeeper
from helix_v3.journal.flashcards import FlashcardSystem
from helix_v3.notifications.whatsapp import WhatsAppNotifier
from helix_v3.scanner.market_scanner import MarketScanner
from helix_v3.utils.logger import get_logger
from helix_v3.visualization.chart_exporter import MMMChartVisualizer

logger = get_logger("orchestrator")

SCAN_INTERVAL_SECONDS = 60          # Trade pipeline poll every 60s
MARKET_SCAN_INTERVAL_SECONDS = 900  # Market scanner every 15 min


class HelixOrchestrator:
    """Main pipeline orchestrator for the Helix V3 MMM system.

    Pipeline per symbol per scan cycle:
    1. Fetch data & compute quant signals (accumulation, stop-hunt, EMA vectors)
    2. If pre-filter passes, export vision-ready chart
    3. Send chart to dual-LLM consensus validator
    4. If consensus reached, build and execute order via MT5
    5. Manage open positions (partial close, breakeven locks)
    6. Every 15 min: full market condition scan + WhatsApp alerts
    """

    def __init__(self) -> None:
        self.engine = MMMQuantitativeEngine()
        self.visualizer = MMMChartVisualizer()
        self.validator = MMMConsensusValidator()
        self.gatekeeper = MT5ExecutionGatekeeper()
        self.scanner: MarketScanner | None = None  # initialized after MT5 connect
        self.mtf: MTFAnalyzer | None = None         # initialized after MT5 connect
        self.flashcards = FlashcardSystem()
        self.notifier = WhatsAppNotifier()
        self._running = False
        self._symbols: List[str] = list(settings.trading.symbols)
        self._last_market_scan: float = 0
        self._last_session: str = ""
        self._reports_sent_today: Set[str] = set()  # Track which reports sent

    def _setup_signals(self) -> None:
        def _stop(signum, frame):
            logger.info("Shutdown signal received (%s)", signum)
            self._running = False

        signal.signal(signal.SIGINT, _stop)
        signal.signal(signal.SIGTERM, _stop)

    async def _process_symbol(self, symbol: str, timeframe: str) -> None:
        """Run the full pipeline for one symbol on one timeframe."""
        try:
            # Step 1: Quantitative pre-filter
            quant_signal = self.engine.generate_signal(symbol, timeframe)

            if not quant_signal.pre_filter_passed:
                logger.debug(
                    "Pre-filter not passed for %s %s, skipping vision.",
                    symbol, timeframe,
                )
                return

            logger.info(
                "PRE-FILTER PASSED: %s %s | accum=%s hunt=%s",
                symbol, timeframe,
                quant_signal.accumulation_active,
                quant_signal.stop_hunt_detected,
            )

            # Step 2: Export vision chart
            df = self.engine.fetch_rates(symbol, timeframe, count=200)
            image_b64, chart_path = self.visualizer.export_vision_matrix(
                df, symbol, timeframe
            )

            # Step 3: Vision consensus
            consensus = await self.validator.evaluate(image_b64, symbol, timeframe)

            if not consensus.agreed:
                logger.info(
                    "No consensus for %s: %s",
                    symbol, consensus.divergence_notes,
                )
                return

            # Notify: valid setup detected
            cycle_lvl = 0
            if consensus.verdicts:
                cl = consensus.verdicts[0].cycle_level
                cycle_lvl = cl.value if cl else 0

            self.notifier.notify_trade_setup(
                symbol=symbol,
                timeframe=timeframe,
                direction=consensus.direction.value,
                confidence=consensus.avg_confidence,
                cycle_level=cycle_lvl,
                readiness=100,
            )

            # Step 4: Build and execute order
            order = self.gatekeeper.build_order(symbol, quant_signal, consensus)
            if order is None:
                logger.info("Order construction blocked for %s", symbol)
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
                    "TRADE EXECUTED: %s %s ticket=%d lots=%.2f",
                    order.direction.value, symbol, ticket, order.lot_size,
                )
                # Notify: trade entered
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
                )
            else:
                logger.warning("Order execution failed for %s", symbol)

        except ConnectionError as e:
            logger.error("Connection error for %s: %s", symbol, e)
        except Exception as e:
            logger.exception("Unexpected error processing %s: %s", symbol, e)

    async def _scan_cycle(self) -> None:
        """Run one scan cycle across all symbols and timeframes."""
        # Manage existing positions and sync journal
        actions = self.gatekeeper.manage_open_positions()
        self.gatekeeper.journal.sync_from_mt5()

        # Notify on trade management actions
        for action in actions:
            self.notifier._send(f"HELIX V3 TRADE MGMT\n{'='*25}\n{action}")

        # 15-minute market condition scan
        now = time.monotonic()
        if now - self._last_market_scan >= MARKET_SCAN_INTERVAL_SECONDS:
            self._run_market_scan()
            self._last_market_scan = now

        # Trade pipeline
        tasks = []
        for symbol in self._symbols:
            for tf in settings.trading.timeframes:
                tasks.append(self._process_symbol(symbol, tf))

        for task in tasks:
            await task

    def _run_market_scan(self) -> None:
        """Execute the 15-minute market condition scan."""
        if not self.scanner:
            return

        try:
            results = self.scanner.scan_all()
            dashboard = self.scanner.print_dashboard()
            logger.info(dashboard)

            # Notify on high-readiness setups
            high = self.scanner.get_high_readiness(min_score=50)
            if high:
                self.notifier.notify_market_conditions(dashboard, high)

            # Session transition detection + scheduled reports
            from helix_v3.scanner.market_scanner import _get_session_name
            current_session = _get_session_name()
            if current_session != self._last_session and self._last_session:
                logger.info("Session transition: %s -> %s", self._last_session, current_session)
                self._send_session_report(self._last_session)
            self._last_session = current_session

            # Check for EOD / weekly / monthly reports
            self._check_scheduled_reports()

        except Exception as e:
            logger.error("Market scan failed: %s", e)

    # ------------------------------------------------------------------
    # Scheduled Reports
    # ------------------------------------------------------------------

    SESSION_NAMES = {
        "ASIAN_EARLY": "Asian Early",
        "ASIAN_LATE": "Asian Late",
        "LONDON_PREMARKET": "London Pre-Market",
        "LONDON": "London",
        "NY_OVERLAP": "NY Overlap",
        "NY_LATE": "NY Late",
    }

    # Session close times in EAT (UTC+3) hours
    SESSION_CLOSE_MAP = {
        "ASIAN_EARLY": "02:00",
        "ASIAN_LATE": "10:00",
        "LONDON_PREMARKET": "11:00",
        "LONDON": "15:00",
        "NY_OVERLAP": "19:00",
        "NY_LATE": "00:00",
    }

    def _send_session_report(self, closed_session: str) -> None:
        """Send report for a session that just ended."""
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
        """Check if EOD, weekly, or monthly reports are due."""
        eat = timezone(timedelta(hours=3))
        now = datetime.now(eat)
        today_key = now.strftime("%Y-%m-%d")
        journal = self.gatekeeper.journal

        # Reset daily tracker at midnight
        if hasattr(self, "_report_date") and self._report_date != today_key:
            self._reports_sent_today.clear()
        self._report_date = today_key

        # --- EOD Report at midnight EAT (hour == 0, minute < 15) ---
        if now.hour == 0 and now.minute < 15:
            report_key = f"eod_{(now - timedelta(days=1)).strftime('%Y-%m-%d')}"
            if report_key not in self._reports_sent_today:
                yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
                stats = journal.get_daily_stats(yesterday)
                self.notifier.notify_period_report(
                    period_name="END OF DAY",
                    period_range=yesterday,
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
                self._reports_sent_today.add(report_key)
                logger.info("EOD report sent for %s", yesterday)

        # --- Weekly Report: Saturday at 00:00-00:15 EAT ---
        if now.weekday() == 5 and now.hour == 0 and now.minute < 15:
            report_key = f"weekly_{today_key}"
            if report_key not in self._reports_sent_today:
                stats = journal.get_weekly_stats()
                monday = (now - timedelta(days=now.weekday())).strftime("%Y-%m-%d")
                friday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
                self.notifier.notify_period_report(
                    period_name="WEEKLY",
                    period_range=f"{monday} to {friday}",
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
                self._reports_sent_today.add(report_key)
                logger.info("Weekly report sent")

        # --- Monthly Report: 1st of month at 00:00-00:15 EAT ---
        if now.day == 1 and now.hour == 0 and now.minute < 15:
            report_key = f"monthly_{today_key}"
            if report_key not in self._reports_sent_today:
                stats = journal.get_monthly_stats()
                last_month = (now - timedelta(days=1)).strftime("%B %Y")
                self.notifier.notify_period_report(
                    period_name="MONTHLY",
                    period_range=last_month,
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
                self._reports_sent_today.add(report_key)
                logger.info("Monthly report sent for %s", last_month)

    async def run(self) -> None:
        """Main event loop. Runs until shutdown signal."""
        self._setup_signals()

        if not self.engine.connect():
            logger.critical("Failed to connect to MT5. Exiting.")
            return

        self.scanner = MarketScanner(self.engine)
        self.mtf = MTFAnalyzer(self.engine)
        self._running = True
        self._last_market_scan = 0  # Force immediate first scan

        logger.info(
            "Helix V3 started | Symbols: %s | Timeframes: %s | WhatsApp: %s",
            self._symbols,
            list(settings.trading.timeframes.keys()),
            "ON" if self.notifier.enabled else "OFF",
        )

        try:
            while self._running:
                cycle_start = time.monotonic()

                await self._scan_cycle()

                elapsed = time.monotonic() - cycle_start
                sleep_time = max(0, SCAN_INTERVAL_SECONDS - elapsed)

                if sleep_time > 0 and self._running:
                    logger.debug("Next scan in %.0fs", sleep_time)
                    await asyncio.sleep(sleep_time)
        finally:
            if self.scanner:
                self.scanner.close()
            self.flashcards.close()
            self.gatekeeper.journal.close()
            self.engine.disconnect()
            logger.info("Helix V3 shutdown complete.")


def main() -> None:
    orchestrator = HelixOrchestrator()
    asyncio.run(orchestrator.run())


if __name__ == "__main__":
    main()
