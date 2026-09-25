Here is a structured breakdown of this lesson on constructing objects and accessing attributes and methods.

---

### 1. Attributes vs. Methods

```python
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy.color())        # attribute access: object.attribute
timmy.forward(100)          # method call: object.method()

my_screen = Screen()
print(my_screen.canvwidth)  # e.g. 704
my_screen.exitonclick()
```

* **Attributes** — variables attached to an object → no parentheses (`timmy.color`,
  `my_screen.canvwidth`).
* **Methods** — actions attached to an object → parentheses (`timmy.forward(100)`).

> **Note:** Mixing these up is the most common beginner OOP error — if calling it errors
> with "object is not callable" or prints something odd, check whether it's an attribute.

---

### 2. The Dot Notation

`object.thing` — Python looks up `thing` on that object: first its attributes, then its
class's methods. The same dot notation you've used on strings and lists all along
(`"a".upper()`, `nums.append()`) — those were objects too.

---

### Summary Checklist

1. Attribute = state, no parentheses; method = action, with parentheses.
2. Dot notation walks from the object to its data/behaviour.
3. Everything you've called methods on is already an object.
