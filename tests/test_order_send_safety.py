"""Tests for order-send portability + safety (audit Tier 3.3)."""
from __future__ import annotations

from types import SimpleNamespace

from helix_v3.execution import gatekeeper as gatekeeper_mod
from helix_v3.execution.gatekeeper import MT5ExecutionGatekeeper


def _gatekeeper() -> MT5ExecutionGatekeeper:
    gk = MT5ExecutionGatekeeper.__new__(MT5ExecutionGatekeeper)
    gk._active_orders = {}
    return gk


def _info(**kw) -> SimpleNamespace:
    base = dict(
        digits=5,
        point=0.00001,
        filling_mode=2,
        trade_stops_level=0,
        trade_freeze_level=0,
        visible=True,
    )
    base.update(kw)
    return SimpleNamespace(**base)


# ---------------------------------------------------------------------------
# Filling mode + deviation
# ---------------------------------------------------------------------------

def test_filling_mode_follows_symbol_flags(monkeypatch) -> None:
    gk = _gatekeeper()
    cases = [
        (2, gatekeeper_mod.mt5.ORDER_FILLING_IOC),       # IOC supported
        (3, gatekeeper_mod.mt5.ORDER_FILLING_IOC),       # both -> prefer IOC
        (1, gatekeeper_mod.mt5.ORDER_FILLING_FOK),       # FOK only
        (0, gatekeeper_mod.mt5.ORDER_FILLING_RETURN),    # neither -> RETURN
    ]
    for flags, expected in cases:
        monkeypatch.setattr(
            gk, "_get_symbol_info", lambda symbol, f=flags: _info(filling_mode=f)
        )
        assert gk._filling_mode("EURUSD") == expected


def test_deviation_is_pips_not_points(monkeypatch) -> None:
    gk = _gatekeeper()
    # 5-digit FX: 1 pip = 10 points. EURUSD spread budget 2.0 pips -> 20 points.
    monkeypatch.setattr(gk, "_get_symbol_info", lambda s: _info())
    monkeypatch.setattr(gk, "_get_pip_value", lambda s: 0.0001)
    assert gk._deviation_points("EURUSD") == 20

    # Gold: pip == point (0.01) — budget 5.0 pips -> 5 points, NOT 10.
    monkeypatch.setattr(
        gk, "_get_symbol_info", lambda s: _info(digits=2, point=0.01)
    )
    monkeypatch.setattr(gk, "_get_pip_value", lambda s: 0.01)
    assert gk._deviation_points("XAUUSD") == 5


# ---------------------------------------------------------------------------
# _modify_sl safety
# ---------------------------------------------------------------------------

def _wire_modify(monkeypatch, gk, *, pos, tick, info, sent: list) -> None:
    monkeypatch.setattr(gk, "_get_symbol_info", lambda s: info)
    monkeypatch.setattr(
        gatekeeper_mod.mt5, "positions_get",
        lambda ticket=None, **kw: [pos] if ticket == pos.ticket else [],
    )
    monkeypatch.setattr(gatekeeper_mod.mt5, "symbol_info_tick", lambda s: tick)
    monkeypatch.setattr(
        gatekeeper_mod.mt5, "order_send",
        lambda req: sent.append(req) or SimpleNamespace(
            retcode=gatekeeper_mod.mt5.TRADE_RETCODE_DONE
        ),
    )


def test_modify_sl_preserves_tp_and_rounds_to_digits(monkeypatch) -> None:
    """TRADE_ACTION_SLTP with tp omitted CLEARS the TP — it must be carried."""
    gk = _gatekeeper()
    sent: list = []
    pos = SimpleNamespace(
        ticket=7, type=gatekeeper_mod.mt5.POSITION_TYPE_BUY,
        sl=199.50, tp=201.2345678, price_open=199.80,
    )
    _wire_modify(
        monkeypatch, gk,
        pos=pos,
        tick=SimpleNamespace(bid=200.50, ask=200.52),
        info=_info(digits=3, point=0.001),
        sent=sent,
    )

    assert gk._modify_sl(7, "GBPJPY", 200.1234567) is True
    req = sent[0]
    assert req["tp"] == 201.235      # preserved, rounded to 3 digits
    assert req["sl"] == 200.123      # rounded to symbol digits, not 5


def test_modify_sl_clamps_to_stops_level(monkeypatch) -> None:
    gk = _gatekeeper()
    sent: list = []
    pos = SimpleNamespace(
        ticket=7, type=gatekeeper_mod.mt5.POSITION_TYPE_BUY,
        sl=199.50, tp=0.0, price_open=199.80,
    )
    # stops_level 200 points x 0.001 = 0.200 price units; bid 200.50
    _wire_modify(
        monkeypatch, gk,
        pos=pos,
        tick=SimpleNamespace(bid=200.50, ask=200.52),
        info=_info(digits=3, point=0.001, trade_stops_level=200),
        sent=sent,
    )

    # Request 200.45 (only 0.05 from bid) -> clamped to 200.30
    assert gk._modify_sl(7, "GBPJPY", 200.45) is True
    assert sent[0]["sl"] == 200.300


def test_modify_sl_skips_when_clamp_would_loosen(monkeypatch) -> None:
    gk = _gatekeeper()
    sent: list = []
    pos = SimpleNamespace(
        ticket=7, type=gatekeeper_mod.mt5.POSITION_TYPE_BUY,
        sl=200.40, tp=0.0, price_open=199.80,  # existing stop already tight
    )
    _wire_modify(
        monkeypatch, gk,
        pos=pos,
        tick=SimpleNamespace(bid=200.50, ask=200.52),
        info=_info(digits=3, point=0.001, trade_stops_level=200),
        sent=sent,
    )

    # Clamp target (200.30) is BELOW the existing 200.40 stop -> skip, no send
    assert gk._modify_sl(7, "GBPJPY", 200.48) is False
    assert sent == []


def test_modify_sl_respects_freeze_level(monkeypatch) -> None:
    gk = _gatekeeper()
    sent: list = []
    pos = SimpleNamespace(
        ticket=7, type=gatekeeper_mod.mt5.POSITION_TYPE_BUY,
        sl=200.45, tp=0.0, price_open=199.80,
    )
    # freeze 100 points x 0.001 = 0.100; bid 200.50, stop 0.05 away -> frozen
    _wire_modify(
        monkeypatch, gk,
        pos=pos,
        tick=SimpleNamespace(bid=200.50, ask=200.52),
        info=_info(digits=3, point=0.001, trade_freeze_level=100),
        sent=sent,
    )

    assert gk._modify_sl(7, "GBPJPY", 200.49) is False
    assert sent == []


def test_modify_sl_falls_back_when_precheck_unavailable(monkeypatch) -> None:
    """Lookup failures degrade to the old raw modify, not a crash."""
    gk = _gatekeeper()
    sent: list = []
    monkeypatch.setattr(
        gk, "_get_symbol_info",
        lambda s: (_ for _ in ()).throw(ValueError("no symbol")),
    )
    monkeypatch.setattr(
        gatekeeper_mod.mt5, "order_send",
        lambda req: sent.append(req) or SimpleNamespace(
            retcode=gatekeeper_mod.mt5.TRADE_RETCODE_DONE
        ),
    )

    assert gk._modify_sl(7, "GBPJPY", 200.1) is True
    assert sent[0]["sl"] == 200.1
    assert "tp" not in sent[0]
