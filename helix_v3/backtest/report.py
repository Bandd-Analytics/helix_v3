"""Backtest reporting — metrics, per-pair breakdown, and equity curve."""

from __future__ import annotations

import math
from collections import defaultdict
from datetime import datetime
from statistics import NormalDist
from typing import List

import numpy as np

from helix_v3.backtest.engine import TradeSimulator, SimulatedTrade

# Assumed number of strategy configurations tried during research/calibration.
# The Deflated Sharpe Ratio corrects for selection across trials; with ~450
# tunable parameters this default is, if anything, generous to the strategy.
DEFAULT_N_TRIALS = 50


def compute_metrics(trades: List[SimulatedTrade]) -> dict:
    """Compute strategy-level metrics from closed trades."""
    if not trades:
        return {
            "total_trades": 0, "win_rate": 0, "avg_win": 0, "avg_loss": 0,
            "profit_factor": 0, "expectancy": 0, "sharpe": 0, "max_dd": 0,
        }

    wins = [t for t in trades if t.pnl_pips > 0]
    losses = [t for t in trades if t.pnl_pips <= 0]

    total = len(trades)
    win_rate = len(wins) / total * 100 if total else 0
    avg_win = np.mean([t.pnl_pips for t in wins]) if wins else 0
    avg_loss = np.mean([abs(t.pnl_pips) for t in losses]) if losses else 0

    gross_profit = sum(t.pnl_dollars for t in wins)
    gross_loss = abs(sum(t.pnl_dollars for t in losses))
    profit_factor = gross_profit / gross_loss if gross_loss > 0 else float("inf")

    all_pnl = [t.pnl_pips for t in trades]
    expectancy = np.mean(all_pnl)

    # NOTE: no "Sharpe" here. The old per-trade-pips x sqrt(252) formula
    # treated every trade as a daily return and mixed pips across pairs —
    # a 0.28-sigma per-trade edge mechanically printed "4.37". The real
    # Sharpe comes from equity_curve_metrics() on daily MTM dollar returns.

    # Max drawdown from realized dollar P&L sequence (per-group fallback;
    # the MTM curve drawdown in equity_curve_metrics is authoritative)
    cumulative = np.cumsum([t.pnl_dollars for t in trades])
    peak = np.maximum.accumulate(cumulative)
    drawdowns = peak - cumulative
    max_dd_dollars = float(np.max(drawdowns)) if len(drawdowns) > 0 else 0

    return {
        "total_trades": total,
        "wins": len(wins),
        "losses": len(losses),
        "win_rate": win_rate,
        "avg_win": float(avg_win),
        "avg_loss": float(avg_loss),
        "profit_factor": profit_factor,
        "expectancy": float(expectancy),
        "max_dd_dollars": max_dd_dollars,
        "gross_profit": gross_profit,
        "gross_loss": gross_loss,
        "net_pnl": gross_profit - gross_loss,
        "avg_mfe": float(np.mean([t.max_favorable_pips for t in trades])),
        "avg_mae": float(np.mean([t.max_adverse_pips for t in trades])),
    }


def equity_curve_metrics(equity_curve: List[tuple]) -> dict:
    """Daily dollar-return Sharpe, return-moment shape, and MTM drawdown.

    The curve is (timestamp, mark-to-market equity) snapshots. Daily returns
    use the last snapshot of each UTC day; drawdown uses every snapshot so
    intraday floating excursions count.
    """
    empty = {
        "daily_sharpe": 0.0, "n_days": 0, "skew": 0.0, "kurtosis": 3.0,
        "max_dd_pct": 0.0, "max_dd_dollars": 0.0, "sharpe_daily_raw": 0.0,
    }
    if not equity_curve or len(equity_curve) < 2:
        return empty

    eq = np.array([e for _, e in equity_curve], dtype=float)
    peak = np.maximum.accumulate(eq)
    dd = peak - eq
    with np.errstate(divide="ignore", invalid="ignore"):
        dd_pct = np.where(peak > 0, dd / peak, 0.0)
    max_dd_dollars = float(dd.max())
    max_dd_pct = float(dd_pct.max()) * 100.0

    # Last MTM equity of each UTC day -> daily returns
    daily: dict = {}
    for ts, e in equity_curve:
        daily[ts.date()] = e
    vals = np.array(list(daily.values()), dtype=float)
    if len(vals) < 3 or np.any(vals[:-1] <= 0):
        return {**empty, "max_dd_pct": max_dd_pct, "max_dd_dollars": max_dd_dollars}

    rets = np.diff(vals) / vals[:-1]
    std = rets.std(ddof=1)
    sr_daily = float(rets.mean() / std) if std > 0 else 0.0

    mu = rets.mean()
    m2 = ((rets - mu) ** 2).mean()
    if m2 > 0:
        skew = float(((rets - mu) ** 3).mean() / m2 ** 1.5)
        kurt = float(((rets - mu) ** 4).mean() / m2 ** 2)
    else:
        skew, kurt = 0.0, 3.0

    return {
        "daily_sharpe": sr_daily * math.sqrt(252),
        "sharpe_daily_raw": sr_daily,
        "n_days": len(rets),
        "skew": skew,
        "kurtosis": kurt,
        "max_dd_pct": max_dd_pct,
        "max_dd_dollars": max_dd_dollars,
    }


