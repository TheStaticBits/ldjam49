import pygame

from src.platform import Platform

class Objects:
    def __init__(self):
        self.platforms = []
        self.platforms.append(Platform((120, 240), (100, 30)))
    
    def check_all(self, rect):
        for platform in self.platforms:
            if platform.collision_check(rect):
                return platform.rect
        
        return False

    def update(self):
        for platform in self.platforms:
            platform.update()
    
    def render(self, window):
        for platform in self.platforms:
            platform.render(window)