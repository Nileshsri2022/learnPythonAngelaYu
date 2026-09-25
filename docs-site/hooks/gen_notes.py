"""
Generate the MkDocs site from the course notes and transcripts.

Design goals (UI simplicity + study workflow):
  * Top tab bar: Home | Study plan | Cheat sheets | Topic index | Beginner |
    Intermediate | Intermediate+ | Web Dev | Advanced
  * Every lecture note carries a **lecture card**: day, lecture number, reading time,
    a link to the matching raw transcript, the sibling lectures, and the note's file
    on GitHub.
  * Every transcript links *back* to its notes, and says so when the notes for that
    lecture do not exist yet (some lectures only have a transcript).
  * Day pages list every lecture (flagging transcript-only ones), the day's runnable
    project files, and a "mark this day complete" checkbox that the custom
    JavaScript persists in localStorage.
  * Auto-generated study aids: a study plan for all 85 days, per-track cheat sheets
    assembled from every note's "Summary Checklist", and an A–Z topic index built
    from every section heading.

Produces (in-memory virtual files, nothing written to disk):
  index.md                      homepage (+ progress widget)
  study-plan.md                 schedule, reading times, projects for all 85 days
  cheat-sheets/index.md         overview of the per-track cheat sheets
  cheat-sheets/<track>.md       every "Summary Checklist" item for that track
  topics/index.md               A–Z topic index (every section heading)
  days/<nn>/index.md            per-day overview (notes + transcripts + projects)
  days/<nn>/<slug>.md           one page per lecture note
  days/<nn>/transcript-*.md     one page per raw transcript (linked, not in the nav)
  SUMMARY.md                    explicit navigation for literate-nav
"""

from __future__ import annotations

import ast
import difflib
import html
import re
from pathlib import Path
from urllib.parse import quote

import mkdocs_gen_files

ROOT = Path(__file__).resolve().parent.parent          # docs-site/
REPO = ROOT.parent                                     # learnPythonAngelaYu/
ANGELAYU = REPO / "angelaYu"
TRANSCRIPTS = ANGELAYU / "transcripts"
GITHUB_BASE = "https://github.com/Nileshsri2022/learnPythonAngelaYu/blob/main/"
WORDS_PER_MINUTE = 200

# Track ranges — each track gets its own tab
TRACKS: dict[int, tuple[int, int, str]] = {
    1: (1, 14, "Beginner"),
    2: (15, 31, "Intermediate"),
    3: (32, 40, "Intermediate+"),
    4: (41, 58, "Web Dev"),
    5: (59, 85, "Advanced"),
}
TRACK_ORDER = list(TRACKS)

NOTE_RE = re.compile(r"^(\d+)\s*[.\-]?\s*(.*)$")
DASHES_RE = re.compile(r"^-{5,}\s*$")
DAY_PREFIX_RE = re.compile(r"^Day\s*\d+\s*[-–]?\s*(.*)$")
FENCE_RE = re.compile(r"^(\s*)(```|~~~)(.*)$")
UNSAFE_LABEL_RE = re.compile(r"[\[\]{}`|<>]")
CHECKLIST_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+(.*)$")

# Some transcript files are placeholders ("[No transcript available for this
# lecture]") because the lecture was never transcribed. The site must say so rather
# than pretend the lecture has a transcript.
PLACEHOLDER_MARKER = "No transcript available"

NAV_DAY_MAX = 36        # sidebar label length for day titles
NAV_LECTURE_MAX = 50    # sidebar label length for lecture titles

# Headings that are noise in the topic index (they repeat in many notes).
INDEX_STOPLIST = {
    "summary checklist", "overview", "key concepts", "next steps", "introduction",
    "what you will learn", "the solution", "the task", "the challenge", "the message",
    "the problem", "the project", "the pattern", "summary", "recap", "your turn",
    "practice exercise", "the setup", "the result",
}


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "page"