def deflated_sharpe_probability(
    sharpe_daily: float,
    n_obs: int,
    skew: float = 0.0,
    kurtosis: float = 3.0,
    n_trials: int = DEFAULT_N_TRIALS,
) -> float:
    """Deflated Sharpe Ratio (Bailey & Lopez de Prado, 2014).

    Probability that the observed (non-annualized, daily) Sharpe exceeds the
    expected MAXIMUM Sharpe of `n_trials` skill-less strategies — i.e. the
    chance this result is not just selection bias. The variance of trial
    Sharpes is approximated by the SR estimator variance (the trial SRs
    themselves were not recorded during calibration).
    """
    if n_obs < 3:
        return 0.0
    nd = NormalDist()
    euler_gamma = 0.5772156649015329

    sr_var = (1 - skew * sharpe_daily + (kurtosis - 1) / 4 * sharpe_daily**2) / (n_obs - 1)
    sr_std = math.sqrt(max(sr_var, 1e-12))
    n_trials = max(int(n_trials), 2)
    z1 = nd.inv_cdf(1 - 1 / n_trials)
    z2 = nd.inv_cdf(1 - 1 / (n_trials * math.e))
    sr0 = sr_std * ((1 - euler_gamma) * z1 + euler_gamma * z2)

    denom = math.sqrt(max(1 - skew * sharpe_daily + (kurtosis - 1) / 4 * sharpe_daily**2, 1e-12))
    z = (sharpe_daily - sr0) * math.sqrt(n_obs - 1) / denom
    return nd.cdf(z)


def per_pair_breakdown(trades: List[SimulatedTrade]) -> dict:
    """Group metrics by symbol."""
    by_pair: dict = defaultdict(list)
    for t in trades:
        by_pair[t.symbol].append(t)
    return {sym: compute_metrics(pair_trades) for sym, pair_trades in sorted(by_pair.items())}


def grade_breakdown(trades: List[SimulatedTrade]) -> dict:
    """Group metrics by advisory grade."""
    by_grade: dict = defaultdict(list)
    for t in trades:
        grade = t.advisory_grade or "UNGRADED"
        by_grade[grade].append(t)
    return {g: compute_metrics(gt) for g, gt in sorted(by_grade.items())}


def exit_reason_breakdown(trades: List[SimulatedTrade]) -> dict:
    """Count trades by exit reason."""
    counts: dict = defaultdict(int)
    for t in trades:
        counts[t.exit_reason] += 1
    return dict(sorted(counts.items(), key=lambda x: -x[1]))


def monthly_pnl(trades: List[SimulatedTrade]) -> dict:
    """Monthly P&L breakdown."""
    by_month: dict = defaultdict(float)
    for t in trades:
        if t.exit_time:
            key = t.exit_time.strftime("%Y-%m")
            by_month[key] += t.pnl_dollars
    return dict(sorted(by_month.items()))


