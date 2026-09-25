# Introducing the NATO Alphabet Project

---

### 1. The Problem It Solves

Phone calls: *"Can you spell your name?"* — is that B, D, or P? The NATO phonetic alphabet
(Alfa, Bravo, Charlie…) exists precisely for this. The app spells any word you type into
NATO code words.

---

### 2. What You're Given

* `nato_phonetic_alphabet.csv` — `letter,code` rows (A→Alfa, B→Bravo, …, Z→Zulu).
* A blank `main.py`.

**Requirements:**

1. Read the CSV into a dictionary — `{letter: code}` — using **dictionary comprehension**
   over the DataFrame.
2. Ask for a word.
3. Output the code word for **each letter** using **list comprehension**.

Two comprehensions, two data conversions, one tiny program — every concept from today
exercised exactly once.

---

### Summary Checklist

1. CSV → DataFrame → dict comprehension → lookup table.
2. Word → list comprehension → list of code words.
3. Attempt it solo before the walkthrough.
