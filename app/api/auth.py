"""Authentication dependency stub."""

from fastapi import Header, HTTPException, status

from app.config.settings import get_settings


def require_api_key(x_api_key: str = Header(alias="X-Api-Key")) -> str:
    """Validate the API key header.

    Raises HTTPException 401 if the key is missing or invalid.
    This is a basic stub; replace with production auth before deployment.
    """
    settings = get_settings()
    if x_api_key != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key.",
        )
    return x_api_key
