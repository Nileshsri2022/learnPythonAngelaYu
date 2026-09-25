Here is a structured breakdown of this practice lesson on object attributes and methods.

---

### 1. Practising on a PrettyTable Object

The exercise: given a table of Pokémon, set the alignment by **modifying the attribute**
and add data by **calling the methods**:

```python
from prettytable import PrettyTable

table = PrettyTable()

# Calling methods — add a column at a time
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Modifying an attribute — note: no parentheses, and the value is a string
table.align = "l"

print(table)
```

---

### 2. The Difference in Practice

| You want to… | Syntax | Example |
|--------------|--------|---------|
| Read/replace state | `object.attribute = value` | `table.align = "l"` |
| Perform an action | `object.method(args)` | `table.add_column(...)` |

A method call **does** something (often changing state); an assignment just **sets** state.

> **Tip:** When exploring an unfamiliar object, `dir(obj)` lists every attribute and
> method it has — your first stop with any new library.

---

### Summary Checklist

1. Set attributes directly; call methods with parentheses.
2. `dir(obj)` reveals an object's capabilities.
3. Library objects are used exactly like the ones you build yourself.
