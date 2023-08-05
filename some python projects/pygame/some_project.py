import pygame as py
import random 
r = random.randint


py.init()
h,w=600,600
fpsClock=py.time.Clock()
FPS=30

screen = py.display.set_mode((w,h))

def to_int(a):
    return (int(a[0]), int(a[1]))

num_of_types = 255
entities = []

for x in range(num_of_types):
    entities.append([])


color_p = 255//num_of_types
entity_colors = []
for x in range(num_of_types):
    entity_colors.append(((color_p*x),(color_p*x),(color_p*x)))



margin = 200
ent_radius = 5
amount_of_entities = 300
speed = 50
d=10

def create_entities(ent_type, amount):
    for x in range(amount):
        x = (r(d*(1+margin),d*(w-margin)))/d
        y = (r(d*(1+margin),d*(h-margin)))/d
        vx = (r(1,speed*2)-speed)/10
        vy = (r(1,speed*2)-speed)/10
        entities[ent_type].append([[x,y],[vx,vy]])

def draw_entities():
    for ent_type in range(num_of_types):
        for ent in entities[ent_type]:
            py.draw.circle(screen, entity_colors[ent_type], to_int(ent[0]), int(ent_radius))



def create_each_type_amount(amount):
    for ent_type in range(num_of_types):
        create_entities(ent_type, amount)


def entities_move():
    global ent_radius
    ent_radius*=1.003
    for ent_type in range(num_of_types):
        for ent in range(amount_of_entities):
            entities[ent_type][ent][0][0] += entities[ent_type][ent][1][0]
            entities[ent_type][ent][0][1] += entities[ent_type][ent][1][1]


def change_speed(p):
    if p == 0:a,b = 1,0
    if p == 1:a,b = 0,1
    if p == 2:a,b = -1,0
    if p == 3:a,b = 0,-1

    for ent_type in range(num_of_types):
        for ent in range(amount_of_entities):
            entities[ent_type][ent][1][0]+=a
            entities[ent_type][ent][1][1]+=b



create_each_type_amount(amount_of_entities)
while True:
    fpsClock.tick(FPS)

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()
            if event.key == py.K_RIGHT:
                change_speed(0)
            if event.key == py.K_DOWN:
                change_speed(1)
            if event.key == py.K_LEFT:
                change_speed(2)
            if event.key == py.K_UP:
                change_speed(3)


    screen.fill((0,0,0))
    draw_entities()
    entities_move()

        
    
   



    py.display.flip()

