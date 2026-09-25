# Using API Keys to Authenticate and Get the Weather from OpenWeatherMap

The first rule of a new API: **read the documentation**. Everything below is what the
OpenWeatherMap docs tell you, turned into a working request.

---

### 1. Pick an Endpoint

OpenWeatherMap sells several products, each with its own endpoint:

| Product | Endpoint |
|---------|----------|
| Current weather | `api.openweathermap.org/data/2.5/weather` |
| 5-day / 3-hour forecast | `api.openweathermap.org/data/2.5/forecast` |
| One Call, hourly, … | other endpoints from the same docs |

Start with the simplest thing that can work — current weather:

```text
https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=YOUR_KEY
```

* `q` — the **query** parameter for the city name (`London,uk` avoids London, Ontario).
* `appid` — your **API key**; every call to this service needs it.

---

### 2. Get Your Own Key

1. Sign up at openweathermap.org and sign in.
2. Open **API keys** → generate one (name it e.g. `Python` so you know where it is used).
3. Paste it into your project — *for now* as a string in `main.py`:

```python
API_KEY = "your-key-here"
```

> ⚠️ A key in your code will end up on GitHub. Day 35's later lesson replaces this
> with an environment variable.

---

### 3. Read the Response Code First

```python
import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 51.5074,      # note: no "g" — it really is lon, not long
    "lon": -0.1278,
    "appid": API_KEY,
}
response = requests.get(OWM_ENDPOINT, params=weather_params)
print(response.status_code)          # 200 = everything A-OK
```

| Code | Meaning | What to do |
|------|---------|-----------|
| **200** | Success | Parse the JSON |
| **401** | Unauthorized | Key invalid, misspelled or missing — check `appid` |

---

### 4. The 5-Day / 3-Hour Forecast Payload

The `/forecast` endpoint returns the weather **every three hours** for five days:

* **8 forecasts per day** (03:00, 06:00, 09:00, … 00:00) → **40 entries in total**.
* Get your coordinates from latlong.net (keep the minus sign for west/south).
* Paste the JSON into an online JSON viewer to explore it — the raw string is unreadable.

Useful fields inside each entry:

| Field | Notes |
|-------|-------|
| `dt_txt` | Human-readable time (`2026-09-25 12:00:00`) — `dt` alone is a Unix timestamp |
| `main.temp` | Temperature **in Kelvin** by default |
| `weather` | A **list** — `weather[0]["description"]` is e.g. `overcast clouds` |
| `city.name` | The place OpenWeatherMap matched to your coordinates (e.g. Abbey Wood) |

```python
data = response.json()
print(data["list"][0]["weather"][0]["description"])   # overcast clouds
```

---

### 5. Your Turn

Repeat the request with the 5-day forecast endpoint using **your own** latitude,
longitude and `appid`, then find the forecast list in the JSON. Reading the docs and
getting a working call out of a brand-new API is the actual skill here — you will do
it hundreds of times as a developer.

---

### Summary Checklist

1. Read the docs first: endpoint, parameters, authentication.
2. `q=City,country` for current weather; `lat`/`lon`/`appid` for coordinates.
3. `requests.get(endpoint, params=params)` then check `status_code`.
4. 200 = OK; 401 = your API key is wrong or missing (`appid`, all lowercase).
5. `/forecast` = 3-hourly data for 5 days = **40 forecasts**; `weather` is a **list**,
   temperature is in Kelvin, `dt_txt` is the readable time.
