"""Run MMM vision review packets through authenticated local account CLIs.

This module intentionally avoids API keys. It calls the user's logged-in Codex
and Claude Code sessions, stores each blind/labeled review under the packet's
`reviews/` directory, then scores blind predictions against `answer_key.csv`.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

DEFAULT_PACKET_ROOT = Path("data/mmm_training/vision_review_packets")
BASE_DIR = Path(__file__).resolve().parents[2]
PROVIDER_LABELS = {
    "codex": "Codex / ChatGPT Pro",
    "claude": "Claude Max",
}
REVIEW_FILES = {
    ("codex", "blind"): "codex_blind.md",
    ("codex", "labeled"): "codex_labeled_comparison.md",
    ("claude", "blind"): "claude_blind.md",
    ("claude", "labeled"): "claude_labeled_comparison.md",
}


@dataclass(frozen=True)
class ReviewRunConfig:
    packet_root: Path = DEFAULT_PACKET_ROOT
    packet_names: tuple[str, ...] = ()
    providers: tuple[str, ...] = ("codex", "claude")
    stages: tuple[str, ...] = ("blind", "labeled")
    force: bool = False
    timeout_seconds: int = 900


@dataclass(frozen=True)
class BlindScore:
    provider: str
    correct: int
    total: int
    misses: tuple[str, ...]
    predictions_found: int
    status: str

    @property
    def accuracy(self) -> float:
        return self.correct / self.total * 100.0 if self.total else 0.0


def run_account_reviews(config: ReviewRunConfig) -> list[Path]:
    written: list[Path] = []
    for packet_dir in _packet_dirs(config.packet_root, config.packet_names):
        reviews_dir = packet_dir / "reviews"
        reviews_dir.mkdir(exist_ok=True)

        if "blind" in config.stages:
            prompt_path = reviews_dir / "blind_prompt_full.md"
            prompt_path.write_text(_blind_prompt(packet_dir), encoding="utf-8")
            written.append(prompt_path)
            for provider in config.providers:
                written.extend(
                    _run_stage(
                        provider=provider,
                        stage="blind",
                        packet_dir=packet_dir,
                        force=config.force,
                        timeout_seconds=config.timeout_seconds,
                    )
                )

        if "labeled" in config.stages:
            prompt_path = reviews_dir / "labeled_prompt_full.md"
            prompt_path.write_text(_labeled_prompt(packet_dir), encoding="utf-8")
            written.append(prompt_path)
            for provider in config.providers:
                written.extend(
                    _run_stage(
                        provider=provider,
                        stage="labeled",
                        packet_dir=packet_dir,
                        force=config.force,
                        timeout_seconds=config.timeout_seconds,
                    )
                )

        written.append(write_model_comparison_summary(packet_dir))

    written.append(write_model_review_index(config.packet_root))
    return written


def write_model_comparison_summary(packet_dir: Path) -> Path:
    manifest = _load_manifest(packet_dir)
    scores = [
        _score_blind(packet_dir, "codex"),
        _score_blind(packet_dir, "claude"),
    ]
    packet_name = packet_dir.name
    summary_path = packet_dir / "reviews" / "model_comparison_summary.md"
    lines = [
        f"# {manifest.get('symbol', packet_name)} Packet Vision Review Summary",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        f"Packet: `{packet_name}`",
        "",
        "## Blind Accuracy",
        "",
        "| Model | Correct | Total | Accuracy | Predictions Found | Misses | Status |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for score in scores:
        misses = ", ".join(score.misses) if score.misses else "-"
        lines.append(
            f"| {PROVIDER_LABELS[score.provider]} | {score.correct} | {score.total} | "
            f"{score.accuracy:.1f}% | {score.predictions_found} | {misses} | {score.status} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Blind accuracy measures whether the account model separated historical winners from losers before seeing outcomes.",
            "- Labeled comparisons are hypothesis sources only; filters still require deterministic replay validation.",
            "- No setup should be promoted from these packet reviews without train/validation/out-of-sample confirmation.",
            "",
        ]
    )
    summary_path.write_text("\n".join(lines), encoding="utf-8")
    return summary_path


def write_model_review_index(packet_root: Path = DEFAULT_PACKET_ROOT) -> Path:
    rows: list[dict[str, Any]] = []
    for packet_dir in _packet_dirs(packet_root, ()):
        manifest = _load_manifest(packet_dir)
        rows.append(
            {
                "symbol": manifest.get("symbol", "-"),
                "packet": packet_dir.name,
                "codex": _score_blind(packet_dir, "codex"),
                "claude": _score_blind(packet_dir, "claude"),
            }
        )

    lines = [
        "# Vision Model Review Index",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        "| Pair | Packet | Codex Blind | Claude Blind |",
        "|---|---|---:|---:|",
    ]
    for row in rows:
        codex = row["codex"]
        claude = row["claude"]
        lines.append(
            f"| {row['symbol']} | [{row['packet']}](./{row['packet']}/reviews/model_comparison_summary.md) | "
            f"{_score_cell(codex)} | {_score_cell(claude)} |"
        )
    if not rows:
        lines.append("| - | - | - | - |")

    path = packet_root / "MODEL_REVIEW_INDEX.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _run_stage(
    *,
    provider: str,
    stage: str,
    packet_dir: Path,
    force: bool,
    timeout_seconds: int,
) -> list[Path]:
    if provider not in PROVIDER_LABELS:
        raise ValueError(f"Unsupported provider: {provider}")
    if stage not in ("blind", "labeled"):
        raise ValueError(f"Unsupported stage: {stage}")

    reviews_dir = packet_dir / "reviews"
    reviews_dir.mkdir(exist_ok=True)
    output_path = reviews_dir / REVIEW_FILES[(provider, stage)]
    if output_path.exists() and not force:
        return []

    prompt = _blind_prompt(packet_dir) if stage == "blind" else _labeled_prompt(packet_dir)
    if provider == "codex":
        return [_run_codex(packet_dir, prompt, output_path, timeout_seconds)]
    prompt_file = packet_dir / "reviews" / f"{stage}_prompt_full.md"
    return [_run_claude(packet_dir, stage, prompt_file, output_path, timeout_seconds)]


def _run_codex(
    packet_dir: Path,
    prompt: str,
    output_path: Path,
    timeout_seconds: int,
) -> Path:
    stdout_path = output_path.with_suffix(".stdout.txt")
    command = [
        _resolve_executable("codex"),
        "exec",
        "--cd",
        str(BASE_DIR),
        "--sandbox",
        "read-only",
        "--output-last-message",
        str(output_path),
    ]
    for image_path in _image_paths(packet_dir):
        command.append(f"--image={image_path}")
    command.append("-")

    result = subprocess.run(
        command,
        cwd=str(BASE_DIR),
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        timeout=timeout_seconds,
        check=False,
    )
    stdout_path.write_text(result.stdout + result.stderr, encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(
            f"Codex review failed for {packet_dir.name} with code {result.returncode}. "
            f"See {stdout_path}"
        )
    return output_path


def _run_claude(
    packet_dir: Path,
    stage: str,
    prompt_file: Path,
    output_path: Path,
    timeout_seconds: int,
) -> Path:
    stdout_path = output_path.with_suffix(".stdout.txt")
    prompt = (
        f"Read this instruction file and follow it exactly: {prompt_file.resolve()}\n"
        f"Review only this one packet: {packet_dir.name}\n"
        "Do not inspect sibling packet directories or produce instructions to save multiple files.\n"
        f"Output only the requested {stage} JSON payload to stdout."
    )
    command = [
        _resolve_executable("claude"),
        "--print",
        "--model",
        "opus",
        "--system-prompt",
        "You are a strict single-packet MMM research review runner. Return only the requested JSON payload with no markdown, no prose wrapper, and no file-saving instructions.",
        "--permission-mode",
        "dontAsk",
        "--tools=Read",
        "--output-format",
        "text",
        prompt,
    ]
    result = subprocess.run(
        command,
        cwd=str(BASE_DIR),
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        timeout=timeout_seconds,
        check=False,
    )
    stdout_path.write_text(result.stderr, encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(
            f"Claude review failed with code {result.returncode}. See {stdout_path}"
        )
    output_path.write_text(result.stdout, encoding="utf-8")
    return output_path


def _blind_prompt(packet_dir: Path) -> str:
    prompt = _read_text_flexible(packet_dir / "blind_prompt.md")
    return "\n".join(
        [
            "You are running an account-backed MMM vision packet review.",
            f"Packet directory: {packet_dir.resolve()}",
            "",
            "Inspect only the chart images listed below. Do not read `answer_key.csv`, `manifest.json`, or outcome labels.",
            "",
            "Local chart images:",
            *_image_prompt_lines(packet_dir),
            "",
            prompt,
            "",
            "Return only the requested JSON array. Do not include markdown fences or prose.",
            "",
        ]
    )


def _labeled_prompt(packet_dir: Path) -> str:
    reviews_dir = packet_dir / "reviews"
    prompt = _read_text_flexible(packet_dir / "labeled_comparison_prompt.md")
    codex_blind = _optional_text(reviews_dir / "codex_blind.md")
    claude_blind = _optional_text(reviews_dir / "claude_blind.md")
    return "\n".join(
        [
            "Use the Read tool to inspect the local chart images when needed.",
            f"Packet directory: {packet_dir.resolve()}",
            "",
            prompt,
            "",
            "Local chart images:",
            *_image_prompt_lines(packet_dir),
            "",
            "Answer key:",
            _read_text_flexible(packet_dir / "answer_key.csv"),
            "",
            "Blind Codex review:",
            codex_blind or "(not available)",
            "",
            "Blind Claude review:",
            claude_blind or "(not available)",
            "",
            "Return only the requested concise JSON object. Do not recommend live trading.",
            "",
        ]
    )


def _score_blind(packet_dir: Path, provider: str) -> BlindScore:
    output_path = packet_dir / "reviews" / REVIEW_FILES[(provider, "blind")]
    answer_key = _answer_key(packet_dir / "answer_key.csv")
    if not output_path.exists():
        return BlindScore(
            provider=provider,
            correct=0,
            total=len(answer_key),
            misses=tuple(answer_key),
            predictions_found=0,
            status="missing review",
        )

    try:
        predictions = _extract_prediction_array(_read_text_flexible(output_path))
    except ValueError as exc:
        return BlindScore(
            provider=provider,
            correct=0,
            total=len(answer_key),
            misses=tuple(answer_key),
            predictions_found=0,
            status=f"unparsed: {exc}",
        )

    predicted_by_id = {
        str(row.get("review_id") or "").strip(): _normalize_label(row.get("predicted_label"))
        for row in predictions
        if isinstance(row, dict)
    }
    misses: list[str] = []
    correct = 0
    for review_id, label in answer_key.items():
        predicted = predicted_by_id.get(review_id)
        if predicted == label:
            correct += 1
        else:
            misses.append(review_id)

    return BlindScore(
        provider=provider,
        correct=correct,
        total=len(answer_key),
        misses=tuple(misses),
        predictions_found=len(predicted_by_id),
        status="ok",
    )


def _extract_prediction_array(raw: str) -> list[dict[str, Any]]:
    text = raw.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
    start = text.find("[")
    end = text.rfind("]")
    if start < 0 or end < start:
        raise ValueError("no JSON array found")
    try:
        parsed = json.loads(text[start : end + 1])
    except json.JSONDecodeError as exc:
        raise ValueError(str(exc)) from exc
    if not isinstance(parsed, list):
        raise ValueError("JSON payload is not an array")
    return [row for row in parsed if isinstance(row, dict)]


def _answer_key(path: Path) -> dict[str, str]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        rows = csv.DictReader(handle)
        return {
            str(row.get("review_id") or "").strip(): _normalize_label(row.get("label"))
            for row in rows
            if row.get("review_id")
        }


def _packet_dirs(packet_root: Path, packet_names: tuple[str, ...]) -> list[Path]:
    if packet_names:
        dirs = [packet_root / name for name in packet_names]
    else:
        dirs = sorted(path for path in packet_root.iterdir() if path.is_dir())
    return [path for path in dirs if (path / "manifest.json").exists()]


def _load_manifest(packet_dir: Path) -> dict[str, Any]:
    return json.loads(_read_text_flexible(packet_dir / "manifest.json"))


def _image_paths(packet_dir: Path) -> list[Path]:
    manifest = _load_manifest(packet_dir)
    paths: list[Path] = []
    for item in manifest.get("items", []):
        if not isinstance(item, dict):
            continue
        raw_path = str(item.get("image_path") or "")
        image_path = packet_dir / raw_path
        if image_path.exists():
            paths.append(image_path.resolve())
    return paths


def _image_prompt_lines(packet_dir: Path) -> list[str]:
    manifest = _load_manifest(packet_dir)
    lines: list[str] = []
    for item in manifest.get("items", []):
        if not isinstance(item, dict):
            continue
        review_id = str(item.get("review_id") or "").strip()
        raw_path = str(item.get("image_path") or "")
        if not review_id or not raw_path:
            continue
        lines.append(f"- {review_id}: `{(packet_dir / raw_path).resolve()}`")
    return lines


def _read_text_flexible(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-16")


def _optional_text(path: Path) -> str:
    return _read_text_flexible(path) if path.exists() else ""


def _resolve_executable(name: str) -> str:
    for candidate in (name, f"{name}.cmd", f"{name}.exe", f"{name}.ps1"):
        resolved = shutil.which(candidate)
        if resolved:
            return resolved
    raise FileNotFoundError(f"Unable to find executable for {name}")


def _normalize_label(value: Any) -> str:
    normalized = str(value or "").strip().lower()
    if "winner" in normalized or normalized in {"win", "profitable", "profit"}:
        return "winner"
    if "loser" in normalized or normalized in {"loss", "failed", "fail"}:
        return "loser"
    return normalized


def _score_cell(score: BlindScore) -> str:
    if score.status != "ok":
        return score.status
    return f"{score.correct}/{score.total} ({score.accuracy:.1f}%)"


def _parse_csv_arg(raw: str) -> tuple[str, ...]:
    return tuple(item.strip() for item in raw.split(",") if item.strip())


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Run MMM vision packets through account CLIs")
    parser.add_argument("--packet-root", type=Path, default=DEFAULT_PACKET_ROOT)
    parser.add_argument("--packets", default="", help="Comma-separated packet directory names")
    parser.add_argument("--providers", default="codex,claude", help="codex, claude, or both")
    parser.add_argument("--stages", default="blind,labeled", help="blind, labeled, or both")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--timeout-seconds", type=int, default=900)
    args = parser.parse_args(argv)

    written = run_account_reviews(
        ReviewRunConfig(
            packet_root=args.packet_root,
            packet_names=_parse_csv_arg(args.packets),
            providers=_parse_csv_arg(args.providers),
            stages=_parse_csv_arg(args.stages),
            force=args.force,
            timeout_seconds=args.timeout_seconds,
        )
    )
    print(f"Wrote or refreshed {len(written)} review artifact(s).")


if __name__ == "__main__":
    main()
