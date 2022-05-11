import pygame
from constants import *


def main(event_function, step_function):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                event_function(event)
            else:
                event_function(event)
        step_function(screen, clock.tick(FPS))


if __name__ == "__main__":
    def empty_function(*_): return None
    main(empty_function, empty_function)
