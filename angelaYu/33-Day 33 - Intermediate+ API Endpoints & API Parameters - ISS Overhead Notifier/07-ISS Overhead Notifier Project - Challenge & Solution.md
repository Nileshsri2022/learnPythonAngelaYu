# ISS Overhead Notifier Project - Challenge & Solution

---

### 1. The Logic

Email me when **both** are true:

1. The ISS is within ±5° of my position.
2. It's currently dark (after sunset, before sunrise).

---

### 2. The Solution

```python
import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 26.8467     # Lucknow
MY_LONG = 80.9462
my_email = "your@gmail.com"
password = "app_password"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])
    return (MY_LAT - 5 <= iss_lat <= MY_LAT + 5
            and MY_LONG - 5 <= iss_long <= MY_LONG + 5)

def is_night():
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    results = response.json()["results"]
    sunrise = int(results["sunrise"].split("T")[1].split(":")[0])
    sunset = int(results["sunset"].split("T")[1].split(":")[0])
    hour_now = datetime.now().hour
    return hour_now >= sunset or hour_now <= sunrise

while True:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:Look Up 👆\n\nThe ISS is above you in the sky!")
    time.sleep(60)
```

* Two helper functions return Booleans; the `while True` polls every minute — the
  composition of everything since Day 5.

---

### Summary Checklist

1. Overhead check = position within a ±5° bounding box.
2. Darkness check = current hour vs. sunset/sunrise.
3. Runnable version: [`main.py`](main.py)
