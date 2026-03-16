# Repository Map

Quick reference for AI agents navigating this codebase.

## Key Entry Points

- `app/main.py` — FastAPI application factory
- `app/config/settings.py` — all configuration
- `app/contracts/` — all external I/O schemas
- `app/domain/reason_codes.py` — verdict/reason code enum

## Module Purposes

| Path | Purpose |
|------|---------|
| `app/api/` | FastAPI route handlers |
| `app/contracts/` | Pydantic v2 I/O schemas |
| `app/db/` | SQLAlchemy models + repositories |
| `app/adapters/` | External integrations |
| `app/domain/` | Pure business logic |
| `app/services/` | Orchestration |
| `app/workers/` | Background job hooks |
| `app/utils/` | Stateless utilities |
| `alembic/` | Database migrations |
| `schemas/` | JSON Schema definitions |
| `tests/` | Test suite |

## What Is Implemented

See `IMPLEMENTATION_PROGRESS.md`.
