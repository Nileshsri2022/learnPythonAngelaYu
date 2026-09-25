Here is a structured breakdown of this lesson on debugging — starting with describing the problem.

---

### 1. What is Debugging?

**Debugging** is the process of finding and removing bugs — the mistakes every programmer
inevitably makes. Debugging isn't an occasional chore; it's a *core programming skill*.

---

### 2. Tip #1: Describe the Problem Precisely

Before touching code, write down (in a comment or on paper) **exactly** what's wrong:

```python
# def my_sum(a, b):
#     return a + b
# BUG: my_sum(1, 2) should be 3 — but it returns 12 when called with strings
```

The discipline of describing forces you to answer:

* What did you **expect** to happen?
* What **actually** happened?
* Under **which inputs** does it fail?

> **Tip:** Rubber-duck debugging — explain the bug out loud to an inanimate object.
> Saying it precisely often reveals the cause before the duck answers.

---

### Summary Checklist

1. Bugs are normal; debugging is a *skill to practise*, not an interruption.
2. Describe the problem in one precise sentence before fixing anything.
3. Expected vs. actual vs. inputs — the three questions.
