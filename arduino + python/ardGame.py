import serial 
serialport = serial.Serial('COM3', baudrate = 9600, timeout = 2)

import pygame as py
import random 
py.init()
h,w=450,800
fpsClock=py.time.Clock()
FPS=60

screen = py.display.set_mode((w,h))


motion="NONE"
color1=(255, 255, 255)
clr=(255, 0, 0)

r=1
a,b= 250, 250

while True: 

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
        else:
            motion="NONE"


    data = serialport.readline().decode('ascii')
    if data:
        ww = eval(data)
        x, y =ww
        
        x//=64
        y//=64

        x-=8
        y-=8

        if -1<=x<=1:x=0
        if -1<=y<=1:y=0

        print(ww, x,y)

    a+=x
    b+=y
    
    if not (0<=a<=w):a=w//2
    if not (0<=b<=h):b=h//2


    if motion=="UP":
        b-=r
    if motion=="DOWN":
        b+=r
    if motion=="LEFT":
        a-=r
    if motion=="RIGHT":
        a+=r



    screen.fill(color1)
    
    py.draw.circle(screen, clr,(a, b), 20)
        
    
   



    py.display.flip()

