# Step 3 - Login with Facebook

---

### 1. The "Log in with Facebook" Button

Third-party login means a **second window or tab** — Selenium must hand control back and
forth between them:

```python
# the popup opens in a NEW window handle
driver.find_element(By.CSS_SELECTOR, "button[aria-label='Log in with Facebook']").click()

# grab every window; the new one is the last
windows = driver.window_handles
driver.switch_to.window(windows[1])

driver.find_element(By.ID, "email").send_keys(FB_EMAIL)
driver.find_element(By.ID, "pass").send_keys(FB_PASSWORD)
driver.find_element(By.NAME, "login").click()

# hand control back to the Tinder window
driver.switch_to.window(windows[0])
```

| Call | Purpose |
|------|---------|
| `driver.window_handles` | list of all open windows/tabs |
| `driver.switch_to.window(handle)` | focus one of them |
| `driver.current_window_handle` | the window you're controlling now |

---

### 2. Wait for Facebook to Redirect Back

```python
WebDriverWait(driver, 20).until(EC.url_contains("tinder.com"))
```

Login redirects are slow and can involve several hops — give them a generous timeout.

---

### 3. Real Life Intervenes

* **Captcha / "Are you a robot?"** — you cannot and should not automate it. Log in
  manually once and keep the profile.
* **2FA** — same story.
* **Cookie banners** on the Facebook side — dismiss them with the
  `dismiss_if_present()` helper from Step 2.

> **Tip:** Put credentials in environment variables (Day 35) rather than in the file —
> `os.environ["FB_EMAIL"]` — especially if you ever share the project.

---

### 4. Confirm the Session

```python
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='main']"))
)
print("Logged in.")
```

---

### Summary Checklist

1. Third-party login opens a new window — switch with `window_handles` /
   `switch_to.window`.
2. Type into the Facebook form, submit, then switch back to the app window.
3. Wait for the redirect to your app's domain before continuing.
4. Captchas and 2FA mean manual first login; persist the browser profile afterwards.
