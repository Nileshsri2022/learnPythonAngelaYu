Here is a structured breakdown of this lesson on the tweeting bot.

---

### 1. Login and Post

```python
def tweet_at_provider(self):
    self.driver.get("https://x.com/login")
    # ... fill email/username + password from env vars, submit ...

    tweet_box = self.driver.find_element(
        By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']")
    tweet_box.send_keys(
        f"Hey @{self.provider_handle}, why is my internet speed "
        f"{self.down}down/{self.up}up when I pay for "
        f"{self.promised_down}down/{self.promised_up}up?")
    self.driver.find_element(
        By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']").click()
```

```python
bot = InternetSpeedTwitterBot(promised_down=150, promised_up=20)
bot.get_internet_speed()
if bot.down < bot.promised_down or bot.up < bot.promised_up:
    bot.tweet_at_provider()
```

* The main guard: measure first, complain only when the numbers justify it.
* data-testid attributes are X's most stable selectors.

---

### Summary Checklist

1. Login → type into the composer → click post.
2. Complain only if the measurement says so.
3. Runnable version: [`main.py`](main.py)
