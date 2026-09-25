# Reproduce the Bug

---

### 1. Tip #2: Reproduce the Bug Reliably

A bug you can trigger **on demand** is a bug you can fix. If it only appears sometimes,
find the exact conditions — the input, the state, the order of actions — that produce it.

```python
import random

def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    # BUG: missing else — odd numbers fall through and return None sometimes
```

* Run it many times with different inputs.
* Find the **smallest input** that still breaks it.
* Once reproducible, your fix can be verified immediately.

---

### 2. Why "It Works on My Machine" Isn't Enough

Intermittent bugs suggest you haven't understood the cause yet — maybe it's an unhandled
branch, an off-by-one at a boundary, or a random value you assumed away. Reproduction turns
a mystery into a test case.

---

### Summary Checklist

1. Can't reproduce = can't verify the fix.
2. Hunt for the minimal failing input.
3. Random behaviour in bugs usually means an uncovered branch or boundary.
