# How to Modify a Global Variable

---

### 1. The Trap

You *can* change a global from inside a function — but by default you shouldn't, because
the assignment silently creates a local instead (last lesson). Python's escape hatch is
the `global` keyword:

```python
enemies = 1

def increase_enemies():
    global enemies        # "I mean the global one"
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()        # enemies inside function: 2
print(f"enemies outside function: {enemies}")   # enemies outside function: 2
```

---

### 2. Why This Is Discouraged

Any function can now change `enemies` from anywhere — after a bug appears, *every* function
is a suspect. Recommended instead — **pass data in and out**:

```python
enemies = 1

def increase_enemies(current_enemies):
    return current_enemies + 1

enemies = increase_enemies(enemies)
```

* The function stays **self-contained** and testable.
* Data flow is visible at the call site.

> **Note:** There are legitimate cases (like a game-over flag), but prefer parameters and
> returns — they scale to bigger programs.

---

### Summary Checklist

1. `global name` inside a function re-binds the global — possible, but risky.
2. Default behaviour (assignment = local) is safer for you.
3. **Parameters + return values beat `global`** in almost every situation.
