from pygame import *
import asyncio
from math import floor
import time as t
from random import randint

# main
init()
w = 900
h = 600
size = w, h
screen = display.set_mode(size)
display.set_caption('Game3')

# game
main_color = 255,26,0
bg_color = (225, 225, 225)
bg_rect = Rect((-50, -50), (w + 100, h + 100), fill=bg_color)
font_size = 30
myfont = font.SysFont('Comic Sans MS', font_size)
speed = 1
score = 0
a = 150
red, green, blue = 0, 0, 0
clr_ch = 55


class Ball:
    def __init__(self, start_x, start_y, color, diametr):

        self.x = start_x
        self.y = start_y
        self.clr = color
        self.d = diametr
        self.r = floor(self.d / 2)
        self.rect = Rect((self.x, self.y), (self.d, self.d))

    def draw(self):
        self.rect = Rect((self.x, self.y), (self.d, self.d))
        draw.circle(screen, self.clr, (self.x + self.r, self.y + self.r), self.r)
        draw.circle(screen, (0, 0, 0), (self.x + self.r, self.y + self.r), self.r, 1)

    track = False

    def set_pos(self):
        if self.track:
            new_x = mouse.get_pos()[0]
            self.x = new_x - self.r

    async def move(self):
        while True:
            evs = event.get()
            for ev in evs:
                if ev.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mouse.get_pos()[0], mouse.get_pos()[1]):
                    self.track = True
                if ev.type == MOUSEBUTTONUP:
                    self.track = False
                self.set_pos()
                if ev.type == QUIT:
                    display.quit()
                if ev.type == KEYDOWN:
                    if ev.key == K_ESCAPE:
                        display.quit()
            await asyncio.sleep(0.001)

    def gameover(self, block_rect):
        if self.rect.colliderect(block_rect):
            from time import sleep
            sleep(1)
            display.quit()


class Block:
    def __init__(self, x, y, color, width, height, hole_width):
        self.x = x
        self.y = y
        self.clr = color
        self.w = width
        self.h = height
        self.hole_w = hole_width
        self.small_w = floor((self.w - self.hole_w) / 2)
        # self.rect = Rect((self.x, self.y), (self.w, self.h))
        self.rect1 = Rect((self.x, self.y), (self.small_w, self.h))
        self.rect2 = Rect((self.x + self.hole_w + self.small_w, self.y), (self.small_w, self.h))

    def draw(self):
        # self.rect = Rect((self.x, self.y), (self.w, self.h))
        self.rect1 = Rect((self.x, self.y), (self.small_w, self.h))
        draw.rect(screen, self.clr, self.rect1)
        draw.rect(screen, (0, 0, 0), self.rect1, 1)
        self.rect2 = Rect((self.x + self.hole_w + self.small_w, self.y), (self.small_w, self.h))
        draw.rect(screen, self.clr, self.rect2)
        draw.rect(screen, (0, 0, 0), self.rect2, 1)

    movement = True

    def up_move(self):
        if self.movement:
            self.y -= speed

    def is_above_window(self):
        if self.y <= -self.h:
            return True
        else:
            return False


# ball
ball = Ball(floor(w / 2), 40, main_color, 30)
# Block
bl_color = 255, 221, 110
bl_h = 30  # block_height
blocks = []
bl_am = floor((w) / bl_h)  # block_amount
print("BLock amount: ", bl_am)
for x in range(0, bl_am):
    new_block = Block(0, x * bl_h, bl_color, w, bl_h, 200)
    blocks.append(new_block)


async def game():
    global score, a, speed, red, green, blue, clr_ch
    while True:
        draw.rect(screen, bg_color, bg_rect)
        ball.draw()
        for block in blocks:
            block.up_move()
            ball.gameover(block.rect1)
            ball.gameover(block.rect2)
            if block.is_above_window():
                score += 1
                r = randint(-a, a)
                r_clr = randint(30, 255 - clr_ch)

                new_block = Block(r - a, bl_am * bl_h - bl_h, (r_clr + red, r_clr + green, r_clr + blue), w - r + a + 1,
                                  bl_h,
                                  randint(a, 400+a))
                blocks.append(new_block)
                blocks.remove(blocks[0])
                print(score)
                if score % 10 == 0:
                    a += 5
                    speed *= 1.05
                if score % 50 == 0:
                    red = randint(0, clr_ch)
                    green = randint(0, clr_ch)
                    blue = randint(0, clr_ch)

            block.draw()

        textsurface = myfont.render('Score: ' + str(round(score)), False, (0, 0, 0))
        screen.blit(textsurface, (w - font_size * 6, h - font_size * 2))

        display.flip()
        await asyncio.sleep(0.001)


loop = asyncio.get_event_loop()

asyncio.ensure_future(game())
asyncio.ensure_future(ball.move())

loop.run_forever()
