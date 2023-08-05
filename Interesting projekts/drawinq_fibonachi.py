import turtle

win = turtle.Screen()
pen = turtle.Turtle()
pen.speed(100)
colors = ['black','black','black','black']
pen.penup()
pen.setpos(-100,-100)
pen.pendown()

def polygon_maker(polygon=3, side=100, pen_size=1):
    x = polygon
    pen.pensize(pen_size)
    if x != 0:
        angel = 180 - (180 * (polygon - 2)) / polygon
    while x > 0:
        i = x % 4
        pen.color(colors[i])
        pen.left(angel)
        pen.forward(side)
        x -= 1

pen.right(35)
x=0
a,b=1,1
z=0
side=3
y=[]
till_numb=20
while x<=till_numb:
    y.append(a)
    y.append(b)
    a=a+b
    b=b+a
    z=z
    pen.right(270)
    pen.color('red')
    pen.circle(radius=y[x]*side,extent=90)
    pen.color('black')
    if y[x]==1:
        polygon_maker(4,y[x]*side)
    elif y[x]==2:
        polygon_maker(4, y[x] * side)

    else:
        pen.forward(-y[x]*side)
        pen.forward(y[x]*side)
        polygon_maker(4,y[x]*side)

    pen.right(90)
    print(y[x])

    x+=1


win.mainloop()
