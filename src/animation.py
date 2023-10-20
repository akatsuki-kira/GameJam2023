import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'sprites/{name}.png')  # Fichier image du joueur
        self.animation_index = 0 # Détermine laquel des 3 images de l'entité on veut aller chercher.
        self.clock = 0
        self.images = {
            'down': self.get_images(0),
            'left': self.get_images(32),
            'right': self.get_images(64),
            'up': self.get_images(96),
            'suicide': self.get_multiple(0, 128)
        }
        self.speed = 3 # Vitesse du joueur

    def update_sprite(self, name):
        self.sprite_sheet = pygame.image.load(f'sprites/{name}.png')
        self.images = {
            'down': self.get_images(0),
            'left': self.get_images(32),
            'right': self.get_images(64),
            'up': self.get_images(96),
            'suicide': self.get_multiple(0, 128)
        }
        return name

    def change_animation(self, name):
        if name == 'suicide':
            self.image = self.images[name][self.animation_index]
            self.image.set_colorkey([0, 255, 0])
            self.clock += self.speed*5 # Détermine la vitesse de l'animation en fonction de la vitesse en limitant le nombre de changement d'image / seconde

            if self.clock >= 250:

                self.animation_index += 1 #Permet de passer à l'image suivante

                if self.animation_index >= 7:
                    return True
                if self.animation_index >= len(self.images[name]):
                    self.animation_index = 0
                self.clock = 0
        else:
            self.image = self.images[name][self.animation_index]
            self.image.set_colorkey([0, 255, 0])
            self.clock += self.speed*5 # Détermine la vitesse de l'animation en fonction de la vitesse en limitant le nombre de changement d'image / seconde

            if self.clock >= 100:

                self.animation_index += 1 #Permet de passer à l'image suivante

                if self.animation_index >= len(self.images[name]):
                    self.animation_index = 0
                self.clock = 0
        return False
            

    def stop_animation(self, name = 'down'):
        self.image = self.images[name][1]
        self.image.set_colorkey([0, 255, 0])
        self.clock += self.speed*5 # Détermine la vitesse de l'animation en fonction de la vitesse en limitant le nombre de changement d'image / seconde

        if self.clock >= 0:

            self.animation_index += 1 #Permet de passer à l'image suivante

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0
            self.clock = 0
        return name

    def get_images(self, y):
        images = []

        for i in range(0, 3):
            x = i*32
            image = self.get_image(x, y)
            images.append(image)
        return images
    
    def get_multiple(self, x, y):
        images = []

        for j in range(0, 3):
            y = y + 32*j
            for i in range(0, 3):
                x = i*32
                image = self.get_image(x, y)
                images.append(image)
        return images


    def get_image(self, x, y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
    

