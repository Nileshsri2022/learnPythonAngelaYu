Here is a structured breakdown of this lesson on logging in.

---

### 1. Navigate and Submit the Form

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

LOGIN_URL = "https://www.instagram.com/"      # or the Share-a-Naan clone


def login(self):
    self.driver.get(LOGIN_URL)

    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located((By.NAME, "username"))
    ).send_keys(self.username)

    self.driver.find_element(By.NAME, "password").send_keys(self.password)
    self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
```

* Instagram's login form keeps the familiar `name="username"` / `name="password"` hooks.
* One `WebDriverWait` on the first field is enough — if it exists, so does the form.

---

### 2. The Post-Login Pop-up Storm

After a successful login Instagram (and many apps) show two modals:

* *"Save your login info?"* → usually **Not now**
* *"Turn on notifications?"* → usually **Not now**

```python
click_if_present(self.driver, By.XPATH, "//button[text()='Not now']")
click_if_present(self.driver, By.XPATH, "//button[text()='Not Now']")
```

Reuse the `click_if_present()` helper from Day 50 — the same defensive pattern appears
in every bot you build.

---

### 3. Confirm You're In

```python
WebDriverWait(self.driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "svg[aria-label='Home']"))
)
```

Or check the profile icon / a logged-in-only element. Also handle the failure path: if
Instagram shows *"Your account has been locked"*, stop rather than hammering login.

---

### 4. Persist the Session

```python
options.add_argument(f"--user-data-dir={PROFILE_DIR}")
```

With a persistent profile, `login()` will mostly be a no-op after the first run — and you
won't hit "suspicious login attempt" screens every time.

> **Tip:** Login detection is flaky on Instagram because the DOM is obfuscated. Prefer
> finding a **visible element that only exists when logged in**, not a specific class name.

---

### Summary Checklist

1. `name="username"` / `name="password"` + submit button.
2. Dismiss "Save login info?" and "Turn on notifications" with `click_if_present`.
3. Verify login by a logged-in-only element; watch for lock/challenge screens.
4. Persist the profile so login is a one-time event.
