from __future__ import annotations

import json
from datetime import datetime, timezone

from helix_v3.journal.flashcards import FlashcardSystem
from helix_v3.training.vision_packet_chart_backfill import (
    ChartBackfillConfig,
    collect_packet_flashcard_ids,
    load_chart_targets,
)


def test_collect_packet_flashcard_ids_targets_missing_images_only(tmp_path) -> None:
    packet_root = tmp_path / "packets"
    packet = packet_root / "XAUUSD_test_packet"
    image_dir = packet / "images"
    image_dir.mkdir(parents=True)
    (image_dir / "existing.png").write_bytes(b"fake png")
    (packet / "manifest.json").write_text(
        json.dumps(
            {
                "symbol": "XAUUSD",
                "items": [
                    {"flashcard_id": 101, "image_path": "", "source_chart_path": ""},
                    {
                        "flashcard_id": 102,
                        "image_path": "images/existing.png",
                        "source_chart_path": "",
                    },
                ],
            }
        ),
        encoding="utf-8",
    )

    ids = collect_packet_flashcard_ids(
        ChartBackfillConfig(packet_root=packet_root, symbols=("XAUUSD",))
    )
    all_ids = collect_packet_flashcard_ids(
        ChartBackfillConfig(
            packet_root=packet_root,
            symbols=("XAUUSD",),
            replace_existing=True,
        )
    )

    assert ids == (101,)
    assert all_ids == (101, 102)


def test_load_chart_targets_skips_existing_flashcard_chart_paths(tmp_path) -> None:
    flashcards_db = tmp_path / "flashcards.db"
    packet_root = tmp_path / "packets"
    packet = packet_root / "XAUUSD_test_packet"
    packet.mkdir(parents=True)
    chart_path = tmp_path / "existing_chart.png"
    chart_path.write_bytes(b"fake png")

    flashcards = FlashcardSystem(db_path=flashcards_db)
    try:
        existing_id = flashcards.save_historical_flashcard(
            symbol="XAUUSD",
            timeframe="M15",
            chart_path=str(chart_path),
            snapshot_at=datetime(2026, 6, 1, 8, 0, tzinfo=timezone.utc),
            mtf_context={},
        )
        missing_id = flashcards.save_historical_flashcard(
            symbol="XAUUSD",
            timeframe="M15",
            chart_path="",
            snapshot_at=datetime(2026, 6, 1, 9, 0, tzinfo=timezone.utc),
            mtf_context={},
        )
    finally:
        flashcards.close()

    (packet / "manifest.json").write_text(
        json.dumps(
            {
                "symbol": "XAUUSD",
                "items": [
                    {"flashcard_id": existing_id, "image_path": "", "source_chart_path": ""},
                    {"flashcard_id": missing_id, "image_path": "", "source_chart_path": ""},
                ],
            }
        ),
        encoding="utf-8",
    )

    targets = load_chart_targets(
        ChartBackfillConfig(
            flashcards_db=flashcards_db,
            packet_root=packet_root,
            symbols=("XAUUSD",),
        )
    )

    assert [row["id"] for row in targets] == [missing_id]
