import pygame

class Platform:
    def __init__(self, pos, size):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def collision_check(self, rect):
        if self.rect.colliderect(rect):
            return True
        
        return False
    
    def update(self):
        pass

    def render(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.rect)