# Random Module

---

### 1. Why Computers Need Help Being Random

Computers are **deterministic** — they repeat actions in a fully predictable way. True
randomness (splashed paint, TV static) doesn't exist inside them, so Python uses a
**pseudo-random number generator** (the *Mersenne Twister* algorithm) to produce numbers
that are unpredictable enough for games and simulations.

To use it, **import the module** at the top of your file:

```python
import random
```

---

### 2. `random.randint(a, b)` — Random Integer

A random whole number **between a and b, inclusive of both ends**:

```python
import random

random_number = random.randint(0, 1)   # 0 or 1 (coin flip)
print(random.randint(1, 10))           # any of 1…10
```

> **Warning:** Both bounds are **included** — `randint(0, 10)` can return 10. This
> differs from many other languages and is a classic source of bugs.

---

### 3. `random.random()` — Random Float Between 0 and 1

```python
print(random.random())   # e.g. 0.7364918… (never quite 1.0)
```

Scale it to any range by multiplying:

```python
random_float = random.random() * 5   # 0.0 up to (but not including) 5.0
```

And `random.uniform(a, b)` gives a float in **any** range:

```python
print(random.uniform(5, 10))   # e.g. 7.234…
```

---

### 4. Heads or Tails Challenge

```python
import random

coin = random.randint(0, 1)
if coin == 0:
    print("Heads")
else:
    print("Tails")
```

---

### Summary Checklist

1. `import random` first — modules are libraries of extra functionality.
2. `randint(a, b)` → random int **including both bounds**.
3. `random()` → float in `0 ≤ x < 1`; multiply to scale, `uniform(a, b)` for any range.
