import pygame
import pygame_app
from constants import *
import data


def event_function(event):
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == pygame.BUTTON_LEFT:
            create_star(event.pos[0] / SCREEN_WIDTH, event.pos[1] / SCREEN_HEIGHT)
    if event.type == pygame.QUIT:
        data.save(star_list)


def draw_star(screen, ratio_x, ratio_y, color_key):
    square_rect = pygame.Rect(0, 0, BASE_SQUARE_SIZE, BASE_SQUARE_SIZE)
    square_rect.center = SCREEN_WIDTH * ratio_x, SCREEN_HEIGHT * ratio_y
    pygame.draw.rect(screen, COLORS[color_key], square_rect)


def get_star_data():
    result = []
    for index, row in data.df.iterrows():
        result.append((row[X_KEY], row[Y_KEY], int(row[COLOR_KEY])))
    return result


star_list = get_star_data()


def create_star(ratio_x, ratio_y, color=0):
    star_list.append((ratio_x, ratio_y, color))



def step_function(screen, delta_time):
    for star in star_list:
        draw_star(screen, *star)


if __name__ == "__main__":
    pygame_app.main(event_function,
                    step_function)
