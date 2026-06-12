"""Trash bin for Helix V3 — safe, reversible removal of files and directories.

Instead of deleting, move anything the codebase no longer needs into trash/
with a manifest entry recording where it came from and why. Nothing is
permanently deleted by this script — that is trash_review.py's job, and only
after an item has been classified as junk and aged past the grace period.

Usage:
    python tools/trash.py put <path> [--reason "why"]   # move item into trash
    python tools/trash.py list                          # show trash contents
    python tools/trash.py restore <id>                  # move item back

Statuses (managed here and by trash_review.py):
    held                — just trashed, awaiting review
    unsure              — reviewed, no references found but not provably junk: MAINTAIN
    restore-recommended — reviewed, live code still references it: consider restore
    delete-candidate    — reviewed, provable junk; reaped after the grace period
    deleted             — permanently removed by trash_review.py
    restored            — moved back to its original location
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRASH_DIR = REPO_ROOT / "trash"
MANIFEST = TRASH_DIR / "manifest.json"

# Never allow these to be trashed.
PROTECTED = {".git", ".env", "trash", "tools"}


def load_manifest() -> list[dict]:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return []


def save_manifest(entries: list[dict]) -> None:
    TRASH_DIR.mkdir(exist_ok=True)
    MANIFEST.write_text(json.dumps(entries, indent=2), encoding="utf-8")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def next_id(entries: list[dict]) -> str:
    used = [int(e["id"]) for e in entries] or [0]
    return f"{max(used) + 1:04d}"


def cmd_put(path_arg: str, reason: str) -> int:
    src = Path(path_arg)
    if not src.is_absolute():
        src = REPO_ROOT / src
    src = src.resolve()

    if not src.exists():
        print(f"ERROR: {src} does not exist")
        return 1
    try:
        rel = src.relative_to(REPO_ROOT)
    except ValueError:
        print(f"ERROR: {src} is outside the repo — refusing")
        return 1
    if rel.parts[0] in PROTECTED:
        print(f"ERROR: '{rel.parts[0]}' is protected — refusing")
        return 1

    entries = load_manifest()
    item_id = next_id(entries)
    trashed_name = f"{item_id}__{src.name}"
    TRASH_DIR.mkdir(exist_ok=True)
    dest = TRASH_DIR / trashed_name

    shutil.move(str(src), str(dest))
    entries.append(
        {
            "id": item_id,
            "original_path": rel.as_posix(),
            "trashed_name": trashed_name,
            "is_dir": dest.is_dir(),
            "reason": reason,
            "trashed_at": now_iso(),
            "status": "held",
            "marked_at": None,
            "review_notes": "",
        }
    )
    save_manifest(entries)
    print(f"[{item_id}] trashed: {rel.as_posix()} -> trash/{trashed_name}")
    print(f"        reason: {reason}")
    return 0


def cmd_list() -> int:
    entries = load_manifest()
    if not entries:
        print("Trash is empty.")
        return 0
    print(f"{'ID':<6}{'STATUS':<22}{'TRASHED AT':<22}ORIGINAL PATH")
    print("-" * 90)
    for e in entries:
        print(f"{e['id']:<6}{e['status']:<22}{e['trashed_at']:<22}{e['original_path']}")
        if e.get("reason"):
            print(f"{'':<6}reason: {e['reason']}")
        if e.get("review_notes"):
            print(f"{'':<6}review: {e['review_notes']}")
    return 0


def cmd_restore(item_id: str) -> int:
    entries = load_manifest()
    entry = next((e for e in entries if e["id"] == item_id), None)
    if entry is None:
        print(f"ERROR: no trash entry with id {item_id}")
        return 1
    if entry["status"] in ("deleted", "restored"):
        print(f"ERROR: item {item_id} is already {entry['status']}")
        return 1

    src = TRASH_DIR / entry["trashed_name"]
    dest = REPO_ROOT / entry["original_path"]
    if not src.exists():
        print(f"ERROR: trash/{entry['trashed_name']} is missing on disk")
        return 1
    if dest.exists():
        print(f"ERROR: {entry['original_path']} already exists — resolve manually")
        return 1

    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dest))
    entry["status"] = "restored"
    entry["review_notes"] = f"restored at {now_iso()}"
    save_manifest(entries)
    print(f"[{item_id}] restored: {entry['original_path']}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_put = sub.add_parser("put", help="move a file/directory into trash")
    p_put.add_argument("path")
    p_put.add_argument("--reason", default="", help="why this is being trashed")

    sub.add_parser("list", help="show trash contents")

    p_restore = sub.add_parser("restore", help="move an item back to its original location")
    p_restore.add_argument("id")

    args = parser.parse_args()
    if args.command == "put":
        return cmd_put(args.path, args.reason)
    if args.command == "list":
        return cmd_list()
    if args.command == "restore":
        return cmd_restore(args.id)
    return 1


if __name__ == "__main__":
    sys.exit(main())
