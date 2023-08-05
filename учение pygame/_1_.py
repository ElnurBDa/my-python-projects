import pygame, sys
from pygame.locals import *
from math import floor ,ceil
#1
w=1600
h=800
pygame.init()
DISPLAYSURF = pygame.display.set_mode((w, h),0,0)
pygame.display.set_caption('Hello World!')
bg_color=[0,0,0]
#2




while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN and event.key==K_LEFT :
            w-=10
            DISPLAYSURF = pygame.display.set_mode((w, h))
        elif event.type==KEYDOWN and event.key==K_RIGHT:
            w += 10
            DISPLAYSURF = pygame.display.set_mode((w, h))
        elif event.type==KEYDOWN and event.key==K_DOWN:
            h += 10
            DISPLAYSURF = pygame.display.set_mode((w, h))
        elif event.type==KEYDOWN and event.key==K_UP:
            h -= 10
            DISPLAYSURF = pygame.display.set_mode((w, h))
    a = [0, 0, 1, h]
    for x in range(1,w):
        a[0] = x
        r=50
        g=255-r
        b=255/w*x
        pygame.draw.rect(DISPLAYSURF,(r,g,b),Rect(a))


    pygame.display.update()
