Here is a structured breakdown of this lesson on adding resilience for network failures.

---

### 1. Networks Fail — Bot Code Shouldn't

Enable the gym app's **network simulation** and some requests will fail mid-flow. Without
handling, the whole run dies on one flaky click. The fix is **retry logic**, written once
and reused everywhere.

---

### 2. Retry with a Decorator

A decorator wraps a function with extra behaviour (Day 54's decorator lessons, applied):

```python
import time
from functools import wraps

def retry(times: int = 3, delay: float = 1.0):
    """Retry the decorated function on failure, up to `times` attempts."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:          # StaleElement, Timeout, ...
                    last_error = error
                    print(f"⚠️ {func.__name__} failed (attempt {attempt}/{times}): {error}")
                    time.sleep(delay * attempt)     # simple backoff
            raise last_error
        return wrapper
    return decorator
```

* `*args, **kwargs` make the wrapper work with *any* function.
* `@wraps` preserves the original function's name and docstring.
* The delay grows with each attempt — a crude but effective **exponential backoff**.

---

### 3. Apply It Where Things Break

```python
@retry(times=3, delay=1)
def book_class(driver, target_date):
    cards = driver.find_elements(By.CSS_SELECTOR, "div.class-card")
    ...                      # find card, click the right button
```

Decorating `book_class`, `login` and `open_my_bookings` covers most failure points without
cluttering the logic.

---

### 4. Retry the Whole Booking Pass Too

A single class failing shouldn't abandon the other days:

```python
for target in upcoming_dates(TARGET_WEEKDAYS):
    try:
        book_class(driver, target)
    except Exception as error:
        failed += 1
        print(f"❌ Giving up on {target}: {error}")
```

> **Tip:** Retry *inside* the function for transient blips; catch *outside* the loop so one
> hard failure can't stop the rest of the batch (the Day 30 exception patterns).

---

### 5. Test It Properly

1. Turn **network simulation ON**.
2. Run the bot; watch the retry messages in the log.
3. Confirm the verified booking count still equals the expected count.
4. Turn simulation OFF and confirm a clean run is unaffected.

---

### Summary Checklist

1. Decorator + `try/except` + loop = retry logic in ~15 lines.
2. `*args`/`**kwargs` in the wrapper keep it universal; `@wraps` keeps names intact.
3. Back off between attempts instead of hammering the server.
4. Catch per-item so one failure doesn't kill the batch.
5. Prove it with network simulation on, then re-check with it off.
