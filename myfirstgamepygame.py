# My first pygame, Terrance Holland, 11/30/21, 2:15, v0.3

import pygame, sys 
from pygame.locals import*

#start pygame
pygame.init()

#set up the game window.
windowsurface = pygame.display. set_mode ((500, 400),0,32)
pygame.display.set_captain('hello, world!')

#setup color values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0,215,0)
BLUE = ( 0,0, 255)
VIOLET = (125,255,25)

#setup fonts,
basicfonts = pygame.font. sysfont(none, 48)

#setup text.
text = basicFont. render('hello, world', True, WHITE,BLUE)
textReact = text.get_react ()
textReact.centrex = windowSurface.get_react().centerx
textReact.centrex = windowSurface.get_react().centery

 