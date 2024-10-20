import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Tahoma', 32)
        self.running = True

    def new(self):
        # new game start
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 1, 2)

    def events(self):
        # game loop events
        for event in pygame.event.get(): #every single event that happens in pygame
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                
    def update(self):
        # game loop updates
        self.all_sprites.update()

    def draw(self):
        # game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update() #update the screen

    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update() #so that the game isn't a static image
            self.draw() #displays sprites
        self.running = False
    
    def game_over(self):
        pass

    def intro_screen(self):
        pass