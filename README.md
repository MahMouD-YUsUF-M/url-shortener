# URL Shortener — MVP

A minimal, container-ready URL shortening service built with **FastAPI**. This README documents what has been completed,
what is in-progress, how to run the project for development, and the roadmap to complete the MVP.

---

## 🚀 Project Goal

Build a simple, secure URL shortening service for **anonymous users** that converts long URLs into short, shareable
links and provides basic metadata and click-tracking.

### MVP core features

* Shorten HTTP/HTTPS URLs into 8 character codes
* Redirect short codes to original URLs
* URL expiration after 30 days
* Show basic metadata (original URL, created date, clicks)
* Basic validation, HTTPS enforcement, and rate-limiting

---

## ✅ What I have completed (Done)

This section lists the project work that is implemented and currently available in the repository.

### System & project structure

* Project layout created under `src/`:

  * `appurlshort/` — FastAPI app: routers, middleware, error handlers
  * `liburlshort/` — Domain logic (services, entities, models)
  * `libutil/` — Utilities (DB session helpers, small utils)
  * `dev-env/` — Docker Compose and helper script `dev-env/dev.sh`
* Dockerfile and `docker-compose.yml` added for containerized local development

### Database & models

* SQLAlchemy models & schema helpers in `src/liburlshort/data/models/tables.py`
* Schema creation helpers for local dev (dev-only helpers available)

### Domain logic

* Encapsulated business logic inside `liburlshort/domain`:

  * `AddUrl` — create a new short URL, validate inputs, check collisions
  * `GetUrls` — list URLs for a guest (filters out expired)
  * `GetTargetUrl` — find the original target URL for redirect
* URL codes: 8-character alphanumeric strings (A–Z, a–z, 0–9) with collision-check and retry limit
* Target URL validation: requires `http` or `https` scheme; max length approx. 2000 chars

### FastAPI endpoints (working)

* `POST /v1/urls` — Create a short URL (body: `{ "target_url": "https://example.com" }`)
* `GET  /v1/urls` — List all *active* (unexpired) URLs for the guest
* `GET  /v1/{url_code}` — Redirect to the original URL (returns a 302/307 redirect)
* Global middleware and error handlers present to return consistent JSON responses
* Header contract enforced: `X-Guest-Code` required for anonymous user scoping

### Dev tooling & tests

* `dev-env/dev.sh` helper created for:

  * `./dev-env/dev.sh up` (start app + services)
  * `./dev-env/dev.sh up --env` (start app only, use services in dev-env)
  * `./dev-env/dev.sh t` (run tests)
* Test skeletons and pytest config added (some domain tests exist)

### Docs & examples

* API design doc included in repository describing endpoints & example responses
* Example responses and error shapes standardized in API handlers

---

## 🔧 In-progress / TODO

Work being actively implemented or planned next. (Status and owner notes optional.)

### High priority

* **Rate limiting** (10 requests/min per IP) — middleware integration and tests (in progress)
* **Click tracking** — increment `number_of_clicks` atomically on each redirect (in progress)
* **Accurate expiry enforcement** — background cleanup job or DB TTL enforcement (in design)

### Medium priority

* **Comprehensive tests** — expand unit tests and add integration tests for endpoints
* **Hardening validation** — stricter validation against malicious payloads and open redirects
* **HTTPS enforcement on redirects** — force `https://` for target URLs where possible

### Lower priority / future improvements

* Guest deduplication and quota per guest
* Admin endpoints for debugging / manual cleanup
* Analytics UI (clicks over time, geo, referrers)
* Custom slugs for users who want branded short codes

---

## 📦 How to run (local / dev)

> Assumes Docker (and Docker Compose) installed and running.

1. From project root start app + dev services:

```bash
./dev-env/dev.sh up
```

2. Start app only (use services from `dev-env/docker-compose.yml`):

```bash
./dev-env/dev.sh up --env
```

3. Run tests:

```bash
./dev-env/dev.sh t
# or inside container
./dev-env/dev.sh exec pytest
```

Troubleshooting:

* If `get_container_name` errors, ensure Docker daemon is running.
* If ports conflict, inspect `docker-compose.yml`.

---

## 🧩 API Reference (short)

**Header** (required for all requests)

```
X-Guest-Code: <guest-unique-id>
```

### Create short URL

```
POST /v1/urls
Body: { "target_url": "https://example.com/path" }
Response: { success: true, message: "Url added successfully!", data: { short_url: "https://short.url/aB3d9Z" } }
```

### List URLs for guest

```
GET /v1/urls
Response: { data: { urls: [ { short_url, target_url, created_at, expires_at, number_of_clicks } ] } }
```

### Redirect

```
GET /v1/{url_code}
- Returns HTTP 302/307 with Location set to target URL
- If expired / not found -> JSON error with code 400/404
```

---

## 🔒 Security & Reliability

* Input validation to accept only http(s) URLs and enforce max length
* Collision-checked code generation with retry limit
* Basic sanitization to prevent injection vectors
* Rate limiting (10 req/min per IP) — middleware in-progress
* Error handling and consistent JSON error shapes

---

## 🗂 Database schema (summary)

Main table: `urls`

* `id` (pk)
* `url_code` (unique)
* `target_url`
* `guest_code`
* `created_at`
* `expires_at`
* `number_of_clicks`

Indexes:

* unique index on `url_code`
* index on `guest_code` + `expires_at`

---

## ✅ Code checklist (what's implemented)

* [x] Project scaffolding, routers, middleware
* [x] SQLAlchemy models & local schema helpers
* [x] Domain services for Add/Get/Redirect
* [x] FastAPI endpoints for create/list/redirect
* [x] `X-Guest-Code` header support
* [x] Dev helper script `dev-env/dev.sh`

## ⚙️ Roadmap (MVP phases)

* **Phase 1**: System design, DB schema, API design, project structure — *done*
* **Phase 2**: Shortening + redirection — *done*
* **Phase 3**: Rate limiting + robust error handling — *in progress*
* **Phase 4**: Click tracking + URL information display — *in progress*
* **Phase 5**: Tests + deployment — *in progress*

---

## 📝 Example curl commands

Create:

```bash
curl -X POST http://localhost:8000/v1/urls \
  -H "Content-Type: application/json" \
  -H "X-Guest-Code: guest-123" \
  -d '{"target_url": "https://example.com/path"}'
```

List:

```bash
curl -H "X-Guest-Code: guest-123" http://localhost:8000/v1/urls
```

Redirect (visit in browser or curl to follow redirect):

```bash
curl -I http://localhost:8000/v1/aB3d9Z
```

---
