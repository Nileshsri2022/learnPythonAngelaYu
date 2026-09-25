Here is a structured breakdown of this challenge: building the automated game playing bot.

---

### 1. The Challenge

No new syntax today — take the Cookie Clicker plan and build the whole bot yourself.
The loop is the deliverable:

* Click the cookie as fast as the browser allows.
* Every 5 seconds, buy the best upgrade you can afford.
* Stop after ~5 minutes and report cookies per second.

---

### 2. Step 1 — Open the Game and Find the Cookie

```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "bigCookie")
```

---

### 3. Step 2 — Discover the Upgrade Buttons

In DevTools the shop items look like:

```html
<div id="product0" class="product unlocked enabled">  <!-- Cursor -->
<div id="product1" class="product unlocked enabled">  <!-- Grandma -->
```

The price lives in a sibling: `<div id="productPrice0">15</div>`.

```python
# ids created in order of price: product0 is cheapest
items = [item.get_attribute("id")
         for item in driver.find_elements(By.CSS_SELECTOR, "[id^='product']")]
```

---

### 4. Step 3 — The Buying Logic

```python
def buy_upgrades():
    """Buy the most expensive upgrade we can currently afford."""
    cookies = int(driver.find_element(By.ID, "cookies").text.split(" ")[0])

    for item in items[::-1]:                       # most expensive first
        price = int(driver.find_element(By.ID, f"productPrice{item[-1]}").text)
        if cookies >= price:
            driver.find_element(By.ID, item).click()
            return
```

* `items[::-1]` reverses the list (list slicing from Day 21) so the best upgrade is tried
  first.
* `"123 cookies".split(" ")[0]` → `"123"` → `int` (string cleaning from Day 47).

---

### 5. Step 4 — Click, Check, Repeat

```python
timeout = time.time() + 5 * 60   # 5 minutes from now
five_seconds = time.time() + 5

while True:
    cookie.click()

    if time.time() > five_seconds:
        buy_upgrades()
        five_seconds = time.time() + 5

    if time.time() > timeout:
        cps = driver.find_element(By.ID, "cps").text
        print(f"Cookies per second: {cps}")
        driver.quit()
        break
```

> **Tip:** Clicking an element that is disabled raises an exception — check the `enabled`
> class or wrap the click in `try/except` (Day 30) for a resilient bot.

---

### 6. Going Further

* Wrap the buy step in `try/except` to ignore upgrades that vanish mid-loop.
* Only buy when the item is at least ~10 % more efficient than the last upgrade.
* Try a headless browser and compare CPS.

---

### Summary Checklist

1. Grab `#bigCookie`, click it in a tight loop.
2. Enumerate `#productN` ids and their `#productPriceN` values.
3. Buy the most expensive affordable upgrade, checking every 5 seconds.
4. Track time for a 5-minute run, then print CPS and `quit()`.
5. Clean text → `int` conversions are the glue between the page and your logic.
