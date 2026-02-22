"""Root-level shared test fixtures."""

import os
from collections.abc import Callable
from pathlib import Path

import pytest

TESTS_DIR = Path(__file__).parent


@pytest.fixture
def tmp_data_dir(tmp_path: Path) -> Path:
    """Provide a temporary data directory for tests."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    return data_dir


@pytest.fixture
def env_vars(monkeypatch: pytest.MonkeyPatch) -> dict[str, str]:
    """Provide a helper to set environment variables for tests.

    Returns a dict; set values in it and they'll be applied as env vars.
    """
    vars_dict: dict[str, str] = {}
    return vars_dict


@pytest.fixture
def set_env(monkeypatch: pytest.MonkeyPatch) -> Callable[..., None]:
    """Return a callable to set environment variables that auto-cleanup."""

    def _set_env(**kwargs: str) -> None:
        for key, value in kwargs.items():
            monkeypatch.setenv(key, value)

    return _set_env


@pytest.fixture
def requires_network() -> None:
    """Skip test if CI environment (no network access expected)."""
    if os.environ.get("CI"):
        pytest.skip("Skipping network-dependent test in CI")
