from data import df
import tkinter
from tkinter import PhotoImage
from tkinter.scrolledtext import ScrolledText
# константы
WIDTH, HEIGHT = 1000, 850

# настройка окна и его содержимого
app = tkinter.Tk()
up_image = PhotoImage(file="images/up.png")
down_image = PhotoImage(file="images/down.png")
cancel_image = PhotoImage(file="images/cancel.png")

app.geometry(f"{WIDTH}x{HEIGHT}")
df_display = ScrolledText(app, width=120, height=50)

df_display.configure(state=tkinter.DISABLED)
df_display.place(x=10, y=60)
x_pos = [80, 385, 460, 545, 635, 725, 895]

buttons = []
for column in df:
    sort_frame = tkinter.Frame(app)
    sort_label = tkinter.Label(sort_frame, text=column)
    sort_up_btn = tkinter.Button(sort_frame, image=up_image)
    sort_down_btn = tkinter.Button(sort_frame, image=down_image)
    stop_sort_btn = tkinter.Button(sort_frame, image=cancel_image)
    buttons.append((column, sort_up_btn, sort_down_btn, stop_sort_btn))
    sort_label.pack()
    stop_sort_btn.pack(side=tkinter.RIGHT)
    sort_up_btn.pack(side=tkinter.RIGHT)
    sort_down_btn.pack(side=tkinter.RIGHT)
    sort_frame.place(x=x_pos.pop(0), y=10)

# функции взаимодействия
def display_dataframe(dataframe):
    df_display.configure(state=tkinter.NORMAL)
    df_display.delete('1.0', tkinter.END)
    text = dataframe.to_string()
    df_display.insert(tkinter.END, text[text.find('\n') + 1:])
    df_display.configure(state=tkinter.DISABLED)

def sort(dataframe, column, sort_up):
    sorted_frame = dataframe.sort_values(by=[column], ascending=sort_up)
    display_dataframe(sorted_frame)

def make_function(column, sort_up): return lambda: sort(df, column, sort_up)

for column, sort_up_btn, sort_down_btn, stop_sort_btn in buttons:
    sort_up_btn.configure(command=make_function(column, True))
    sort_down_btn.configure(command=make_function(column, False))
    stop_sort_btn.configure(command=lambda: display_dataframe(df))


if __name__ == '__main__':
    # заполнение окна данными
    display_dataframe(df)
    sort(df, 'name', True)
    app.mainloop()
