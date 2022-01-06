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