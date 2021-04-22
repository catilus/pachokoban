import pygame
from pygame.locals import *

class Pacho:  
    
    def __init__(self, tile, position):
        self.tile = tile
        self.position = position
    #def getPosition(levelfile):
    
    def modifyPosition(self, x_move, y_move):
        self.position = (self.position[0]+x_move, self.position[1]+y_move)