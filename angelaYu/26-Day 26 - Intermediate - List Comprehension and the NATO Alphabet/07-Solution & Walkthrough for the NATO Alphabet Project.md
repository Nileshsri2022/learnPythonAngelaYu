Here is a structured walkthrough of the NATO Alphabet solution.

---

### 1. The Solution

```python
import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1: dictionary comprehension {letter: code}
phonetic_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(phonetic_dict)

# TODO 2: ask for a word
word = input("Enter a word: ").upper()

# TODO 3: list comprehension over the word's letters
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
```

**Output for `abroad`:**
```
['Alfa', 'Bravo', 'Romeo', 'Oscar', 'Alfa', 'Delta']
```

---

### 2. The Pieces

1. `iterrows()` (previous lesson) supplies `row.letter` and `row.code` to build the dict.
2. `.upper()` normalises the input against the all-caps keys.
3. A string iterates like a list of characters — so the comprehension walks the word,
   and the dict turns each letter into its code.

> **Note:** An unknown character (space, digit) raises a `KeyError` — Day 30's
> exception-handling revisit fixes exactly that.

---

### Summary Checklist

1. Dict comprehension over `iterrows()` builds the lookup.
2. List comprehension over the word's characters does the translation.
3. Runnable version: [`main.py`](main.py) (needs `nato_phonetic_alphabet.csv`)
