# Step 4 - Scrape the live Amazon site

---

### 1. The Live Script

Put the whole pipeline together against the real Amazon URL, then run it **daily** —
locally via cron / Windows Task Scheduler, or in the cloud on GitHub Actions (exactly
like the Rain Alert on Day 35):

```yaml
on:
  schedule:
    - cron: '0 3 * * *'   # 03:00 UTC every day
```

* Price drops are a game of patience — automation beats memory.
* Keep the target price in a variable at the top so it's easy to change per product.

---

### Summary Checklist

1. Live URL + headers + scrape + compare + email.
2. Schedule it and forget it.
3. Runnable version: [`main.py`](main.py)
