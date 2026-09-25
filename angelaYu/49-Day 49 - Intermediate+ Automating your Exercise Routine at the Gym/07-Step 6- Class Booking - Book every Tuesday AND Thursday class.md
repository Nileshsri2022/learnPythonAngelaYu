Here is a structured breakdown of this lesson on booking both weekly classes.

---

### 1. Two Target Days

```python
TARGET_WEEKDAYS = {1, 3}      # Monday=0 → Tuesday=1, Thursday=3

for day in sorted(TARGET_WEEKDAYS):
    delta = (day - today.weekday()) % 7 or 7
    target = today + dt.timedelta(days=delta)
    book_class_on(target)
```

* Same booking function, called once per weekday — data-driven, not copy-pasted.
* The booking function returns an outcome the counters tally.

---

### Summary Checklist

1. Loop over target weekdays; one function does the work.
2. Adding Friday is a one-character change.
