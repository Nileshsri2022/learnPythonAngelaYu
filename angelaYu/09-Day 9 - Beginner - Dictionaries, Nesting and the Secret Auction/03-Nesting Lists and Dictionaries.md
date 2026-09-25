Here is a structured breakdown of everything covered in this lesson on nesting lists and dictionaries.

---

### 1. What is Nesting?

If a list or dictionary is like a **folder**, nesting is putting folders *inside* folders.
Any combination is legal:

```python
# List inside a dictionary (key → list)
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Dictionary inside a dictionary (key → dict)
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Dictionary inside a list (each item is a dict)
travel_log = [
    {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
]
```

The last form — **a list of dictionaries** — is the workhorse: it's how you store many
records of the same shape (like rows in a table).

---

### 2. Retrieving Nested Data

Chain the lookups from the outside in:

```python
print(travel_log[0]["cities_visited"][1])   # Lille
#            ^item  ^key            ^inner item
```

---

### 3. Adding to Nested Structures

```python
travel_log.append({"country": "Italy", "cities_visited": ["Rome"], "total_visits": 3})
travel_log["France"]["total_visits"] = 13     # edit deep inside
```

---

### Summary Checklist

1. Nesting = collections inside collections; any mix of lists and dicts.
2. **List of dictionaries** = the standard way to store multiple records.
3. Access nested data by chaining `[index]["key"][index]`.
