"""Ablate vision-review filter hypotheses against MMM replay records."""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Optional

from config.settings import settings
from helix_v3.backtest.setup_intelligence import rrs_grade
from helix_v3.training.vision_feature_backfill import FEATURE_COLUMNS

DEFAULT_FLASHCARDS_DB = Path(settings.log_dir) / "flashcards.db"
DEFAULT_REPLAY_DB = Path(settings.log_dir) / "vision_backtests.db"
DEFAULT_PACKET_ROOT = Path("data/mmm_training/vision_review_packets")
DEFAULT_PAIR_RESEARCH_ROOT = Path("data/mmm_training/pair_research")
DEFAULT_PAIR_ABLATION_ROOT = Path("data/mmm_training/pair_feature_ablations")
DEFAULT_PAIR_SYMBOLS = "GBPJPY,EURJPY"
FAVORABLE_OUTCOMES = {"TARGET_2", "TRAIL_STOP", "TIME_EXIT_PROFIT", "OPEN_PROFIT"}
SCANNER_BASELINE_FAVORABLE_RATE = 85.0
SCANNER_BASELINE_AVG_EXIT_PIPS = 10.9


@dataclass(frozen=True)
class FilterVariant:
    name: str
    description: str
    predicate: Callable[[dict[str, Any]], bool]


def run_packet_ablation(
    *,
    packet_root: Path = DEFAULT_PACKET_ROOT,
    flashcards_db: Path = DEFAULT_FLASHCARDS_DB,
    replay_db: Path = DEFAULT_REPLAY_DB,
) -> list[Path]:
    written: list[Path] = []
    index_rows: list[dict[str, Any]] = []
    for manifest_path in sorted(packet_root.glob("*/manifest.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        rows = _load_rows(
            flashcards_db=flashcards_db,
            replay_db=replay_db,
            symbol=str(manifest["symbol"]),
            normalized_key=str(manifest["normalized_key"]),
        )
        results = [_variant_result(variant, rows) for variant in _variants()]
        packet_dir = manifest_path.parent
        reviews_dir = packet_dir / "reviews"
        reviews_dir.mkdir(exist_ok=True)
        json_path = reviews_dir / "filter_ablation.json"
        md_path = reviews_dir / "filter_ablation.md"
        payload = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "symbol": manifest["symbol"],
            "normalized_key": manifest["normalized_key"],
            "sample_total": len(rows),
            "variants": results,
        }
        json_path.write_text(
            json.dumps(payload, indent=2, sort_keys=True, default=str),
            encoding="utf-8",
        )
        md_path.write_text(_format_markdown(payload), encoding="utf-8")
        written.extend([json_path, md_path])
        best = _best_variant(results)
        index_rows.append(
            {
                "packet": packet_dir.name,
                "symbol": manifest["symbol"],
                "sample_total": len(rows),
                "best_name": best.get("name", "-"),
                "best_total": best.get("total", 0),
                "best_rrs_grade": best.get("rrs_grade", "-"),
                "best_favorable_rate": best.get("favorable_rate"),
                "best_avg_exit_pips": best.get("avg_exit_pips"),
                "best_profit_factor": best.get("profit_factor"),
                "best_payoff_ratio": best.get("payoff_ratio"),
            }
        )
    index_path = packet_root / "FILTER_ABLATION_INDEX.md"
    index_path.write_text(_format_index(index_rows), encoding="utf-8")
    written.append(index_path)
    return written


