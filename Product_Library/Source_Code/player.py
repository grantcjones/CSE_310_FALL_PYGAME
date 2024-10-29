import pygame

class Player(pygame.sprite.Sprite) :
    def __init__(self, player_image):
        self.image = pygame.image.load(player_image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (500, 500)
        self.rect.bottom = 24