"""Execution-layer test matrix (audit Tier 3.6 — the final audit item).

Where test_execution_gatekeeper.py and test_order_send_safety.py pin the
headline Tier 0.2/0.3/3.3 regressions, this file fills out the *matrix* around
the gatekeeper's hardest paths so a future edit to any branch trips a test:

  - order_send retcode/retry reconciliation — the branches NOT already pinned:
    a None that never reconciles, exhausted retries, terminal-error short
    circuit, a DONE_PARTIAL the server already shows fully filled, and a None
    that leaves a partial then completes (the Tier 0.3 double-fill defense).
  - lot-size pip arithmetic per instrument CLASS — FX major, JPY cross, gold,
    index. The (pip_size / tick_size) * tick_value derivation differs by class;
    the existing lot tests only exercise a single EURUSD-shaped mock.
  - orphan adoption pre-T1 and post-T1 on the SELL side (the existing tests
    cover BUY only) — neither may double-fire the 50% partial close.
  - kill-switch trip wiring — a tripped breaker must abort build_order, not
    just return False from check_drawdown_limit.

Style mirrors the sibling files: mt5 is mocked with SimpleNamespace, no live
terminal is ever touched.
"""
from __future__ import annotations

from datetime import datetime, timezone
from types import SimpleNamespace

from helix_v3.core.types import (
    ConsensusResult,
    Direction,
    EMAVector,
    ExecutionOrder,
    QuantSignal,
    SessionBounds,
)
from helix_v3.execution import gatekeeper as gatekeeper_mod
from helix_v3.execution.gatekeeper import MT5ExecutionGatekeeper


def _gatekeeper() -> MT5ExecutionGatekeeper:
    gk = MT5ExecutionGatekeeper.__new__(MT5ExecutionGatekeeper)
    gk._active_orders = {}
    gk.journal = SimpleNamespace()
    return gk


# ===========================================================================
# Lot-size pip arithmetic per instrument class
# ===========================================================================
#
# pip_size depends on digits: 3/5-digit symbols quote pips at 10x the point
# (1 pip = 10 points); 1/2-digit symbols (gold, indices) quote pips AT the
# point. pip_value_per_lot = (pip_size / tick_size) * tick_value. Each class
# below exercises a distinct combination.

INSTRUMENT_CLASSES = {
    # symbol:  (point,    digits, tick_size, tick_value, pip_size, pip_cost/lot)
    "EURUSD": (0.00001, 5, 0.00001, 1.00, 0.0001, 10.0),   # FX major
    "GBPJPY": (0.001,   3, 0.001,   0.65, 0.01,    6.5),    # JPY cross
    "XAUUSD": (0.01,    2, 0.01,    1.00, 0.01,    1.0),    # gold
    "US30":   (0.1,     1, 0.1,     0.50, 0.1,     0.5),    # index
}


def _spec(point, digits, tick_size, tick_value, **kw):
    base = dict(
        point=point,
        digits=digits,
        trade_tick_size=tick_size,
        trade_tick_value=tick_value,
        volume_min=0.01,
        volume_max=100.0,
        volume_step=0.01,
        visible=True,
    )
    base.update(kw)
    return SimpleNamespace(**base)


def test_pip_size_and_pip_cost_resolve_per_instrument_class(monkeypatch) -> None:
    gk = _gatekeeper()
    for symbol, (point, digits, ts, tv, exp_pip, exp_cost) in INSTRUMENT_CLASSES.items():
        monkeypatch.setattr(
            gk, "_get_symbol_info",
            lambda s, p=point, d=digits, ts=ts, tv=tv: _spec(p, d, ts, tv),
        )
        assert gk._get_pip_value(symbol) == exp_pip, symbol
        # pip cost scales linearly with lot size
        assert abs(gk._get_pip_cost(symbol, 1.0) - exp_cost) < 1e-9, symbol
        assert abs(gk._get_pip_cost(symbol, 0.5) - exp_cost / 2) < 1e-9, symbol


def _wire_lot_env(monkeypatch, gk, symbol, equity, risk_pct, min_sl) -> None:
    point, digits, ts, tv, pip_size, _ = INSTRUMENT_CLASSES[symbol]
    monkeypatch.setattr(gk, "_get_account_equity", lambda: equity)
    monkeypatch.setattr(gk, "_get_pip_value", lambda s: pip_size)
    monkeypatch.setattr(
        gk, "_get_symbol_info", lambda s: _spec(point, digits, ts, tv)
    )
    monkeypatch.setattr(
        gk, "_resolved_profile",
        lambda s: SimpleNamespace(
            max_risk_pct=risk_pct,
            min_sl_pips=min_sl,
            max_lot_size=50.0,
            risk_tier="test",
        ),
    )


