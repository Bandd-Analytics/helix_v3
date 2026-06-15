"""Tests for the Phase 1 signature audit engine (edge discovery)."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from helix_v3.backtest import signature_audit as sa
from helix_v3.backtest.signature_audit import Outcome


def _o(symbol, direction, facets, day, favorable, net_r, dur_h=2):
    snap = datetime(2023, 1, 1, tzinfo=timezone.utc) + timedelta(days=day)
    return Outcome(
        symbol=symbol, direction=direction, facets=facets,
        snapshot_at=snap, exit_at=snap + timedelta(hours=dur_h),
        favorable=favorable, net_r=net_r,
    )


def _facets(**over):
    """13-tuple in normalized_key order with overridable named facets."""
    base = ["FAM", "BUY", "MID_WEEK", "L0", "LONDON", "AR_VALID",
            "HUNT_PAIR_RANGE", "PUSH1", "W_BOTTOM", "NO_RRT", "TDI_CONFIRM",
            "THE_33", "CONF_50_74"]
    for name, val in over.items():
        base[sa.FACET_INDEX[name]] = val
    return tuple(base)


def test_non_overlapping_drops_adjacent_events() -> None:
    # Three outcomes, each 2h long, snapped 1h apart -> only 2 survive
    f = _facets()
    items = [
        _o("EURUSD", "BUY", f, 0, True, 1.0, dur_h=2),
        # 1h later — overlaps the first's [0h,2h] window -> dropped
        Outcome("EURUSD", "BUY", f,
                datetime(2023, 1, 1, 1, tzinfo=timezone.utc),
                datetime(2023, 1, 1, 3, tzinfo=timezone.utc), True, 1.0),
        _o("EURUSD", "BUY", f, 1, True, 1.0, dur_h=2),
    ]
    kept = sa.non_overlapping(items)
    assert len(kept) == 2


def test_coarse_key_projects_selected_facets() -> None:
    o = _o("EURUSD", "BUY", _facets(tdi="TDI_CONFLICT"), 0, False, -1.0)
    assert sa.coarse_key(o, ["family", "direction", "tdi"]) == "FAM|BUY|TDI_CONFLICT"


def test_base_rate_is_per_symbol_direction() -> None:
    f = _facets()
    outs = (
        [_o("EURUSD", "BUY", f, d, d % 4 == 0, 0.0, dur_h=1) for d in range(40)]
        + [_o("EURUSD", "SELL", f, d, True, 0.0, dur_h=1) for d in range(40)]
    )
    rates = sa.base_rates(outs, pooled=False)
    assert abs(rates[("EURUSD", "BUY")] - 0.25) < 1e-9
    assert rates[("EURUSD", "SELL")] == 1.0


def test_validated_cell_needs_significance_and_holdout_replication() -> None:
    # Base rate ~25% (control). One cell fires favorable ~80% both in-sample
    # AND on the holdout -> should validate. Spaced 1 day apart, 1h duration:
    # non-overlapping keeps all.
    control_facets = _facets(tdi="TDI_NONE")          # the generic population
    edge_facets = _facets(tdi="TDI_CONFIRM")          # the candidate cell

    outcomes = []
    # In-sample control: 200 EURUSD BUY at 25% fav (2023)
    for d in range(200):
        outcomes.append(_o("EURUSD", "BUY", control_facets, d, d % 4 == 0, -0.2, dur_h=1))
    # In-sample edge: 60 at 80% fav, positive net R (2023, offset to avoid cl-overlap dates)
    for d in range(60):
        fav = d % 5 != 0  # 80%
        outcomes.append(_o("EURUSD", "BUY", edge_facets, 300 + d, fav, 0.5 if fav else -0.3, dur_h=1))

    # Holdout (2025+): same edge cell replicates at 80%
    hold0 = (sa.IN_SAMPLE_END - datetime(2023, 1, 1, tzinfo=timezone.utc)).days + 30
    for d in range(40):
        fav = d % 5 != 0
        outcomes.append(_o("EURUSD", "BUY", edge_facets, hold0 + d, fav, 0.5 if fav else -0.3, dur_h=1))
    # Holdout control so the holdout base rate stays ~25%
    for d in range(200):
        outcomes.append(_o("EURUSD", "BUY", control_facets, hold0 + d, d % 4 == 0, -0.2, dur_h=1))

    results = sa.audit_scheme(outcomes, "S_test", ["family", "direction", "tdi"], pooled=False)
    by_key = {r.key: r for r in results}
    edge = by_key["FAM|BUY|TDI_CONFIRM"]
    assert edge.bh_significant is True
    assert edge.mean_net_r > 0
    assert edge.holdout_n >= sa.MIN_HOLDOUT_N
    assert edge.verdict == "VALIDATED"


def test_underpowered_cell_is_insufficient_n() -> None:
    f = _facets()
    outcomes = [_o("EURUSD", "BUY", f, d, True, 1.0, dur_h=1) for d in range(10)]
    results = sa.audit_scheme(outcomes, "S_test", ["family", "direction", "tdi"], pooled=False)
    assert all(r.verdict == "INSUFFICIENT_N" for r in results)
