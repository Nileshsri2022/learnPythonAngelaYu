Here is a structured breakdown of everything covered in this lesson on Python constants and global scope.

---

### 1. Global Constants — the Good Globals

A **constant** is a value defined once and never changed — pi, the alphabet, difficulty
settings. Global scope is *perfect* for them:

```python
PI = 3.14159
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
```

By convention Python constants are named in **ALL_CAPS** — a signal to every reader:
*don't touch this*.

---

### 2. Why They're Safe

* Nothing ever *writes* to them, so they can't cause the mutation bugs of the last lesson.
* They centralise configuration — change `HARD_LEVEL_TURNS` in one place, the whole game
  updates.

Typical layout: constants at the **top of the file**, functions below them using them as
read-only inputs.

---

### Summary Checklist

1. Constants: `ALL_CAPS`, defined at global scope, never reassigned.
2. Read-only globals are safe and genuinely useful.
3. Mutable globals are the problem — constants are the solution.
