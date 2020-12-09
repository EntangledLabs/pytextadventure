#Imports. Optimize imports for only needed modules
import pygame, sys
from pygame.locals import *

#Global variables.
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

#Color definitions
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

#Initialization. Make sure to optimize inits for specific needed modules.
pygame.init()

#Creating the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Text Adventure Game')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLACK)
screen.blit(background, (0, 0))
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.blit(background, (0, 0))
    pygame.display.flip()
