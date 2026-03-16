# Implementation Progress

## Scaffolded ✅

- `pyproject.toml` — project packaging and tooling config
- `.gitignore`, `.env.example`
- `docker-compose.yml` — local dev environment (app + postgres)
- `alembic.ini` — migration tooling wiring
- `README.md`, `AGENTS.md`, `IMPLEMENTATION_PROGRESS.md`
- `.github/copilot-instructions.md`

### App Package

- `app/main.py` — FastAPI application factory, health routes registered
- `app/api/routes_health.py` — `/healthz` and `/readyz` implemented
- `app/api/routes_verify.py` — stub (501): `POST /verify`
- `app/api/routes_inventory.py` — stubs (501): `GET /inventory`, `POST /inventory/refresh`
- `app/api/routes_requests.py` — stubs (501): `GET /requests`, `GET /requests/{request_id}`
- `app/api/routes_verdicts.py` — stubs (501): `GET /verdicts`, `GET /verdicts/{verdict_id}`
- `app/api/deps.py` — dependency injection stubs
- `app/api/auth.py` — auth dependency stub
- `app/config/settings.py` — Pydantic Settings model
- `app/config/logging.py` — structlog configuration
- `app/config/auth.py` — auth config stub
- `app/contracts/` — Pydantic v2 request/response schemas
- `app/db/base.py` — SQLAlchemy `DeclarativeBase`
- `app/db/session.py` — session factory
- `app/db/models/` — all model placeholders with initial columns
- `app/db/repositories/` — repository interface stubs
- `app/adapters/` — adapter module boundaries (CrowdStrike, F5, probes)
- `app/domain/` — domain module boundaries
- `app/services/` — service stubs
- `app/workers/verify_job.py` — worker stub
- `app/metrics/registry.py` — Prometheus metrics stub
- `app/utils/` — utility modules (time, net, hashing, redact)
- `app/cli/main.py` — Typer CLI entrypoint
- `alembic/env.py`, `alembic/script.py.mako`
- `schemas/` — JSON Schema files
- `docs/` — architecture, threat model, operations, verdicts, api, event-schemas, ai/
- `tests/unit/` — contract, settings, health, reason_codes tests
- `tests/integration/` — stub integration tests
- `tests/fixtures/` — JSON fixtures
- `scripts/` — dev.sh, lint.sh, test.sh

## Not Yet Implemented ❌

- Real F5 BIG-IP API client (`app/adapters/f5/client.py`)
- Real CrowdStrike callback client (`app/adapters/crowdstrike/callback_client.py`)
- Real probe execution (`app/adapters/probes/`)
- Full policy engine (`app/domain/policy_engine.py`)
- Full verdict engine (`app/domain/verdict_engine.py`)
- Async job processing (`app/workers/`)
- Production authentication hardening
- Database migrations (Alembic versions)
- Redis integration
- Full verify flow (`POST /api/v1/verify`)
- Inventory sync (`app/adapters/f5/inventory_sync.py`)
- Callback delivery (`app/services/callback_service.py`)
