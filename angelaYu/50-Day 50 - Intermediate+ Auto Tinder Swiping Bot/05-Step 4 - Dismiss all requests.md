# Step 4 - Dismiss all requests

---

### 1. The Pop-up Gauntlet

A freshly logged-in Tinder account gets buried in modals:

* *"Allow Tinder to send notifications?"*
* *"Allow Tinder to know your location?"*
* *"Allow cookies?"*
* Add-to-home-screen prompts, upgrade nags, "verify your photo" cards…

The swipe buttons don't exist until these are gone. This is the single most fragile part
of the bot.

---

### 2. Dismiss Defensively

Never assume a pop-up exists — write helpers that handle *present* and *absent*:

```python
def click_if_present(driver, by, value, timeout=5):
    """Click the first match if it appears within `timeout`; else move on."""
    try:
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        ).click()
        return True
    except TimeoutException:
        return False

# notifications, location, cookies — order doesn't matter, presence does
click_if_present(driver, By.CSS_SELECTOR, "button[aria-label='Allow']")
click_if_present(driver, By.XPATH, "//button[text()='Not interested']")
click_if_present(driver, By.CSS_SELECTOR, "button[aria-label='Dismiss']")
```

* `try/except TimeoutException` is the idiomatic "optional element" pattern — the call
  succeeds or the timeout is swallowed.
* Loop over a **list** of candidates rather than copy-pasting:

```python
dismissals = [
    (By.XPATH, "//button[text()='Not interested']"),
    (By.XPATH, "//button[text()='I'll pass']"),
    (By.CSS_SELECTOR, "button[aria-label='Dismiss']"),
]
for by, value in dismissals:
    click_if_present(driver, by, value)
```

---

### 3. Handle the Location Prompt

For a real browser you can grant geolocation up front and skip the dialog entirely:

```python
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 1,   # allow
    "profile.default_content_setting_values.notifications": 1,  # allow
})
```

---

### 4. Verify the Page Is "Clear"

The swipe view shows a card with Like / Nope buttons. Only continue when they exist:

```python
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Like']"))
)
```

---

### Summary Checklist

1. Notifications, location, cookies and upsells all block the buttons you need.
2. Write `click_if_present()` once; use it for every optional modal.
3. Pre-configure geolocation/notification permissions to avoid two of them entirely.
4. Don't swipe until you've confirmed the Like button is actually clickable.
