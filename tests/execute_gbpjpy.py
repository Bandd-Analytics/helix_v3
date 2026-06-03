"""Live execution test - GBPJPY M15 SELL via full Helix pipeline."""

from __future__ import annotations

import asyncio
from datetime import datetime, timezone

import MetaTrader5 as mt5

from config.settings import settings
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.types import Direction
from helix_v3.consensus.validator import MMMConsensusValidator
from helix_v3.execution.gatekeeper import MT5ExecutionGatekeeper
from helix_v3.utils.logger import get_logger
from helix_v3.visualization.chart_exporter import MMMChartVisualizer

logger = get_logger("execute_gbpjpy")

SYMBOL = "GBPJPY"
TIMEFRAME = "M15"


async def main() -> None:
    print(f"\n{'='*60}")
    print(f"  HELIX V3 - LIVE EXECUTION: {SYMBOL} {TIMEFRAME} SELL")
    print(f"  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"{'='*60}\n")

    engine = MMMQuantitativeEngine()
    visualizer = MMMChartVisualizer()
    validator = MMMConsensusValidator()
    gatekeeper = MT5ExecutionGatekeeper()

    try:
        # 1. Connect
        if not engine.connect():
            print("FATAL: Cannot connect to MT5")
            return

        info = mt5.account_info()
        print(f"  Account:  {info.login} ({info.server})")
        print(f"  Balance:  {info.balance:.2f} {info.currency}")
        print(f"  Equity:   {info.equity:.2f}")

        # 2. Pre-flight checks
        print(f"\n--- PRE-FLIGHT CHECKS ---")

        if not gatekeeper.check_drawdown_limit():
            print("  BLOCKED: Max drawdown reached")
            return
        print(f"  Drawdown:  PASS")

        if not gatekeeper.check_position_limit():
            print("  BLOCKED: Max positions reached")
            return
        print(f"  Positions: PASS")

        tick = mt5.symbol_info_tick(SYMBOL)
        sym_info = mt5.symbol_info(SYMBOL)
        pip_size = sym_info.point * (10 if sym_info.digits in (3, 5) else 1)
        spread_pips = (tick.ask - tick.bid) / pip_size
        print(f"  Spread:    {spread_pips:.1f} pips ({'PASS' if spread_pips < 5 else 'WIDE'})")

        if spread_pips >= 5:
            print("  BLOCKED: Spread too wide")
            return

        # 3. Generate quant signal
        print(f"\n--- QUANT SIGNAL ---")
        signal = engine.generate_signal(SYMBOL, TIMEFRAME)

        if signal.session_bounds:
            sb = signal.session_bounds
            print(f"  Asian H/L: {sb.high:.3f} / {sb.low:.3f} ({sb.range_pips:.1f} pips)")
        if signal.stop_hunt:
            sh = signal.stop_hunt
            print(f"  Stop Hunt: {sh.direction.value} breach={sh.breach_pips:.1f} pips z={sh.z_score:.2f}")
        print(f"  EMA Trend: {signal.ema_vector.trend_alignment.value}")

        # 4. Vision consensus
        print(f"\n--- VISION CONSENSUS ---")
        df = engine.fetch_rates(SYMBOL, TIMEFRAME, count=200)
        image_b64, chart_path = visualizer.export_vision_matrix(df, SYMBOL, TIMEFRAME)
        consensus = await validator.evaluate(image_b64, SYMBOL, TIMEFRAME)

        print(f"  Mode:      {validator.mode}")
        print(f"  Direction: {consensus.direction.value}")
        print(f"  Confidence:{consensus.avg_confidence:.2f}")
        print(f"  Agreed:    {consensus.agreed}")

        if not consensus.agreed:
            print(f"  BLOCKED: No consensus - {consensus.divergence_notes}")
            return

        if consensus.direction != Direction.SELL:
            print(f"  BLOCKED: Expected SELL, got {consensus.direction.value}")
            return

        # 5. Build order
        print(f"\n--- ORDER CONSTRUCTION ---")
        order = gatekeeper.build_order(SYMBOL, signal, consensus)

        if order is None:
            print("  BLOCKED: Order construction failed (risk/spread check)")
            return

        print(f"  Direction: {order.direction.value}")
        print(f"  Lot Size:  {order.lot_size}")
        print(f"  Entry:     {order.entry_price:.3f}")
        print(f"  Stop Loss: {order.stop_loss:.3f} ({order.sl_pips:.1f} pips)")
        print(f"  TP1 (1:1): {order.take_profit_1:.3f}")
        print(f"  TP2 (2.5): {order.take_profit_2:.3f}")
        print(f"  Risk/Rew:  {order.risk_reward:.1f}")

        # 6. Execute
        print(f"\n--- EXECUTING ORDER ---")
        ticket = gatekeeper.execute_order(order)

        if ticket:
            print(f"\n  *** ORDER FILLED ***")
            print(f"  Ticket:    {ticket}")
            print(f"  Symbol:    {SYMBOL}")
            print(f"  Direction: SELL")
            print(f"  Lots:      {order.lot_size}")
            print(f"  SL:        {order.stop_loss:.3f}")
            print(f"  TP:        {order.take_profit_2:.3f}")

            # Verify position exists
            pos = mt5.positions_get(ticket=ticket)
            if pos:
                p = pos[0]
                print(f"\n  --- POSITION CONFIRMED ---")
                print(f"  Open Price:{p.price_open:.3f}")
                print(f"  Current:   {p.price_current:.3f}")
                print(f"  Profit:    {p.profit:.2f} {info.currency}")
                print(f"  Swap:      {p.swap:.2f}")
            else:
                print(f"  Position verification: checking by symbol...")
                all_pos = mt5.positions_get(symbol=SYMBOL)
                if all_pos:
                    for p in all_pos:
                        if p.magic == 314159:
                            print(f"  Found: ticket={p.ticket} lots={p.volume} open={p.price_open:.3f}")
        else:
            print(f"\n  ORDER REJECTED")
            print(f"  Status: {order.status}")

    finally:
        engine.disconnect()
        print(f"\n{'='*60}")
        print(f"  EXECUTION TEST COMPLETE")
        print(f"{'='*60}")


if __name__ == "__main__":
    asyncio.run(main())
