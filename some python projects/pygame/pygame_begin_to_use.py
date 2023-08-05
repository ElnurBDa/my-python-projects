import pygame as py


py.init()
h,w=600,600
fpsClock=py.time.Clock()
FPS=30

screen = py.display.set_mode((w,h))


while True:
    fpsClock.tick(FPS)

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()


    screen.fill((0,0,0))

    py.display.flip()

