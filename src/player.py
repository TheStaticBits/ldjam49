import pygame

class Player:
    speed = 4
    jumpPower = -10

    def __init__(self, winSize):
        self.pos = [winSize[0] / 2, winSize[1] / 2]
        
        self.vel = 0
    
    def update(self, inputs):
        self.pos[0] -= inputs["left"] * self.speed
        self.pos[0] += inputs["right"] * self.speed

        self.vel += 0.5 # Gravity
        
        # Jump
        # Needs another collision test
        if inputs["up"]:
            self.vel = self.jumpPower

        self.pos[1] += self.vel
    
    def render(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.pos[0], self.pos[1], 20, 20))