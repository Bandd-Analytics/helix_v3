from __future__ import annotations

import json
import sqlite3

from helix_v3.training.vision_filter_ablation import run_pair_research_ablation


def test_pair_research_ablation_writes_report(tmp_path) -> None:
    flashcards_db = tmp_path / "flashcards.db"
    replay_db = tmp_path / "vision_backtests.db"
    pair_root = tmp_path / "pair_research"
    output_root = tmp_path / "feature_ablations"
    key = "THE_33_MW|BUY|EARLY_WEEK|L3|STOP_HUNT|W_BOTTOM"

    with sqlite3.connect(flashcards_db) as conn:
        conn.execute(
            """CREATE TABLE flashcards (
                id INTEGER PRIMARY KEY,
                symbol TEXT,
                snapshot_type TEXT,
                snapshot_at TEXT,
                weekly_trend TEXT,
                asian_range_pips REAL,
                stop_hunt_pips REAL,
                confluence_score INTEGER,
                tdi_signals TEXT,
                tdi_vb_squeeze INTEGER,
                tdi_rsi REAL,
                tdi_signal REAL,
                tdi_base REAL,
                h1_session TEXT,
                h4_level INTEGER,
                rrt_detected INTEGER
            )"""
        )
        for row_id in range(1, 6):
            conn.execute(
                """INSERT INTO flashcards VALUES (
                    ?, 'GBPJPY', 'HISTORICAL', ?, 'BUY', 35, 50, 70,
                    '[]', 0, 55, 50, 50, 'STOP_HUNT', 3, 0
                )""",
                (row_id, f"2026-01-0{row_id}T00:00:00+00:00"),
            )

    with sqlite3.connect(replay_db) as conn:
        conn.execute(
            """CREATE TABLE mmm_setup_signatures (
                source TEXT,
                source_id INTEGER,
                symbol TEXT,
                direction TEXT,
                normalized_key TEXT
            )"""
        )
        conn.execute(
            """CREATE TABLE mmm_event_outcomes (
                source TEXT,
                source_id INTEGER,
                outcome TEXT,
                exit_pips REAL,
                max_favorable_pips REAL,
                max_adverse_pips REAL,
                t1_hit INTEGER
            )"""
        )
        for row_id in range(1, 6):
            conn.execute(
                "INSERT INTO mmm_setup_signatures VALUES ('historical_flashcard', ?, 'GBPJPY', 'BUY', ?)",
                (row_id, key),
            )
            conn.execute(
                "INSERT INTO mmm_event_outcomes VALUES ('historical_flashcard', ?, ?, ?, 20, 5, 0)",
                (row_id, "TARGET_2" if row_id < 5 else "LOSS", 12.0 if row_id < 5 else -6.0),
            )

    pair_dir = pair_root / "GBPJPY"
    pair_dir.mkdir(parents=True)
    (pair_dir / "setup_performance.json").write_text(
        json.dumps(
            [
                {
                    "symbol": "GBPJPY",
                    "direction": "BUY",
                    "normalized_key": key,
                    "total": 5,
                    "favorable_rate": 80.0,
                    "avg_exit_pips": 8.4,
                }
            ]
        ),
        encoding="utf-8",
    )

    written = run_pair_research_ablation(
        pair_research_root=pair_root,
        output_root=output_root,
        flashcards_db=flashcards_db,
        replay_db=replay_db,
        symbols=("GBPJPY",),
        min_total=5,
    )

    assert output_root / "INDEX.md" in written
    report = (output_root / "GBPJPY" / "FEATURE_ABLATION.md").read_text(encoding="utf-8")
    assert "GBPJPY Pair Feature Ablation" in report
    assert "THE_33_MW|BUY|EARLY_WEEK" in report
    assert "Base RRS" in report
    assert "Best RRS" in report
    assert "PF" in report
    assert "Payoff" in report
