from pico2d import *

import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update_character():
    global x, y
    global hand_x, hand_y

    t = 0.01
    x = (1-t)*x + t*hand_x
    y = (1-t)*y + t*hand_y

    dist = (hand_x-x)**2 + (hand_y-y)**2
    if dist < 10**2:
        hand_x, hand_y = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hand_x, hand_y = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)
hide_cursor()


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand.draw(hand_x, hand_y)
    update_canvas()
    frame = (frame + 1) % 8

    # 캐릭터 좌표 계산
    update_character()


    handle_events()

close_canvas()
