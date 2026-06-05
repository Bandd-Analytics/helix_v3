from __future__ import annotations

import json
import sqlite3

from helix_v3.journal.flashcards import FlashcardSystem


def test_flashcard_saves_enriched_setup_fields(tmp_path) -> None:
    db_path = tmp_path / "flashcards.db"
    flashcards = FlashcardSystem(db_path=db_path)
    try:
        flashcard_id = flashcards.save_missed_flashcard(
            symbol="GBPJPY",
            timeframe="M15",
            chart_path="charts/test.png",
            mtf_context={
                "weekly": {
                    "cycle_position": "LEVEL_3",
                    "week_phase": "LATE_WEEK",
                    "trend_direction": "SELL",
                    "days_since_peak": 3,
                },
                "four_hour": {
                    "cycle_position": "LEVEL_3",
                    "level_count": 3,
                    "trend_direction": "BUY",
                    "is_choppy": False,
                },
                "one_hour": {
                    "session_phase": "TRUE_TREND",
                    "trend_direction": "BUY",
                    "intraday_level": 2,
                    "hod_locked": False,
                    "lod_locked": True,
                    "ema_50_200_cross": "none",
                },
                "fifteen_min": {
                    "asian_range_pips": 22.0,
                    "accumulation_valid": True,
                    "stop_hunt_detected": True,
                    "stop_hunt_direction": "BUY",
                    "stop_hunt_pips": 42.0,
                    "push_count": 4,
                    "m_w_forming": True,
                    "m_w_pattern": "W_BOTTOM",
                    "rrt_detected": True,
                    "entry_direction": "BUY",
                    "entry_confidence": 0.85,
                },
                "ema": {"fast_slow_div": 0.4},
                "tdi": {
                    "signals": ["SHARK_FIN_LONG", "VB_SQUEEZE"],
                    "shark_fin_active": True,
                    "shark_fin_direction": "LONG",
                    "vb_squeeze": True,
                    "divergence": "none",
                    "crossed_signal": "bullish",
                    "rsi": 45.0,
                    "signal": 43.0,
                    "base": 50.0,
                },
                "patterns": {
                    "trade_type": "THE_33",
                    "pattern_count": 7,
                    "rrt_count": 2,
                    "spike_count": 1,
                    "pin_bar_count": 3,
                    "half_batman": False,
                },
                "convergence": {
                    "themes": ["GBP_STRENGTH", "JPY_WEAKNESS"],
                    "theme_score": 72.0,
                },
                "advisory": {
                    "confidence_score": 84.0,
                    "grade": "A",
                    "action": "entry-grade",
                    "reasons": ["M/W formation present"],
                    "blockers": [],
                },
                "profile": {"risk_tier": "medium", "max_risk_pct": 0.008},
                "confluence_score": 70,
            },
            reason="unit test",
        )
    finally:
        flashcards.close()

    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT * FROM flashcards WHERE id = ?", (flashcard_id,)).fetchone()
    finally:
        conn.close()

    assert row["m_w_pattern"] == "W_BOTTOM"
    assert json.loads(row["tdi_signals"]) == ["SHARK_FIN_LONG", "VB_SQUEEZE"]
    assert row["tdi_shark_direction"] == "LONG"
    assert row["pattern_trade_type"] == "THE_33"
    assert row["pattern_rrt_count"] == 2
    assert json.loads(row["convergence_themes"]) == ["GBP_STRENGTH", "JPY_WEAKNESS"]
    assert row["convergence_theme_score"] == 72.0
    assert row["advisory_confidence_score"] == 84.0
    assert row["advisory_grade"] == "A"
    assert row["advisory_action"] == "entry-grade"
    assert json.loads(row["advisory_reasons"]) == ["M/W formation present"]
