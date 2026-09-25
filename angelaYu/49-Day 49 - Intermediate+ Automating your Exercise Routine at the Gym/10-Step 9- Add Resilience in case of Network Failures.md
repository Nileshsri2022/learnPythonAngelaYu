Here is a structured breakdown of this lesson on network-failure resilience.

---

### 1. Wrap the Risky Parts

The bot runs unattended; a dropped connection must not leave a half-booked mess:

```python
import time

for attempt in range(3):
    try:
        book_class_on(target)
        break
    except Exception as error:
        print(f"Attempt {attempt + 1} failed: {error}")
        time.sleep(5)
else:
    failed += 1
    print("All retries failed.")
```

* Retry with a pause rides out transient Wi-Fi blips.
* `try/except` around the booking click keeps one failure from aborting the other
  weekdays.
* The final summary (Step 5) reports anything still broken.

---

### Summary Checklist

1. Retries + per-class error handling = an unattended-safe bot.
2. Runnable version: [`main.py`](main.py)
