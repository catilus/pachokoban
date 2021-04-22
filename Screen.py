import pygame
from pygame.locals import *

class Screen:

    def __init__(self, width, height):
        self.width = width
        self.heigth = height
        self.window = pygame.display.set_mode((width,height))   # screen size

    def shows(self, background_color, levelfile):
        self.window.fill(background_color)  # screen background color
        pygame.display.update() # updates portions of the screen
        #pygame.display.flip()

        