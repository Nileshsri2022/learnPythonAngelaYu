# Documentation site

A searchable study companion for the course, built with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

The pages are **generated in memory** from `angelaYu/` at build time by
[`hooks/gen_notes.py`](hooks/gen_notes.py) (via the `mkdocs-gen-files` plugin) —
nothing is duplicated on disk, so editing a note or transcript and saving rebuilds the
live site.

## What the site gives you

| | |
| --- | --- |
| **Lecture notes** | 473 structured notes across 66 days — one idea per section, runnable code, a summary checklist at the end |
| **Lecture card** | Every note opens with its day/lecture number, reading time, a link to the matching **raw transcript**, sibling-lecture links and the note's source file on GitHub |
| **Transcripts** | 367 verbatim transcripts, linked both ways: each transcript links back to its note, and says *"notes not written yet"* when there are none |
| **Placeholders** | 237 further transcripts were never recorded and hold only "[No transcript available for this lecture]" — the site flags them ⚠️ instead of passing them off as source material |
| **Study plan** | `study-plan.md` — a realistic pace, how to work through a day, and every day with its reading time and project files |
| **Cheat sheets** | `cheat-sheets/*` — every note's **Summary Checklist**, collected per track for quick revision (print-friendly) |
| **Topic index** | `topics/index.md` — an A–Z index of ~1,200 section headings, so you can find where any concept is taught |
| **Progress tracking** | Tick a day off on its page; the home page shows how many days you have completed (stored in your browser, never uploaded) |
| **Honest coverage** | Day pages list lectures whose notes are still to be written, with their transcript, instead of hiding them |
| **Navigation** | Top tabs per track, breadcrumbs, previous/next links, dark mode, full-text search across notes *and* transcripts |

## Run locally

```bash
pip install -r requirements.txt
mkdocs serve          # http://localhost:8000
```

## Build a static bundle

```bash
mkdocs build --strict     # output in site/
```

## Verify the site and the notes

```bash
python3 check_links.py                      # built site: internal links, thin pages
python3 check_notes.py --report             # notes: structure, fidelity vs transcripts, coverage
python3 tools/normalize_notes.py --check    # notes: normalisation drift (CI gate)
```

`check_notes.py` prints the coverage report — real transcripts, notes with no source
text, and lectures that were never transcribed. See [QUALITY.md](QUALITY.md) for the
audit results and what is still missing.

## Deploy to GitHub Pages (automatic)

Every push to `main` that touches `angelaYu/` or `docs-site/` runs the quality gates and
publishes the site to **https://nileshsri2022.github.io/learnPythonAngelaYu/** via
[`.github/workflows/deploy-docs.yml`](../.github/workflows/deploy-docs.yml). A separate
[`docs-quality.yml`](../.github/workflows/docs-quality.yml) workflow runs the same gates
on pull requests.

One-time setup (already done if the site is live): repository **Settings → Pages →
Build and deployment → Source: GitHub Actions**. You can also redeploy manually from the
**Actions** tab → *Deploy docs to GitHub Pages* → **Run workflow**.

Prefer pushing by hand instead? `mkdocs gh-deploy` still works — it builds and
force-pushes `site/` to the `gh-pages` branch.

## Structure

| Path | Purpose |
| --- | --- |
| `mkdocs.yml` | Site configuration (Material theme, search, dark mode, progress widget) |
| `hooks/gen_notes.py` | Generates the home page, day pages, lecture-note and transcript pages, study plan, cheat sheets, topic index and the nav |
| `tools/normalize_notes.py` | Keeps every note structurally consistent (H1, fences, entities, duplicates) |
| `tools/merge_duplicate_days.py` | (One-off) merged the duplicated Day 35/37/39/40 folders |
| `check_notes.py` | Source checks: structure, fidelity against transcripts, coverage report |
| `check_links.py` | Post-build crawler: internal links, thin pages, external sample |
| `docs/` | Handwritten assets: `404.md`, `stylesheets/extra.css`, `javascripts/progress.js` |
| `site/` | Build output (git-ignored) |
