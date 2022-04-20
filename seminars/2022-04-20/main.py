from PIL import Image, ImageTk
import tkinter
from matplotlib import pyplot as plt


def plot_binomial(a, b, c, mn=-10, mx=10):
    values = tuple(range(mn, mx + 1))
    ys = tuple(a * x**2 + b * x + c for x in values)
    return plt.plot(values, ys)


# init
window = tkinter.Tk()
window.geometry("800x600+10+20")

# настройка ui
row = tkinter.Frame()
lab = tkinter.Label(row, width=8, text="Размер: ", anchor='w')

ent = tkinter.Entry(row)
button = tkinter.Button(row, text='!!!')
row.pack()
lab.pack(side=tkinter.LEFT)
ent.pack()
button.pack(side=tkinter.RIGHT)

label = tkinter.Label(window)
label.pack()


# заполнение GUI
def display_image(new_image, new_scale=1.0):
    image = new_image.resize(
        (int(new_image.size[0] * new_scale),
         int(new_image.size[1] * new_scale)))
    tk_image = ImageTk.PhotoImage(image)
    label.configure(image=tk_image)
    label.image = tk_image


# обработчики кнопок
def scale_image():
    try:
        new_scale = float(ent.get())
    except Exception:
        print("Число не float!")
        return
    display_image(raw_image, new_scale)


button.configure(command=scale_image)


def main(image, scale):
    global raw_image, start_scale
    raw_image = image
    start_scale = scale
    ent.insert(tkinter.END, str(start_scale))
    display_image(raw_image, start_scale)
    window.mainloop()


if __name__ == "__main__":
    raw_image = Image.open('teo_ik.png')
    start_scale = 0.1
    main(raw_image, start_scale)
