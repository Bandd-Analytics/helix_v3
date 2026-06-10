"""
Setup Miner — Mines 13K+ historical setups to answer:
  1. Which exact setups win? (by family, by normalized key)
  2. Which setups recur across pairs? At what frequency?
  3. Which days/sessions are most profitable per pair?
  4. Which price levels correlate with immediate profit?
  5. Best setups per pair with full metadata

Usage:
    python -m helix_v3.analysis.setup_miner                 # full report + promote to validation library
    python -m helix_v3.analysis.setup_miner --report         # report only
    python -m helix_v3.analysis.setup_miner --pair GBPJPY    # single pair deep dive
    python -m helix_v3.analysis.setup_miner --json           # machine-readable output
"""

import argparse
import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Optional

DB_PATH = Path("logs/vision_backtests.db")
VALIDATION_DB = Path("logs/validation_library.db")

# Minimum samples for statistical significance
MIN_SAMPLES = 5
EXCLUDED = "('STALE_EXIT','AMBIGUOUS','OPEN_PROFIT')"
PROFITABLE = "('TARGET_2','TRAIL_STOP','TIME_EXIT_PROFIT','BREAKEVEN_AFTER_T1')"
BIG_WINS = "('TARGET_2','TRAIL_STOP')"
LOSSES = "('LOSS','SL_HIT','TIME_EXIT_LOSS')"


def _conn(db: Path) -> sqlite3.Connection:
    c = sqlite3.connect(str(db))
    c.row_factory = sqlite3.Row
    return c


def _wr(prof, total):
    return round(prof / total * 100, 1) if total > 0 else 0.0


def mine_families(conn, pair: Optional[str] = None) -> list[dict]:
    w = "AND s.symbol = ?" if pair else ""
    p = (pair,) if pair else ()
    rows = conn.execute(f"""
        SELECT s.setup_family, s.symbol, s.direction,
            COUNT(*) as total,
            SUM(CASE WHEN o.outcome IN {PROFITABLE} THEN 1 ELSE 0 END) as profitable,
            SUM(CASE WHEN o.outcome IN {BIG_WINS} THEN 1 ELSE 0 END) as big_wins,
            SUM(CASE WHEN o.outcome IN {LOSSES} THEN 1 ELSE 0 END) as losses,
            ROUND(AVG(o.exit_pips), 2) as avg_pips,
            ROUND(AVG(o.max_favorable_pips), 2) as avg_mfe,
            ROUND(AVG(o.max_adverse_pips), 2) as avg_mae,
            ROUND(SUM(o.exit_pips), 2) as total_pips,
            ROUND(AVG(CASE WHEN o.outcome IN {BIG_WINS} THEN o.exit_pips END), 2) as avg_win_pips,
            ROUND(AVG(CASE WHEN o.outcome IN {LOSSES} THEN o.exit_pips END), 2) as avg_loss_pips,
            ROUND(AVG(o.t1_hit)*100, 1) as t1_rate,
            ROUND(AVG(o.minutes_to_t1), 1) as avg_min_to_t1
        FROM mmm_setup_signatures s
        JOIN mmm_event_outcomes o ON o.signature_id = s.id
        WHERE o.outcome NOT IN {EXCLUDED} {w}
        GROUP BY s.setup_family, s.symbol, s.direction
        HAVING total >= {MIN_SAMPLES}
        ORDER BY CAST(profitable AS FLOAT) / total DESC
    """, p).fetchall()
    return [dict(r) for r in rows]


