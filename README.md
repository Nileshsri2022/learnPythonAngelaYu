# learnPythonAngelaYu

Personal study notes and transcripts for learning Python with **Angela Yu**, following
[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)
(Beginner → Advanced).

## Repository structure

```
angelaYu/
├── Day 1 … Day 85/          # Per-day lecture notes (.md) derived from transcripts
│   ├── 01-Day 1 - Beginner - Working with Variables in Python to Manage Data
│   ├── 02-Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings
│   ├── …
│   ├── 81-Day 81 - Advanced - Capstone Project - Predict House Prices
│   ├── 82-Day 82 - Professional Portfolio Project - [Python Scripting]
│   ├── 83-Day 83 - Professional Portfolio Project - [Python Web Development]
│   ├── 84-Final Stretch
│   └── 85-Bonus Lecture- Succeed in the Age of AI
└── transcripts/              # Full course transcripts, one folder per day
    ├── 01-Day 1 … 85-Bonus Lecture/
    └── _full-transcript.txt  # Complete concatenated transcript
```

**Lecture notes** are structured study notes — one heading per concept, syntax-highlighted
code blocks, bullet-point explanations, tips, and a **Summary Checklist** at the end of
every note.

* **473 lecture notes** across **66 days** (plus 6 reference pages such as
  [`git_cheatsheet.md`](angelaYu/70-Day%2070%20-%20Advanced%20-%20Git%2C%20Github%20and%20Version%20Control/git_cheatsheet.md)
  and [`DEPLOY.md`](angelaYu/71-Day%2071%20-%20Advanced%20-%20Deploying%20Your%20Web%20Application/DEPLOY.md))
* **367 lecture transcripts** (plus 237 placeholder files for lectures that were never
  transcribed) — the verbatim word-for-word reference text, kept under
  `angelaYu/transcripts/`
* **Every lecture with a real transcript has a note.** 106 notes were written without
  source text (their lecture was never transcribed), and 138+ lectures have neither —
  all of this is reported honestly by `check_notes.py` and explained in
  [`docs-site/QUALITY.md`](docs-site/QUALITY.md).

Each day folder also contains **runnable project code** (`.py`, `.html`, `.css`) for that
day's final project — e.g. `band_name_generator.py`, `rock_paper_scissors.py`,
`password_generator.py` (72 project files in total).

## Documentation site

The notes and transcripts are also available as a **searchable website**
(MkDocs Material):

```bash
cd docs-site
pip install -r requirements.txt
mkdocs serve          # http://localhost:8000
```

What it adds on top of the raw markdown:

- **Lecture cards** — every note links to its raw transcript, its neighbours and its
  GitHub source file, with a reading-time estimate
- **Study plan** — a pace you can keep, plus every day with its reading time and projects
- **Cheat sheets** — every note's Summary Checklist collected per track, print-friendly
- **Topic index** — an A–Z index of ~1,200 section headings
- **Progress tracking** — tick days off; the home page counts them (stored in your
  browser only)
- **Honest coverage** — lectures without notes are shown as "not written yet"; transcript
  pages that are only placeholders are marked ⚠️, never passed off as real

Pages are generated in memory from `angelaYu/` at build time — see
[`docs-site/README.md`](docs-site/README.md). A static bundle can be built with
`mkdocs build --strict` (output in `docs-site/site/`, git-ignored) and is published to
**https://nileshsri2022.github.io/learnPythonAngelaYu/** on every push to `main`.

## Note quality

```bash
cd docs-site
python3 tools/normalize_notes.py --check    # structural drift (CI gate)
python3 check_notes.py --report             # structure, fidelity vs transcripts, coverage
python3 check_links.py                      # built site: links, thin pages
```

All three run in CI (`.github/workflows/docs-quality.yml`, plus the deploy workflow) and
must pass before the site is published. [`docs-site/QUALITY.md`](docs-site/QUALITY.md)
records the audit: what was normalised across all notes, the 22 transcript-dump notes
that were rewritten against the source, the duplicated Day 35/37/39/40 folders that were
merged (restoring 14 invisible notes), the content that was removed for not appearing in
any transcript, and the coverage numbers above.

## Topics covered

- **Beginner (Days 1–14):** Python basics, variables, data types, control flow, loops, functions, OOP fundamentals, debugging
- **Intermediate (Days 15–31):** Tkinter GUI, file I/O, CSV & Pandas, list comprehension, APIs, automation, capstone projects
- **Intermediate+ (Days 32–40):** API integration, web scraping with Beautiful Soup & Selenium, stock alerts, habit tracking, flight deal finder
- **Web Development (Days 41–58):** HTML, CSS, Bootstrap, Flask, Jinja templating, full-stack apps
- **Advanced (Days 59–81):** SQLAlchemy, REST APIs, authentication, Git/GitHub, deployment, data science with Pandas, NumPy, Matplotlib, Seaborn, Plotly, machine learning capstone
- **Professional (Days 82–83):** Portfolio projects — Python scripting, web development
