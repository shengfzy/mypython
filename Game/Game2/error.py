import pygame

try:
    screen = pygame.display.set_mode((640,-1))
except pygame.error as e:
    print ("Can't create the display :-(")
    print(e)
