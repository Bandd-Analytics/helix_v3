from __future__ import annotations

from helix_v3.core import reentry_guard
from helix_v3.core.reentry_guard import ReentryGuard


def test_reentry_guard_default_bans_same_direction_only(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(reentry_guard.mt5, "positions_get", lambda symbol=None: ())

    guard = ReentryGuard(db_path=tmp_path / "guard.db", ban_scope="direction")
    try:
        guard.record_loss("GBPUSD", "BUY")
        assert "COOLDOWN" in str(guard.check("GBPUSD", "BUY"))

        guard.record_loss("GBPUSD", "BUY")
        assert "BANNED" in str(guard.check("GBPUSD", "BUY"))
        assert guard.check("GBPUSD", "SELL") is None
        assert "GBPUSD" not in guard.get_status()["banned"]
    finally:
        guard.close()


def test_reentry_guard_symbol_scope_bans_opposite_direction(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(reentry_guard.mt5, "positions_get", lambda symbol=None: ())

    guard = ReentryGuard(db_path=tmp_path / "guard.db", ban_scope="symbol")
    try:
        guard.record_loss("EURJPY", "SELL")
        guard.record_loss("EURJPY", "SELL")

        assert "BANNED" in str(guard.check("EURJPY", "SELL"))
        assert "symbol-wide" in str(guard.check("EURJPY", "BUY"))
        assert "EURJPY" in guard.get_status()["banned"]
    finally:
        guard.close()
