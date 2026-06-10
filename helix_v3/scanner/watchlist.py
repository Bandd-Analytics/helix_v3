"""Scanner-first watchlist alerts with promotion gates.

This module is alert-only. It reads scanner snapshots from SQLite and never
places, modifies, or closes MT5 orders.
"""

from __future__ import annotations

import argparse
import os
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable, Optional

from config.pair_profiles import get_pair_profile
from helix_v3.backtest.scanner_replay import (
    SCANNER_DB_PATH,
    ScannerCandidate,
    baseline_direction,
)
from helix_v3.backtest.setup_intelligence import DEFAULT_INTELLIGENCE_DB_PATH
from helix_v3.backtest.validation_library import ValidationLibrary, ValidationRecord
from helix_v3.core.types import Direction

EAT = timezone(timedelta(hours=3))
DEFAULT_ALERT_SYMBOLS = (
    "EURUSD",
    "GBPUSD",
    "GBPJPY",
    "USDJPY",
    "EURJPY",
    "GBPCHF",
    "AUDUSD",
    "GBPAUD",
    "GBPNZD",
    "EURGBP",
    "XAUUSD",
    "US30",
    "USTEC",
)


@dataclass(frozen=True)
class WatchlistConfig:
    symbols: list[str] = field(default_factory=lambda: list(DEFAULT_ALERT_SYMBOLS))
    timeframe: str = "M15"
    min_readiness: int = 70
    max_age_minutes: int = 180
    baseline_policy: str = "stop_hunt_then_bias"
    require_stop_hunt: bool = False
    allow_analysis_only_pairs: bool = True
    require_exact_validation: bool = True
    min_validation_score: float = 0.0
    historical_match_limit: int = 3
    historical_min_total: int = 10
    require_alert_basket: bool = False
    alert_basket_limit: int = 30
    alert_basket_modes: tuple[str, ...] = (
        "DEMO_ALERT",
        "WATCH_ALERT",
        "ASYM_WATCH",
        "RESEARCH_ONLY",
    )
    limit: int = 10


@dataclass(frozen=True)
class ScannerAlertCandidate:
    scanner: ScannerCandidate
    normalized_key: str = ""


@dataclass(frozen=True)
class HistoricalSetupMatch:
    symbol: str
    direction: str
    normalized_key: str
    total: int
    favorable_rate: float
    avg_exit_pips: Optional[float]
    fast_profit_rate: float
    recurrence_per_30d: float
    reappearance_score: float
    opportunity_score: float
    decision: str
    top_session: str
    top_day: str
    top_price_level: str
    rrs_grade: str = ""
    expectancy_tier: str = ""
    profit_factor: Optional[float] = None
    payoff_ratio: Optional[float] = None
    split_passes: Optional[int] = None
    basket_rank: Optional[int] = None
    basket_mode: str = ""


@dataclass(frozen=True)
class ScannerWatchlistItem:
    symbol: str
    timeframe: str
    scan_time: datetime
    direction: Direction
    status: str
    readiness: int
    spread_pips: float
    validation_matches: int
    historical_matches: list[HistoricalSetupMatch]
    blockers: list[str]
    notes: str

    @property
    def is_promoted_entry(self) -> bool:
        return self.status == "PROMOTED_ENTRY"

    @property
    def is_watch_only(self) -> bool:
        return self.status == "WATCH_ONLY"


