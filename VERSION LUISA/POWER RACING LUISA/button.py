import pygame
import sys


# Carga las imágenes de los botones y el fondo del menú
""" button_image = pygame.image.load("Frame 3.png")
button_hover_image = pygame.image.load("Frame 4.png")
fondo_menu = pygame.image.load("Fondo_Menu.jpg") """
class Button:
    def __init__(self, x, y, width, height,image,hover_image,action):
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action
        self.image = image
        self.hover_image = hover_image
        self.hovered = False  # Nuevo atributo para rastrear el estado de hover

    def draw(self, screen):
        if self.hovered:
            screen.blit(self.hover_image, self.rect.topleft)
        else:
            screen.blit(self.image, self.rect.topleft)

    def handle_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.action()

    def handle_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True  # Mouse está sobre el botón
        else:
            self.hovered = False  #