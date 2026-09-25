"""
Generate the MkDocs site from the course notes and transcripts.

Design goals (UI simplicity):
  * Top tab bar: Home | Beginner | Intermediate | Intermediate+ | Web Dev | Advanced
  * Sidebar shows ONLY the days (short titles) and, inside one day, its
    lecture notes.
  * Long titles are shortened for the sidebar; full titles stay on the pages.

Produces (in-memory virtual files, nothing written to disk):
  index.md                      homepage
  days/<nn>/index.md            per-day overview (notes + transcripts)
  days/<nn>/<slug>.md           one page per lecture note
  days/<nn>/transcript-*.md     one page per raw transcript (not in the sidebar)
  SUMMARY.md                    explicit navigation for literate-nav
"""

from __future__ import annotations

import html
import re
from pathlib import Path

import mkdocs_gen_files

ROOT = Path(__file__).resolve().parent.parent          # docs-site/
REPO = ROOT.parent                                     # learnPythonAngelaYu/
TRANSCRIPTS = REPO / "angelaYu" / "transcripts"
GITHUB_BASE = "https://github.com/Nileshsri2022/learnPythonAngelaYu/blob/main/"

# Track ranges — each track gets its own tab
TRACKS = {
    1: (1, 14, "Beginner"),
    2: (15, 31, "Intermediate"),
    3: (32, 40, "Intermediate+"),
    4: (41, 58, "Web Dev"),
    5: (59, 85, "Advanced"),
}

NOTE_RE = re.compile(r"^(\d+)\s*[.\-]?\s*(.*)$")
DASHES_RE = re.compile(r"^-{5,}\s*$")
DAY_PREFIX_RE = re.compile(r"^Day\s*\d+\s*[-–]?\s*(.*)$")

NAV_DAY_MAX = 36        # sidebar label length for day titles
NAV_LECTURE_MAX = 50    # sidebar label length for lecture titles


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "page"


