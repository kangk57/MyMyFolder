from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True
x = 0
frame = 0


def handle_events():
    global running  # 바깥에 정의된 것 쓰겠다

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # 윈도우 종료버튼(X)
            running = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:  # 키가 눌렸다는 이벤트고 esc 이면
            running = False


while x < 800 and running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 1
    delay(0.01)

close_canvas()

