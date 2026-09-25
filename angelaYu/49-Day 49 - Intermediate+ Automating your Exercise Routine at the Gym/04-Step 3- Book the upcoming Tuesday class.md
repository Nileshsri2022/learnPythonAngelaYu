# Step 3- Book the upcoming Tuesday class

---

### 1. Work Out Which Date "Next Tuesday" Is

```python
from datetime import datetime, timedelta

def next_weekday(weekday: int) -> datetime.date:
    """Return the date of the next occurrence of weekday (0=Mon … 6=Sun)."""
    today = datetime.now().date()
    days_ahead = (weekday - today.weekday()) % 7
    days_ahead = days_ahead or 7          # if today IS Tuesday, take next week
    return today + timedelta(days=days_ahead)
```

* `date.weekday()` returns 0 for Monday … 6 for Sunday, so Tuesday is `1`.
* `% 7` handles wrapping across the end of the week; `or 7` stops "today" matching itself.

---

### 2. Find That Class on the Schedule

The schedule lists classes by date — inspect one card to see its shape:

```html
<div class="class-card">
  <h3 data-date="2026-09-29">Spin · 18:00</h3>
  <button class="book">Book</button>
</div>
```

```python
target = next_weekday(1)               # Tuesday
cards = driver.find_elements(By.CSS_SELECTOR, "div.class-card")

for card in cards:
    if card.find_element(By.TAG_NAME, "h3").get_attribute("data-date") == str(target):
        card.find_element(By.CSS_SELECTOR, "button").click()
        break
```

> **Tip:** Prefer a `data-*` attribute (or the visible date text) over a hard-coded CSS
> selector — the schedule is generated from data, so dates move.

---

### 3. Handle the Button State

The same slot can show different buttons:

| Button | Meaning | Bot action |
|--------|---------|------------|
| **Book** | space available | click it |
| **Join waitlist** | class full | click it, count as waitlisted |
| **Booked** | you already have it | skip |

```python
button = card.find_element(By.CSS_SELECTOR, "button")
if button.text.strip().lower() == "book":
    button.click()
    print(f"Booked spin class on {target}")
```

---

### 4. Confirm the Booking

```python
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.toast"), "Booked")
)
```

The site shows a confirmation toast — waiting for it is the cheapest proof the click
actually worked.

---

### Summary Checklist

1. `datetime` + `timedelta` compute the next Tuesday instead of hard-coding a date.
2. Match the class card by its date attribute, then click its button.
3. Read the button label to tell Book / Waitlist / Booked apart.
4. Wait for the confirmation toast before moving on.
