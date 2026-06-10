from __future__ import annotations

from datetime import datetime, timezone
import sqlite3

from helix_v3.backtest.setup_intelligence import SCHEMA
from helix_v3.backtest.scanner_replay import ScannerCandidate
from helix_v3.backtest.validation_library import ValidationRecord
from helix_v3.core.types import Direction
from helix_v3.scanner.watchlist import (
    HistoricalSetupMatch,
    ScannerAlertCandidate,
    ScannerWatchlist,
    WatchlistConfig,
    evaluate_candidate,
    format_watchlist_report,
)


NOW = datetime(2026, 6, 8, 8, 0, tzinfo=timezone.utc)


def _candidate(**overrides) -> ScannerCandidate:
    data = {
        "id": 1,
        "scan_time": datetime(2026, 6, 8, 7, 45, tzinfo=timezone.utc),
        "symbol": "GBPJPY",
        "timeframe": "M15",
        "bid": 215.094,
        "ask": 215.100,
        "spread_pips": 0.6,
        "session": "LONDON",
        "bias": Direction.BUY,
        "trend": Direction.BUY,
        "trade_readiness": 80,
        "readiness_notes": "Stop hunt + absorption",
        "stop_hunt_active": True,
        "stop_hunt_direction": Direction.SELL,
        "stop_hunt_breach_pips": 29.9,
        "atr_14": 8.3,
    }
    data.update(overrides)
    return ScannerCandidate(**data)


def _record(**overrides) -> ValidationRecord:
    data = {
        "scope": "PAIR",
        "symbol": "GBPJPY",
        "direction": "SELL",
        "normalized_key": "GBPJPY_VALIDATED_SETUP",
        "setup_family": "THE_33_MW",
        "primary_theme": "GBP_WEAKNESS",
        "symbols": ["GBPJPY"],
        "total": 20,
        "favorable": 18,
        "favorable_rate": 90.0,
        "t1_rate": 60.0,
        "avg_exit_pips": 18.0,
        "avg_mfe": 28.0,
        "avg_mae": 7.0,
        "realistic_target_pips": 18.0,
        "confidence_score": 88.0,
        "entry_rules": {},
        "exit_rules": {},
        "example_source_ids": [1, 2],
    }
    data.update(overrides)
    return ValidationRecord(**data)


def _historical_match(**overrides) -> HistoricalSetupMatch:
    data = {
        "symbol": "GBPJPY",
        "direction": "SELL",
        "normalized_key": "GBPJPY_RESEARCH_SETUP",
        "total": 24,
        "favorable_rate": 66.7,
        "avg_exit_pips": 12.4,
        "fast_profit_rate": 20.8,
        "recurrence_per_30d": 0.9,
        "reappearance_score": 44.0,
        "opportunity_score": 52.0,
        "decision": "WATCH_RESEARCH",
        "top_session": "STOP_HUNT",
        "top_day": "Wednesday",
        "top_price_level": "AR_LOWER_MID",
    }
    data.update(overrides)
    return HistoricalSetupMatch(**data)


def test_high_readiness_scanner_candidate_is_watch_only_without_exact_validation() -> None:
    config = WatchlistConfig()
    alert = ScannerAlertCandidate(scanner=_candidate())

    item = evaluate_candidate(alert, config, now=NOW)

    assert item.status == "WATCH_ONLY"
    assert item.direction == Direction.SELL
    assert "exact setup signature missing" in item.blockers
    assert "no promoted validation-library match" in item.blockers


def test_historical_setup_context_does_not_promote_without_validation_match() -> None:
    config = WatchlistConfig()
    alert = ScannerAlertCandidate(scanner=_candidate())

    item = evaluate_candidate(
        alert,
        config,
        historical_matches=[
            _historical_match(
                expectancy_tier="DEMO_CANDIDATE",
                rrs_grade="R_REPEATER",
                profit_factor=1.35,
                payoff_ratio=2.0,
                split_passes=2,
            )
        ],
        now=NOW,
    )
    report = format_watchlist_report([item], config, generated_at=NOW)

    assert item.status == "WATCH_ONLY"
    assert item.validation_matches == 0
    assert item.historical_matches[0].decision == "WATCH_RESEARCH"
    assert "historical: WATCH_RESEARCH N=24 Fav=66.7%" in report
    assert "expectancy: DEMO_CANDIDATE RRS=R_REPEATER PF=1.35 Payoff=2.00 Splits=2/3" in report
    assert "gate: exact setup signature missing" in report


def test_alert_basket_gate_blocks_without_ranked_match() -> None:
    config = WatchlistConfig(require_alert_basket=True)
    alert = ScannerAlertCandidate(scanner=_candidate())

    item = evaluate_candidate(alert, config, now=NOW)

    assert item.status == "BLOCKED"
    assert "no ranked alert-basket match" in item.blockers


