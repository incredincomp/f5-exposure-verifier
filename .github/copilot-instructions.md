# Copilot Instructions

This file provides guidance for GitHub Copilot and other AI coding assistants working on this repository.

## Core Principles

1. **Keep changes bounded.** Only modify code directly related to your task. Do not refactor unrelated modules.

2. **Update docs when behavior changes.** If you implement a stub, update `IMPLEMENTATION_PROGRESS.md` to mark it as done.

3. **Prefer tests with real assertions.** Do not write `assert True` or trivially passing tests. Tests must validate real behavior.

4. **Preserve module separation.** The following boundaries must be maintained:
   - `contracts/` — Pydantic schemas for external I/O only
   - `adapters/` — external system integrations only
   - `domain/` — pure business logic, no I/O
   - `services/` — orchestration between adapters and domain

5. **Avoid fake implementations.** If a feature is not yet implemented:
   - In internal code: raise `NotImplementedError`
   - At API boundaries: return HTTP 501

6. **Loop-break discipline.** If the same failure repeats twice, stop and create a `LOOP_BREAK.md` file at the repo root explaining:
   - The failure
   - What was tried
   - What context or human decision is needed to proceed

## What NOT to Do

- Do not add exploit, vulnerability scan, brute-force, or stealth functionality
- Do not commit secrets
- Do not bypass authentication in non-test code
- Do not implement real F5 or CrowdStrike API calls without explicit instruction
- Do not add dependencies without security review
- Do not create god classes or massive utility files
