#!/usr/bin/env python3
"""
Normalise the lecture notes in ``angelaYu/`` (mechanical, idempotent, safe).

The notes were written over many sessions and drift in small ways. This tool
fixes the *structural* drift only — it never rewrites prose:

1. **Title**   every note starts with ``# <Lecture title>``.
               The title is taken from an existing H1 (emoji stripped) or, if the
               note has no H1, from the file name (``03-Nesting Lists.md`` ->
               ``Nesting Lists``). The blank line after the H1 is guaranteed.
2. **Filler**  a leading "Here is a structured breakdown of …" sentence is
               dropped — it carries no information and read as machine output.
3. **Entities** HTML entities (``&#x27;``, ``&amp;``, ``&lt;`` …) introduced by an
               earlier escaping pass are decoded, so code and prose read correctly.
4. **Duplicates** a ``### Next Steps`` section that repeats ``### Summary``
               verbatim (18 notes in Days 23-40) is removed.
5. **Boilerplate** a ``### Key Concepts`` table whose rows all say
               "Introduced/used in this lecture" adds nothing and is removed.
6. **Fences**   every code fence gets a language: ``python`` when it parses as Python,
               ``text`` otherwise (output, tracebacks, diagrams, CSV samples).
7. **Trailing space** is stripped, files end with exactly one newline.

Usage::

    python3 tools/normalize_notes.py --check     # CI: non-zero if anything to fix
    python3 tools/normalize_notes.py --apply     # rewrite the files
    python3 tools/normalize_notes.py --apply --dry-run   # show the diff only
"""

from __future__ import annotations

import argparse
import ast
import difflib
import html
import re
import sys
from pathlib import Path

FENCE_RE = re.compile(r"^(\s*)(```|~~~)(.*)$")

DOCS_SITE = Path(__file__).resolve().parent.parent
REPO = DOCS_SITE.parent
ANGELAYU = REPO / "angelaYu"

PREAMBLE_RE = re.compile(r"^Here is (?:a|an|the|short|structured)\b.*?\.\s*$", re.I)
EMOJI_PREFIX_RE = re.compile(r"^[\U0001F300-\U0001FAFF\u2600-\u27BF]+\s*")
NUM_PREFIX_RE = re.compile(r"^\d+\s*[-.]\s*")
SECTION_RE = re.compile(r"^###\s+(.+?)\s*$")
BOILERPLATE_DESC = "introduced/used in this lecture"


