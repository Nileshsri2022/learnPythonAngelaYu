Here is a structured breakdown of the pixel-adding challenge.

---

### 1. The Task

POST a quantity to today's date on your graph — one pixel per day of the habit.

---

### 2. The Solution

```python
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

pixel_data = {
    "date": "20260925",     # YYYYMMDD
    "quantity": "6.5",      # hours coded today
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(pixel_response.text)
```

* The date format is strict `YYYYMMDD`; quantity is a **string**.
* Posting to an existing date overwrites it (a whole pixel history in one endpoint).

---

### Summary Checklist

1. `POST /users/<user>/graphs/<id>` with `date` + `quantity`.
2. Daily runs build the chart automatically.
