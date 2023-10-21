import pygame
from pygame.locals import *

class Startscreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._began = False
        self.image = pygame.image.load("Noemie\demarrage.png")
        self.rect = self.image.get_rect()




    def render(self, surface):
        surface.blit(self.image, (0,0))

class Player(pygame.sprite.Sprite):
    def __init__(self,name):
        super().__init__()
        self._name = name
        self.image = pygame.image.load("")
