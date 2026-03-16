# Operations

## Health Checks

| Endpoint | Description |
|----------|-------------|
| GET /healthz | Liveness — process is running |
| GET /readyz | Readiness — database is reachable |

## Configuration

All configuration via environment variables. See `.env.example`.

## Database Migrations

```bash
# Apply all pending migrations
f5-verifier db-upgrade

# Or directly via alembic
alembic upgrade head
```

## Logging

Structured JSON logging via structlog. Set `APP_LOG_LEVEL` to control verbosity.

## Metrics

Prometheus metrics exposed at `/metrics` (not yet implemented).