def config_from_env() -> WatchlistConfig:
    return WatchlistConfig(
        symbols=_parse_symbols(
            os.getenv("SCANNER_ALERT_SYMBOLS", ",".join(DEFAULT_ALERT_SYMBOLS))
        ),
        timeframe=os.getenv("SCANNER_ALERT_TIMEFRAME", "M15"),
        min_readiness=int(os.getenv("SCANNER_ALERT_MIN_READINESS", "70")),
        max_age_minutes=int(os.getenv("SCANNER_ALERT_MAX_AGE_MINUTES", "180")),
        baseline_policy=os.getenv("SCANNER_ALERT_POLICY", "stop_hunt_then_bias"),
        require_stop_hunt=_parse_bool(os.getenv("SCANNER_ALERT_REQUIRE_STOP_HUNT", "false")),
        allow_analysis_only_pairs=_parse_bool(
            os.getenv("SCANNER_ALERT_ALLOW_ANALYSIS_ONLY_PAIRS", "true")
        ),
        require_exact_validation=_parse_bool(
            os.getenv("SCANNER_ALERT_REQUIRE_EXACT_VALIDATION", "true")
        ),
        min_validation_score=float(os.getenv("SCANNER_ALERT_MIN_VALIDATION_SCORE", "0")),
        historical_match_limit=int(os.getenv("SCANNER_ALERT_HISTORICAL_MATCH_LIMIT", "3")),
        historical_min_total=int(os.getenv("SCANNER_ALERT_HISTORICAL_MIN_TOTAL", "10")),
        require_alert_basket=_parse_bool(
            os.getenv("SCANNER_ALERT_REQUIRE_BASKET", "false")
        ),
        alert_basket_limit=int(os.getenv("SCANNER_ALERT_BASKET_LIMIT", "30")),
        alert_basket_modes=tuple(
            _parse_symbols(
                os.getenv(
                    "SCANNER_ALERT_BASKET_MODES",
                    "DEMO_ALERT,WATCH_ALERT,ASYM_WATCH,RESEARCH_ONLY",
                )
            )
        ),
        limit=int(os.getenv("SCANNER_ALERT_LIMIT", "10")),
    )


