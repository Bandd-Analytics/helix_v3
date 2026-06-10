"""Offline calibration audit for non-FX instruments and pip-value assumptions."""

from __future__ import annotations

import argparse
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

from config.pair_profiles import PairProfile, get_pair_profile
from helix_v3.backtest.setup_intelligence import DEFAULT_INTELLIGENCE_DB_PATH
from helix_v3.core.instruments import fallback_pip_size, pip_size_from_digits, pip_value_per_lot

DEFAULT_SYMBOLS = ("XAUUSD", "US30", "USTEC")
DEFAULT_REPORT_PATH = Path("data/mmm_training/instrument_calibration/REPORT.md")
EAT = timezone(timedelta(hours=3))


@dataclass(frozen=True)
class SymbolSpec:
    symbol: str
    visible: bool
    digits: int
    point: float
    pip_size: float
    trade_tick_size: float
    trade_tick_value: float
    trade_contract_size: float
    volume_min: float
    volume_step: float
    volume_max: float
    bid: Optional[float]
    ask: Optional[float]
    spread_pips: Optional[float]
    pip_value_per_lot: Optional[float]


@dataclass(frozen=True)
class ReplayCalibrationStats:
    symbol: str
    occurrences: int
    expectancy_candidates: int
    demo_candidates: int
    asymmetric_exceptions: int
    watch_candidates: int
    avg_exit_pips: Optional[float]
    median_exit_pips: Optional[float]
    p90_abs_exit_pips: Optional[float]
    p90_mfe_pips: Optional[float]
    p90_mae_pips: Optional[float]
    avg_profit_factor: Optional[float]


@dataclass(frozen=True)
class CalibrationRow:
    symbol: str
    profile_tradeable: bool
    status: str
    spec: Optional[SymbolSpec]
    replay: ReplayCalibrationStats
    avg_exit_price_move: Optional[float]
    p90_abs_exit_price_move: Optional[float]
    p90_mfe_price_move: Optional[float]
    p90_mae_price_move: Optional[float]
    avg_exit_value_per_lot: Optional[float]
    notes: list[str]


def build_calibration_rows(
    *,
    symbols: list[str],
    intelligence_db: Path = DEFAULT_INTELLIGENCE_DB_PATH,
    specs: Optional[dict[str, SymbolSpec]] = None,
) -> list[CalibrationRow]:
    specs = specs or {}
    conn = sqlite3.connect(str(intelligence_db))
    conn.row_factory = sqlite3.Row
    try:
        return [
            _calibration_row(
                symbol=symbol,
                spec=specs.get(symbol),
                replay=_load_replay_stats(conn, symbol),
                profile=get_pair_profile(symbol),
            )
            for symbol in symbols
        ]
    finally:
        conn.close()


def fetch_mt5_specs(symbols: list[str]) -> dict[str, SymbolSpec]:
    import MetaTrader5 as mt5

    specs: dict[str, SymbolSpec] = {}
    for symbol in symbols:
        info = mt5.symbol_info(symbol)
        if info is None:
            continue
        if not info.visible:
            mt5.symbol_select(symbol, True)
            info = mt5.symbol_info(symbol)
            if info is None:
                continue
        tick = mt5.symbol_info_tick(symbol)
        point = float(info.point or 0.0)
        digits = int(info.digits or 0)
        pip_size = pip_size_from_digits(point=point, digits=digits)
        spread_pips: Optional[float] = None
        bid: Optional[float] = None
        ask: Optional[float] = None
        if tick is not None:
            bid = float(tick.bid or 0.0)
            ask = float(tick.ask or 0.0)
            if pip_size > 0:
                spread_pips = (ask - bid) / pip_size
        tick_size = float(getattr(info, "trade_tick_size", 0.0) or 0.0)
        tick_value = float(getattr(info, "trade_tick_value", 0.0) or 0.0)
        specs[symbol] = SymbolSpec(
            symbol=symbol,
            visible=bool(info.visible),
            digits=digits,
            point=point,
            pip_size=pip_size,
            trade_tick_size=tick_size,
            trade_tick_value=tick_value,
            trade_contract_size=float(getattr(info, "trade_contract_size", 0.0) or 0.0),
            volume_min=float(getattr(info, "volume_min", 0.0) or 0.0),
            volume_step=float(getattr(info, "volume_step", 0.0) or 0.0),
            volume_max=float(getattr(info, "volume_max", 0.0) or 0.0),
            bid=bid,
            ask=ask,
            spread_pips=spread_pips,
            pip_value_per_lot=pip_value_per_lot(
                pip_size=pip_size,
                tick_size=tick_size,
                tick_value=tick_value,
            ),
        )
    return specs


