Here is a structured breakdown of Step 5 — checking every destination.

---

### 1. The Loop

```python
data_manager = DataManager()
flight_search = FlightSearch()

for destination in data_manager.destination_data:
    city = destination["city"]
    code = destination["iataCode"]
    target = destination["lowestPrice"]

    flight = flight_search.search_flight(ORIGIN, code)
    cheapest = find_cheapest(flight)

    if cheapest and cheapest.price < target:
        notification_manager.send_sms(
            f"Low price alert! Only ₹{cheapest.price} to fly "
            f"from {ORIGIN} to {code}, "
            f"out {cheapest.out_date} and back {cheapest.return_date}."
        )
```

* One API call per row — the sheet drives the whole run.
* `if cheapest and …` guards against destinations with no results.

---

### Summary Checklist

1. Loop destinations → search → compare against the target price.
2. The cheapest-under-target condition is the entire business logic.