def clean_title(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip(" .–-")


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
    return t[:maxlen].rsplit(" ", 1)[0] + "…"


def nav_label(text: str) -> str:
    """Make a title safe to embed as literate-nav link text; strip [ ] { } ` |."""
    return re.sub(r"\s+", " ", UNSAFE_LABEL_RE.sub("", text)).strip()


def first_h1(text: str) -> str | None:
    """Return the first real H1, ignoring '#' comments inside fenced code blocks."""
    in_fence = False
    fence = ""
    for line in text.splitlines():
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(2)
            if not in_fence:
                in_fence, fence = True, marker
            elif line.strip().startswith(fence):
                in_fence, fence = False, ""
            continue
        if in_fence:
            continue
        if line.startswith("# "):
            return clean_title(line[2:])
    return None


def headings(text: str) -> list[str]:
    """All H2/H3 headings in a note, ignoring fenced code blocks."""
    out, in_fence, fence = [], False, ""
    for line in text.splitlines():
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(2)
            if not in_fence:
                in_fence, fence = True, marker
            elif line.strip().startswith(fence):
                in_fence, fence = False, ""
            continue
        if in_fence:
            continue
        h = re.match(r"^#{2,3}\s+(?:[\d.]+\s*)?(.+?)\s*$", line)
        if h:
            out.append(clean_title(h.group(1)))
    return out


def checklist_items(text: str) -> list[str]:
    """Items of the note's final 'Summary Checklist' section."""
    items: list[str] = []
    collecting = False
    for line in text.splitlines():
        if line.strip().lower().startswith(("### summary checklist", "## summary checklist")):
            collecting = True
            continue
        if collecting and line.startswith("#"):
            break
        if collecting:
            m = CHECKLIST_RE.match(line)
            if m:
                items.append(clean_title(m.group(1)))
    return items


def github_url(path: Path) -> str:
    rel = path.relative_to(REPO).as_posix()
    return GITHUB_BASE + quote(rel)


def reading_time(text: str) -> int:
    return max(1, round(len(text.split()) / WORDS_PER_MINUTE))


def human_time(minutes: int) -> str:
    if minutes < 60:
        return f"{minutes} min"
    h, rem = divmod(minutes, 60)
    return f"{h} h" if rem < 5 else f"{h} h {rem} min"


# --------------------------------------------------------------------------
# Post-processing of note markdown
# --------------------------------------------------------------------------

# Markdown links to files that live in the repo but not in the site (main.py,
# style.css, screenshots...). They are pointed at GitHub instead of being copied
# into the docs, which keeps the built site warning-free.
REL_LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)\s]+)(\))")


def rewrite_repo_links(text: str, note_path: Path) -> str:
    out: list[str] = []
    in_fence, fence = False, ""
    for line in text.splitlines():
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(2)
            if not in_fence:
                in_fence, fence = True, marker
            elif line.strip().startswith(fence):
                in_fence, fence = False, ""
            out.append(line)
            continue
        if not in_fence and "](" in line:
            line = REL_LINK_RE.sub(lambda mm: _link_or_github(mm, note_path), line)
        out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def _link_or_github(m: "re.Match[str]", note_path: Path) -> str:
    prefix, target, suffix = m.group(1), m.group(2), m.group(3)
    if re.match(r"^(https?:|mailto:|#|/)", target) or target.endswith((".md", ".txt")):
        return m.group(0)
    try:
        resolved = (note_path.parent / target).resolve()
        resolved.relative_to(REPO)
    except (ValueError, OSError):
        return m.group(0)
    if not resolved.is_file():
        return m.group(0)
    return f"{prefix}{github_url(resolved)}{suffix}"


def label_fences(text: str) -> str:
    """Give unlabelled code fences a language.

    An unlabelled block is highlighted as Python by MkDocs and copied as Python by
    readers. Many such blocks are expected program output, tracebacks or diagrams, so
    label a fence ``python`` when it parses as Python and ``text`` when it does not.
    Fences that already have a language are copied verbatim — including the closing
    fence, which must never be mistaken for the start of a new block.
    """
    lines = text.splitlines()
    out: list[str] = []
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
        if m.group(3).strip():                      # already labelled: keep as written
            out.append(lines[i])
        else:
            out.append(f"{indent}{marker}{'python' if _is_python(body) else 'text'}")
        out.extend(body)
        if close < n:
            out.append(lines[close])
        i = close + 1
    return "\n".join(out)


def _is_python(body: list[str]) -> bool:
    src = "\n".join(body)
    if not src.strip():
        return False
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False


# --------------------------------------------------------------------------
# Discover days, notes, transcripts, project files
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


