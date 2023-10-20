import pygame
from player import Player
class DialogBox:

    X_POSITION = 20
    Y_POSITION = 480

    def __init__(self):
        self.box = pygame.image.load('dialogs/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (700, 200))
        self.texts = []
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font('dialogs/dialog_font.ttf', 29)
        self.reading = False
        self.player = Player()

    def get_text_index(self):
        return int(self.text_index)

    def execute(self, dialog=[], name = ''):
        if self.reading:
            if self.text_index < 0:
                self.text_index = 0
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog
            self.name = name

    def render(self, screen):
        if self.reading:  # Si le text est en cour de lecture alors on à le droit d'afficher la boite de dialogue
            self.letter_index += 1

            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index
            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (255, 255, 255))  # Paramettre: quel text, utiliser des Allias ?, couleur en RGB
            screen.blit(text, (self.X_POSITION + 15, self.Y_POSITION + 80))

            name = self.font.render(self.name, False, (255, 255, 255))
            screen.blit(name, (self.X_POSITION + 10, self.Y_POSITION + 10))


    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            # fermer le dialogue
            self.reading = False
            self.text_index = -1
