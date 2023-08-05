from pygame import *
import random
import asyncio

init()

color = 200,144,94

w = 500
h = 500
size = w, h
screen = display.set_mode(size)
display.set_caption('Snake')
speed = 8
food_n = 10
row = 20
column = 20

row_h = w / row
column_w = h / column

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


points = []
for x in range(0, food_n):
    f = Point(random.randint(0, column - 1), random.randint(0, row - 1))
    points.append(f)


class Snake:
    point_list = []
    pre_point_list = []
    direct = None

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        p1 = Point(start_x, start_y)
        self.point_list.append(p1)

    async def direct_(self):
        while True:
            evs = event.get()
            for ev in evs:
                if ev.type == KEYDOWN:
                    if ev.key == K_LEFT:
                        self.direct = 'l'
                    if ev.key == K_RIGHT:
                        self.direct = 'r'
                    if ev.key == K_UP:
                        self.direct = 'u'
                    if ev.key == K_DOWN:
                        self.direct = 'd'
                    if ev.key == K_ESCAPE:
                        quit()
                        с = 2 / 0
            await asyncio.sleep(0.01)


    def spec_func(self, p):

        self.point_list.append(p)
        self.point_list.remove(self.point_list[0])

    def move(self):
        d = self.direct
        x = self.point_list[-1].pre_x()
        y = self.point_list[-1].pre_y()
        self.pre_point_list = self.point_list
        if d == 'l':
            if x < 1:
                x = column
            p = Point(x - 1, y)

            self.spec_func(p)
        if d == 'r':
            if x > column - 2:
                x = -1
            p = Point(x + 1, y)
            self.spec_func(p)
        if d == 'u':
            if y < 1:
                y = row

            p = Point(x, y - 1)
            self.spec_func(p)
        if d == 'd':
            if y > row - 2:
                y = -1
            p = Point(x, y + 1)
            self.spec_func(p)

    def all_draw(self):
        for x in self.point_list:
            x.draw(color)

    def all_remove(self):
        for x in self.pre_point_list:
            x.draw((0, 0, 0))

    def eat(self, f):
        if self.point_list[-1].is_hit(f):
            self.point_list.append(f)
            points.remove(f)

            while True:
                count = 0
                z = Point(random.randint(0, column - 1), random.randint(0, row - 1))
                for x in self.point_list:
                    if z.is_hit(x):
                        count += 1
                if count == 0:
                    points.append(z)
                    break

    def is_game_over(self):
        w = self.point_list
        head = w[-1]

        count = 0
        for x in w:
            if head.is_hit(x):
                count += 1
        if count == 2:
            quit()
            c = 2 / 0


def setka():
    for r in range(0, row):
        draw.line(screen, color, (0, r * row_h), (w, r * row_h))
    for c in range(0, column):
        draw.line(screen, color, (c * column_w, 0), (c * column_w, h))


async def game():
    while True:
        clock.tick(speed)
        setka()
        snk.all_remove()
        snk.move()
        snk.all_draw()
        snk.is_game_over()
        for x in points:
            x.draw((225, 54, 24))
            snk.eat(x)

        display.flip()
        await asyncio.sleep(0.1)
snk = Snake(3, 4)
loop=asyncio.get_event_loop()


asyncio.ensure_future(game())
asyncio.ensure_future(snk.direct_())


loop.run_forever()