def test_ranked_basket_context_is_reported() -> None:
    config = WatchlistConfig(require_alert_basket=True)
    alert = ScannerAlertCandidate(scanner=_candidate())

    item = evaluate_candidate(
        alert,
        config,
        historical_matches=[
            _historical_match(
                expectancy_tier="DEMO_CANDIDATE",
                rrs_grade="R_RUNNER",
                profit_factor=2.5,
                payoff_ratio=3.0,
                split_passes=3,
                basket_rank=1,
                basket_mode="DEMO_ALERT",
            )
        ],
        now=NOW,
    )
    report = format_watchlist_report([item], config, generated_at=NOW)

    assert item.status == "WATCH_ONLY"
    assert "Basket gate: top 30 modes=DEMO_ALERT,WATCH_ALERT,ASYM_WATCH,RESEARCH_ONLY" in report
    assert "basket: #1 DEMO_ALERT" in report


def test_scanner_watchlist_loads_ranked_basket_matches(tmp_path) -> None:
    db = tmp_path / "setup_intelligence.db"
    conn = sqlite3.connect(str(db))
    conn.row_factory = sqlite3.Row
    try:
        conn.executescript(SCHEMA)
        conn.execute(
            """INSERT INTO expectancy_candidates (
                symbol, direction, normalized_key, setup_family, primary_theme,
                rrs_grade, candidate_tier, total, favorable, favorable_rate, t1_rate,
                fast_profit_rate, clean_departure_rate, avg_exit_pips, avg_win_pips,
                avg_loss_pips, gross_profit_pips, gross_loss_pips, profit_factor,
                payoff_ratio, avg_mfe, avg_mae, split_passes, split_summary,
                recurrence_per_30d, reappearance_score, opportunity_score, top_session,
                top_day, top_price_level, example_flashcards, notes
            ) VALUES (
                'GBPJPY', 'SELL', 'GBPJPY_BASKET_SETUP', 'THE_33_MW', 'GBP',
                'R_RUNNER', 'DEMO_CANDIDATE', 10, 9, 90.0, 50.0,
                30.0, 40.0, 18.4, 22.0, -3.0, 198.0, 3.0, 66.0,
                7.33, 35.0, 4.0, 3, 'train:N=4,Avg=+5.0',
                0.5, 75.0, 90.0, 'STOP_HUNT', 'Monday', 'AR_LOW',
                '[1,2]', 'unit test'
            )"""
        )
        conn.commit()
    finally:
        conn.close()

    watchlist = ScannerWatchlist(
        intelligence_db_path=db,
        validation_library=object(),
    )
    matches = watchlist._historical_matches(
        ScannerAlertCandidate(scanner=_candidate()),
        WatchlistConfig(require_alert_basket=True, historical_match_limit=1),
    )

    assert len(matches) == 1
    assert matches[0].normalized_key == "GBPJPY_BASKET_SETUP"
    assert matches[0].basket_rank == 1
    assert matches[0].basket_mode == "DEMO_ALERT"


def test_candidate_with_exact_promoted_record_is_entry_eligible() -> None:
    config = WatchlistConfig()
    alert = ScannerAlertCandidate(
        scanner=_candidate(),
        normalized_key="GBPJPY_VALIDATED_SETUP",
    )

    item = evaluate_candidate(
        alert,
        config,
        validation_records=[_record()],
        now=NOW,
    )

    assert item.status == "PROMOTED_ENTRY"
    assert item.validation_matches == 1
    assert item.blockers == []


def test_spread_blocks_candidate_even_when_promoted_record_exists() -> None:
    config = WatchlistConfig()
    alert = ScannerAlertCandidate(
        scanner=_candidate(spread_pips=9.0),
        normalized_key="GBPJPY_VALIDATED_SETUP",
    )

    item = evaluate_candidate(
        alert,
        config,
        validation_records=[_record()],
        now=NOW,
    )

    assert item.status == "BLOCKED"
    assert any("spread" in blocker for blocker in item.blockers)


def test_report_keeps_watch_only_separate_from_promoted_entries() -> None:
    config = WatchlistConfig()
    watch_only = evaluate_candidate(
        ScannerAlertCandidate(scanner=_candidate()),
        config,
        now=NOW,
    )
    promoted = evaluate_candidate(
        ScannerAlertCandidate(
            scanner=_candidate(id=2),
            normalized_key="GBPJPY_VALIDATED_SETUP",
        ),
        config,
        validation_records=[_record()],
        now=NOW,
    )

    report = format_watchlist_report([watch_only, promoted], config, generated_at=NOW)

    assert "Mode: alert-only; live execution disabled" in report
    assert "Promoted entries: 1 | Watch-only: 1" in report
    assert "PROMOTED ENTRY CANDIDATES" in report
    assert "WATCH ONLY" in report
