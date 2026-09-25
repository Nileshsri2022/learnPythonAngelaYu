# Documentation site

A searchable, browsable website for the course transcripts, built with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

The pages are **generated in memory** from `../angelaYu/transcripts/` at build time by
[`hooks/gen_notes.py`](hooks/gen_notes.py) (via the `mkdocs-gen-files` plugin) —
nothing is duplicated on disk, so editing a transcript in `angelaYu/transcripts/` and saving
automatically rebuilds the live site.

## Run locally

```bash
pip install -r requirements.txt
mkdocs serve          # http://localhost:8000
```

## Build a static bundle

```bash
mkdocs build          # output in site/
```

## Deploy to GitHub Pages (automatic)

Deployment is automated with [`.github/workflows/deploy-docs.yml`](../.github/workflows/deploy-docs.yml):
every push to `main` that touches `angelaYu/` or `docs-site/` rebuilds the
site and publishes it to
**https://nileshsri2022.github.io/learnPythonAngelaYu/**

One-time setup (already done if the site is live): repository **Settings →
Pages → Build and deployment → Source: GitHub Actions**. You can also redeploy
manually from the **Actions** tab → *Deploy docs to GitHub Pages* → **Run workflow**.

Prefer pushing by hand instead? `mkdocs gh-deploy` still works — it builds and
force-pushes `site/` to the `gh-pages` branch.

## Verify the site

After `mkdocs build`, run the checker — it crawls every page, verifies every
internal link resolves, and confirms every page has real content:

```bash
python3 check_links.py
```

## Structure

| Path | Purpose |
| --- | --- |
| `mkdocs.yml` | Site configuration (Material theme, search, dark mode) |
| `hooks/gen_notes.py` | Generates homepage, day pages, transcript pages and the nav |
| `docs/` | Reserved for handwritten pages (currently empty) |
| `site/` | Build output (git-ignored) |

What you get:

- **Top tab bar** — Home · Beginner · Intermediate · Intermediate+ · Web Dev · Advanced — with collapsed day sections and short sidebar labels
- One page per **lecture note** (367 pages), grouped into 85 days
- One page per **raw transcript** (604 pages), marked with 🗣 in the sidebar
- Full-text **search across everything**, dark mode, copy-buttons on code blocks