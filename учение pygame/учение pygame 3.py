import pygame
from pygame.locals import *


class Text:

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        pygame.init()
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        App.screen.blit(self.img, self.rect)


class Scene:
    id = 0
    bg = Color('gray')

    def __init__(self, *args, **kwargs):
        App.scenes.append(self)
        App.scene = self
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg

    def draw(self):
        App.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()

    def __str__(self):
        return 'Scene {}'.format(self.id)


class App:
    scenes = []

    def __init__(self):
        # 1
        self.rect = Rect(0, 0, 600, 500)
        pygame.init()
        self.flags = RESIZABLE
        App.screen = pygame.display.set_mode(self.rect.size, self.flags)
        pygame.display.set_caption("Elnur's game!")
        App.running = True

        # 2
        self.txt = Text('HEyy!', (10, 10))
        self.shortcuts = {
            (K_f, KMOD_LALT): 'self.toggle_fullscreen()',
            (K_r, KMOD_LALT): 'self.toggle_resizable()',
            (K_g, KMOD_LALT): 'self.toggle_frame()',

        }

    def do_shortcut(self, event):
        k = event.key
        m = event.mod
        if (k, m) in self.shortcuts:
            exec(self.shortcuts[k, m])

    def toggle_fullscreen(self):
        self.flags ^= FULLSCREEN
        pygame.display.set_mode((0, 0), self.flags)

    def toggle_resizable(self):
        self.flags ^= RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)

    def toggle_frame(self):
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                if event.type == KEYDOWN:
                    self.do_shortcut(event)

            App.screen.fill(Color('gray'))
            self.txt.draw()
            pygame.display.update()
        pygame.quit()


class Demo(App):

    def __init__(self):
        super().__init__()

        Scene(caption='Intro')
        Text('Scene 0',(10,10))
        Text('Introduction screen the app',(30,30))

        Scene(bg=Color('yellow'), caption='Options')
        Text('Scene 1',(10,10))
        Text('Option screen of the app',(30,30))

        Scene(bg=Color('green'), caption='Main')
        Text('Scene 2',(10,10))
        Text('Main screen of the app',(30,30))

        App.scene = App.scenes[0]


if __name__ == '__main__':
    Demo().run()
