Here is a structured breakdown of this lesson on tuples and random RGB colours.

---

### 1. Tuples

A **tuple** is an ordered collection that — unlike a list — **cannot change** after
creation (immutable):

```python
my_tuple = (1, 3, 8)
my_tuple[0]        # 1 — indexing works like lists
my_tuple[0] = 5    # TypeError: 'tuple' object does not support item assignment
```

* Syntax: parentheses (vs. list square brackets).
* Use a tuple when the data *shouldn't* change — coordinates, RGB colours, dates.

---

### 2. Random RGB Colours

Turtle accepts colours as RGB triples in 0–1 range after `colormode(255)`:

```python
import random
import turtle

turtle.colormode(255)               # accept 0-255 RGB values

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)                # a tuple

timmy.color(random_color())
```

---

### Summary Checklist

1. Tuple = immutable list — `(r, g, b)`.
2. Immutability protects data that must stay constant.
3. `colormode(255)` + a tuple-returning function = any colour in the spectrum.
