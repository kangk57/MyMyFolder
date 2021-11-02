from pico2d import *


class World:
    def __init__(self):
        self.image = load_image('world1.png')

    def draw(self):
        self.image.draw(1696, 112)


class Mario:
    def __init__(self):
        self.image = load_image('mario_sheet.png')
        self.x, self.y = 50, 32
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += dir*5
        self.y += height*5

    def draw(self):
        self.image.clip_draw(210, 172, 14, 16, self.x, self.y)
        if dir > 0:
            self.image.clip_draw(210 + self.frame * 30, 172, 14, 16, self.x, self.y)
        if dir < 0:
            self.image.clip_draw(150 - self.frame * 30, 172, 14, 16, self.x, self.y)


def handle_events():
    global running
    global dir
    global height
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d:
                dir += 1
            elif event.key == SDLK_a:
                dir -= 1
            elif event.key == SDLK_w:
                height += 1
            elif event.key == SDLK_s:
                height -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                dir -= 1
            elif event.key == SDLK_a:
                dir += 1
            elif event.key == SDLK_w:
                height -= 1
            elif event.key == SDLK_s:
                height += 1


open_canvas(800, 224)

world = World()
mario = Mario()

running = True
dir = 0
height = 0

while running:
    handle_events()
    mario.update()

    clear_canvas()
    world.draw()
    mario.draw()
    update_canvas()

    delay(0.05)
