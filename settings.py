from dataclasses import dataclass
from pathlib import Path
import paths
import platform
import pygame

class Settings:

        @dataclass
        class ScreenSize:
                pygame.display.init()

                if platform.system() == 'Darwin':
                        x: int = pygame.display.get_desktop_sizes()[0][0]
                        y: int = pygame.display.get_desktop_sizes()[0][1] - 61 # Stupid Menu Bar.. USABLE screen size please...
                else:
                        x: int = pygame.display.get_desktop_sizes()[0][0]
                        y: int = pygame.display.get_desktop_sizes()[0][1]

        def __init__(self):

                self.name : str  = '👾 Alien Invasion 👾'
                self.screen_size : tuple[int, int] = (self.ScreenSize().x, self.ScreenSize().y)
                self.background : Path = paths.Graphics().background