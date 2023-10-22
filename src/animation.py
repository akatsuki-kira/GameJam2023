import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'sprites/{name}.png')  # Fichier image du joueur
        self.animation_index = 0 # Détermine laquel des 3 images de l'entité on veut aller chercher.
        self.clock = 0
        if name == 'amelia' or name == 'boss':
            self.images = {
                'down': self.get_images(0),
                'right': self.get_images(48),
                'left': self.get_images(96),
                'up': self.get_images(144),
            
        }
        else:
            self.images = {
                'down': self.get_images(0),
                'right': self.get_images(32),
                'left': self.get_images(64),
                'up': self.get_images(96),
        }
        self.speed = 3 # Vitesse du joueur

    def update_sprite(self, name):
        self.sprite_sheet = pygame.image.load(f'sprites/{name}.png')
        if name == 'amelia' or name == 'boss':
            self.images = {
                'down': [pygame.transform.scale(i, (27,40)) for i in self.get_images(0)],
                'right': [pygame.transform.scale(i, (27,40)) for i in self.get_images(48)],
                'left': [pygame.transform.scale(i, (27,40)) for i in self.get_images(96)],
                'up': [pygame.transform.scale(i, (27,40)) for i in self.get_images(144)],
        }
        else:
            self.images = {
                'down': self.get_images(0),
                'right': self.get_images(32),
                'left': self.get_images(64),
                'up': self.get_images(96),
            }
            
        return name

    def change_animation(self, name):
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
        if self.name != 'amelia':
            for j in range(0, 3):
                y = y + 32*j
                for i in range(0, 3):
                    x = i*32
                    image = self.get_image(x, y)
                    images.append(image)
        else:
            for j in range(0, 3):
                y = y + 32*j
                for i in range(0, 3):
                    x = i*48
                    image = self.get_image(x, y)
                    images.append(image)
        return images


    def get_image(self, x, y):
        if self.name == 'amelia' or self.name == 'boss':
            image = pygame.Surface([32,48])
            image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 48))
        else:
            image = pygame.Surface([32,32])
            image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
    

