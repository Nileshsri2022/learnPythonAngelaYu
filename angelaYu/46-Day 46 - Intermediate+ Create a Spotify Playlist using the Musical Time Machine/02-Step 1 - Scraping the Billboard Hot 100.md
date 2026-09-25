# Step 1 - Scraping the Billboard Hot 100

---

### 1. Billboard's Chart URLs

```python
import requests
from bs4 import BeautifulSoup

date = "2000-08-12"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
```

Billboard keeps an archive — any date works, and the URL pattern is simply the date.

---

### 2. Pulling Out the Song Titles

```python
song_titles = [tag.getText().strip()
               for tag in soup.select("li h3#title-of-a-story")]
```

* Each chart entry's title lives in an `<h3>`; `strip()` removes the whitespace the
  markup adds.
* Billboard redesigns its site regularly — if the list comes back empty, re-find the
  class in DevTools and update the selector.

---

### Summary Checklist

1. Date in the URL = any week in Hot 100 history.
2. Scrape titles into a list; Spotify work comes next.
