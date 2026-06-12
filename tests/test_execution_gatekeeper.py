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
from helix_v3.orchestrator_v2 import HelixOrchestratorV2


def _gatekeeper() -> MT5ExecutionGatekeeper:
    gatekeeper = MT5ExecutionGatekeeper.__new__(MT5ExecutionGatekeeper)
    gatekeeper._active_orders = {}
    gatekeeper.journal = SimpleNamespace()
    return gatekeeper


def _signal(symbol: str, low: float, high: float) -> QuantSignal:
    return QuantSignal(
        symbol=symbol,
        timeframe="M15",
        timestamp=datetime(2026, 6, 12, 8, 0, tzinfo=timezone.utc),
        session_bounds=SessionBounds(
            high=high,
            low=low,
            range_pips=10.0,
            volatility_compression=0.5,
            is_accumulation=True,
            timestamp=datetime(2026, 6, 12, 7, 0, tzinfo=timezone.utc),
        ),
        stop_hunt=None,
        ema_vector=EMAVector(
            ema_5_angle=0.0,
            ema_13_angle=0.0,
            ema_50_angle=0.0,
            ema_200_angle=0.0,
            ema_800_angle=0.0,
            fast_slow_divergence=0.0,
            trend_alignment=Direction.BUY,
        ),
        accumulation_active=True,
        stop_hunt_detected=True,
        pre_filter_passed=True,
    )


def test_build_order_widens_tight_structural_stop_to_pair_floor(monkeypatch) -> None:
    gatekeeper = _gatekeeper()
    monkeypatch.setattr(gatekeeper, "check_drawdown_limit", lambda: True)
    monkeypatch.setattr(gatekeeper, "check_position_limit", lambda: True)
    monkeypatch.setattr(gatekeeper, "_check_spread", lambda symbol: True)
    monkeypatch.setattr(gatekeeper, "_get_pip_value", lambda symbol: 0.01)
    monkeypatch.setattr(gatekeeper, "calculate_lot_size", lambda symbol, sl_pips: 0.10)
    monkeypatch.setattr(
        gatekeeper_mod.mt5,
        "symbol_info_tick",
        lambda symbol: SimpleNamespace(ask=200.00, bid=199.99),
    )

    order = gatekeeper.build_order(
        "GBPJPY",
        _signal("GBPJPY", low=199.95, high=200.05),
        ConsensusResult(agreed=True, direction=Direction.BUY, avg_confidence=80.0),
    )

    assert order is not None
    assert order.sl_pips == 25.0
    assert order.stop_loss == 199.75
    assert order.take_profit_1 == 200.25
    assert order.take_profit_2 == 200.625
    assert order.risk_reward == 2.5


def test_manage_open_positions_uses_wall_clock_when_mt5_time_is_unavailable(monkeypatch) -> None:
    gatekeeper = _gatekeeper()
    now = int(datetime.now(timezone.utc).timestamp())
    position = SimpleNamespace(
        magic=314159,
        ticket=101,
        symbol="EURUSD",
        type=0,
        volume=0.10,
        price_open=1.1000,
        price_current=1.1000,
        sl=1.0985,
        tp=1.1030,
        time=now - 91 * 60,
    )
    gatekeeper._active_orders[101] = ExecutionOrder(
        symbol="EURUSD",
        direction=Direction.BUY,
        lot_size=0.10,
        entry_price=1.1000,
        stop_loss=1.0985,
        take_profit_1=1.1015,
        take_profit_2=1.1030,
        sl_pips=15.0,
        risk_reward=2.0,
        ticket=101,
        status="FILLED",
    )
    closed = []

    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", lambda: [position])
    monkeypatch.setattr(gatekeeper_mod.mt5, "symbol_info_tick", lambda symbol: None)
    monkeypatch.setattr(gatekeeper, "_get_pip_value", lambda symbol: 0.0001)
    monkeypatch.setattr(gatekeeper, "_partial_close", lambda pos, volume: closed.append((pos.ticket, volume)) or True)

    actions = gatekeeper.manage_open_positions()

    assert closed == [(101, 0.10)]
    assert actions == ["STALE EXIT: EURUSD BUY ticket=101 +0.0 pips after 91min"]


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


