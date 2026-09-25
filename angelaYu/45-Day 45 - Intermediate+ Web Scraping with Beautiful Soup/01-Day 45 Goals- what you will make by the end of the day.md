Here is a structured breakdown of this lesson on the goals for Day 45.

---

### 1. Why Scraping When We Have APIs?

APIs (Days 32–40) are the *official* door to a website's data — but not every site has
one, and not every API exposes what you want. **Web scraping** is reading the site's
underlying HTML directly and extracting the data yourself.

* Search engines (Google, Bing) are essentially web scrapers at planetary scale.
* Today's toolkit: `requests` (fetch) + **Beautiful Soup** (parse).

---

### 2. Today's Project

Scrape Empire Magazine's "100 Greatest Movies" list and turn it into a personal
watch-list file you can check off.

---

### Summary Checklist

1. No API → scrape the HTML.
2. requests downloads; BeautifulSoup makes it searchable.
