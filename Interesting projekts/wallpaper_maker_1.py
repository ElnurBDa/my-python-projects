from tkinter import *
from math import floor
from time import sleep
from itertools import combinations


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

p=4.4
w,h = floor(108*p),floor(192*p)

root = Tk()
root.resizable(False, False)

root.geometry(str(w) + 'x' + str(h)+'+100+0')
xolst = Canvas(root, bg='#4169E1', width=w, height=h, highlightthickness=0)
xolst.pack()

for x in range(1, w):
    z = 255 - floor((x / w) * 255)
    y = floor((x / w) * 255)
    per=1
    z=floor(z*per)
    y=floor(y*per)
    a = rgb_to_hex((0,z,y))
    xolst.create_rectangle(x, x, w, h, fill=a, outline=a)


root.mainloop()
