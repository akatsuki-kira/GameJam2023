
import pygame
from pygame.locals import *
from sys import exit
import random

touches=[
    ("A",pygame.K_a),
    ("B",pygame.K_b),
    ("C",pygame.K_c),
    ("D",pygame.K_d),
    ("E",pygame.K_e),
    ("F",pygame.K_f),
    ("G",pygame.K_g),
    ("H",pygame.K_h),
    ("I",pygame.K_i),
    ("J",pygame.K_j),
    ("K",pygame.K_k),
    ("L",pygame.K_l),
    ("M",pygame.K_m),
    ("N",pygame.K_n),
    ("O",pygame.K_o),
    ("P",pygame.K_p),
    ("Q",pygame.K_q),
    ("R",pygame.K_r),
    ("R",pygame.K_s),
    ("T",pygame.K_t),
    ("U",pygame.K_u),
    ("V",pygame.K_v),
    ("W",pygame.K_w),
    ("X",pygame.K_x),
    ("Y",pygame.K_y),
    ("Z",pygame.K_z),
    
]

def main(screen):
    pygame.init()
    font = pygame.font.SysFont('Arial', 30)
    pygame.display.set_caption("Bagarre!")
    boxcontour = pygame.Surface((800,300))
    boxcontour.fill((255,255,255))
    box = pygame.Surface((780,280)) 

    clock = pygame.time.Clock()

    battleisrunning=True
    firsttime = True
    vieperso = 3
    vieennemi = 10
    dt = 0
    dmax = 2.5

    while battleisrunning:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        if firsttime:
            touche = random.choice(touches)
            text = font.render(f"Appuie sur la touche {touche[0]}!!",True,(255,255,255),(0,0,0))
            firsttime = False

        event = pygame.event.wait()
        if event.type == KEYDOWN:
            if event.key != touche[1]:
                text = font.render("WRONG!",True,(255,255,255),(0,0,0))
                dmax = round(dmax+0.1, 3)
                vieperso-=1
                screen.blit(boxcontour, (0,460))
                screen.blit(box, (10,470))
                screen.blit(text,(20,480))
                pygame.display.update()
                pygame.time.wait(1000)
                dt = clock.tick(60)
                touche = random.choice(touches)
                text = font.render(f"Appuie sur la touche {touche[0]}!!",True,(255,255,255),(0,0,0))
            else:
                dt = clock.tick(60) / 1000
                print(f"{dt}///{dmax}")
                if dt<dmax:
                    text = font.render("Nice!",True,(255,255,255),(0,0,0))
                    vieennemi-=1
                    dmax = round(dmax-0.2, 3)
                else:
                    text = font.render("Tu as mis trop de temps!",True,(255,255,255),(0,0,0))
                    vieperso-=1
                    dmax = round(dmax+0.1, 3)
                
                screen.blit(boxcontour, (0,460))
                screen.blit(box, (10,470))
                screen.blit(text,(20,480))
                pygame.display.update()
                pygame.time.wait(1000)
                dt = clock.tick(60)
                touche = random.choice(touches)
                text = font.render(f"Appuie sur la touche {touche[0]}!!",True,(255,255,255),(0,0,0))

        if vieperso<=0 or vieennemi<=0:
            battleisrunning=False
            break

        screen.blit(boxcontour, (0,460))
        screen.blit(box, (10,470))
        screen.blit(text,(20,480))
        pygame.display.update()





    return (vieperso, vieennemi)
