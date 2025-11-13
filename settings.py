from dataclasses import dataclass
import paths

class Settings:

        @dataclass
        class ScreenSize:
                x : int = 1470
                y : int = 895

        def __init__(self):
                self.name: str  = '👾 Alien Invasion 👾'
                self.screen_size: tuple[int, int] = (self.ScreenSize().x, self.ScreenSize().y)
                self.background = paths.Graphics().background