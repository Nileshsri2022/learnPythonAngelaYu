Here is a structured breakdown of this lesson introducing the Cookie Clicker project.

---

### 1. The Game

Cookie Clicker is deliberately addictive and deliberately simple:

* Click the giant cookie → bake cookies.
* Spend cookies on **upgrades** (cursor, grandma, farm…) that bake cookies *for* you.
* The score that matters is **cookies per second (CPS)** — every add-on you buy raises it.

> Doing this by hand is a fast route to repetitive strain injury. Perfect job for a bot.

---

### 2. Today's Project

Use Selenium to play the game for you:

1. Open the Cookie Clicker URL.
2. Click the cookie continuously (hundreds of times).
3. Every ~5 seconds, check the upgrade shop.
4. Buy the **most expensive upgrade you can afford** — it gives the biggest CPS boost.
5. Repeat.
6. Run for about **5 minutes**, then read the CPS display and compare scores.

```python
# the shape of the whole bot
while True:
    cookie.click()          # bake
    # every 5 s: find affordable upgrades, buy the best one
```

---

### 3. Why This Works as a Project

It combines everything from Days 45–48:

| Skill | Where it shows up |
|-------|-------------------|
| Finding elements | Cookie image, cookie counter, shop upgrades |
| `find_elements` | Iterating over every upgrade on the page |
| Reading element text | Parsing `"123 cookies"` / `"5 cookies per second"` |
| Clicking | Cookie + buy buttons |
| Timing | Buying only every 5 seconds so the shop can refresh |

---

### 4. Before You Build

Play the game by hand for ~5 minutes first — see how each upgrade improves CPS, and note
the element ids in DevTools (`#bigCookie`, `#cookies`, `#productPrice0`, …).

> **Tip:** The click loop is the one place where a `while True` is doing real work; the
> shop check runs on a schedule inside that loop.

---

### Summary Checklist

1. Click cookie → earn cookies → buy upgrades → raise cookies per second.
2. The bot clicks in a loop and buys the best affordable upgrade every 5 seconds.
3. Success metric: CPS after ~5 minutes, not total cookies.
4. Inspect the page first; ids like `#bigCookie` and the `product`/`productPrice` ids are
   what your selectors will hang on.
