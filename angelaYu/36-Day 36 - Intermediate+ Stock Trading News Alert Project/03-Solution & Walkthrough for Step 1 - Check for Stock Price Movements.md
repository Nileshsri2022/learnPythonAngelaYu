# Solution & Walkthrough for Step 1 - Check for Stock Price Movements

---

### 1. Fetching the Data

```python
import requests
from datetime import datetime

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
```

---

### 2. Yesterday vs. Day Before

```python
data_list = [value for (key, value) in data.items()]   # newest first
yesterday_data = data_list[0]
yesterday_closing = float(yesterday_data["4. close"])

day_before_yesterday = data_list[1]
dby_closing = float(day_before_yesterday["4. close"])

difference = yesterday_closing - dby_closing
up_down = "🔺" if difference > 0 else "🔻"

diff_percent = round((difference / dby_closing) * 100, 2)
```

* `data.items()` preserves newest-first order — index 0 is yesterday.
* Percentage change relative to the **older** price.

---

### Summary Checklist

1. Daily time series → list → first two entries.
2. Difference → sign emoji → percentage.
