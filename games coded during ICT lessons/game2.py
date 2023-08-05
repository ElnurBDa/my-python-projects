import pygame as py
import random 
py.init()
h,w=450,800

screen = py.display.set_mode((w,h))

a,b=20,50
c,d=w-50,50
q=30
l=h/4

motion1="NONE"
motion2="NONE"
color=(255, 255, 255)
color2=(255, 0, 0)
color3=(0, 0, 255)
color4=(0, 255, 0)

vector=[random.random()/5-0.1,random.random()/5-0,1]
j,k=w/2,h/2
r=20

'''

(a,b)---(a+q,b)
(a,b+l)-(a+q,b+l)

'''



while True:

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()
            if event.key == py.K_UP:
                motion2="UP"
            if event.key == py.K_DOWN:
                motion2="DOWN"
            if event.key == py.K_LEFT:
                motion1="UP"
                print("ELNUR BESDII")
            if event.key == py.K_RIGHT:
                motion1="DOWN"
        else:
            motion1="NONE"
            motion2="NONE"

    j+=vector[0]*5
    k+=vector[1]*0.5
    if j+r+1>=w or j-r-1<=0:
        vector[0]=-vector[0]
    if k+r+1>=h or k-r-1<=0:
        vector[1]=-vector[1]
    if b<=k<=b+l and j-r-1<=a+q:
        vector[0]=-vector[0]
    if d<=k<=d+l and j+r+1>=c:
        vector[0]=-vector[0]
    
    


    
    
    if motion1=="UP" and b>0:
        b-=.3
    if motion1=="DOWN" and b+l<h:
        b+=.3
    if motion2=="UP" and d>0:
        d-=.3
    if motion2=="DOWN" and d+l<h:
        d+=.3
    
    
            
                
        
    
    screen.fill(color)

    py.draw.circle(screen, color4, (int(j),int(k)), r)
    py.draw.rect(screen, color2, py.Rect(a, b, q, l))
    py.draw.rect(screen, color3, py.Rect(c, d, q, l))
    py.display.flip()

