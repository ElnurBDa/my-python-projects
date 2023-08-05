import pygame as py
import random 
from time import time
py.init()
rr=random.randint

fpsClock=py.time.Clock()
FPS=30
h,w=900,1600
screen = py.display.set_mode((w,h))

centerpos=(w//2,h//2)
cr=25
clr1=(255,23,123)
a=[]
clr2=(23,255,123)

enemies=[((rr(50,w-50),rr(50,h-50)),rr(10,20),(rr(100,255),rr(100,255),rr(100,255))) for x in range(10)]
c=0
while True:
    fpsClock.tick(FPS)

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()
        elif py.mouse.get_pressed()[0]:
            b=py.mouse.get_pos()
            a.append([[centerpos[0],centerpos[1]],b])

    screen.fill((0,0,0)) 
    for x in a:
        py.draw.circle(screen, clr2, list(map(int,x[0])), 5)
        x[0][0]+=(x[1][0]-centerpos[0])/50
        x[0][1]+=(x[1][1]-centerpos[1])/50
        for y in enemies:
            if y[0][0]-y[1]<=x[0][0]<=y[0][0]+y[1] and y[0][1]-y[1]<=x[0][1]<=y[0][1]+y[1]:
                enemies.remove(y)

        if x[0][0]>=w or x[0][0]<=0 or x[0][1]>=h or x[0][1]<=0:
            a.remove(x)

    

    py.draw.circle(screen, clr1, centerpos, cr)
    
    for x in enemies:
        py.draw.circle(screen, x[2], x[0], x[1])

    if len(enemies)<=20+c*50:
        c+=1
        for x in range(10+c*1000):
            enemies.append(((rr(50,w-50),rr(50,h-50)),rr(10,20),(rr(100,255),rr(100,255),rr(100,255))))

  

    py.display.flip()

