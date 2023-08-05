import pygame as py
import random 
py.init()
r=random.randint



edge=50
cols,rows=15,15
h,w=cols*edge,rows*edge
fpsClock=py.time.Clock()
FPS=7
screen = py.display.set_mode((w,h))


clr1=(100,255,100)
clr2=(255,100,100)
def grid():
    for x in range(rows):
        py.draw.line(screen,clr1,(x*edge,0),(x*edge,h))
    for x in range(cols):
        py.draw.line(screen,clr1,(0,x*edge),(w,x*edge))



motion="NONE"
snake_ps=[(r(0,cols-1),r(0,rows-1))]
apple=[r(0,cols-1),r(0,rows-1)]
while apple in snake_ps:
    apple=[r(0,cols-1),r(0,rows-1)]
 


game_over=False
while True:
    fpsClock.tick(FPS)

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()
            if event.key == py.K_UP and motion!="DOWN":
                motion="UP"
            if event.key == py.K_DOWN and motion!="UP":
                motion="DOWN"
            if event.key == py.K_LEFT and motion!="RIGHT":
                motion="LEFT"
            if event.key == py.K_RIGHT and motion!="LEFT":
                motion="RIGHT"
            if event.key == py.K_SPACE:
                motion="NONE"
                snake_ps=[(r(0,cols-1),r(0,rows-1))]
                apple=[r(0,cols-1),r(0,rows-1)]
                game_over=False

    screen.fill((0,0,0)) 
    first=snake_ps[-1]
    if motion=="UP":
        first=[first[0],first[1]-1]
    if motion=="DOWN":
        first=[first[0],first[1]+1]
    if motion=="LEFT":
        first=[first[0]-1,first[1]]
    if motion=="RIGHT":
        first=[first[0]+1,first[1]]
    if first[0]<0 or first[0]>=cols or first[1]<0 or first[1]>=rows:
        game_over=True

    snake_ps+=[first]
    if first==apple:
        while apple in snake_ps:
            apple=[r(0,cols-1),r(0,rows-1)]
    else:snake_ps.pop(0)
    if first in snake_ps[0:-1]:
        game_over=True



    a,b=apple[0],apple[1]
    py.draw.rect(screen, clr2, py.Rect(a*edge,b*edge,edge,edge))

    for p in snake_ps:
        a,b=p[0],p[1]
        py.draw.rect(screen, clr1, py.Rect(a*edge,b*edge,edge,edge))


    if game_over:
        screen.fill(clr2)
        motion="NONE"

    grid()

    py.display.flip()

