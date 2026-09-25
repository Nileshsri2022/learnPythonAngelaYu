# Day 47 Goals- what you will make by the end of the day

---

### 1. The Problem

Online prices swing wildly day to day. The Amazon price tracker watches a product for
you and **emails you when it drops below your target price** — no more refreshing the
page.

---

### 2. The Recipe

| Step | Tool |
|------|------|
| 1. Fetch the product page | `requests` (with browser-like headers) |
| 2. Find the price | BeautifulSoup |
| 3. Compare with your target | plain Python |
| 4. Email yourself a deal alert | `smtplib` (Day 32) |

---

### Summary Checklist

1. Scrape → compare → notify.
2. The one new trick: making requests look like a real browser.
