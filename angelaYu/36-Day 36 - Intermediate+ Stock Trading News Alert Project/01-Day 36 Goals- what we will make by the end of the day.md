# Day 36 Goals- what we will make by the end of the day

---

### 1. Skills Covered on Day 36

* Chaining **three APIs** in one pipeline: stocks, news, messaging
* Percentage-change maths over historical price data
* String formatting into alert messages
* Optional: your own twist ("Choose Your Destiny" — different stock, different alert)

---

### 2. The Project

Monitor Tesla (TSLA):

1. **Alpha Vantage** — yesterday's and day-before-yesterday's closing prices.
2. If the price moved more than **±5%** →
3. **NewsAPI** — fetch the top 3 company articles.
4. **Twilio** — SMS you: the move (🔺/🔻 + percent) plus each headline.

```text
TSLA: 🔺4.2%
Headline: Tesla shares surge after...
Brief: ...
```

---

### Summary Checklist

1. Data → decision → context → delivery: a real monitoring pipeline.
2. All secrets via environment variables (Day 35).
