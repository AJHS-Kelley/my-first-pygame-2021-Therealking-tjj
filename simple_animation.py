# siimple Animation with pygame, ryan kelley, 1/6/22, 1:31pm, v0.0

import pygame,sys, time
from pygame.locals import *

# setup pygame
pygame.init()

# setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
WINDOWSURFACE = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32) 
# change WINDOWSURFACE to windowSurface on the line above.  
pygame.display.set_caption('Animation example!')


# setup the direction variables
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# setup color values
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN =(0,255,0)
BLUE = (0, 0, 255)

# setup the box data
b1 = {'rect':pygame.Rect (300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect (200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 ={'rect':pygame.Rect (100, 150, 60, 60), 'color':RED, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# Run the game loop.
while True:
    # Chech for Quit event.
    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            sys.exit()

    WINDOWSURFACE.fill(WHITE)
    # change WINDOWSURFACE to windowSurface on the line above.  

    for b in boxes:
        # moves the data structure.
        if b['dir'] == DOWNLEFT:
                 b['rect'].left -= MOVESPEED
                 b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
                b['rect'].left += MOVESPEED
                b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
                b['rect'].left -= MOVESPEED
                b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
                b['rect'].left += MOVESPEED
                b['rect'].top -= MOVESPEED

        if b['rect'].top < 0:
            # The box has moved passed thE top
            if b['dir'] == UPLEFT:
                b['dir']= DOWNLEFT
            if b['dir'] == UPRIGHT:
                b ['dir'] = DOWNRIGHT
            if b['rect'].bottom > WINDOWHEIGHT:
                # The box has moved passed the bottom 
                if b['dir'] == DOWNLEFT:
                    b['dir']= UPLEFT
                if b['dir'] == DOWNRIGHT: 
                    b ['dir'] = UPRIGHT
            if b['rect'].left < 0:
                    #the box has moved passed the right 
                if b['dir'] == DOWNLEFT:
                    b['dir']= DOWNRIGHT
                if b['dir'] == UPLEFT:
                    b['dir'] = UPRIGHT
            if b['rect'].right > WINDOWWIDTH:
                    # The box has moved past the right 
                    if b['dir'] == DOWNRIGHT:
                        b['dir']= DOWNLEFT
                    if b['dir'] == UPRIGHT:
                        b['dir'] = UPLEFT
            #Draw the box onto the game surface.
            pygame.draw.rect (WINDOWSURFACE, b['color'], b['rect']) # Move this to the left 4 spaces.   
            # change WINDOWSURFACE to windowSurface on the line above.  


            # Draw the window to the screen.
            pygame.display.update()    # This line should 4 spaces from the LEFT MARGIN.
            time.sleep(0.02)           # This line should 4 spaces from the LEFT MARGIN.  