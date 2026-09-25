Here is a structured breakdown of this lesson on using API keys with OpenWeatherMap.

---

### 1. Read the Docs First

Every API's documentation defines its endpoint, parameters and auth method. For
OpenWeatherMap (after signing up and generating a key):

```
https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
```

---

### 2. The Call

```python
import requests

API_KEY = "your_key_here"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 26.8467,
    "lon": 80.9462,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 12,          # next 12 forecast slices (3h each)
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
```

* `appid` — the key travels as a parameter (their documented auth method).
* `units=metric` gives Celsius; `cnt` limits the number of timestamps returned.

---

### Summary Checklist

1. Docs → endpoint + params + auth mechanism.
2. Key in `appid`; `params` dict assembles the request.
