from tkinter import Tk


def init(init_function):
    app = Tk()
    init_function(app)
    app.mainloop()


if __name__ == "__main__":
    init(lambda app: None)
