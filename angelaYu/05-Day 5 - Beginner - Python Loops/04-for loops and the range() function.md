Here is a structured breakdown of everything covered in this lesson on `for` loops and the `range()` function.

---

### 1. The Gauss Story

Aged ten, mathematician Carl Gauss was told to add every number from 1 to 100. He spotted
50 pairs that each sum to 101 — `1+100`, `2+99`, `3+98`… — and answered **5050** in two
minutes. We can outshine Gauss with a few lines of code, looping over a **range** of numbers.

---

### 2. Looping Without a List: `range()`

So far loops always iterated over a list. `range()` generates a sequence of numbers to loop
over instead:

```python
for number in range(1, 101):
    print(number)
```

* The loop runs for `1, 2, 3, …, 100`.
* `range(a, b)` **includes `a` but excludes `b`** — exactly like list indexes.

---

### 3. Solving Gauss's Problem

```python
total = 0
for number in range(1, 101):
    total += number
print(total)   # 5050
```

---

### 4. Things to Know About `range()`

* It's lazy — `print(range(1, 10))` just prints `range(1, 10)`; feed it to a loop (or
  `list()`) to see the numbers.
* With **one** argument, it starts from 0: `range(6)` → `0, 1, 2, 3, 4, 5`.

```python
for n in range(1, 11, 3):   # step by 3
    print(n)                # 1, 4, 7, 10
```

* A third argument is the **step** (even negative steps count *down*).

> **Warning:** The classic `range` gotcha: to loop up to and including 100 you must
> write `range(1, 101)` — the stop value is never included.

---

### Summary Checklist

1. `for x in range(a, b):` loops the numbers `a` up to (not including) `b`.
2. Add everything with the accumulator pattern: `total += number`.
3. `range(stop)`, `range(start, stop)` or `range(start, stop, step)`.
4. Stop value is **excluded** — `range(1, 101)` for 1–100.
