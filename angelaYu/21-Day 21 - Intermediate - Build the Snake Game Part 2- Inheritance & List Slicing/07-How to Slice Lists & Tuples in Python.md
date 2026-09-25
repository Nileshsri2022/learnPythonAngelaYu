Here is a structured breakdown of this lesson on slicing lists and tuples.

---

### 1. Slice Syntax

Slicing extracts a sub-sequence with `sequence[start:end]` — **end excluded**:

```python
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

piano_keys[2:5]     # ["c", "d", "e"]
piano_keys[2:]      # ["c", "d", "e", "f", "g"]  — to the end
piano_keys[:5]      # ["a", "b", "c", "d", "e"]  — from the start
piano_keys[::2]     # ["a", "c", "e", "g"]       — every 2nd (step)
piano_keys[::-1]    # reversed copy!
```

Works identically on tuples and strings.

---

### 2. Applying It to the Snake

Instead of skipping the head inside the loop, slice it away:

```python
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        scoreboard.game_over()
        game_is_on = False
```

`segments[1:]` = "everything except the first element" — the wordy skip-check gone.

---

### Summary Checklist

1. `[start:end:step]`, end excluded; any part may be omitted.
2. `[::-1]` reverses; `[1:]` drops the head.
3. Slicing replaces manual index bookkeeping with intent.
