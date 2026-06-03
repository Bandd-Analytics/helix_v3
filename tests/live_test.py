"""Live integration test - connects to MT5 and runs full pipeline on EURUSD & GBPUSD.

Runs everything except actual order execution (dry-run mode).
"""

from __future__ import annotations

import asyncio
import sys
from datetime import datetime, timezone

import MetaTrader5 as mt5

from config.settings import settings
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.types import Direction
from helix_v3.consensus.validator import MMMConsensusValidator
from helix_v3.execution.gatekeeper import MT5ExecutionGatekeeper
from helix_v3.utils.logger import get_logger
from helix_v3.visualization.chart_exporter import MMMChartVisualizer

logger = get_logger("live_test")

SYMBOLS = list(settings.trading.symbols)
TIMEFRAMES = ["M15", "H1"]


def print_header(text: str) -> None:
    print(f"\n{'='*70}")
    print(f"  {text}")
    print(f"{'='*70}")


def test_mt5_connection(engine: MMMQuantitativeEngine) -> bool:
    print_header("STEP 1: MT5 CONNECTION")
    if not engine.connect():
        print("FAILED: Cannot connect to MT5 terminal")
        return False

    info = mt5.account_info()
    print(f"  Account:  {info.login}")
    print(f"  Server:   {info.server}")
    print(f"  Balance:  {info.balance:.2f} {info.currency}")
    print(f"  Equity:   {info.equity:.2f}")
    print(f"  Leverage: 1:{info.leverage}")
    print(f"  Trade OK: {info.trade_allowed}")

    terminal = mt5.terminal_info()
    print(f"  Terminal: {terminal.name}")
    print(f"  Connected:{terminal.connected}")
    return True


def test_data_fetch(engine: MMMQuantitativeEngine) -> bool:
    print_header("STEP 2: DATA INGESTION")
    for symbol in SYMBOLS:
        for tf in TIMEFRAMES:
            try:
                df = engine.fetch_rates(symbol, tf, count=200)
                latest = df.iloc[-1]
                print(
                    f"  {symbol} {tf:>3s}: {len(df)} bars | "
                    f"Last: O={latest['Open']:.5f} H={latest['High']:.5f} "
                    f"L={latest['Low']:.5f} C={latest['Close']:.5f} | "
                    f"Time: {df.index[-1]}"
                )
            except Exception as e:
                print(f"  {symbol} {tf}: FAILED - {e}")
                return False
    return True


def test_quant_signals(engine: MMMQuantitativeEngine) -> dict:
    print_header("STEP 3: QUANTITATIVE PRE-FILTER")
    signals = {}
    for symbol in SYMBOLS:
        for tf in TIMEFRAMES:
            sig = engine.generate_signal(symbol, tf)
            signals[(symbol, tf)] = sig

            print(f"\n  --- {symbol} {tf} ---")
            if sig.session_bounds:
                sb = sig.session_bounds
                print(f"  Asian Session:  H={sb.high:.5f}  L={sb.low:.5f}  Range={sb.range_pips:.1f} pips")
                print(f"  Vol Compression:{sb.volatility_compression:.4f}  Accumulation={sb.is_accumulation}")
            else:
                print("  Asian Session:  N/A")

            if sig.stop_hunt:
                sh = sig.stop_hunt
                print(f"  Stop Hunt:      Dir={sh.direction.value}  Breach={sh.breach_pips:.1f} pips  Z={sh.z_score:.2f}  Absorb={sh.is_absorption}")
            else:
                print("  Stop Hunt:      None detected")

            ev = sig.ema_vector
            print(f"  EMA Vectors:    5={ev.ema_5_angle:+.2f}  13={ev.ema_13_angle:+.2f}  50={ev.ema_50_angle:+.2f}  200={ev.ema_200_angle:+.2f}  800={ev.ema_800_angle:+.2f}")
            print(f"  Fast/Slow Div:  {ev.fast_slow_divergence:+.2f}  Trend={ev.trend_alignment.value}")
            print(f"  PRE-FILTER:     {'PASSED' if sig.pre_filter_passed else 'NOT PASSED'}")

    return signals


def test_chart_export(engine: MMMQuantitativeEngine, visualizer: MMMChartVisualizer) -> dict:
    print_header("STEP 4: CHART EXPORT (VISION MATRIX)")
    charts = {}
    for symbol in SYMBOLS:
        for tf in TIMEFRAMES:
            try:
                df = engine.fetch_rates(symbol, tf, count=200)
                b64, path = visualizer.export_vision_matrix(df, symbol, tf)
                charts[(symbol, tf)] = b64
                size_kb = len(b64) * 3 / 4 / 1024  # approx decoded size
                print(f"  {symbol} {tf}: Exported {path} ({size_kb:.0f} KB)")
            except Exception as e:
                print(f"  {symbol} {tf}: FAILED - {e}")
    return charts


