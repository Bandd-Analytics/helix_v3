"""Backfill deterministic OHLC features for MMM vision-review filters."""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Optional

import pandas as pd

from config.settings import settings
from helix_v3.backtest.mmm_event_replay import infer_asian_range, nearest_close
from helix_v3.backtest.scanner_replay import (
    connect_mt5,
    disconnect_mt5,
    fetch_rates_range,
    get_pip_size,
)
from helix_v3.core.types import Direction

DEFAULT_FLASHCARDS_DB = Path(settings.log_dir) / "flashcards.db"
DEFAULT_REPLAY_DB = Path(settings.log_dir) / "vision_backtests.db"
DEFAULT_PACKET_ROOT = Path("data/mmm_training/vision_review_packets")

FEATURE_COLUMNS = {
    "feature_hunt_to_ar_ratio": "REAL",
    "feature_candles_since_hunt_extreme": "INTEGER",
    "feature_close_to_ar_low_pips": "REAL",
    "feature_close_to_ar_mid_pips": "REAL",
    "feature_close_to_ar_high_pips": "REAL",
    "feature_range_pos": "REAL",
    "feature_close_to_hod_pips": "REAL",
    "feature_close_to_lod_pips": "REAL",
    "feature_pullback_from_session_extreme_pips": "REAL",
    "feature_distance_from_hunt_extreme_pips": "REAL",
    "feature_prior_8_candle_expansion_pips": "REAL",
    "feature_prior_8_candle_directional_move_pips": "REAL",
    "feature_bars_since_first_ar_edge_break": "INTEGER",
    "feature_ema50_ema200_spread_pips": "REAL",
    "feature_ema200_slope_8_pips": "REAL",
    "feature_tdi_rsi_minus_signal": "REAL",
    "feature_updated_at": "TEXT",
}


@dataclass(frozen=True)
class FeatureBackfillConfig:
    flashcards_db: Path = DEFAULT_FLASHCARDS_DB
    replay_db: Path = DEFAULT_REPLAY_DB
    packet_root: Path = DEFAULT_PACKET_ROOT
    symbols: tuple[str, ...] = ()
    packet_names: tuple[str, ...] = ()
    lookback_days: int = 10
    forward_days: int = 1


def backfill_packet_features(
    config: FeatureBackfillConfig,
    *,
    fetch_rates: Callable[[str, str, datetime, datetime], pd.DataFrame] = fetch_rates_range,
    pip_size_for_symbol: Callable[[str], float] = get_pip_size,
) -> int:
    rows = _load_target_rows(config)
    if not rows:
        return 0

    conn = sqlite3.connect(str(config.flashcards_db))
    try:
        _ensure_feature_columns(conn)
        updated = 0
        for symbol, symbol_rows in _rows_by_symbol(rows).items():
            start = min(_parse_time(row["snapshot_at"]) for row in symbol_rows)
            end = max(_parse_time(row["snapshot_at"]) for row in symbol_rows)
            frame = _fetch_m15_window(
                fetch_rates,
                symbol,
                start - timedelta(days=config.lookback_days),
                end + timedelta(days=config.forward_days),
            )
            pip_size = pip_size_for_symbol(symbol)
            for row in symbol_rows:
                features = compute_ohlc_features(
                    frame,
                    snapshot_at=_parse_time(row["snapshot_at"]),
                    direction=_parse_direction(row.get("entry_direction")),
                    pip_size=pip_size,
                    asian_range_pips=_float(row.get("asian_range_pips")),
                    stop_hunt_pips=_float(row.get("stop_hunt_pips")),
                    tdi_rsi=_float(row.get("tdi_rsi")),
                    tdi_signal=_float(row.get("tdi_signal")),
                )
                if not features:
                    continue
                _update_features(conn, int(row["id"]), features)
                updated += 1
        conn.commit()
        return updated
    finally:
        conn.close()


