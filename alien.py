"""
Alien entities for the Alien Invasion game.

Provides sprite loading, positioning logic, and screen drawing behavior
for the alien ship. Integrates with the main AlienInvasion game
instance to access window dimensions, settings, and display surfaces.
"""

from typing import TYPE_CHECKING
import pygame


# Forward reference to avoid circular imports at runtime
if TYPE_CHECKING:
        from Alien_Invasion import AlienInvasion


class Aliens(pygame.sprite.Sprite):
        """Houses the alien surf, rect, and movement behavior."""

        # Initialize local variables
        def __init__(self, game: 'AlienInvasion', x: int, y: int) -> None:

                # Initialize sprite class
                super().__init__()

                # Basic references to AlienInvasion class and Settings class
                self.game = game
                self.settings = game.settings
                self.ship = game.ship

                # Main display surface and its bounding rectangle
                self.screen_image: pygame.Surface = game.screen
                self.screen_rect: pygame.Rect = game.screen_rect

                # Surf and rect for alien sprite
                self.image: pygame.Surface = pygame.transform.scale(pygame.image.load(self.settings.alien_image), self.settings.alien_size).convert_alpha()
                self.rect: pygame.Rect = self.image.get_rect(center = (x, y))


        def check_edges(self):
                """
                Return True if alien touches either edge of the screen.
                """

                # Get screen Rect
                screen_rect: pygame.Rect = self.game.screen.get_rect()

                # True if
                return self.rect.right >= screen_rect.right or self.rect.left <= 0 or self.rect.bottom >= self.screen_rect.bottom



        def update(self):
                """
                Move alien horizontally using global horde direction.
                """
                self.rect.x += (self.settings.horde_speed *
                        self.settings.horde_direction)

                # Delete the alien when it leaves the screen
                if self.rect.midtop[1] > self.screen_rect.midbottom[1]:
                        self.game.you_lose = True
                        self.kill()

