from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd

from helix_v3.backtest.vision_store import label_future_path
from helix_v3.core.types import Direction


def test_label_future_path_buy_hits_take_profit_first() -> None:
    idx = pd.date_range("2026-06-04 10:00:00", periods=5, freq="15min")
    df = pd.DataFrame(
        {
            "Open": [1.1000, 1.1010, 1.1020, 1.1030, 1.1040],
            "High": [1.1005, 1.1025, 1.1040, 1.1050, 1.1060],
            "Low": [1.0995, 1.1008, 1.1018, 1.1029, 1.1038],
            "Close": [1.1002, 1.1020, 1.1035, 1.1045, 1.1055],
        },
        index=idx,
    )

    outcome = label_future_path(
        df,
        snapshot_at=datetime(2026, 6, 4, 10, 0, tzinfo=timezone.utc),
        direction=Direction.BUY,
        entry_price=1.1000,
        pip_size=0.0001,
        horizon_minutes=60,
        stop_loss_pips=20,
        take_profit_pips=20,
    )

    assert outcome.outcome == "WIN"
    assert outcome.hit_take_profit is True
    assert outcome.hit_stop_loss is False
    assert outcome.max_favorable_pips is not None
    assert outcome.max_favorable_pips >= 20
    assert outcome.max_adverse_pips is not None
    assert outcome.max_adverse_pips >= 0


def test_label_future_path_neutral_is_no_trade() -> None:
    idx = pd.date_range("2026-06-04 10:00:00", periods=2, freq="15min")
    df = pd.DataFrame(
        {
            "Open": [1.1000, 1.1010],
            "High": [1.1010, 1.1020],
            "Low": [1.0990, 1.1000],
            "Close": [1.1005, 1.1015],
        },
        index=idx,
    )

    outcome = label_future_path(
        df,
        snapshot_at=datetime(2026, 6, 4, 10, 0, tzinfo=timezone.utc),
        direction=Direction.NEUTRAL,
        entry_price=1.1000,
        pip_size=0.0001,
        horizon_minutes=60,
    )

    assert outcome.outcome == "NO_TRADE"
    assert outcome.pips_at_horizon is None
