import pygame
from hud import text_label
from typing import TYPE_CHECKING
from pathlib import Path
import paths
if TYPE_CHECKING:
        from Alien_Invasion import AlienInvasion

class Button:

        def __init__(
                        self,
                        text: str,
                        font: Path,
                        center: tuple[int, int],
                        size: tuple[int, int],
                        text_color: str | tuple[int, int, int],
                        fill_color: str | tuple[int, int, int],
                        game: 'AlienInvasion'
                        ) -> None:

                # Basic references to AlienInvasion class and Settings class
                self.game = game
                self.settings = game.settings

                # Main display surface and its bounding rectangle
                self.screen_image: pygame.Surface = game.screen
                self.screen_rect: pygame.Rect = game.screen_rect

                self.button = pygame.Surface(size)
                pygame.Surface.fill(self.button, fill_color)

                self.rect = self.button.get_rect(center = center)

                self.label = text_label(text, font, size[1] - (size[1] // 8), text_color)

        def draw(self, location, rect):

                location.blit(self.button, rect)
                self.button.blit(self.label, self.rect.center)