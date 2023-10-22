import pygame
from game import Start_Screen

if __name__ == '__main__':
    pygame.init()
    game = Start_Screen()
    game.start_game()