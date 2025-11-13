from pathlib import Path
from dataclasses import dataclass

BASE = Path.cwd() / 'assets'

@dataclass
class Audio:
        impact: Path = BASE / "audio" / "impactSound.mp3"
        laser: Path = BASE / "audio" / "laser.mp3"
@dataclass
class File:
        scores: Path = BASE / "file" / "scores.json"
@dataclass
class Font:
        bold: Path = BASE / "fonts" / "Silkscreen-Bold.ttf"
        regular: Path = BASE / "fonts" / "Silkscreen-Regular.ttf"
@dataclass
class Graphics:
        asteroid: Path = BASE / "graphics" / "Asteroid Brown.png"
        beams: Path = BASE / "graphics" / "beams.png"
        enemy: Path = BASE / "graphics" / "enemy_4.png"
        laser: Path = BASE / "graphics" / "laserBlast.png"
        ship1: Path = BASE / "graphics" / "ship.png"
        ship2: Path = BASE / "graphics" / "ship2.png"
        ship2nobg: Path = BASE / "graphics" / "ship2(no bg).png"
        background: Path = BASE / "graphics" / "Starbasesnow.png"