def run_pair_research_ablation(
    *,
    pair_research_root: Path = DEFAULT_PAIR_RESEARCH_ROOT,
    output_root: Path = DEFAULT_PAIR_ABLATION_ROOT,
    flashcards_db: Path = DEFAULT_FLASHCARDS_DB,
    replay_db: Path = DEFAULT_REPLAY_DB,
    symbols: tuple[str, ...] = ("GBPJPY", "EURJPY"),
    min_total: int = 10,
    split_min_total: int = 3,
    required_split_passes: int = 2,
) -> list[Path]:
    output_root.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    index_rows: list[dict[str, Any]] = []

    for symbol in symbols:
        candidates = _load_pair_candidates(pair_research_root, symbol, min_total=min_total)
        split_windows = _load_split_windows(pair_research_root, symbol)
        setup_payloads: list[dict[str, Any]] = []
        for candidate in candidates:
            rows = _load_rows(
                flashcards_db=flashcards_db,
                replay_db=replay_db,
                symbol=symbol,
                normalized_key=str(candidate["normalized_key"]),
            )
            results = [_variant_result(variant, rows) for variant in _variants()]
            best = _best_variant(results)
            best_variant = _variant_by_name(best.get("name"))
            split_stats = (
                _split_variant_stats(best_variant, rows, split_windows)
                if best_variant and split_windows
                else {}
            )
            split_passes = sum(
                1
                for split in split_stats.values()
                if _split_passes_baseline(split, split_min_total=split_min_total)
            )
            expectancy_split_passes = sum(
                1
                for split in split_stats.values()
                if _split_passes_expectancy(split, split_min_total=split_min_total)
            )
            setup_payloads.append(
                {
                    "candidate": candidate,
                    "sample_total": len(rows),
                    "base_variant": results[0] if results else {},
                    "variants": results,
                    "best_variant": best,
                    "best_variant_split_stats": split_stats,
                    "best_variant_split_passes": split_passes,
                    "best_variant_expectancy_split_passes": expectancy_split_passes,
                    "beats_scanner_baseline": _beats_scanner_baseline(best),
                    "promotion_ready": _beats_scanner_baseline(best)
                    and split_passes >= required_split_passes,
                }
            )

        pair_dir = output_root / symbol
        pair_dir.mkdir(parents=True, exist_ok=True)
        json_path = pair_dir / "feature_ablation.json"
        md_path = pair_dir / "FEATURE_ABLATION.md"
        payload = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "symbol": symbol,
            "min_total": min_total,
            "scanner_baseline": {
                "favorable_rate": SCANNER_BASELINE_FAVORABLE_RATE,
                "avg_exit_pips": SCANNER_BASELINE_AVG_EXIT_PIPS,
                "required_split_passes": required_split_passes,
                "split_min_total": split_min_total,
            },
            "split_windows": split_windows,
            "setups": setup_payloads,
        }
        json_path.write_text(
            json.dumps(payload, indent=2, sort_keys=True, default=str),
            encoding="utf-8",
        )
        md_path.write_text(_format_pair_markdown(payload), encoding="utf-8")
        written.extend([json_path, md_path])
        best_overall = _best_pair_setup(setup_payloads)
        index_rows.append(
            {
                "symbol": symbol,
                "setup_count": len(setup_payloads),
                "best_setup": best_overall,
                "path": md_path,
            }
        )

    index_path = output_root / "INDEX.md"
    index_path.write_text(_format_pair_index(index_rows), encoding="utf-8")
    written.append(index_path)
    return written


def _load_rows(
    *,
    flashcards_db: Path,
    replay_db: Path,
    symbol: str,
    normalized_key: str,
) -> list[dict[str, Any]]:
    conn = sqlite3.connect(str(replay_db))
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("ATTACH DATABASE ? AS flashcards_db", (str(flashcards_db),))
        _ensure_feature_columns(conn)
        rows = conn.execute(
            """SELECT
                s.symbol,
                s.direction,
                s.normalized_key,
                o.outcome,
                o.exit_pips,
                o.max_favorable_pips,
                o.max_adverse_pips,
                o.t1_hit,
                f.id AS flashcard_id,
                f.snapshot_at,
                f.weekly_trend,
                f.asian_range_pips,
                f.stop_hunt_pips,
                f.confluence_score,
                f.tdi_signals,
                f.tdi_vb_squeeze,
                f.tdi_rsi,
                f.tdi_signal,
                f.tdi_base,
                f.h1_session,
                f.h4_level,
                f.rrt_detected,
                f.feature_hunt_to_ar_ratio,
                f.feature_candles_since_hunt_extreme,
                f.feature_close_to_ar_low_pips,
                f.feature_close_to_ar_mid_pips,
                f.feature_close_to_ar_high_pips,
                f.feature_range_pos,
                f.feature_close_to_hod_pips,
                f.feature_close_to_lod_pips,
                f.feature_pullback_from_session_extreme_pips,
                f.feature_distance_from_hunt_extreme_pips,
                f.feature_prior_8_candle_expansion_pips,
                f.feature_prior_8_candle_directional_move_pips,
                f.feature_bars_since_first_ar_edge_break,
                f.feature_ema50_ema200_spread_pips,
                f.feature_ema200_slope_8_pips,
                f.feature_tdi_rsi_minus_signal
            FROM mmm_setup_signatures s
            JOIN mmm_event_outcomes o
              ON o.source = s.source AND o.source_id = s.source_id
            JOIN flashcards_db.flashcards f
              ON f.id = s.source_id
             AND f.snapshot_type = 'HISTORICAL'
            WHERE s.source = 'historical_flashcard'
              AND s.symbol = ?
              AND s.normalized_key = ?
            ORDER BY f.snapshot_at""",
            (symbol, normalized_key),
        ).fetchall()
    finally:
        conn.close()
    return [{key: row[key] for key in row.keys()} for row in rows]


