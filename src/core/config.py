"""
Application configuration.

This module centralizes all environment variables using Pydantic Settings.

Usage:
    from src.core.config import settings

    print(settings.APP_NAME)
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # Application
    APP_NAME: str = "SentiNews API"
    APP_VERSION: str = "1.0.0"

    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # PostgreSQL
    DATABASE_URL: str = Field(...)

    POSTGRES_USER: str = Field(...)
    POSTGRES_PASSWORD: str = Field(...)
    POSTGRES_DB: str = Field(...)

    # Redis
    REDIS_URL: str = Field(...)

    # JWT
    SECRET_KEY: str = Field(...)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # External APIs
    GEMINI_API_KEY: str = ""
    NEWS_API_KEY: str = ""
    TWELVEDATA_API_KEY: str = ""

    # CORS
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
    ]

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = (
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.

    Prevents re-reading the .env file multiple times.
    """

    return Settings()


settings = get_settings()