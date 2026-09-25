# CSS Selectors

---

### 1. Selecting Elements

```css
h2 { }              /* tag — every <h2> */

.fancy { }          /* class — every element with class="fancy" */
#main-title { }     /* id — the single element with id="main-title" */

* { }               /* universal — everything */
```

```html
<h2 id="main-title">Title</h2>
<p class="fancy">Styled paragraph</p>
```

| Selector | Symbol | Matches |
|----------|--------|---------|
| tag | none | all of that element |
| class | `.` | all with that class (reusable) |
| id | `#` | the one with that id (unique) |

---

### 2. Combining Selectors

```css
p.fancy { }              /* <p> elements that ALSO have class fancy */
.fancy h2 { }            /* <h2> anywhere INSIDE an element of class fancy */
```

* No space = both conditions on one element.
* Space = descendant relationship.

---

### 3. Pseudo-classes

```css
a:hover {          /* when the mouse is over it */
    color: orange;
}
```

---

### Summary Checklist

1. Tag, `.class`, `#id` — the three daily selectors.
2. Compound (no space) vs descendant (space).
3. `:hover` reacts to the user.
