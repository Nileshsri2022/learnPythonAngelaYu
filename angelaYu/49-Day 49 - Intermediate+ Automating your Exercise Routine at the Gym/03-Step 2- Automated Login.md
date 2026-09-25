Here is a structured breakdown of this lesson on automated login.

---

### 1. Fill the Form, Submit

```python
from selenium.webdriver.common.by import By

driver.find_element(By.ID, "email").send_keys(os.environ.get("GYM_EMAIL"))
driver.find_element(By.ID, "password").send_keys(os.environ.get("GYM_PASSWORD"))
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
```

* Credentials from **environment variables**, not literals — bots that type your
  password must not carry it in source.
* After the click, the session cookie keeps you logged in for later runs.

---

### Summary Checklist

1. The Day 48 verbs: `send_keys` + `click`.
2. Secrets stay in env vars.
