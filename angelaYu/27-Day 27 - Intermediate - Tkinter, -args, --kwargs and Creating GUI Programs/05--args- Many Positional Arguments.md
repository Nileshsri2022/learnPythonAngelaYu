Here is a structured breakdown of this lesson on `*args`.

---

### 1. Functions with Unlimited Arguments

```python
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

add(1, 2, 3)          # 6
add(1, 2, 3, 4, 5)    # 15
```

The `*` before the parameter name collects **all extra positional arguments into a tuple**
inside the function. The name `args` is convention, the star is the magic.

---

### 2. Details

```python
def with_others(a, b, *args):
    print(a, b, args)

with_others(1, 2, 3, 4, 5)    # 1 2  (3, 4, 5)
```

* Regular parameters first, `*args` catches the rest.
* Inside, `args` is an ordinary tuple — index it, loop it, slice it.

This is exactly how Python's own `print("a", "b", "c", sep=", ")` accepts anything.

---

### Summary Checklist

1. `*args` = variable-length positional input, packed into a tuple.
2. Loop it like any sequence.
3. The `*` is the syntax; the name is convention.
