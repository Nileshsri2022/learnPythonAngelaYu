# Day 33 Goals: what you will make by the end of the day

Day 33 introduces **APIs** — Application Programming Interfaces — and builds an
**ISS overhead notifier**: a script that emails you when the International Space
Station is passing over your location.

---

### 1. The Project

The ISS circles the Earth many times a day. The plan:

1. Ask an API **where the ISS is right now** (latitude and longitude).
2. Ask a second API **when the sun sets and rises** at *your* position.
3. If the ISS is within ~5° of you **and** it is night, send yourself an email:
   *"Look up — the ISS is overhead."*

That is your first program that combines **two live data sources** and reacts to
real-world conditions.

---

### 2. What You Will Learn

| Idea | Used for |
|------|----------|
| What an API is | Requesting data that someone else maintains |
| API **endpoints** | The URL you call (`http://api.open-notify.org/iss-now.json`) |
| HTTP status codes & exceptions | Knowing whether the request worked |
| **JSON** responses | Turning the reply into a Python dictionary |
| API **parameters** | Customising the reply (latitude, longitude, date, formatted=0) |

```python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()          # blow up on 4xx / 5xx
data = response.json()["iss_position"]
print(data["latitude"], data["longitude"])
```

---

### Summary Checklist

1. An API is a service you *call* to get data you cannot produce yourself.
2. `requests.get(endpoint, params={...})` → check the status → `response.json()`.
3. Endpoint = *where* the data lives; parameters = *which* data you want.
4. ISS notifier = ISS position + sunrise/sunset at your coordinates + email.