def test_lot_size_fx_major(monkeypatch) -> None:
    # $10000 x 1% = $100 over 25 pips at $10/pip = 0.4 lots
    gk = _gatekeeper()
    _wire_lot_env(monkeypatch, gk, "EURUSD", equity=10000.0, risk_pct=0.01, min_sl=15.0)
    assert gk.calculate_lot_size("EURUSD", sl_pips=25.0) == 0.40


def test_lot_size_jpy_cross(monkeypatch) -> None:
    # $10000 x 0.8% = $80 over 30 pips at $6.5/pip = 0.4102.. -> FLOORED to 0.41
    gk = _gatekeeper()
    _wire_lot_env(monkeypatch, gk, "GBPJPY", equity=10000.0, risk_pct=0.008, min_sl=25.0)
    assert gk.calculate_lot_size("GBPJPY", sl_pips=30.0) == 0.41


def test_lot_size_gold(monkeypatch) -> None:
    # $10000 x 0.5% = $50 over 200 pips at $1/pip = 0.25 lots
    gk = _gatekeeper()
    _wire_lot_env(monkeypatch, gk, "XAUUSD", equity=10000.0, risk_pct=0.005, min_sl=150.0)
    assert gk.calculate_lot_size("XAUUSD", sl_pips=200.0) == 0.25


def test_lot_size_index(monkeypatch) -> None:
    # $10000 x 1% = $100 over 50 pips at $0.5/pip = 4.0 lots
    gk = _gatekeeper()
    _wire_lot_env(monkeypatch, gk, "US30", equity=10000.0, risk_pct=0.01, min_sl=20.0)
    assert gk.calculate_lot_size("US30", sl_pips=50.0) == 4.0


def test_lot_size_never_exceeds_three_percent_cap_any_class(monkeypatch) -> None:
    """The 3% account-proportional cap holds across every instrument class."""
    gk = _gatekeeper()
    for symbol in INSTRUMENT_CLASSES:
        _, _, _, _, pip_size, pip_cost = INSTRUMENT_CLASSES[symbol]
        _wire_lot_env(monkeypatch, gk, symbol, equity=10000.0, risk_pct=0.01, min_sl=10.0)
        lot = gk.calculate_lot_size(symbol, sl_pips=10.0)
        assert lot is not None, symbol
        actual_risk = lot * 10.0 * pip_cost  # sl_pips x pip_cost/lot x lot
        assert actual_risk <= 10000.0 * 0.03 + 1e-6, (symbol, actual_risk)


# ===========================================================================
# order_send retcode / retry matrix — branches not covered elsewhere
# ===========================================================================

def _exec_order(symbol: str = "EURUSD") -> ExecutionOrder:
    return ExecutionOrder(
        symbol=symbol,
        direction=Direction.BUY,
        lot_size=0.10,
        entry_price=1.1000,
        stop_loss=1.0985,
        take_profit_1=1.1015,
        take_profit_2=1.1030,
        sl_pips=15.0,
        risk_reward=2.0,
    )


def _patch_exec_env(monkeypatch, gk) -> None:
    monkeypatch.setattr(
        gk, "_get_symbol_info", lambda symbol: SimpleNamespace(volume_min=0.01)
    )
    monkeypatch.setattr(
        gatekeeper_mod.mt5, "symbol_info_tick",
        lambda symbol: SimpleNamespace(ask=1.1000, bid=1.0999),
    )
    monkeypatch.setattr(
        gatekeeper_mod.mt5, "order_check",
        lambda request: SimpleNamespace(retcode=0, comment="ok"),
    )


def test_none_result_that_never_reconciles_is_rejected(monkeypatch) -> None:
    """None on every attempt with NO server-side fill must abort, not adopt."""
    gk = _gatekeeper()
    _patch_exec_env(monkeypatch, gk)
    sends: list = []
    monkeypatch.setattr(
        gatekeeper_mod.mt5, "order_send",
        lambda req: sends.append(dict(req)) or None,
    )
    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", lambda symbol=None: [])

    order = _exec_order()
    assert gk.execute_order(order) is None
    assert order.status == "REJECTED"
    assert len(sends) == 3  # retried the full max_retries, never a phantom adopt


def test_none_then_partial_then_completes_resends_only_remainder(monkeypatch) -> None:
    """A None that left a partial fill must resend ONLY the unfilled remainder."""
    gk = _gatekeeper()
    _patch_exec_env(monkeypatch, gk)
    sends: list = []
    state = {"filled": 0.0}

    def fake_order_send(req):
        sends.append(dict(req))
        if len(sends) == 1:
            state["filled"] = 0.06  # server filled 0.06 despite the None
            return None
        return SimpleNamespace(
            retcode=gatekeeper_mod.mt5.TRADE_RETCODE_DONE,
            order=808, volume=req["volume"], comment="done",
        )

    def fake_positions_get(symbol=None):
        if state["filled"]:
            return [SimpleNamespace(ticket=801, magic=314159, type=0, volume=state["filled"])]
        return []

    monkeypatch.setattr(gatekeeper_mod.mt5, "order_send", fake_order_send)
    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", fake_positions_get)

    ticket = gk.execute_order(_exec_order())
    assert [s["volume"] for s in sends] == [0.10, 0.04]
    assert ticket == 808


