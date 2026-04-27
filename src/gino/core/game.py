"""Core application loop abstractions.

This module is intentionally minimal and focused on loop lifecycle,
so game logic can stay in systems/scenes and remain transferable.
"""

from dataclasses import dataclass

import pygame

from gino.core.settings import DEFAULT_FPS, DEFAULT_HEIGHT, DEFAULT_WIDTH


@dataclass
class Game:
    """Owns the PyGame lifecycle and delegates gameplay work to loop hooks."""

    is_running: bool = False
    width: int = DEFAULT_WIDTH
    height: int = DEFAULT_HEIGHT
    fps: int = DEFAULT_FPS
    title: str = "GINO - Game Is Not Over"

    def run(self) -> None:
        """Start the application loop."""
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        clock = pygame.time.Clock()

        self.is_running = True
        while self.is_running:
            delta_time = clock.tick(self.fps) / 1000.0
            self.handle_events()
            self.update(delta_time)
            self.render(screen)
            pygame.display.flip()

        pygame.quit()

    def handle_events(self) -> None:
        """Process backend events that affect the application lifecycle."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.is_running = False

    def update(self, delta_time: float) -> None:
        """Advance game simulation by ``delta_time`` seconds."""

    def render(self, screen: pygame.Surface) -> None:
        """Draw the current frame."""
        screen.fill((8, 10, 18))
