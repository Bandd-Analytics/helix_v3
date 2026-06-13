"""Chart directory rotation (audit Tier 3.5).

charts/ had grown to 3.5 GB / 12,600+ PNGs with no retention policy.
Age-based purge: PNGs older than CHART_RETENTION_DAYS (default 14) are
deleted recursively. Flashcard/journal rows keep their chart_path —
a missing image on an old record is acceptable; an unbounded disk
isn't.
"""
from __future__ import annotations

import time
from pathlib import Path
from typing import Dict, Optional

from config.settings import settings
from helix_v3.utils.logger import get_logger

logger = get_logger("chart_rotation")


def rotate_charts(
    directory: Optional[Path] = None,
    retention_days: Optional[int] = None,
) -> Dict[str, float]:
    """Delete chart PNGs older than the retention window.

    Returns {"deleted": count, "freed_mb": megabytes}. Never raises —
    rotation is housekeeping and must not take down the trade loop.
    """
    directory = Path(directory or settings.chart.output_dir)
    retention = (
        retention_days
        if retention_days is not None
        else settings.chart.retention_days
    )
    stats = {"deleted": 0.0, "freed_mb": 0.0}
    if retention <= 0 or not directory.exists():
        return stats

    cutoff = time.time() - retention * 86400
    freed_bytes = 0
    try:
        for png in directory.rglob("*.png"):
            try:
                st = png.stat()
                if st.st_mtime < cutoff:
                    size = st.st_size
                    png.unlink()
                    stats["deleted"] += 1
                    freed_bytes += size
            except OSError:
                continue  # in use / already gone — skip
    except Exception as e:
        logger.error("Chart rotation failed in %s: %s", directory, e)

    stats["freed_mb"] = round(freed_bytes / (1024 * 1024), 1)
    if stats["deleted"]:
        logger.info(
            "Chart rotation: deleted %d PNGs older than %dd, freed %.1f MB",
            int(stats["deleted"]), retention, stats["freed_mb"],
        )
    return stats
