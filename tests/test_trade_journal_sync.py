"""Tests for journal deal accounting, back-fill, and close classification
(audit Tier 3.4)."""
from __future__ import annotations

from datetime import datetime, timezone
from types import SimpleNamespace

import MetaTrader5 as mt5
import pytest

from helix_v3.journal.trade_journal import TradeJournal

MAGIC = 314159


@pytest.fixture
def journal(tmp_path):
    j = TradeJournal(db_path=tmp_path / "journal.db")
    yield j
    j.close()


def _insert_open_trade(j: TradeJournal, ticket: int, symbol="GBPJPY",
                       direction="BUY", entry=200.000) -> None:
    j._conn.execute(
        """INSERT INTO trades
           (ticket, symbol, timeframe, direction, setup_type, lot_size,
            entry_price, stop_loss, take_profit_1, take_profit_2,
            sl_pips, risk_reward, opened_at)
           VALUES (?, ?, 'M15', ?, 'MMM', 0.10, ?, 199.7, 200.3, 200.6,
                   30, 2.0, ?)""",
        (ticket, symbol, direction, entry,
         datetime(2026, 6, 12, 8, 0, tzinfo=timezone.utc).isoformat()),
    )
    j._conn.commit()


def _deal(*, entry, price, volume, profit=0.0, commission=0.0, swap=0.0,
          reason=getattr(mt5, "DEAL_REASON_EXPERT", 3), comment=""):
    return SimpleNamespace(
        entry=entry, price=price, volume=volume, profit=profit,
        commission=commission, swap=swap, reason=reason, comment=comment,
    )


def _wire(monkeypatch, *, positions=(), deals_by_ticket=None):
    monkeypatch.setattr(mt5, "positions_get", lambda **kw: list(positions))
    monkeypatch.setattr(
        mt5, "history_deals_get",
        lambda position=None, **kw: (deals_by_ticket or {}).get(position, []),
    )
    monkeypatch.setattr(
        mt5, "symbol_info",
        lambda s: SimpleNamespace(point=0.001, digits=3),
    )
    monkeypatch.setattr(
        mt5, "account_info", lambda: SimpleNamespace(equity=1000.0)
    )


def test_all_deals_summed_including_t1_leg(journal, monkeypatch) -> None:
    """Entry commission + T1 partial leg + final leg must ALL be counted.

    The old code read only the last deal: this trade's recorded P&L
    missed the T1 leg's +$10 profit and $0.75 of costs."""
    _insert_open_trade(journal, ticket=42)
    deals = [
        _deal(entry=mt5.DEAL_ENTRY_IN, price=200.000, volume=0.10,
              commission=-0.50),                                   # entry
        _deal(entry=mt5.DEAL_ENTRY_OUT, price=200.300, volume=0.05,
              profit=10.0, commission=-0.25, comment="HelixV3_T1"),  # T1 leg
        _deal(entry=mt5.DEAL_ENTRY_OUT, price=200.500, volume=0.05,
              profit=16.5, commission=-0.25, swap=-0.10,
              reason=getattr(mt5, "DEAL_REASON_TP", 5)),            # final
    ]
    _wire(monkeypatch, positions=(), deals_by_ticket={42: deals})

    stats = journal.sync_from_mt5()
    assert stats["closed"] == 1

    trade = journal.get_trade(42)
    assert trade["gross_profit"] == pytest.approx(26.5)       # 10 + 16.5
    assert trade["commission"] == pytest.approx(-1.0)          # all three legs
    assert trade["swap"] == pytest.approx(-0.10)
    # Exit price is the lot-weighted average of the OUT legs
    assert trade["exit_price"] == pytest.approx(200.400)
    # Weighted pips: (200.400 - 200.000) / 0.01 pip
    assert trade["pips_gained"] == pytest.approx(40.0)
    assert trade["exit_reason"] == "TP"                        # broker reason code


def test_helix_close_classified_from_own_comment(journal, monkeypatch) -> None:
    _insert_open_trade(journal, ticket=43)
    deals = [
        _deal(entry=mt5.DEAL_ENTRY_IN, price=200.000, volume=0.10),
        _deal(entry=mt5.DEAL_ENTRY_OUT, price=199.900, volume=0.10,
              profit=-6.6, comment="HelixV3_stale"),
    ]
    _wire(monkeypatch, positions=(), deals_by_ticket={43: deals})

    journal.sync_from_mt5()
    assert journal.get_trade(43)["exit_reason"] == "STALE_EXIT"


def test_sl_reason_code_beats_comment_text(journal, monkeypatch) -> None:
    """Broker reason codes win — no more 'sl' substring matching."""
    _insert_open_trade(journal, ticket=44)
    deals = [
        _deal(entry=mt5.DEAL_ENTRY_IN, price=200.000, volume=0.10),
        _deal(entry=mt5.DEAL_ENTRY_OUT, price=199.700, volume=0.10,
              profit=-19.8, reason=getattr(mt5, "DEAL_REASON_SL", 4),
              comment="arbitrary broker text"),
    ]
    _wire(monkeypatch, positions=(), deals_by_ticket={44: deals})

    journal.sync_from_mt5()
    assert journal.get_trade(44)["exit_reason"] == "SL"


def test_unknown_broker_position_is_backfilled(journal, monkeypatch) -> None:
    pos = SimpleNamespace(
        ticket=99, magic=MAGIC, symbol="EURUSD", type=0, volume=0.20,
        price_open=1.1000, sl=1.0950, tp=1.1100,
        time=datetime(2026, 6, 12, 9, 0, tzinfo=timezone.utc).timestamp(),
    )
    _wire(monkeypatch, positions=(pos,), deals_by_ticket={})

    stats = journal.sync_from_mt5()
    assert stats["backfilled"] == 1
    assert stats["closed"] == 0  # still open on broker — not closed

    trade = journal.get_trade(99)
    assert trade is not None
    assert trade["setup_type"] == "BACKFILL"
    assert trade["direction"] == "BUY"
    assert trade["closed_at"] is None

    # Second sync must not duplicate it
    assert journal.sync_from_mt5()["backfilled"] == 0


def test_foreign_magic_positions_ignored(journal, monkeypatch) -> None:
    pos = SimpleNamespace(
        ticket=77, magic=12345, symbol="EURUSD", type=0, volume=0.20,
        price_open=1.1000, sl=0.0, tp=0.0, time=0,
    )
    _wire(monkeypatch, positions=(pos,), deals_by_ticket={})
    assert journal.sync_from_mt5()["backfilled"] == 0
    assert journal.get_trade(77) is None
