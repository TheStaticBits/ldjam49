import pygame
from random import choice, randint

from src.platform import Platform
from src.animation import Animation

class Objects:
    platformLevels = [80, 130, 180, 230]

    def __init__(self, windowSize):
        self.platforms = []
        
        # Platforms
        for level in self.platformLevels:
            for count in range(5):
                self.platforms.append(Platform((count * (windowSize[0] / 5), level), (windowSize[0] / 5, 10)))
        
        # Lava animation
        self.lavaAnim = Animation("res/lava.png", 25, 40)

        # Background image
        img = pygame.image.load("res/background.png").convert()
        self.background = pygame.Surface(windowSize)
        for y in range(int(windowSize[1] / 25)):
            for x in range(int(windowSize[0] / 25)):
                self.background.blit(img, (x * 25, y * 25))
        
        # Difficulty
        self.difficulty = 0
    
    def reset(self):
        for platform in self.platforms:
            platform.reset()
    
    def changeDifficulty(self, difficulty):
        self.difficulty = 95 - (difficulty * 15)
    
    def check_all(self, rect):
        for platform in self.platforms:
            if platform.collision_check(rect):
                return platform.rect
        
        return False

    def update(self):
        for platform in self.platforms:
            platform.update()

        if randint(1, self.difficulty) == 2:
            platform = choice(self.platforms)
            if not platform.collapsing and not platform.collapsed:
                platform.start_collapse()
        
        self.lavaAnim.flip()
    
    def render_background(self, window):
        window.blit(self.background, (0, 0))

    def render_platforms(self, window):
        # Platforms
        for platform in self.platforms:
            platform.render(window)
    
    def render_lava(self, window):
        # Lava
        for count in range(int(window.get_width() / 25)):
            window.blit(self.lavaAnim.get_image(), (25 * count, window.get_height() - 25))