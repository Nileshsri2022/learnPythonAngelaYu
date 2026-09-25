# API Endpoints and Making API Calls

---

### 1. Endpoints

An **endpoint** is an API's address — a URL that returns data:

```text
http://api.open-notify.org/iss-now.json
```

---

### 2. Calling It with `requests`

```python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()          # stop on 4xx/5xx errors

data = response.json()
print(data)
# {'message': 'success', 'iss_position': {'latitude': '-38.2938', 'longitude': '131.8432'},
#  'timestamp': 1691642400}

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
```

* `.json()` parses the JSON response body into Python dicts/lists.
* `raise_for_status()` turns bad HTTP statuses into exceptions — Day 30's pattern
  applied to networking.

---

### Summary Checklist

1. Endpoint = URL serving data (often ending in `.json`).
2. `requests.get()` → `.raise_for_status()` → `.json()`.
3. JSON nests like your dicts — chain the keys.
