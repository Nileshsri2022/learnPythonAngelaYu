Here is a structured breakdown of the Highest Score coding exercise and its solution.

---

### 1. The Task

Given a list of student exam scores, find the **highest score** — *without* using the
built-in `max()` function. Only `for` loops and basic logic are allowed.

```python
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
```

---

### 2. The Building Block: Accumulating in a Loop

Python's `sum()` totals a list for you — but it's just a loop in disguise. You can rebuild
it yourself with an **accumulator** variable that starts at 0 and collects values:

```python
total = 0
for score in student_scores:
    total += score        # add each score to the running total
print(total)              # same result as sum(student_scores)
```

---

### 3. The Solution: `max()` by Hand

For the *highest score*, the accumulator starts at 0 and **keeps whichever value is bigger**:

```python
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
```

* Each pass asks: *is this score bigger than the best so far?*
* If yes, it becomes the new best. After the loop, `highest_score` holds the maximum —
  exactly what `max(student_scores)` would return.

---

### Summary Checklist

1. **Accumulator pattern:** create a variable before the loop, update it inside the loop.
2. `sum()`-style: `total += score`.
3. `max()`-style: `if score > best: best = score`.
4. Built-ins like `sum()` and `max()` are just loops you could write yourself.
