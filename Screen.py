import pygame
from pygame.locals import *

class Screen:

    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width,height))   # screen size
        self.window.fill(background_color)  # screen background color
        pygame.display.set_caption("Pachokoban")    # sets window caption

    def shows(self, tile, position, background_color, steps_counter):
        tile_size = 50
        
        if tile == 'w':     # wall
            tile_image = pygame.image.load("tiles/wall-yellow.png")
            self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))
            pygame.display.update() # only update portions of the screen
            pygame.display.flip()    # updates the entire screen with all the tiles    

        elif tile == 's':   # spot where cheese is meant to go
            tile_image = pygame.image.load("tiles/spot-yellow.png")
            self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))
            pygame.display.update()
            pygame.display.flip()

        elif tile == 'p':   # pacho
            tile_image = pygame.image.load("tiles/pacho.png")
            self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))
            pygame.display.update()
            pygame.display.flip()

        elif tile == 'c':   # full cheese
            tile_image = pygame.image.load("tiles/cheese-full.png")
            self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))
            pygame.display.update()
            pygame.display.flip()

        elif tile == 'e':   # eaten cheese
            tile_image = pygame.image.load("tiles/cheese-eaten.png")
            self.window.blit(tile_image, (position[1]*tile_size, position[0]*tile_size))
            pygame.display.update()
            pygame.display.flip()    

        elif tile == 'b':   # background tile
            rect=(position[1]*tile_size, position[0]*tile_size, tile_size, tile_size)
            pygame.draw.rect(self.window,background_color,rect)
            pygame.display.update()
            pygame.display.flip()

        elif tile == 'counter':     # show counter
            font = pygame.font.Font('fonts/Raleway-ExtraLight.ttf', 20)
            text = font.render('Steps: {}'.format(steps_counter), True, (0,0,0), None)
            text_rect = (position[0], position[1], 100, 25)
            pygame.draw.rect(self.window, background_color, text_rect)
            self.window.blit(text, position)
            pygame.display.update()
            pygame.display.flip()

        elif tile == 'victory':
            # creates a new surface that manages transparency
            s = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            # sets colors, 255 = fully opaque
            s.fill((255,255,255,180))
            # blits onto screen
            self.window.blit(s, (0,0))

            # writes victory text on window
            font = pygame.font.Font('fonts/Raleway-SemiBold.ttf', 50)
            text = font.render('You won!', True, (0,0,0), None)
            textRect = text.get_rect()
            textRect.center = (self.width//2, self.height//2)   # centers text on window
            self.window.blit(text, textRect)
            
            pygame.display.update()
            pygame.display.flip()

        elif tile == 'menu':
            s = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            s.fill((255,255,255,180))
            self.window.blit(s, (0,0))

            font = pygame.font.Font('fonts/Raleway-SemiBold.ttf', 30)
            text = font.render('Exit game (press Q)', True, (0,0,0), None)
            textRect = text.get_rect()
            textRect.center = (self.width//2, self.height//4)
            self.window.blit(text, textRect)

            pygame.display.update()
            pygame.display.flip() 

        else:
            pass    
            
        

        

