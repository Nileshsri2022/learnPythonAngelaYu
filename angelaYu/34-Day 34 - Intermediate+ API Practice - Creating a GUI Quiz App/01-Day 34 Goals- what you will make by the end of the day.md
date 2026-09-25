# Day 34 Goals: what you will make by the end of the day

Day 34 is **review with a purpose**: the API skills from Day 33 are rebuilt from
scratch inside a Tkinter app called **Quizzler**.

---

### 1. The App

* Questions come from the **Open Trivia Database** — 3,000+ verified trivia
  questions, which is why you don't have to write any yourself.
* One **True/False** question is shown at a time; ✔ True / ✘ False buttons.
* A **score counter** updates after every answer.

```text
Score: 1
Q.2: The vapor produced by e-cigarettes is water.   [ True ]  [ False ]
```

---

### 2. What It Reviews

| From Day 33 | Reused here |
|-------------|-------------|
| API **endpoints** | `https://opentdb.com/api.php` — the trivia endpoint |
| API **parameters** | `amount=10`, `type=boolean`, `category=…` — how many and what kind of questions |
| HTTP response handling | Checking the response, reading the JSON |
| JSON → Python | `response.json()["results"]` is a **list of dictionaries** |

New on top of it: **classes** to hold a question (`Question`) and the quiz logic
(`QuizBrain`), so the GUI only worries about drawing.

```python
parameters = {"amount": 10, "type": "boolean"}
response = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]
```

---

### Summary Checklist

1. Quizzler = Open Trivia DB + Tkinter GUI + score tracking.
2. Parameters shape the data (`amount`, `type`, `category`).
3. The JSON payload nests a **list of question dictionaries** — index and key it.
4. Separate the *data/logic* (`QuizBrain`) from the *UI* (Tkinter).
