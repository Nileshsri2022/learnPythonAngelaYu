Here is a structured breakdown of Step 4 — parsing flight data.

---

### 1. Digging Into Nested JSON

Flight APIs return deeply nested structures — select the offers and pick the cheapest:

```python
class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest(data):
    offers = data.get("best_flights") or data.get("other_flights") or []
    cheapest = None
    for offer in offers:
        flight = offer["flights"][0]
        price = offer["price"]
        if cheapest is None or price < cheapest.price:
            cheapest = FlightData(
                price=price,
                origin_airport=flight["departure_airport"]["id"],
                destination_airport=flight["arrival_airport"]["id"],
                out_date=flight["departure_airport"]["time"][:10],
                return_date=offer["layovers"] and offer["flights"][-1]["departure_airport"]["time"][:10],
            )
    return cheapest
```

* `.get()` with defaults survives API responses missing sections (Day 30/34 patterns).
* The `FlightData` object normalises messy API JSON into one clean shape.

---

### Summary Checklist

1. Walk the nesting with `.get()` guards, not blind indexes.
2. Model one offer as one small class.