def format_report(rows: list[CalibrationRow], *, generated_at: Optional[datetime] = None) -> str:
    generated = (generated_at or datetime.now(timezone.utc)).astimezone(EAT)
    lines = [
        "# Instrument Calibration Report",
        "",
        f"Generated: {generated.strftime('%Y-%m-%d %H:%M EAT')}",
        "",
        "This is an offline research audit. It does not place, modify, or close trades.",
        "",
        "## Summary",
        "",
        (
            "| Symbol | Status | Tradeable | Digits | Point | PipSize | TickSize | "
            "TickValue | PipValue/Lot | Spread | Occ | Demo | Asym | AvgExit | "
            "P90Abs | AvgValue/Lot |"
        ),
        (
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"
            "---:|---:|---:|"
        ),
    ]
    for row in rows:
        spec = row.spec
        replay = row.replay
        lines.append(
            f"| {row.symbol} | {row.status} | {int(row.profile_tradeable)} | "
            f"{_fmt_int(spec.digits if spec else None)} | {_fmt_float(spec.point if spec else None, 6)} | "
            f"{_fmt_float(spec.pip_size if spec else None, 6)} | "
            f"{_fmt_float(spec.trade_tick_size if spec else None, 6)} | "
            f"{_fmt_money(spec.trade_tick_value if spec else None)} | "
            f"{_fmt_money(spec.pip_value_per_lot if spec else None)} | "
            f"{_fmt_float(spec.spread_pips if spec else None, 1)} | "
            f"{replay.occurrences} | {replay.demo_candidates} | "
            f"{replay.asymmetric_exceptions} | {_fmt_signed(replay.avg_exit_pips)} | "
            f"{_fmt_signed(replay.p90_abs_exit_pips)} | {_fmt_money(row.avg_exit_value_per_lot)} |"
        )

    lines.extend(["", "## Notes", ""])
    for row in rows:
        lines.append(f"### {row.symbol}")
        if row.spec is None:
            lines.append("- MT5 symbol metadata was unavailable. Treat replay expectancy as uncalibrated.")
        else:
            lines.append(
                "- MT5 units: "
                f"point={row.spec.point:g}, pip_size={row.spec.pip_size:g}, "
                f"pip_value_per_lot={_fmt_money(row.spec.pip_value_per_lot)}."
            )
            lines.append(
                "- Replay translation: "
                f"avg_exit_price_move={_fmt_float(row.avg_exit_price_move, 3)}, "
                f"p90_abs_exit_price_move={_fmt_float(row.p90_abs_exit_price_move, 3)}, "
                f"p90_mfe_price_move={_fmt_float(row.p90_mfe_price_move, 3)}, "
                f"p90_mae_price_move={_fmt_float(row.p90_mae_price_move, 3)}."
            )
        for note in row.notes:
            lines.append(f"- {note}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _calibration_row(
    *,
    symbol: str,
    spec: Optional[SymbolSpec],
    replay: ReplayCalibrationStats,
    profile: PairProfile,
) -> CalibrationRow:
    notes: list[str] = []
    pip_size = spec.pip_size if spec else fallback_pip_size(symbol)
    avg_exit_price_move = _scale(replay.avg_exit_pips, pip_size)
    p90_abs_exit_price_move = _scale(replay.p90_abs_exit_pips, pip_size)
    p90_mfe_price_move = _scale(replay.p90_mfe_pips, pip_size)
    p90_mae_price_move = _scale(replay.p90_mae_pips, pip_size)
    avg_exit_value_per_lot = _scale(replay.avg_exit_pips, spec.pip_value_per_lot if spec else None)

    if spec is None:
        status = "METADATA_BLOCKED"
        notes.append("No MT5 symbol_info available; do not rank this instrument for demo use.")
    elif (
        spec.point <= 0
        or spec.pip_size <= 0
        or spec.trade_tick_size <= 0
        or spec.trade_tick_value <= 0
        or spec.pip_value_per_lot is None
    ):
        status = "METADATA_BLOCKED"
        notes.append("Invalid point/tick metadata; pip-value and risk conversion are unsafe.")
    elif not profile.tradeable:
        status = "RESEARCH_CALIBRATED_EXECUTION_BLOCKED"
        notes.append("PairProfile is analysis-only; keep out of live validation and auto-entry.")
    else:
        status = "RESEARCH_CALIBRATED"

    if symbol.upper().startswith("XAU") and spec and abs(spec.pip_size - 0.01) > 1e-9:
        notes.append("Gold pip size differs from the expected 0.01; audit broker convention manually.")
    if symbol.upper() in {"US30", "USTEC"}:
        notes.append("Index point values are broker-specific; require manual contract-value approval.")
    if replay.expectancy_candidates == 0:
        notes.append("No expectancy candidates found in setup intelligence.")
    if replay.demo_candidates or replay.asymmetric_exceptions:
        notes.append(
            "Promising research candidates exist, but visual flashcard and demo validation are still required."
        )

    return CalibrationRow(
        symbol=symbol,
        profile_tradeable=profile.tradeable,
        status=status,
        spec=spec,
        replay=replay,
        avg_exit_price_move=avg_exit_price_move,
        p90_abs_exit_price_move=p90_abs_exit_price_move,
        p90_mfe_price_move=p90_mfe_price_move,
        p90_mae_price_move=p90_mae_price_move,
        avg_exit_value_per_lot=avg_exit_value_per_lot,
        notes=notes,
    )


