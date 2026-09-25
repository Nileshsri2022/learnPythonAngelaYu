# How to Open, Read, and Write to Files using the -with- Keyword

---

### 1. Reading a File

```python
with open("my_file.txt") as file:
    contents = file.read()
print(contents)
```

---

### 2. Writing and Appending

```python
with open("my_file.txt", mode="w") as file:   # write — REPLACES everything
    file.write("New text!")

with open("my_file.txt", mode="a") as file:   # append — adds at the end
    file.write("\nAnother line")
```

| Mode | Meaning | If file missing |
|------|---------|-----------------|
| `"r"` (default) | read | **error** |
| `"w"` | write (overwrite from scratch) | creates it |
| `"a"` | append to the end | creates it |

---

### 3. Why `with`?

`with` **closes the file automatically** when the block ends — even if an error occurs.
The old way required remembering `file.close()` yourself; forgetting it risks corrupted
or locked files.

> **Warning:** `"w"` mode obliterates the existing content the moment it opens. When you
> mean "add", use `"a"`.

---

### Summary Checklist

1. `open(path, mode)` + `read()` / `write()`.
2. `with` block = guaranteed close, no housekeeping.
3. `r` reads, `w` replaces, `a` appends.
