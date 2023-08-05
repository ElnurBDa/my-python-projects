from pygame import *
from math import ceil ,floor



#main things
init()
w = 900
h = 600
size = w, h
screen = display.set_mode(size)
display.set_caption('Game3')

#This rect
bgrect=Rect((0,0),(w,h))
bgrectcolor=(255,255,255)
#Colors
black = (0, 0, 0)


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
def ukazatel():
    draw.line(screen, black, (0, 1), (w, 1), 3)
    draw.line(screen, black, (1, 0), (1, h), 3)
    c = 50
    myfont = font.SysFont('Arial', 15)
    for a in range(0, ceil(w / c * 2)):
        draw.line(screen, black, (a * c, 0), (a * c, 10))
        draw.line(screen, black, (a * 2 * c, 0), (a * 2 * c, 15), 2)
        textsurface = myfont.render(str(a * c), False, (0, 0, 0))
        screen.blit(textsurface, (a * c - 5, 10))
    for a in range(0, ceil(h / c * 2)):
        draw.line(screen, black, (0, a * c), (10, a * c))
        draw.line(screen, black, (0, a * 2 * c), (15, a * 2 * c), 2)
        textsurface = myfont.render(str(a * c), False, (0, 0, 0))
        screen.blit(textsurface, (10, a * c - 5))
while True:
    draw.rect(screen,bgrectcolor,bgrect)
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