def _patch_exec_env(monkeypatch, gatekeeper) -> None:
    monkeypatch.setattr(
        gatekeeper, "_get_symbol_info", lambda symbol: SimpleNamespace(volume_min=0.01)
    )
    monkeypatch.setattr(
        gatekeeper_mod.mt5,
        "symbol_info_tick",
        lambda symbol: SimpleNamespace(ask=1.1000, bid=1.0999),
    )
    monkeypatch.setattr(
        gatekeeper_mod.mt5,
        "order_check",
        lambda request: SimpleNamespace(retcode=0, comment="ok"),
    )


def test_execute_order_adopts_fill_after_none_result_without_resending(monkeypatch) -> None:
    """order_send returning None can still mean the order reached the server.

    Regression: the old loop blindly resent full volume up to 2 more times.
    """
    gatekeeper = _gatekeeper()
    _patch_exec_env(monkeypatch, gatekeeper)
    sends: list = []
    state = {"sent": False}

    def fake_order_send(request):
        sends.append(dict(request))
        state["sent"] = True
        return None  # ...but the position appears server-side

    def fake_positions_get(symbol=None):
        if state["sent"]:
            return [SimpleNamespace(ticket=555, magic=314159, type=0, volume=0.10)]
        return []

    monkeypatch.setattr(gatekeeper_mod.mt5, "order_send", fake_order_send)
    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", fake_positions_get)

    order = _exec_order()
    ticket = gatekeeper.execute_order(order)

    assert ticket == 555
    assert len(sends) == 1  # never resent
    assert order.status == "FILLED"
    assert gatekeeper._active_orders[555] is order


def test_execute_order_resends_only_remainder_after_partial_fill(monkeypatch) -> None:
    """DONE_PARTIAL leaves a live position — only the remainder may be resent."""
    gatekeeper = _gatekeeper()
    _patch_exec_env(monkeypatch, gatekeeper)
    sends: list = []
    state = {"filled": 0.0}

    def fake_order_send(request):
        sends.append(dict(request))
        if len(sends) == 1:
            state["filled"] = 0.06
            return SimpleNamespace(
                retcode=gatekeeper_mod.mt5.TRADE_RETCODE_DONE_PARTIAL,
                order=601, volume=0.06, comment="partial",
            )
        return SimpleNamespace(
            retcode=gatekeeper_mod.mt5.TRADE_RETCODE_DONE,
            order=602, volume=request["volume"], comment="done",
        )

    def fake_positions_get(symbol=None):
        if state["filled"]:
            return [SimpleNamespace(ticket=601, magic=314159, type=0, volume=state["filled"])]
        return []

    monkeypatch.setattr(gatekeeper_mod.mt5, "order_send", fake_order_send)
    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", fake_positions_get)

    ticket = gatekeeper.execute_order(_exec_order())

    assert [s["volume"] for s in sends] == [0.10, 0.04]
    assert ticket == 602


def test_execute_order_never_resends_after_placed_retcode(monkeypatch) -> None:
    """PLACED means accepted-pending — resending would risk a double fill."""
    gatekeeper = _gatekeeper()
    _patch_exec_env(monkeypatch, gatekeeper)
    sends: list = []

    def fake_order_send(request):
        sends.append(dict(request))
        return SimpleNamespace(
            retcode=gatekeeper_mod.mt5.TRADE_RETCODE_PLACED,
            order=0, volume=0.0, comment="placed",
        )

    monkeypatch.setattr(gatekeeper_mod.mt5, "order_send", fake_order_send)
    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", lambda symbol=None: [])

    order = _exec_order()
    ticket = gatekeeper.execute_order(order)

    assert ticket is None
    assert len(sends) == 1
    assert order.status == "PENDING"


