"""GPU transcription helper for MMM training videos in Google Colab.

This script is intentionally standalone: run it from a mounted Google Drive
folder that contains `data/mmm_training/manifest.json` plus either extracted
audio files or the source videos.

Example:
    python scripts/colab_transcribe_mmm.py \
        --root /content/drive/MyDrive/Helix_V3/data/mmm_training \
        --video-id video_002 \
        --model-size small.en \
        --device cuda \
        --compute-type float16
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Optional


@dataclass(frozen=True)
class ManifestAsset:
    id: str
    title: str
    path: str
    duration_seconds: Optional[float] = None


@dataclass(frozen=True)
class TranscriptSegment:
    start_ms: int
    end_ms: int
    text: str


def load_manifest(root: Path) -> list[ManifestAsset]:
    manifest_path = root / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")

    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    return [
        ManifestAsset(
            id=item["id"],
            title=item["title"],
            path=item["path"],
            duration_seconds=item.get("duration_seconds"),
        )
        for item in data.get("videos", [])
    ]


def select_assets(
    assets: list[ManifestAsset],
    video_ids: Optional[list[str]],
) -> list[ManifestAsset]:
    if not video_ids:
        return assets

    wanted = set(video_ids)
    selected = [asset for asset in assets if asset.id in wanted]
    missing = sorted(wanted - {asset.id for asset in selected})
    if missing:
        raise ValueError(f"Unknown video IDs: {', '.join(missing)}")
    return selected


def source_for_asset(root: Path, asset: ManifestAsset) -> Path:
    audio_path = root / "audio" / f"{asset.id}.wav"
    if audio_path.exists():
        return audio_path

    video_path = root / asset.path
    if video_path.exists():
        return video_path

    normalized_video_path = root / asset.path.replace("\\", "/")
    if normalized_video_path.exists():
        return normalized_video_path

    raise FileNotFoundError(f"No audio or video source found for {asset.id}")


def transcribe_asset(
    *,
    root: Path,
    asset: ManifestAsset,
    model: Any,
    beam_size: int,
    language: str,
    overwrite: bool,
    output_srt: bool,
    prepare_audio: bool,
    work_dir: Path,
    ffmpeg_path: Optional[str],
    max_duration_seconds: Optional[int],
    progress_seconds: int,
) -> Path:
    transcript_dir = root / "transcripts"
    transcript_dir.mkdir(parents=True, exist_ok=True)
    output_path = transcript_dir / f"{asset.id}.json"
    partial_path = output_path.with_suffix(".json.partial")
    if output_path.exists() and not overwrite:
        print(f"Reusing existing transcript: {output_path}")
        return output_path

    source_path = source_for_asset(root, asset)
    if prepare_audio:
        source_path = prepare_local_audio(
            source_path=source_path,
            asset=asset,
            work_dir=work_dir,
            ffmpeg_path=ffmpeg_path,
            max_duration_seconds=max_duration_seconds,
            overwrite=overwrite,
        )

    print(f"Transcribing {asset.id}: {asset.title}")
    print(f"Source: {source_path}")

    segments_iter, info = model.transcribe(
        str(source_path),
        beam_size=beam_size,
        language=language,
        vad_filter=True,
    )
    print(
        "Detected language "
        f"{getattr(info, 'language', language)} "
        f"with probability {getattr(info, 'language_probability', 0.0):.2f}"
    )

    segments: list[TranscriptSegment] = []
    last_progress_ms = 0
    if partial_path.exists() and overwrite:
        partial_path.unlink()

    with partial_path.open("w", encoding="utf-8") as handle:
        for segment in segments_iter:
            text = segment.text.strip()
            if not text:
                continue
            transcript_segment = TranscriptSegment(
                start_ms=seconds_to_ms(segment.start),
                end_ms=seconds_to_ms(segment.end),
                text=text,
            )
            segments.append(transcript_segment)
            handle.write(json.dumps(segment_to_dict(transcript_segment), ensure_ascii=False) + "\n")
            handle.flush()

            if (
                progress_seconds > 0
                and transcript_segment.end_ms - last_progress_ms >= progress_seconds * 1000
            ):
                last_progress_ms = transcript_segment.end_ms
                print(
                    f"{asset.id}: processed {format_hms(transcript_segment.end_ms)} "
                    f"({len(segments)} segments); partial={partial_path}"
                )

    partial_path.replace(output_path)
    if output_srt:
        write_srt(output_path.with_suffix(".srt"), segments)
    print(f"Wrote {len(segments)} segments: {output_path}")
    return output_path


def prepare_local_audio(
    *,
    source_path: Path,
    asset: ManifestAsset,
    work_dir: Path,
    ffmpeg_path: Optional[str],
    max_duration_seconds: Optional[int],
    overwrite: bool,
) -> Path:
    work_dir.mkdir(parents=True, exist_ok=True)
    suffix = "" if max_duration_seconds is None else f"_{max_duration_seconds}s"
    output_path = work_dir / f"{asset.id}{suffix}.wav"
    if output_path.exists() and not overwrite:
        print(f"Reusing local audio: {output_path}")
        return output_path

    ffmpeg = ffmpeg_path or shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg is required for --prepare-audio but was not found on PATH.")

    cmd = [
        ffmpeg,
        "-hide_banner",
        "-y" if overwrite else "-n",
        *([] if max_duration_seconds is None else ["-t", str(max_duration_seconds)]),
        "-i",
        str(source_path),
        "-vn",
        "-ac",
        "1",
        "-ar",
        "16000",
        str(output_path),
    ]
    print(f"Preparing local audio: {output_path}")
    subprocess.run(cmd, check=True)
    return output_path


def segment_to_dict(segment: TranscriptSegment) -> dict[str, Any]:
    return {
        "start": segment.start_ms,
        "end": segment.end_ms,
        "text": segment.text,
    }


def write_json_lines(path: Path, segments: Iterable[TranscriptSegment]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for segment in segments:
            handle.write(
                json.dumps(
                    segment_to_dict(segment),
                    ensure_ascii=False,
                )
                + "\n"
            )


def write_srt(path: Path, segments: list[TranscriptSegment]) -> None:
    lines: list[str] = []
    for index, segment in enumerate(segments, start=1):
        lines.extend(
            [
                str(index),
                f"{format_srt_time(segment.start_ms)} --> {format_srt_time(segment.end_ms)}",
                segment.text,
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def seconds_to_ms(value: float) -> int:
    return int(round(value * 1000))


def format_srt_time(milliseconds: int) -> str:
    seconds_total, ms = divmod(milliseconds, 1000)
    minutes_total, seconds = divmod(seconds_total, 60)
    hours, minutes = divmod(minutes_total, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{ms:03d}"


def format_hms(milliseconds: int) -> str:
    seconds_total = milliseconds // 1000
    minutes_total, seconds = divmod(seconds_total, 60)
    hours, minutes = divmod(minutes_total, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Transcribe MMM training videos with faster-whisper")
    parser.add_argument("--root", required=True, type=Path, help="Path to data/mmm_training")
    parser.add_argument(
        "--video-id",
        action="append",
        dest="video_ids",
        help="Transcribe only this manifest video ID. Repeat for multiple IDs.",
    )
    parser.add_argument("--model-size", default="small.en")
    parser.add_argument("--device", default="cuda", choices=["cuda", "cpu", "auto"])
    parser.add_argument("--compute-type", default="float16")
    parser.add_argument("--beam-size", type=int, default=5)
    parser.add_argument("--language", default="en")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--srt", action="store_true", help="Also write .srt files")
    parser.add_argument(
        "--prepare-audio",
        action="store_true",
        help="Extract/copy source audio to local Colab disk before transcription.",
    )
    parser.add_argument("--work-dir", type=Path, default=Path("/content/mmm_transcribe_work"))
    parser.add_argument("--ffmpeg-path")
    parser.add_argument(
        "--max-duration-seconds",
        type=int,
        help="Debug option: transcribe only the first N seconds after local audio extraction.",
    )
    parser.add_argument("--progress-seconds", type=int, default=300)
    return parser


def main(argv: Optional[list[str]] = None) -> None:
    args = build_parser().parse_args(argv)
    root = args.root.expanduser().resolve()

    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise SystemExit(
            "faster-whisper is not installed. In Colab run: "
            "!pip install -U faster-whisper ctranslate2"
        ) from exc

    assets = select_assets(load_manifest(root), args.video_ids)
    if not assets:
        raise SystemExit("No videos found in manifest.")

    print(f"Loading faster-whisper model: {args.model_size}")
    model = WhisperModel(
        args.model_size,
        device=args.device,
        compute_type=args.compute_type,
    )

    for asset in assets:
        transcribe_asset(
            root=root,
            asset=asset,
            model=model,
            beam_size=args.beam_size,
            language=args.language,
            overwrite=args.overwrite,
            output_srt=args.srt,
            prepare_audio=args.prepare_audio,
            work_dir=args.work_dir,
            ffmpeg_path=args.ffmpeg_path,
            max_duration_seconds=args.max_duration_seconds,
            progress_seconds=args.progress_seconds,
        )


if __name__ == "__main__":
    main()
