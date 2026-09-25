Here is a structured breakdown of this lesson on dismissing popups.

---

### 1. Clear the Popup Stack

After login, Tinder throws a parade of permission dialogs (notifications, location,
privacy notice). Dismiss them in a loop until none remain:

```python
for _ in range(5):
    try:
        dismiss = driver.find_element(By.XPATH,
            "//button[text()='I accept'] | //button[text()='Not now']")
        dismiss.click()
    except Exception:
        break        # no more popups
```

* Assume 3–5 dialogs; stop when the button can't be found.
* `try/except` as flow control: *absence of the popup* is the loop's exit condition.

---

### Summary Checklist

1. Loop → find dismiss button → click → repeat until gone.
2. A clean deck is required before swiping works.
