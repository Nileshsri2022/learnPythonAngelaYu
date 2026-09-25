Here is a structured breakdown of this lesson on catching exceptions.

---

### 1. The Four Keywords

```python
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])          # works
except FileNotFoundError:
    file = open("a_file.txt", "w")      # handle the missing file
    a_dictionary["missing"]             # would raise KeyError — not caught here
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    contents = file.read()              # runs ONLY if try succeeded
finally:
    file.close()                        # ALWAYS runs — success or failure
    print("done")
```

| Block | Runs when |
|-------|-----------|
| `try` | always (the risky code) |
| `except SpecificError` | that exception occurs |
| `else` | the `try` block raised **nothing** |
| `finally` | unconditionally (cleanup) |

---

### 2. The Rules

* Catch **specific** exceptions by name — bare `except:` hides bugs.
* `as error_message` captures the exception's payload for logging.
* Execution never returns to a failed `try` block; the rest of it is skipped.

---

### Summary Checklist

1. `try` = attempt; `except` = rescue; `else` = success path; `finally` = cleanup.
2. Name the exceptions you expect — one `except` per type.
3. `finally` guarantees close/cleanup semantics.
