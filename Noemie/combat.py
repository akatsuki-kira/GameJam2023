from classes_ennemis import Robarbre, Fantomaths, Chitrouille
import pygame
from pygame.locals import *
import sys
import random
# from tkinter import filedialog
# from tkinter import *


WIDTH, HEIGHT = 1920,1080

class CombatApp:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (WIDTH,HEIGHT)
        
 
    def on_init(self):
        pygame.init()
        self.font = pygame.font.SysFont('Cheese Burger', 30)

        self.text_renders = [self.font.render(text, True, (0, 0, 255)) for text in texts_debut]
        pygame.display.set_caption("Fuyez les maths approfondies!!")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._color1 = pygame.Color(255, 0, 0)
        #self._display_surf.fill(self._color1)
        
        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")
            x, y = pygame.mouse.get_pos()
            print(x,y)
            if x>1260 and x<1730 and y>610 and y<765:
                demarrage._began = True

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        COUNT = 0
        pygame.display.set_caption("Fuyez les maths approfondies!!")


        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            
    
            if not demarrage._began:
                demarrage.update()
                demarrage.render(self._display_surf)
                print("update")

            if demarrage._began:
                self._display_surf.fill((0,0,0))
                pygame.draw.rect(self._display_surf, (0, 255, 0), self.text_box_debut, width=2)
                if pygame.key.get_pressed()[pygame.K_SPACE] and space_released:
                    space_released = False
                    index = (index + 1) if (index + 1) != len(self.text_renders) else 0
                elif not pygame.key.get_pressed()[pygame.K_SPACE]:
                    space_released = True
            else:
                index = -1

            if index != -1:
                self._display_surf.blit(self.text_renders[index], (0, 0))


            pygame.display.flip()
            pygame.display.update()
            COUNT +=1
            pygame.time.Clock().tick(24)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    demarrage = Startscreen()
    theApp.on_execute()

