from pico2d import *
import random

# Game object class here


# 생성자 self는 다음에설명
# 클래스안에 객체의 상태를 나타내는 변수에 연결하거나
# 그 객체의 함수를 호출할 때는 self를 붙여줘야함
class Grass:
    def __init__(self):  # 생성자
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(0, 700), 90
        self.frame = 0

    def update(self):  # 소년의 행위 구현
        self.x += 5  # 속성값을 바꿈으로써, 행위(오른쪽으로 이동)을 구현.
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


# grass = Grass() # Grass 라는 클래스로부터, grass 객체를 생성한다.


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code 초기화
open_canvas()

grass = Grass()  # 잔디 객체를 생성
# boy = Boy()  # 소년 객체를 생성

# team
team = [Boy() for i in range(11)]

running = True

# game main loop code  로직/드로잉/끝?
while running:

    handle_events()  # 키 입력을 받아들이는 처리..

    # Game logic
    # grass 에 대한 상호작용. 은 움직이지 않으므로 무시
    for boy in team:
        boy.update()  # 소년의 상호작용

    # Game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)

# finalization code
# 갈비지 컬렉션 자동화/ 객체 지우는거 등등 / 나중에 복잡할땐 직접해줄 필요 있음
