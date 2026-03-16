# AGENTS.md — Execution Guardrails

This file defines execution guardrails for AI coding agents working on this repository.

## Scope Boundaries

- Keep changes bounded to the module you are working on.
- Do not modify contracts, schemas, or models unless explicitly asked.
- Do not add new dependencies without checking for security vulnerabilities first.
- Do not implement real F5 or CrowdStrike API calls without explicit instruction.
- Do not add probe, scan, or exploit functionality.

## Change Discipline

- Update documentation when behavior changes.
- Prefer tests with real assertions over placeholder assertions.
- Preserve separation of: `contracts/`, `adapters/`, `domain/`, `services/`.
- Avoid fake implementations — raise `NotImplementedError` or return HTTP 501 instead.
- If the same failure repeats twice, stop and write a `LOOP_BREAK.md` note at the repo root explaining the failure, what was tried, and what context is needed.

## Code Standards

- Python 3.13 syntax
- Type hints on all public functions/methods
- Pydantic v2 (`model_config = ConfigDict(...)`, not `class Config`)
- SQLAlchemy 2.x (`DeclarativeBase`, `Mapped`, `mapped_column`)
- No circular imports
- Small focused files
- Run `ruff check` and `mypy` before committing

## Security

- Never commit secrets to source code
- Never generate exploit, vuln-scan, brute-force, or stealth functionality
- Always validate external inputs via Pydantic schemas
- Keep auth stubs clean but do not bypass auth in non-test code
