Here is a structured breakdown of this lesson on adding counters for a neat summary.

---

### 1. Why Counters?

Unattended scripts need a report. A one-line summary at the end tells you at a glance
whether the bot did what you hoped — and gives you something to log or email.

```python
booked = 0
waitlisted = 0
skipped = 0
failed = 0
```

---

### 2. Increment Where the Action Happens

```python
if state == "available":
    click_book(card)
    booked += 1
elif state == "waitlist":
    click_book(card)
    waitlisted += 1
elif state == "booked":
    skipped += 1
else:
    failed += 1
```

Keep the counter bump on the line *after* the successful click — incrementing first hides
failures.

---

### 3. Print a Summary

```python
def print_summary(booked, waitlisted, skipped, failed) -> None:
    print("\n" + "=" * 34)
    print("  Snack & Lift booking summary")
    print("=" * 34)
    print(f"  Booked          : {booked}")
    print(f"  Joined waitlist : {waitlisted}")
    print(f"  Already booked  : {skipped}")
    print(f"  Failed          : {failed}")
    print("=" * 34)
```

```
==================================
  Snack & Lift booking summary
==================================
  Booked          : 2
  Joined waitlist : 1
  Already booked  : 0
  Failed          : 0
==================================
```

---

### 4. Counters as a Sanity Check

`booked + waitlisted + skipped + failed` should equal the number of classes the bot looked
at. If it doesn't, a branch is unaccounted for — usually a state you haven't handled yet.

> **Tip:** Collect the report in a dictionary instead of loose variables if you plan to
> `json.dump()` it or send it to yourself later (Day 30).

---

### Summary Checklist

1. One counter per outcome: booked / waitlisted / skipped / failed.
2. Increment only after the action succeeds.
3. Print a tidy summary — the scoreboard for an unattended run.
4. The counters should add up to the number of classes processed.
