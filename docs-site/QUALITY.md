# Note quality: what was checked, what was fixed, what is left

The notes were written over many sessions and had drifted. This document records the
audit, the fixes that were applied, and the work that remains — so the next pass starts
from facts instead of guesses.

Re-run everything with:

```bash
cd docs-site
python3 tools/normalize_notes.py --check     # structure
python3 check_notes.py --report              # structure + fidelity + coverage
mkdocs build --strict && python3 check_links.py
```

---

## 1. Structural drift — fixed

`tools/normalize_notes.py` normalises every note mechanically (and `--check` fails CI if
a note drifts again):

| Problem | Notes affected | Fix |
| --- | --- | --- |
| No `# Title` — the page opened with a machine-sounding *"Here is a structured breakdown of …"* sentence | 466 | H1 added from the existing heading or the file name; the filler sentence removed |
| HTML entities left over from an escaping pass (`&#x27;`, `&amp;`) | 26 | decoded (`html.unescape`) |
| `### Next Steps` repeating `### Summary` verbatim | 18 | duplicate section removed |
| `### Overview` block repeating Course/Chapter/Lecture/Level | 22 | removed — the site now renders that as a lecture card |
| `### Key Concepts` tables whose every row said *"Introduced/used in this lecture"* | 20 | removed (rows were auto-generated filler, sometimes mislabelled) |
| Unlabelled code fences (output, tracebacks, diagrams highlighted as Python) | 84 | labelled `python` when the block parses, otherwise `text` |
| Fenced code leaked into the rendered page because a closing fence was treated as an opening one | 4 notes | fixed in the site builder's fence pass (this had also produced 9 broken links) |
| Trailing whitespace / triple blank lines | all | tidied |

## 2. Duplicated days — fixed

Days **35, 37, 39 and 40** existed twice under differently punctuated folder names
(`… Variables - Send SMS` vs `… Variables- Send SMS`), so the site generator only saw
one copy of each:

| Day | Notes visible before | Notes after merging |
| --- | --- | --- |
| 35 | 7 | 9 |
| 37 | 6 | 6 |
| 39 | 1 | 7 |
| 40 | 1 | 6 |

`tools/merge_duplicate_days.py` merged each pair into the folder that matches the
transcripts folder name, kept the longer version where a lecture existed twice, and
deleted the emptied folder. The site gained 14 previously invisible lecture pages.

## 3. Rewritten notes (Days 23–40 legacy shape) — replaced

22 notes were verbatim transcript dumps: a `### Summary` field holding raw spoken text,
the same text repeated under `### Next Steps`, and a boilerplate "Key Concepts" table.
All 22 were rewritten, checked line by line against the transcript, into the normal note
shape (short sections, real code, practice notes, summary checklist):

Day 23 goals · Day 24 goals · Day 31 goals · Day 33 goals · Day 34 goals ·
Day 35 goals, *What is API Authentication…*, *Using API Keys…*, *Challenge: rain in 12
hours*, *Sending SMS via the Twilio API*, *PythonAnywhere*, *Environment variables* ·
Day 36 goals · Day 37 goals, *HTTP Post Requests*, *Advanced Authentication using an
HTTP Header*, *Add a Pixel…*, *strftime*, *Put and Delete* · Day 38 goals ·
Day 39 goals · Day 40 goals.

## 4. Invented content — removed

Manual verification against the transcripts found notes that taught material the lecture
never contained. Example: *Day 10 — Multiple return values* included a `days_in_month()`
/ `is_leap()` exercise that appears in **no** transcript of the course; the note now
covers only what the lecture does (multiple `return`s, early return, empty return,
meaningful messages).

`check_notes.py` now flags notes whose code literals never appear in the matching
transcript (**53 candidates** today). Most are legitimate — the notes contain the
**solution** code that the video types on screen but never reads out — so these are
warnings to review, not failures. Placeholder transcripts are excluded from this check,
so the warning list stays meaningful.

## 5. Coverage — the honest to-do list

The first version of this audit reported "≈130 lectures with a transcript but no note".
That was wrong: it counted *placeholder* transcript files. The repository holds **606
lecture transcript files, 237 of which only say "[No transcript available for this lecture]"** (the repository also holds a
full-course dump and a stray `hello.txt`, both ignored by the site).
Counting only real text changes the picture completely:

| | Lectures |
| --- | --- |
| Real transcript **and** a note (checked in `check_notes.py`) | **367** |
| Real transcript, no note yet | **0** |
| Note written **without** source text (no transcript exists) — unverifiable | 99 |
| Note with no transcript file at all | 7 |
| Neither transcript nor note (the video was never transcribed) | 138 |

So there is **no lecture with a real transcript that lacks notes**. The remaining work is
different in kind:

1. **99 + 7 = 106 notes have no source text** to check against. They are marked in
   `check_notes.py` (the `UNSOURCED NOTES` line). Spot-check them by hand if you rely on
   them, or treat them as "best effort" until a transcript appears.
2. **138 lectures were never transcribed** (mostly the Advanced block, Days 59–82). For
   those, the day page lists the lecture with no transcript link and marks it
   *"not written yet"*; the video is the only source.
3. The site now marks placeholder transcripts with ⚠️ so nobody mistakes them for real
   source material.

## 6. How to add a note (keeps the checks green)

1. Create `angelaYu/<NN-Day …>/NN-Title.md` (number + title matching the transcript).
2. Open with `# Title`, then `---`, then numbered `###` sections.
3. Label every code fence (`python`, `text`, `bash`, `html`, …).
4. End with `### Summary Checklist` (3–6 items — it is what the cheat sheets collect).
5. Run `python3 tools/normalize_notes.py --apply && python3 check_notes.py`.
