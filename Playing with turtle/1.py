import turtle
import time

pen = turtle.Turtle()
win = turtle.Screen()
pen.speed(1000)
pen.penup()
pen.setpos(-50, 100)
pen.pendown()


def tr(l,s):
    if s == 'r':
        pen.forward(l)
        pen.right(90)
        pen.forward(l)
        pen.right(135)
        pen.forward(l * (2 ** (1 / 2)))
    elif s == 'l':
        pen.forward(l)
        pen.left(90)
        pen.forward(l)
        pen.left(135)
        pen.forward(l * (2 ** (1 / 2)))






for i in range(4):
    l=270
    a=l
    b=l/(2**(1/2))
    for  i in range(1,17):
        tr(a,'r')
        pen.right(90)
        a=a/(2**(1/2))
    pen.forward(l)
    pen.right(90)
    pen.forward(l)
    pen.right(-135)
    for  i in range(1,16):
        tr(b,'l')
        pen.left(90)
        b=b/(2**(1/2))



win.mainloop()
