import pygame
from player import Player
import map
from dialogs import DialogBox

class Game:

    def __init__(self):
        # Crée la fenètre du jeu
        self.screen = pygame.display.set_mode((1200,720)) 
        pygame.display.set_caption("GameJam2023")  # Renomme la fenêtre 

        # Generer un joueur
        self.player = Player()  # Détermine la position du joueur
        self.map_manager = map.MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()
        self.player.change_name(self.map_manager.get_map().player_sprite)


    def handle_input(self, mouvement):  # Déplacement du joueur
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_z]:  # Haut
            self.player.move_up()
            return 'up'
        elif pressed[pygame.K_d]:  # Droite
            self.player.move_right()
            return 'right'
        elif pressed[pygame.K_q]:  # Gauche
            self.player.move_left()
            return 'left'
        elif pressed[pygame.K_s]:  # Bas
            self.player.move_down()
            return 'down'
        elif pressed[pygame.K_m]:
            self.map_manager.press_m = True
            return mouvement    
        else:
            return self.player.stop_animation(name = mouvement)

    def update(self):
        self.map_manager.update()

    def run(self):

        clock = pygame.time.Clock()
        mouvement = 'down'

        # Boucle du jeu:
        running = True 

        #Initialisation du jeu:
        #pygame.display.set_icon(pygame.image.load("SmallLogo.png").convert())
        for npc in self.map_manager.get_map().npcs: #On initialise la position de tout les NPC vers le bas.
            npc.stop_animation('down')

        

        while running:  # Tant que running = True:
            self.player.save_location()
            mouvement = self.handle_input(mouvement) # Enregistre les entrée de main du joueur
            self.update()  # Update de la position du joueur
            self.map_manager.draw()  # Dessine la carte et centre la caméra
            self.dialog_box.render(self.screen)

            self.map_manager.render_map(self.screen)
            
            pygame.display.flip()

            for event in pygame.event.get():  # Liste des évènement
                if event.type == pygame.QUIT:  # Vérifie si l'utilisateur à tenter de fermer la fenètre avec la croix rouge
                    #self.map_manager.sauvegarde()
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collisions(self.dialog_box)
                        self.map_manager.check_interaction_collisions(self.dialog_box)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.map_manager.sauvegarde()
                        running = False
            clock.tick(60)

            
        pygame.quit()   

class Start_Screen:

    def __init__(self):
        # Crée la fenètre du jeu
        self.screen = pygame.display.set_mode((1200,720))  
        pygame.display.set_caption("Omori 2 - Le retour du jedi.")  # Renome la fenètre "Omori 2 - Le retour du jedi"
        self.texts_debut = [
            "Depuis quelques années, on observe une montée de cas de phobie des mathématiques chez les jeunes étudiants bordelais..",
            "Les scientifiques tentèrent d'expliquer ça... En vain. Pourquoi avaient-ils autant peur ??",
            "Les discours étaient confus, irrationnels... Ils disaient voir des fantômes, avoir la sensation d'être hantés..",
            "Quand tout à coup, une jeune aventurière eut une idée..",
            "En 20XX, dû à un grand scandale à l'échelle internationale, l'Université Sciences et Technologies de Bordeaux ferma ses portes..",
            "Le bâtiment fût laissé en ruines. Cela devint rapidement un endroit considéré comme hanté..",
            "Et si la source de ce mal-être venait des bâtiments de sciences de ce campus abandonné ??",
            "...."]
        self.dialog_box = DialogBox()

    def start_game(self):

        clock = pygame.time.Clock()  
        running = True
        game = Game()
        self.screen.blit(pygame.transform.scale(pygame.image.load(f'images\debut_fondnoir.png'), (1200, 720)), (0, 0))
        index = 0
        while running: 
            pygame.display.flip()
            self.dialog_box.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Vérifie si l'utilisateur à tenter de fermer la fenètre avec la croix rouge
                        running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if index == 7:
                            running = False
                            Game().run()
                        index += 1
                        self.dialog_box.execute(self.texts_debut, "vieux", func=None)

            clock.tick(20) 

        pygame.quit()