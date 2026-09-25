Here is a structured breakdown of this lesson on API parameters.

---

### 1. What Parameters Are

Parameters are the *order details* — extras appended to the endpoint that customise the
response. The Sunrise-Sunset API takes lat/long:

```python
import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise, sunset)
```

* `params=` — requests appends `?lat=51.5&lng=-0.12&formatted=0` for you.
* String slicing carves the hour out of ISO timestamps like `2026-09-25T05:42:19`.

---

### 2. Comparing With the Current Time

```python
time_now = datetime.now()
```

If `sunrise < current_hour < sunset` it's daytime — the exact check the ISS notifier
needs (email only while it's **dark** enough to see the station).

---

### Summary Checklist

1. Parameters = `?key=value&...`, built via the `params` dict.
2. Parse timestamps with `.split("T")`.
3. Sunrise/sunset vs. current hour = darkness check.
