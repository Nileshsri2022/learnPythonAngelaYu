Here is a structured breakdown of this lesson on checking whether a class is already booked.

---

### 1. Why Check Before Clicking?

Running the script twice shouldn't cancel, double-book or error — an automation that
isn't *idempotent* is a liability. Before clicking anything, ask the page: **is this
already booked?**

---

### 2. Read the Button State

```python
def booking_state(card) -> str:
    """Return 'booked', 'waitlist', or 'available' for a class card."""
    button = card.find_element(By.CSS_SELECTOR, "button")
    label = button.text.strip().lower()

    if "booked" in label:
        return "booked"
    if "waitlist" in label:
        return "waitlist"
    return "available"
```

Use substring checks (`"booked" in label`) rather than equality — labels often carry extra
spacing, capitals or icons.

---

### 3. Skip What You Already Have

```python
state = booking_state(card)

if state == "available":
    card.find_element(By.CSS_SELECTOR, "button").click()
    booked += 1
elif state == "waitlist":
    print("Class full — joining the waitlist")
    card.find_element(By.CSS_SELECTOR, "button").click()
    waitlisted += 1
else:
    print("Already booked — skipping")
    skipped += 1
```

---

### 4. Attributes Beat Text When Available

Text is for humans; attributes are for bots. If the button carries a class or attribute
such as `class="book-btn booked"` or `disabled`, prefer it:

```python
css_class = button.get_attribute("class")
if "booked" in css_class:
    ...
```

> **Note:** `button.text` returns `""` for elements hidden behind CSS — another reason to
> reach for attributes when a button might be invisible.

---

### 5. Log Everything

Print one line per class with the date, the action taken and why. When something goes
wrong at 11 p.m., the log is the only witness.

---

### Summary Checklist

1. Check the current state before clicking — makes reruns safe.
2. Read button text with substring matching, or use a class/attribute if one exists.
3. Branch into book / waitlist / skip and count each outcome.
4. Log every decision with its reason.
