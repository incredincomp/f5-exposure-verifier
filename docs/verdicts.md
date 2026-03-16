# Verdict Reference

## Verdict Codes

| Code | Meaning |
|------|---------|
| APPROVED | Target is in approved F5 inventory and passes all policies |
| UNAPPROVED | Target is not in inventory or fails policy checks |
| UNKNOWN | Classification was inconclusive |
| ERROR | A system error prevented verdict computation |

## Reason Codes

See `app/domain/reason_codes.py` for the full list of structured reason codes.
