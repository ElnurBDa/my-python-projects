from pygame import *
from math import ceil, floor
from random import randint

# main things
init()
w = 900
h = 600
size = w, h
screen = display.set_mode(size)
display.set_caption('Оtражение и Переломление')
whalf = floor(w / 2)
hhalf = floor(h / 2)
# This rect
bgrect = Rect((0, 0), (w, h))
bgrectcolor = (0, 0, 0)


class Line:
    pO = (whalf, hhalf)
    rclr1 = (randint(0, 255), randint(0, 255), randint(0, 255))
    rclr2 = (randint(0, 255), randint(0, 255), randint(0, 255))

    def __init__(self, pStart, pEnd, color, n2=1):
        self.pStart = pStart
        self.pEnd = pEnd
        self.clr = color
        self.n2 = n2

    def draw(self):
        draw.line(screen, self.clr, self.pStart, self.pEnd, 2)

    def draw_reflection(self):
        x1 = self.pStart[0]
        y1 = self.pStart[1]
        k = 100
        endx = (whalf - x1) * k + whalf
        endy = (y1 - hhalf) * k + hhalf
        draw.line(screen, self.rclr1, self.pEnd, (endx, endy), 2)

    def draw_refraction(self):
        x1 = self.pStart[0]
        y1 = self.pStart[1]
        self.sinAlpha = (whalf - x1) / (((x1 - whalf) ** 2 + (y1 - hhalf) ** 2) ** .5)
        self.sinBeta = self.sinAlpha / self.n2
        if self.sinBeta < 1:
            self.tgBeta = self.sinBeta / ((1 - self.sinBeta ** 2) ** .5)
        else:
            self.tgBeta = 1000
        k = 10
        endx = 1000
        endy = floor((endx - whalf) / self.tgBeta + hhalf)
        draw.line(screen, self.rclr2, self.pEnd, (endx, endy), 2)


def win_quit():
    evs = event.get()
    for ev in evs:
        if ev.type == QUIT:
            display.quit()
            break
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                display.quit()
                break


def set():
    global xm, ym
    xm, ym = mouse.get_pos()


# some lines
lhorizont = Line((0, hhalf), (w, hhalf), (255, 8, 0))
lvertic = Line((whalf, 0), (whalf, h), (255, 8, 0))

l1 = Line((100, hhalf - 10), Line.pO, (255, 242, 0), 2)

while True:
    draw.rect(screen, bgrectcolor, bgrect)
    evs = event.get()
    for ev in evs:
        if ev.type == QUIT:
            display.quit()
            break
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                display.quit()
            '''if ev.key == K_p:
                set()
                print(xm, ym)
                l1.pStart = (xm, ym)'''
            break

    lhorizont.draw()
    lvertic.draw()
    set()
    l1.pStart = (xm, ym)
    if xm <= whalf and ym <= hhalf:
        l1.draw()
        l1.draw_reflection()
        try:
            l1.draw_refraction()
        except:
            pass
    display.flip()
