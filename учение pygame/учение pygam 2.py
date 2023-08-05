import pygame
from time import time
from pygame.rect import *
from pygame.locals import *

pygame.init()
# data
RED = (255, 0, 0)
BLUE= (0,0,255)
w, h = 600, 600
main_color = [75, 75, 75]
running = True
# Text edit
text = 'this text is editable'
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, RED)
rect = img.get_rect()
rect.topleft = (20, 20)
cursor = Rect(rect.topright, (3, rect.height))


win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Elnur's game!")

while running:
    # Keys work
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_BACKSPACE:
                if len(text) > 0:
                    text = text[:-1]
            elif event.key== K_LCTRL:
                text=' '
            else:
                text += event.unicode
            img = font.render(text, True, RED)
            rect.size = img.get_size()
            cursor.topleft = rect.topright


    win.fill(main_color)

    win.blit(img, rect)
    if time() % 1 > 0.5:
        pygame.draw.rect(win, RED, cursor)

    pygame.display.update()

pygame.quit()
