from pygame import *
from math import tan, pi, ceil

# main things
init()
w = 900
h = 600
size = w, h
screen = display.set_mode(size)
display.set_caption('Прога')
bg_color = (114, 193, 110)
bg_rect = Rect(Rect((-50, -50), (w + 100, h + 100), fill=bg_color))

# logs
main_color = (193, 116, 8)
laser_color = (255, 0, 0)

xpos, ypos = pos = 0, 0
k = 0
block_pos = [0, 0]  # left_x, up_y
blocks = []


class Block:
    def __init__(self, left_x, up_y, right_x, down_y, color):
        self.x1 = left_x
        self.y1 = up_y
        self.x2 = right_x
        self.y2 = down_y
        self.clr = color

    def draw(self):
        draw.line(screen, self.clr, (self.x1, self.y1), (self.x2, self.y2), 3)


class Laser:
    def __init__(self, x, y, color, phi=0):
        self.x1 = x
        self.y1 = y
        self.phi = pi * (phi / 180)  # угол от оси y
        self.k = tan(self.phi + pi / 2)
        self.clr = color
        self.big_num = 1000
        self.x2 = self.big_num
        self.y2 = self.k * (self.x2 - self.x1) + self.y1

    def draw(self):
        draw.line(screen, self.clr, (self.x1, self.y1), (self.x2, self.y2), 5)
        draw.circle(screen, self.clr, (self.x1, self.y1), 10)



laser1 = Laser(0, ceil(h / 2), laser_color, 45)

while True:
    draw.rect(screen, bg_color, bg_rect)
    evs = event.get()
    for ev in evs:
        if ev.type == QUIT:
            display.quit()
            break
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                display.quit()
                break
        if ev.type == MOUSEBUTTONDOWN:
            xpos, ypos = pos = mouse.get_pos()
            draw.circle(screen, main_color, pos, 3)
            if k % 2 == 0:
                block_pos[0], block_pos[1] = pos
            if k % 2 == 1:
                block = Block(block_pos[0], block_pos[1], xpos, ypos, main_color)
                blocks.append(block)
            k += 1
    laser1.draw()
    draw.circle(screen, main_color, pos, 3)
    for block in blocks:
        block.draw()

    display.flip()
