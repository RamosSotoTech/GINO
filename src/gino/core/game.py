"""Core application loop abstractions.

This module is intentionally minimal and focused on loop lifecycle,
so game logic can stay in systems/scenes and remain transferable.
"""

from dataclasses import dataclass


@dataclass
class Game:
    """Tiny placeholder game loop object for project scaffolding."""

    is_running: bool = False

    def run(self) -> None:
        """Start the application loop (placeholder implementation)."""
        self.is_running = True
        # TODO: initialize backend (e.g. pygame), then call update/render loop.

