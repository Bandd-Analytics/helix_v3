"""Trash reviewer/reaper for Helix V3 — decides what in trash/ can really go.

For every item in the trash manifest it answers three questions:

1. Does live code still reference it?  -> mark `restore-recommended` (kept;
   run `python tools/trash.py restore <id>` to bring it back).
2. Is it provable junk (build artifacts, crash logs, caches, tmp files)?
   -> mark `delete-candidate` and start the grace-period clock.
3. Anything else (e.g. Python source nothing imports but a human might still
   run as a CLI tool) -> mark `unsure` and MAINTAIN. Unsure items are never
   auto-deleted; a human promotes them with `approve <id>` once truly done.

Delete-candidates older than the grace period (default 2 hours) are
permanently deleted on the next `review` run.

Usage:
    python tools/trash_review.py review [--dry-run]   # classify + reap expired
    python tools/trash_review.py approve <id>         # human: unsure -> delete-candidate
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from trash import (  # noqa: E402
    REPO_ROOT,
    TRASH_DIR,
    load_manifest,
    now_iso,
    save_manifest,
)

GRACE_PERIOD = timedelta(hours=2)

# Categories that are provably junk: safe to delete once aged.
JUNK_NAME_PATTERNS = [
    r"^hs_err_pid\d+\.log$",
    r"\.egg-info$",
    r"^__pycache__$",
    r"\.pyc$",
    r"^\.tmp$",
    r"\.tmp$",
    r"^\.pytest_cache$",
    r"^\.ruff_cache$",
    r"^dist$",
    r"^build$",
    r"\.bak$",
    r"\.log$",
]

# Where to look for live references. Code/config only — doc mentions don't
# keep code alive.
REFERENCE_EXTENSIONS = {".py", ".toml", ".bat", ".ps1", ".cfg", ".ini", ".yaml", ".yml", ".json"}
EXCLUDED_DIRS = {
    "trash", ".venv", ".git", "__pycache__", ".idea", ".pytest_cache",
    ".ruff_cache", ".claude", "data", "logs", "charts", "MMM", "node_modules",
    "helix_v3.egg-info", "verdicts",
}
# These files legitimately mention trashed items without depending on them.
EXCLUDED_FILES = {"trash.py", "trash_review.py", "manifest.json"}


def is_junk(name: str) -> bool:
    return any(re.search(p, name) for p in JUNK_NAME_PATTERNS)


def iter_reference_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if path.is_dir():
            continue
        if path.suffix.lower() not in REFERENCE_EXTENSIONS:
            continue
        if path.name in EXCLUDED_FILES:
            continue
        rel_parts = path.relative_to(REPO_ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        files.append(path)
    return files


def find_references(entry: dict, ref_files: list[Path]) -> list[str]:
    """Search live code for real references to the trashed item.

    For Python modules: the dotted import path (helix_v3.backtest.foo) or an
    import statement naming the module stem. Prose mentions of a common word
    like "orchestrator" don't count. `\\b` treats `_` as a word char, so
    `orchestrator` will NOT match `orchestrator_v2`.
    For everything else: the exact file/dir name or repo-relative path.
    """
    original = Path(entry["original_path"])
    patterns: list[re.Pattern[str]] = []

    if original.suffix == ".py":
        dotted = original.with_suffix("").as_posix().replace("/", r"\.")
        patterns.append(re.compile(rf"\b{dotted}\b"))
        stem = original.stem
        patterns.append(re.compile(rf"\b(?:import|from)\s+[\w.]*\b{re.escape(stem)}\b"))
        # Path string in scripts/configs (either slash direction).
        patterns.append(re.compile(re.escape(original.as_posix()).replace("/", r"[/\\]")))
    else:
        patterns.append(re.compile(re.escape(original.name)))

    hits: list[str] = []
    for path in ref_files:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if any(p.search(line) for p in patterns):
                hits.append(f"{path.relative_to(REPO_ROOT).as_posix()}:{lineno}")
                if len(hits) >= 10:
                    return hits
    return hits


def permanently_delete(entry: dict, dry_run: bool) -> bool:
    target = (TRASH_DIR / entry["trashed_name"]).resolve()
    # Safety: only ever delete inside trash/.
    if TRASH_DIR.resolve() not in target.parents:
        print(f"  [{entry['id']}] REFUSING delete outside trash/: {target}")
        return False
    if dry_run:
        print(f"  [{entry['id']}] would permanently delete trash/{entry['trashed_name']}")
        return False
    if target.is_dir():
        shutil.rmtree(target, ignore_errors=True)
    elif target.exists():
        target.unlink()
    return True


def cmd_review(dry_run: bool) -> int:
    entries = load_manifest()
    if not entries:
        print("Trash is empty — nothing to review.")
        return 0

    now = datetime.now(timezone.utc)
    ref_files = iter_reference_files()
    changed = False
    counts = {"reaped": 0, "delete-candidate": 0, "unsure": 0, "restore-recommended": 0}

    for entry in entries:
        status = entry["status"]
        if status in ("deleted", "restored"):
            continue

        # 1) Reap aged delete-candidates.
        if status == "delete-candidate" and entry.get("marked_at"):
            marked = datetime.strptime(entry["marked_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            age = now - marked
            if age >= GRACE_PERIOD:
                if permanently_delete(entry, dry_run):
                    entry["status"] = "deleted"
                    entry["review_notes"] = f"permanently deleted at {now_iso()} (junk, aged {age})"
                    counts["reaped"] += 1
                    changed = True
                    print(f"  [{entry['id']}] DELETED permanently: {entry['original_path']}")
            else:
                remaining = GRACE_PERIOD - age
                print(f"  [{entry['id']}] delete-candidate, {remaining} left in grace period: {entry['original_path']}")
                counts["delete-candidate"] += 1
            continue

        # 2) Classify held/unsure/restore-recommended items.
        refs = find_references(entry, ref_files)
        if refs:
            new_status = "restore-recommended"
            notes = f"still referenced by live code: {', '.join(refs[:5])}" + (" ..." if len(refs) > 5 else "")
        elif is_junk(Path(entry["original_path"]).name):
            new_status = "delete-candidate"
            notes = "provable junk (build artifact/log/cache), no references — grace period started"
            entry["marked_at"] = now_iso()
        else:
            new_status = "unsure"
            notes = "no live references found, but not provably junk — maintaining (use 'approve <id>' to allow deletion)"

        if new_status != status or notes != entry.get("review_notes"):
            entry["status"] = new_status
            entry["review_notes"] = notes
            changed = True
        counts[new_status] += 1
        print(f"  [{entry['id']}] {new_status}: {entry['original_path']}")
        print(f"         {notes}")

    if changed and not dry_run:
        save_manifest(entries)
    print(
        f"\nSummary: {counts['reaped']} reaped, {counts['delete-candidate']} awaiting grace period, "
        f"{counts['unsure']} maintained (unsure), {counts['restore-recommended']} restore-recommended."
    )
    return 0


def cmd_approve(item_id: str) -> int:
    entries = load_manifest()
    entry = next((e for e in entries if e["id"] == item_id), None)
    if entry is None:
        print(f"ERROR: no trash entry with id {item_id}")
        return 1
    if entry["status"] in ("deleted", "restored"):
        print(f"ERROR: item {item_id} is already {entry['status']}")
        return 1
    entry["status"] = "delete-candidate"
    entry["marked_at"] = now_iso()
    entry["review_notes"] = "human-approved for deletion — grace period started"
    save_manifest(entries)
    print(f"[{item_id}] approved for deletion: {entry['original_path']}")
    print(f"        will be permanently deleted by the next 'review' run after {GRACE_PERIOD}.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_review = sub.add_parser("review", help="classify trash items and reap expired delete-candidates")
    p_review.add_argument("--dry-run", action="store_true", help="report without changing anything")

    p_approve = sub.add_parser("approve", help="promote an unsure item to delete-candidate")
    p_approve.add_argument("id")

    args = parser.parse_args()
    if args.command == "review":
        return cmd_review(args.dry_run)
    if args.command == "approve":
        return cmd_approve(args.id)
    return 1


if __name__ == "__main__":
    sys.exit(main())