def test_execute_order_retries_full_volume_when_nothing_filled(monkeypatch) -> None:
    gatekeeper = _gatekeeper()
    _patch_exec_env(monkeypatch, gatekeeper)
    sends: list = []

    def fake_order_send(request):
        sends.append(dict(request))
        if len(sends) == 1:
            return SimpleNamespace(
                retcode=gatekeeper_mod.mt5.TRADE_RETCODE_REQUOTE,
                order=0, volume=0.0, comment="requote",
            )
        return SimpleNamespace(
            retcode=gatekeeper_mod.mt5.TRADE_RETCODE_DONE,
            order=700, volume=request["volume"], comment="done",
        )

    monkeypatch.setattr(gatekeeper_mod.mt5, "order_send", fake_order_send)
    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", lambda symbol=None: [])

    ticket = gatekeeper.execute_order(_exec_order())

    assert [s["volume"] for s in sends] == [0.10, 0.10]
    assert ticket == 700


def _patch_lot_env(monkeypatch, gatekeeper, equity: float, volume_step: float = 0.01) -> None:
    """1 lot = $1/pip, EURUSD-like 5-digit symbol, fake low-tier profile."""
    monkeypatch.setattr(gatekeeper, "_get_account_equity", lambda: equity)
    monkeypatch.setattr(gatekeeper, "_get_pip_value", lambda symbol: 0.0001)
    monkeypatch.setattr(
        gatekeeper,
        "_get_symbol_info",
        lambda symbol: SimpleNamespace(
            volume_min=0.01,
            volume_max=100.0,
            volume_step=volume_step,
            trade_tick_value=1.0,
            trade_tick_size=0.0001,
        ),
    )
    monkeypatch.setattr(
        gatekeeper_mod,
        "get_pair_profile",
        lambda symbol: SimpleNamespace(
            max_risk_pct=0.01,
            min_sl_pips=15.0,
            max_lot_size=5.0,
            risk_tier="low",
        ),
    )


def test_lot_sizing_rejects_when_even_min_lot_exceeds_risk_cap(monkeypatch) -> None:
    """Regression: layer 3 used to clamp to vol_min and send anyway."""
    gatekeeper = _gatekeeper()
    # $20 equity, 100-pip SL: min lot 0.01 risks $1 = 5% > 3% hard cap
    _patch_lot_env(monkeypatch, gatekeeper, equity=20.0)
    assert gatekeeper.calculate_lot_size("EURUSD", sl_pips=100.0) is None


def test_lot_sizing_floors_to_volume_step_instead_of_rounding_up(monkeypatch) -> None:
    gatekeeper = _gatekeeper()
    # $1000 * 1% = $10 risk over 15 pips -> raw 0.667 lots; step 0.1 must
    # floor to 0.6, not round to 0.7 (which would exceed the intended risk).
    _patch_lot_env(monkeypatch, gatekeeper, equity=1000.0, volume_step=0.1)
    assert gatekeeper.calculate_lot_size("EURUSD", sl_pips=15.0) == 0.6


def test_build_order_aborts_when_lot_sizing_rejects(monkeypatch) -> None:
    gatekeeper = _gatekeeper()
    monkeypatch.setattr(gatekeeper, "check_drawdown_limit", lambda: True)
    monkeypatch.setattr(gatekeeper, "check_position_limit", lambda: True)
    monkeypatch.setattr(gatekeeper, "_check_spread", lambda symbol: True)
    monkeypatch.setattr(gatekeeper, "_get_pip_value", lambda symbol: 0.01)
    monkeypatch.setattr(gatekeeper, "calculate_lot_size", lambda symbol, sl_pips: None)
    monkeypatch.setattr(
        gatekeeper_mod.mt5,
        "symbol_info_tick",
        lambda symbol: SimpleNamespace(ask=200.00, bid=199.99),
    )

    order = gatekeeper.build_order(
        "GBPJPY",
        _signal("GBPJPY", low=199.95, high=200.05),
        ConsensusResult(agreed=True, direction=Direction.BUY, avg_confidence=80.0),
    )
    assert order is None


def test_execute_order_aborts_when_order_check_fails(monkeypatch) -> None:
    gatekeeper = _gatekeeper()
    _patch_exec_env(monkeypatch, gatekeeper)
    monkeypatch.setattr(
        gatekeeper_mod.mt5,
        "order_check",
        lambda request: SimpleNamespace(retcode=10019, comment="No money"),
    )
    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", lambda symbol=None: [])
    sends: list = []
    monkeypatch.setattr(
        gatekeeper_mod.mt5, "order_send", lambda request: sends.append(request)
    )

    order = _exec_order()
    assert gatekeeper.execute_order(order) is None
    assert sends == []  # never reached the server
    assert order.status == "REJECTED"


