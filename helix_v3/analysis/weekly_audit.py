"""
Weekly Audit — Archive underperformers to graveyard, keep best setups, report changes.

Run as part of the weekly report cycle or standalone:
    python -m helix_v3.analysis.weekly_audit
    python -m helix_v3.analysis.weekly_audit --graveyard     # graveyard-only report
    python -m helix_v3.analysis.weekly_audit --symbol GBPJPY # pair-specific
"""

import argparse
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Optional

VALIDATION_DB = Path("logs/validation_library.db")


def audit(min_total: int = 5, min_favorable_rate: float = 50.0) -> str:
    """Rebuild validation library, archive dropped setups, report changes."""
    # Snapshot current state
    before = _snapshot()

    # Rebuild — this now archives dropped setups to setup_graveyard
    from helix_v3.backtest.validation_library import ValidationLibrary
    lib = ValidationLibrary()
    count = lib.rebuild_from_replay(
        min_total=min_total,
        min_favorable_rate=min_favorable_rate,
        min_symbols=1,
    )

    # Compare
    after = _snapshot()

    added = set(after.keys()) - set(before.keys())
    removed = set(before.keys()) - set(after.keys())
    changed = {
        k for k in set(before.keys()) & set(after.keys())
        if abs(before[k]["favorable_rate"] - after[k]["favorable_rate"]) > 2.0
    }

    # Graveyard stats
    grave_total = lib._conn.execute("SELECT COUNT(*) FROM setup_graveyard").fetchone()[0]
    grave_repeat = lib._conn.execute(
        "SELECT COUNT(*) FROM setup_graveyard WHERE times_demoted >= 2"
    ).fetchone()[0]
    grave_worst = lib._conn.execute(
        """SELECT symbol, direction, normalized_key, favorable_rate, times_demoted,
                  peak_favorable_rate
           FROM setup_graveyard
           ORDER BY times_demoted DESC, favorable_rate ASC
           LIMIT 5"""
    ).fetchall()

    lib.close()

    lines = [
        "HELIX V3 WEEKLY AUDIT",
        f"{'='*60}",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M EAT')}",
        f"",
        f"Validation library: {count} proven setups",
        f"Added:   {len(added)} | Removed: {len(removed)} | Changed: {len(changed)}",
        f"Graveyard: {grave_total} archived | {grave_repeat} repeat offenders",
    ]

    if added:
        lines.append(f"\nNEW PROVEN SETUPS:")
        for k in sorted(added)[:10]:
            r = after[k]
            lines.append(f"  {r['symbol']:<8} {r['direction']:<5} fav={r['favorable_rate']:.0f}% "
                         f"n={r['total']} key={r['normalized_key'][:50]}")

    if removed:
        lines.append(f"\nARCHIVED TO GRAVEYARD:")
        for k in sorted(removed)[:10]:
            r = before[k]
            lines.append(f"  {r['symbol']:<8} {r['direction']:<5} fav={r['favorable_rate']:.0f}% "
                         f"n={r['total']} key={r['normalized_key'][:50]}")

    if changed:
        lines.append(f"\nSIGNIFICANT CHANGES:")
        for k in sorted(changed)[:10]:
            b, a = before[k], after[k]
            delta = a["favorable_rate"] - b["favorable_rate"]
            lines.append(f"  {a['symbol']:<8} {delta:+.1f}% ({b['favorable_rate']:.0f}% -> {a['favorable_rate']:.0f}%) "
                         f"key={a['normalized_key'][:50]}")

    if grave_worst:
        lines.append(f"\nWORST GRAVEYARD OFFENDERS:")
        for r in grave_worst:
            sym = r[0] or "CROSS"
            peak = r[4] or r[3]
            lines.append(f"  {sym:<8} {r[1]:<5} fav={r[3]:.0f}% peak={peak:.0f}% "
                         f"demoted={r[4]}x key={r[2][:45]}")

    # Top 5 best active setups
    top = sorted(after.values(), key=lambda x: (-x["favorable_rate"], -x["total"]))[:5]
    lines.append(f"\nTOP 5 ACTIVE SETUPS:")
    for r in top:
        lines.append(f"  {r['symbol']:<8} {r['direction']:<5} fav={r['favorable_rate']:.0f}% "
                     f"n={r['total']} score={r['confidence_score']:.0f} "
                     f"key={r['normalized_key'][:50]}")

    return "\n".join(lines)


def graveyard_report(symbol: Optional[str] = None, limit: int = 50) -> str:
    """Standalone graveyard report without triggering a rebuild."""
    from helix_v3.backtest.validation_library import ValidationLibrary
    lib = ValidationLibrary()
    report = lib.graveyard_report(symbol=symbol, limit=limit)
    lib.close()
    return report


def _snapshot() -> dict:
    """Snapshot current validation library as {composite_key: row_dict}."""
    if not VALIDATION_DB.exists():
        return {}
    conn = sqlite3.connect(str(VALIDATION_DB))
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM validation_setups").fetchall()
    conn.close()
    result = {}
    for r in rows:
        d = dict(r)
        key = f"{d.get('symbol', '')}|{d.get('direction', '')}|{d.get('normalized_key', '')}"
        result[key] = d
    return result


def main():
    parser = argparse.ArgumentParser(description="Weekly audit of validation library")
    parser.add_argument("--graveyard", action="store_true", help="Show graveyard report only")
    parser.add_argument("--symbol", type=str, help="Filter to single pair")
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    if args.graveyard:
        print(graveyard_report(symbol=args.symbol, limit=args.limit))
    else:
        print(audit())


if __name__ == "__main__":
    main()