def mine_keys(conn, pair: Optional[str] = None) -> list[dict]:
    w = "AND s.symbol = ?" if pair else ""
    p = (pair,) if pair else ()
    rows = conn.execute(f"""
        SELECT s.normalized_key, s.setup_family, s.symbol, s.direction,
            COUNT(*) as total,
            SUM(CASE WHEN o.outcome IN {PROFITABLE} THEN 1 ELSE 0 END) as profitable,
            SUM(CASE WHEN o.outcome IN {BIG_WINS} THEN 1 ELSE 0 END) as big_wins,
            SUM(CASE WHEN o.outcome IN {LOSSES} THEN 1 ELSE 0 END) as losses,
            ROUND(AVG(o.exit_pips), 2) as avg_pips,
            ROUND(AVG(o.max_favorable_pips), 2) as avg_mfe,
            ROUND(SUM(o.exit_pips), 2) as total_pips
        FROM mmm_setup_signatures s
        JOIN mmm_event_outcomes o ON o.signature_id = s.id
        WHERE o.outcome NOT IN {EXCLUDED} {w}
        GROUP BY s.normalized_key
        HAVING total >= {MIN_SAMPLES}
        ORDER BY CAST(profitable AS FLOAT) / total DESC
    """, p).fetchall()
    return [dict(r) for r in rows]


def mine_day_session(conn, pair: Optional[str] = None) -> list[dict]:
    w = "AND s.symbol = ?" if pair else ""
    p = (pair,) if pair else ()
    rows = conn.execute(f"""
        SELECT s.symbol,
            CASE CAST(strftime('%w', o.snapshot_at) AS INTEGER)
                WHEN 1 THEN 'Mon' WHEN 2 THEN 'Tue' WHEN 3 THEN 'Wed'
                WHEN 4 THEN 'Thu' WHEN 5 THEN 'Fri' ELSE 'Other'
            END as day,
            CASE
                WHEN s.normalized_key LIKE '%STOP_HUNT%' THEN 'STOP_HUNT'
                WHEN s.normalized_key LIKE '%ACCUMULATION%' THEN 'ACCUMULATION'
                WHEN s.normalized_key LIKE '%TRUE_TREND%' THEN 'TRUE_TREND'
                WHEN s.normalized_key LIKE '%NYC_REVERSAL%' THEN 'NYC_REVERSAL'
                ELSE 'OTHER'
            END as session,
            COUNT(*) as total,
            SUM(CASE WHEN o.outcome IN {PROFITABLE} THEN 1 ELSE 0 END) as profitable,
            SUM(CASE WHEN o.outcome IN {BIG_WINS} THEN 1 ELSE 0 END) as big_wins,
            ROUND(AVG(o.exit_pips), 2) as avg_pips,
            ROUND(SUM(o.exit_pips), 2) as total_pips,
            ROUND(AVG(o.max_favorable_pips), 2) as avg_mfe
        FROM mmm_setup_signatures s
        JOIN mmm_event_outcomes o ON o.signature_id = s.id
        WHERE o.outcome NOT IN {EXCLUDED} {w}
        GROUP BY s.symbol, day, session
        HAVING total >= {MIN_SAMPLES}
        ORDER BY s.symbol, CAST(profitable AS FLOAT) / total DESC
    """, p).fetchall()
    return [dict(r) for r in rows]