class ScannerWatchlist:
    """Build a gated watchlist from stored scanner snapshots."""

    def __init__(
        self,
        *,
        scanner_db_path: Optional[Path] = None,
        intelligence_db_path: Optional[Path] = None,
        validation_library: Optional[ValidationLibrary] = None,
    ) -> None:
        self._scanner_db_path = scanner_db_path or SCANNER_DB_PATH
        self._intelligence_db_path = intelligence_db_path or DEFAULT_INTELLIGENCE_DB_PATH
        self._validation_library = validation_library
        self._owns_validation_library = False
        if self._validation_library is None:
            self._validation_library = ValidationLibrary()
            self._owns_validation_library = True

    def close(self) -> None:
        if self._validation_library and self._owns_validation_library:
            self._validation_library.close()

    def latest_candidates(self, config: WatchlistConfig) -> list[ScannerAlertCandidate]:
        if not self._scanner_db_path.exists():
            return []

        conn = sqlite3.connect(str(self._scanner_db_path))
        conn.row_factory = sqlite3.Row
        try:
            table_exists = conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'market_scans'"
            ).fetchone()
            if not table_exists:
                return []

            clauses = ["timeframe = ?"]
            params: list[object] = [config.timeframe]
            if config.symbols:
                placeholders = ", ".join("?" for _ in config.symbols)
                clauses.append(f"symbol IN ({placeholders})")
                params.extend(config.symbols)

            where = " AND ".join(clauses)
            sql = f"""SELECT * FROM market_scans
            WHERE id IN (
                SELECT MAX(id) FROM market_scans
                WHERE {where}
                GROUP BY symbol, timeframe
            )
            ORDER BY trade_readiness DESC, scan_time DESC
            LIMIT ?"""
            rows = conn.execute(sql, [*params, config.limit]).fetchall()
            return [_alert_candidate_from_row(row) for row in rows]
        finally:
            conn.close()

    def build(
        self,
        config: WatchlistConfig,
        *,
        now: Optional[datetime] = None,
    ) -> list[ScannerWatchlistItem]:
        current_time = _to_utc(now or datetime.now(timezone.utc))
        candidates = self.latest_candidates(config)
        return [
            evaluate_candidate(
                candidate,
                config,
                validation_records=self._validation_records(candidate, config),
                historical_matches=self._historical_matches(candidate, config),
                now=current_time,
            )
            for candidate in candidates
        ]

    def _validation_records(
        self,
        candidate: ScannerAlertCandidate,
        config: WatchlistConfig,
    ) -> list[ValidationRecord]:
        if not self._validation_library:
            return []

        direction = baseline_direction(candidate.scanner, policy=config.baseline_policy)
        if direction == Direction.NEUTRAL:
            return []

        records = self._validation_library.top_records(
            symbol=candidate.scanner.symbol,
            limit=50,
        )
        records = [
            record
            for record in records
            if record.direction == direction.value
            and record.confidence_score >= config.min_validation_score
        ]
        if config.require_exact_validation:
            if not candidate.normalized_key:
                return []
            records = [
                record for record in records if record.normalized_key == candidate.normalized_key
            ]
        return records

    def _historical_matches(
        self,
        candidate: ScannerAlertCandidate,
        config: WatchlistConfig,
    ) -> list[HistoricalSetupMatch]:
        if config.historical_match_limit <= 0 or not self._intelligence_db_path.exists():
            return []

        direction = baseline_direction(candidate.scanner, policy=config.baseline_policy)
        if direction == Direction.NEUTRAL:
            return []

        if config.require_alert_basket:
            return self._alert_basket_matches(candidate, config, direction)

        conn = sqlite3.connect(str(self._intelligence_db_path))
        conn.row_factory = sqlite3.Row
        try:
            table_exists = conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'setup_stats'"
            ).fetchone()
            if not table_exists:
                return []
            expectancy_exists = conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'expectancy_candidates'"
            ).fetchone()
            select_sql = (
                """ss.*, ec.candidate_tier, ec.profit_factor, ec.payoff_ratio,
                   ec.split_passes"""
                if expectancy_exists
                else """ss.*, NULL AS candidate_tier, NULL AS profit_factor,
                   NULL AS payoff_ratio, NULL AS split_passes"""
            )
            join_sql = (
                """LEFT JOIN expectancy_candidates ec
                   ON ec.symbol = ss.symbol
                  AND ec.direction = ss.direction
                  AND ec.normalized_key = ss.normalized_key"""
                if expectancy_exists
                else ""
            )
            tier_order_sql = (
                """CASE ec.candidate_tier
                        WHEN 'DEMO_CANDIDATE' THEN 0
                        WHEN 'ASYMMETRIC_EXCEPTION' THEN 1
                        WHEN 'WATCH_CANDIDATE' THEN 2
                        ELSE 3
                    END,"""
                if expectancy_exists
                else ""
            )

            exact_matches: list[HistoricalSetupMatch] = []
            if candidate.normalized_key:
                exact_rows = conn.execute(
                    f"""SELECT {select_sql}
                    FROM setup_stats ss
                    {join_sql}
                    WHERE ss.symbol = ? AND ss.direction = ? AND ss.normalized_key = ?
                      AND ss.total >= ?
                    LIMIT ?""",
                    (
                        candidate.scanner.symbol,
                        direction.value,
                        candidate.normalized_key,
                        config.historical_min_total,
                        config.historical_match_limit,
                    ),
                ).fetchall()
                exact_matches = [_historical_match_from_row(row) for row in exact_rows]

            remaining = max(0, config.historical_match_limit - len(exact_matches))
            if remaining <= 0:
                return exact_matches

            rows = conn.execute(
                f"""SELECT {select_sql}
                FROM setup_stats ss
                {join_sql}
                WHERE ss.symbol = ? AND ss.direction = ? AND ss.total >= ?
                ORDER BY
                    {tier_order_sql}
                    CASE ss.decision
                        WHEN 'PROMOTE_CANDIDATE' THEN 0
                        WHEN 'WATCH_RESEARCH' THEN 1
                        ELSE 2
                    END,
                    ss.opportunity_score DESC,
                    ss.favorable_rate DESC,
                    ss.avg_exit_pips DESC
                LIMIT ?""",
                (
                    candidate.scanner.symbol,
                    direction.value,
                    config.historical_min_total,
                    remaining,
                ),
            ).fetchall()
            matches = [*exact_matches, *[_historical_match_from_row(row) for row in rows]]
            return _dedupe_historical_matches(matches, limit=config.historical_match_limit)
        finally:
            conn.close()

    def _alert_basket_matches(
        self,
        candidate: ScannerAlertCandidate,
        config: WatchlistConfig,
        direction: Direction,
    ) -> list[HistoricalSetupMatch]:
        conn = sqlite3.connect(str(self._intelligence_db_path))
        conn.row_factory = sqlite3.Row
        try:
            table_exists = conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'expectancy_candidates'"
            ).fetchone()
            if not table_exists:
                return []
            rows = conn.execute(
                """SELECT *
                FROM expectancy_candidates
                ORDER BY CASE candidate_tier
                    WHEN 'DEMO_CANDIDATE' THEN 0
                    WHEN 'ASYMMETRIC_EXCEPTION' THEN 1
                    ELSE 2
                END,
                CASE rrs_grade
                    WHEN 'R_RUNNER' THEN 0
                    WHEN 'R_REPEATER' THEN 1
                    ELSE 2
                END,
                split_passes DESC,
                profit_factor DESC,
                payoff_ratio DESC,
                avg_exit_pips DESC,
                total DESC
                LIMIT ?""",
                (config.alert_basket_limit,),
            ).fetchall()
        finally:
            conn.close()

        allowed_modes = {mode.upper() for mode in config.alert_basket_modes}
        matches: list[HistoricalSetupMatch] = []
        for rank, row in enumerate(rows, start=1):
            if str(row["symbol"]).upper() != candidate.scanner.symbol.upper():
                continue
            if str(row["direction"]).upper() != direction.value:
                continue
            mode = _basket_mode_for_row(row)
            if allowed_modes and mode.upper() not in allowed_modes:
                continue
            matches.append(_historical_match_from_basket_row(row, rank=rank, mode=mode))
            if len(matches) >= config.historical_match_limit:
                break
        return matches


