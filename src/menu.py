import pygame

class Menu:
    def __init__(self, windowSize):
        self.logo = pygame.image.load("res/Logo (120x80).png").convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (360, 240))
        self.logoPos = (
            (windowSize[1] / 2) - (self.logo.get_width() / 2),
            windowSize[1] - self.logo.get_height()
        )

        self.playButtonText = pygame.font.Font("font/monogram.ttf", 80).render("PLAY", False, (255, 255, 255))
        self.playButtonRect = pygame.Rect(
            (windowSize[0] / 2) - (self.playButtonText.get_width() / 2),
            100,
            self.playButtonText.get_width(), self.playButtonText.get_height()
        )

        self.difficultyText = pygame.font.Font("font/monogram.ttf", 40).render("Difficulty", False, (255, 255, 255))
        self.difficultyPos = (
            (windowSize[0] / 2) - (self.difficultyText.get_width() / 2),
            200
        )

        self.difficultyFont = pygame.font.Font("font/monogram.ttf", 100)

        self.difficulty = 3

        self.arrow = pygame.image.load("res/arrow.png").convert_alpha()

        self.arrow1 = pygame.Rect(
            self.difficultyPos[0] + 16,
            self.difficultyPos[1] + 55,
            self.arrow.get_width(),
            self.arrow.get_height()
        )
        self.arrow2 = pygame.Rect(
            self.difficultyPos[0] + 95,
            self.difficultyPos[1] + 55,
            self.arrow.get_width(),
            self.arrow.get_height()
        )
    
    def update(self, mousePos, mouseDown):
        if mouseDown:
            if self.playButtonRect.collidepoint(mousePos):
                return "play"
            
            elif self.arrow1.collidepoint(mousePos):
                self.difficulty -= 1
            
            elif self.arrow2.collidepoint(mousePos):
                self.difficulty += 1
            
            if self.difficulty < 1:
                self.difficulty = 1

            elif self.difficulty > 6:
                self.difficulty = 6

    def render(self, window):
        # Logo
        window.blit(self.logo, self.logoPos)

        # Play button
        window.blit(self.playButtonText, (self.playButtonRect.x, self.playButtonRect.y))

        # Difficulty text
        window.blit(self.difficultyText, self.difficultyPos)

        # Difficulty number
        render = self.difficultyFont.render(str(self.difficulty), False, (255, 255, 255))
        renderPos = (
            (window.get_width() / 2) - (render.get_width() / 2),
            self.difficultyPos[1] + 25
        )
        window.blit(render, renderPos)
        
        # Left arrow
        window.blit(self.arrow, (self.arrow1.x, self.arrow1.y))
        # Right arrow
        window.blit(pygame.transform.flip(self.arrow, True, False), (self.arrow2.x, self.arrow2.y))