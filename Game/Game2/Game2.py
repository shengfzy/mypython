background_image_filename = 'Resources/sushiplate.jpg'
mouse_image_filename = 'Resources/fugu.png'

import pygame, os
from pygame.locals import *
from sys import exit
os.chdir(r'C:\Users\沈恺\OneDrive\mypython\Game\Game2')

pygame.init()

print(pygame.display.list_modes())

screen = pygame.display.set_mode((640, 480), RESIZABLE, 32)
pygame.display.set_caption('Hello World!')

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
mouse_cursor2 = pygame.image.load(mouse_image_filename).convert_alpha()

cursor2_x, cursor2_y = 0,0
move_x, move_y = 0,0
FULL_SCREEN = False
SCREEN_SIZE = (640,480)

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption('Window resized to ' + str(event.size))
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            move_x = -1
        elif event.key == K_RIGHT:
            move_x = 1
        elif event.key == K_UP:
            move_y = -1
        elif event.key == K_DOWN:
            move_y = 1
        elif event.key == K_f:
            FULL_SCREEN = not FULL_SCREEN
            if FULL_SCREEN:
                screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
        else:
            pass
    elif event.type == KEYUP:
        move_x, move_y = 0,0
    
    # screen.blit(background,(0,0))
    # x, y = pygame.mouse.get_pos()
    # x -= mouse_cursor.get_width()/2
    # y -= mouse_cursor.get_height()/2
    
    # screen.blit(mouse_cursor,(x,y))
    
    # cursor2_x += move_x
    # cursor2_y += move_y
    
    # screen.blit(mouse_cursor2,(cursor2_x,cursor2_y))
    
    screen_width, screen_height = SCREEN_SIZE
    for y1 in range(0, screen_height, background.get_height()):
        for x1 in range(0, screen_width, background.get_width()):
            screen.blit(background, (x1,y1))
    
    pygame.display.update()

