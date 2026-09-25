# Step 1- Setup, Chrome Profile, and Basic Navigation

---

### 1. Create the Project

```bash
mkdir gym-booking-bot && cd gym-booking-bot
pip install selenium
```

Then open the course's gym test site in Chrome and log out of any existing session so you
know exactly what the bot will see.

---

### 2. Reuse Your Real Chrome Profile

The gym's data lives in the browser (IndexedDB), so the bot must open the **same profile**
every run:

```python
from selenium import webdriver

PROFILE = "/Users/you/Library/Application Support/Google/Chrome/Default"

options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={PROFILE}")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(GYM_URL)
```

* `--user-data-dir` points at the folder Chrome uses for cookies, logins and IndexedDB.
* Point it at a *dedicated* profile folder if you don't want the bot sharing your everyday
  browsing profile.

> **⚠️ Warning:** Chrome refuses to start if another window already uses that profile —
> close Chrome before running the bot.

---

### 3. Basic Navigation

```python
driver.get(GYM_URL)                    # home page
driver.find_element(By.LINK_TEXT, "Login").click()
```

Useful to know: `driver.back()`, `driver.forward()`, `driver.refresh()`, and
`driver.current_url` for asserting where you ended up.

---

### 4. Waiting for the Page

Browser apps render asynchronously, so elements may not exist the instant the page loads:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "email"))
)
```

* Waits up to 10 s, then raises `TimeoutException`.
* Far more reliable than `time.sleep(2)` sprinkled through the script.

---

### Summary Checklist

1. Fresh project + `pip install selenium`.
2. `--user-data-dir=<profile>` keeps cookies and the IndexedDB database stable between runs.
3. Close Chrome first — a locked profile refuses to open.
4. `driver.get()` / `.click()` navigate; `driver.current_url` tells you where you are.
5. `WebDriverWait` + `expected_conditions` beat blind `sleep()` calls.
