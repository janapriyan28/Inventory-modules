# Inventory ERP

Small inventory system: item & warehouse masters, stock in / stock out, current stock, low-stock alerts and CSV export.

**Stack:** FastAPI · SQLAlchemy 2 · Alembic · PostgreSQL | Next.js 15 (App Router) · TypeScript · Tailwind CSS · TanStack Query

## Quick start (Docker)
```bash
cp .env.example .env
make up          # builds and starts db, backend, frontend
make migrate     # applies Alembic migrations
```
- Frontend: http://localhost:3000
- API docs: http://localhost:8000/docs

## Run without Docker
```bash
# backend (uses SQLite by default if DATABASE_URL is not set)
cd backend && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload

# frontend
cd frontend && cp .env.local.example .env.local
npm install && npm run dev
```

## Tests
```bash
make test        # or: cd backend && pytest
```

See `docs/` for architecture, schema, API and business rules.
