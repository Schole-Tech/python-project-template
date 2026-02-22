"""Tests for myproject.core module."""

import pytest

from myproject.core import Greeter


class TestGreeter:
    """Tests for Greeter class."""

    def test_init_with_valid_name(self) -> None:
        """Greeter initializes with a valid name."""
        greeter = Greeter("World")
        assert greeter.name == "World"

    def test_init_strips_whitespace(self) -> None:
        """Greeter strips leading/trailing whitespace from name."""
        greeter = Greeter("  Alice  ")
        assert greeter.name == "Alice"

    def test_init_with_empty_name_raises_error(self) -> None:
        """Empty name raises ValueError."""
        with pytest.raises(ValueError, match="Name must not be empty"):
            Greeter("")

    def test_init_with_whitespace_only_raises_error(self) -> None:
        """Whitespace-only name raises ValueError."""
        with pytest.raises(ValueError, match="Name must not be empty"):
            Greeter("   ")

    def test_greet_default(self) -> None:
        """greet() returns default greeting."""
        greeter = Greeter("World")
        assert greeter.greet() == "Hello, World!"

    def test_greet_custom(self) -> None:
        """greet() accepts custom greeting word."""
        greeter = Greeter("Bob")
        assert greeter.greet("Hi") == "Hi, Bob!"

    def test_repr(self) -> None:
        """Repr returns expected string."""
        greeter = Greeter("Alice")
        assert repr(greeter) == "Greeter(name='Alice')"

    def test_return_type_is_str(self) -> None:
        """greet() returns a string."""
        greeter = Greeter("Test")
        result = greeter.greet()
        assert isinstance(result, str)
