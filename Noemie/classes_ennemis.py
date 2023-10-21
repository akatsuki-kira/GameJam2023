import pygame, random
from pygame.locals import *

personalities = [
    "pong",
    "quiz",
    "battle",
]
class Fantomaths(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("fantomaths.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self.image.get_rect() 
        self._name = "Fantomaths"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self.image, (0,0)) 

class Robarbre(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("robarbre.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self.image.get_rect() 
        self._name = "Robarbre"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self.image, (0,0)) 

class Chitrouille(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("chitrouille.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self.image.get_rect() 
        self._name = "Chitrouille"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self.image, (0,0)) 

class Cerftete(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("cerf-tête.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self.image.get_rect() 
        self._name = "Cerf-Tête"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self.image, (0,0))

class Hector(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("hector.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self.image.get_rect() 
        self._name = "Hector"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self.image, (0,0))

class Perforatrice(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("perforatrice.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self.image.get_rect() 
        self._name = "Perforatrice"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self.image, (0,0))


class Perforatrice2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("perforatrice2.png")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self.image.get_rect() 
        self._name = "Perforatrice?"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self.image, (0,0))

class MathsTeacher(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self.image.get_rect() 
        self._name = "Mr. Coulangênant"
        self._personality = "boss"
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self.image, (0,0)) 
