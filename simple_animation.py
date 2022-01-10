# siimple Animation with pygame, ryan kelley, 1/6/22, 1:31pm, v0.0

import pygame,sys, time
from pygame.locals import *

# setup pygame
pygame.init()

# setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
WINDOWSURFACE = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Animation example!')


# setup the direction variables
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# setup color values
WHITE =(255, 255, 255)
RED = (255, 0, 0)
GREEN =(0,255,0)
BLUE = (0, 0, 255)

# setup the box data
b1 = {'rect':pygame.Rect (300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect (200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
B3 ={'rect':pygame.Rect (100, 150, 60, 60), 'color':RED, 'dir':DOWNLEFT}
BOXES = [B1, B2, B3]

# Run the game loop.
while True:
    # Chech for Quit event.
    for event in pygmae.event.get():
        if event.type == Quit
        pygame.quit()
        sys.exit()

        windowsurface.fill(WHITE)

        for b in boxes:
            # moves the data structure.
            if b['dir'] == DOWNLEFT:
                b['rect'].left. -= MOVESPEED
                b['rect'].top += MOVESPEED
            if b['dir'] == DOWNRIGHT:
                b['rect'].left. += MOVESPEED
                b['rect'].top += MOVESPEED
            if b['dir'] == UPLEFT:
                b['rect'].left. -= MOVESPEED
                b['rect'].top -= MOVESPEED
            if b['dir'] == UPRIGHT:
                b['rect'].left. += MOVESPEED
                b['rect'].top -= MOVESPEED