def mine_price_levels(conn, pair: Optional[str] = None) -> list[dict]:
    w = "AND s.symbol = ?" if pair else ""
    p = (pair,) if pair else ()
    rows = conn.execute(f"""
        SELECT s.symbol, s.direction,
            CASE
                WHEN json_extract(s.raw_json, '$.setup.asian_range_pips') < 15 THEN 'TIGHT'
                WHEN json_extract(s.raw_json, '$.setup.asian_range_pips') < 30 THEN 'NORMAL'
                WHEN json_extract(s.raw_json, '$.setup.asian_range_pips') < 50 THEN 'WIDE'
                ELSE 'EXTENDED'
            END as ar,
            CASE
                WHEN json_extract(s.raw_json, '$.setup.stop_hunt_pips') < 10 THEN 'SOFT'
                WHEN json_extract(s.raw_json, '$.setup.stop_hunt_pips') < 25 THEN 'NORMAL'
                WHEN json_extract(s.raw_json, '$.setup.stop_hunt_pips') < 40 THEN 'STRONG'
                ELSE 'EXTENDED'
            END as hunt,
            CASE
                WHEN json_extract(s.raw_json, '$.setup.confluence_score') >= 80 THEN 'VERY_HIGH'
                WHEN json_extract(s.raw_json, '$.setup.confluence_score') >= 60 THEN 'HIGH'
                ELSE 'MEDIUM'
            END as conf,
            COUNT(*) as total,
            SUM(CASE WHEN o.outcome IN {PROFITABLE} THEN 1 ELSE 0 END) as profitable,
            SUM(CASE WHEN o.outcome IN {BIG_WINS} THEN 1 ELSE 0 END) as big_wins,
            ROUND(AVG(o.exit_pips), 2) as avg_pips,
            ROUND(AVG(o.max_favorable_pips), 2) as avg_mfe
        FROM mmm_setup_signatures s
        JOIN mmm_event_outcomes o ON o.signature_id = s.id
        WHERE o.outcome NOT IN {EXCLUDED}
          AND json_extract(s.raw_json, '$.setup.asian_range_pips') IS NOT NULL
          AND json_extract(s.raw_json, '$.setup.stop_hunt_pips') IS NOT NULL
          {w}
        GROUP BY s.symbol, s.direction, ar, hunt, conf
        HAVING total >= {MIN_SAMPLES}
        ORDER BY CAST(profitable AS FLOAT) / total DESC
    """, p).fetchall()
    return [dict(r) for r in rows]


def mine_cross_pair(conn) -> list[dict]:
    rows = conn.execute(f"""
        SELECT s.normalized_key,
            GROUP_CONCAT(DISTINCT s.symbol) as pairs,
            COUNT(DISTINCT s.symbol) as pair_count,
            COUNT(*) as total,
            SUM(CASE WHEN o.outcome IN {PROFITABLE} THEN 1 ELSE 0 END) as profitable,
            SUM(CASE WHEN o.outcome IN {BIG_WINS} THEN 1 ELSE 0 END) as big_wins,
            ROUND(AVG(o.exit_pips), 2) as avg_pips,
            ROUND(SUM(o.exit_pips), 2) as total_pips
        FROM mmm_setup_signatures s
        JOIN mmm_event_outcomes o ON o.signature_id = s.id
        WHERE o.outcome NOT IN {EXCLUDED}
        GROUP BY s.normalized_key
        HAVING pair_count >= 2 AND total >= 10
        ORDER BY pair_count DESC, CAST(profitable AS FLOAT) / total DESC
        LIMIT 30
    """).fetchall()
    return [dict(r) for r in rows]


def mine_recurrence(conn, pair: Optional[str] = None) -> list[dict]:
    """How often do winning setups recur? Frequency analysis."""
    w = "AND s.symbol = ?" if pair else ""
    p = (pair,) if pair else ()
    rows = conn.execute(f"""
        SELECT s.normalized_key, s.symbol,
            COUNT(*) as occurrences,
            MIN(o.snapshot_at) as first_seen,
            MAX(o.snapshot_at) as last_seen,
            ROUND(julianday(MAX(o.snapshot_at)) - julianday(MIN(o.snapshot_at)), 1) as span_days,
            SUM(CASE WHEN o.outcome IN {PROFITABLE} THEN 1 ELSE 0 END) as profitable,
            ROUND(AVG(o.exit_pips), 2) as avg_pips
        FROM mmm_setup_signatures s
        JOIN mmm_event_outcomes o ON o.signature_id = s.id
        WHERE o.outcome NOT IN {EXCLUDED} {w}
        GROUP BY s.normalized_key, s.symbol
        HAVING occurrences >= 3
        ORDER BY occurrences DESC
        LIMIT 30
    """, p).fetchall()
    results = []
    for r in rows:
        d = dict(r)
        span = d.get("span_days") or 1
        d["freq_per_week"] = round(d["occurrences"] / max(span, 1) * 7, 2)
        results.append(d)
    return results


