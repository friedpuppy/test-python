import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("first game")

x = 50
y = 50
width = 40
height = 60
vel = 5

while True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.draw.rect(win, (255,0,0), win.get_rect())

    pygame.display.update()