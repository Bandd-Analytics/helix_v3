"""Build winner-vs-loser vision review packets from MMM flashcards.

This is an offline preparation step. It copies chart images and writes
manifests/prompts so account-backed ChatGPT and Claude review can isolate the
visual differences between profitable and failed variants of the same setup.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from config.settings import settings

DEFAULT_FLASHCARDS_DB = Path(settings.log_dir) / "flashcards.db"
DEFAULT_REPLAY_DB = Path(settings.log_dir) / "vision_backtests.db"
DEFAULT_PAIR_RESEARCH_ROOT = Path("data/mmm_training/pair_research")
DEFAULT_OUTPUT_ROOT = Path("data/mmm_training/vision_review_packets")
DEFAULT_SYMBOLS = "GBPJPY,EURJPY"
FAVORABLE_OUTCOMES = {"TARGET_2", "TRAIL_STOP", "TIME_EXIT_PROFIT", "OPEN_PROFIT"}


@dataclass(frozen=True)
class PacketConfig:
    flashcards_db: Path = DEFAULT_FLASHCARDS_DB
    replay_db: Path = DEFAULT_REPLAY_DB
    pair_research_root: Path = DEFAULT_PAIR_RESEARCH_ROOT
    output_root: Path = DEFAULT_OUTPUT_ROOT
    symbols: tuple[str, ...] = ("GBPJPY", "EURJPY")
    min_total: int = 10
    min_favorable_rate: float = 55.0
    min_avg_exit_pips: float = 0.0
    max_setups_per_pair: int = 3
    winners_per_setup: int = 8
    losers_per_setup: int = 8
    copy_images: bool = True


def build_review_packets(config: PacketConfig) -> list[Path]:
    config.output_root.mkdir(parents=True, exist_ok=True)
    packet_paths: list[Path] = []
    index_rows: list[dict[str, Any]] = []

    for symbol in config.symbols:
        candidates = _load_setup_candidates(config, symbol)
        for candidate in candidates[: config.max_setups_per_pair]:
            rows = _load_flashcard_rows(config, symbol, str(candidate["normalized_key"]))
            winners = _select_rows(rows, winner=True, limit=config.winners_per_setup)
            losers = _select_rows(rows, winner=False, limit=config.losers_per_setup)
            if not winners or not losers:
                continue

            packet_dir = _packet_dir(config.output_root, symbol, str(candidate["normalized_key"]))
            _reset_packet_dir(packet_dir, config.output_root)
            image_dir = packet_dir / "images"
            if config.copy_images:
                image_dir.mkdir(exist_ok=True)

            items = _packet_items(
                winners=winners,
                losers=losers,
                packet_dir=packet_dir,
                image_dir=image_dir,
                copy_images=config.copy_images,
            )
            manifest = {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "symbol": symbol,
                "normalized_key": candidate["normalized_key"],
                "setup_performance": candidate,
                "counts": {
                    "winners": len(winners),
                    "losers": len(losers),
                    "items": len(items),
                },
                "items": items,
                "instructions": {
                    "blind_prompt": "blind_prompt.md",
                    "labeled_prompt": "labeled_comparison_prompt.md",
                    "answer_key": "answer_key.csv",
                    "review_matrix": "review_matrix.csv",
                },
            }

            _write_packet_files(packet_dir, manifest)
            packet_paths.append(packet_dir)
            index_rows.append(
                {
                    "symbol": symbol,
                    "packet": packet_dir,
                    "normalized_key": candidate["normalized_key"],
                    "total": candidate.get("total"),
                    "favorable_rate": candidate.get("favorable_rate"),
                    "avg_exit_pips": candidate.get("avg_exit_pips"),
                    "winners": len(winners),
                    "losers": len(losers),
                }
            )

    _write_index(config.output_root, index_rows)
    return packet_paths


def _load_setup_candidates(config: PacketConfig, symbol: str) -> list[dict[str, Any]]:
    path = config.pair_research_root / symbol / "setup_performance.json"
    if not path.exists():
        return []
    rows = json.loads(path.read_text(encoding="utf-8"))
    candidates = [
        row for row in rows
        if int(row.get("total") or 0) >= config.min_total
        and float(row.get("favorable_rate") or 0.0) >= config.min_favorable_rate
        and float(row.get("avg_exit_pips") or 0.0) >= config.min_avg_exit_pips
        and "W_BOTTOM" in str(row.get("normalized_key") or "")
    ]
    return sorted(
        candidates,
        key=lambda row: (
            float(row.get("favorable_rate") or 0.0),
            float(row.get("avg_exit_pips") or 0.0),
            int(row.get("total") or 0),
        ),
        reverse=True,
    )


def _load_flashcard_rows(config: PacketConfig, symbol: str, normalized_key: str) -> list[dict[str, Any]]:
    conn = sqlite3.connect(str(config.replay_db))
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("ATTACH DATABASE ? AS flashcards_db", (str(config.flashcards_db),))
        rows = conn.execute(
            """SELECT
                s.symbol,
                s.direction,
                s.normalized_key,
                s.raw_key,
                s.ratios,
                s.theme_tags,
                o.outcome AS replay_outcome,
                o.exit_pips,
                o.max_favorable_pips,
                o.max_adverse_pips,
                o.t1_hit,
                o.minutes_to_t1,
                o.event_path,
                f.id AS flashcard_id,
                f.snapshot_at,
                f.timeframe,
                f.chart_path,
                f.weekly_phase,
                f.weekly_trend,
                f.h4_level,
                f.h4_trend,
                f.h1_session,
                f.h1_trend,
                f.asian_range_pips,
                f.stop_hunt_detected,
                f.stop_hunt_direction,
                f.stop_hunt_pips,
                f.push_count,
                f.m_w_pattern,
                f.rrt_detected,
                f.tdi_signals,
                f.tdi_shark_fin,
                f.tdi_shark_direction,
                f.tdi_vb_squeeze,
                f.tdi_divergence,
                f.tdi_crossed_signal,
                f.pattern_trade_type,
                f.confluence_score,
                f.advisory_confidence_score,
                f.advisory_grade,
                f.tags
            FROM mmm_setup_signatures s
            JOIN mmm_event_outcomes o
              ON o.source = s.source AND o.source_id = s.source_id
            JOIN flashcards_db.flashcards f
              ON f.id = s.source_id
             AND f.snapshot_type = 'HISTORICAL'
            WHERE s.source = 'historical_flashcard'
              AND s.symbol = ?
              AND s.normalized_key = ?
            ORDER BY o.exit_pips DESC, o.max_favorable_pips DESC""",
            (symbol, normalized_key),
        ).fetchall()
    finally:
        conn.close()
    return [_row_dict(row) for row in rows]


def _select_rows(rows: list[dict[str, Any]], *, winner: bool, limit: int) -> list[dict[str, Any]]:
    if winner:
        selected = [
            row for row in rows
            if _optional_float(row.get("exit_pips")) is not None
            and float(row["exit_pips"]) > 0
            and row.get("replay_outcome") in FAVORABLE_OUTCOMES
        ]
        return selected[:limit]
    selected = [
        row for row in rows
        if _optional_float(row.get("exit_pips")) is not None
        and float(row["exit_pips"]) <= 0
    ]
    return sorted(
        selected,
        key=lambda row: (
            float(row.get("exit_pips") or 0.0),
            -float(row.get("max_adverse_pips") or 0.0),
        ),
    )[:limit]


def _packet_items(
    *,
    winners: list[dict[str, Any]],
    losers: list[dict[str, Any]],
    packet_dir: Path,
    image_dir: Path,
    copy_images: bool,
) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    cases = [
        {"label": "winner", "row": row}
        for row in winners
    ] + [
        {"label": "loser", "row": row}
        for row in losers
    ]
    cases = sorted(cases, key=_case_sort_key)
    for index, case in enumerate(cases, start=1):
        row = case["row"]
        label = str(case["label"])
        review_id = f"C{index:02d}"
        source_path = _resolve_chart_path(str(row.get("chart_path") or ""))
        image_name = _image_name(review_id, row)
        packet_image_path = image_dir / image_name
        if copy_images and source_path and source_path.exists():
            shutil.copy2(source_path, packet_image_path)
            image_path = packet_image_path.relative_to(packet_dir).as_posix()
        else:
            image_path = str(row.get("chart_path") or "")

        items.append(
            {
                "review_id": review_id,
                "label": label,
                "image_path": image_path,
                "source_chart_path": str(row.get("chart_path") or ""),
                "flashcard_id": row["flashcard_id"],
                "snapshot_at": row["snapshot_at"],
                "symbol": row["symbol"],
                "timeframe": row["timeframe"],
                "direction": row["direction"],
                "outcome": row["replay_outcome"],
                "exit_pips": _optional_float(row.get("exit_pips")),
                "max_favorable_pips": _optional_float(row.get("max_favorable_pips")),
                "max_adverse_pips": _optional_float(row.get("max_adverse_pips")),
                "t1_hit": bool(row.get("t1_hit")),
                "minutes_to_t1": _optional_float(row.get("minutes_to_t1")),
                "context": _context(row),
            }
        )
    return items


def _reset_packet_dir(packet_dir: Path, output_root: Path) -> None:
    output_root_abs = output_root.resolve()
    packet_abs = packet_dir.resolve()
    if output_root_abs not in (packet_abs, *packet_abs.parents):
        raise ValueError(f"Refusing to reset packet outside output root: {packet_dir}")
    if packet_dir.exists():
        shutil.rmtree(packet_dir)
    packet_dir.mkdir(parents=True, exist_ok=True)


def _case_sort_key(case: dict[str, Any]) -> str:
    row = case["row"]
    return hashlib.sha1(
        f"{row.get('flashcard_id')}|{row.get('snapshot_at')}".encode("utf-8")
    ).hexdigest()


def _write_packet_files(packet_dir: Path, manifest: dict[str, Any]) -> None:
    (packet_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    _write_answer_key(packet_dir / "answer_key.csv", manifest["items"])
    _write_review_matrix(packet_dir / "review_matrix.csv", manifest["items"])
    (packet_dir / "README.md").write_text(_packet_readme(manifest), encoding="utf-8")
    (packet_dir / "blind_prompt.md").write_text(_blind_prompt(manifest), encoding="utf-8")
    (packet_dir / "labeled_comparison_prompt.md").write_text(
        _labeled_prompt(manifest),
        encoding="utf-8",
    )


def _write_answer_key(path: Path, items: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "review_id",
                "label",
                "flashcard_id",
                "snapshot_at",
                "outcome",
                "exit_pips",
                "max_favorable_pips",
                "max_adverse_pips",
                "t1_hit",
                "image_path",
            ],
        )
        writer.writeheader()
        for item in items:
            writer.writerow({field: item.get(field, "") for field in writer.fieldnames})


def _write_review_matrix(path: Path, items: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "review_id",
                "predicted_label",
                "real_mmm_stop_hunt",
                "return_inside_asian_range",
                "clean_w_bottom",
                "second_leg_quality",
                "tdi_state_visible",
                "entry_timing",
                "reject_reason",
                "proposed_filter",
                "confidence_0_100",
            ],
        )
        writer.writeheader()
        for item in items:
            writer.writerow({"review_id": item["review_id"]})


def _write_index(output_root: Path, rows: list[dict[str, Any]]) -> None:
    lines = [
        "# MMM Vision Review Packets",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        "These packets are for winner-vs-loser visual isolation. They do not promote rules.",
        "",
        "| Pair | Packet | N | Fav% | AvgExit | Winners | Losers | Setup |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        packet = Path(row["packet"])
        lines.append(
            f"| {row['symbol']} | [{packet.name}](./{packet.name}/README.md) | "
            f"{row['total']} | {_fmt_pct(row['favorable_rate'])} | "
            f"{_fmt_plain(row['avg_exit_pips'])} | {row['winners']} | {row['losers']} | "
            f"{_md_cell(row['normalized_key'])} |"
        )
    if not rows:
        lines.append("| - | - | - | - | - | - | - | No packets generated. |")
    (output_root / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _packet_readme(manifest: dict[str, Any]) -> str:
    performance = manifest["setup_performance"]
    return "\n".join(
        [
            f"# {manifest['symbol']} Vision Review Packet",
            "",
            f"Generated: {manifest['generated_at']}",
            "",
            "Purpose: isolate visual differences between winning and losing versions of the same MMM setup signature.",
            "",
            "## Setup",
            "",
            f"- Pair: `{manifest['symbol']}`",
            f"- Signature: `{manifest['normalized_key']}`",
            f"- Total replay samples: {performance.get('total')}",
            f"- Favorable rate: {_fmt_pct(performance.get('favorable_rate'))}",
            f"- Average exit: {_fmt_plain(performance.get('avg_exit_pips'))} pips",
            f"- Winners in packet: {manifest['counts']['winners']}",
            f"- Losers in packet: {manifest['counts']['losers']}",
            "",
            "## Review Flow",
            "",
            "1. Open `blind_prompt.md` and attach the images from `images/`.",
            "2. Ask ChatGPT Pro and Claude Max to classify each chart without `answer_key.csv`.",
            "3. Then open `labeled_comparison_prompt.md` with `answer_key.csv` and ask for winner-vs-loser visual filters.",
            "4. Convert agreed filters into deterministic replay rules before any promotion.",
            "",
            "## Files",
            "",
            "- `manifest.json`: full packet metadata.",
            "- `answer_key.csv`: outcome labels; hide during blind review.",
            "- `review_matrix.csv`: fillable model-review table.",
            "- `blind_prompt.md`: first-pass model prompt.",
            "- `labeled_comparison_prompt.md`: second-pass explanation prompt.",
            "",
        ]
    )


def _blind_prompt(manifest: dict[str, Any]) -> str:
    image_lines = [
        f"- {item['review_id']}: `{item['image_path']}`"
        for item in manifest["items"]
    ]
    return "\n".join(
        [
            "You are reviewing MMM trading flashcards blind. Do not use `answer_key.csv`.",
            "",
            "Task: inspect each chart image and predict whether the setup was likely a winner or loser.",
            "",
            f"Pair: {manifest['symbol']}",
            f"Shared setup signature: {manifest['normalized_key']}",
            "",
            "Images:",
            *image_lines,
            "",
            "For each image, return a JSON array. Each object must contain:",
            "`review_id`, `predicted_label`, `confidence_0_100`, `real_mmm_stop_hunt`, "
            "`return_inside_asian_range`, `clean_w_bottom`, `second_leg_quality`, "
            "`tdi_state_visible`, `entry_timing`, `reject_reason`, and `proposed_filter`.",
            "",
            "Use only visual evidence from the chart. Be conservative: if the entry is unclear, label it loser.",
            "",
        ]
    )


def _labeled_prompt(manifest: dict[str, Any]) -> str:
    return "\n".join(
        [
            "You are now allowed to use `answer_key.csv` after completing the blind review.",
            "",
            "Compare winners against losers for this exact same MMM setup signature.",
            "",
            f"Pair: {manifest['symbol']}",
            f"Shared setup signature: {manifest['normalized_key']}",
            "",
            "Goal: identify the visual/structural filters that separate profitable examples from failed examples.",
            "",
            "Return a concise JSON object with:",
            "`summary`, `winner_traits`, `loser_traits`, `filters_to_test`, "
            "`filters_to_reject`, `pair_specific_notes`, `uncertain_items`, and `next_backtest_spec`.",
            "",
            "Each `filters_to_test` item must be deterministic enough for Codex to encode. Include measurable thresholds where possible, such as candles, pips, ratios, relative position to Asian range, or TDI state.",
            "",
            "Do not recommend live trading. These are research filters only.",
            "",
        ]
    )


def _context(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "weekly_phase": row.get("weekly_phase"),
        "weekly_trend": row.get("weekly_trend"),
        "h4_level": row.get("h4_level"),
        "h4_trend": row.get("h4_trend"),
        "h1_session": row.get("h1_session"),
        "h1_trend": row.get("h1_trend"),
        "asian_range_pips": _optional_float(row.get("asian_range_pips")),
        "stop_hunt_detected": bool(row.get("stop_hunt_detected")),
        "stop_hunt_direction": row.get("stop_hunt_direction"),
        "stop_hunt_pips": _optional_float(row.get("stop_hunt_pips")),
        "push_count": row.get("push_count"),
        "m_w_pattern": row.get("m_w_pattern"),
        "rrt_detected": bool(row.get("rrt_detected")),
        "tdi_signals": _load_json_list(row.get("tdi_signals")),
        "tdi_shark_fin": bool(row.get("tdi_shark_fin")),
        "tdi_shark_direction": row.get("tdi_shark_direction"),
        "tdi_vb_squeeze": bool(row.get("tdi_vb_squeeze")),
        "tdi_divergence": row.get("tdi_divergence"),
        "tdi_crossed_signal": row.get("tdi_crossed_signal"),
        "pattern_trade_type": row.get("pattern_trade_type"),
        "confluence_score": row.get("confluence_score"),
        "advisory_confidence_score": _optional_float(row.get("advisory_confidence_score")),
        "advisory_grade": row.get("advisory_grade"),
        "ratios": _load_json_dict(row.get("ratios")),
        "theme_tags": _load_json_list(row.get("theme_tags")),
        "event_path": _load_json_list(row.get("event_path")),
        "tags": _load_json_list(row.get("tags")),
    }


def _packet_dir(output_root: Path, symbol: str, normalized_key: str) -> Path:
    digest = hashlib.sha1(normalized_key.encode("utf-8")).hexdigest()[:10]
    parts = normalized_key.split("|")
    summary = "_".join(parts[:5]).lower()
    safe = "".join(ch if ch.isalnum() or ch in ("_", "-") else "_" for ch in summary)
    return output_root / f"{symbol}_{safe}_{digest}"


def _image_name(review_id: str, row: dict[str, Any]) -> str:
    snapshot = str(row.get("snapshot_at") or "").replace(":", "").replace("-", "")[:15]
    source = Path(str(row.get("chart_path") or "chart.png"))
    suffix = source.suffix if source.suffix else ".png"
    return f"{review_id.lower()}_fc{row['flashcard_id']}_{snapshot}{suffix}"


def _resolve_chart_path(raw: str) -> Optional[Path]:
    if not raw:
        return None
    path = Path(raw)
    if path.is_absolute():
        return path
    return Path.cwd() / path


def _row_dict(row: sqlite3.Row) -> dict[str, Any]:
    return {key: row[key] for key in row.keys()}


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


def _fmt_pct(value: Any) -> str:
    number = _optional_float(value)
    return "-" if number is None else f"{number:.1f}%"


def _fmt_plain(value: Any) -> str:
    number = _optional_float(value)
    return "-" if number is None else f"{number:+.1f}"


def _md_cell(value: Any) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def _parse_symbols(raw: str) -> tuple[str, ...]:
    return tuple(symbol.strip().upper() for symbol in raw.split(",") if symbol.strip())


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Build MMM vision review packets")
    parser.add_argument("--symbols", default=DEFAULT_SYMBOLS)
    parser.add_argument("--flashcards-db", type=Path, default=DEFAULT_FLASHCARDS_DB)
    parser.add_argument("--replay-db", type=Path, default=DEFAULT_REPLAY_DB)
    parser.add_argument("--pair-research-root", type=Path, default=DEFAULT_PAIR_RESEARCH_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--min-total", type=int, default=10)
    parser.add_argument("--min-favorable-rate", type=float, default=55.0)
    parser.add_argument("--min-avg-exit-pips", type=float, default=0.0)
    parser.add_argument("--max-setups-per-pair", type=int, default=3)
    parser.add_argument("--winners-per-setup", type=int, default=8)
    parser.add_argument("--losers-per-setup", type=int, default=8)
    parser.add_argument("--no-copy-images", action="store_true")
    args = parser.parse_args(argv)

    packets = build_review_packets(
        PacketConfig(
            flashcards_db=args.flashcards_db,
            replay_db=args.replay_db,
            pair_research_root=args.pair_research_root,
            output_root=args.output_root,
            symbols=_parse_symbols(args.symbols),
            min_total=args.min_total,
            min_favorable_rate=args.min_favorable_rate,
            min_avg_exit_pips=args.min_avg_exit_pips,
            max_setups_per_pair=args.max_setups_per_pair,
            winners_per_setup=args.winners_per_setup,
            losers_per_setup=args.losers_per_setup,
            copy_images=not args.no_copy_images,
        )
    )
    print(f"Wrote {len(packets)} vision review packet(s) to {args.output_root}")


if __name__ == "__main__":
    main()
