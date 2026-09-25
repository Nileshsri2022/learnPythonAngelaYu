# Code Exercise- Exception Handling in the NATO Phonetic Alphabet Project

---

### 1. The Problem (from Day 26)

```python
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
```

Type `"abroad 12!"` → `KeyError: '1'` — the program crashes on non-letters.

---

### 2. Three Possible Fixes

```python
# Option 1: try/except around the whole comprehension
try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet, please.")

# Option 2: filter first, then translate
output_list = [phonetic_dict[letter]
               for letter in word if letter in phonetic_dict]

# Option 3: validate with a loop and warn
```

All three are legitimate. The course's chosen pattern:

```python
word = input("Enter a word: ").upper()

try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet, please.")
else:
    print(output_list)
```

* `try` wraps the risky translation; `else` prints only on success.
* The user gets a friendly message instead of a traceback.

---

### Summary Checklist

1. Identify the crash line, wrap *it* — not the whole program.
2. `try`/`except`/`else` converts crashes into user feedback.
