"""Validation library for historically proven MMM setup signatures."""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from config.settings import settings
from helix_v3.backtest.mmm_event_replay import (
    DEFAULT_DB_PATH,
    ReplaySetup,
    build_setup_signature,
)
from helix_v3.utils.logger import get_logger

logger = get_logger("validation_library")

DEFAULT_LIBRARY_DB_PATH = Path(settings.log_dir) / "validation_library.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS validation_setups (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at          TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at          TEXT NOT NULL,

    scope               TEXT NOT NULL,
    symbol              TEXT NOT NULL DEFAULT '',
    direction           TEXT NOT NULL DEFAULT '',
    normalized_key      TEXT NOT NULL,
    setup_family        TEXT NOT NULL,
    primary_theme       TEXT,
    symbols             TEXT NOT NULL,

    total               INTEGER NOT NULL,
    favorable           INTEGER NOT NULL,
    favorable_rate      REAL NOT NULL,
    t1_rate             REAL NOT NULL,
    avg_exit_pips       REAL,
    avg_mfe             REAL,
    avg_mae             REAL,
    realistic_target_pips REAL,
    confidence_score    REAL NOT NULL,

    entry_rules         TEXT NOT NULL,
    exit_rules          TEXT NOT NULL,
    example_source_ids  TEXT NOT NULL,

    UNIQUE(scope, symbol, direction, normalized_key)
);

