Here is a structured breakdown of this lesson on type hints and arrows.

---

### 1. The Syntax

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

age: int = 25                  # variable annotation
scores: list[float] = [9.0, 8.5]
```

* **Parameter hint:** `name: str` — colon after the name.
* **Return hint:** `-> str` — arrow before the colon ending the signature.
* Hints are **not enforced** at runtime — `greet(5)` still runs — they are documentation
  that editors, linters and type checkers (mypy) use.

---

### 2. Why Bother in Python?

Dynamic typing (Day 28) trades safety for speed; hints give the safety back:

* Autocomplete knows what methods exist on a parameter.
* Bugs like passing a string into `count - 1` are flagged *before* running.
* Function signatures become self-documenting.

```python
def check_answer(self, user_answer: str, correct_answer: str) -> bool:
```

reads instantly — no docstring needed to know what goes in and out.

---

### Summary Checklist

1. `param: type` in, `-> type` out.
2. Hints = documentation + editor checks, not runtime enforcement.
3. Annotate public functions first — that's where readers live.