def _ensure_feature_columns(conn: sqlite3.Connection) -> None:
    existing = {
        row["name"]
        for row in conn.execute("PRAGMA flashcards_db.table_info(flashcards)").fetchall()
    }
    for column, column_type in FEATURE_COLUMNS.items():
        if column not in existing:
            conn.execute(f"ALTER TABLE flashcards_db.flashcards ADD COLUMN {column} {column_type}")


def _load_pair_candidates(
    pair_research_root: Path,
    symbol: str,
    *,
    min_total: int,
) -> list[dict[str, Any]]:
    path = pair_research_root / symbol / "setup_performance.json"
    if not path.exists():
        return []
    rows = json.loads(path.read_text(encoding="utf-8"))
    return [
        row for row in rows
        if int(row.get("total") or 0) >= min_total
    ]


def _load_split_windows(pair_research_root: Path, symbol: str) -> list[dict[str, Any]]:
    summary_path = pair_research_root / symbol / "SUMMARY.md"
    if not summary_path.exists():
        return []
    windows: list[dict[str, Any]] = []
    for line in summary_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        for name in ("train", "validation", "out_of_sample"):
            prefix = f"- {name}: "
            if not stripped.startswith(prefix):
                continue
            raw = stripped.removeprefix(prefix)
            if " to " not in raw:
                continue
            start_raw, end_raw = raw.split(" to ", 1)
            windows.append(
                {
                    "name": name,
                    "start": _parse_date(start_raw),
                    "end": _parse_date(end_raw) + timedelta(days=1),
                }
            )
    return windows


