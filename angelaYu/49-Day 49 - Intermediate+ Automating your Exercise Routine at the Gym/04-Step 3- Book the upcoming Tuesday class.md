Here is a structured breakdown of this lesson on booking the upcoming Tuesday class.

---

### 1. Compute the Target Date

```python
import datetime as dt

today = dt.datetime.now()
days_until_tuesday = (1 - today.weekday()) % 7 or 7   # 0=Mon … 6=Sun
next_tuesday = today + dt.timedelta(days=days_until_tuesday)
print(next_tuesday.strftime("%d/%m/%Y"))
```

* `weekday()` — Monday is 0. Arithmetic with `timedelta` (Day 35 pattern) lands on the
  next Tuesday.
* The schedule page labels each class card with its date — find the card that matches.

---

### Summary Checklist

1. Target date from `datetime`, not from your memory.
2. Find the matching class card, click **Book**.
