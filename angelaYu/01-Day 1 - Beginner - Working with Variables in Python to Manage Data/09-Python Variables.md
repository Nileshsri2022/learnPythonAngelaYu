# Python Variables

---

### 1. Why Variables Exist

After `input()` receives the user's text, the data just **disappears** — there's no way to
refer to it again. A **variable** solves this: it's a *name* you attach to a piece of data so
you can use it later.

Think of a **phone book**: a bare phone number is useless unless you write a name next to it.
The name is the variable; the number is the data.

```python
james = "07700900461"
```

Now the number can be retrieved any time just by using the name `james`.

---

### 2. Creating a Variable

Write a name, an equals sign, then the data — this **assigns** the data to the name:

```python
name = input("What is your name?")
print(name)
```

Whatever the user typed is now stored in `name` and can be printed or used anywhere later in the code.

---

### 3. Variables Can Change (They Vary!)

A variable can be reassigned to new data at any time:

```python
name = "Jack"
print(name)      # Jack

name = "Angela"
print(name)      # Angela
```

Each assignment **overwrites** the previous value — the variable holds only the most recent one.

---

### 4. Variable vs. String: Order Matters

```python
print("name")    # prints the literal text:  name
print(name)      # prints the value stored in the variable, e.g. Jack
```

With **quotes** you get the word itself; **without** quotes Python looks up the variable.

---

### 5. Using Variables to Build Outputs

Variables can be combined with strings via concatenation:

```python
name = "Angela"
print("Hello " + name)   # Hello Angela
```

---

### Summary Checklist

1. A **variable** is a name attached to a piece of data, created with `=`.
2. Use it later simply by writing its name (no quotes).
3. Reassigning overwrites the old value.
4. `"name"` (quotes) = literal text; `name` (no quotes) = the variable's value.
