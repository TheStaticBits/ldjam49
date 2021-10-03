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
            self.playButtonText.get_width(), self.playButtonText.get_height())
    
    def update(self, mousePos, mouseDown):
        if mouseDown:
            if self.playButtonRect.collidepoint(mousePos):
                return "play"

    def render(self, window):
        window.blit(self.logo, self.logoPos)

        window.blit(self.playButtonText, (self.playButtonRect.x, self.playButtonRect.y))