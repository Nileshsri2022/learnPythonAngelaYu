Here is a structured breakdown of this lesson on hitting Like.

---

### 1. The Swipe Buttons

On the web app, swiping is done with buttons that carry ARIA labels:

```html
<button aria-label="Like">…</button>
<button aria-label="Nope">…</button>
```

```python
like_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Like']")
```

ARIA labels are more stable than class names — they exist for accessibility and rarely
change for cosmetic reasons.

---

### 2. The Loop

```python
import time

for _ in range(50):                    # stay well under the daily cap
    try:
        click_if_present(driver, By.CSS_SELECTOR, "button[aria-label='Like']", timeout=3)
    except Exception as error:
        print("Stopping:", error)
        break

    # a match pop-up replaces the card view — dismiss and continue
    click_if_present(driver, By.XPATH, "//button[text()='Back to Tinder']", timeout=2)
    click_if_present(driver, By.CSS_SELECTOR, "button[aria-label='Dismiss']", timeout=1)

    time.sleep(1)                      # be a polite bot
```

* Try/except keeps one weird state from killing the whole run (Day 30).
* A short `sleep` avoids hammering the site — and looks less robotic.
* Count your swipes so you know when you're approaching the ~100/day free limit.

---

### 3. What Can Go Wrong

| Symptom | Cause | Fix |
|---------|-------|-----|
| `ElementClickInterceptedException` | a match/promo pop-up appeared | dismiss first (`click_if_present`) |
| `NoSuchElementException` | out of swipes / "no more people nearby" | detect the message and stop gracefully |
| Nothing happens | rate limited | lower the pace, fewer swipes |
| Logged out mid-run | session expired | re-login step at the start |

---

### 4. Wrap It Up

```python
print(f"Swiped {count} profiles this session.")
driver.quit()
```

> **Tip:** Add `--user-data-dir=<profile>` so the login survives between runs — Tinder's
> session cookie then makes repeated logins unnecessary (and avoids captcha prompts).

---

### Summary Checklist

1. Click `button[aria-label='Like']` (or `'Nope'` to stay kind to real people).
2. Dismiss match pop-ups between swipes with the `click_if_present` helper.
3. Catch exceptions per swipe, count them, and pause ~1 s.
4. Stop cleanly when out of swipes or logged out; `quit()` the driver.
