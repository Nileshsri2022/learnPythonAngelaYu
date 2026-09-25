# Step 3 - Get flights and prices for a single city

---

### 1. The Search Parameters

```python
from datetime import datetime, timedelta

tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)

class FlightSearch:
    def search_flight(self, origin, destination):
        params = {
            "engine": "google_flights",
            "departure_id": origin,          # e.g. "DEL"
            "arrival_id": destination,       # e.g. "CDG"
            "outbound_date": six_months.strftime("%Y-%m-%d"),
            "return_date": (six_months + timedelta(days=7)).strftime("%Y-%m-%d"),
            "currency": "INR",
            "hl": "en",
            "api_key": os.environ.get("SERPAPI_KEY"),
        }
        response = requests.get(FLIGHT_SEARCH_ENDPOINT, params=params)
        response.raise_for_status()
        return response.json()
```

* Flights are searched roughly **1 day to 6 months** ahead.
* Dates must be `YYYY-MM-DD` strings.

---

### Summary Checklist

1. IATA codes in, offers out — origin, destination, dates, key.
2. `timedelta` (Day 32) builds the search window.
