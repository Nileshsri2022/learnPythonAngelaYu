Here is a structured breakdown of this lesson on counters and the run summary.

---

### 1. Count the Outcomes

```python
booked, skipped, failed = 0, 0, 0

for card in class_cards:
    ...
    if already_booked:
        skipped += 1
    elif clicked_ok:
        booked += 1
    else:
        failed += 1

print(f"Booked: {booked} | Already booked: {skipped} | Failed: {failed}")
```

* One glance at the console tells you if the run worked — vital when it runs while
  you're still asleep.
* A counter per outcome beats a wall of prints.

---

### Summary Checklist

1. Track booked / skipped / failed.
2. End every bot run with a one-line summary.
