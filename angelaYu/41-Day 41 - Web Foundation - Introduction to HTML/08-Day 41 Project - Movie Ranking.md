Here is a structured breakdown of the Day 41 project — Movie Ranking.

---

### 1. The Task

A single HTML page ranking your top three movies, using only headings, paragraphs, `hr`
and `em`/`strong`:

```
<h1>The Best Movies According to Nilesh</h1>
<p>All-time favourite movies, ranked.</p>
<hr>
<h2>Fall Guy</h2>
<p>... description ...</p>
<hr>
<h2>Upgraded</h2>
...
```

---

### 2. The Solution

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Movie Ranking Project</title>
</head>
<body>
    <h1>The Best Movies According to Nilesh</h1>
    <p>All-time favourite movies, ranked from best to not-quite-best.</p>
    <hr>
    <h2>Fall Guy</h2>
    <p>A stuntman is mistaken for the star he doubles for. Escalates
    <strong>gloriously</strong>.</p>
    <hr>
    <h2>Upgraded</h2>
    <p>An artist fakes a promotion and improvises her way through high society.</p>
    <hr>
    <h2>Anyone But You</h2>
    <p>Two exes must survive a wedding together. Physics involved.</p>
</body>
</html>
```

* `<strong>` (bold) and `<em>` (italic) mark *emphasis* inside paragraphs.

---

### Summary Checklist

1. Headings for the outline, `p` for content, `hr` between movies.
2. Runnable version: [`movie_ranking.html`](movie_ranking.html)
