import pygame
from pygame.locals import *

#define a method wich checks if the player coordinates out of the screen


def check_out_of_screen(x, y):
    if x < 0:
        x = 0
    elif x > 640 - sprite.get_width():
        x = 640 - sprite.get_width()
    if y < 0:
        y = 0
    elif y > 480 - sprite.get_height():
        y = 480 - sprite.get_height()
    return (x, y)


if __name__ == '__main__':

    pygame.init()
    screensize = (640, 480)
    screen = pygame.display.set_mode(screensize)
    sprite = pygame.image.load(r"favicon.png")
    pygame.display.set_caption("Hello World")
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    game_over = False
    x, y = 0, 0
    while not game_over:
        dt = clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]: y -= 0.5 * dt
        if pressed[pygame.K_DOWN]: y += 0.5 * dt
        if pressed[pygame.K_LEFT]: x -= 0.5 * dt
        if pressed[pygame.K_RIGHT]: x += 0.5 * dt

        x, y = check_out_of_screen(x, y)

        screen.fill((0, 0, 0))
        screen.blit(sprite, (x, y))

        pygame.display.update()
