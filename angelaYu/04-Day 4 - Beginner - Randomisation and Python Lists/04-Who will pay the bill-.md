Here is a structured breakdown of the "Who will pay the bill?" coding exercise and its solutions.

---

### 1. The Task

The "banker's Russian roulette": everyone puts a business card in a bowl and whoever's card
is drawn **pays the whole bill**. Your program must print **one random name** from a list
of friends — a different name each time you run it.

```python
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
```

---

### 2. Solution 1 — `random.choice()`

The cleanest way: hand the list to Python and let it pick.

```python
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends) + " is going to buy the meal today!")
```

---

### 3. Solution 2 — `randint()` + Indexing

Do it manually: generate a random index within the list's range, then subscript the list.

```python
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_index = random.randint(0, len(friends) - 1)
print(friends[random_index] + " is going to buy the meal today!")
```

> **Warning:** The index must go up to `len(friends) - 1`, because indexes start at 0 —
> `len()` of a 5-item list is 5, but the last index is 4. Getting this wrong is the
> classic **off-by-one error** (see next lesson).

---

### Summary Checklist

1. `random.choice(list)` — one-liner for "pick a random item".
2. `randint(0, len(list) - 1)` + `list[index]` — the manual equivalent.
3. Remember why the `-1` is there: **offsets start at 0**.
