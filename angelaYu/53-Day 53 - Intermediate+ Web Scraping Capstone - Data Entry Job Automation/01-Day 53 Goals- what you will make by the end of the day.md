Here is a structured breakdown of this lesson on the Day 53 capstone goals.

---

### 1. The Genre: Data-Entry Automation

A lot of paid work is "move data from format A to format B" — from a PDF to a spreadsheet,
from a website into a form. That task is repetitive, rule-based and perfect for Python.

Today's job posting, in effect: *research rental listings in San Francisco under $3,000
with one bedroom, and deliver them in a spreadsheet.*

---

### 2. The Two Halves of the Project

| Half | Tool | Why |
|------|------|-----|
| **Read** the listings | `requests` + Beautiful Soup | static HTML, fast, no browser needed |
| **Write** them into a Google Form | Selenium | the form needs typing and clicking |

This is the *choose the right tool* lesson: scraping doesn't need a browser; form filling
does.

---

### 3. The Practice Site

Zillow's real markup changes constantly (and blocks scraping), so the course provides a
**stable clone**:

```
https://appbrewery.github.io/Zillow-Clone/
```

It's pre-filtered: San Francisco, for rent, up to $3,000, one bedroom.

---

### 4. What to Extract

For every listing card:

| Field | Example |
|-------|---------|
| Price per month | `$2,895` |
| Address | `2650 Steiner St, San Francisco, CA 94123` |
| Listing URL | `https://www.zillow.com/homedetails/…` |

Then submit each listing to a **Google Form** (address, price, link) — Google Forms turn
responses into a **Google Sheet** with one click, which is what the "client" receives.

---

### 5. Why It Matters

* The pattern generalises: scrape → clean → submit, over and over.
* Google Forms is a free database + spreadsheet for any small automation.
* An "unpaid overtime" story from the transcript: automating 70 % of a data-entry job is a
  well-known Python win — just don't tell your boss *and* do it badly.

---

### Summary Checklist

1. Capstone = scrape Zillow clone with Beautiful Soup, submit to Google Form with Selenium.
2. Practice URL: `https://appbrewery.github.io/Zillow-Clone/`.
3. Extract price, address and listing link for each property.
4. Form responses become a Google Sheet — the deliverable.
5. Right tool for each half: requests/BS4 for reading, Selenium for interacting.
