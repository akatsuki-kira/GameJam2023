from classes_ennemis import Robarbre, Fantomaths, Chitrouille, sprites_
import pygame
from dialogs import DialogBox
from pygame.locals import *
import sys
import random
from minigames import pong,quiz,pongv2
# from tkinter import filedialog
# from tkinter import *


WIDTH, HEIGHT = 800,800


class CombatApp:
    def __init__(self,ennemi):
        self.index = 0
        self._running = True
        self._nbminijeu = 0
        self._win_minijeu = False
        self._lose_minijeu =False
        self._display_surf = None
        self._fin_battle = False
        self.size = (WIDTH,HEIGHT)
        self._name = ennemi._name
        self._minijeu_encours = False
        self.choix_minijeu = random.choice(["pong",])#"quiz","bagarre"
        if self.choix_minijeu == "pong":
            self.choix_minijeu = "jouer au pong contre toi"
            self._nbminijeu = 1
        elif self.choix_minijeu == "quiz":
            self.choix_minijeu = "voir si tu réussiras son quiz"
            self._nbminijeu = 2
        elif self.choix_minijeu == "bagarre":
            self.choix_minijeu = "te casser la gueule ?"
            self._nbminijeu = 3
        
 
    def on_init(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 30)

        pygame.display.set_caption("Fuyez les maths approfondies!!")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True 
        self._intro = True
        self._color1 = pygame.Color(255, 0, 0)
        self.texts_debut = [
            f"{self._name.capitalize()} veut se battre!!",
            f"Il souhaite... {self.choix_minijeu}!!"
        ]
        self.texts_win = [
            random.choice([
                "\"Pouah! Tu as gagné! Bien joué, heheh.\" ",
                "\"Décidément...\" ",
                "\"De toute façon, c'est trop simple.\" ",
                "\"T'aurais au moins pu faire genre...\" ",
                "\"A la prochaine!\" ",
                "\"C'est sûr que les cours de Guilhem sont + durs...\" ",
                "\"Non mais oh?\" ",
                "\"Bj ma quoicoubaka heheheha t'as les cramptapagnans xD\" "
            ]),
            f"Tu as gagné contre {self._name}!!"
        ]
        self.texts_lose = [
            random.choice([
                "\"YAYYYYYYYY!!!!\" ",
                "\"A la prochaine!\" ",
                "\"Pourtant c'était censé être facile..\" ",
                "\"MDR allez salut...\" ",
                "\"Oh le big quoicouflop sucré au seum!!!\" "
            ]),
            f"Tu as perdu contre {self._name}!!"
        ]
        self.dialog_box = DialogBox() 
        self.db_win = DialogBox()
        self.db_lose = DialogBox()       
        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self._minijeu_encours:
                if self.index == 2:
                    self._intro = False
                    self._minijeu_encours = True
                elif self.index == 5:
                    self._running = False
                self.index += 1
                print(self.index)
                if self._intro:
                    self.dialog_box.execute(self.texts_debut, f"{self._name.capitalize()}")
                elif self._win_minijeu:
                    self.db_win.execute(self.texts_win,f"{self._name.capitalize()}")
                elif self._lose_minijeu:
                    self.db_lose.execute(self.texts_lose,f"{self._name.capitalize()}")

        print(self.index)

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
    
            if self._intro:
                self._display_surf.fill((50,50,50))
                self.dialog_box.render(self._display_surf)
                rb._image = pygame.image.load(f"images/{self._name}/{sprites_[COUNT%58]}")
                rb.render(self._display_surf)
            elif self._minijeu_encours: 
                if self._nbminijeu==1:
                    score1,score2 = pongv2.main(self._display_surf)
                    if score1>=2 or score2>=2:
                        self._minijeu_encours = False
                        self._fin_battle = True
                        self.index = 3
                        if score1 > score2:
                            self._win_minijeu = True
                        else:
                            self._lose_minijeu = True
                elif self._nbminijeu==2:
                    quiz.main()
                else:
                    self._running=False
            elif self._fin_battle:
                self._display_surf.fill((50,50,50))
                if self._win_minijeu:
                    self.db_win.render(self._display_surf)
                elif self._lose_minijeu:
                    self.db_lose.render(self._display_surf)
                rb._image = pygame.image.load(f"images/{self._name}/{sprites_[COUNT%58]}")
                rb.render(self._display_surf)                

            pygame.display.flip()
            pygame.display.update()
            COUNT +=1
            pygame.time.Clock().tick(60)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    rb = Robarbre()
    fm = Fantomaths()
    ct = Chitrouille()
    theApp = CombatApp(random.choice([rb,fm,ct]))
    theApp.on_execute()

