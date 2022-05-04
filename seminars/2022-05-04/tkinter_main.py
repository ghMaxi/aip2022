from tkinter import Tk
app = Tk()


def init(init_function):
    init_function(app)
    app.mainloop()


if __name__ == "__main__":
    init(lambda app: None)
