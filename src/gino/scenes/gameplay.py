from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from gino.scenes.base import Scene

if TYPE_CHECKING:
    from gino.core.game import Game

class GameplayScene(Scene):

    background_color = (20, 24, 35)
    player_color = (88, 242, 152)

    def __init__(self, game: Game) -> None:
        self.game = game
        self.player_rect: pygame.Rect = pygame.Rect(0, 0, 100, 100)

        # Move Player into entities later
        self.player_position = pygame.Vector2(self.player_rect.center)
        self.player_speed : float = 300.0 # pixels per seconds

    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, delta_time: float) -> None:
        keys = pygame.key.get_pressed()
        distance = self.player_speed * delta_time
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player_position.x -= distance
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player_position.x += distance
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player_position.y -= distance
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player_position.y += distance

        self.player_rect.center = (
            round(self.player_position.x),
            round(self.player_position.y),
        )

    def render(self, screen: pygame.Surface) -> None:
        screen.fill(self.background_color)
        pygame.draw.rect(screen, self.player_color, self.player_rect)
