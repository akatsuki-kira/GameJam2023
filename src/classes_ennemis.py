import pygame, random
from pygame.locals import *

personalities = [
    #"pong",
    "quiz",
    #"battle"
]

sprites_ = [f"frame_{i}_delay-0.02s.gif" for i in range(59)]

class Fantomaths(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("images/fantomaths.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self._image.get_rect() 
        self._name = "fantomaths"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self._image, (0,0)) 

class Robarbre(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("images/robarbre.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self._image.get_rect() 
        self._name = "robarbre"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self._image, (0,0)) 

class Chitrouille(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("images/chitrouille.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self._image.get_rect() 
        self._name = "chitrouille"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self._image, (0,0)) 

class Cerftete(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("images/cerf-tete.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self._image.get_rect() 
        self._name = "cerf-tête"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self._image, (0,0))

class Hector(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("images/hector.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self._image.get_rect() 
        self._name = "hector"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self._image, (0,0))

class Perforatrice(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("images/perforatrice.gif")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self._image.get_rect() 
        self._name = "perforatrice"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self._image, (0,0))


class Perforatrice2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("images/perforatrice2.png")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self._image.get_rect() 
        self._name = "perforatrice?"
        self._personality = None
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self._image, (0,0))

class MathsTeacher(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = pygame.image.load("")
        #self._image = pygame.transform.scale(self._image, (x,y))
        self.rect = self._image.get_rect() 
        self._name = "Mr. Coulangênant"
        self._personality = "boss"
        self._hp = 0
        self._atk = 10
        self._dfs = 10
    def render(self, surface):
        surface.blit(self._image, (0,0)) 
