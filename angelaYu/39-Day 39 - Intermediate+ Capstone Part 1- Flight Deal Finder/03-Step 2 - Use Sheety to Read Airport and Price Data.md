Here is a structured breakdown of Step 2 — reading destinations via Sheety.

---

### 1. GET the Sheet

```python
class DataManager:
    def __init__(self):
        self.sheet_token = os.environ.get("SHEET_TOKEN")
        self.sheet_endpoint = os.environ.get("SHEET_ENDPOINT")
        self.destination_data = self.get_data()

    def get_data(self):
        headers = {"Authorization": f"Bearer {self.sheet_token}"}
        response = requests.get(url=self.sheet_endpoint, headers=headers)
        response.raise_for_status()
        return response.json()["prices"]
        # [{"city": "Paris", "iataCode": "CDG", "lowestPrice": 55000, "id": 2}, ...]
```

* Day 37/38 taught POST and PUT to Sheety; now **GET** reads the destinations.
* The `prices` tab becomes a list of dicts — one per city.

---

### 2. Why Data-Driven Matters

Adding a destination = adding a sheet row. No code changes, no redeploys — the sheet is
the app's configuration.

---

### Summary Checklist

1. `requests.get` + Bearer header → destination rows as JSON.
2. Configuration lives in the sheet, not the code.
