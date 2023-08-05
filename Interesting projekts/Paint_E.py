from tkinter import *

c_w = 800
c_h = 5000
size = 5
red = 'red'
blue = 'blue'
yellow = 'yellow'
green = 'green'
black = 'black'
white = 'white'
color = black
def paint(event):
    global size
    global color_fill
    x1 = event.x - size
    x2 = event.x + size
    y1 = event.y - size
    y2 = event.y + size
    w.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
def color_change(new_color):
    global color
    color = new_color
def size_change(new):
    global size
    size = new

root = Tk()
root.title('My Paint')
w = Canvas(root, width=c_w, height=c_h, bg='white')

w.bind('<B1-Motion>', paint)
w.grid(row=2, column=0, padx=5, pady=5, columnspan=10, sticky=W + E + N + S)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

red_btn = Button(width=15, command=lambda: color_change(red), bg=red)
red_btn.grid(row=1, column=0)
green_btn = Button(width=15, command=lambda: color_change(green), bg=green)
green_btn.grid(row=1, column=1)
yellow_btn = Button(width=15, command=lambda: color_change(yellow), bg=yellow)
yellow_btn.grid(row=1, column=2)
black_btn = Button(width=15, command=lambda: color_change(black), bg=black)
black_btn.grid(row=1, column=4)
blue_btn = Button(width=15, command=lambda: color_change(blue), bg=blue)
blue_btn.grid(row=1, column=3)
white_btn = Button(width=15, command=lambda: color_change(white), bg=white)
white_btn.grid(row=1, column=5)
delete_btn = Button(width=15, command=lambda: w.delete('all'), bg=white, text='Delete all')
delete_btn.grid(row=1, column=6)
scale = Scale(w, orient=VERTICAL, length=600, from_=0, to=100, tickinterval=5, resolution=1, )
scale.grid()
get_btn=Button(width=15, command=lambda: size_change(scale.get()), bg=white, text='Press and change')
get_btn.grid(row=4,column=0)


root.mainloop()
