"""Application configuration using Pydantic settings.

This module provides a typed configuration pattern using Pydantic BaseModel.
Configuration values can be loaded from environment variables via ``from_env()``.
"""

import os

from pydantic import BaseModel, Field
from typing_extensions import Self


class AppConfig(BaseModel):
    """Application configuration.

    Attributes:
        app_name: Name of the application.
        debug: Whether to enable debug mode.
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        port: Port number for the application server.
    """

    app_name: str = "myproject"
    debug: bool = False
    log_level: str = Field(default="INFO", pattern=r"^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$")
    port: int = Field(default=8080, ge=1, le=65535)

    @classmethod
    def from_env(cls) -> Self:
        """Create configuration from environment variables.

        Environment variables are read with the ``APP_`` prefix:
        ``APP_NAME``, ``APP_DEBUG``, ``APP_LOG_LEVEL``, ``APP_PORT``.

        Returns:
            AppConfig instance populated from environment.
        """
        return cls(
            app_name=os.environ.get("APP_NAME", "myproject"),
            debug=os.environ.get("APP_DEBUG", "false").lower() in ("true", "1", "yes"),
            log_level=os.environ.get("APP_LOG_LEVEL", "INFO"),
            port=int(os.environ.get("APP_PORT", "8080")),
        )
