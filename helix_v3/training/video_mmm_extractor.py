"""MMM training-video extraction pipeline.

The goal is not to reproduce a proprietary course as a verbatim text copy. The
pipeline keeps local source references, timestamps, screenshots/keyframes, OCR,
and concise methodology notes that can be validated against market data.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from config.settings import BASE_DIR
from helix_v3.utils.logger import get_logger

logger = get_logger("video_mmm_extractor")

TRAINING_ROOT = BASE_DIR / "data" / "mmm_training"
VIDEO_DIR = TRAINING_ROOT / "videos"
FRAME_DIR = TRAINING_ROOT / "frames"
AUDIO_DIR = TRAINING_ROOT / "audio"
TRANSCRIPT_DIR = TRAINING_ROOT / "transcripts"
OCR_DIR = TRAINING_ROOT / "ocr"
RULE_DIR = TRAINING_ROOT / "rules"
NOTE_DIR = TRAINING_ROOT / "notes"
SKILL_DIR = TRAINING_ROOT / "skills"
VALIDATION_DIR = TRAINING_ROOT / "validation"
MODEL_DIR = TRAINING_ROOT / "models"
MANIFEST_PATH = TRAINING_ROOT / "manifest.json"

VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}


@dataclass(frozen=True)
class VideoAsset:
    id: str
    title: str
    path: str
    size_bytes: int
    modified_at: str
    duration_seconds: Optional[float] = None
    width: Optional[int] = None
    height: Optional[int] = None
    fps: Optional[float] = None
    probe_status: str = "not_probed"


@dataclass(frozen=True)
class RuleCard:
    rule_id: str
    title: str
    source_video: str
    start_time: str
    end_time: str
    summary: str
    timeframes: list[str] = field(default_factory=list)
    entry_conditions: list[str] = field(default_factory=list)
    exit_conditions: list[str] = field(default_factory=list)
    invalidation: list[str] = field(default_factory=list)
    visual_evidence: list[str] = field(default_factory=list)
    validation_status: str = "unvalidated"


@dataclass(frozen=True)
class TranscriptSegment:
    video_id: str
    start_ms: int
    end_ms: int
    text: str


@dataclass(frozen=True)
class MethodologyHit:
    video_id: str
    title: str
    start_ms: int
    end_ms: int
    score: int
    keywords: list[str]
    summary: str
    frame_hint: Optional[str] = None


METHODOLOGY_KEYWORDS = {
    "asian": 5,
    "accumulation": 6,
    "session": 3,
    "london": 3,
    "new york": 3,
    "stop hunt": 8,
    "stop": 2,
    "high of the day": 7,
    "low of the day": 7,
    "hod": 5,
    "lod": 5,
    "m formation": 8,
    "w formation": 8,
    "m pattern": 7,
    "w pattern": 7,
    "three pushes": 8,
    "push": 3,
    "level": 3,
    "levels": 3,
    "reset": 5,
    "ema": 4,
    "tdi": 6,
    "shark fin": 8,
    "reversal": 5,
    "continuation": 4,
    "entry": 6,
    "exit": 5,
    "target": 5,
    "profit": 2,
    "pip": 3,
    "pips": 3,
    "risk": 4,
    "stop loss": 7,
    "break even": 5,
    "breakeven": 5,
    "pair": 2,
    "yen": 2,
    "pound": 2,
    "euro": 2,
    "swiss": 2,
    "dollar": 2,
    "market maker": 6,
    "technical": 3,
    "trade plan": 7,
    "homework": 2,
    "chart": 3,
    "candle": 3,
    "trend": 4,
}

def ensure_training_dirs(root: Path = TRAINING_ROOT) -> None:
    for path in [
        root,
        root / "videos",
        root / "frames",
        root / "audio",
        root / "transcripts",
        root / "ocr",
        root / "rules",
        root / "notes",
        root / "skills",
        root / "validation",
        root / "models",
    ]:
        path.mkdir(parents=True, exist_ok=True)


def build_manifest(
    *,
    root: Path = TRAINING_ROOT,
    probe: bool = False,
    ffprobe_path: Optional[str] = None,
) -> list[VideoAsset]:
    ensure_training_dirs(root)
    video_dir = root / "videos"
    assets: list[VideoAsset] = []
    for index, path in enumerate(sorted(video_dir.iterdir()), start=1):
        if not path.is_file() or path.suffix.lower() not in VIDEO_EXTENSIONS:
            continue
        stat = path.stat()
        asset = VideoAsset(
            id=f"video_{index:03d}",
            title=path.stem.strip(),
            path=str(path.relative_to(root)),
            size_bytes=stat.st_size,
            modified_at=datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
        )
        if probe:
            asset = probe_video(asset, root=root, ffprobe_path=ffprobe_path)
        assets.append(asset)

    manifest_path = root / "manifest.json"
    manifest_path.write_text(
        json.dumps(
            {
                "created_at": datetime.now(timezone.utc).isoformat(),
                "content_policy": "Store concise methodology notes and source references; avoid full redistributed course transcripts.",
                "videos": [asdict(asset) for asset in assets],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    write_source_index(assets, root=root)
    return assets


def probe_video(
    asset: VideoAsset,
    *,
    root: Path = TRAINING_ROOT,
    ffprobe_path: Optional[str] = None,
) -> VideoAsset:
    ffprobe = ffprobe_path or shutil.which("ffprobe")
    if not ffprobe:
        return _replace_asset(asset, probe_status="ffprobe_missing")

    path = root / asset.path
    cmd = [
        ffprobe,
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,r_frame_rate:format=duration",
        "-of",
        "json",
        str(path),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout or "{}")
    except (subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        logger.warning("ffprobe failed for %s: %s", path, exc)
        return _replace_asset(asset, probe_status="probe_failed")

    stream = (data.get("streams") or [{}])[0]
    duration = _optional_float((data.get("format") or {}).get("duration"))
    fps = _parse_rate(stream.get("r_frame_rate"))
    return _replace_asset(
        asset,
        duration_seconds=duration,
        width=_optional_int(stream.get("width")),
        height=_optional_int(stream.get("height")),
        fps=fps,
        probe_status="ok",
    )


def extract_audio(
    *,
    root: Path = TRAINING_ROOT,
    ffmpeg_path: Optional[str] = None,
    overwrite: bool = False,
) -> list[Path]:
    assets = load_manifest(root=root)
    ffmpeg = ffmpeg_path or shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg is not available on PATH. Install ffmpeg or pass --ffmpeg-path.")

    outputs: list[Path] = []
    for asset in assets:
        source = root / asset.path
        out = root / "audio" / f"{asset.id}.wav"
        if out.exists() and not overwrite:
            outputs.append(out)
            continue
        cmd = [
            ffmpeg,
            "-y" if overwrite else "-n",
            "-i",
            str(source),
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            str(out),
        ]
        subprocess.run(cmd, check=True)
        outputs.append(out)
    return outputs


def extract_frames(
    *,
    root: Path = TRAINING_ROOT,
    ffmpeg_path: Optional[str] = None,
    every_seconds: int = 30,
    overwrite: bool = False,
) -> list[Path]:
    assets = load_manifest(root=root)
    ffmpeg = ffmpeg_path or shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg is not available on PATH. Install ffmpeg or pass --ffmpeg-path.")

    output_dirs: list[Path] = []
    for asset in assets:
        source = root / asset.path
        out_dir = root / "frames" / asset.id
        out_dir.mkdir(parents=True, exist_ok=True)
        if any(out_dir.glob("frame_*.jpg")) and not overwrite:
            output_dirs.append(out_dir)
            continue
        cmd = [
            ffmpeg,
            "-y" if overwrite else "-n",
            "-i",
            str(source),
            "-vf",
            f"fps=1/{every_seconds}",
            "-q:v",
            "2",
            str(out_dir / "frame_%06d.jpg"),
        ]
        subprocess.run(cmd, check=True)
        output_dirs.append(out_dir)
    return output_dirs


def transcribe_audio(
    *,
    root: Path = TRAINING_ROOT,
    model_path: Optional[str] = None,
    ffmpeg_path: Optional[str] = None,
    language: str = "en",
    output_format: str = "json",
    overwrite: bool = False,
    use_gpu: bool = False,
    video_ids: Optional[list[str]] = None,
) -> list[Path]:
    assets = _filter_assets(load_manifest(root=root), video_ids)
    ffmpeg = ffmpeg_path or shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg is not available on PATH. Install ffmpeg or pass --ffmpeg-path.")

    model = Path(model_path).resolve() if model_path else root / "models" / "ggml-base.en.bin"
    if not model.exists():
        raise FileNotFoundError(
            f"Whisper model not found: {model}. Download a whisper.cpp ggml model first."
        )

    if output_format not in {"json", "srt", "text"}:
        raise ValueError("output_format must be one of: json, srt, text")

    extension = "txt" if output_format == "text" else output_format
    outputs: list[Path] = []
    for asset in assets:
        source = root / "audio" / f"{asset.id}.wav"
        if not source.exists():
            raise FileNotFoundError(f"Audio not found for {asset.id}: {source}. Run extract-audio.")

        out = root / "transcripts" / f"{asset.id}.{extension}"
        if out.exists() and not overwrite:
            outputs.append(out)
            continue

        whisper_filter = ":".join(
            [
                f"whisper=model={_ffmpeg_filter_path(model, cwd=root)}",
                f"language={language}",
                f"destination={_ffmpeg_filter_path(out, cwd=root)}",
                f"format={output_format}",
                f"use_gpu={'true' if use_gpu else 'false'}",
            ]
        )
        cmd = [
            ffmpeg,
            "-hide_banner",
            "-i",
            str(source),
            "-af",
            whisper_filter,
            "-f",
            "null",
            "-",
        ]
        subprocess.run(cmd, cwd=str(root), check=True)
        outputs.append(out)
    return outputs


def initialize_methodology_files(*, root: Path = TRAINING_ROOT) -> None:
    ensure_training_dirs(root)
    assets = load_manifest(root=root, missing_ok=True)
    if not assets:
        assets = build_manifest(root=root, probe=False)

    write_methodology_index(assets, root=root)
    write_notes_templates(assets, root=root)
    write_rule_templates(root=root)
    write_skill_documents(root=root)
    write_validation_plan(root=root)


def build_transcript_index(
    *,
    root: Path = TRAINING_ROOT,
    window_seconds: int = 180,
    min_score: int = 10,
    top_limit: int = 80,
) -> list[MethodologyHit]:
    assets = load_manifest(root=root)
    hits: list[MethodologyHit] = []
    for asset in assets:
        segments = load_transcript_segments(asset.id, root=root)
        hits.extend(
            score_transcript_windows(
                segments=segments,
                asset=asset,
                root=root,
                window_seconds=window_seconds,
                min_score=min_score,
            )
        )

    hits = sorted(hits, key=lambda item: (-item.score, item.video_id, item.start_ms))[:top_limit]
    write_transcript_index(hits, root=root)
    return hits


def load_transcript_segments(video_id: str, *, root: Path = TRAINING_ROOT) -> list[TranscriptSegment]:
    path = root / "transcripts" / f"{video_id}.json"
    if not path.exists():
        return []

    segments: list[TranscriptSegment] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        data = parse_transcript_line(line, path=path, line_number=line_number)
        segments.append(
            TranscriptSegment(
                video_id=video_id,
                start_ms=int(data["start"]),
                end_ms=int(data["end"]),
                text=str(data["text"]).strip(),
            )
        )
    return segments


def parse_transcript_line(line: str, *, path: Path, line_number: int) -> dict[str, Any]:
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        # ffmpeg's whisper filter can emit unescaped double quotes inside text.
        match = re.fullmatch(r'\{"start":\s*(\d+),\s*"end":\s*(\d+),\s*"text":"(.*)"\}', line)
        if match:
            return {
                "start": int(match.group(1)),
                "end": int(match.group(2)),
                "text": match.group(3),
            }
    raise ValueError(f"Invalid transcript JSON at {path}:{line_number}")


def score_transcript_windows(
    *,
    segments: list[TranscriptSegment],
    asset: VideoAsset,
    root: Path = TRAINING_ROOT,
    window_seconds: int = 180,
    min_score: int = 10,
) -> list[MethodologyHit]:
    if not segments:
        return []

    window_ms = window_seconds * 1000
    windows: list[MethodologyHit] = []
    index = 0
    while index < len(segments):
        start_ms = segments[index].start_ms
        end_ms = start_ms + window_ms
        bucket: list[TranscriptSegment] = []
        while index < len(segments) and segments[index].start_ms < end_ms:
            bucket.append(segments[index])
            index += 1

        text = " ".join(segment.text for segment in bucket)
        score, keywords = score_methodology_text(text)
        if score >= min_score:
            windows.append(
                MethodologyHit(
                    video_id=asset.id,
                    title=asset.title,
                    start_ms=bucket[0].start_ms,
                    end_ms=bucket[-1].end_ms,
                    score=score,
                    keywords=keywords,
                    summary=summarize_methodology_keywords(keywords),
                    frame_hint=nearest_frame_hint(
                        video_id=asset.id,
                        start_ms=bucket[0].start_ms,
                        root=root,
                    ),
                )
            )
    return windows


def score_methodology_text(text: str) -> tuple[int, list[str]]:
    lowered = text.lower()
    matched: list[str] = []
    score = 0
    for keyword, weight in METHODOLOGY_KEYWORDS.items():
        if keyword in lowered:
            matched.append(keyword)
            score += weight
    return score, matched


def summarize_methodology_keywords(keywords: list[str], *, max_keywords: int = 8) -> str:
    if not keywords:
        return "Methodology relevance detected by context."
    visible = keywords[:max_keywords]
    return f"Methodology discussion involving: {', '.join(visible)}."


def nearest_frame_hint(
    *,
    video_id: str,
    start_ms: int,
    root: Path = TRAINING_ROOT,
    every_seconds: int = 30,
) -> Optional[str]:
    frame_index = int(round((start_ms / 1000) / every_seconds)) + 1
    frame_path = root / "frames" / video_id / f"frame_{frame_index:06d}.jpg"
    if frame_path.exists():
        return str(frame_path.relative_to(root))
    return None


def write_transcript_index(hits: list[MethodologyHit], *, root: Path = TRAINING_ROOT) -> Path:
    path = root / "transcript_index.md"
    lines = [
        "# MMM Transcript Methodology Index",
        "",
        "This is a pointer index into local transcripts. It intentionally avoids full transcript reproduction.",
        "",
        "| Video | Time | Score | Keywords | Frame | Summary |",
        "|---|---:|---:|---|---|---|",
    ]
    for hit in hits:
        frame = f"`{hit.frame_hint}`" if hit.frame_hint else ""
        lines.append(
            f"| {hit.video_id} | {format_timestamp(hit.start_ms)}-{format_timestamp(hit.end_ms)} | "
            f"{hit.score} | {', '.join(hit.keywords[:8])} | {frame} | {hit.summary} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def format_timestamp(milliseconds: int) -> str:
    total_seconds = milliseconds // 1000
    minutes_total, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes_total, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def write_source_index(assets: list[VideoAsset], *, root: Path = TRAINING_ROOT) -> Path:
    lines = [
        "# MMM Training Source Index",
        "",
        "This index references local video sources. Do not paste full course transcripts here.",
        "",
        "| ID | Title | File | Size MB | Probe | Duration |",
        "|---|---|---|---:|---|---:|",
    ]
    for asset in assets:
        duration = "" if asset.duration_seconds is None else f"{asset.duration_seconds:.1f}s"
        lines.append(
            f"| {asset.id} | {asset.title} | `{asset.path}` | "
            f"{asset.size_bytes / 1_000_000:.1f} | {asset.probe_status} | {duration} |"
        )
    path = root / "source_index.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_methodology_index(assets: list[VideoAsset], *, root: Path = TRAINING_ROOT) -> Path:
    lines = [
        "# Steve Mauro MMM Methodology Extraction Index",
        "",
        "Purpose: convert training videos into timestamped, testable MMM rules.",
        "",
        "Content boundary: notes should paraphrase methodology and preserve timestamps, screenshots, and evidence references. Avoid rebuilding the course as a full verbatim transcript.",
        "",
        "## Workflow",
        "",
        "1. Extract audio and keyframes.",
        "2. Build timestamped notes per video.",
        "3. Convert notes into rule cards.",
        "4. Map rule cards to flashcard fields and MMM replay signatures.",
        "5. Validate each rule against historical market behavior.",
        "6. Promote only validated rules into Claude/Codex skill documents.",
        "",
        "## Source Videos",
        "",
    ]
    for asset in assets:
        lines.append(f"- `{asset.id}`: {asset.title} (`{asset.path}`)")
    lines.extend(
        [
            "",
            "## Rule Status",
            "",
            "- `source_only`: observed in training, not converted into rule.",
            "- `candidate`: converted into setup/exit/management parameters.",
            "- `backtested`: replayed against market data.",
            "- `validated`: statistically useful enough to enter the validation library.",
            "- `rejected`: taught pattern did not correlate with market behavior under current tests.",
        ]
    )
    path = root / "methodology_index.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_notes_templates(assets: list[VideoAsset], *, root: Path = TRAINING_ROOT) -> list[Path]:
    outputs: list[Path] = []
    for asset in assets:
        path = root / "notes" / f"{asset.id}_{_slug(asset.title)}.md"
        if path.exists():
            outputs.append(path)
            continue
        lines = [
            f"# Notes: {asset.title}",
            "",
            f"Source: `{asset.path}`",
            f"Video ID: `{asset.id}`",
            "",
            "## Extraction Log",
            "",
            "| Start | End | Visual Evidence | Paraphrased Teaching | Candidate Rule ID | Validation Status |",
            "|---|---|---|---|---|---|",
            "| 00:00:00 | 00:00:00 |  |  |  | source_only |",
            "",
            "## Chart/Visual Observations",
            "",
            "- ",
            "",
            "## Setup Parameters Mentioned",
            "",
            "- Timeframes:",
            "- Session/window:",
            "- Entry trigger:",
            "- Stop/invalidation:",
            "- Target/management:",
            "- Examples requiring market validation:",
            "",
        ]
        path.write_text("\n".join(lines), encoding="utf-8")
        outputs.append(path)
    return outputs


def write_rule_templates(*, root: Path = TRAINING_ROOT) -> list[Path]:
    rules_path = root / "rules" / "steve_mauro_mmm_methodology.md"
    cards_path = root / "rules" / "rule_cards.md"

    if not rules_path.exists():
        rules_path.write_text(
            "\n".join(
                [
                    "# Steve Mauro MMM Methodology Notes",
                    "",
                    "This file is for distilled, timestamped methodology. Keep each item testable.",
                    "",
                    "## Top-Down Structure",
                    "",
                    "- Source timestamp:",
                    "- Teaching summary:",
                    "- Required market evidence:",
                    "- Backtest mapping:",
                    "",
                    "## Entry Models",
                    "",
                    "- Source timestamp:",
                    "- Setup:",
                    "- Entry conditions:",
                    "- Exit conditions:",
                    "- Invalidations:",
                    "- Validation status:",
                    "",
                    "## Trade Management",
                    "",
                    "- Source timestamp:",
                    "- Teaching summary:",
                    "- Market validation status:",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

    if not cards_path.exists():
        cards_path.write_text(
            "\n".join(
                [
                    "# MMM Rule Cards",
                    "",
                    "Each card should be a concise, testable rule. Example schema:",
                    "",
                    "```json",
                    json.dumps(
                        asdict(
                            RuleCard(
                                rule_id="MMM-001",
                                title="Example M/W stop-hunt reversal",
                                source_video="video_001",
                                start_time="00:00:00",
                                end_time="00:00:00",
                                summary="Paraphrased teaching goes here.",
                                timeframes=["D1", "H4", "H1", "M15"],
                                entry_conditions=[
                                    "Pair-specific Asian range is valid",
                                    "Stop hunt occurs beyond Asian range",
                                    "M/W formation confirms direction",
                                ],
                                exit_conditions=["T1 at 1R", "Trail after breakeven"],
                                invalidation=["Structural stop beyond setup"],
                                validation_status="candidate",
                            )
                        ),
                        indent=2,
                    ),
                    "```",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    return [rules_path, cards_path]


def write_skill_documents(*, root: Path = TRAINING_ROOT) -> list[Path]:
    codex_path = root / "skills" / "CODEX_MMM_STRATEGY.md"
    claude_path = root / "skills" / "CLAUDE_MMM_STRATEGY.md"
    body = "\n".join(
        [
            "# MMM Strategy Skill Draft",
            "",
            "Status: draft. Promote rules here only after they are timestamped and market-validated.",
            "",
            "## Operating Rules",
            "",
            "- Use MMM top-down context: Weekly/D1/H4 -> H1 -> M15.",
            "- Treat pair profiles as unique unless validation proves cross-pair convergence.",
            "- Do not accept training claims as trading rules until historical replay supports them.",
            "- Store setup evidence as flashcards with chart path, timestamp, rule ID, and outcome.",
            "",
            "## Validated Setup Library",
            "",
            "Populate from `logs/validation_library.db` after promotion.",
            "",
            "## Rejected Or Unproven Teachings",
            "",
            "Keep these out of live enforcement until replay improves.",
            "",
        ]
    )
    for path in (codex_path, claude_path):
        if not path.exists():
            path.write_text(body, encoding="utf-8")
    return [codex_path, claude_path]


def write_validation_plan(*, root: Path = TRAINING_ROOT) -> Path:
    path = root / "validation" / "market_validation_plan.md"
    if not path.exists():
        path.write_text(
            "\n".join(
                [
                    "# MMM Training vs Market Reality Validation Plan",
                    "",
                    "Every extracted teaching must pass through this validation layer before it becomes a strategy skill rule.",
                    "",
                    "## Validation Gates",
                    "",
                    "1. Source reference exists: video ID and timestamp.",
                    "2. Rule is parameterized: timeframe, setup, entry, exit, invalidation.",
                    "3. Rule maps to flashcard fields and MMM replay signature components.",
                    "4. Backtest sample is pair-specific first.",
                    "5. Cross-pair convergence is considered only after pair-specific evidence.",
                    "6. Rule is promoted only if replay outcomes beat the scanner baseline.",
                    "",
                    "## Metrics",
                    "",
                    "- favorable rate",
                    "- T1 hit rate",
                    "- average exit pips",
                    "- average MFE/MAE",
                    "- stale-exit rate",
                    "- ambiguity rate",
                    "- pair-specific sample size",
                    "",
                    "## Decisions",
                    "",
                    "- `validated`: promote to skill docs and validation library.",
                    "- `watch`: keep for more samples.",
                    "- `rejected`: keep as training-only context, not live logic.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
    return path


def load_manifest(*, root: Path = TRAINING_ROOT, missing_ok: bool = False) -> list[VideoAsset]:
    path = root / "manifest.json"
    if not path.exists():
        if missing_ok:
            return []
        raise FileNotFoundError(f"Manifest not found: {path}. Run manifest first.")
    data = json.loads(path.read_text(encoding="utf-8"))
    return [VideoAsset(**item) for item in data.get("videos", [])]


def _filter_assets(
    assets: list[VideoAsset],
    video_ids: Optional[list[str]],
) -> list[VideoAsset]:
    if not video_ids:
        return assets

    wanted = set(video_ids)
    selected = [asset for asset in assets if asset.id in wanted]
    found = {asset.id for asset in selected}
    missing = sorted(wanted - found)
    if missing:
        raise ValueError(f"Unknown video IDs: {', '.join(missing)}")
    return selected


def _replace_asset(asset: VideoAsset, **changes: Any) -> VideoAsset:
    data = asdict(asset)
    data.update(changes)
    return VideoAsset(**data)


def _parse_rate(value: Any) -> Optional[float]:
    if not value:
        return None
    text = str(value)
    if "/" in text:
        num, den = text.split("/", 1)
        denominator = _optional_float(den)
        if denominator:
            return (_optional_float(num) or 0.0) / denominator
    return _optional_float(text)


def _optional_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _optional_int(value: Any) -> Optional[int]:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _slug(value: str) -> str:
    chars = []
    for char in value.lower():
        if char.isalnum():
            chars.append(char)
        elif chars and chars[-1] != "_":
            chars.append("_")
    return "".join(chars).strip("_") or "video"


def _parse_root(value: Optional[str]) -> Path:
    return Path(value).resolve() if value else TRAINING_ROOT


def _ffmpeg_filter_path(path: Path, *, cwd: Path) -> str:
    resolved = path.resolve()
    try:
        value = resolved.relative_to(cwd.resolve()).as_posix()
    except ValueError:
        value = resolved.as_posix()
    return value.replace(":", r"\:").replace("'", r"\'")


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="MMM training-video extraction pipeline")
    parser.add_argument("--root", help="Training root directory", default=None)
    sub = parser.add_subparsers(dest="command", required=True)

    p_manifest = sub.add_parser("manifest", help="Create/update video manifest")
    p_manifest.add_argument("--probe", action="store_true", help="Probe video metadata with ffprobe")
    p_manifest.add_argument("--ffprobe-path")

    sub.add_parser("init-md", help="Create methodology markdown templates")

    p_audio = sub.add_parser("extract-audio", help="Extract 16k mono wav audio with ffmpeg")
    p_audio.add_argument("--ffmpeg-path")
    p_audio.add_argument("--overwrite", action="store_true")

    p_frames = sub.add_parser("extract-frames", help="Extract sampled keyframes with ffmpeg")
    p_frames.add_argument("--ffmpeg-path")
    p_frames.add_argument("--every-seconds", type=int, default=30)
    p_frames.add_argument("--overwrite", action="store_true")

    p_transcribe = sub.add_parser("transcribe", help="Transcribe extracted audio with ffmpeg whisper")
    p_transcribe.add_argument("--model-path")
    p_transcribe.add_argument("--ffmpeg-path")
    p_transcribe.add_argument("--language", default="en")
    p_transcribe.add_argument("--format", choices=["json", "srt", "text"], default="json")
    p_transcribe.add_argument("--overwrite", action="store_true")
    p_transcribe.add_argument("--use-gpu", action="store_true")
    p_transcribe.add_argument(
        "--video-id",
        action="append",
        dest="video_ids",
        help="Transcribe only this manifest video ID. Repeat for multiple IDs.",
    )

    p_index = sub.add_parser("transcript-index", help="Build methodology pointer index")
    p_index.add_argument("--window-seconds", type=int, default=180)
    p_index.add_argument("--min-score", type=int, default=10)
    p_index.add_argument("--top-limit", type=int, default=80)

    args = parser.parse_args(argv)
    root = _parse_root(args.root)

    if args.command == "manifest":
        assets = build_manifest(root=root, probe=args.probe, ffprobe_path=args.ffprobe_path)
        print(f"Wrote manifest for {len(assets)} videos: {root / 'manifest.json'}")
    elif args.command == "init-md":
        initialize_methodology_files(root=root)
        print(f"Initialized methodology markdown under {root}")
    elif args.command == "extract-audio":
        outputs = extract_audio(
            root=root,
            ffmpeg_path=args.ffmpeg_path,
            overwrite=args.overwrite,
        )
        print(f"Extracted/reused {len(outputs)} audio files.")
    elif args.command == "extract-frames":
        outputs = extract_frames(
            root=root,
            ffmpeg_path=args.ffmpeg_path,
            every_seconds=args.every_seconds,
            overwrite=args.overwrite,
        )
        print(f"Extracted/reused frames for {len(outputs)} videos.")
    elif args.command == "transcribe":
        outputs = transcribe_audio(
            root=root,
            model_path=args.model_path,
            ffmpeg_path=args.ffmpeg_path,
            language=args.language,
            output_format=args.format,
            overwrite=args.overwrite,
            use_gpu=args.use_gpu,
            video_ids=args.video_ids,
        )
        print(f"Transcribed/reused {len(outputs)} transcript files.")
    elif args.command == "transcript-index":
        hits = build_transcript_index(
            root=root,
            window_seconds=args.window_seconds,
            min_score=args.min_score,
            top_limit=args.top_limit,
        )
        print(f"Wrote {len(hits)} transcript methodology hits: {root / 'transcript_index.md'}")


if __name__ == "__main__":
    main()
