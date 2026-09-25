Here is a structured breakdown of this lesson on time-travel QA.

---

### 1. Testing a Date-Dependent Bot

The bot only books *next Tuesday* — how do you test it without waiting a week?
**Time travel**: temporarily fake "today" so the date logic is exercised today:

```python
today = dt.datetime(2020, 3, 6)   # a Friday, for testing
```

or better — inject it:

```python
def get_today(fake=None):
    return fake or dt.datetime.now()
```

* Run once with the fake date; confirm it books the right upcoming Tuesday/Thursday.
* Then remove the fake and let the real clock drive.

> **Tip:** never QA a booking bot against the real class slot — book yourself a test
> class or you'll be doing spin at 6 AM.

---

### Summary Checklist

1. Make "today" injectable; test the date maths with a fixed date.
2. Verify the bot picks the right cards before going live.