def day_dir(day: int) -> Path | None:
    if not ANGELAYU.is_dir():
        return None
    nn = f"{day:02d}"
    for entry in sorted(ANGELAYU.iterdir()):
        if entry.is_dir() and re.match(rf"^{nn}-", entry.name):
            return entry
    return None


def notes_for_day(day: int) -> list[tuple[int | None, str, Path]]:
    directory = day_dir(day)
    if directory is None:
        return []
    items: list[tuple[int | None, str, Path]] = []
    for path in sorted(directory.glob("*.md")):
        m = NOTE_RE.match(path.stem)
        num = int(m.group(1)) if m and m.group(1).isdigit() else None
        title = clean_title(m.group(2)) if m else clean_title(path.stem)
        h1 = first_h1(path.read_text(encoding="utf-8", errors="replace"))
        items.append((num, h1 or title or f"Lecture {num}", path))
    items.sort(key=lambda it: (it[0] is None, it[0] if it[0] is not None else it[1]))
    return items


def project_files(day: int) -> list[Path]:
    directory = day_dir(day)
    if directory is None:
        return []
    wanted = {".py", ".html", ".css", ".csv", ".sh", ".json", ".txt", ".example"}
    seen: set[str] = set()
    out: list[Path] = []
    for p in sorted(directory.rglob("*")):
        if p.is_file() and p.suffix.lower() in wanted and p.name != "sdvh.txt":
            if p.name in seen and p.name.startswith("index"):
                continue
            seen.add(p.name)
            out.append(p)
    return out


def transcripts_for_day(day: int) -> list[tuple[str, Path]]:
    folder = None
    if TRANSCRIPTS.is_dir():
        for entry in sorted(TRANSCRIPTS.iterdir()):
            m = re.match(r"^(\d+)\s*-", entry.name)
            if entry.is_dir() and m and int(m.group(1)) == day:
                folder = entry
                break
    if folder is None:
        return []
    return [(p.stem, p) for p in sorted(folder.glob("*.txt"))]


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
    return title, html.escape(body)


def stem_key(stem: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"^\d+\s*[-.]\s*", "", stem.lower()))


def match_by_stem(stem: str, candidates: list[str]) -> str | None:
    """Find the candidate file stem that corresponds to ``stem`` (note <-> transcript)."""
    want = stem_key(stem)
    keys = {c: stem_key(c) for c in candidates}
    for c, key in keys.items():
        if key == want:
            return c
    m = re.match(r"^(\d+)", stem)
    if m:
        for c in candidates:
            if re.match(rf"^{m.group(1)}\b", c):
                return c
    best = difflib.get_close_matches(want, list(keys.values()), n=1, cutoff=0.72)
    if best:
        return next(c for c, key in keys.items() if key == best[0])
    return None


# --------------------------------------------------------------------------
# Output helpers
# --------------------------------------------------------------------------

def write(vpath: str, content: str) -> None:
    with mkdocs_gen_files.open(vpath, "w") as f:
        f.write(content)


def unique_slug(base: str, used: set[str]) -> str:
    slug, i = base, 2
    while slug in used:
        slug = f"{base}-{i}"
        i += 1
    used.add(slug)
    return slug


def lecture_card(*, day: int, track_name: str, position: int, total: int, minutes: int,
                 transcript: str | None, source: Path, prev_link: str,
                 next_link: str) -> str:
    links = []
    if transcript:
        links.append(f"[🗣 Full transcript]({transcript})")
    links.append(f"[📄 Note source]({github_url(source)})")
    return (
        '<div class="lecture-card" markdown>\n\n'
        f"**Day {day}** · {track_name} · **Lecture {position} of {total}** · "
        f"⏱ {human_time(minutes)} read\n\n"
        f"{' · '.join(links)}\n\n"
        f"[← Previous]({prev_link}) · [Day overview](index.md) · [Next →]({next_link})\n\n"
        "</div>\n"
    )


# --------------------------------------------------------------------------
# Build the site
# --------------------------------------------------------------------------

titles = day_titles()
tracks_nav: dict[int, list[str]] = {k: [] for k in TRACK_ORDER}
day_rows: dict[int, list[str]] = {k: [] for k in TRACK_ORDER}
cheat_sections: dict[int, list[str]] = {k: [] for k in TRACK_ORDER}
plan_rows: list[str] = []
topics: dict[str, dict[str, str]] = {}      # heading -> {link: label}
stats = {"notes": 0, "transcripts": 0, "transcript_only": 0, "minutes": 0}

