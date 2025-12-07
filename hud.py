"""
Module providing UI/HUD rendering utilities.

Includes font caching, and UI helpers.
"""

from button import Button
from pathlib import Path
import pygame
from typing import TYPE_CHECKING


# Forward reference to avoid circular imports at runtime
if TYPE_CHECKING:
        from Alien_Invasion import AlienInvasion


class HUD:
        def __init__(self, game: 'AlienInvasion') -> None:

                self.game = game
                self.settings = game.settings

                # Create the play button
                self.play_button = Button(
                        self.settings.play_button_text,
                        self.settings.play_button_font,
                        self.settings.play_button_loc,
                        self.settings.play_button_font_size,
                        "white",
                        "green",
                        "black",
                        True,
                        game
                        )

                # Create the pause button
                self.pause_button = Button(
                        self.settings.pause_button_text,
                        self.settings.pause_button_font,
                        self.settings.pause_button_loc,
                        self.settings.pause_button_font_size,
                        "white",
                        "green",
                        "black",
                        False,
                        game
                        )

                self.buttons = [self.play_button, self.pause_button]

        # TODO
        def wave(self) -> None:
                """
                Handles the wave increments and label.
                """

                # Increment the wave
                self.settings.wave += 1
