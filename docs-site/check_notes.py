#!/usr/bin/env python3
"""
Check the *source* lecture notes against the course transcripts.

Usage:
    python3 check_notes.py            # structure + fidelity warnings
    python3 check_notes.py --strict   # warnings become failures too
    python3 check_notes.py --report   # plus the coverage report
    python3 check_notes.py --coverage # only the coverage report

Structural checks (failures):
  * every lecture note (`NN-Title.md`) starts with an H1 on line 1
  * no note starts with the "Here is a structured breakdown…" filler preamble
  * no unescaped HTML entities (`&#x27;`) anywhere in a note
  * code fences are balanced and every fence carries a language
  * no `### Next Steps` repeating `### Summary` verbatim (Days 23–40 legacy shape)
  * no placeholder links (`[...](...)`, `[...](#)`)

Fidelity checks (warnings — the heuristics are deliberately conservative):
  * dictionary keys / string literals used in a note's code that never appear in the
    matching transcript (possible invented API or renamed identifiers)
  * notes whose transcript cannot be found at all

Coverage report:
  * lectures that have a transcript but no note yet (the honest to-do list)
  * notes with no transcript (usually goals lectures or hand-written reference pages)

Exit code is non-zero when a structural check fails (or any warning under --strict).
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ANGELAYU = ROOT / "angelaYu"
TRANSCRIPTS = ANGELAYU / "transcripts"

FENCE_RE = re.compile(r"^(\s*)(```|~~~)(.*)$")
FILLER_RE = re.compile(r"^\s*Here is (?:a|an|the|short|structured)\b", re.I)
ENTITY_RE = re.compile(r"&#?\w+;")
PLACEHOLDER_LINK_RE = re.compile(r"\[[^\]]*\]\((?:\.\.\.|…+|#)\)")
LECTURE_NOTE_RE = re.compile(r"^\d+\s*[-.]\s*\S")
# Reference material that lives next to the notes but is not a lecture note.
NON_LECTURE = {"git_cheatsheet", "DEPLOY", "portfolio_projects", "career_action_plan",
               "ai_workflow", "README"}
STR_RE = re.compile(r"""(?<![\w.])(?:"([^"\n]{4,40})"|'([^'\n]{4,40})')""")
# Transcripts that were never written out: the file exists but only says so.
PLACEHOLDER_MARKER = "No transcript available"
STOPWORDS = {
    "the", "and", "for", "with", "this", "that", "from", "your", "you", "are", "was",
    "will", "have", "has", "not", "but", "all", "any", "can", "use", "used", "its",
    "their", "then", "than", "into", "over", "out", "off", "one", "two", "three",
    "hello", "world", "value", "name", "true", "false", "none", "print", "input",
}


def day_dirs(base: Path) -> dict[int, Path]:
    out: dict[int, Path] = {}
    if not base.is_dir():
        return out
    for entry in sorted(base.iterdir()):
        m = re.match(r"^(\d+)\s*-", entry.name)
        if entry.is_dir() and m:
            out.setdefault(int(m.group(1)), entry)
    return out


def stem_key(stem: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"^\d+\s*[-.]\s*", "", stem.lower()))


def code_bodies(text: str) -> list[tuple[str, list[str], bool]]:
    """(language, body lines, was_closed) for every fence in a note."""
    lines, out = text.splitlines(), []
    i = 0
    while i < len(lines):
        m = FENCE_RE.match(lines[i])
        if not m:
            i += 1
            continue
        marker = m.group(2)
        close = i + 1
        while close < len(lines) and not lines[close].strip().startswith(marker):
            close += 1
        out.append((m.group(3).strip(), lines[i + 1:close], close < len(lines)))
        i = close + 1
    return out


