from pygame import *
from math import ceil
from time import time

# main things
init()
w = 900
h = 600
size = w, h
screen = display.set_mode(size)
display.set_caption('File')
# This rect
bgrect = Rect((0, 0), (w, h))
bgrectcolor = (81, 0, 36)
# logs
clr1 = (255, 225, 0)
clr2 = (43, 255, 0)


class Block:
    def __init__(self, x1, y1, x2, y2, clr=(255, 255, 255)):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.clr = clr
        self.rect = Rect((x1, y1), (x2 - x1, y2 - y1))

    def draw(self):
        draw.rect(screen, self.clr, self.rect)

    def give_parametrs(self):
        return (self.rect, self.x1, self.y1, self.x2, self.y2)


class Ball:
    start_time = time()

    def __init__(self, x1, y1, r, clr=(255, 255, 255)):
        self.x1 = x1
        self.y1 = y1
        self.r = r
        self.clr = clr
        self.one = 1
        self.rect = Rect((self.x1 - self.r, self.y1 - self.r), (self.r * 2, self.r * 2))

    def draw(self):
        self.rect = Rect((self.x1 - self.r, self.y1 - self.r), (self.r * 2, self.r * 2))
        draw.rect(screen, (0, 0, 0), self.rect)
        draw.circle(screen, self.clr, (self.x1, self.y1), self.r)

    def moving(self):
        y0 = self.y1
        t = time() - self.start_time
        v = self.one
        y = y0 + v
        self.y1 = ceil(y)

    def touch(self, gotrect):
        if self.rect.colliderect(gotrect[0]):
            self.one = self.one * (-1)
            self.y1 +=self.one*3


blockdown = Block(0, h - 50, w, h, clr1)
blockup = Block(0, 0, w, 50, clr1)
ball = Ball(ceil(w / 2), 100, 30, clr2)

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
                break

    blockdown.draw()
    blockup.draw()
    ball.draw()
    ball.moving()
    ball.touch(blockdown.give_parametrs())
    ball.touch(blockup.give_parametrs())

    display.flip()
