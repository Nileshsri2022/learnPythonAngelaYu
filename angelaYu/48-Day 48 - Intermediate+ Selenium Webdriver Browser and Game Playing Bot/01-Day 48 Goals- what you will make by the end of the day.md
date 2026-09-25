# Day 48 Goals- what you will make by the end of the day

---

### 1. Why Learn Selenium When We Have Beautiful Soup?

Beautiful Soup is brilliant at *reading* HTML — but it cannot *act*. It cannot type into
a box, click a button, or wait for JavaScript to finish. Selenium WebDriver drives a
**real browser**, so it can do anything a human can:

| Capability | Beautiful Soup | Selenium |
|------------|----------------|----------|
| Download & parse HTML | ✅ | ✅ |
| Handles JavaScript-rendered pages | ❌ | ✅ |
| Type into inputs | ❌ | ✅ |
| Click buttons / links / scroll | ❌ | ✅ |
| Sends real browser headers (no 403 surprises) | ❌ | ✅ |

> **Tip:** If a page loads its content with React, Angular or plain JavaScript, the HTML
> Beautiful Soup receives is often empty. Selenium sees the *fully rendered* page.

---

### 2. What "Browser Automation" Means

You write a script; Selenium translates it into real browser actions:

```python
driver.get("https://example.com")        # open a page
driver.find_element(By.NAME, "q")        # pick an element
search.send_keys("Python")               # type
button.click()                           # click
```

Think of it as building a robot that sits in front of Chrome and does the boring parts
for you — the browser equivalent of the Karel robot from Day 6.

---

### 3. Practical Uses

* Filling in repetitive web forms (e.g. Excel data → Google Form).
* Scraping sites that only render client-side.
* Testing a web app you're building.
* Playing web games — today's project: an automatic **Cookie Clicker** bot.

---

### 4. Today's Project: The Cookie Clicker Bot

The game: click a giant cookie to bake cookies, spend cookies on upgrades (cursors,
grandmas…) that bake more cookies per second (CPS). The bot will:

1. Open the game.
2. Click the cookie continuously.
3. Every 5 seconds, find upgrades it can afford and buy the best one.
4. Run for ~5 minutes, then report **cookies per second** — the score to beat.

---

### Summary Checklist

1. Beautiful Soup reads; Selenium *acts* — it drives a real browser.
2. Selenium handles JavaScript-rendered pages and sends normal browser headers.
3. Use it for form filling, scraping, testing and (of course) cheating at Cookie Clicker.
4. Today's score metric: cookies baked per second.
