#!/usr/bin/env python3
"""
Merge duplicate day folders in ``angelaYu/``.

Four days were written twice into differently punctuated folders (one with
"Variables - Send SMS", one with "Variables- Send SMS"), so half of those notes were
invisible to the site generator, which picks the first folder it finds:

    Day 35: 7 notes in one folder, 9 in the other
    Day 37: 6 / 6
    Day 39: 1 / 7
    Day 40: 1 / 6

The folder whose name matches the course's transcripts folder is the canonical one
(that is also how notes find their transcript). Files are merged in, the longer
Markdown wins where a lecture exists in both, and the emptied folder is deleted.

Usage::

    python3 tools/merge_duplicate_days.py            # dry-run report
    python3 tools/merge_duplicate_days.py --apply    # do it
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

DOCS_SITE = Path(__file__).resolve().parent.parent
REPO = DOCS_SITE.parent
ANGELAYU = REPO / "angelaYu"
TRANSCRIPTS = ANGELAYU / "transcripts"
DAY_RE = re.compile(r"^(\d+)\s*-\s*(.+)$")


def days_in(base: Path) -> dict[int, list[Path]]:
    groups: dict[int, list[Path]] = defaultdict(list)
    if not base.is_dir():
        return groups
    for entry in sorted(base.iterdir()):
        m = DAY_RE.match(entry.name)
        if entry.is_dir() and m:
            groups[int(m.group(1))].append(entry)
    return groups


def canonical_name(day: int, notes_dirs: list[Path]) -> Path:
    """The notes folder that matches the transcripts folder for the same day."""
    transcript_dirs = days_in(TRANSCRIPTS)[day]
    for t in transcript_dirs:
        for d in notes_dirs:
            if d.name == t.name:
                return d
    # fall back: the folder with the most files
    return max(notes_dirs, key=lambda d: len(list(d.iterdir())))


def merge(day: int, dirs: list[Path], apply: bool) -> list[str]:
    target = canonical_name(day, dirs)
    log = [f"Day {day}: keeping {target.name}"]
    for spare in [d for d in dirs if d != target]:
        log.append(f"    merging {spare.name}")
        for src in sorted(spare.iterdir()):
            dst = target / src.name
            if not dst.exists():
                log.append(f"      + {src.name}")
                if apply:
                    shutil.move(str(src), str(dst))
                continue
            if src.suffix.lower() == ".md" and dst.suffix.lower() == ".md":
                a = len(dst.read_text(encoding="utf-8", errors="replace").split())
                b = len(src.read_text(encoding="utf-8", errors="replace").split())
                if b > a:
                    log.append(f"      ↑ {src.name} (replacing {a} words with {b})")
                    if apply:
                        dst.unlink()
                        shutil.move(str(src), str(dst))
                else:
                    log.append(f"      = {src.name} (keeping the {a}-word version)")
                    if apply:
                        src.unlink()
            else:
                log.append(f"      = {src.name} (already present, left in place)")
        if apply:
            leftovers = list(spare.iterdir())
            if leftovers:
                log.append(f"      ! {spare.name} still has "
                           f"{[p.name for p in leftovers]}, not removed")
            else:
                spare.rmdir()
                log.append(f"      - removed empty {spare.name}")
    return log


def dedupe_topics(folder: Path, apply: bool) -> list[str]:
    """Drop the shorter of two notes that cover the same lecture number and topic.

    The two copies of these days spelled the goals lectures differently — "what we
    will make" vs "what you will make" — so a name-based merge would keep both.
    """
    log: list[str] = []
    by_number: dict[str, list[Path]] = defaultdict(list)
    for p in sorted(folder.glob("*.md")):
        m = re.match(r"^(\d+)", p.stem)
        if m:
            by_number[m.group(1)].append(p)
    for number, paths in by_number.items():
        if len(paths) < 2:
            continue
        keep = max(paths, key=lambda p: len(p.read_text(encoding="utf-8",
                                                       errors="replace").split()))
        for p in paths:
            if p == keep:
                continue
            log.append(f"      - {p.name} (duplicate topic of {keep.name}, "
                       f"shorter)")
            if apply:
                p.unlink()
    return log


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    groups = {d: v for d, v in days_in(ANGELAYU).items() if len(v) > 1}
    if not groups:
        print("no duplicate day folders found")
        return 0
    for day in sorted(groups):
        for line in merge(day, groups[day], args.apply):
            print(line)
        target = canonical_name(day, groups[day])
        for line in dedupe_topics(target, args.apply):
            print(line)
    if not args.apply:
        print("\n(dry run — pass --apply to merge)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
