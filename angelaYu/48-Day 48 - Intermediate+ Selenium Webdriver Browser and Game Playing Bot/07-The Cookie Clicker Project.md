Here is a structured breakdown of this lesson on the Cookie Clicker project.

---

### 1. The Game

Cookie Clicker: click a giant cookie → earn cookies → buy upgrades (cursors, grandmas,
farms) that click *for* you. The strategy: always buy the cheapest affordable upgrade
with the best return. Perfect for a bot.

---

### 2. The Bot Loop

```python
import time

while True:
    cookies = int(driver.find_element(By.ID, "cookies").text.split()[0])
    store = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.toFill)")[::-1]

    for item in store:                    # cheapest last → first affordable wins
        price = int(item.find_element(By.CLASS_NAME, "price").text.replace(",", ""))
        if cookies >= price:
            item.click()
            break
    time.sleep(5)                         # let the cookies flow, then re-check
```

1. **Read** the cookie count (strip commas).
2. **List** affordable upgrades, cheapest-last so the first match is the best buy.
3. **Buy**, wait, repeat — for two minutes, then print the final cookies-per-second.

---

### Summary Checklist

1. Read state → decide → act → wait → repeat.
2. Every game bot is this loop with different selectors.
