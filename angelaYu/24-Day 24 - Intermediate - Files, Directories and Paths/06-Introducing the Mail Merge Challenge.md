# Introducing the Mail Merge Challenge

---

### 1. The Task

Classic mail merge — produce one personalised letter per guest:

* **Input 1:** `./Input/Names/invited_names.txt` — one name per line.
* **Input 2:** `./Input/Letters/starting_letter.txt` — contains the placeholder
  `[name]`.
* **Output:** `./Output/ReadyToSend/` — one finished letter per guest, named after them.

```text
Dear [name],

You are invited to my Birthday Party on Saturday 24th March...
```

---

### 2. The Tools You'll Need

* `readlines()` — file → list of lines (names).
* `strip()` — remove the trailing `\n` from each line.
* `replace("[name]", name)` — string substitution for the placeholder.
* `"w"` mode — write each finished letter to its own file.

All four are standard string/file methods — this challenge is about *combining* them
into a small automation pipeline.

---

### Summary Checklist

1. Read names → loop → personalise template → write one file per person.
2. No new syntax — pure application of Day 24's file skills.
