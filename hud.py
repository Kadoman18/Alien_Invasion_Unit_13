"""
Module providing UI/HUD rendering utilities.

Includes font caching, and UI helpers.
"""

from pathlib import Path
import pygame
from settings import Settings


# Reference to settings
settings = Settings()


def text_label(text: str, font_path: Path, size: int, color: str | tuple[int, int, int]) -> pygame.Surface:
        """
        Render a text label using a cached pygame font.

        Parameters
        ----------
        text : str
                The text content to render.
        font_path : Path
                A pathlib Path object to the font file.
        size : int
                The pixel size of the font.
        color : str
                A pygame-compatible color value (name or RGB tuple).

        Returns
        -------
        pygame.Surface
                A rendered text surface ready to blit to the screen.
        """
        # Extract the fonts name
        font_key = Path(font_path).name

        # Create font group in cache if missing
        if font_key not in settings.font_cache:
                settings.font_cache[font_key] = {}

        # Load the font at this size if not previously loaded
        if size not in settings.font_cache[font_key]:
                settings.font_cache[font_key][size] = pygame.font.Font(font_path, size)

        # Retrieve font from cache and render the text
        font = settings.font_cache[font_key][size]
        return font.render(text, False, color)


# TODO
def wave() -> None:
        """
        Handles the wave increments and label.
        """

        # Increment the wave
        settings.wave += 1
