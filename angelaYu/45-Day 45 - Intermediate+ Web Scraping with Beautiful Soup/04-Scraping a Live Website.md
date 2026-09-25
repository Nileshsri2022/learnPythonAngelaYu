Here is a structured breakdown of this lesson on scraping a live website.

---

### 1. requests + BeautifulSoup

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
```

`response.text` is the raw HTML — exactly what right-click → *View Page Source* shows.

---

### 2. Hacker News Article Scores

```python
articles = soup.find_all(name="a", class_="storylink")
article_texts  = [tag.getText() for tag in articles]
article_links  = [tag.get("href") for tag in articles]
article_scores = [int(score.getText().split()[0])
                  for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_scores)
largest_index  = article_scores.index(largest_number)
print(article_texts[largest_index])   # headline of the top-voted story
```

* Find the CSS class in DevTools first, then target it with `find_all`.
* List comprehensions turn tag soup into clean parallel lists.

---

### Summary Checklist

1. `requests.get(...).text` replaces the local file as the HTML source.
2. `raise_for_status()` before parsing — always.