def evaluate_candidate(
    candidate: ScannerAlertCandidate,
    config: WatchlistConfig,
    *,
    validation_records: Iterable[ValidationRecord] = (),
    historical_matches: Iterable[HistoricalSetupMatch] = (),
    now: Optional[datetime] = None,
) -> ScannerWatchlistItem:
    scanner = candidate.scanner
    current_time = _to_utc(now or datetime.now(timezone.utc))
    direction = baseline_direction(scanner, policy=config.baseline_policy)
    blockers: list[str] = []

    if scanner.trade_readiness < config.min_readiness:
        blockers.append(
            f"readiness {scanner.trade_readiness} below minimum {config.min_readiness}"
        )

    age_minutes = (current_time - _to_utc(scanner.scan_time)).total_seconds() / 60.0
    if config.max_age_minutes > 0 and age_minutes > config.max_age_minutes:
        blockers.append(
            f"scan age {age_minutes:.0f}m exceeds {config.max_age_minutes}m"
        )

    profile = get_pair_profile(scanner.symbol)
    if not config.allow_analysis_only_pairs and not profile.tradeable:
        blockers.append("pair profile is analysis-only")

    if scanner.spread_pips > profile.max_spread_pips:
        blockers.append(
            f"spread {scanner.spread_pips:.1f}p exceeds pair limit {profile.max_spread_pips:.1f}p"
        )

    if direction == Direction.NEUTRAL:
        blockers.append("baseline direction is NEUTRAL")

    if config.require_stop_hunt and not scanner.stop_hunt_active:
        blockers.append("stop hunt required but not active")

    records = list(validation_records)
    historical = list(historical_matches)
    if config.require_alert_basket and not historical:
        blockers.append("no ranked alert-basket match")

    validation_blockers: list[str] = []
    if config.require_exact_validation and not candidate.normalized_key:
        validation_blockers.append("exact setup signature missing")
    if not records:
        validation_blockers.append("no promoted validation-library match")

    if blockers:
        status = "BLOCKED"
        all_blockers = [*blockers, *validation_blockers]
    elif validation_blockers:
        status = "WATCH_ONLY"
        all_blockers = validation_blockers
    else:
        status = "PROMOTED_ENTRY"
        all_blockers = []

    return ScannerWatchlistItem(
        symbol=scanner.symbol,
        timeframe=scanner.timeframe,
        scan_time=scanner.scan_time,
        direction=direction,
        status=status,
        readiness=scanner.trade_readiness,
        spread_pips=scanner.spread_pips,
        validation_matches=len(records),
        historical_matches=historical,
        blockers=all_blockers,
        notes=scanner.readiness_notes,
    )


