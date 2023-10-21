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
     ("What is the sine of pi/2?","1"),
     ("What is the name of the blood cell \nresponsible for its red colour?","Hemoglobin"),
     ("What is the name of the hardest rock?","Diamond"),
     ("What is the 12th periodic element?","Magnesium"),
     ("What is the derivative of 3x^2?","6x"),
     ("Who created a famous algorithm to \ncalculate the GCD of two numbers?","Euclid"),
     ("Who discovered the identity e^{i pi}+1=0?","Euler"),
     ("What do you obtain when you mix H2O and NaCl ?","Salt water"),
     ("What will be your state if \nI throw a 100kg rock at your head?","dead")
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
        self.button1 = Button(self.root, text = "Confirm answer",
                        command = self.confirm, padx=20, pady=20)
        
        self.label_qst.pack()
        self.txt_input.pack()
        self.button1.pack()
        self.root.update()
        print(self._question, self._answer)
        self.root.mainloop()


    def confirm(self):
        self._data = self.txt_input.get().lower().strip()
        if self._data!=self._answer.lower().strip():
            self._badanswer=True
            self.label_qst['text']="WRONG!"
        else:
            self._goodanswer=True
            self.label_qst['text']="That's right!"
        if self._done:
            time.sleep(1)
            self.root.destroy()
        else:
            self._done=True
            self.button1['text']="Leave"


# Game Manager
def main():
    running = True
    q = Quiz()
    q.handler()

    while running:
        screen.fill(BLACK)
        COUNT=0
        if q._goodanswer:	
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            text = font20.render('You won!',GREEN,BLACK)
            textRect = text.get_rect()
            textRect.center = (WIDTH//2, HEIGHT//2)
            screen.fill(GREEN)
            screen.blit(text, textRect)

        elif q._badanswer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            text = font20.render('You lost!',RED,BLACK)
            textRect = text.get_rect()
            textRect.center = (WIDTH//2, HEIGHT//2)
            screen.fill(RED)
            screen.blit(text, textRect)
			

        pygame.display.update()
        COUNT +=1
        # Adjusting the frame rate
        clock.tick(FPS)
	
if __name__=="__main__":
	main()
	pygame.quit
