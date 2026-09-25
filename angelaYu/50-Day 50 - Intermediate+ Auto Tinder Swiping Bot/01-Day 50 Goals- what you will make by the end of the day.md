Here is a structured breakdown of this lesson on the goals for Day 50.

---

### 1. The Idea: Auto-Swiping

Halfway through the course, today's project automates **Tinder**: log in, clear the
pop-ups, and swipe — all with Selenium, no thumb required.

The inspiration is the numbers: in interviews, Tinder has reported users logging in ~11×
per day with sessions around 7–8.5 minutes, plus users sharing their data showing one
match per ~100 swipes. Swiping is a repetitive, low-value loop — textbook automation.

---

### 2. What the Bot Will Do

1. Open Tinder in Chrome.
2. Log in **with Facebook**.
3. Dismiss the pop-ups Tinder throws at a new browser (notifications, location, cookies).
4. Click **Like** repeatedly.
5. When a match pop-up appears, dismiss it and keep going.

---

### 3. Know Before You Build

| Fact | Implication |
|------|-------------|
| Tinder caps free accounts at ~100 swipes/day | The bot is rate-limited by the app, not by code |
| A "Tinder finger" gadget does this physically | We're doing it in software instead |
| Not everyone wants a bot dating *for* them | Use the practice clone (**Tindog**) or spam *dislike* |

> **⚠️ Warning:** Automating a real account is against most apps' terms of service, may get
> the account flagged, and can surprise people you match with. Practise on the course's
> clone site; if you use a real one, tell the humans in your life and prefer dislikes so
> nobody gets auto-matched.

> **Tip:** If you don't want to use your own photo, `thispersondoesnotexist.com` generates
> neural-network faces (not real people) for a practice profile.

---

### 4. Skills Reused

* `find_element` / `find_elements` (Day 48) to locate pop-up buttons.
* `.click()` for login, dismissals and swipe buttons.
* Handling **state that changes on every page load** — pop-ups only appear the first time,
  so "dismiss if present" must be optional, not assumed.

---

### Summary Checklist

1. Bot: login with Facebook → dismiss pop-ups → click Like → handle matches.
2. Free accounts are limited to ~100 swipes/day regardless of the bot.
3. Practise on the course clone; respect other people and the app's terms.
4. Today's new skill: dealing with conditional, unpredictable pop-ups.
