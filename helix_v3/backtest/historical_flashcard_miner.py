"""Historical MMM flashcard miner.

This module is offline-only: it reads historical MT5 candles, mines candidate
MMM setups, saves annotated flashcards with their real historical timestamps,
labels outcomes through MMM event replay, and promotes proven signatures into
the validation library.
"""

from __future__ import annotations

import argparse
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
            frames[timeframe] = _normalize_df_index(fetch_rates(symbol, timeframe, tf_start, tf_end))
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
