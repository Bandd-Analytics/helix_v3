from __future__ import annotations

import sqlite3

from helix_v3.analysis.instrument_calibration import (
    SymbolSpec,
    build_calibration_rows,
)
from helix_v3.core.instruments import fallback_pip_size, pip_size_from_digits, pip_value_per_lot


def test_pip_size_helpers_cover_gold_and_indices() -> None:
    assert pip_size_from_digits(point=0.00001, digits=5) == 0.0001
    assert pip_size_from_digits(point=0.001, digits=3) == 0.01
    assert pip_size_from_digits(point=0.01, digits=2) == 0.01
    assert fallback_pip_size("XAUUSD") == 0.01
    assert fallback_pip_size("US30") == 0.01
    assert pip_value_per_lot(pip_size=0.01, tick_size=0.01, tick_value=1.0) == 1.0


def test_calibration_rows_keep_analysis_only_symbols_execution_blocked(tmp_path) -> None:
    db = tmp_path / "setup_intelligence.db"
    conn = sqlite3.connect(str(db))
    try:
        conn.executescript(
            """
            CREATE TABLE setup_occurrences (
                symbol TEXT,
                exit_pips REAL,
                max_favorable_pips REAL,
                max_adverse_pips REAL
            );
            CREATE TABLE expectancy_candidates (
                symbol TEXT,
                candidate_tier TEXT,
                profit_factor REAL
            );
            """
        )
        conn.executemany(
            """INSERT INTO setup_occurrences
            (symbol, exit_pips, max_favorable_pips, max_adverse_pips)
            VALUES ('XAUUSD', ?, ?, ?)""",
            [(100.0, 200.0, 20.0), (-25.0, 50.0, 40.0), (50.0, 120.0, 30.0)],
        )
        conn.execute(
            """INSERT INTO expectancy_candidates
            (symbol, candidate_tier, profit_factor)
            VALUES ('XAUUSD', 'DEMO_CANDIDATE', 2.5)"""
        )
        conn.commit()
    finally:
        conn.close()

    rows = build_calibration_rows(
        symbols=["XAUUSD"],
        intelligence_db=db,
        specs={
            "XAUUSD": SymbolSpec(
                symbol="XAUUSD",
                visible=True,
                digits=2,
                point=0.01,
                pip_size=0.01,
                trade_tick_size=0.01,
                trade_tick_value=1.0,
                trade_contract_size=100.0,
                volume_min=0.01,
                volume_step=0.01,
                volume_max=100.0,
                bid=2300.0,
                ask=2300.1,
                spread_pips=10.0,
                pip_value_per_lot=1.0,
            )
        },
    )

    assert len(rows) == 1
    row = rows[0]
    assert row.status == "RESEARCH_CALIBRATED_EXECUTION_BLOCKED"
    assert row.replay.demo_candidates == 1
    assert row.avg_exit_value_per_lot == 125.0 / 3.0
