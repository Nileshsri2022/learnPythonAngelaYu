Here is a structured breakdown of this lesson on interacting with elements — clicking and typing.

---

### 1. Clicking an Element

Any element you've located can be clicked:

```python
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
article_count.click()
```

The browser navigates exactly as if a human had clicked — no mouse involved.

---

### 2. Finding Links by Their Text

Because clicking links is so common, Selenium has a dedicated locator:

```python
all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
all_portals.click()
```

`By.LINK_TEXT` matches the text **between** `<a>` and `</a>`;
`By.PARTIAL_LINK_TEXT` matches just a fragment.

---

### 3. Typing with `send_keys()`

```python
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
```

`send_keys()` sends keystrokes to the focused element — perfect for forms and search bars.

---

### 4. Pressing Special Keys

Letters and numbers can be typed directly; keys like Enter, Tab or Shift need the `Keys`
class:

```python
from selenium.webdriver.common.keys import Keys

search.send_keys("Python")
search.send_keys(Keys.ENTER)
```

> **Tip:** `Keys` is a class of constants (Day 16: constants live on the class, not an
> instance) — `Keys.ENTER`, `Keys.TAB`, `Keys.SHIFT`, `Keys.BACKSPACE`…

---

### 5. Challenge: Fill In and Submit a Form

Given a sign-up page with `<input name="fname">`, `<input name="lname">`,
`<input name="email">` and one `<button>` inside a `<form>`:

```python
driver.get(SIGNUP_URL)

driver.find_element(By.NAME, "fname").send_keys("Ada")
driver.find_element(By.NAME, "lname").send_keys("Lovelace")
driver.find_element(By.NAME, "email").send_keys("ada@example.com")

# the only <button> inside the <form> — no id or name exists
driver.find_element(By.CSS_SELECTOR, "form button").click()
```

The script runs in order: load → type → type → type → click → success page.

> **⚠️ Warning:** Practise on test pages, not on real sites. Automated sign-ups create
> junk traffic and can get your IP blocked. Course pages built for practice are the right
> playground.

---

### 6. The Pattern Behind Every Automation

1. `get()` a URL.
2. `find_element()` the field or button.
3. Act: `.click()`, `.send_keys()`, `.send_keys(Keys.X)`.
4. Repeat for the next step in the flow.

---

### Summary Checklist

1. `.click()` activates links and buttons you've located.
2. `By.LINK_TEXT` / `By.PARTIAL_LINK_TEXT` find anchors by their visible words.
3. `.send_keys("text")` types; `Keys.ENTER` presses special keys.
4. Forms are usually best targeted by `name` attributes; lone buttons by CSS selector.
5. Chain the steps in order to automate a whole flow.
