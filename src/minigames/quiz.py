import pygame,random
from tkinter import *
import time
 
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
 
font20 = pygame.font.Font('freesansbold.ttf', 20)

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz")
clock = pygame.time.Clock()
FPS = 30

qst = [
    ("Quel est le sinus de pi/2 ?","1"),
    ("D'où vient la couleur rouge du sang?",("Hémoglobine","l'hémoglobine")),
    ("Si je fais tomber un corps du 10e étage, \nsa trajectoire est...",("Rectiligne","Linéaire")),
    ("La loi des noeuds stipule que la somme des \nintensités allant dans un noeud est...",("Nulle","0")),
    ("Comment écrit-on la molécule de l'éthanol?","C2H6O"),

    ("0.24999999... est la décomposition \ndécimale ______ de 1/4. (compléter)","impropre"),
    ("Le diamant est composé de (atome)...","carbone"),
    ("Quel est le plus grand ensemble de nombres? \n(nom, ou lettre)",("complexes","complexe","c")),

    ("La développeuse des combats a consommé...\n1: De la drogue\n2: 1 litre de monster\n3: Rien, la pauvre n'a pas mangé depuis 2 jours","2"),
]

class Quiz:
    def __init__(self):
        self._done = False
        self._question, self._answer = random.choice(qst)
        self._goodanswer=False
        self._badanswer=False
    
    def handler(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.label_qst = Label(self.root, text=self._question, padx=20, pady=20)
        self.txt_input = Entry(self.root)
        self.button1 = Button(self.root, text = "Confirmer réponse",
                        command = self.confirm, padx=20, pady=20)
        
        self.label_qst.pack()
        self.txt_input.pack()
        self.button1.pack()
        self.root.update()
        print(self._question, self._answer)
        self.root.mainloop()

        

    def confirm(self):
        if self._done:
            self.root.destroy()
        else:
            self._data = self.txt_input.get().lower().strip()
            if isinstance(self._answer,tuple):
                if self._data not in map(lambda x:x.lower().strip(),self._answer):
                    self._badanswer=True
                    self.label_qst['text']="FAUX!"
                else:
                    self._goodanswer=True
                    self.label_qst['text']="Bien joué!"
            else:
                if self._data != self._answer.lower().strip():
                    self._badanswer=True
                    self.label_qst['text']="FAUX!"
                else:
                    self._goodanswer=True
                    self.label_qst['text']="Bien joué!"
            self._done=True
            self.button1['text']="Quitter"
        

# Game Manager
def main(x):
    if x>=2:
        return (False, True)
    q = Quiz()
    q.handler()
    print(q._goodanswer, q._badanswer)
    return (q._goodanswer, q._badanswer)
	