for day in sorted(titles):
    tid = next((t for t in TRACK_ORDER if TRACKS[t][0] <= day <= TRACKS[t][1]), None)
    if tid is None:
        continue
    track_name = TRACKS[tid][2]
    day_title = titles.get(day, f"Day {day}")
    notes = notes_for_day(day)
    transcripts = transcripts_for_day(day)
    transcripts_with_text = [s for s, p in transcripts
                             if PLACEHOLDER_MARKER not in
                             p.read_text(encoding="utf-8", errors="replace")]
    projects = project_files(day)

    nn = f"{day:02d}"
    section = f"days/{nn}"
    used: set[str] = set()

    # ---- transcript pages (written first: note cards link to them) ---------
    trans_slugs: dict[str, str] = {}
    for stem, path in transcripts:
        slug = unique_slug(slugify(stem), used)
        trans_slugs[stem] = f"transcript-{slug}.md"
    note_stems = [p.stem for _, _, p in notes]
    note_slugs = {}
    for num, title, path in notes:
        base = f"{num}-{slugify(title)}" if num is not None else slugify(title)
        note_slugs[path.stem] = f"{unique_slug(base, used)}.md"

    for stem, path in transcripts:
        t_title, body = transcript_body(path)
        words = len(body.split())
        has_text = PLACEHOLDER_MARKER not in body
        partner = match_by_stem(stem, note_stems)
        links = []
        if partner:
            links.append(f"[📖 Lecture notes for this topic]({note_slugs[partner]})")
        else:
            links.append("📖 *Notes for this lecture have not been written yet — "
                         "this is the raw source material.*")
        links.append(f"[← Day {day} overview](index.md)")
        if has_text:
            intro = (f"> 🗣 **Raw course transcript** — what the instructor said, "
                     f"word for word ({words:,} words).")
        else:
            intro = ("> ⚠️ **No transcript exists for this lecture.** The course video "
                     "was never transcribed, so this page is a placeholder.")
        write(
            f"{section}/{trans_slugs[stem]}",
            f"---\ntitle: {html.escape(t_title)}\n---\n\n"
            f"# {html.escape(t_title)}\n\n"
            f"{intro}\n\n"
            f"{' · '.join(links)}\n\n"
            f"{body}\n",
        )

    # ---- note pages --------------------------------------------------------
    toc: list[tuple[str, str, int]] = []          # nav label, link, minutes
    for idx, (num, title, path) in enumerate(notes):
        slug = note_slugs[path.stem]
        raw = path.read_text(encoding="utf-8", errors="replace")
        body = label_fences(rewrite_repo_links(raw, path))
        minutes = reading_time(body)
        prev_link = note_slugs[notes[idx - 1][2].stem] if idx > 0 else "index.md"
        next_link = (note_slugs[notes[idx + 1][2].stem]
                     if idx + 1 < len(notes) else "index.md")
        t_stem = match_by_stem(path.stem, list(trans_slugs))
        card = lecture_card(
            day=day, track_name=track_name, position=idx + 1, total=len(notes),
            minutes=minutes, transcript=trans_slugs.get(t_stem) if t_stem else None,
            source=path, prev_link=prev_link, next_link=next_link,
        )
        label = f"{num}. {title}" if num is not None else title
        write(f"{section}/{slug}",
              f"---\ntitle: {html.escape(title)}\n---\n\n{card}\n{body}")
        toc.append((label, slug, minutes))

        # study aids
        for h in headings(body):
            if h.lower() not in INDEX_STOPLIST and len(h) > 2:
                topics.setdefault(h, {})[f"../{section}/{slug}"] = f"Day {day} — {title}"
        items = checklist_items(body)
        if items:
            block = [f"### Day {day} · {title}", "",
                     f"[Open the notes](../{section}/{slug})", ""]
            block += [f"- {html.escape(i)}" for i in items]
            block.append("")
            cheat_sections[tid].append("\n".join(block))

    # ---- day overview page -------------------------------------------------
    tracked_minutes = sum(m for _, _, m in toc)
    total_minutes = tracked_minutes or 1
    overview = [f"# Day {day} — {html.escape(day_title)}", ""]
    head_bits = [f"**{track_name}**"]
    if notes:
        head_bits.append(f"**{len(notes)} notes**")
    if transcripts_with_text:
        head_bits.append(f"**{len(transcripts_with_text)} transcripts**")
    if len(transcripts) > len(transcripts_with_text):
        head_bits.append(f"{len(transcripts) - len(transcripts_with_text)} without text")
    if tracked_minutes:
        head_bits.append(f"⏱ ~{human_time(tracked_minutes)} of reading")
    overview += [" · ".join(head_bits), ""]
    overview += [
        "!!! tip \"How to study this day\"",
        "    1. Skim the lecture notes below for the day's shape.",
        "    2. Read a note, then try the code yourself before opening the transcript.",
        "    3. Use the transcript only when the note is not enough (it is word for word).",
        "    4. Finish with the day's project file and the summary checklist.",
        "",
    ]

    if projects:
        overview += ["## 🧩 Project files", ""]
        for p in projects[:12]:
            rel = p.relative_to(day_dir(day)).as_posix()
            overview.append(f"- [`{rel}`]({github_url(p)})")
        if len(projects) > 12:
            overview.append(f"- … and {len(projects) - 12} more in the repository")
        overview.append("")

    if notes or transcripts:
        overview += ["## 📖 Lectures", "",
                     "| # | Lecture | Notes | Transcript |", "| --- | --- | --- | --- |"]
        tr_candidates = list(trans_slugs)
        for num, title, path in notes:
            n = num if num is not None else "—"
            t_stem = match_by_stem(path.stem, tr_candidates)
            if t_stem and t_stem in transcripts_with_text:
                t_link = f"[🗣 transcript]({trans_slugs[t_stem]})"
            elif t_stem:
                t_link = f"[⚪ placeholder]({trans_slugs[t_stem]})"
            else:
                t_link = "—"
            overview.append(
                f"| {n} | [{html.escape(title)}]({note_slugs[path.stem]}) | "
                f"📖 notes | {t_link} |")
        # transcripts with no note at all
        for stem, path in transcripts:
            partner = match_by_stem(stem, note_stems)
            if partner:
                continue
            t_title = clean_title(stem.split("-", 1)[1] if "-" in stem else stem)
            overview.append(
                f"| — | {html.escape(t_title)} | ❔ *not written yet* | "
                f"[🗣 transcript]({trans_slugs[stem]}) |")
        overview.append("")
        missing = sum(1 for stem, _ in transcripts if not match_by_stem(stem, note_stems))
        if missing:
            untranscribed = sum(
                1 for stem, _ in transcripts
                if not match_by_stem(stem, note_stems) and stem not in transcripts_with_text)
            detail = (" (the source material has no transcript for "
                      f"{untranscribed} of them)") if untranscribed else ""
            overview += [
                f"> ❔ **{missing} lecture(s) today have no written notes yet**{detail}. "
                "Notes are added over time.",
                "",
            ]

    overview += [
        "## ✅ Progress",
        "",
        "- [ ] I have finished this day",
        "",
        "<div class=\"progress-note\">Tick the box and it is remembered in this browser "
        "(nothing is uploaded anywhere). The <a href=\"../../index.md\">home page</a> "
        "shows how many days you have completed.</div>",
        "",
    ]
    prev_day = f"[← Day {day - 1}]({'../' + str(day - 1).zfill(2) + '/index.md'})" \
        if day > 1 else "[← Home](../../index.md)"
    next_day = (f"[Day {day + 1} →]({'../' + str(day + 1).zfill(2) + '/index.md'})"
                if day < max(titles) else "[All days →](../../index.md)")
    overview += [f"{prev_day} · [All days](../../index.md) · {next_day}", ""]
    write(f"{section}/index.md", "\n".join(overview))

    # ---- nav / tables ------------------------------------------------------
    day_index = f"{section}/index.md"
    tracks_nav[tid].append(f"    - [Day {day} · {nav_label(short_title(day_title))}]"
                           f"({day_index})")
    for label, slug, _ in toc:
        short = label if len(label) <= NAV_LECTURE_MAX else \
            label[:NAV_LECTURE_MAX].rsplit(" ", 1)[0] + "…"
        tracks_nav[tid].append(f"        - [{nav_label(short)}]({section}/{slug})")

    n_missing = sum(1 for stem, _ in transcripts if not match_by_stem(stem, note_stems))
    day_rows[tid].append(
        f"| [Day {day}]({day_index}) | {html.escape(day_title)} | "
        f"{len(notes) or '—'} | {len(transcripts) or '—'} | "
        f"{'⏱ ' + human_time(tracked_minutes) if tracked_minutes else '—'} |")
    plan_rows.append(
        f"| [Day {day}]({day_index}) | {track_name} | {html.escape(day_title)} | "
        f"{len(notes)} | {len(transcripts)} | "
        f"{'~' + human_time(tracked_minutes) if tracked_minutes else '—'} | "
        f"{len(projects) or '—'} |")

    stats["notes"] += len(notes)
    stats["transcripts"] += len(transcripts_with_text)
    stats["transcripts"] += 0  # placeholders are not counted as transcripts
    stats["transcript_only"] += n_missing
    stats["minutes"] += tracked_minutes

