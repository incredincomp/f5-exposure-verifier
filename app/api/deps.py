"""FastAPI dependency injection helpers."""

from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_session


def get_db() -> Generator[Session]:
    """Yield a database session."""
    yield from get_session()


DbSession = Annotated[Session, Depends(get_db)]
