# While Loops

---

### 1. The Robot Charger Analogy

A robot told **"while you have electricity, keep moving forwards"** will move until the
plug is pulled. That's a `while` loop: **repeat as long as a condition is true** — it
doesn't need to know in advance how many times it will run.

---

### 2. The Two Flavours of Loop

```python
# for loop #1 — once per item of a list
for item in fruits:
    print(item)

# for loop #2 — once per number of a range
for n in range(6):
    print(n)

# while loop — repeat while condition holds
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
```

---

### 3. Rewriting Hurdle 1 with a `while` Loop

```python
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
```

Each pass jumps one hurdle and **decrements** the counter; when the counter reaches 0 the
condition is `False` and the loop ends.

---

### 4. When to Use Which?

| Situation | Loop of choice |
|-----------|----------------|
| Known number of items/repetitions | `for` |
| Repeat until *something becomes true/false* | `while` |

> **Warning:** If the condition **never becomes False**, you get an **infinite loop** —
> the program never ends. Make sure something inside the loop can change the condition.

---

### Summary Checklist

1. `while condition:` repeats **while** the condition stays `True`.
2. Counter + `-=` converts a "do N times" problem into a `while` loop.
3. `for` = counted; `while` = conditional. Pick the one that matches the problem.
