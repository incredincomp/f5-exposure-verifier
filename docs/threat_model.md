# Threat Model

## Trust Boundaries

- **Inbound API**: Untrusted. All inputs must be validated via Pydantic schemas.
- **F5 BIG-IP API**: Trusted internal system. Credentials must be stored in environment variables, never source code.
- **CrowdStrike API**: Trusted external SaaS. Webhook signatures must be verified.
- **Callback URLs**: Untrusted. Must be validated against an allowlist before delivery.

## Key Risks

| Risk | Mitigation |
|------|-----------|
| SSRF via callback URL | Validate callback URLs against allowlist; reject private IPs |
| Credential leakage | Use environment variables; redact in logs |
| Probe abuse | Bounded probe targets only; no user-controlled scan parameters |
| Replay attacks | Idempotency service deduplicates by request_id |
| Excessive exposure | Probe logic must be explicitly bounded; no scan ranges |

## What This Service Must NOT Do

- Full port scanning
- Vulnerability exploitation
- Brute-force authentication
- Stealth or evasion techniques
