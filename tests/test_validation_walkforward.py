"""Walk-forward partitioning tests for the validation library (Tier 1.3).

The library promoted patterns from a run's own trades and the engine queried
it on the same data — memorization presented as edge. `before=` must hard-
partition: only outcomes strictly before the cutoff may contribute.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from helix_v3.backtest.mmm_event_replay import MMMReplayStore
from helix_v3.backtest.validation_library import ValidationLibrary

KEY = "STOP_HUNT_REVERSAL|BUY|EARLY|L1|LONDON|AR_TIGHT|HUNT_SOFT|P2|W|RRT_NO|TDI_SF|PAT_NONE"


def _seed_replay(db_path: Path) -> None:
    """6 outcomes (4 favorable) in May, 5 outcomes in June — same signature."""
    store = MMMReplayStore(db_path=db_path)  # creates schema
    store.close() if hasattr(store, "close") else None
    conn = sqlite3.connect(str(db_path))

    def add(source_id: int, snapshot: str, outcome: str) -> None:
        conn.execute(
            """INSERT INTO mmm_setup_signatures (
                source, source_id, symbol, timeframe, snapshot_at, direction,
                normalized_key, raw_key, setup_family, theme_tags, ratios, raw_json
            ) VALUES ('backtest', ?, 'GBPJPY', 'M15', ?, 'BUY', ?, ?, 'STOP_HUNT_REVERSAL', '[]', '{}', '{}')""",
            (source_id, snapshot, KEY, KEY),
        )
        conn.execute(
            """INSERT INTO mmm_event_outcomes (
                source, source_id, evaluated_at, symbol, timeframe, snapshot_at,
                direction, exit_pips, max_favorable_pips, max_adverse_pips,
                t1_hit, outcome, label, event_path
            ) VALUES ('backtest', ?, ?, 'GBPJPY', 'M15', ?, 'BUY', 20.0, 30.0, 5.0, 1, ?, 'L', '[]')""",
            (source_id, snapshot, snapshot, outcome),
        )

    may = "2026-05-{:02d}T08:00:00+00:00"
    june = "2026-06-{:02d}T08:00:00+00:00"
    for i, outcome in enumerate(
        ["TARGET_2", "TARGET_2", "TARGET_2", "TARGET_2", "STOP_HUNTED", "STOP_HUNTED"]
    ):
        add(100 + i, may.format(i + 1), outcome)
    for i in range(5):
        add(200 + i, june.format(i + 1), "TARGET_2")
    conn.commit()
    conn.close()


def test_before_cutoff_excludes_in_window_outcomes(tmp_path) -> None:
    replay_db = tmp_path / "replay.db"
    _seed_replay(replay_db)
    lib = ValidationLibrary(db_path=tmp_path / "lib.db", replay_db_path=replay_db)

    cutoff = datetime(2026, 6, 1, tzinfo=timezone.utc)
    count = lib.rebuild_from_replay(min_total=5, min_symbols=1, before=cutoff)
    assert count >= 1

    records = lib.top_records()
    pair = [r for r in records if r.scope == "PAIR"][0]
    # Only the 6 May outcomes — the 5 June (in-window) outcomes are invisible
    assert pair.total == 6
    assert pair.favorable == 4
    lib.close()


def test_no_cutoff_includes_everything(tmp_path) -> None:
    replay_db = tmp_path / "replay.db"
    _seed_replay(replay_db)
    lib = ValidationLibrary(db_path=tmp_path / "lib.db", replay_db_path=replay_db)

    count = lib.rebuild_from_replay(min_total=5, min_symbols=1)
    assert count >= 1
    pair = [r for r in lib.top_records() if r.scope == "PAIR"][0]
    assert pair.total == 11
    lib.close()


def test_cutoff_before_all_data_yields_empty_library(tmp_path) -> None:
    replay_db = tmp_path / "replay.db"
    _seed_replay(replay_db)
    lib = ValidationLibrary(db_path=tmp_path / "lib.db", replay_db_path=replay_db)

    cutoff = datetime(2026, 1, 1, tzinfo=timezone.utc)
    count = lib.rebuild_from_replay(min_total=5, min_symbols=1, before=cutoff)
    assert count == 0
    assert lib.top_records() == []
    lib.close()
