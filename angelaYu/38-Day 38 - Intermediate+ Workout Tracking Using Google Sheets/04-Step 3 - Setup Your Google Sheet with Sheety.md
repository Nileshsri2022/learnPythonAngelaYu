Here is a structured breakdown of Step 3 — Sheety setup.

---

### 1. What Sheety Does

[Sheety](https://sheety.co) turns any Google Sheet into a JSON REST API:

```
GET    https://api.sheety.co/<username>/myWorkouts/workouts    # read rows
POST   https://api.sheety.co/<username>/myWorkouts/workouts    # add a row
PUT    …/workouts/<rowId>                                       # update a row
DELETE …/workouts/<rowId>                                       # delete a row
```

* The **project name** (`myWorkouts`) and **tab name** (`workouts`) become the URL.
* Row names come from the sheet's header row.

---

### 2. Row Shape

A POST body mirrors the headers (lower-cased):

```json
{
  "workout": {
    "date": "2026-09-25",
    "time": "10:03:00",
    "exercise": "Running",
    "duration": "25",
    "calories": "310"
  }
}
```

---

### Summary Checklist

1. Sheet → REST API; headers → field names.
2. Same CRUD verbs you learned on Day 37.
