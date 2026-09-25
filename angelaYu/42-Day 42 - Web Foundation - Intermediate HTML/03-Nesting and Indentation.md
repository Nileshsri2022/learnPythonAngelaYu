Here is a structured breakdown of this lesson on nesting and indentation.

---

### 1. Elements Inside Elements

```html
<ul>
    <li>Macros
        <ul>
            <li>Protein</li>
            <li>Carbs</li>
            <li>Fats</li>
        </ul>
    </li>
    <li>Vitamins</li>
</ul>
```

* A child element lives entirely inside its parent's opening and closing tags.
* Indenting each level isn't decoration — it's how humans read the tree.

---

### 2. The Rules

* Close tags in reverse order of opening — last opened, first closed.
* Mis-nesting (`<b><i>text</b></i>`) produces unpredictable DOM; browsers will try to
  repair it, inconsistently.

> Python's indentation (Day 6) trained you for exactly this — same tree, same discipline.

---

### Summary Checklist

1. Nesting = the DOM tree; indentation shows it.
2. Clean nesting = predictable rendering.
