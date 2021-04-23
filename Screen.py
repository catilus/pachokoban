import pygame
from pygame.locals import *

class Screen:

    def __init__(self, width, height, background_color):
        self.width = width
        self.heigth = height
        self.window = pygame.display.set_mode((width,height))   # screen size
        self.window.fill(background_color)  # screen background color
        pygame.display.set_caption("Pachokoban")    # sets window caption

    def shows(self, tile, position, background_color):
        tile_size = 50
        
        if tile == 'w':
            tile_image = pygame.image.load("tiles/wall-yellow.png")
            self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))
            pygame.display.update() # only update portions of the screen
            pygame.display.flip()    # updates the entire screen with all the tiles    

        elif tile == 's':
            tile_image = pygame.image.load("tiles/spot-yellow.png")
            self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))
            pygame.display.update()
            pygame.display.flip()

        elif tile == 'p':
            tile_image = pygame.image.load("tiles/pacho.png")
            self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))
            pygame.display.update()
            pygame.display.flip()

        elif tile == 'c':
            tile_image = pygame.image.load("tiles/cheese-full.png")
            self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))
            pygame.display.update()
            pygame.display.flip()

        elif tile == 'b':   # background tile
            #background_color=(0,0,0)
            rect=(position[1]*tile_size, position[0]*tile_size, tile_size, tile_size)
            pygame.draw.rect(self.window,background_color,rect)
            pygame.display.update()
            pygame.display.flip()

        

