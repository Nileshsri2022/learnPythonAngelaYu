Here is a structured breakdown of Step 2 — natural-language exercise queries.

---

### 1. The Query

```python
exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 172.5,
    "age": 30,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
```

POST *"ran 5k and cycled 20 minutes"* and NutritionIX returns parsed exercises:

```json
{"exercises": [
  {"name": "running", "duration_min": 25.0, "nf_calories": 310.4},
  {"name": "cycling", "duration_min": 20.0, "nf_calories": 187.2}
]}
```

---

### 2. Looping the Results

```python
for exercise in result["exercises"]:
    print(exercise["name"], exercise["duration_min"], exercise["nf_calories"])
```

---

### Summary Checklist

1. Natural language → structured exercise records (NLP as a service).
2. `for exercise in result["exercises"]:` handles any number of activities.
