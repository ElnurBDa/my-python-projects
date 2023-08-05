import pygame
from pygame.locals import *
from pygame.rect import *

pygame.init()

# Data
main_color = [10, 70, 160]
running = True
width = 600
height = 600
'''# Text
text='Elnur is great man!You should respect him!'
'''
'''# The image
img = pygame.image.load('mesi.png')
img0=img
rect = img.get_rect()
rect.center = width // 2, height // 2
moving = False
angle = 0
scale = 1'''
'''#Self moving rect
rect = Rect(300, 300, 50, 50)
v = [2, -2]'''
'''#Move a rectangle with the mouse
rect = Rect(50, 60, 200, 80)
moving = False'''
'''# Clip a rectangle
r0 = Rect(50, 60, 200, 80)
r1 = Rect(100, 20, 100, 140)
dirr = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}
dird = {K_a: (-5, 0), K_d: (5, 0), K_w: (0, -5), K_s: (0, 5)}'''
'''#REct inflating
rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()
dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}'''
'''Rect moving
rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()
dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}'''
'''Rect pos
rect=Rect(20,50,60,90)
'''
'''# Ball
played = pygame.image.load('ball.png')
rect = played.get_rect()
speed = [1, 1]'''
'''# drawing rect
start = (0, 0)
size = (0, 0)
drawing = False
list_of_rects=[]'''
'''# Drawing lines
drawing = False
points = []'''

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Elnur's game!")

while running:
    # Keys work
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if main_color[0] + 10 >= 240:
                    main_color[0] = 1
                if main_color[1] + 20 >= 230:
                    main_color[1] = 1
                if main_color[2] + 30 >= 220:
                    main_color[2] = 1
                main_color[0] += 10
                main_color[1] += 20
                main_color[2] += 30
            elif event.key == pygame.K_ESCAPE:
                running = False
        '''# The image
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
        if event.type == KEYDOWN:
            if event.key == K_r:
                if event.mod & KMOD_SHIFT:
                    angle -= 10
                else:
                    angle += 10
                img = pygame.transform.rotozoom(img, angle, scale)
            elif event.key == K_s:
                if event.mod & KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1
                img = pygame.transform.rotozoom(img, angle, scale)
            elif event.key == K_o:
                img = img0
                angle = 0
                scale = 1
            elif event.key == K_h:
                img = pygame.transform.flip(img, True, False)
            elif event.key == K_v:
                img = pygame.transform.flip(img, False, True)
            elif event.key == K_l:
                img = pygame.transform.laplacian(img)
            elif event.key == K_2:
                img = pygame.transform.scale2x(img)
            rect = img.get_rect()
            rect.center = width // 2, height // 2'''
        '''# Drawing lines
        if event.key == K_d:
            if len(points) > 0:
                points.pop()
    elif event.type == MOUSEBUTTONDOWN:
        points.append(event.pos)
        drawing = True
    elif event.type == MOUSEBUTTONUP:
        drawing = False
    elif event.type == MOUSEMOTION and drawing:
        points[-1] = event.pos'''
        '''# Move a rectangle with the mouse
    elif event.type == MOUSEBUTTONDOWN:
        if rect.collidepoint(event.pos):
            moving = True
    elif event.type == MOUSEBUTTONUP:
        moving = False
    elif event.type == MOUSEMOTION and moving:
        rect.move_ip(event.rel)'''
        '''# Clip a rectangle
    if event.type == KEYDOWN:
        if event.key in dirr:
            r1.move_ip(dirr[event.key])
        if event.key in dird:
            r0.move_ip(dird[event.key])'''
        '''#REct inflating
    if event.type == KEYDOWN:
        if event.key in dir:
            v = dir[event.key]
            rect.inflate_ip(v)'''
        '''#Rect moving
    if event.type == KEYDOWN:
        if event.key in dir:
            v = dir[event.key]
            rect.move_ip(v)'''
        '''Rect pos
    if event.type == KEYDOWN:
        if event.key == K_l:
            rect.left = 0
        if event.key == K_c:
            rect.centerx = width // 2
        if event.key == K_r:
            rect.right = width
        if event.key == K_t:
            rect.top = 0
        if event.key == K_m:
            rect.centery = height // 2
        if event.key == K_b:
            rect.bottom = height'''
        '''Drawing rects
    elif event.type == MOUSEBUTTONDOWN:
        start = event.pos
        size = 0, 0
        drawing = True
    elif event.type == MOUSEBUTTONUP:
        end = event.pos
        size = end[0] - start[0], end[1] - start[1]
        drawing = False
        color=(main_color[0] / 2, main_color[1] / 2, main_color[2] / 2)
        list_of_rects.append((start,size,color))
    elif event.type == MOUSEMOTION and drawing:
        end = event.pos
        size = end[0] - start[0], end[1] - start[1]'''
    win.fill(main_color)
    '''# Text
    font = pygame.font.SysFont(None, 40)
    img=font.render(text, True,(main_color[0] / 2, main_color[1] / 2, main_color[2] / 2))
    rect = img.get_rect()
    pygame.draw.rect(img, (main_color[0]*2 / 3, main_color[1]*2 / 3, main_color[2]*2 / 3), rect, 2)
    win.blit(img, (0, 200))'''
    '''#The image
    win.blit(img, rect)
    pygame.draw.rect(win, (0, 0, 255), rect, 1)'''
    ''' # Self moving rect
rect.move_ip(v)
if rect.left < 0:
    v[0] *= -1
if rect.right > width:
    v[0] *= -1
if rect.top < 0:
    v[1] *= -1
if rect.bottom > height:
    v[1] *= -1
pygame.draw.rect(win, (0,120,230), rect)'''
    '''# Move a rectangle with the mouse
pygame.draw.rect(win, (255,0,0), rect)
if moving:
    pygame.draw.rect(win, (0,255,0), rect, 4)
else:
    pygame.draw.rect(win, (0, 0, 255), rect, 4)'''
    '''# Clip a rectangle
clip = r0.clip(r1)
union = r0.union(r1)
pygame.draw.rect(win, (191, 225, 0), union, 0)
pygame.draw.rect(win, (0, 225, 26), clip, 0)
pygame.draw.rect(win, (73, 31, 225), r0, 4)
pygame.draw.rect(win, (225, 0, 0), r1, 4)'''
    '''#REct inflating
pygame.draw.rect(win, (200,20,200), rect0, 4)
pygame.draw.rect(win, (20,20,200), rect, 4)'''
    '''#Rect moving
pygame.draw.rect(win, (0,250,250), rect0, 5)
pygame.draw.rect(win, (250,0,250), rect, 5)'''
    '''REct pos
pygame.draw.rect(win,(123,23,231),rect)
'''
    '''#Drawing lines
if len(points) > 1:
    rect = pygame.draw.lines(win, (0,50,250), True, points, 3)
    pygame.draw.rect(win, (0,250,0), rect, 1)'''
    '''Drawing rects
for x in list_of_rects:
    pygame.draw.rect(win,x[2] , (x[0],x[1]),5)'''
    '''BALL
rect = rect.move(speed)
if rect.left < 0 or rect.right > width:
 speed[0] = -speed[0]
if rect.top < 0 or rect.bottom > height:
 speed[1] = -speed[1]
pygame.draw.rect(win, main_color, rect, 1)
win.blit(played, rect)'''
    pygame.display.update()

pygame.quit()
