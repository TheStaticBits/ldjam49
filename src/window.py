import pygame

class Window:
    def __init__(self, size):
        self.window = pygame.display.set_mode(size)
        self.screen = pygame.Surface(((size[0] - 100) / 2, (size[1] - 100) / 2))

        self.size = (self.screen.get_width(), self.screen.get_height())
        self.winSize = (self.window.get_width(), self.window.get_height())

        pygame.display.set_caption("Ludum Dare 49")

        self.clock = pygame.time.Clock()

    def update(self):
        self.window.blit(pygame.transform.scale(self.screen, (self.size[0] * 2, self.size[1] * 2)), (50, 50))
        
        pygame.display.flip()
        self.clock.tick(60)
        
        self.screen.fill((0, 0, 0))
        self.window.fill((0, 0, 0))