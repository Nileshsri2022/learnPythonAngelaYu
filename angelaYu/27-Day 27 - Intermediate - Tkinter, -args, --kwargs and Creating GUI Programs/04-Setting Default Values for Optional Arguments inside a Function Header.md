Here is a structured breakdown of this lesson on default argument values.

---

### 1. Optional Parameters

Give a parameter a default; the argument becomes optional:

```python
def greet(name="friend", emoji="👋"):
    print(f"Hello {name} {emoji}")

greet()               # Hello friend 👋
greet("Angela")       # Hello Angela 👋
greet("Angela", "🚀") # Hello Angela 🚀
```

* Defaults must come **after** non-default parameters.
* Defaults make functions friendlier — the 90% case needs no arguments
  (that's why `Label(text=...)` needs nothing else to work).

---

### 2. Where You've Seen It

Tkinter is built on this: `window.minsize(width=500, height=300)`,
`Label(text="hi", font=("Arial", 24))`, `turtle.color("coral")` — every one is an
optional keyword argument with a default.

---

### Summary Checklist

1. `def f(a, b=2):` — b optional.
2. Defaults = API ergonomics; callers override only what they need.
