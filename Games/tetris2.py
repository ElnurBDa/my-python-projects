from pygame import *
from math import ceil, floor
import asyncio
import random

# main things
init()
w = 900
h = 600
size = w, h
screen = display.set_mode(size)
display.set_caption('-')
clock = time.Clock()
# Grid
row = 16
column = 12
side = h / row

grid_color = (71, 199, 235)


def draw_grid():
    for a in range(0, row + 1):
        draw.line(screen, grid_color, (0, side * a), (column * side, side * a))
    for a in range(0, column + 1):
        draw.line(screen, grid_color, (a * side, 0), (a * side, h))


'''
Point= (x,y,full/empty(1/0),color)
'''


def draw_point(p):
    x = p[0]
    y = p[1]
    point_rect = Rect(((x - 1) * side, (y - 1) * side), (side, side))
    draw.rect(screen, p[3], point_rect)


# This rect
bgrect = Rect((0, 0), (w, h))
bgrectcolor = (0, 0, 0)


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


# p1 = [1, 1, 1, (221, 111, 211)]
moveble_points = []
stable_points = []

for x in range(0, 7):
    stable_points.append([5, row - x, 1, (212, 0, 0)])

for x in range(0, 7):
    moveble_points.append([x + 2, 1, 1, (221, 111, 211)])




async def game():
    while True:
        for p in moveble_points:
            moveble_points.remove(p)
            px = p
            px[1] += 1
            moveble_points.append(px)

        display.flip()
        await asyncio.sleep(.5)


async def control():
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

                if ev.key == K_d:
                    for p in moveble_points:
                        good = True
                        for ps in stable_points:
                            if p[1] == ps[1] and p[0] == ps[0] - 1:
                                good = False
                                break
                        if good:
                            moveble_points.remove(p)
                            px = p
                            px[0] += 1
                            moveble_points.append(px)
                if ev.key == K_a:
                    good = True
                    for ps in stable_points:
                        if p[1] == ps[1] and p[0] == ps[0] + 1:
                            good = False
                            break
                    if good:
                        moveble_points.remove(p)
                        px = p
                        px[0] -= 1
                        moveble_points.append(px)
                if ev.key == K_s:
                    for p in moveble_points:
                        moveble_points.remove(p)
                        px = p
                        px[1] += 1
                        moveble_points.append(px)
        for p in moveble_points:
            draw_point(p)
        for p in stable_points:
            draw_point(p)

        for pm in moveble_points:
            for ps in stable_points:
                if pm[0] == ps[0] and pm[1] == ps[1] - 1:
                    for p in moveble_points:
                        stable_points.append(p)
                        moveble_points.remove(p)
                    if len(moveble_points)==0:
                        moveble_points.append([3, 1, 1, (221, 111, 2)])
                    break

        for p in moveble_points:
            if p[1] == row:
                for p in moveble_points:
                    stable_points.append(p)
                    moveble_points.remove(p)
                moveble_points.append([1, 1, 1, (221, 111, 211)])

        draw_grid()

        display.flip()
        await asyncio.sleep(0.01)


loop = asyncio.get_event_loop()

asyncio.ensure_future(game())
asyncio.ensure_future(control())

loop.run_forever()
