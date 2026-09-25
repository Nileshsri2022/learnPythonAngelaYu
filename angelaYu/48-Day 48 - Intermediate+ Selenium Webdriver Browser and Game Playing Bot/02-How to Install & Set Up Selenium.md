# How to Install & Set Up Selenium

---

### 1. Install the Pieces

1. **Google Chrome** — the browser we'll automate (Firefox/Safari also work, but Chrome
   has the DevTools workflow we use throughout this section).
2. **The Selenium package**:

```bash
pip install selenium
```

PyCharm shortcut: type `import selenium`, then click the red light-bulb → *Install package*.

---

### 2. Create the Driver

```python
from selenium import webdriver

driver = webdriver.Chrome()      # note the capital C
driver.get("https://www.amazon.com")
```

* `webdriver.Chrome()` instantiates a **ChromeDriver** object — an object-oriented
  concept from Day 16: a class describes a Chrome driver, `driver` is one instance of it.
* `driver.get(url)` is the Selenium equivalent of typing a URL and pressing Enter.

> **Note:** Each browser needs its own *bridge* driver: ChromeDriver for Chrome, GeckoDriver
> for Firefox. The bridge translates your Python commands into that browser's language.
> Modern Selenium (4.6+) downloads and manages the correct driver for you automatically.

---

### 3. macOS: Allowing ChromeDriver

The first run may show
*"chromedriver cannot be opened because the developer cannot be verified"*.

1. **Cancel** the dialog.
2.  → **System Preferences** → **Security & Privacy** → *Allow Anyway*.
3. Re-run — a final **Open** confirmation appears; the browser then launches normally.

---

### 4. Keeping the Browser Open (`detach`)

By default Chrome closes the moment the script ends. To keep it open for inspection:

```python
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")
```

You can also run headless (no visible window) with
`chrome_options.add_argument("--headless=new")`.

---

### 5. `close()` vs `quit()`

| Method | What it does |
|--------|--------------|
| `driver.close()` | Closes just the **current tab** |
| `driver.quit()` | Closes the **entire browser** and ends the session |

> **Tip:** Prefer `quit()` when you're finished — every un-quit run leaves another Chrome
> process behind, and they pile up fast. Comment it out while experimenting if you want
> the window to stay on screen.

---

### Summary Checklist

1. `pip install selenium` + Chrome installed.
2. `driver = webdriver.Chrome()` then `driver.get(url)`.
3. ChromeDriver is the bridge between Selenium and Chrome.
4. macOS may need *Allow Anyway* in Security & Privacy.
5. `add_experimental_option("detach", True)` keeps the window open.
6. `close()` = one tab, `quit()` = whole browser.
