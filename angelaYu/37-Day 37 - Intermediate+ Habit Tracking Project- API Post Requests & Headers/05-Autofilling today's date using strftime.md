# Autofilling today's date using strftime

Every API wants dates in a different shape — `yyyyMMdd` here, day-first there, month
names elsewhere. **`strftime()`** formats a `datetime` into *any* of them.

---

### 1. Get Today's Date

```python
from datetime import datetime

today = datetime.now()
print(today)          # 2026-09-25 07:41:03.512 — not what Pixela wants
```

---

### 2. Format It

`strftime` takes a **format string** and returns text:

```python
today = datetime.now().strftime("%Y%m%d")
pixel_data = {"date": today, "quantity": "9.74"}
```

The codes you need most:

| Code | Gives | Example |
|------|-------|---------|
| `%Y` | Four-digit year | `2026` |
| `%m` | Month, zero-padded | `09` |
| `%d` | Day of month, zero-padded | `25` |
| `%a` / `%A` | Weekday, short / full | `Thu` / `Thursday` |
| `%b` / `%B` | Month name, short / full | `Sep` / `September` |

Anything that is not a `%` code is copied literally — dashes, spaces, even asterisks:

```python
datetime.now().strftime("%d/%m/%Y")      # 25/09/2026
datetime.now().strftime("%Y-%m-%d")      # 2026-09-25
```

---

### 3. Posting for Another Day

Build a date by hand instead of using `now()` — useful for backfilling:

```python
yesterday = datetime(year=2026, month=9, day=24).strftime("%Y%m%d")

pixel_data = {"date": yesterday, "quantity": "15.0"}   # cycled further yesterday
```

The second pixel is darker — the same quantity scale that makes the graph readable at
a glance.

---

### Summary Checklist

1. `from datetime import datetime`; `datetime.now()` gives the current moment.
2. `strftime("…")` converts a datetime into a custom **string** format.
3. `%Y%m%d` → `20260925`; other codes: `%m`, `%d`, `%a`, `%b`, `%B`.
4. Literal characters pass straight through — `%Y-%m-%d`, `%d/%m/%Y`.
5. `datetime(year, month, day)` lets you post pixels for past or future dates.
