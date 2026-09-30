# Architecture

**Backend** (FastAPI) uses a layered design; each layer only talks to the one below it:

`api/` (HTTP, validation) → `services/` (business rules) → `repositories/` (SQLAlchemy queries) → `models/` (tables)

- `schemas/` – Pydantic request/response models
- `core/` – settings, DB session, error types and handlers
- `utils/csv_export.py` – builds the CSV for the current-stock export
- `migrations/` – Alembic revisions 001–004

**Frontend** (Next.js App Router) – pages in `src/app`, feature components in `src/components/<feature>`,
generic UI in `components/ui`, data access through TanStack Query hooks in `src/hooks`, single fetch wrapper in `lib/api.ts`.

Current stock is **derived**, not stored: total stock-in minus total stock-out per (item, warehouse).