def compute_ohlc_features(
    df: pd.DataFrame,
    *,
    snapshot_at: datetime,
    direction: Direction,
    pip_size: float,
    asian_range_pips: Optional[float] = None,
    stop_hunt_pips: Optional[float] = None,
    tdi_rsi: Optional[float] = None,
    tdi_signal: Optional[float] = None,
) -> dict[str, Any]:
    if df.empty or pip_size <= 0:
        return {}
    frame = _normalize_df_index(df)
    snap = _timestamp_for_index(snapshot_at, frame.index)
    past = frame[frame.index <= snap].tail(240)
    if len(past) < 10:
        return {}

    close = nearest_close(past, snapshot_at)
    if close is None:
        return {}

    asian_high, asian_low = infer_asian_range(past, pip_size)
    if asian_high is None or asian_low is None or asian_high <= asian_low:
        asian_high, asian_low = _fallback_range(past)
    ar_pips = asian_range_pips or abs(asian_high - asian_low) / pip_size
    ar_mid = (asian_high + asian_low) / 2.0

    day = past[past.index.date == _to_utc(snapshot_at).date()]
    session = day if not day.empty else past.tail(96)
    hod = float(session["High"].max())
    lod = float(session["Low"].min())

    recent = past.tail(64)
    hunt_extreme, candles_since_hunt = _hunt_extreme(recent, direction)
    distance_from_hunt = _directional_distance(direction, close, hunt_extreme, pip_size)

    prior_8 = past.tail(8)
    expansion = (float(prior_8["High"].max()) - float(prior_8["Low"].min())) / pip_size
    directional_move = _directional_distance(
        direction,
        close,
        float(prior_8["Open"].iloc[0]),
        pip_size,
    )

    ema50, ema200 = _ema_values(past)
    ema200_slope = None
    if len(ema200) >= 9:
        ema200_slope = _directional_distance(direction, float(ema200.iloc[-1]), float(ema200.iloc[-9]), pip_size)

    return {
        "feature_hunt_to_ar_ratio": _safe_ratio(stop_hunt_pips, ar_pips),
        "feature_candles_since_hunt_extreme": candles_since_hunt,
        "feature_close_to_ar_low_pips": (close - asian_low) / pip_size,
        "feature_close_to_ar_mid_pips": (close - ar_mid) / pip_size,
        "feature_close_to_ar_high_pips": (close - asian_high) / pip_size,
        "feature_range_pos": (close - asian_low) / (asian_high - asian_low),
        "feature_close_to_hod_pips": (close - hod) / pip_size,
        "feature_close_to_lod_pips": (close - lod) / pip_size,
        "feature_pullback_from_session_extreme_pips": _pullback_from_extreme(
            direction,
            close,
            hod,
            lod,
            pip_size,
        ),
        "feature_distance_from_hunt_extreme_pips": distance_from_hunt,
        "feature_prior_8_candle_expansion_pips": expansion,
        "feature_prior_8_candle_directional_move_pips": directional_move,
        "feature_bars_since_first_ar_edge_break": _bars_since_first_ar_edge_break(
            recent,
            direction,
            asian_high,
            asian_low,
        ),
        "feature_ema50_ema200_spread_pips": _directional_distance(
            direction,
            float(ema50.iloc[-1]),
            float(ema200.iloc[-1]),
            pip_size,
        ),
        "feature_ema200_slope_8_pips": ema200_slope,
        "feature_tdi_rsi_minus_signal": (
            tdi_rsi - tdi_signal if tdi_rsi is not None and tdi_signal is not None else None
        ),
        "feature_updated_at": datetime.now(timezone.utc).isoformat(),
    }


def _load_target_rows(config: FeatureBackfillConfig) -> list[dict[str, Any]]:
    packet_filters = _packet_filters(config.packet_root, config.packet_names) if (
        config.packet_names or not config.symbols
    ) else []
    if not packet_filters and not config.symbols:
        return []

    conn = sqlite3.connect(str(config.flashcards_db))
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("ATTACH DATABASE ? AS replay_db", (str(config.replay_db),))
        clauses = ["f.snapshot_type = 'HISTORICAL'", "s.source = 'historical_flashcard'"]
        params: list[Any] = []
        if config.symbols:
            placeholders = ",".join("?" for _ in config.symbols)
            clauses.append(f"f.symbol IN ({placeholders})")
            params.extend(config.symbols)
        if packet_filters:
            packet_clauses = []
            for symbol, normalized_key in packet_filters:
                packet_clauses.append("(s.symbol = ? AND s.normalized_key = ?)")
                params.extend([symbol, normalized_key])
            clauses.append("(" + " OR ".join(packet_clauses) + ")")
        rows = conn.execute(
            f"""SELECT f.*
            FROM flashcards f
            JOIN replay_db.mmm_setup_signatures s
              ON s.source_id = f.id
             AND s.source = 'historical_flashcard'
            WHERE {' AND '.join(clauses)}
            ORDER BY f.symbol, f.snapshot_at""",
            params,
        ).fetchall()
    finally:
        conn.close()
    return [dict(row) for row in rows]


def _packet_filters(packet_root: Path, packet_names: tuple[str, ...]) -> list[tuple[str, str]]:
    manifest_paths = []
    if packet_names:
        manifest_paths = [packet_root / name / "manifest.json" for name in packet_names]
    elif packet_root.exists():
        manifest_paths = sorted(packet_root.glob("*/manifest.json"))

    filters: list[tuple[str, str]] = []
    for path in manifest_paths:
        if not path.exists():
            continue
        manifest = json.loads(path.read_text(encoding="utf-8"))
        filters.append((str(manifest["symbol"]), str(manifest["normalized_key"])))
    return filters


