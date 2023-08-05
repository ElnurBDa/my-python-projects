from pygame import *
import random

init()
rad = random.randint
w = 800
h = 600
screen = display.set_mode([w, h])
bg_color = (25, 255, 255)
bg_rect_color = (20, 250, 255)
bg_rect = Rect((0, 0), (w, h), fill=bg_rect_color)
clock = time.Clock()
score = 0
p = (-5, -5)
enimies = []
n = 1
livin = False
# Man standart
man_color = (166, 0, 255)
man_pos = int(w / 2), int(h / 2)
man_radius = 20
man_speed = 40
man_health = 5


def win_quit():
    evs = event.get()
    for ev in evs:
        if ev.type == QUIT:
            display.quit()
            break
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                display.quit()
                break


class Body:
    life = True

    def __init__(self, x, y, color, r, speed, health):
        self.x = x
        self.y = y
        self.r = r
        self.speed = speed
        self.color = color
        self.health = health

    def draw(self):
        if self.life:
            color = self.color
            x = self.x
            y = self.y
            r = self.r
            draw.circle(screen, color, (x, y), r)
            self.rect = Rect(x - r, y - r, 2 * r, 2 * r)


class Man(Body):
    def move(self):
        x = self.x
        y = self.y
        r = self.r
        speed = self.speed
        evs = event.get()
        for ev in evs:
            if ev.type == QUIT:
                display.quit()
                breaker = 0 / 0
                break
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    display.quit()
                    breaker = 0 / 0
                if ev.key == K_LEFT:
                    x -= speed
                    if x <= r:
                        x = r
                    self.x = x
                if ev.key == K_RIGHT:
                    x += speed
                    if x >= w - r:
                        x = w - r
                    self.x = x
                if ev.key == K_UP:
                    y -= speed
                    if y <= r:
                        y = r
                    self.y = y
                if ev.key == K_DOWN:
                    y += speed
                    if y >= h - r:
                        y = h - r
                    self.y = y

    def gameover(self, enemy):
        if self.rect.colliderect(enemy.rect):
            enemy.die()
            self.health -= 1
            draw.circle(screen, (255, 0, 0), (self.x, self.y), self.r + 10, 3)
            if self.health == 0:
                quit()

    def boom(self):
        m = mouse.get_pos()
        pressed = mouse.get_pressed()
        if pressed[0]:
            draw.line(screen, (255, 0, 234), (self.x, self.y), m, 5)
            return m
        return (-5, -5)


class Enemy(Body):

    def move(self):
        if self.life:
            r = self.r
            x = self.x
            y = self.y
            x += rad(-self.speed, self.speed)
            y += rad(-self.speed, self.speed)
            if x <= r:
                x = r
            if x >= w - r:
                x = w - r
            if y <= r:
                y = r
            if y >= h - r:
                y = h - r
            self.x = x
            self.y = y

    def die(self):
        global score
        self.life = False
        score += 1

    def be_destroyed(self, pos):
        if self.rect.collidepoint(pos[0], pos[1]):
            self.die()
            return False
        return True


man1 = Man(man_pos[0], man_pos[1], man_color, man_radius, man_speed, man_health)
try:
    while True:
        draw.rect(screen, bg_color, bg_rect)
        win_quit()
        clock.tick(60)
        # Enemy
        if len(enimies) <= 0:
            for x in range(0, round(n)):
                enemy_color = (rad(1, 255), rad(1, 255), rad(1, 255))
                enemy_radius = rad(19, 50)
                enemy_pos = rad(enemy_radius, w - enemy_radius), rad(enemy_radius, h - enemy_radius)
                enemy_speed = rad(1, 40)
                enemy_health = rad(1, 3)
                new_enemy = Enemy(enemy_pos[0], enemy_pos[1], enemy_color, enemy_radius, enemy_speed, enemy_health)
                enimies.append(new_enemy)
            n += 0.1

        for en in enimies:
            en.draw()
            en.move()
            en.be_destroyed(p)
            # man
            man1.move()
            man1.draw()
            man1.gameover(en)
            if en.life == False:
                enimies.remove(en)
            p = man1.boom()
        print(score)
        display.flip()
except:
    init()
    font.init()
    screen = display.set_mode([w, h])
    bg_color = (255, 25, 25)
    bg_rect_color = (20, 250, 255)
    bg_rect = Rect((0, 0), (w, h), fill=bg_rect_color)
    myfont = font.SysFont('Comic Sans MS', 60)
    textsurface = myfont.render('Your Score: ' + str(score), False, (0, 0, 0))
    while True:
        draw.rect(screen, bg_color, bg_rect)

        screen.blit(textsurface, (0, 0))
        win_quit()
        display.flip()
