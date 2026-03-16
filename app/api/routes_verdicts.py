"""Verdict routes — not yet implemented."""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/verdicts")
def list_verdicts() -> JSONResponse:
    """List verification verdicts.

    Not yet implemented.
    """
    return JSONResponse(
        status_code=501,
        content={"detail": "Not implemented.", "endpoint": "GET /api/v1/verdicts"},
    )


@router.get("/verdicts/{verdict_id}")
def get_verdict(verdict_id: str) -> JSONResponse:
    """Get a specific verification verdict.

    Not yet implemented.
    """
    return JSONResponse(
        status_code=501,
        content={
            "detail": "Not implemented.",
            "endpoint": f"GET /api/v1/verdicts/{verdict_id}",
        },
    )
