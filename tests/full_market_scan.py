"""Full 13-pair market scan with all V2-verified indicators.

Generates:
  1. Annotated flashcard chart per pair (with TDI, patterns, pivots, HUD)
  2. Trade opportunity table (ranked by confluence)
  3. WhatsApp notification with top setups
  4. Detailed technical breakdown per pair
"""

from __future__ import annotations

import asyncio
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

import MetaTrader5 as mt5

from config.settings import settings
from config.pair_profiles import get_pair_profile
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.mtf_analyzer import MTFAnalyzer
from helix_v3.core.tdi import (
    compute_tdi, compute_pivots, compute_adr, compute_adr_marker,
    compute_hud, compute_crossover_arrows, compute_daily_hilo,
)
from helix_v3.core.patterns import scan_patterns
from helix_v3.visualization.annotated_chart import AnnotatedChartGenerator
from helix_v3.notifications.whatsapp import WhatsAppNotifier
from helix_v3.utils.logger import get_logger

logger = get_logger("full_scan")
EAT = timezone(timedelta(hours=3))
SYMBOLS = list(settings.trading.symbols)


def run_full_scan():
    now_eat = datetime.now(EAT)
    print(f"\n{'='*100}")
    print(f"  HELIX V3 FULL MARKET SCAN | {now_eat.strftime('%Y-%m-%d %H:%M EAT')} | {len(SYMBOLS)} pairs")
    print(f"{'='*100}\n")

    engine = MMMQuantitativeEngine()
    if not engine.connect():
        print("FATAL: MT5 connection failed")
        return

    info = mt5.account_info()
    print(f"  Account: {info.login} | Balance: ${info.balance:.2f} | Equity: ${info.equity:.2f}\n")

    mtf = MTFAnalyzer(engine)
    annotator = AnnotatedChartGenerator()
    notifier = WhatsAppNotifier()

    results = []
    charts = {}

    for symbol in SYMBOLS:
        try:
            t0 = time.monotonic()
            pp = get_pair_profile(symbol)
            pip_size = 0.01 if "JPY" in symbol else 0.0001
            if symbol == "XAUUSD":
                pip_size = 0.1

            # MTF Analysis
            analysis = mtf.analyze(symbol)

            # Data
            df_m15 = engine.fetch_rates(symbol, "M15", count=200)
            df_d1 = engine.fetch_rates(symbol, "D1", count=140)

            # TDI (V2-verified)
            tdi = compute_tdi(df_m15)

            # Pivots (V2-verified with day-type)
            prev_d = df_d1.iloc[-2]
            prev_bullish = prev_d["Close"] > prev_d["Open"]
            pivots = compute_pivots(prev_d["High"], prev_d["Low"], prev_d["Close"], prev_bullish)

            # ADR Marker (Wilder ATR)
            adr_m = compute_adr_marker(df_d1, pip_size)
            adr_val = compute_adr(df_d1)

            # Full HUD
            hud = compute_hud(df_d1, pip_size)

            # Crossover arrows
            xo = compute_crossover_arrows(df_m15)

            # Daily HiLo
            hilo = compute_daily_hilo(df_d1)

            # Pattern scan
            patterns = scan_patterns(
                df_m15.iloc[-50:], pip_size,
                prev_hod=hilo["phod"], prev_lod=hilo["plod"],
                asian_high=analysis.fifteen_min.asian_range_high,
                asian_low=analysis.fifteen_min.asian_range_low,
            )

            # Generate annotated chart
            _, chart_path = annotator.generate_from_mtf(
                df_m15, symbol, "M15", analysis,
                tdi_result=tdi, pattern_scan=patterns, pivots=pivots,
                adr=adr_val, prev_hod=hilo["phod"], prev_lod=hilo["plod"],
            )

            elapsed = time.monotonic() - t0

            # Collect result
            tick = mt5.symbol_info_tick(symbol)
            sym_info = mt5.symbol_info(symbol)
            spread_pips = 0
            if tick and sym_info:
                ps = sym_info.point * (10 if sym_info.digits in (3, 5) else 1)
                spread_pips = (tick.ask - tick.bid) / ps

            entry = {
                "symbol": symbol,
                "tier": pp.risk_tier,
                "risk_pct": pp.max_risk_pct,
                "weekly_trend": analysis.weekly.trend_direction.value,
                "weekly_phase": analysis.weekly.week_phase.value,
                "weekly_cycle": analysis.weekly.cycle_position.value,
                "days_from_peak": analysis.weekly.days_since_peak,
                "h4_level": analysis.four_hour.level_count,
                "h4_trend": analysis.four_hour.trend_direction.value,
                "h4_choppy": analysis.four_hour.is_choppy,
                "h1_session": analysis.one_hour.session_phase.value,
                "h1_trend": analysis.one_hour.trend_direction.value,
                "h1_hod": analysis.one_hour.hod,
                "h1_lod": analysis.one_hour.lod,
                "h1_hod_locked": analysis.one_hour.hod_locked,
                "h1_lod_locked": analysis.one_hour.lod_locked,
                "h1_50_200_cross": analysis.one_hour.ema_50_200_cross,
                "m15_asian_pips": analysis.fifteen_min.asian_range_pips,
                "m15_accum": analysis.fifteen_min.accumulation_valid,
                "m15_hunt": analysis.fifteen_min.stop_hunt_detected,
                "m15_hunt_dir": analysis.fifteen_min.stop_hunt_direction.value,
                "m15_hunt_pips": analysis.fifteen_min.stop_hunt_pips,
                "m15_pushes": analysis.fifteen_min.push_count,
                "m15_mw": analysis.fifteen_min.m_w_forming,
                "m15_rrt": analysis.fifteen_min.rrt_detected,
                "confluence": analysis.confluence_score,
                "trade_valid": analysis.trade_valid,
                "trade_dir": analysis.trade_direction.value,
                "rejections": analysis.rejection_reasons,
                # TDI
                "tdi_rsi": tdi.rsi,
                "tdi_signal": tdi.signal,
                "tdi_base": tdi.base,
                "tdi_signals": [s.value for s in tdi.signals],
                "tdi_shark": tdi.shark_fin_active,
                "tdi_shark_dir": tdi.shark_fin_direction,
                "tdi_squeeze": tdi.vb_squeeze,
                "tdi_divergence": tdi.divergence,
                "tdi_crossed": tdi.rsi_crossed_signal,
                # Patterns
                "patterns_count": len(patterns.patterns),
                "trade_type": patterns.trade_type.value,
                "rrt_count": patterns.rrt_count,
                "spike_count": patterns.spike_count,
                "pin_bar_count": patterns.pin_bar_count,
                "pat_mw": patterns.m_w_detected,
                "half_batman": patterns.half_batman,
                # Pivots
                "pivot_pp": pivots["PP"],
                "pivot_day_type": pivots["day_type"],
                # HUD
                "hud_tdr": hud["TDR"],
                "hud_ydr": hud["YDR"],
                "hud_wadr": hud["WADR"],
                "hud_madr": hud["MADR"],
                "hud_hyadr": hud["HYADR"],
                "hud_wr": hud["WR"],
                "hud_3xadr": hud["3xADR"],
                # ADR
                "adr_pips": adr_m["adr_pips"],
                "adr_high": adr_m["marker_high"],
                "adr_low": adr_m["marker_low"],
                # Crossovers
                "xo_short": xo["short_cross"],
                "xo_long": xo["long_cross"],
                # Spread
                "spread": spread_pips,
                # Chart
                "chart_path": str(chart_path),
                "scan_time": elapsed,
            }
            results.append(entry)
            charts[symbol] = chart_path

        except Exception as e:
            print(f"  ERROR {symbol}: {e}")
            import traceback
            traceback.print_exc()

    # ================================================================
    # TRADE OPPORTUNITY TABLE (ranked by confluence)
    # ================================================================
    results.sort(key=lambda x: x["confluence"], reverse=True)

    print(f"\n{'='*100}")
    print(f"  TRADE OPPORTUNITIES — Ranked by Confluence Score")
    print(f"{'='*100}\n")

    print(f"  {'#':<3} {'Pair':<8} {'Confl':<6} {'Dir':<8} {'Weekly':<20} {'H4':<14} "
          f"{'Session':<16} {'TDI':<20} {'Setup':<14} {'Action':<10}")
    print(f"  {'-'*115}")

    watchlist = []
    for i, r in enumerate(results):
        # Determine action recommendation
        action = "WAIT"
        if r["trade_valid"]:
            action = "ENTRY"
        elif r["confluence"] >= 40:
            action = "WATCH"
        elif r["confluence"] >= 30:
            action = "MONITOR"

        tdi_summary = []
        for s in r["tdi_signals"]:
            if s != "NONE":
                tdi_summary.append(s.replace("_", " ")[:18])
        tdi_str = "; ".join(tdi_summary) if tdi_summary else f"RSI {r['tdi_rsi']:.0f}"

        print(f"  {i+1:<3} {r['symbol']:<8} {r['confluence']:<6} {r['trade_dir']:<8} "
              f"{r['weekly_phase']:<10} {r['weekly_trend']:<8} "
              f"L{r['h4_level']} {r['h4_trend']:<8} "
              f"{r['h1_session']:<16} "
              f"{tdi_str:<20} "
              f"{r['trade_type']:<14} "
              f"{action:<10}")

        if r["rejections"]:
            for rej in r["rejections"][:2]:
                print(f"  {'':>3} {'':>8} {'':>6} {'':>8} {'':>20}   WARN: {rej}")

        if action in ("ENTRY", "WATCH"):
            watchlist.append(r)

    # ================================================================
    # DETAILED TECHNICALS FOR TOP PAIRS
    # ================================================================
    print(f"\n{'='*100}")
    print(f"  DETAILED TECHNICAL BREAKDOWN — Top {min(5, len(results))} Pairs")
    print(f"{'='*100}")

    for r in results[:5]:
        sym = r["symbol"]
        print(f"\n  {'─'*90}")
        print(f"  {sym} | Confluence: {r['confluence']}/100 | Action: {'ENTRY' if r['trade_valid'] else 'WATCH' if r['confluence']>=40 else 'MONITOR'}")
        print(f"  {'─'*90}")

        print(f"\n  WEEKLY STRUCTURE:")
        print(f"    Phase: {r['weekly_phase']} | Trend: {r['weekly_trend']} | Cycle: {r['weekly_cycle']}")
        print(f"    Days from peak: {r['days_from_peak']}")

        print(f"\n  4-HOUR CONTEXT:")
        print(f"    Level: L{r['h4_level']} | Trend: {r['h4_trend']} | Choppy: {r['h4_choppy']}")

        print(f"\n  1-HOUR INTRADAY:")
        print(f"    Session: {r['h1_session']} | Trend: {r['h1_trend']}")
        print(f"    HOD: {r['h1_hod']:.5f} (locked={r['h1_hod_locked']}) | LOD: {r['h1_lod']:.5f} (locked={r['h1_lod_locked']})")
        print(f"    50/200 cross: {r['h1_50_200_cross']}")

        print(f"\n  15-MIN ENTRY:")
        print(f"    Asian Range: {r['m15_asian_pips']:.0f} pips (valid={r['m15_accum']})")
        print(f"    Stop Hunt: {'YES' if r['m15_hunt'] else 'no'} dir={r['m15_hunt_dir']} {r['m15_hunt_pips']:.1f}p")
        print(f"    Pushes: {r['m15_pushes']}/3 | M/W: {r['m15_mw']} | RRT: {r['m15_rrt']}")

        print(f"\n  TDI (V2-Verified RSI=21):")
        print(f"    RSI PL: {r['tdi_rsi']:.1f} | Signal: {r['tdi_signal']:.1f} | Base: {r['tdi_base']:.1f}")
        print(f"    Signals: {', '.join(r['tdi_signals'])}")
        print(f"    Shark Fin: {r['tdi_shark']} ({r['tdi_shark_dir']}) | Squeeze: {r['tdi_squeeze']}")
        print(f"    Divergence: {r['tdi_divergence']} | Cross: {r['tdi_crossed']}")

        print(f"\n  PATTERNS:")
        print(f"    Trade Type: {r['trade_type']} | Total: {r['patterns_count']}")
        print(f"    RRT: {r['rrt_count']} | Spikes: {r['spike_count']} | Pin Bars: {r['pin_bar_count']}")
        print(f"    M/W: {r['pat_mw']} | Half Batman: {r['half_batman']}")

        print(f"\n  PIVOTS & ADR:")
        print(f"    PP: {r['pivot_pp']:.5f} | Day Type: {r['pivot_day_type']}")
        print(f"    ADR: {r['adr_pips']:.0f}p | ADR High: {r['adr_high']:.5f} | ADR Low: {r['adr_low']:.5f}")

        print(f"\n  HUD DASHBOARD:")
        print(f"    TDR: {r['hud_tdr']:.0f}p | YDR: {r['hud_ydr']:.0f}p | WADR: {r['hud_wadr']:.0f}p | MADR: {r['hud_madr']:.0f}p")
        print(f"    HYADR: {r['hud_hyadr']:.0f}p | WR: {r['hud_wr']:.0f}p | 3xADR: {r['hud_3xadr']:.0f}p")

        print(f"\n  CROSSOVERS: Short={r['xo_short']} | Long={r['xo_long']}")
        print(f"  SPREAD: {r['spread']:.1f} pips")
        print(f"  CHART: {r['chart_path']}")

    # ================================================================
    # WHATSAPP — Send top setups with charts
    # ================================================================
    print(f"\n{'='*100}")
    print(f"  SENDING WHATSAPP NOTIFICATIONS")
    print(f"{'='*100}\n")

    # Build summary message
    msg_lines = [
        f"HELIX V3 MARKET ANALYSIS",
        f"{'='*30}",
        f"{now_eat.strftime('%Y-%m-%d %H:%M EAT')}",
        f"Account: {info.login} | ${info.balance:.2f}",
        f"",
    ]

    for r in results[:6]:
        action = "ENTRY" if r["trade_valid"] else "WATCH" if r["confluence"] >= 40 else "MONITOR"
        tdi_str = f"RSI {r['tdi_rsi']:.0f}"
        for s in r["tdi_signals"]:
            if s not in ("NONE",):
                tdi_str = s.replace("_", " ")[:20]
                break

        msg_lines.append(
            f"{r['symbol']} | Confl: {r['confluence']}/100 | {action}\n"
            f"  {r['weekly_phase']} {r['weekly_trend']} | L{r['h4_level']} {r['h4_trend']}\n"
            f"  {r['h1_session']} | TDI: {tdi_str}\n"
            f"  Setup: {r['trade_type']} | AR: {r['m15_asian_pips']:.0f}p\n"
            f"  ADR: {r['adr_pips']:.0f}p | WADR: {r['hud_wadr']:.0f}p\n"
        )

    summary = "\n".join(msg_lines)
    sent = notifier._send(summary)
    print(f"  Summary message: {'SENT' if sent else 'FAILED'}")

    # Send top 3 charts with detailed flashcard messages
    for r in results[:3]:
        sym = r["symbol"]
        chart = r["chart_path"]

        flash_msg = (
            f"HELIX V3 FLASHCARD: {sym} M15\n"
            f"{'='*30}\n"
            f"\n"
            f"Weekly: {r['weekly_phase']} {r['weekly_trend']} ({r['weekly_cycle']})\n"
            f"H4: Level {r['h4_level']} {r['h4_trend']}\n"
            f"H1: {r['h1_session']} {r['h1_trend']}\n"
            f"HOD: {r['h1_hod']:.5f} | LOD: {r['h1_lod']:.5f}\n"
            f"\n"
            f"TDI: RSI={r['tdi_rsi']:.0f} Sig={r['tdi_signal']:.0f} Base={r['tdi_base']:.0f}\n"
            f"  {', '.join(s for s in r['tdi_signals'] if s != 'NONE') or 'No signal'}\n"
            f"\n"
            f"Patterns: {r['trade_type']}\n"
            f"  RRT={r['rrt_count']} Spikes={r['spike_count']} PinBars={r['pin_bar_count']}\n"
            f"  M/W={r['pat_mw']} HalfBat={r['half_batman']}\n"
            f"\n"
            f"Pivots: PP={r['pivot_pp']:.5f} ({r['pivot_day_type']})\n"
            f"ADR: {r['adr_pips']:.0f}p H={r['adr_high']:.5f} L={r['adr_low']:.5f}\n"
            f"WADR: {r['hud_wadr']:.0f}p MADR: {r['hud_madr']:.0f}p\n"
            f"\n"
            f"Confluence: {r['confluence']}/100\n"
            f"{now_eat.strftime('%Y-%m-%d %H:%M EAT')}"
        )

        sent = notifier.send_with_chart(flash_msg, chart)
        print(f"  {sym} flashcard: {'SENT' if sent else 'FAILED'} -> {chart}")

    engine.disconnect()

    # Save results
    output = Path("updates") / f"scan_{now_eat.strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output, "w", encoding="utf-8") as f:
        f.write(f"HELIX V3 FULL SCAN | {now_eat.strftime('%Y-%m-%d %H:%M EAT')}\n\n")
        for r in results:
            f.write(f"{r['symbol']}: confluence={r['confluence']} dir={r['trade_dir']} "
                    f"valid={r['trade_valid']} type={r['trade_type']} "
                    f"tdi_rsi={r['tdi_rsi']:.1f} adr={r['adr_pips']:.0f}p\n")
    print(f"\n  Scan saved to: {output}")
    print(f"\n{'='*100}")
    print(f"  SCAN COMPLETE")
    print(f"{'='*100}")


if __name__ == "__main__":
    run_full_scan()
