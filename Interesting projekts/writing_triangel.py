import turtle

pen = turtle.Turtle()
win = turtle.Screen()


def write_triangle(a, b, c, s=100):
    from math import pi, sin
    print(a, b, c)
    A = (a / 180) * pi
    B = (b / 180) * pi
    C = (c / 180) * pi
    print(a, b, c)
    AB, BC, CA = s, s, s
    if a + b + c != 180 or min(a, b, c) <= 0:
        print("It's not a triangle!")
    else:
        if a == max(a, b, c):
            print(A, a, 'is a')
            AB = (BC / sin(A)) * sin(C)
            CA = (BC / sin(A)) * sin(B)
            print(AB, BC, CA)
        if b == max(a, b, c):
            print(B, b, 'is b')
            BC = (CA / sin(B)) * sin(A)
            AB = (CA / sin(B)) * sin(C)
            print(AB, BC, CA)
        if c == max(a, b, c):
            print(C, c, 'is c')
            BC = (AB / sin(C)) * sin(A)
            CA = (AB / sin(C)) * sin(B)
            print(AB, BC, CA)
        pen.fd(AB)
        pen.left(180 - b)
        pen.fd(BC)
        pen.left(180 - c)
        pen.fd(CA)
        pen.left(180 - a)


write_triangle(40,70,70, 321)

win.mainloop()
