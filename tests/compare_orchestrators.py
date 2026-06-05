"""Side-by-side comparison of Orchestrator V1 vs V2.

Runs a single scan cycle through both pipelines and produces a detailed
evaluation report showing what each version sees, decides, and why.

Output:
  - Console report
  - updates/eval_YYYYMMDD_HHMMSS.txt — persisted evaluation log
"""

from __future__ import annotations

import asyncio
import json
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import MetaTrader5 as mt5

from config.settings import settings
from helix_v3.core.mtf_analyzer import MTFAnalyzer
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.consensus.validator import MMMConsensusValidator
from helix_v3.execution.gatekeeper import MT5ExecutionGatekeeper
from helix_v3.visualization.chart_exporter import MMMChartVisualizer
from helix_v3.visualization.annotated_chart import AnnotatedChartGenerator
from helix_v3.utils.logger import get_logger

logger = get_logger("compare")
EAT = timezone(timedelta(hours=3))
SYMBOLS = list(settings.trading.symbols)
TIMEFRAMES = ["M15", "H1"]

OUTPUT_DIR = Path("updates")
OUTPUT_DIR.mkdir(exist_ok=True)


def print_header(text: str, lines: list) -> None:
    sep = "=" * 90
    for s in [f"\n{sep}", f"  {text}", sep]:
        print(s)
        lines.append(s)


def p(text: str, lines: list) -> None:
    print(text)
    lines.append(text)


