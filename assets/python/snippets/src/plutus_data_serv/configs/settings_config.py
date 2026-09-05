import os
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Determine which profile to load (Defaults to local)
ENV_STAGE = os.getenv("ENV_STAGE", "local")


class Settings(BaseSettings):
    """Strongly typed application configuration schema."""

    # Core Infrastructure
    ENVIRONMENT: Literal["local", "cloud"] = Field(default="local")
    GRPC_PORT: int = Field(default=50051, ge=1024, le=65535)
    GRPC_MAX_WORKERS: int = Field(default=10, ge=1)

    # Application Config Example
    REDIS_HOST: str = Field(default="localhost")
    REDIS_PORT: int = Field(default=6379)

    # Logging config
    LOG_FORMAT: str = Field()
    LOG_LEVEL: str = Field()

    # Docker compose
    DOCKER_CONF_PAHT: str = Field()

    # Postgress Config
    PGSQL_HOSTS: str = Field(default="localhost")
    PGSQL_PORT: int = Field(default=5432)
    PGSQL_DB: str = Field(default="plutus_schema")
    PGSQL_USERNAME: str = Field(default="postgres")
    PGSQL_PASSWORD: str = Field(default="postgres")

    # Concurrency config
    THREADS_MUL: int = Field(default=1)

    # Base year config
    MIN_FETCH_YEAR: int = Field(default=1970)

    # Load .env.base and then overwrite with .env.[target env]
    model_config = SettingsConfigDict(
        env_file=("env/.env.base", f"env/.env.{ENV_STAGE}"),
        env_file_encoding="utf-8",
        extra="forbid",  # Strict validation
    )


# Instantiate a singleton instance to use throughout the application lifecycle
SETTINGS: Settings = Settings()
