import pygame
import sys

#JUGADOR PRINCIPAL
Player_image = pygame.image.load("cars/modern_red.png").convert_alpha()

#ENEMIGOS
enemy_modern_blue = pygame.image.load("cars/modern_blue.png").convert_alpha()
enemy_super_cyan = pygame.image.load("cars/super_cyan.png").convert_alpha()
enemy_kar_pink = pygame.image.load("cars/kar_pink.png").convert_alpha()
enemy_modern_green = pygame.image.load("cars/modern_green.png").convert_alpha()
enemy_modern_pink = pygame.image.load("cars/modern_pink.png").convert_alpha()
hueco = pygame.image.load("cars/hueco.png").convert_alpha()