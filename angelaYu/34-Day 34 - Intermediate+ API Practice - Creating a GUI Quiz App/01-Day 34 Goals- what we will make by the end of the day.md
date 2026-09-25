Here is a structured breakdown of the Day 34 goals — the Quizzler GUI quiz app.

---

### 1. Skills Covered on Day 34

* **Consuming the Open Trivia DB API** — fetching real quiz questions
* **Unescaping HTML entities** (`&#039;` → `'`) with `html.unescape()`
* **Class-based Tkinter UI** — wrapping the whole interface in a class
* **Type hints** — `parameter: type` and `-> return_type`
* Wiring API → engine → GUI with callbacks

---

### 2. The Project: Quizzler

```
[Score: 0]
┌──────────────────────┐
│  Question text here  │   ← card canvas
└──────────────────────┘
   [✘ False]      [✔ True]
```

* 10 true/false questions fetched live from opentdb.com.
* True/False buttons check the answer, flash the card green/red, update the score.
* At quiz end: "You've finished!" and the buttons disable.

---

### Summary Checklist

1. Day 17's console quiz upgraded to a GUI with live API data.
2. New ideas: entity unescaping, class-based UI, type hints.
