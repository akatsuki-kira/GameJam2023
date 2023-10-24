from classes_ennemis import Robarbre, Fantomaths, Chitrouille, Cerftete, Hector, Perforatrice, sprites_
import pygame
from dialogs import DialogBox
from pygame.locals import *
import sys
import random
from minigames import quiz,pongv2,bagarre
# from tkinter import filedialog
# from tkinter import *


WIDTH, HEIGHT = 800,800


class CombatApp:
    def __init__(self,ennemi,screen):
        ennemi = ennemi.strip().lower()
        if ennemi=="cerftete":
            self._ennemi = Cerftete()
        elif ennemi=="chitrouille":
            self._ennemi = Chitrouille()
        elif ennemi=="fantomaths":
            self._ennemi = Fantomaths()
        elif ennemi=="hector":
            self._ennemi = Hector()
        elif ennemi=="perforatrice":
            self._ennemi = Perforatrice()
        elif ennemi=="robarbre":
            self._ennemi = Robarbre()
        else:
            return
        
        self.index = 0
        self._autodialog = 10
        self._running = True
        self._count_quiz = 0
        self._nbminijeu = 0
        self._win_minijeu = False
        self._lose_minijeu =False
        self._display_surf = screen
        self._fin_battle = False
        self.size = (WIDTH,HEIGHT)
        self._name = self._ennemi._name
        self._minijeu_encours = False
        self.choix_minijeu = random.choice(["quiz","pong","bagarre"])
        if self.choix_minijeu == "pong":
            self.choix_minijeu = "jouer au pong contre toi!!"
            self._nbminijeu = 1
        elif self.choix_minijeu == "quiz":
            self.choix_minijeu = "voir si tu réussiras son quiz!!"
            self._nbminijeu = 2
        elif self.choix_minijeu == "bagarre":
            self.choix_minijeu = "te casser la gueule ?! \nExplication: Appuie sur la bone touche de plus en plus rapidement pour faire des dégâts à l'ennemi. Sinon, tu perds de la vie!!"
            self._nbminijeu = 3
        
 
    def on_init(self):
        pygame.init()
        self.font = pygame.font.Font('dialogs/dialog2.otf', 23)

        pygame.display.set_caption("Fuyez les maths approfondies!!")
        self._running = True 
        self._intro = True
        self._color1 = pygame.Color(255, 0, 0)
        self.texts_debut = [
            f"{self._name.capitalize()} veut se battre!!",
            f"Il souhaite... {self.choix_minijeu}"
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

        elif not self._minijeu_encours:

            if  event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :

                if self.index == 2:
                    self._intro = False
                    self._minijeu_encours = True
                elif self.index == 5:
                    self._running = False
                
            
                if self._intro:
                    self.dialog_box.execute(self.texts_debut, f"{self._name.capitalize()}")
                elif self._win_minijeu:
                    self.db_win.execute(self.texts_win,f"{self._name.capitalize()}")
                elif self._lose_minijeu:
                    self.db_lose.execute(self.texts_lose,f"{self._name.capitalize()}")
                self.index += 1

            elif  self.index >=2 and self.index <5 and self._autodialog<1:

                self._autodialog+=1
                if self.index == 2:
                    self._intro = False
                    self._minijeu_encours = True
                elif self.index == 5:
                    self._running = False
                
            
                if self._intro:
                    self.dialog_box.execute(self.texts_debut, f"{self._name.capitalize()}")
                elif self._win_minijeu:
                    self.db_win.execute(self.texts_win,f"{self._name.capitalize()}")
                elif self._lose_minijeu:
                    self.db_lose.execute(self.texts_lose,f"{self._name.capitalize()}")
                self.index += 1

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
    
    # --- Intro ---

            if self._intro:
                self._display_surf.fill((50,50,50))
                self.dialog_box.render(self._display_surf)
                self._ennemi._image = pygame.image.load(f"images/{self._name}/{sprites_[COUNT%58]}")
                self._ennemi.render(self._display_surf)

    # --- Minijeux ---

            elif self._minijeu_encours: 

                # Pong -----------

                if self._nbminijeu==1:
                    score1,score2 = pongv2.main(self._display_surf)
                    if score1>=2 or score2>=2:
                        self._win_minijeu = score1>=2
                        self._lose_minijeu = score2 >=2

                        self._fin_battle = True
                        self._minijeu_encours = False
                        self.index = 3
                        self._autodialog=0

                            

                # Quiz ----------

                elif self._nbminijeu==2:
                    self._count_quiz += 1
                    self._win_minijeu, self._lose_minijeu = quiz.main(self._count_quiz)
                    if self._win_minijeu==True or self._lose_minijeu==True:

                        self._fin_battle = True
                        self._minijeu_encours = False
                        self.index = 3
                        self._autodialog=0
                        

                # Bagarre ----------

                else:
                    a,b = bagarre.main(self._display_surf)
                    self._win_minijeu = a>0
                    self._lose_minijeu = b>0
                    if (self._win_minijeu and not self._lose_minijeu) or (self._lose_minijeu and not self._win_minijeu):

                        self._fin_battle = True
                        self._minijeu_encours = False       
                        self.index = 3             
                        self._autodialog=0
            
    # --- Fin minijeu ---

            elif self._fin_battle: 

                self._display_surf.fill((50,50,50))
                if self._win_minijeu:
                    self.db_win.render(self._display_surf)
                elif self._lose_minijeu:

                    self.db_lose.render(self._display_surf)
                self._ennemi._image = pygame.image.load(f"images/{self._name}/{sprites_[COUNT%58]}")
                self._ennemi.render(self._display_surf)                

            pygame.display.flip()
            pygame.display.update()
            COUNT +=1
            pygame.time.Clock().tick(60)
            self.on_loop()
            self.on_render()
        # self.on_cleanup()
        if self._win_minijeu:
            return True
        elif self._lose_minijeu:
            return False

if __name__ == "__main__" :

    theApp = CombatApp("robarbre", pygame.display.set_mode((WIDTH,HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF))
    theApp.on_execute()

