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

