from __future__ import annotations

import json

import pytest

from helix_v3.training import video_mmm_extractor as extractor


def _add_video(root, name: str, payload: bytes = b"fake video") -> None:
    video_dir = root / "videos"
    video_dir.mkdir(parents=True, exist_ok=True)
    (video_dir / name).write_bytes(payload)


def test_build_manifest_indexes_local_videos(tmp_path) -> None:
    _add_video(tmp_path, "MMM Day 2.mp4", b"222")
    _add_video(tmp_path, "MMM Day 1.mp4", b"111")
    (tmp_path / "videos" / "notes.txt").write_text("ignore me", encoding="utf-8")

    assets = extractor.build_manifest(root=tmp_path)

    assert [asset.id for asset in assets] == ["video_001", "video_002"]
    assert [asset.title for asset in assets] == ["MMM Day 1", "MMM Day 2"]
    assert assets[0].path.replace("\\", "/") == "videos/MMM Day 1.mp4"

    manifest = json.loads((tmp_path / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["content_policy"].startswith("Store concise methodology notes")
    assert len(manifest["videos"]) == 2
    assert "MMM Day 1" in (tmp_path / "source_index.md").read_text(encoding="utf-8")


def test_initialize_methodology_files_creates_notes_rules_skills_and_validation_plan(
    tmp_path,
) -> None:
    _add_video(tmp_path, "MMM 8-2-2011 Day 1 .mp4")
    _add_video(tmp_path, "MMM 8-3-2011 Day 2 .mp4")

    extractor.initialize_methodology_files(root=tmp_path)

    assert (tmp_path / "methodology_index.md").exists()
    assert (tmp_path / "rules" / "steve_mauro_mmm_methodology.md").exists()
    assert (tmp_path / "rules" / "rule_cards.md").exists()
    assert (tmp_path / "skills" / "CODEX_MMM_STRATEGY.md").exists()
    assert (tmp_path / "skills" / "CLAUDE_MMM_STRATEGY.md").exists()
    assert (tmp_path / "validation" / "market_validation_plan.md").exists()

    note_files = sorted((tmp_path / "notes").glob("*.md"))
    assert len(note_files) == 2
    note_text = note_files[0].read_text(encoding="utf-8")
    assert "Paraphrased Teaching" in note_text
    assert "Validation Status" in note_text

    validation_text = (tmp_path / "validation" / "market_validation_plan.md").read_text(
        encoding="utf-8"
    )
    assert "Backtest sample is pair-specific first" in validation_text


def test_probe_marks_missing_ffprobe(tmp_path, monkeypatch) -> None:
    _add_video(tmp_path, "MMM Day 1.mp4")
    monkeypatch.setattr(extractor.shutil, "which", lambda _name: None)

    assets = extractor.build_manifest(root=tmp_path, probe=True)

    assert assets[0].probe_status == "ffprobe_missing"


def test_extractors_fail_clearly_when_ffmpeg_is_missing(tmp_path, monkeypatch) -> None:
    _add_video(tmp_path, "MMM Day 1.mp4")
    extractor.build_manifest(root=tmp_path)
    monkeypatch.setattr(extractor.shutil, "which", lambda _name: None)

    with pytest.raises(RuntimeError, match="ffmpeg is not available"):
        extractor.extract_audio(root=tmp_path)

    with pytest.raises(RuntimeError, match="ffmpeg is not available"):
        extractor.extract_frames(root=tmp_path)


def test_transcribe_fails_clearly_without_model(tmp_path, monkeypatch) -> None:
    _add_video(tmp_path, "MMM Day 1.mp4")
    extractor.build_manifest(root=tmp_path)
    audio_dir = tmp_path / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    (audio_dir / "video_001.wav").write_bytes(b"fake audio")
    monkeypatch.setattr(extractor.shutil, "which", lambda _name: "ffmpeg")

    with pytest.raises(FileNotFoundError, match="Whisper model not found"):
        extractor.transcribe_audio(root=tmp_path)


def test_transcribe_rejects_invalid_output_format(tmp_path, monkeypatch) -> None:
    _add_video(tmp_path, "MMM Day 1.mp4")
    extractor.build_manifest(root=tmp_path)
    model_dir = tmp_path / "models"
    model_dir.mkdir(parents=True, exist_ok=True)
    model = model_dir / "ggml-base.en.bin"
    model.write_bytes(b"fake model")
    audio_dir = tmp_path / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    (audio_dir / "video_001.wav").write_bytes(b"fake audio")
    monkeypatch.setattr(extractor.shutil, "which", lambda _name: "ffmpeg")

    with pytest.raises(ValueError, match="output_format"):
        extractor.transcribe_audio(root=tmp_path, output_format="vtt")


def test_transcribe_can_target_one_video(tmp_path, monkeypatch) -> None:
    _add_video(tmp_path, "MMM Day 1.mp4")
    _add_video(tmp_path, "MMM Day 2.mp4")
    extractor.build_manifest(root=tmp_path)
    (tmp_path / "models").mkdir(parents=True, exist_ok=True)
    (tmp_path / "models" / "ggml-base.en.bin").write_bytes(b"fake model")
    (tmp_path / "audio").mkdir(parents=True, exist_ok=True)
    (tmp_path / "audio" / "video_001.wav").write_bytes(b"fake audio")
    (tmp_path / "audio" / "video_002.wav").write_bytes(b"fake audio")
    calls = []

    def fake_run(cmd, cwd, check):  # noqa: ANN001
        calls.append((cmd, cwd, check))

    monkeypatch.setattr(extractor.subprocess, "run", fake_run)

    outputs = extractor.transcribe_audio(
        root=tmp_path,
        ffmpeg_path="ffmpeg",
        video_ids=["video_002"],
    )

    assert outputs == [tmp_path / "transcripts" / "video_002.json"]
    assert len(calls) == 1
    assert "video_002.wav" in calls[0][0][3]


def test_transcribe_rejects_unknown_video_id(tmp_path) -> None:
    _add_video(tmp_path, "MMM Day 1.mp4")
    extractor.build_manifest(root=tmp_path)

    with pytest.raises(ValueError, match="Unknown video IDs"):
        extractor.transcribe_audio(root=tmp_path, video_ids=["video_999"])
