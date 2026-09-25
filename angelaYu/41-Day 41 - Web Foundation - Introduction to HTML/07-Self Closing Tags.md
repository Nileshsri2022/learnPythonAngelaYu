# Self Closing Tags

---

### 1. Void Elements

Some elements have **no content**, so they need no closing tag:

```html
<hr>     <!-- horizontal rule: a thematic break line -->
<br>     <!-- line break inside text -->
```

```html
<p>
    The butterfly is <em>inside</em> the chrysalis...<br>
    — attributed to Ovid
</p>
<hr>
```

* `<br>` forces a new line (e.g. in an address or a poem).
* `<hr>` separates sections visually.

---

### 2. Why They Have No Closing Tag

A closing tag exists to say *"my content ends here"* — with no content, there's nothing
to close. `img`, `input`, `meta` and `link` (met later) are void elements too.

> **Tip:** In HTML5, `<br>` and `<br/>` are both legal; plain `<br>` is conventional.

---

### Summary Checklist

1. Content-less elements = no closing tag.
2. `hr` = break between sections; `br` = break within text.
