import pygame
from math import ceil

class Player:
    speed = 3
    jumpPower = -5

    def __init__(self, winSize):
        self.img = pygame.image.load("res/player.png").convert_alpha()
        self.rect = pygame.Rect((winSize[0] / 2) - self.img.get_width(), 50, self.img.get_width(), self.img.get_height())
        
        self.vel = 0
        self.canJump = True

    def reset(self, winSize):
        self.rect = pygame.Rect((winSize[0] / 2) - self.img.get_width(), 50, self.img.get_width(), self.img.get_height())
    
    def update(self, inputs, windowSize, check_all):
        directions = []

        # Left and right
        if inputs["left"]:
            self.rect.x -= self.speed
            directions.append("left")
        if inputs["right"]:
            self.rect.x += self.speed
            directions.append("right")

        if directions != []: # if the player has moved
            result = check_all(self.rect)
            if result != False:
                if "left" in directions:
                    self.rect.left = result.right
                elif "right" in directions:
                    self.rect.right = result.left
        
        # Clamps player between bricks
        self.rect.clamp_ip((0, 0, windowSize[0], windowSize[1]))
        
        # Gravity
        self.vel += 0.5
        
        # Jump
        if inputs["up"] and self.canJump:
            self.vel = self.jumpPower
            self.canJump = False
        
        self.rect.y += ceil(self.vel)

        result = check_all(self.rect)
        if result != False:
            if self.vel < 0: # If rising
                self.rect.top = result.bottom
                
            else: # If falling
                self.rect.bottom = result.top
                self.canJump = True
            
            self.vel = 0
        
        else:
            self.canJump = False

        # Testing if the player fell off the screen
        if self.rect.y > windowSize[1]:
            return False
        
        return True
    
    def render(self, window):
        window.blit(self.img, (self.rect.x, self.rect.y))