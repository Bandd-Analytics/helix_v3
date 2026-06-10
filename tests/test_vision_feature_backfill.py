from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd

from helix_v3.core.types import Direction
from helix_v3.training.vision_feature_backfill import (
    FeatureBackfillConfig,
    compute_ohlc_features,
    _load_target_rows,
)


def test_compute_ohlc_features_extracts_directional_metrics() -> None:
    index = pd.date_range(
        datetime(2026, 1, 5, 0, 0, tzinfo=timezone.utc),
        periods=40,
        freq="15min",
    )
    rows = []
    for pos, _ in enumerate(index):
        base = 200.00 + pos * 0.02
        rows.append(
            {
                "Open": base,
                "High": base + 0.04,
                "Low": base - 0.04,
                "Close": base + 0.01,
                "Volume": 100,
            }
        )
    df = pd.DataFrame(rows, index=index)
    df.iloc[10, df.columns.get_loc("Low")] = 199.00

    features = compute_ohlc_features(
        df,
        snapshot_at=index[-1].to_pydatetime(),
        direction=Direction.BUY,
        pip_size=0.01,
        asian_range_pips=25.0,
        stop_hunt_pips=50.0,
        tdi_rsi=55.0,
        tdi_signal=50.0,
    )

    assert features["feature_hunt_to_ar_ratio"] == 2.0
    assert features["feature_candles_since_hunt_extreme"] == 29
    assert features["feature_distance_from_hunt_extreme_pips"] > 0
    assert features["feature_prior_8_candle_expansion_pips"] > 0
    assert features["feature_ema50_ema200_spread_pips"] is not None
    assert features["feature_tdi_rsi_minus_signal"] == 5.0


def test_symbol_backfill_selection_is_not_limited_to_packet_manifests(tmp_path) -> None:
    flashcards_db = tmp_path / "flashcards.db"
    replay_db = tmp_path / "vision_backtests.db"
    packet_root = tmp_path / "packets"
    packet_dir = packet_root / "packet_a"
    packet_dir.mkdir(parents=True)

    import sqlite3

    with sqlite3.connect(flashcards_db) as conn:
        conn.execute(
            """CREATE TABLE flashcards (
                id INTEGER PRIMARY KEY,
                symbol TEXT,
                snapshot_type TEXT,
                snapshot_at TEXT
            )"""
        )
        conn.executemany(
            "INSERT INTO flashcards VALUES (?, ?, 'HISTORICAL', '2026-01-01T00:00:00+00:00')",
            [(1, "GBPJPY"), (2, "GBPJPY")],
        )
    with sqlite3.connect(replay_db) as conn:
        conn.execute(
            """CREATE TABLE mmm_setup_signatures (
                source TEXT,
                source_id INTEGER,
                symbol TEXT,
                normalized_key TEXT
            )"""
        )
        conn.executemany(
            "INSERT INTO mmm_setup_signatures VALUES ('historical_flashcard', ?, 'GBPJPY', ?)",
            [(1, "KEY_A"), (2, "KEY_B")],
        )
    (packet_dir / "manifest.json").write_text(
        '{"symbol": "GBPJPY", "normalized_key": "KEY_A"}',
        encoding="utf-8",
    )

    packet_rows = _load_target_rows(
        FeatureBackfillConfig(
            flashcards_db=flashcards_db,
            replay_db=replay_db,
            packet_root=packet_root,
        )
    )
    symbol_rows = _load_target_rows(
        FeatureBackfillConfig(
            flashcards_db=flashcards_db,
            replay_db=replay_db,
            packet_root=packet_root,
            symbols=("GBPJPY",),
        )
    )

    assert [row["id"] for row in packet_rows] == [1]
    assert [row["id"] for row in symbol_rows] == [1, 2]
