Here is a structured breakdown of this lesson on creating the bot class.

---

### 1. OOP Meets Selenium

```python
class InternetSpeedTwitterBot:
    def __init__(self, promised_down, promised_up):
        self.down = promised_down
        self.up = promised_up
        self.driver = webdriver.Chrome()

    def get_internet_speed(self):
        ...

    def tweet_at_provider(self):
        ...
```

* State the bot needs (promised speeds, driver, measured speeds) lives on `self`.
* Behaviour is methods: measure, complain.
* This is the Day 36-41 style — a clean module you could import anywhere.

---

### Summary Checklist

1. Class = state + behaviour; Selenium driver as an attribute.
2. Two verbs: `get_internet_speed()`, `tweet_at_provider()`.
