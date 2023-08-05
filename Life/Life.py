from pygame import *
from math import floor
from random import randint

init()
w = 800
h = 800
size = w, h
screen = display.set_mode(size)
display.set_caption('Life')
# Main
column = 30
row = 30
row_h = h / row
column_w = w / column
main_rect = ((-10, -10), (w + 20, h + 20))
clock = time.Clock()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, colo):
        rect = Rect((self.x * column_w, self.y * row_h), (column_w, row_h), fill=colo)
        draw.rect(screen, colo, rect)

    def is_hit(self, p):
        if self.x == p.x and self.y == p.y:
            return True
        return False

    def pre_x(self):
        return self.x

    def pre_y(self):
        return self.y


def setka():
    for r in range(0, row):
        draw.line(screen, (155, 155, 155), (0, (r * row_h)), (w, (r * row_h)))
    for c in range(0, column):
        draw.line(screen, (155, 155, 155), ((c * column_w), 0), ((c * column_w), h))


points = []
postpoints = []
enter = True
tick = 40


def set_point():
    x, y = mouse.get_pos()
    new_p = Point(floor(x / column_w), floor(y / row_h))
    for p in points:
        if p.pre_x() == new_p.pre_x() and p.pre_y() == new_p.pre_y():
            points.remove(p)
            return True
    points.append(new_p)


gen = -1
while True:
    draw.rect(screen, (255, 255, 255), main_rect)
    evs = event.get()
    for ev in evs:
        if ev.type == QUIT:
            display.quit()
            break
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                display.quit()
                break
            if ev.key == K_SPACE:
                enter = False
                tick = 5
        if ev.type == MOUSEBUTTONDOWN and enter:
            set_point()

    if not enter:
        for r in range(0, row):
            for c in range(0, column):
                this_p = Point(c, r)
                itisin = False
                rght_c = c + 1
                lft_c = c - 1
                up_r = r - 1
                dwn_r = r + 1
                if rght_c > column - 1:
                    rght_c = 0
                if lft_c < 0:
                    lft_c = column - 1
                if dwn_r > row - 1:
                    dwn_r = 0
                if up_r < 0:
                    up_r = row - 1
                for p in points:
                    if p.pre_x() == this_p.pre_x() and p.pre_y() == this_p.pre_y():
                        itisin = True
                """
                (c-1,r-1)(c,r-1)(c+1,r-1)
                (c-1,r)   (c,r)  (c+1,r)
                (c-1,r+1)(c,r+1)(c+1,r+1)
                """
                n_points = [
                    Point(lft_c, up_r),
                    Point(lft_c, dwn_r),
                    Point(lft_c, r),
                    Point(rght_c, up_r),
                    Point(rght_c, dwn_r),
                    Point(rght_c, r),
                    Point(c, up_r),
                    Point(c, dwn_r)
                ]
                # while True:
                #     for p in n_points:
                #         p.draw((255,0,0))
                #     clock.tick(tick)
                #     setka()
                #     display.flip()
                count = 0
                for x in n_points:
                    for p in points:
                        if p.pre_x() == x.pre_x() and p.pre_y() == x.pre_y():
                            count += 1
                # Main rules
                if itisin is False and count == 3:
                    postpoints.append(this_p)
                if itisin and (count == 2 or count == 3):
                    postpoints.append(this_p)

        points = postpoints
        postpoints = []
        gen += 1
        print("Generation: ", gen)

    color = 0
    for x in points:
        x.draw((color, color, color))

    clock.tick(tick)
    setka()
    display.flip()
    if len(points) == 0 and enter is False:
        quit()
