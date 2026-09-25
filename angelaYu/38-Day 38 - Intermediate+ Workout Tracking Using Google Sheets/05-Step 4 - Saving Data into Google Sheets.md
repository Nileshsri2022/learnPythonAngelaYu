Here is a structured breakdown of Step 4 — saving data into the sheet.

---

### 1. Posting Each Exercise

```python
from datetime import datetime

today = datetime.now()
date_now = today.strftime("%d/%m/%Y")
time_now = today.strftime("%X")          # 10:03:22

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
print(sheet_response.text)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)
```

* One POST per exercise — multiple activities become multiple rows.
* `strftime` fills date and time automatically (Day 37).

---

### Summary Checklist

1. Parse (NutritionIX) → shape (dict) → POST (Sheety) → row in the sheet.
