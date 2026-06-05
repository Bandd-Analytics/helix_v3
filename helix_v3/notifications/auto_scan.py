"""Automated Market Scan with Telegram Notifications.

Runs the full 13-pair MTF analysis and sends a narrative report
with top charts to Telegram. Can be run:
  - Manually: python -m helix_v3.notifications.auto_scan
  - Scheduled: via Windows Task Scheduler or cron
  - Loop mode: python -m helix_v3.notifications.auto_scan --loop

Schedule targets (all EAT):
  08:00 - Pre-London scan (Asian range formed, looking for stop hunts)
  10:00 - London open scan (setups forming, entries imminent)
  15:00 - NYC overlap scan (second wave entries)
  00:00 - EOD summary (what happened, what to watch tomorrow)
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Tuple

sys.stdout.reconfigure(encoding="utf-8")

EAT = timezone(timedelta(hours=3))

# Scheduled scan times (hour in EAT)
SCAN_SCHEDULE = {
    8: "PRE-LONDON",
    10: "LONDON OPEN",
    15: "NYC OVERLAP",
    0: "END OF DAY",
}


def run_scan() -> Tuple[str, List[str]]:
    """Execute full market scan and return (analysis_text, chart_paths)."""
    from helix_v3.core.quant_engine import MMMQuantitativeEngine
    from helix_v3.core.mtf_analyzer import MTFAnalyzer
    from helix_v3.core.tdi import compute_tdi, compute_pivots, compute_adr, compute_hud, compute_daily_hilo
    from helix_v3.core.patterns import scan_patterns
    from helix_v3.core.reentry_guard import ReentryGuard
    from helix_v3.visualization.annotated_chart import AnnotatedChartGenerator
    from config.pair_profiles import get_pair_profile
    import MetaTrader5 as mt5

    now = datetime.now(EAT)
    session = _current_session(now)

    engine = MMMQuantitativeEngine()
    engine.connect()
    mtf_analyzer = MTFAnalyzer(engine)
    annotator = AnnotatedChartGenerator()
    guard = ReentryGuard()
    info = mt5.account_info()

    SYMBOLS = [
        'EURUSD', 'GBPUSD', 'AUDUSD', 'GBPAUD', 'GBPJPY', 'GBPNZD',
        'EURJPY', 'EURCHF', 'GBPCHF', 'USDCHF', 'USDJPY', 'AUDJPY', 'XAUUSD',
    ]

    positions = mt5.positions_get()
    results = []
    charts = {}

    for symbol in SYMBOLS:
        a = mtf_analyzer.analyze(symbol)
        df_m15 = engine.fetch_rates(symbol, "M15", count=200)
        df_d1 = engine.fetch_rates(symbol, "D1", count=140)
        pip_size = 0.01 if "JPY" in symbol else (0.1 if symbol == "XAUUSD" else 0.0001)

        tdi = compute_tdi(df_m15)
        prev_d = df_d1.iloc[-2]
        hud = compute_hud(df_d1, pip_size)
        hilo = compute_daily_hilo(df_d1)
        adr_val = compute_adr(df_d1)
        pivots = compute_pivots(prev_d["High"], prev_d["Low"], prev_d["Close"],
                                prev_d["Close"] > prev_d["Open"])
        patterns = scan_patterns(
            df_m15.iloc[-50:], pip_size, hilo["phod"], hilo["plod"],
            a.fifteen_min.asian_range_high, a.fifteen_min.asian_range_low,
        )

        chart_path = None
        if a.confluence_score >= 40:
            try:
                _, chart_path = annotator.generate_from_mtf(
                    df_m15, symbol, "M15", a,
                    tdi_result=tdi, pattern_scan=patterns, pivots=pivots,
                    adr=adr_val, prev_hod=hilo["phod"], prev_lod=hilo["plod"],
                )
                charts[symbol] = str(chart_path)
            except Exception:
                pass

        tdi_sigs = [s.value.replace("_", " ") for s in tdi.signals if s.value != "NONE"]
        guard_block = guard.check(symbol, a.trade_direction.value) if a.trade_direction.value != "NEUTRAL" else None

        results.append({
            "s": symbol, "c": a.confluence_score, "v": a.trade_valid,
            "d": a.trade_direction.value,
            "wt": a.weekly.trend_direction.value, "wp": a.weekly.week_phase.value,
            "wc": a.weekly.cycle_position.value, "dpk": a.weekly.days_since_peak,
            "h4l": a.four_hour.level_count, "h4t": a.four_hour.trend_direction.value,
            "h1s": a.one_hour.session_phase.value, "h1t": a.one_hour.trend_direction.value,
            "hod": a.one_hour.hod, "lod": a.one_hour.lod,
            "hod_l": a.one_hour.hod_locked, "lod_l": a.one_hour.lod_locked,
            "ar": a.fifteen_min.asian_range_pips, "acc": a.fifteen_min.accumulation_valid,
            "hunt": a.fifteen_min.stop_hunt_detected, "hunt_d": a.fifteen_min.stop_hunt_direction.value,
            "hunt_p": a.fifteen_min.stop_hunt_pips, "push": a.fifteen_min.push_count,
            "mw": a.fifteen_min.m_w_forming, "rrt": a.fifteen_min.rrt_detected,
            "entry_d": a.fifteen_min.entry_direction.value,
            "tdi_sigs": tdi_sigs, "tdi_rsi": tdi.rsi, "tdi_sig": tdi.signal, "tdi_base": tdi.base,
            "tdi_shark": tdi.shark_fin_active, "tdi_sq": tdi.vb_squeeze, "tdi_div": tdi.divergence,
            "pt": patterns.trade_type.value, "rrtc": patterns.rrt_count, "spk": patterns.spike_count,
            "hud_tdr": hud["TDR"], "hud_wadr": hud["WADR"], "hud_madr": hud["MADR"],
            "adr_p": adr_val / pip_size,
            "rej": a.rejection_reasons, "guard": guard_block, "chart": chart_path,
        })

    results.sort(key=lambda x: x["c"], reverse=True)

    # Build narrative analysis
    text = _build_narrative(results, info, positions, guard, now, session)

    # Collect top charts
    top_charts = []
    for r in results[:5]:
        if r.get("chart"):
            top_charts.append(str(r["chart"]))

    engine.disconnect()
    guard.close()

    return text, top_charts


def _current_session(now: datetime) -> str:
    h = now.hour
    if 0 <= h < 8:
        return "ASIAN"
    elif 8 <= h < 10:
        return "PRE-LONDON"
    elif 10 <= h < 15:
        return "LONDON"
    elif 15 <= h < 19:
        return "NYC OVERLAP"
    else:
        return "NYC LATE"


def _build_narrative(
    results: list, info, positions, guard, now: datetime, session: str,
) -> str:
    """Build a top-down narrative analysis like the manual scan."""
    lines = []
    day_name = now.strftime("%A")

    lines.append(f"HELIX V3 MARKET SCAN")
    lines.append(f"{now.strftime('%Y-%m-%d %H:%M EAT')} | {day_name} | {session}")
    lines.append(f"Bal: ${info.balance:.2f} | Eq: ${info.equity:.2f} | P&L: ${info.profit:+.2f}")
    lines.append("")

    # Open positions
    if positions:
        lines.append("OPEN POSITIONS:")
        for p in positions:
            pip_div = 100 if "JPY" in p.symbol else 10000
            pips = (p.price_current - p.price_open) * pip_div if p.type == 0 else (p.price_open - p.price_current) * pip_div
            d = "BUY" if p.type == 0 else "SELL"
            lines.append(f"  {d} {p.symbol} {p.volume}L | {pips:+.1f}p | ${p.profit:+.2f}")
        lines.append("")

    # Guard status
    gs = guard.get_status()
    if gs["banned"] or gs["cooldowns"]:
        lines.append(f"GUARD: Banned={gs['banned']} | Cooldowns={gs['cooldowns']}")
        lines.append("")

    # Entry-grade setups
    entries = [r for r in results if r["v"] and not r["guard"]]
    watches = [r for r in results if r["c"] >= 40 and not r["v"]]
    waiting = [r for r in results if r["c"] < 40]

    if entries:
        lines.append("=" * 35)
        lines.append("ENTRY SETUPS")
        lines.append("=" * 35)
        for r in entries:
            lines.append("")
            lines.append(f"{r['s']} {r['d']} | {r['c']}/100")
            lines.append(f"  Wkly: {r['wt']} ({r['wp']})")
            lines.append(f"  H4: L{r['h4l']} {r['h4t']} | H1: {r['h1s']} {r['h1t']}")
            lines.append(f"  Asian: {r['ar']:.0f}p | M/W: {r['mw']} -> {r['entry_d']}")
            if r["hunt"]:
                lines.append(f"  Hunt: {r['hunt_d']} {r['hunt_p']:.1f}p | Push: {r['push']}/3")
            tdi_str = "; ".join(r["tdi_sigs"][:2]) if r["tdi_sigs"] else "neutral"
            lines.append(f"  TDI: RSI={r['tdi_rsi']:.0f} | {tdi_str}")
            lines.append(f"  ADR: {r['hud_tdr']:.0f}/{r['adr_p']:.0f}p used ({r['hud_tdr']/r['adr_p']*100:.0f}%)" if r['adr_p'] > 0 else "")
            if r["wt"] != r["d"] and r["d"] != "NEUTRAL":
                lines.append(f"  ** COUNTER-WEEKLY **")
            for rej in r["rej"]:
                lines.append(f"  ! {rej}")
    else:
        lines.append("No entry-grade setups right now.")

    # Watch list
    if watches:
        lines.append("")
        lines.append("WATCH LIST:")
        for r in watches:
            status = "BLOCKED" if r["guard"] else "WATCH"
            tdi_short = "; ".join(r["tdi_sigs"][:1]) if r["tdi_sigs"] else f"RSI {r['tdi_rsi']:.0f}"
            lines.append(f"  {r['s']:<8} {r['c']:>3} {r['d']:<8} {status:<8} {tdi_short}")

    # Market bias
    buy_v = sum(1 for r in results if r["d"] == "BUY" and r["c"] >= 50)
    sell_v = sum(1 for r in results if r["d"] == "SELL" and r["c"] >= 50)
    blocked = sum(1 for r in results if r["guard"])

    lines.append("")
    lines.append(f"BIAS: {buy_v} BUY | {sell_v} SELL | {blocked} blocked")

    return "\n".join(lines)


def send_to_telegram(text: str, charts: List[str]) -> None:
    """Send scan results via Telegram."""
    from helix_v3.notifications.telegram import TelegramNotifier

    notifier = TelegramNotifier()
    if not notifier.enabled:
        print("Telegram not configured. Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env")
        print("\nAnalysis (console only):\n")
        print(text)
        return

    notifier.notify_market_scan(text, charts)
    print(f"Scan sent to Telegram ({len(charts)} charts attached)")


def run_loop() -> None:
    """Run scans on schedule (loop mode).

    Checks every 5 minutes. Fires a scan at each scheduled hour.
    Also fires an immediate scan on startup.
    """
    print("HELIX V3 AUTO-SCAN LOOP MODE")
    print(f"Schedule (EAT): {SCAN_SCHEDULE}")
    print("Press Ctrl+C to stop.\n")

    fired_today: set = set()
    last_date = ""

    # Immediate scan on startup
    print(f"[{datetime.now(EAT).strftime('%H:%M EAT')}] Startup scan...")
    try:
        text, charts = run_scan()
        send_to_telegram(text, charts)
    except Exception as e:
        print(f"Startup scan failed: {e}")

    while True:
        try:
            now = datetime.now(EAT)
            today = now.strftime("%Y-%m-%d")

            # Reset fired set on new day
            if today != last_date:
                fired_today.clear()
                last_date = today

            hour = now.hour
            if hour in SCAN_SCHEDULE and hour not in fired_today:
                label = SCAN_SCHEDULE[hour]
                print(f"\n[{now.strftime('%H:%M EAT')}] Scheduled scan: {label}")
                try:
                    text, charts = run_scan()
                    send_to_telegram(text, charts)
                    fired_today.add(hour)
                except Exception as e:
                    print(f"Scan failed: {e}")

            time.sleep(300)  # Check every 5 minutes

        except KeyboardInterrupt:
            print("\nAuto-scan loop stopped.")
            break


def main() -> None:
    parser = argparse.ArgumentParser(description="Helix V3 Automated Market Scan")
    parser.add_argument("--loop", action="store_true", help="Run in scheduled loop mode")
    parser.add_argument("--console", action="store_true", help="Print to console only, no Telegram")
    args = parser.parse_args()

    if args.loop:
        run_loop()
    else:
        text, charts = run_scan()
        if args.console:
            print(text)
            print(f"\nCharts: {charts}")
        else:
            send_to_telegram(text, charts)
            print(text)


if __name__ == "__main__":
    main()
