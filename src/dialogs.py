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
        self.font = pygame.font.Font('dialogs/dialog2.otf', 23)
        self.reading = False
        self.player = Player()

    def get_text_index(self):
        return int(self.text_index)

    def execute(self, dialog=[], name = '', func = None):
        if self.reading:
            if self.text_index < 0:
                self.text_index = 0
            self.next_text(name)
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog
            self.name = name

    def render(self, screen):
        if self.reading:  # Si le texte est en cours de lecture alors on a le droit d'afficher la boîte de dialogue
            self.letter_index += 1
            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index - 1
            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            name = self.font.render(self.name, False, (255, 255, 255))
            screen.blit(name, (self.X_POSITION + 10, self.Y_POSITION + 10))

            max_line_length = 60  # Nombre maximal de caractères par ligne
            text_to_render = self.texts[self.text_index][0:self.letter_index]

            lines = []
            current_line = ""
            for word in text_to_render.split():
                if len(current_line) + len(word) + 1 <= max_line_length:
                    if current_line:
                        current_line += " "
                    current_line += word
                else:
                    lines.append(current_line)
                    current_line = word

            if current_line:
                lines.append(current_line)

            for i, line in enumerate(lines):
                text = self.font.render(line, False, (255, 255, 255))
                screen.blit(text, (self.X_POSITION + 15, self.Y_POSITION + 70 + i * 30))




    def next_text(self, name, func = None):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            # fermer le dialogue
            self.reading = False
            self.text_index = -1

            # On appelle la fonction
