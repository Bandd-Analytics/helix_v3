"""Historical MMM flashcard miner.

This module is offline-only: it reads historical MT5 candles, mines candidate
MMM setups, saves annotated flashcards with their real historical timestamps,
labels outcomes through MMM event replay, and promotes proven signatures into
the validation library.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import replace
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Optional

import pandas as pd

import helix_v3.core.mtf_analyzer as mtf_module
from config.pair_profiles import get_pair_profile
from config.settings import settings
from helix_v3.backtest.mmm_event_replay import (
    FLASHCARDS_DB_PATH,
    MMMReplayStore,
    ReplaySetup,
    build_setup_signature,
    classify_tdi_state,
    currency_theme_tags,
    label_mmm_event_path,
    nearest_close,
)
from helix_v3.backtest.validation_library import ValidationLibrary
from helix_v3.core.advisory_confidence import advisory_setup_from_mtf, score_advisory_setup
from helix_v3.core.mtf_analyzer import MTFAnalysis, MTFAnalyzer
from helix_v3.core.patterns import scan_patterns
from helix_v3.core.tdi import compute_adr, compute_daily_hilo, compute_pivots, compute_tdi
from helix_v3.core.types import Direction
from helix_v3.journal.flashcards import FlashcardSystem
from helix_v3.utils.logger import get_logger
from helix_v3.visualization.annotated_chart import AnnotatedChartGenerator

logger = get_logger("historical_flashcard_miner")

DEFAULT_RESEARCH_SYMBOLS = "EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD"
DEFAULT_PAIR_RESEARCH_DIR = Path("data/mmm_training/pair_research")
DEFAULT_SCANNER_BASELINE_FAVORABLE_RATE = 85.0
DEFAULT_SCANNER_BASELINE_AVG_EXIT_PIPS = 10.9
FAVORABLE_OUTCOMES = {"TARGET_2", "TRAIL_STOP", "TIME_EXIT_PROFIT", "OPEN_PROFIT"}


class HistoricalSliceEngine:
    """MTFAnalyzer-compatible engine that returns bars up to a snapshot."""

    def __init__(
        self,
        *,
        symbol: str,
        frames: dict[str, pd.DataFrame],
        snapshot_at: datetime,
        pip_size: float,
    ) -> None:
        self._symbol = symbol
        self._frames = frames
        self._snapshot_at = _to_utc(snapshot_at)
        self._pip_size = pip_size

    def fetch_rates(self, symbol: str, timeframe: str, count: int = 1000) -> pd.DataFrame:
        if symbol != self._symbol:
            raise ValueError(f"HistoricalSliceEngine only has data for {self._symbol}")
        df = self._frames[timeframe]
        snap = _timestamp_for_index(self._snapshot_at, df.index)
        past = df[df.index <= snap]
        if past.empty:
            raise ConnectionError(f"No {timeframe} bars available before {self._snapshot_at}")
        return past.tail(count).copy()

    def _get_pip_value(self, symbol: str) -> float:
        if symbol != self._symbol:
            raise ValueError(f"HistoricalSliceEngine only has data for {self._symbol}")
        return self._pip_size


class HistoricalFlashcardMiner:
    """Mine historical MMM candidates and save labeled flashcards."""

    def __init__(
        self,
        *,
        flashcards_db_path: Optional[Path] = None,
        replay_db_path: Optional[Path] = None,
        library_db_path: Optional[Path] = None,
        chart_generator: Optional[AnnotatedChartGenerator] = None,
    ) -> None:
        self._flashcards_db_path = flashcards_db_path or FLASHCARDS_DB_PATH
        self._flashcards = FlashcardSystem(db_path=self._flashcards_db_path)
        self._replay_store = MMMReplayStore(replay_db_path)
        self._library = ValidationLibrary(db_path=library_db_path, replay_db_path=replay_db_path)
        self._chart_generator = chart_generator or AnnotatedChartGenerator()

    def close(self) -> None:
        self._flashcards.close()
        self._replay_store.close()
        self._library.close()

    def mine(
        self,
        *,
        symbols: list[str],
        fetch_rates: Callable[[str, str, datetime, datetime], pd.DataFrame],
        get_pip_size: Callable[[str], float],
        start: datetime,
        end: datetime,
        min_confluence: int = 50,
        step_bars: int = 4,
        limit_per_symbol: int = 100,
        min_spacing_minutes: int = 90,
        require_trade_valid: bool = True,
        generate_charts: bool = True,
        promote_library: bool = True,
    ) -> int:
        total_saved = 0
        for symbol in symbols:
            saved = self.mine_symbol(
                symbol=symbol,
                fetch_rates=fetch_rates,
                get_pip_size=get_pip_size,
                start=start,
                end=end,
                min_confluence=min_confluence,
                step_bars=step_bars,
                limit=limit_per_symbol,
                min_spacing_minutes=min_spacing_minutes,
                require_trade_valid=require_trade_valid,
                generate_charts=generate_charts,
            )
            total_saved += saved
            logger.info("Historical miner saved %d flashcards for %s", saved, symbol)

        if promote_library:
            promoted = self._library.promote_from_replay(min_total=5)
            logger.info("Validation library promoted/reused %d records", promoted)
        return total_saved

    def mine_symbol(
        self,
        *,
        symbol: str,
        fetch_rates: Callable[[str, str, datetime, datetime], pd.DataFrame],
        get_pip_size: Callable[[str], float],
        start: datetime,
        end: datetime,
        min_confluence: int = 50,
        step_bars: int = 4,
        limit: int = 100,
        min_spacing_minutes: int = 90,
        require_trade_valid: bool = True,
        generate_charts: bool = True,
    ) -> int:
        frames = self._fetch_symbol_frames(symbol, fetch_rates, start=start, end=end)
        pip_size = get_pip_size(symbol)
        saved = 0
        last_saved_by_key: dict[str, datetime] = {}

        m15 = frames["M15"]
        candidate_index = [
            _dt_from_index(idx)
            for idx in m15[(m15.index >= _timestamp_for_index(start, m15.index))
                           & (m15.index <= _timestamp_for_index(end, m15.index))].index
        ]
        for offset, snapshot_at in enumerate(candidate_index):
            if offset % max(1, step_bars) != 0:
                continue
            if saved >= limit:
                break
            if self._historical_flashcard_exists(symbol, "M15", snapshot_at):
                continue

            try:
                analysis = self._analyze_snapshot(symbol, frames, snapshot_at, pip_size)
            except Exception as exc:
                logger.debug("Historical analysis skipped %s %s: %s", symbol, snapshot_at, exc)
                continue

            if analysis.confluence_score < min_confluence:
                continue
            if analysis.trade_direction == Direction.NEUTRAL:
                continue
            if require_trade_valid and not analysis.trade_valid:
                continue

            setup_key = f"{symbol}:{analysis.trade_direction.value}"
            last_saved = last_saved_by_key.get(setup_key)
            if last_saved and (snapshot_at - last_saved).total_seconds() < min_spacing_minutes * 60:
                continue

            result = self._save_labeled_flashcard(
                symbol=symbol,
                frames=frames,
                pip_size=pip_size,
                analysis=analysis,
                snapshot_at=snapshot_at,
                generate_chart=generate_charts,
            )
            if result:
                saved += 1
                last_saved_by_key[setup_key] = snapshot_at
        return saved

    def validate_current_setups(
        self,
        *,
        symbols: list[str],
        engine: Any,
    ) -> str:
        analyzer = MTFAnalyzer(engine)
        lines = [
            "",
            "=" * 118,
            "  HELIX V3 CURRENT SETUP VALIDATION",
            "=" * 118,
            f"  {'Symbol':<8} {'Dir':<6} {'Conf':>5} {'Matches':>7} {'BestFav':>8} {'Target':>8} Setup",
            "-" * 118,
        ]
        for symbol in symbols:
            analysis = analyzer.analyze(symbol)
            tdi_result = None
            patterns = None
            try:
                df_m15 = _normalize_df_index(engine.fetch_rates(symbol, "M15", count=240))
                df_d1 = _normalize_df_index(engine.fetch_rates(symbol, "D1", count=220))
                tdi_result = compute_tdi(df_m15)
                hilo = compute_daily_hilo(df_d1) if len(df_d1) >= 2 else {}
                patterns = scan_patterns(
                    df_m15.iloc[-50:],
                    engine._get_pip_value(symbol),
                    prev_hod=hilo.get("phod"),
                    prev_lod=hilo.get("plod"),
                    asian_high=analysis.fifteen_min.asian_range_high,
                    asian_low=analysis.fifteen_min.asian_range_low,
                    session_hour_utc=df_m15.index[-1].hour,
                )
            except Exception as exc:
                logger.warning("Current validation enrichment failed for %s: %s", symbol, exc)
            setup = replay_setup_from_analysis(
                analysis,
                tdi_result=tdi_result,
                patterns=patterns,
                source="current_scan",
                source_id=0,
            )
            matches = self._library.validate_setup(setup)
            best = matches[0] if matches else None
            lines.append(
                f"  {symbol:<8} {analysis.trade_direction.value:<6} "
                f"{analysis.confluence_score:>5} {len(matches):>7} "
                f"{_fmt(best.favorable_rate if best else None):>8} "
                f"{_fmt(best.realistic_target_pips if best else None):>8} "
                f"{best.normalized_key if best else 'no historical validation match'}"
            )
        lines.append("=" * 118)
        return "\n".join(lines)

    def export_pair_research_archive(
        self,
        *,
        symbols: list[str],
        output_root: Path = DEFAULT_PAIR_RESEARCH_DIR,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        min_total: int = 5,
        min_favorable_rate: float = 55.0,
        min_avg_exit_pips: float = 0.0,
        baseline_favorable_rate: float = DEFAULT_SCANNER_BASELINE_FAVORABLE_RATE,
        baseline_avg_exit_pips: float = DEFAULT_SCANNER_BASELINE_AVG_EXIT_PIPS,
        split_min_total: int = 3,
        required_split_passes: int = 0,
        validation_days: int = 365,
        out_of_sample_days: int = 180,
        max_examples: int = 50,
        scanner_baseline: str = "",
    ) -> list[Path]:
        output_root.mkdir(parents=True, exist_ok=True)
        written: list[Path] = []
        split_windows = _split_windows(
            start=start,
            end=end,
            validation_days=validation_days,
            out_of_sample_days=out_of_sample_days,
        )
        index_lines = [
            "# MMM Pair Research Archive",
            "",
            f"Generated: {datetime.now(timezone.utc).isoformat()}",
            "",
            "Scope: pair-specific historical flashcards and MMM event replay outcomes.",
            "Promotion remains pair-specific unless cross-pair convergence is separately validated.",
            "",
            "| Pair | Historical Cards | Direct Profit | Best Baseline-Qualified Setup | Fav% | AvgExit | SplitPass | Archive |",
            "|---|---:|---:|---|---:|---:|---:|---|",
        ]

        for symbol in symbols:
            summary = self._pair_flashcard_summary(symbol)
            setup_rows = self._pair_setup_performance(symbol, min_total=min_total)
            self._attach_split_stats(
                symbol,
                setup_rows,
                split_windows=split_windows,
                baseline_favorable_rate=baseline_favorable_rate,
                baseline_avg_exit_pips=baseline_avg_exit_pips,
                split_min_total=split_min_total,
            )
            examples = self._pair_profitable_flashcards(symbol, limit=max_examples)
            baseline_rows = [
                row for row in setup_rows
                if _is_baseline_qualified(
                    row,
                    min_total=min_total,
                    baseline_favorable_rate=baseline_favorable_rate,
                    baseline_avg_exit_pips=baseline_avg_exit_pips,
                    required_split_passes=required_split_passes,
                )
            ]
            research_rows = [
                row for row in setup_rows
                if _is_research_candidate(
                    row,
                    min_total=min_total,
                    min_favorable_rate=min_favorable_rate,
                    min_avg_exit_pips=min_avg_exit_pips,
                )
            ]
            pair_dir = output_root / symbol
            pair_dir.mkdir(parents=True, exist_ok=True)
            setup_path = pair_dir / "setup_performance.json"
            examples_path = pair_dir / "profitable_flashcards.jsonl"
            summary_path = pair_dir / "SUMMARY.md"

            setup_path.write_text(json.dumps(setup_rows, indent=2, sort_keys=True), encoding="utf-8")
            examples_path.write_text(
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in examples),
                encoding="utf-8",
            )
            summary_path.write_text(
                _format_pair_summary_markdown(
                    symbol=symbol,
                    summary=summary,
                    setup_rows=setup_rows,
                    baseline_rows=baseline_rows,
                    research_rows=research_rows,
                    examples=examples,
                    start=start,
                    end=end,
                    scanner_baseline=scanner_baseline,
                    min_total=min_total,
                    min_favorable_rate=min_favorable_rate,
                    min_avg_exit_pips=min_avg_exit_pips,
                    baseline_favorable_rate=baseline_favorable_rate,
                    baseline_avg_exit_pips=baseline_avg_exit_pips,
                    split_min_total=split_min_total,
                    required_split_passes=required_split_passes,
                    split_windows=split_windows,
                ),
                encoding="utf-8",
            )
            written.extend([setup_path, examples_path, summary_path])
            best = baseline_rows[0] if baseline_rows else {}
            index_lines.append(
                f"| {symbol} | {summary['total']} | {summary['direct_profit']} | "
                f"{_md_cell(best.get('normalized_key', 'none'))} | "
                f"{_fmt_pct(best.get('favorable_rate'))} | "
                f"{_fmt_plain(best.get('avg_exit_pips'))} | "
                f"{best.get('baseline_split_passes', '-') if best else '-'} | "
                f"[SUMMARY](./{symbol}/SUMMARY.md) |"
            )

        index_path = output_root / "INDEX.md"
        index_path.write_text("\n".join(index_lines) + "\n", encoding="utf-8")
        written.append(index_path)
        return written

    def _fetch_symbol_frames(
        self,
        symbol: str,
        fetch_rates: Callable[[str, str, datetime, datetime], pd.DataFrame],
        *,
        start: datetime,
        end: datetime,
    ) -> dict[str, pd.DataFrame]:
        frame_ranges = {
            "M15": (start - timedelta(days=10), end + timedelta(hours=8)),
            "H1": (start - timedelta(days=21), end + timedelta(hours=8)),
            "H4": (start - timedelta(days=45), end + timedelta(hours=8)),
            "D1": (start - timedelta(days=260), end + timedelta(days=2)),
        }
        frames: dict[str, pd.DataFrame] = {}
        for timeframe, (tf_start, tf_end) in frame_ranges.items():
            frames[timeframe] = _normalize_df_index(
                _fetch_rates_chunked(fetch_rates, symbol, timeframe, tf_start, tf_end)
            )
        return frames

    def _analyze_snapshot(
        self,
        symbol: str,
        frames: dict[str, pd.DataFrame],
        snapshot_at: datetime,
        pip_size: float,
    ) -> MTFAnalysis:
        engine = HistoricalSliceEngine(
            symbol=symbol,
            frames=frames,
            snapshot_at=snapshot_at,
            pip_size=pip_size,
        )
        original_now = mtf_module.now_utc
        mtf_module.now_utc = lambda: _to_utc(snapshot_at)
        try:
            analysis = MTFAnalyzer(engine).analyze(symbol)
        finally:
            mtf_module.now_utc = original_now
        analysis.timestamp = _to_utc(snapshot_at)
        return analysis

    def _save_labeled_flashcard(
        self,
        *,
        symbol: str,
        frames: dict[str, pd.DataFrame],
        pip_size: float,
        analysis: MTFAnalysis,
        snapshot_at: datetime,
        generate_chart: bool,
    ) -> bool:
        df_m15 = _past_frame(frames["M15"], snapshot_at, bars=240)
        df_d1 = _past_frame(frames["D1"], snapshot_at, bars=220)
        if len(df_m15) < 60 or len(df_d1) < 2:
            return False

        tdi_result = compute_tdi(df_m15)
        hilo = compute_daily_hilo(df_d1)
        prev_hod = float(hilo["phod"]) if hilo.get("phod") else 0.0
        prev_lod = float(hilo["plod"]) if hilo.get("plod") else 0.0
        patterns = scan_patterns(
            df_m15.iloc[-50:],
            pip_size,
            prev_hod=prev_hod or None,
            prev_lod=prev_lod or None,
            asian_high=analysis.fifteen_min.asian_range_high,
            asian_low=analysis.fifteen_min.asian_range_low,
            session_hour_utc=df_m15.index[-1].hour,
        )

        chart_path = ""
        if generate_chart:
            pivots = _compute_pivots_safe(df_d1)
            adr = compute_adr(df_d1) if len(df_d1) >= 14 else 0.0
            try:
                _, path = self._chart_generator.generate_from_mtf(
                    df_m15,
                    symbol,
                    "M15",
                    analysis,
                    tdi_result=tdi_result,
                    pattern_scan=patterns,
                    pivots=pivots,
                    adr=adr,
                    prev_hod=prev_hod,
                    prev_lod=prev_lod,
                )
                chart_path = str(path)
            except Exception as exc:
                logger.warning("Historical chart generation failed %s %s: %s", symbol, snapshot_at, exc)

        setup = replay_setup_from_analysis(
            analysis,
            tdi_result=tdi_result,
            patterns=patterns,
            source="historical_flashcard",
            source_id=0,
        )
        profile = get_pair_profile(symbol)
        replay_window = _window_frame(
            frames["M15"],
            snapshot_at - timedelta(days=3),
            snapshot_at + timedelta(minutes=profile.max_duration_minutes + 30),
        )
        entry = nearest_close(replay_window, snapshot_at)
        if entry is None:
            return False
        outcome = label_mmm_event_path(
            replay_window,
            setup=setup,
            entry_price=entry,
            pip_size=pip_size,
            profile=profile,
        )

        advisory_setup = advisory_setup_from_mtf(analysis, tdi_result=tdi_result, patterns=patterns)
        advisory = score_advisory_setup(advisory_setup)
        context = flashcard_context_from_analysis(
            analysis,
            tdi_result=tdi_result,
            patterns=patterns,
            advisory=advisory,
        )
        tags = [
            "historical",
            outcome.outcome,
            analysis.trade_direction.value,
            f"L{analysis.four_hour.level_count}",
            analysis.weekly.week_phase.value,
        ]
        flashcard_id = self._flashcards.save_historical_flashcard(
            symbol=symbol,
            timeframe="M15",
            chart_path=chart_path,
            mtf_context=context,
            snapshot_at=snapshot_at,
            tags=tags,
            notes=f"Historical MMM replay: {outcome.outcome}",
        )
        self._flashcards.record_outcome_by_id(
            flashcard_id,
            outcome=outcome.outcome,
            pips_gained=float(outcome.exit_pips or 0.0),
            duration_minutes=_duration_minutes(snapshot_at, outcome.exit_at),
            exit_reason=outcome.notes or outcome.outcome,
            t1_hit=outcome.t1_hit,
        )

        setup = replace(setup, source_id=flashcard_id)
        signature = build_setup_signature(setup, profile)
        signature_id = self._replay_store.record_signature(signature)
        self._replay_store.record_outcome(
            replace(outcome, source="historical_flashcard", source_id=flashcard_id),
            signature_id,
        )
        return True

    def _historical_flashcard_exists(
        self,
        symbol: str,
        timeframe: str,
        snapshot_at: datetime,
    ) -> bool:
        conn = sqlite3.connect(str(self._flashcards_db_path))
        try:
            row = conn.execute(
                """SELECT id FROM flashcards
                WHERE symbol = ? AND timeframe = ? AND snapshot_type = 'HISTORICAL'
                  AND snapshot_at = ?
                LIMIT 1""",
                (symbol, timeframe, _to_utc(snapshot_at).isoformat()),
            ).fetchone()
            return row is not None
        finally:
            conn.close()

    def _pair_flashcard_summary(self, symbol: str) -> dict[str, Any]:
        conn = sqlite3.connect(str(self._flashcards_db_path))
        conn.row_factory = sqlite3.Row
        try:
            row = conn.execute(
                """SELECT
                    COUNT(*) AS total,
                    SUM(CASE WHEN pips_gained > 0 THEN 1 ELSE 0 END) AS direct_profit,
                    SUM(CASE WHEN t1_hit = 1 THEN 1 ELSE 0 END) AS t1_hits,
                    AVG(pips_gained) AS avg_pips,
                    AVG(CASE WHEN pips_gained > 0 THEN pips_gained END) AS avg_profit_pips,
                    MIN(snapshot_at) AS first_snapshot,
                    MAX(snapshot_at) AS last_snapshot
                FROM flashcards
                WHERE symbol = ? AND snapshot_type = 'HISTORICAL'""",
                (symbol,),
            ).fetchone()
        finally:
            conn.close()
        total = int((row or {})["total"] or 0)
        direct_profit = int((row or {})["direct_profit"] or 0)
        t1_hits = int((row or {})["t1_hits"] or 0)
        return {
            "symbol": symbol,
            "total": total,
            "direct_profit": direct_profit,
            "direct_profit_rate": direct_profit / total * 100.0 if total else 0.0,
            "t1_hits": t1_hits,
            "t1_rate": t1_hits / total * 100.0 if total else 0.0,
            "avg_pips": _optional_float((row or {})["avg_pips"] if row else None),
            "avg_profit_pips": _optional_float((row or {})["avg_profit_pips"] if row else None),
            "first_snapshot": str((row or {})["first_snapshot"] or ""),
            "last_snapshot": str((row or {})["last_snapshot"] or ""),
        }

    def _pair_setup_performance(self, symbol: str, *, min_total: int) -> list[dict[str, Any]]:
        conn = sqlite3.connect(str(self._replay_store._db_path))
        conn.row_factory = sqlite3.Row
        try:
            rows = conn.execute(
                """SELECT
                    s.symbol,
                    s.direction,
                    s.normalized_key,
                    MIN(s.raw_key) AS raw_key,
                    s.setup_family,
                    s.primary_theme,
                    COUNT(*) AS total,
                    SUM(CASE WHEN o.outcome IN ('TARGET_2', 'TRAIL_STOP',
                        'TIME_EXIT_PROFIT', 'OPEN_PROFIT') THEN 1 ELSE 0 END) AS favorable,
                    SUM(CASE WHEN o.exit_pips > 0 THEN 1 ELSE 0 END) AS direct_profit,
                    SUM(CASE WHEN o.t1_hit = 1 THEN 1 ELSE 0 END) AS t1_hits,
                    AVG(o.exit_pips) AS avg_exit_pips,
                    AVG(o.max_favorable_pips) AS avg_mfe,
                    AVG(o.max_adverse_pips) AS avg_mae,
                    MIN(o.snapshot_at) AS first_snapshot,
                    MAX(o.snapshot_at) AS last_snapshot,
                    GROUP_CONCAT(CASE WHEN o.exit_pips > 0 THEN o.source_id END) AS profitable_source_ids
                FROM mmm_setup_signatures s
                JOIN mmm_event_outcomes o
                  ON o.source = s.source AND o.source_id = s.source_id
                WHERE s.symbol = ?
                  AND s.source = 'historical_flashcard'
                GROUP BY s.symbol, s.direction, s.normalized_key,
                         s.setup_family, s.primary_theme
                HAVING total >= ?""",
                (symbol, min_total),
            ).fetchall()
        finally:
            conn.close()

        records = [_setup_performance_record(row) for row in rows]
        return sorted(
            records,
            key=lambda item: (
                item["favorable_rate"],
                item["avg_exit_pips"] if item["avg_exit_pips"] is not None else -999.0,
                item["total"],
            ),
            reverse=True,
        )

    def _pair_profitable_flashcards(self, symbol: str, *, limit: int) -> list[dict[str, Any]]:
        conn = sqlite3.connect(str(self._flashcards_db_path))
        conn.row_factory = sqlite3.Row
        try:
            rows = conn.execute(
                """SELECT
                    id,
                    snapshot_at,
                    symbol,
                    timeframe,
                    entry_direction,
                    outcome,
                    pips_gained,
                    duration_minutes,
                    t1_hit,
                    chart_path,
                    weekly_phase,
                    weekly_trend,
                    h4_level,
                    h4_trend,
                    h1_session,
                    h1_trend,
                    asian_range_pips,
                    stop_hunt_detected,
                    stop_hunt_direction,
                    stop_hunt_pips,
                    push_count,
                    m_w_pattern,
                    rrt_detected,
                    tdi_signals,
                    tdi_shark_fin,
                    tdi_shark_direction,
                    pattern_trade_type,
                    confluence_score,
                    advisory_confidence_score,
                    advisory_grade,
                    tags,
                    notes
                FROM flashcards
                WHERE symbol = ?
                  AND snapshot_type = 'HISTORICAL'
                  AND pips_gained > 0
                ORDER BY pips_gained DESC, t1_hit DESC, confluence_score DESC
                LIMIT ?""",
                (symbol, limit),
            ).fetchall()
        finally:
            conn.close()
        return [_flashcard_archive_record(row) for row in rows]

    def _attach_split_stats(
        self,
        symbol: str,
        setup_rows: list[dict[str, Any]],
        *,
        split_windows: list[dict[str, Any]],
        baseline_favorable_rate: float,
        baseline_avg_exit_pips: float,
        split_min_total: int,
    ) -> None:
        if not setup_rows or not split_windows:
            return
        split_map = self._pair_setup_split_performance(symbol, split_windows=split_windows)
        for row in setup_rows:
            key = _row_key(row)
            stats = split_map.get(key, {})
            row["split_stats"] = stats
            row["baseline_split_passes"] = sum(
                1
                for split in stats.values()
                if _split_passes_baseline(
                    split,
                    split_min_total=split_min_total,
                    baseline_favorable_rate=baseline_favorable_rate,
                    baseline_avg_exit_pips=baseline_avg_exit_pips,
                )
            )

    def _pair_setup_split_performance(
        self,
        symbol: str,
        *,
        split_windows: list[dict[str, Any]],
    ) -> dict[str, dict[str, dict[str, Any]]]:
        conn = sqlite3.connect(str(self._replay_store._db_path))
        conn.row_factory = sqlite3.Row
        try:
            grouped: dict[str, dict[str, dict[str, Any]]] = {}
            for window in split_windows:
                rows = conn.execute(
                    """SELECT
                        s.symbol,
                        s.direction,
                        s.normalized_key,
                        COUNT(*) AS total,
                        SUM(CASE WHEN o.outcome IN ('TARGET_2', 'TRAIL_STOP',
                            'TIME_EXIT_PROFIT', 'OPEN_PROFIT') THEN 1 ELSE 0 END) AS favorable,
                        SUM(CASE WHEN o.exit_pips > 0 THEN 1 ELSE 0 END) AS direct_profit,
                        SUM(CASE WHEN o.t1_hit = 1 THEN 1 ELSE 0 END) AS t1_hits,
                        AVG(o.exit_pips) AS avg_exit_pips,
                        AVG(o.max_favorable_pips) AS avg_mfe,
                        AVG(o.max_adverse_pips) AS avg_mae
                    FROM mmm_setup_signatures s
                    JOIN mmm_event_outcomes o
                      ON o.source = s.source AND o.source_id = s.source_id
                    WHERE s.symbol = ?
                      AND s.source = 'historical_flashcard'
                      AND o.snapshot_at >= ?
                      AND o.snapshot_at < ?
                    GROUP BY s.symbol, s.direction, s.normalized_key""",
                    (
                        symbol,
                        _to_utc(window["start"]).isoformat(),
                        _to_utc(window["end"]).isoformat(),
                    ),
                ).fetchall()
                for row in rows:
                    key = _row_key(
                        {
                            "symbol": row["symbol"],
                            "direction": row["direction"],
                            "normalized_key": row["normalized_key"],
                        }
                    )
                    grouped.setdefault(key, {})[window["name"]] = _split_performance_record(row)
            return grouped
        finally:
            conn.close()


def replay_setup_from_analysis(
    analysis: MTFAnalysis,
    *,
    tdi_result: Any = None,
    patterns: Any = None,
    source: str = "historical_flashcard",
    source_id: int = 0,
) -> ReplaySetup:
    tdi_signals = []
    if tdi_result is not None:
        tdi_signals = [signal.value for signal in tdi_result.signals if signal.value != "NONE"]
    pattern_trade_type = patterns.trade_type.value if patterns is not None else ""
    return ReplaySetup(
        symbol=analysis.symbol,
        timeframe="M15",
        snapshot_at=analysis.timestamp,
        direction=analysis.trade_direction,
        confluence_score=analysis.confluence_score,
        weekly_phase=analysis.weekly.week_phase.value,
        weekly_trend=analysis.weekly.trend_direction,
        h4_level=analysis.four_hour.level_count,
        h4_trend=analysis.four_hour.trend_direction,
        h1_session=analysis.one_hour.session_phase.value,
        h1_trend=analysis.one_hour.trend_direction,
        asian_range_pips=analysis.fifteen_min.asian_range_pips,
        accumulation_valid=analysis.fifteen_min.accumulation_valid,
        stop_hunt_detected=analysis.fifteen_min.stop_hunt_detected,
        stop_hunt_direction=analysis.fifteen_min.stop_hunt_direction,
        stop_hunt_pips=analysis.fifteen_min.stop_hunt_pips,
        push_count=analysis.fifteen_min.push_count,
        m_w_forming=analysis.fifteen_min.m_w_forming,
        m_w_pattern=analysis.fifteen_min.m_w_pattern,
        rrt_detected=analysis.fifteen_min.rrt_detected,
        tdi_signals=tdi_signals,
        tdi_shark_fin=bool(getattr(tdi_result, "shark_fin_active", False)),
        tdi_shark_direction=str(getattr(tdi_result, "shark_fin_direction", "") or ""),
        tdi_vb_squeeze=bool(getattr(tdi_result, "vb_squeeze", False)),
        tdi_divergence=str(getattr(tdi_result, "divergence", "") or ""),
        tdi_crossed_signal=str(getattr(tdi_result, "rsi_crossed_signal", "") or ""),
        tdi_rsi=_optional_float(getattr(tdi_result, "rsi", None)),
        tdi_signal=_optional_float(getattr(tdi_result, "signal", None)),
        tdi_base=_optional_float(getattr(tdi_result, "base", None)),
        pattern_trade_type=pattern_trade_type,
        pattern_count=len(patterns.patterns) if patterns is not None else 0,
        pattern_rrt_count=patterns.rrt_count if patterns is not None else 0,
        pattern_spike_count=patterns.spike_count if patterns is not None else 0,
        pattern_pin_bar_count=patterns.pin_bar_count if patterns is not None else 0,
        pattern_half_batman=patterns.half_batman if patterns is not None else False,
        setup_class=pattern_trade_type,
        source=source,
        source_id=source_id,
    )


def flashcard_context_from_analysis(
    analysis: MTFAnalysis,
    *,
    tdi_result: Any,
    patterns: Any,
    advisory: Any,
) -> dict[str, Any]:
    direction = analysis.trade_direction.value
    setup = replay_setup_from_analysis(analysis, tdi_result=tdi_result, patterns=patterns)
    tdi_state = classify_tdi_state(setup)
    return {
        "weekly": {
            "cycle_position": analysis.weekly.cycle_position.value,
            "week_phase": analysis.weekly.week_phase.value,
            "trend_direction": analysis.weekly.trend_direction.value,
            "days_since_peak": analysis.weekly.days_since_peak,
        },
        "four_hour": {
            "cycle_position": analysis.four_hour.cycle_position.value,
            "level_count": analysis.four_hour.level_count,
            "trend_direction": analysis.four_hour.trend_direction.value,
            "is_choppy": analysis.four_hour.is_choppy,
        },
        "one_hour": {
            "session_phase": analysis.one_hour.session_phase.value,
            "trend_direction": analysis.one_hour.trend_direction.value,
            "intraday_level": analysis.one_hour.intraday_level,
            "hod_locked": analysis.one_hour.hod_locked,
            "lod_locked": analysis.one_hour.lod_locked,
            "ema_50_200_cross": analysis.one_hour.ema_50_200_cross,
        },
        "fifteen_min": {
            "asian_range_pips": analysis.fifteen_min.asian_range_pips,
            "accumulation_valid": analysis.fifteen_min.accumulation_valid,
            "stop_hunt_detected": analysis.fifteen_min.stop_hunt_detected,
            "stop_hunt_direction": analysis.fifteen_min.stop_hunt_direction.value,
            "stop_hunt_pips": analysis.fifteen_min.stop_hunt_pips,
            "push_count": analysis.fifteen_min.push_count,
            "m_w_forming": analysis.fifteen_min.m_w_forming,
            "m_w_pattern": analysis.fifteen_min.m_w_pattern,
            "rrt_detected": analysis.fifteen_min.rrt_detected,
            "entry_direction": direction,
            "entry_confidence": analysis.fifteen_min.entry_confidence,
        },
        "ema": {
            "ema_5_angle": analysis.four_hour.ema_vector.ema_5_angle,
            "ema_13_angle": analysis.four_hour.ema_vector.ema_13_angle,
            "ema_50_angle": analysis.four_hour.ema_vector.ema_50_angle,
            "ema_200_angle": analysis.four_hour.ema_vector.ema_200_angle,
            "ema_800_angle": analysis.four_hour.ema_vector.ema_800_angle,
            "fast_slow_div": analysis.four_hour.ema_vector.fast_slow_divergence,
        },
        "tdi": {
            "signals": [signal.value for signal in tdi_result.signals if signal.value != "NONE"],
            "shark_fin_active": tdi_result.shark_fin_active,
            "shark_fin_direction": tdi_result.shark_fin_direction,
            "vb_squeeze": tdi_result.vb_squeeze,
            "divergence": tdi_result.divergence,
            "crossed_signal": tdi_result.rsi_crossed_signal,
            "rsi": tdi_result.rsi,
            "signal": tdi_result.signal,
            "base": tdi_result.base,
            "state": tdi_state,
        },
        "patterns": {
            "trade_type": patterns.trade_type.value,
            "pattern_count": len(patterns.patterns),
            "pattern_types": [pattern.pattern.value for pattern in patterns.patterns],
            "rrt_count": patterns.rrt_count,
            "spike_count": patterns.spike_count,
            "pin_bar_count": patterns.pin_bar_count,
            "m_w_detected": patterns.m_w_detected,
            "half_batman": patterns.half_batman,
        },
        "convergence": {
            "themes": currency_theme_tags(analysis.symbol, analysis.trade_direction),
            "theme_score": advisory.convergence_score,
        },
        "advisory": {
            "confidence_score": advisory.final_score,
            "grade": advisory.grade,
            "action": advisory.action,
            "reasons": advisory.reasons,
            "blockers": advisory.blockers,
            "peer_symbols": advisory.peer_symbols,
        },
        "profile": {
            "risk_tier": analysis.pair_profile.risk_tier,
            "max_risk_pct": analysis.pair_profile.max_risk_pct,
        },
        "confluence_score": analysis.confluence_score,
    }


def _compute_pivots_safe(df_d1: pd.DataFrame) -> Optional[dict[str, float]]:
    if len(df_d1) < 2:
        return None
    prev_d = df_d1.iloc[-2]
    prev_bullish = bool(prev_d["Close"] > prev_d["Open"])
    return compute_pivots(prev_d["High"], prev_d["Low"], prev_d["Close"], prev_bullish)


def _fetch_rates_chunked(
    fetch_rates: Callable[[str, str, datetime, datetime], pd.DataFrame],
    symbol: str,
    timeframe: str,
    start: datetime,
    end: datetime,
) -> pd.DataFrame:
    chunk_days = {
        "M15": 90,
        "H1": 180,
        "H4": 365,
        "D1": 1095,
    }.get(timeframe, 90)
    chunks: list[pd.DataFrame] = []
    cursor = _to_utc(start)
    end = _to_utc(end)
    while cursor < end:
        chunk_end = min(cursor + timedelta(days=chunk_days), end)
        chunks.extend(
            _fetch_rates_chunk_or_split(
                fetch_rates,
                symbol,
                timeframe,
                cursor,
                chunk_end,
                min_chunk_days=7,
            )
        )
        cursor = chunk_end
    if not chunks:
        return fetch_rates(symbol, timeframe, start, end)
    combined = pd.concat(chunks).sort_index()
    return combined[~combined.index.duplicated(keep="last")]


def _fetch_rates_chunk_or_split(
    fetch_rates: Callable[[str, str, datetime, datetime], pd.DataFrame],
    symbol: str,
    timeframe: str,
    start: datetime,
    end: datetime,
    *,
    min_chunk_days: int,
) -> list[pd.DataFrame]:
    try:
        df = fetch_rates(symbol, timeframe, start, end)
    except Exception as exc:
        span = end - start
        if span <= timedelta(days=min_chunk_days):
            logger.warning(
                "Skipping unavailable MT5 history chunk %s %s %s -> %s: %s",
                symbol,
                timeframe,
                start.isoformat(),
                end.isoformat(),
                exc,
            )
            return []
        midpoint = start + span / 2
        return [
            *_fetch_rates_chunk_or_split(
                fetch_rates,
                symbol,
                timeframe,
                start,
                midpoint,
                min_chunk_days=min_chunk_days,
            ),
            *_fetch_rates_chunk_or_split(
                fetch_rates,
                symbol,
                timeframe,
                midpoint,
                end,
                min_chunk_days=min_chunk_days,
            ),
        ]
    if df.empty:
        return []
    return [df]


def _past_frame(df: pd.DataFrame, snapshot_at: datetime, *, bars: int) -> pd.DataFrame:
    snap = _timestamp_for_index(snapshot_at, df.index)
    return df[df.index <= snap].tail(bars).copy()


def _window_frame(df: pd.DataFrame, start: datetime, end: datetime) -> pd.DataFrame:
    start_ts = _timestamp_for_index(start, df.index)
    end_ts = _timestamp_for_index(end, df.index)
    return df[(df.index >= start_ts) & (df.index <= end_ts)].copy()


def _duration_minutes(start: datetime, end: Optional[datetime]) -> float:
    if end is None:
        return 0.0
    return max(0.0, (_to_utc(end) - _to_utc(start)).total_seconds() / 60.0)


def _normalize_df_index(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    out = df.copy()
    if not isinstance(out.index, pd.DatetimeIndex):
        raise TypeError("Historical miner dataframes must use a DatetimeIndex")
    if out.index.tz is None:
        out.index = out.index.tz_localize(timezone.utc)
    else:
        out.index = out.index.tz_convert(timezone.utc)
    return out


def _timestamp_for_index(dt: datetime, index: pd.DatetimeIndex) -> pd.Timestamp:
    ts = pd.Timestamp(_to_utc(dt))
    if index.tz is None:
        return ts.tz_localize(None)
    return ts.tz_convert(index.tz)


def _dt_from_index(idx: Any) -> datetime:
    ts = pd.Timestamp(idx)
    if ts.tzinfo is None:
        ts = ts.tz_localize(timezone.utc)
    return ts.to_pydatetime().astimezone(timezone.utc)


def _to_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _optional_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _parse_symbols(raw: str) -> list[str]:
    return [symbol.strip().upper() for symbol in raw.split(",") if symbol.strip()]


def _parse_date(value: Optional[str], default: datetime) -> datetime:
    if not value:
        return default
    return _to_utc(datetime.fromisoformat(value.replace("Z", "+00:00")))


def _fmt(value: Any) -> str:
    return "-" if value is None else f"{float(value):+.1f}"


def _setup_performance_record(row: sqlite3.Row) -> dict[str, Any]:
    total = int(row["total"] or 0)
    favorable = int(row["favorable"] or 0)
    direct_profit = int(row["direct_profit"] or 0)
    t1_hits = int(row["t1_hits"] or 0)
    avg_exit = _optional_float(row["avg_exit_pips"])
    avg_mfe = _optional_float(row["avg_mfe"])
    avg_mae = _optional_float(row["avg_mae"])
    t1_rate = t1_hits / total * 100.0 if total else 0.0
    return {
        "symbol": str(row["symbol"]),
        "direction": str(row["direction"] or ""),
        "normalized_key": str(row["normalized_key"] or ""),
        "raw_key": str(row["raw_key"] or ""),
        "setup_family": str(row["setup_family"] or ""),
        "primary_theme": str(row["primary_theme"] or ""),
        "total": total,
        "favorable": favorable,
        "favorable_rate": favorable / total * 100.0 if total else 0.0,
        "direct_profit": direct_profit,
        "direct_profit_rate": direct_profit / total * 100.0 if total else 0.0,
        "t1_hits": t1_hits,
        "t1_rate": t1_rate,
        "avg_exit_pips": avg_exit,
        "avg_mfe": avg_mfe,
        "avg_mae": avg_mae,
        "realistic_target_pips": _realistic_target(avg_exit, avg_mfe, t1_rate),
        "first_snapshot": str(row["first_snapshot"] or ""),
        "last_snapshot": str(row["last_snapshot"] or ""),
        "profitable_source_ids": [
            int(value)
            for value in str(row["profitable_source_ids"] or "").split(",")
            if value.strip().isdigit()
        ][:50],
    }


def _split_performance_record(row: sqlite3.Row) -> dict[str, Any]:
    total = int(row["total"] or 0)
    favorable = int(row["favorable"] or 0)
    direct_profit = int(row["direct_profit"] or 0)
    t1_hits = int(row["t1_hits"] or 0)
    avg_exit = _optional_float(row["avg_exit_pips"])
    avg_mfe = _optional_float(row["avg_mfe"])
    avg_mae = _optional_float(row["avg_mae"])
    return {
        "total": total,
        "favorable": favorable,
        "favorable_rate": favorable / total * 100.0 if total else 0.0,
        "direct_profit": direct_profit,
        "direct_profit_rate": direct_profit / total * 100.0 if total else 0.0,
        "t1_hits": t1_hits,
        "t1_rate": t1_hits / total * 100.0 if total else 0.0,
        "avg_exit_pips": avg_exit,
        "avg_mfe": avg_mfe,
        "avg_mae": avg_mae,
    }


def _flashcard_archive_record(row: sqlite3.Row) -> dict[str, Any]:
    return {
        "flashcard_id": int(row["id"]),
        "snapshot_at": str(row["snapshot_at"] or ""),
        "symbol": str(row["symbol"] or ""),
        "timeframe": str(row["timeframe"] or ""),
        "direction": str(row["entry_direction"] or ""),
        "outcome": str(row["outcome"] or ""),
        "pips_gained": _optional_float(row["pips_gained"]),
        "duration_minutes": _optional_float(row["duration_minutes"]),
        "t1_hit": bool(row["t1_hit"]),
        "chart_path": str(row["chart_path"] or ""),
        "weekly_phase": str(row["weekly_phase"] or ""),
        "weekly_trend": str(row["weekly_trend"] or ""),
        "h4_level": int(row["h4_level"] or 0),
        "h4_trend": str(row["h4_trend"] or ""),
        "h1_session": str(row["h1_session"] or ""),
        "h1_trend": str(row["h1_trend"] or ""),
        "asian_range_pips": _optional_float(row["asian_range_pips"]),
        "stop_hunt_detected": bool(row["stop_hunt_detected"]),
        "stop_hunt_direction": str(row["stop_hunt_direction"] or ""),
        "stop_hunt_pips": _optional_float(row["stop_hunt_pips"]),
        "push_count": int(row["push_count"] or 0),
        "m_w_pattern": str(row["m_w_pattern"] or ""),
        "rrt_detected": bool(row["rrt_detected"]),
        "tdi_signals": _load_json_list(row["tdi_signals"]),
        "tdi_shark_fin": bool(row["tdi_shark_fin"]),
        "tdi_shark_direction": str(row["tdi_shark_direction"] or ""),
        "pattern_trade_type": str(row["pattern_trade_type"] or ""),
        "confluence_score": int(row["confluence_score"] or 0),
        "advisory_confidence_score": _optional_float(row["advisory_confidence_score"]),
        "advisory_grade": str(row["advisory_grade"] or ""),
        "tags": _load_json_list(row["tags"]),
        "notes": str(row["notes"] or ""),
    }


def _is_research_candidate(
    row: dict[str, Any],
    *,
    min_total: int,
    min_favorable_rate: float,
    min_avg_exit_pips: float,
) -> bool:
    return (
        int(row["total"]) >= min_total
        and float(row["favorable_rate"]) >= min_favorable_rate
        and (_optional_float(row["avg_exit_pips"]) or 0.0) >= min_avg_exit_pips
        and int(row["direct_profit"]) > 0
    )


def _is_baseline_qualified(
    row: dict[str, Any],
    *,
    min_total: int,
    baseline_favorable_rate: float,
    baseline_avg_exit_pips: float,
    required_split_passes: int,
) -> bool:
    if not _is_research_candidate(
        row,
        min_total=min_total,
        min_favorable_rate=baseline_favorable_rate,
        min_avg_exit_pips=baseline_avg_exit_pips,
    ):
        return False
    if required_split_passes <= 0:
        return True
    return int(row.get("baseline_split_passes") or 0) >= required_split_passes


def _split_passes_baseline(
    split: dict[str, Any],
    *,
    split_min_total: int,
    baseline_favorable_rate: float,
    baseline_avg_exit_pips: float,
) -> bool:
    return (
        int(split.get("total") or 0) >= split_min_total
        and float(split.get("favorable_rate") or 0.0) >= baseline_favorable_rate
        and (_optional_float(split.get("avg_exit_pips")) or 0.0) >= baseline_avg_exit_pips
    )


def _split_windows(
    *,
    start: Optional[datetime],
    end: Optional[datetime],
    validation_days: int,
    out_of_sample_days: int,
) -> list[dict[str, Any]]:
    if not start or not end:
        return []
    start_utc = _to_utc(start)
    end_utc = _to_utc(end)
    oos_start = max(start_utc, end_utc - timedelta(days=max(0, out_of_sample_days)))
    validation_start = max(start_utc, oos_start - timedelta(days=max(0, validation_days)))
    windows = [
        {"name": "train", "start": start_utc, "end": validation_start},
        {"name": "validation", "start": validation_start, "end": oos_start},
        {"name": "out_of_sample", "start": oos_start, "end": end_utc + timedelta(seconds=1)},
    ]
    return [window for window in windows if window["start"] < window["end"]]


def _split_window_lines(split_windows: list[dict[str, Any]]) -> list[str]:
    if not split_windows:
        return ["- No validation split was configured for this archive."]
    return [
        f"- {window['name']}: {_to_utc(window['start']).date().isoformat()} "
        f"to {(_to_utc(window['end']) - timedelta(seconds=1)).date().isoformat()}"
        for window in split_windows
    ]


def _md_cell(value: Any) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def _format_pair_summary_markdown(
    *,
    symbol: str,
    summary: dict[str, Any],
    setup_rows: list[dict[str, Any]],
    baseline_rows: list[dict[str, Any]],
    research_rows: list[dict[str, Any]],
    examples: list[dict[str, Any]],
    start: Optional[datetime],
    end: Optional[datetime],
    scanner_baseline: str,
    min_total: int,
    min_favorable_rate: float,
    min_avg_exit_pips: float,
    baseline_favorable_rate: float,
    baseline_avg_exit_pips: float,
    split_min_total: int,
    required_split_passes: int,
    split_windows: list[dict[str, Any]],
) -> str:
    lines = [
        f"# {symbol} MMM Pair Research",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Study window: {_date_text(start)} to {_date_text(end)}",
        "",
        "This report is pair-specific. Do not generalize the setup to other pairs "
        "unless cross-pair convergence is separately validated.",
        "",
        "## Promotion Gate",
        "",
        f"- Minimum setup sample: {min_total}",
        f"- Research candidate gate: Fav >= {min_favorable_rate:.1f}%, "
        f"AvgExit >= {min_avg_exit_pips:+.1f} pips",
        f"- Baseline-qualified gate: Fav >= {baseline_favorable_rate:.1f}%, "
        f"AvgExit >= {baseline_avg_exit_pips:+.1f} pips",
        f"- Split confirmation: {required_split_passes} pass(es) required; "
        f"split minimum sample = {split_min_total}",
        f"- Scanner baseline: {scanner_baseline or 'not supplied'}",
        "",
        "## Validation Splits",
        "",
        *_split_window_lines(split_windows),
        "",
        "## Flashcard Summary",
        "",
        f"- Historical flashcards: {summary['total']}",
        f"- Direct-profit flashcards: {summary['direct_profit']} "
        f"({_fmt_pct(summary['direct_profit_rate'])})",
        f"- T1 hit rate: {_fmt_pct(summary['t1_rate'])}",
        f"- Average pips: {_fmt_plain(summary['avg_pips'])}",
        f"- Average profitable pips: {_fmt_plain(summary['avg_profit_pips'])}",
        f"- First snapshot: {summary['first_snapshot'] or '-'}",
        f"- Last snapshot: {summary['last_snapshot'] or '-'}",
        "",
        "## Baseline-Qualified Setups",
        "",
    ]
    if baseline_rows:
        lines.extend(_setup_table(baseline_rows[:20], baseline_keys=_row_keys(baseline_rows)))
    else:
        lines.append("No setup currently beats the scanner baseline gate.")
    lines.extend(["", "## Research Candidate Setups", ""])
    if research_rows:
        lines.extend(
            _setup_table(
                research_rows[:30],
                baseline_keys=_row_keys(baseline_rows),
                research_keys=_row_keys(research_rows),
            )
        )
    else:
        lines.append("No setup currently passes the lower research gate.")
    lines.extend(["", "## All Repeated Setups", ""])
    if setup_rows:
        lines.extend(
            _setup_table(
                setup_rows[:50],
                baseline_keys=_row_keys(baseline_rows),
                research_keys=_row_keys(research_rows),
            )
        )
    else:
        lines.append("No repeated setup has enough samples yet.")
    lines.extend(["", "## Top Direct-Profit Flashcards", ""])
    if examples:
        lines.extend(
            [
                "| ID | Time | Dir | Outcome | Pips | T1 | Conf | Setup | Chart |",
                "|---:|---|---|---|---:|---|---:|---|---|",
            ]
        )
        for item in examples[:50]:
            lines.append(
                f"| {item['flashcard_id']} | {item['snapshot_at']} | {item['direction']} | "
                f"{item['outcome']} | {_fmt_plain(item['pips_gained'])} | "
                f"{'yes' if item['t1_hit'] else 'no'} | {item['confluence_score']} | "
                f"{_md_cell(item['m_w_pattern'] or item['pattern_trade_type'] or '-')} | "
                f"{_md_cell(item['chart_path'] or '-')} |"
            )
    else:
        lines.append("No direct-profit historical flashcards are archived for this pair yet.")
    lines.extend(
        [
            "",
            "## Artifact Files",
            "",
            "- `setup_performance.json`: replay grouped by normalized MMM setup signature.",
            "- `profitable_flashcards.jsonl`: direct-profit flashcard manifest with chart references.",
            "",
        ]
    )
    return "\n".join(lines)


def _setup_table(
    rows: list[dict[str, Any]],
    *,
    baseline_keys: Optional[set[str]] = None,
    research_keys: Optional[set[str]] = None,
) -> list[str]:
    baseline_keys = baseline_keys or set()
    research_keys = research_keys or set()
    lines = [
        "| Decision | SplitPass | Direction | N | Fav% | Direct% | T1% | AvgExit | Target | MFE | MAE | Setup |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        row_key = _row_key(row)
        if row_key in baseline_keys:
            decision = "baseline_qualified"
        elif row_key in research_keys:
            decision = "research_candidate"
        else:
            decision = "research_only"
        lines.append(
            f"| {decision} | {row.get('baseline_split_passes', 0)} | "
            f"{row['direction']} | {row['total']} | "
            f"{_fmt_pct(row['favorable_rate'])} | {_fmt_pct(row['direct_profit_rate'])} | "
            f"{_fmt_pct(row['t1_rate'])} | {_fmt_plain(row['avg_exit_pips'])} | "
            f"{_fmt_plain(row['realistic_target_pips'])} | {_fmt_plain(row['avg_mfe'])} | "
            f"{_fmt_plain(row['avg_mae'])} | {_md_cell(row['normalized_key'])} |"
        )
    return lines


def _row_keys(rows: list[dict[str, Any]]) -> set[str]:
    return {_row_key(row) for row in rows}


def _row_key(row: dict[str, Any]) -> str:
    return f"{row.get('symbol')}|{row.get('direction')}|{row.get('normalized_key')}"


def _realistic_target(
    avg_exit_pips: Optional[float],
    avg_mfe: Optional[float],
    t1_rate: float,
) -> Optional[float]:
    if avg_mfe is None:
        return avg_exit_pips
    factor = 0.65 if t1_rate >= 50.0 else 0.45
    target = avg_mfe * factor
    if avg_exit_pips is not None and avg_exit_pips > 0:
        target = max(target, avg_exit_pips)
    return max(0.0, target)


def _load_json_list(value: Any) -> list[str]:
    try:
        parsed = json.loads(str(value or "[]"))
    except json.JSONDecodeError:
        return []
    if not isinstance(parsed, list):
        return []
    return [str(item) for item in parsed]


def _date_text(value: Optional[datetime]) -> str:
    return _to_utc(value).date().isoformat() if value else "-"


def _fmt_pct(value: Any) -> str:
    number = _optional_float(value)
    return "-" if number is None else f"{number:.1f}%"


def _fmt_plain(value: Any) -> str:
    number = _optional_float(value)
    return "-" if number is None else f"{number:+.1f}"


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Historical MMM flashcard miner")
    sub = parser.add_subparsers(dest="command", required=True)

    p_mine = sub.add_parser("mine", help="Mine backdated MMM flashcards from MT5 history")
    p_mine.add_argument("--days", type=int, default=180)
    p_mine.add_argument("--until")
    p_mine.add_argument("--symbols", default=",".join(settings.trading.symbols))
    p_mine.add_argument("--min-confluence", type=int, default=50)
    p_mine.add_argument("--step-bars", type=int, default=4)
    p_mine.add_argument("--limit-per-symbol", type=int, default=100)
    p_mine.add_argument("--min-spacing-minutes", type=int, default=90)
    p_mine.add_argument("--include-invalid", action="store_true")
    p_mine.add_argument("--no-charts", action="store_true")
    p_mine.add_argument("--no-promote-library", action="store_true")

    p_pair = sub.add_parser(
        "pair-study",
        help="Run/archive pair-specific historical flashcard research",
    )
    p_pair.add_argument("--days", type=int, default=1095)
    p_pair.add_argument("--until")
    p_pair.add_argument("--symbols", default=DEFAULT_RESEARCH_SYMBOLS)
    p_pair.add_argument("--min-confluence", type=int, default=50)
    p_pair.add_argument("--step-bars", type=int, default=4)
    p_pair.add_argument("--limit-per-symbol", type=int, default=250)
    p_pair.add_argument("--min-spacing-minutes", type=int, default=90)
    p_pair.add_argument("--include-invalid", action="store_true")
    p_pair.add_argument("--no-charts", action="store_true")
    p_pair.add_argument("--archive-only", action="store_true")
    p_pair.add_argument("--output-root", type=Path, default=DEFAULT_PAIR_RESEARCH_DIR)
    p_pair.add_argument("--min-total", type=int, default=5)
    p_pair.add_argument("--min-favorable-rate", type=float, default=55.0)
    p_pair.add_argument("--min-avg-exit-pips", type=float, default=0.0)
    p_pair.add_argument(
        "--baseline-favorable-rate",
        type=float,
        default=DEFAULT_SCANNER_BASELINE_FAVORABLE_RATE,
    )
    p_pair.add_argument(
        "--baseline-avg-exit-pips",
        type=float,
        default=DEFAULT_SCANNER_BASELINE_AVG_EXIT_PIPS,
    )
    p_pair.add_argument("--split-min-total", type=int, default=3)
    p_pair.add_argument("--required-split-passes", type=int, default=0)
    p_pair.add_argument("--validation-days", type=int, default=365)
    p_pair.add_argument("--out-of-sample-days", type=int, default=180)
    p_pair.add_argument("--max-examples", type=int, default=50)
    p_pair.add_argument(
        "--scanner-baseline",
        default="90m scanner baseline: N=100, Fav=85.0%, AvgExit=+10.9p",
    )

    p_report = sub.add_parser("library-report", help="Show promoted validation records")
    p_report.add_argument("--scope", choices=("PAIR", "CROSS_PAIR"))
    p_report.add_argument("--symbol")
    p_report.add_argument("--limit", type=int, default=50)

    p_validate = sub.add_parser("validate-current", help="Compare current MT5 setups to library")
    p_validate.add_argument("--symbols", default=",".join(settings.trading.symbols))

    args = parser.parse_args(argv)
    miner = HistoricalFlashcardMiner()
    try:
        if args.command == "mine":
            from helix_v3.backtest.scanner_replay import (
                connect_mt5,
                disconnect_mt5,
                fetch_rates_range,
                get_pip_size,
            )

            until = _parse_date(args.until, datetime.now(timezone.utc))
            start = until - timedelta(days=args.days)
            if not connect_mt5():
                raise SystemExit(1)
            try:
                count = miner.mine(
                    symbols=_parse_symbols(args.symbols),
                    fetch_rates=fetch_rates_range,
                    get_pip_size=get_pip_size,
                    start=start,
                    end=until,
                    min_confluence=args.min_confluence,
                    step_bars=args.step_bars,
                    limit_per_symbol=args.limit_per_symbol,
                    min_spacing_minutes=args.min_spacing_minutes,
                    require_trade_valid=not args.include_invalid,
                    generate_charts=not args.no_charts,
                    promote_library=not args.no_promote_library,
                )
            finally:
                disconnect_mt5()
            print(f"Saved {count} historical flashcards.")
        elif args.command == "pair-study":
            from helix_v3.backtest.scanner_replay import (
                connect_mt5,
                disconnect_mt5,
                fetch_rates_range,
                get_pip_size,
            )

            symbols = _parse_symbols(args.symbols)
            until = _parse_date(args.until, datetime.now(timezone.utc))
            start = until - timedelta(days=args.days)
            saved = 0
            promoted = 0
            if not args.archive_only:
                if not connect_mt5():
                    raise SystemExit(1)
                try:
                    saved = miner.mine(
                        symbols=symbols,
                        fetch_rates=fetch_rates_range,
                        get_pip_size=get_pip_size,
                        start=start,
                        end=until,
                        min_confluence=args.min_confluence,
                        step_bars=args.step_bars,
                        limit_per_symbol=args.limit_per_symbol,
                        min_spacing_minutes=args.min_spacing_minutes,
                        require_trade_valid=not args.include_invalid,
                        generate_charts=not args.no_charts,
                        promote_library=False,
                    )
                finally:
                    disconnect_mt5()
                promoted = miner._library.promote_from_replay(
                    min_total=args.min_total,
                    min_favorable_rate=max(args.min_favorable_rate, args.baseline_favorable_rate),
                    min_avg_exit_pips=max(args.min_avg_exit_pips, args.baseline_avg_exit_pips),
                    min_symbols=2,
                )
            written = miner.export_pair_research_archive(
                symbols=symbols,
                output_root=args.output_root,
                start=start,
                end=until,
                min_total=args.min_total,
                min_favorable_rate=args.min_favorable_rate,
                min_avg_exit_pips=args.min_avg_exit_pips,
                baseline_favorable_rate=args.baseline_favorable_rate,
                baseline_avg_exit_pips=args.baseline_avg_exit_pips,
                split_min_total=args.split_min_total,
                required_split_passes=args.required_split_passes,
                validation_days=args.validation_days,
                out_of_sample_days=args.out_of_sample_days,
                max_examples=args.max_examples,
                scanner_baseline=args.scanner_baseline,
            )
            print(
                f"Pair study complete. Saved {saved} flashcards, "
                f"promoted/reused {promoted} records, wrote {len(written)} archive files."
            )
        elif args.command == "library-report":
            print(miner._library.report(scope=args.scope, symbol=args.symbol, limit=args.limit))
        elif args.command == "validate-current":
            from helix_v3.core.quant_engine import MMMQuantitativeEngine

            engine = MMMQuantitativeEngine()
            if not engine.connect():
                raise SystemExit(1)
            try:
                print(miner.validate_current_setups(symbols=_parse_symbols(args.symbols), engine=engine))
            finally:
                engine.disconnect()
    finally:
        miner.close()


if __name__ == "__main__":
    main()
