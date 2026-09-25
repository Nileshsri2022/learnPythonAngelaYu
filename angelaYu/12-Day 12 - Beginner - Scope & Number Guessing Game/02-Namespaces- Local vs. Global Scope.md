# Namespaces- Local vs. Global Scope

---

### 1. What is Scope?

**Scope** determines where a variable can be *seen* and how long it *lives*:

* **Global scope** — created at the top level of the file; visible everywhere, lives for
  the whole program.
* **Local scope** — created inside a function; visible *only* inside it, dies when the
  function ends.

```python
enemies = 1                       # global

def increase_enemies():
    potion = 2                    # local
    enemies = 2                   # a NEW local variable — not the global one!
    print(f"enemies inside function: {enemies}")

increase_enemies()                # enemies inside function: 2
print(f"enemies outside function: {enemies}")   # enemies outside function: 1
```

The assignment inside the function created a **second, unrelated** `enemies` that vanished
when the function returned — the global one was never touched.

---

### 2. Namespaces

A **namespace** is the "container" of names Python searches when it meets a variable:

1. First the **local** namespace (this function)
2. Then the **global** namespace (the file)
3. Then built-ins (`print`, `random`, …)

That's why a function can *read* a global — but assigning creates a local shadow instead.

---

### Summary Checklist

1. Function = its own local namespace, destroyed on return.
2. Assigning to a name inside a function creates a **local** variable, even if a global
   with the same name exists.
3. Local → global → built-ins is the lookup order.