def check_note(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    problems: list[str] = []

    if not lines or not lines[0].startswith("# "):
        problems.append("does not start with an H1 title")
    if lines and FILLER_RE.match(lines[0]):
        problems.append("starts with a 'Here is a …' filler preamble")
    if len(lines) > 1 and lines[1].strip():
        problems.append("no blank line after the H1")

    for m in ENTITY_RE.finditer(text):
        if html.unescape(m.group(0)) != m.group(0):
            problems.append(f"unescaped HTML entity {m.group(0)!r}")
            break
    if PLACEHOLDER_LINK_RE.search(text):
        problems.append("contains a placeholder link like [...](...)")

    for lang, body, closed in code_bodies(text):
        if not closed:
            problems.append("has an unclosed code fence")
            break
        if not lang:
            problems.append("has a code fence without a language (```python/```text)")
            break

    if "summary checklist" not in text.lower() and path.stem not in NON_LECTURE:
        problems.append("has no 'Summary Checklist' section")

    secs = dict(re.findall(r"(?ms)^###\s+(Summary|Next Steps)\s*\n(.*?)(?=\n###|\Z)",
                           text))
    if "Summary" in secs and "Next Steps" in secs:
        a = re.sub(r"\W+", " ", secs["Summary"]).strip()
        b = re.sub(r"\W+", " ", secs["Next Steps"]).strip()
        if a[:200] and a[:200] == b[:200]:
            problems.append("'Next Steps' duplicates 'Summary' verbatim")
    return problems


def is_placeholder(path: Path) -> bool:
    return PLACEHOLDER_MARKER in path.read_text(encoding="utf-8", errors="replace")


def fidelity_warnings(note: Path, transcript: Path) -> list[str]:
    """String literals in the note's code that never appear in the transcript."""
    text = note.read_text(encoding="utf-8", errors="replace")
    ttext = transcript.read_text(encoding="utf-8", errors="replace").lower()
    literals: set[str] = set()
    for lang, body, _ in code_bodies(text):
        if lang not in ("python", "py", "json", "bash", "text", ""):
            continue
        for a, b in STR_RE.findall("\n".join(body)):
            s = (a or b).strip()
            if len(s) < 4 or s.lower() in STOPWORDS:
                continue
            if not re.search(r"[a-z]{3}", s, re.I):
                continue
            if re.fullmatch(r"[\d\s./:%+-]+", s):
                continue
            literals.add(s)
    missing = sorted(s for s in literals if s.lower() not in ttext)
    if len(missing) >= 3:
        return [f"{len(missing)} code literal(s) absent from the transcript, e.g. "
                + ", ".join(repr(m) for m in missing[:4])]
    return []


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    ap.add_argument("--report", action="store_true", help="print the coverage report")
    ap.add_argument("--coverage", action="store_true", help="print only coverage")
    args = ap.parse_args()

    ay, tr = day_dirs(ANGELAYU), day_dirs(TRANSCRIPTS)
    failures: list[tuple[Path, list[str]]] = []
    warnings: list[tuple[Path, list[str]]] = []
    unsourced: list[Path] = []
    notes_checked = 0
    lecture_notes = 0

    for day, directory in sorted(ay.items()):
        tx_dir = tr.get(day)
        transcripts = {p.stem: p for p in tx_dir.glob("*.txt")} if tx_dir else {}
        tx_keys = {stem_key(s): s for s in transcripts}
        for note in sorted(directory.glob("*.md")):
            if note.stem in NON_LECTURE or note.name == "README.md":
                continue
            if "images" in note.parts:
                continue
            notes_checked += 1
            is_lecture = bool(LECTURE_NOTE_RE.match(note.stem))
            problems = check_note(note)
            if not is_lecture:
                problems = [p for p in problems if "Summary Checklist" not in p]
            else:
                lecture_notes += 1
            if problems:
                failures.append((note, problems))
            stem = tx_keys.get(stem_key(note.stem))
            if stem and is_lecture and not is_placeholder(transcripts[stem]):
                w = fidelity_warnings(note, transcripts[stem])
                if w:
                    warnings.append((note, w))
            elif is_lecture and not stem:
                warnings.append((note, ["no matching transcript file"]))
            elif is_lecture:
                unsourced.append(note)

    if not args.coverage:
        print(f"lecture notes checked: {lecture_notes} "
              f"(+{notes_checked - lecture_notes} reference pages)")
        if failures:
            print(f"\nSTRUCTURAL PROBLEMS: {len(failures)}")
            for note, problems in failures[:40]:
                print(f"  {note.relative_to(ROOT)}")
                for p in problems:
                    print(f"      - {p}")
            if len(failures) > 40:
                print(f"  ... and {len(failures) - 40} more")
        if warnings:
            print(f"\nFIDELITY WARNINGS (heuristic — review, do not panic): "
                  f"{len(warnings)}")
            print("  Notes contain the *solution* code shown on screen in the videos,")
            print("  which the instructor never reads out loud, so literals that do not")
            print("  appear in the transcript are usually fine. Treat these as a")
            print("  to-review list, not as errors.")
            for note, warns in warnings[:10]:
                print(f"  {note.relative_to(ROOT)}: {'; '.join(warns)}")
            if len(warnings) > 10:
                print(f"  ... and {len(warnings) - 10} more")
        if unsourced:
            print(f"\nUNSOURCED NOTES: {len(unsourced)} notes were written for lectures "
                  f"that have no transcript text,")
            print("  so they cannot be checked against the course (spot-check them by")
            print("  hand if you rely on them).")

    if args.report or args.coverage:
        missing_notes, missing_untranscribed = [], []
        untranscribed_without_note = 0
        notes_without_source = 0
        real_transcripts = 0
        for day in sorted(set(ay) | set(tr)):
            tx_dir, note_dir = tr.get(day), ay.get(day)
            t_stems = {p.stem: p for p in tx_dir.glob("*.txt")} if tx_dir else {}
            n_stems = ([p.stem for p in note_dir.glob("*.md")] if note_dir else [])
            n_keys = {stem_key(s) for s in n_stems}
            for stem, path in t_stems.items():
                placeholder = is_placeholder(path)
                if not placeholder:
                    real_transcripts += 1
                if stem_key(stem) in n_keys:
                    continue
                if placeholder:
                    missing_untranscribed.append((day, stem))
                else:
                    missing_notes.append((day, stem))
            for stem in n_stems:
                if not LECTURE_NOTE_RE.match(stem):
                    continue
                partner = t_stems.get(stem) or next(
                    (p for s, p in t_stems.items() if stem_key(s) == stem_key(stem)), None)
                if partner is None:
                    notes_without_source += 1
                elif is_placeholder(partner):
                    notes_without_source += 1
        print(f"\nCOVERAGE: {real_transcripts} transcripts contain real text "
              f"(and {real_transcripts - len(missing_notes)} of them have a note)")
        print(f"COVERAGE: {len(missing_notes)} lecture(s) with real text still need a "
              f"note{f' — {missing_notes}' if missing_notes else ''}")
        print(f"COVERAGE: {len(missing_untranscribed) + untranscribed_without_note} "
              f"lectures have neither transcript nor notes (never transcribed)")
        print(f"COVERAGE: {notes_without_source} notes were written without source text "
              f"(no transcript exists — they cannot be verified against the course)")

    print()
    if failures or (args.strict and warnings):
        print("RESULT: FAIL")
        return 1
    status = "OK" if not warnings else "OK (with fidelity warnings to review)"
    print(f"RESULT: {status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
