# Step 1 - Setup your account on Tinder (or on Tindog)

---

### 1. Pick Your Playground

| Option | Notes |
|--------|-------|
| **Tindog** (course clone) | Stable markup, built for practice — recommended |
| Real Tinder | Log in with Facebook, but see the warning below |

> **⚠️ Warning:** Bots on live dating apps violate the terms of service and can get your
> account suspended. If you do use a real account, keep it low-key, prefer dislike
> swipes, and know that the free tier stops you at ~100 swipes/day anyway.

---

### 2. Create / Open the Account

* If using the clone: the course resources link, and it works with a dummy
  Facebook-style login.
* If using real Tinder on the web: sign in at `tinder.com` → *Log in with Facebook* —
  the same flow the bot will replay.

---

### 3. Project Setup

```bash
mkdir tinder-bot && cd tinder-bot
pip install selenium
```

```python
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDER_URL)

input("Press Enter once you're logged in (first time only)…")
```

> **Tip:** On the very first run you may have to log in by hand — captchas and 2FA are
> designed to stop exactly the thing you're building. Log in once, keep the profile
> (`--user-data-dir`), and the bot inherits the session afterwards.

---

### 4. Sanity-Check the Page

Open DevTools and confirm what a "logged in, pop-ups pending" page looks like — that's
the state Step 3 starts from.

---

### Summary Checklist

1. Practise on **Tindog**; live apps are ToS-hostile and rate-limited.
2. Fresh project, `pip install selenium`, keep the browser detached.
3. First login may be manual; persist the profile so later runs start logged in.
4. Inspect the logged-in page before writing any selector.
