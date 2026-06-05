"""Fresh market scan with corrected M/W direction logic."""
import sys, time
sys.stdout.reconfigure(encoding="utf-8")
from datetime import datetime, timedelta, timezone
from helix_v3.core.quant_engine import MMMQuantitativeEngine
from helix_v3.core.mtf_analyzer import MTFAnalyzer
from helix_v3.core.tdi import compute_tdi, compute_pivots, compute_adr, compute_hud, compute_daily_hilo
from helix_v3.core.patterns import scan_patterns
from helix_v3.core.reentry_guard import ReentryGuard
from helix_v3.visualization.annotated_chart import AnnotatedChartGenerator
from config.pair_profiles import get_pair_profile
import MetaTrader5 as mt5

EAT = timezone(timedelta(hours=3))
now = datetime.now(EAT)

engine = MMMQuantitativeEngine()
engine.connect()
mtf = MTFAnalyzer(engine)
annotator = AnnotatedChartGenerator()
guard = ReentryGuard()
info = mt5.account_info()

SYMBOLS = ['EURUSD','GBPUSD','AUDUSD','GBPAUD','GBPJPY','GBPNZD',
           'EURJPY','EURCHF','GBPCHF','USDCHF','USDJPY','AUDJPY','XAUUSD']

print(f"HELIX V3 FRESH SCAN — Direction Fix Applied")
print("=" * 80)
print(f"{now.strftime('%Y-%m-%d %H:%M EAT')} | Bal: ${info.balance:.2f} | Eq: ${info.equity:.2f} | P&L: ${info.profit:+.2f}")

positions = mt5.positions_get()
if positions:
    print(f"\nOPEN POSITIONS:")
    for p in positions:
        pip_div = 100 if "JPY" in p.symbol else 10000
        pips = (p.price_current - p.price_open) * pip_div if p.type == 0 else (p.price_open - p.price_current) * pip_div
        d = "BUY" if p.type == 0 else "SELL"
        print(f"  {d} {p.symbol} {p.volume}L @ {p.price_open} -> {p.price_current} | {pips:+.1f}p | ${p.profit:+.2f}")

gs = guard.get_status()
if gs["banned"] or gs["cooldowns"]:
    print(f"\nGUARD: Banned={gs['banned']} | Cooldowns={gs['cooldowns']}")

results = []
charts = {}
for symbol in SYMBOLS:
    a = mtf.analyze(symbol)
    df_m15 = engine.fetch_rates(symbol, "M15", count=200)
    df_d1 = engine.fetch_rates(symbol, "D1", count=140)
    pip_size = 0.01 if "JPY" in symbol else (0.1 if symbol == "XAUUSD" else 0.0001)

    tdi = compute_tdi(df_m15)
    prev_d = df_d1.iloc[-2]
    hud = compute_hud(df_d1, pip_size)
    hilo = compute_daily_hilo(df_d1)
    adr_val = compute_adr(df_d1)
    pivots = compute_pivots(prev_d["High"], prev_d["Low"], prev_d["Close"], prev_d["Close"] > prev_d["Open"])
    patterns = scan_patterns(df_m15.iloc[-50:], pip_size, hilo["phod"], hilo["plod"],
        a.fifteen_min.asian_range_high, a.fifteen_min.asian_range_low)

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

for i, r in enumerate(results[:7]):
    action = "ENTRY" if r["v"] else ("WATCH" if r["c"] >= 40 else "WAIT")
    if r["guard"]:
        action = "BLOCKED"

    sep = "-" * 80
    print(f"\n{sep}")
    print(f"#{i+1} {r['s']} {r['d']} | Confluence: {r['c']}/100 | {action}")
    if r["guard"]:
        print(f"  *** GUARD: {r['guard']} ***")
    print(sep)

    print(f"\n  WEEKLY: {r['wt']} ({r['wp']}) | Cycle: {r['wc']} | {r['dpk']}d from peak")
    print(f"  H4: Level {r['h4l']} {r['h4t']}")
    print(f"  H1: {r['h1s']} {r['h1t']}")
    print(f"    HOD: {r['hod']:.5f} (locked={r['hod_l']}) | LOD: {r['lod']:.5f} (locked={r['lod_l']})")

    print(f"\n  15M:")
    print(f"    Asian Range: {r['ar']:.0f}p (valid={r['acc']})")
    print(f"    M/W: {r['mw']} -> entry direction: {r['entry_d']}")
    if r["hunt"]:
        print(f"    Stop Hunt: {r['hunt_d']} {r['hunt_p']:.1f}p | Pushes: {r['push']}/3")
    print(f"    Setup: {r['pt']} | RRT: {r['rrtc']}x | Spikes: {r['spk']}")

    tdi_str = "; ".join(r["tdi_sigs"][:2]) if r["tdi_sigs"] else "neutral"
    print(f"\n  TDI: RSI={r['tdi_rsi']:.0f} Sig={r['tdi_sig']:.0f} Base={r['tdi_base']:.0f} | {tdi_str}")
    if r["tdi_shark"]:
        print(f"    SHARK FIN active")
    if r["tdi_sq"]:
        print(f"    VB SQUEEZE")
    if r["tdi_div"] != "none":
        print(f"    DIVERGENCE: {r['tdi_div']}")

    print(f"\n  HUD: TDR={r['hud_tdr']:.0f}p | WADR={r['hud_wadr']:.0f}p | MADR={r['hud_madr']:.0f}p | ADR={r['adr_p']:.0f}p")
    for rej in r["rej"]:
        print(f"  WARN: {rej}")
    if r["chart"]:
        print(f"  CHART: {r['chart']}")

print(f"\n{'-'*80}")
print("REMAINING:")
for r in results[7:]:
    action = "BLOCKED" if r["guard"] else ("WATCH" if r["c"] >= 40 else "WAIT")
    tdi_short = "; ".join(r["tdi_sigs"][:1]) if r["tdi_sigs"] else f"RSI {r['tdi_rsi']:.0f}"
    print(f"  {r['s']:<8} {r['c']:>3} {r['d']:<8} {action:<8} M/W->{r['entry_d']:<5} {tdi_short}")

buy_v = sum(1 for r in results if r["d"] == "BUY" and r["c"] >= 50)
sell_v = sum(1 for r in results if r["d"] == "SELL" and r["c"] >= 50)
blocked = sum(1 for r in results if r["guard"])
print(f"\n{'='*80}")
print(f"MARKET BIAS: {buy_v} BUY (conf>=50) | {sell_v} SELL (conf>=50) | {13-buy_v-sell_v} other")
print(f"GUARD: {blocked} pair(s) blocked")
print(f"{'='*80}")

engine.disconnect()
guard.close()