def format_watchlist_report(
    items: Iterable[ScannerWatchlistItem],
    config: WatchlistConfig,
    *,
    generated_at: Optional[datetime] = None,
    include_blocked: bool = False,
) -> str:
    generated = (generated_at or datetime.now(timezone.utc)).astimezone(EAT)
    visible = [
        item for item in items
        if include_blocked or item.status != "BLOCKED"
    ]
    promoted = [item for item in visible if item.is_promoted_entry]
    watches = [item for item in visible if item.is_watch_only]
    blocked = [item for item in visible if item.status == "BLOCKED"]

    lines = [
        "HELIX V3 SCANNER WATCHLIST",
        f"{generated.strftime('%Y-%m-%d %H:%M EAT')}",
        "Mode: alert-only; live execution disabled",
        (
            "Entry gate: exact promoted setup"
            if config.require_exact_validation
            else "Entry gate: symbol/direction promoted setup"
        ),
        (
            f"Scope: {','.join(config.symbols) or 'all'} {config.timeframe} "
            f"ready>={config.min_readiness} age<={config.max_age_minutes}m"
        ),
        (
            "Basket gate: "
            + (
                f"top {config.alert_basket_limit} modes={','.join(config.alert_basket_modes)}"
                if config.require_alert_basket
                else "off"
            )
        ),
        "",
        f"Promoted entries: {len(promoted)} | Watch-only: {len(watches)} | Blocked shown: {len(blocked)}",
    ]

    if not visible:
        lines.extend(["", "No scanner candidates matched the current watchlist scope."])
        return "\n".join(lines)

    if promoted:
        lines.extend(["", "PROMOTED ENTRY CANDIDATES"])
        for item in promoted:
            lines.extend(_format_item_lines(item))
    else:
        lines.extend(["", "No promoted entry candidates. Do not auto-enter from this report."])

    if watches:
        lines.extend(["", "WATCH ONLY"])
        for item in watches:
            lines.extend(_format_item_lines(item))

    if blocked:
        lines.extend(["", "BLOCKED"])
        for item in blocked:
            lines.extend(_format_item_lines(item))

    return "\n".join(lines)


def notify_watchlist_report(report: str) -> bool:
    backend = os.getenv("NOTIFICATION_BACKEND", "whatsapp").lower()
    if backend == "telegram":
        from helix_v3.notifications.telegram import TelegramNotifier

        notifier = TelegramNotifier()
        if not notifier.enabled:
            print("Telegram not configured. Printing watchlist report only.")
            print(report)
            return False
        return notifier.notify_scanner_watchlist(report)

    from helix_v3.notifications.whatsapp import WhatsAppNotifier

    notifier = WhatsAppNotifier()
    if not notifier.enabled:
        print("WhatsApp not configured. Printing watchlist report only.")
        print(report)
        return False
    return notifier.notify_scanner_watchlist(report)


def _alert_candidate_from_row(row: sqlite3.Row) -> ScannerAlertCandidate:
    data = dict(row)
    normalized_key = str(data.get("normalized_key") or data.get("setup_key") or "")
    return ScannerAlertCandidate(
        scanner=ScannerCandidate.from_row(data),
        normalized_key=normalized_key,
    )


def _historical_match_from_row(row: sqlite3.Row) -> HistoricalSetupMatch:
    split_passes = _row_value(row, "split_passes")
    return HistoricalSetupMatch(
        symbol=str(row["symbol"]),
        direction=str(row["direction"]),
        normalized_key=str(row["normalized_key"]),
        total=int(row["total"] or 0),
        favorable_rate=float(row["favorable_rate"] or 0.0),
        avg_exit_pips=_optional_float(row["avg_exit_pips"]),
        fast_profit_rate=float(row["fast_profit_rate"] or 0.0),
        recurrence_per_30d=float(row["recurrence_per_30d"] or 0.0),
        reappearance_score=float(row["reappearance_score"] or 0.0),
        opportunity_score=float(row["opportunity_score"] or 0.0),
        decision=str(row["decision"] or ""),
        top_session=str(row["top_session"] or ""),
        top_day=str(row["top_day"] or ""),
        top_price_level=str(row["top_price_level"] or ""),
        rrs_grade=str(_row_value(row, "rrs_grade", "") or ""),
        expectancy_tier=str(_row_value(row, "candidate_tier", "") or ""),
        profit_factor=_optional_float(_row_value(row, "profit_factor")),
        payoff_ratio=_optional_float(_row_value(row, "payoff_ratio")),
        split_passes=int(split_passes) if split_passes is not None else None,
    )


