Here is a structured breakdown of this lesson on creating the bot class.

---

### 1. Why a Class?

The bot has **state** (the measured speeds) and **behaviour** (measure, tweet). That is
exactly what classes are for (Day 16–17), and it keeps the driver, credentials and results
in one place instead of loose globals.

---

### 2. The Skeleton

```python
from selenium import webdriver


class InternetSpeedTwitterBot:
    def __init__(self, promised_down, promised_up):
        self.promised_down = promised_down
        self.promised_up = promised_up
        self.down = 0            # filled in by get_internet_speed()
        self.up = 0

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        """Run Speedtest and store the results on self.down / self.up."""
        ...

    def tweet_at_provider(self):
        """Log in to X and post the complaint."""
        ...

    def close(self):
        self.driver.quit()
```

| Attribute | Meaning |
|-----------|---------|
| `promised_down` / `promised_up` | what the ISP sold you |
| `down` / `up` | what you actually got |
| `driver` | the Selenium browser this bot owns |

---

### 3. Using It

```python
bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
bot.get_internet_speed()
print(f"Down {bot.down} / Up {bot.up} Mbps")

if bot.down < bot.promised_down or bot.up < bot.promised_up:
    bot.tweet_at_provider()

bot.close()
```

* `__init__` builds the driver; `close()` quits it — the class owns its browser.
* The decision to tweet lives in the script, not buried inside a method.

> **Tip:** Passing the promised speeds into `__init__` (rather than reading globals inside
> the class) makes the class reusable for a friend's contract too — dependency injection
> in one line.

---

### Summary Checklist

1. Class = state (speeds) + behaviour (measure, tweet) + the driver.
2. `__init__` configures Chrome once; `close()` quits cleanly.
3. Store measured values on `self` so both methods can use them.
4. Compare promised vs measured *outside* the class and decide whether to tweet.
