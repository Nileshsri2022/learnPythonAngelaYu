Here is a structured breakdown of this lesson on creating the bot class.

---

### 1. The Class

Same design as Day 51's bot — state + behaviour + its own driver:

```python
from selenium import webdriver


class InstaFollower:
    def __init__(self, similar_account, username, password):
        self.similar_account = similar_account
        self.username = username
        self.password = password

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        """Log in to Instagram / Share-a-Naan."""
        ...

    def find_followers(self):
        """Open `similar_account` and click the followers link."""
        ...

    def follow(self):
        """Follow the people in the followers list."""
        ...

    def close(self):
        self.driver.quit()
```

---

### 2. Why Three Methods?

Each method maps to one *step* of the job, so you can run them one at a time and inspect
the browser in between:

```python
bot = InstaFollower(SIMILAR_ACCOUNT, INSTA_USERNAME, INSTA_PASSWORD)
bot.login()
bot.find_followers()
bot.follow()
bot.close()
```

That is also how you debug a Selenium bot: run the pieces, look at the real page, then
move to the next step.

---

### 3. Setup the Driver Once

* Create the driver in `__init__` so all methods share one session.
* Pass in the account/credentials rather than reading globals inside the class.
* Add a `close()` method for a clean `quit()`.

> **Tip:** A `DEBUG = True` flag that skips `follow()` but performs login and navigation is
> the fastest way to test selector changes without annoying the site.

---

### Summary Checklist

1. `InstaFollower` holds the target account, credentials and driver.
2. `login()` → `find_followers()` → `follow()` mirrors the steps of the task.
3. Configure Chrome once in `__init__`; quit in `close()`.
4. Run the methods individually to debug against the live page.