def _orphan_position(sl: float, current: float = 1.1020) -> SimpleNamespace:
    now = int(datetime.now(timezone.utc).timestamp())
    return SimpleNamespace(
        magic=314159,
        ticket=909,
        symbol="EURUSD",
        type=0,  # BUY
        volume=0.05,
        price_open=1.1000,
        price_current=current,
        sl=sl,
        tp=1.1040,
        time=now - 10 * 60,  # 10 min old — no time/stale exits
    )


def _patch_manage_env(monkeypatch, gatekeeper, position) -> tuple:
    partial_closes: list = []
    sl_modifies: list = []
    monkeypatch.setattr(gatekeeper_mod.mt5, "positions_get", lambda: [position])
    monkeypatch.setattr(
        gatekeeper_mod.mt5,
        "symbol_info_tick",
        lambda symbol: SimpleNamespace(
            time=int(datetime.now(timezone.utc).timestamp()), ask=1.1021, bid=1.1020
        ),
    )
    monkeypatch.setattr(gatekeeper, "_get_pip_value", lambda symbol: 0.0001)
    monkeypatch.setattr(
        gatekeeper, "_partial_close",
        lambda pos, volume: partial_closes.append((pos.ticket, volume)) or True,
    )
    monkeypatch.setattr(
        gatekeeper, "_modify_sl",
        lambda ticket, symbol, new_sl: sl_modifies.append((ticket, new_sl)) or True,
    )
    # Pin the session so the session-exit rule can't fire during the test
    import helix_v3.scanner.market_scanner as scanner_mod
    monkeypatch.setattr(scanner_mod, "_get_session_name", lambda: "LONDON")
    return partial_closes, sl_modifies


def test_orphan_adoption_at_breakeven_does_not_refire_t1(monkeypatch) -> None:
    """Regression: a post-T1 position (SL at entry) got take_profit_1=entry
    reconstructed on restart, firing a second 50% partial close every time."""
    gatekeeper = _gatekeeper()
    gatekeeper._risk_cfg = gatekeeper_mod.settings.risk
    position = _orphan_position(sl=1.1000)  # breakeven SL = post-T1
    partial_closes, _ = _patch_manage_env(monkeypatch, gatekeeper, position)

    gatekeeper.manage_open_positions()

    adopted = gatekeeper._active_orders[909]
    assert adopted.status == "T1_HIT"
    assert partial_closes == []  # no second partial close


def test_orphan_adoption_pre_t1_reconstructs_t1_from_sl_distance(monkeypatch) -> None:
    gatekeeper = _gatekeeper()
    gatekeeper._risk_cfg = gatekeeper_mod.settings.risk
    # SL 15 pips below entry, price barely moved — normal pre-T1 position
    position = _orphan_position(sl=1.0985, current=1.1002)
    partial_closes, _ = _patch_manage_env(monkeypatch, gatekeeper, position)

    gatekeeper.manage_open_positions()

    adopted = gatekeeper._active_orders[909]
    assert adopted.status == "FILLED"
    assert abs(adopted.take_profit_1 - 1.1015) < 1e-9
    assert abs(adopted.sl_pips - 15.0) < 1e-6
    assert partial_closes == []


def _orchestrator(direction: Direction = Direction.SELL) -> tuple:
    """Bare orchestrator with a recording guard and one active GBPJPY order."""
    orchestrator = HelixOrchestratorV2.__new__(HelixOrchestratorV2)
    orchestrator._symbols = ["GBPJPY"]
    orchestrator.gatekeeper = SimpleNamespace(
        _active_orders={
            202: ExecutionOrder(
                symbol="GBPJPY",
                direction=direction,
                lot_size=0.10,
                entry_price=200.0,
                stop_loss=200.5,
                take_profit_1=199.5,
                take_profit_2=198.75,
                sl_pips=50.0,
                risk_reward=2.5,
                ticket=202,
                status="FILLED",
            )
        },
        journal=SimpleNamespace(),
    )
    losses: list = []
    exits: list = []
    orchestrator.guard = SimpleNamespace(
        record_loss=lambda symbol, direction: losses.append((symbol, direction)),
        record_exit=lambda symbol: exits.append(symbol),
    )
    return orchestrator, losses, exits


