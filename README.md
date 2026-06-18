# SentiNews Backend

Production-ready backend powering the SentiNews platform.

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy 2.0 (Async)
- Alembic
- Redis
- Docker
- JWT Authentication
- Google Gemini
- TwelveData
- News API
- Yahoo Finance

---

## Architecture

```text
Client
    │
    ▼
FastAPI Routers
    │
    ▼
Services
    │
    ▼
Repositories
    │
    ▼
PostgreSQL
```

---

## Project Structure

```text
src/
api/
core/
db/
repositories/
services/
schemas/
integrations/
utils/
```

---

## Setup

### Clone

```bash
git clone <repo>
cd backend
```

### Create Environment

```bash
cp .env.example .env
```

### Start Docker

```bash
docker compose up --build
```

---

## API Docs

Swagger

```
http://localhost:8000/docs
```

Redoc

```
http://localhost:8000/redoc
```

---

## Development

```bash
uvicorn src.main:app --reload
```

---

## Code Quality

```bash
black .
ruff check .
isort .
mypy .
```

---

## Testing

```bash
pytest
```

---

## License

MIT