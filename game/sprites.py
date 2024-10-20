import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite): #calls the __init__ method for the inherited class
    def __init__(self, game, x, y): #the game is passed in as an object

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites #this adds the player to the all_sprites group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.wdith = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height]) #creation of a rectangle that is 32x32 pixels, then the rectangle is set as the sprite image
        self.image.fill(RED)