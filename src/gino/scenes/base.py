"""Base scene contract.

Scenes are high-level game states such as the start menu, gameplay, settings,
pause screen, or game-over screen. The main ``Game`` loop owns the PyGame
runtime and delegates input, simulation, and drawing to whichever scene is
currently active.
"""

from abc import ABC, abstractmethod

import pygame


class Scene(ABC):
    """Interface shared by all game scenes."""

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle one PyGame event for this scene."""

    @abstractmethod
    def update(self, delta_time: float) -> None:
        """Advance this scene by ``delta_time`` seconds."""

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        """Draw this scene to the given screen surface."""
