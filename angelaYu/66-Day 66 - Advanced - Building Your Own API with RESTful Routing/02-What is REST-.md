Here is a structured breakdown of this lesson on what REST is.

---

### 1. REST = REpresentational State Transfer

Not a framework or a library — an **architectural style** for building APIs on top of the
classic client–server model that the whole internet runs on.

---

### 2. The Restaurant Analogy

| Internet | Restaurant |
|----------|-----------|
| Client | the customer ordering |
| Server | the waiter/kitchen |
| Request | "I'd like a pizza please" |
| Valid request → response | the pizza arrives |
| Invalid request → `404` | "we don't have sausages" |
| HTTP | the language you order in |
| HTTPS | ordering in code (encrypted) |

If the kitchen doesn't speak your language, or the dish isn't on the menu, you don't get
served — that's what status codes tell you.

---

### 3. HTTP Is the Language

* **HTTP** — HyperText Transfer Protocol: the request/response format all web servers speak.
* **HTTPS** — HTTP *Secure*: the same request encrypted, so nobody can read your card
  details or passwords in transit.
* Other protocols exist (**FTP** for files) but HTTP(S) is the web's standard.

---

### 4. What the Server Does With a Request

1. Checks the request is valid (otherwise a status code like `404`).
2. Produces the response, either by:
   * **computation** — running code (a calculator app), or
   * **fetching from a database** — pulling the requested records, or
   * both.
3. Sends the result back — HTML, images, or (for APIs) JSON.

---

### 5. REST's Rules of Thumb

| Rule | Meaning |
|------|---------|
| Resources have URLs | `/cafes`, `/cafes/2` |
| Verbs do the work | `GET` read, `POST` create, `PUT`/`PATCH` update, `DELETE` remove |
| Statelessness | each request carries everything needed; the server keeps no session state |
| Representation | the resource is sent as JSON/XML/HTML — a *representation* of its state |
| Status codes | the result's meaning, machine-readable |

> **Note:** "Stateless" is why a REST API can be scaled horizontally — any server can
> answer any request, because nothing is remembered between calls.

---

### Summary Checklist

1. REST is an architectural style, not a technology.
2. Client asks, server answers, HTTP is the language, codes are the grammar.
3. Servers compute, query a database, or both.
4. Resources + verbs + statelessness + JSON = a RESTful API.
