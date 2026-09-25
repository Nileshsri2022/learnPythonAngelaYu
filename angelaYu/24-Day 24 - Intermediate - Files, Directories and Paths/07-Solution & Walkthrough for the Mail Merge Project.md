# Solution & Walkthrough for the Mail Merge Project

---

### 1. The Solution

```python
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace("[name]", stripped_name)

        with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
```

---

### 2. Line by Line

1. `readlines()` — `["Angela\n", "Jack\n", …]` — every name keeps its newline.
2. `.strip()` — removes the `\n` so filenames and greetings are clean.
3. `letter_contents` is read **once** before the loop; each pass produces a fresh
   replaced copy (strings are immutable — `replace` returns a new string).
4. `"w"` mode creates each output file; the f-string names it after the guest.

> **Tip:** Notice the nesting — the loop lives *inside* the template's `with` block,
> but each output letter gets its own short-lived `with`.

---

### Summary Checklist

1. `readlines` + `strip` = clean list of names.
2. `replace` personalises; `"w"` persists.
3. Runnable version: [`mail_merge.py`](mail_merge.py) (+ sample input files)
