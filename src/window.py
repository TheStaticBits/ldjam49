import pygame

class Window:
    def __init__(self, size):
        self.window = pygame.display.set_mode(size)
        self.screen = pygame.Surface((size[0] - 40, size[1] - 40))

        self.size = (self.screen.get_width(), self.screen.get_height())

        pygame.display.set_caption("Ludum Dare 49")

        self.clock = pygame.time.Clock()

    def update(self):
        self.window.blit(self.screen, (20, 20))
        
        pygame.display.flip()
        self.clock.tick(60)
        
        self.screen.fill((0, 0, 0))
        self.window.fill((0, 0, 0))