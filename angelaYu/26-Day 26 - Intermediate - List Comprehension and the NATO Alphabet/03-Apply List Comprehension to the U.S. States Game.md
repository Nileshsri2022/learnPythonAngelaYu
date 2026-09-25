Here is a structured breakdown of this lesson applying comprehensions to the U.S. States Game.

---

### 1. Squishing Yesterday's Code

The missing-states line from Day 25:

```python
missing_states = []
for state in all_states:
    if state not in guessed_states:
        missing_states.append(state)
```

becomes a one-liner:

```python
missing_states = [state for state in all_states if state not in guessed_states]
```

Same result, 4 lines → 1, and arguably *more* readable once you know the idiom.

---

### 2. Other Uses in the Game

```python
all_states = data.state.to_list()                  # already one line
guessed = [s for s in all_states if s in guessed_states]   # filter doubles
```

The lesson's point: comprehensions aren't just syntax sugar — they let the *intent*
(read this collection into that one) sit on one line.

---

### Summary Checklist

1. Rewrite loop-append blocks as comprehensions.
2. `not in` filtering is a comprehension classic.
