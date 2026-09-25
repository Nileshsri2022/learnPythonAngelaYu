# Day 66 Goals- Build Your Own REST API Service

---

### 1. From Consuming APIs to Building One

Days 32–40 were about *using* other people's APIs (OpenWeather, Twilio, Sheety…). Now you
build your own: a **RESTful API** for a database of cafes.

Clients will be able to:

| Want | HTTP method | Endpoint |
|------|-------------|----------|
| a random cafe | `GET` | `/random` |
| every cafe | `GET` | `/all` |
| cafes in a location | `GET` | `/search?location=London` |
| add a new cafe | `POST` | `/add` |
| update the coffee price | `PATCH` | `/update-price/<cafe_id>` |
| close a cafe down | `DELETE` | `/report-closed/<cafe_id>` |

---

### 2. Why RESTful?

**REST** = *REpresentational State Transfer*. It's a convention for designing APIs around
**resources** (here: cafes) and the standard HTTP verbs, so any client — a website, a
mobile app, `requests`, Postman, another server — knows what to expect without reading a
manual.

---

### 3. The Stack

| Piece | Role |
|-------|------|
| Flask | routes and request handling |
| SQLite + SQLAlchemy | the cafe database |
| Postman | an API testing client |
| JSON | the response format |

---

### 4. The Shape of a Response

```json
{
  "cafe": {
    "id": 2,
    "name": "Cafe Mocha",
    "map_url": "https://goo.gl/maps/…",
    "img_url": "https://…jpg",
    "location": "London",
    "seats": "20",
    "has_toilet": true,
    "has_wifi": true,
    "has_sockets": true,
    "can_take_calls": false,
    "coffee_price": "£3.10"
  }
}
```

Status codes matter as much as the body: `200` OK, `201` created, `404` not found,
`400` bad request, `403` forbidden.

---

### Summary Checklist

1. Today: build, test and document your own REST API for cafes.
2. REST = resources + standard HTTP verbs + status codes + JSON.
3. Endpoints: random, all, search, add, update-price, report-closed.
4. Stack: Flask + SQLAlchemy/SQLite, tested with Postman.