def test_done_partial_already_fully_filled_finalizes_without_resend(monkeypatch) -> None:
    """If the server already shows the full size, DONE_PARTIAL must not resend."""
    gk = _gatekeeper()
    _patch_exec_env(monkeypatch, gk)
    sends: list = []

    def fake_order_send(req):
        sends.append(dict(req))
        return SimpleNamespace(
            retcode=gatekeeper_mod.mt5.TRADE_RETCODE_DONE_PARTIAL,
            order=900, volume=0.10, comment="partial-but-full",
        )

    monkeypatch.setattr(gatekeeper_mod.mt5, "order_send", fake_order_send)
    monkeypatch.setattr(
        gatekeeper_mod.mt5, "positions_get",
        lambda symbol=None: [SimpleNamespace(ticket=900, magic=314159, type=0, volume=0.10)],
    )

    order = _exec_order()
    ticket = gk.execute_order(order)
    assert ticket == 900
    assert len(sends) == 1  # full size already on the book — no remainder resend
    assert order.status == "FILLED"


def test_terminal_error_short_circuits_without_retrying(monkeypatch) -> None:
    """NO_MONEY (and peers) is terminal — break immediately, do not retry."""
    gk = _gatekeeper()
    _patch_exec_env(monkeypatch, gk)
    sends: list = []

    def fake_order_send(req):
        sends.append(dict(req))
        return SimpleNamespace(
            retcode=gatekeeper_mod.mt5.TRADE_RETCODE_NO_MONEY,
            order=0, volume=0.0, comment="no money",
        )

    monkeypatch.setattr(gatekeeper_mod.mt5, "order_send", fake_order_send)
    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", lambda symbol=None: [])

    order = _exec_order()
    assert gk.execute_order(order) is None
    assert order.status == "REJECTED"
    assert len(sends) == 1  # no retry on a terminal error


def test_exhausted_requote_retries_are_rejected(monkeypatch) -> None:
    """Non-terminal failures retry to max and then reject cleanly."""
    gk = _gatekeeper()
    _patch_exec_env(monkeypatch, gk)
    sends: list = []

    def fake_order_send(req):
        sends.append(dict(req))
        return SimpleNamespace(
            retcode=gatekeeper_mod.mt5.TRADE_RETCODE_REQUOTE,
            order=0, volume=0.0, comment="requote",
        )

    monkeypatch.setattr(gatekeeper_mod.mt5, "order_send", fake_order_send)
    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", lambda symbol=None: [])

    order = _exec_order()
    assert gk.execute_order(order, max_retries=3) is None
    assert order.status == "REJECTED"
    assert len(sends) == 3


# ===========================================================================
# Orphan adoption pre-T1 / post-T1 on the SELL side
# ===========================================================================

def _sell_orphan(sl: float, current: float) -> SimpleNamespace:
    now = int(datetime.now(timezone.utc).timestamp())
    return SimpleNamespace(
        magic=314159,
        ticket=777,
        symbol="EURUSD",
        type=1,  # SELL
        volume=0.05,
        price_open=1.1000,
        price_current=current,
        sl=sl,
        tp=1.0960,
        time=now - 10 * 60,  # 10 min old — no time/stale exits
    )


def _patch_manage_env(monkeypatch, gk, position) -> list:
    partial_closes: list = []
    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", lambda: [position])
    monkeypatch.setattr(
        gatekeeper_mod.mt5, "symbol_info_tick",
        lambda symbol: SimpleNamespace(
            time=int(datetime.now(timezone.utc).timestamp()),
            ask=position.price_current + 0.0001,
            bid=position.price_current,
        ),
    )
    monkeypatch.setattr(gk, "_get_pip_value", lambda symbol: 0.0001)
    monkeypatch.setattr(
        gk, "_partial_close",
        lambda pos, volume, **kw: partial_closes.append((pos.ticket, volume)) or True,
    )
    monkeypatch.setattr(gk, "_modify_sl", lambda ticket, symbol, new_sl: True)
    import helix_v3.scanner.market_scanner as scanner_mod
    monkeypatch.setattr(scanner_mod, "_get_session_name", lambda: "LONDON")
    return partial_closes


