from pygame import *
import asyncio
import random as r

init()

w = 320
h = 2 * w
size = w, h
row = 20
column = 10
row_h = h / row
column_w = w / column
screen = display.set_mode(size)
display.set_caption('Tetris')

bg_rect = Rect((-50, -50), (w + 100, h + 100), fill=(0, 0, 0))
optimal_speed = 0.001
main_color = (200, 8, 91)
# colors and their figurs
color_J = (200, 197, 0)
color_I = (62, 200, 16)
color_O = (8, 200, 162)
color_L = (0, 53, 200)
color_Z = (135, 24, 200)
color_T = (177, 0, 200)
color_S = (200, 0, 40)
figure_names = {
    "": (0, 0, 0),
    "J": color_J, "I": color_I, "O": color_O,
    "L": color_L, "Z": color_Z, "T": color_T,
    "S": color_S
}
# Birth_place
bx = column / 2 - 1
by = 3


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
    for rr in range(0, row):
        draw.line(screen, main_color, (0, (rr * row_h)), (w, (rr * row_h)))
    for c in range(0, column):
        draw.line(screen, main_color, ((c * column_w), 0), ((c * column_w), h))


class Figure:
    p = Point(-1, -1)
    fig_point_list = [p, p, p, p]
    copy_fig_point_list = [p, p, p, p]
    moving = True

    def __init__(self, figure_name, ):
        self.fn = figure_name
        self.clr = figure_names[self.fn]
        if self.fn == "":
            p1 = Point(bx, by)
            self.fig_point_list[0] = p1
        if self.fn == "L":
            p1 = Point(bx, by)
            p2 = Point(bx, by + 1)
            p3 = Point(bx, by + 2)
            p4 = Point(bx + 1, by + 2)
            self.fig_point_list[0] = p1
            self.fig_point_list[1] = p2
            self.fig_point_list[2] = p3
            self.fig_point_list[3] = p4
        if self.fn == "J":
            p1 = Point(bx, by)
            p2 = Point(bx, by + 1)
            p3 = Point(bx, by + 2)
            p4 = Point(bx - 1, by + 2)
            self.fig_point_list[0] = p1
            self.fig_point_list[1] = p2
            self.fig_point_list[2] = p3
            self.fig_point_list[3] = p4
        if self.fn == "S":
            p1 = Point(bx, by)
            p2 = Point(bx + 1, by)
            p3 = Point(bx + 1, by + 1)
            p4 = Point(bx + 2, by + 1)
            self.fig_point_list[0] = p1
            self.fig_point_list[1] = p2
            self.fig_point_list[2] = p3
            self.fig_point_list[3] = p4
        if self.fn == "I":
            p1 = Point(bx, by)
            p2 = Point(bx, by + 1)
            p3 = Point(bx, by + 2)
            p4 = Point(bx, by + 3)
            self.fig_point_list[0] = p1
            self.fig_point_list[1] = p2
            self.fig_point_list[2] = p3
            self.fig_point_list[3] = p4
        if self.fn == "Z":
            p1 = Point(bx, by)
            p2 = Point(bx + 1, by)
            p3 = Point(bx + 1, by + 1)
            p4 = Point(bx + 2, by + 1)
            self.fig_point_list[0] = p1
            self.fig_point_list[1] = p2
            self.fig_point_list[2] = p3
            self.fig_point_list[3] = p4
        if self.fn == "O":
            p1 = Point(bx, by)
            p2 = Point(bx + 1, by)
            p3 = Point(bx, by - 1)
            p4 = Point(bx + 1, by - 1)
            self.fig_point_list[0] = p1
            self.fig_point_list[1] = p2
            self.fig_point_list[2] = p3
            self.fig_point_list[3] = p4
        if self.fn == "T":
            p1 = Point(bx, by)
            p2 = Point(bx + 1, by)
            p3 = Point(bx + 2, by)
            p4 = Point(bx + 1, by - 1)
            self.fig_point_list[0] = p1
            self.fig_point_list[1] = p2
            self.fig_point_list[2] = p3
            self.fig_point_list[3] = p4

    def draw(self):
        for p in self.fig_point_list:
            p.draw(self.clr)

    def passive_moving(self):
        if self.moving:
            for p in self.fig_point_list:
                new_p = Point(p.pre_x(), p.pre_y() + 1)
                self.copy_fig_point_list.append(new_p)
            self.fig_point_list = self.copy_fig_point_list
            self.copy_fig_point_list = []

    def not_to_go_under_floor(self):
        y_of_points = []
        for p in self.fig_point_list:
            y_of_points.append(p.pre_y())
        if max(y_of_points) == row - 1:
            self.moving = False

    async def hand_moving(self):
        while True:
            evs = event.get()
            for ev in evs:
                if ev.type == QUIT:
                    display.quit()
                    break
                if ev.type == KEYDOWN:
                    if ev.key == K_ESCAPE:
                        display.quit()
                        break
                    if ev.key == K_LEFT:
                        print("yes it is!")
            await asyncio.sleep(optimal_speed)

    def rotate(self):
        pass

    def not_to_go_very_left_or_right(self):
        pass


# Figure

spec_points = []
L = Figure("")

fig_names = [
    "J", "I", "O",
    "L", "Z", "T",
    "S"
]


async def game():
    global L
    while True:
        draw.rect(screen, (0, 0, 0), bg_rect)

        if not L.moving:
            L = Figure(r.choice(fig_names))
        L.passive_moving()
        L.not_to_go_under_floor()
        L.draw()
        setka()
        display.flip()
        await asyncio.sleep(0.1)


loop = asyncio.get_event_loop()

asyncio.ensure_future(L.hand_moving())
asyncio.ensure_future(game())

loop.run_forever()
"""
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!
Начать всё сначало!




"""