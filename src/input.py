import pygame

class Input:
    def __init__(self):
        self.closeWindow = False

        self.keys = {
            "left": False,
            "right": False,
            "up": False
        }

        self.mousePos = (0, 0)
        self.mouseDown = False
    
    def update(self):
        # Resetting one-time inputs
        self.keys["up"] = False # You cannot hold the up key
        self.mouseDown = False

        # Mouse Position
        self.mousePos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Handling inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.keys["left"] = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.keys["right"] = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.keys["up"] = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.keys["left"] = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.keys["right"] = False
            
            # Mouse Down event
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseDown = True

            # Handling the X button
            elif event.type == pygame.QUIT:
                self.closeWindow = True