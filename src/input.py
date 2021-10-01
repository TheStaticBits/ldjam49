import pygame

class Input:
    def __init__(self):
        self.closeWindow = False

        self.keys = {
            "left": 0,
            "right": 0,
            "up": 0
        }
    
    def update(self):
        self.keys["up"] = 0 # Cannot hold the up key
        for event in pygame.event.get():
            # Handling inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.keys["left"] = 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.keys["right"] = 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.keys["up"] = 1
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.keys["left"] = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.keys["right"] = 0

            # Handling the X button
            elif event.type == pygame.QUIT:
                self.closeWindow = True