# Architecture

## Overview

F5 Exposure Verifier is a bounded service that:

1. Receives inbound exposure events (from CrowdStrike or other upstream systems)
2. Classifies the target against approved F5 inventory
3. Performs bounded outside-in probing (TCP, TLS, HTTP)
4. Evaluates policy expectations
5. Computes a structured verdict
6. Delivers the result via callback or polling

## Module Boundaries

```
contracts/   → Pydantic schemas for external I/O (inputs and outputs)
adapters/    → External system integrations (F5, CrowdStrike, probes)
domain/      → Pure business logic (classification, policy, verdict)
services/    → Orchestration layer (coordinates adapters + domain)
db/          → Persistence (SQLAlchemy models, repositories, sessions)
api/         → FastAPI route handlers
workers/     → Background job hooks (not yet implemented)
```

## Data Flow (planned)

```
Inbound event
    │
    ▼
POST /api/v1/verify
    │
    ▼
VerifyService.run()
    ├── IdempotencyService.is_duplicate()
    ├── InventoryService.get_latest()
    ├── inventory_classifier.classify_target()
    ├── policy_engine.evaluate_policies()
    ├── probes (tcp/tls/http)
    ├── verdict_engine.compute_verdict()
    ├── AuditService.log()
    └── CallbackService.deliver()
```