def print_report(conn, pair: Optional[str] = None):
    print("=" * 100)
    print("  HELIX V3 SETUP INTELLIGENCE REPORT")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M EAT')}")
    if pair:
        print(f"  Filter: {pair}")
    print("=" * 100)

    # 1. FAMILY RANKINGS
    fam = mine_families(conn, pair)
    print(f"\n{'='*100}")
    print("  1. SETUP FAMILY RANKINGS")
    print(f"{'='*100}")
    hdr = f"{'family':<16}{'pair':<8}{'dir':<5}{'n':>5}{'prof':>5}{'bigW':>5}{'loss':>5}{'WR%':>6}{'avgP':>7}{'MFE':>7}{'MAE':>7}{'totP':>9}{'T1%':>6}"
    print(hdr)
    print("-" * 100)
    for r in fam:
        print(f"{r['setup_family']:<16}{r['symbol']:<8}{r['direction']:<5}"
              f"{r['total']:>5}{r['profitable']:>5}{r['big_wins']:>5}{r['losses']:>5}"
              f"{_wr(r['profitable'], r['total']):>6}{r['avg_pips'] or 0:>7}"
              f"{r['avg_mfe'] or 0:>7}{r['avg_mae'] or 0:>7}"
              f"{r['total_pips'] or 0:>9.1f}{r['t1_rate'] or 0:>6.1f}")

    # 2. TOP EXACT SETUPS
    keys = mine_keys(conn, pair)
    print(f"\n{'='*100}")
    print("  2. TOP 25 EXACT SETUP SIGNATURES")
    print(f"{'='*100}")
    print(f"{'key':<55}{'pair':<8}{'n':>4}{'prof':>5}{'WR%':>6}{'avgP':>7}{'MFE':>7}{'totP':>8}")
    print("-" * 100)
    for r in keys[:25]:
        print(f"{r['normalized_key'][:53]:<55}{r['symbol']:<8}{r['total']:>4}"
              f"{r['profitable']:>5}{_wr(r['profitable'], r['total']):>6}"
              f"{r['avg_pips'] or 0:>7}{r['avg_mfe'] or 0:>7}{r['total_pips'] or 0:>8.1f}")

    # 3. RECURRENCE
    rec = mine_recurrence(conn, pair)
    print(f"\n{'='*100}")
    print("  3. SETUP RECURRENCE — How often do winning setups reappear?")
    print(f"{'='*100}")
    print(f"{'pair':<8}{'occ':>5}{'span':>7}{'freq/wk':>8}{'prof':>5}{'WR%':>6}{'avgP':>7} key")
    print("-" * 100)
    for r in rec[:20]:
        print(f"{r['symbol']:<8}{r['occurrences']:>5}{r['span_days'] or 0:>7.0f}d"
              f"{r['freq_per_week']:>7.1f}{r['profitable']:>5}"
              f"{_wr(r['profitable'], r['occurrences']):>6}{r['avg_pips'] or 0:>7}"
              f" {r['normalized_key'][:60]}")

    # 4. DAY + SESSION
    ds = mine_day_session(conn, pair)
    print(f"\n{'='*100}")
    print("  4. BEST DAY + SESSION PER PAIR")
    print(f"{'='*100}")
    print(f"{'pair':<8}{'day':<5}{'session':<15}{'n':>5}{'prof':>5}{'WR%':>6}{'avgP':>7}{'totP':>9}{'MFE':>7}")
    print("-" * 100)
    seen = {}
    for r in ds:
        p = r["symbol"]
        seen[p] = seen.get(p, 0) + 1
        if seen[p] > 3:
            continue
        print(f"{p:<8}{r['day']:<5}{r['session']:<15}{r['total']:>5}"
              f"{r['profitable']:>5}{_wr(r['profitable'], r['total']):>6}"
              f"{r['avg_pips'] or 0:>7}{r['total_pips'] or 0:>9.1f}{r['avg_mfe'] or 0:>7}")

    # 5. CROSS-PAIR
    if not pair:
        cross = mine_cross_pair(conn)
        print(f"\n{'='*100}")
        print("  5. CROSS-PAIR PATTERNS (same setup works on 2+ pairs)")
        print(f"{'='*100}")
        print(f"{'key':<50}{'pairs':<30}{'#p':>3}{'n':>5}{'WR%':>6}{'avgP':>7}")
        print("-" * 100)
        for r in cross[:15]:
            print(f"{r['normalized_key'][:48]:<50}{r['pairs'][:28]:<30}"
                  f"{r['pair_count']:>3}{r['total']:>5}"
                  f"{_wr(r['profitable'], r['total']):>6}{r['avg_pips'] or 0:>7}")

    # 6. PRICE LEVEL SWEET SPOTS
    lvl = mine_price_levels(conn, pair)
    print(f"\n{'='*100}")
    print("  6. PRICE LEVEL SWEET SPOTS (best AR + Hunt + Confluence combos)")
    print(f"{'='*100}")
    print(f"{'pair':<8}{'dir':<5}{'AR':<10}{'hunt':<10}{'conf':<12}{'n':>4}{'prof':>5}{'WR%':>6}{'avgP':>7}{'MFE':>7}")
    print("-" * 100)
    seen = {}
    for r in lvl[:35]:
        p = r["symbol"]
        seen[p] = seen.get(p, 0) + 1
        if seen[p] > 4:
            continue
        print(f"{p:<8}{r['direction']:<5}{r['ar']:<10}{r['hunt']:<10}"
              f"{r['conf']:<12}{r['total']:>4}{r['profitable']:>5}"
              f"{_wr(r['profitable'], r['total']):>6}{r['avg_pips'] or 0:>7}{r['avg_mfe'] or 0:>7}")

    # 7. ACTIONABLE SUMMARY
    print(f"\n{'='*100}")
    print("  7. ACTIONABLE SUMMARY")
    print(f"{'='*100}")
    best = {}
    for r in fam:
        p = r["symbol"]
        if p not in best:
            wr = r["profitable"] / r["total"] if r["total"] > 0 else 0
            if wr >= 0.50 and r["total"] >= 10:
                best[p] = r
    print(f"\n  TRADE THESE (>50% profitable, n>=10):")
    print(f"  {'pair':<10}{'family':<16}{'dir':<6}{'n':>6}{'profR':>8}{'bigWR':>8}{'avgP':>8}{'totP':>10}")
    print("  " + "-" * 72)
    for p in sorted(best.keys()):
        r = best[p]
        print(f"  {p:<10}{r['setup_family']:<16}{r['direction']:<6}{r['total']:>6}"
              f"{_wr(r['profitable'], r['total']):>7}%"
              f"{_wr(r['big_wins'], r['total']):>7}%"
              f"{r['avg_pips'] or 0:>8.1f}{r['total_pips'] or 0:>10.1f}")

    print(f"\n  AVOID:")
    for r in fam:
        wr = r["profitable"] / r["total"] if r["total"] > 0 else 0
        if wr < 0.45 and r["total"] >= 10:
            print(f"    {r['symbol']} {r['direction']} — {_wr(r['profitable'], r['total'])}% "
                  f"(n={r['total']}, avg {r['avg_pips'] or 0:+.1f}p)")


def main():
    parser = argparse.ArgumentParser(description="Mine historical setups for winning patterns")
    parser.add_argument("--report", action="store_true", help="Report only, no DB writes")
    parser.add_argument("--pair", type=str, help="Filter to single pair")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    conn = _conn(DB_PATH)
    print_report(conn, args.pair)

    if not args.report:
        print(f"\n{'='*100}")
        print("  PROMOTING TO VALIDATION LIBRARY...")
        print(f"{'='*100}")
        try:
            from helix_v3.backtest.validation_library import ValidationLibrary
            lib = ValidationLibrary()
            count = lib.rebuild_from_replay(
                min_total=5, min_favorable_rate=50.0, min_symbols=1
            )
            print(f"  {count} proven setups promoted to validation library")
            print(f"  Database: {VALIDATION_DB}")
            lib.close()
        except Exception as e:
            print(f"  Error promoting: {e}")

    conn.close()


if __name__ == "__main__":
    main()
