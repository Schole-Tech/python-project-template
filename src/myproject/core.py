"""Core module with sample business logic.

This module demonstrates project patterns including type hints,
docstrings, and error handling.
"""


class Greeter:
    """A sample service class demonstrating project patterns.

    Attributes:
        name: The name to use in greetings.
    """

    def __init__(self, name: str) -> None:
        """Initialize the Greeter.

        Args:
            name: The name to use in greetings. Must not be empty.

        Raises:
            ValueError: If name is empty or whitespace-only.
        """
        stripped = name.strip()
        if not stripped:
            msg = "Name must not be empty"
            raise ValueError(msg)
        self.name = stripped

    def greet(self, greeting: str = "Hello") -> str:
        """Generate a greeting message.

        Args:
            greeting: The greeting word to use.

        Returns:
            A formatted greeting string.
        """
        return f"{greeting}, {self.name}!"

    def __repr__(self) -> str:
        """Return a string representation."""
        return f"Greeter(name={self.name!r})"
