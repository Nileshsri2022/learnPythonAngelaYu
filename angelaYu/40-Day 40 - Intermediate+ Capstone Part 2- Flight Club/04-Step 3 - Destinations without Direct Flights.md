Here is a structured breakdown of Step 3 — handling destinations without direct flights.

---

### 1. The Problem

Some routes have no direct flight — the search returns nothing and the destination is
silently skipped. The upgrade: search **1-stop routes** too.

```python
def search_flight(self, origin, destination, via=None):
    params = {
        "engine": "google_flights",
        "departure_id": origin,
        "arrival_id": destination,
        ...
    }
```

* Search the direct route; if no offers come back, search again with a routing
  parameter that allows stop-overs.
* The cheapest result wins, whether direct or 1-stop — the deal logic never changes.

---

### 2. Filling Missing IATA Codes

The same class also gained `get_iata_code(city_name)` — querying the flight API to
convert a city name into its IATA code and PUT-ing it back into the sheet with
`data_manager.update_iata_code()` (Day 37's PUT!).

---

### Summary Checklist

1. No results ≠ skip — retry with stop-overs allowed.
2. Sheet rows self-heal: missing IATA codes get filled back via PUT.
