Here is a structured breakdown of the Day 45 project — 100 Movies that You Must Watch.

---

### 1. The Task

Scrape Empire's "100 Greatest Movies of All Time" list and save every title to
`movies.txt` — one per line, #1 first — ready to work through.

---

### 2. The Solution

```python
import requests
from bs4 import BeautifulSoup

URL = ("https://web.archive.org/web/20200518073855/"
       "https://www.empireonline.com/movies/features/best-movies-2/")

response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

titles = [tag.getText() for tag in soup.find_all(name="h3", class_="title")]
titles.reverse()          # the page ranks 100 → 1; we want #1 first

with open("movies.txt", mode="w", encoding="utf-8") as file:
    file.write("\n".join(titles))
```

* The **Wayback Machine** snapshot is used because the live page's markup has changed —
  a very common real-world scraping fix.
* The list arrives as #100 → #1, so `reverse()` puts the best first.

> **Tip:** if a site redesign breaks your scraper, re-find the CSS class with DevTools —
> that's always the first thing to check.

---

### Summary Checklist

1. Locate the repeating element + class in DevTools → `find_all` → extract text.
2. Runnable version: [`main.py`](main.py)
