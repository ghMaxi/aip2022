from tkinter_main import init
WIDTH, HEIGHT, OFFSET_X, OFFSET_Y = 800, 600, 10, 10


def init_window(app):
    app.geometry(f'{WIDTH}x{HEIGHT}+{OFFSET_X}+{OFFSET_Y}')



if __name__ == "__main__":
    init(init_window)
