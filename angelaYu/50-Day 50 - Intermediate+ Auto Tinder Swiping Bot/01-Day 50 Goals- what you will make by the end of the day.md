Here is a structured breakdown of this lesson on the goals for Day 50.

---

### 1. Halfway Celebration: the Tinder Bot

The bot opens Tinder (or **Tindog**, the course's practice clone), logs in via
Facebook, dismisses the popup dialogs, then hits **Like** on every profile until the
free supply of likes runs dry.

---

### 2. The Flow

| Step | Selenium action |
|------|-----------------|
| 1. Account ready | manual, once |
| 2. Navigate to login | `driver.get()` |
| 3. Login with Facebook | switch windows, fill form |
| 4. Dismiss popups | loop `.click()` on the dismiss button |
| 5. Like everything | loop `.click()` on the Like button |

---

### Summary Checklist

1. Bots excel at mindless repetition — that's the whole joke of Day 50.
2. Popups are the real boss fight.
