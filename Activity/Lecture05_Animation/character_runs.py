from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 0
frame = 0
while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8  # 프레임이 계속 증가하면 이미지 영역을 벗어나기 때문에 다시 0번으로 가기 위해서 %(나머지연산) 사용
    x += 5
    delay(0.05)
    get_events()  # 나중에 설명
    # 다른쪽 태스크로 이동할 수 있는 방법을 제시해 주어야 함 (9.30 강의에 설명해주심)
    # 다른 일을 수행할 수 있도록 길을 잠깐 터주는 내용이 담겨있다 / 멀티태스킹
close_canvas()
