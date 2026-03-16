# f5-exposure-verifier

A bounded external exposure verification and enrichment service for CrowdStrike/F5-driven workflows.

## Purpose

This service receives suspicious inbound exposure events from upstream workflow tooling, classifies the target against approved F5 inventory, performs tightly bounded outside-in verification, and returns a structured verdict plus evidence.

## Status

**Scaffold only.** Core business logic is not yet implemented. See [IMPLEMENTATION_PROGRESS.md](IMPLEMENTATION_PROGRESS.md) for details.

## Quick Start

### Prerequisites

- Python 3.13+
- Docker + Docker Compose
- `uv` or `pip` for package management

### Local development (Docker Compose)

```bash
cp .env.example .env
docker compose up
```

### Local development (no Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
# Edit .env to point to your local Postgres
uvicorn app.main:app --reload
```

### Running tests

```bash
pytest tests/unit/
```

### Linting

```bash
ruff check app/ tests/
```

### Type checking

```bash
mypy app/
```

## API Endpoints

| Method | Path | Status |
|--------|------|--------|
| GET | /healthz | ✅ Implemented |
| GET | /readyz | ✅ Implemented |
| POST | /api/v1/verify | 🚧 Stub (501) |
| GET | /api/v1/inventory | 🚧 Stub (501) |
| GET | /api/v1/requests | 🚧 Stub (501) |
| GET | /api/v1/verdicts | 🚧 Stub (501) |

## Configuration

All configuration is via environment variables. See [.env.example](.env.example) for all available options.

## Architecture

See [docs/architecture.md](docs/architecture.md).