def _historical_match_from_basket_row(
    row: sqlite3.Row,
    *,
    rank: int,
    mode: str,
) -> HistoricalSetupMatch:
    return HistoricalSetupMatch(
        symbol=str(row["symbol"]),
        direction=str(row["direction"]),
        normalized_key=str(row["normalized_key"]),
        total=int(row["total"] or 0),
        favorable_rate=float(row["favorable_rate"] or 0.0),
        avg_exit_pips=_optional_float(row["avg_exit_pips"]),
        fast_profit_rate=float(row["fast_profit_rate"] or 0.0),
        recurrence_per_30d=float(row["recurrence_per_30d"] or 0.0),
        reappearance_score=float(row["reappearance_score"] or 0.0),
        opportunity_score=float(row["opportunity_score"] or 0.0),
        decision=str(row["candidate_tier"] or ""),
        top_session=str(row["top_session"] or ""),
        top_day=str(row["top_day"] or ""),
        top_price_level=str(row["top_price_level"] or ""),
        rrs_grade=str(row["rrs_grade"] or ""),
        expectancy_tier=str(row["candidate_tier"] or ""),
        profit_factor=_optional_float(row["profit_factor"]),
        payoff_ratio=_optional_float(row["payoff_ratio"]),
        split_passes=int(row["split_passes"]) if row["split_passes"] is not None else None,
        basket_rank=rank,
        basket_mode=mode,
    )


def _basket_mode_for_row(row: sqlite3.Row) -> str:
    symbol = str(row["symbol"] or "").upper()
    try:
        profile = get_pair_profile(symbol)
    except Exception:
        return "RESEARCH_ONLY"
    if not profile.tradeable:
        return "RESEARCH_ONLY"
    tier = str(row["candidate_tier"] or "")
    if tier == "DEMO_CANDIDATE":
        return "DEMO_ALERT"
    if tier == "ASYMMETRIC_EXCEPTION":
        return "ASYM_WATCH"
    return "WATCH_ALERT"


def _dedupe_historical_matches(
    matches: Iterable[HistoricalSetupMatch],
    *,
    limit: int,
) -> list[HistoricalSetupMatch]:
    deduped: list[HistoricalSetupMatch] = []
    seen: set[str] = set()
    for match in matches:
        key = f"{match.symbol}|{match.direction}|{match.normalized_key}"
        if key in seen:
            continue
        seen.add(key)
        deduped.append(match)
        if len(deduped) >= limit:
            break
    return deduped


def _format_item_lines(item: ScannerWatchlistItem) -> list[str]:
    scan_time = item.scan_time.astimezone(EAT).strftime("%Y-%m-%d %H:%M EAT")
    lines = [
        (
            f"- {item.symbol} {item.direction.value} {item.timeframe} "
            f"ready={item.readiness}/100 spread={item.spread_pips:.1f}p "
            f"matches={item.validation_matches} scan={scan_time}"
        )
    ]
    if item.notes:
        lines.append(f"  notes: {item.notes[:120]}")
    if item.historical_matches:
        best = item.historical_matches[0]
        avg_exit = _fmt_signed(best.avg_exit_pips)
        lines.append(
            "  historical: "
            f"{best.decision} N={best.total} Fav={best.favorable_rate:.1f}% "
            f"AvgExit={avg_exit} Fast={best.fast_profit_rate:.1f}% "
            f"Recur/30d={best.recurrence_per_30d:.2f} "
            f"Reappear={best.reappearance_score:.1f} Opp={best.opportunity_score:.1f}"
        )
        context_parts = [
            part
            for part in (best.top_day, best.top_session, best.top_price_level)
            if part
        ]
        if context_parts:
            lines.append(f"  historical context: {' / '.join(context_parts)}")
        if best.expectancy_tier:
            split_text = "-" if best.split_passes is None else f"{best.split_passes}/3"
            lines.append(
                "  expectancy: "
                f"{best.expectancy_tier} RRS={best.rrs_grade or '-'} "
                f"PF={_fmt_decimal(best.profit_factor)} "
                f"Payoff={_fmt_decimal(best.payoff_ratio)} Splits={split_text}"
            )
        if best.basket_rank is not None:
            lines.append(
                f"  basket: #{best.basket_rank} {best.basket_mode or '-'}"
            )
        lines.append(f"  setup: {_short_key(best.normalized_key, 100)}")
    if item.blockers:
        lines.append(f"  gate: {'; '.join(item.blockers)}")
    return lines


def _optional_float(value: object) -> Optional[float]:
    try:
        if value is None:
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def _row_value(row: sqlite3.Row, column: str, default: object = None) -> object:
    return row[column] if column in row.keys() else default


def _fmt_signed(value: Optional[float]) -> str:
    if value is None:
        return "-"
    return f"{value:+.1f}p"


