# Nesting Lists and Dictionaries

If a list or dictionary is a **folder**, nesting is putting folders *inside* folders.
Any combination is legal — and it is how you model more complex, real data.

---

### 1. A List as a Value

Each key can hold only one value — so to store several cities for one country, make that
value a **list**:

```python
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
```

---

### 2. Getting Data Out of a Nested List

Chain the lookups, outside in — first the dictionary key, then the list index:

```python
print(travel_log["France"])            # ['Paris', 'Lille', 'Dijon']
print(travel_log["France"][1])         # Lille
```

`travel_log["France"]` *is* the list, so the second pair of square brackets indexes it.

---

### 3. A List Inside a List (a 2D list)

The same idea works for lists within lists:

```python
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2])          # ['C', 'D']
print(nested_list[2][1])       # D
```

---

### 4. A Dictionary Inside a Dictionary

Values can be dictionaries too — useful when one record has several fields:

```python
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],
               "num_times_visited": 8},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"]},
}
```

Note the shape: `travel_log` → country → dictionary → list.

```python
print(travel_log["Germany"])                        # the inner dictionary
print(travel_log["Germany"]["cities_visited"])      # the list of cities
print(travel_log["Germany"]["cities_visited"][2])   # Stuttgart
```

---

### 5. Adding to Nested Structures

Dictionaries are mutable at any depth, and you can add new entries at the top level:

```python
travel_log["France"]["num_times_visited"] = 9               # edit deep inside

travel_log["Italy"] = [{"cities_visited": ["Rome"],
                        "total_visits": 3}]                 # new country
```

---

### Summary Checklist

1. Nesting = collections inside collections; any mix of lists and dictionaries.
2. Access nested data by chaining, outside in: `[key]` then `[index]` then `[key]`…
3. A **list inside a list** is a 2D list — index it twice: `nested_list[2][1]`.
4. A **dictionary inside a dictionary** models records with several fields.
5. Typos in nested keys are the usual bug — copy the key instead of retyping it.
