Here is a structured walkthrough of Step 2 — getting the news articles.

---

### 1. The Branch

Only spend a NewsAPI call when the move is significant:

```python
if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]   # top 3
```

---

### 2. Shaping the Messages

```python
formatted_articles = [
    f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
    f"Headline: {article['title']}.\n"
    f"Brief: {article['description']}"
    for article in articles
]
```

* A list comprehension (Day 26) builds one alert string per article — each includes the
  stock line so every SMS is self-contained.

---

### Summary Checklist

1. Threshold branch → fetch → take 3 articles.
2. Comprehension formats stock + headline + brief per message.
