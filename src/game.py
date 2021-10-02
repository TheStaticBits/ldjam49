import pygame

from src.window import Window
from src.input import Input
from src.player import Player
from src.objects import Objects

class Game:
    def __init__(self):
        pygame.init()

        self.scene = "play"

        self.window = Window((400, 400))
        self.input = Input()

        self.player = Player(self.window.size)
        self.objects = Objects()
    
    def update(self):
        self.input.update()
        
        if self.scene == "play":
            self.player.update(self.input.keys, self.objects.check_all)
    
    def render(self):
        if self.scene == "play":
            self.objects.render(self.window.screen)
            self.player.render(self.window.screen)

    def run(self):
        while not self.input.closeWindow:
            self.update()
            self.render()

            self.window.update()