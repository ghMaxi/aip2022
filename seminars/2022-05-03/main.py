from data import df
import tkinter
from tkinter.scrolledtext import ScrolledText


def show_text(text_gui, text_to_show):
    text_gui.configure(state=tkinter.NORMAL)
    text_gui.delete('1.0', tkinter.END)
    text_gui.insert(tkinter.END, text_to_show)
    text_gui.configure(state=tkinter.DISABLED)


def init(window):
    init_text = df.to_string()
    line_break = init_text.find('\n')
    display_text = ScrolledText(window, width=120, height=35)

    headers = init_text[:line_break].split()
    positions = (100, 200, 300, 400, 500, 600)
    for header, pos_x in zip(headers, positions):
        frame = tkinter.Frame()
        tkinter.Label(frame, text=header).pack()
        button_down = tkinter.Button(frame, text='v')
        button_up = tkinter.Button(frame, text='^')
        sort_button_command(display_text, button_down, header, False)
        sort_button_command(display_text, button_up, header, True)
        button_down.pack(side=tkinter.LEFT)
        button_up.pack()
        frame.place(y=5, x=pos_x)

    init_text = init_text[line_break + 1:]
    show_text(display_text, init_text)
    display_text.place(x=5, y=60)


def display_sorted_by(text_gui, dataframe, column, ascending=True):
    sorted_df = dataframe.sort_values(column, ascending=ascending)
    show_text(text_gui, sorted_df.to_string())

def sort_button_command(text_gui, button, column, ascending):
    button.configure(
        command=lambda: display_sorted_by(
            text_gui, df, column, ascending))

WIDTH, HEIGHT, OFFSET_X, OFFSET_Y = 1000, 600, 10, 10
if __name__ == "__main__":
    app = tkinter.Tk()
    app.geometry(f"{WIDTH}x{HEIGHT}+{OFFSET_X}+{OFFSET_Y}")
    init(app)
    app.mainloop()
