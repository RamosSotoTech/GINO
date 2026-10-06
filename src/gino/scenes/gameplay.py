from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from gino.scenes.base import Scene

if TYPE_CHECKING:
    from gino.core.game import Game

class GameplayScene(Scene):

    background_color = (20, 24, 35)
    player_color = (88, 242, 152)
    player_rect: pygame.Rect = pygame.Rect(0, 0, 100, 100)

    def __init__(self, game: Game) -> None:
        self.game = game

    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, delta_time: float) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        screen.fill(self.background_color)
        pygame.draw.rect(screen, self.player_color, self.player_rect)
