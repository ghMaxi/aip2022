import pygame
from constants import *


def main(event_function, step_function):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            event_function(event)
        step_function(screen, clock.tick(FPS))
        pygame.display.flip()


if __name__ == "__main__":
    def empty_function(*args): pass
    main(empty_function, empty_function)
