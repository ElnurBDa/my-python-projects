import pygame as py
import random 
py.init()
r=random.randint

developer_mode=False

edge=50
cols,rows=10,10
h,w=cols*edge,rows*edge
fpsClock=py.time.Clock()
FPS=7
screen = py.display.set_mode((w,h))


clr1=(100,255,100)
clr2=(255,100,100)
clr3=(255,200,55)
clr4=(55,125,255)

def grid():
    for x in range(rows):
        py.draw.line(screen,clr1,(x*edge,0),(x*edge,h))
    for x in range(cols):
        py.draw.line(screen,clr1,(0,x*edge),(w,x*edge))



motion="NONE"
bricks=[[0, 0], [0, 1], [1, 1], [1, 2], [2, 2], [2, 3], [0, 3], [1, 3], [0, 2], [3, 3], [3, 2], [3, 0], [2, 0], [1, 0], [2, 1], [3, 1], [4, 0], [4, 1], [4, 2], [4, 3], [5, 3], [5, 2], [5, 0], [5, 1], [6, 0], [6, 1], [6, 2], [7, 3], [7, 1], [7, 0], [8, 0], [9, 0], [9, 1], [8, 1], [7, 2], [8, 2], [8, 3], [9, 2], [6, 3], [9, 3], [9, 5], [9, 6], [9, 8], [9, 9], [9, 7], [9, 4], [8, 5], [8, 4], [8, 6], [8, 7], [8, 8], [8, 9], [7, 4], [7, 6], [7, 7], [7, 8], [7, 9], [7, 5], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [3, 8], [3, 7], [3, 5], [3, 4], [3, 6], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]]
pos=[r(0,cols-1),r(0,rows-1)]
while pos in bricks:pos=[r(0,cols-1),r(0,rows-1)]
c,d=1,.2
ms_ps=(-3423,-3123123)
fires=[]#[pos0x,pos0y]


game_over=False
while True:
    fpsClock.tick(FPS)
    screen.fill((0,0,0)) 

    if not developer_mode:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit()
                elif event.key == py.K_UP:
                    c,d=1,.2
                    motion="UP"
                elif event.key == py.K_DOWN:
                    c,d=1,.8
                    motion="DOWN"
                elif event.key == py.K_LEFT:
                    c,d=.2,1
                    motion="LEFT"
                elif event.key == py.K_RIGHT:
                    c,d=.8,1
                    motion="RIGHT"
                elif event.key == py.K_RCTRL and pos not in fires:
                    if (c,d)==(1,.2):m="UP"
                    if (c,d)==(1,.8):m="DOWN"
                    if (c,d)==(.2,1):m="LEFT"
                    if (c,d)==(.8,1):m="RIGHT"

                    fires.append([[pos[0],pos[1]],m])
            else:motion="NONE"
        #Движение танка
        if motion=="UP" and pos[1]>0 and [pos[0],pos[1]-1] not in bricks:
            pos[1]-=1
        if motion=="DOWN" and pos[1]<rows-1 and [pos[0],pos[1]+1] not in bricks:
            pos[1]+=1
        if motion=="LEFT" and pos[0]>0 and [pos[0]-1,pos[1]] not in bricks:
            pos[0]-=1
        if motion=="RIGHT" and pos[0]<cols-1 and [pos[0]+1,pos[1]] not in bricks:
            pos[0]+=1

        py.draw.rect(screen, clr1, py.Rect(pos[0]*edge,pos[1]*edge,edge,edge))
        py.draw.rect(screen, clr2, py.Rect(pos[0]*edge,pos[1]*edge,edge*c,edge*d))

        for i in range(len(fires)):
            if fires[i][1]=="UP":
                fires[i][0][1]-=1
            if fires[i][1]=="DOWN":
                fires[i][0][1]+=1
            if fires[i][1]=="LEFT":
                fires[i][0][0]-=1
            if fires[i][1]=="RIGHT":
                fires[i][0][0]+=1
            py.draw.rect(screen, clr4, py.Rect(fires[i][0][0]*edge+edge/4,fires[i][0][1]*edge+edge/4,edge/2,edge/2))

            p=[fires[i][0][0],fires[i][0][1]]
            if p in bricks:
                fires[i]=[[-5,-5],"NONE"]
                bricks.remove(p)



    else:#DEVELOPERSKAYA CHASTЬ
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit()
                elif event.key == py.K_SPACE:print(bricks)
                elif event.key == py.K_c:bricks=[]
                elif event.key == py.K_BACKSPACE:bricks.pop()
            elif event.type == py.MOUSEBUTTONDOWN:
                ms_ps=py.mouse.get_pos()
                if [int(ms_ps[0]/edge),int(ms_ps[1]/edge)] not in bricks:
                    bricks.append([int(ms_ps[0]/edge),int(ms_ps[1]/edge)])

    
    for brick in bricks:
        py.draw.rect(screen, clr3, py.Rect(brick[0]*edge,brick[1]*edge,edge,edge))


    grid()
    py.display.flip()

