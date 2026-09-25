Here is a structured breakdown of Step 1 — the starting project and SerpAPI.

---

### 1. The Starting Files

```
main.py            — orchestrates the steps
data_manager.py    — reads/writes the Google Sheet via Sheety
flight_search.py   — queries the flight API
flight_data.py     — a FlightData structure for one offer
notification_manager.py — SMS via Twilio
```

Each class owns one responsibility — the architecture every capstone project uses.

---

### 2. SerpAPI

1. Register at serpapi.com → copy your API key (env var!).
2. Its `google_flights_engine` endpoint wraps Google Flights results as JSON —
   departure/arrival airports, dates, and offers with prices.

```python
FLIGHT_SEARCH_ENDPOINT = "https://serpapi.com/search.json"
```

---

### Summary Checklist

1. Five files, five responsibilities — read them before coding.
2. SerpAPI key goes straight into an environment variable.
