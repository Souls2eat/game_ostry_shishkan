from pygame import *

clock = time.Clock()

screen = display.set_mode((1600, 900))
display.set_caption("Супер-мега игра")

img = image.load("background_norm1.jpg").convert_alpha()


running = True
while running:

    screen.blit(img, (0, 0))

    clock.tick(75)
    display.update()

    for e in event.get():
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            running = False
        if e.type == QUIT:
            running = False
        

