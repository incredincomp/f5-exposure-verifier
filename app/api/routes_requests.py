"""Verification requests routes — not yet implemented."""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/requests")
def list_requests() -> JSONResponse:
    """List verification requests.

    Not yet implemented.
    """
    return JSONResponse(
        status_code=501,
        content={"detail": "Not implemented.", "endpoint": "GET /api/v1/requests"},
    )


@router.get("/requests/{request_id}")
def get_request(request_id: str) -> JSONResponse:
    """Get a specific verification request.

    Not yet implemented.
    """
    return JSONResponse(
        status_code=501,
        content={
            "detail": "Not implemented.",
            "endpoint": f"GET /api/v1/requests/{request_id}",
        },
    )
