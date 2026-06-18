"""
Centralized logging configuration for the application.

This module configures both console and rotating file logging.

Usage:
    from src.core.logging import get_logger

    logger = get_logger(__name__)
    logger.info("Application started")
"""

from __future__ import annotations

import logging
import logging.config
from pathlib import Path

from src.core.config import settings

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        },
        "detailed": {
            "format": "%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "app.log",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 5,
            "formatter": "detailed",
        },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "error.log",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 5,
            "formatter": "detailed",
            "level": "ERROR",
        },
    },
    "root": {
        "handlers": [
            "console",
            "file",
            "error_file",
        ],
        "level": settings.LOG_LEVEL,
    },
}


logging.config.dictConfig(LOGGING_CONFIG)


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger.
    """
    return logging.getLogger(name)