"""Verification routes — not yet implemented."""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/verify")
def submit_verification() -> JSONResponse:
    """Submit an exposure event for verification.

    Not yet implemented.
    """
    return JSONResponse(
        status_code=501,
        content={"detail": "Not implemented.", "endpoint": "POST /api/v1/verify"},
    )
