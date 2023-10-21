import pygame
from pygame.locals import *
import sys
import random
from classes import Startscreen, Player
from dialogs import DialogBox
# from tkinter import filedialog
# from tkinter import *


WIDTH, HEIGHT = 1920,1080

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (WIDTH,HEIGHT)
        
 
    def on_init(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 30)
        self.text_box_debut = pygame.Rect((WIDTH//2)-750, 800, 1500, 200)
        self.index = -1
        self.space_released = True
        self._intro_done = False
        self.texts_debut = [
            "Depuis quelques années, on observe une montée de cas de phobie des mathématiques chez les jeunes étudiants bordelais.",
            "Les scientifiques tentèrent d'expliquer ça... En vain. Pourquoi avaient-ils autant peur?",
            "Les discours étaient confus, irrationnels... Ils disaient voir des fantômes, avoir la sensation d'être hantés.",
            "Quand tout à coup, une jeune aventurière eut une idée.",
            "En 20XX, dû à un grand scandale à l'échelle internationale, l'Université Sciences et Technologies de Bordeaux ferma ses portes.",
            "Le bâtiment fût laissé en ruines. Cela devint rapidement un endroit considéré comme hanté.",
            "Et si la source de ce mal-être venait des bâtiments de sciences de ce campus abandonné?"
            "..."
        ]

        self.text_renders = [self.font.render(text, True, (255,255,255)) for text in self.texts_debut]
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
        COUNT_DEMARRAGE = 0
        pygame.display.set_caption("Fuyez les maths approfondies!!")


        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            
    
            if not demarrage._began:
                demarrage.update()
                demarrage.render(self._display_surf)
                print("update")

            if not self._intro_done:
                print(COUNT_DEMARRAGE, len(self.text_renders))
                if demarrage._began:
                    self._display_surf.fill((0,0,0))
                    pygame.draw.rect(self._display_surf, (255, 255, 255), self.text_box_debut, width=2)
                    if pygame.key.get_pressed()[pygame.K_SPACE] and space_released:
                        space_released = False
                        COUNT_DEMARRAGE+=1
                        index = (index + 1) if (index + 1) != len(self.text_renders) else 0
                    elif not pygame.key.get_pressed()[pygame.K_SPACE]:
                        space_released = True
                        
                else:
                    index = -1

                if index != -1:
                    self._display_surf.blit(self.text_renders[index], ((WIDTH//2)-745, 805))

                if COUNT_DEMARRAGE == len(self.text_renders):
                    self._intro_done = True
                
                    self._display_surf.fill((0,0,0))
                    pygame.time.delay(2000)

                


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

