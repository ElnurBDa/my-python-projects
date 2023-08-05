from tkinter import *
from tkinter import messagebox
from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")

    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    # hides borders
    ax.axis[direction].set_visible(False)
root = Tk()
root.resizable(False, False)
xolst = Canvas(root, bg="grey")
xolst.pack(side="left")
xolst.create_text(160, 20, text="ax^2+bx+c       D(f)=(-100,100)", font="arial 15")
xolst.create_text(115, 50, text="Введите коэфицент a : ", font="arial 15")
xolst.create_text(115, 80, text="Введите коэфицент b : ", font="arial 15")
xolst.create_text(115, 110, text="Введите коэфицент c : ", font="arial 15")
entry_a = Entry(xolst, width=10)
entry_a.place(x=220, y=42)
entry_b = Entry(xolst, width=10)
entry_b.place(x=220, y=72)
entry_c = Entry(xolst, width=10)
entry_c.place(x=220, y=102)
a = 1
b = 1
c = 1


def shitat(event):
    global a
    global b
    global c
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        D = b * b - 4 * a * c
        xolst.create_text(80, 150, text="Дискриминант : " + str(D), font="arial 10")
        if D >= 0:
            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
            xolst.create_text(80, 180, text="Первый корень : " + str(x1) + "\n" + "Второй корень : " + str(x2),
                              font="arial 10")
        else:
            xolst.create_text(80, 170, text="Уравнение не имеет действительный корней!", font="arial 10")
        xolst.create_text(80, 210, text="Вершина параболы:", font="arial 10")
        m = (-b) / (2 * a)
        n = a * m * m + b * m + c
        xolst.create_text(80, 230, text="( " + str(m) + " , " + str(n) + " )", font="arial 10")
        if 1==1:
            x = np.linspace(-100, 100, 1000)
            ax.plot(x, a * x * x + b * x + c)
            plt.show()


    except:
        messagebox.showerror("Ошибка!", "Введите число!")


btn = Button(root, text="Ра\nсс\nчи\nта\nть", width=2, height=5, bg="#998")
btn.bind('<Button-1>', shitat)
btn.place(x=300, y=39)

root.mainloop()
