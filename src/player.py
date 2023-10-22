import pygame
import json
from pygame import *
import time

from animation import AnimateSprite


class Entity(AnimateSprite):

    def __init__(self, name, x, y):
        self.name = name
        super().__init__(self.name)

        self.image = self.get_image(0, 0)  # Prend l'image en 0, 0
        self.image.set_colorkey([0,255,0])
        self.rect = self.image.get_rect()
        self.position = [x, y]  # Détermine la position du joueur sur l'écran
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 3 #Default: 3
        self.can_moove = True

    def get_name(self):
        return self.name

    def update_sprite(self, name):
        return super().update_sprite(name)
    
    def get_suicide_permission(self):
        return self.allow_suicide
    
    def change_suicide_permission(self, yes_no: bool):
        self.allow_suicide = yes_no

    def change_name(self, name):
        self.name = name
        
    def save_location(self): self.old_position = self.position.copy()

    def get_damage(self, damage):
        self.HP -= damage

    def allow_moove(self, yes_no: bool):
        self.can_moove = yes_no

    def move_right(self):
        if self.can_moove:
            self.change_animation('right')
            self.position[0] += self.speed  # Décaler de 3 pixel vers la droite
            return 'right'
            
    def move_left(self):
        if self.can_moove:
            self.change_animation('left')
            self.position[0] -= self.speed  # Décaler de 3 pixel vers la gauche
            return 'left'

    def move_up(self):
        if self.can_moove:
            self.change_animation('up')
            self.position[1] -= self.speed  # Décaler de 3 pixel vers le haut
            return 'up'

    def move_down(self):
        if self.can_moove:
            self.change_animation('down')
            self.position[1] += self.speed  # Décaler de 3 pixel vers le bas
            return 'down'

    def update(self):
        if self.can_moove:
            self.rect.topleft = self.position
            self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom


class Player(Entity):

    def __init__(self, name = 'amelia'):
        super().__init__(name, 0, 0)
        self.exp = 0

    def change_name(self, name):
        super().change_name(name)
        super().update_sprite(name)
    
    def get_name(self):
        return super().get_name()
    
    def change_suicide_permission(self, yes_no: bool):
        return super().change_suicide_permission(yes_no)
    






class NPC(Entity):
    def __init__(self, name, nb_points,dialog):
        super().__init__(name, 0, 0)
        self.nb_points = nb_points
        self.dialog = dialog
        self.points = []
        self.name = name
        self.speed = 1  # Vitesse du NPC, possibilité de le passer en paramètre pour faire une vitesse diferente en fonction des NPC, attention dans la fonction collision, dans map, la vitesse est remise à 1 après collision
        self.current_point = 0
        self.orientation = 'down'
        self.state = 1


    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def move(self):
        current_point = self.current_point
        target_point = self.current_point + 1

        if target_point >= self.nb_points:
            target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]
        if self.speed == 0:
            pass
        elif current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.orientation = self.move_down()
        elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.orientation = self.move_up()
        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.orientation = self.move_right()
        elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.orientation = self.move_left()

        if self.rect.colliderect(target_rect):
            self.current_point = target_point

    def load_points(self, tmx_data):
        for num in range(1, self.nb_points + 1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)

    def get_orientation(self):
        return self.orientation
    
    def get_name(self):
        return self.name
