# Working with AI as a Developer — practical notes (Day 85)

A checklist version of the habits the bonus lecture points at, written for the code you've
already built in this course.

---

## 1. Where AI genuinely helps

| Task | Good use | Watch out for |
|------|----------|---------------|
| Boilerplate | "write a Flask route that…" | it doesn't know your schema — check names |
| Debugging | paste the traceback, ask for likely causes | verify with the actual error, not vibes |
| Learning | "explain what `@login_required` does, with an example" | it can be confidently wrong |
| Refactoring | "make this function clearer, keep behaviour" | re-run your tests afterwards |
| Docs/tests | "write pytest cases for this function" | it tests what you *said*, not what you meant |
| Naming | "10 options for this variable/route" | taste is still yours |

---

## 2. Rules of engagement

1. **You own the output.** If you can't explain a line, delete it or learn it.
2. **Run everything.** Generated code compiles in the model's imagination only.
3. **Never paste secrets** — API keys, passwords, customer data. Use redacted examples.
4. **Small asks beat big asks.** "Fix this regex" works; "build my startup" doesn't.
5. **Ask for the reasoning**, not just the answer — that's how it teaches instead of
   automating you out of your own learning.
6. **Beware hallucinated libraries.** If a package name sounds plausible but unfamiliar,
   check PyPI before `pip install`.

---

## 3. A productive loop

```
1. I write the smallest version I can
2. AI reviews it and lists problems
3. I decide what's right, fix it myself
4. AI writes the boring parts (tests, docs, boilerplate)
5. I run the tests, deploy, and read the errors
6. I write one line in my log about what I learned
```

AI accelerates steps 2 and 4. Steps 1, 3 and 5 are where the skill lives — skip them and
you're just a very fast typist with no judgement.

---

## 4. Systems, not willpower

* **Focus block:** 25–50 minutes, one task, phone in another room (Day 84).
* **Next action:** end each session by writing the first line of the next one.
* **Daily commit:** something, however small, goes into Git.
* **Weekly review:** what shipped? what's stuck? what's the one thing for next week?
* **Automate twice-touched work:** if you do it manually a second time, script it — that's
  the whole spirit of Days 32–53.

---

## 5. Using AI to keep learning

* Ask it to quiz you on a topic ("ask me five questions about Flask sessions").
* Ask for a **counter-example** to your design ("what breaks if I store the answer in a
  constant?").
* Ask it to review your code as a senior engineer would, then argue with it.
* Ask for the *simplest* version of a concept, then progressively harder versions.

---

## 6. The bigger picture

Productivity isn't doing more — it's removing friction between you and the work that
matters. AI removes the mechanical friction: boilerplate, tab-completion, summaries,
first drafts of tests. The judgement — what to build, what good looks like, what to ship —
is still the job. That part compounds only through practice.
