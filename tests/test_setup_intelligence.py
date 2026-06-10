from helix_v3.backtest.setup_intelligence import (
    SCHEMA,
    _chronological_slices,
    _payoff_ratio,
    _profit_factor,
    expectancy_candidate_tier,
    format_alert_only_basket_report,
    rrs_grade,
)


def test_rrs_grade_boundaries() -> None:
    assert rrs_grade(90.0) == "R_RUNNER"
    assert rrs_grade(75.0) == "R_RUNNER"
    assert rrs_grade(74.99) == "R_REPEATER"
    assert rrs_grade(50.0) == "R_REPEATER"
    assert rrs_grade(49.99) == "S_STRANGER"


def test_expectancy_candidate_tier_promotes_repeaters_by_expectancy() -> None:
    tier = expectancy_candidate_tier(
        total=30,
        rrs="R_REPEATER",
        favorable_rate=56.0,
        avg_exit_pips=8.0,
        profit_factor=1.35,
        payoff_ratio=1.4,
        split_passes=2,
    )

    assert tier == "DEMO_CANDIDATE"


def test_expectancy_candidate_tier_keeps_strangers_as_exceptions() -> None:
    tier = expectancy_candidate_tier(
        total=40,
        rrs="S_STRANGER",
        favorable_rate=38.0,
        avg_exit_pips=24.0,
        profit_factor=1.8,
        payoff_ratio=3.2,
        split_passes=2,
    )

    assert tier == "ASYMMETRIC_EXCEPTION"


def test_expectancy_candidate_tier_rejects_negative_expectancy() -> None:
    tier = expectancy_candidate_tier(
        total=100,
        rrs="R_RUNNER",
        favorable_rate=80.0,
        avg_exit_pips=-1.0,
        profit_factor=0.95,
        payoff_ratio=1.2,
        split_passes=3,
    )

    assert tier == "REJECT_EXPECTANCY"


def test_profit_factor_and_payoff_ratio_handle_no_losses() -> None:
    assert _profit_factor(50.0, 0.0) == 999.0
    assert _profit_factor(0.0, 0.0) == 0.0
    assert _payoff_ratio(20.0, None) == 999.0


def test_chronological_slices_preserve_order_and_balance() -> None:
    slices = _chronological_slices([1.0, 2.0, 3.0, 4.0, 5.0], parts=3)

    assert slices == [[1.0, 2.0], [3.0, 4.0], [5.0]]


def test_alert_only_basket_report_ranks_rrs_expectancy_and_blocks_analysis_only(tmp_path) -> None:
    import sqlite3

    db_path = tmp_path / "setup_intelligence.db"
    conn = sqlite3.connect(str(db_path))
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
                'GBPJPY', 'BUY', 'THE_33_MW|BUY|EARLY_WEEK|L3', 'THE_33_MW', 'GBP',
                'R_REPEATER', 'DEMO_CANDIDATE', 30, 18, 60.0, 40.0,
                20.0, 30.0, 12.5, 25.0, -8.0, 450.0, 96.0, 4.69,
                3.13, 40.0, 10.0, 2, 'train:N=10,Avg=+5.0',
                1.2, 70.0, 88.0, 'STOP_HUNT', 'Tuesday', 'ROUND_00',
                '[1,2]', 'unit test'
            )"""
        )
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
                'XAUUSD', 'BUY', 'RRT_REVERSAL|BUY|MID_WEEK|L3', 'RRT_REVERSAL', 'USD',
                'R_RUNNER', 'DEMO_CANDIDATE', 12, 10, 83.3, 50.0,
                20.0, 30.0, 100.0, 150.0, -25.0, 1500.0, 50.0, 30.0,
                6.0, 200.0, 30.0, 2, 'train:N=4,Avg=+5.0',
                0.8, 80.0, 92.0, 'ACCUMULATION', 'Wednesday', 'ADR_HIGH',
                '[3,4]', 'unit test'
            )"""
        )
        conn.commit()

        report = format_alert_only_basket_report(conn, limit=10)
    finally:
        conn.close()

    assert "Alert-Only Demo Basket" in report
    assert "DEMO_ALERT" in report
    assert "RESEARCH_ONLY" in report
    assert "R_REPEATER" in report
    assert "R_RUNNER" in report
