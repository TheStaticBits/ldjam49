import pygame

from src.window import Window
from src.input import Input
from src.player import Player
from src.objects import Objects

class Game:
    def __init__(self):
        pygame.init()

        self.scene = "play"

        self.window = Window((590, 640))
        self.input = Input()

        self.player = Player(self.window.size)
        self.objects = Objects(self.window.size)
    
    def update(self):
        self.input.update()
        
        if self.scene == "play":
            result = self.player.update(self.input.keys, self.window.size[0], self.objects.check_all)
            if not result:
                self.input.closeWindow = True
            
            self.objects.update()
    
    def render(self):
        if self.scene == "play":
            self.objects.render_background(self.window.screen)
            self.player.render(self.window.screen)
            self.objects.render_platforms(self.window.screen)
            self.objects.render_lava(self.window.screen)

    def run(self):
        while not self.input.closeWindow:
            self.update()
            self.render()

            self.window.update()