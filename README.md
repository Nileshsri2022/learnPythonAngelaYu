# learnPythonAngelaYu

Personal notes and transcripts for learning Python with **Angela Yu**, following
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

**Lecture notes** are proper structured study notes in the style of the
[learnAndroidDev](https://github.com/Nileshsri2022/learnAndroidDev) repo — one heading per
concept, syntax-highlighted **code blocks**, bullet-point explanations, tips and a
**Summary Checklist** at the end of every note. **Days 1–5 are fully rewritten** in this
style (more days are being converted progressively; later days still contain the older
transcript-style notes until their turn comes).

Each day folder also contains **runnable project code** (`.py`) for that day's final
project — e.g. `band_name_generator.py`, `rock_paper_scissors.py`, `password_generator.py`.

**Transcripts** (604 `.txt` files) remain under `angelaYu/transcripts/` as the verbatim
word-for-word reference text of each lecture.

## Topics covered

- **Beginner (Days 1–14):** Python basics, variables, data types, control flow, loops, functions, OOP fundamentals, debugging
- **Intermediate (Days 15–31):** Tkinter GUI, file I/O, CSV & Pandas, list comprehension, APIs, automation, capstone projects
- **Intermediate+ (Days 32–40):** API integration, web scraping with Beautiful Soup & Selenium, stock alerts, habit tracking, flight deal finder
- **Web Development (Days 41–58):** HTML, CSS, Bootstrap, Flask, Jinja templating, full-stack apps
- **Advanced (Days 59–81):** SQLAlchemy, REST APIs, authentication, Git/GitHub, deployment, data science with Pandas, NumPy, Matplotlib, Seaborn, Plotly, machine learning capstone
- **Professional (Days 82–83):** Portfolio projects — Python scripting, web development

## Documentation site

The transcripts are also available as a **searchable website**
(MkDocs Material, with full-text search and dark mode):

```bash
cd docs-site
pip install -r requirements.txt
mkdocs serve          # http://localhost:8000
```

Pages are generated in memory from `angelaYu/transcripts/` at build time — see
[`docs-site/README.md`](docs-site/README.md). A static bundle can be built with
`mkdocs build` (output in `docs-site/site/`, git-ignored) and published, e.g.
with `mkdocs gh-deploy`.