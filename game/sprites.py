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
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0 # temporary variables that store the change in movement during one loop
        self.y_change = 0

        self.facing = 'down' #is character facing up left or down etc

        self.image = pygame.Surface([self.width, self.height]) #creation of a rectangle that is 32x32 pixels, then the rectangle is set as the sprite image
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x #tells pygame the coordinates of our rectangle
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed() # list of every key pressed on keyboard stored in 'keys'
        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED # referenced in config.py
            self.facing = 'left'
        if keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'            