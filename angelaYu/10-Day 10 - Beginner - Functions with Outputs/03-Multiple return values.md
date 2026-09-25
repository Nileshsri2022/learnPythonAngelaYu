# Multiple return values

A function can contain several `return` statements — but **only the first one that
runs** does anything, because `return` ends the function immediately.

---

### 1. `return` Is the End of the Function

```python
def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"
    print("this line is never reached")     # dead code — after return
```

Any code after a `return` inside the same block is unreachable. The moment the
computer meets `return`, it exits the function.

---

### 2. Several `return`s, in Different Branches

You *can* have many `return` keywords — one per branch:

```python
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."      # early exit
    return f"Result: {f_name.title()} {l_name.title()}"  # normal path
```

When the function is called with inputs, only one of these lines executes.

---

### 3. Guarding Against Empty Input

Put it together with `input()` and the problem becomes obvious:

```python
print(format_name(input("What is your first name? "),
                  input("What is your last name? ")))
```

* Leave both blank **without** the guard → `.title()` runs on empty strings and you
  get a meaningless `Result: ` line.
* With the guard → the function exits early with a message that tells the caller what
  went wrong.

> **Note:** an empty `return` (just the keyword) is also legal: the function ends and
> the caller receives `None`, which prints as `None`. Returning a **message** is
> usually friendlier than returning nothing — it says what went wrong.

---

### Summary Checklist

1. `return` immediately ends the function; later lines in that block never run.
2. Multiple `return` statements are fine — one per branch, only one executes.
3. Use an **early return** to escape invalid input before doing real work.
4. A bare `return` gives back `None`; a message (`"You didn't provide valid inputs."`)
   is more useful to whoever calls the function.
5. The pattern generalises: validate → exit early, otherwise → main logic.
