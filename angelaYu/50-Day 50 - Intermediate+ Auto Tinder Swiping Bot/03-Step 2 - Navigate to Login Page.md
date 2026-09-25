Here is a structured breakdown of this lesson on navigating to the login page.

---

### 1. The Landing Page Has a Login Entry Point

Tinder's landing page has a **Log in** button that leads to the auth flow:

```python
driver.get(TINDER_URL)

# Tinder exposes a data-testid on its "Log in" button
login_button = driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
login_button.click()
```

If the anchor has no useful hook, use link text or add a wait:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))
).click()
```

---

### 2. Expect a Pop-up (Sometimes)

Modern sites greet first-time visitors with cookie/consent modals, and these **can cover
the button you want to click**. Selenium will raise

```
ElementClickInterceptedException: element click intercepted
```

when something invisible to you sits on top of the element.

Handle it defensively:

```python
def dismiss_if_present(driver, by, value):
    """Click an optional pop-up button; do nothing if it isn't there."""
    elements = driver.find_elements(by, value)      # plural: returns [] if absent
    if elements:
        elements[0].click()
```

* `find_elements` returning an empty list is far safer than `try/except` around
  `find_element`.
* Call it before each real interaction: dismiss cookies, then click login.

---

### 3. Wait for the Login Page

```python
WebDriverWait(driver, 10).until(EC.url_contains("/login"))
print("On the login page:", driver.current_url)
```

---

### Summary Checklist

1. `driver.get()` the app, then click the *Log in* entry point.
2. Use `WebDriverWait(...).until(EC.element_to_be_clickable(…))` — buttons often need a
   moment to become clickable.
3. Optional pop-ups break clicks — dismiss them with `find_elements` + `if elements`.
4. Assert you arrived: `EC.url_contains("/login")`.
