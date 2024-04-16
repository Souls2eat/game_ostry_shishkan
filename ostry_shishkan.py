import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Супер-мега игра")

img = pygame.image.load("ff").convert_alpha()

running = True
while running:

    screen.blit()

    clock.tick(75)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
