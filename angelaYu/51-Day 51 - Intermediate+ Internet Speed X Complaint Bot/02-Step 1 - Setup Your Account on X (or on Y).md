Here is a structured breakdown of this lesson on setting up your account.

---

### 1. Get an Account on X (Twitter)

You need an account to post the complaint. The course provides an equivalent practice
site so you can build the bot without a real account:

| Option | Notes |
|--------|-------|
| **Practice clone (course resources)** | identical flow, no risk to a real account |
| Real X/Twitter account | enables 2FA; posting bots may be rate-limited or flagged |

---

### 2. Know Your Promised Speeds

Find the **guaranteed minimum download/upload** in your ISP contract or plan page. The
bot compares live measurements against these numbers:

```python
PROMISED_DOWN = 150     # Mbps — from your contract
PROMISED_UP = 10        # Mbps
```

Also note the provider's handle to complain at: `@comcast`, `@BT`, `@Ask_Spectrum`…

---

### 3. Project Setup

```bash
mkdir internet-speed-bot && cd internet-speed-bot
pip install selenium
```

```python
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
```

> **Tip:** Reuse the `--user-data-dir=<profile>` trick from Day 49/50 so the X session
> (and any captcha you solved by hand once) sticks around between runs.

---

### 4. Credentials

```python
import os

X_EMAIL = os.environ.get("X_EMAIL")
X_PASSWORD = os.environ.get("X_PASSWORD")
X_HANDLE = "@YourProvider"
```

Environment variables keep credentials out of the source file (Day 35).

---

### Summary Checklist

1. Use the practice clone, or accept the risk on a real account.
2. Write down the promised down/up speeds from your contract.
3. Fresh project, Selenium installed, browser detached.
4. Put credentials and the provider handle in constants/env vars.