def _variants() -> list[FilterVariant]:
    return [
        FilterVariant("all", "No extra visual-review filter.", lambda row: True),
        FilterVariant(
            "hunt_to_ar_ratio_le_2_0",
            "Reject if stop_hunt_pips / asian_range_pips > 2.0.",
            lambda row: _ratio(row) <= 2.0,
        ),
        FilterVariant(
            "hunt_to_ar_ratio_le_2_5",
            "Reject if stop_hunt_pips / asian_range_pips > 2.5.",
            lambda row: _ratio(row) <= 2.5,
        ),
        FilterVariant(
            "stop_hunt_le_90",
            "Reject GBPJPY-style extreme hunts above 90 pips.",
            lambda row: (_float(row.get("stop_hunt_pips")) or 0.0) <= 90.0,
        ),
        FilterVariant(
            "asian_range_gte_30",
            "Reject GBPJPY ranges below 30 pips.",
            lambda row: (_float(row.get("asian_range_pips")) or 0.0) >= 30.0,
        ),
        FilterVariant(
            "confluence_gte_60",
            "Require confluence score >= 60.",
            lambda row: int(row.get("confluence_score") or 0) >= 60,
        ),
        FilterVariant(
            "confluence_gte_70",
            "Require confluence score >= 70.",
            lambda row: int(row.get("confluence_score") or 0) >= 70,
        ),
        FilterVariant(
            "tdi_rsi_gt_signal",
            "Require raw TDI RSI above signal line.",
            lambda row: _float(row.get("tdi_rsi")) is not None
            and _float(row.get("tdi_signal")) is not None
            and float(row["tdi_rsi"]) > float(row["tdi_signal"]),
        ),
        FilterVariant(
            "tdi_rsi_gte_50",
            "Require raw TDI RSI >= 50.",
            lambda row: (_float(row.get("tdi_rsi")) or 0.0) >= 50.0,
        ),
        FilterVariant(
            "ratio_le_2_and_asian_gte_30",
            "Combine hunt_to_ar_ratio <= 2.0 and Asian range >= 30p.",
            lambda row: _ratio(row) <= 2.0 and (_float(row.get("asian_range_pips")) or 0.0) >= 30.0,
        ),
        FilterVariant(
            "ratio_le_2_asian_gte_30_tdi_positive",
            "Combine ratio/Asian filter with TDI RSI > signal.",
            lambda row: _ratio(row) <= 2.0
            and (_float(row.get("asian_range_pips")) or 0.0) >= 30.0
            and _float(row.get("tdi_rsi")) is not None
            and _float(row.get("tdi_signal")) is not None
            and float(row["tdi_rsi"]) > float(row["tdi_signal"]),
        ),
        FilterVariant(
            "feature_fresh_reclaim_within_8",
            "Require close back above AR low and AR mid within 8 candles of hunt extreme.",
            lambda row: _feature(row, "feature_close_to_ar_low_pips") is not None
            and _feature(row, "feature_close_to_ar_mid_pips") is not None
            and _feature(row, "feature_candles_since_hunt_extreme") is not None
            and float(row["feature_close_to_ar_low_pips"]) >= 0.0
            and float(row["feature_close_to_ar_mid_pips"]) >= 0.0
            and int(row["feature_candles_since_hunt_extreme"]) <= 8,
        ),
        FilterVariant(
            "feature_extreme_hunt_with_exception",
            "Reject extreme hunts unless weekly BUY, VB squeeze, and Asian range <= 30p.",
            _feature_extreme_hunt_with_exception,
        ),
        FilterVariant(
            "feature_stale_hod_exhaustion_reject",
            "Reject late range-top BUYs after 1.5x AR expansion with bearish TDI.",
            lambda row: not _feature_stale_hod_exhaustion(row),
        ),
        FilterVariant(
            "feature_momentum_breakout_exception",
            "Allow AR-high breakouts only when fresh, impulsive, and not TDI-bearish.",
            _feature_momentum_breakout_exception,
        ),
        FilterVariant(
            "feature_eurjpy_tdi50_reclaim",
            "Require TDI RSI >= 50 and close back above AR low.",
            lambda row: (_float(row.get("tdi_rsi")) or 0.0) >= 50.0
            and _feature(row, "feature_close_to_ar_low_pips") is not None
            and float(row["feature_close_to_ar_low_pips"]) >= 0.0,
        ),
    ]


def _variant_result(variant: FilterVariant, rows: list[dict[str, Any]]) -> dict[str, Any]:
    kept = [row for row in rows if variant.predicate(row)]
    total = len(kept)
    favorable = sum(1 for row in kept if _is_favorable(row))
    direct = sum(1 for row in kept if (_float(row.get("exit_pips")) or 0.0) > 0)
    t1_hits = sum(1 for row in kept if bool(row.get("t1_hit")))
    exits = [_float(row.get("exit_pips")) for row in kept]
    exit_values = [value for value in exits if value is not None]
    wins = [value for value in exit_values if value > 0.0]
    losses = [value for value in exit_values if value < 0.0]
    avg_exit = _avg(exit_values)
    favorable_rate = favorable / total * 100.0 if total else 0.0
    gross_profit = sum(wins)
    gross_loss = abs(sum(losses))
    return {
        "name": variant.name,
        "description": variant.description,
        "total": total,
        "kept_pct": total / len(rows) * 100.0 if rows else 0.0,
        "favorable": favorable,
        "favorable_rate": favorable_rate,
        "rrs_grade": rrs_grade(favorable_rate),
        "direct_profit": direct,
        "direct_profit_rate": direct / total * 100.0 if total else 0.0,
        "t1_hits": t1_hits,
        "t1_rate": t1_hits / total * 100.0 if total else 0.0,
        "avg_exit_pips": avg_exit,
        "avg_win_pips": _avg(wins),
        "avg_loss_pips": _avg(losses),
        "gross_profit_pips": gross_profit,
        "gross_loss_pips": gross_loss,
        "profit_factor": _profit_factor(gross_profit, gross_loss),
        "payoff_ratio": _payoff_ratio(_avg(wins), _avg(losses)),
        "positive_expectancy": bool(avg_exit is not None and avg_exit > 0.0),
        "avg_mfe": _avg(_float(row.get("max_favorable_pips")) for row in kept),
        "avg_mae": _avg(_float(row.get("max_adverse_pips")) for row in kept),
        "source_ids": [int(row["flashcard_id"]) for row in kept[:50]],
    }


