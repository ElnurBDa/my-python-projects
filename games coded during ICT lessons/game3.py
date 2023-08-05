import pygame as py
import random 
py.init()
h,w=450,800
fpsClock=py.time.Clock()
FPS=15

screen = py.display.set_mode((w,h))


motion="NONE"
color1=(255, 255, 255)
clr=(255, 0, 0)

r=25
a,b=r,r
l=[]

while True:
    fpsClock.tick(FPS)

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()
            if event.key == py.K_UP:
                motion="UP"
            if event.key == py.K_DOWN:
                motion="DOWN"
            if event.key == py.K_LEFT:
                motion="LEFT"
            if event.key == py.K_RIGHT:
                motion="RIGHT"
            if event.key == py.K_s:
                l.append((a,b,clr))
                a,b=r,r
            if event.key == py.K_c:
                clr=(123,213,23)
            if event.key == py.K_x:
                clr=(255, 0, 0)

        else:
            motion="NONE"



            
    if motion=="UP":
        b-=r
    if motion=="DOWN":
        b+=r
    if motion=="LEFT":
        a-=r
    if motion=="RIGHT":
        a+=r

    screen.fill(color1)
    for x in l:
        py.draw.rect(screen, x[2], py.Rect(x[0],x[1],r,r))
    
    py.draw.rect(screen, clr, py.Rect(a,b,r,r))
        
    
   



    py.display.flip()

