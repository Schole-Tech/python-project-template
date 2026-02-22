"""Tests for myproject.config module."""

import pytest

from myproject.config import AppConfig


class TestAppConfig:
    """Tests for AppConfig."""

    def test_default_values(self) -> None:
        """Default config has expected values."""
        config = AppConfig()
        assert config.app_name == "myproject"
        assert config.debug is False
        assert config.log_level == "INFO"
        assert config.port == 8080

    def test_custom_values(self) -> None:
        """Config accepts custom values."""
        config = AppConfig(app_name="testapp", debug=True, log_level="DEBUG", port=3000)
        assert config.app_name == "testapp"
        assert config.debug is True
        assert config.log_level == "DEBUG"
        assert config.port == 3000

    def test_invalid_log_level_raises_error(self) -> None:
        """Invalid log level raises ValidationError."""
        with pytest.raises(Exception):  # noqa: B017
            AppConfig(log_level="INVALID")

    def test_invalid_port_raises_error(self) -> None:
        """Port out of range raises ValidationError."""
        with pytest.raises(Exception):  # noqa: B017
            AppConfig(port=0)

    def test_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """from_env reads environment variables correctly."""
        monkeypatch.setenv("APP_NAME", "envapp")
        monkeypatch.setenv("APP_DEBUG", "true")
        monkeypatch.setenv("APP_LOG_LEVEL", "DEBUG")
        monkeypatch.setenv("APP_PORT", "9090")

        config = AppConfig.from_env()
        assert config.app_name == "envapp"
        assert config.debug is True
        assert config.log_level == "DEBUG"
        assert config.port == 9090

    def test_from_env_defaults(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """from_env uses defaults when env vars are not set."""
        monkeypatch.delenv("APP_NAME", raising=False)
        monkeypatch.delenv("APP_DEBUG", raising=False)
        monkeypatch.delenv("APP_LOG_LEVEL", raising=False)
        monkeypatch.delenv("APP_PORT", raising=False)

        config = AppConfig.from_env()
        assert config.app_name == "myproject"
        assert config.debug is False
