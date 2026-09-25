# Day 35 Goals: what you will make by the end of the day

Day 35 is a packed one: **API keys, authentication, environment variables and SMS** —
ending with a rain-alert program that texts you before you leave the house.

---

### 1. The Project: Rain Alert

Every morning, before you head out:

* Check the weather forecast for the next 12 hours with the **OpenWeatherMap** API.
* If rain is coming, send yourself an **SMS** with the **Twilio** API:
  *"It's going to rain today. Bring an umbrella!"*

No more checking the weather app — your phone tells you.

---

### 2. The Three New Ideas

| Idea | What it means |
|------|---------------|
| **Authentication** | Proving who you are to an API — your **API key** is your account number *and* password |
| **Twilio API** | A service that sends SMS (and WhatsApp) messages on your behalf |
| **Environment variables** | Keeping your keys **out of your code**, so they never end up in a Git commit |

Why the fuss? Valuable data (weather, financial) costs money to produce, so providers
meter it. A free tier plus an API key lets them track how much *you* use — and it
keeps paying customers' data safe.

```python
# the pattern for every authenticated API call
import os, requests

API_KEY = os.environ.get("OWM_API_KEY")      # never hard-code the key
parameters = {"lat": 51.5074, "lon": -0.1278, "appid": API_KEY, "cnt": 4}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                        params=parameters)
response.raise_for_status()
```

---

### Summary Checklist

1. Rain alert = weather API + `if` rain in the next 4 slots → SMS via Twilio.
2. An **API key** authenticates your requests and is rate-limited per account.
3. Authenticated endpoints take the key as a **parameter** (`appid`, `api_key`).
4. Store keys in **environment variables** — never in code you commit.
5. Optional extras: WhatsApp instead of SMS, PythonAnywhere/GitHub Actions to run daily.