def clean_title(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip(" .–-")


def title_for(path: Path, text: str) -> str:
    """Title of the note: an H1 on line 1 if there is one, else the file name.

    Only line 1 counts — a ``#`` comment on the first line of a fenced Python
    block must never be mistaken for the page title (it once was: a note opened
    with ``# List inside a dictionary`` and the nav label followed it).
    """
    first = text.splitlines()[0].strip() if text.strip() else ""
    if first.startswith("# "):
        t = EMOJI_PREFIX_RE.sub("", clean_title(first[2:]))
        if t:
            return t
    return clean_title(NUM_PREFIX_RE.sub("", path.stem)) or path.stem


def strip_filler(text: str) -> tuple[str, bool]:
    """Drop a leading 'Here is a …' sentence (only when it is the first block)."""
    lines = text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and PREAMBLE_RE.match(lines[i].strip()):
        j = i
        while j < len(lines) and lines[j].strip():
            j += 1
        del lines[i:j]
        return "\n".join(lines), True
    return text, False


def set_h1(text: str, title: str) -> tuple[str, bool]:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        if lines[0].strip() == f"# {title}":
            # still guarantee a blank line after the H1
            if len(lines) > 1 and lines[1].strip():
                lines.insert(1, "")
                return "\n".join(lines), True
            return text, False
        lines[0] = f"# {title}"
        rest = lines[1:]
        while rest and not rest[0].strip():
            rest.pop(0)
        return "\n".join([lines[0], ""] + rest), True
    while lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join([f"# {title}", ""] + lines), True


def decode_entities(text: str) -> tuple[str, bool]:
    if not re.search(r"&#?\w+;", text):
        return text, False
    decoded = html.unescape(text)
    return (decoded, decoded != text)


def drop_duplicate_sections(text: str) -> tuple[str, bool]:
    """Remove a '### Next Steps' section that only repeats '### Summary'."""
    blocks = re.split(r"(?m)^(?=###\s)", text)
    sections: dict[str, int] = {}
    for idx, b in enumerate(blocks):
        m = SECTION_RE.match(b.splitlines()[0]) if b.strip() else None
        if m:
            sections.setdefault(m.group(1).strip().lower(), idx)
    if "summary" in sections and "next steps" in sections:
        # compare the bodies only — the heading line itself always differs
        body = lambda b: re.sub(r"\W+", " ", "\n".join(b.splitlines()[1:])).strip()  # noqa: E731
        summary = body(blocks[sections["summary"]])
        nxt = body(blocks[sections["next steps"]])
        if summary[:200] and summary[:200] == nxt[:200]:
            del blocks[sections["next steps"]]
            return re.sub(r"\n{3,}", "\n\n", "".join(blocks)).strip() + "\n", True
    return text, False


def drop_metadata_overview(text: str) -> tuple[str, bool]:
    """Drop the '### Overview' block that only repeats Course/Chapter/Lecture/Level.

    The generated site renders that metadata as a proper lecture card, so the
    hand-written copy is pure duplication.
    """
    blocks = re.split(r"(?m)^(?=###\s)", text)
    out, changed = [], False
    for b in blocks:
        head = b.splitlines()[0].strip().lower() if b.strip() else ""
        if head == "### overview":
            fields = re.findall(r"^\*\*(Course|Chapter|Lecture|Level|Duration|Difficulty):",
                                b, re.M | re.I)
            leftovers = [ln for ln in b.splitlines()[1:]
                         if ln.strip() and not ln.startswith("**")
                         and ln.strip() != "---"]
            if len(fields) >= 3 and not leftovers:
                changed = True
                continue
        out.append(b)
    if changed:
        return re.sub(r"\n{3,}", "\n\n", "".join(out)).strip() + "\n", True
    return text, False


def drop_boilerplate_key_concepts(text: str) -> tuple[str, bool]:
    blocks = re.split(r"(?m)^(?=###\s)", text)
    out, changed = [], False
    for b in blocks:
        head = b.splitlines()[0] if b.strip() else ""
        if head.strip().lower() in ("### key concepts", "### key concepts ") and \
                BOILERPLATE_DESC in b.lower():
            rows = [r for r in b.splitlines() if r.strip().startswith("|")]
            body = [r for r in rows if BOILERPLATE_DESC not in r.lower()]
            if len(body) <= 2:      # header row + separator only -> nothing left
                changed = True
                continue
        out.append(b)
    if changed:
        return re.sub(r"\n{3,}", "\n\n", "".join(out)).strip() + "\n", True
    return text, False


def label_fences(text: str) -> tuple[str, bool]:
    """Give every code fence a language: ``python`` if it parses, else ``text``.

    Unlabelled fences are highlighted as Python and copied as Python, but many of them
    are program output, tracebacks, diagrams or CSV samples. The generated site does
    the same thing at build time; doing it in the source keeps the repository readable
    and lets ``check_notes.py`` enforce it.
    """
    lines = text.splitlines()
    out: list[str] = []
    changed = False
    i, n = 0, len(lines)
    while i < n:
        m = FENCE_RE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        marker, indent = m.group(2), m.group(1)
        close = i + 1
        while close < n and not lines[close].strip().startswith(marker):
            close += 1
        body = lines[i + 1:close]
        if m.group(3).strip():
            out.append(lines[i])
        else:
            lang = "python" if _is_python(body) else "text"
            out.append(f"{indent}{marker}{lang}")
            changed = True
        out.extend(body)
        if close < n:
            out.append(lines[close])
        i = close + 1
    return "\n".join(out), changed


def _is_python(body: list[str]) -> bool:
    src = "\n".join(body)
    if not src.strip():
        return False
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False


def tidy(text: str) -> str:
    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def normalize(path: Path) -> tuple[str, str]:
    text = original = path.read_text(encoding="utf-8", errors="replace")
    text, _ = strip_filler(text)
    text, _ = set_h1(text, title_for(path, original))
    text, _ = decode_entities(text)
    text, _ = drop_duplicate_sections(text)
    text, _ = drop_metadata_overview(text)
    text, _ = drop_boilerplate_key_concepts(text)
    text, _ = label_fences(text)
    return original, tidy(text)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="write the changes")
    mode.add_argument("--check", action="store_true",
                      help="exit 1 if any note still needs normalising (CI)")
    ap.add_argument("--dry-run", action="store_true", help="print diffs, write nothing")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    changed, checked = [], 0
    for path in sorted(ANGELAYU.rglob("*.md")):
        if "transcripts" in path.parts:
            continue
        checked += 1
        before, after = normalize(path)
        if before == after:
            continue
        changed.append(path)
        if args.apply and not args.dry_run:
            path.write_text(after, encoding="utf-8")
            continue
        if not args.quiet and not args.check:
            rel = path.relative_to(REPO).as_posix()
            diff = difflib.unified_diff(before.splitlines(), after.splitlines(),
                                        lineterm="", n=1,
                                        fromfile=f"a/{rel}", tofile=f"b/{rel}")
            print("\n".join(list(diff)[:14]))

    if args.check:
        if changed:
            print(f"FAIL: {len(changed)} of {checked} notes are not normalised — "
                  f"run: python3 tools/normalize_notes.py --apply", file=sys.stderr)
            for p in changed[:20]:
                print("  ", p.relative_to(REPO).as_posix(), file=sys.stderr)
            return 1
        print(f"OK: all {checked} notes are normalised")
        return 0

    verb = "updated" if args.apply and not args.dry_run else "to update"
    if not args.quiet:
        print(f"\n{checked} notes checked, {len(changed)} {verb}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