def _load_replay_stats(conn: sqlite3.Connection, symbol: str) -> ReplayCalibrationStats:
    occurrence_rows: list[sqlite3.Row] = []
    candidate_rows: list[sqlite3.Row] = []
    if _table_exists(conn, "setup_occurrences"):
        occurrence_rows = conn.execute(
            """SELECT exit_pips, max_favorable_pips, max_adverse_pips
            FROM setup_occurrences
            WHERE symbol = ?""",
            (symbol,),
        ).fetchall()
    if _table_exists(conn, "expectancy_candidates"):
        candidate_rows = conn.execute(
            """SELECT candidate_tier, profit_factor
            FROM expectancy_candidates
            WHERE symbol = ?""",
            (symbol,),
        ).fetchall()
    exits = [_optional_float(row["exit_pips"]) for row in occurrence_rows]
    exits = [value for value in exits if value is not None]
    mfe = [_optional_float(row["max_favorable_pips"]) for row in occurrence_rows]
    mfe = [value for value in mfe if value is not None]
    mae = [_optional_float(row["max_adverse_pips"]) for row in occurrence_rows]
    mae = [value for value in mae if value is not None]
    pfs = [_optional_float(row["profit_factor"]) for row in candidate_rows]
    pfs = [value for value in pfs if value is not None]

    return ReplayCalibrationStats(
        symbol=symbol,
        occurrences=len(occurrence_rows),
        expectancy_candidates=len(candidate_rows),
        demo_candidates=sum(1 for row in candidate_rows if row["candidate_tier"] == "DEMO_CANDIDATE"),
        asymmetric_exceptions=sum(
            1 for row in candidate_rows if row["candidate_tier"] == "ASYMMETRIC_EXCEPTION"
        ),
        watch_candidates=sum(1 for row in candidate_rows if row["candidate_tier"] == "WATCH_CANDIDATE"),
        avg_exit_pips=_avg(exits),
        median_exit_pips=_median(exits),
        p90_abs_exit_pips=_quantile([abs(value) for value in exits], 0.90),
        p90_mfe_pips=_quantile(mfe, 0.90),
        p90_mae_pips=_quantile(mae, 0.90),
        avg_profit_factor=_avg(pfs),
    )


def _table_exists(conn: sqlite3.Connection, table: str) -> bool:
    return bool(
        conn.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?",
            (table,),
        ).fetchone()
    )


def _parse_symbols(raw: str) -> list[str]:
    return [part.strip().upper() for part in raw.split(",") if part.strip()]


def _optional_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _avg(values: list[float]) -> Optional[float]:
    if not values:
        return None
    return sum(values) / len(values)


def _median(values: list[float]) -> Optional[float]:
    if not values:
        return None
    ordered = sorted(values)
    midpoint = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[midpoint]
    return (ordered[midpoint - 1] + ordered[midpoint]) / 2.0


def _quantile(values: list[float], q: float) -> Optional[float]:
    if not values:
        return None
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * q)))
    return ordered[index]


def _scale(value: Optional[float], multiplier: Optional[float]) -> Optional[float]:
    if value is None or multiplier is None:
        return None
    return value * multiplier


def _fmt_int(value: Optional[int]) -> str:
    return "-" if value is None else str(value)


def _fmt_float(value: Optional[float], precision: int) -> str:
    return "-" if value is None else f"{value:.{precision}f}"


def _fmt_money(value: Optional[float]) -> str:
    return "-" if value is None else f"{value:.2f}"


def _fmt_signed(value: Optional[float]) -> str:
    return "-" if value is None else f"{value:+.1f}"


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Audit symbol pip/tick calibration")
    parser.add_argument("--symbols", default=",".join(DEFAULT_SYMBOLS))
    parser.add_argument("--intelligence-db", type=Path, default=DEFAULT_INTELLIGENCE_DB_PATH)
    parser.add_argument("--report-path", type=Path, default=DEFAULT_REPORT_PATH)
    parser.add_argument("--no-mt5", action="store_true", help="Skip MT5 metadata lookup")
    args = parser.parse_args(argv)

    symbols = _parse_symbols(args.symbols)
    specs: dict[str, SymbolSpec] = {}
    if not args.no_mt5:
        from helix_v3.backtest.scanner_replay import connect_mt5, disconnect_mt5

        if connect_mt5():
            try:
                specs = fetch_mt5_specs(symbols)
            finally:
                disconnect_mt5()

    rows = build_calibration_rows(
        symbols=symbols,
        intelligence_db=args.intelligence_db,
        specs=specs,
    )
    report = format_report(rows)
    args.report_path.parent.mkdir(parents=True, exist_ok=True)
    args.report_path.write_text(report, encoding="utf-8")
    print(report)
    print(f"Report: {args.report_path}")


if __name__ == "__main__":
    main()
