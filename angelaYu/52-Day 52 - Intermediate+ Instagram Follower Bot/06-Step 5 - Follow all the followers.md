# Step 5 - Follow all the followers

---

### 1. Click, Pause, Repeat

```python
import random
import time

def follow(self, limit=20):
    dialog = self.driver.find_element(By.CSS_SELECTOR, "div[role='dialog']")

    followed = 0
    for button in dialog.find_elements(By.CSS_SELECTOR, "button"):
        if button.text != "Follow":
            continue                              # skip Following / Requested
        try:
            button.click()
            followed += 1
        except Exception as error:                # noqa: BLE001
            print("Stopped at", followed, "-", error)
            break

        time.sleep(random.uniform(2, 5))          # human-ish pacing

        if followed >= limit:
            print("Daily/self-imposed limit reached.")
            break

    print(f"Followed {followed} accounts.")
```

* Filtering on `button.text == "Follow"` prevents accidental **unfollows**.
* Random 2–5 s pauses look far more human than a metronomic 1 s.
* Stop reasons: self-imposed limit, rate limit, or an exception (element vanished because
  the list re-rendered).

---

### 2. Why the Buttons Change

After clicking, the button's text turns into **Following**, and the list sometimes
re-renders, invalidating your element references. That's why the loop re-reads
`find_elements` and re-checks the text each iteration, and why it tolerates exceptions
rather than assuming every click works.

---

### 3. Respect the Platform

| Signal | Meaning | Response |
|--------|---------|----------|
| "Try again later" | rate limited | stop, wait hours |
| "We restrict certain activity" | temporary action block | stop, lower volume next time |
| Login challenge | suspicious activity | solve by hand once, slow down |

Instagram's free-tier app is designed to stop exactly this bot — the practice clone is the
place to run it repeatedly.

> **Tip:** Follow 10–20 people per run, once a day. Slow and consistent grows an account;
> fast and aggressive gets it locked.

---

### 4. Wrap Up

```python
bot.follow(limit=20)
bot.close()
```

---

### Summary Checklist

1. Click only buttons whose text is `"Follow"` — never `"Following"`.
2. Random pauses of 2–5 s; a modest per-run limit (10–20).
3. Re-read the button list each iteration; expect stale elements and rate-limit banners.
4. Detect "try again later" and stop immediately — then go slower tomorrow.
