Here is a structured breakdown of this lesson on hitting Like.

---

### 1. Swipe Right Forever

```python
like_button = driver.find_element(By.XPATH,
    "//button[@aria-label='Like']")

for _ in range(100):
    like_button.click()
```

* Find the Like button once; click it in a loop — the site swaps profiles under it.
* Free accounts run out of likes (~100/day); the bot's honest limit.
* Add a small `time.sleep(1)` between clicks to look less like a machine.

> **Warning:** Auto-liking violates Tinder's ToS — this project is a Selenium drill on
> a demo/practice account, not an endorsement.

---

### Summary Checklist

1. Locate once, click in a loop.
2. Respect rate limits — even where ToS doesn't.
3. Runnable version: [`main.py`](main.py)
