Here is a structured breakdown of this challenge lesson — the finished game bot.

---

### 1. The Full Bot

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

timeout = time.time() + 60 * 5          # play for 5 minutes
check_after = time.time() + 5

while time.time() < timeout:
    if time.time() > check_after:       # shop every 5 seconds
        cookies = int(driver.find_element(By.ID, "cookies").text.split()[0])
        items = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.toFill)")[::-1]
        for item in items:
            price = int(item.find_element(By.CLASS_NAME, "price").text.replace(",", ""))
            if cookies >= price:
                item.click()
                break
        check_after = time.time() + 5

print(driver.find_element(By.ID, "cookiesPerSecond").text)
driver.quit()
```

* `driver.quit()` at the end — close the browser cleanly.
* Tune the selectors if the site's markup changed; the loop never changes.

---

### Summary Checklist

1. Timed loop + state read + greedy buy = a competent idle-game bot.
2. Runnable version: [`main.py`](main.py)