def _best_variant(results: list[dict[str, Any]]) -> dict[str, Any]:
    viable = [row for row in results if int(row.get("total") or 0) >= 5]
    if not viable:
        return {}
    return max(
        viable,
        key=lambda row: (
            int(bool(row.get("positive_expectancy"))),
            _rrs_rank(row.get("rrs_grade")),
            float(row.get("favorable_rate") or 0.0),
            float(row.get("profit_factor") or 0.0),
            float(row.get("avg_exit_pips") or -999.0),
            int(row.get("total") or 0),
        ),
    )


def _format_markdown(payload: dict[str, Any]) -> str:
    lines = [
        f"# {payload['symbol']} Vision Filter Ablation",
        "",
        f"Generated: {payload['generated_at']}",
        f"Sample total: {payload['sample_total']}",
        "",
        f"Setup: `{payload['normalized_key']}`",
        "",
        "| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in payload["variants"]:
        lines.append(
            f"| `{row['name']}` | {row['total']} | {row['rrs_grade']} | {_pct(row['kept_pct'])} | "
            f"{_pct(row['favorable_rate'])} | {_pct(row['direct_profit_rate'])} | "
            f"{_pct(row['t1_rate'])} | {_pips(row['avg_exit_pips'])} | "
            f"{_metric(row['profit_factor'])} | {_metric(row['payoff_ratio'])} | "
            f"{_pips(row['avg_mfe'])} | {_pips(row['avg_mae'])} |"
        )
    lines.append("")
    lines.append("These are hypothesis ablations only; no row promotes a live rule by itself.")
    lines.append("")
    return "\n".join(lines)


def _format_index(rows: list[dict[str, Any]]) -> str:
    lines = [
        "# Vision Filter Ablation Index",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        "| Pair | Packet | Samples | Best Variant | Kept | RRS | Fav% | AvgExit | PF | Payoff |",
        "|---|---|---:|---|---:|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['symbol']} | [{row['packet']}](./{row['packet']}/reviews/filter_ablation.md) | "
            f"{row['sample_total']} | `{row['best_name']}` | {row['best_total']} | "
            f"{row['best_rrs_grade']} | {_pct(row['best_favorable_rate'])} | "
            f"{_pips(row['best_avg_exit_pips'])} | {_metric(row['best_profit_factor'])} | "
            f"{_metric(row['best_payoff_ratio'])} |"
        )
    return "\n".join(lines) + "\n"


def _format_pair_markdown(payload: dict[str, Any]) -> str:
    lines = [
        f"# {payload['symbol']} Pair Feature Ablation",
        "",
        f"Generated: {payload['generated_at']}",
        f"Minimum setup sample: {payload['min_total']}",
        (
            "Scanner baseline gate: "
            f"Fav >= {SCANNER_BASELINE_FAVORABLE_RATE:.1f}% and "
            f"AvgExit >= {_pips(SCANNER_BASELINE_AVG_EXIT_PIPS)}; "
            f"split pass requirement = {payload['scanner_baseline']['required_split_passes']} "
            f"with split N >= {payload['scanner_baseline']['split_min_total']}"
        ),
        "",
        (
            "| Setup | Base N | Base RRS | Base Fav% | Base AvgExit | Best Variant | Kept | "
            "Best RRS | Fav% | AvgExit | PF | Payoff | ScannerSplit | ExpSplit | Decision |"
        ),
        "|---|---:|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for setup in payload["setups"]:
        candidate = setup["candidate"]
        base = setup.get("base_variant") or {}
        best = setup["best_variant"] or {}
        lines.append(
            f"| `{_short_key(candidate.get('normalized_key'))}` | "
            f"{base.get('total', candidate.get('total'))} | {base.get('rrs_grade', '-')} | "
            f"{_pct(base.get('favorable_rate', candidate.get('favorable_rate')))} | "
            f"{_pips(base.get('avg_exit_pips', candidate.get('avg_exit_pips')))} | "
            f"`{best.get('name', '-')}` | {best.get('total', 0)} | "
            f"{best.get('rrs_grade', '-')} | {_pct(best.get('favorable_rate'))} | "
            f"{_pips(best.get('avg_exit_pips'))} | {_metric(best.get('profit_factor'))} | "
            f"{_metric(best.get('payoff_ratio'))} | {setup['best_variant_split_passes']} | "
            f"{setup['best_variant_expectancy_split_passes']} | {_decision(setup)} |"
        )
    if not payload["setups"]:
        lines.append("| - | - | - | - | - | - | - | - | no candidates |")
    lines.extend(
        [
            "",
            "## Candidate Details",
            "",
        ]
    )
    for setup in payload["setups"]:
        candidate = setup["candidate"]
        lines.extend(
            [
                f"### {_short_key(candidate.get('normalized_key'))}",
                "",
                f"Setup: `{candidate.get('normalized_key')}`",
                "",
                _split_summary_line(setup),
                "",
                "| Variant | Kept | RRS | Kept% | Fav% | Direct% | T1% | AvgExit | PF | Payoff | MFE | MAE |",
                "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in setup["variants"]:
            lines.append(
                f"| `{row['name']}` | {row['total']} | {row['rrs_grade']} | {_pct(row['kept_pct'])} | "
                f"{_pct(row['favorable_rate'])} | {_pct(row['direct_profit_rate'])} | "
                f"{_pct(row['t1_rate'])} | {_pips(row['avg_exit_pips'])} | "
                f"{_metric(row['profit_factor'])} | {_metric(row['payoff_ratio'])} | "
                f"{_pips(row['avg_mfe'])} | {_pips(row['avg_mae'])} |"
            )
        lines.append("")
    lines.append("Research-only: a baseline-gate pass here still needs split confirmation before promotion.")
    lines.append("")
    return "\n".join(lines)


def _format_pair_index(rows: list[dict[str, Any]]) -> str:
    lines = [
        "# Pair Feature Ablation Index",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        "| Pair | Setups | Best Setup | Best Variant | Kept | RRS | Fav% | AvgExit | PF | Split | Decision | Report |",
        "|---|---:|---|---|---:|---|---:|---:|---:|---:|---|---|",
    ]
    for row in rows:
        setup = row["best_setup"] or {}
        best = setup.get("best_variant") or {}
        candidate = setup.get("candidate") or {}
        report = Path(row["path"])
        lines.append(
            f"| {row['symbol']} | {row['setup_count']} | "
            f"`{_short_key(candidate.get('normalized_key', '-'))}` | "
            f"`{best.get('name', '-')}` | {best.get('total', 0)} | "
            f"{best.get('rrs_grade', '-')} | {_pct(best.get('favorable_rate'))} | "
            f"{_pips(best.get('avg_exit_pips'))} | {_metric(best.get('profit_factor'))} | "
            f"{setup.get('best_variant_split_passes', 0)}/"
            f"{setup.get('best_variant_expectancy_split_passes', 0)} | {_decision(setup)} | "
            f"[FEATURE_ABLATION](./{row['symbol']}/{report.name}) |"
        )
    if not rows:
        lines.append("| - | - | - | - | - | - | - | - | - |")
    return "\n".join(lines) + "\n"


def _is_favorable(row: dict[str, Any]) -> bool:
    return str(row.get("outcome") or "") in FAVORABLE_OUTCOMES


def _ratio(row: dict[str, Any]) -> float:
    asian = _float(row.get("asian_range_pips")) or 0.0
    hunt = _float(row.get("stop_hunt_pips")) or 0.0
    if asian <= 0:
        return 999.0
    return hunt / asian


def _feature_extreme_hunt_with_exception(row: dict[str, Any]) -> bool:
    ratio = _feature(row, "feature_hunt_to_ar_ratio")
    stop_hunt = _float(row.get("stop_hunt_pips"))
    if ratio is None and stop_hunt is None:
        return False
    is_extreme = (ratio is not None and ratio >= 2.0) or (stop_hunt is not None and stop_hunt >= 90.0)
    if not is_extreme:
        return True
    return (
        str(row.get("weekly_trend") or "").upper() == "BUY"
        and bool(row.get("tdi_vb_squeeze"))
        and (_float(row.get("asian_range_pips")) or 999.0) <= 30.0
    )


def _feature_stale_hod_exhaustion(row: dict[str, Any]) -> bool:
    range_pos = _feature(row, "feature_range_pos")
    distance_from_hunt = _feature(row, "feature_distance_from_hunt_extreme_pips")
    asian = _float(row.get("asian_range_pips"))
    if range_pos is None or distance_from_hunt is None or asian is None or asian <= 0:
        return False
    return range_pos >= 0.85 and distance_from_hunt >= 1.5 * asian and _tdi_bearish(row)


def _feature_momentum_breakout_exception(row: dict[str, Any]) -> bool:
    range_pos = _feature(row, "feature_range_pos")
    if range_pos is None:
        return False
    if range_pos <= 1.0:
        return True

    bars_since_break = _feature(row, "feature_bars_since_first_ar_edge_break")
    distance_from_hunt = _feature(row, "feature_distance_from_hunt_extreme_pips")
    asian = _float(row.get("asian_range_pips"))
    if bars_since_break is None or distance_from_hunt is None or asian is None or asian <= 0:
        return False
    return bars_since_break <= 6 and distance_from_hunt >= 0.6 * asian and not _tdi_bearish(row)


def _tdi_bearish(row: dict[str, Any]) -> bool:
    signals = str(row.get("tdi_signals") or "").upper()
    if "BEARISH" in signals or "SHORT" in signals:
        return True
    rsi = _float(row.get("tdi_rsi"))
    signal = _float(row.get("tdi_signal"))
    return rsi is not None and signal is not None and rsi < signal


def _feature(row: dict[str, Any], key: str) -> Optional[float]:
    return _float(row.get(key))


def _variant_by_name(name: Any) -> Optional[FilterVariant]:
    if not name:
        return None
    for variant in _variants():
        if variant.name == name:
            return variant
    return None


def _split_variant_stats(
    variant: FilterVariant,
    rows: list[dict[str, Any]],
    windows: list[dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    stats: dict[str, dict[str, Any]] = {}
    for window in windows:
        split_rows = [
            row for row in rows
            if _in_window(row.get("snapshot_at"), window)
        ]
        stats[str(window["name"])] = _variant_result(variant, split_rows)
    return stats


def _split_passes_baseline(split: dict[str, Any], *, split_min_total: int) -> bool:
    return (
        int(split.get("total") or 0) >= split_min_total
        and float(split.get("favorable_rate") or 0.0) >= SCANNER_BASELINE_FAVORABLE_RATE
        and float(split.get("avg_exit_pips") or -999.0) >= SCANNER_BASELINE_AVG_EXIT_PIPS
    )


def _split_passes_expectancy(split: dict[str, Any], *, split_min_total: int) -> bool:
    return (
        int(split.get("total") or 0) >= split_min_total
        and bool(split.get("positive_expectancy"))
        and float(split.get("profit_factor") or 0.0) >= 1.05
    )


def _in_window(value: Any, window: dict[str, Any]) -> bool:
    if not value:
        return False
    parsed = _parse_datetime(str(value))
    return window["start"] <= parsed < window["end"]


def _best_pair_setup(setups: list[dict[str, Any]]) -> dict[str, Any]:
    viable = [
        setup for setup in setups
        if int((setup.get("best_variant") or {}).get("total") or 0) >= 5
    ]
    if not viable:
        return {}
    return max(
        viable,
        key=lambda setup: (
            int(bool((setup.get("best_variant") or {}).get("positive_expectancy"))),
            _rrs_rank((setup.get("best_variant") or {}).get("rrs_grade")),
            float((setup.get("best_variant") or {}).get("favorable_rate") or 0.0),
            float((setup.get("best_variant") or {}).get("profit_factor") or 0.0),
            float((setup.get("best_variant") or {}).get("avg_exit_pips") or -999.0),
            int((setup.get("best_variant") or {}).get("total") or 0),
        ),
    )


def _beats_scanner_baseline(row: dict[str, Any]) -> bool:
    return (
        int(row.get("total") or 0) >= 5
        and float(row.get("favorable_rate") or 0.0) >= SCANNER_BASELINE_FAVORABLE_RATE
        and float(row.get("avg_exit_pips") or -999.0) >= SCANNER_BASELINE_AVG_EXIT_PIPS
    )


def _decision(setup: dict[str, Any]) -> str:
    if setup.get("promotion_ready"):
        return "promotion_candidate"
    if setup.get("beats_scanner_baseline"):
        return "research_only_split_fail"
    if int(setup.get("best_variant_expectancy_split_passes") or 0) >= 2:
        return "demo_watch_candidate"
    if bool((setup.get("best_variant") or {}).get("positive_expectancy")):
        return "watch_research"
    return "fail"


def _split_summary_line(setup: dict[str, Any]) -> str:
    stats = setup.get("best_variant_split_stats") or {}
    if not stats:
        return "Best-variant splits: not available."
    parts = []
    for name, split in stats.items():
        parts.append(
            f"{name} N={split.get('total', 0)} Fav={_pct(split.get('favorable_rate'))} "
            f"Avg={_pips(split.get('avg_exit_pips'))}"
        )
    return f"Best-variant splits: {'; '.join(parts)}."


def _short_key(value: Any) -> str:
    parts = str(value or "").split("|")
    if len(parts) <= 8:
        return str(value or "")
    return "|".join([*parts[:5], "...", *parts[-3:]])


def _parse_date(raw: str) -> datetime:
    return datetime.fromisoformat(raw.strip()).replace(tzinfo=timezone.utc)


def _parse_datetime(raw: str) -> datetime:
    value = raw.strip().replace("Z", "+00:00")
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _profit_factor(gross_profit_pips: float, gross_loss_pips: float) -> float:
    if gross_loss_pips <= 0.0:
        return 999.0 if gross_profit_pips > 0.0 else 0.0
    return round(max(0.0, gross_profit_pips) / gross_loss_pips, 2)


def _payoff_ratio(avg_win_pips: Optional[float], avg_loss_pips: Optional[float]) -> float:
    win = avg_win_pips or 0.0
    loss = abs(avg_loss_pips or 0.0)
    if loss <= 0.0:
        return 999.0 if win > 0.0 else 0.0
    return round(max(0.0, win) / loss, 2)


def _rrs_rank(value: Any) -> int:
    return {"R_RUNNER": 2, "R_REPEATER": 1, "S_STRANGER": 0}.get(str(value or ""), -1)


def _avg(values: Any) -> Optional[float]:
    parsed = [value for value in values if value is not None]
    return sum(parsed) / len(parsed) if parsed else None


def _pct(value: Any) -> str:
    number = _float(value)
    return "-" if number is None else f"{number:.1f}%"


def _pips(value: Any) -> str:
    number = _float(value)
    return "-" if number is None else f"{number:+.1f}"


def _metric(value: Any) -> str:
    number = _float(value)
    return "-" if number is None else f"{number:.2f}"


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Run vision filter ablations for review packets")
    parser.add_argument("--packet-root", type=Path, default=DEFAULT_PACKET_ROOT)
    parser.add_argument("--flashcards-db", type=Path, default=DEFAULT_FLASHCARDS_DB)
    parser.add_argument("--replay-db", type=Path, default=DEFAULT_REPLAY_DB)
    parser.add_argument("--pair-research", action="store_true", help="Run pair research ablations")
    parser.add_argument("--pair-research-root", type=Path, default=DEFAULT_PAIR_RESEARCH_ROOT)
    parser.add_argument("--pair-output-root", type=Path, default=DEFAULT_PAIR_ABLATION_ROOT)
    parser.add_argument("--symbols", default=DEFAULT_PAIR_SYMBOLS)
    parser.add_argument("--min-total", type=int, default=10)
    parser.add_argument("--split-min-total", type=int, default=3)
    parser.add_argument("--required-split-passes", type=int, default=2)
    args = parser.parse_args(argv)
    if args.pair_research:
        written = run_pair_research_ablation(
            pair_research_root=args.pair_research_root,
            output_root=args.pair_output_root,
            flashcards_db=args.flashcards_db,
            replay_db=args.replay_db,
            symbols=_parse_symbols(args.symbols),
            min_total=args.min_total,
            split_min_total=args.split_min_total,
            required_split_passes=args.required_split_passes,
        )
    else:
        written = run_packet_ablation(
            packet_root=args.packet_root,
            flashcards_db=args.flashcards_db,
            replay_db=args.replay_db,
        )
    print(f"Wrote {len(written)} ablation files.")


def _parse_symbols(raw: str) -> tuple[str, ...]:
    return tuple(symbol.strip().upper() for symbol in raw.split(",") if symbol.strip())


if __name__ == "__main__":
    main()
