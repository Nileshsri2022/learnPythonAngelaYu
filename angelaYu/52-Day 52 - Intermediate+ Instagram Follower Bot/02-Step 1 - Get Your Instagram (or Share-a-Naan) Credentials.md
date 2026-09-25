# Step 1 - Get Your Instagram (or Share-a-Naan) Credentials

---

### 1. Pick Your Site

| Option | Notes |
|--------|-------|
| **Share-a-Naan** (course clone) | identical flow, safe to hammer with a bot |
| Real Instagram | expect rate limits, "suspicious activity" checks, possible blocks |

> **⚠️ Warning:** Instagram aggressively rate-limits automated actions. On a real account,
> following hundreds of people in a loop can trigger a temporary action block or a login
> challenge. Keep volumes tiny and behaviour human.

---

### 2. Create the Practice Account

* Open the course's clone link.
* Sign up with a throwaway email + password (or reuse the demo credentials from the
  course resources).
* Set `TARGET_ACCOUNT` to the account whose followers you want to poach:

```python
SIMILAR_ACCOUNT = "chefsteps"      # an account with a matching audience
INSTA_USERNAME = "your_handle"
INSTA_PASSWORD = "your_password"   # better: read from os.environ
```

---

### 3. Project Setup

```bash
mkdir instagram-follower-bot && cd instagram-follower-bot
pip install selenium
```

```python
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
```

---

### 4. Credentials Belong in the Environment

```python
import os

INSTA_USERNAME = os.environ.get("INSTA_USERNAME")
INSTA_PASSWORD = os.environ.get("INSTA_PASSWORD")
```

Same habit as Days 35 and 51 — never hard-code logins in a file you might push to GitHub.

---

### Summary Checklist

1. Practise on **Share-a-Naan**; real Instagram punishes rapid automated following.
2. Choose a *similar* account as the follower source.
3. Fresh project + Selenium; keep the browser detached.
4. Credentials from environment variables, not source code.
