import pygame

from src.window import Window
from src.input import Input
from src.player import Player

class Game:
    def __init__(self):
        pygame.init()

        self.scene = "play"

        self.window = Window((400, 400))
        self.input = Input()

        self.player = Player(self.window.size)
    
    def update(self):
        self.input.update()
        
        if self.scene == "play":
            self.player.update(self.input.keys)
    
    def render(self):
        if self.scene == "play":
            self.player.render(self.window.screen)

    def run(self):
        while not self.input.closeWindow:
            self.update()
            self.render()

            self.window.update()