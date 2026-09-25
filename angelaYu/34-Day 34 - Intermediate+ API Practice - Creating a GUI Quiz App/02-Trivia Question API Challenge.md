Here is a structured breakdown of this lesson on the Trivia API challenge.

---

### 1. The Task

`data.py` must fetch 10 true/false questions from the **Open Trivia Database**:

```
https://opentdb.com/api.php?amount=10&type=boolean
```

and shape them into `question_data` for the rest of the app.

---

### 2. The Solution

```python
import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
```

* The `params` dict builds the query string (`?amount=10&type=boolean`) — Day 33.
* Each result: `{"category": ..., "question": ..., "correct_answer": "True"/"False", ...}`.

---

### Summary Checklist

1. Endpoint + parameters → GET → `.json()["results"]`.
2. Every run produces a *different* quiz — the data is now live.
