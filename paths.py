from pathlib import Path
from dataclasses import dataclass

ROOT = Path.cwd() / 'assets'


@dataclass
class Audio:
        """
        File paths for all audio resources used by the game.

        Attributes
        ----------
        impact : Path
                Path to the player impact sound effect.
        laser : Path
                Path to the laser firing sound effect.
        """
        impact: Path = ROOT / "audio" / "impact.mp3"
        laser: Path = ROOT / "audio" / "laser.mp3"


@dataclass
class File:
        """
        File paths for data and JSON-based persistent storage.

        Attributes
        ----------
        scores : Path
                Path to the JSON file storing player score data.
        """
        scores: Path = ROOT / "file" / "scores.json"


@dataclass
class Font:
        """
        File paths for all font resources used in rendering UI text.

        Attributes
        ----------
        bold : Path
                Path to the bold silkscreen font.
        regular : Path
                Path to the regular silkscreen font.
        """
        bold: Path = ROOT / "fonts" / "silkscreen" / "silkscreen_bold.ttf"
        regular: Path = ROOT / "fonts" / "silkscreen" / "silkscreen_regular.ttf"


@dataclass
class Graphics:
        """
        File paths for all graphical assets, including sprites, UI elements,
        and backgrounds.

        Attributes
        ----------
        asteroid : Path
                Asteroid sprite asset.
        beams : Path
                Beam graphics asset.
        alien : Path
                Alien ship sprite.
        laser : Path
                Laser blast sprite.
        ship : Path
                Primary player ship sprite.
        background : Path
                Primary game background image.
        icon : Path
                App icon image.
        """
        asteroid: Path = ROOT / "graphics" / "asteroid.png"
        beams: Path = ROOT / "graphics" / "beams.png"
        alien: Path = ROOT / "graphics" / "alien.png"
        laser: Path = ROOT / "graphics" / "laser.png"
        ship: Path = ROOT / "graphics" / "ship.png"
        background: Path = ROOT / "graphics" / "background.png"
        icon: Path = ROOT / "graphics" / "icon.png"


