Here is a structured breakdown of this lesson on logging in.

---

### 1. The Cookie Banner First

Instagram's landing page shows a cookies dialog *before* the login form is usable:

```python
def login(self):
    self.driver.get("https://www.instagram.com/accounts/login/")

    self.driver.find_element(
        By.XPATH, "//button[text()='Allow essential cookies']").click()
    self.driver.find_element(
        By.NAME, "username").send_keys(self.username)
    self.driver.find_element(
        By.NAME, "password").send_keys(self.password)
    self.driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(5)     # let the dashboard load
```

1. Dismiss whatever dialog blocks the form.
2. Fill username + password by `name`.
3. Submit, then wait — the next page loads slowly.

---

### Summary Checklist

1. Popup → fields → submit → wait.
2. Selectors by name attribute are the most stable here.
