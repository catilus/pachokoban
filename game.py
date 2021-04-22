## Import packages and classes
import json
import pygame
import pygame.locals

from Screen import *
from Pacho import *

pygame.init()       # Initializes the display as well as other things

## Loads level structure from .json file
levelfile = json.load(open("level_001.json"))

## Initialize objects
screen = Screen(350, 350, background_color=[255,228,182])   # screen width and height are in px

# Display first level
for i in range(0,len(levelfile[0])-1):    # customize this so we don't use integers
    for j in range(0,len(levelfile)):
        position = (i,j)    # save object position
        tile = levelfile[i][j]     # read object to draw
        screen.shows(tile, position)   # show objects on screen

        # Initializes pacho object with its position
        if tile == 'p':
            pacho = Pacho(tile, position)

## Event loop.
while True:
    for event in pygame.event.get():
        
        # If user presses keyboard touch
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacho.modifyPosition(x_move=0, y_move=-1)
                screen.shows('p', pacho.position)
        
        if event.type == QUIT:          # Keeps pygame window open unless asked otherwise
            pygame.quit()
            quit()


#pygame.display.quit()      # closes the display, automatically handled when user exits program