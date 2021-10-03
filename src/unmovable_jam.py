import pygame
from random import randint
from math import ceil

class UJam:
    def __init__(self, pos):
        self.img = pygame.image.load("res/other_jams/jam_" + str(randint(0, 6)) + ".png").convert_alpha()

        self.vel = 0
        self.rect = pygame.Rect(pos[0], pos[1] - self.img.get_height(), self.img.get_width(), self.img.get_height())

    def update(self, windowHeight, check_all):
        # Gravity
        self.vel += 0.5
        
        self.rect.y += ceil(self.vel)

        result = check_all(self.rect)
        if result != False:
            self.rect.bottom = result.top
            self.vel = 0
        
        # Testing if the jam fell into the lava
        if self.rect.y > windowHeight:
            return False

        return True
    
    def render(self, window):
        window.blit(self.img, (self.rect.x, self.rect.y))