def clean_title(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip(" .–")


def short_title(text: str, maxlen: int = NAV_DAY_MAX) -> str:
    t = clean_title(text)
    if len(t) <= maxlen:
        return t
    t = re.sub(r"\s*[-–]\s*(Beginner|Intermediate\+?|Advanced|Web Foundation)\s*$",
               "", t).strip(" -–")
    if len(t) <= maxlen:
        return t
    parts = [p.strip() for p in t.split(" - ") if p.strip()]
    if len(parts) > 1:
        if len(parts[0]) <= maxlen:
            return parts[0]
        if len(parts[-1]) <= maxlen:
            return parts[-1]
    cut = t[:maxlen].rsplit(" ", 1)[0]
    return cut + "…"


def first_h1(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return clean_title(line[2:])
    return None


def github_url(path: Path) -> str:
    from urllib.parse import quote
    rel = path.relative_to(REPO).as_posix()
    return GITHUB_BASE + quote(rel)


# --------------------------------------------------------------------------
# Discover days
# --------------------------------------------------------------------------

def day_titles() -> dict[int, str]:
    titles: dict[int, str] = {}
    if not TRANSCRIPTS.is_dir():
        return titles
    for entry in sorted(TRANSCRIPTS.iterdir()):
        m = re.match(r"^(\d+)\s*-\s*(.+)$", entry.name)
        if entry.is_dir() and m:
            rest = m.group(2)
            dm = DAY_PREFIX_RE.match(rest)
            titles[int(m.group(1))] = clean_title(dm.group(1) if dm else rest)
    return titles


def notes_for_day(day: int) -> list[tuple[int | None, str, Path]]:
    """Find .md lecture note files in angelaYu/Day N/."""
    nn = f"{day:02d}"
    # Find the matching Day N directory
    notes_dir = None
    for entry in (REPO / "angelaYu").iterdir():
        if entry.is_dir() and re.match(rf"^{nn}-", entry.name):
            notes_dir = entry
            break
    if notes_dir is None:
        return []

    items: list[tuple[int | None, str, Path]] = []
    for path in sorted(notes_dir.glob("*.md")):
        stem = path.stem
        m = NOTE_RE.match(stem)
        num = int(m.group(1)) if m and m.group(1).isdigit() else None
        title = clean_title(m.group(2)) if m else clean_title(stem)
        h1 = first_h1(path.read_text(encoding="utf-8", errors="replace"))
        items.append((num, h1 or title or f"Lecture {num}", path))
    items.sort(key=lambda it: (it[0] is None, it[0] if it[0] is not None else it[1]))
    return items


def transcripts_for_day(day: int) -> list[tuple[str, Path]]:
    folder = TRANSCRIPTS / _transcript_dirname(day)
    if folder is None or not folder.is_dir():
        return []
    return [(p.stem, p) for p in sorted(folder.glob("*.txt"))]


def _transcript_dirname(day: int) -> str | None:
    if not TRANSCRIPTS.is_dir():
        return None
    for entry in TRANSCRIPTS.iterdir():
        m = re.match(r"^(\d+)\s*-", entry.name)
        if entry.is_dir() and m and int(m.group(1)) == day:
            return entry.name
    return None


def transcript_body(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    title, body_start = path.stem, 0
    for i, line in enumerate(lines[:12]):
        if DASHES_RE.match(line.strip()):
            body_start = i + 1
            break
        lm = re.match(r"^Lecture:\s*(.+)$", line)
        if lm:
            title = clean_title(lm.group(1))
    body = "\n".join(lines[body_start:]).strip()
    # Escape raw HTML tags in transcripts
    body = html.escape(body)
    return title, body


# --------------------------------------------------------------------------
# Slugs / output helper
# --------------------------------------------------------------------------

page_slugs: set[str] = set()


def unique_slug(base: str) -> str:
    slug, i = base, 2
    while slug in page_slugs:
        slug = f"{base}-{i}"
        i += 1
    page_slugs.add(slug)
    return slug


def write(vpath: str, content: str) -> None:
    with mkdocs_gen_files.open(vpath, "w") as f:
        f.write(content)


# --------------------------------------------------------------------------
# Build virtual files
# --------------------------------------------------------------------------

titles = day_titles()
tracks_nav: dict[int, list[str]] = {k: [] for k in TRACKS}
day_rows: dict[int, list[str]] = {k: [] for k in TRACKS}
totals = {"notes": 0, "transcripts": 0}

for day in sorted(titles):
    track = None
    for tid, (start, end, _) in TRACKS.items():
        if start <= day <= end:
            track = tid
            break
    if track is None:
        continue

    day_title = titles.get(day, f"Day {day}")
    notes = notes_for_day(day)
    transcripts = transcripts_for_day(day)

    nn = f"{day:02d}"
    section = f"days/{nn}"
    page_slugs = set()

    # ---- lecture note pages ------------------------------------------------
    toc: list[tuple[str, str, str]] = []
    for num, title, path in notes:
        base = f"{num}-{slugify(title)}" if num is not None else slugify(title)
        slug = unique_slug(base)
        write(f"{section}/{slug}.md",
              path.read_text(encoding="utf-8", errors="replace"))
        label = f"{num}. {title}" if num is not None else title
        toc.append((label, f"{slug}.md", slug))

    # ---- transcript pages (NOT in the sidebar) ----------------------------
    trans_links: list[tuple[str, str]] = []
    for stem, path in transcripts:
        t_title, body = transcript_body(path)
        slug = unique_slug(slugify(stem))
        write(f"{section}/transcript-{slug}.md",
              f"# {html.escape(t_title)}\n\n"
              f"> 🗣 Raw course transcript — what the instructor said, word for word.\n\n"
              f"{body}\n")
        trans_links.append((clean_title(t_title), f"transcript-{slug}.md"))

    # ---- day overview page ------------------------------------------------
    overview = [f"# Day {day} — {html.escape(day_title)}", ""]
    track_name = TRACKS[track][2]
    stats_parts = [f"**{track_name}**"]
    if notes:
        stats_parts.append(f"**{len(notes)} notes**")
    stats_parts.append(f"**{len(transcripts)} transcripts**")
    overview += [" · ".join(stats_parts), ""]

    if notes:
        overview += ["## 📖 Lecture notes", ""]
        for label, link, _ in toc:
            overview.append(f"- [{html.escape(label)}]({link})")
        overview.append("")
    if trans_links:
        overview += ["## 🗣 Raw transcripts", ""]
        overview += [f"<details><summary>Show the verbatim lecture transcripts "
                     f"({len(trans_links)})</summary>", ""]
        for label, link in trans_links:
            overview.append(f"- [{html.escape(label)}]({link})")
        overview += ["", "</details>", ""]
    overview += [f"[← All days](../../index.md)", ""]
    write(f"{section}/index.md", "\n".join(overview))

    # ---- nav: days carry only their lecture notes --------------------------
    day_index = f"{section}/index.md"
    nav_day = f"    - [Day {day} · {html.escape(short_title(day_title))}]({day_index})"
    tracks_nav[track].append(nav_day)
    for label, link, _ in toc:
        short = label if len(label) <= NAV_LECTURE_MAX else label[:NAV_LECTURE_MAX].rsplit(" ", 1)[0] + "…"
        tracks_nav[track].append(f"        - [{html.escape(short)}]({section}/{link})")

    totals["notes"] += len(notes)
    totals["transcripts"] += len(trans_links)
    day_rows[track].append(
        f"| [Day {day}]({day_index}) | {html.escape(day_title)} | "
        f"{len(notes) or '—'} | {len(transcripts)} |"
    )

# --------------------------------------------------------------------------
# Homepage
# --------------------------------------------------------------------------

home = [
    "# 100 Days of Python — Study Notes",
    "",
    "Personal study notes and full course transcripts for **Angela Yu's",
    "100 Days of Code: The Complete Python Pro Bootcamp**.",
    "",
    f"- **{len(titles)} days · {totals['notes']} lecture notes · {totals['transcripts']} transcripts**",
    "- Search everything with <kbd>Ctrl</kbd>+<kbd>K</kbd> — notes, transcripts.",
    "",
    "| | |",
    "| --- | --- |",
    "| 📖 **Learn** | Pick a day from the tabs above |",
    "| 🗣 **Transcripts** | Collapsed at the bottom of each day page |",
    "",
    "## All days at a glance",
    "",
]

for tid in TRACKS:
    start, end, name = TRACKS[tid]
    home.append(f"### {name} (Days {start}–{end})")
    home.append("")
    home.append("| Day | Focus | Notes | Transcripts |")
    home.append("| --- | ----- | ----- | ----------- |")
    home += day_rows[tid]
    home.append("")

home += [
    "## Topics covered",
    "",
    "- **Beginner:** Python basics, variables, data types, loops, functions, "
    "OOP fundamentals",
    "- **Intermediate:** Tkinter GUI, file I/O, CSV, list comprehension, "
    "APIs, automation",
    "- **Intermediate+:** API integration, web scraping, Selenium, "
    "Flask web development",
    "- **Web Dev:** HTML, CSS, Bootstrap, Jinja templating, "
    "Flask full-stack apps",
    "- **Advanced:** SQLAlchemy, REST APIs, authentication, deployment, "
    "data science with Pandas, NumPy, Matplotlib, Seaborn, Plotly",
    "",
]

write("index.md", "\n".join(home))

# --------------------------------------------------------------------------
# SUMMARY.md — top tabs
# --------------------------------------------------------------------------

summary = [
    "# Table of contents",
    "",
    "- [Home](index.md)",
]
for tid in TRACKS:
    start, end, name = TRACKS[tid]
    summary.append(f"- Days {start}–{end} · {name}()")
    summary += tracks_nav[tid]
summary.append("")

write("SUMMARY.md", "\n".join(summary))