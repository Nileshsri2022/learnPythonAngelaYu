# Step 2- Automated Login

---

### 1. Find the Login Fields

Open DevTools on the login page and note the hooks:

```html
<input id="email" name="email" type="email">
<input id="password" name="password" type="password">
<button type="submit">Log in</button>
```

---

### 2. Fill and Submit

```python
from selenium.webdriver.common.by import By

EMAIL = "student@test.com"
PASSWORD = "password123"

driver.get(f"{GYM_URL}/login")

driver.find_element(By.NAME, "email").send_keys(EMAIL)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
```

* `send_keys()` types; `.click()` submits.
* CSS attribute selectors (`button[type='submit']`) are handy when an element has no
  class or id.

---

### 3. Confirm the Login Worked

```python
WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
print("Logged in:", driver.current_url)
```

Checks worth making:

* URL changed away from `/login`.
* The nav bar shows *My Bookings* (only present when authenticated).
* No "invalid password" element on the page.

> **Tip:** Keep credentials in constants (or environment variables) at the top of the file —
> you'll re-login in every step of this project.

---

### 4. Wrap It in a Function

```python
def login(driver):
    """Log in and wait until the dashboard is on screen."""
    driver.get(f"{GYM_URL}/login")
    driver.find_element(By.NAME, "email").send_keys(EMAIL)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
```

Functions keep each step testable on its own (Day 10) and make the resilience wrapper in
Step 9 trivial to apply.

---

### Summary Checklist

1. Locate inputs by `name`/`id` using DevTools.
2. `send_keys()` the credentials, then click the submit button.
3. Wait for a URL/text change instead of sleeping.
4. Wrap login in a function so later steps can reuse it.
