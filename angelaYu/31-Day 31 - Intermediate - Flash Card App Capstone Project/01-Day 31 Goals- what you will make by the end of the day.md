# Day 31 Goals: what you will make by the end of the day

Capstone time. Day 31 combines everything from the last two weeks — files, CSV,
Pandas, JSON and Tkinter — into a **flash card study app**.

---

### 1. Why Flashcards Work: The Frequency Idea

Angela's story: years of French grammar tables never produced a conversation.
What finally worked was learning the **most frequent words first**, using a
*frequency dictionary* rather than an A–Z dictionary.

| Language (Chinese example) | Characters needed |
|---------------------------|-------------------|
| Eloquent professor | ~10,000 |
| Everyday adult | ~8,000 |
| Average teenager | ~3,000 |
| Simple movies and books | **~1,000** |

The first ~1,000 words of a language are its bread and butter — `the`, `of`, `from`,
`yes`, `no`. Rarer words (`glioblastoma`, `anti-establishment`) can wait. Ten new
words a day ≈ 1,000 words in under a year.

---

### 2. The App

A Tkinter window shows a card with a **French word on the front**. After three
seconds the card **flips** to reveal the English translation.

| Button | Meaning | Effect |
|--------|---------|--------|
| ✔ | "I knew it" | Card is **removed** from the deck — stop studying what you know |
| ✘ | "I didn't know it" | Card is **kept** and shown again later |

Only the words you don't yet know come back — that is the whole learning trick.

---

### 3. Where the Word List Comes From

1. A **frequency list** of the language (Hermit Dave's GitHub repo, `fr` = French,
   compiled from movie subtitles) gives the most common words in order.
2. Paste the top words into a spreadsheet.
3. Google Sheets' `=GOOGLETRANSLATE(text, "fr", "en")` fills in the translations.
4. Export as **CSV** → `french_words.csv` in the starter project, with `French` and
   `English` columns.

The second file you will create yourself is `words_to_learn.csv`: the words you got
wrong, so your progress survives closing the app.

---

### Summary Checklist

1. Learn the ~1,000 most **frequent** words first; ignore the rare ones.
2. Flash card = front (French) → after 3 s → back (English flip).
3. ✔ deletes the card from the deck; ✘ keeps it for another round.
4. Data comes from a frequency list → `GOOGLETRANSLATE` → CSV export.
5. `words_to_learn.csv` stores your progress between sessions.
6. Skills used: Tkinter UI, `csv`/Pandas, `try`/`except`, file paths.
