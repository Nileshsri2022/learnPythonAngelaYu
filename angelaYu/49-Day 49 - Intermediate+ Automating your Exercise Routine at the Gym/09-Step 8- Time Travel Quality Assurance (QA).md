Here is a structured breakdown of this lesson on quality assurance with the time simulator.

---

### 1. The Bug Class You Can't See Today

"Book the next Tuesday" logic is easy to get wrong in ways that only show up on particular
days — *is today Tuesday? Near midnight? Across a month boundary?* Waiting a week to find
out is not testing.

---

### 2. The Time Simulator

The gym test app has a **time simulation** toggle that lets you pretend it is a different
day. Use it to re-run your bot as if:

* today is Monday → Tuesday's class is tomorrow;
* today **is** Tuesday → the bot must pick *next* week, not today;
* today is the 31st → month rollover still works.

---

### 3. QA Checklist

| Scenario | What to verify |
|----------|----------------|
| Today is Monday | Books tomorrow's (Tuesday) class |
| Today is Tuesday | Books *next* Tuesday, doesn't try today's finished class |
| Today is Thursday evening | Thursday booking skipped or waitlisted sensibly |
| Week / month boundary | Dates formatted correctly, no `IndexError`, no wrong week |
| Time simulation off | Normal run still works |

```python
# in code: make the "today" you test with explicit, so it can be simulated
TODAY_OVERRIDE = None      # e.g. datetime.date(2026, 9, 29) while testing

def today() -> datetime.date:
    return TODAY_OVERRIDE or datetime.now().date()
```

> **Tip:** Injecting "today" as a function is the tiny bit of design that makes time
> travel possible without touching the rest of the script.

---

### 4. Reset Between Runs

* Admin panel → **Clear Bookings only** (or **Reset All Data** for a full factory reset).
* Clear the counters by just running the script fresh.
* Confirm the stats at the top of the admin page show the state you expect.

Every QA run should begin from a known state, or the results mean nothing.

---

### 5. Record the Results

Keep a short table in your notes: scenario → expected → actual → pass/fail. When the bot
grows (Step 9's retries), re-run the table; it is your regression suite.

---

### Summary Checklist

1. Time simulation lets you test date logic today instead of next Tuesday.
2. Check the nasty cases: today is the target weekday, month/week boundaries.
3. Inject "today" through a function so tests can override it.
4. Reset the database before each scenario; log expected vs actual.
