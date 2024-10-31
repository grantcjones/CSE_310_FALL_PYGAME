import pygame

class Player(pygame.sprite.Sprite) :
    def __init__(self, player_image):
        self.image = pygame.image.load(player_image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (500, 500)
        self.rect.bottom = 24
        self.direction = True

    def flip_True(self):
        self.direction = True
        if self.direction == True:
            self.image = pygame.image.load("Product_Library/Source_Code/art/player_frame1_True.png")

    def flip_False(self):
        self.direction = False
        if self.direction == False:
            self.image = pygame.image.load("Product_Library/Source_Code/art/player_frame1_False.png")