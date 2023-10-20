from dataclasses import dataclass
import pygame
import pytmx
import pyscroll
from player import *
import json
from dialogs import DialogBox
from random import choice

@dataclass
class Portal:
    from_world: str  # Monde avant TP
    origin_point: str  # Point d'origine de la téléportation (porte de maison, téléporteur)
    target_world: str  # Monde après TP
    teleport_point: str  # Point d'arrivé après TP

@dataclass
class Interaction:
    name: str
    zone: pygame.Rect
    dialogs: list #[str]


@dataclass  # La classe "Map" vas automatiquement récupérer des élement et ne sera pas a titre fonctionnel directement
class Map:
    name: str
    walls: list #[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list #[Portal]
    npcs: list #[NPC]
    interactions: list #[Interaction]
    player_sprite: str

class MapManager:

    def __init__(self, screen, player):
        self.maps = dict()  # "house" -> Map("house", walls, group)
        self.screen = screen
        self.player = player
        with open(r'src/data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.current_map = data[2]  # Définie la map actuel à partir du fichier data.json

        # Paramettre d'affichage de la carte
        self.press_m = False

        # On enregistre la liste des mondes et les points de tp respectifs de ceux-ci
        self.register_map("White_Space", portals=[
            Portal(from_world="White_Space", origin_point="leave_white_space", target_world ="house_1", teleport_point="origin")
        ], npcs=[])



        self.teleport_player_at_checkpoint()
        self.teleport_npcs()

    def check_npc_collisions(self, dialog_box):
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is NPC: 
                self.player.allow_moove(False)
                dialog_box.execute(sprite.dialog, sprite.name)
                if dialog_box.get_text_index() == -1:
                    self.player.allow_moove(True)
        return True
    
    def check_interaction_collisions(self, dialog_box):
        for interaction in self.get_interaction():
            if self.player.feet.collidelist([interaction.zone]) > -1:
                self.player.allow_moove(False)
                if interaction.dialogs[0] == 1:
                    dialog_box.execute(interaction.dialogs[2], interaction.dialogs[0])
                    if dialog_box.get_text_index() == -1:
                        self.player.allow_moove(True)
                else:
                    dialogue = [choice(interaction.dialogs[2])]
                    dialog_box.execute(dialogue, interaction.dialogs[0])
                    if dialog_box.get_text_index() == -1:
                        self.player.allow_moove(True)


    def register_map(self, name, portals=[], npcs=[], sprite_name = 'OMORI', allow_suicide = True):
        # Charger la carte en format TMX
        tmx_data = pytmx.util_pygame.load_pygame(f"map/{name}.tmx") # Vas chercher le fichier en fonction du nom de la carte (name)
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1.8  # Définie le zoom de la carte

        # Définir une liste qui vas stocker les rectangles de collisions
        walls = []
        interactions = []
        # Vérifie les obj dans lesquels le joueur entre
        for obj in tmx_data.objects:
            """
            if obj.name:
                if obj.name.startswith('NPC_'):
                    with open(f"src\data\dialogues\{name}.json", 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        dialogue = data[obj.name[4:]]
                    interactions.append(Interaction(zone=pygame.Rect(obj.x, obj.y, obj.width, obj.height), dialogs=dialogue, name = obj.name))
            """
            if obj.col == True:
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))  # Définis comme un mur les objets an fonct° de leurs positions et leurs tailles




        # Dessiner le groupe de calque
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        group.add(self.player)

        # Récuperer tout les NPC pour les ajouter au groupe
        for npc in npcs:
            group.add(npc)

        # Crée un objet map
        self.maps[name] = Map(name, walls, group, tmx_data, portals, npcs, interactions, sprite_name) # la vaiable maps contient la LISTE des monde chargé

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group # Vas renvoyer un objet map

    def get_interaction(self): return self.get_map().interactions #Renvoie la liste d'interactions

    def get_walls(self): return self.get_map().walls # Récupère les murs de la map

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def teleport_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs

            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def check_collision(self):
        #portails
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)
                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)
                    self.player.change_name(self.get_map().player_sprite)
                    self.player.change_suicide_permission(self.get_map().allow_suicide)
                    pygame.mixer.stop() 
        #collision
        for sprite in self.get_group().sprites(): # Pour toute les entité:

            if type(sprite) is NPC:
                if sprite.feet.colliderect(self.player.rect):
                    sprite.speed = 0
                    sprite.stop_animation(sprite.get_orientation())
                else:
                    sprite.speed = 1

            if sprite.feet.collidelist(self.get_walls()) > -1:  # On vérifie que les pied du joueur entre en collision avec un des murs de la liste
                sprite.move_back()

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x  # Remplace la position en x du joueur par les coordonée en x du point de téléportation
        self.player.position[1] = point.y  # Remplace la position en y du joueur par les coordonée en ydu point de téléportation
        self.player.save_location()

    def teleport_player_at_checkpoint(self):
        with open(r'src/data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.player.position[0] = data[0]  # Remplace la position en x du joueur par les coordonée en x sauvegardé
            self.player.position[1] = data[1]  # Remplace la position en y du joueur par les coordonée en y sauvegardé
            self.player.position[1] = data[1]  # Remplace la position en y du joueur par les coordonée en y sauvegardé
        self.player.save_location()

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)  # Place la caméra sur le centre du joueur
        self.player.change_name(self.get_map().player_sprite)

    def render_map(self, screen):
        if self.press_m:  # Affiche la carte du monde actuelle
            # Afficher sur l'écran la carte en prenant en paramettre la carte actuelle, activé en apuyant sur m
            screen.blit(pygame.transform.scale(pygame.image.load(f'cartes/Carte_{self.current_map}.png'), (700, 700)), (250, 10))
        self.press_m = False

    def update(self):
        self.get_group().update()
        self.check_collision()

        for npc in self.get_map().npcs:
            npc.move()

