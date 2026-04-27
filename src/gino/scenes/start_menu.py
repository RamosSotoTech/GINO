"""Start menu scene for GINO.

This scene is the player's first stop when the game launches. It owns the
menu-specific input, placeholder actions, and drawing for the start screen
while the main ``Game`` object stays focused on the application loop.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

import pygame

from gino.scenes.base import Scene

if TYPE_CHECKING:
    from gino.core.game import Game


@dataclass(frozen=True)
class MenuItem:
    """A selectable start-menu command."""

    label: str
    action: str


class StartMenuScene(Scene):
    """Keyboard-driven placeholder scene for the game's main menu.

    The scene intentionally keeps menu actions lightweight for now. ``Exit``
    closes the game, while ``Continue``, ``New Game``, and ``Settings`` update
    a status message so their future behavior has a clear place to land.
    """

    background_color = (8, 10, 18)
    title_color = (235, 246, 255)
    text_color = (156, 170, 190)
    selected_color = (88, 242, 152)
    disabled_color = (86, 98, 116)

    def __init__(self, game: Game) -> None:
        """Create menu state and fonts.

        Args:
            game: The running game object. The scene uses it for lifecycle
                actions such as exiting the application.
        """
        self.game = game
        self.items = (
            MenuItem("Continue", "continue"),
            MenuItem("New Game", "new_game"),
            MenuItem("Settings", "settings"),
            MenuItem("Exit", "exit"),
        )
        self.selected_index = 1
        self.status_message = "Select an option"
        self.title_font = pygame.font.Font(None, 96)
        self.menu_font = pygame.font.Font(None, 48)
        self.status_font = pygame.font.Font(None, 28)

    def handle_event(self, event: pygame.event.Event) -> None:
        """React to keyboard input for navigating and selecting menu items."""
        if event.type != pygame.KEYDOWN:
            return

        if event.key in (pygame.K_DOWN, pygame.K_s):
            self.selected_index = (self.selected_index + 1) % len(self.items)
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.selected_index = (self.selected_index - 1) % len(self.items)
        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            self.select_current_item()
        elif event.key == pygame.K_ESCAPE:
            self.game.is_running = False

    def update(self, delta_time: float) -> None:
        """Advance menu state.

        The menu has no animated state yet, but keeping this hook in place lets
        future visual polish or scene transitions fit the same scene contract.
        """

    def render(self, screen: pygame.Surface) -> None:
        """Draw the start menu."""
        screen.fill(self.background_color)
        center_x = screen.get_width() // 2

        self._draw_centered_text(
            screen,
            "GINO",
            self.title_font,
            self.title_color,
            center_x,
            120,
        )
        self._draw_centered_text(
            screen,
            "Game Is Not Over",
            self.status_font,
            self.text_color,
            center_x,
            185,
        )

        start_y = 290
        row_height = 62
        for index, item in enumerate(self.items):
            is_selected = index == self.selected_index
            marker = "> " if is_selected else "  "
            color = self.selected_color if is_selected else self.text_color
            if item.action == "continue":
                color = self.selected_color if is_selected else self.disabled_color

            self._draw_centered_text(
                screen,
                f"{marker}{item.label}",
                self.menu_font,
                color,
                center_x,
                start_y + index * row_height,
            )

        self._draw_centered_text(
            screen,
            self.status_message,
            self.status_font,
            self.text_color,
            center_x,
            screen.get_height() - 90,
        )

    def select_current_item(self) -> None:
        """Run the selected menu item's placeholder behavior."""
        selected_item = self.items[self.selected_index]

        if selected_item.action == "exit":
            self.game.is_running = False
        elif selected_item.action == "continue":
            self.status_message = "Continue placeholder: no save data yet"
        elif selected_item.action == "new_game":
            self.status_message = "New Game placeholder: gameplay scene coming soon"
        elif selected_item.action == "settings":
            self.status_message = "Settings placeholder: options scene coming soon"

    def _draw_centered_text(
        self,
        screen: pygame.Surface,
        text: str,
        font: pygame.font.Font,
        color: tuple[int, int, int],
        center_x: int,
        y: int,
    ) -> None:
        """Render one text line centered on the given x coordinate."""
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(center_x, y))
        screen.blit(text_surface, text_rect)
