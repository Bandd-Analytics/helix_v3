from __future__ import annotations

import json

from helix_v3.training.vision_account_review_runner import (
    write_model_comparison_summary,
    write_model_review_index,
)


def test_model_review_summary_scores_blind_predictions(tmp_path) -> None:
    packet_root = tmp_path / "packets"
    packet = packet_root / "GBPJPY_test_packet"
    reviews = packet / "reviews"
    images = packet / "images"
    reviews.mkdir(parents=True)
    images.mkdir()

    (images / "c01.png").write_bytes(b"fake")
    (images / "c02.png").write_bytes(b"fake")
    (packet / "manifest.json").write_text(
        json.dumps(
            {
                "symbol": "GBPJPY",
                "items": [
                    {"review_id": "C01", "image_path": "images/c01.png"},
                    {"review_id": "C02", "image_path": "images/c02.png"},
                ],
            }
        ),
        encoding="utf-8",
    )
    (packet / "answer_key.csv").write_text(
        "\n".join(
            [
                "review_id,label,flashcard_id,snapshot_at,outcome,exit_pips,max_favorable_pips,max_adverse_pips,t1_hit,image_path",
                "C01,winner,1,2026-01-01T00:00:00+00:00,TARGET_2,10,20,2,True,images/c01.png",
                "C02,loser,2,2026-01-02T00:00:00+00:00,TIME_EXIT_LOSS,-5,3,8,False,images/c02.png",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    (reviews / "codex_blind.md").write_text(
        '[{"review_id":"C01","predicted_label":"winner"},'
        '{"review_id":"C02","predicted_label":"winner"}]',
        encoding="utf-8",
    )
    (reviews / "claude_blind.md").write_text(
        '```json\n[{"review_id":"C01","predicted_label":"loser"},'
        '{"review_id":"C02","predicted_label":"loser"}]\n```',
        encoding="utf-8",
    )

    summary_path = write_model_comparison_summary(packet)
    index_path = write_model_review_index(packet_root)

    summary = summary_path.read_text(encoding="utf-8")
    index = index_path.read_text(encoding="utf-8")
    assert "| Codex / ChatGPT Pro | 1 | 2 | 50.0% | 2 | C02 | ok |" in summary
    assert "| Claude Max | 1 | 2 | 50.0% | 2 | C01 | ok |" in summary
    assert "1/2 (50.0%)" in index
