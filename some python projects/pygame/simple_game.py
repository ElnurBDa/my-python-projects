import pygame as py
import random

py.init()
h,w=400,800
fpsClock=py.time.Clock()
FPS=30

screen = py.display.set_mode((w,h))


class Blocks:
    def __init__(self, vertexes, side, pos, speed = 0, width = 2, color = (255,255,255)):
        self.vertexes = vertexes 
        self.pos = pos
        self.color = color
        self.width = width
        self.side = side
        self.speed = speed

        self.points = []
        for v in self.vertexes:
            self.points.append((v[0]*self.side+self.pos[0],v[1]*self.side+self.pos[1]))

    def draw(self):
        py.draw.polygon(screen, self.color, self.points, self.width)

    def get_pos(self):return self.pos
    def get_points(self):return self.points


    def define_points(self):
        self.points = []
        for v in self.vertexes:
            self.points.append((v[0]*self.side+self.pos[0],v[1]*self.side+self.pos[1]))
    
    def move(self):
        x, y = self.pos
        self.pos = x+self.speed[0], y+self.speed[1]
        self.define_points()

    def set_speed(self,speed): self.speed = speed


game_over = False
class Player(Blocks):

    def game(self):
        for block in blocks:
            points = block.get_points()
            a, b = points[0], points[2]

            for p in self.points:
                if (a[0]>p[0]>b[0])&(a[1]>=p[1]>=b[1]):
                    print(a,b,p)
                    return 1
        return 0








number_of_blocks = 0
blocks = []

player = Player([(0,0),(0,-1),(-1,-1),(-1,0)],50 , (100,h//2),(0,0))
player_v = 0
start_v = 24
dv = -start_v
jump = False

line = Blocks([(0,0),(1,0)],w,(0,h//2))

while True:
    fpsClock.tick(FPS)
    if game_over:
        screen.fill((255,255,255))
    else:
        game_over = player.game()
        screen.fill((0,0,0))

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()
            if event.key == py.K_SPACE:
                jump = True

    if number_of_blocks<3:
        blocks.append(Blocks([(0,0),(0,-1),(-1,-1),(-1,0)],50 , (w+100+number_of_blocks*100*random.randint(1,4),h//2),(-10,0)))
        number_of_blocks+=1

    for block in blocks:
        block.move()
        block.draw()
        if block.get_pos()[0]<=-200:
            blocks.remove(block)
            number_of_blocks-=1

    if jump:
        dv+=1.5
        player_v = dv
        if dv >= start_v:
            dv = -start_v
            jump = False
            player_v = 0

    player.set_speed((0,player_v))
    player.move()
    player.draw()
    line.draw()

    py.display.flip()

