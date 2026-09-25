# Step 2 - Download the Starting Project

---

### 1. What's New vs. Part 1

```text
main.py                  — now also loads users and emails them
data_manager.py          — get_destination_data() AND get_customer_emails()
flight_search.py         — search for both direct and 1-stop flights
flight_data.py           — plus find_cheapest_flight() helper
notification_manager.py  — send_sms() AND send_emails()
```

---

### 2. The Users Data

```python
def get_customer_emails(self):
    customers_endpoint = f"{self.sheety_pr_end_point}/users"
    response = requests.get(url=customers_endpoint, headers=self._headers)
    response.raise_for_status()
    return response.json()["users"]
    # [{"firstName": "Nilesh", "lastName": "S", "email": "n@example.com"}, ...]
```

A second GET on a second tab — the multi-table pattern from Day 9 (lists of dicts).

---

### Summary Checklist

1. Same classes, more responsibilities — read the TODOs in order.
2. Users arrive as a list of dicts, ready to loop.
