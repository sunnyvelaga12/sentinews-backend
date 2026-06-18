"""
FastAPI lifespan management.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.events import shutdown
from src.core.events import startup


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Controls application startup and shutdown lifecycle.
    """

    await startup()

    yield

    await shutdown()