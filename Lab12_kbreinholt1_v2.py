import pygame
import settings
import paths


font_cache = {}
fonts = {
        'ss_reg': 'assets/fonts/Silkscreen/Silkscreen-Regular.ttf',
        'ss_bold': 'assets/fonts/Silkscreen/Silkscreen-Bold.ttf'
}

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

class AlienInvasion:

        def __init__(self):
                pygame.init()
                self.screen = pygame.display.set_mode((settings.Settings().screen_size))
                self.settings = settings.Settings()

                self.screen = pygame.display.set_mode((settings.Settings().screen_size))
                pygame.display.set_caption(self.settings.name)
                self.sky_surf = pygame.image.load(settings.Settings().background)

                self.running = True
                self.clock = pygame.time.Clock()

        def run_game(self) -> None:
                while self.running:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        self.running = False
                                        pygame.quit()
                                        exit()
                        self.screen.blit(self.sky_surf, (0, 0))
                        pygame.display.flip()
                        self.clock.tick(60)

if __name__ == '__main__':
        AlienInvasion().run_game()