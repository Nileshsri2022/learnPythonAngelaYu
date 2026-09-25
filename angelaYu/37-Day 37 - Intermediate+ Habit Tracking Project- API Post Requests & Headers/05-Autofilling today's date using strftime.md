Here is a structured breakdown of this lesson on strftime.

---

### 1. Auto-Date the Pixel

No more typing dates — `datetime` formats itself:

```python
from datetime import datetime

today = datetime.now()
TODAY = today.strftime("%Y%m%d")     # "20260925"

pixel_data = {
    "date": TODAY,
    "quantity": input("How many hours did you code today? "),
}
```

---

### 2. strftime Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | 2026 |
| `%m` | zero-padded month | 09 |
| `%d` | zero-padded day | 25 |
| `%H:%M:%S` | time | 14:07:33 |
| `%A` | weekday name | Friday |

`strftime` = *string from time*; the format string is the template.

---

### Summary Checklist

1. `datetime.now().strftime("%Y%m%d")` — the daily-script essential.
2. Any date shape you need is a format string away.
