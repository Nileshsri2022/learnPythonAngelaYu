Here is a structured breakdown of this lesson on navigating to the login page.

---

### 1. Straight to the Action

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://tinder.com/")
login_link = driver.find_element(By.XPATH, '//*[@id="t975"]/div/div/div[1]/a')
login_link.click()
```

* `driver.get()` to the homepage, then click through to the login screen.
* Absolute XPaths like `//*[@id="t975"]/...` are **fragile** — the `t975` id is
  auto-generated. Prefer stable selectors (link text, class names) wherever possible.

---

### Summary Checklist

1. Navigate → click the login entry point.
2. Auto-generated ids break silently; anchor to stable attributes.