def print_backtest_report(
    simulator: TradeSimulator,
    start: datetime,
    end: datetime,
) -> None:
    """Print a complete backtest report to stdout."""
    trades = simulator.closed_trades
    metrics = compute_metrics(trades)

    print()
    print("=" * 80)
    print("  HELIX V3 BACKTEST REPORT")
    print(f"  Period: {start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}")
    print("=" * 80)

    if not trades:
        print("\n  No trades generated during backtest period.")
        print("=" * 80)
        return

    curve = equity_curve_metrics(simulator.equity_curve)
    dsr = deflated_sharpe_probability(
        curve["sharpe_daily_raw"], curve["n_days"],
        curve["skew"], curve["kurtosis"],
    )

    # Overall metrics
    print(f"""
  OVERALL METRICS
  {'-' * 40}
  Total Trades:    {metrics['total_trades']}
  Win Rate:        {metrics['win_rate']:.1f}% ({metrics['wins']}W / {metrics['losses']}L)
  Avg Win:         {metrics['avg_win']:+.1f} pips
  Avg Loss:        {metrics['avg_loss']:.1f} pips
  Profit Factor:   {metrics['profit_factor']:.2f}
  Expectancy:      {metrics['expectancy']:+.1f} pips/trade
  Sharpe (daily $ returns, annualized): {curve['daily_sharpe']:.2f}  (n={curve['n_days']} days)
  Deflated Sharpe prob.: {dsr:.2f}  (vs max of {DEFAULT_N_TRIALS} assumed trials; >0.95 = likely real)
  Net P&L:         ${metrics['net_pnl']:+.2f}
  Max Drawdown:    {curve['max_dd_pct']:.1f}% (${curve['max_dd_dollars']:.2f}, mark-to-market)
  Avg MFE:         {metrics['avg_mfe']:.1f} pips
  Avg MAE:         {metrics['avg_mae']:.1f} pips
  Final Equity:    ${simulator.equity:.2f}
""")

    # Exit reasons
    exits = exit_reason_breakdown(trades)
    print(f"  EXIT REASONS")
    print(f"  {'-' * 40}")
    for reason, count in exits.items():
        pct = count / len(trades) * 100
        print(f"  {reason:<20} {count:>4} ({pct:>5.1f}%)")

    # Advisory grade breakdown
    grade_data = grade_breakdown(trades)
    if grade_data:
        print(f"\n  ADVISORY GRADE BREAKDOWN")
        print(f"  {'--' * 36}")
        print(f"  {'Grade':<10} {'Trades':>6} {'Win%':>6} {'AvgW':>7} {'AvgL':>7} "
              f"{'PF':>6} {'Exp':>7} {'Net$':>8}")
        print(f"  {'--' * 36}")
        for g, m in grade_data.items():
            print(
                f"  {g:<10} {m['total_trades']:>6} {m['win_rate']:>5.1f}% "
                f"{m['avg_win']:>+6.1f} {m['avg_loss']:>6.1f} "
                f"{m['profit_factor']:>5.2f} {m['expectancy']:>+6.1f} "
                f"${m['net_pnl']:>+7.2f}"
            )

    # Per-pair breakdown
    pair_data = per_pair_breakdown(trades)
    if pair_data:
        print(f"\n  PER-PAIR BREAKDOWN")
        print(f"  {'-' * 72}")
        print(f"  {'Pair':<10} {'Trades':>6} {'Win%':>6} {'AvgW':>7} {'AvgL':>7} "
              f"{'PF':>6} {'Exp':>7} {'Net$':>8}")
        print(f"  {'-' * 72}")
        for sym, m in pair_data.items():
            print(
                f"  {sym:<10} {m['total_trades']:>6} {m['win_rate']:>5.1f}% "
                f"{m['avg_win']:>+6.1f} {m['avg_loss']:>6.1f} "
                f"{m['profit_factor']:>5.2f} {m['expectancy']:>+6.1f} "
                f"${m['net_pnl']:>+7.2f}"
            )

    # Monthly P&L
    months = monthly_pnl(trades)
    if months:
        print(f"\n  MONTHLY P&L")
        print(f"  {'-' * 30}")
        for month, pnl in months.items():
            bar = "+" * max(0, int(pnl / 5)) if pnl > 0 else "-" * max(0, int(abs(pnl) / 5))
            print(f"  {month}  ${pnl:>+8.2f}  {bar}")

    # Equity curve summary
    if simulator.equity_curve:
        equities = [e for _, e in simulator.equity_curve]
        print(f"\n  EQUITY CURVE")
        print(f"  {'-' * 30}")
        print(f"  Start:    ${equities[0]:.2f}")
        print(f"  End:      ${equities[-1]:.2f}")
        print(f"  Peak:     ${max(equities):.2f}")
        print(f"  Trough:   ${min(equities):.2f}")

    print()
    print("=" * 80)