CREATE INDEX IF NOT EXISTS idx_validation_key ON validation_setups(normalized_key);
CREATE INDEX IF NOT EXISTS idx_validation_symbol ON validation_setups(symbol, direction);
CREATE INDEX IF NOT EXISTS idx_validation_score ON validation_setups(confidence_score);
"""

FAVORABLE_OUTCOMES = {"TARGET_2", "TRAIL_STOP", "TIME_EXIT_PROFIT", "OPEN_PROFIT"}


@dataclass(frozen=True)
class ValidationRecord:
    scope: str
    symbol: str
    direction: str
    normalized_key: str
    setup_family: str
    primary_theme: str
    symbols: list[str]
    total: int
    favorable: int
    favorable_rate: float
    t1_rate: float
    avg_exit_pips: Optional[float]
    avg_mfe: Optional[float]
    avg_mae: Optional[float]
    realistic_target_pips: Optional[float]
    confidence_score: float
    entry_rules: dict[str, Any]
    exit_rules: dict[str, Any]
    example_source_ids: list[int]

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


class ValidationLibrary:
    """SQLite-backed library of historically validated MMM setup signatures."""

    def __init__(
        self,
        *,
        db_path: Optional[Path] = None,
        replay_db_path: Optional[Path] = None,
    ) -> None:
        self._db_path = db_path or DEFAULT_LIBRARY_DB_PATH
        self._replay_db_path = replay_db_path or DEFAULT_DB_PATH
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self._db_path))
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.executescript(SCHEMA)
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    def rebuild_from_replay(
        self,
        *,
        min_total: int = 5,
        min_favorable_rate: float = 55.0,
        min_avg_exit_pips: float = 0.0,
        min_symbols: int = 2,
    ) -> int:
        self._conn.execute("DELETE FROM validation_setups")
        self._conn.commit()
        return self.promote_from_replay(
            min_total=min_total,
            min_favorable_rate=min_favorable_rate,
            min_avg_exit_pips=min_avg_exit_pips,
            min_symbols=min_symbols,
        )

    def promote_from_replay(
        self,
        *,
        min_total: int = 5,
        min_favorable_rate: float = 55.0,
        min_avg_exit_pips: float = 0.0,
        min_symbols: int = 2,
    ) -> int:
        replay_conn = sqlite3.connect(str(self._replay_db_path))
        replay_conn.row_factory = sqlite3.Row
        try:
            records = self._build_pair_records(
                replay_conn,
                min_total=min_total,
                min_favorable_rate=min_favorable_rate,
                min_avg_exit_pips=min_avg_exit_pips,
            )
            records.extend(
                self._build_cross_pair_records(
                    replay_conn,
                    min_total=min_total,
                    min_favorable_rate=min_favorable_rate,
                    min_avg_exit_pips=min_avg_exit_pips,
                    min_symbols=min_symbols,
                )
            )
        finally:
            replay_conn.close()

        for record in records:
            self.upsert(record)
        return len(records)

    def upsert(self, record: ValidationRecord) -> None:
        self._conn.execute(
            """INSERT INTO validation_setups (
                updated_at, scope, symbol, direction, normalized_key, setup_family,
                primary_theme, symbols, total, favorable, favorable_rate, t1_rate,
                avg_exit_pips, avg_mfe, avg_mae, realistic_target_pips,
                confidence_score, entry_rules, exit_rules, example_source_ids
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(scope, symbol, direction, normalized_key) DO UPDATE SET
                updated_at = excluded.updated_at,
                setup_family = excluded.setup_family,
                primary_theme = excluded.primary_theme,
                symbols = excluded.symbols,
                total = excluded.total,
                favorable = excluded.favorable,
                favorable_rate = excluded.favorable_rate,
                t1_rate = excluded.t1_rate,
                avg_exit_pips = excluded.avg_exit_pips,
                avg_mfe = excluded.avg_mfe,
                avg_mae = excluded.avg_mae,
                realistic_target_pips = excluded.realistic_target_pips,
                confidence_score = excluded.confidence_score,
                entry_rules = excluded.entry_rules,
                exit_rules = excluded.exit_rules,
                example_source_ids = excluded.example_source_ids""",
            (
                datetime.now(timezone.utc).isoformat(),
                record.scope,
                record.symbol,
                record.direction,
                record.normalized_key,
                record.setup_family,
                record.primary_theme,
                json.dumps(record.symbols),
                record.total,
                record.favorable,
                record.favorable_rate,
                record.t1_rate,
                record.avg_exit_pips,
                record.avg_mfe,
                record.avg_mae,
                record.realistic_target_pips,
                record.confidence_score,
                json.dumps(record.entry_rules, sort_keys=True),
                json.dumps(record.exit_rules, sort_keys=True),
                json.dumps(record.example_source_ids),
            ),
        )
        self._conn.commit()

    def validate_setup(self, setup: ReplaySetup) -> list[ValidationRecord]:
        signature = build_setup_signature(setup)
        rows = self._conn.execute(
            """SELECT * FROM validation_setups
            WHERE normalized_key = ?
              AND direction = ?
              AND (
                  (scope = 'PAIR' AND symbol = ?)
                  OR scope = 'CROSS_PAIR'
              )
            ORDER BY scope = 'PAIR' DESC, confidence_score DESC""",
            (signature.normalized_key, setup.direction.value, setup.symbol),
        ).fetchall()
        return [self._row_to_record(row) for row in rows]

    def top_records(
        self,
        *,
        scope: Optional[str] = None,
        symbol: Optional[str] = None,
        limit: int = 50,
    ) -> list[ValidationRecord]:
        clauses: list[str] = []
        params: list[Any] = []
        if scope:
            clauses.append("scope = ?")
            params.append(scope)
        if symbol:
            clauses.append("(symbol = ? OR symbols LIKE ?)")
            params.extend([symbol, f"%{symbol}%"])
        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        params.append(limit)
        rows = self._conn.execute(
            f"""SELECT * FROM validation_setups
            {where}
            ORDER BY confidence_score DESC, favorable_rate DESC, total DESC
            LIMIT ?""",
            params,
        ).fetchall()
        return [self._row_to_record(row) for row in rows]

    def report(
        self,
        *,
        scope: Optional[str] = None,
        symbol: Optional[str] = None,
        limit: int = 50,
    ) -> str:
        records = self.top_records(scope=scope, symbol=symbol, limit=limit)
        if not records:
            return "No validation-library records promoted yet."
        lines = [
            "",
            "=" * 128,
            "  HELIX V3 VALIDATION LIBRARY",
            "=" * 128,
            f"  {'Scope':<10} {'Symbol':<8} {'N':>5} {'Fav%':>7} {'T1%':>7} "
            f"{'AvgExit':>9} {'Target':>9} {'Score':>7} Setup",
            "-" * 128,
        ]
        for record in records:
            symbol_text = record.symbol or ",".join(record.symbols)[:8]
            lines.append(
                f"  {record.scope:<10} {symbol_text:<8} {record.total:>5} "
                f"{record.favorable_rate:>6.1f}% {record.t1_rate:>6.1f}% "
                f"{_fmt(record.avg_exit_pips):>9} {_fmt(record.realistic_target_pips):>9} "
                f"{record.confidence_score:>6.1f} {record.normalized_key}"
            )
        lines.append("=" * 128)
        return "\n".join(lines)

    def _build_pair_records(
        self,
        replay_conn: sqlite3.Connection,
        *,
        min_total: int,
        min_favorable_rate: float,
        min_avg_exit_pips: float,
    ) -> list[ValidationRecord]:
        rows = replay_conn.execute(
            """SELECT
                s.symbol,
                s.direction,
                s.normalized_key,
                s.setup_family,
                s.primary_theme,
                COUNT(*) AS total,
                SUM(CASE WHEN o.outcome IN ('TARGET_2', 'TRAIL_STOP',
                    'TIME_EXIT_PROFIT', 'OPEN_PROFIT') THEN 1 ELSE 0 END) AS favorable,
                SUM(CASE WHEN o.t1_hit = 1 THEN 1 ELSE 0 END) AS t1_hits,
                AVG(o.exit_pips) AS avg_exit_pips,
                AVG(o.max_favorable_pips) AS avg_mfe,
                AVG(o.max_adverse_pips) AS avg_mae,
                GROUP_CONCAT(o.source_id) AS source_ids
            FROM mmm_setup_signatures s
            JOIN mmm_event_outcomes o
              ON o.source = s.source AND o.source_id = s.source_id
            GROUP BY s.symbol, s.direction, s.normalized_key, s.setup_family, s.primary_theme
            HAVING total >= ?""",
            (min_total,),
        ).fetchall()
        return [
            record for row in rows
            if (
                record := self._record_from_stats(
                    row,
                    scope="PAIR",
                    symbols=[str(row["symbol"])],
                )
            )
            and record.favorable_rate >= min_favorable_rate
            and (record.avg_exit_pips or 0.0) >= min_avg_exit_pips
        ]

    def _build_cross_pair_records(
        self,
        replay_conn: sqlite3.Connection,
        *,
        min_total: int,
        min_favorable_rate: float,
        min_avg_exit_pips: float,
        min_symbols: int,
    ) -> list[ValidationRecord]:
        rows = replay_conn.execute(
            """SELECT
                '' AS symbol,
                s.direction,
                s.normalized_key,
                s.setup_family,
                s.primary_theme,
                COUNT(*) AS total,
                GROUP_CONCAT(DISTINCT s.symbol) AS symbols,
                SUM(CASE WHEN o.outcome IN ('TARGET_2', 'TRAIL_STOP',
                    'TIME_EXIT_PROFIT', 'OPEN_PROFIT') THEN 1 ELSE 0 END) AS favorable,
                SUM(CASE WHEN o.t1_hit = 1 THEN 1 ELSE 0 END) AS t1_hits,
                AVG(o.exit_pips) AS avg_exit_pips,
                AVG(o.max_favorable_pips) AS avg_mfe,
                AVG(o.max_adverse_pips) AS avg_mae,
                GROUP_CONCAT(o.source_id) AS source_ids
            FROM mmm_setup_signatures s
            JOIN mmm_event_outcomes o
              ON o.source = s.source AND o.source_id = s.source_id
            GROUP BY s.direction, s.normalized_key, s.setup_family, s.primary_theme
            HAVING total >= ?""",
            (min_total,),
        ).fetchall()
        records: list[ValidationRecord] = []
        for row in rows:
            symbols = sorted(set(str(row["symbols"] or "").split(",")) - {""})
            if len(symbols) < min_symbols:
                continue
            record = self._record_from_stats(row, scope="CROSS_PAIR", symbols=symbols)
            if (
                record
                and record.favorable_rate >= min_favorable_rate
                and (record.avg_exit_pips or 0.0) >= min_avg_exit_pips
            ):
                records.append(record)
        return records

    def _record_from_stats(
        self,
        row: sqlite3.Row,
        *,
        scope: str,
        symbols: list[str],
    ) -> Optional[ValidationRecord]:
        total = int(row["total"] or 0)
        if total <= 0:
            return None
        favorable = int(row["favorable"] or 0)
        favorable_rate = favorable / total * 100.0
        t1_rate = int(row["t1_hits"] or 0) / total * 100.0
        avg_exit = _optional_float(row["avg_exit_pips"])
        avg_mfe = _optional_float(row["avg_mfe"])
        avg_mae = _optional_float(row["avg_mae"])
        target = _realistic_target(avg_exit, avg_mfe, t1_rate)
        confidence = _confidence_score(
            favorable_rate=favorable_rate,
            t1_rate=t1_rate,
            avg_exit_pips=avg_exit,
            avg_mae=avg_mae,
            total=total,
        )
        normalized_key = str(row["normalized_key"])
        direction = str(row["direction"] or "")
        source_ids = [
            int(value) for value in str(row["source_ids"] or "").split(",")
            if value.strip().isdigit()
        ][:20]
        return ValidationRecord(
            scope=scope,
            symbol=str(row["symbol"] or ""),
            direction=direction,
            normalized_key=normalized_key,
            setup_family=str(row["setup_family"] or ""),
            primary_theme=str(row["primary_theme"] or ""),
            symbols=symbols,
            total=total,
            favorable=favorable,
            favorable_rate=favorable_rate,
            t1_rate=t1_rate,
            avg_exit_pips=avg_exit,
            avg_mfe=avg_mfe,
            avg_mae=avg_mae,
            realistic_target_pips=target,
            confidence_score=confidence,
            entry_rules=_entry_rules_from_key(normalized_key, direction, symbols),
            exit_rules=_exit_rules(target),
            example_source_ids=source_ids,
        )

    def _row_to_record(self, row: sqlite3.Row) -> ValidationRecord:
        return ValidationRecord(
            scope=str(row["scope"]),
            symbol=str(row["symbol"] or ""),
            direction=str(row["direction"] or ""),
            normalized_key=str(row["normalized_key"]),
            setup_family=str(row["setup_family"] or ""),
            primary_theme=str(row["primary_theme"] or ""),
            symbols=_load_json_list(row["symbols"]),
            total=int(row["total"]),
            favorable=int(row["favorable"]),
            favorable_rate=float(row["favorable_rate"]),
            t1_rate=float(row["t1_rate"]),
            avg_exit_pips=_optional_float(row["avg_exit_pips"]),
            avg_mfe=_optional_float(row["avg_mfe"]),
            avg_mae=_optional_float(row["avg_mae"]),
            realistic_target_pips=_optional_float(row["realistic_target_pips"]),
            confidence_score=float(row["confidence_score"]),
            entry_rules=_load_json_dict(row["entry_rules"]),
            exit_rules=_load_json_dict(row["exit_rules"]),
            example_source_ids=[
                int(value) for value in _load_json_list(row["example_source_ids"])
                if str(value).isdigit()
            ],
        )


def _entry_rules_from_key(normalized_key: str, direction: str, symbols: list[str]) -> dict[str, Any]:
    parts = normalized_key.split("|")
    return {
        "direction": direction,
        "symbols": symbols,
        "normalized_key": normalized_key,
        "setup_family": parts[0] if parts else "",
        "weekly_phase": _part(parts, 2),
        "h4_level": _part(parts, 3),
        "h1_session": _part(parts, 4),
        "asian_range_bucket": _part(parts, 5),
        "hunt_bucket": _part(parts, 6),
        "push_bucket": _part(parts, 7),
        "mw_pattern": _part(parts, 8),
        "rrt_state": _part(parts, 9),
        "tdi_state": _part(parts, 10),
        "pattern_state": _part(parts, 11),
    }


def _exit_rules(target_pips: Optional[float]) -> dict[str, Any]:
    return {
        "target_pips": target_pips,
        "management": "T1 at 1R, move SL to breakeven, trail only while in profit",
        "stale_exit": "90 minutes only if not in profit",
    }


def _realistic_target(
    avg_exit_pips: Optional[float],
    avg_mfe: Optional[float],
    t1_rate: float,
) -> Optional[float]:
    if avg_mfe is None:
        return avg_exit_pips
    factor = 0.65 if t1_rate >= 50.0 else 0.45
    target = avg_mfe * factor
    if avg_exit_pips is not None and avg_exit_pips > 0:
        target = max(target, avg_exit_pips)
    return max(0.0, target)


def _confidence_score(
    *,
    favorable_rate: float,
    t1_rate: float,
    avg_exit_pips: Optional[float],
    avg_mae: Optional[float],
    total: int,
) -> float:
    exit_component = min(20.0, max(0.0, (avg_exit_pips or 0.0) * 2.0))
    mae_penalty = min(15.0, max(0.0, (avg_mae or 0.0) * 0.5))
    sample_bonus = min(10.0, total)
    return max(
        0.0,
        min(100.0, favorable_rate * 0.55 + t1_rate * 0.25 + exit_component + sample_bonus - mae_penalty),
    )


def _part(parts: list[str], index: int) -> str:
    return parts[index] if index < len(parts) else ""


def _optional_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _load_json_list(value: Any) -> list[str]:
    try:
        parsed = json.loads(str(value or "[]"))
    except json.JSONDecodeError:
        return []
    if not isinstance(parsed, list):
        return []
    return [str(item) for item in parsed]


def _load_json_dict(value: Any) -> dict[str, Any]:
    try:
        parsed = json.loads(str(value or "{}"))
    except json.JSONDecodeError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _fmt(value: Any) -> str:
    return "-" if value is None else f"{float(value):+.1f}"


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="MMM validation-library builder")
    sub = parser.add_subparsers(dest="command", required=True)

    p_promote = sub.add_parser("promote", help="Promote proven replay signatures")
    p_promote.add_argument("--min-total", type=int, default=5)
    p_promote.add_argument("--min-favorable-rate", type=float, default=55.0)
    p_promote.add_argument("--min-avg-exit-pips", type=float, default=0.0)
    p_promote.add_argument("--min-symbols", type=int, default=2)

    p_rebuild = sub.add_parser(
        "rebuild",
        help="Clear validation records and rebuild from replay signatures",
    )
    p_rebuild.add_argument("--min-total", type=int, default=5)
    p_rebuild.add_argument("--min-favorable-rate", type=float, default=55.0)
    p_rebuild.add_argument("--min-avg-exit-pips", type=float, default=0.0)
    p_rebuild.add_argument("--min-symbols", type=int, default=2)

    p_report = sub.add_parser("report", help="Show validation-library records")
    p_report.add_argument("--scope", choices=("PAIR", "CROSS_PAIR"))
    p_report.add_argument("--symbol")
    p_report.add_argument("--limit", type=int, default=50)

    args = parser.parse_args(argv)
    library = ValidationLibrary()
    try:
        if args.command == "promote":
            count = library.promote_from_replay(
                min_total=args.min_total,
                min_favorable_rate=args.min_favorable_rate,
                min_avg_exit_pips=args.min_avg_exit_pips,
                min_symbols=args.min_symbols,
            )
            print(f"Promoted/reused {count} validation records.")
        elif args.command == "rebuild":
            count = library.rebuild_from_replay(
                min_total=args.min_total,
                min_favorable_rate=args.min_favorable_rate,
                min_avg_exit_pips=args.min_avg_exit_pips,
                min_symbols=args.min_symbols,
            )
            print(f"Rebuilt validation library with {count} records.")
        elif args.command == "report":
            print(library.report(scope=args.scope, symbol=args.symbol, limit=args.limit))
    finally:
        library.close()


if __name__ == "__main__":
    main()
