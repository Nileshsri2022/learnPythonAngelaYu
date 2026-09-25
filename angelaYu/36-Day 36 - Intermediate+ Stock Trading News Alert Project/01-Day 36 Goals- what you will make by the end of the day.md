# Day 36 Goals: what you will make by the end of the day

Day 36 is a challenge project: build your own **budget Bloomberg terminal[^1]** that
watches a stock and texts you the news behind any big move.

[^1]: A Bloomberg terminal costs around \$24,000 a year. This costs nothing but a few
    free API tiers.

---

### 1. What the Project Does

```text
1. get yesterday's closing price        ← stock price API
2. get the day-before's closing price   ← same API
3. compare: is the change >= 10%?       ← your own logic
4. if yes → fetch the latest news       ← news API
5. send the headlines by SMS            ← Twilio (Day 35)
```

A worked example from the lecture:

| Day | Closing price |
|-----|---------------|
| March 9 | \$1,000 |
| March 10 | \$1,100 |

Difference **+\$100** → `100 / 1000 * 100` = **+10%** → above the threshold → fetch
news for that company and send an alert.

---

### 2. Why News Matters

A price move on its own tells you *something happened*; the headlines tell you *why*
(new product, new factory, bad earnings). That is what you need in order to decide
whether to buy more or sell.

---

### 3. Your Job, Not the Instructor's

This is deliberately **self-directed**: pick the normal, hard or extra-hard starter
project, then work through the comments yourself. Expect 30–45 minutes minimum.

> **The real skill being practised:** reading an API's documentation and working out
> how to call an API you have never used before. There are millions of APIs — being
> able to dig through docs is what every developer actually does.

---

### Summary Checklist

1. Compare two consecutive closing prices; trigger on a ≥10% change.
2. On a trigger, fetch company news, then send it by SMS.
3. Twilio's SMS skills from Day 35 do the messaging.
4. Choose your difficulty and work from the starter project's comments.
5. The transferable skill: reading API docs and figuring it out alone.
