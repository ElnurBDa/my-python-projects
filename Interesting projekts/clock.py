from pygame import *
import time as pytime
from math import floor, sin, cos, pi

# main
init()
w = 600
h = 600
size = w, h
screen = display.set_mode(size)
display.set_caption('Game3')


class Circle:
    def __init__(self, pos_center, radius, color):
        self.pos = pos_center
        self.r = radius
        self.clr = color

    def draw(self):
        draw.circle(screen, self.clr, self.pos, self.r)
        draw.circle(screen, (0, 0, 0), self.pos, self.r, 5)
        draw.circle(screen, (0, 0, 0), self.pos, 2)


class Strelka:
    def __init__(self, circle, color, time,width,phi=pi/2):
        self.circle = circle
        self.clr = color
        self.w=width
        self.p=phi
        if time == 'H':
            self.len = floor(self.circle.r * .5)
            self.d = 24 * 1800
        if time == 'M':
            self.len = floor(self.circle.r * .75)
            self.d = 1800
        if time == 'S':
            self.len = floor(self.circle.r * .9)
            self.d = 30
        self.x = 0
        self.y = 0
        self.start=pytime.time()

    def set_pos(self):
        self.x = floor(self.len * cos((pi * (pytime.time()-self.start)) / self.d-self.p))+self.circle.pos[0]
        self.y = floor(self.len * sin((pi * (pytime.time()-self.start)) / self.d-self.p))+self.circle.pos[1]

    def draw(self):
        draw.line(screen,self.clr,self.circle.pos,(self.x,self.y),self.w)


# Clock's main things
bg_rect = Rect((-10, -10), (w + 20, h + 20))

# Circle
main_circle_radius = floor(h / 2 - 30)
main_circle_color = (150, 150, 150)
center_pos = (floor(w / 2), floor(h / 2))
main_circle = Circle(center_pos, main_circle_radius, main_circle_color)
# Strelka
sec=Strelka(main_circle,(255,0,155),"S",3)
min=Strelka(main_circle,(255,0,155),"M",5,)
hour=Strelka(main_circle,(255,0,155),"H",10)
a=[sec,min,hour]
# Circle2
not_main_circle_radius = 100
not_main_circle_color = (100, 100, 100)
not_center_pos = (100,100)
not_main_circle = Circle(not_center_pos, not_main_circle_radius, not_main_circle_color)
# Strelka
not_sec=Strelka(not_main_circle,(0,255,155),"S",1)
not_min=Strelka(not_main_circle,(0,255,155),"M",3,)
not_hour=Strelka(not_main_circle,(0,255,155),"H",5)
b=[not_sec,not_min,not_hour]


while True:

    draw.rect(screen, (200, 200, 200), bg_rect)
    main_circle.draw()
    print(floor(pytime.time()))
    for x in a:
        x.set_pos()
        x.draw()
    not_main_circle.draw()
    print(floor(pytime.time()))
    for x in b:
        x.set_pos()
        x.draw()
    evs = event.get()
    for ev in evs:
        if ev.type == QUIT:
            display.quit()
            break
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                display.quit()
                break

    display.flip()
