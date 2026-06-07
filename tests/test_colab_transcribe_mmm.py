from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "colab_transcribe_mmm.py"
SPEC = importlib.util.spec_from_file_location("colab_transcribe_mmm", SCRIPT_PATH)
assert SPEC and SPEC.loader
colab = importlib.util.module_from_spec(SPEC)
sys.modules["colab_transcribe_mmm"] = colab
SPEC.loader.exec_module(colab)


def _write_manifest(root: Path) -> None:
    (root / "manifest.json").write_text(
        json.dumps(
            {
                "videos": [
                    {
                        "id": "video_001",
                        "title": "Day 1",
                        "path": "videos\\Day 1.mp4",
                        "duration_seconds": 10.0,
                    },
                    {
                        "id": "video_002",
                        "title": "Day 2",
                        "path": "videos\\Day 2.mp4",
                        "duration_seconds": 20.0,
                    },
                ]
            }
        ),
        encoding="utf-8",
    )


def test_load_manifest_and_select_assets(tmp_path: Path) -> None:
    _write_manifest(tmp_path)

    assets = colab.load_manifest(tmp_path)
    selected = colab.select_assets(assets, ["video_002"])

    assert [asset.id for asset in assets] == ["video_001", "video_002"]
    assert [asset.id for asset in selected] == ["video_002"]


def test_select_assets_rejects_unknown_id(tmp_path: Path) -> None:
    _write_manifest(tmp_path)

    with pytest.raises(ValueError, match="Unknown video IDs"):
        colab.select_assets(colab.load_manifest(tmp_path), ["missing"])


def test_source_for_asset_prefers_audio_then_video(tmp_path: Path) -> None:
    _write_manifest(tmp_path)
    asset = colab.load_manifest(tmp_path)[0]
    audio_dir = tmp_path / "audio"
    audio_dir.mkdir(parents=True)
    audio_path = audio_dir / "video_001.wav"
    audio_path.write_bytes(b"audio")

    assert colab.source_for_asset(tmp_path, asset) == audio_path


def test_source_for_asset_normalizes_windows_video_path(tmp_path: Path) -> None:
    _write_manifest(tmp_path)
    asset = colab.load_manifest(tmp_path)[0]
    video_dir = tmp_path / "videos"
    video_dir.mkdir(parents=True)
    video_path = video_dir / "Day 1.mp4"
    video_path.write_bytes(b"video")

    assert colab.source_for_asset(tmp_path, asset) == video_path


def test_write_json_lines_and_srt(tmp_path: Path) -> None:
    segments = [
        colab.TranscriptSegment(start_ms=1234, end_ms=5678, text="First"),
        colab.TranscriptSegment(start_ms=3723004, end_ms=3724999, text="Second"),
    ]
    json_path = tmp_path / "video_001.json"
    srt_path = tmp_path / "video_001.srt"

    colab.write_json_lines(json_path, segments)
    colab.write_srt(srt_path, segments)

    lines = json_path.read_text(encoding="utf-8").splitlines()
    assert json.loads(lines[0]) == {"start": 1234, "end": 5678, "text": "First"}
    assert "01:02:03,004 --> 01:02:04,999" in srt_path.read_text(encoding="utf-8")


def test_seconds_to_ms_rounds() -> None:
    assert colab.seconds_to_ms(1.2345) == 1234
    assert colab.seconds_to_ms(1.2355) == 1236


def test_prepare_local_audio_builds_ffmpeg_command(tmp_path: Path, monkeypatch) -> None:
    source = tmp_path / "source.mp4"
    source.write_bytes(b"video")
    asset = colab.ManifestAsset(id="video_002", title="Day 2", path="source.mp4")
    calls = []

    def fake_run(cmd, check):  # noqa: ANN001
        calls.append((cmd, check))
        Path(cmd[-1]).write_bytes(b"wav")

    monkeypatch.setattr(colab.subprocess, "run", fake_run)

    output = colab.prepare_local_audio(
        source_path=source,
        asset=asset,
        work_dir=tmp_path / "work",
        ffmpeg_path="ffmpeg",
        max_duration_seconds=600,
        overwrite=True,
    )

    assert output == tmp_path / "work" / "video_002_600s.wav"
    assert output.exists()
    assert calls[0][0][0] == "ffmpeg"
    assert "-t" in calls[0][0]
    assert "600" in calls[0][0]


def test_format_hms() -> None:
    assert colab.format_hms(3_723_004) == "01:02:03"
