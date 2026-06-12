"""TradeSimulator honest-accounting tests (Tier 1.4 / 1.5 / 1.6 / 1.8).

Pins the fixes for: T1 partials booking $0 then full-size TP2 (winners
inflated ~43%), near-zero costs, SL fills at the level through gaps,
unrealized P&L hardcoded to 0, and the stale-tighten double no-op
(pip_size = min_sl/min_sl = 1.0 writing a field nothing reads).
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

import pandas as pd
import pytest

import helix_v3.backtest.engine as engine_mod
from helix_v3.backtest.engine import TradeSimulator
from helix_v3.core.types import Direction

T0 = datetime(2026, 6, 10, 8, 0, tzinfo=timezone.utc)

PROFILE = SimpleNamespace(
    max_risk_pct=0.01,
    min_sl_pips=10.0,
    max_lot_size=5.0,
    max_spread_pips=1.0,       # full spread; half per side
    expected_level_move_pips=70.0,
    sl_buffer_pips=3.0,
    stale_minutes=90,
    stale_exit_minutes=135,    # extended window -> tighten phase exists
    max_duration_minutes=240,
    trail_activation_pips=12.0,
    trail_distance_pips=10.0,
)


@pytest.fixture(autouse=True)
def _pin_profile(monkeypatch):
    monkeypatch.setattr(engine_mod, "get_pair_profile", lambda symbol: PROFILE)


def _bar(open_, high, low, close) -> pd.Series:
    return pd.Series({"Open": open_, "High": high, "Low": low, "Close": close})


def _sim(**kwargs) -> TradeSimulator:
    defaults = dict(initial_equity=10_000.0, slippage_pips=0.5, commission_per_lot=0.0)
    defaults.update(kwargs)
    return TradeSimulator(**defaults)


def _open_buy(sim: TradeSimulator, close: float = 1.1000, sl: float = 1.0980):
    """BUY off a 1.1000 close. Side cost = 0.5 spread + 0.5 slippage = 1 pip."""
    return sim.open_trade(
        symbol="EURUSD",
        direction=Direction.BUY,
        entry_price=close,
        entry_time=T0,
        sl_price=sl,
        pip_size=0.0001,
        pip_value_per_lot=10.0,
    )


def test_entry_pays_half_spread_plus_slippage() -> None:
    sim = _sim()
    trade = _open_buy(sim)
    assert trade.entry_price == pytest.approx(1.1001)  # close + 1 pip cost


def test_t1_partial_books_realized_cash_and_tp2_pays_remainder_only() -> None:
    """Regression: T1 booked $0, then TP2 paid 2.5R on the FULL position."""
    sim = _sim()
    trade = _open_buy(sim)
    entry = trade.entry_price
    equity_before = sim.equity

    # Bar 1: tags T1 exactly (no TP2)
    sim.process_bar(T0 + timedelta(minutes=15), {"EURUSD": _bar(entry, trade.take_profit_1, entry, entry)})
    t1_lots = round(trade.lot_size * 0.5, 2)
    sl_pips = trade.sl_pips
    # T1 leg: 1R gross minus 1 pip exit cost, on HALF the lots
    expected_t1 = (sl_pips - 1.0) * 10.0 * t1_lots
    assert sim.equity - equity_before == pytest.approx(expected_t1)
    assert trade.remaining_lots == pytest.approx(trade.lot_size - t1_lots)
    assert trade.current_sl == pytest.approx(entry)  # breakeven

    # Bar 2: tags TP2 — pays the REMAINDER only. Low stays above breakeven
    # (the SL now sits at entry, and SL-first ordering would tag it).
    above_be = entry + 0.0002
    sim.process_bar(
        T0 + timedelta(minutes=30),
        {"EURUSD": _bar(above_be, trade.take_profit_2, above_be, above_be)},
    )
    tp2_pips = (trade.take_profit_2 - entry) / 0.0001 - 1.0  # minus exit cost
    expected_total = expected_t1 + tp2_pips * 10.0 * (trade.lot_size - t1_lots)
    assert sim.equity - equity_before == pytest.approx(expected_total)
    assert trade.status == "CLOSED"
    assert trade.pnl_dollars == pytest.approx(expected_total)


def test_same_bar_t1_and_tp2_banks_t1_first() -> None:
    """One wide bar spanning T1 and TP2: half banks at T1, half at TP2 —
    NOT the full position at TP2 (the old optimistic path)."""
    sim = _sim()
    trade = _open_buy(sim)
    entry = trade.entry_price

    sim.process_bar(
        T0 + timedelta(minutes=15),
        {"EURUSD": _bar(entry, trade.take_profit_2 + 0.0005, entry, entry)},
    )
    assert trade.status == "CLOSED"
    assert trade.exit_reason == "TP2_HIT"
    t1_lots = round(trade.lot_size * 0.5, 2)
    tp2_pips = (trade.take_profit_2 - entry) / 0.0001 - 1.0
    t1_pips = trade.sl_pips - 1.0
    expected = t1_pips * 10.0 * t1_lots + tp2_pips * 10.0 * (trade.lot_size - t1_lots)
    assert trade.pnl_dollars == pytest.approx(expected)


def test_sl_fills_at_bar_open_when_gapped_through() -> None:
    """Weekend/news gap: the bar opens 10 pips below the stop — a stop is a
    market order and fills at the open, not at the level."""
    sim = _sim()
    trade = _open_buy(sim)
    gap_open = trade.current_sl - 0.0010

    sim.process_bar(
        T0 + timedelta(minutes=15),
        {"EURUSD": _bar(gap_open, gap_open + 0.0002, gap_open - 0.0002, gap_open)},
    )
    assert trade.exit_reason == "SL_HIT"
    # Net exit = gap open minus 1 pip exit cost — strictly worse than the SL level
    assert trade.exit_price == pytest.approx(gap_open - 0.0001)
    assert trade.pnl_dollars < -(trade.sl_pips * 10.0 * trade.lot_size) * 0.99


def test_equity_curve_is_mark_to_market() -> None:
    """Floating losses must show in the curve and the drawdown breaker —
    _unrealized_pnl was hardcoded 0.0."""
    sim = _sim()
    trade = _open_buy(sim, sl=1.0950)  # wide SL so the drop stays open
    entry = trade.entry_price
    drop = entry - 0.0030  # -30 pips floating

    sim.process_bar(T0 + timedelta(minutes=15), {"EURUSD": _bar(entry, entry, drop, drop)})
    assert trade.status != "CLOSED"
    _, mtm = sim.equity_curve[-1]
    expected_float = -30.0 * 10.0 * trade.lot_size
    assert mtm - sim.equity == pytest.approx(expected_float, rel=1e-6)
    assert sim.max_drawdown_pct > 0.0


def test_stale_tighten_moves_the_live_stop() -> None:
    """Regression: pip_size computed as min_sl/min_sl == 1.0 and the tighten
    wrote trade.stop_loss while exits read trade.current_sl — a double no-op."""
    sim = _sim()
    trade = _open_buy(sim)
    entry = trade.entry_price
    flat = entry - 0.0001  # slightly underwater, not at SL

    # 95 minutes in, flat: phase-1 tighten should move current_sl to half distance
    actions = sim.process_bar(T0 + timedelta(minutes=95), {"EURUSD": _bar(flat, flat, flat, flat)})
    assert any("STALE TIGHTEN" in a for a in actions)
    expected_sl = entry - (trade.sl_pips / 2.0) * 0.0001
    assert trade.current_sl == pytest.approx(expected_sl)

    # Next bar touches the tightened stop -> exit (the old code never did)
    sim.process_bar(
        T0 + timedelta(minutes=110),
        {"EURUSD": _bar(flat, flat, expected_sl - 0.0001, expected_sl)},
    )
    assert trade.exit_reason == "SL_HIT"


def test_commission_charged_per_lot_at_close() -> None:
    sim = _sim(commission_per_lot=7.0)
    trade = _open_buy(sim)
    equity_before = sim.equity
    sl = trade.current_sl

    sim.process_bar(T0 + timedelta(minutes=15), {"EURUSD": _bar(sl, sl, sl - 0.0002, sl)})
    loss_pips = trade.sl_pips + 1.0  # SL distance + exit cost
    expected = -loss_pips * 10.0 * trade.lot_size - 7.0 * trade.lot_size
    assert sim.equity - equity_before == pytest.approx(expected)
