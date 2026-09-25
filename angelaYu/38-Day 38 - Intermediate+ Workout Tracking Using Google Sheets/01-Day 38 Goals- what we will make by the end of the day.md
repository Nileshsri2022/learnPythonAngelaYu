# Day 38 Goals- what we will make by the end of the day

---

### 1. Skills Covered on Day 38

* **Natural-language APIs** — POST *"ran 5k and cycled 20 minutes"* and get parsed data
* **Sheety** — turning a Google Sheet into a REST API
* **Header-based authentication** for both services
* Environment variables for all credentials

---

### 2. The Project

```text
Tell me which exercises you did: ran 5k and cycled 20 minutes
```

1. The text goes to the **NutritionIX** exercise API, which parses it into
   `{exercise, duration, calories}` per activity.
2. Each activity is POSTed as a row into your **Google Sheet** via Sheety:

| Date | Time | Exercise | Duration | Calories |
|------|------|----------|----------|----------|
| 2026-09-25 | 10:03 | Running | 25 | 310 |

---

### Summary Checklist

1. Plain English in → structured rows in a spreadsheet.
2. Two APIs, two authentications, one pipeline.