def test_sell_orphan_post_t1_breakeven_does_not_refire_t1(monkeypatch) -> None:
    gk = _gatekeeper()
    gk._risk_cfg = gatekeeper_mod.settings.risk
    # SELL with SL at breakeven (entry) = post-T1; 2 pips in profit
    position = _sell_orphan(sl=1.1000, current=1.0998)
    partial_closes = _patch_manage_env(monkeypatch, gk, position)

    gk.manage_open_positions()

    adopted = gk._active_orders[777]
    assert adopted.direction == Direction.SELL
    assert adopted.status == "T1_HIT"
    assert partial_closes == []  # no second 50% close


def test_sell_orphan_pre_t1_reconstructs_t1_from_sl_distance(monkeypatch) -> None:
    gk = _gatekeeper()
    gk._risk_cfg = gatekeeper_mod.settings.risk
    # SELL with SL 15 pips ABOVE entry (the stop for a short), barely moved
    position = _sell_orphan(sl=1.1015, current=1.0998)
    partial_closes = _patch_manage_env(monkeypatch, gk, position)

    gk.manage_open_positions()

    adopted = gk._active_orders[777]
    assert adopted.status == "FILLED"
    # T1 reconstructed 1:1 below entry for a short: 1.1000 - 0.0015
    assert abs(adopted.take_profit_1 - 1.0985) < 1e-9
    assert abs(adopted.sl_pips - 15.0) < 1e-6
    assert partial_closes == []


# ===========================================================================
# Kill-switch trip wiring — a tripped breaker aborts build_order
# ===========================================================================

def _signal(symbol: str, low: float, high: float) -> QuantSignal:
    return QuantSignal(
        symbol=symbol,
        timeframe="M15",
        timestamp=datetime(2026, 6, 12, 8, 0, tzinfo=timezone.utc),
        session_bounds=SessionBounds(
            high=high, low=low, range_pips=10.0, volatility_compression=0.5,
            is_accumulation=True,
            timestamp=datetime(2026, 6, 12, 7, 0, tzinfo=timezone.utc),
        ),
        stop_hunt=None,
        ema_vector=EMAVector(
            ema_5_angle=0.0, ema_13_angle=0.0, ema_50_angle=0.0,
            ema_200_angle=0.0, ema_800_angle=0.0, fast_slow_divergence=0.0,
            trend_alignment=Direction.BUY,
        ),
        accumulation_active=True,
        stop_hunt_detected=True,
        pre_filter_passed=True,
    )


def _risk_state(tmp_path):
    from helix_v3.execution.risk_state import RiskState
    return RiskState(
        db_path=tmp_path / "risk_state.db",
        max_daily_loss_pct=0.04,
        max_total_drawdown_pct=0.08,
    )


def test_tripped_kill_switch_aborts_build_order(tmp_path, monkeypatch) -> None:
    """A real RiskState trip must abort build_order at the FIRST gate.

    Every downstream gate and sizing is forced to succeed, so the only path
    to a None order is the kill switch — if its wiring regressed, build_order
    would proceed to a fully-built (non-None) order and this test would fail.
    """
    gk = _gatekeeper()
    gk.risk_state = _risk_state(tmp_path)
    gk._kill_notified_day = ""
    gk.kill_switch_callback = None

    account = {"balance": 1000.0, "equity": 1000.0}
    monkeypatch.setattr(gk, "_get_account_balance", lambda: account["balance"])
    monkeypatch.setattr(gk, "_get_account_equity", lambda: account["equity"])
    # Force everything AFTER the breaker open, so None can only be the breaker.
    monkeypatch.setattr(gk, "check_position_limit", lambda: True)
    monkeypatch.setattr(gk, "_check_spread", lambda s: True)
    monkeypatch.setattr(gk, "_check_news_blackout", lambda s: True)
    monkeypatch.setattr(gk, "_check_currency_exposure", lambda s, d: True)
    monkeypatch.setattr(gk, "_get_pip_value", lambda s: 0.0001)
    monkeypatch.setattr(gk, "calculate_lot_size", lambda s, sl_pips: 0.10)
    monkeypatch.setattr(
        gk, "_resolved_profile",
        lambda s: SimpleNamespace(
            sl_buffer_pips=3.0, expected_level_move_pips=70.0, min_sl_pips=15.0,
        ),
    )
    monkeypatch.setattr(
        gatekeeper_mod.mt5, "symbol_info_tick",
        lambda s: SimpleNamespace(ask=1.1010, bid=1.1009),
    )

    sig = _signal("EURUSD", 1.0990, 1.1010)
    cons = ConsensusResult(agreed=True, direction=Direction.BUY, avg_confidence=80.0)

    # Healthy: anchors the day and builds a real order (breaker open).
    assert gk.build_order("EURUSD", sig, cons) is not None

    # Realize a 5% loss -> daily limit trips -> build_order aborts.
    account["balance"] = account["equity"] = 950.0
    assert gk.build_order("EURUSD", sig, cons) is None
