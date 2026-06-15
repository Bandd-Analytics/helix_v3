"""Forward Plan Track 2.1: recording live trade outcomes to the replay store.

The live forward-validation loop builds an MMMEventOutcome from a CLOSED
trade-journal row + the setup captured at entry. These tests pin the
exit_reason -> replay-taxonomy mapping (so live data stays comparable to the
backtest data the signature audit consumes) and the full builder.
"""
from __future__ import annotations

from datetime import datetime, timezone

from helix_v3.backtest.mmm_event_replay import (
    ReplaySetup,
    live_outcome_from_journal_row,
    _live_outcome_label,
)
from helix_v3.core.types import Direction

FAVORABLE = {"TARGET_2", "TRAIL_STOP", "TIME_EXIT_PROFIT"}


def _setup(direction=Direction.BUY) -> ReplaySetup:
    return ReplaySetup(
        symbol="EURUSD", timeframe="M15",
        snapshot_at=datetime(2026, 6, 15, 8, 0, tzinfo=timezone.utc),
        direction=direction, source="live", source_id=123,
    )


def _row(**over):
    base = dict(
        ticket=123, symbol="EURUSD", direction="BUY",
        entry_price=1.1000, stop_loss=1.0985, take_profit_1=1.1015,
        take_profit_2=1.1030, sl_pips=15.0, exit_price=1.1015,
        pips_gained=15.0, t1_hit=0, exit_reason="TP",
        opened_at="2026-06-15T08:00:00+00:00",
        closed_at="2026-06-15T09:30:00+00:00", duration_minutes=90.0,
    )
    base.update(over)
    return base


# --- label mapping ---------------------------------------------------------

def test_label_profit_paths_are_favorable() -> None:
    assert _live_outcome_label("TP", 15.0, False, 1.0) == "TARGET_2"
    assert _live_outcome_label("SL", 8.0, True, 1.0) == "TRAIL_STOP"   # trailed in profit
    assert _live_outcome_label("SESSION_EXIT", 6.0, False, 1.0) == "TIME_EXIT_PROFIT"
    for lbl in ("TARGET_2", "TRAIL_STOP", "TIME_EXIT_PROFIT"):
        assert lbl in FAVORABLE


def test_label_loss_paths_are_unfavorable() -> None:
    assert _live_outcome_label("SL", -15.0, False, 1.0) == "LOSS"
    assert _live_outcome_label("TIME_EXIT", -4.0, False, 1.0) == "TIME_EXIT_LOSS"
    assert _live_outcome_label("STALE_EXIT", -3.0, False, 1.0) == "STALE_EXIT"
    assert _live_outcome_label("NEWS_EXIT", -2.0, False, 1.0) == "STALE_EXIT"
    for r in ("LOSS", "TIME_EXIT_LOSS", "STALE_EXIT"):
        assert r not in FAVORABLE


def test_label_breakeven_after_t1() -> None:
    assert _live_outcome_label("SL", 0.2, True, 1.0) == "BREAKEVEN_AFTER_T1"
    assert _live_outcome_label("SL", 0.2, False, 1.0) == "STALE_EXIT"


# --- full builder ----------------------------------------------------------

def test_builder_target_2_carries_setup_identity_and_pips() -> None:
    out = live_outcome_from_journal_row(_row(), _setup())
    assert out is not None
    assert out.outcome == "TARGET_2"
    assert out.source == "live" and out.source_id == 123
    assert out.symbol == "EURUSD" and out.direction == Direction.BUY
    assert out.exit_pips == 15.0
    # pip_size derived from sl distance / sl_pips = 0.0015/15 = 0.0001
    assert abs(out.t1_pips - 15.0) < 1e-6
    assert abs(out.t2_pips - 30.0) < 1e-6


def test_builder_sl_loss_is_unfavorable() -> None:
    out = live_outcome_from_journal_row(
        _row(exit_reason="SL", exit_price=1.0985, pips_gained=-15.0), _setup()
    )
    assert out.outcome == "LOSS"
    assert out.exit_pips == -15.0


def test_builder_skips_t1_partial_and_open_rows() -> None:
    assert live_outcome_from_journal_row(_row(exit_reason="T1_PARTIAL"), _setup()) is None
    assert live_outcome_from_journal_row(_row(closed_at=None), _setup()) is None
    assert live_outcome_from_journal_row(_row(closed_at=""), _setup()) is None


def test_builder_event_path_marks_t1() -> None:
    out = live_outcome_from_journal_row(
        _row(exit_reason="SL", t1_hit=1, exit_price=1.1000, pips_gained=8.0), _setup()
    )
    assert out.outcome == "TRAIL_STOP"
    assert out.event_path == ["ENTRY", "T1_HIT", "TRAIL_STOP"]
