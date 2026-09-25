# Step 6- Class Booking - Book every Tuesday AND Thursday class

---

### 1. From One Class to a Week of Classes

Booking a single class proved the mechanics. Real value comes from booking **every**
qualifying class: all Tuesdays *and* Thursdays in the schedule.

---

### 2. Pick the Target Weekdays

```python
TARGET_WEEKDAYS = {
    1: "Tuesday",
    3: "Thursday",
}
```

A dictionary (Day 9) keeps the weekday number and its human label together.

---

### 3. Generate the Dates

```python
from datetime import datetime, timedelta

def upcoming_dates(weekdays, weeks=4):
    """Yield the next `weeks` occurrences of every weekday in `weekdays`."""
    today = datetime.now().date()
    for offset in range(weeks * 7):
        day = today + timedelta(days=offset)
        if day.weekday() in weekdays and day != today:
            yield day
```

* `weekday()` maps the date to 0–6.
* A generator (Day 26 style) streams dates as you need them.

---

### 4. Loop: Dates × Class Cards

```python
for target in upcoming_dates(TARGET_WEEKDAYS):
    cards = driver.find_elements(By.CSS_SELECTOR, "div.class-card")
    for card in cards:
        if card_date(card) != str(target):
            continue

        state = booking_state(card)
        if state == "available":
            click_book(card)
            booked += 1
            print(f"Booked {TARGET_WEEKDAYS[target.weekday()]} {target}")
        elif state == "waitlist":
            join_waitlist(card)
            waitlisted += 1
        else:
            skipped += 1
```

> **Tip:** Re-query `find_elements` inside the loop — after a booking the page re-renders,
> and stale element references raise `StaleElementReferenceException`.

---

### 5. Refactor While You Grow

By this step the script has real structure:

```text
login(driver)
for each target date:
    for each matching card:
        decide → click → count
print_summary(...)
```

Each helper does one job, so a change to "how we detect a full class" is a one-line edit.

---

### Summary Checklist

1. Tuesday `1` and Thursday `3` from `date.weekday()`.
2. Generate upcoming dates with `timedelta`, not hard-coded strings.
3. Re-fetch cards each iteration to avoid stale element references.
4. Reuse the state check + counters from Steps 4–5; the loop is the only new part.