async def test_consensus(charts: dict) -> dict:
    print_header("STEP 5: VISION CONSENSUS")

    validator = MMMConsensusValidator()
    print(f"  Mode: {validator.mode}")

    results = {}
    for (symbol, tf), b64 in charts.items():
        try:
            print(f"\n  Evaluating {symbol} {tf} ({validator.mode} mode)...")
            consensus = await validator.evaluate(b64, symbol, tf)
            results[(symbol, tf)] = consensus

            print(f"  Consensus:  {'AGREED' if consensus.agreed else 'DECLINED'}")
            print(f"  Direction:  {consensus.direction.value}")
            print(f"  Avg Conf:   {consensus.avg_confidence:.2f}")
            for v in consensus.verdicts:
                print(f"    {v.model_name}: dir={v.direction.value} conf={v.confidence:.2f} M/W={v.m_w_detected} RRT={v.rrt_detected} cycle={v.cycle_level}")
            if consensus.divergence_notes:
                print(f"  Divergence: {consensus.divergence_notes}")
        except Exception as e:
            print(f"  {symbol} {tf}: FAILED - {e}")

    return results


def test_risk_engine(gatekeeper: MT5ExecutionGatekeeper) -> None:
    print_header("STEP 6: RISK ENGINE STATUS")

    dd_ok = gatekeeper.check_drawdown_limit()
    pos_ok = gatekeeper.check_position_limit()
    print(f"  Drawdown check:  {'PASS' if dd_ok else 'BLOCKED (max DD reached)'}")
    print(f"  Position check:  {'PASS' if pos_ok else 'BLOCKED (max positions reached)'}")

    info = mt5.account_info()
    if info:
        balance = info.balance
        equity = info.equity
        dd_pct = ((balance - equity) / balance * 100) if balance > 0 else 0
        print(f"  Current DD:      {dd_pct:.2f}% (limit: {settings.risk.max_drawdown_pct * 100:.0f}%)")

    positions = mt5.positions_get()
    helix_count = sum(1 for p in (positions or []) if p.magic == 314159)
    total_count = len(positions or [])
    print(f"  Open positions:  {total_count} total, {helix_count} Helix")

    for symbol in SYMBOLS:
        try:
            sl_pips = 25.0  # test value
            lot = gatekeeper.calculate_lot_size(symbol, sl_pips)
            print(f"  Lot calc ({symbol}, 25 pip SL): {lot:.2f} lots")
        except Exception as e:
            print(f"  Lot calc ({symbol}): FAILED - {e}")


def test_spread_check(gatekeeper: MT5ExecutionGatekeeper) -> None:
    print_header("STEP 7: MARKET CONDITIONS")
    for symbol in SYMBOLS:
        tick = mt5.symbol_info_tick(symbol)
        info = mt5.symbol_info(symbol)
        if tick and info:
            pip_size = info.point * (10 if info.digits in (3, 5) else 1)
            spread_pips = (tick.ask - tick.bid) / pip_size
            print(
                f"  {symbol}: Bid={tick.bid:.5f} Ask={tick.ask:.5f} "
                f"Spread={spread_pips:.1f} pips | "
                f"{'TRADEABLE' if spread_pips < 5 else 'WIDE SPREAD'}"
            )


async def main() -> None:
    print("\n" + "=" * 70)
    print("  HELIX V3 - LIVE INTEGRATION TEST")
    print(f"  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 70)

    engine = MMMQuantitativeEngine()
    visualizer = MMMChartVisualizer()
    gatekeeper = MT5ExecutionGatekeeper()

    try:
        # 1. Connect
        if not test_mt5_connection(engine):
            sys.exit(1)

        # 2. Data
        if not test_data_fetch(engine):
            sys.exit(1)

        # 3. Quant signals
        signals = test_quant_signals(engine)

        # 4. Charts
        charts = test_chart_export(engine, visualizer)

        # 5. Vision consensus (if API keys present)
        consensus_results = await test_consensus(charts)

        # 6. Risk engine
        test_risk_engine(gatekeeper)

        # 7. Market conditions
        test_spread_check(gatekeeper)

        # Summary
        print_header("SUMMARY")
        passed_filters = [(k, v) for k, v in signals.items() if v.pre_filter_passed]
        print(f"  Symbols tested:    {len(SYMBOLS)}")
        print(f"  Timeframes tested: {len(TIMEFRAMES)}")
        print(f"  Charts exported:   {len(charts)}")
        print(f"  Pre-filter passed: {len(passed_filters)}/{len(signals)}")
        print(f"  Consensus results: {len(consensus_results)}")

        if passed_filters:
            print("\n  Signals that passed pre-filter:")
            for (sym, tf), sig in passed_filters:
                print(f"    {sym} {tf}: hunt={sig.stop_hunt.direction.value if sig.stop_hunt else 'N/A'} trend={sig.ema_vector.trend_alignment.value}")

        print(f"\n  STATUS: LIVE TEST COMPLETE")
        print(f"  NOTE: No trades were executed (dry-run mode)")

    finally:
        engine.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
