import pygame

from src.window import Window
from src.input import Input

from src.menu import Menu
from src.player import Player
from src.objects import Objects

class Game:
    def __init__(self):
        pygame.init()

        self.score = 0
        self.scene = "menu"

        self.window = Window((650, 700))
        self.input = Input()

        self.menu = Menu(self.window.winSize)
        self.player = Player(self.window.size)
        self.objects = Objects(self.window.size)

        # Sets up the brick background
        brick = pygame.transform.scale(pygame.image.load("res/bricks.png").convert(), (50, 50))
        self.bricks = pygame.Surface(self.window.winSize)
        for y in range(int(self.window.winSize[1] / 50)):
            for x in range(int(self.window.winSize[0] / 50)):
                self.bricks.blit(brick, (x * 50, y * 50))
        
        # Score's font
        self.font = pygame.font.Font("font/monogram.ttf", 60)
    
    def update(self):
        self.score += 1

        self.input.update()
        
        if self.scene == "play":
            result = self.player.update(self.input.keys, self.window.size, self.objects.check_all)
            if not result:
                self.scene = "menu"

                self.player.reset(self.window.size)
                self.objects.reset()
                self.score = 0
            
            self.objects.update()
        
        elif self.scene == "menu":
            result = self.menu.update(self.input.mousePos, self.input.mouseDown)
            if result == "play":
                self.scene = result
                self.objects.changeDifficulty(self.menu.difficulty)
    
    def render(self):
        self.window.window.blit(self.bricks, (0, 0))
        
        if self.scene == "play":
            # Every second gives you 10 points
            self.window.window.blit(self.font.render("SCORE: " + str(int(self.score / 6)), False, (255, 255, 255)), (50, 10))

            self.objects.render_background(self.window.screen)
            self.player.render(self.window.screen)
            self.objects.render_platforms(self.window.screen)
            self.objects.render_lava(self.window.screen)
        
        elif self.scene == "menu":
            self.menu.render(self.window.window)

    def run(self):
        while not self.input.closeWindow:
            self.update()
            self.render()

            self.window.update(self.scene == "play")