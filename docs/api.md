# API Reference

## Authentication

All endpoints (except health checks) require an `X-Api-Key` header.

## Endpoints

### Health

#### GET /healthz

Liveness probe.

**Response 200:**
```json
{"status": "ok"}
```

#### GET /readyz

Readiness probe.

**Response 200:**
```json
{"status": "ok", "database": "ok"}
```

### Verification (not yet implemented)

#### POST /api/v1/verify

Submit an exposure event for verification.

**Response 501:** Not implemented.

### Inventory (not yet implemented)

#### GET /api/v1/inventory

List inventory snapshots.

**Response 501:** Not implemented.

### Requests (not yet implemented)

#### GET /api/v1/requests

List verification requests.

**Response 501:** Not implemented.

### Verdicts (not yet implemented)

#### GET /api/v1/verdicts

List verification verdicts.

**Response 501:** Not implemented.
