import pygame
import sys
import random
import pygame.mask
import math

pygame.init()

screen_size = pygame.display.set_mode([800, 500])
clock = pygame.time.Clock()

background = pygame.image.load("./Img/Carretera.png").convert()
background_width = background.get_width()

from Player import *
from enemy import *
from settings import *

settings = Settings()
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
enemy_sprites = pygame.sprite.Group()
enemy_timer = 0

aux = False
collision_count = 0

def crash(value):
    global aux, collision_count

    if value == True and aux == False:
        aux = True
        collision_count += 1

    if value == False and aux == True:
        aux = False

    if collision_count >= settings.num_vidas:
        print("GAME OVER")
        sys.exit()

# LÓGICA DEL JUEGO
def main_juego():
    scroll = 0  # Posición vertical inicial de la carretera
    game_over = False
    enemy_timer = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            player.process_event_car(event)
        player.move_car()

        # Desplazamiento de la carretera    
        screen_size.blit(background, (0, scroll))
        screen_size.blit(background, (0, scroll - background.get_height()))  # Copia desplazada

        scroll += 5

        if scroll >= background.get_height():
            scroll = 0  # Restablece la posición cuando alcanza el tamaño de la imagen de fondo

        # Crea los enemigos
        enemy_timer += 1
        if enemy_timer >= settings.time_enemy:
            enemy_timer = 0
            lane = random.choice([settings.carril_1, settings.carril_2, settings.carril_3, settings.carril_4])
            enemy = enemy_car(random.randint(1, 5), lane)
            all_sprites.add(enemy)
            enemy_sprites.add(enemy)

        # Mueve los enemigos
        for enemy in enemy_sprites:
            enemy.move()

        # Colisiones
        for enemy in enemy_sprites:
            car_collision_list = pygame.sprite.spritecollide(player, enemy_sprites, False, pygame.sprite.collide_mask)
            if car_collision_list:
                crash(True)
            else:
                crash(False)

        # Dibuja los sprites
        all_sprites.draw(screen_size)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()