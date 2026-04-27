"""Core application loop abstractions.

This module is intentionally minimal and focused on loop lifecycle,
so game logic can stay in systems/scenes and remain transferable.
"""

from dataclasses import dataclass

import pygame

from gino.core.settings import DEFAULT_FPS, DEFAULT_HEIGHT, DEFAULT_WIDTH, GameConfig
from gino.scenes.base import Scene
from gino.scenes.start_menu import StartMenuScene


@dataclass
class Game:
    """Owns the PyGame lifecycle and delegates gameplay work to loop hooks."""

    is_running: bool = False
    width: int = DEFAULT_WIDTH
    height: int = DEFAULT_HEIGHT
    fps: int = DEFAULT_FPS
    title: str = "GINO - Game Is Not Over"
    fullscreen: bool = False
    active_scene: Scene | None = None

    @classmethod
    def from_config(cls, config: GameConfig) -> "Game":
        """Create a game instance from saved or default configuration."""
        return cls(
            width=config.width,
            height=config.height,
            fps=config.fps,
            fullscreen=config.fullscreen,
        )

    def run(self) -> None:
        """Start the application loop."""
        pygame.init()
        display_flags = pygame.FULLSCREEN if self.fullscreen else 0
        screen = pygame.display.set_mode((self.width, self.height), display_flags)
        pygame.display.set_caption(self.title)
        clock = pygame.time.Clock()
        self.active_scene = StartMenuScene(self)

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
            if event.type == pygame.QUIT:
                self.is_running = False
            elif self.active_scene is not None:
                self.active_scene.handle_event(event)

    def update(self, delta_time: float) -> None:
        """Advance game simulation by ``delta_time`` seconds."""
        if self.active_scene is not None:
            self.active_scene.update(delta_time)

    def render(self, screen: pygame.Surface) -> None:
        """Draw the current frame."""
        if self.active_scene is not None:
            self.active_scene.render(screen)