# --------------------------------------------------------------------------
# Study plan
# --------------------------------------------------------------------------

write("study-plan.md", "\n".join([
    "# Study plan",
    "",
    f"The course is {len(titles)} days long. At one day per sitting that is roughly "
    "**three months**; at a day per week it is a two-year hobby. Pick a pace you can "
    "keep, and keep the *streak* — momentum is the whole point of the format.",
    "",
    "| Pace | Days per week | Finish in |",
    "| --- | --- | --- |",
    "| Casual | 3 | ~7 months |",
    "| Steady (recommended) | 5 | ~4 months |",
    "| Intensive | 7 | ~3 months |",
    "",
    "## How to work through a day",
    "",
    "1. **Read the notes first** — they are the condensed version of the lecture.",
    "2. **Write the code yourself** before looking at the day's `.py` file.",
    "3. **Use the transcript** when a note leaves you with a question; it is verbatim.",
    "4. **Do the project** — the projects are the point; the syntax is the excuse.",
    "5. **Tick the day off** on its page so the home page progress bar moves.",
    "",
    "## Every day at a glance",
    "",
    "| Day | Track | Focus | Notes | Transcripts | Reading | Project files |",
    "| --- | ----- | ----- | ----- | ----------- | ------- | ------------- |",
    *plan_rows,
    "",
]))

