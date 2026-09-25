Here is a structured breakdown of this lesson on the already-booked check.

---

### 1. Read Before You Click

A class card can say **"Book"** or **"Booked"/"Full"** — clicking "Booked" throws an
error. So inspect the card's text first:

```python
book_button = card.find_element(By.TAG_NAME, "button")
if book_button.text.strip().lower() == "book":
    book_button.click()
else:
    print("Already booked — skipping.")
```

* Idempotent bots are safe bots: re-running must not double-book or crash.
* Always `.strip()` button text — pages hide whitespace in markup.

---

### Summary Checklist

1. Check state, then act.
2. Handle the "already done" path explicitly.
