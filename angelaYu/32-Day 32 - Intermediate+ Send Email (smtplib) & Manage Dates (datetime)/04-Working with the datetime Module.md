Here is a structured breakdown of this lesson on the datetime module.

---

### 1. The Objects

```python
import datetime

now = datetime.datetime.now()          # full timestamp
print(now.year, now.month, now.day)
print(now.day_of_week if hasattr(now, "day_of_week") else now.weekday())  # 0=Monday

date_of_birth = datetime.datetime(year=1995, month=12, day=15)
```

* `datetime.now()` — the current moment as a `datetime` object.
* `.year/.month/.day/.hour/...` — attribute access.
* `weekday()` — Monday=0 … Sunday=6.

---

### 2. The Classic Use — Death-Second Calculator

```python
import datetime

DOB = datetime.datetime(year=1995, month=12, day=15)
now = datetime.datetime.now()
difference = now - DOB                 # a timedelta!
print(difference.days)                 # days alive
seconds_alive = difference.total_seconds()
print(f"You have lived for {seconds_alive:,} seconds")
```

Subtracting datetimes yields a **timedelta** — days, seconds and totals between moments.

---

### Summary Checklist

1. `datetime.now()` and constructor by parts.
2. `weekday()` for day-of-week logic (0 = Monday).
3. Datetime − datetime = `timedelta` with `.days` / `.total_seconds()`.