# --------------------------------------------------------------------------
# Cheat sheets (built from every note's Summary Checklist)
# --------------------------------------------------------------------------

write("cheat-sheets/index.md", "\n".join([
    "# Cheat sheets",
    "",
    "Every lecture note ends with a **Summary Checklist**. This section collects all of",
    "them, track by track, so you can revise a whole module in a few minutes without",
    "re-reading the notes.",
    "",
    "| Track | Days | Reference |",
    "| --- | --- | --- |",
    *[f"| {TRACKS[t][2]} | {TRACKS[t][0]}–{TRACKS[t][1]} | "
      f"[Open cheat sheet]({slugify(TRACKS[t][2])}.md) |" for t in TRACK_ORDER],
    "",
    "> Printing hint: open a cheat sheet and use your browser's print view — the site",
    "> ships a print stylesheet that drops the navigation.",
    "",
]))

for tid in TRACK_ORDER:
    start, end, name = TRACKS[tid]
    blocks = cheat_sections[tid]
    write(f"cheat-sheets/{slugify(name)}.md", "\n".join([
        f"# {name} — cheat sheet",
        "",
        f"Days {start}–{end} · {len(blocks)} lectures with a summary checklist.",
        "",
        "---",
        "",
        *blocks,
        "",
        "[← All cheat sheets](index.md)",
        "",
    ]))

# --------------------------------------------------------------------------
# Topic index (A–Z of every section heading in every note)
# --------------------------------------------------------------------------

letters: dict[str, list[tuple[str, str]]] = {}
for heading, places in topics.items():
    first = heading[0].upper()
    key = first if first.isalpha() else "0–9 / symbols"
    letters.setdefault(key, []).append((heading, str(len(places))))

