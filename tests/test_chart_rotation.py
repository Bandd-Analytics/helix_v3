"""Tests for chart directory rotation (audit Tier 3.5)."""
from __future__ import annotations

import os
import time
from pathlib import Path

from helix_v3.utils.chart_rotation import rotate_charts


def _png(directory: Path, name: str, age_days: float, size: int = 1024) -> Path:
    p = directory / name
    p.write_bytes(b"\x89PNG" + b"0" * size)
    old = time.time() - age_days * 86400
    os.utime(p, (old, old))
    return p


def test_old_pngs_deleted_recent_kept(tmp_path) -> None:
    old = _png(tmp_path, "old.png", age_days=30)
    nested_old = tmp_path / "flashcards"
    nested_old.mkdir()
    old2 = _png(nested_old, "nested_old.png", age_days=15)
    fresh = _png(tmp_path, "fresh.png", age_days=2)

    stats = rotate_charts(tmp_path, retention_days=14)

    assert stats["deleted"] == 2
    assert stats["freed_mb"] >= 0
    assert not old.exists()
    assert not old2.exists()
    assert fresh.exists()


def test_non_png_files_untouched(tmp_path) -> None:
    db = tmp_path / "flashcards.db"
    db.write_bytes(b"sqlite")
    old_time = time.time() - 100 * 86400
    os.utime(db, (old_time, old_time))

    rotate_charts(tmp_path, retention_days=14)
    assert db.exists()


def test_zero_retention_disables(tmp_path) -> None:
    old = _png(tmp_path, "old.png", age_days=100)
    stats = rotate_charts(tmp_path, retention_days=0)
    assert stats["deleted"] == 0
    assert old.exists()


def test_missing_directory_is_noop(tmp_path) -> None:
    stats = rotate_charts(tmp_path / "does_not_exist", retention_days=14)
    assert stats == {"deleted": 0.0, "freed_mb": 0.0}
