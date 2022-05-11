from app import main
import pygame
from constants import *
import data

star_color = WHITE, VIOLET, YELLOW, RED


def square_from_star(star_phase, x, y):
    star_rect = pygame.Rect(SCREEN_SIZE[0] * x - BASE_RECT[2] // 2,
                            SCREEN_SIZE[1] * y - BASE_RECT[3] // 2,
                            BASE_RECT[2], BASE_RECT[3])
    return star_color[star_phase], star_rect


def squares_from_df():
    result_list = []
    for _, row in data.df.iterrows():
        print(row)
        result_list.append(square_from_star(int(row[1]), row[3], row[4]))
    return result_list


square_list = squares_from_df()


def event_function(event):
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == pygame.BUTTON_LEFT:
            add_new_star(event.pos[0] / SCREEN_SIZE[0], event.pos[1] / SCREEN_SIZE[1])
        if event.button == pygame.BUTTON_RIGHT:
            print("remove_star_NOT_DONE!")
    elif event.type == pygame.QUIT:
        data.save()


def find_star(px_x, px_y):
    square: pygame.Rect
    for square in square_list:
        if square.collidepoint(px_x, px_y):
            # TODO: вернуть звезду в правильном формате
            return square


def remove_star(star):
    # TODO: убрать звезду из df
    # обновить список
    global square_list
    square_list = squares_from_df()


def add_new_star(x, y):
    data.append(0, x, y)
    global square_list
    square_list = squares_from_df()


def step_function(screen, delta_time):
    for square_color, square in square_list:
        pygame.draw.rect(screen, square_color, square)
    pygame.display.flip()


if __name__ == "__main__":
    main(event_function, step_function)
