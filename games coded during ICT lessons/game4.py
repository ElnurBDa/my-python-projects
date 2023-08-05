import pygame as py
import random 
py.init()


edge=40
cols,rows=5,5
h,w=cols*edge,rows*edge
fpsClock=py.time.Clock()
FPS=15
amount_of_mines=int(.18*cols*rows)

screen = py.display.set_mode((w,h))


clr1=(random.randint(150,250), random.randint(150,250), random.randint(150,250))
clr2=(random.randint(100,250), random.randint(100,250), random.randint(100,250))
clr3=(random.randint(50,100), random.randint(50,100), random.randint(50,100))

mines_pos=[]

def grid():
    global screen, clr1
    for x in range(rows):
        py.draw.line(screen,clr1,(x*edge,0),(x*edge,h))
    for x in range(cols):
        py.draw.line(screen,clr1,(0,x*edge),(w,x*edge))


for x in range(amount_of_mines):
    mines_pos.append((random.randint(0,cols),random.randint(0,rows)))

font = py.font.Font('freesansbold.ttf', 20)
ts=[]
for i in range(0,9):
    if i==0:
        t=font.render("", True, clr2)
    else:t=font.render(str(i), True, clr2)
    ts.append(t)

numb_pos=[]

for x in range(cols):
    for y in range(rows):
        c=0
        if (x+1,y-1) in mines_pos:
            c+=1
        if (x+1,y) in mines_pos:
            c+=1
        if (x+1,y+1) in mines_pos:
            c+=1
        if (x-1,y-1) in mines_pos:
            c+=1
        if (x-1,y) in mines_pos:
            c+=1
        if (x-1,y+1) in mines_pos:
            c+=1
        if (x,y-1) in mines_pos:
            c+=1
        if (x,y+1) in mines_pos:
            c+=1
        numb_pos.append((x,y,c))


covered=[]
for x in range(cols):
    for y in range(rows):
        covered.append((x,y))

while True:
    fpsClock.tick(FPS)

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()
        elif event.type == py.MOUSEBUTTONDOWN:
            ms_ps=py.mouse.get_pos()
            prpr_ms_ps=int(ms_ps[0]/edge),int(ms_ps[1]/edge)
            print(prpr_ms_ps)
            try:
                covered.remove(prpr_ms_ps)
                if prpr_ms_ps in mines_pos:
                    print("CHMO!!!")
                run=False
            except:
                pass
    

    screen.fill((0,0,0))

    for x in numb_pos:
        screen.blit(ts[x[2]], (x[0]*edge+edge/3,x[1]*edge+edge/3))

    for x in mines_pos:
        py.draw.rect(screen, clr2, py.Rect(x[0]*edge,x[1]*edge,edge,edge))

    for x in covered:
        py.draw.rect(screen, clr3, py.Rect(x[0]*edge,x[1]*edge,edge,edge))


    grid()

    py.display.flip()

