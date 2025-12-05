"""
Module providing the main Alien Invasion game loop using pygame.
Includes the core game window initialization.
"""

import pygame
import paths
from settings import Settings
from ship import Ship
from arsenal import Laser
from alien_horde import AlienHorde
from button import Button


class AlienInvasion:
        """Main game controller for the Alien Invasion application."""

        def __init__(self) -> None:

                # Initialize
                pygame.init()
                self.settings = Settings()

                # Set the screen mode, scaling depending on screen size
                self.screen = pygame.display.set_mode((self.settings.screen_size))

                # Define the screen rect for sprite placements
                self.screen_rect: pygame.Rect = self.screen.get_rect(
                        midbottom=(
                                self.settings.ScreenSize.x // 2,
                                self.settings.ScreenSize.y
                        )
                )

                self.play_button = Button(
                        "Play",
                        paths.Font.bold,
                        self.screen_rect.center,
                        (
                                self.settings.screen_size[0] // 20,
                                self.settings.screen_size[1] // 20
                                ),
                        "white",
                        "green",
                        self
                        )
                self.play_button.draw(self.screen, self.screen_rect.center)

                self.pause_duration = 0
                self.pause_start_time = None
                self.last_shot_time = 0

                # Customize game window title and icon
                pygame.display.set_caption(self.settings.name)
                pygame.display.set_icon(pygame.image.load(self.settings.icon))

                # Load and resize the sky image to fit the window and get its rect
                self.sky_image: pygame.Surface = pygame.transform.scale(
                        pygame.image.load(self.settings.background).convert(),
                        self.settings.screen_size
                )
                self.sky_rect: pygame.Rect = self.sky_image.get_rect()

                # Create the player's ship sprite, sprite group, and add the sprite to it.
                self.ship = Ship(self)
                self.ship_group = pygame.sprite.GroupSingle()
                self.ship_group.add(self.ship)

                # Create the lasers sprite group
                self.lasers = pygame.sprite.Group()
                self.lasers_noise = pygame.mixer.Sound(self.settings.laser_noise)

                # Create the horde of aliens
                self.horde = AlienHorde(self)

                # Game running boolean
                self.running: bool = True
                self.paused: bool = True

                # Game clock
                self.clock = pygame.time.Clock()


        def _fire_laser(self) -> None:
                """Handles the logic for continuous laser firing and rate"""
                if self.paused:
                        return

                now = pygame.time.get_ticks()
                relative_now = now - self.pause_duration

                # Base fire
                if self.ship.firing and (relative_now - self.last_shot_time >= self.settings.ship_base_fire_rate):
                        self.lasers.add(Laser(self))
                        self.last_shot_time = relative_now

                # Rapid fire
                elif self.ship.firing and self.ship.firing_rapid and (
                    relative_now - self.last_shot_time >= self.settings.ship_rapid_fire_rate
                ):
                        self.lasers.add(Laser(self))
                        self.last_shot_time = relative_now



        def _event_listener(self) -> None:
                """Listens for events like quit, or keyboard input."""

                for event in pygame.event.get():
                        # Quit game
                        if event.type == pygame.QUIT:
                                self.running = False
                                pygame.quit()
                                exit()

                        # Mouse Right Click event
                        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == True:
                                self._toggle_pause()

                        # Keydown event
                        elif event.type == pygame.KEYDOWN:
                                self._key_down_event(event)

                        # Keyup event
                        elif event.type == pygame.KEYUP:
                                self._key_up_event(event)


        def _key_down_event(self, event):
                """Listens for key down events (Key Presses)"""

                # Rightward movement
                if event.key == pygame.K_d:
                        self.ship.moving_right = True
                elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True

                # Leftward movement
                elif event.key == pygame.K_a:
                        self.ship.moving_left = True
                elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True

                # Firing (base and rapid)
                elif event.key == pygame.K_SPACE:
                        self.ship.firing = True
                elif event.key == pygame.K_LSHIFT:
                        self.ship.firing_rapid = True

                # Quit game with Escape
                elif event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                        exit()


        def _key_up_event(self, event) -> None:
                """Listens for key up events (Key Releases)"""

                if event.key == pygame.K_p:
                        self._toggle_pause()

                # Rightward movement stop
                elif event.key == pygame.K_d:
                        self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False

                # Leftward movement stop
                elif event.key == pygame.K_a:
                        self.ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False

                # Firing stop
                elif event.key == pygame.K_SPACE:
                        self.ship.firing = False
                elif event.key == pygame.K_LSHIFT:
                        self.ship.firing_rapid = False

        def _toggle_pause(self) -> None:
                """Listens for right mouse click events on the play button and the pressing of P"""
                if not self.paused:
                        # Going from unpaused → paused
                        self.paused = True
                        self.pause_start_time = pygame.time.get_ticks()
                else:
                        # Going from paused → unpaused
                        self.paused = False
                        paused_time = 0
                        if self.pause_start_time != None:
                                paused_time = pygame.time.get_ticks() - self.pause_start_time
                        self.pause_duration += paused_time
                        self.pause_start_time = None

        def _update_screen(self) -> None:
                """Updates the screen with relevant movements, sprites, and UI elements"""

                # Draw background
                self.screen.blit(self.sky_image, (0, 0))

                # Draw ship sprite
                self.ship_group.draw(self.screen)

                # Draw lasers sprite group
                self.lasers.draw(self.screen)

                # Draw alien horde
                self.horde.horde.draw(self.screen)

                # Update the display (swap buffers)
                pygame.display.flip()


        def run_game(self) -> None:
                """Main game loop"""


                while self.running == True:
                        # Handle system and player events
                        self._event_listener()

                        # Update ship sprite group
                        self.ship_group.update()

                        # Fire lasers if conditions are met
                        self._fire_laser()

                        # Update lasers sprite group
                        self.lasers.update()

                        # Update alien horde movement
                        self.horde.update()

                        # Draws all relevant surfaces, rects, sprites, to the screen.
                        self._update_screen()

                        # Limit framerate to avoid running too fast
                        self.clock.tick(self.settings.fps)


if __name__ == '__main__':
        AlienInvasion().run_game()
