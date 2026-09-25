# Day 52 Goals- what you will make by the end of the day

---

### 1. The Idea: Grow a Following by Following

The trick an Instagram consultant shared: find an account whose audience matches yours,
open its **followers list**, and follow those people one by one. Many will follow back.

Example: a food brand follows the followers of an established food account — those people
are exactly the audience you want.

The problem: the target account had **247,000 followers**. Nobody is clicking that list
by hand. Perfect automation job.

---

### 2. What the Bot Does

1. Log in to Instagram automatically.
2. Navigate to the target account's profile.
3. Click the **followers** link (opens a modal list).
4. Scroll/click through the list, hitting **Follow** on each account.

All while your mouse sits untouched.

---

### 3. Why It's a Good Selenium Exercise

| Challenge | Skill |
|-----------|-------|
| Login page with changing UI | locators + waits |
| Followers list in a **scrollable modal** | scroll a container, not the page |
| Buttons that read *Follow* / *Following* / *Requested* | conditional logic |
| Very long list | loops + rate limits |
| Pop-ups ("you've followed too many people") | defensive handling |

---

### 4. House Rules

* Instagram rate-limits and may temporarily block accounts that follow too fast.
  Follow ~10–20 accounts, pause, and stop long before the site tells you to.
* Practise on the course clone (**Share-a-Naan**) so a real account is never at risk.
* Only follow people you'd genuinely be happy to have follow you back.

---

### Summary Checklist

1. Follow the followers of a similar account — many follow back.
2. Bot: log in → open profile → click followers → follow each one.
3. New mechanics today: switching into a scrollable modal window of results.
4. Be gentle: rate limits are real, and the practice clone exists for a reason.
