import pygame
from pygame.locals import *

class Screen:

    def __init__(self, width, height):
        self.width = width
        self.heigth = height
        self.window = pygame.display.set_mode((width,height))   # screen size

    def shows(self, background_color, levelfile):
        self.window.fill(background_color)  # screen background color
        pygame.display.set_caption("Pachokoban")    # sets window caption
        #pygame.display.update() # only update portions of the screen

        # Display tiles from levelfile
        tile_size = 50
        
        for i in range(0,6):    # customize this so we don't use integers
            for j in range(0,7):
                position = (i,j)    # save object position
                tile = levelfile[i][j]     # read object to draw

                if tile == 'w':
                    tile_image = pygame.image.load("tiles/wall-yellow.png")
                    self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))

                elif tile == 's':
                    tile_image = pygame.image.load("tiles/spot-yellow.png")
                    self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))

                elif tile == 'c':
                    tile_image = pygame.image.load("tiles/cheese-full.png")
                    self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))

                elif tile == 'p':
                    tile_image = pygame.image.load("tiles/pacho.png")
                    self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))
            
        pygame.display.flip()    # updates the entire screen with all the tiles

