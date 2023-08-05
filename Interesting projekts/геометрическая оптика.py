from pygame import *
from math import ceil, floor, sqrt

# main things
init()
w = 1500
he = 800
size = w, he
screen = display.set_mode(size)
display.set_caption('Геометрическая Оптика')
# Bg Rect
bg_color = (8, 6, 110)
bgrect = Rect((-1, -1), (w + 1, he + 1))
# constss
color = (179, 179, 179)
color2 = (8,44,163)
hw = floor(w / 2)
hh = floor(he / 2)
x, y = hw + 1, hh
# that lines
clr_0=(0,0,0)
clr_l = (204, 255, 0)
clr_2 = (255, 138, 55)
clr_3 = (255, 0, 0)
center_pos = (hw, hh)
#yacheyka
l=30
clmn=floor(hw/l)+3
rw=floor(he/l)+3
# phisics
focus = l*3  # px
d = hw - x
f = floor(1 / (1 / focus - 1 / d))
i_x = hw + f
h = hh - y
H = floor((abs(f) / d) * h)
i_y = hh + H


def draw_all():
    draw.rect(screen, bg_color, bgrect)
    for c in range(0,clmn):
    	draw.line(screen,color2,(c*l+hw,0),(c*l+hw,he))
    	draw.line(screen,color2,(c*l+(hw-l*clmn),0),(c*l+(hw-l*clmn),he))
    for r in range(0,rw):
    	draw.line(screen,color2,(0,r*l+hh),(w,r*l+hh))
    	draw.line(screen,color2,(0,r*l+(hh-l*rw)),(w,r*l+(hh-l*rw)))
    draw.line(screen, color, (hw, 0), (hw, he))
    draw.line(screen, color, (0, hh), (w, hh))
    for x in range(1, floor(w / focus / 2+1)):
        draw.circle(screen, clr_3, (hw - x * focus, hh), 3)
        draw.circle(screen, clr_3, (hw + x * focus, hh), 3)


def set():
    global x, y, d, f, i_x, h, H, i_y
    x, y = mouse.get_pos()
    d = hw - x
    try:
        f = floor(1 / (1 / focus - 1 / d))
        H = floor((f / d) * h)
    except:
        f = w
        H = 0
    i_x = hw + f
    h = hh - y
    i_y = hh + H







while True:
    draw_all()
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
            	focus -= 10
            if ev.key == K_a:
            	focus += 10
    set()
    # Lines
    draw.line(screen, clr_0,(x,y),(i_x, i_y) ,3)

    draw.line(screen, clr_0,(x,y),(hw,y) ,3)
    draw.line(screen, clr_0,(hw,y),(i_x, i_y) ,3)

    draw.line(screen, clr_0,(i_x, i_y),(hw,i_y) ,3)
    draw.line(screen, clr_0,(hw,i_y),(x, y) ,3)

    draw.line(screen, clr_l, (x, y), (x, hh),4)
    draw.line(screen, clr_2, (i_x, i_y), (i_x, hh),4)
    
    # Circles
    # draw.circle(screen, clr_l ,(x,y),5)
    # draw.circle(screen, clr_2 ,(i_x,i_y),5)

    display.flip()