async def main() -> None:
    now_eat = datetime.now(EAT)
    ts = now_eat.strftime("%Y%m%d_%H%M%S")
    lines: list[str] = []

    print_header(
        f"HELIX V3: ORCHESTRATOR V1 vs V2 COMPARISON | {now_eat.strftime('%Y-%m-%d %H:%M EAT')}",
        lines,
    )

    engine = MMMQuantitativeEngine()
    visualizer = MMMChartVisualizer()
    annotator = AnnotatedChartGenerator()
    gatekeeper = MT5ExecutionGatekeeper()

    if not engine.connect():
        p("FATAL: Cannot connect to MT5", lines)
        sys.exit(1)

    info = mt5.account_info()
    p(f"  Account: {info.login} | Balance: {info.balance:.2f} | Equity: {info.equity:.2f}", lines)

    mtf = MTFAnalyzer(engine)

    # ----------------------------------------------------------------
    # V1 Analysis: flat quant signals per symbol per timeframe
    # ----------------------------------------------------------------
    print_header("V1 ANALYSIS (Flat Quant Engine — per symbol per timeframe)", lines)

    v1_results = {}
    v1_start = time.monotonic()

    for symbol in SYMBOLS:
        v1_results[symbol] = {}
        for tf in TIMEFRAMES:
            sig = engine.generate_signal(symbol, tf)
            v1_results[symbol][tf] = {
                "pre_filter_passed": sig.pre_filter_passed,
                "accumulation": sig.accumulation_active,
                "stop_hunt": sig.stop_hunt_detected,
                "hunt_dir": sig.stop_hunt.direction.value if sig.stop_hunt else "N/A",
                "hunt_pips": sig.stop_hunt.breach_pips if sig.stop_hunt else 0,
                "trend": sig.ema_vector.trend_alignment.value,
                "asian_range": sig.session_bounds.range_pips if sig.session_bounds else 0,
            }

    v1_elapsed = time.monotonic() - v1_start

    p(f"\n  {'Symbol':<10} {'TF':<5} {'Filter':<8} {'Accum':<7} {'Hunt':<7} "
      f"{'HuntDir':<8} {'HuntPips':<9} {'Trend':<10} {'AsianRng':<10}", lines)
    p("-" * 90, lines)

    v1_passed = 0
    for symbol in SYMBOLS:
        for tf in TIMEFRAMES:
            r = v1_results[symbol][tf]
            passed = "PASS" if r["pre_filter_passed"] else "no"
            if r["pre_filter_passed"]:
                v1_passed += 1
            p(f"  {symbol:<10} {tf:<5} {passed:<8} "
              f"{'Y' if r['accumulation'] else 'n':<7} "
              f"{'Y' if r['stop_hunt'] else 'n':<7} "
              f"{r['hunt_dir']:<8} "
              f"{r['hunt_pips']:<9.1f} "
              f"{r['trend']:<10} "
              f"{r['asian_range']:<10.1f}", lines)

    p(f"\n  V1 Summary: {v1_passed}/{len(SYMBOLS)*len(TIMEFRAMES)} passed pre-filter | "
      f"Time: {v1_elapsed:.2f}s", lines)

    # ----------------------------------------------------------------
    # V2 Analysis: full MTF top-down per symbol
    # ----------------------------------------------------------------
    print_header("V2 ANALYSIS (MTF Top-Down — per symbol, all TFs in one pass)", lines)

    v2_results = {}
    v2_start = time.monotonic()

    for symbol in SYMBOLS:
        try:
            analysis = mtf.analyze(symbol)
            v2_results[symbol] = {
                "weekly_trend": analysis.weekly.trend_direction.value,
                "weekly_phase": analysis.weekly.week_phase.value,
                "weekly_cycle": analysis.weekly.cycle_position.value,
                "days_since_peak": analysis.weekly.days_since_peak,
                "midweek_reversal": analysis.weekly.midweek_reversal_expected,
                "h4_level": analysis.four_hour.level_count,
                "h4_trend": analysis.four_hour.trend_direction.value,
                "h4_choppy": analysis.four_hour.is_choppy,
                "h4_peak": analysis.four_hour.peak_formation_detected,
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
                "trade_conf": analysis.trade_confidence,
                "rejections": analysis.rejection_reasons,
                "full_report": mtf.format_analysis(analysis),
            }
        except Exception as e:
            v2_results[symbol] = {"error": str(e)}

    v2_elapsed = time.monotonic() - v2_start

    # Summary table
    p(f"\n  {'Symbol':<10} {'Weekly':<18} {'H4':<14} {'H1 Session':<16} "
      f"{'M15 Hunt':<12} {'Push':<6} {'Confl':<6} {'Valid':<6} {'Dir':<8}", lines)
    p("-" * 90, lines)

    v2_valid = 0
    v2_high_confluence = 0
    for symbol in SYMBOLS:
        r = v2_results[symbol]
        if "error" in r:
            p(f"  {symbol:<10} ERROR: {r['error']}", lines)
            continue

        hunt = f"{r['m15_hunt_dir']} {r['m15_hunt_pips']:.0f}p" if r["m15_hunt"] else "-"
        valid_str = "YES" if r["trade_valid"] else "no"
        if r["trade_valid"]:
            v2_valid += 1
        if r["confluence"] >= 50:
            v2_high_confluence += 1

        p(f"  {symbol:<10} "
          f"{r['weekly_phase']:<8} {r['weekly_trend']:<8} "
          f"L{r['h4_level']} {r['h4_trend']:<8} "
          f"{r['h1_session']:<16} "
          f"{hunt:<12} "
          f"{r['m15_pushes']:<6} "
          f"{r['confluence']:<6} "
          f"{valid_str:<6} "
          f"{r['trade_dir']:<8}", lines)

        if r["rejections"]:
            for rej in r["rejections"]:
                p(f"  {'':>10}   WARN: {rej}", lines)

    p(f"\n  V2 Summary: {v2_valid}/{len(SYMBOLS)} trade valid | "
      f"{v2_high_confluence}/{len(SYMBOLS)} confluence >= 50 | Time: {v2_elapsed:.2f}s", lines)

    # ----------------------------------------------------------------
    # Detailed MTF reports for top symbols
    # ----------------------------------------------------------------
    print_header("V2 DETAILED MTF REPORTS (Top 5 by confluence)", lines)

    sorted_syms = sorted(
        [(s, r) for s, r in v2_results.items() if "confluence" in r],
        key=lambda x: x[1]["confluence"],
        reverse=True,
    )

    for symbol, r in sorted_syms[:5]:
        p(r["full_report"], lines)

    # ----------------------------------------------------------------
    # Head-to-head comparison
    # ----------------------------------------------------------------
    print_header("HEAD-TO-HEAD COMPARISON", lines)

    p(f"\n  {'Metric':<40} {'V1':<25} {'V2':<25}", lines)
    p("-" * 90, lines)
    p(f"  {'Analysis approach':<40} {'Flat per TF':<25} {'Top-down MTF':<25}", lines)
    p(f"  {'Scan time':<40} {f'{v1_elapsed:.2f}s':<25} {f'{v2_elapsed:.2f}s':<25}", lines)
    p(f"  {'Symbols analyzed':<40} {len(SYMBOLS):<25} {len(SYMBOLS):<25}", lines)
    p(f"  {'TF combinations':<40} {f'{len(SYMBOLS)}x{len(TIMEFRAMES)}={len(SYMBOLS)*len(TIMEFRAMES)}':<25} {f'{len(SYMBOLS)}x1={len(SYMBOLS)} (all TFs in 1)':<25}", lines)
    p(f"  {'Passed entry gate':<40} {f'{v1_passed} pre_filter_passed':<25} {f'{v2_valid} trade_valid':<25}", lines)
    p(f"  {'High confidence setups':<40} {'N/A (boolean only)':<25} {f'{v2_high_confluence} confluence>=50':<25}", lines)
    p(f"  {'Weekly context':<40} {'No':<25} {'Yes (phase+trend+peak)':<25}", lines)
    p(f"  {'H4 cycle level':<40} {'No':<25} {'Yes (L1/L2/L3)':<25}", lines)
    p(f"  {'Session awareness':<40} {'No':<25} {'Yes (phase detection)':<25}", lines)
    p(f"  {'HOD/LOD tracking':<40} {'No':<25} {'Yes (with lock detect)':<25}", lines)
    p(f"  {'Push count (3 pushes)':<40} {'No':<25} {'Yes':<25}", lines)
    p(f"  {'M/W formation':<40} {'Via vision only':<25} {'Quant + vision':<25}", lines)
    p(f"  {'Annotated charts':<40} {'No':<25} {'Yes (Asian/hunt/HOD)':<25}", lines)
    p(f"  {'WhatsApp with chart':<40} {'Text only':<25} {'Chart image attached':<25}", lines)
    p(f"  {'Flashcard learning':<40} {'Not connected':<25} {'Active (entry/scan/miss)':<25}", lines)
    p(f"  {'Confluence scoring':<40} {'No':<25} {'Yes (0-100 composite)':<25}", lines)

    # ----------------------------------------------------------------
    # Key insights
    # ----------------------------------------------------------------
    print_header("KEY INSIGHTS", lines)

    # Find where V2 sees things V1 misses
    v2_sees_more = []
    for symbol in SYMBOLS:
        r2 = v2_results.get(symbol, {})
        if "error" in r2:
            continue

        v1_m15 = v1_results[symbol].get("M15", {})

        # V2 has weekly context V1 doesn't
        notes = []
        if r2["weekly_phase"] == "MID_WEEK" and r2["midweek_reversal"]:
            notes.append("Mid-week reversal expected")
        if r2["h4_level"] >= 2:
            notes.append(f"H4 at L{r2['h4_level']} ({r2['h4_trend']})")
        if r2["h1_hod_locked"] or r2["h1_lod_locked"]:
            locked = []
            if r2["h1_hod_locked"]:
                locked.append("HOD")
            if r2["h1_lod_locked"]:
                locked.append("LOD")
            notes.append(f"{'+'.join(locked)} locked")
        if r2["h1_50_200_cross"] != "none":
            notes.append(f"H1 50/200 {r2['h1_50_200_cross']} cross")
        if r2["m15_pushes"] >= 2:
            notes.append(f"{r2['m15_pushes']} pushes detected")

        if notes:
            v2_sees_more.append((symbol, r2["confluence"], notes))

    if v2_sees_more:
        p("\n  V2 detects context V1 cannot see:", lines)
        for symbol, conf, notes in sorted(v2_sees_more, key=lambda x: -x[1]):
            p(f"    {symbol} (confluence={conf}): {'; '.join(notes)}", lines)
    else:
        p("\n  Market conditions are quiet — neither version sees strong setups.", lines)

    # Chart generation test
    print_header("ANNOTATED CHART TEST (V2 only)", lines)
    best_sym = sorted_syms[0][0] if sorted_syms else SYMBOLS[0]
    best_analysis = None
    for sym in SYMBOLS:
        if sym == best_sym and "error" not in v2_results.get(sym, {"error": True}):
            best_analysis = mtf.analyze(sym)
            break

    if best_analysis:
        df = engine.fetch_rates(best_sym, "M15", count=200)
        _, chart_path = annotator.generate_from_mtf(df, best_sym, "M15", best_analysis)
        p(f"  Generated annotated chart: {chart_path}", lines)
        p(f"  (This chart would be attached to WhatsApp in V2)", lines)
    else:
        p("  Skipped — no analysis available", lines)

    # ----------------------------------------------------------------
    # Verdict
    # ----------------------------------------------------------------
    print_header("EVALUATION VERDICT", lines)

    improvements = [
        "V2 provides full Weekly->4H->1H->15M context per symbol (V1 has none)",
        "V2 tracks weekly cycle position, mid-week reversal expectation, days from peak",
        "V2 counts H4 cycle levels (L1/L2/L3) — critical for MMM entry timing",
        "V2 detects session phase and HOD/LOD locks — tells you where in the day you are",
        "V2 counts pushes in stop hunt zone (3 pushes = MMM entry signal)",
        "V2 scores confluence 0-100 instead of binary pass/fail — gradual readiness",
        "V2 generates annotated charts with Asian range, hunt zone, entry markers",
        "V2 sends chart images with WhatsApp (not text-only)",
        "V2 saves flashcards for pattern learning (entry/scan/missed)",
    ]

    for i, imp in enumerate(improvements, 1):
        p(f"  {i}. {imp}", lines)

    tradeoffs = [
        f"V2 scan time ({v2_elapsed:.2f}s) vs V1 ({v1_elapsed:.2f}s) — V2 fetches more data (D1, H4, H1, M15)",
    ]

    p("\n  Trade-offs:", lines)
    for t in tradeoffs:
        p(f"  - {t}", lines)

    p(f"\n  RECOMMENDATION: V2 should replace V1 as the primary orchestrator.", lines)
    p(f"  V1 can remain as a lightweight fast-scan fallback.", lines)

    engine.disconnect()

    # Save to file
    output_file = OUTPUT_DIR / f"eval_{ts}.txt"
    output_file.write_text("\n".join(lines), encoding="utf-8")
    p(f"\n  Evaluation saved to: {output_file}", lines)


if __name__ == "__main__":
    asyncio.run(main())
