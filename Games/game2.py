from pygame import *
import time as tim
from random import randint

init()

# Window
developer_mode = False
r_w = 700
r_h = 500

if developer_mode:
    w = r_w * 2
    h = r_h * 2
    a = 2
    dx = int(w / (2 * a))
    dy = int(h / (2 * a))
else:
    w = r_w
    h = r_h
    dx = 0
    dy = 0
    a = 1

fg_color = (200, 200, 200)
bg_color = (255, 255, 255)
screen = display.set_mode([w, h])
fg_rect = Rect((dx, dy), (int(w / a), int(h / a)), fill=fg_color)
bg_rect = Rect((0, 0), (w, h), fill=bg_color)


def ground():
    draw.rect(screen, bg_color, bg_rect)
    draw.rect(screen, fg_color, fg_rect)


# Game
movement = False
run = True
clock = time.Clock()
line_color = (0, 0, 0)
head_line = r_h - 20 + dy
score = 0
speed = 1.1
border_count = 0
g = 200


def land_line():
    draw.line(screen, line_color, (0, head_line), (w, head_line), 5)


def win_quit():
    evs = event.get()
    for ev in evs:
        if ev.type == QUIT:
            display.quit()
            breaker=2/0
            break
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                display.quit()
                breaker=2/0
                break


class Scelet:
    rect = None

    def __init__(self, x_left, y_up, w_, h_, colorr):
        self.x_left = x_left
        self.y_up = y_up
        self.color = colorr
        self.w = w_
        self.h = h_

    def draw(self):
        self.rect = Rect((self.x_left + dx, self.y_up + dy), (self.w, self.h))
        draw.rect(screen, self.color, self.rect)


class Thing(Scelet):
    jumping = False
    jump_pos = 0
    start_jump = 0

    def inner_jump(self):
        y0 = self.jump_pos
        start_jump = self.start_jump
        while self.jumping:
            yield y0 - 300 * (speed ** 3) * (tim.time() - start_jump) + g * (tim.time() - start_jump) ** 2

    def move(self):
        global movement, speed
        evs = event.get()
        for ev in evs:
            movement = True
            if ev.type == QUIT:
                display.quit()
                breaker=2/0
                break
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    display.quit()
                    breaker=2/0
                    break
                if ev.key == K_UP:
                    speed *= 1.00005
                    self.jumping = True
                    self.jump_pos = self.y_up
                    self.start_jump = tim.time()

    def jumpi(self):
        try:
            self.y_up = next(self.inner_jump())
            if self.y_up >= head_line - self.h - 3 - dy:
                self.y_up = head_line - self.h - 5 - dy
                self.jumping = False
            if self.y_up<=-70:
                self.y_up = head_line - self.h - 5 - dy
                self.jumping = False

        except:
            pass

    def is_dead(self, border):
        try:
            if self.rect.colliderect(border.rect):
                tim.sleep(1)
                quit()
                breaker=2/0
        except:
            pass

    def is_on_floor(self):
        if self.y_up == head_line - self.h - 5 - dy:
            return True
        else:
            return False


class Border(Scelet):
    def move(self):
        if movement:
            self.x_left -= 4 * speed

    def is_should_be_destroyed(self):
        if self.x_left <= -200:
            return True


# Main_thing = mt
mt_w = 50
mt_h = 50
mt_left_x = 80
mt_up_y = r_h - mt_h - 25
mt_color = (105, 105, 105)
mt = Thing(mt_left_x, mt_up_y, mt_w, mt_h, mt_color)

# borders
borders = []
font_size = round(r_h / 10)
myfont = font.SysFont('Comic Sans MS', font_size)
while run:
    ground()
    land_line()
    win_quit()
    clock.tick(60)
    # mt
    mt.move()
    mt.jumpi()
    mt.draw()
    # score
    a = mt.is_on_floor()
    if a and movement:
        mt.move()
        score += 0.1 * (speed ** 2)
    if developer_mode:
        mt.move()
        textsurface = myfont.render('Score: ' + str(round(score)), False, (0, 0, 0))
        screen.blit(textsurface, (r_w - font_size * 5, 0))
        textsurface = myfont.render('Speed: ' + str(speed), False, (0, 0, 0))
        screen.blit(textsurface, (r_w - font_size * 5, font_size + 5))
        textsurface = myfont.render('Borders: ' + str(border_count), False, (0, 0, 0))
        screen.blit(textsurface, (r_w - font_size * 5, font_size * 2 + 5))
    else:
        mt.move()
        textsurface = myfont.render('Score: ' + str(round(score)), False, (0, 0, 0))
        screen.blit(textsurface, (r_w - font_size * 5, 0))

    # borders
    if len(borders) < 3:
        mt.move()
        b_w = randint(40, 130)
        b_h = randint(20, 130)
        b_left_x = r_w + randint(300, 1000)
        b_up_y = head_line - b_h - 5 - dy
        c = randint(0, 170)
        b_color = (c, c, c)
        b = Border(b_left_x, b_up_y, b_w, b_h, b_color)
        borders.append(b)

    for b_ in borders:
        mt.move()
        b_.draw()
        b_.move()
        if b_.is_should_be_destroyed():
            mt.move()
            borders.remove(b_)
            border_count += 1
            score+=0.5
        mt.is_dead(b_)
    mt.move()
    display.flip()
