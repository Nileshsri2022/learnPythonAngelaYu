# How to Iterate over a Pandas DataFrame

---

### 1. DataFrame From a Dict

```python
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 32],
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)
```

---

### 2. Three Ways to Loop It

```python
# 1. Loop the column (a Series)
for (key, value) in student_data_frame.items():
    print(value)

# 2. Loop the rows — the recommended way
for (index, row) in student_data_frame.iterrows():
    print(row.student)      # attribute access on the row
    print(row.score)

# 3. Row as a dict-like record
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)     # 56
```

`iterrows()` yields `(index, Series)` pairs — each `row` is a Series whose labels are the
column names, so `row.column_name` just works.

---

### Summary Checklist

1. `.items()` iterates columns; `.iterrows()` iterates rows.
2. Each row is a Series — access columns as attributes.
3. `for (i, row) in df.iterrows():` is the idiom to memorise.
