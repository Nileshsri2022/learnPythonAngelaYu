# Unescaping HTML Entities

---

### 1. The Problem

APIs often return text safe for HTML display: `'` for `'`, `"` for `"`,
`&` for `&`. Printing that raw looks like gibberish.

---

### 2. The Fix — `html.unescape()`

```python
import html

question_text = html.unescape(question["question"])
```

Applied where the bank is built:

```python
for question in question_data:
    question_text = html.unescape(question["question"])
    question_bank.append(Question(question_text, question["correct_answer"]))
```

**Output before:** `"Southern Cross" is the name of the UK's flag.`
**Output after:** `"Southern Cross" is the name of the UK's flag.`

> **Tip:** Decode at the data boundary (in `data.py`/the bank loop) so every downstream
> component sees clean text.

---

### Summary Checklist

1. HTML entities are escaped characters from web-safe transport.
2. `html.unescape()` converts them back to real characters.
3. Clean data at the boundary, not in every consumer.
