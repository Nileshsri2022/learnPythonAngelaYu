Here is a structured breakdown of this lesson on installing Selenium.

---

### 1. Setup

```bash
pip install selenium
```

Modern Selenium (4.6+) bundles its drivers — no manual chromedriver downloads:

```python
from selenium import webdriver

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://www.amazon.com/dp/B075CYNTQV")
```

A real Chrome window opens and navigates to the URL.

---

### 2. Useful Driver Commands

```python
chrome_driver.title()      # page title
chrome_driver.current_url  # after redirects
chrome_driver.page_source  # the rendered HTML
chrome_driver.close()      # close the window / quit the driver
```

* Keep Chrome installed — Selenium drives the browser you have.

---

### Summary Checklist

1. `pip install selenium` + `webdriver.Chrome()` — that's the whole setup.
2. `driver.get(url)` opens a page like typing in the address bar.
