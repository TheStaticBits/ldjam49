import pygame
from math import floor

pygame.display.init()

class Platform:
    blinkDelay = 12
    collapsesAt = blinkDelay * 4
    comingBackDelay = 120

    def __init__(self, pos, size):
        # Image
        self.img = pygame.image.load("res/platform.png").convert_alpha()
        
        # Blink overlay
        self.blinkOverlay = pygame.Surface((self.img.get_width(), self.img.get_height()), pygame.SRCALPHA) 
        self.blinkOverlay.fill((100, 100, 100, 125))

        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        
        self.collapsed = False
        self.collapsing = False
        self.collapsingStage = 0

        self.comingBack = 0

    def start_collapse(self):
        self.collapsing = True

    def collision_check(self, rect):
        if not self.collapsed:
            if self.rect.colliderect(rect):
                return True
        
        return False
    
    def update(self):
        if self.collapsing:
            self.collapsingStage += 1

            if self.collapsingStage == self.collapsesAt:
                self.collapsed = True
                self.collapsing = False
                self.collapsingStage = 0
        
        elif self.collapsed:
            self.comingBack += 1

            if self.comingBack == self.comingBackDelay:
                self.comingBack = 0
                self.collapsed = False

    def render(self, window):
        if not self.collapsed:
            window.blit(self.img, (self.rect.x, self.rect.y))
        
        if self.collapsing:
            if floor(self.collapsingStage / self.blinkDelay) % 2 == 0:
                window.blit(self.blinkOverlay, (self.rect.x, self.rect.y))