def _fmt_decimal(value: Optional[float]) -> str:
    if value is None:
        return "-"
    return f"{value:.2f}"


def _short_key(value: str, max_len: int) -> str:
    if len(value) <= max_len:
        return value
    return value[: max_len - 3] + "..."


def _parse_symbols(raw: str) -> list[str]:
    return [part.strip().upper() for part in raw.split(",") if part.strip()]


def _parse_bool(raw: str) -> bool:
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _to_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def main(argv: Optional[list[str]] = None) -> None:
    env_config = config_from_env()
    parser = argparse.ArgumentParser(
        description="Build an alert-only scanner watchlist from stored market scans"
    )
    parser.add_argument("--symbols", default=",".join(env_config.symbols))
    parser.add_argument("--timeframe", default=env_config.timeframe)
    parser.add_argument("--min-readiness", type=int, default=env_config.min_readiness)
    parser.add_argument("--max-age-minutes", type=int, default=env_config.max_age_minutes)
    parser.add_argument("--limit", type=int, default=env_config.limit)
    parser.add_argument(
        "--intelligence-db",
        type=Path,
        default=Path(os.getenv("SETUP_INTELLIGENCE_DB", str(DEFAULT_INTELLIGENCE_DB_PATH))),
        help="Read-only setup intelligence database for historical match context",
    )
    parser.add_argument(
        "--historical-match-limit",
        type=int,
        default=env_config.historical_match_limit,
    )
    parser.add_argument(
        "--historical-min-total",
        type=int,
        default=env_config.historical_min_total,
        help="Minimum historical setup sample size to show as watchdog context",
    )
    parser.add_argument(
        "--require-alert-basket",
        action="store_true",
        default=env_config.require_alert_basket,
        help="Block scanner candidates unless they match the ranked expectancy basket",
    )
    parser.add_argument(
        "--alert-basket-limit",
        type=int,
        default=env_config.alert_basket_limit,
        help="Use only the top N ranked basket rows when --require-alert-basket is set",
    )
    parser.add_argument(
        "--alert-basket-modes",
        default=",".join(env_config.alert_basket_modes),
        help="Comma-separated basket modes allowed when --require-alert-basket is set",
    )
    parser.add_argument(
        "--policy",
        default=env_config.baseline_policy,
        choices=("bias", "trend", "stop_hunt", "stop_hunt_then_bias"),
    )
    parser.add_argument(
        "--require-stop-hunt",
        action="store_true",
        default=env_config.require_stop_hunt,
    )
    parser.add_argument(
        "--block-analysis-only-pairs",
        action="store_true",
        help="Block pairs whose PairProfile is analysis-only",
    )
    parser.add_argument(
        "--allow-symbol-direction-promotion",
        action="store_true",
        help="Allow promoted entry status from symbol/direction records without exact setup keys",
    )
    parser.add_argument(
        "--min-validation-score",
        type=float,
        default=env_config.min_validation_score,
    )
    parser.add_argument("--include-blocked", action="store_true")
    parser.add_argument("--notify", action="store_true")
    args = parser.parse_args(argv)

    config = WatchlistConfig(
        symbols=_parse_symbols(args.symbols),
        timeframe=args.timeframe,
        min_readiness=args.min_readiness,
        max_age_minutes=args.max_age_minutes,
        baseline_policy=args.policy,
        require_stop_hunt=args.require_stop_hunt,
        allow_analysis_only_pairs=not args.block_analysis_only_pairs,
        require_exact_validation=not args.allow_symbol_direction_promotion,
        min_validation_score=args.min_validation_score,
        historical_match_limit=args.historical_match_limit,
        historical_min_total=args.historical_min_total,
        require_alert_basket=args.require_alert_basket,
        alert_basket_limit=args.alert_basket_limit,
        alert_basket_modes=tuple(_parse_symbols(args.alert_basket_modes)),
        limit=args.limit,
    )
    watchlist = ScannerWatchlist(intelligence_db_path=args.intelligence_db)
    try:
        items = watchlist.build(config)
        report = format_watchlist_report(
            items,
            config,
            include_blocked=args.include_blocked,
        )
        if args.notify:
            notify_watchlist_report(report)
        else:
            print(report)
    finally:
        watchlist.close()


if __name__ == "__main__":
    main()
