Here is a structured breakdown of this lesson on the bot class.

---

### 1. Same Skeleton as Day 51

```python
class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        ...

    def find_followers(self):
        ...

    def follow_all(self):
        ...
```

* Three methods, one per step: `login()`, `find_followers()`, `follow_all()`.
* Keeping Selenium inside a class makes the driver swap-able (Chrome → Firefox) without
  touching the logic.

---

### Summary Checklist

1. State on `self`, steps as methods.
2. Same OOP skeleton, new target site.
