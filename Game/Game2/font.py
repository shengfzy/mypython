# -*- coding: utf-8 -*-
import pygame,os
from pygame.locals import *
from sys import exit

os.chdir(r'C:\Users\沈恺\OneDrive\mypython\Game\Game2')

SCREEN_SIZE = (640,480)
background_image_filename = 'Resources/sushiplate.jpg'
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont('华文宋体', 40)
text_surface = font.render(u'你好', True, (0,0,0))

x = 0
y = (480 - text_surface.get_height())/2

background = pygame.image.load(background_image_filename).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background,(0,0))
    
    x -= 0.1
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()
        
    screen.blit(text_surface,(x,y))
    
    pygame.display.update()