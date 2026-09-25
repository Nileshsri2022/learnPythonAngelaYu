Here is a structured breakdown of this lesson on setup and the Chrome profile.

---

### 1. Start Chrome as *You*

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:5001")
# or: options.add_argument(r"--user-data-dir=/path/to/ChromeProfile")
driver = webdriver.Chrome(options=options)
driver.get("https://www.gym-site.com/schedule")
```

Attaching to your real profile means cookies and sessions come along — the site
already trusts this browser.

> **Warning:** close all Chrome windows first when attaching to a profile, or the port
> won't answer.

---

### Summary Checklist

1. Real profile = saved logins, no captcha friction.
2. `driver.get()` to the schedule page.
