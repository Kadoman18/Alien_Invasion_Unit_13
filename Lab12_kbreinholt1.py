import pygame
import sys
from types import SimpleNamespace # wanted dot operators, got this from ai.


# TODO update later for full screen (x=3000, y=1500)
screen_size = SimpleNamespace(x=900, y=450)

font_cache = {}
fonts = {
        'ss_reg': 'assets/fonts/Silkscreen/Silkscreen-Regular.ttf',
        'ss_bold': 'assets/fonts/Silkscreen/Silkscreen-Bold.ttf'
}

class Ship(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
                self.image = pygame.image.load('assets/graphics/ship.png').convert_alpha()
                self.rect = self.image.get_rect(midbottom=(450, 440))
                self.fire_rate = 750
                self.speed = 5

        def ship_input(self, lasers):
                keys = pygame.key.get_pressed()
                move_right_input = (keys[pygame.K_RIGHT] or keys[pygame.K_d])
                move_left_input = (keys[pygame.K_LEFT] or keys[pygame.K_a])
                if move_left_input and not move_right_input:
                        self.rect.x -= self.speed
                if move_right_input and not move_left_input:
                        self.rect.x += self.speed
                now = pygame.time.get_ticks()
                if not hasattr(self, 'last_shot_time'):
                        self.last_shot_time = 0
                if keys[pygame.K_SPACE]:
                        if now - self.last_shot_time >= self.fire_rate:
                                lasers.add(Laser(self.rect.midtop))
                                self.last_shot_time = now
                if keys[pygame.K_LSHIFT]:
                        self.fire_rate = 250
                        self.speed = 2
                else:
                        self.fire_rate = 750
                        self.speed = 5

class Laser(pygame.sprite.Sprite):
        def __init__(self, pos):
                super().__init__()
                self.image = pygame.image.load('assets/graphics/laserBlast.png').convert_alpha()
                self.rect = self.image.get_rect(center=pos)
                self.speed = -8

        def update(self):
                self.rect.y += self.speed
                if self.rect.bottom < 0:
                        self.kill()

def get_font(font_key, size):
        if font_key not in font_cache:
                font_cache[font_key] = {}

        if size not in font_cache[font_key]:
                font_cache[font_key][size] = pygame.font.Font(fonts[font_key], size)

        return font_cache[font_key][size]

def wave() -> str:
        wave = 1
        return f'Wave: {wave}'

def text_label(text, font_key, size, color):
        font = get_font(font_key, size)
        return font.render(text, False, color)

def main():
        pygame.init()
        screen = pygame.display.set_mode((screen_size.x, screen_size.y))
        pygame.display.set_caption("👾 Alien Invasion 👾")
        clock = pygame.time.Clock()

        sky_surf = pygame.image.load('assets/graphics/Starbasesnow.png').convert()

        enemy_surf = pygame.image.load('assets/graphics/enemy_4.png').convert_alpha()
        enemy_surf = pygame.image.load('assets/graphics/enemy_4.png').convert_alpha()

        ship = pygame.sprite.GroupSingle()
        ship.add(Ship())

        lasers = pygame.sprite.Group()
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                screen.blit(sky_surf, (0, 0))

                screen.blit(text_label(wave(), 'ss_reg', 25, (255, 255, 255)), (10, 10))

                ship.sprite.ship_input(lasers)

                if ship.sprite.rect.right < 5:
                        ship.sprite.rect.left = screen_size.x - 5
                if ship.sprite.rect.left > screen_size.x - 5:
                        ship.sprite.rect.right = 5

                # TODO
                # if laser_blast_rect.colliderect(enemy_rect)
                        # CODE IT

                ship.draw(screen)
                lasers.update()
                lasers.draw(screen)

                pygame.display.update()
                clock.tick(60)
if __name__ == '__main__':
        main()
