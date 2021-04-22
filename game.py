import json
import pygame
import pygame.locals

from Screen import *


pygame.init()       # Initializes the display as well as other things

# Loads level structure from .json file
levelfile = json.load(open("level_001.json"))

# Initialize objects
screen = Screen(350, 350)       # screen size in px
screen.shows([255,228,182], levelfile)  


# Event loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:          # Keeps pygame window open unless asked otherwise
            pygame.quit()
            quit()











#pygame.display.quit()      # closes the display, automatically handled when user exits program