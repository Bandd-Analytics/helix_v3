from __future__ import annotations

import sqlite3

import pandas as pd

from config.pair_profiles import get_pair_profile
from helix_v3.core.sessions import classify_sessions
from helix_v3.training.taught_rule_validator import (
    TaughtRuleValidationStore,
    TaughtRuleValidator,
    detect_stop_hunt_high_m_reversal,
    detect_three_hit_w_reversal,
)


def _base_m15_df() -> pd.DataFrame:
    idx = pd.date_range("2026-06-01 00:00:00+00:00", periods=220, freq="15min")
    base = 1.1000
    df = pd.DataFrame(
        {
            "Open": [base] * len(idx),
            "High": [base + 0.0008] * len(idx),
            "Low": [base - 0.0008] * len(idx),
            "Close": [base] * len(idx),
        },
        index=idx,
    )
    return df


def test_detect_three_hit_w_reversal() -> None:
    df = _base_m15_df()
    position = 160
    low = 1.0940
    for offset in (10, 6, 2):
        idx = position - offset
        df.iloc[idx, df.columns.get_loc("Low")] = low + offset * 0.00001
        df.iloc[idx, df.columns.get_loc("Close")] = low + 0.0005
    df.iloc[position, df.columns.get_loc("Open")] = 1.0960
    df.iloc[position, df.columns.get_loc("Low")] = 1.0958
    df.iloc[position, df.columns.get_loc("High")] = 1.0995
    df.iloc[position, df.columns.get_loc("Close")] = 1.0990

    sessions = classify_sessions(df, 0.0001)
    hit = detect_three_hit_w_reversal(
        "EURUSD",
        df,
        position,
        0.0001,
        profile=get_pair_profile("EURUSD"),
        sessions=sessions,
    )

    assert hit is not None
    assert hit.rule_id == "MMM-TRAIN-002"
    assert hit.direction.value == "BUY"
    assert hit.details["m_w_pattern"] == "W_BOTTOM"


def test_detect_stop_hunt_high_m_reversal() -> None:
    df = _base_m15_df()
    # Force previous day's HOD.
    df.iloc[20, df.columns.get_loc("High")] = 1.1050
    position = 160
    df.iloc[position - 2, df.columns.get_loc("High")] = 1.1065
    df.iloc[position, df.columns.get_loc("Open")] = 1.1054
    df.iloc[position, df.columns.get_loc("High")] = 1.1058
    df.iloc[position, df.columns.get_loc("Low")] = 1.1035
    df.iloc[position, df.columns.get_loc("Close")] = 1.1040

    sessions = classify_sessions(df, 0.0001)
    hit = detect_stop_hunt_high_m_reversal(
        "EURUSD",
        df,
        position,
        0.0001,
        profile=get_pair_profile("EURUSD"),
        sessions=sessions,
    )

    assert hit is not None
    assert hit.rule_id == "MMM-TRAIN-003"
    assert hit.direction.value == "SELL"
    assert hit.details["m_w_pattern"] == "M_TOP"


def test_validator_records_rule_outcomes(tmp_path) -> None:
    df = _base_m15_df()
    position = 160
    low = 1.0940
    for offset in (10, 6, 2):
        idx = position - offset
        df.iloc[idx, df.columns.get_loc("Low")] = low + offset * 0.00001
        df.iloc[idx, df.columns.get_loc("Close")] = low + 0.0005
    df.iloc[position, df.columns.get_loc("Open")] = 1.0960
    df.iloc[position, df.columns.get_loc("Low")] = 1.0958
    df.iloc[position, df.columns.get_loc("High")] = 1.0995
    df.iloc[position, df.columns.get_loc("Close")] = 1.0990
    for idx in range(position + 1, min(position + 20, len(df))):
        df.iloc[idx, df.columns.get_loc("High")] = 1.1050
        df.iloc[idx, df.columns.get_loc("Close")] = 1.1040

    store = TaughtRuleValidationStore(tmp_path / "rules.db")
    validator = TaughtRuleValidator(store=store)
    try:
        evaluations = validator.validate_frames(
            symbol="EURUSD",
            df_m15=df,
            pip_size=0.0001,
            rule_ids={"MMM-TRAIN-002"},
            step_bars=1,
            limit_per_rule=1,
        )
        report = validator.report()
        markdown = store.markdown_report(
            scanner_baseline="90m scanner baseline: N=100, Fav=85.0%, AvgExit=+10.9p"
        )
    finally:
        validator.close()

    assert len(evaluations) == 1
    assert "MMM-TRAIN-002" in report
    assert "MMM Taught Rule Validation Report" in markdown
    assert "Promoted rules: none" in markdown
    assert "90m scanner baseline" in markdown

    conn = sqlite3.connect(str(tmp_path / "rules.db"))
    try:
        rows = conn.execute("SELECT rule_id, symbol FROM taught_rule_events").fetchall()
    finally:
        conn.close()

    assert rows == [("MMM-TRAIN-002", "EURUSD")]

    store = TaughtRuleValidationStore(tmp_path / "rules.db")
    try:
        removed = store.delete_scope(
            symbols=["EURUSD"],
            rule_ids={"MMM-TRAIN-002"},
        )
        empty_report = store.report()
    finally:
        store.close()

    assert removed == 1
    assert "No taught-rule validation events" in empty_report