# Every action string manage_open_positions can emit, and whether the
# position is closed afterwards. If a new action is added to the gatekeeper
# it must be classified here.
GATEKEEPER_ACTIONS = {
    "TIME EXIT: GBPJPY SELL ticket=202 after 240min pips=-8.2": True,
    "TIME EXIT: GBPJPY SELL ticket=202 after 240min pips=+14.2": True,
    "STALE EXIT: GBPJPY SELL ticket=202 -3.0 pips after 135min": True,
    "STALE EXIT: GBPJPY BUY ticket=202 +0.0 pips after 91min": True,
    "SESSION EXIT: GBPJPY BUY ticket=202 before ASIAN_EARLY pips=-2.0": True,
    "SESSION EXIT: GBPJPY BUY ticket=202 before ASIAN_EARLY pips=+1.5": True,
    "STALE TIGHTEN: GBPJPY ticket=202 SL halved at 92min, exit at 135min if still flat": False,
    "T1 HIT: GBPJPY ticket=202 +25.0 pips, closed 0.05 lots": False,
    "TRAIL: GBPJPY ticket=202 SL->200.50000 locking 12.3 pips": False,
}


def test_exit_action_classification_covers_every_gatekeeper_action() -> None:
    for action, is_exit in GATEKEEPER_ACTIONS.items():
        assert HelixOrchestratorV2._is_exit_action(action) is is_exit, action


def test_open_position_management_actions_never_record_guard_loss() -> None:
    """TRAIL/T1/STALE TIGHTEN mention 'SL' but the position is still open.

    Regression: the old substring matcher recorded a loss for every TRAIL
    update, so two trails on a winning trade day-banned its direction.
    """
    orchestrator, losses, _ = _orchestrator()
    for action, is_exit in GATEKEEPER_ACTIONS.items():
        if not is_exit:
            orchestrator._record_guard_loss_from_action(action)
    assert losses == []


def test_only_negative_pips_exits_record_guard_loss() -> None:
    orchestrator, losses, _ = _orchestrator()
    for action in GATEKEEPER_ACTIONS:
        orchestrator._record_guard_loss_from_action(action)
    assert losses == [
        ("GBPJPY", "SELL"),  # TIME EXIT pips=-8.2
        ("GBPJPY", "SELL"),  # STALE EXIT -3.0 pips
        ("GBPJPY", "BUY"),   # SESSION EXIT pips=-2.0
    ]


def test_loss_direction_parsed_from_action_overrides_active_order() -> None:
    # Active order says SELL, but the exit action says BUY — trust the action.
    orchestrator, losses, _ = _orchestrator(direction=Direction.SELL)
    orchestrator._record_guard_loss_from_action(
        "SESSION EXIT: GBPJPY BUY ticket=202 before ASIAN_EARLY pips=-2.0"
    )
    assert losses == [("GBPJPY", "BUY")]


def test_orchestrator_records_guard_loss_direction_from_active_order() -> None:
    orchestrator = HelixOrchestratorV2.__new__(HelixOrchestratorV2)
    orchestrator._symbols = ["GBPJPY"]
    orchestrator.gatekeeper = SimpleNamespace(
        _active_orders={
            202: ExecutionOrder(
                symbol="GBPJPY",
                direction=Direction.SELL,
                lot_size=0.10,
                entry_price=200.0,
                stop_loss=200.5,
                take_profit_1=199.5,
                take_profit_2=198.75,
                sl_pips=50.0,
                risk_reward=2.5,
                ticket=202,
                status="FILLED",
            )
        },
        journal=SimpleNamespace(),
    )
    losses = []
    orchestrator.guard = SimpleNamespace(record_loss=lambda symbol, direction: losses.append((symbol, direction)))

    orchestrator._record_guard_loss_from_action("STALE EXIT: GBPJPY ticket=202 -3.0 pips after 135min")

    assert losses == [("GBPJPY", "SELL")]

