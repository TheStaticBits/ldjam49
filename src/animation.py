import pygame
from math import floor

class Animation:
    def __init__(self, filePath, indivWidth, gap):
        img = pygame.image.load(filePath).convert_alpha()

        self.images = []

        for count in range(int(img.get_width() / indivWidth)):
            frameImg = pygame.Surface((indivWidth, img.get_width()))
            frameImg.blit(img, (-count * indivWidth, 0))
            print((-count * img.get_width()))
            self.images.append(frameImg)
        
        self.gap = gap
        self.frame = 0

    def flip(self):
        # Incrementing frame number
        self.frame += 1

        # Resetting animation if it ended
        if self.frame / self.gap == len(self.images):
            self.frame = 0
            return True
        
        return False
        # Return statements are for if the animation is only supposed to be played once
    
    # Renders and flips to the next image
    def get_image(self):
        return self.images[floor(self.frame / self.gap)]
    
    # Returns first image
    def get_first(self):
        return self.images[0]
    
    # A combination of rendering and flipping
    def render_and_flip(self, window, pos):
        window.blit(self.get_image, pos)
        return self.flip()