def _rows_by_symbol(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(str(row["symbol"]), []).append(row)
    return grouped


def _fetch_m15_window(
    fetch_rates: Callable[[str, str, datetime, datetime], pd.DataFrame],
    symbol: str,
    start: datetime,
    end: datetime,
) -> pd.DataFrame:
    chunks: list[pd.DataFrame] = []
    cursor = _to_utc(start)
    end = _to_utc(end)
    while cursor < end:
        chunk_end = min(cursor + timedelta(days=90), end)
        chunk = fetch_rates(symbol, "M15", cursor, chunk_end)
        if not chunk.empty:
            chunks.append(_normalize_df_index(chunk))
        cursor = chunk_end
    if not chunks:
        return pd.DataFrame()
    combined = pd.concat(chunks).sort_index()
    return combined[~combined.index.duplicated(keep="last")]


def _ensure_feature_columns(conn: sqlite3.Connection) -> None:
    existing = {row[1] for row in conn.execute("PRAGMA table_info(flashcards)").fetchall()}
    for column, column_type in FEATURE_COLUMNS.items():
        if column not in existing:
            conn.execute(f"ALTER TABLE flashcards ADD COLUMN {column} {column_type}")


def _update_features(conn: sqlite3.Connection, flashcard_id: int, fields: dict[str, Any]) -> None:
    assignments = ", ".join(f"{column} = ?" for column in fields)
    conn.execute(
        f"UPDATE flashcards SET {assignments} WHERE id = ?",
        (*fields.values(), flashcard_id),
    )


def _hunt_extreme(recent: pd.DataFrame, direction: Direction) -> tuple[float, int]:
    if direction == Direction.SELL:
        index_position = int(recent["High"].to_numpy().argmax())
        value = float(recent["High"].iloc[index_position])
    else:
        index_position = int(recent["Low"].to_numpy().argmin())
        value = float(recent["Low"].iloc[index_position])
    return value, len(recent) - 1 - index_position


def _bars_since_first_ar_edge_break(
    recent: pd.DataFrame,
    direction: Direction,
    asian_high: float,
    asian_low: float,
) -> Optional[int]:
    if direction == Direction.SELL:
        hits = recent.index[recent["Low"] <= asian_low]
    else:
        hits = recent.index[recent["High"] >= asian_high]
    if len(hits) == 0:
        return None
    first = hits[0]
    positions = {idx: pos for pos, idx in enumerate(recent.index)}
    return len(recent) - 1 - positions[first]


def _pullback_from_extreme(
    direction: Direction,
    close: float,
    hod: float,
    lod: float,
    pip_size: float,
) -> float:
    if direction == Direction.SELL:
        return (close - lod) / pip_size
    return (hod - close) / pip_size


def _directional_distance(
    direction: Direction,
    current: float,
    reference: float,
    pip_size: float,
) -> float:
    if direction == Direction.SELL:
        return (reference - current) / pip_size
    return (current - reference) / pip_size


def _ema_values(past: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    close = past["Close"].astype(float)
    return close.ewm(span=50, adjust=False).mean(), close.ewm(span=200, adjust=False).mean()


def _fallback_range(past: pd.DataFrame) -> tuple[float, float]:
    recent = past.tail(32)
    return float(recent["High"].max()), float(recent["Low"].min())


def _safe_ratio(numerator: Optional[float], denominator: Optional[float]) -> Optional[float]:
    if numerator is None or denominator is None or denominator <= 0:
        return None
    return numerator / denominator


def _normalize_df_index(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    out = df.copy()
    if not isinstance(out.index, pd.DatetimeIndex):
        raise TypeError("Feature backfill dataframe must use a DatetimeIndex")
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


def _to_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _parse_time(value: str) -> datetime:
    return _to_utc(datetime.fromisoformat(value.replace("Z", "+00:00")))


def _parse_direction(value: Any) -> Direction:
    try:
        return Direction(str(value or "NEUTRAL").upper())
    except ValueError:
        return Direction.NEUTRAL


def _float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _parse_csv_arg(raw: str) -> tuple[str, ...]:
    return tuple(item.strip().upper() for item in raw.split(",") if item.strip())


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Backfill MMM vision OHLC feature columns")
    parser.add_argument("--flashcards-db", type=Path, default=DEFAULT_FLASHCARDS_DB)
    parser.add_argument("--replay-db", type=Path, default=DEFAULT_REPLAY_DB)
    parser.add_argument("--packet-root", type=Path, default=DEFAULT_PACKET_ROOT)
    parser.add_argument("--packets", default="", help="Comma-separated packet directory names")
    parser.add_argument("--symbols", default="", help="Optional comma-separated symbols")
    parser.add_argument("--lookback-days", type=int, default=10)
    parser.add_argument("--forward-days", type=int, default=1)
    parser.add_argument("--no-mt5-connect", action="store_true")
    args = parser.parse_args(argv)

    if not args.no_mt5_connect and not connect_mt5():
        raise SystemExit(1)
    try:
        count = backfill_packet_features(
            FeatureBackfillConfig(
                flashcards_db=args.flashcards_db,
                replay_db=args.replay_db,
                packet_root=args.packet_root,
                packet_names=tuple(item.strip() for item in args.packets.split(",") if item.strip()),
                symbols=_parse_csv_arg(args.symbols),
                lookback_days=args.lookback_days,
                forward_days=args.forward_days,
            )
        )
    finally:
        if not args.no_mt5_connect:
            disconnect_mt5()
    print(f"Backfilled OHLC vision features for {count} flashcard(s).")


if __name__ == "__main__":
    main()
