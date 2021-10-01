import pygame

class Window:
    def __init__(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption("Ludum Dare 49")

        self.clock = pygame.time.Clock()

    def update(self):
        pygame.display.flip()
        self.clock.tick(60)
        self.screen.fill((0, 0, 0))