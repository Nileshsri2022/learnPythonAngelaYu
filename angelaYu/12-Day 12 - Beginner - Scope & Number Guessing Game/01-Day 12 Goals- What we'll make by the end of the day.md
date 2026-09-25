Here is a structured breakdown of the Day 12 goals and the project you'll have built by the end of the day.

---

### 1. Skills Covered on Day 12

* **Scope** — where a variable exists and can be seen
* **Local vs. global namespaces**
* Block scope (and why Python doesn't have it)
* Modifying global variables — and why to avoid it
* **Global constants** — the good kind of global

---

### 2. The End-of-Day Project: Number Guessing Game

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again: 25
You got it! The answer was 25.
```

* **Easy** = 10 attempts, **Hard** = 5 attempts.
* The game loops, tracking attempts remaining — and scope rules decide where each
  variable lives.

This is the first project you build **entirely from scratch** — no starter code.

---

### Summary Checklist

1. Scope answers: *where can this variable be seen, and how long does it live?*
2. Function = local scope; top level = global scope.
3. You'll use constants (ATTEMPTS) correctly and never need `global`.
