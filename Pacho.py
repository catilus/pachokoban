import pygame
from pygame.locals import *

class Pacho:  
    
    def __init__(self, tile, position):
        self.tile = tile
        self.position = position
    
    #def checkPosition(calculated_position,levelfile):
    #    self.calculated_position = (self.position[0]+x_move, self.position[1]+y_move)
            
    def modifyPosition(self, x_move, y_move):
        self.position = (self.position[0]+x_move, self.position[1]+y_move)