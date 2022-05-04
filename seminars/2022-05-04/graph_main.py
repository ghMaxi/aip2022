from tkinter_main import init
from tkinter import PhotoImage, Label, OptionMenu,\
                    StringVar, Frame, Text, LEFT, END
from matplotlib import pyplot as plt
WIDTH, HEIGHT, OFFSET_X, OFFSET_Y = 800, 600, 10, 10
TEMP_IMAGE_PATH = 'images/temp.png'

graph_image = PhotoImage(file="images/placeholder_graph.png")
graph_label = Label()


def linear_function(x, **p):
    return x * p['a'] + p['b']


def square_function(x, **p):
    return x ** 2 * p['a'] + x * p['b'] + p['c']


function_dict = {
    'ax + b': (linear_function, ('a', 'b')),
    'ax^2 + bx + c': (square_function, ('a', 'b', 'c')),
}
params = {'a': 1, 'b': 1, 'c': 1}
function_options = list(function_dict.keys())
function = StringVar(value=function_options[0])


def image_from_matplotlib(new_function):
    X = tuple(x / 10 for x in range(100))
    Y = tuple(new_function(x, **params) for x in X)
    plt.figure()
    plt.plot(X, Y)
    plt.savefig(TEMP_IMAGE_PATH)
    global graph_image
    graph_image = PhotoImage(file=TEMP_IMAGE_PATH)
    graph_label.configure(image=graph_image)

def on_function_change(*_):
    function_key = function.get()
    new_function, new_params = function_dict[function_key]
    image_from_matplotlib(new_function)


def draw_params():
    need_params = function_dict[function.get()][1]
    params.clear()
    pos_y = 50
    for param in need_params:
        params[param] = 1
        frame = Frame()
        Label(frame, text=f'{param}:').pack(side=LEFT)
        text = Text(frame, width=2, height=1)
        text.insert(END, '1')
        text.pack()
        frame.place(x=10, y=pos_y)
        pos_y += 30
def init_window(app):
    app.geometry(f'{WIDTH}x{HEIGHT}+{OFFSET_X}+{OFFSET_Y}')
    draw_params()
    image_from_matplotlib(function_dict[function.get()][0])
    graph_label.place(x=150, y=50)
    function_menu = OptionMenu(app, function, *function_options)
    function_menu.place(x=10, y=10)
    function.trace('w', on_function_change)


if __name__ == "__main__":
    init(init_window)
