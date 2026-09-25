# Challenge: Check if it Will Rain in the Next 12 Hours

The umbrella decision only depends on the next 12 hours — so stop downloading
five days of weather and ask for exactly what you need.

---

### 1. Ask for Less Data: `cnt`

The free OpenWeatherMap forecast has 40 entries, one every 3 hours. Twelve hours is
the **first four** entries, and the API can send only those:

```python
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,               # the "count" parameter → next 4 slots = 12 hours
}
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()          # raise instead of silently continuing on 4xx/5xx
weather_data = response.json()
```

> Run the script at 06:00 and the four slots cover 06:00 → 18:00: your whole trip
> away from home. This is why you read the API docs — the `cnt` parameter saves
> bandwidth and code.

---

### 2. Decode the Weather: Condition Codes

Each entry's `weather` field is a **list** of conditions (you can have snow *and*
fog), and the first item is the main one. Every condition has an **id**:

| Code starts with | Weather |
|------------------|---------|
| 2xx | Thunderstorm |
| 3xx | Drizzle |
| 5xx | Rain |
| 6xx | Snow |
| 7xx | Atmosphere — mist, smoke, dust, fog |

So "is precipitation coming?" becomes: **is any `id` in the next four slots `< 700`?**

```python
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:        # JSON gives it as a string → convert
        will_rain = True

if will_rain:
    print("Bring an umbrella ☔")
```

Using a flag means one message instead of one per rainy slot.

---

### 3. Tips for Testing

* `weather_data["list"][0]["weather"][0]["id"]` — drill down level by level, or paste
  the JSON into an online **JSON viewer** to see the shape.
* Want guaranteed rain for a test? Pick a currently-soaked city from
  **ventusky.com** (precipitation layer), e.g. Łódź, Poland, and use its coordinates
  from latlong.net.

---

### Summary Checklist

1. Only the first **4** of the 40 forecast slots matter: the next 12 hours.
2. `cnt=4` requests just those; `raise_for_status()` turns errors into exceptions.
3. `weather` is a list; use its first item's `id`.
4. Any code **< 700** means precipitation → bring an umbrella.
5. Set a `will_rain` flag in the loop and act once after it — not once per hit.
6. Test against a location that is actually raining right now.
