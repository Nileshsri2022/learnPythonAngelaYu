Here is a structured breakdown of Step 1 — API credentials and the spreadsheet.

---

### 1. NutritionIX

1. Create a developer account at nutritionix.com.
2. Note your **APP ID** and **API Key** — both travel in request headers:

```python
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
```

---

### 2. The Google Sheet

1. Create a sheet named e.g. `MyWorkouts`, with a tab `workouts`.
2. Add headers: `Date | Time | Exercise | Duration | Calories`.
3. Note the sheet ID from its URL — Sheety will use it.

---

### Summary Checklist

1. Two credentials (header pair) for NutritionIX.
2. The sheet's *tab name* becomes the API's resource name.
