"""Backfill chart images for existing MMM vision-review packet flashcards.

This is an offline preparation command. It renders historical flashcard charts
for packet cases that were mined without images, then updates only
``flashcards.chart_path`` so the packet builder can copy the PNGs.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Callable, Optional

import pandas as pd

import helix_v3.core.mtf_analyzer as mtf_module
from config.settings import settings
from helix_v3.backtest.historical_flashcard_miner import (
    HistoricalSliceEngine,
    _compute_pivots_safe,
    _fetch_rates_chunked,
    _normalize_df_index,
    _past_frame,
    _to_utc,
)
from helix_v3.backtest.scanner_replay import (
    connect_mt5,
    disconnect_mt5,
    fetch_rates_range,
    get_pip_size,
)
from helix_v3.core.mtf_analyzer import MTFAnalysis, MTFAnalyzer
from helix_v3.core.patterns import scan_patterns
from helix_v3.core.tdi import compute_adr, compute_daily_hilo, compute_tdi
from helix_v3.utils.logger import get_logger
from helix_v3.visualization.annotated_chart import AnnotatedChartGenerator

DEFAULT_FLASHCARDS_DB = Path(settings.log_dir) / "flashcards.db"
DEFAULT_PACKET_ROOT = Path("data/mmm_training/vision_review_packets")

logger = get_logger("vision_packet_chart_backfill")


@dataclass(frozen=True)
class ChartBackfillConfig:
    flashcards_db: Path = DEFAULT_FLASHCARDS_DB
    packet_root: Path = DEFAULT_PACKET_ROOT
    packet_names: tuple[str, ...] = ()
    symbols: tuple[str, ...] = ()
    replace_existing: bool = False


def backfill_packet_charts(
    config: ChartBackfillConfig,
    *,
    fetch_rates: Callable[[str, str, datetime, datetime], pd.DataFrame] = fetch_rates_range,
    pip_size_for_symbol: Callable[[str], float] = get_pip_size,
    chart_generator: Optional[AnnotatedChartGenerator] = None,
) -> int:
    """Render missing packet charts and update ``flashcards.chart_path``."""

    targets = load_chart_targets(config)
    if not targets:
        return 0

    generator = chart_generator or AnnotatedChartGenerator()
    conn = sqlite3.connect(str(config.flashcards_db))
    try:
        updated = 0
        for symbol, rows in _rows_by_symbol(targets).items():
            start = min(_parse_time(str(row["snapshot_at"])) for row in rows)
            end = max(_parse_time(str(row["snapshot_at"])) for row in rows)
            frames = _fetch_symbol_frames(symbol, fetch_rates, start=start, end=end)
            pip_size = pip_size_for_symbol(symbol)
            for row in rows:
                snapshot_at = _parse_time(str(row["snapshot_at"]))
                try:
                    chart_path = render_historical_chart(
                        symbol=symbol,
                        frames=frames,
                        snapshot_at=snapshot_at,
                        pip_size=pip_size,
                        chart_generator=generator,
                    )
                except Exception as exc:
                    logger.warning(
                        "Chart backfill failed for flashcard %s %s %s: %s",
                        row["id"],
                        symbol,
                        snapshot_at.isoformat(),
                        exc,
                    )
                    continue
                conn.execute(
                    "UPDATE flashcards SET chart_path = ? WHERE id = ?",
                    (str(chart_path), int(row["id"])),
                )
                updated += 1
        conn.commit()
        return updated
    finally:
        conn.close()


def render_historical_chart(
    *,
    symbol: str,
    frames: dict[str, pd.DataFrame],
    snapshot_at: datetime,
    pip_size: float,
    chart_generator: AnnotatedChartGenerator,
) -> Path:
    df_m15 = _past_frame(frames["M15"], snapshot_at, bars=240)
    df_d1 = _past_frame(frames["D1"], snapshot_at, bars=220)
    if len(df_m15) < 60 or len(df_d1) < 2:
        raise ValueError(f"Insufficient bars for {symbol} at {snapshot_at.isoformat()}")

    analysis = _analyze_snapshot(symbol, frames, snapshot_at, pip_size)
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
    pivots = _compute_pivots_safe(df_d1)
    adr = compute_adr(df_d1) if len(df_d1) >= 14 else 0.0
    _, chart_path = chart_generator.generate_from_mtf(
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
        pip_size=pip_size,
    )
    return chart_path


def load_chart_targets(config: ChartBackfillConfig) -> list[dict[str, Any]]:
    flashcard_ids = collect_packet_flashcard_ids(config)
    if not flashcard_ids:
        return []

    conn = sqlite3.connect(str(config.flashcards_db))
    conn.row_factory = sqlite3.Row
    try:
        placeholders = ",".join("?" for _ in flashcard_ids)
        clauses = [
            "id IN (" + placeholders + ")",
            "snapshot_type = 'HISTORICAL'",
        ]
        params: list[Any] = list(flashcard_ids)
        if config.symbols:
            symbol_placeholders = ",".join("?" for _ in config.symbols)
            clauses.append(f"symbol IN ({symbol_placeholders})")
            params.extend(config.symbols)
        rows = conn.execute(
            f"""SELECT id, symbol, timeframe, snapshot_at, chart_path
            FROM flashcards
            WHERE {' AND '.join(clauses)}
            ORDER BY symbol, snapshot_at""",
            params,
        ).fetchall()
    finally:
        conn.close()

    out: list[dict[str, Any]] = []
    for row in rows:
        item = dict(row)
        chart_path = _resolve_path(str(item.get("chart_path") or ""), Path.cwd())
        if not config.replace_existing and chart_path and chart_path.exists():
            continue
        out.append(item)
    return out


def collect_packet_flashcard_ids(config: ChartBackfillConfig) -> tuple[int, ...]:
    ids: set[int] = set()
    symbols = set(config.symbols)
    for manifest_path in _manifest_paths(config.packet_root, config.packet_names):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        symbol = str(manifest.get("symbol") or "").upper()
        if symbols and symbol not in symbols:
            continue
        for item in manifest.get("items", []):
            if not config.replace_existing and _item_has_existing_image(manifest_path.parent, item):
                continue
            try:
                ids.add(int(item["flashcard_id"]))
            except (KeyError, TypeError, ValueError):
                continue
    return tuple(sorted(ids))


def _fetch_symbol_frames(
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


def _manifest_paths(packet_root: Path, packet_names: tuple[str, ...]) -> list[Path]:
    if packet_names:
        return [packet_root / name / "manifest.json" for name in packet_names]
    if not packet_root.exists():
        return []
    return sorted(packet_root.glob("*/manifest.json"))


def _item_has_existing_image(packet_dir: Path, item: dict[str, Any]) -> bool:
    for key in ("source_chart_path", "image_path"):
        path = _resolve_path(str(item.get(key) or ""), packet_dir)
        if path and path.exists():
            return True
    return False


def _resolve_path(raw: str, base_dir: Path) -> Optional[Path]:
    if not raw:
        return None
    path = Path(raw)
    if path.is_absolute():
        return path
    packet_relative = base_dir / path
    if packet_relative.exists():
        return packet_relative
    return Path.cwd() / path


def _rows_by_symbol(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(str(row["symbol"]), []).append(row)
    return grouped


def _parse_time(value: str) -> datetime:
    return _to_utc(datetime.fromisoformat(value.replace("Z", "+00:00")))


def _parse_csv_arg(raw: str) -> tuple[str, ...]:
    return tuple(item.strip().upper() for item in raw.split(",") if item.strip())


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Backfill packet chart PNGs")
    parser.add_argument("--flashcards-db", type=Path, default=DEFAULT_FLASHCARDS_DB)
    parser.add_argument("--packet-root", type=Path, default=DEFAULT_PACKET_ROOT)
    parser.add_argument("--packets", default="", help="Comma-separated packet directory names")
    parser.add_argument("--symbols", default="", help="Optional comma-separated symbols")
    parser.add_argument(
        "--replace-existing",
        action="store_true",
        help="Regenerate charts even when chart paths or packet images already exist",
    )
    parser.add_argument("--no-mt5-connect", action="store_true")
    args = parser.parse_args(argv)

    if not args.no_mt5_connect and not connect_mt5():
        raise SystemExit(1)
    try:
        count = backfill_packet_charts(
            ChartBackfillConfig(
                flashcards_db=args.flashcards_db,
                packet_root=args.packet_root,
                packet_names=tuple(item.strip() for item in args.packets.split(",") if item.strip()),
                symbols=_parse_csv_arg(args.symbols),
                replace_existing=args.replace_existing,
            )
        )
    finally:
        if not args.no_mt5_connect:
            disconnect_mt5()
    print(f"Backfilled chart paths for {count} flashcard(s).")


if __name__ == "__main__":
    main()
