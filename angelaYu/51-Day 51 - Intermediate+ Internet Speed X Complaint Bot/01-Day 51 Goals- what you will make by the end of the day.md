Here is a structured breakdown of this lesson on the goals for Day 51.

---

### 1. The Idea: Complain Automatically

Internet providers promise a minimum speed in your contract. Proving you're not getting it
usually means calling support and waiting on hold. Today's bot does the complaining for
you, in public, where customer-service teams actually pay attention.

**The pipeline:**

```
speedtest.net  →  read download/upload  →  compare with what you pay for  →  tweet at your ISP
```

---

### 2. Why Twitter/X Works for This

Complaints on social media are **public** — big brands staff social media monitors, and
replies there are often faster and more generous than a phone queue (JetBlue is the
famous example). A bot can post the same complaint every day, at any hour, with evidence
(a Speedtest result ID) attached.

---

### 3. The Project

Build a class, `InternetSpeedTwitterBot`, with two jobs:

| Method | Responsibility |
|--------|----------------|
| `get_internet_speed()` | drive Speedtest, wait for the test to finish, scrape download & upload |
| `tweet_at_provider()` | log in to X, compose the complaint, post it |

Then compare actual speeds against your **promised** speeds and only tweet when the bot
finds you've been short-changed.

---

### 4. Things to Keep in Mind

* A Speedtest run takes 30 s – 2 min — Selenium must *wait*, not guess.
* The numbers appear as text in elements whose ids/classes can change; inspect the page.
* X login has 2FA/captcha traps; a persistent profile saves you from repeated logins.
* Keep the tweet polite and factual — it's a complaint, not a rant.

---

### Summary Checklist

1. Speedtest → scrape speeds → compare to the contract → tweet the ISP.
2. Public complaints get better customer service responses than private ones.
3. Two methods, one class: `get_internet_speed()` and `tweet_at_provider()`.
4. Real sites change markup — inspect before trusting any selector.
5. Only tweet when the measured speed is actually below the promised one.
