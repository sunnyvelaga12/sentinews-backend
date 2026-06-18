"""
Application startup and shutdown events.
"""

from src.core.logging import get_logger

logger = get_logger(__name__)


async def startup() -> None:
    """
    Executes when the application starts.
    """

    logger.info("===================================")
    logger.info("Starting SentiNews Backend...")
    logger.info("Environment initialized.")
    logger.info("===================================")


async def shutdown() -> None:
    """
    Executes during graceful shutdown.
    """

    logger.info("===================================")
    logger.info("Stopping SentiNews Backend...")
    logger.info("Shutdown complete.")
    logger.info("===================================")