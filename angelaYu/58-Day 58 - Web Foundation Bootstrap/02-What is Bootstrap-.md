Here is a structured breakdown of this lesson on what Bootstrap is.

---

### 1. A CSS Framework

**Bootstrap** (2010, Mark Otto + Jacob Thornton, open-source) is a collection of
pre-written CSS files. Include them, add the right classes, and you get pre-styled
components and a responsive 12-column layout system — no CSS written by you.

```html
<button class="btn btn-success">Ok</button>
```

An unstyled `<button>` becomes a rounded, green, hover-animated button.

---

### 2. Frameworks vs Your Own CSS

Bootstrap does **not** replace what you learned. Usage across the web:

| Approach | Share |
|----------|-------|
| Bootstrap | ~80 % of framework users |
| Other frameworks (Foundation, Tailwind, MUI…) | the rest |
| **No framework at all** | the single largest group |

Plenty of sites still use hand-written Flexbox/Grid — and you can read them all now.

---

### 3. Pros and Cons

| ✅ Pros | ❌ Cons |
|--------|--------|
| Fast to build with | **Class bloat** — lots of style in the HTML |
| Huge library of components | Blurs the structure/style separation |
| Consistent, professional look | Customising every pixel takes effort |
| Tested cross-browser | Everything looks "Bootstrap-y" by default |

**Use it when:** you need a mobile-first responsive site quickly and want professional,
uniform components.

**Skip it when:** the site is trivially simple, or the design must be completely custom.

---

### 4. How to Include It (CDN)

**Content Delivery Network**: the CSS is served from a nearby hub, so it loads fast
wherever your user is.

```html
<head>
    <!-- 1. styling -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
          rel="stylesheet">
</head>
<body>
    …

    <!-- 2. JavaScript behaviour (dropdowns, mobile menu) — before </body> -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
```

> **⚠️ Warning:** Forget the second file and everything *looks* fine but nothing *works* —
> dropdowns and the hamburger menu stay dead. You'll meet this on the TinDog project.

---

### Summary Checklist

1. Bootstrap = pre-written CSS + components + responsive grid.
2. ~80 % of framework users use Bootstrap, but most sites use no framework.
3. Pros: speed, components, consistency. Cons: class bloat, customisation cost.
4. Add the CSS in `<head>`, the JS bundle before `</body>`.
5. Know plain CSS — the framework is optional, your fundamentals aren't.
