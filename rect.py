
# Importing the library
import pygame
 
# Initializing Pygame
pygame.init()
clock = pygame.time.Clock()
running = True
dt = 0

 
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Initializing surface
    surface = pygame.display.set_mode((400,300))
 
    # Initializing Color
    color = (255,0,0)
 
    # Drawing Rectangle
    pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()