topic_lines = [
    "# Topic index",
    "",
    f"Every section heading in the lecture notes ({len(topics)} topics), alphabetically.",
    "Use <kbd>Ctrl</kbd>+<kbd>F</kbd> (or <kbd>⌘</kbd>+<kbd>F</kbd>) on this page to jump",
    "to a concept and see which lectures cover it.",
    "",
]
for key in sorted(letters, key=lambda k: (k == "0–9 / symbols", k.lower())):
    topic_lines += [f"## {key}", ""]
    for heading, places in sorted(letters[key], key=lambda h: h[0].lower()):
        links = topics[heading]
        if len(links) == 1:
            link, label = next(iter(links.items()))
            topic_lines.append(f"- [{heading}]({link}) — {label}")
        else:
            topic_lines.append(f"- **{heading}** — {len(links)} lectures")
    topic_lines.append("")
write("topics/index.md", "\n".join(topic_lines))

# --------------------------------------------------------------------------
# Homepage
# --------------------------------------------------------------------------

home = [
    "# 100 Days of Python — Study Notes",
    "",
    "Study notes and full transcripts for **Angela Yu's 100 Days of Code: The Complete",
    "Python Pro Bootcamp** — written to be *read*, not skimmed.",
    "",
    f"**{len(titles)} days · {stats['notes']} lecture notes · "
    f"{stats['transcripts']} transcripts · ~{human_time(stats['minutes'])} of reading**",
    "",
    f'<div id="progress-widget" class="progress-widget" data-days="{len(titles)}" markdown>',
    "",
    "Your progress: *<span id=\"progress-line\">no days marked yet</span>*",
    "",
    "<div class=\"progress-bar\"><span id=\"progress-fill\"></span></div>",
    "",
    "</div>",
    "",
    "## Start here",
    "",
    "| | |",
    "| --- | --- |",
    "| 🗺 **[Study plan](study-plan.md)** | A realistic pace, and how to work through a day |",
    "| 🧾 **[Cheat sheets](cheat-sheets/index.md)** | Every summary checklist, per track |",
    "| 🔎 **[Topic index](topics/index.md)** | Find any concept (A–Z) and where it is taught |",
    "| 📖 **Day pages** | Pick a day from the tabs above |",
    "| 🗣 **Transcripts** | Linked from every note, word for word |",
    "",
    "## What makes these notes different",
    "",
    "- **One idea per section** with runnable code, not walls of video transcript.",
    "- **Every note links to its raw transcript**, so you can always check the source.",
    "- **Summary checklists** at the end of each note — collected in the cheat sheets.",
    "- **Day pages show what is missing**: lectures whose notes are still to be written",
    "  are listed honestly, with their transcript.",
    "",
    "## All days at a glance",
    "",
]

for tid in TRACK_ORDER:
    start, end, name = TRACKS[tid]
    home += [f"### {name} (Days {start}–{end})", "",
             "| Day | Focus | Notes | Transcripts | Reading |",
             "| --- | ----- | ----- | ----------- | ------- |",
             *day_rows[tid], ""]

home += [
    "## Topics covered",
    "",
    "- **Beginner:** variables, data types, control flow, loops, functions, debugging,",
    "  the first capstone projects",
    "- **Intermediate:** OOP, Turtle GUI games, files & paths, CSV/Pandas, list",
    "  comprehension, Tkinter apps, errors & JSON",
    "- **Intermediate+:** APIs, authentication, SMS, web scraping, Selenium, data entry",
    "  automation, Flask foundations",
    "- **Web Dev:** HTML, CSS, Bootstrap, Flask, Jinja templating, full-stack apps",
    "- **Advanced:** SQLite & SQLAlchemy, REST APIs, authentication, Git/GitHub,",
    "  deployment, data science (Pandas, NumPy, Matplotlib, Seaborn, Plotly)",
    "",
    "---",
    "",
    "*Notes are derived from the course transcripts; the originals live in*",
    "[`angelaYu/transcripts/`](https://github.com/Nileshsri2022/learnPythonAngelaYu/tree/main/angelaYu/transcripts).",
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
    "- [Study plan](study-plan.md)",
    "- Cheat sheets",
    "    - [Overview](cheat-sheets/index.md)",
]
for tid in TRACK_ORDER:
    name = TRACKS[tid][2]
    summary.append(f"    - [{nav_label(name)}](cheat-sheets/{slugify(name)}.md)")
summary.append("- [Topic index](topics/index.md)")
for tid in TRACK_ORDER:
    start, end, name = TRACKS[tid]
    summary.append(f"- Days {start}–{end} · {name}()")
    summary += tracks_nav[tid]
summary.append("")

write("SUMMARY.md", "\n".join(summary))
